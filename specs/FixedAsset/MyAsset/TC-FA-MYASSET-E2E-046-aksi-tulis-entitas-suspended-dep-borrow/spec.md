---
id: TC-FA-MYASSET-E2E-046-aksi-tulis-entitas-suspended-dep-borrow
title: "Entitas Suspended: aksi tulis pinjaman di My Asset ditolak dan baris tetap tampil"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.4.1#r1", "§9.4.2#r79", "§9.4.2#r80", "EB-AKS-7"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§9.4.1#r1": [8, 9, 15, 16, 21, 24, 28, 29, 36, 37, 42, 43, 48, 49, 54, 55, 60, 64]
  "§9.4.2#r79": [8, 15, 21, 28, 36, 42, 48, 54, 60]
  "§9.4.2#r80": [9, 16, 24, 29, 37, 43, 49, 55, 64]
  "EB-AKS-7": [3, 4, 8, 9, 15, 16, 21, 24, 28, 29, 36, 37, 42, 43, 48, 49, 54, 55, 60, 64]
anchor: []
coverage:
  web: automated
---

# Entitas Suspended: aksi tulis pinjaman di My Asset ditolak dan baris tetap tampil

## Prerequisites
- Aktor: Borrower `Ratna Kusumawati {runId}` (DU-046-1). Aktor lain yang memicu perubahan: Operator Admin Console, yang mengubah status entitas aktor menjadi Suspended sesudah baris-baris di bawah terbentuk.
- Layar awal: halaman masuk Fixed Asset.
- Data:
  - DU-046-1: pengguna `Ratna Kusumawati {runId}`, role `Read Only`, Group `Head Office`.
  - DU-046-2: pinjaman aset `Scanner Epson DS-530 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Source `Admin`, Borrower `Me`. Task `Confirm Handover` dengan Total Asset `1`.
  - DU-046-3: pinjaman aset `Kamera Nikon Z30 {runId}`, Group `Head Office`, Status `Waiting for Approval`, Source `Admin`, Borrower `Me`.
  - DU-046-4: pinjaman aset `Laptop Dell Inspiron 15 {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Me`.
  - DU-046-5: pinjaman aset `Tablet iPad 10 {runId}`, Group `Head Office`, Status `Extension Request`, Source `Admin`, Borrower `Me`. Pengajuan Extend diajukan aktor dan menunggu review Aktor Borrow.
  - DU-046-6: pinjaman aset `Monitor Samsung S24 {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Me`.
  - DU-046-7: pinjaman aset `Speaker JBL Charge 5 {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Me`.
  - DU-046-8: pinjaman aset `Mikrofon Rode NT-USB {runId}`, Group `Head Office`, Status `Borrowed`, badge `Reported Damaged`, Source `Admin`, Borrower `Me`. Damage Report diajukan aktor dan berstatus `Waiting for Confirmation`.
  - DU-046-9: pinjaman aset `Tripod Benro T660 {runId}`, Group `Head Office`, Status `Borrowed`, badge `Reported Missing`, Source `Admin`, Borrower `Me`. Laporan Missing diajukan aktor dan berstatus `Waiting for Confirmation`.
  - DU-046-10: pinjaman aset `Proyektor Epson EB-E01 {runId}`, Group `Head Office`, Status `Borrowed`, Source `Self-service`, Borrower `Me`.
  - DU-046-11: isian Report Damaged: Damaged Photo `damaged-monitor-046.jpg`, What happened `Layar retak setelah terjatuh dari meja`.
- Kondisi:
  - Spec ini memakai entitas khusus berstatus Suspended yang tidak dipakai spec lain.
  - Entitas aktor berstatus Suspended. Seluruh baris DU-046-2 sampai DU-046-10 terbentuk sebelum entitas di-Suspend.
  - Tab Borrowed aktor memuat 9 baris, yaitu DU-046-2 sampai DU-046-10. Tab Task aktor memuat 1 baris, yaitu DU-046-2.
  - Halaman Extension Request untuk `Laptop Dell Inspiron 15 {runId}` terisi bawaan dengan isian valid, sehingga `[Submit Request]` tidak ditolak validasi klien.
  - Dialog `Report Missing` untuk `Speaker JBL Charge 5 {runId}` tidak memuat field wajib yang kosong, sehingga `[Report Missing]` tidak ditolak validasi klien.
  - Halaman Return untuk `Proyektor Epson EB-E01 {runId}` terisi otomatis dengan Borrower `Ratna Kusumawati {runId}` dan aset `Proyektor Epson EB-E01 {runId}`, tanpa isian wajib yang kosong, sehingga pengiriman Return tidak ditolak validasi klien.

## Test Steps

### Produk tetap terbuka dan data terbaca pada entitas Suspended
1. Masuk sebagai `Ratna Kusumawati {runId}`
2. Buka `My Asset` dari menu profil pada navbar
3. Verifikasi tab `Task`, `Borrowed`, `Assigned`, dan `History` tampil
4. Verifikasi baris Task `Confirm Handover` untuk pinjaman DU-046-2 tampil

### Confirm Handover ditolak dan baris Task tetap tampil
5. Buka menu `⋯` pada baris Task `Confirm Handover` untuk pinjaman DU-046-2
6. Klik `Confirm Handover`
7. Klik `[Confirm]`
8. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
9. Verifikasi baris Task `Confirm Handover` untuk pinjaman DU-046-2 tetap tampil
10. Tutup toast

### Cancel Borrow ditolak dan baris tetap Waiting for Approval
11. Klik tab `Borrowed`
12. Buka menu `⋯` pada baris `Kamera Nikon Z30 {runId}`
13. Klik `Cancel Borrow`
14. Klik `[Cancel Borrow]` pada dialog `Cancel Borrow`
15. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
16. Verifikasi baris `Kamera Nikon Z30 {runId}` tetap tampil dengan Status `Waiting for Approval`
17. Tutup toast

### Request Extension ditolak dan baris tetap Borrowed
18. Buka menu `⋯` pada baris `Laptop Dell Inspiron 15 {runId}`
19. Klik `Request Extension`
20. Klik `[Submit Request]` dengan isian halaman Extension Request yang terisi bawaan dan valid
21. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
22. Tutup toast
23. Klik breadcrumb `Borrowed`
24. Verifikasi baris `Laptop Dell Inspiron 15 {runId}` tetap tampil dengan Status `Borrowed`

### Cancel Extension Request ditolak dan baris tetap Extension Request
25. Buka menu `⋯` pada baris `Tablet iPad 10 {runId}`
26. Klik `Cancel Extension Request`
27. Klik `[Cancel Extension]` pada dialog `Cancel Extension`
28. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
29. Verifikasi baris `Tablet iPad 10 {runId}` tetap tampil dengan Status `Extension Request`
30. Tutup toast

### Report Damaged ditolak dan baris tetap Borrowed
31. Buka menu `⋯` pada baris `Monitor Samsung S24 {runId}`
32. Klik `Report Damaged`
33. Unggah Damaged Photo `damaged-monitor-046.jpg`
34. Isi What happened dengan `Layar retak setelah terjatuh dari meja`
35. Klik `[Report Damaged]`
36. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
37. Verifikasi baris `Monitor Samsung S24 {runId}` tetap tampil dengan Status `Borrowed`
38. Tutup toast

### Report Missing ditolak dan baris tetap Borrowed
39. Buka menu `⋯` pada baris `Speaker JBL Charge 5 {runId}`
40. Klik `Report Missing`
41. Klik `[Report Missing]`
42. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
43. Verifikasi baris `Speaker JBL Charge 5 {runId}` tetap tampil dengan Status `Borrowed`
44. Tutup toast

### Cancel Damage Report ditolak dan badge Reported Damaged tetap tampil
45. Buka menu `⋯` pada baris `Mikrofon Rode NT-USB {runId}`
46. Klik `Cancel Damage Report`
47. Konfirmasi pembatalan pada dialog `Cancel Report`
48. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
49. Verifikasi baris `Mikrofon Rode NT-USB {runId}` tetap tampil dengan badge `Reported Damaged`
50. Tutup toast

### Cancel Missing Report ditolak dan badge Reported Missing tetap tampil
51. Buka menu `⋯` pada baris `Tripod Benro T660 {runId}`
52. Klik `Cancel Missing Report`
53. Konfirmasi pembatalan pada dialog `Cancel Report`
54. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
55. Verifikasi baris `Tripod Benro T660 {runId}` tetap tampil dengan badge `Reported Missing`
56. Tutup toast

### Return ditolak dan baris pinjaman Self-service tetap Borrowed
57. Buka menu `⋯` pada baris `Proyektor Epson EB-E01 {runId}`
58. Klik `Return`
59. Kirim Return dari halaman Return dengan Borrower dan aset `Proyektor Epson EB-E01 {runId}` yang terisi otomatis, tanpa mengubah isian
60. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
61. Tutup toast
62. Buka `My Asset` dari menu profil pada navbar
63. Klik tab `Borrowed`
64. Verifikasi baris `Proyektor Epson EB-E01 {runId}` tetap tampil dengan Status `Borrowed`
