---
id: TC-GS-ROLE-E2E-085-sinkron-sidebar-target-assign-dan-remove-total-control
title: "Sinkronisasi Sidebar Target: Assign dan Remove Total Control"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-229
  - TC-GS-ROLE-230
coverage:
  web: automated
---

# Sinkronisasi Sidebar Target: Assign dan Remove Total Control

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (aktor): Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Layar awal Sesi A (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Akun Sesi B (target, objek asersi): Sari Wulandari (Pre-setup #11, Active, Access Global Settings, tanpa access level dan tanpa baris role). Email disediakan tim FE (tidak ada di Tabel Pre-setup TC), kredensial `Spectra.env.GS_ROLE_TARGET_PASSWORD`. Sesi B dibuka di konteks browser kedua dengan login pada langkah pembuka tiap TC dan ditutup di akhir TC (konteks ditutup, sesi login terkait dihapus).
- Kelas harness: multi-konteks (kelas c). Hasil di Sesi B adalah objek asersi, bukan pemicu.
- Environment variable: `GS_TC_PASSWORD` dan `GS_ROLE_TARGET_PASSWORD`. `GS_ROLE_TARGET_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang diubah: Sari Wulandari di-assign Total Control pada TC-GS-ROLE-229 dan di-Remove pada TC-GS-ROLE-230, sehingga kembali ke Pre-setup #11. Hook `before` memastikan Sari Wulandari tanpa access level dan tanpa baris role lewat API; hook `after` memulihkannya ke state itu bila TC-GS-ROLE-230 tidak selesai. Efek yang tidak dipulihkan: Last Updated dan entri Changelog, Activity Log, serta System Log (log bersifat immutable).
- Tabel "Menu sidebar Total Control" (Expected TC-GS-ROLE-229): `User`, `Role & Permission`, `Import`, `TAG`, `Hardware`, `Brand`, `Measurement`, `File Manager`, `General Settings`, `Activity Log`.
- Kemampuan teknis: dua konteks browser paralel; muat ulang halaman tanpa logout di Sesi B; pemulihan access level lewat API.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite), termasuk untuk akun target Sesi B; spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-229: Assign Total Control menampilkan General Settings dan Activity Log untuk target

1. [Sesi B] Buka konteks browser baru, login sebagai Sari Wulandari
2. [Sesi A] Klik `[+ Assign]`
3. [Sesi A] Ketik Search `Sari Wulandari`, tekan Enter
4. [Sesi A] Centang Sari Wulandari
5. [Sesi A] Klik `[Assign]`
6. [Sesi A] Tunggu aksi selesai
7. [Sesi B] Muat ulang halaman
8. [Sesi B] Untuk setiap menu pada tabel "Menu sidebar Total Control", lakukan langkah 9
9. [Sesi B] Verifikasi menu tersebut tampil di sidebar
10. [Sesi B] Tutup konteks browser Sesi B dan hapus sesi login terkait

### TC-GS-ROLE-230: Remove Total Control mengosongkan sidebar target

11. [Sesi B] Buka konteks browser baru, login sebagai Sari Wulandari
12. [Sesi A] Ketik Search `Sari Wulandari`, tekan Enter
13. [Sesi A] Klik `(⋯)` pada baris Sari Wulandari
14. [Sesi A] Klik `Remove`
15. [Sesi A] Klik `[Remove]`
16. [Sesi A] Tunggu aksi selesai
17. [Sesi B] Muat ulang halaman
18. [Sesi B] Verifikasi pesan "You don't have access to any menu yet." tampil
19. [Sesi B] Verifikasi sidebar Global Settings tidak memuat menu apa pun
20. [Sesi B] Tutup konteks browser Sesi B dan hapus sesi login terkait

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Kedua TC bertanda Automation `Manual Only — (d) dua sesi paralel`; tetap masuk spec, kebutuhan dua konteks ada di Prerequisites.
- Subjudul `###` memetakan langkah ke id TC granular. TC-GS-ROLE-229 dijalankan lebih dulu karena menghasilkan state Total Control yang menjadi precondition TC-GS-ROLE-230.
- Langkah 8 dan 9 adalah perulangan atas sepuluh baris tabel "Menu sidebar Total Control" (satu `Verifikasi` per menu; langkah yang diulang: 9).
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka dan menutup konteks Sesi B (langkah 1, 10, 11, 20); Search baris target di Tab Total Control (langkah 12); Search nama target di Popup Assign sebelum dicentang, karena daftar user di popup (urut Name A-Z) bisa lebih dari satu halaman (langkah 3, R-16/S-03); "Tunggu aksi selesai" sebelum Sesi B memuat ulang (langkah 6, 16).
- Urutan Verifikasi TC-GS-ROLE-230: pesan "You don't have access to any menu yet." (Expected b, langkah 18) ditulis lebih dulu sebagai anchor positif bahwa halaman termuat setelah muat ulang, lalu sidebar kosong (Expected a, langkah 19), karena sidebar kosong tidak punya menu lain yang dapat menjadi anchor.
- Langkah penghubung (S-15, bukan dari TC sumber): row action `Remove` berada di overlay `(⋯)` baris, sehingga "Klik Remove pada baris Sari Wulandari" (TC-GS-ROLE-230) ditulis `Klik (⋯)` pada baris (langkah 13) lalu `Klik Remove` (langkah 14).
- Temuan untuk QA:
  - TC-GS-ROLE-229 dan TC-GS-ROLE-230 tidak menyebut hasil Assign dan Remove di Sesi A (toast); spec tidak mengasersinya.
  - TC-GS-ROLE-230 precondition a ("Sari Wulandari (Total Control) login di sesi B") dan langkah 1 tidak menyatakan apakah Sesi B login sebelum Remove; spec membuka konteks Sesi B baru sebelum Remove dan memuat ulang sesudahnya.
  - TC-GS-ROLE-230 "Klik Remove pada baris Sari Wulandari" tidak menyebut overlay `(⋯)`; spec membuka overlay `(⋯)` lalu klik `Remove`.
