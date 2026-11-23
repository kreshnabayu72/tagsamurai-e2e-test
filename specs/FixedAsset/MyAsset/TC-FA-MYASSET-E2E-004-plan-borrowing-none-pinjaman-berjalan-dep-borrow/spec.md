---
id: TC-FA-MYASSET-E2E-004-plan-borrowing-none-pinjaman-berjalan-dep-borrow
title: "Plan Borrowing None dengan pinjaman berjalan: tab Borrowed read-only, tanpa Task Confirm Handover (Borrow), item My Asset hilang setelah pinjaman terakhir selesai"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§4.3#r7", "§9.10#p1", "§9.4.2#r94", "§9.4.2#r95", "§9.4.2#r96"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§4.3#r7": 16
  "§9.10#p1": [3, 5, 6, 37, 39, 44]
  "§9.4.2#r94": [12, 16, 17, 21]
  "§9.4.2#r95": [25, 30]
  "§9.4.2#r96": 44
anchor: [8, 9, 11, 15, 20, 24, 27, 29, 43]
coverage:
  web: automated
---

# Plan Borrowing None dengan pinjaman berjalan: tab Borrowed read-only, tanpa Task Confirm Handover (Borrow), item My Asset hilang setelah pinjaman terakhir selesai

## Prerequisites
- Aktor: Borrower `Bambang Hartono {runId}` di entitas khusus dengan plan Borrowing `None` dan Assignment `None`; entitas ini tidak dipakai spec lain. Aktor lain yang memicu perubahan: Aktor Borrow `Rina Wulandari {runId}`, yang mengonfirmasi Handover dan melakukan Return pada langkah 32 sampai 34 dan langkah 40 (LK-8).
- Layar awal: halaman FAMS yang memuat navbar.
- Data:
  - DU-004-1: Entitas `Entitas Level None Pinjaman {runId}` dengan Borrowing level `None` dan Assignment level `None`; Borrowing dan Assignment tidak tersedia pada plan itu.
  - DU-004-2: User `Bambang Hartono {runId}`, Borrower aktif di entitas DU-004-1, tanpa role admin, cakupan Group `Head Office`, tanpa penugasan berjalan.
  - DU-004-3: User `Rina Wulandari {runId}`, Asset Admin dengan hak Aktor Borrow, cakupan Group `Head Office`, di entitas DU-004-1.
  - DU-004-4: pinjaman Admin atas nama `Bambang Hartono {runId}`, aset `Proyektor Epson EB-X06 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Duration `3 days`. Sesi Handover menunggu konfirmasi Borrower dan jendela konfirmasinya masih berlaku sampai langkah 32 selesai.
  - DU-004-5: pinjaman Admin atas nama `Bambang Hartono {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Status `Borrowed`, Duration `3 days`.
  - DU-004-6: pinjaman Self-service atas nama `Bambang Hartono {runId}`, aset `Meeting Mic Set {runId}`, Group `Head Office`, Status `Borrowed`, Duration `4 days`.
  - DU-004-7: pinjaman Admin atas nama `Bambang Hartono {runId}`, aset `Kamera Canon EOS 90D {runId}`, Group `Head Office`, Status `Returned`, Duration `2 days`.
- Kondisi:
  - Akun `Bambang Hartono {runId}` aktif dan kredensialnya disediakan fase 2.
  - Entitas aktor memakai plan dengan Borrowing None dan Assignment None. Pinjaman DU-004-4 sampai DU-004-6 sudah berjalan sebelum entitas diturunkan ke plan itu.
  - `Bambang Hartono {runId}` tidak punya penugasan berjalan dan tidak punya sesi Handover lain yang menunggu konfirmasinya selain DU-004-4.
  - Jendela konfirmasi sesi Handover DU-004-4 cukup panjang untuk seluruh langkah spec ini sampai langkah 32, sehingga tidak habis di tengah jalan.
  - Aktor Borrow dapat mengonfirmasi Handover dan melakukan Return atas pinjaman yang sudah berjalan pada plan itu.

## Test Steps

### Item My Asset tampil dan tab disusun menurut level None selama ada pinjaman berjalan
1. Masuk sebagai `Bambang Hartono {runId}`
2. Klik avatar di navbar untuk membuka menu profil
3. Verifikasi item `My Asset` tampil di menu profil
4. Klik `My Asset`
5. Verifikasi tab `Task`, `Borrowed`, dan `History` tampil
6. Verifikasi tab `Assigned` tidak tampil

### Tab Borrowed read-only: aksi baris tidak tampil
7. Klik tab `Borrowed`
8. Verifikasi baris `Proyektor Epson EB-X06 {runId}`, `Laptop Dell Latitude 5420 {runId}`, dan `Meeting Mic Set {runId}` tampil di tabel Borrowed
9. Verifikasi Status baris `Proyektor Epson EB-X06 {runId}` adalah `Waiting for Handover`
10. Klik `⋯` pada baris `Proyektor Epson EB-X06 {runId}`
11. Verifikasi menu baris `Proyektor Epson EB-X06 {runId}` memuat `Borrow Log`
12. Verifikasi `Cancel Borrow` tidak tampil di menu baris `Proyektor Epson EB-X06 {runId}`
13. Tekan `Esc` untuk menutup menu baris
14. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
15. Verifikasi menu baris `Laptop Dell Latitude 5420 {runId}` memuat `Borrow Log`
16. Verifikasi `Request Extension` tidak tampil di menu baris `Laptop Dell Latitude 5420 {runId}`
17. Verifikasi `Report Damaged` dan `Report Missing` tidak tampil di menu baris `Laptop Dell Latitude 5420 {runId}`
18. Tekan `Esc` untuk menutup menu baris
19. Klik `⋯` pada baris `Meeting Mic Set {runId}`
20. Verifikasi menu baris `Meeting Mic Set {runId}` memuat `Borrow Log`
21. Verifikasi `Return` tidak tampil di menu baris `Meeting Mic Set {runId}`
22. Tekan `Esc` untuk menutup menu baris

### Task Confirm Handover (Borrow) tidak ada
23. Klik tab `Task`
24. Verifikasi empty state `No tasks` tampil di tab Task
25. Verifikasi tidak ada baris Task `Confirm Handover` untuk pinjaman DU-004-4

### Tab History read-only
26. Klik tab `History`
27. Verifikasi baris `Kamera Canon EOS 90D {runId}` tampil di tab History dengan Status `Returned`
28. Klik `⋯` pada baris `Kamera Canon EOS 90D {runId}`
29. Verifikasi menu baris `Kamera Canon EOS 90D {runId}` memuat `Borrow Log`
30. Verifikasi `Return`, `Request Extension`, `Report Damaged`, `Report Missing`, dan `Cancel Borrow` tidak tampil di menu baris `Kamera Canon EOS 90D {runId}`
31. Tekan `Esc` untuk menutup menu baris

### Item My Asset dan alamat langsung tetap tersedia selama masih ada pinjaman berjalan
32. Aktor Borrow `Rina Wulandari {runId}` mengonfirmasi Handover pinjaman DU-004-4 lewat `Confirm on This Device` di perangkat admin
33. Aktor Borrow `Rina Wulandari {runId}` melakukan Return aset `Proyektor Epson EB-X06 {runId}` milik `Bambang Hartono {runId}`
34. Aktor Borrow `Rina Wulandari {runId}` melakukan Return aset `Laptop Dell Latitude 5420 {runId}` milik `Bambang Hartono {runId}`
35. Muat ulang halaman
36. Klik avatar di navbar untuk membuka menu profil
37. Verifikasi item `My Asset` tetap tampil di menu profil karena pinjaman `Meeting Mic Set {runId}` masih berjalan
38. Buka halaman My Asset lewat alamat langsung
39. Verifikasi halaman My Asset terbuka dan tidak ditolak, dengan tab `Borrowed` tampil karena pinjaman `Meeting Mic Set {runId}` masih berjalan

### Item My Asset hilang setelah pinjaman terakhir selesai
40. Aktor Borrow `Rina Wulandari {runId}` melakukan Return aset `Meeting Mic Set {runId}` milik `Bambang Hartono {runId}`
41. Muat ulang halaman
42. Klik avatar di navbar untuk membuka menu profil
43. Verifikasi menu profil `Bambang Hartono {runId}` memuat item akun lain
44. Verifikasi tidak ada item `My Asset` di menu profil karena Borrowing dan Assignment None dan tidak ada pinjaman maupun penugasan berjalan
