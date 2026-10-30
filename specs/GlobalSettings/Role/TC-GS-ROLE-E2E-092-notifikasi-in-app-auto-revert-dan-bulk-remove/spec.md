---
id: TC-GS-ROLE-E2E-092-notifikasi-in-app-auto-revert-dan-bulk-remove
title: "Notifikasi In-App Auto-Revert dan Bulk Remove"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-243
  - TC-GS-ROLE-244
  - TC-GS-ROLE-245
coverage:
  web: automated
---

# Notifikasi In-App Auto-Revert dan Bulk Remove

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (aktor): Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Layar awal Sesi A (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Akun target (objek asersi, konteks browser terpisah dari Sesi A): Nina Kartika (TC-GS-ROLE-243), Wawan Setiawan (TC-GS-ROLE-244 dan TC-GS-ROLE-245), Siti Nurhaliza dan Rina Putri (TC-GS-ROLE-245). Email disediakan tim FE (tidak ada di Tabel Pre-setup TC), kredensial `Spectra.env.GS_ROLE_TARGET_PASSWORD`. Sesi B, Sesi C, dan Sesi D dibuka dengan login di konteks browser baru dan ditutup (konteks ditutup, sesi login terkait dihapus) sebelum TC atau akun berikutnya, kecuali Sesi B pada TC-GS-ROLE-245 yang dibuka sebelum aksi untuk baseline.
- Kelas harness: multi-konteks (kelas c). Hasil di Sesi B, C, dan D adalah objek asersi, bukan pemicu.
- Environment variable: `GS_TC_PASSWORD` dan `GS_ROLE_TARGET_PASSWORD`. Env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`: `GS_ROLE_TARGET_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang diubah (Given dipasang lewat API di hook `before`; pemulihan di hook `after`, tanpa berasumsi langkah spec berhasil penuh):
  - Nina Kartika (Pre-setup #11, Active): di-assign Total Control (keenam role CRUD penuh; setara dependensi TC-GS-ROLE-106, precondition TC-GS-ROLE-243). Pemulihan: access level kosong dan semua baris role dihapus (state kandidat Pre-setup #11).
  - Wawan Setiawan (Pre-setup #11, Active): di-assign Read Only (precondition TC-GS-ROLE-244, setara dependensi TC-GS-ROLE-107). Sesudah TC-GS-ROLE-244 ia kehilangan Read Only dan tetap memegang baris keenam role, sehingga menjadi user regular dengan baris Manage master reference pada TC-GS-ROLE-245. Pemulihan: semua baris role dihapus (state kandidat Pre-setup #11).
  - Siti Nurhaliza (Pre-setup #4, Active): di-assign Total Control (precondition TC-GS-ROLE-245, Dynamic #3). Pemulihan: Total Control dicabut dan Read Only di-assign ulang; baris Manage TAG tidak berubah.
  - Rina Putri (Pre-setup #4, Inactive): diaktifkan dan di-assign Read Only (Dynamic #14) supaya dapat login (TC-GS-ROLE-245 mensyaratkan login Rina Putri). Pemulihan: Read Only di-assign ulang, status dikembalikan ke Inactive; baris Manage TAG tidak berubah.
  - Efek yang tidak dipulihkan: Last Updated, entri log, dan notifikasi target (bersifat immutable).
- Jam server dan jam browser sinkron; `[Date]` dibandingkan dengan tanggal aksi yang dicatat sesudah aksi pemicu.
- Kemampuan teknis: konteks browser paralel (sampai tiga konteks target aktif bersamaan pada TC-GS-ROLE-245); Overlay Notifikasi di tiap konteks; seeding dan pemulihan access level, baris role, dan status user lewat API.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite), termasuk untuk akun target; spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-243: Notifikasi in-app ke target untuk Auto-Revert Total Control

1. [Sesi A] Buka Tab System, lalu Detail "Manage TAG"
2. [Sesi A] Ketik Search `Nina Kartika`, tekan Enter
3. [Sesi A] Uncheck Update pada baris Nina Kartika
4. [Sesi A] Klik `[Remove]` pada dialog
5. [Sesi A] Tunggu aksi selesai, catat tanggal aksi
6. [Sesi B] Buka konteks browser baru, login sebagai Nina Kartika
7. [Sesi B] Buka Overlay Notifikasi
8. [Sesi B] Verifikasi notifikasi terbaru: Title "Your Total Control access was removed"
9. [Sesi B] Verifikasi Body notifikasi terbaru: "Your Total Control access was automatically removed after Ahmad Fauzi changed your role permissions on [Date]."
10. [Sesi B] Verifikasi [Date] pada Body sesuai tanggal aksi langkah 5
11. [Sesi B] Verifikasi tombol `[Mark as Read]` tampil pada notifikasi
12. [Sesi B] Verifikasi tombol `[Detail]` tidak tampil pada notifikasi
13. [Sesi B] Tutup konteks browser Sesi B dan hapus sesi login terkait

### TC-GS-ROLE-244: Notifikasi in-app ke target untuk Auto-Revert Read Only

14. [Sesi A] Buka Tab System, lalu Detail "Manage hardware"
15. [Sesi A] Ketik Search `Wawan Setiawan`, tekan Enter
16. [Sesi A] Centang Create pada baris Wawan Setiawan
17. [Sesi A] Klik `[Remove]` pada dialog
18. [Sesi A] Tunggu aksi selesai, catat tanggal aksi
19. [Sesi B] Buka konteks browser baru, login sebagai Wawan Setiawan
20. [Sesi B] Buka Overlay Notifikasi
21. [Sesi B] Verifikasi notifikasi terbaru: Title "Your Read Only access was removed"
22. [Sesi B] Verifikasi Body notifikasi terbaru: "Your Read Only access was automatically removed after Ahmad Fauzi changed your role permissions on [Date]."
23. [Sesi B] Verifikasi [Date] pada Body sesuai tanggal aksi langkah 18
24. [Sesi B] Verifikasi tombol `[Mark as Read]` tampil pada notifikasi
25. [Sesi B] Verifikasi tombol `[Detail]` tidak tampil pada notifikasi
26. [Sesi B] Tutup konteks browser Sesi B dan hapus sesi login terkait

### TC-GS-ROLE-245: Bulk Remove campuran mengirim notifikasi per target tier

27. [Sesi B] Buka konteks browser baru, login sebagai Wawan Setiawan
28. [Sesi B] Buka Overlay Notifikasi, catat jumlah notifikasi sebagai baseline, tutup overlay
29. [Sesi A] Buka Tab System, lalu Detail "Manage master reference"
30. [Sesi A] Centang Wawan Setiawan, Siti Nurhaliza, dan Rina Putri
31. [Sesi A] Klik Bulk Action > Remove
32. [Sesi A] Klik `[Remove]`
33. [Sesi A] Tunggu aksi selesai
34. [Sesi C] Buka konteks browser baru, login sebagai Siti Nurhaliza
35. [Sesi C] Buka Overlay Notifikasi
36. [Sesi C] Verifikasi notifikasi terbaru Siti Nurhaliza: Title "Your Total Control access was removed"
37. [Sesi C] Tutup konteks browser Sesi C dan hapus sesi login terkait
38. [Sesi D] Buka konteks browser baru, login sebagai Rina Putri
39. [Sesi D] Buka Overlay Notifikasi
40. [Sesi D] Verifikasi notifikasi terbaru Rina Putri: Title "Your Read Only access was removed"
41. [Sesi D] Tutup konteks browser Sesi D dan hapus sesi login terkait
42. [Sesi B] Buka Overlay Notifikasi
43. [Sesi B] Verifikasi Overlay Notifikasi Wawan Setiawan tidak memuat notifikasi baru (jumlah notifikasi sama dengan baseline langkah 28)
44. [Sesi B] Tutup konteks browser Sesi B dan hapus sesi login terkait

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Spec melewati sekitar 35 langkah (44 langkah). Alasan: semua blok satu kelas harness (multi-konteks, kelas c) dan satu topik (notifikasi in-app bagi target yang kehilangan access level lewat auto-revert atau Bulk Remove); tiap TC berdiri sendiri dengan target dan aksi pemicu sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Panjang berasal dari pembukaan konteks tiap target dan penutupan konteks sesuai S-09.
- Subjudul `###` memetakan langkah ke id TC granular. TC-GS-ROLE-244 dijalankan sebelum TC-GS-ROLE-245 karena Wawan Setiawan yang kehilangan Read Only menjadi user regular pada TC-GS-ROLE-245.
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka dan menutup konteks target (langkah 6, 13, 19, 26, 27, 34, 37, 38, 41, 44); Search baris target di Detail (langkah 2, 15); "Tunggu aksi selesai" dan mencatat tanggal aksi (langkah 5, 18, 33); mencatat baseline dan membuka Overlay Notifikasi (langkah 7, 20, 28, 35, 39, 42).
- Urutan Expected TC-GS-ROLE-245: Siti Nurhaliza (a, langkah 36) dan Rina Putri (b, langkah 40) lebih dulu, lalu Wawan Setiawan (c, langkah 43). Notifikasi Siti Nurhaliza dan Rina Putri membuktikan bahwa Bulk Remove sudah menghasilkan notifikasi, sehingga absence notifikasi Wawan Setiawan (c) berada sesudah anchor positif pada pemicu yang sama (bagian 8b butir 2 dan butir 11). Konteks Wawan Setiawan dibuka sebelum aksi (langkah 27) supaya baseline jumlah notifikasi tercatat sebelum pemicu.
- Temuan untuk QA:
  - TC-GS-ROLE-243 dan TC-GS-ROLE-244 tidak menyebut target; spec memakai Nina Kartika (Active) untuk TC-GS-ROLE-243 karena dependensi TC-GS-ROLE-106 memakai Maya Anggraini yang berstatus Inactive dan tidak dapat login, serta Wawan Setiawan (dependensi TC-GS-ROLE-107) untuk TC-GS-ROLE-244.
  - TC-GS-ROLE-245 mensyaratkan login Rina Putri, sedangkan Pre-setup #4 mencatat Rina Putri berstatus Inactive; spec mengaktifkannya sebagai Given dan mengembalikannya ke Inactive di hook `after`.
  - TC-GS-ROLE-245 tidak menyebut Detail role tempat Bulk Remove; spec memakai Detail "Manage master reference" mengikuti TC-GS-ROLE-131 (dependensi).
  - TC-GS-ROLE-243, TC-GS-ROLE-244, dan TC-GS-ROLE-245 tidak menyebut hasil aksi di Sesi A (toast); spec tidak mengasersinya. TC-GS-ROLE-245 Expected a dan b hanya menyebut Title; Body tidak diasersi.
