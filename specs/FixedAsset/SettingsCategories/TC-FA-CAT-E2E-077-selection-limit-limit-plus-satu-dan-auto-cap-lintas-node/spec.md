---
id: TC-FA-CAT-E2E-077-selection-limit-limit-plus-satu-dan-auto-cap-lintas-node
title: "Selection Limit: Checkbox Limit+1 Disabled, Select All Melebihi Limit Di-cap Otomatis, dan Hitungan Lintas Node Sidebar"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-245
  - TC-FA-CAT-246
  - TC-FA-CAT-574
coverage:
  web: automated
---

# Selection Limit: Checkbox Limit+1 Disabled, Select All Melebihi Limit Di-cap Otomatis, dan Hitungan Lintas Node Sidebar

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatSelLimit (Pre-setup #36), password dari `Spectra.env.FA_TC_PASSWORD`. Email akun client CatSelLimit tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua lewat langkah Ganti akun: Total Control pada client CatMain (Pre-setup #20) dengan varian Selection Limit 100, password `Spectra.env.FA_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #36: client CatSelLimit dengan Selection Limit 100 dan 120 kategori L1 `Sel Cat 001` sampai `Sel Cat 120`; varian CatMain dengan Selection Limit 100 dan 92 kategori L1 tambahan `Fill 001` sampai `Fill 092` (total 100 kategori L1, termasuk `Vehicle` dan `Electronics` dengan anak `Laptop` dan `Monitor`). Volume data disediakan tim FE/BE lewat seed (kelas e, 5.000 tidak diperlukan; 100 sampai 120 baris).
- State global yang diubah: Selection Limit client (Principal Automation, Pre-setup #11, via sesi API; akun tidak tertulis di Pre-setup TC, disediakan tim FE; mengikuti butir "Sesi API aktor" di `suite.md`). Pemulihan nilai Selection Limit awal CatMain dan seed varian dilakukan hook `before` dan `after` (disediakan tim FE/BE). Suite berjalan serial (`parallel: false`).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-245: Checkbox ke limit+1 disabled dengan tooltip

1. Atur jumlah baris per halaman menjadi 100
2. Centang 100 baris pertama satu per satu
3. Pindah ke halaman 2
4. Verifikasi checkbox baris ke-101 disabled
5. Hover checkbox baris ke-101
6. Verifikasi tooltip `You've reached the maximum selection of 100 rows.`
7. Pindah ke halaman 1
8. Verifikasi seratus baris pertama tetap tercentang
9. Verifikasi Bulk Action Bar tetap aktif
10. Klik `Unselect All`

### TC-FA-CAT-246: Select All melebihi limit di-cap otomatis dengan toast error persist

11. Klik `Select All (120 records)`
12. Verifikasi seleksi di-cap ke 100 baris pertama
13. Verifikasi Bulk Action Bar tetap muncul
14. Verifikasi toast error `Error, only the first 100 of 120 rows were selected. Narrow your filter to include the rest.` tampil
15. Tunggu 10 detik
16. Verifikasi toast error tetap ada
17. Dismiss toast secara manual
18. Klik icon (×) pada Bulk Action Bar

### TC-FA-CAT-574: Selection Limit dihitung lintas node sidebar

19. Logout, lalu login sebagai Total Control client CatMain varian Selection Limit 100 (password `Spectra.env.FA_TC_PASSWORD`)
20. Atur jumlah baris per halaman menjadi 100
21. Pada node `All Categories`, centang satu per satu 99 baris L1 (semua kecuali `Vehicle`)
22. Klik node `Electronics` di Sidebar Category Tree
23. Centang checkbox baris `Laptop`
24. Verifikasi counter `100 categories selected` (seleksi kedua node dihitung bersama)
25. Verifikasi checkbox baris `Monitor` disabled
26. Hover checkbox baris `Monitor`
27. Verifikasi tooltip `You've reached the maximum selection of 100 rows.`
28. Verifikasi seluruh 100 baris tetap tercentang
29. Verifikasi Bulk Action Bar tetap aktif
30. Klik icon (×) pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Kelas e (volume data ≥ 100 baris); ketiga TC berbagi state global Selection Limit 100 dan dataset volume sehingga satu spec (P-4). Principal Automation hanya memicu state (sesi API), bukan konteks kedua.
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): pengaturan jumlah baris per halaman, berpindah halaman, `Unselect All`, dismiss toast, pembatalan seleksi, Logout dan login pada Ganti akun.
- Urutan TC: TC-FA-CAT-245, TC-FA-CAT-246, TC-FA-CAT-574 (client berbeda terakhir).
- Temuan untuk QA:
  - Email akun Total Control client CatSelLimit tidak tertulis di Pre-setup TC.
  - TC-FA-CAT-574 Precondition menyebut varian CatMain sebagai Pre-setup #36 dan #20; ditulis mengikuti Precondition.
  - TC-FA-CAT-246 Expected a ("di-cap ke 100 baris pertama") tidak menyebut teks counter; spec tidak menuliskannya.
