---
id: TC-FA-MYASSET-E2E-062-mobile-seleksi-bulk-dep-borrow
title: "Mobile: seleksi bulk Request Extension lewat tekan lama tanpa checkbox permanen"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-16", "§4.1b#p6", "§4.6#p1"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "FI-16": [4, 6, 7, 10, 23, 24, 31, 32]
  "§4.1b#p6": [12, 20, 27, 28, 29, 33]
  "§4.6#p1": [4, 6, 7, 8, 9, 11, 14, 15, 17, 18, 23, 24]
anchor: [3, 22]
coverage:
  android: automated
---
# Mobile: seleksi bulk Request Extension lewat tekan lama tanpa checkbox permanen

## Prerequisites
- Aktor: Borrower yang juga PIC dari satu Borrower tanpa akun, karyawan aktif ber-akun login.
- Layar awal: halaman `My Asset` tab Task di aplikasi Android.
- Data:
  - DU-062-1: pinjaman Admin milik aktor berstatus `Borrowed` dengan aset `Projector Epson EB-X06 {runId}`, Duration `3 days`, tanpa Damage Report, tanpa laporan Missing, dan tanpa pengajuan Extend yang menunggu.
  - DU-062-2: pinjaman Admin milik aktor berstatus `Borrowed` dengan aset `Meeting Mic Set {runId}`, Duration `3 days`, tanpa Damage Report, tanpa laporan Missing, dan tanpa pengajuan Extend yang menunggu.
  - DU-062-3: pinjaman Admin atas nama Borrower tanpa akun `Wulan Pratama {runId}`, PIC-nya adalah aktor, berstatus `Borrowed` dengan aset `Laptop Dell Latitude 5420 {runId}`, Duration `3 days`, tanpa Damage Report, tanpa laporan Missing, dan tanpa pengajuan Extend yang menunggu.

## Test Steps

### Kartu Borrowed tanpa kotak centang permanen
1. Klik tab `Borrowed`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi kartu aset milik DU-062-1, DU-062-2, dan DU-062-3 tampil di tab Borrowed
4. Verifikasi tidak ada kotak centang pada kartu aset milik DU-062-1, DU-062-2, dan DU-062-3

### Tekan lama memulai mode seleksi
5. Tekan lama kartu aset `Projector Epson EB-X06 {runId}`
6. Verifikasi kartu aset milik DU-062-1 terpilih
7. Verifikasi kotak seleksi kosong muncul pada kartu aset milik DU-062-2
8. Verifikasi counter seleksi menampilkan `1 Selected`
9. Verifikasi tombol `[Select All]` tampil
10. Verifikasi aksi `Request Extension` tampil
11. Verifikasi tombol `[✕]` tampil
12. Verifikasi kartu aset milik DU-062-3 nonaktif dengan alasan `Select assets from one borrower only.` tersampaikan

### Ketuk kartu lain memilih, membatalkan, dan menolak Borrower lain
13. Klik kartu aset `Meeting Mic Set {runId}`
14. Verifikasi kartu aset milik DU-062-2 terpilih
15. Verifikasi counter seleksi menunjukkan jumlah `2`
16. Klik kartu aset `Meeting Mic Set {runId}`
17. Verifikasi kartu aset milik DU-062-2 tidak terpilih
18. Verifikasi counter seleksi menunjukkan jumlah `1`
19. Klik kartu aset `Laptop Dell Latitude 5420 {runId}`
20. Verifikasi counter seleksi tetap menunjukkan jumlah `1`

### Tombol tutup keluar dari mode seleksi
21. Klik `[✕]`
22. Verifikasi kartu aset milik DU-062-1 tampil di tab Borrowed
23. Verifikasi bilah aksi massal tidak tampil
24. Verifikasi tidak ada kotak centang pada kartu aset milik DU-062-1

### Select All memilih hanya kartu Borrower yang sama
25. Tekan lama kartu aset `Projector Epson EB-X06 {runId}`
26. Klik `[Select All]`
27. Verifikasi kartu aset milik DU-062-2 terpilih
28. Verifikasi counter seleksi menunjukkan jumlah `2`
29. Verifikasi kartu aset milik DU-062-3 nonaktif dengan alasan `Select assets from one borrower only.` tersampaikan

### Request Extension membuka satu halaman untuk kartu terpilih
30. Klik `Request Extension`
31. Verifikasi halaman Extension Request terbuka dengan breadcrumb `My Asset > Borrowed > Extension Request`
32. Verifikasi halaman Extension Request memuat aset milik DU-062-1 dan DU-062-2
33. Verifikasi halaman Extension Request tidak memuat aset milik DU-062-3
