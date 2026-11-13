---
id: TC-FA-FAREG-E2E-057-edit-draft-remove-item
title: "Edit draft: Remove from List menghapus Item"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§9.7#r19, FI-REG-07, T-REG-15]
smoke: [FI-REG-07, T-REG-15]
dependsOn: []
trace:
  §9.7#r19: [10, 12, 25, 27, 31, 34, 38, 41]
  FI-REG-07: [8, 10, 21]
  T-REG-15: [7, 23]
anchor: [4, 9, 18, 24]
coverage:
  web: automated
---

# Edit draft: Remove from List menghapus Item

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Hapus Item A {runId}`, `Gudang Hapus Item B {runId}`, dan `Gudang Hapus Item C {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-057-1: Draft tersimpan milik `Rina W` untuk Group `Gudang Hapus Item A {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `1`; Item 2 `Office Desk`, `Kayu Jati`, `No Model` dengan Quantity `2`; seluruh aset kedua Item kosong (tanpa Tag, Photo, maupun Custom field per aset).
  - DU-057-2: Draft tersimpan milik `Rina W` untuk Group `Gudang Hapus Item B {runId}`. Item 1 `Office Desk`, `Kayu Jati`, `No Model` dengan Quantity `1`, asetnya kosong; Item 2 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2`, aset 1 berisi Serial Number `SN-0005` dan aset 2 kosong.
  - DU-057-3: Draft tersimpan milik `Rina W` untuk Group `Gudang Hapus Item C {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2`: aset 1 Serial Number `SN-0006` dan aset 2 Serial Number `SN-0007`, keduanya Tag RFID `Verified` dan Condition `Normal`, sehingga berstatus `✓ Ready`; Item 2 `Office Desk`, `Kayu Jati`, `No Model` dengan Quantity `2`, kedua asetnya kosong. Progress batch `50%` (2 dari 4 aset Ready).

## Test Steps

### Remove from List pada Item yang semua asetnya kosong
1. Ketik Search `Gudang Hapus Item A {runId}`, tekan Enter
2. Klik Group `Gudang Hapus Item A {runId}` pada baris untuk membuka form Edit
3. Klik tab `Asset`
4. Verifikasi kartu filter `All` menampilkan `3` aset
5. Klik tab `General Information`
6. Klik row option `Remove from List` pada Item 2 (`Office Desk`)
7. Verifikasi toast `Success, item has been deleted.` tampil
8. Verifikasi dialog `Remove Assets` tidak tampil karena semua aset Item 2 masih kosong
9. Verifikasi tabel Item tetap memuat Item `Laptop`
10. Verifikasi tabel Item tidak lagi memuat Item `Office Desk`
11. Klik tab `Asset`
12. Verifikasi kartu filter `All` menampilkan `1` aset, yaitu aset Item `Laptop`
13. Klik `[Save draft]`
14. Klik `[Cancel]` pada form (form belum diubah sejak Save draft)

### Remove from List pada Item yang asetnya berisi data
15. Ketik Search `Gudang Hapus Item B {runId}`, tekan Enter
16. Klik Group `Gudang Hapus Item B {runId}` pada baris untuk membuka form Edit
17. Klik tab `Asset`
18. Verifikasi kartu filter `All` menampilkan `3` aset
19. Klik tab `General Information`
20. Klik row option `Remove from List` pada Item 2 (`Laptop`)
21. Verifikasi dialog `Remove Assets` tampil lebih dulu karena salah satu aset Item `Laptop` berisi Serial Number `SN-0005`
22. Klik `[Remove]`
23. Verifikasi toast `Success, item has been deleted.` tampil
24. Verifikasi tabel Item tetap memuat Item `Office Desk`
25. Verifikasi tabel Item tidak lagi memuat Item `Laptop`
26. Klik tab `Asset`
27. Verifikasi kartu filter `All` menampilkan `1` aset, yaitu aset Item `Office Desk`
28. Klik `[Save draft]`
29. Klik `[Cancel]` pada form (form belum diubah sejak Save draft)

### Skor kelengkapan diperbarui sesudah Remove from List
30. Ganti isi kotak search dengan `Gudang Hapus Item C {runId}`, tekan Enter
31. Verifikasi Progress batch `Gudang Hapus Item C {runId}` `50%` (2 dari 4 aset Ready)
32. Klik Group `Gudang Hapus Item C {runId}` pada baris untuk membuka form Edit
33. Klik tab `Asset`
34. Verifikasi kartu filter `Ready` menampilkan `2` aset dan kartu `Needs data` menampilkan `2`
35. Klik tab `General Information`
36. Klik row option `Remove from List` pada Item 2 (`Office Desk`)
37. Klik tab `Asset`
38. Verifikasi kartu filter `Ready` menampilkan `2` aset dan kartu `Needs data` menampilkan `0`
39. Klik `[Save draft]`
40. Klik `[Cancel]` pada form (form belum diubah sejak Save draft)
41. Verifikasi Progress batch `Gudang Hapus Item C {runId}` `100%` (2 dari 2 aset Ready), naik dari `50%`
