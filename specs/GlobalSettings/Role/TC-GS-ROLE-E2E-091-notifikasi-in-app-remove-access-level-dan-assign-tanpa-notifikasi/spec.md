---
id: TC-GS-ROLE-E2E-091-notifikasi-in-app-remove-access-level-dan-assign-tanpa-notifikasi
title: "Notifikasi In-App Remove Access Level dan Assign Total Control Tanpa Notifikasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-62
  - TC-GS-ROLE-241
  - TC-GS-ROLE-242
coverage:
  web: automated
---

# Notifikasi In-App Remove Access Level dan Assign Total Control Tanpa Notifikasi

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (aktor): Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Layar awal Sesi A (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Akun Sesi B (target, objek asersi): Sari Wulandari (TC-GS-ROLE-62 dan TC-GS-ROLE-241) dan Rahmat Hidayat (TC-GS-ROLE-242), Active, Access Global Settings. Email disediakan tim FE (tidak ada di Tabel Pre-setup TC), kredensial `Spectra.env.GS_ROLE_TARGET_PASSWORD`. Sesi B dibuka di konteks browser kedua dengan login, dan ditutup di akhir tiap TC (konteks ditutup, sesi login terkait dihapus).
- Kelas harness: multi-konteks (kelas c). Hasil di Sesi B adalah objek asersi, bukan pemicu.
- Environment variable: `GS_TC_PASSWORD` dan `GS_ROLE_TARGET_PASSWORD`. Env yang dipakai spec ini: `GS_ROLE_TARGET_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; didaftarkan tim FE). Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang diubah (Given dipasang lewat API di hook `before`; pemulihan di hook `after`, tanpa berasumsi langkah spec berhasil penuh):
  - Sari Wulandari (Pre-setup #11): tanpa access level dan tanpa baris role (precondition TC-GS-ROLE-62). TC-GS-ROLE-62 meng-assign Total Control dan TC-GS-ROLE-241 me-Remove-nya, sehingga kembali ke Pre-setup #11.
  - Rahmat Hidayat (Pre-setup #11, Dynamic #4): di-assign Read Only lewat API (precondition TC-GS-ROLE-242, setara dependensi TC-GS-ROLE-88). Hook `after` memulihkan Rahmat Hidayat tanpa access level dengan baris Manage files Read dan Delete (Pre-setup #11).
  - Efek yang tidak dipulihkan: Last Updated, entri log, dan notifikasi yang diterima Sari Wulandari dan Rahmat Hidayat (bersifat immutable).
- Date Format General Settings aktif dibaca dari Global Settings > General Settings sebelum aksi pertama; nilai konkretnya dipakai pada asersi `[Date]`. Jam server dan jam browser sinkron; `[Date]` dibandingkan dengan tanggal aksi.
- Kemampuan teknis: dua konteks browser paralel; membuka Overlay Notifikasi di Sesi B; membaca jumlah notifikasi lewat Overlay Notifikasi sebagai baseline; seeding dan pemulihan access level dan baris role lewat API.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite), termasuk untuk akun target Sesi B; spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-62: Assign Total Control tidak memicu notifikasi ke target

1. [Sesi B] Buka konteks browser baru, login sebagai Sari Wulandari
2. [Sesi B] Buka Overlay Notifikasi, catat jumlah notifikasi sebagai baseline, tutup overlay
3. [Sesi A] Klik `[+ Assign]`
4. [Sesi A] Ketik Search `Sari Wulandari`, tekan Enter
5. [Sesi A] Centang Sari Wulandari
6. [Sesi A] Klik `[Assign]`
7. [Sesi A] Verifikasi toast sukses: "Success, Total Control has been assigned."
8. [Sesi B] Buka Overlay Notifikasi
9. [Sesi B] Verifikasi Overlay Notifikasi Sari Wulandari tidak memuat notifikasi baru terkait Total Control (jumlah notifikasi sama dengan baseline langkah 2)
10. [Sesi B] Tutup konteks browser Sesi B dan hapus sesi login terkait

### TC-GS-ROLE-241: Notifikasi in-app ke target untuk Remove Total Control

11. [Sesi A] Ketik Search `Sari Wulandari`, tekan Enter
12. [Sesi A] Klik `(⋯)` pada baris Sari Wulandari
13. [Sesi A] Klik `Remove`
14. [Sesi A] Klik `[Remove]`
15. [Sesi A] Tunggu aksi selesai, catat tanggal aksi dalam Date Format General Settings aktif
16. [Sesi B] Buka konteks browser baru, login sebagai Sari Wulandari
17. [Sesi B] Buka Overlay Notifikasi
18. [Sesi B] Verifikasi notifikasi terbaru: Title "Your Total Control access was removed"
19. [Sesi B] Verifikasi Body notifikasi terbaru: "Ahmad Fauzi removed your Total Control access on [Date]."
20. [Sesi B] Verifikasi [Date] pada Body sesuai tanggal aksi langkah 15
21. [Sesi B] Verifikasi [Date] pada Body tampil dalam format Date Format General Settings aktif
22. [Sesi B] Verifikasi tombol `[Mark as Read]` tampil pada notifikasi
23. [Sesi B] Verifikasi tombol `[Detail]` tidak tampil pada notifikasi
24. [Sesi B] Tutup konteks browser Sesi B dan hapus sesi login terkait

### TC-GS-ROLE-242: Notifikasi in-app ke target untuk Remove Read Only

25. [Sesi A] Klik Tab Read Only, ketik Search `Rahmat Hidayat`, tekan Enter
26. [Sesi A] Klik `(⋯)` pada baris Rahmat Hidayat
27. [Sesi A] Klik `Remove`
28. [Sesi A] Klik `[Remove]`
29. [Sesi A] Tunggu aksi selesai, catat tanggal aksi dalam Date Format General Settings aktif
30. [Sesi B] Buka konteks browser baru, login sebagai Rahmat Hidayat
31. [Sesi B] Buka Overlay Notifikasi
32. [Sesi B] Verifikasi notifikasi terbaru: Title "Your Read Only access was removed"
33. [Sesi B] Verifikasi Body notifikasi terbaru: "Ahmad Fauzi removed your Read Only access on [Date]."
34. [Sesi B] Verifikasi [Date] pada Body sesuai tanggal aksi langkah 29
35. [Sesi B] Verifikasi tombol `[Mark as Read]` tampil pada notifikasi
36. [Sesi B] Verifikasi tombol `[Detail]` tidak tampil pada notifikasi
37. [Sesi B] Tutup konteks browser Sesi B dan hapus sesi login terkait

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. TC-GS-ROLE-62 bertanda Automation `Manual Only — (d) dua sesi paralel`; tetap masuk spec, kebutuhan dua konteks ada di Prerequisites.
- Subjudul `###` memetakan langkah ke id TC granular. TC-GS-ROLE-62 dijalankan lebih dulu karena Total Control hasil Assign menjadi precondition TC-GS-ROLE-241 (setara dependensi TC-GS-ROLE-86).
- Asersi absence TC-GS-ROLE-62 (kelas g: absence notifikasi in-app) ditulis di spec ini sebagai langkah 9 sesudah anchor positif toast sukses pemicu (langkah 7, Expected b ditulis lebih dulu daripada Expected a) dan baseline jumlah notifikasi (langkah 2), sesuai bagian 8b butir 2 dan butir 11. Spec ini memuat TC-GS-ROLE-241 dan TC-GS-ROLE-242, yang membuktikan sisi positif notifikasi untuk tipe aksi Remove, sehingga absence notifikasi pada Assign berada di spec yang sama dengan notifikasi positif.
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka dan menutup konteks Sesi B (langkah 1, 10, 16, 24, 30, 37); mencatat baseline dan membuka Overlay Notifikasi (langkah 2, 8, 17, 31); Search baris target, termasuk Search nama target di Popup Assign sebelum dicentang karena pool user bisa lebih dari satu halaman (langkah 4, 11, 25; R-16); "Tunggu aksi selesai" dan mencatat tanggal aksi (langkah 15 dan 29).
- Sesi B pada TC-GS-ROLE-241 dan TC-GS-ROLE-242 login sesudah aksi (precondition a TC: "Target login setelah aksi"); konteks dibuka baru sesudah Remove.
- Langkah 19 dan 33 memverifikasi template body Expected b TC dengan `[Date]` sebagai placeholder; nilai tanggalnya diasersi pada langkah 20, 21, dan 34. Nama admin pada Body (`Ahmad Fauzi`) adalah nama lengkap aktor (Expected b TC-GS-ROLE-241).
- Spec melewati sekitar 35 langkah (37 langkah) karena ketiga TC satu kelas harness (multi-konteks, dua sesi) dan satu layar; tiap blok punya target, pemicu Sesi A, dan asersi Sesi B sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Dua langkah tambahan berasal dari pemecahan `Klik (⋯)` dan `Klik Remove`.
- Langkah penghubung (S-15, bukan dari TC sumber): row action `Remove` berada di overlay `(⋯)` baris, sehingga "Klik Remove pada baris X" (TC-GS-ROLE-241 dan TC-GS-ROLE-242) ditulis `Klik (⋯)` pada baris lalu `Klik Remove` (langkah 12 dan 13; langkah 26 dan 27).
- Temuan untuk QA:
  - TC-GS-ROLE-241 dan TC-GS-ROLE-242 tidak menyebut target; spec memakai Sari Wulandari (dependensi TC-GS-ROLE-86) dan Rahmat Hidayat (dependensi TC-GS-ROLE-88).
  - TC-GS-ROLE-241 Expected c tidak menyebut komponen [Date] (tanggal saja atau tanggal dan jam) dan nilai Date Format aktif; spec membaca Date Format dari General Settings dan membandingkan [Date] dengan tanggal aksi.
  - TC-GS-ROLE-62 Expected a tidak menyebut baseline notifikasi; spec memakai jumlah notifikasi Sari Wulandari sebelum Assign.
  - TC-GS-ROLE-241 dan TC-GS-ROLE-242 tidak menyebut hasil Remove di Sesi A (toast); spec tidak mengasersinya.
  - TC-GS-ROLE-241 dan TC-GS-ROLE-242 "Klik Remove pada baris X" tidak menyebut overlay `(⋯)`; spec membuka overlay `(⋯)` lalu klik `Remove`.
