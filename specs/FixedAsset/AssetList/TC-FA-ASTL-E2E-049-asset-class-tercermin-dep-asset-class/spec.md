---
id: TC-FA-ASTL-E2E-049-asset-class-tercermin-dep-asset-class
title: "Asset Class tercermin di Asset Value"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-12b", "ASTL-LOGIC-12m", "§9.7#r8"]
smoke: []
dependsOn: ["Asset Class: Asset Class dan metode"]
trace:
  "ASTL-LOGIC-12b": 9
  "ASTL-LOGIC-12m": [13, 15, 16]
  "§9.7#r8": [11, 12, 13]
anchor: [8]
coverage:
  web: automated
---

# Asset Class tercermin di Asset Value

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-049-1: aset `Laptop Pro 16 {runId} - 1`, Group `IT`, Purchase Cost `Rp 18.000.000,00` dari `18000000`, Asset Class `Kelas Elektronik {runId}`, Tax Depreciation Class `Kelompok Pajak 1 {runId}`, Asset Value (Commercial) `Rp 17.700.000,00`, Asset Value (Fiscal) `Rp 17.400.000,00` menurut periode Posted terakhir.
  - DU-049-3: aset `Meja Kerja {runId} - 1`, Group `IT`, Purchase Cost `Rp 18.000.000,00` dari `18000000`, Asset Class `Kelas Furnitur {runId}` dengan metode komersial menyusut dan Tax Method kosong, dengan Asset Value (Commercial) di bawah harga perolehan menurut periode Posted terakhir.

## Test Steps

### Kolom buku mengikuti Asset Class
1. Ketik Search `Laptop Pro 16 {runId}`, tekan Enter
2. Buka Setup Column
3. Centang `Asset Class`
4. Centang `Tax Depreciation Class`
5. Centang `Asset Value (Commercial)`
6. Centang `Asset Value (Fiscal)`
7. Tutup Setup Column
8. Verifikasi baris `Laptop Pro 16 {runId} - 1` menampilkan Asset Class `Kelas Elektronik {runId}` dan Tax Depreciation Class `Kelompok Pajak 1 {runId}`
9. Verifikasi tabel memuat tepat dua kolom nilai buku berurutan, `Asset Value (Commercial)` lalu `Asset Value (Fiscal)`, tanpa kolom nilai buku dinamis lain

### Ubah Asset Class tercermin tanpa muat ulang
10. Pada modul Asset Class, Hendra Saputra mengubah Asset Class `Kelas Elektronik {runId}` menjadi `Kelas Elektronik Baru {runId}` dengan metode `Not Depreciated`, tanpa memuat ulang halaman Fixed Asset > Assets
11. Verifikasi kolom Asset Class baris `Laptop Pro 16 {runId} - 1` menampilkan `Kelas Elektronik Baru {runId}`
12. Verifikasi kolom Tax Depreciation Class baris `Laptop Pro 16 {runId} - 1` menampilkan `—` karena Asset Class tanpa Tax Depreciation Class
13. Verifikasi kolom `Asset Value (Commercial)` dan `Asset Value (Fiscal)` baris `Laptop Pro 16 {runId} - 1` menampilkan `Rp 18.000.000,00` yang sama dengan harga perolehan karena metode `Not Depreciated`, bukan `—`

### Tax Method kosong
14. Ganti isi kotak Search dengan `Meja Kerja {runId}`, tekan Enter
15. Verifikasi kolom `Asset Value (Fiscal)` baris `Meja Kerja {runId} - 1` menampilkan `Rp 18.000.000,00` yang sama dengan harga perolehan karena Tax Method kosong
16. Verifikasi kolom `Asset Value (Commercial)` baris `Meja Kerja {runId} - 1` menampilkan nilai di bawah `Rp 18.000.000,00` karena metode komersial menyusut
