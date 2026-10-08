---
id: TC-GS-USER-E2E-052-batas-seleksi-bulk
title: Seleksi bulk dibatasi oleh Bulk Action Checkbox Limit
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-410
  - TC-GS-USER-393
coverage:
  web: automated
---

# Seleksi bulk dibatasi oleh Bulk Action Checkbox Limit

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- Bulk Action Checkbox Limit entity ini dikecilkan lewat Admin Console > Plans & Licensing > Lifecycle Settings > tab System Limits (default 1.000) menjadi N, misalnya 5. Nilai N ditentukan tim FE
- Jumlah user yang cocok dengan filter aktif adalah M, dengan M lebih besar dari N (misalnya M = 8) dan tersebar minimal di 2 halaman
- Spec ini tidak menjalankan aksi bulk apa pun (tidak menghapus atau mengubah user), jadi tidak butuh cleanup selain mengembalikan limit
- Spec ini mengubah System Limits, jadi harus dijalankan sendirian dan terpisah dari spec lain yang memakai bulk action. Limit dikembalikan ke nilai semula setelahnya

## Test Steps

### Seleksi manual satu per satu

1. Centang checkbox baris satu per satu sampai baris ke-N
2. Verifikasi checkbox baris ke-(N+1) dan seterusnya berstatus Disabled dengan tooltip "You've reached the maximum selection of N rows." (N diganti nilai limit yang berlaku)
3. Verifikasi N baris sebelumnya tetap tercentang
4. Verifikasi Bulk Action Bar tetap tampil normal dan bisa dipakai
5. Hapus seluruh centang

### Select All melebihi limit

6. Klik "Select All ({M} records)" pada Bulk Action Bar lintas halaman
7. Verifikasi seleksi otomatis dipotong ke N baris pertama, bukan seleksi ditolak total
8. Verifikasi toast error persisten "Error, only the first N of M rows were selected. Narrow your filter to include the rest." muncul (N dan M diganti nilai sesungguhnya) dan bukan Dialog Blok
9. Verifikasi N baris pertama tetap tercentang dan Bulk Action Bar tetap aktif
10. Hapus seluruh centang

## Notes

- Dipisah dari spec bulk lain karena membutuhkan limit yang dikecilkan dan mengubah pengaturan platform-wide (System Limits), yang bisa memengaruhi spec yang berjalan bersamaan.
- Sumber TC memakai angka default 1.000 dan 1.500 baris. Spec ini memakai N dan M kecil melalui setelan Bulk Action Checkbox Limit, dengan maksud dan hasil yang sama.
- Penegakan limit di sisi server saat request API dikirim langsung (`TC-GS-USER-176`) dicakup lapisan BE (`TC-GS-USER-BE-117`).
- Master Data Count Limit, yang juga ada di tab System Limits, dicakup `TC-GS-USER-E2E-040-batas-kuota-master-data`.
