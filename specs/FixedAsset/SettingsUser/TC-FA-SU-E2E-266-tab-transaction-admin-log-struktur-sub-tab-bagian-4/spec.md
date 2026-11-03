---
id: TC-FA-SU-E2E-266-tab-transaction-admin-log-struktur-sub-tab-bagian-4
title: "Tab Transaction Admin Log: Struktur Sub-tab (Bagian 4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-804
coverage:
  web: automated
---

# Tab Transaction Admin Log: Struktur Sub-tab (Bagian 4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrowing & Assignment berisi 5 baris (`BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`) dengan nilai Group, Role, Action Taken, Date, dan Transaction Status per baris sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan (nama, ekstensi, dan isi) di browser uji serta membaca isi CSV dan XLSX; berkas unduhan dibuang setelah spec.
- Kemampuan seed (disediakan tim FE): sub-tab Maintenance Routine milik Budi Santoso memuat sedikitnya satu baris supaya klik sel `Transaction ID` dapat dilakukan; Pre-setup #29 tidak menjamin hal itu (lihat Temuan untuk QA). Pengguna tanpa data transaksi: Hana Kusuma (Pre-setup #20); tidak ada Transaction Admin Log untuknya.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, lalu klik Tab Transaction Admin Log

### TC-FA-SU-804: Struktur Sub-tab Maintenance Routine (Budi Santoso)

2. Klik Sub-tab Maintenance Routine
3. Verifikasi Sub-tab Maintenance Routine tampil pada switcher Tab Transaction Admin Log dengan urutan katalog Jenis Transaksi
4. Verifikasi Table Tools `Search`, `Filter`, dan `Download` tampil
5. Klik icon Search
6. Verifikasi placeholder Search `Search transaction ID, group, or role...` tampil
7. Klik `←` pada kotak Search
8. Verifikasi Table Tools tanpa icon Changelog dan tanpa aksi tulis
9. Verifikasi kolom berurutan `Transaction ID`, `Group`, `Role`, `Action Taken`, `Date`, `Transaction Status`
10. Klik sel `Transaction ID` pada baris pertama
11. Verifikasi klik `Transaction ID` tidak melakukan apa pun (halaman tetap dan tidak ada dialog)
12. Verifikasi header `Date` menunjukkan sort descending (↓) sebagai default sort
13. Klik icon Filter
14. Verifikasi panel Filter berisi field `Group`, `Role`, `Action Taken`, `Date`, dan `Transaction Status`
15. Klik icon Filter untuk menutup panel
16. Klik icon Download
17. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
18. Pilih `Download as CSV`
19. Verifikasi file `Transaction-Admin-Log-Budi-Santoso-Maintenance-Routine.csv` terunduh
20. Klik Back breadcrumb ke User List, cari Hana Kusuma lewat Search, buka Detail User Hana Kusuma, lalu klik Tab Transaction Admin Log

### TC-FA-SU-804: Struktur Sub-tab Maintenance Routine (pengguna tanpa transaksi)

21. Klik Sub-tab Maintenance Routine
22. Verifikasi empty state `No transaction log yet` dengan deskripsi `Transactions this user has processed as PIC will appear here.` tampil
23. Ketik Search `zzzz`, tekan Enter
24. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
25. Kosongkan isi kotak search, tekan Enter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16) dan pengosongan Search; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Bagian pengguna tanpa transaksi (Hana Kusuma) dijalankan sesudah bagian Budi Santoso.
- Pre-setup #29 hanya menjamin 5 baris pada sub-tab Borrowing & Assignment; sub-tab lain berisi data atau kosong tanpa asersi nilai (NC-23). Karena itu isi baris, nilai Action Taken, dan nilai Transaction Status tidak diasersi.
- Temuan untuk QA (S-15): (1) Klausa "klik Transaction ID tidak melakukan apa pun" membutuhkan sedikitnya satu baris pada sub-tab yang diuji, sedangkan Pre-setup #29 tidak menjamin baris pada sub-tab selain Borrowing & Assignment; kebutuhan itu ditulis di `## Prerequisites` sebagai kemampuan seed yang disediakan tim FE. (2) Expected "Search atau Filter tanpa hasil" pada pengguna tanpa data hanya diasersi lewat Search; opsi dropdown Filter tidak ada pada pengguna tanpa data. (3) Pembukaan panel Filter diasersi sebatas daftar field; opsi dropdown tidak diasersi (NC-23). (4) Post Condition tidak ada.
