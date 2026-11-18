---
id: TC-FA-BORROW-BE-091-entitas-suspended-expired-server
title: "Server menolak aksi tulis Aktor saat entitas Suspended, Expired, atau Grace, dan job sistem tetap berjalan"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: ["EC-BRW-163", "F-BORROW-03.k10"]
smoke: []
dependsOn: []
owner: BE
trace:
  "EC-BRW-163": [5, 8, 9, 12, 14, 17, 20, 21, 24, 27, 28, 31, 33, 36, 37]
  "F-BORROW-03.k10": [8, 10, 20, 22, 27]
---

# Server menolak aksi tulis Aktor saat entitas Suspended, Expired, atau Grace, dan job sistem tetap berjalan

## Prerequisites
- Aktor:
  - Principal, operator di luar tenant yang mengubah status entitas DU-091-1 dan mengaktifkannya kembali.
  - Asset Admin DU-091-2, Group penugasan Head Office.
  - Borrower DU-091-3, punya akun login.
- Data:
  - DU-091-1: Entitas, Entitas khusus spec ini dengan status yang diubah Principal; Entity Name `Entitas Status Borrow {runId}`.
  - DU-091-2: User, Asset Admin pengaju, Group penugasan Head Office; Name `Intan Permatasari {runId}`; Role `Asset Admin`.
  - DU-091-3: User, Borrower yang punya akun login; Name `Reza Maulana {runId}`.
  - DU-091-4: Asset, aset yang pengajuannya ditolak saat entitas Suspended, Expired, dan Grace; Asset Name `Laptop Acer Swift 3 {runId}`; Group `Head Office`.
  - DU-091-5: Asset, aset Borrowed yang Return-nya ditolak lalu dicatat setelah entitas aktif; Asset Name `Kamera Nikon Z6 II {runId}`; Group `Head Office`.
  - DU-091-6: Asset, aset Waiting for Handover untuk uji Handover dan bulk Cancel Borrow yang ditolak; Asset Name `Proyektor ViewSonic PA503S {runId}`; Group `Head Office`.
  - DU-091-7: Parameter pengajuan status entitas, Duration dan Purpose pengajuan satuan Days; Duration `4 Day(s)`; Purpose `Pemakaian lapangan {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus DU-091-1 yang tidak dipakai spec lain.
  - Entitas DU-091-1 awalnya aktif dengan plan slot `paid_1` dan Approval Workflow tidak aktif.
  - Seluruh aset DU-091 berstatus `Available` dan tidak dipakai transaksi lain sebelum spec dimulai.

## Test Steps

### Baris disiapkan saat entitas aktif
1. Asset Admin DU-091-2 mengajukan BRW untuk aset DU-091-5 atas nama Borrower DU-091-3 dengan Duration `4 Day(s)` dan Purpose `Pemakaian lapangan {runId}`
2. Asset Admin DU-091-2 menyerahkan aset DU-091-5 kepada Borrower DU-091-3 dengan Condition `Normal`
3. Borrower DU-091-3 mengonfirmasi handover aset DU-091-5
4. Asset Admin DU-091-2 mengajukan BRW untuk aset DU-091-6 atas nama Borrower DU-091-3 dengan Duration `4 Day(s)` dan Purpose `Pemakaian lapangan {runId}`
5. Verifikasi aset DU-091-5 berstatus `Borrowed` dan aset DU-091-6 berstatus `Waiting for Handover` sebelum entitas diubah statusnya

### Aksi tulis ditolak saat entitas Suspended dan job sistem tetap berjalan
6. Principal menetapkan status entitas DU-091-1 menjadi Suspended
7. Asset Admin DU-091-2 mengajukan BRW untuk aset DU-091-4 atas nama Borrower DU-091-3 dengan Duration `4 Day(s)` dan Purpose `Pemakaian lapangan {runId}`
8. Verifikasi pengajuan BRW aset DU-091-4 ditolak server saat entitas Suspended
9. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil dan bukan toast `You don't have permission to do this.`
10. Verifikasi Borrow Log aset DU-091-4 tidak memuat node `Borrow requested by [Actor]` dan tidak ada baris baru untuk aset DU-091-4
11. Asset Admin DU-091-2 menyerahkan aset DU-091-6 kepada Borrower DU-091-3 dengan Condition `Normal`
12. Verifikasi aksi domain Handover aset DU-091-6 ditolak server dan baris tetap `Waiting for Handover`
13. Asset Admin DU-091-2 menerima kembali aset DU-091-5 dengan Condition `Normal`
14. Verifikasi Return aset DU-091-5 ditolak server saat entitas Suspended dan baris tetap `Borrowed`
15. Waktu berlalu sampai 1 hari sesudah Due date aset DU-091-5
16. Job Overdue berjalan
17. Verifikasi job sistem tidak diblokir dan baris aset DU-091-5 berstatus `Overdue`

### Aksi tulis ditolak saat entitas Expired
18. Principal menetapkan status entitas DU-091-1 menjadi Expired
19. Asset Admin DU-091-2 mengajukan BRW untuk aset DU-091-4 atas nama Borrower DU-091-3 dengan Duration `4 Day(s)` dan Purpose `Pemakaian lapangan {runId}`
20. Verifikasi pengajuan BRW aset DU-091-4 ditolak server saat entitas Expired
21. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil dan bukan toast `You don't have permission to do this.`
22. Verifikasi Borrow Log aset DU-091-4 tetap tidak memuat node `Borrow requested by [Actor]`
23. Asset Admin DU-091-2 menerima kembali aset DU-091-5 dengan Condition `Normal`
24. Verifikasi Return aset DU-091-5 ditolak server saat entitas Expired dan baris tetap `Overdue`

### Aksi tulis termasuk bulk ditolak saat entitas Grace
25. Principal menetapkan status entitas DU-091-1 menjadi Grace setelah Expired
26. Asset Admin DU-091-2 mengajukan BRW untuk aset DU-091-4 atas nama Borrower DU-091-3 dengan Duration `4 Day(s)` dan Purpose `Pemakaian lapangan {runId}`
27. Verifikasi pengajuan BRW aset DU-091-4 ditolak server saat entitas Grace
28. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil dan bukan toast `You don't have permission to do this.`
29. Asset Admin DU-091-2 memilih baris aset DU-091-6 dan aset DU-091-5
30. Asset Admin DU-091-2 menjalankan bulk Cancel Borrow atas kedua baris
31. Verifikasi bulk Cancel Borrow ditolak server dan baris aset DU-091-6 tetap `Waiting for Handover` serta baris aset DU-091-5 tetap `Overdue`
32. Asset Admin DU-091-2 menerima kembali aset DU-091-5 dengan Condition `Normal`
33. Verifikasi Return aset DU-091-5 ditolak server saat entitas Grace

### Return dapat dicatat setelah entitas aktif kembali
34. Principal mengaktifkan kembali entitas DU-091-1 lewat Renew Subscription
35. Asset Admin DU-091-2 menerima kembali aset DU-091-5 dengan Condition `Normal`
36. Verifikasi Return aset DU-091-5 dicatat dan baris berstatus `Returned`
37. Verifikasi node `Returned to [Receiver]` untuk aset DU-091-5 tercatat dengan penerima Asset Admin DU-091-2
