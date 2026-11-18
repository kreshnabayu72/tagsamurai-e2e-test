---
id: TC-FA-BORROW-E2E-042-transaction-log-aset-dep-asset-detail
title: "Transaction log aset di Asset Detail memuat peristiwa Borrow lintas transaksi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§8.1a#p1", "§8.1a#r1", "§8.1a#r2", "§8.1a#r3", "§8.1a#r4", "§8.1a#r5", "§8.1a#r6", "§8.1a#r7", "§8.1a#r8", "§8.1a#r9", "§8.1a#r10", "§8.1a#r11", "§8.1a#r12", "§8.1a#r13", "§8.1a#r14", "§8.1a#r15", "§8.1a#r16", "§8.1a#r17", "§8.1a#r18", "§8.1a#r19", "§8.1a#p4"]
smoke: []
dependsOn: ["Asset Detail: Transaction log"]
trace:
  "§8.1a#p1": [4, 20]
  "§8.1a#r1": 5
  "§8.1a#r2": 6
  "§8.1a#r3": 14
  "§8.1a#r4": 15
  "§8.1a#r5": 16
  "§8.1a#r6": [17, 34]
  "§8.1a#r7": [18, 35]
  "§8.1a#r8": [7, 32]
  "§8.1a#r9": 8
  "§8.1a#r10": 33
  "§8.1a#r11": 40
  "§8.1a#r12": 9
  "§8.1a#r13": [10, 55]
  "§8.1a#r14": [11, 56, 63]
  "§8.1a#r15": 12
  "§8.1a#r16": 45
  "§8.1a#r17": 50
  "§8.1a#r18": [13, 64]
  "§8.1a#r19": 58
  "§8.1a#p4": [23, 27]
anchor: [57]
coverage:
  web: automated
---

# Transaction log aset di Asset Detail memuat peristiwa Borrow lintas transaksi

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office`; ia hanya membaca Transaction log aset dan bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: daftar aset (Assets > All).
- Data:
  - DU-042-1: aset `Kamera Sony ZV-1 {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}` (punya akun login), tanpa PIC, dengan satu BRW (DU-042-8) yang riwayatnya berurutan dari paling awal: Requested, Approved, Handed over (scan lewat Handheld Reader `Handheld Zebra RFD40 {runId}`), Extension requested, Extended, Overdue, lalu Returned (scan lewat reader yang sama); tujuh baris log.
  - DU-042-2: aset `Proyektor Epson EB-X49 {runId}`, Group `Head Office`, Borrower karyawan tanpa akun login `Nico Prasetyo {runId}` dengan PIC `Rina Wijaya {runId}`, dengan satu BRW (DU-042-9) yang riwayatnya Requested, Approval rerouted, lalu Rejected; tiga baris log.
  - DU-042-3: aset `Gimbal DJI RS 3 {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`, dengan satu BRW (DU-042-10) yang riwayatnya Requested, Approved, lalu Canceled; tiga baris log.
  - DU-042-4: aset `Mikrofon Rode VideoMic {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`, dengan satu BRW (DU-042-11) yang riwayatnya Requested, Approved, Handed over, lalu Reported missing oleh Aktor Borrow yang memegang hak Aktor Missing; empat baris log.
  - DU-042-5: aset `Tablet Samsung Tab S9 {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`, dengan satu BRW (DU-042-12) yang riwayatnya Requested, Approved, Handed over, Extension requested, Extension forwarded, Extension rejected, Extension requested, Extension canceled, lalu Returned; di sela riwayat itu terjadi Damage reported, Damage report canceled, laporan kehilangan oleh Borrower, pembatalan laporan kehilangan, TAG reported, dan Handover not confirmed; sembilan baris log.
  - DU-042-6: aset `Printer Epson L5290 {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`, dengan satu BRW (DU-042-13) yang riwayatnya Requested, Approved, Handed over, Overdue, Extension requested, Extension rejected sesudah Due date, lalu Returned dengan penanda Damaged; tujuh baris log.
  - DU-042-7: aset `Speaker Bose S1 Pro {runId}`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`, dengan satu BRW (DU-042-14) yang riwayatnya Requested, Approved, Handed over, Reported missing oleh Borrower, lalu Missing confirmed oleh Aktor Missing; empat baris log.
  - DU-042-8: BRW `Returned` milik DU-042-1, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-9: BRW `Rejected` milik DU-042-2, Group `Head Office`, Borrower `Nico Prasetyo {runId}`, PIC `Rina Wijaya {runId}`.
  - DU-042-10: BRW `Canceled` milik DU-042-3, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-11: BRW `Returned` milik DU-042-4 dengan penanda `Missing`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-12: BRW `Returned` milik DU-042-5, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-13: BRW `Returned` milik DU-042-6 dengan penanda `Damaged`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
  - DU-042-14: BRW `Returned` milik DU-042-7 dengan penanda `Missing`, Group `Head Office`, Borrower `Oscar Wijaya {runId}`.
- Kondisi:
  - Date Format dan Time Format di General Settings entitas berlaku untuk tampilan tanggal dan waktu.

## Test Steps

### Kolom dan baris log satu aset dengan riwayat lengkap dari Requested sampai Returned
1. Ketik Search `Kamera Sony ZV-1 {runId}`, tekan Enter
2. Buka Asset Detail aset `Kamera Sony ZV-1 {runId}`
3. Klik tab `Transaction log`
4. Verifikasi log memuat tepat tujuh baris, satu per perubahan status baris aset pada BRW milik DU-042-8
5. Verifikasi kolom `Date` menampilkan waktu peristiwa dengan format Date Format dan Time Format General Settings
6. Verifikasi kolom `Transaction ID` memuat nomor BRW milik DU-042-8 sebagai tautan pada ketujuh baris
7. Verifikasi peristiwa Requested tercatat sebagai baris dengan Status `Waiting for Approval`
8. Verifikasi peristiwa Approved tercatat sebagai baris dengan Status `Waiting for Handover`
9. Verifikasi peristiwa Handed over tercatat sebagai baris dengan Status `Borrowed`
10. Verifikasi peristiwa Extension requested tercatat sebagai baris dengan Status `Extension Request`
11. Verifikasi peristiwa Extended tercatat sebagai baris dengan Status `Borrowed`
12. Verifikasi peristiwa Overdue tercatat sebagai baris dengan Status `Overdue`
13. Verifikasi peristiwa Returned tercatat sebagai baris dengan Status `Returned`
14. Verifikasi kolom `Status` pada baris `Returned` tampil sebagai teks biasa tanpa badge
15. Verifikasi kolom `Reader name` berisi `Handheld Zebra RFD40 {runId}` pada baris Handed over dan baris Returned, serta `—` pada baris lain
16. Verifikasi kolom `Group` berisi `Head Office` pada ketujuh baris
17. Verifikasi kolom `PIC` berisi `—` pada ketujuh baris karena Borrower punya akun login
18. Verifikasi kolom `Borrower` berisi `Oscar Wijaya {runId}` pada ketujuh baris

### Klik Transaction ID membuka Borrow Detail dan log aset memuat peristiwa yang sama dengan Borrow Log
19. Klik Transaction ID BRW milik DU-042-8 pada baris dengan Status `Returned`
20. Verifikasi Borrow Detail BRW milik DU-042-8 terbuka
21. Klik menu ⋯ pada baris aset `Kamera Sony ZV-1 {runId}`
22. Klik `Borrow Log`
23. Verifikasi Borrow Log aset `Kamera Sony ZV-1 {runId}` memuat node `Handed over by [Giver]` dan node `Returned to [Receiver]` untuk peristiwa yang sama dengan baris Status `Borrowed` dan `Returned` di Transaction log aset
24. Tutup dialog Borrow Log
25. Klik tab `History` pada halaman Borrow
26. Ketik Search `Oscar Wijaya {runId}`, tekan Enter
27. Verifikasi BRW milik DU-042-8 tampil di tab `History` sebagai riwayat tingkat BRW

### Borrower tanpa akun login menampilkan PIC, dan Approval rerouted serta Rejected
28. Buka daftar aset lewat sidebar `Assets` > `All`
29. Ketik Search `Proyektor Epson EB-X49 {runId}`, tekan Enter
30. Buka Asset Detail aset `Proyektor Epson EB-X49 {runId}`
31. Klik tab `Transaction log`
32. Verifikasi peristiwa Requested dan Approval rerouted masing-masing tercatat sebagai baris dengan Status `Waiting for Approval`
33. Verifikasi peristiwa Rejected tercatat sebagai baris dengan Status `Rejected`
34. Verifikasi kolom `PIC` berisi `Rina Wijaya {runId}` pada ketiga baris karena Borrower tidak punya akun login
35. Verifikasi kolom `Borrower` berisi `Nico Prasetyo {runId}` pada ketiga baris

### Peristiwa Canceled tercatat sebagai Status Canceled
36. Buka daftar aset lewat sidebar `Assets` > `All`
37. Ketik Search `Gimbal DJI RS 3 {runId}`, tekan Enter
38. Buka Asset Detail aset `Gimbal DJI RS 3 {runId}`
39. Klik tab `Transaction log`
40. Verifikasi peristiwa Canceled tercatat sebagai baris dengan Status `Canceled`

### Report Missing oleh Aktor Borrow dan Missing confirmed menutup baris Returned dengan penanda Missing
41. Buka daftar aset lewat sidebar `Assets` > `All`
42. Ketik Search `Mikrofon Rode VideoMic {runId}`, tekan Enter
43. Buka Asset Detail aset `Mikrofon Rode VideoMic {runId}`
44. Klik tab `Transaction log`
45. Verifikasi peristiwa laporan kehilangan oleh Aktor Borrow tercatat sebagai baris dengan Status `Returned` dan penanda laporan aset tak ditemukan
46. Buka daftar aset lewat sidebar `Assets` > `All`
47. Ketik Search `Speaker Bose S1 Pro {runId}`, tekan Enter
48. Buka Asset Detail aset `Speaker Bose S1 Pro {runId}`
49. Klik tab `Transaction log`
50. Verifikasi peristiwa konfirmasi laporan kehilangan tercatat sebagai baris dengan Status `Returned` dan penanda laporan aset tak ditemukan

### Extension forwarded, rejected, dan canceled serta peristiwa yang tidak membentuk baris
51. Buka daftar aset lewat sidebar `Assets` > `All`
52. Ketik Search `Tablet Samsung Tab S9 {runId}`, tekan Enter
53. Buka Asset Detail aset `Tablet Samsung Tab S9 {runId}`
54. Klik tab `Transaction log`
55. Verifikasi peristiwa Extension forwarded tercatat sebagai baris dengan Status `Extension Approval`
56. Verifikasi peristiwa Extension rejected dan Extension canceled masing-masing tercatat sebagai baris dengan Status `Borrowed`
57. Verifikasi log memuat baris Status `Extension Approval` dan baris Status `Returned` untuk BRW milik DU-042-12
58. Verifikasi tidak ada baris tambahan di log yang memuat tepat sembilan baris untuk Damage reported, Damage report canceled, laporan kehilangan oleh Borrower, pembatalan laporan kehilangan, TAG reported, dan Handover not confirmed

### Extension rejected sesudah Due date berstatus Overdue dan Returned membawa penanda Damaged
59. Buka daftar aset lewat sidebar `Assets` > `All`
60. Ketik Search `Printer Epson L5290 {runId}`, tekan Enter
61. Buka Asset Detail aset `Printer Epson L5290 {runId}`
62. Klik tab `Transaction log`
63. Verifikasi peristiwa Extension rejected sesudah Due date tercatat sebagai baris dengan Status `Overdue`
64. Verifikasi peristiwa Returned tercatat sebagai baris dengan Status `Returned` dan penanda `Damaged`
