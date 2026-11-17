---
id: TC-FA-MYASSET-E2E-046-aksi-tulis-entitas-suspended-dep-borrow
title: "Entitas Suspended: aksi tulis pinjaman di My Asset ditolak dan baris tetap tampil"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["§9.4.1#r1", "§9.4.2#r79", "§9.4.2#r80", "EB-AKS-7"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§9.4.1#r1": [8, 15, 21, 28, 36, 43, 49, 55, 61, 9, 16, 24, 29, 37, 44, 50, 56, 65]
  "§9.4.2#r79": [8, 15, 21, 28, 36, 43, 49, 55, 61]
  "§9.4.2#r80": [9, 16, 24, 29, 37, 44, 50, 56, 65]
  "EB-AKS-7": [3, 4, 8, 15, 21, 28, 36, 43, 49, 55, 61, 9, 16, 24, 29, 37, 44, 50, 56, 65]
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
20. Klik `[Submit Request]`
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
41. Isi seluruh field wajib pada dialog `Report Missing`
42. Klik `[Report Missing]`
43. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
44. Verifikasi baris `Speaker JBL Charge 5 {runId}` tetap tampil dengan Status `Borrowed`
45. Tutup toast

### Cancel Damage Report ditolak dan badge Reported Damaged tetap tampil
46. Buka menu `⋯` pada baris `Mikrofon Rode NT-USB {runId}`
47. Klik `Cancel Damage Report`
48. Konfirmasi pembatalan pada dialog `Cancel Report`
49. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
50. Verifikasi baris `Mikrofon Rode NT-USB {runId}` tetap tampil dengan badge `Reported Damaged`
51. Tutup toast

### Cancel Missing Report ditolak dan badge Reported Missing tetap tampil
52. Buka menu `⋯` pada baris `Tripod Benro T660 {runId}`
53. Klik `Cancel Missing Report`
54. Konfirmasi pembatalan pada dialog `Cancel Report`
55. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
56. Verifikasi baris `Tripod Benro T660 {runId}` tetap tampil dengan badge `Reported Missing`
57. Tutup toast

### Return ditolak dan baris pinjaman Self-service tetap Borrowed
58. Buka menu `⋯` pada baris `Proyektor Epson EB-E01 {runId}`
59. Klik `Return`
60. Kirim Return dari halaman Return
61. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
62. Tutup toast
63. Buka `My Asset` dari menu profil pada navbar
64. Klik tab `Borrowed`
65. Verifikasi baris `Proyektor Epson EB-E01 {runId}` tetap tampil dengan Status `Borrowed`
