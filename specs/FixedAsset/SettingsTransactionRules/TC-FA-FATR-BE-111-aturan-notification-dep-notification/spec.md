---
id: TC-FA-FATR-BE-111-aturan-notification-dep-notification
title: "Notifikasi dan email akibat setting transaksi"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
owner: BE
sourceRules: ["§Aturan Logika Modul#r10", "§Aturan Logika Modul#r68", "§Aturan Logika Modul#r69", "§Aturan Logika Modul#r70", "§4.1#r214", "§4.1#r215", "§9.2#b208", "§9.2#b228", "§9.2#b229", "§9.2#b230", "§9.2#b231", "§9.2#b232", "§9.2#b233", "§9.2#b234", "§9.2#b236", "§9.2#b237", "§9.2#b238", "§9.2#b239", "§9.2#b302", "§9.2#b303", "§9.2#b304", "§9.2#b305", "§9.2#b306", "§9.2#b479", "§9.2#b480", "§9.2#b483", "§9.2#b484", "§9.2#b485", "§9.2#b486", "§9.4.2#r132", "§9.4.4#r40", "§9.7#r2", "§9.7#r12", "§9.7#r32", "§9.7#r33", "§9.10.1#b6", "§11#r13", "§11#r17"]
smoke: []
dependsOn: ["Notification: notifikasi in-app dan email"]
trace:
  "§4.1#r214": [3, 5, 7, 8]
  "§Aturan Logika Modul#r68": [3, 5, 7, 8, 17, 19, 21, 22, 46, 48]
  "§11#r13": [3, 5, 7, 8, 17, 19, 21, 22, 80]
  "§4.1#r215": [10, 24]
  "§Aturan Logika Modul#r10": [10, 17, 19, 21, 22, 24]
  "§Aturan Logika Modul#r69": [12, 13, 38, 43]
  "§Aturan Logika Modul#r70": [12, 27, 28, 38, 42, 43]
  "§11#r17": 12
  "§9.2#b479": [30, 37]
  "§9.2#b480": 30
  "§9.7#r12": 30
  "§9.2#b485": 31
  "§9.2#b484": 32
  "§9.2#b483": 34
  "§9.2#b486": 35
  "§9.4.2#r132": 37
  "§9.2#b229": 50
  "§9.2#b302": 50
  "§9.7#r32": [50, 58]
  "§9.2#b228": 51
  "§9.4.4#r40": 52
  "§9.2#b208": [55, 58]
  "§9.7#r2": [55, 58]
  "§9.2#b230": [63, 67]
  "§9.2#b237": 63
  "§9.2#b306": 63
  "§9.2#b236": 64
  "§9.2#b238": 65
  "§9.2#b239": 66
  "§9.2#b231": 68
  "§9.2#b232": [71, 72, 73]
  "§9.2#b303": [71, 72, 73]
  "§9.7#r33": [71, 72, 73, 74, 75]
  "§9.2#b233": [74, 80]
  "§9.2#b304": [74, 80]
  "§9.2#b234": 75
  "§9.2#b305": 75
  "§9.10.1#b6": 83
---

# Notifikasi dan email akibat setting transaksi

## Prerequisites
- Aktor: Total Control. Pengaju peminjaman: `Rudi Hartono {runId}`. Operator di luar tenant, hanya untuk mengubah paket entitas.
- Data:
  - DU-111-1: entitas khusus `Entitas Notifikasi Transaksi {runId}`, tidak dipakai spec lain; semua data di bawah ada di entitas ini.
  - DU-111-2: aset `Laptop Kantor {runId}`, peminjaman berstatus Borrowed dengan Due date `T0 − 1 hari`; event `borrow_overdue` untuk peminjaman ini belum pernah terjadi sebelum spec mulai.
  - DU-111-3: aset `Printer Lantai 2 {runId}`, penugasan berstatus Waiting for Approval sejak `T0 − 14 hari 1 jam`.
  - DU-111-4: aset `Meja Rapat {runId}`, transfer berstatus In Transit.
  - DU-111-5: aset `Kursi Gudang {runId}`, pelepasan aset berstatus Waiting for Approval sejak `T0 − 14 hari 1 jam`.
  - DU-111-6: aset `Tablet Kasir {runId}`, tersedia untuk dipinjam.
  - DU-111-7: aset `Router Cadangan {runId}`, Condition `Missing`, hilang sejak `T0 − 40 hari`.
  - DU-111-8: aset `Monitor Ruang Rapat {runId}`, peminjaman berstatus Borrowed dengan Due date `T0 − 1 hari`; event `borrow_overdue` untuk peminjaman ini belum pernah terjadi sebelum spec mulai.
  - DU-111-9: aset `Scanner Arsip {runId}`, penugasan berstatus Waiting for Approval sejak `T0 − 13 hari 23 jam`.
  - DU-111-10: aset `Lemari Berkas {runId}`, transfer berstatus In Transit.
  - DU-111-11: aset `Kipas Angin Besar {runId}`, pelepasan aset berstatus Waiting for Approval sejak `T0 − 13 hari 23 jam`.
  - DU-111-12: aset `Tablet Gudang {runId}`, tersedia untuk dipinjam.
  - DU-111-13: aset `Mixer Audio {runId}`, Condition `Missing`, hilang sejak `T0 − 25 hari`.
  - DU-111-14: Group `Gudang Timur {runId}`, tanpa Role Transaksi `Approver` yang ditugaskan.
  - DU-111-15: aset `Forklift Gudang {runId}`, ada di Group `Gudang Timur {runId}`, tersedia untuk dipinjam.
  - DU-111-16: aset `Genset Proyek {runId}`, pengajuan pinjam berstatus Waiting for Approval sejak `T0 − 13 hari 12 jam`.
  - DU-111-17: aset `Speaker Aula {runId}`, ada di Group `Gudang Barat {runId}`, tersedia untuk dipinjam.
  - DU-111-18: aset `Mobil Operasional {runId}`, peminjaman berstatus Borrowed dengan perpanjangan berstatus Waiting for Approval sejak `T0 − 2 jam`.
  - DU-111-19: aset `Kamera Mirrorless {runId}`, peminjaman berstatus Waiting for Handover sejak `T0 − 23 jam`.
  - DU-111-20: aset `Radio Panggil {runId}`, penugasan berstatus Waiting for Approval sejak `T0 − 3 hari`.
  - DU-111-21: aset `Timbangan Digital {runId}`, transfer berstatus Waiting for Approval sejak `T0 − 3 hari`.
  - DU-111-22: aset `Mesin Cetak {runId}`, pelepasan aset berstatus Waiting for Approval sejak `T0 − 3 hari`.
  - DU-111-23: aset `Kompor Lapangan {runId}`, peminjaman berstatus Waiting for Handover sejak `T0 − 3 hari`.
  - DU-111-24: aset `Tenda Lapangan {runId}`, peminjaman berstatus Borrowed dengan perpanjangan yang menunggu review sejak `T0 − 3 hari`.
  - DU-111-25: user `Rudi Hartono {runId}`, pengaju peminjaman, bukan Total Control dan bukan Group Manager yang menaungi Group mana pun.
  - DU-111-26: user `Maya Kusuma {runId}`, calon Approver peminjaman untuk Group `Gudang Barat {runId}`.
  - DU-111-27: Group `Gudang Barat {runId}`.
  - DU-111-28: aset `Kursi Lipat Aula {runId}`, ada di Group `Gudang Barat {runId}`, tersedia untuk dipinjam.
  - DU-111-29: aset `Forklift Cadangan {runId}`, ada di Group `Gudang Timur {runId}`, tersedia untuk dipinjam.
  - DU-111-30: aset `Drone Survei {runId}`, peminjaman berstatus Borrowed dengan Due date `T0 − 1 hari`; event `borrow_overdue` untuk peminjaman ini belum pernah terjadi sebelum spec mulai.
  - DU-111-31: aset `Rak Gudang Besi {runId}`, transfer berstatus In Transit.
- Kondisi:
  - Approval Workflow tersedia pada paket entitas.
  - Require approval bernilai `OFF` untuk transaksi pinjam.
  - Max duration bernilai `14` untuk transaksi pinjam.
  - Long missing after bernilai `30` (days).
  - Level Feature Suite Borrowing bernilai `Full`.
  - Transaction timeout bernilai `14` (days) untuk setiap transaksi pada awal spec.
  - Entitas memakai plan khusus miliknya sendiri, tidak dipakai entitas lain.

## Test Steps

### Send email notifications ON: notifikasi transaksi itu juga dikirim lewat email
1. Total Control menyimpan Send email notifications bernilai `ON` untuk setiap transaksi di All categories
2. Job harian Overdue Borrow berjalan sehingga peminjaman aset `Laptop Kantor {runId}` untuk pertama kali Overdue dan event `borrow_overdue` terjadi
3. Verifikasi notifikasi `borrow_overdue` untuk aset `Laptop Kantor {runId}` terkirim in-app dan lewat email
4. Job pengecekan Transaction timeout berjalan sehingga penugasan aset `Printer Lantai 2 {runId}` dan pelepasan aset `Kursi Gudang {runId}`, yang menunggu approval sejak `T0 − 14 hari 1 jam`, melewati batas Transaction timeout `14` (days)
5. Verifikasi notifikasi berawalan `assignment_` dan berakhiran `_auto_canceled` untuk aset `Printer Lantai 2 {runId}` terkirim in-app dan lewat email
6. Event `transfer_transit_overdue` terjadi untuk aset `Meja Rapat {runId}`
7. Verifikasi notifikasi `transfer_transit_overdue` untuk aset `Meja Rapat {runId}` terkirim in-app dan lewat email
8. Verifikasi notifikasi berawalan `disposal_` dan berakhiran `_auto_canceled` untuk aset `Kursi Gudang {runId}` terkirim in-app dan lewat email
9. Total Control mengajukan peminjaman aset `Tablet Kasir {runId}`
10. Verifikasi email konfirmasi peminjaman aset `Tablet Kasir {runId}` ke peminjam terkirim saat Send email notifications `ON`

### missing_long hanya dikirim in-app saat Send email notifications ON
11. Job harian untuk aset hilang berjalan
12. Verifikasi notifikasi `missing_long` untuk aset `Router Cadangan {runId}` terkirim in-app saat Send email notifications `ON`
13. Verifikasi tidak ada email notifikasi `missing_long` untuk aset `Router Cadangan {runId}`

### Send email notifications OFF: notifikasi transaksi itu hanya in-app
14. Waktu berlalu 2 jam
15. Total Control menyimpan Send email notifications bernilai `OFF` untuk setiap transaksi di All categories
16. Job harian Overdue Borrow berjalan sehingga peminjaman aset `Monitor Ruang Rapat {runId}` untuk pertama kali Overdue dan event `borrow_overdue` terjadi
17. Verifikasi notifikasi `borrow_overdue` untuk aset `Monitor Ruang Rapat {runId}` terkirim in-app dan tidak ada email
18. Job pengecekan Transaction timeout berjalan sehingga penugasan aset `Scanner Arsip {runId}` dan pelepasan aset `Kipas Angin Besar {runId}`, yang menunggu approval sejak `T0 − 13 hari 23 jam`, melewati batas Transaction timeout `14` (days)
19. Verifikasi notifikasi berawalan `assignment_` dan berakhiran `_auto_canceled` untuk aset `Scanner Arsip {runId}` terkirim in-app dan tidak ada email
20. Event `transfer_transit_overdue` terjadi untuk aset `Lemari Berkas {runId}`
21. Verifikasi notifikasi `transfer_transit_overdue` untuk aset `Lemari Berkas {runId}` terkirim in-app dan tidak ada email
22. Verifikasi notifikasi berawalan `disposal_` dan berakhiran `_auto_canceled` untuk aset `Kipas Angin Besar {runId}` terkirim in-app dan tidak ada email
23. Total Control mengajukan peminjaman aset `Tablet Gudang {runId}`
24. Verifikasi email konfirmasi peminjaman aset `Tablet Gudang {runId}` ke peminjam tetap terkirim saat Send email notifications `OFF`

### missing_long tidak dikendalikan switch Send email notifications
25. Total Control menyimpan Long missing after bernilai `20` di All categories
26. Job harian untuk aset hilang berjalan
27. Verifikasi notifikasi `missing_long` untuk aset `Mixer Audio {runId}` yang hilang sejak `T0 − 25 hari` terkirim in-app saat semua Send email notifications `OFF`
28. Verifikasi tidak ada email notifikasi `missing_long` untuk aset `Mixer Audio {runId}` saat semua Send email notifications `OFF`, sama seperti saat `ON`

### Save konfigurasi Approval tanpa Approver mengirim approver_required
29. Total Control menyimpan Require approval bernilai `ON` untuk transaksi pinjam di All categories, padahal tidak ada Role Transaksi `Approver` yang ditugaskan
30. Verifikasi notifikasi `approver_required` terkirim tepat satu kali sesudah Save konfigurasi Approval menimbulkan kondisi tidak ada Approver
31. Verifikasi notifikasi `approver_required` itu adalah peringatan guard konfigurasi, tanpa pemberitahuan perubahan Settings yang menyertainya
32. Verifikasi penerima, Title, Body, dan Click-path notifikasi `approver_required` sesuai katalog notifikasi
33. Total Control menyimpan Max duration bernilai `20` untuk transaksi pinjam di All categories tanpa mengubah konfigurasi Approval
34. Verifikasi tidak ada notifikasi `approver_required` baru selama konfigurasi Approval tidak diubah
35. Verifikasi Save yang tidak menimbulkan kondisi tidak ada Approver tidak mengirim notifikasi apa pun
36. `Rudi Hartono {runId}` mengajukan transaksi pinjam atas aset `Forklift Gudang {runId}` di Group `Gudang Timur {runId}` yang tidak dicakup Approver eligible mana pun
37. Verifikasi notifikasi `approver_required` terkirim untuk aset `Forklift Gudang {runId}` karena tidak ada Approver eligible yang mencakup Group aset
38. Verifikasi tidak ada email notifikasi `approver_required` saat semua Send email notifications `OFF`
39. Total Control menyimpan Send email notifications bernilai `ON` untuk setiap transaksi di All categories
40. Total Control menyimpan Require approval bernilai `OFF` untuk transaksi pinjam di All categories
41. Total Control menyimpan Require approval bernilai `ON` untuk transaksi pinjam di All categories, padahal tidak ada Role Transaksi `Approver` yang ditugaskan
42. Verifikasi notifikasi `approver_required` terkirim in-app sekali lagi saat semua Send email notifications `ON`, sama seperti saat `OFF`
43. Verifikasi tidak ada email notifikasi `approver_required` saat semua Send email notifications `ON`

### Switch Send email notifications dibedakan per transaksi
44. Total Control menyimpan Send email notifications bernilai `ON` untuk transaksi pinjam dan `OFF` untuk transaksi transfer di All categories
45. Job harian Overdue Borrow berjalan sehingga peminjaman aset `Drone Survei {runId}` untuk pertama kali Overdue dan event `borrow_overdue` terjadi
46. Verifikasi notifikasi `borrow_overdue` untuk aset `Drone Survei {runId}` terkirim in-app dan lewat email
47. Event `transfer_transit_overdue` terjadi untuk aset `Rak Gudang Besi {runId}`
48. Verifikasi notifikasi `transfer_transit_overdue` untuk aset `Rak Gudang Besi {runId}` terkirim in-app dan tidak ada email

### Peringatan 1 hari sebelum batas dikirim ulang saat Transaction timeout berubah
49. Job pengecekan Transaction timeout berjalan
50. Verifikasi notifikasi `*_almost_timeout` untuk transaksi atas aset `Genset Proyek {runId}` yang diajukan `T0 − 13 hari 12 jam` terkirim satu kali karena sisa waktu ke batas `14` (days) kurang dari 24 jam
51. Verifikasi notifikasi `*_almost_timeout` itu mengikuti katalog notifikasi
52. Verifikasi pengiriman notifikasi `*_almost_timeout` tidak menulis entri baru di Changelog Transaction Settings atau log lain
53. Total Control menyimpan Transaction timeout bernilai `30` untuk setiap transaksi di All categories
54. Job pengecekan Transaction timeout berjalan
55. Verifikasi notifikasi `*_almost_timeout` untuk aset `Genset Proyek {runId}` tidak bertambah karena sisa waktu ke batas baru lebih dari 24 jam
56. Total Control menyimpan Transaction timeout bernilai `14` untuk setiap transaksi di All categories
57. Job pengecekan Transaction timeout berjalan
58. Verifikasi notifikasi `*_almost_timeout` untuk aset `Genset Proyek {runId}` dikirim ulang sehingga tercatat dua kali karena sisa waktu ke batas baru 24 jam atau kurang

### Transaction timeout 1 hari: peringatan segera terkirim
59. Total Control menugaskan Role Transaksi `Approver` untuk transaksi pinjam kepada `Maya Kusuma {runId}` dengan cakupan Group `Gudang Barat {runId}`
60. Total Control menyimpan Transaction timeout bernilai `1` untuk setiap transaksi di All categories
61. `Rudi Hartono {runId}` mengajukan peminjaman aset `Speaker Aula {runId}` di Group `Gudang Barat {runId}` yang menunggu approval `Maya Kusuma {runId}`
62. Job pengecekan Transaction timeout berjalan untuk pertama kalinya sesudah pengajuan itu
63. Verifikasi notifikasi `*_almost_timeout` untuk pengajuan pinjam aset `Speaker Aula {runId}` yang baru masuk status menunggu approval saat Transaction timeout `1` terkirim pada pengecekan job pertama itu
64. Verifikasi batas Transaction timeout `1` hari untuk pengajuan pinjam aset `Speaker Aula {runId}` adalah 24 jam sejak masuk status menunggu approval, sehingga titik 1 hari sebelum batas jatuh saat transaksi masuk status itu
65. Verifikasi peringatan untuk aset `Speaker Aula {runId}` tidak dilewati: tepat satu notifikasi `*_almost_timeout` tercatat sebelum batas
66. Verifikasi peringatan untuk Transaction timeout `1` memakai event `*_almost_timeout` yang sama seperti nilai Transaction timeout lain, tanpa event pengganti
67. Verifikasi notifikasi `*_almost_timeout` untuk perpanjangan peminjaman aset `Mobil Operasional {runId}` yang berstatus Waiting for Approval sejak `T0 − 2 jam` terkirim
68. Verifikasi notifikasi `*_almost_timeout` untuk peminjaman aset `Kamera Mirrorless {runId}` yang menunggu serah terima sejak `T0 − 23 jam` terkirim

### Batas terlewati: notifikasi auto-cancel sesuai transaksi
69. Waktu berlalu lebih dari 24 jam sejak Transaction timeout `1` disimpan
70. Job pengecekan Transaction timeout berjalan
71. Verifikasi notifikasi berawalan `assignment_` dengan akhiran `_auto_canceled` untuk aset `Radio Panggil {runId}` yang menunggu approval sejak `T0 − 3 hari` terkirim
72. Verifikasi notifikasi berawalan `transfer_` dengan akhiran `_auto_canceled` untuk aset `Timbangan Digital {runId}` yang menunggu approval sejak `T0 − 3 hari` terkirim
73. Verifikasi notifikasi berawalan `disposal_` dengan akhiran `_auto_canceled` untuk aset `Mesin Cetak {runId}` yang menunggu approval sejak `T0 − 3 hari` terkirim
74. Verifikasi notifikasi `borrow_auto_canceled` untuk aset `Kompor Lapangan {runId}` yang menunggu serah terima sejak `T0 − 3 hari` dan baris peminjamannya ditutup Canceled terkirim
75. Verifikasi notifikasi `borrow_extension_resolved` varian Timed out untuk perpanjangan peminjaman aset `Tenda Lapangan {runId}` yang menunggu review sejak `T0 − 3 hari` terkirim

### Level Borrowing Basic: baris yang melewati batas ditutup Canceled dan tetap dinotifikasi
76. Operator mengubah level Feature Suite Borrowing paket entitas menjadi `Basic`
77. `Rudi Hartono {runId}` mengajukan peminjaman aset `Kursi Lipat Aula {runId}` di Group `Gudang Barat {runId}` yang menunggu approval `Maya Kusuma {runId}`
78. Waktu berlalu lebih dari 24 jam sejak pengajuan aset `Kursi Lipat Aula {runId}`
79. Job pengecekan Transaction timeout berjalan
80. Verifikasi notifikasi `borrow_auto_canceled` untuk aset `Kursi Lipat Aula {runId}` yang peminjamannya ditutup Canceled pada level Feature Suite Borrowing `Basic` terkirim

### Paket tanpa Approval Workflow menonaktifkan approver_required
81. Operator mengubah paket entitas menjadi paket yang Approval Workflow-nya `OFF` dengan level Feature Suite Borrowing `Full`
82. `Rudi Hartono {runId}` mengajukan transaksi pinjam atas aset `Forklift Cadangan {runId}` di Group `Gudang Timur {runId}` yang tidak dicakup Approver eligible mana pun
83. Verifikasi tidak ada notifikasi `approver_required` baru dan transaksi tidak menunggu approval saat Approval Workflow `OFF`
