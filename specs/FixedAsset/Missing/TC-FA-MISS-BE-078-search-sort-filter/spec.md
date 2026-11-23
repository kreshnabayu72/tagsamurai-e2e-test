---
id: TC-FA-MISS-BE-078-search-sort-filter
title: "Server: Search per kelas kolom termasuk nama PIC dan karyawan, urutan sort per tipe termasuk TAG multi-ikon, filter AND antar field dan OR dalam field, Long missing checkbox"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [EB-SRC-1, EB-SRT-1, EB-SRT-2, EB-FLT-3, §5#r3, §4.1#p5, §4.1a#r6, §4.1a#r15, §4.1b#r6, §4.1b#r14, §9.5#r2, §9.5#r3, §4.1a#r2, §4.1b#r2, §9.2#b14, §4.1a#p1, §9.11#b1, §9.10#p1]
smoke: []
dependsOn: []
trace:
  EB-SRC-1: [2, 4, 6, 8, 10, 12, 20, 22, 24, 26]
  EB-SRT-1: [30, 32, 34, 38, 40, 50, 52]
  EB-SRT-2: [34, 36, 40, 44, 46, 54]
  EB-FLT-3: [56, 58, 60, 71]
  §5#r3: [2, 4, 26]
  §4.1#p5: [14, 16, 18, 42, 44, 64, 66, 69, 80, 82]
  §4.1a#r6: [34, 36]
  §4.1a#r15: [38, 62]
  §4.1b#r6: 54
  §4.1b#r14: [50, 71]
  §9.5#r2: 28
  §9.5#r3: 48
  §4.1a#r2: [30, 32]
  §4.1b#r2: 52
  §9.2#b14: 68
  §4.1a#p1: 62
  §9.11#b1: [73, 75]
  §9.10#p1: [77, 78]
---

# Server: Search per kelas kolom termasuk nama PIC dan karyawan, urutan sort per tipe termasuk TAG multi-ikon, filter AND antar field dan OR dalam field, Long missing checkbox

## Prerequisites
- Aktor: Rina W, Total Control dengan cakupan seluruh client; `Hari Susanto {runId}` (DU-078-1), pemegang View asset value dengan Group Head Office beserta descendant.
- Data:
  - DU-078-1: User Name `Hari Susanto {runId}`, Peran `View asset value`, Cakupan `Group Head Office beserta descendant`.
  - DU-078-2: User Name `Rudi Hartono {runId}`, Peran `PIC yang melapor atas nama karyawan tanpa akun`, Cakupan `aset karyawan yang ia wakili`.
  - DU-078-3: User Name `Joko Susilo {runId}`, Peran `karyawan tanpa akun`, Cakupan `tanpa akses`.
  - DU-078-4: User Name `Budi Santoso {runId}`, Peran `karyawan tanpa akun`, Cakupan `tanpa akses`.
  - DU-078-5: User Name `Sari Dewi {runId}`, Peran `pemegang tanpa hak Aktor Missing`, Cakupan `aset yang ia pegang`.
  - DU-078-6: User Name `Agus Pratama {runId}`, Peran `pengguna terautentikasi tanpa hak Aktor Missing`, Cakupan `tanpa cakupan Group`.
  - DU-078-7: Asset Name `Camera Canon EOS {runId}`, Increment `1`, Name tampil `Camera Canon EOS {runId} - 1`, Asset ID `FA078-001`, Status `Missing`, Source `Borrow`, TAG `NFC`, Last Holder `Budi Santoso {runId}`, Reported By `Rina W`, Reported Date `T0 − 5 hari, pukul 09:00`, Purchase Cost `12500000`, Asset Value (Commercial) `9800000`.
  - DU-078-8: Asset Name `Drill Bosch GSB {runId}`, Increment `1`, Name tampil `Drill Bosch GSB {runId} - 1`, Asset ID `FA078-002`, Status `Missing`, Source `Manual`, TAG `NFC, QR`, Last Holder `tidak ada`, Reported By `Rina W`, Reported Date `T0 − 12 hari, pukul 09:00`.
  - DU-078-9: Asset Name `Hand Pallet Truck {runId}`, Increment `1`, Name tampil `Hand Pallet Truck {runId} - 1`, Asset ID `FA078-003`, Status `Reported Disposal`, Source `Transfer`, TAG `QR`, Last Holder `tidak ada`, Reported By `Rina W`, Reported Date `T0 − 40 hari, pukul 09:00`.
  - DU-078-10: Asset Name `Hand Pallet Truck {runId}`, Increment `2`, Name tampil `Hand Pallet Truck {runId} - 2`, Asset ID `FA078-004`, Status `In Disposal Process`, Source `Manual`, TAG `tidak ada`, Last Holder `tidak ada`, Reported By `Rina W`, Reported Date `T0 − 20 hari, pukul 09:00`.
  - DU-078-11: Asset Name `Hand Pallet Truck {runId}`, Increment `10`, Name tampil `Hand Pallet Truck {runId} - 10`, Asset ID `FA078-005`, Status `Missing`, Source `Borrow`, TAG `RFID`, Last Holder `Joko Susilo {runId}`, Reported By `Rudi Hartono {runId} (on behalf of Joko Susilo {runId})`, Reported Date `T0 − 45 hari, pukul 09:00`, Penanda `Long missing`.
  - DU-078-12: Asset Name `Laptop Dell Latitude 5420 {runId}`, Increment `1`, Name tampil `Laptop Dell Latitude 5420 {runId} - 1`, Asset ID `FA078-006`, Status `Waiting for Confirmation`, Source `Reported by holder`, TAG `BLE`, Last Holder `Sari Dewi {runId}`, Reported By `Sari Dewi {runId}`, Reported Date `T0 − 2 hari, pukul 09:00`.
  - DU-078-13: Asset Name `Monitor LG 27UL500 {runId}`, Increment `1`, Name tampil `Monitor LG 27UL500 {runId} - 1`, Asset ID `FA078-007`, Status `Missing`, Source `Audit`, TAG `GPS`, Last Holder `tidak ada`, Reported By `Agus Pratama {runId}`, Reported Date `T0 − 8 hari, pukul 09:00`.
  - DU-078-14: Asset Name `Rak Gudang Timur 50% {runId}`, Increment `1`, Name tampil `Rak Gudang Timur 50% {runId} - 1`, Asset ID `FA078-008`, Status `Missing`, Source `Manual`, TAG `tidak ada`, Last Holder `tidak ada`, Reported By `Rina W`, Reported Date `T0 − 6 hari, pukul 09:00`.
  - DU-078-15: Asset Name `Rak Gudang Timur 5001 {runId}`, Increment `1`, Name tampil `Rak Gudang Timur 5001 {runId} - 1`, Asset ID `FA078-009`, Status `Missing`, Source `Manual`, TAG `tidak ada`, Last Holder `tidak ada`, Reported By `Rina W`, Reported Date `T0 − 7 hari, pukul 09:00`.
  - DU-078-16: Asset Name `Projector Epson EB-X06 {runId}`, Increment `1`, Name tampil `Projector Epson EB-X06 {runId} - 1`, Asset ID `FA078-011`, Status `Found`, Source `Borrow`, TAG `NFC`, Reported By `Rina W`, Reported Date `T0 − 30 hari, pukul 09:00`, Resolved By `Rina W`, Resolved Date `T0 − 20 hari, pukul 09:00`, Duration `10 days`.
  - DU-078-17: Asset Name `Printer HP LaserJet M404 {runId}`, Increment `1`, Name tampil `Printer HP LaserJet M404 {runId} - 1`, Asset ID `FA078-012`, Status `Disposed`, Source `Reconciliation`, TAG `NFC, QR`, Reported By `Rina W`, Reported Date `T0 − 90 hari, pukul 09:00`, Resolved By `System`, Resolved Date `T0 − 10 hari, pukul 09:00`, Duration `80 days`.
  - DU-078-18: Asset Name `Toyota Innova {runId}`, Increment `1`, Name tampil `Toyota Innova {runId} - 1`, Asset ID `FA078-013`, Status `Rejected`, Source `Reported by holder`, TAG `QR`, Reported By `Rina W`, Reported Date `T0 − 7 hari, pukul 09:00`, Resolved By `Rina W`, Resolved Date `T0 − 6 hari, pukul 09:00`, Duration `1 day`.
  - DU-078-19: Asset Name `Kamera Sony A7 {runId}`, Increment `1`, Name tampil `Kamera Sony A7 {runId} - 1`, Asset ID `FA078-014`, Status `Canceled`, Source `Reported by holder`, TAG `tidak ada`, Reported By `Rina W`, Reported Date `T0 − 10 hari, pukul 09:00`, Resolved By `Rina W`, Resolved Date `T0 − 7 hari, pukul 09:00`, Duration `3 days`.
  - DU-078-20: Asset Name `Vacuum Cleaner Industri {runId}`, Increment `1`, Name tampil `Vacuum Cleaner Industri {runId} - 1`, Asset ID `FA078-015`, Status `Canceled`, Source `Reported by holder`, TAG `RFID`, Reported By `Rudi Hartono {runId} (on behalf of Joko Susilo {runId})`, Reported Date `T0 − 200 hari, pukul 09:00`, Resolved By `Rudi Hartono {runId} (on behalf of Joko Susilo {runId})`, Resolved Date `T0 − 100 hari, pukul 09:00`, Duration `100 days`.
- Kondisi:
  - Plan client membuka semua tipe TAG `RFID`, `NFC`, `QR`, `BLE`, dan `GPS`
  - Date Format bernilai `DD/MM/YY`
  - Time Format bernilai `HH:mm`

## Test Steps
### Search Active mencocokkan substring tanpa membedakan huruf besar kecil per kelas kolom
1. Rina W mengambil daftar sub-tab Active dengan Search `camera canon`
2. Verifikasi hasil memuat baris `Camera Canon EOS {runId} - 1`
3. Rina W mengambil daftar sub-tab Active dengan Search `CAMERA CANON`
4. Verifikasi hasil memuat baris `Camera Canon EOS {runId} - 1`, sama dengan hasil Search huruf kecil
5. Rina W mengambil daftar sub-tab Active dengan Search `anon eo`
6. Verifikasi hasil memuat baris `Camera Canon EOS {runId} - 1` karena kata kunci di tengah nama dicocokkan sebagai substring
7. Rina W mengambil daftar sub-tab Active dengan Search `FA078-003`
8. Verifikasi hasil memuat baris `Hand Pallet Truck {runId} - 1` dan tidak memuat baris `Camera Canon EOS {runId} - 1`
9. Rina W mengambil daftar sub-tab Active dengan Search `Reported Disposal`
10. Verifikasi hasil memuat baris `Hand Pallet Truck {runId} - 1` berstatus `Reported Disposal` dan tidak memuat baris `Laptop Dell Latitude 5420 {runId} - 1`
11. Rina W mengambil daftar sub-tab Active dengan Search `RFID`
12. Verifikasi hasil memuat baris `Hand Pallet Truck {runId} - 10` yang memakai ikon TAG berlabel `RFID` dan tidak memuat baris `Camera Canon EOS {runId} - 1`
13. Rina W mengambil daftar sub-tab Active dengan Search `Rudi`
14. Verifikasi hasil memuat baris `Hand Pallet Truck {runId} - 10` karena Search mencocokkan nama PIC yang melapor
15. Rina W mengambil daftar sub-tab Active dengan Search `Joko Susilo {runId}`
16. Verifikasi hasil memuat baris `Hand Pallet Truck {runId} - 10` karena Search mencocokkan nama karyawan yang diwakili
17. Rina W mengambil daftar sub-tab Active dengan Search `Budi Santoso {runId}`
18. Verifikasi hasil memuat baris `Camera Canon EOS {runId} - 1` karena `Budi Santoso {runId}` adalah Last holder pada baris itu
19. Rina W mengambil daftar sub-tab Active dengan Search `45 days`
20. Verifikasi hasil tidak memuat baris `Hand Pallet Truck {runId} - 10` karena kolom Days Missing tidak ikut Search
21. Rina W mengambil daftar sub-tab Active dengan Search `50%`
22. Verifikasi hasil memuat baris `Rak Gudang Timur 50% {runId} - 1` dan tidak memuat baris `Rak Gudang Timur 5001 {runId} - 1`, karena tanda persen dicocokkan sebagai teks biasa
23. Rina W mengambil daftar sub-tab Active dengan Search `zzq-078-tidak-ada`
24. Verifikasi hasil tidak memuat satu baris pun sehingga tampil `No results found`

### Search History terpisah dari Active
25. Rina W mengambil daftar sub-tab History dengan Search `projector`
26. Verifikasi hasil memuat baris `Projector Epson EB-X06 {runId} - 1` dan Search yang sama pada sub-tab Active tidak memuat baris itu

### Urutan sort Active per tipe kolom
27. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` tanpa sort tambahan
28. Verifikasi urutan bawaan: baris `Laptop Dell Latitude 5420 {runId} - 1` berstatus `Waiting for Confirmation` paling atas, lalu `Hand Pallet Truck {runId} - 10`, `Hand Pallet Truck {runId} - 1`, `Hand Pallet Truck {runId} - 2`, `Drill Bosch GSB {runId} - 1`, `Monitor LG 27UL500 {runId} - 1`, `Rak Gudang Timur 5001 {runId} - 1`, `Rak Gudang Timur 50% {runId} - 1`, dan `Camera Canon EOS {runId} - 1` menurut Days Missing terlama dulu
29. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` diurutkan menurut Name ascending
30. Verifikasi urutan relatif baris: `Camera Canon EOS {runId} - 1`, lalu `Drill Bosch GSB {runId} - 1`, `Hand Pallet Truck {runId} - 1`, `Hand Pallet Truck {runId} - 2`, `Hand Pallet Truck {runId} - 10`, `Laptop Dell Latitude 5420 {runId} - 1`, dan `Monitor LG 27UL500 {runId} - 1`, dengan Increment dibandingkan sebagai angka sehingga 10 berada sesudah 2, lalu `Rak Gudang Timur 50% {runId} - 1` dan `Rak Gudang Timur 5001 {runId} - 1` berada sesudah `Monitor LG 27UL500 {runId} - 1` tanpa urutan di antara keduanya yang diasersi
31. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` diurutkan menurut Name descending
32. Verifikasi urutan relatif baris: `Rak Gudang Timur 50% {runId} - 1` dan `Rak Gudang Timur 5001 {runId} - 1` berada sebelum `Monitor LG 27UL500 {runId} - 1` tanpa urutan di antara keduanya yang diasersi, lalu `Monitor LG 27UL500 {runId} - 1`, `Laptop Dell Latitude 5420 {runId} - 1`, `Hand Pallet Truck {runId} - 10`, `Hand Pallet Truck {runId} - 2`, `Hand Pallet Truck {runId} - 1`, `Drill Bosch GSB {runId} - 1`, dan `Camera Canon EOS {runId} - 1`
33. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` diurutkan menurut TAG ascending
34. Verifikasi urutan baris menurut label ikon: `Laptop Dell Latitude 5420 {runId} - 1` (`BLE`), `Monitor LG 27UL500 {runId} - 1` (`GPS`), `Camera Canon EOS {runId} - 1` (`NFC`), `Drill Bosch GSB {runId} - 1` (`NFC, QR`), `Hand Pallet Truck {runId} - 1` (`QR`), lalu `Hand Pallet Truck {runId} - 10` (`RFID`), dan baris tanpa TAG paling akhir
35. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` diurutkan menurut TAG descending
36. Verifikasi urutan baris kebalikannya: baris tanpa TAG paling awal, lalu `Hand Pallet Truck {runId} - 10`, `Hand Pallet Truck {runId} - 1`, `Drill Bosch GSB {runId} - 1`, `Camera Canon EOS {runId} - 1`, `Monitor LG 27UL500 {runId} - 1`, dan `Laptop Dell Latitude 5420 {runId} - 1`
37. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` diurutkan menurut Days Missing ascending
38. Verifikasi urutan numerik baris: `Laptop Dell Latitude 5420 {runId} - 1`, `Camera Canon EOS {runId} - 1`, `Rak Gudang Timur 50% {runId} - 1`, `Rak Gudang Timur 5001 {runId} - 1`, `Monitor LG 27UL500 {runId} - 1`, `Drill Bosch GSB {runId} - 1`, `Hand Pallet Truck {runId} - 2`, `Hand Pallet Truck {runId} - 1`, lalu `Hand Pallet Truck {runId} - 10`
39. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` diurutkan menurut Status ascending
40. Verifikasi urutan label status: `Hand Pallet Truck {runId} - 2` (`In Disposal Process`), baris `Missing` (`Hand Pallet Truck {runId} - 10`, `Drill Bosch GSB {runId} - 1`, `Monitor LG 27UL500 {runId} - 1`, `Rak Gudang Timur 5001 {runId} - 1`, `Rak Gudang Timur 50% {runId} - 1`, `Camera Canon EOS {runId} - 1`), `Hand Pallet Truck {runId} - 1` (`Reported Disposal`), lalu `Laptop Dell Latitude 5420 {runId} - 1` (`Waiting for Confirmation`), dengan baris berstatus sama mengikuti urutan bawaan
41. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` diurutkan menurut Reported By ascending
42. Verifikasi urutan memakai nama PIC sebagai pelaku: baris `Monitor LG 27UL500 {runId} - 1` (Agus P) lebih dulu dari baris yang dilaporkan Rina W, lalu `Hand Pallet Truck {runId} - 10` (Rudi H), lalu `Laptop Dell Latitude 5420 {runId} - 1` (Sari D)
43. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` diurutkan menurut Last Holder ascending
44. Verifikasi urutan memakai nama karyawan: `Camera Canon EOS {runId} - 1` (`Budi Santoso {runId}`), lalu `Hand Pallet Truck {runId} - 10` (`Joko Susilo {runId}`), lalu `Laptop Dell Latitude 5420 {runId} - 1` (`Sari Dewi {runId}`), dan baris tanpa Last holder paling akhir
45. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` diurutkan menurut Last Holder descending
46. Verifikasi baris tanpa Last holder berada paling awal, lalu `Laptop Dell Latitude 5420 {runId} - 1`, `Hand Pallet Truck {runId} - 10`, dan `Camera Canon EOS {runId} - 1`

### Urutan bawaan dan sort History
47. Rina W mengambil daftar sub-tab History dengan Search `{runId}` tanpa sort tambahan
48. Verifikasi urutan bawaan menurut Resolved Date terbaru dulu: `Toyota Innova {runId} - 1`, lalu `Kamera Sony A7 {runId} - 1`, `Printer HP LaserJet M404 {runId} - 1`, `Projector Epson EB-X06 {runId} - 1`, dan terakhir `Vacuum Cleaner Industri {runId} - 1`
49. Rina W mengambil daftar sub-tab History dengan Search `{runId}` diurutkan menurut Duration ascending
50. Verifikasi urutan numerik baris: `Toyota Innova {runId} - 1` (`1 day`), `Kamera Sony A7 {runId} - 1` (`3 days`), `Projector Epson EB-X06 {runId} - 1` (`10 days`), lalu `Printer HP LaserJet M404 {runId} - 1` (`80 days`), dan terakhir `Vacuum Cleaner Industri {runId} - 1` (`100 days`)
51. Rina W mengambil daftar sub-tab History dengan Search `{runId}` diurutkan menurut Name ascending
52. Verifikasi urutan baris: `Kamera Sony A7 {runId} - 1`, lalu `Printer HP LaserJet M404 {runId} - 1`, `Projector Epson EB-X06 {runId} - 1`, `Toyota Innova {runId} - 1`, dan `Vacuum Cleaner Industri {runId} - 1`
53. Rina W mengambil daftar sub-tab History dengan Search `{runId}` diurutkan menurut TAG ascending
54. Verifikasi urutan baris menurut label ikon: `Projector Epson EB-X06 {runId} - 1` (`NFC`), `Printer HP LaserJet M404 {runId} - 1` (`NFC, QR`), `Toyota Innova {runId} - 1` (`QR`), lalu `Vacuum Cleaner Industri {runId} - 1` (`RFID`), dan `Kamera Sony A7 {runId} - 1` tanpa TAG paling akhir

### Filter OR dalam satu field, AND antar field, dan checkbox Long missing
55. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` dan filter Status `Missing` serta `Reported Disposal`
56. Verifikasi hasil memuat baris `Camera Canon EOS {runId} - 1`, `Drill Bosch GSB {runId} - 1`, `Hand Pallet Truck {runId} - 10`, `Monitor LG 27UL500 {runId} - 1`, dan `Hand Pallet Truck {runId} - 1`, serta tidak memuat baris `Hand Pallet Truck {runId} - 2` dan `Laptop Dell Latitude 5420 {runId} - 1`, karena dalam satu field berlaku OR
57. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` dan filter Status `Missing` serta Source `Borrow`
58. Verifikasi hasil memuat baris `Camera Canon EOS {runId} - 1` dan `Hand Pallet Truck {runId} - 10`, serta tidak memuat baris `Drill Bosch GSB {runId} - 1` (Source `Manual`) dan `Monitor LG 27UL500 {runId} - 1` (Source `Audit`), karena antar field berlaku AND
59. Rina W mengambil daftar sub-tab Active dengan Search `Hand Pallet` dan filter Status `Missing`
60. Verifikasi hasil memuat baris `Hand Pallet Truck {runId} - 10` dan tidak memuat baris `Hand Pallet Truck {runId} - 1` dan `Hand Pallet Truck {runId} - 2`, karena Search dan filter beroperasi sebagai irisan
61. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` dan filter checkbox `Long missing` pada Days Missing
62. Verifikasi hasil memuat baris `Hand Pallet Truck {runId} - 10` yang bertanda `Long missing` dan tidak memuat baris `Camera Canon EOS {runId} - 1`, `Hand Pallet Truck {runId} - 1`, maupun `Laptop Dell Latitude 5420 {runId} - 1`
63. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` dan filter Reported By `Rudi Hartono {runId}`
64. Verifikasi hasil memuat baris `Hand Pallet Truck {runId} - 10` karena filter Reported By memakai nama PIC
65. Rina W mengambil daftar sub-tab Active dengan Search `{runId}` dan filter Last Holder `Joko Susilo {runId}`
66. Verifikasi hasil memuat baris `Hand Pallet Truck {runId} - 10` karena filter Last Holder memakai nama karyawan
67. Rina W meminta opsi filter Source dan Last Holder pada sub-tab Active
68. Verifikasi opsi Source memuat nilai DISTINCT dari baris sub-tab Active, yaitu `Borrow`, `Manual`, `Transfer`, `Reported by holder`, dan `Audit`, tanpa `Reconciliation` yang hanya ada di History
69. Verifikasi opsi Last Holder dan Reported By memuat `Joko Susilo {runId}` sebagai karyawan tanpa akun dan `Rudi Hartono {runId}` sebagai PIC

### Filter Duration History inklusif di kedua ujung
70. Rina W mengambil daftar sub-tab History dengan Search `{runId}` dan filter Duration Min `3` dan Max `10`
71. Verifikasi hasil memuat baris `Kamera Sony A7 {runId} - 1` (`3 days`) dan `Projector Epson EB-X06 {runId} - 1` (`10 days`), serta tidak memuat baris `Toyota Innova {runId} - 1` dan `Printer HP LaserJet M404 {runId} - 1`

### Pemegang View asset value dapat memfilter dan mengurutkan kolom finansial
72. `Hari Susanto {runId}` mengambil daftar sub-tab Active dengan Search `{runId}` dan filter Purchase Cost Min `10000000` dan Max `15000000`
73. Verifikasi hasil memuat baris `Camera Canon EOS {runId} - 1` dengan Purchase Cost `12500000` karena `Hari Susanto {runId}` memegang View asset value
74. `Hari Susanto {runId}` mengambil daftar sub-tab Active dengan Search `{runId}` diurutkan menurut Asset Value (Commercial) ascending
75. Verifikasi permintaan itu diterima dan baris `Camera Canon EOS {runId} - 1` memuat Asset Value (Commercial) `9800000`

### Kolom TAG hanya memuat tipe TAG yang terbuka di plan client
76. Rina W meminta opsi filter TAG pada sub-tab Active
77. Verifikasi opsi itu hanya memuat tipe TAG yang terbuka di plan client, yaitu `BLE`, `GPS`, `NFC`, `QR`, dan `RFID`, sesuai nilai DISTINCT dari baris tabel
78. Verifikasi daftar baris dan kolom TAG pada berkas Download hanya memuat tipe TAG yang terbuka di plan client

### Filter dan Sort Resolved By memakai nama PIC
79. Rina W mengambil daftar sub-tab History dengan Search `{runId}` dan filter Resolved By `Rudi Hartono {runId}`
80. Verifikasi hasil memuat baris `Vacuum Cleaner Industri {runId} - 1` karena filter Resolved By memakai nama PIC yang menyelesaikan record
81. Rina W mengambil daftar sub-tab History dengan Search `{runId}` diurutkan menurut Resolved By ascending
82. Verifikasi urutan memakai nama PIC sebagai pelaku: baris yang diselesaikan Rina W lebih dulu, lalu `Vacuum Cleaner Industri {runId} - 1` (`Rudi Hartono {runId}`), lalu `Printer HP LaserJet M404 {runId} - 1` yang diselesaikan `System`
