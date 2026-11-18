---
id: TC-FA-MYASSET-E2E-038-tautan-url-tab-dan-highlight-dep-borrow
title: "Tautan My Asset dengan parameter tab dan highlight: baris transaksi disorot dan tabel pindah halaman"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r22", "§4.2.1#b4", "§4.4#r48", "§4.4#r49", "§9.2#b16"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§1.2#r22": [3, 4, 11, 12, 14, 16, 17, 20, 35, 36]
  "§4.2.1#b4": [6, 10, 11, 27, 29, 30]
  "§4.4#r48": [2, 19]
  "§4.4#r49": [3, 12, 20]
  "§9.2#b16": [2, 19]
anchor: [8, 25, 33]
coverage:
  web: automated
---

# Tautan My Asset dengan parameter tab dan highlight: baris transaksi disorot dan tabel pindah halaman

## Prerequisites
- Aktor: Borrower `Lestari Putri {runId}`, pengguna karyawan ber-akun login tanpa role admin.
- Layar awal: halaman Fixed Asset (FAMS) dengan navbar.
- Data:
  - DU-038-1: User `Lestari Putri {runId}`, tanpa role admin, cakupan Group `Head Office`.
  - DU-038-2: User `Agus Prasetyo {runId}`, tanpa role admin, cakupan Group `Head Office`.
  - DU-038-3: 3 aset `Laptop Kantor {n} {runId}` dengan n dari 1 sampai 3 dalam satu pinjaman Admin atas nama `Lestari Putri {runId}`, Group `Head Office`, Status `Borrowed`, Duration `1 day`, Handed Over At `T0 − 1 hari`, Due Date `T0`. Transaction ID dibentuk server dan sama untuk ketiga aset.
  - DU-038-4: 12 aset `Kursi Kerja {n} {runId}` dengan n dari 1 sampai 12, pinjaman Admin atas nama `Lestari Putri {runId}`, Group `Head Office`, Status `Borrowed`, Duration `1 day`, Handed Over At `T0`, Due Date `T0 + 1 hari`.
  - DU-038-5: aset `Laptop Dell Latitude 5420 {runId}`, Brand `Dell`, dalam satu pinjaman Admin atas nama `Lestari Putri {runId}`, Group `Head Office`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0`, Due Date `T0 + 3 hari`. Satu pinjaman dengan DU-038-7.
  - DU-038-6: 8 aset `Meja Lipat {n} {runId}` dengan n dari 1 sampai 8, Brand `Informa`, pinjaman Admin atas nama `Lestari Putri {runId}`, Group `Head Office`, Status `Borrowed`, Duration `5 days`, Handed Over At `T0`, Due Date `T0 + 5 hari`.
  - DU-038-7: aset `Laptop Dell Latitude 5430 {runId}`, Brand `Dell`, dalam pinjaman yang sama dengan DU-038-5, Group `Head Office`, Status `Borrowed`, Duration `8 days`, Handed Over At `T0`, Due Date `T0 + 8 hari`.
  - DU-038-8: pinjaman atas nama `Lestari Putri {runId}`, aset `Kamera Canon EOS 90D {runId}`, Group `Head Office`, Status `Returned`, Handed Over At `T0 − 6 hari`, Closed At `T0 − 3 hari`. Baris ini hanya ada di tab History.
  - DU-038-9: pinjaman Admin atas nama `Agus Prasetyo {runId}`, aset `Proyektor BenQ {runId}`, Group `Head Office`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0`.
  - Kata kunci Search: DU-038-10 `Meja Lipat`.
  - Nilai Filter: DU-038-11 field `Brand` dengan nilai `Informa`.
- Kondisi:
  - Tab Borrowed `Lestari Putri {runId}` berisi 25 baris aset dengan 10 baris per halaman bawaan dan Sort bawaan Due Date terdekat. Urutannya: DU-038-3 pada posisi 1 sampai 3, DU-038-4 pada posisi 4 sampai 15, DU-038-5 pada posisi 16 (halaman kedua), DU-038-6 pada posisi 17 sampai 24, dan DU-038-7 pada posisi 25 (halaman ketiga).
  - Tab History `Lestari Putri {runId}` berisi 1 baris aset, DU-038-8.

## Test Steps

### Tautan dengan tab dan highlight membuka tab dan menyorot semua baris transaksi
1. Buka tautan My Asset dengan parameter `tab` bernilai `borrowed` dan parameter `highlight` berisi Transaction ID milik DU-038-3
2. Verifikasi tab `Borrowed` terbuka
3. Verifikasi ketiga baris `Laptop Kantor {n} {runId}` milik DU-038-3 tersorot
4. Verifikasi hanya tiga baris yang tersorot di tabel
5. Waktu berlalu sampai 4 detik sejak sorotan tampil, lebih lama dari durasi sorotan 3 detik
6. Verifikasi sorotan sudah hilang dari ketiga baris `Laptop Kantor {n} {runId}`

### Baris tersebar di beberapa halaman: Search di-reset dan tabel pindah ke halaman baris pertama
7. Ketik Search `Meja Lipat`, tekan Enter
8. Verifikasi tabel hanya memuat 8 baris `Meja Lipat {n} {runId}`
9. Buka tautan My Asset dengan parameter `tab` bernilai `borrowed` dan parameter `highlight` berisi Transaction ID milik DU-038-5 dan DU-038-7
10. Verifikasi kotak Search kosong dan tabel tidak lagi tersaring oleh kata kunci `Meja Lipat`
11. Verifikasi tabel menampilkan halaman kedua yang memuat baris `Laptop Dell Latitude 5420 {runId}`
12. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tersorot
13. Klik halaman `3` pada paginasi
14. Verifikasi baris `Laptop Dell Latitude 5430 {runId}` di halaman ketiga tidak tersorot

### Highlight yang tidak dikenal tidak membuka data dan tidak menyorot baris
15. Buka tautan My Asset dengan parameter `tab` bernilai `borrowed` dan parameter `highlight` berisi Transaction ID milik DU-038-9
16. Verifikasi tab `Borrowed` tetap terbuka
17. Verifikasi tidak ada baris yang tersorot dan baris `Proyektor BenQ {runId}` milik `Agus Prasetyo {runId}` tidak tampil di tabel

### Tautan ke tab History menyorot baris pinjaman yang sudah ditutup
18. Buka tautan My Asset dengan parameter `tab` bernilai `history` dan parameter `highlight` berisi Transaction ID milik DU-038-8
19. Verifikasi tab `History` terbuka
20. Verifikasi baris `Kamera Canon EOS 90D {runId}` tersorot

### Filter ter-Apply yang menyaring keluar baris tujuan di-reset dan tabel pindah halaman
21. Klik tab `Borrowed`
22. Klik ikon `Filter` pada toolbar
23. Pilih `Informa` pada field Filter `Brand`
24. Klik `[Apply]`
25. Verifikasi Filter `Brand` bernilai `Informa` menyisakan 8 baris `Meja Lipat {n} {runId}` di tabel
26. Buka tautan My Asset dengan parameter `tab` bernilai `borrowed` dan parameter `highlight` berisi Transaction ID milik DU-038-5 dan DU-038-7
27. Verifikasi ikon `Filter` tidak menampilkan badge titik karena Filter `Brand` sudah di-reset
28. Klik ikon `Filter` pada toolbar untuk membuka Filter Panel
29. Verifikasi field Filter `Brand` kosong
30. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil dan tersorot setelah Filter `Brand` di-reset

### Tabel pindah ke halaman yang memuat baris pertama menurut Sort aktif
31. Klik header kolom Duration
32. Klik header kolom Duration
33. Verifikasi baris `Laptop Dell Latitude 5430 {runId}` tampil sebagai baris pertama tabel menurut Longest First
34. Buka tautan My Asset dengan parameter `tab` bernilai `borrowed` dan parameter `highlight` berisi Transaction ID milik DU-038-5 dan DU-038-7
35. Verifikasi tabel menampilkan halaman pertama yang memuat baris `Laptop Dell Latitude 5430 {runId}` sebagai baris pertama menurut Sort aktif
36. Verifikasi baris `Laptop Dell Latitude 5430 {runId}` dan baris `Laptop Dell Latitude 5420 {runId}` tersorot di halaman pertama
