---
id: TC-FA-MYASSET-E2E-041-pic-borrower-berpindah-dep-users
title: "PIC Borrower diganti: baris pindah ke My Asset PIC baru dan PIC lama tidak melihatnya"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r52", "§9.2#r23", "§9.4.2#r48", "§9.4.2#r49", "§9.7#r11"]
smoke: []
dependsOn: ["Users: Borrower tanpa akun beserta PIC-nya, dan User Detail > User Log", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§1.2#r52": [11, 13, 17, 19, 21, 24]
  "§9.2#r23": [11, 17]
  "§9.4.2#r48": 17
  "§9.4.2#r49": [11, 13]
  "§9.7#r11": [11, 17]
anchor: [4, 6, 10]
coverage:
  web: automated
---

# PIC Borrower diganti: baris pindah ke My Asset PIC baru dan PIC lama tidak melihatnya

## Prerequisites
- Aktor: PIC lama `Nugroho Wibowo {runId}` (DU-041-1) dan PIC baru `Rahayu Pertiwi {runId}` (DU-041-2). Aktor lain yang memicu perubahan: Admin `Bambang Santoso {runId}` (DU-041-7), yang mengganti PIC.
- Layar awal: halaman masuk Fixed Asset.
- Data:
  - DU-041-1: pengguna `Nugroho Wibowo {runId}`, role `Read Only`, Group `Head Office`.
  - DU-041-2: pengguna `Rahayu Pertiwi {runId}`, role `Read Only`, Group `Head Office`.
  - DU-041-3: Borrower tanpa akun `Dewi Anggraini`, PIC awal `Nugroho Wibowo {runId}`. Nama tampil `Dewi A`, dari Full Name `Dewi Anggraini`. Hover yang diharapkan sesudah PIC diganti `Dewi Anggraini · PIC: Rahayu Pertiwi {runId}`, dari Full Name dan User Name PIC baru.
  - DU-041-4: pinjaman aset `Kamera Sony A6400 {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Dewi Anggraini`.
  - DU-041-5: pinjaman aset `Printer Epson L3250 {runId}`, Group `Head Office`, Status `Returned`, Source `Admin`, Borrower `Dewi Anggraini`. Handover dikonfirmasi PIC `Nugroho Wibowo {runId}` atas nama Borrower.
  - DU-041-6: pinjaman aset `Monitor LG 24MK {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Me`, milik PIC lama sendiri.
  - DU-041-7: pengguna `Bambang Santoso {runId}`, role `Total Control`, Group `Head Office`.
- Kondisi:
  - Akun DU-041-1, DU-041-2, dan DU-041-7 aktif.
  - Tab Borrowed PIC lama memuat 2 baris, yaitu DU-041-4 dan DU-041-6. Tab History PIC lama memuat 1 baris, yaitu DU-041-5.

## Test Steps

### PIC lama melihat baris aktif dan riwayat Borrower tanpa akun sebelum PIC diganti
1. Masuk sebagai PIC lama `Nugroho Wibowo {runId}`
2. Buka `My Asset` dari menu profil pada navbar
3. Klik tab `Borrowed`
4. Verifikasi baris `Kamera Sony A6400 {runId}` tampil dengan kolom `Borrower` berisi `Dewi A`
5. Klik tab `History`
6. Verifikasi baris `Printer Epson L3250 {runId}` tampil dengan kolom `Holder` berisi `Dewi A`

### PIC lama tidak lagi melihat baris maupun riwayat Borrower tanpa akun sesudah PIC diganti
7. Admin `Bambang Santoso {runId}` mengganti PIC Borrower tanpa akun `Dewi Anggraini` dari `Nugroho Wibowo {runId}` menjadi `Rahayu Pertiwi {runId}` lewat `Change PIC` di Users

8. Muat ulang halaman
9. Klik tab `Borrowed`
10. Verifikasi baris `Monitor LG 24MK {runId}` milik PIC lama sendiri tampil
11. Verifikasi baris `Kamera Sony A6400 {runId}` tidak tampil di tabel Borrowed
12. Klik tab `History`
13. Verifikasi empty state `No history yet` tampil karena baris `Printer Epson L3250 {runId}` tidak lagi terlihat oleh PIC lama

### PIC baru melihat baris aktif dan riwayat yang pindah
14. Masuk sebagai PIC baru `Rahayu Pertiwi {runId}`
15. Buka `My Asset` dari menu profil pada navbar
16. Klik tab `Borrowed`
17. Verifikasi baris `Kamera Sony A6400 {runId}` tampil dengan kolom `Borrower` berisi `Dewi A`
18. Klik tab `History`
19. Verifikasi baris `Printer Epson L3250 {runId}` tampil
20. Arahkan kursor ke kolom `Holder` pada baris `Printer Epson L3250 {runId}`
21. Verifikasi hover kolom `Holder` memuat `Dewi Anggraini · PIC: Rahayu Pertiwi {runId}`
22. Buka menu `⋯` pada baris `Printer Epson L3250 {runId}`
23. Klik `Borrow Log`
24. Verifikasi node konfirmasi pada dialog Borrow Log dicatat `Confirmed by [PIC] on behalf of [Borrower]` dengan PIC `Nugroho Wibowo {runId}` dan Borrower `Dewi Anggraini`
