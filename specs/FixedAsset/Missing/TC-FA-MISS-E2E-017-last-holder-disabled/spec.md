---
id: TC-FA-MISS-E2E-017-last-holder-disabled
title: "Pemisahan tugas: Review, Mark as Found, dan Report Disposal Disabled bagi Last holder, aktif bagi admin lain"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§1.2#r118", "§1.2#r119", "§1.2#r120", "§1.2#r121", "§1.2#r74", "§6#r1", "§4.3#r4", "§9.4.2#r17", "§9.2#b28", "§2.1#b9", "§2.1#p12", "§2.1#p17", "§2.1#p18", "§2.1#p19", "§2.1#p20", "§9.4.3#b6", "§9.4.4#r14", "§8.1#r6", "§4.8#r6", "EB-TBL-5@aksi-last-holder", "§4.5#p1", "§4.8#r9"]
smoke: []
dependsOn: []
trace:
  "§1.2#r118": [2, 8, 11, 39, 54, 64, 74]
  "§1.2#r119": [3, 8]
  "§1.2#r120": [14, 18, 37, 84]
  "§1.2#r121": [15, 21, 37, 85, 89, 90]
  "§1.2#r74": [15, 18, 36, 85, 89]
  "§6#r1": [9, 12, 19, 22, 27, 68, 69, 78, 79, 89, 90]
  "§4.3#r4": [8, 9, 11, 18, 25, 68, 78, 89]
  "§9.4.2#r17": [8, 9]
  "§9.2#b28": [8, 11, 18, 25, 68, 78, 89]
  "§2.1#b9": [8, 32]
  "§2.1#p12": [2]
  "§2.1#p17": [2, 4]
  "§2.1#p18": [6, 9, 12]
  "§2.1#p19": [32, 33]
  "§2.1#p20": [3, 8]
  "§9.4.3#b6": [8, 11, 18, 21, 68, 78, 89]
  "§9.4.4#r14": [8, 9]
  "§8.1#r6": [25, 27]
  "§4.8#r6": [8, 18, 21, 25, 32, 36, 42, 45, 49, 57, 61]
  "EB-TBL-5@aksi-last-holder": [9, 12, 19, 43, 46, 58, 69, 79, 90]
  "§4.5#p1": [9, 19, 27, 69, 79, 90]
  "§4.8#r9": [11, 65, 68, 75, 78, 86, 89]
anchor: []
coverage:
  web: automated
---

# Pemisahan tugas: Review, Mark as Found, dan Report Disposal Disabled bagi Last holder, aktif bagi admin lain

## Prerequisites
- Aktor: Andi P, Group Manager pada Group Head Office, tercatat sebagai Last Holder DU-017-1 dan sebagai PIC yang tercatat bagi DU-017-2 dan DU-017-8; lalu Rina W, Total Control, yang bukan Last Holder DU-017-1 dan DU-017-2 tetapi Last Holder DU-017-3 dan DU-017-6; lalu `Bimo Tirta {runId}`, Manage asset & TAG (Update) pada Group Head Office, Last Holder DU-017-4 dan DU-017-7.
- Layar awal: halaman Missing, sub-tab Active.
- Data:
  - DU-017-1: Record Missing `Laptop Dell Latitude 7440 {runId}`, Asset ID `LPT-017-0001`, Group `Finance Room`, Status `Missing`, Source `Manual`, Last Holder `Andi P`, Reported By `Andi P`, Reported Date `T0 − 3 hari, pukul 10:00`; Andi P melapor sendiri sebagai Pelapor admin sehingga record langsung `Missing`.
  - DU-017-2: Record Waiting for Confirmation `Pallet Stacker Electric {runId}`, Asset ID `PST-017-0002`, Group `Head Office`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Joko S`, Reported By `Andi P (on behalf of Joko S)`, Reported Date `T0 − 1 hari, pukul 09:20`; Joko S adalah karyawan pemegang tanpa akun dan PIC yang tercatat saat dilaporkan adalah Andi P; saat laporan itu dibuat Andi P belum memegang hak Aktor Missing pada Group aset, dan hak itu (Group Manager pada Group Head Office) baru ia terima sesudah laporan dibuat.
  - DU-017-3: Record Waiting for Confirmation `Mesin Label Printer {runId}`, Asset ID `MLP-017-0003`, Group `Head Office`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Rina W`, Reported By `Rina W`, Reported Date `T0 − 2 hari, pukul 13:40`; Rina W memegang aset ini dan melapor saat belum memegang hak Aktor Missing, dan hak Total Control baru ia terima sesudah laporan dibuat.
  - DU-017-4: Record Waiting for Confirmation `Scanner Barcode Zebra {runId}`, Asset ID `SBZ-017-0004`, Group `Head Office`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Bimo T`, Reported By `Bimo T`, Reported Date `T0 − 2 hari, pukul 08:15`; Bimo T memegang aset ini dan melapor saat belum memegang hak Aktor Missing, dan hak Manage asset & TAG (Update) pada Group Head Office baru ia terima sesudah laporan dibuat.
  - DU-017-6: Record Missing `Proyektor Epson EB-X49 {runId}`, Asset ID `PRJ-017-0006`, Group `Head Office`, Status `Missing`, Source `Manual`, Last Holder `Rina W`, Reported By `Rina W`, Reported Date `T0 − 4 hari, pukul 10:30`; Rina W (Total Control) melapor sendiri sebagai Pelapor admin sehingga record langsung `Missing`.
  - DU-017-7: Record Missing `Printer HP LaserJet Pro {runId}`, Asset ID `PHP-017-0007`, Group `Head Office`, Status `Missing`, Source `Manual`, Last Holder `Bimo T`, Reported By `Bimo T`, Reported Date `T0 − 5 hari, pukul 14:10`; Bimo T (Manage asset & TAG (Update) pada Group Head Office) melapor sendiri sebagai Pelapor admin sehingga record langsung `Missing`.
  - DU-017-8: Record Missing `Trolley Dorong Gudang {runId}`, Asset ID `TDG-017-0008`, Group `Head Office`, Status `Missing`, Source `Reported by holder`, Last Holder `Joko S`, Reported By `Andi P (on behalf of Joko S)`, Reported Date `T0 − 6 hari, pukul 11:45`; Joko S adalah karyawan pemegang tanpa akun dan PIC yang tercatat saat dilaporkan adalah Andi P; saat melapor atas nama Joko S, Andi P sudah memegang hak Aktor Missing (Group Manager pada Group Head Office), sehingga ia melapor sebagai Pelapor admin dan record langsung `Missing`.
  - DU-017-5: Pengguna `Bimo Tirta {runId}`, role Manage asset & TAG (Update) pada Group `Head Office`; tampil sebagai `Bimo T`, dari `Bimo Tirta {runId}`.
  - Pengguna pada data: Andi P, Group Manager pada Group Head Office beserta sub-group; Rina W, Total Control, seluruh client; Joko S, karyawan pemegang tanpa akun.
  - Waktu pada data ditulis relatif terhadap waktu run `T0`.
- Kondisi:
  - Level Feature Suite Disposal pada entitas aktor adalah Full

## Test Steps

### Last Holder yang melapor sendiri tidak dapat Mark as Found dan Report Disposal
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi Last Holder baris `Laptop Dell Latitude 7440 {runId}` menampilkan `Andi P`
3. Verifikasi Reported By baris `Laptop Dell Latitude 7440 {runId}` menampilkan `Andi P`
4. Verifikasi Status baris `Laptop Dell Latitude 7440 {runId}` menampilkan `Missing`
5. Klik `⋯` pada baris `Laptop Dell Latitude 7440 {runId}`
6. Verifikasi menu baris memuat `Add Update` yang aktif
7. Arahkan kursor ke `Mark as Found` pada menu baris
8. Verifikasi `Mark as Found` Disabled
9. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Mark as Found` yang Disabled[^drift-1]
10. Arahkan kursor ke `Report Disposal` pada menu baris
11. Verifikasi `Report Disposal` Disabled
12. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Report Disposal` yang Disabled[^drift-1]
13. Tekan Esc untuk menutup menu baris
### PIC yang tercatat adalah Last Holder bagi pemegang tanpa akun
14. Verifikasi Last Holder baris `Pallet Stacker Electric {runId}` menampilkan `Joko S`
15. Verifikasi Reported By baris `Pallet Stacker Electric {runId}` menampilkan `Andi P (on behalf of Joko S)`
16. Klik `⋯` pada baris `Pallet Stacker Electric {runId}`
17. Arahkan kursor ke `Review` pada menu baris
18. Verifikasi `Review` Disabled
19. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Review` yang Disabled[^drift-1]
20. Arahkan kursor ke `Mark as Found` pada menu baris
21. Verifikasi `Mark as Found` Disabled bagi PIC yang tercatat
22. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Mark as Found` yang Disabled bagi PIC[^drift-1]
23. Tekan Esc untuk menutup menu baris
24. Klik nama `Pallet Stacker Electric {runId}` pada kolom Name
25. Verifikasi footer `[Reject]` dan `[Confirm]` tampil dan Disabled
26. Arahkan kursor ke `[Confirm]` pada footer dialog Missing Log
27. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada footer `[Confirm]` yang Disabled[^drift-1]
28. Klik `✕` pada dialog Missing Log
### Admin lain yang bukan Last Holder tidak terhalang
29. Masuk sebagai Rina W
30. Ketik Search `{runId}`, tekan Enter
31. Klik `⋯` pada baris `Laptop Dell Latitude 7440 {runId}`
32. Verifikasi `Mark as Found` aktif
33. Verifikasi `Report Disposal` aktif
34. Tekan Esc untuk menutup menu baris
35. Klik `⋯` pada baris `Pallet Stacker Electric {runId}`
36. Verifikasi `Review` aktif
37. Verifikasi `Mark as Found` aktif pada baris ini
### Total Control yang menjadi Last Holder tidak dapat Review dan Mark as Found
38. Ketik Search `{runId}`, tekan Enter
39. Verifikasi Last Holder baris `Mesin Label Printer {runId}` menampilkan `Rina W`
40. Klik `⋯` pada baris `Mesin Label Printer {runId}`
41. Arahkan kursor ke `Review` pada menu baris
42. Verifikasi `Review` Disabled bagi Total Control yang menjadi Last Holder
43. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Review` yang Disabled bagi Total Control[^drift-1]
44. Arahkan kursor ke `Mark as Found` pada menu baris
45. Verifikasi `Mark as Found` Disabled bagi Total Control yang menjadi Last Holder
46. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Mark as Found` yang Disabled bagi Total Control[^drift-1]
47. Tekan Esc untuk menutup menu baris
48. Klik nama `Mesin Label Printer {runId}` pada kolom Name
49. Verifikasi footer `[Reject]` dan `[Confirm]` tampil dan Disabled bagi Total Control yang menjadi Last Holder
50. Klik `✕` pada dialog Missing Log
### Manage asset & TAG (Update) yang menjadi Last Holder tidak dapat Review dan Confirm
51. Keluar dari akun
52. Masuk sebagai `Bimo Tirta {runId}`
53. Ketik Search `{runId}`, tekan Enter
54. Verifikasi Last Holder baris `Scanner Barcode Zebra {runId}` menampilkan `Bimo T`
55. Klik `⋯` pada baris `Scanner Barcode Zebra {runId}`
56. Arahkan kursor ke `Review` pada menu baris
57. Verifikasi `Review` Disabled bagi Manage asset & TAG (Update) yang menjadi Last Holder
58. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Review` yang Disabled bagi Manage asset & TAG (Update)[^drift-1]
59. Tekan Esc untuk menutup menu baris
60. Klik nama `Scanner Barcode Zebra {runId}` pada kolom Name
61. Verifikasi footer `[Reject]` dan `[Confirm]` tampil dan Disabled bagi Manage asset & TAG (Update) yang menjadi Last Holder
62. Klik `✕` pada dialog Missing Log
### Manage asset & TAG (Update) yang menjadi Last Holder tidak dapat Report Disposal record Missing
63. Ketik Search `{runId}`, tekan Enter
64. Verifikasi Last Holder baris `Printer HP LaserJet Pro {runId}` menampilkan `Bimo T`
65. Verifikasi Status baris `Printer HP LaserJet Pro {runId}` menampilkan `Missing`
66. Klik `⋯` pada baris `Printer HP LaserJet Pro {runId}`
67. Arahkan kursor ke `Report Disposal` pada menu baris
68. Verifikasi `Report Disposal` Disabled bagi Manage asset & TAG (Update) yang menjadi Last Holder
69. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Report Disposal` yang Disabled bagi Manage asset & TAG (Update)[^drift-1]
70. Tekan Esc untuk menutup menu baris
### Total Control yang menjadi Last Holder tidak dapat Report Disposal record Missing
71. Keluar dari akun
72. Masuk sebagai Rina W
73. Ketik Search `{runId}`, tekan Enter
74. Verifikasi Last Holder baris `Proyektor Epson EB-X49 {runId}` menampilkan `Rina W`
75. Verifikasi Status baris `Proyektor Epson EB-X49 {runId}` menampilkan `Missing`
76. Klik `⋯` pada baris `Proyektor Epson EB-X49 {runId}`
77. Arahkan kursor ke `Report Disposal` pada menu baris
78. Verifikasi `Report Disposal` Disabled bagi Total Control yang menjadi Last Holder
79. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Report Disposal` yang Disabled bagi Total Control[^drift-1]
80. Tekan Esc untuk menutup menu baris
### PIC yang tercatat tidak dapat Report Disposal record Missing atas pemegang tanpa akun
81. Keluar dari akun
82. Masuk sebagai Andi P
83. Ketik Search `{runId}`, tekan Enter
84. Verifikasi Last Holder baris `Trolley Dorong Gudang {runId}` menampilkan `Joko S`
85. Verifikasi Reported By baris `Trolley Dorong Gudang {runId}` menampilkan `Andi P (on behalf of Joko S)`
86. Verifikasi Status baris `Trolley Dorong Gudang {runId}` menampilkan `Missing`
87. Klik `⋯` pada baris `Trolley Dorong Gudang {runId}`
88. Arahkan kursor ke `Report Disposal` pada menu baris
89. Verifikasi `Report Disposal` Disabled bagi PIC yang tercatat pada record Missing
90. Verifikasi alasan `You were holding this asset. Ask another admin.` tersampaikan pada `Report Disposal` yang Disabled bagi PIC pada record Missing[^drift-1]
91. Tekan Esc untuk menutup menu baris

[^drift-1]: Drift PRD vs kontrak komponen. PRD §4.5: «Tooltip Disabled 🔖 dapat diakses lewat fokus.»; kontrak `Tooltip#38`: «A disabled control cannot be focused, so its tooltip opens on hover only.», `Button#2`: «A disabled button (`disabled`) is a native disabled button with `aria-disabled="true"`: it cannot take focus» dan `Menu#6`: item menu yang disabled dilewati Tab dan tombol panah. Diasersi: kontrak, sehingga alasan pada item menu dan tombol yang Disabled dibuka lewat hover, bukan fokus keyboard (SB-7).
