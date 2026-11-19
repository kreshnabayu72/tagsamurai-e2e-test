---
id: TC-FA-BORROW-E2E-010-borrow-log-dialog
title: "Dialog Borrow Log menampilkan riwayat satu aset di dalam satu BRW"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#r8", "§8#p1", "§8#r1", "§8#r2", "§8#r3", "§8#r4", "§8.1#p1", "§8.1#r1", "§8.1#r2", "§8.1#r3", "§8.1#r4", "§8.1#r5", "§8.1#b1", "§8.1#b2", "§8.1#b3"]
smoke: []
dependsOn: []
trace:
  "§5#r8": [1]
  "§8#p1": [18]
  "§8#r1": [12]
  "§8#r2": [1]
  "§8#r3": [1]
  "§8#r4": [16]
  "§8.1#p1": [12, 13, 14]
  "§8.1#r1": [7]
  "§8.1#r2": [7]
  "§8.1#r3": [8, 36, 37, 39, 41, 42]
  "§8.1#r4": [9, 10, 28]
  "§8.1#r5": [11, 49, 50, 55]
  "§8.1#b1": [26]
  "§8.1#b2": [17, 20]
  "§8.1#b3": [15]
anchor: []
coverage:
  web: automated
---

# Dialog Borrow Log menampilkan riwayat satu aset di dalam satu BRW

## Prerequisites
- Aktor: Total Control `Admin Borrow {runId}` (DU-010-1), cakupan seluruh client.
- Layar awal: Transactions > Borrow, tab Transactions.
- Data:
  - DU-010-1: User `Admin Borrow {runId}`, role Total Control, cakupan seluruh client.
  - Pelaku riwayat: `Agus Pratama` (Asset Admin, Group penugasan `Head Office`) sebagai pengaju, pemberi saat handover, pengaju Extend, dan penerima Return; `Siti Rahmawati` (Group Manager, Group binaan `Head Office`) sebagai approver dengan mode `Any one`; `Rina Wijaya` (Asset Admin, Group penugasan `Head Office`) sebagai PIC.
  - DU-010-2: BRW Returned, Borrower `Oscar Wijaya` (tampil `Oscar W`), Group `Head Office`, pengaju `Agus Pratama`, dengan tiga aset yang dibuat berurutan dari `Mikrofon Rode VideoMic {runId}`, `Kamera Sony ZV-1 {runId}`, lalu `Gimbal DJI RS 3 {runId}` (bukan urutan abjad), sehingga urutan tabel Assets (Name A–Z) adalah `Gimbal DJI RS 3 {runId}`, `Kamera Sony ZV-1 {runId}`, lalu `Mikrofon Rode VideoMic {runId}`. Aset `Kamera Sony ZV-1 {runId}` berstatus Returned dengan riwayat berurutan dari yang paling awal: Borrow requested (Duration `3 Day(s)`, Purpose `Client presentation`), Approved by `Siti Rahmawati` (Approved duration `3 Day(s)`, Mode `Any one`), Handed over oleh `Agus Pratama` (Duration `3 Day(s)`, Condition `Normal`), Extension requested oleh `Agus Pratama` (Extend duration `2 Day(s)`), Extension approved oleh `Siti Rahmawati` (Due date `T0 − 3 hari → T0 − 1 hari`, Extension `1 of 2`), dan Returned ke `Agus Pratama` (Condition `Normal`). Aset `Gimbal DJI RS 3 {runId}` dan `Mikrofon Rode VideoMic {runId}` memiliki riwayat sendiri.
  - DU-010-3: BRW Borrowed, Borrower `Nico Prasetyo` (karyawan tanpa akun login, PIC `Rina Wijaya`), Group `Head Office`, pengaju `Agus Pratama`, satu aset `Proyektor Epson EB-X49 {runId}` yang sudah diserahkan oleh `Agus Pratama` dan dikonfirmasi oleh `Rina Wijaya` atas nama `Nico Prasetyo`.
  - DU-010-4: BRW Self-service Borrowed, Borrower `Dian Kusuma` (tampil `Dian K`, karyawan ber-akun), Group `Head Office`, satu aset `Headset JBL Tune 510 {runId}` berstatus Borrowed dengan pengajuan Extend yang menunggu approval (tampil `Extension Approval`).
  - DU-010-5: BRW Borrowed, Borrower `Fitri Handayani` (tampil `Fitri H`), Group `Head Office`, pengaju `Agus Pratama`, satu aset `Kamera Canon EOS R10 {runId}` berstatus Borrowed dengan pengajuan Extend dari My Asset yang menunggu review (tampil `Extension Request`).
- Kondisi:
  - Date Format di General Settings entitas berlaku untuk tampilan tanggal.

## Test Steps

### Modul tidak memakai Changelog
1. Verifikasi toolbar tabel Transactions memuat `Search` dan `Download` dan tidak memuat `Changelog`

### Borrow Log satu aset dalam satu BRW
2. Klik tab `History`
3. Ketik Search `{runId}`, tekan Enter
4. Klik Transaction ID baris Borrower `Oscar W`
5. Klik `⋯` pada baris aset `Kamera Sony ZV-1 {runId}`
6. Klik `Borrow Log`
7. Verifikasi dialog `Borrow Log` terbuka dengan Transaction ID BRW milik DU-010-2
8. Verifikasi dialog menyediakan `Prev` dan `Next` untuk berpindah ke aset lain di BRW yang sama
9. Verifikasi dialog menampilkan Requested By `Agus Pratama` dan Borrower `Oscar Wijaya`
10. Verifikasi Borrower `Oscar Wijaya` berupa tautan profil
11. Verifikasi dialog menampilkan badge status baris `Returned`
12. Verifikasi urutan node dari atas ke bawah: `Returned to Agus Pratama`, `Extension approved by Siti Rahmawati`, `Extension requested by Agus Pratama`, `Handed over by Agus Pratama`, `Approved by Siti Rahmawati`, lalu `Borrow requested by Agus Pratama`
13. Verifikasi dialog hanya memuat riwayat aset `Kamera Sony ZV-1 {runId}` dan tidak memuat node milik aset `Gimbal DJI RS 3 {runId}`
14. Verifikasi node `Borrow requested by Agus Pratama` memuat `Duration: 3 Day(s)` dan `Purpose: Client presentation`
15. Verifikasi node `Approved by Siti Rahmawati` memuat nama approver, `Approved duration: 3 Day(s)`, dan `Mode: Any one`
16. Verifikasi node `Extension approved by Siti Rahmawati` memuat baris detail Due date dari nilai lama ke nilai baru `T0 − 3 hari → T0 − 1 hari` dan `Extension: 1 of 2`
17. Verifikasi node `Returned to Agus Pratama` mencatat penerima Return dan memuat `Condition: Normal`
18. Verifikasi dialog Borrow Log tidak menyediakan aksi untuk mengubah atau menghapus entri
19. Tutup dialog Borrow Log
20. Verifikasi tabel Assets tidak memiliki kolom `Received By`

### Pelaku atas nama PIC pada Borrow Log
21. Kembali ke tab History lewat segmen Origin Tab pada breadcrumb
22. Klik tab `Borrowed Assets`
23. Ketik Search `{runId}`, tekan Enter
24. Klik `⋯` pada baris aset `Proyektor Epson EB-X49 {runId}`
25. Klik `Borrow Log`
26. Verifikasi node `Handed over by Agus Pratama` memuat `Confirmation: Confirmed by Rina Wijaya on behalf of Nico Prasetyo`
27. Arahkan kursor ke ikon tautan di samping Borrower `Nico Prasetyo`
28. Verifikasi tooltip `On behalf of: Rina Wijaya (PIC)` tampil

### Prev dan Next berpindah hanya di antara aset dalam BRW yang sama
29. Tutup dialog Borrow Log
30. Klik tab `History`
31. Ketik Search `{runId}`, tekan Enter
32. Klik Transaction ID baris Borrower `Oscar W`
33. Klik `⋯` pada baris aset `Kamera Sony ZV-1 {runId}`
34. Klik `Borrow Log`
35. Klik `Next`
36. Verifikasi dialog Borrow Log menampilkan riwayat aset `Mikrofon Rode VideoMic {runId}` mengikuti urutan tabel Assets
37. Verifikasi `Next` Disabled karena `Mikrofon Rode VideoMic {runId}` aset terakhir di BRW ini
38. Klik `Prev`
39. Verifikasi dialog Borrow Log menampilkan riwayat aset `Kamera Sony ZV-1 {runId}`
40. Klik `Prev`
41. Verifikasi dialog Borrow Log menampilkan riwayat aset `Gimbal DJI RS 3 {runId}`
42. Verifikasi `Prev` Disabled karena `Gimbal DJI RS 3 {runId}` aset pertama di BRW ini
43. Tutup dialog Borrow Log

### Badge status baris Extension Approval dan penanda Self-service
44. Kembali ke tab History lewat segmen Origin Tab pada breadcrumb
45. Klik tab `Borrowed Assets`
46. Ganti isi kotak search dengan `Headset JBL Tune 510 {runId}`, tekan Enter
47. Klik `⋯` pada baris aset `Headset JBL Tune 510 {runId}`
48. Klik `Borrow Log`
49. Verifikasi dialog menampilkan badge status baris `Extension Approval`
50. Verifikasi dialog menampilkan penanda `Self-service`
51. Tutup dialog Borrow Log

### Badge status baris Extension Request
52. Ganti isi kotak search dengan `Kamera Canon EOS R10 {runId}`, tekan Enter
53. Klik `⋯` pada baris aset `Kamera Canon EOS R10 {runId}`
54. Klik `Borrow Log`
55. Verifikasi dialog menampilkan badge status baris `Extension Request`
56. Tutup dialog Borrow Log
