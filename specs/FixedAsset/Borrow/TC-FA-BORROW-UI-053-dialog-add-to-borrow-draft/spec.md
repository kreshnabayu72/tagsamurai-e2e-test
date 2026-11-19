---
id: TC-FA-BORROW-UI-053-dialog-add-to-borrow-draft
title: "Dialog Add to Borrow Draft memilih Draft milik Borrower atau membuat Draft baru"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1b#r1", "§4.1b#r2", "§4.1b#r3", "§4.1b#r4", "§4.1b#p3"]
smoke: []
dependsOn: []
trace:
  "§4.1b#r1": [5, 7, 8, 10, 11]
  "§4.1b#r2": [5, 13, 14, 16, 17, 34, 36]
  "§4.1b#r3": [5, 19]
  "§4.1b#r4": [5, 20, 21]
  "§4.1b#p3": [2, 3, 24, 27, 28, 29, 30, 31, 32, 38, 39, 40, 41, 43]
anchor: [23]
coverage:
  web: automated
---
# Dialog Add to Borrow Draft memilih Draft milik Borrower atau membuat Draft baru

## Prerequisites
- Aktor: Aktor Borrow dalam cakupan Group `Head Office`.
- Layar awal: dialog Add to Borrow Draft sudah terbuka untuk Borrower `Budi Santoso`.
- Komponen: Dialog Add to Borrow Draft
- Data:
  - DU-053-1: Draft Group `Head Office`, Total Asset `2`, semua aset layak, Modified By `Rina W`, Last Updated `09/11/26, 08:01`.
  - DU-053-2: Draft Group `Branch Surabaya`, Total Asset `1` dengan tanda ⚠ karena aset `Toyota Avanza - 6` tidak layak, Modified By `Agus P`, Last Updated `08/11/26, 14:20`.
  - DU-053-3: Draft dengan tiga Group `Head Office`, `Branch Surabaya`, dan `Branch Medan`, Total Asset `4`, Modified By `Rina W`, Last Updated `07/11/26, 16:45`.
  - DU-053-4: Draft tanpa aset dan tanpa Group, Total Asset `0`, Modified By `Agus P`, Last Updated `06/11/26, 09:15`.
  - DU-053-5: Draft Group `Head Office`, Total Asset `3` dengan tanda ⚠ karena baris aset `Projector Epson EB-X06 - 14` belum lengkap (Duration dan Purpose kosong), sedangkan aset `Laptop Dell Latitude 5420 - 10` dan `Meeting Mic Set - 2` lengkap dan layak, Modified By `Sari D`, Last Updated `05/11/26, 10:30`.
  - Chip overflow Group yang diharapkan pada DU-053-3 adalah `+1 more`, dari template `+N more` dengan N satu Group sisa di luar dua badge yang tampil. Dua badge yang tampil adalah dua Group pertama menurut urutan alfabetis A–Z, `Branch Medan` dan `Branch Surabaya`, sehingga `Head Office` ada di chip.
- Kondisi:
  - K1: dialog memuat DU-053-1 sampai DU-053-4 dan belum ada Draft terpilih.
  - K2: tanggal dan waktu pada Last Updated mengikuti format General Settings entitas aktor, yang menghasilkan teks seperti pada DU-053-1 sampai DU-053-4.
  - K3: dialog memuat DU-053-5 dan belum ada Draft terpilih.

## Test Steps

### Kolom bawaan tampil dan Borrower tidak menjadi kolom
1. Tampilkan Dialog Add to Borrow Draft dengan kondisi K1
2. Verifikasi tabel memuat kolom Group, Total Asset, Modified By, dan Last Updated
3. Verifikasi tabel tidak memuat kolom Borrower karena Borrower sudah dipilih pada dialog Select Borrower
4. Klik ikon `⋯` pada header kolom Actions
5. Verifikasi panel Column Visibility mencentang Group, Total Asset, Modified By, dan Last Updated

### Kolom Group menampilkan badge dan ringkasan
6. Tampilkan Dialog Add to Borrow Draft dengan kondisi K1
7. Verifikasi sel Group Draft `Head Office` menampilkan satu badge `Head Office`
8. Verifikasi sel Group Draft ketiga menampilkan dua badge `Branch Medan` dan `Branch Surabaya` berurutan alfabetis A–Z, diikuti chip `+1 more`
9. Arahkan kursor ke sel Group Draft ketiga
10. Verifikasi daftar Group `Head Office`, `Branch Surabaya`, dan `Branch Medan` tersampaikan pada sel itu
11. Verifikasi sel Group Draft tanpa aset menampilkan `—`

### Kolom Total Asset menampilkan jumlah dan tanda aset bermasalah
12. Tampilkan Dialog Add to Borrow Draft dengan kondisi K1
13. Verifikasi sel Total Asset Draft pertama menampilkan `2` tanpa tanda ⚠
14. Verifikasi sel Total Asset Draft `Branch Surabaya` menampilkan `1` dengan tanda ⚠
15. Arahkan kursor ke sel Total Asset Draft `Branch Surabaya`
16. Verifikasi daftar aset `Toyota Avanza - 6` beserta kelayakannya tersampaikan pada sel itu
17. Verifikasi sel Total Asset Draft tanpa aset menampilkan `0`

### Kolom Modified By dan Last Updated terisi
18. Tampilkan Dialog Add to Borrow Draft dengan kondisi K1
19. Verifikasi sel Modified By Draft pertama menampilkan `Rina W` dan Draft `Branch Surabaya` menampilkan `Agus P`
20. Verifikasi sel Last Updated Draft pertama menampilkan `09/11/26, 08:01`
21. Verifikasi sel Last Updated Draft `Branch Surabaya` menampilkan `08/11/26, 14:20`

### Pilihan Draft memakai radio dan toolbar tanpa Download
22. Tampilkan Dialog Add to Borrow Draft dengan kondisi K1
23. Verifikasi keempat baris Draft tampil pada tabel
24. Verifikasi radio tampil pada setiap baris Draft
25. Pilih radio Draft `Head Office` yang pertama
26. Pilih radio Draft `Branch Surabaya`
27. Verifikasi hanya radio Draft `Branch Surabaya` yang terpilih
28. Verifikasi tabel memuat kolom Actions
29. Verifikasi sel Actions baris Draft pertama kosong tanpa aksi baris
30. Verifikasi toolbar memuat kotak Search dan Filter
31. Verifikasi toolbar tidak memuat tombol Download
32. Verifikasi jumlah baris per halaman bernilai `10` dengan pilihan `10`, `25`, `50`, dan `100`

### Total Asset bertanda peringatan untuk Draft yang belum lengkap
33. Tampilkan Dialog Add to Borrow Draft dengan kondisi K3
34. Verifikasi sel Total Asset Draft pada dialog menampilkan `3` dengan tanda ⚠
35. Arahkan kursor ke sel Total Asset Draft itu
36. Verifikasi daftar aset `Projector Epson EB-X06 - 14` beserta isian yang kurang, yaitu Duration dan Purpose, tersampaikan pada sel itu

### Urutan toolbar dan aksi di footer dialog
37. Tampilkan Dialog Add to Borrow Draft dengan kondisi K1
38. Verifikasi toolbar memuat kotak Search lalu Filter berurutan dari kiri ke kanan
39. Verifikasi footer dialog memuat tombol `[Cancel]`, `[New Draft]`, dan `[Add to Borrow Draft]`
40. Verifikasi tombol `[New Draft]` tidak disabled walaupun belum ada Draft yang dipilih
41. Verifikasi tombol `[Add to Borrow Draft]` disabled karena belum ada Draft yang dipilih
42. Pilih radio Draft `Head Office` yang pertama
43. Verifikasi tombol `[Add to Borrow Draft]` tidak disabled setelah satu Draft dipilih
