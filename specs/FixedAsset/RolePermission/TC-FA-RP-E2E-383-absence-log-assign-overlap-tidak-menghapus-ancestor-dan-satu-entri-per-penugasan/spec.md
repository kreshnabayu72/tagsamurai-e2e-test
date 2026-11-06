---
id: TC-FA-RP-E2E-383-absence-log-assign-overlap-tidak-menghapus-ancestor-dan-satu-entri-per-penugasan
title: "Absence log: Assign Role Transaksi overlap tidak mencatat Remove untuk penugasan ancestor dan dicatat satu entri per penugasan"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1210
  - TC-FA-RP-1211
  - TC-FA-RP-1223
coverage:
  web: automated
---

# Absence log: Assign Role Transaksi overlap tidak mencatat Remove untuk penugasan ancestor dan dicatat satu entri per penugasan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #15 (Ahmad Fauzi, kolam pengguna Standard), #18 (pohon Group), #19 (seed Role Transaksi pada `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri, Monitoring & Report Oscar Pratama, Staff Putri Wulandari, Approver Pandu Wijaya), #24 (`Company Changelog`; latar log, tidak diasersi).
- Seeding precondition (hook `before`, kemampuan disediakan tim FE/BE, tanpa endpoint karangan): Nadia Putri, Oscar Pratama, dan Putri Wulandari tanpa penugasan di `Data Center` sub-tab `Disposal` (penugasan yang tersisa dari spec lain dicabut); Ahmad Fauzi tanpa penugasan Approver di `IT Infrastructure` sub-tab `Disposal`. Spec tidak membuat data Dinamis.
- Kemampuan teknis: membaca jumlah entri Changelog Transaction Role sub-tab `Disposal` sebagai baseline (audit trail permanen, S-12 dan bagian 8b butir 10; disediakan tim FE/BE); mengubah dan membaca penugasan Role Transaksi lewat fixture BE untuk pemulihan.
- State yang diubah dan pemulihannya: Assign Monitoring & Report Nadia Putri, Asset Admin Oscar Pratama dan Putri Wulandari pada `Data Center`, serta Approver Ahmad Fauzi pada `IT Infrastructure`, sub-tab `Disposal`. Dipulihkan ke Pre-setup #19 pada langkah terakhir spec dan di hook `after` sebagai cadangan, lewat fixture BE (bukan lewat `Remove` di UI, supaya tidak menambah entri `Remove` ke Changelog). Entri Changelog bersifat permanen. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1210: Assign Monitoring & Report Nadia Putri di `Data Center` tidak mencatat Remove untuk Asset Admin Nadia Putri

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Changelog Transaction Role sub-tab `Disposal`
2. Klik Tab `Transaction Role`
3. Klik node `Data Center` lalu sub-tab `Disposal`
4. Klik `[+ Assign]` pada section Monitoring & Report
5. Ketik Search `Nadia Putri` pada popup, tekan Enter, lalu centang Nadia Putri
6. Klik `[Assign]`
7. Tunggu aksi selesai: popup tertutup
8. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
9. Verifikasi jumlah entri bertambah tepat satu terhadap baseline langkah 1
10. Verifikasi entri terbaru ber-Action `Assign` dengan Field `Monitoring & Report — Data Center`
11. Verifikasi tidak ada entri `Remove` untuk baris Asset Admin Nadia Putri
12. Tutup modal Changelog

### TC-FA-RP-1211: Assign Asset Admin Oscar Pratama dan Putri Wulandari di `Data Center` tidak mencatat Remove untuk baris `IT Infrastructure`

13. Catat baseline (aksi tanpa `Verifikasi`): jumlah entri Changelog Transaction Role sub-tab `Disposal`
14. Klik `[+ Assign]` pada section Asset Admin
15. Telusuri seluruh halaman Pagination popup, lalu centang Oscar Pratama dan Putri Wulandari
16. Klik `[Assign]`
17. Tunggu aksi selesai: popup tertutup
18. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
19. Verifikasi jumlah entri bertambah tepat dua terhadap baseline langkah 13
20. Verifikasi dua entri baru ber-Action `Assign` dengan Field `Asset Admin — Data Center`, satu untuk Oscar Pratama dan satu untuk Putri Wulandari
21. Verifikasi tidak ada entri `Remove` untuk baris Monitoring & Report Oscar Pratama dan baris Staff Putri Wulandari di `IT Infrastructure`
22. Tutup modal Changelog

### TC-FA-RP-1223: Assign Approver Ahmad Fauzi pada `IT Infrastructure` dicatat satu entri tanpa entri per descendant

23. Catat baseline (aksi tanpa `Verifikasi`): jumlah entri Changelog Transaction Role sub-tab `Disposal`
24. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
25. Klik `[+ Assign]` pada section Approver
26. Ketik Search `Ahmad Fauzi` pada popup, tekan Enter, lalu centang Ahmad Fauzi
27. Klik `[Assign]`
28. Tunggu aksi selesai: popup tertutup
29. Klik ikon `[Changelog]` di baris sub-tab `Disposal`
30. Verifikasi jumlah entri bertambah tepat satu terhadap baseline langkah 23
31. Verifikasi entri baru ber-Action `Assign`; Field `Approver — IT Infrastructure`; Old Value `—`; New Value `Ahmad Fauzi`; Modified By `Siti R`
32. Verifikasi tidak ada entri baru dengan Field `Data Center`, `Rack A1`, atau `Helpdesk`
33. Tutup modal Changelog
34. Pulihkan penugasan hasil spec ke Pre-setup #19 lewat fixture BE: cabut Monitoring & Report Nadia Putri, Asset Admin Oscar Pratama dan Putri Wulandari pada `Data Center`, serta Approver Ahmad Fauzi pada `IT Infrastructure`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 34 langkah.
- Kelas g (absence log): tiap TC punya aksi Assign nyata, baseline sendiri yang dicatat tepat sebelum aksi pemicu (S-12; langkah 1, 13, 23), dan anchor positif sebelum tiap asersi absence (bagian 8b butir 2): selisih jumlah entri dan entri `Assign` yang baru tampil (langkah 9 dan 10, 19 dan 20, 30 dan 31) mendahului asersi tidak ada entri `Remove` (langkah 11, 21) dan tidak ada entri dengan Field node lain (langkah 32).
- Pembagian TC lintas spec (S-05): TC-FA-RP-1210 dan TC-FA-RP-1211 ada di `sourceTc` dua spec, spec asal dan spec ini. Klausa a dan b kedua TC (dialog, toast, dan baris di `Data Center` dan `IT Infrastructure`) berada di spec 377; spec ini memuat aksi Assign nyata dan baseline sendiri untuk klausa c (entri `Remove` tidak ada). TC-FA-RP-1223 hanya ada di spec ini.
- Cara baca entri baru (S-14): entri baru dibaca pada baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan; pada langkah 20 himpunan dua baris teratas diasersi tanpa mengandalkan urutan keduanya (keduanya dapat jatuh pada menit yang sama).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1, 13, 23 (baseline); langkah 2, 3, 24 (navigasi Tab, node, dan sub-tab); langkah 4 sampai 6, 14 sampai 16, 25 sampai 27 (aksi Assign pemicu); langkah 7, 17, 28 (tunggu aksi selesai sebelum membuka Changelog, bagian 8b butir 8); langkah 8, 18, 29 (membuka Changelog) dan langkah 12, 22, 33 (menutup modal); langkah 34 (pemulihan, S-09). Search pada langkah 5 dan 26 adalah langkah penghubung untuk menemukan kandidat target di Table User Picker (R-16); langkah 15 menelusuri seluruh halaman Pagination popup karena dua user dicentang tanpa Search (R-22).
- Modal Changelog `Changelog: Role & Permission > Transaction Role > Disposal` memuat entri seluruh node pada sub-tab `Disposal`; Field memuat nama node, sehingga membuka modal dari node `Data Center` atau `IT Infrastructure` menampilkan modal yang sama.
- Langkah 9, 19, 30 mengasersi "tepat satu" atau "tepat dua" entri baru. Angka itu diturunkan dari frasa TC "entri terbaru hanya `Assign`" (TC-FA-RP-1210), "dua entri `Assign`" (TC-FA-RP-1211), dan "tepat satu entri baru" (TC-FA-RP-1223); TC-FA-RP-1210 dan 1211 tidak menulis angka selisih secara eksplisit.
- Temuan untuk QA:
  - Post Condition TC-FA-RP-1210 dan 1211 (rung tertinggi efektif pada `Data Center`; hak efektif pada modul transaksi diamati di modul pemilik, NC-11) tidak punya langkah observasi di TC dan hak efektif tidak teramati di surface ini; tidak diasersi.
  - TC-FA-RP-1210 dan 1211 Expected c tidak menyebut Old Value dan New Value entri `Assign`; spec hanya mengasersi Action dan Field yang disebut TC.
  - TC-FA-RP-1211 Expected c menyebut "baris `IT Infrastructure`" tanpa menyebut nama baris; spec mengasersi tidak ada entri `Remove` untuk baris Monitoring & Report Oscar Pratama dan baris Staff Putri Wulandari (precondition d TC).
  - TC-FA-RP-1223 Precondition tidak menyebut keadaan Ahmad Fauzi pada sub-tab `Disposal`; spec menetapkan Ahmad Fauzi tanpa penugasan Approver di `IT Infrastructure` (seeding hook `before`) agar `V-09` (role sama pada node yang sama) tidak menolak Assign.
  - Penugasan `Data Center` yang tersisa dari spec lain pada Nadia Putri, Oscar Pratama, dan Putri Wulandari dicabut di hook `before`; spec tidak membaca Prerequisites spec lain.
  - Priority TC-FA-RP-1210 (P0) menjadi `Critical` pada frontmatter; `caseType` `Edge` mengikuti TC dominan (1210 dan 1211).
