---
id: TC-FA-DAMAGED-E2E-010-review-reject
title: "Reject laporan lewat D-DMG-04 dengan Reason memindahkan record ke History sebagai Rejected dan menambah node Report rejected by"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, D-DMG-04, §4.2.4#p5, §4.2.4#r16, §4.4#r6, §4.4#p1, §8.1#b1, §8.1#r8, TS-DMG-04, §Aturan Logika Modul#r54, §Aturan Logika Modul#r23, §9.7#r6, FLD-DMG-06, §9.6#r3, F-DMG-04, §3#p4, §4.2.4#r17, §4.2.4#p13, EB-FB-1@reject, EB-FRM-1@reject-report]
smoke: [EB-FB-1@reject, EB-FRM-1@reject-report]
dependsOn: []
trace:
  T-DMG-01: [3, 5, 29, 46, 73]
  D-DMG-04: [9, 18, 25, 50, 67]
  §4.2.4#p5: 9
  §4.2.4#r16: [9, 12, 16, 85]
  §4.4#r6: [7, 9, 12]
  §4.4#p1: [13, 14, 15, 16, 17, 22]
  §8.1#b1: [13, 15, 17]
  §8.1#r8: [17, 18]
  TS-DMG-04: [12, 79]
  §Aturan Logika Modul#r54: [16, 18]
  §Aturan Logika Modul#r23: [16, 25]
  §9.7#r6: [21, 22, 25]
  FLD-DMG-06: 18
  §9.6#r3: [12, 16, 17]
  F-DMG-04: [12, 16, 25]
  §3#p4: [9, 16, 18, 25]
  §4.2.4#r17: [36, 37, 38, 40, 43]
  §4.2.4#p13: [53, 55, 57, 59, 63, 68, 70, 81]
  EB-FB-1@reject: 12
  EB-FRM-1@reject-report: [19, 26]
anchor: []
coverage:
  web: automated
---

# Reject laporan lewat D-DMG-04 dengan Reason memindahkan record ke History sebagai Rejected dan menambah node Report rejected by

## Prerequisites
- Aktor: Total Control (DU-010-4).
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-010-1: Damage record aset `Camera Canon EOS {runId}` di Group `Head Office`, status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pemegang aset DU-010-3 dengan What happened `Lensa kamera berembun dan gambar tidak fokus`; Damage Log hanya memuat node `Reported damaged by`.
  - DU-010-3: User `Dewi Anggraeni {runId}`, pelapor umum pemegang aset DU-010-1, tanpa hak Aktor Damaged; cakupan: aset yang ia pegang.
  - DU-010-4: User `Agus Pratama {runId}`, role Total Control; cakupan: seluruh client.
  - DU-010-5: Damage record aset `Speaker Polycom Trio 8500 {runId}` di Group `Head Office`, status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pemegang aset DU-010-3; Damage Log hanya memuat node `Reported damaged by`.
  - DU-010-6: Damage record aset `Webcam Logitech BRIO 4K {runId}` di Group `Head Office`, status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pemegang aset DU-010-3; Damage Log hanya memuat node `Reported damaged by`.

## Test Steps

### Reject dari footer Damage Log membuka dialog Reject Report
1. Catat jumlah pada badge tab `Damaged` sebagai jumlah awal
2. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
3. Verifikasi baris aset `Camera Canon EOS {runId}` tampil di tabel dengan status `Waiting for Confirmation`
4. Klik `⋯` pada baris `Camera Canon EOS {runId}`
5. Verifikasi item `Review` tampil pada menu baris
6. Klik `Review`
7. Verifikasi footer dialog `Damage Log` memuat tombol `[Reject]` dan `[Confirm]` yang aktif
8. Klik `[Reject]`
9. Verifikasi dialog `Reject Report` terbuka dengan nama aset `Camera Canon EOS {runId}`

### Reject dengan Reason memindahkan record ke History sebagai Rejected
10. Isi Reason `Foto kerusakan berbeda dari aset yang dilaporkan`
11. Klik `[Reject]` pada dialog `Reject Report`
12. Verifikasi toast `Success, report has been rejected.` tampil
13. Verifikasi dialog `Damage Log` tetap terbuka
14. Verifikasi dialog `Reject Report` tidak lagi tampil
15. Verifikasi tombol `[Reject]` dan `[Confirm]` tidak lagi tampil di footer dialog `Damage Log`
16. Verifikasi badge status record pada dialog `Damage Log` `Rejected`
17. Verifikasi timeline memuat node `Report rejected by` dengan aktor yang sedang masuk sebagai pelaku
18. Verifikasi node `Report rejected by` memuat baris detail Reason `Foto kerusakan berbeda dari aset yang dilaporkan`
19. Verifikasi timeline memuat tepat satu node `Report rejected by`
20. Klik `✕` pada dialog `Damage Log`
21. Verifikasi badge tab `Damaged` berkurang satu dari jumlah awal
22. Verifikasi sub-tab Active menampilkan `No results found` untuk Search `Camera Canon EOS {runId}`
23. Klik sub-tab `History`
24. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
25. Verifikasi baris aset `Camera Canon EOS {runId}` tampil di tabel History dengan status `Rejected`
26. Verifikasi hasil Search di History berjumlah satu baris

### Reject atas laporan yang sudah dibatalkan pelapor ditolak dengan Already Changed
27. Klik sub-tab `Active`
28. Ketik Search `Webcam Logitech BRIO 4K {runId}`, tekan Enter
29. Verifikasi baris aset `Webcam Logitech BRIO 4K {runId}` tampil di tabel dengan status `Waiting for Confirmation`
30. Klik `⋯` pada baris `Webcam Logitech BRIO 4K {runId}`
31. Klik `Review`
32. Klik `[Reject]`
33. Isi Reason `Foto kerusakan tidak menunjukkan aset yang dilaporkan`
34. Dewi Anggraeni {runId} membatalkan laporannya atas aset `Webcam Logitech BRIO 4K {runId}` dari sesi lain
35. Klik `[Reject]` pada dialog `Reject Report`
36. Verifikasi dialog `Already Changed` terbuka
37. Verifikasi dialog memuat pesan `This record was changed by [User Name]. Reload to see the latest status.` dengan `[User Name]` berisi `Dewi Anggraeni {runId}`, pelapor yang lebih dulu membatalkan laporan
38. Verifikasi dialog memuat tombol `[Reload]`
39. Klik `[Reload]` pada dialog `Already Changed`
40. Verifikasi dialog `Already Changed` tidak lagi tampil
41. Klik sub-tab `History`
42. Ketik Search `Webcam Logitech BRIO 4K {runId}`, tekan Enter
43. Verifikasi baris aset `Webcam Logitech BRIO 4K {runId}` tampil di tabel History dengan status `Canceled`

### Reject Report yang kotor memunculkan konfirmasi bawaan browser saat muat ulang atau tutup tab
44. Klik sub-tab `Active`
45. Ketik Search `Speaker Polycom Trio 8500 {runId}`, tekan Enter
46. Verifikasi baris aset `Speaker Polycom Trio 8500 {runId}` tampil di tabel dengan status `Waiting for Confirmation`
47. Klik `⋯` pada baris `Speaker Polycom Trio 8500 {runId}`
48. Klik `Review`
49. Klik `[Reject]`
50. Verifikasi dialog `Reject Report` terbuka dengan nama aset `Speaker Polycom Trio 8500 {runId}`
51. Isi Reason `Laporan duplikat dengan laporan sebelumnya atas aset yang sama`
52. Muat ulang halaman (F5)
53. Verifikasi konfirmasi bawaan browser muncul
54. Batalkan konfirmasi bawaan browser agar tetap di halaman
55. Verifikasi dialog `Reject Report` tetap terbuka dengan isian Reason `Laporan duplikat dengan laporan sebelumnya atas aset yang sama`
56. Tutup tab browser
57. Verifikasi konfirmasi bawaan browser muncul
58. Batalkan konfirmasi bawaan browser agar tab tidak tertutup
59. Verifikasi dialog `Reject Report` tetap terbuka dengan isian Reason `Laporan duplikat dengan laporan sebelumnya atas aset yang sama`
60. Klik `✕` pada dialog `Reject Report`
61. Klik `[Leave]` pada dialog `Unsaved Changes`
62. Klik `✕` pada dialog `Damage Log`

### Reject Report yang bersih atau sudah tersimpan tidak memunculkan konfirmasi bawaan browser
63. Verifikasi baris aset `Speaker Polycom Trio 8500 {runId}` tampil di tabel dengan status `Waiting for Confirmation`
64. Klik `⋯` pada baris `Speaker Polycom Trio 8500 {runId}`
65. Klik `Review`
66. Klik `[Reject]`
67. Verifikasi dialog `Reject Report` terbuka dengan nama aset `Speaker Polycom Trio 8500 {runId}`
68. Verifikasi isian Reason pada dialog `Reject Report` belum diisi
69. Muat ulang halaman (F5)
70. Verifikasi muat ulang berjalan tanpa konfirmasi bawaan browser
71. Buka halaman Assets, tab `Damaged`
72. Ketik Search `Speaker Polycom Trio 8500 {runId}`, tekan Enter
73. Verifikasi baris aset `Speaker Polycom Trio 8500 {runId}` tampil di tabel dengan status `Waiting for Confirmation`
74. Klik `⋯` pada baris `Speaker Polycom Trio 8500 {runId}`
75. Klik `Review`
76. Klik `[Reject]`
77. Isi Reason `Laporan duplikat dengan laporan sebelumnya atas aset yang sama`
78. Klik `[Reject]` pada dialog `Reject Report`
79. Verifikasi toast `Success, report has been rejected.` tampil
80. Muat ulang halaman (F5)
81. Verifikasi muat ulang berjalan tanpa konfirmasi bawaan browser
82. Buka halaman Assets, tab `Damaged`
83. Klik sub-tab `History`
84. Ketik Search `Speaker Polycom Trio 8500 {runId}`, tekan Enter
85. Verifikasi baris aset `Speaker Polycom Trio 8500 {runId}` tampil di tabel History dengan status `Rejected`
