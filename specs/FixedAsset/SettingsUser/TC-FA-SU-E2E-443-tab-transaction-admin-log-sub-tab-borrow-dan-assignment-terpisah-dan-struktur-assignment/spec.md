---
id: TC-FA-SU-E2E-443-tab-transaction-admin-log-sub-tab-borrow-dan-assignment-terpisah-dan-struktur-assignment
title: "Tab Transaction Admin Log: Sub-tab Borrow dan Assignment Terpisah dan Struktur Sub-tab Assignment"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1133
  - TC-FA-SU-1132
coverage:
  web: automated
---

# Tab Transaction Admin Log: Sub-tab Borrow dan Assignment Terpisah dan Struktur Sub-tab Assignment

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup, hanya dibaca dan tidak diubah (S-06): Client `FaUserMain` (#20) dan Transaction Admin Log Budi Santoso (#29): sub-tab Borrow 5 baris dan sub-tab Assignment 4 baris, yaitu baris A `ASG-20260720-0071` (`20/07/26`, `Handed over`, `Laptop Dell Latitude - 8`, Assignee `Rina W`, Group `Branch Surabaya`), baris B `ASG-20260719-0070` (`19/07/26`, `Approved`, `Monitor LG 24 - 4`, Assignee Division `General Affairs`, Group `IT Infrastructure`), baris C `ASG-20260717-0069` (`17/07/26`, `Requested`, `Camera Sony A7 - 3`, Assignee `Andi P`, Group `Logistics Warehouse`), dan baris D `ASG-20260715-0068` (`15/07/26`, `Rejected`, `Printer HP LaserJet - 2`, Assignee `Dewi L`, Group `Finance & Accounting`). Pengguna tanpa transaksi: Hana Kusuma (#20), hanya dibaca. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan (nama dan ekstensi) di browser uji; berkas dibuang setelah spec. Nama berkas mengikuti nama pengguna target dengan spasi menjadi tanda hubung, yaitu `Transaction-Admin-Log-Budi-Santoso-Assignment.csv` (nama literal TC, tanpa akhiran spec karena target adalah Budi Santoso Pre-setup #29, bukan pengguna milik spec).

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, klik Name Budi Santoso, lalu klik Tab Transaction Admin Log

### TC-FA-SU-1133: Sub-tab Borrow dan Assignment terpisah

2. Verifikasi switcher berisi 8 sub-tab berurutan `Borrow`, `Assignment`, `Transfer`, `Damaged`, `Missing`, `Disposal`, `Audit`, `Maintenance Routine`; tidak ada sub-tab `Repair Ticketing` dan `Tracking`
3. Verifikasi tidak ada sub-tab berlabel `Borrowing & Assignment`
4. Verifikasi sub-tab awal saat tab dibuka adalah `Borrow`
5. Verifikasi kolom sub-tab Borrow berurutan `Date`, `Activity`, `Transaction ID`, `Name`, `Borrower`, `Group`
6. Klik icon Search
7. Verifikasi placeholder Search `Search activity, transaction ID, asset, or borrower...` tampil
8. Klik `←` pada kotak Search
9. Klik Sub-tab Assignment
10. Verifikasi kolom sub-tab Assignment berurutan `Date`, `Activity`, `Transaction ID`, `Name`, `Assignee`, `Group`
11. Klik icon Search
12. Verifikasi placeholder Search `Search activity, transaction ID, asset, or assignee...` tampil
13. Klik `←` pada kotak Search
14. Klik Sub-tab Borrow
15. Verifikasi kolom sub-tab Borrow berurutan `Date`, `Activity`, `Transaction ID`, `Name`, `Borrower`, `Group`

### TC-FA-SU-1132: Struktur Sub-tab Assignment (Budi Santoso)

16. Klik Sub-tab Assignment
17. Verifikasi Sub-tab Assignment tampil pada switcher tepat setelah Sub-tab Borrow dengan urutan katalog Jenis Transaksi
18. Verifikasi Table Tools `Search`, `Filter`, dan `Download` tampil
19. Klik icon Search
20. Verifikasi placeholder Search `Search activity, transaction ID, asset, or assignee...` tampil
21. Klik `←` pada kotak Search
22. Verifikasi Table Tools tanpa ikon Changelog
23. Verifikasi Table Tools tanpa aksi tulis
24. Verifikasi kolom berurutan `Date`, `Activity`, `Transaction ID`, `Name`, `Assignee`, `Group`, dan header kolom `⋯` (Column Visibility)
25. Verifikasi kolom `Date`, `Transaction ID`, `Name`, `Assignee`, dan `Group` sortable dan kolom `Activity` unsortable
26. Verifikasi kolom `Role` dan `Transaction Status` tidak ada
27. Klik sel `Transaction ID` pada baris pertama
28. Verifikasi klik `Transaction ID` tidak melakukan apa pun
29. Verifikasi Assignee baris `ASG-20260719-0070` menampilkan nama Division `General Affairs`
30. Verifikasi default sort Date newest first: `ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`
31. Klik icon Filter
32. Verifikasi panel Filter berisi field `Date` (`Select date`), `Activity` (`All activities`), `Name` (`All assets`), `Assignee` (`All assignees`), dan `Group` (`All groups`) dengan label `Date`, `Activity`, `Name`, `Assignee`, `Group`
33. Verifikasi panel Filter tanpa field `Role` dan `Transaction Status`
34. Klik icon Filter untuk menutup panel
35. Klik icon Download
36. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
37. Pilih `Download as CSV`
38. Verifikasi berkas `Transaction-Admin-Log-Budi-Santoso-Assignment.csv` terunduh
39. Klik Back breadcrumb ke User List, ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, klik Name Hana Kusuma, lalu klik Tab Transaction Admin Log
40. Klik Sub-tab Assignment
41. Verifikasi empty state `No transaction log yet` dengan deskripsi `Transactions this user has processed as PIC will appear here.` tampil
42. Ketik Search `zzzz`, tekan Enter
43. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
44. Kosongkan isi kotak search, tekan Enter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan blok TC-FA-SU-1133 lalu TC-FA-SU-1132 berbeda dari urutan nomor TC karena blok pertama membaca kedua sub-tab dari awal tab dan blok kedua merinci sub-tab Assignment.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 dan 39 (mencari pengguna lewat Search di User List lalu membuka tab; R-16, 8b.9: sesudah kembali lewat Back kotak Search mempertahankan nilainya sehingga langkah 39 mengganti isinya), langkah 6, 8, 9, 11, 13, 14, 16, 19, 21, 31, 34, 35, dan 37 (membuka dan menutup input Search, panel Filter, overlay Download, dan berpindah sub-tab), serta pengosongan Search di langkah 44 (S-09). Langkah 14 dan 15 mengamati kembali kolom Borrow sesudah berpindah dari Assignment (langkah 4 TC-FA-SU-1133).
- Struktur sub-tab lain yang berdiri sendiri: Transfer di spec 441, Damaged di spec 468, Missing di spec 471, Disposal di spec 263, Audit di spec 442, dan Maintenance Routine di spec 266.
- Alasan melewati sekitar 35 langkah (44 langkah): kedua TC satu kelas (fungsional baca) pada satu pengguna dengan seed Pre-setup yang sama, berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), terutama kolom, toolbar, dan panel Filter yang tampil di dua sub-tab.
- Bagian pengguna tanpa transaksi (Hana Kusuma) dijalankan sesudah bagian Budi Santoso.
- Nama berkas Download memakai nama target Budi Santoso (Pre-setup #29) persis seperti TC, tanpa akhiran nomor spec, karena spec tidak membuat pengguna sendiri.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1132 dan 1133 memakai seed Assignment Budi Santoso dari Pre-setup #29 (`ASG-20260720-0071` sampai `ASG-20260715-0068`) tanpa menyatakan mekanisme seed; spec membaca seed itu apa adanya dan tidak mengarang endpoint. (2) Kolom ACC TC-FA-SU-1133 menyebut `#20; Role Total Control`; `#20` adalah Client `FaUserMain`, bukan akun, sehingga aktor diambil dari hook suite (Lina Marlina, Pre-setup #1). (3) TC-FA-SU-1132 langkah 5 memakai Hana Kusuma (Pending Activation) sebagai pengguna tanpa transaksi; Pre-setup tidak menyatakan Transaction Admin Log Hana Kusuma kosong. (4) Expected f "Search atau Filter tanpa hasil" diasersi lewat Search saja karena panel Filter tidak punya opsi pada pengguna tanpa data. Post Condition tidak ada.
