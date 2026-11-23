---
id: TC-FA-SU-E2E-441-tab-transaction-admin-log-struktur-sub-tab-transfer
title: "Tab Transaction Admin Log: Struktur Sub-tab Transfer"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-797
coverage:
  web: automated
---

# Tab Transaction Admin Log: Struktur Sub-tab Transfer

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; pengguna tanpa transaksi: Hana Kusuma (Pre-setup #20, tanpa Transaction Admin Log). Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log; state yang diubah hanya Search, panel Filter, dan preferensi tampilan sisi klien.
- Kemampuan seed (disediakan tim FE/BE, tanpa endpoint karangan): sub-tab Transfer milik Budi Santoso memuat sedikitnya dua baris dengan nilai Date berbeda, supaya klik sel `Transaction ID` dan default sort dapat diasersi; Pre-setup #29 tidak menjamin baris pada sub-tab selain Borrow (lihat Temuan untuk QA). Baris seed bersifat tambahan, tidak mengubah baris Pre-setup #29, dan tercatat sebagai entri log permanen yang tidak dipulihkan.
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan (nama dan ekstensi) di browser uji; berkas dibuang setelah spec.

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, klik Name Budi Santoso, lalu klik Tab Transaction Admin Log

### TC-FA-SU-797: Struktur Sub-tab Transfer (Budi Santoso)

2. Klik Sub-tab Transfer
3. Verifikasi Sub-tab Transfer tampil pada switcher Tab Transaction Admin Log dengan urutan katalog Jenis Transaksi
4. Verifikasi Table Tools `Search`, `Filter`, dan `Download` tampil
5. Klik icon Search
6. Verifikasi placeholder Search `Search activity, transaction ID, asset, or group...` tampil
7. Klik `←` pada kotak Search
8. Verifikasi Table Tools tanpa ikon Changelog
9. Verifikasi Table Tools tanpa aksi tulis
10. Verifikasi kolom berurutan `Date`, `Activity`, `Transaction ID`, `Name`, `Group`
11. Verifikasi kolom `Role` dan `Transaction Status` tidak ada
12. Klik sel `Transaction ID` pada baris pertama
13. Verifikasi klik `Transaction ID` tidak melakukan apa pun
14. Verifikasi tabel memuat sedikitnya dua baris data uji
15. Verifikasi default sort Date newest first (header `Date` menunjukkan descending)
16. Klik icon Filter
17. Verifikasi panel Filter berisi field `Date`, `Activity` (placeholder `All activities`), `Name` (placeholder `All assets`), dan `Group`
18. Verifikasi panel Filter tanpa field `Role` dan `Transaction Status`
19. Klik icon Filter untuk menutup panel
20. Klik icon Download
21. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
22. Pilih `Download as CSV`
23. Verifikasi berkas `Transaction-Admin-Log-Budi-Santoso-Transfer.csv` terunduh

### TC-FA-SU-797: Struktur Sub-tab Transfer (pengguna tanpa transaksi)

24. Klik Back breadcrumb ke User List, ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, klik Name Hana Kusuma, lalu klik Tab Transaction Admin Log
25. Klik Sub-tab Transfer
26. Verifikasi empty state `No transaction log yet` dengan deskripsi `Transactions this user has processed as PIC will appear here.` tampil
27. Ketik Search `zzzz`, tekan Enter
28. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
29. Kosongkan isi kotak search, tekan Enter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 dan 24 (mencari pengguna di User List lewat Search lalu membuka tab; R-16, 8b.9: sesudah kembali lewat Back, kotak Search mempertahankan nilainya sehingga langkah 24 mengganti isinya), langkah 5, 7, 16, 19, 20, dan 22 (membuka dan menutup input Search, panel Filter, dan overlay Download), serta pengosongan Search di langkah 29 (S-09). Langkah 14 adalah `Verifikasi` pembanding sebelum asersi sort (8b.15d) dan memuat dua baris data uji dengan Date berbeda (S-11).
- Struktur sub-tab tabel Kolom Transfer, Disposal, Audit, Maintenance Routine dibagi satu TC satu spec: Transfer di spec 441, Disposal di spec 263, Audit di spec 442, dan Maintenance Routine di spec 266; sub-tab Repair Ticketing dan Tracking tidak ditampilkan (PRD §4.3g, Open Item §12 #1); sub-tab Assignment memakai tabel sendiri dan diuji di spec 443. TC-FA-SU-797 tidak mengasersi nilai Activity (NC-23).
- Bagian pengguna tanpa transaksi (Hana Kusuma) dijalankan sesudah bagian Budi Santoso.
- Temuan untuk QA (S-15): (1) Klausa "klik Transaction ID tidak melakukan apa pun" dan default sort membutuhkan baris pada sub-tab Transfer, sedangkan Pre-setup #29 hanya menjamin 5 baris sub-tab Borrow; kebutuhan seed dicatat di `## Prerequisites`. (2) Expected f "Search atau Filter tanpa hasil" pada pengguna tanpa data hanya diasersi lewat Search; panel Filter tidak punya opsi pada pengguna tanpa data. (3) Isi panel Filter diasersi sebatas daftar field dan placeholder; opsi dropdown tidak diasersi (NC-23). (4) Post Condition tidak ada.
