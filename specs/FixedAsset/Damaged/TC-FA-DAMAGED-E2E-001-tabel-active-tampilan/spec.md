---
id: TC-FA-DAMAGED-E2E-001-tabel-active-tampilan
title: "Sub-tab Active menampilkan record berjalan dengan kolom, badge status, penanda, dan urutan default"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, "§4.1#r1", "§4.1#p3", "§4.1#p4", "§4.2.1#p1", "§4.2.1#b1", "§4.2.1#b2", "§4.2.1#b4", "§4.4#r1", "§4.4#r11", "§5#r1", "§9.2#b12", "§9.5#r1", "§9.5#r2", "§9.5#r5", S-DMG-02, F-DMG-02, "§Aturan Logika Modul#r11", "§Aturan Logika Modul#r13", "§8.1#r2", "§9.2#b4"]
smoke: []
dependsOn: []
trace:
  T-DMG-01: [19, 68, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 67]
  "§4.1#r1": [12, 14, 19]
  "§4.1#p3": [24, 25, 26, 27, 28, 29, 68]
  "§4.1#p4": [48]
  "§4.2.1#p1": [2, 4, 12]
  "§4.2.1#b1": [16]
  "§4.2.1#b2": [3]
  "§4.2.1#b4": [51, 54, 55, 58]
  "§4.4#r1": [8, 11, 75, 77, 78, 79, 80, 81]
  "§4.4#r11": [61, 62]
  "§5#r1": [12, 14, 15]
  "§9.2#b12": [19, 20]
  "§9.5#r1": [5]
  "§9.5#r2": [22, 23]
  "§9.5#r5": [21]
  S-DMG-02: [28, 29]
  F-DMG-02: [12, 19]
  "§Aturan Logika Modul#r11": [49]
  "§Aturan Logika Modul#r13": [38]
  "§8.1#r2": [63]
  "§9.2#b4": [30, 31, 32, 33, 34, 35, 36, 37]
anchor: []
coverage:
  web: automated
---

# Sub-tab Active menampilkan record berjalan dengan kolom, badge status, penanda, dan urutan default

## Prerequisites
- Aktor: Total Control, user `Admin T`.
- Layar awal: halaman Assets.
- Data:
  - DU-001-1: record `Waiting for Confirmation`, Name `Laptop Dell Latitude {runId} - 4`, Asset ID `LPT-0004-{runId}`, Group `Head Office {runId}`, Source `Reported by holder`, Last Holder `Budi S`, Reported By `Budi S`, Reported Date `T0 − 1 hari, pukul 08:15`, Days Damaged `1 day`.
  - DU-001-2: record `In Disposal Process`, Name `Monitor Dell P2422H {runId} - 6`, Asset ID `MON-0006-{runId}`, Group `Head Office {runId}`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 52 hari, pukul 14:20`, Days Damaged `52 days`.
  - DU-001-3: record `Reported Disposal`, Name `Printer HP LaserJet M404 {runId} - 8`, Asset ID `PRN-0008-{runId}`, Group `Head Office {runId}`, Source `Audit`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 27 hari, pukul 10:00`, Days Damaged `27 days`.
  - DU-001-4: record `Damaged` berpenanda `Reported Missing`, Name `Drill Bosch GSB {runId} - 6`, Asset ID `DRL-0006-{runId}`, Group `Warehouse {runId}`, Source `Manual`, Last Holder `Sari D`, Reported By `Agus P`, Reported Date `T0 − 14 hari, pukul 10:00`, Days Damaged `14 days`.
  - DU-001-5: record `Damaged` berpenanda `Missing`, Name `Camera Canon EOS {runId} - 3`, Asset ID `CAM-0003-{runId}`, Group `Head Office {runId}`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 8 hari, pukul 11:00`, Days Damaged `8 days`, Modified By `System`.
  - DU-001-6: record `Damaged`, Name `Projector Epson EB-X06 {runId} - 2`, Asset ID `PRJ-0002-{runId}`, Group `Head Office {runId}`, Source `Borrow return`, Last Holder `Sari D`, Reported By `Rina W`, Reported Date `T0 − 7 hari, pukul 17:10`, Days Damaged `7 days`.
  - DU-001-7: record `Damaged`, Name `Office Chair Ergo {runId} - 31`, Asset ID `CHR-0031-{runId}`, Group `Branch Surabaya {runId}`, Source `Reported by scan`, Last Holder `—`, Reported By `Dedi K`, Reported Date `T0 − 5 hari, pukul 13:00`, Days Damaged `5 days`.
  - DU-001-8: record `Damaged`, Name `Laptop Dell Latitude {runId} - 6`, Asset ID `LPT-0006-{runId}`, Group `Head Office {runId}`, Source `Missing asset`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 2 hari, pukul 15:20`, Days Damaged `2 days`.
  - DU-001-9: record `Damaged`, Name `Projector Epson EB-X06 {runId} - 7`, Asset ID `PRJ-0007-{runId}`, Group `Branch Surabaya {runId}`, Source `Registration`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 3 hari, pukul 09:00`, Days Damaged `3 days`.
  - DU-001-10: record `Damaged`, Name `Forklift Toyota 8FD {runId} - 1`, Asset ID `FLT-0001-{runId}`, Group `Head Office {runId}`, Source `Transfer receive`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 6 hari, pukul 14:00`, Days Damaged `6 days`.
  - DU-001-11: record `Repaired` (sudah selesai), Name `Projector Epson EB-X06 {runId} - 5`, Asset ID `PRJ-0005-{runId}`, Group `Head Office {runId}`, Source `Registration`, Reported By `Rina W`, Reported Date `T0 − 3 hari, pukul 09:00`.
  - DU-001-12: record `Waiting for Confirmation`, Name `Scanner Fujitsu fi-7160 {runId} - 2`, Asset ID `SCN-0002-{runId}`, Group `Head Office {runId}`, Source `Reported by holder`, Last Holder `Admin T`, Reported By `Admin T`, Reported Date `T0 − 2 hari, pukul 10:30`, Days Damaged `2 days`; pelapornya adalah aktor spec ini sendiri.
  - DU-001-1 sampai DU-001-10 dan DU-001-12 adalah `11` record berjalan milik spec ini; Group `Branch Surabaya {runId}` memuat `2` record berjalan, yaitu DU-001-7 dan DU-001-9.
  - Urutan pembuatan menurut tanggal laporan terlama: DU-001-2, DU-001-3, DU-001-4, DU-001-5, DU-001-6, DU-001-10, DU-001-7, DU-001-9, DU-001-8; DU-001-1 dan DU-001-12 adalah record `Waiting for Confirmation`.
  - User pelapor dan pemegang pada data di atas adalah user ber-runId di entitas aktor dengan nama tampil `Budi S` (pemegang dan pelapor umum, tanpa hak Aktor Damaged), `Sari D` (pemegang aset), `Dedi K` (pelapor umum lewat scan), serta `Rina W` dan `Agus P` (Pelapor admin, pemegang Manage asset & TAG dengan Update pada Group aset).
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.
  - Time Zone bernilai `Asia/Jakarta`.
  - Level Feature Suite Disposal bernilai `Basic`.

## Test Steps

### Tab Damaged membuka sub-tab Active sebagai sub-tab awal
1. Buka tab `Damaged` pada halaman Assets
2. Verifikasi tab `Assets`, `Registration`, `Damaged`, dan `Missing` tampil pada halaman Assets
3. Verifikasi tab `Damaged` menampilkan badge jumlah record
4. Verifikasi sub-tab `Active` dan `History` tampil
5. Verifikasi sub-tab `Active` aktif sebagai sub-tab awal

### Sub-tab aktif tersimpan di URL
6. Klik sub-tab `History`
7. Muat ulang halaman
8. Verifikasi sub-tab `History` tetap aktif sesudah muat ulang
9. Klik sub-tab `Active`
10. Muat ulang halaman
11. Verifikasi sub-tab `Active` tetap aktif sesudah muat ulang

### Toolbar sub-tab Active tanpa tombol Report Damaged
12. Verifikasi ikon `Search`, `Filter`, dan `Download` tampil pada toolbar sub-tab Active
13. Klik ikon `Search`
14. Verifikasi tombol `Search by Scan` tampil di dalam kotak Search
15. Verifikasi placeholder kotak Search adalah `Search asset name or ID...`
16. Verifikasi tab `Damaged` tidak memiliki tombol `[Report Damaged]`

### Tabel hanya memuat record berjalan milik spec ini
17. Ketik Search `{runId}`, tekan Enter
18. Ubah ukuran halaman menjadi `25`
19. Verifikasi tabel memuat `11` baris, yaitu DU-001-1 sampai DU-001-10 dan DU-001-12
20. Verifikasi record `Projector Epson EB-X06 {runId} - 5` yang berstatus `Repaired` tidak tampil di sub-tab Active
21. Verifikasi ikon `Filter` tidak menampilkan badge titik saringan aktif

### Urutan default record berjalan
22. Verifikasi baris pertama adalah record `Waiting for Confirmation` `Scanner Fujitsu fi-7160 {runId} - 2` (Days Damaged `2 days`) dan baris kedua adalah record `Waiting for Confirmation` `Laptop Dell Latitude {runId} - 4` (Days Damaged `1 day`), karena antar-record `Waiting for Confirmation` Days Damaged terlama dulu
23. Verifikasi urutan baris sesudah kedua record itu, dari atas, antar-record status lain menurut Days Damaged terlama dulu, adalah `Monitor Dell P2422H {runId} - 6`, `Printer HP LaserJet M404 {runId} - 8`, `Drill Bosch GSB {runId} - 6`, `Camera Canon EOS {runId} - 3`, `Projector Epson EB-X06 {runId} - 2`, `Forklift Toyota 8FD {runId} - 1`, `Office Chair Ergo {runId} - 31`, `Projector Epson EB-X06 {runId} - 7`, `Laptop Dell Latitude {runId} - 6`

### Badge status dan penanda Missing pada setiap status record
24. Verifikasi baris `Laptop Dell Latitude {runId} - 4` menampilkan badge status `Waiting for Confirmation`
25. Verifikasi baris `Monitor Dell P2422H {runId} - 6` menampilkan badge status `In Disposal Process`
26. Verifikasi baris `Printer HP LaserJet M404 {runId} - 8` menampilkan badge status `Reported Disposal`
27. Verifikasi baris `Projector Epson EB-X06 {runId} - 2` menampilkan badge status `Damaged`
28. Verifikasi baris `Drill Bosch GSB {runId} - 6` menampilkan badge status `Damaged` disertai penanda `Reported Missing`
29. Verifikasi baris `Camera Canon EOS {runId} - 3` menampilkan badge status `Damaged` disertai penanda `Missing`

### Kolom Source menunjukkan titik masuk laporan pertama
30. Verifikasi kolom Source baris `Laptop Dell Latitude {runId} - 4` bernilai `Reported by holder`
31. Verifikasi kolom Source baris `Monitor Dell P2422H {runId} - 6` bernilai `Manual`
32. Verifikasi kolom Source baris `Printer HP LaserJet M404 {runId} - 8` bernilai `Audit`
33. Verifikasi kolom Source baris `Projector Epson EB-X06 {runId} - 2` bernilai `Borrow return`
34. Verifikasi kolom Source baris `Office Chair Ergo {runId} - 31` bernilai `Reported by scan`
35. Verifikasi kolom Source baris `Laptop Dell Latitude {runId} - 6` bernilai `Missing asset`
36. Verifikasi kolom Source baris `Projector Epson EB-X06 {runId} - 7` bernilai `Registration`
37. Verifikasi kolom Source baris `Forklift Toyota 8FD {runId} - 1` bernilai `Transfer receive`

### Isi kolom data setiap baris
38. Verifikasi baris `Laptop Dell Latitude {runId} - 4` memuat Asset ID `LPT-0004-{runId}`, Group `Head Office {runId}`, Last Holder `Budi S`, Reported By `Budi S`, Reported Date pukul `08:15`, dan Days Damaged `1 day`
39. Verifikasi baris `Monitor Dell P2422H {runId} - 6` memuat Asset ID `MON-0006-{runId}`, Group `Head Office {runId}`, Last Holder `—`, Reported By `Rina W`, Reported Date pukul `14:20`, dan Days Damaged `52 days`
40. Verifikasi baris `Printer HP LaserJet M404 {runId} - 8` memuat Asset ID `PRN-0008-{runId}`, Group `Head Office {runId}`, Last Holder `—`, Reported By `Agus P`, Reported Date pukul `10:00`, dan Days Damaged `27 days`
41. Verifikasi baris `Drill Bosch GSB {runId} - 6` memuat Asset ID `DRL-0006-{runId}`, Group `Warehouse {runId}`, Last Holder `Sari D`, Reported By `Agus P`, Reported Date pukul `10:00`, dan Days Damaged `14 days`
42. Verifikasi baris `Camera Canon EOS {runId} - 3` memuat Asset ID `CAM-0003-{runId}`, Group `Head Office {runId}`, Last Holder `—`, Reported By `Agus P`, Reported Date pukul `11:00`, dan Days Damaged `8 days`
43. Verifikasi baris `Projector Epson EB-X06 {runId} - 2` memuat Asset ID `PRJ-0002-{runId}`, Group `Head Office {runId}`, Last Holder `Sari D`, Reported By `Rina W`, Reported Date pukul `17:10`, dan Days Damaged `7 days`
44. Verifikasi baris `Office Chair Ergo {runId} - 31` memuat Asset ID `CHR-0031-{runId}`, Group `Branch Surabaya {runId}`, Last Holder `—`, Reported By `Dedi K`, Reported Date pukul `13:00`, dan Days Damaged `5 days`
45. Verifikasi baris `Laptop Dell Latitude {runId} - 6` memuat Asset ID `LPT-0006-{runId}`, Group `Head Office {runId}`, Last Holder `—`, Reported By `Rina W`, Reported Date pukul `15:20`, dan Days Damaged `2 days`
46. Verifikasi baris `Projector Epson EB-X06 {runId} - 7` memuat Asset ID `PRJ-0007-{runId}`, Group `Branch Surabaya {runId}`, Last Holder `—`, Reported By `Rina W`, Reported Date pukul `09:00`, dan Days Damaged `3 days`
47. Verifikasi baris `Forklift Toyota 8FD {runId} - 1` memuat Asset ID `FLT-0001-{runId}`, Group `Head Office {runId}`, Last Holder `—`, Reported By `Agus P`, Reported Date pukul `14:00`, dan Days Damaged `6 days`
48. Verifikasi Reported Date baris `Monitor Dell P2422H {runId} - 6` tampil sebagai tanggal `T0 − 52 hari` menurut Date Format `dd/MM/yy` dan pukul `14:20` menurut Time Format `24h`

### Record tidak memiliki nomor transaksi
49. Verifikasi tabel tidak memiliki kolom nomor transaksi

### Group difilter lewat Filter Panel
50. Klik ikon `Filter`
51. Verifikasi Filter Panel menampilkan field `Group`
52. Pilih Group `Branch Surabaya {runId}` pada field `Group`
53. Klik `[Apply]`
54. Verifikasi tabel memuat `2` baris
55. Verifikasi baris yang tampil adalah `Office Chair Ergo {runId} - 31` dan `Projector Epson EB-X06 {runId} - 7`
56. Klik `[Clear Field]`
57. Klik `[Apply]`
58. Verifikasi tabel kembali memuat `11` baris
59. Klik ikon `Filter` untuk menutup Filter Panel

### Damage Log terbuka dari kolom Name
60. Klik nama aset `Laptop Dell Latitude {runId} - 4`
61. Verifikasi dialog `Damage Log` terbuka
62. Verifikasi dialog `Damage Log` menampilkan aset `Laptop Dell Latitude {runId} - 4`
63. Verifikasi judul dialog adalah `Damage Log` tanpa nomor transaksi
64. Tekan `Esc`

### Aktor sistem pada kolom Modified By
65. Klik header kolom Actions `⋯`
66. Centang `Modified By`
67. Verifikasi kolom `Modified By` baris `Camera Canon EOS {runId} - 3` bernilai `System`

### Record Waiting for Confirmation yang dilaporkan aktor sendiri
68. Verifikasi baris `Scanner Fujitsu fi-7160 {runId} - 2` menampilkan badge status `Waiting for Confirmation` dan Reported By `Admin T`

### State Search, Filter, dan Sort sub-tab Active bertahan sesudah muat ulang
69. Klik ikon sort pada header kolom `Name`
70. Klik ikon sort pada header kolom `Name`
71. Klik ikon `Filter`
72. Pilih Group `Branch Surabaya {runId}` pada field `Group`
73. Klik `[Apply]`
74. Klik ikon `Filter` untuk menutup Filter Panel
75. Verifikasi baris berurutan menurun menurut Name: `Projector Epson EB-X06 {runId} - 7`, lalu `Office Chair Ergo {runId} - 31`
76. Muat ulang halaman
77. Verifikasi sub-tab `Active` tetap aktif sesudah muat ulang
78. Verifikasi kotak Search tetap berisi `{runId}` sesudah muat ulang
79. Verifikasi ikon `Filter` tetap menampilkan badge titik saringan aktif sesudah muat ulang
80. Verifikasi tabel tetap memuat `2` baris, yaitu `Office Chair Ergo {runId} - 31` dan `Projector Epson EB-X06 {runId} - 7`
81. Verifikasi urutan sort Name menurun tetap berlaku sesudah muat ulang: baris pertama `Projector Epson EB-X06 {runId} - 7`, baris kedua `Office Chair Ergo {runId} - 31`
