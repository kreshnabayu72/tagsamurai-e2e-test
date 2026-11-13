---
id: TC-FA-FAREG-E2E-056-edit-draft-quantity-naik-turun
title: "Edit draft: Quantity naik dan turun"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-03m, FAREG-LOGIC-03n, §4.4#r3, §9.4.2#r5, §9.4.2#r6, §9.7#r5, FAREG-LOGIC-03o, D-REG-18]
smoke: [FAREG-LOGIC-03o, D-REG-18]
dependsOn: []
trace:
  FAREG-LOGIC-03m: 8
  FAREG-LOGIC-03n: [14, 37]
  §4.4#r3: [8, 14, 23, 29, 35]
  §9.4.2#r5: [12, 14]
  §9.4.2#r6: [23, 29, 31, 37]
  §9.7#r5: [14, 37]
  FAREG-LOGIC-03o: 23
  D-REG-18: [24, 25, 26, 27]
anchor: [4, 11, 20]
coverage:
  web: automated
---

# Edit draft: Quantity naik dan turun

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Qty Naik {runId}` dan `Gudang Qty Turun {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-056-1: Draft tersimpan milik `Rina W` untuk Group `Gudang Qty Naik {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `3`; ketiga aset kosong (tanpa Tag, Photo, maupun Custom field per aset).
  - DU-056-2: Draft tersimpan milik `Rina W` untuk Group `Gudang Qty Turun {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `3`; aset 1 dan aset 2 kosong, aset 3 berisi Serial Number `SN-0003`.
  - Register Asset Bulk Limit bernilai `100`.

## Test Steps

### Quantity naik menambah aset
1. Ketik Search `Gudang Qty Naik {runId}`, tekan Enter
2. Klik Group `Gudang Qty Naik {runId}` pada baris untuk membuka form Edit
3. Klik tab `Asset`
4. Verifikasi Item 1 memuat tiga aset sebelum Quantity diubah
5. Klik tab `General Information`
6. Isi Quantity Item 1 dengan `5`
7. Klik tab `Asset`
8. Verifikasi Item 1 kini memuat lima aset: tiga aset semula tetap ada dan dua aset baru bernama dengan nomor increment berikutnya

### Quantity turun menghapus aset kosong dari increment terakhir tanpa dialog
9. Klik tab `General Information`
10. Isi Quantity Item 1 dengan `3`
11. Verifikasi Quantity Item 1 menampilkan `3`
12. Verifikasi dialog `Remove Assets` tidak tampil
13. Klik tab `Asset`
14. Verifikasi Item 1 memuat tiga aset semula dan dua aset dari increment terakhir sudah dihapus
15. Klik `[Cancel]` pada form
16. Klik `[Leave]` pada dialog Unsaved Changes

### Quantity turun pada aset berisi data meminta konfirmasi
17. Ketik Search `Gudang Qty Turun {runId}`, tekan Enter
18. Klik Group `Gudang Qty Turun {runId}` pada baris untuk membuka form Edit
19. Klik tab `Asset`
20. Verifikasi Item 1 memuat tiga aset sebelum Quantity diubah
21. Klik tab `General Information`
22. Isi Quantity Item 1 dengan `2`
23. Verifikasi dialog `Remove Assets` tampil
24. Verifikasi bullet Name aset ketiga, aset yang akan dihapus, tampil di dialog
25. Verifikasi teks dialog `Their TAG, photo, and custom field data will be lost. This action cannot be undone.`
26. Verifikasi pertanyaan konfirmasi `Are you sure you want to remove it?`
27. Verifikasi tombol `[Cancel]` dan `[Remove]` tampil pada dialog
28. Klik `[Cancel]`
29. Verifikasi Quantity Item 1 kembali menampilkan `3`
30. Klik tab `Asset`
31. Verifikasi Item 1 tetap memuat tiga aset, termasuk aset ketiga dengan Serial Number `SN-0003`
32. Klik tab `General Information`
33. Isi Quantity Item 1 dengan `2`
34. Klik `[Remove]` pada dialog `Remove Assets`
35. Verifikasi Quantity Item 1 menampilkan `2`
36. Klik tab `Asset`
37. Verifikasi Item 1 hanya memuat aset 1 dan aset 2, dan aset ketiga yang berisi Serial Number `SN-0003` sudah dihapus
