---
id: TC-FA-MYASSET-E2E-042-peran-lain-sebagai-borrower-dep-borrow
title: "Pengguna ber-role admin sebagai Borrower: hanya pinjamannya sendiri dan aksi mengikuti posisi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§1.2#r26", "§2.1#b4", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r11", "§4.8#r13", "§9.4.2#r12", "EB-AKS-4"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§1.2#r26": [9, 10]
  "§2.1#b4": [11, 18]
  "§4.8#r1": 3
  "§4.8#r2": 4
  "§4.8#r3": 6
  "§4.8#r5": 17
  "§4.8#r6": 24
  "§4.8#r7": [14, 27]
  "§4.8#r8": 15
  "§4.8#r9": 16
  "§4.8#r11": 21
  "§4.8#r13": 13
  "§9.4.2#r12": [9, 10]
  "EB-AKS-4": [30, 33, 36, 37, 39]
anchor: []
coverage:
  web: automated
---

# Pengguna ber-role admin sebagai Borrower: hanya pinjamannya sendiri dan aksi mengikuti posisi

## Prerequisites
- Aktor: Asset Admin `Rahmat Hidayat {runId}` (DU-042-1), yang juga menjadi Borrower atas pinjamannya sendiri.
- Layar awal: halaman masuk Fixed Asset.
- Data:
  - DU-042-1: pengguna `Rahmat Hidayat {runId}`, role `Asset Admin`, Group `Head Office`.
  - DU-042-2: pengguna `Siska Amelia {runId}`, role `Read Only`, Group `Head Office`, Borrower lain di Group yang sama dengan aktor.
  - DU-042-3: pinjaman aset `Laptop Asus Vivobook {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Me`.
  - DU-042-4: pinjaman aset `Proyektor BenQ MW550 {runId}`, Group `Head Office`, Status `Borrowed`, Source `Self-service`, Borrower `Me`.
  - DU-042-5: pinjaman aset `Kamera Fujifilm X-T30 {runId}`, Group `Head Office`, Status `Waiting for Approval`, Source `Admin`, Borrower `Me`.
  - DU-042-6: pinjaman aset `Scanner Brother ADS-1700 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Source `Admin`, Borrower `Me`. Task `Confirm Handover` dengan Total Asset `1`.
  - DU-042-7: pinjaman aset `Printer Brother HL {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Siska Amelia {runId}`.
  - DU-042-8: pinjaman aset `Tablet Xiaomi Pad 6 {runId}`, Group `Head Office`, Status `Extension Request`, Source `Admin`, Borrower `Me`. Pengajuan Extend diajukan aktor dan menunggu review Aktor Borrow.
  - Teks laporan paginasi tabel Borrowed yang diharapkan `Showing 1 to 5 of 5`, dari `Showing {first} to {last} of {totalRecords}` dengan 5 baris milik aktor.
- Kondisi:
  - Tab Borrowed aktor memuat 5 baris, yaitu DU-042-3 sampai DU-042-6 dan DU-042-8. Pinjaman DU-042-7 milik Borrower lain tidak ikut.
  - Sesi Handover DU-042-6 menunggu konfirmasi dan jendela konfirmasinya belum habis. Tab Task aktor memuat 1 baris, yaitu DU-042-6.

## Test Steps

### Menu My Asset dan keempat tab tersedia bagi role Asset Admin
1. Masuk sebagai Asset Admin `Rahmat Hidayat {runId}`
2. Buka `My Asset` dari menu profil pada navbar
3. Verifikasi tab `Task`, `Borrowed`, `Assigned`, dan `History` tampil

### Tab Task memuat Task pinjaman milik aktor dengan aksi Confirm Handover
4. Verifikasi baris Task `Confirm Handover` untuk pinjaman DU-042-6 tampil
5. Buka menu `⋯` pada baris Task `Confirm Handover` untuk pinjaman DU-042-6
6. Verifikasi menu memuat `Confirm Handover`
7. Tutup menu `⋯` dengan Esc

### Tab Borrowed hanya memuat pinjaman milik aktor
8. Klik tab `Borrowed`
9. Verifikasi baris `Laptop Asus Vivobook {runId}`, `Proyektor BenQ MW550 {runId}`, `Kamera Fujifilm X-T30 {runId}`, `Scanner Brother ADS-1700 {runId}`, dan `Tablet Xiaomi Pad 6 {runId}` tampil
10. Verifikasi baris `Printer Brother HL {runId}` milik Borrower `Siska Amelia {runId}` tidak tampil
11. Verifikasi kolom `Borrower` pada baris `Laptop Asus Vivobook {runId}` berisi `Me`

### Aksi baris mengikuti posisi aktor sebagai Borrower
12. Buka menu `⋯` pada baris `Laptop Asus Vivobook {runId}`
13. Verifikasi menu memuat `Borrow Log`
14. Verifikasi menu memuat `Request Extension`
15. Verifikasi menu memuat `Report Damaged`
16. Verifikasi menu memuat `Report Missing`
17. Verifikasi menu tidak memuat `Unassign`
18. Verifikasi menu tidak memuat `Hand over` dan `Review`
19. Tutup menu `⋯` dengan Esc
20. Buka menu `⋯` pada baris `Proyektor BenQ MW550 {runId}`
21. Verifikasi menu memuat `Return`
22. Tutup menu `⋯` dengan Esc
23. Buka menu `⋯` pada baris `Kamera Fujifilm X-T30 {runId}`
24. Verifikasi menu memuat `Cancel Borrow`
25. Tutup menu `⋯` dengan Esc
26. Buka menu `⋯` pada baris `Tablet Xiaomi Pad 6 {runId}`
27. Verifikasi menu memuat `Cancel Extension Request`
28. Tutup menu `⋯` dengan Esc

### Search, Filter, Sort, Pagination, dan Setup Column tersedia dan aktif bagi aktor
29. Ketik Search `Laptop Asus Vivobook {runId}`, tekan Enter
30. Verifikasi baris `Laptop Asus Vivobook {runId}` tampil sebagai hasil Search
31. Klik `(←)` pada kotak Search
32. Klik ikon `Filter`
33. Verifikasi Filter Panel tampil dengan `[Clear Field]` dan `[Apply]`
34. Klik ulang ikon `Filter` untuk menutup Filter Panel
35. Klik header kolom `Name`
36. Verifikasi baris diurutkan menurut Name `Alphabetical (A–Z)`: baris pertama `Kamera Fujifilm X-T30 {runId}` dan baris terakhir `Tablet Xiaomi Pad 6 {runId}`
37. Verifikasi laporan paginasi `Showing 1 to 5 of 5` tampil
38. Klik `Column Visibility`
39. Verifikasi `Setup Columns` tampil
