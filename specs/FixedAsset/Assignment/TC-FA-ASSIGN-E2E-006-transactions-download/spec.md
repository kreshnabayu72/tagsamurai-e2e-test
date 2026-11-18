---
id: TC-FA-ASSIGN-E2E-006-transactions-download
title: "Download CSV dan XLSX dari tab Transactions"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#r7", F-ASSIGN-13, "EB-DL-1@tabel-transactions", "EB-DL-2@tabel-transactions", "EB-DL-3@tabel-transactions", EB-DL-4, "EB-FB-2@download-transactions", "§9.6#r17"]
smoke: []
dependsOn: []
trace:
  "§5#r7": [3, 28, 31, 34, 49]
  F-ASSIGN-13: [5, 47]
  "EB-DL-1@tabel-transactions": [6, 15, 21, 38, 39, 44, 47]
  "EB-DL-2@tabel-transactions": 7
  "EB-DL-3@tabel-transactions": [5, 10]
  EB-DL-4: [5, 10]
  "EB-FB-2@download-transactions": 7
  "§9.6#r17": 5
anchor: [1, 12, 18, 25, 30]
coverage:
  web: automated
---

# Download CSV dan XLSX dari tab Transactions

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}` pada entitas khusus `Entitas Unduh {runId}`.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-006-1: Entitas khusus `Entitas Unduh {runId}`, tidak dipakai spec lain; daftar Transactions-nya hanya berisi 12 ASG pada entri DU-006-7 dan DU-006-8; Draft DU-006-13 dan ASG selesai DU-006-14 tidak ada di daftar itu.
  - DU-006-2: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-006-3: Group `Head Office {runId}`.
  - DU-006-4: User `Agus Prasetyo {runId}`, role Asset Admin pada Group `Head Office {runId}`; ia pengaju semua ASG.
  - DU-006-5: User `Dewi Anggraini {runId}`, karyawan aktif ber-akun login tanpa akses menu Assignment; PIC aktif semua Division di bawah.
  - DU-006-6: Division `Tim Cetak {runId}` dan sembilan Division `Tim Unduh {n} {runId}`.
  - DU-006-7: Tiga ASG berstatus `Assigned` untuk Assignee Division `Tim Cetak {runId}`, aset `Aset Cetak {n} {runId}`, Total Asset `1`.
  - DU-006-8: Sembilan ASG berstatus `Assigned` untuk Assignee Division `Tim Unduh {n} {runId}`, aset `Aset Unduh {n} {runId}`, Total Asset `1`; bersama entri sebelumnya jumlah ASG seluruh entitas tepat 12.
  - DU-006-13: Draft untuk Assignee Division `Tim Cetak {runId}`, Group `Head Office {runId}`, dengan aset `Proyektor Epson EB-X06 {runId}`; Draft tidak bernomor dan hanya ada di tab Drafts.
  - DU-006-14: ASG berstatus `Canceled` untuk Assignee Division `Tim Cetak {runId}`, Group `Head Office {runId}`, dengan aset `Printer Label Zebra ZD220 {runId}`; ASG sudah selesai sehingga hanya ada di tab History.

## Test Steps

### Unduh CSV dan XLSX tanpa saringan
1. Verifikasi halaman pertama tabel memuat tepat 10 baris dengan laporan `Showing 1 to 10 of 12`
2. Klik `Download`
3. Verifikasi overlay menawarkan `Download as CSV` dan `Download as XLSX`
4. Klik `Download as CSV`
5. Verifikasi berkas `Assignment-Transactions.csv` terunduh
6. Verifikasi berkas yang diunduh memuat 12 baris data walau tabel hanya menampilkan 10 baris per halaman
7. Verifikasi tidak ada toast sukses yang tampil sesudah unduhan berhasil
8. Klik `Download`
9. Klik `Download as XLSX`
10. Verifikasi berkas `Assignment-Transactions.xlsx` terunduh

### Unduh hasil Search
11. Ganti isi kotak search dengan `Tim Cetak {runId}`, tekan Enter
12. Verifikasi tabel memuat tepat 3 baris untuk Assignee `Tim Cetak {runId}`
13. Klik `Download`
14. Klik `Download as CSV`
15. Verifikasi berkas yang diunduh memuat tepat 3 baris data, semuanya untuk Assignee `Tim Cetak {runId}`

### Unduh tanpa kolom yang disembunyikan
16. Klik header kolom `Actions`
17. Hilangkan centang kolom `Group` pada panel Column Visibility
18. Verifikasi kolom `Group` tidak tampil di tabel
19. Klik `Download`
20. Klik `Download as CSV`
21. Verifikasi header berkas yang diunduh tidak memuat kolom `Group` dan tetap memuat kolom `Transaction ID`

### Unduh mengikuti Sort aktif
22. Klik `(←)` pada kotak Search
23. Klik header kolom `Assignee`
24. Klik header kolom `Assignee` sekali lagi
25. Verifikasi tabel terurut Z-A pada kolom `Assignee` dengan baris `Tim Cetak {runId}` berada di bagian akhir
26. Klik `Download`
27. Klik `Download as CSV`
28. Verifikasi baris data terakhir berkas yang diunduh berisi Assignee `Tim Cetak {runId}` sesuai urutan tabel

### Unduh saat hasil nol baris
29. Ganti isi kotak search dengan `{runId} tidakada`, tekan Enter
30. Verifikasi pesan `No results found` tampil
31. Verifikasi tombol `Download` tetap aktif
32. Klik `Download`
33. Klik `Download as CSV`
34. Verifikasi berkas yang diunduh hanya memuat baris header kolom yang tampil, tanpa baris data dan tanpa toast

### Unduhan tanpa saringan tidak memuat Draft maupun ASG selesai
35. Klik `(←)` pada kotak Search
36. Klik `Download`
37. Klik `Download as CSV`
38. Verifikasi berkas yang diunduh memuat 12 baris data
39. Verifikasi berkas yang diunduh tidak memuat aset `Proyektor Epson EB-X06 {runId}` milik Draft dan tidak memuat aset `Printer Label Zebra ZD220 {runId}` milik ASG `Canceled`

### Unduh hasil Filter Panel
40. Klik `Filter`
41. Klik field `Assignee`
42. Pilih opsi `Tim Cetak {runId}` pada field `Assignee`
43. Klik `[Apply]`
44. Verifikasi tabel memuat tepat 3 baris untuk Assignee `Tim Cetak {runId}`
45. Klik `Download`
46. Klik `Download as CSV`
47. Verifikasi berkas yang diunduh memuat tepat 3 baris data, semuanya untuk Assignee `Tim Cetak {runId}`

### Tooltip tombol toolbar unduh
48. Arahkan kursor ke tombol `Download`
49. Verifikasi tombol `Download` menampilkan tooltip `Download`


