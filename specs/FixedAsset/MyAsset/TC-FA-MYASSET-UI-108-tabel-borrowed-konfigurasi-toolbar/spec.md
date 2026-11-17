---
id: TC-FA-MYASSET-UI-108-tabel-borrowed-konfigurasi-toolbar
title: "Tabel Borrowed: kolom tampil awal, urutan kolom, field Filter, dan placeholder Search"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1#p2", "§4.1b#p1", "§4.1b#r1", "§4.1b#r2", "§4.1b#r3", "§4.1b#r4", "§4.1b#r5", "§4.1b#r6", "§4.1b#r7", "§4.1b#r8", "§4.1b#r9", "§4.1b#r10", "§4.1b#r12", "§4.1b#r13", "§4.1b#r14", "§4.1b#r15", "§4.1b#r16", "§4.1b#r17", "§4.1b#r18", "§4.3#r4", "§5#r1", "§5#r3", "§5#r7", "§5#r10"]
smoke: []
dependsOn: []
trace:
  "§4.1#p2": [2, 3, 4, 7, 10, 11]
  "§4.1b#p1": [13, 14]
  "§4.1b#r1": [2, 8, 24]
  "§4.1b#r2": [2, 8, 24, 26]
  "§4.1b#r3": [2, 8, 24]
  "§4.1b#r4": [2, 8, 24, 27, 39]
  "§4.1b#r5": [2, 8, 24, 28]
  "§4.1b#r6": [2, 8, 24, 29]
  "§4.1b#r7": [2, 8, 24, 30]
  "§4.1b#r8": [3, 9, 24, 25, 31]
  "§4.1b#r9": [3, 9, 24, 25, 32]
  "§4.1b#r10": [2, 8, 24, 35]
  "§4.1b#r12": [2, 8, 24, 33]
  "§4.1b#r13": [2, 8, 24]
  "§4.1b#r14": [2, 8, 24, 34]
  "§4.1b#r15": [2, 8, 24]
  "§4.1b#r16": [2, 8, 24, 36]
  "§4.1b#r17": [3, 9, 24, 25, 37]
  "§4.1b#r18": [3, 9, 24]
  "§4.3#r4": 14
  "§5#r1": [13, 14]
  "§5#r3": 21
  "§5#r7": [15, 18]
  "§5#r10": [2, 7]
anchor: []
coverage:
  web: automated
---

# Tabel Borrowed: kolom tampil awal, urutan kolom, field Filter, dan placeholder Search

## Prerequisites
- Aktor: Borrower (Budi Santoso, pengguna yang membuka halaman My Asset miliknya).
- Layar awal: Halaman My Asset > tab Borrowed
- Komponen: Tabel Borrowed (T-MYA-02)
- Data:
  - DU-108-1: respons tiruan, satu baris tabel Borrowed: Photo `laptop-dell-9.jpg`, Name `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Brand `Dell`, Model/Type `Latitude 5420`, Group `Head Office`, Status `Overdue`, TAG `RFID`, Category `Laptop`, Due Date `06/11/26`, Remaining `3 days overdue`, Borrower `Me`, Transaction ID `BRW-2026-0148`, Source `Admin`, Duration `4 days`, Handed Over At `03/11/26, 09:00`, Extensions `1 / 2`, Purpose `Presentasi klien kuartal keempat`.
- Kondisi:
  - K1: tabel Borrowed berisi DU-108-1.

## Test Steps

### Kolom tampil awal dan urutan kolom pada tabel
1. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
2. Verifikasi header tabel memuat kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Due Date`, `Remaining`, `Borrower`, `Transaction ID`, `Source`, `Duration`, dan `Handed Over At`, berurutan dari kiri ke kanan
3. Verifikasi header tabel tidak memuat kolom `TAG`, `Category`, `Extensions`, dan `Purpose`
4. Verifikasi checkbox header seleksi tampil sebagai kolom pertama sebelum kolom `Photo`

### Daftar kolom di Column Visibility
5. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
6. Klik `⋯` pada header kolom Actions (Column Visibility)
7. Verifikasi daftar kolom memuat berurutan `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `TAG`, `Category`, `Due Date`, `Remaining`, `Borrower`, `Transaction ID`, `Source`, `Duration`, `Handed Over At`, `Extensions`, dan `Purpose`
8. Verifikasi checkbox kolom `Photo`, `Name`, `Asset ID`, `Brand`, `Model/Type`, `Group`, `Status`, `Due Date`, `Remaining`, `Borrower`, `Transaction ID`, `Source`, `Duration`, dan `Handed Over At` tercentang
9. Verifikasi checkbox kolom `TAG`, `Category`, `Extensions`, dan `Purpose` tidak tercentang
10. Verifikasi semua checkbox kolom aktif (enabled), sehingga setiap kolom Hideable
11. Verifikasi daftar kolom tidak memuat `Checkbox` dan `Actions`

### Isi toolbar tabel Borrowed
12. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
13. Verifikasi toolbar memuat tepat ikon `Search`, `Filter`, dan `Download`, berurutan dari kiri ke kanan
14. Verifikasi tombol `Borrow an Asset` tidak tampil di halaman
15. Verifikasi ikon `Changelog` tidak tampil di toolbar

### Riwayat aset lewat Borrow Log
16. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
17. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 9`
18. Verifikasi riwayat aset tersedia lewat aksi `Borrow Log` pada menu baris

### Placeholder kotak Search
19. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
20. Klik ikon `Search`
21. Verifikasi kotak Search memiliki placeholder `Search asset name, asset ID...`

### Field Filter menurut kolom yang dapat difilter
22. Tampilkan Tabel Borrowed (T-MYA-02) dengan kondisi K1
23. Klik ikon `Filter`
24. Verifikasi Filter Panel memuat tepat field `Asset Name`, `Brand`, `Model/Type`, `Group`, `Status`, `TAG`, `Category`, `Due Date`, `Borrower`, `Source`, `Handed Over At`, dan `Extensions`
25. Verifikasi field `TAG`, `Category`, dan `Extensions` tampil di Filter Panel walau kolomnya tersembunyi
26. Verifikasi field `Asset Name` di Filter Panel berupa dropdown multi-select searchable dengan placeholder `All asset names`
27. Verifikasi field `Brand` di Filter Panel berupa dropdown multi-select searchable dengan placeholder `All brands`
28. Verifikasi field `Model/Type` di Filter Panel berupa dropdown multi-select searchable dengan placeholder `All models`
29. Verifikasi field `Group` di Filter Panel berupa dropdown multi-select searchable dengan placeholder `All groups`
30. Verifikasi field `Status` di Filter Panel berupa dropdown multi-select searchable dengan placeholder `All statuses`
31. Verifikasi field `TAG` di Filter Panel berupa dropdown multi-select searchable dengan placeholder `All TAGs`
32. Verifikasi field `Category` di Filter Panel berupa dropdown multi-select searchable dengan placeholder `All categories`
33. Verifikasi field `Borrower` di Filter Panel berupa dropdown multi-select searchable dengan placeholder `All users`
34. Verifikasi field `Source` di Filter Panel berupa dropdown multi-select searchable dengan placeholder `All sources`
35. Verifikasi field `Due Date` di Filter Panel berupa date range picker dengan placeholder `Select date`
36. Verifikasi field `Handed Over At` di Filter Panel berupa date range picker dengan placeholder `Select date`
37. Verifikasi field `Extensions` di Filter Panel berupa dua input rentang dengan placeholder `Min` dan `Max`
38. Klik field `Brand` di Filter Panel
39. Verifikasi dropdown field `Brand` memuat kotak cari
