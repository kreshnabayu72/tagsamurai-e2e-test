---
id: TC-FA-ASSIGN-E2E-042-pemisahan-peran-handover-dan-unassign
title: "Aktor yang juga Assignee atau PIC tidak dapat Handover dan Unassign"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [EC-ASG-18, EC-ASG-75, FI-ASG-20, FI-ASG-63, FI-ASG-64, FI-ASG-65, FI-ASG-66, FI-ASG-67, ASSIGN-LOGIC-15b]
smoke: []
dependsOn: []
trace:
  EC-ASG-18: [4, 5]
  EC-ASG-75: [13, 14, 19]
  FI-ASG-20: [4, 13]
  FI-ASG-63: [25, 27]
  FI-ASG-64: [25, 26, 31]
  FI-ASG-65: [34, 44, 45, 51]
  FI-ASG-66: [42, 43]
  FI-ASG-67: [40, 41]
  ASSIGN-LOGIC-15b: [5, 7, 8, 14]
anchor: [30]
coverage:
  web: automated
---

# Aktor yang juga Assignee atau PIC tidak dapat Handover dan Unassign

## Prerequisites
- Aktor: Asset Admin `Hendra Kusuma` (Aktor Assignment) dengan cakupan Group `Head Office`, juga Assignee dan PIC pada ASG di bawah (sesi `Hendra Kusuma`). Asset Admin `Lina Marlina` dengan cakupan Group `Head Office` bekerja di sesi terpisah dan bukan Assignee maupun PIC pada ASG di bawah (sesi `Lina Marlina`).
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-042-1: User `Hendra Kusuma`, Asset Admin dengan cakupan Group `Head Office`, anggota aktif Division `Procurement` dengan akun login.
  - DU-042-2: User `Lina Marlina`, Asset Admin dengan cakupan Group `Head Office`, karyawan aktif dengan akun login.
  - DU-042-3: User `Rizky Aditya`, anggota aktif Division `Procurement` dengan akun login, PIC pada ASG DU-042-13 dan DU-042-15.
  - DU-042-4: User `Fajar Nugroho`, karyawan aktif dengan akun login, Assignee ASG DU-042-17.
  - DU-042-5: Division `Procurement`.
  - DU-042-6: Aset `Kalkulator Casio {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Waiting for Handover`.
  - DU-042-7: Aset `Mesin Hitung Uang {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-042-8: ASG dengan Assignee `Hendra Kusuma` (Employee), Group `Head Office`, memuat DU-042-6 dan DU-042-7, dengan Approval `Not required` dan Purpose `Perlengkapan kerja pribadi {runId}`.
  - DU-042-9: Aset `Printer Epson L3250 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Waiting for Handover`.
  - DU-042-10: Aset `Scanner Fujitsu {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-042-11: ASG dengan Assignee Division `Procurement`, PIC `Hendra Kusuma`, Group `Head Office`, memuat DU-042-9 dan DU-042-10, dengan Approval `Not required` dan Purpose `Peralatan kantor pengadaan {runId}`.
  - DU-042-12: Aset `Laptop Asus Vivobook {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-042-13: ASG dengan Assignee Division `Procurement`, PIC `Rizky Aditya`, Group `Head Office`, memuat DU-042-12, dengan Approval `Not required` dan Purpose `Laptop staf pengadaan {runId}`.
  - DU-042-14: Aset `Monitor Samsung 27 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-042-15: ASG dengan Assignee Division `Procurement`, PIC `Rizky Aditya`, Group `Head Office`, memuat DU-042-14, dengan Approval `Not required` dan Purpose `Monitor staf pengadaan {runId}`.
  - DU-042-16: Aset `Genset Honda 5KVA {runId}`, Group `Branch Surabaya`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-042-17: ASG dengan Assignee `Fajar Nugroho` (Employee), Group `Branch Surabaya`, memuat DU-042-16, dengan Approval `Not required` dan Purpose `Cadangan listrik gudang {runId}`.
- Kondisi:
  - Feature Suite Assignment pada level `Full`.
  - Photo at end bernilai `OFF`.
  - Akun `Hendra Kusuma` dan `Lina Marlina` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Hand Over dan Unassign disabled bagi Aktor yang menjadi Assignee
1. Ketik Search `Kalkulator Casio {runId}`, tekan Enter
2. Klik menu ⋯ pada baris ASG DU-042-8
3. Arahkan kursor ke aksi `Hand Over`
4. Verifikasi aksi `Hand Over` pada baris ASG DU-042-8 disabled
5. Verifikasi alasan `You can't hand over or receive your own assignment.` tersampaikan pada aksi `Hand Over` yang disabled
6. Arahkan kursor ke aksi `Unassign`
7. Verifikasi aksi `Unassign` pada baris ASG DU-042-8 disabled
8. Verifikasi alasan `You can't hand over or receive your own assignment.` tersampaikan pada aksi `Unassign` yang disabled
9. Tekan Esc untuk menutup menu ⋯

### Hand Over disabled bagi Aktor yang menjadi PIC Division
10. Ketik Search `Printer Epson L3250 {runId}`, tekan Enter
11. Klik menu ⋯ pada baris ASG DU-042-11
12. Arahkan kursor ke aksi `Hand Over`
13. Verifikasi aksi `Hand Over` pada baris ASG DU-042-11 disabled
14. Verifikasi alasan `You can't hand over or receive your own assignment.` tersampaikan pada aksi `Hand Over` yang disabled
15. Tekan Esc untuk menutup menu ⋯

### Aktor Assignment lain dapat memproses Hand Over
16. Di sesi `Lina Marlina`, buka halaman Transactions > Assignment, tab Transactions
17. Di sesi `Lina Marlina`, ketik Search `Printer Epson L3250 {runId}`, tekan Enter
18. Di sesi `Lina Marlina`, klik menu ⋯ pada baris ASG DU-042-11
19. Verifikasi di sesi `Lina Marlina`, aksi `Hand Over` aktif
20. Di sesi `Lina Marlina`, tekan Esc untuk menutup menu ⋯

### Halaman Unassign tidak memuat aset penugasan sendiri
21. Ketik Search `Laptop Asus Vivobook {runId}`, tekan Enter
22. Klik Transaction ID pada baris hasil pencarian
23. Klik tombol `[Unassign]` di bawah tabel Assets
24. Buka dropdown field `Assignee`
25. Verifikasi opsi `Procurement (Division)` dengan jumlah `2 assets` tampil
26. Verifikasi opsi `Hendra Kusuma (Employee)` tidak tampil
27. Verifikasi opsi `Fajar Nugroho (Employee)` tidak tampil
28. Tekan Esc untuk menutup dropdown
29. Klik `[+ Asset]`
30. Verifikasi dialog Select Asset memuat DU-042-14
31. Verifikasi dialog Select Asset tidak memuat DU-042-10
32. Centang baris `Monitor Samsung 27 {runId}`
33. Klik `[Select]`
34. Verifikasi kolom Verification DU-042-12 dan DU-042-14 menampilkan `Non TAG`

### Submit ditolak ketika aset daftar menjadi penugasan Aktor sendiri
35. Di sesi `Lina Marlina`, ketik Search `Monitor Samsung 27 {runId}`, tekan Enter
36. Di sesi `Lina Marlina`, klik `Change PIC` pada menu ⋯ baris ASG DU-042-15
37. Di sesi `Lina Marlina`, pilih baris `Hendra Kusuma` pada dialog `Select User`
38. Di sesi `Lina Marlina`, klik `[Select]`
39. Di sesi `Hendra Kusuma`, klik `[Submit]`
40. Verifikasi toast error `Error, you can't hand over or receive your own assignment.` tampil setelah `[Submit]` ditolak
41. Verifikasi toast tidak memiliki tombol aksi
42. Verifikasi baris DU-042-14 ditandai ⚠
43. Verifikasi alasan `You can't hand over or receive your own assignment.` tersampaikan pada ⚠ baris DU-042-14
44. Verifikasi daftar tetap memuat DU-042-12 dan DU-042-14
45. Verifikasi kolom Verification DU-042-12 dan DU-042-14 tetap menampilkan `Non TAG`
46. Klik `[Cancel]`
47. Klik `[Leave]` pada dialog Unsaved Changes
48. Buka halaman Transactions > Assignment, tab Transactions
49. Ketik Search `Laptop Asus Vivobook {runId}`, tekan Enter
50. Klik Transaction ID pada baris hasil pencarian
51. Verifikasi kolom Status DU-042-12 menampilkan `Assigned`
