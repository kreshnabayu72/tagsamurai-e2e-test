---
id: TC-FA-MYASSET-E2E-036-tab-task-isi-dan-toolbar-dep-borrow
title: "Tab Task pada data nyata: satu baris per BRW, nilai kolom, urutan default, Search, dan nama berkas Download"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["T-MYA-01", "§1.2#r10", "§1.2#r20", "§5#r4", "§5#r6", "§9.2#b1", "§9.4.2#r1", "§10#r3", "EB-SRC-5@tabel-task"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "T-MYA-01": [9, 10, 11, 12, 13, 14, 16, 17, 18, 20, 22, 24, 26, 28, 30]
  "§1.2#r10": 8
  "§1.2#r20": 7
  "§5#r4": 9
  "§5#r6": 46
  "§9.2#b1": [8, 13]
  "§9.4.2#r1": 7
  "§10#r3": 8
  "EB-SRC-5@tabel-task": [32, 37, 42]
anchor: []
coverage:
  web: automated
---

# Tab Task pada data nyata: satu baris per BRW, nilai kolom, urutan default, Search, dan nama berkas Download

## Prerequisites
- Aktor: Borrower `Indra Kusuma {runId}`, pengguna karyawan ber-akun login tanpa role admin. Aktor Borrow `Rina Wulandari {runId}` dan `Bagus Santoso {runId}` memicu sesi Handover (LK-8); spec ini hanya membaca layar `Indra Kusuma {runId}` dan tidak mengonfirmasi Task.
- Layar awal: halaman Fixed Asset (FAMS) dengan navbar.
- Data:
  - DU-036-1: User `Indra Kusuma {runId}`, tanpa role admin, cakupan Group `Head Office`, dengan flag Guided Tooltip My Asset sudah disetel (tur sudah pernah dilihat).
  - DU-036-2: User `Rina Wulandari {runId}`, role Asset Admin dengan hak Aktor Borrow, cakupan Group `Head Office`.
  - DU-036-3: User `Bagus Santoso {runId}`, role Asset Admin dengan hak Aktor Borrow, cakupan Group `Head Office`.
  - DU-036-4: User `Agus Prasetyo {runId}`, tanpa role admin, cakupan Group `Head Office`.
  - DU-036-5: 4 aset `Laptop Kantor {n} {runId}` dengan n dari 1 sampai 4, Status `Waiting for Handover`, dalam satu pinjaman Admin atas nama `Indra Kusuma {runId}`, Group `Head Office`.
  - DU-036-6: aset `Tablet Wacom {runId}` dalam pinjaman yang sama dengan DU-036-5, Status `Waiting for Approval`, tidak ikut sesi Handover.
  - DU-036-7: aset `Printer Canon G3010 {runId}` dalam satu pinjaman Admin atas nama `Indra Kusuma {runId}`, Group `Head Office`, Status `Waiting for Handover`.
  - DU-036-8: 2 aset `Kursi Kerja {n} {runId}` dengan n dari 1 sampai 2, Status `Waiting for Handover`, dalam satu pinjaman Admin atas nama `Indra Kusuma {runId}`, Group `Head Office`.
  - DU-036-9: aset `Proyektor BenQ {runId}` dalam satu pinjaman Admin atas nama `Agus Prasetyo {runId}`, Group `Head Office`, Status `Waiting for Handover`.
  - DU-036-10: sesi Handover pinjaman DU-036-5 dan DU-036-6, dimulai `Rina Wulandari {runId}` lebih dulu daripada sesi DU-036-11, dengan Total Asset `4`.
  - DU-036-11: sesi Handover pinjaman DU-036-7, dimulai `Bagus Santoso {runId}` lebih dulu daripada sesi DU-036-12, dengan Total Asset `1`.
  - DU-036-12: sesi Handover pinjaman DU-036-8, dimulai `Rina Wulandari {runId}`, dengan Total Asset `2`.
  - DU-036-13: sesi Handover pinjaman DU-036-9, dimulai `Rina Wulandari {runId}`, milik `Agus Prasetyo {runId}`.
  - Kata kunci Search: DU-036-14 `Bagus`, DU-036-15 `Confirm Handover`, DU-036-16 `4`, DU-036-17 tanggal hari ini berformat `dd/MM/yy`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24 jam`.
  - Tidak ada sesi Handover aktif pada pinjaman `Indra Kusuma {runId}` sebelum langkah pertama.
  - Sesudah langkah 4, tab Task `Indra Kusuma {runId}` hanya berisi 3 baris Task: satu per pinjaman DU-036-5, DU-036-7, dan DU-036-8.

## Test Steps

### Tab awal Task memuat satu baris per pinjaman milik pengguna
1. Aktor Borrow `Rina Wulandari {runId}` memulai sesi Handover untuk pinjaman DU-036-5 yang memuat 4 aset Waiting for Handover
2. Aktor Borrow `Bagus Santoso {runId}` memulai sesi Handover untuk pinjaman DU-036-7
3. Aktor Borrow `Rina Wulandari {runId}` memulai sesi Handover untuk pinjaman DU-036-8
4. Aktor Borrow `Rina Wulandari {runId}` memulai sesi Handover untuk pinjaman DU-036-9 milik `Agus Prasetyo {runId}`
5. Klik avatar di navbar untuk membuka menu profil
6. Klik `My Asset`
7. Verifikasi tab `Task` terbuka sebagai tab awal
8. Verifikasi tabel Task memuat 3 baris, satu baris per pinjaman milik pengguna

### Nilai kolom tab Task dari data nyata dan urutan default
9. Verifikasi baris tampil dari atas ke bawah: baris yang Total Asset-nya `4`, baris yang Total Asset-nya `1`, lalu baris yang Total Asset-nya `2`, menurut Expires At terdekat
10. Verifikasi kolom Transaction ID baris yang Total Asset-nya `4` berformat `BRW-YYYY-NNNN`
11. Verifikasi kolom Task baris yang Total Asset-nya `4` bernilai `Confirm Handover`
12. Verifikasi kolom Group baris yang Total Asset-nya `4` bernilai `Head Office`
13. Verifikasi kolom Total Asset baris yang Total Asset-nya `4` bernilai `4`, tanpa menghitung aset `Tablet Wacom {runId}` yang masih Waiting for Approval
14. Verifikasi kolom Handed Over By baris yang Total Asset-nya `4` bernilai `Rina W`
15. Arahkan kursor ke nilai kolom Handed Over By baris yang Total Asset-nya `4`
16. Verifikasi tooltip bertuliskan nama lengkap `Rina Wulandari {runId}`
17. Verifikasi kolom Handed Over By baris yang Total Asset-nya `1` bernilai `Bagus S`
18. Verifikasi kolom Expires At baris yang Total Asset-nya `4` menampilkan tanggal berformat `dd/MM/yy` beserta jam 24 jam

### Aksi baris dan toolbar tabel Task
19. Klik `⋯` pada baris yang Total Asset-nya `4`
20. Verifikasi menu baris memuat `Confirm Handover`
21. Tekan `Esc` untuk menutup menu baris
22. Verifikasi ikon `Download`, `Filter`, dan `Search` tampil di toolbar tab Task

### Search per kelas kolom, kolom tanggal, dan kolom tersembunyi
23. Ketik Search `Bagus`, tekan Enter
24. Verifikasi tabel hanya memuat baris yang Total Asset-nya `1` karena kolom Handed Over By cocok dengan kata kunci
25. Ganti isi kotak search dengan `Confirm Handover`, tekan Enter
26. Verifikasi tabel memuat 3 baris karena badge kolom Task cocok dengan kata kunci
27. Ganti isi kotak search dengan `4`, tekan Enter
28. Verifikasi baris yang Total Asset-nya `4` tampil karena kolom Total Asset cocok dengan kata kunci
29. Ganti isi kotak search dengan tanggal hari ini berformat `dd/MM/yy`, tekan Enter
30. Verifikasi empty state `No results found` tampil karena kolom Expires At tidak ikut dicari
31. Ganti isi kotak search dengan `Bagus`, tekan Enter
32. Verifikasi baris yang Total Asset-nya `1` tampil sebelum kolom `Handed Over By` disembunyikan
33. Klik header kolom Actions `⋯` untuk membuka Column Visibility
34. Hapus centang kolom `Handed Over By`
35. Tekan `Esc` untuk menutup Column Visibility
36. Ganti isi kotak search dengan `Bagus`, tekan Enter
37. Verifikasi empty state `No results found` tampil karena kolom `Handed Over By` tersembunyi
38. Klik header kolom Actions `⋯` untuk membuka Column Visibility
39. Centang kolom `Handed Over By`
40. Tekan `Esc` untuk menutup Column Visibility
41. Ganti isi kotak search dengan `Bagus`, tekan Enter
42. Verifikasi baris yang Total Asset-nya `1` tampil kembali setelah kolom `Handed Over By` ditampilkan
43. Klik `(←)` pada kotak Search

### Nama berkas Download tab Task
44. Klik ikon `Download` pada toolbar
45. Klik `Download as CSV`
46. Verifikasi berkas `My-Asset-Task.csv` terunduh
