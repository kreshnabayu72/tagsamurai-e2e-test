---
id: TC-FA-BORROW-E2E-037-mobile-scan-borrow-wizard
title: "Wizard mobile Scan > Borrow menambahkan aset, memilih Borrower, dan menangani offline"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FI-BRW-50, FI-BRW-51, FI-BRW-52, FI-BRW-82, FI-BRW-83, FI-BRW-84, "§4.2.13#b3", "§4.6#p1", "§4.6#p3", "§4.6#b1", "§4.6#b2", "§4.6#b3", "§4.6#b4", "§4.6#b5", "§4.6#b7", "§9.11#b3", "§10#r6"]
smoke: []
dependsOn: []
trace:
  FI-BRW-50: [39]
  FI-BRW-51: [43]
  FI-BRW-52: [47]
  FI-BRW-82: [81]
  FI-BRW-83: [82]
  FI-BRW-84: [83, 86]
  "§4.2.13#b3": [8, 17]
  "§4.6#p1": [2, 41, 43, 47, 68]
  "§4.6#p3": [17, 18, 21, 27, 32, 39, 40, 43, 47, 53, 54]
  "§4.6#b1": [23]
  "§4.6#b2": [8, 10, 11, 13, 14]
  "§4.6#b3": [29, 33, 34, 37]
  "§4.6#b4": [58, 60, 62]
  "§4.6#b5": [69, 70, 71, 74, 75]
  "§4.6#b7": [55, 65]
  "§10#r6": [2, 5]
  "§9.11#b3": [65, 81]
anchor: [4, 25, 36, 85]
coverage:
  android: manual
---

# Wizard mobile Scan > Borrow menambahkan aset, memilih Borrower, dan menangani offline

## Prerequisites
- Aktor: Asset Admin pada aplikasi native Android, lalu Borrower pada langkah «Masuk sebagai Borrower».
- Layar awal: layar utama aplikasi native Android Fixed Asset.
- Data:
  - DU-037-1: User `Agus Pratama {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif, memakai aplikasi native Android.
  - DU-037-2: User `Lina Sari {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif.
  - DU-037-3: User `Rudi Hartono {runId}`, karyawan tanpa role Borrow, aktif, Home Group `Head Office {runId}`, tanpa pinjaman aktif.
  - DU-037-4: Karyawan `Wawan Setiadi {runId}`, aktif, tanpa akun login dan tanpa PIC.
  - DU-037-5: Group `Head Office {runId}`.
  - DU-037-6: Group `Branch Surabaya {runId}`.
  - DU-037-7: Aset `Laptop Lenovo T14 {runId}`, Group `Head Office {runId}`, status Available, TAG QR.
  - DU-037-8: Aset `Scanner Epson DS-530 {runId}`, Group `Head Office {runId}`, status Available, TAG QR.
  - DU-037-9: Aset `Excavator Komatsu PC200 {runId}`, Group `Head Office {runId}`, status Damaged, TAG QR.
  - DU-037-10: Aset `Genset Perkins 20 kVA {runId}`, Group `Branch Surabaya {runId}`, status Available, TAG QR.
  - DU-037-11: Aset `Compressor Atlas Copco {runId}`, Group `Head Office {runId}`, status Available, TAG QR, Allowed borrower hanya Group `Branch Surabaya {runId}`.
  - DU-037-12: BRW berstatus Waiting for Handover, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Duration `3 days`, Purpose `Kunjungan klien`, Requested By `Agus Pratama {runId}`.
  - DU-037-13: BRW berstatus Borrowed, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Toyota Avanza {runId}`, Duration `5 days`, Purpose `Survei lokasi`, Requested By `Agus Pratama {runId}`.
  - DU-037-14: Isian wizard untuk aset `Laptop Lenovo T14 {runId}` dan `Scanner Epson DS-530 {runId}`: Duration `2` dan Purpose `Pemeriksaan gudang`; Submit ditolak karena perangkat offline.
- Kondisi:
  - Max assets per borrower bernilai `10`.
  - Perangkat Android terhubung online kecuali pada langkah yang menyatakan koneksi dimatikan.
  - Akun `Rudi Hartono {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Mobile hanya Android native dan tidak ada mobile web
1. Buka aplikasi native Android Fixed Asset
2. Verifikasi menu `Scan` tersedia di aplikasi native Android
3. Buka alamat aplikasi Fixed Asset lewat peramban perangkat Android
4. Verifikasi halaman aplikasi terbuka di peramban perangkat Android
5. Verifikasi peramban tidak menyediakan antarmuka mobile dan `Scan > Borrow` tidak tersedia
6. Kembali ke aplikasi native Android Fixed Asset

### Hasil scan pertama menentukan tombol Borrow
7. Pindai TAG aset `Laptop Lenovo T14 {runId}` lewat menu `Scan`
8. Verifikasi aset `Laptop Lenovo T14 {runId}` ditemukan dan tombol `[Borrow]` tampil
9. Pindai TAG aset `Excavator Komatsu PC200 {runId}` lewat menu `Scan`
10. Verifikasi alasan `This asset is Damaged and can't be borrowed.` tampil di bawah tombol `[Borrow]`
11. Verifikasi tombol `[Borrow]` nonaktif
12. Pindai TAG aset `Genset Perkins 20 kVA {runId}` lewat menu `Scan`
13. Verifikasi pesan scan `This asset belongs to` diikuti nama Group `Branch Surabaya {runId}` tampil
14. Verifikasi tombol `[Borrow]` tidak tampil dan identitas aset `Genset Perkins 20 kVA {runId}` tidak ditampilkan

### Wizard Scan > Borrow langkah 1 Asset
15. Pindai TAG aset `Laptop Lenovo T14 {runId}` lewat menu `Scan`
16. Ketuk `[Borrow]`
17. Verifikasi langkah 1 `Asset` menampilkan kode, nama `Laptop Lenovo T14 {runId}`, dan status `Available`
18. Verifikasi tombol `[+ Scan more]` tampil
19. Ketuk `[+ Scan more]`
20. Pindai TAG aset `Scanner Epson DS-530 {runId}`
21. Verifikasi aset `Scanner Epson DS-530 {runId}` ditambahkan ke langkah 1 `Asset`
22. Pindai TAG aset `Excavator Komatsu PC200 {runId}`
23. Verifikasi alasan `This asset is Damaged and can't be borrowed.` tampil dan aset `Excavator Komatsu PC200 {runId}` tidak ditambahkan ke langkah 1 `Asset`
24. Pindai TAG aset `Compressor Atlas Copco {runId}`
25. Verifikasi aset `Compressor Atlas Copco {runId}` ditambahkan ke langkah 1 `Asset`

### Langkah 2 Borrower: daftar Blocked, teks bantu kuota, dan kartu aset yang tidak lolos Allowed borrower
26. Lanjut ke langkah 2 `Borrower`
27. Verifikasi langkah 2 menyediakan pemindaian QR kartu karyawan dan pencarian nama
28. Cari nama `Wawan Setiadi {runId}` pada langkah 2 `Borrower`
29. Verifikasi karyawan `Wawan Setiadi {runId}` berstatus `Blocked` dengan alasan `No login account and no PIC. Set a PIC in Users first.`
30. Cari nama `Rudi Hartono {runId}` pada langkah 2 `Borrower`
31. Pilih `Rudi Hartono {runId}` sebagai Borrower
32. Verifikasi teks bantu `0 of 10 borrowed` tampil
33. Verifikasi kartu aset `Compressor Atlas Copco {runId}` ditandai ⚠ dengan caption `This asset can no longer be borrowed.`
34. Verifikasi tooltip ⚠ pada kartu `Compressor Atlas Copco {runId}` memuat satu alasan untuk Borrower `Rudi Hartono {runId}` dengan teks `can't borrow assets from` diikuti Group `Head Office {runId}`
35. Keluarkan kartu aset `Compressor Atlas Copco {runId}` dari wizard
36. Verifikasi kartu aset `Laptop Lenovo T14 {runId}` tetap ada di wizard
37. Verifikasi kartu aset `Compressor Atlas Copco {runId}` tidak ada lagi di wizard

### Langkah 3 Duration & purpose: kartu, bottom sheet, dan bar bawah
38. Lanjut ke langkah 3 `Duration & purpose`
39. Verifikasi aset `Laptop Lenovo T14 {runId}` dan `Scanner Epson DS-530 {runId}` tampil sebagai kartu, satu kartu per aset
40. Verifikasi Duration dan Purpose pada kedua kartu masih kosong
41. Verifikasi kartu aset tidak menampilkan checkbox permanen
42. Ketuk kartu aset `Laptop Lenovo T14 {runId}`
43. Verifikasi bottom sheet untuk mengisi Duration dan Purpose terbuka
44. Tutup bottom sheet Duration dan Purpose
45. Tekan lama kartu aset `Laptop Lenovo T14 {runId}`
46. Ketuk kartu aset `Scanner Epson DS-530 {runId}`
47. Verifikasi bar bawah `[Set Duration & Purpose]` tampil untuk kartu terpilih
48. Ketuk `[Set Duration & Purpose]`
49. Isi Duration dengan `2`
50. Isi Purpose dengan `Pemeriksaan gudang`
51. Ketuk `[Apply to 2 assets]`

### Langkah 4 Review: tanpa Note dan Save Draft, kartu yang tidak lagi layak, dan Submit butuh online
52. Lanjut ke langkah 4 `Review`
53. Verifikasi langkah 4 `Review` menampilkan pembagian BRW per Group dan blok Approval per aset
54. Verifikasi tombol `[Submit]` tampil di langkah 4 `Review`
55. Verifikasi wizard tidak memuat Note maupun `[Save Draft]`
56. Asset Admin `Lina Sari {runId}` mengajukan BRW atas aset `Scanner Epson DS-530 {runId}`
57. Kembali ke langkah 3 `Duration & purpose`
58. Verifikasi kartu aset `Scanner Epson DS-530 {runId}` ditandai ⚠ dengan caption `This asset can no longer be borrowed.`
59. Lanjut ke langkah 4 `Review`
60. Verifikasi tombol `[Submit]` diblokir selama kartu aset `Scanner Epson DS-530 {runId}` masih ada
61. Keluarkan kartu aset `Scanner Epson DS-530 {runId}` dari wizard
62. Verifikasi tombol `[Submit]` dapat dipakai setelah kartu dikeluarkan
63. Matikan koneksi data perangkat
64. Ketuk `[Submit]`
65. Verifikasi BRW untuk aset `Laptop Lenovo T14 {runId}` tidak dibuat selama perangkat offline
66. Nyalakan koneksi data perangkat

### Kartu Aktor Borrow dan kartu pinjaman Borrower
67. Buka daftar BRW di aplikasi native Android
68. Verifikasi tabel BRW tampil sebagai kartu, dialog sebagai bottom sheet, dan toolbar sebagai menu ⋯ serta ikon Search
69. Verifikasi kartu aset `Laptop Dell Latitude 5420 {runId}` berlabel `Waiting for Handover` dengan aksi cepat `[Hand Over]`
70. Verifikasi kartu aset `Toyota Avanza {runId}` berlabel `Borrowed` dengan aksi cepat `[Return]` dan `[Request Extension]`
71. Verifikasi label `Ready for handover` tidak tampil pada kartu mana pun
72. Masuk sebagai Borrower `Rudi Hartono {runId}`
73. Buka daftar pinjaman pribadi Borrower di aplikasi native Android
74. Verifikasi kartu pinjaman aset `Laptop Dell Latitude 5420 {runId}` tampil tanpa aksi `[Hand Over]`
75. Verifikasi kartu pinjaman aset `Toyota Avanza {runId}` tampil tanpa aksi `[Return]` karena bukan pinjaman self-service

### Handover saat offline
76. Masuk sebagai Asset Admin `Agus Pratama {runId}`
77. Ketuk `[Hand Over]` pada kartu aset `Laptop Dell Latitude 5420 {runId}`
78. Matikan koneksi data perangkat
79. Pindai TAG aset `Laptop Dell Latitude 5420 {runId}`
80. Ambil foto aset `Laptop Dell Latitude 5420 {runId}`
81. Verifikasi pemindaian TAG dan foto berhasil dilakukan saat perangkat offline
82. Verifikasi konfirmasi Borrower dan perubahan status baris menunggu online
83. Verifikasi status `Pending sync` tampil di perangkat
84. Nyalakan koneksi data perangkat
85. Verifikasi kartu aset `Laptop Dell Latitude 5420 {runId}` tampil di daftar BRW setelah koneksi aktif
86. Verifikasi status `Pending sync` hilang setelah tersinkron
