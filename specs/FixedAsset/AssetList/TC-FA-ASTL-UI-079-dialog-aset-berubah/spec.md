---
id: TC-FA-ASTL-UI-079-dialog-aset-berubah
title: "Dialog Aset Berubah"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-20c", "ASTL-LOGIC-20b", "D-14", "DO-03", "§9.9#p4"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-20c": [7, 8, 13]
  "ASTL-LOGIC-20b": [15, 16]
  "D-14": [2, 3, 7, 10, 11]
  "DO-03": [4, 7, 13]
  "§9.9#p4": 5
anchor: []
coverage:
  web: automated
---
# Dialog Aset Berubah

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Aset Berubah
- Data:
  - DU-079-1: Aset `Laptop Pro 16 - 1`, Asset ID `AST-0001`, Group `IT`, berubah oleh pengguna lain sejak dialog aksi dibuka.
  - DU-079-2: Aset `Laptop Pro 16 - 2`, Asset ID `AST-0002`, Group `IT`, berubah oleh pengguna lain sejak dialog aksi dibuka.
  - DU-079-3: Aset `Laptop Pro 16 - 3`, Asset ID `AST-0003`, Group `IT`, berubah oleh pengguna lain sejak dialog aksi dibuka.
  - DU-079-4: Aset `Genset 20kVA - 1`, Asset ID `AST-0060`, Group `Cabang Medan`, Disposed, berubah menjadi berjejak Posted sejak dialog Delete Asset Data dibuka.
  - Teks yang diharapkan untuk tiga aset: `3 selected assets were changed by someone else. Please review.`, dari jumlah aset penyebab 3.
- Kondisi:
  - K1: aksi Edit Purchase atas DU-079-1 ditolak karena aset berubah; dialog `Edit Purchase` masih terbuka di bawah.
  - K2: aksi Bulk atas DU-079-1 sampai DU-079-3 ditolak karena ketiganya berubah; dialog aksi masih terbuka di bawah.
  - K3: aksi Delete Asset Data atas DU-079-4 ditolak karena versi aset berubah sejak dialog dibuka dan perubahan itu membuat aset berjejak Posted; dialog `Delete Asset Data` masih terbuka di bawah.

## Test Steps

### Satu aset berubah
1. Tampilkan Dialog Aset Berubah dengan kondisi K1
2. Verifikasi dialog berjudul `Asset Changed` tampil dengan teks `This asset was changed by someone else. Please review.`
3. Verifikasi daftar aset penyebab memuat `Laptop Pro 16 - 1`
4. Verifikasi dialog `Asset Changed` tampil di atas dialog `Edit Purchase` yang masih terbuka
5. Verifikasi dialog `Asset Changed` hanya memuat tombol `[OK]` dan tidak memiliki input
6. Klik `[OK]`
7. Verifikasi dialog `Asset Changed` dan dialog `Edit Purchase` tertutup
8. Verifikasi baris `Laptop Pro 16 - 1` dan tabel dimuat ulang

### Beberapa aset berubah
9. Tampilkan Dialog Aset Berubah dengan kondisi K2
10. Verifikasi teks `3 selected assets were changed by someone else. Please review.` tampil
11. Verifikasi daftar aset penyebab memuat `Laptop Pro 16 - 1`, `Laptop Pro 16 - 2`, dan `Laptop Pro 16 - 3` di dalam daftar yang dapat digulir
12. Klik `[OK]`
13. Verifikasi dialog `Asset Changed` dan dialog aksi di bawahnya tertutup

### Perubahan versi didahulukan atas penolakan aturan
14. Tampilkan Dialog Aset Berubah dengan kondisi K3
15. Verifikasi dialog berjudul `Asset Changed` tampil dengan daftar aset penyebab `Genset 20kVA - 1`
16. Verifikasi alert inline `Asset has posted depreciation or journal entries. Use Disposal.` tidak tampil di dialog `Delete Asset Data`
