---
id: TC-FA-BORROW-E2E-006-tab-borrowed-assets-by-borrower
title: "Tab Borrowed Assets By Borrower menampilkan total aset per Borrower dan halaman Borrowed Asset"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1j#r34", "§4.1j#r35", "§4.1j#r36", "§4.1j#p8", "§4.1j#r37", "§4.1j#r38", "§4.2.14#p1", "§4.2.14#p2"]
smoke: []
dependsOn: []
trace:
  "§4.1j#r34": [8, 9, 15]
  "§4.1j#r35": [13, 14]
  "§4.1j#r36": [5, 9, 10, 11, 12]
  "§4.1j#p8": [25]
  "§4.1j#r37": [21, 25, 27]
  "§4.1j#r38": [31]
  "§4.2.14#p1": [17, 18, 19]
  "§4.2.14#p2": [17, 21, 27, 36, 38]
anchor: []
coverage:
  web: automated
---

# Tab Borrowed Assets By Borrower menampilkan total aset per Borrower dan halaman Borrowed Asset

## Prerequisites
- Aktor: Asset Admin `Admin Aset {runId}` (DU-006-1), Group penugasan `Head Office`.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-006-1: User `Admin Aset {runId}`, role Asset Admin, Group penugasan `Head Office`.
  - Pengaju seluruh BRW: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`).
  - DU-006-2: Borrower `Rizky Ramadhan` (tampil `Rizky R`, Employee ID `EMP-6001`) meminjam tiga aset di Group `Head Office` yang berstatus Borrowed: `Laptop HP ProBook {runId}`, `Monitor Dell P2422H {runId}`, dan `Keyboard Logitech K380 {runId}`. Total Asset `3`.
  - DU-006-3: Borrower `Tono Hidayat` (tampil `Tono H`, Employee ID `EMP-6002`) meminjam dua aset di Group `Head Office` yang berstatus Borrowed: `Printer Brother HL-L2320 {runId}` dan `Scanner Epson V39 {runId}`. Total Asset `2`.
  - DU-006-4: Borrower `Sinta Maharani` (tampil `Sinta S`, Employee ID `EMP-6003`) meminjam `Tablet Lenovo Tab M10 {runId}` di Group `Head Office` dan `Kamera Canon M50 {runId}` di Group `Branch Surabaya`, keduanya berstatus Borrowed. Aktor hanya mencakup Group `Head Office`, sehingga Total Asset yang tampil `1`.
  - DU-006-5: Borrower `Umar Faruq` (tampil `Umar F`, Employee ID `EMP-6004`) meminjam satu aset Non TAG di Group `Head Office` yang berstatus Borrowed: `Kabel Roll 10 Meter {runId}`. Total Asset `1`.
  - DU-006-6: Borrower `Vina Kusuma` (tampil `Vina K`, Employee ID `EMP-6005`) meminjam dua aset di Group `Branch Surabaya` yang berstatus Borrowed: `Speaker Anker Soundcore {runId}` dan `Mikrofon Rode Wireless Go {runId}`.
- Kondisi:
  - Photo at end bernilai OFF pada aset DU-006-5.

## Test Steps

### Tab Borrowed Assets By Borrower menampilkan Borrower dalam cakupan aktor
1. Klik tab `Borrowed Assets`
2. Klik sub-tab `By Borrower`
3. Klik `Filter`
4. Klik field `Borrower`
5. Verifikasi opsi `Rizky R`, `Tono H`, `Sinta S`, dan `Umar F` tampil dan opsi `Vina K` tidak tampil karena seluruh asetnya berada di luar cakupan aktor
6. Pilih opsi `Rizky R`, `Tono H`, `Sinta S`, dan `Umar F`
7. Klik `[Apply]`
8. Verifikasi tabel memuat 4 baris dengan Borrower `Rizky R`, `Tono H`, `Sinta S`, dan `Umar F`

### Urutan awal, Total Asset, Group, dan Employee ID per Borrower
9. Verifikasi urutan baris dari atas ke bawah: Borrower `Rizky R`, `Tono H`, `Sinta S`, lalu `Umar F`
10. Verifikasi baris Borrower `Rizky R` menampilkan Total Asset `3` dan baris Borrower `Tono H` menampilkan Total Asset `2`
11. Verifikasi baris Borrower `Sinta S` menampilkan Total Asset `1` tanpa menghitung aset di luar cakupan aktor
12. Verifikasi baris Borrower `Umar F` menampilkan Total Asset `1`
13. Verifikasi baris Borrower `Rizky R`, `Tono H`, `Sinta S`, dan `Umar F` menampilkan Group `Head Office`
14. Verifikasi baris Borrower `Sinta S` tidak menampilkan Group `Branch Surabaya`
15. Verifikasi baris Borrower `Rizky R` menampilkan Employee ID `EMP-6001`

### Halaman Borrowed Asset dibuka dari nama Borrower
16. Klik nama Borrower `Rizky R`
17. Verifikasi halaman `Borrowed Asset` terbuka dengan Borrower `Rizky R` dan memuat aset `Laptop HP ProBook {runId}`, `Monitor Dell P2422H {runId}`, dan `Keyboard Logitech K380 {runId}`
18. Verifikasi tabel aset tidak memuat kolom `Borrower` dan halaman tidak memuat sub-tab `By Asset` maupun `By Borrower`
19. Verifikasi breadcrumb memuat `Transactions > Borrow > Borrowed Assets > Detail`
20. Klik `⋯` pada baris aset `Laptop HP ProBook {runId}`
21. Verifikasi menu baris memuat `Return`, `Request Extension`, `Report Damaged`, `Report Missing`, dan `Borrow Log`
22. Tutup menu baris
23. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb

### Row action Detail membuka halaman Borrowed Asset
24. Klik `⋯` pada baris Borrower `Tono H`
25. Verifikasi menu baris memuat `Detail`
26. Klik `Detail`
27. Verifikasi halaman `Borrowed Asset` terbuka dengan Borrower `Tono H` dan memuat aset `Printer Brother HL-L2320 {runId}` dan `Scanner Epson V39 {runId}`
28. Kembali ke tab Borrowed Assets lewat segmen Origin Tab pada breadcrumb

### Download tabel By Borrower
29. Klik `Download`
30. Pilih `Download as CSV`
31. Verifikasi berkas terunduh dengan nama `Borrowed-Borrowers` dan memuat 4 baris data yang tampil di tabel

### Halaman Borrowed Asset tanpa aset yang dipinjam
32. Klik nama Borrower `Umar F`
33. Klik `⋯` pada baris aset `Kabel Roll 10 Meter {runId}`
34. Klik `Return`
35. Klik `[Submit]`
36. Verifikasi toast `Success, 1 asset has been returned.` tampil
37. Kembali ke halaman `Borrowed Asset` Borrower `Umar F` lewat segmen Origin Tab pada breadcrumb
38. Verifikasi halaman menampilkan `No borrowed assets` dan `Assets held by this borrower will appear here.`
