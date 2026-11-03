---
id: TC-FA-SU-E2E-356-download-user-list-lebih-dari-5-000-baris-loading-screen-unduhan-langsung-dan-tanpa
title: "Volume Data: Download User List Lebih dari 5.000 Baris dan Perubahan Selection Limit Live"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-368
  - TC-FA-SU-950
coverage:
  web: automated
---

# Volume Data: Download User List Lebih dari 5.000 Baris dan Perubahan Selection Limit Live

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini pada Client `FaUserBig`; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Pada langkah 13 sampai 14 akun yang sama login ulang pada Client `FaUserMain`; hook `after` memulihkan sesi ke Client default suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserBig` (#40, plan Enterprise, 5.001 pengguna disiapkan lewat seed API sebelum spec berjalan; N = 5.001 diturunkan dari seeding) dan Client `FaUserMain` (#20, 25 pengguna; 23 baris dapat dipilih karena Default User dan akun sendiri tidak dapat dipilih). Filter yang menyisakan tepat 100 baris pada `FaUserBig` dibaca dari `Fixture.faSettingsUser.filterSeratusBaris` (berkas fixture belum ada, disediakan tim FE). Nilai Pre-setup lain dibaca dari `Fixture.faSettingsUser.preSetup`.
- Kemampuan teknis (disediakan tim FE): seed API 5.001 pengguna pada Client `FaUserBig` (Pre-setup #40) dan akun Lina Marlina pada Client itu beserta cara memilih Client saat login (TC tidak menyebutnya); Principal Automation (Pre-setup #12) mengubah Selection Limit Client `FaUserMain` di Lifecycle Settings > System Limits lewat sesi API; pembacaan berkas unduhan hanya sampai terunduh (isi berkas tidak diasersi).
- State global: Selection Limit Client `FaUserMain` (5 pada langkah 15, dipulihkan ke 100 pada langkah 24 dan di hook `after`). Spec tidak mengubah data pengguna. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-368: Download di atas 5.000 baris

1. Klik `Download`
2. Pilih format CSV
3. Verifikasi loading screen tampil sampai berkas siap
4. Verifikasi tidak ada toast sukses dan tidak ada toast informasional `Preparing`
5. Verifikasi tidak ada notifikasi in-app dan tidak ada perpindahan ke halaman Export History
6. Verifikasi berkas CSV langsung terunduh
7. Terapkan Filter yang menyisakan 100 baris
8. Klik `Download`
9. Pilih format CSV
10. Verifikasi tidak ada loading screen khusus
11. Verifikasi berkas CSV terunduh
12. Hapus Filter

### TC-FA-SU-950: Selection Limit dibaca live

13. Logout sebagai Lina Marlina pada Client `FaUserBig`
14. Login sebagai Lina Marlina (Total Control) dengan `Spectra.env.FA_TC_PASSWORD` pada Client `FaUserMain`
15. Principal Automation mengubah Selection Limit Client `FaUserMain` menjadi 5 di Lifecycle Settings > System Limits lewat sesi API hingga tersimpan
16. Buka halaman Fixed Asset > Settings > User tanpa muat ulang manual
17. Centang lima baris pertama yang dapat dipilih
18. Hover checkbox baris ke-6
19. Verifikasi checkbox baris ke-6 Disabled dengan tooltip "You've reached the maximum selection of 5 rows."
20. Klik `Select All`
21. Verifikasi toast "Error, only the first 5 of 23 rows were selected. Narrow your filter to include the rest."
22. Verifikasi Select All auto-cap ke 5 baris pertama
23. Klik `Unselect All`
24. Principal Automation mengembalikan Selection Limit Client `FaUserMain` ke 100 lewat sesi API hingga tersimpan

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-SU-76 dan TC-FA-SU-123 ada di spec 355.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 dan 12 (pasang dan hapus Filter, S-09), 13 sampai 14 (ganti akun dan Client dengan langkah eksplisit; S-07), 17 (pengulangan centang sebagai satu langkah), 23 (Unselect All), dan 24 (pemulihan sesi API). Langkah 15 adalah pemicu state lewat sesi API (R-20).
- Bagian 8b butir 11: langkah 3 (loading screen) menjadi anchor positif; asersi absence toast dan notifikasi pada langkah 4 dan 5 ditulis segera sesudah pemicu (langkah 2) dan berkas terunduh pada langkah 6 menjadi anchor artefak. Langkah 10 (absence loading screen khusus) didahului pemicu pada langkah 9 dan diikuti berkas terunduh pada langkah 11.
- Kedua TC berkelas e (volume data dan ambang konfigurasi) pada dua Client berbeda; ganti Client dilakukan pada langkah 13 sampai 14.
- Temuan untuk QA (S-15): (1) TC-FA-SU-368 langkah 5 menyebut "filter yang menyisakan 100 baris" tanpa nilai filter; spec memakai fixture yang disediakan tim FE. (2) TC-FA-SU-950 mencantumkan Pre-setup #36 (Client `FaUserSel`, 120 pengguna) tetapi Expected menyebut "23 rows" dan "dari 100 menjadi 5" yang sesuai Client `FaUserMain` (25 pengguna, varian Selection Limit 5); spec memakai Client `FaUserMain`. (3) TC-FA-SU-368 butir b menyebut halaman Export History tanpa lokasinya; spec mengasersi tidak ada perpindahan ke halaman itu, dan "tanpa job background" tidak punya cara cek lain di TC. (4) Pre-setup TC tidak menyebut akun Lina Marlina pada Client `FaUserBig` dan cara memilih Client saat login.
