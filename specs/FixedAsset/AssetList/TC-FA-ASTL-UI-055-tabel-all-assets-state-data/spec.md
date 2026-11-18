---
id: TC-FA-ASTL-UI-055-tabel-all-assets-state-data
title: "State data tabel All Assets: memuat, kosong, gagal"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["S-39", "S-41", "S-42", "EC-21", "EmptystatetabelAllAssets", "§7.1#r1", "§7.1#b3", "EB-TBL-1@tabel-all-assets"]
smoke: []
dependsOn: []
trace:
  "S-39": 2
  "S-41": [4, 13]
  "S-42": [16, 17, 20, 21, 22]
  "EC-21": 16
  "EmptystatetabelAllAssets": [4, 13]
  "§7.1#r1": [4, 5, 8, 9, 13]
  "§7.1#b3": 6
  "EB-TBL-1@tabel-all-assets": [4, 13, 14, 16, 18]
anchor: [11]
coverage:
  web: automated
---
# State data tabel All Assets: memuat, kosong, gagal

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Tabel All Assets
- Data:
  - DU-055-1: Aset pembanding: Name `Printer Laser - 1`, Asset ID `AST-0031`, Status `Not Paired Yet`.
- Kondisi:
  - K1: respons daftar aset belum selesai dimuat.
  - K2: daftar aset kosong tanpa Search maupun Filter, dan aktor memegang hak tab Registration.
  - K3: daftar aset kosong tanpa Search maupun Filter, dan aktor tidak memegang hak tab Registration.
  - K4: daftar memuat DU-055-1, dan Search dengan kata kunci `Tidak Ada` menghasilkan nol baris.
  - K5: memuat daftar aset gagal karena error server pada permintaan pertama, kartu status berhasil dimuat, dan permintaan ulang berhasil memuat DU-055-1; jumlah permintaan kartu status dicatat.

## Test Steps

### Tabel memuat data
1. Tampilkan Tabel All Assets dengan kondisi K1
2. Verifikasi tabel dalam keadaan memuat: tidak ada baris data, empty state, maupun pesan error sampai respons selesai

### Kosong alami dengan hak Registration
3. Tampilkan Tabel All Assets dengan kondisi K2
4. Verifikasi tabel menampilkan ilustrasi, `No assets yet`, dan `Get started by registering your first asset.`
5. Verifikasi frasa `registering your first asset` tampil sebagai tautan ke tab `Registration`
6. Verifikasi deskripsi empty state memakai kata `registering`

### Kosong alami tanpa hak Registration
7. Tampilkan Tabel All Assets dengan kondisi K3
8. Verifikasi tabel menampilkan `No assets yet` dan `Get started by registering your first asset.`
9. Verifikasi frasa `registering your first asset` tampil sebagai teks biasa

### Kosong karena hasil Search
10. Tampilkan Tabel All Assets dengan kondisi K4
11. Verifikasi baris `Printer Laser - 1` tampil
12. Ketik Search `Tidak Ada`, tekan Enter
13. Verifikasi tabel menampilkan ilustrasi, `No results found`, dan `Try adjusting your search or filter.`
14. Verifikasi `No assets yet` tidak tampil

### Gagal memuat tabel
15. Tampilkan Tabel All Assets dengan kondisi K5
16. Verifikasi area tabel menampilkan `Unable to load this data.` dan tombol `[Try Again]`
17. Verifikasi `Unable to load this data.` tidak tampil sebagai toast
18. Verifikasi `No assets yet` tidak tampil
19. Klik `[Try Again]`
20. Verifikasi baris `Printer Laser - 1` tampil pada tabel

### Error hanya pada area tabel
21. Verifikasi kartu status tetap tampil normal tanpa pesan error selama tabel gagal dan sesudah dimuat ulang
22. Verifikasi klik `[Try Again]` tabel tidak memuat ulang kartu status (jumlah permintaan kartu status tidak bertambah)
