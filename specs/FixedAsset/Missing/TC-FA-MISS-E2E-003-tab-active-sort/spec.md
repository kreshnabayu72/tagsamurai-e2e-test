---
id: TC-FA-MISS-E2E-003-tab-active-sort
title: "Tab Active: urutan sort per kolom, siklus kembali ke urutan default"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§9.5#r2, §4.1a#r6, §4.1a#r15, EB-SRT-1, EB-SRT-2, EB-SRT-3@tabel-active]
smoke: [EB-SRT-1, EB-SRT-2, EB-SRT-3@tabel-active]
dependsOn: []
trace:
  §9.5#r2: [2, 4, 27, 33]
  §4.1a#r6: [40, 42]
  §4.1a#r15: [22, 29, 31]
  EB-SRT-1: [7, 9, 12, 14, 22, 29, 44, 46, 48, 56, 58, 60, 62, 66, 68, 74, 76]
  EB-SRT-2: [17, 19, 31, 40, 42, 48, 50, 52, 54, 66, 68, 74, 76]
  EB-SRT-3@tabel-active: [25, 33]
anchor: []
coverage:
  web: automated
---

# Tab Active: urutan sort per kolom, siklus kembali ke urutan default

## Prerequisites
- Aktor: Total Control `Rina Wijaya {runId}`.
- Layar awal: halaman Assets, tab Missing, sub-tab Active.
- Data:
  - DU-003-1: User `Rina Wijaya {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-003-2: User `Citra Lestari {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing; tampil sebagai `Citra L`.
  - DU-003-3: User `Dodi Wibowo {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing; tampil sebagai `Dodi W`.
  - DU-003-4: User `Eka Saputra {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing; tampil sebagai `Eka S`.
  - DU-003-5: User `Fajar Nugroho {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing; tampil sebagai `Fajar N`.
  - DU-003-6: Record `Missing` untuk aset `anggur Press {runId}` (Group `Gudang Uji {runId}`, TAG `RFID`, Purchase Cost `4500000`), Source `Manual`, tanpa Last Holder, Reported Date T0 − 12 hari pukul `09:00`; Days Missing `12 days`.
  - DU-003-7: Record `Missing` untuk aset `Apel Slicer {runId}` (Group `Gudang Uji {runId}`, TAG `NFC` dan `QR`, Purchase Cost `1250000`), Source `Borrow`, tanpa Last Holder, Reported Date T0 − 9 hari pukul `09:00`; Days Missing `9 days`.
  - DU-003-8: Record `Missing` untuk aset `Élan Mixer {runId}` (Group `Gudang Uji {runId}`, TAG `NFC`, Purchase Cost `2750000`), Source `Borrow`, Last Holder `Citra Lestari {runId}`, Reported Date T0 − 20 hari pukul `09:00`; Days Missing `20 days`.
  - DU-003-9: Record `Missing` untuk aset `Elan Mixer {runId}` (Group `Gudang Uji {runId}`, TAG `QR`, Purchase Cost `9800000`), Source `Borrow`, tanpa Last Holder, Reported Date T0 − 20 hari pukul `11:00`; Days Missing `20 days`, sama dengan DU-003-8 pada status dan Days Missing.
  - DU-003-10: Record `Waiting for Confirmation` untuk aset `Ezra Grinder {runId}` (Group `Gudang Uji {runId}`, TAG `BLE`, Purchase Cost `3100000`), Source `Reported by holder`, Last Holder `Dodi Wibowo {runId}`, Reported Date T0 − 2 hari pukul `08:00`; Days Missing `2 days`.
  - DU-003-11: Record `Missing` untuk aset `3D Printer {runId}` (Group `Gudang Uji {runId}`, tanpa TAG, Purchase Cost `6400000`), Source `Transfer`, tanpa Last Holder, Reported Date T0 − 15 hari pukul `09:00`; Days Missing `15 days`.
  - DU-003-12: Record `Missing` untuk aset `#Gudang Rak {runId}` (Group `Gudang Uji {runId}`, TAG `GPS`, Purchase Cost `800000`), Source `Transfer`, Last Holder `Eka Saputra {runId}`, Reported Date T0 − 40 hari pukul `09:00`; Days Missing `40 days`.
  - DU-003-13: Record `Waiting for Confirmation` untuk aset `Forklift Kecil {runId}` (Group `Gudang Uji {runId}`, TAG `BLE` dan `GPS`, Purchase Cost `12000000`), Source `Reported by holder`, Last Holder `Fajar Nugroho {runId}`, Reported Date T0 − 1 hari pukul `08:00`; Days Missing `1 day`.
  - DU-003-14: Dua belas record `Missing` untuk dua belas aset ber-nama sama `Pompa Air {runId}` (Group `Gudang Pompa {runId}`, TAG `NFC`), Source `Manual`, tanpa Last Holder; dibuat berurutan sehingga Increment yang dibentuk server berjalan 1 sampai 12, dan record dengan Increment n dilaporkan T0 − n hari pukul `09:00`, sehingga Days Missing-nya n hari dan urutan pembuatannya kebalikan dari urutan default.
  - DU-003-15: Atribut tambahan aset `anggur Press {runId}` (DU-003-6): Labels `Audit {runId}` dan `Zebra {runId}`, pemindai terakhir reader `Gate A reader {runId}` pada T0 − 14 hari.
  - DU-003-16: Atribut tambahan aset `Apel Slicer {runId}` (DU-003-7): Labels `Berat {runId}`, pemindai terakhir reader `Gate A reader {runId}` pada T0 − 10 hari.
  - DU-003-17: Atribut tambahan aset `Élan Mixer {runId}` (DU-003-8): Labels `Cadangan {runId}`, `Fragile {runId}`, dan `Priority {runId}`, pemindai terakhir reader `Gate A reader {runId}` pada T0 − 22 hari.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - T0 adalah waktu spec dijalankan; Reported Date pada entri di atas dihitung relatif terhadap T0.
  - Ukuran halaman bernilai bawaan `10`.

## Test Steps

### Urutan default dan paginasi lintas halaman pada data bervolume
1. Ketik Search `Pompa Air {runId}`, tekan Enter
2. Verifikasi halaman 1 memuat dari atas ke bawah baris Increment 12 sampai 3, karena default Days Missing terlama dulu berbeda dari urutan pembuatan
3. Klik halaman `2` pada kontrol Pagination
4. Verifikasi halaman 2 memuat baris Increment 2 lalu 1
5. Klik halaman `1` pada kontrol Pagination

### Sort Name memakai Increment natural dan berlaku lintas halaman
6. Klik header `Name`
7. Verifikasi halaman 1 memuat dari atas ke bawah baris Increment 1 sampai 10
8. Klik halaman `2` pada kontrol Pagination
9. Verifikasi halaman 2 memuat baris Increment 11 lalu 12, bukan 11 dan 12 di antara 1 dan 2
10. Klik halaman `1` pada kontrol Pagination
11. Klik header `Name`
12. Verifikasi halaman 1 memuat dari atas ke bawah baris Increment 12 sampai 3
13. Klik halaman `2` pada kontrol Pagination
14. Verifikasi halaman 2 memuat baris Increment 2 lalu 1
15. Klik halaman `1` pada kontrol Pagination

### Nilai sort yang sama di seluruh halaman tetap berurutan menurut default
16. Klik header `Source`
17. Verifikasi halaman 1 memuat dari atas ke bawah baris Increment 12 sampai 3, menurut urutan default karena seluruh dua belas baris ber-Source `Manual`
18. Klik halaman `2` pada kontrol Pagination
19. Verifikasi halaman 2 memuat baris Increment 2 lalu 1 tanpa baris ganda atau terlewat
20. Klik halaman `1` pada kontrol Pagination

### Sort Days Missing numerik dan siklus kembali ke urutan default
21. Klik header `Days Missing`
22. Verifikasi halaman 1 memuat dari atas ke bawah `1 day`, lalu `2 days` sampai `10 days`, dan halaman 2 menyusul `11 days` dan `12 days` sehingga `9 days` berada sebelum `10 days`
23. Klik header `Days Missing`
24. Klik header `Days Missing`
25. Verifikasi halaman 1 kembali memuat dari atas ke bawah baris Increment 12 sampai 3 menurut urutan default dan header `Days Missing` tidak berindikator sort

### Urutan default tab Active memuat Waiting for Confirmation di atas
26. Ganti isi kotak search dengan `Gudang Uji {runId}`, tekan Enter
27. Verifikasi urutan baris dari atas ke bawah: `Ezra Grinder {runId}` lalu `Forklift Kecil {runId}` lalu `#Gudang Rak {runId}`, lalu `Élan Mixer {runId}` dan `Elan Mixer {runId}` pada urutan keempat dan kelima dalam urutan apa pun, lalu `3D Printer {runId}` lalu `anggur Press {runId}` lalu `Apel Slicer {runId}`, yaitu `Waiting for Confirmation` di atas lalu Days Missing terlama dulu

### Sort Days Missing dengan nilai sama membalik urutan identifier mengikuti arah sort
28. Klik header `Days Missing`
29. Verifikasi urutan baris dari atas ke bawah: `Forklift Kecil {runId}` lalu `Ezra Grinder {runId}` lalu `Apel Slicer {runId}` lalu `anggur Press {runId}` lalu `3D Printer {runId}`, lalu `Élan Mixer {runId}` dan `Elan Mixer {runId}` pada urutan keenam dan ketujuh, lalu `#Gudang Rak {runId}`, dengan Days Missing `1 day`, `2 days`, `9 days`, `12 days`, `15 days`, dua baris `20 days`, dan `40 days`
30. Klik header `Days Missing`
31. Verifikasi urutan baris dari atas ke bawah: `#Gudang Rak {runId}`, lalu `Élan Mixer {runId}` dan `Elan Mixer {runId}` pada urutan kedua dan ketiga dengan urutan antar keduanya kebalikan dari urutan saat ascending, lalu `3D Printer {runId}` lalu `anggur Press {runId}` lalu `Apel Slicer {runId}` lalu `Ezra Grinder {runId}` lalu `Forklift Kecil {runId}`
32. Klik header `Days Missing`
33. Verifikasi urutan baris kembali ke urutan default: `Ezra Grinder {runId}` lalu `Forklift Kecil {runId}` lalu `#Gudang Rak {runId}`, lalu `Élan Mixer {runId}` dan `Elan Mixer {runId}`, lalu `3D Printer {runId}` lalu `anggur Press {runId}` lalu `Apel Slicer {runId}`

### Sort kolom TAG menurut label ikon dengan baris tanpa TAG di akhir saat ascending
34. Klik header kolom Actions
35. Klik `Setup Column...`
36. Centang kolom `TAG`
37. Centang kolom `Purchase Cost`
38. Klik `[Save]`
39. Klik header `TAG`
40. Verifikasi urutan baris dari atas ke bawah menurut label ikon: `Ezra Grinder {runId}` (`BLE`), `Forklift Kecil {runId}` (`BLE` dan `GPS`), `#Gudang Rak {runId}` (`GPS`), `Élan Mixer {runId}` (`NFC`), `Apel Slicer {runId}` (`NFC` dan `QR`), `Elan Mixer {runId}` (`QR`), `anggur Press {runId}` (`RFID`), lalu `3D Printer {runId}` tanpa TAG
41. Klik header `TAG`
42. Verifikasi urutan baris dari atas ke bawah: `3D Printer {runId}` tanpa TAG, lalu `anggur Press {runId}` lalu `Elan Mixer {runId}` lalu `Apel Slicer {runId}` lalu `Élan Mixer {runId}` lalu `#Gudang Rak {runId}` lalu `Forklift Kecil {runId}` lalu `Ezra Grinder {runId}`

### Sort Name alfabetis tidak membedakan huruf kapital, aksen, angka, dan simbol
43. Klik header `Name`
44. Verifikasi urutan baris dari atas ke bawah: `#Gudang Rak {runId}` lalu `3D Printer {runId}` yang diawali simbol dan angka, lalu `anggur Press {runId}` lalu `Apel Slicer {runId}` lalu `Elan Mixer {runId}` lalu `Élan Mixer {runId}` lalu `Ezra Grinder {runId}` lalu `Forklift Kecil {runId}`, dengan `anggur Press` sebelum `Apel Slicer` dan `Elan Mixer` sebelum `Élan Mixer`
45. Klik header `Name`
46. Verifikasi urutan baris dari atas ke bawah: `Forklift Kecil {runId}` lalu `Ezra Grinder {runId}` lalu `Élan Mixer {runId}` lalu `Elan Mixer {runId}` lalu `Apel Slicer {runId}` lalu `anggur Press {runId}` lalu `3D Printer {runId}` lalu `#Gudang Rak {runId}`

### Sort Status menurut label dengan nilai sama diurutkan menurut default
47. Klik header `Status`
48. Verifikasi urutan baris dari atas ke bawah: `#Gudang Rak {runId}`, lalu `Élan Mixer {runId}` dan `Elan Mixer {runId}`, lalu `3D Printer {runId}` lalu `anggur Press {runId}` lalu `Apel Slicer {runId}` yang berstatus `Missing` menurut urutan default, lalu `Ezra Grinder {runId}` lalu `Forklift Kecil {runId}` yang berstatus `Waiting for Confirmation`
49. Klik header `Status`
50. Verifikasi urutan baris dari atas ke bawah: `Ezra Grinder {runId}` lalu `Forklift Kecil {runId}` yang berstatus `Waiting for Confirmation`, lalu `#Gudang Rak {runId}`, `Élan Mixer {runId}` dan `Elan Mixer {runId}`, `3D Printer {runId}` lalu `anggur Press {runId}` lalu `Apel Slicer {runId}` yang berstatus `Missing` tetap menurut urutan default

### Sort Last Holder dengan nilai kosong di akhir saat ascending dan di awal saat descending
51. Klik header `Last Holder`
52. Verifikasi urutan baris dari atas ke bawah: `Élan Mixer {runId}` lalu `Ezra Grinder {runId}` lalu `#Gudang Rak {runId}` lalu `Forklift Kecil {runId}` dengan Last Holder `Citra L`, `Dodi W`, `Eka S`, dan `Fajar N`, lalu `Elan Mixer {runId}` lalu `3D Printer {runId}` lalu `anggur Press {runId}` lalu `Apel Slicer {runId}` yang Last Holder-nya `—` menurut urutan default
53. Klik header `Last Holder`
54. Verifikasi urutan baris dari atas ke bawah: `Elan Mixer {runId}` lalu `3D Printer {runId}` lalu `anggur Press {runId}` lalu `Apel Slicer {runId}` yang Last Holder-nya `—`, lalu `Forklift Kecil {runId}` lalu `#Gudang Rak {runId}` lalu `Ezra Grinder {runId}` lalu `Élan Mixer {runId}`

### Sort Reported Date dari yang terlama dan terbaru
55. Klik header `Reported Date`
56. Verifikasi urutan baris dari atas ke bawah menurut Oldest First: `#Gudang Rak {runId}` lalu `Élan Mixer {runId}` lalu `Elan Mixer {runId}` lalu `3D Printer {runId}` lalu `anggur Press {runId}` lalu `Apel Slicer {runId}` lalu `Ezra Grinder {runId}` lalu `Forklift Kecil {runId}`, dengan `Élan Mixer {runId}` sebelum `Elan Mixer {runId}` karena jamnya `09:00` lebih awal dari `11:00`
57. Klik header `Reported Date`
58. Verifikasi urutan baris dari atas ke bawah menurut Newest First: `Forklift Kecil {runId}` lalu `Ezra Grinder {runId}` lalu `Apel Slicer {runId}` lalu `anggur Press {runId}` lalu `3D Printer {runId}` lalu `Elan Mixer {runId}` lalu `Élan Mixer {runId}` lalu `#Gudang Rak {runId}`

### Sort Purchase Cost menurut nilai numerik
59. Klik header `Purchase Cost`
60. Verifikasi urutan baris dari atas ke bawah menurut nilai numerik dari kecil ke besar: `#Gudang Rak {runId}` (`800000`), `Apel Slicer {runId}` (`1250000`), `Élan Mixer {runId}` (`2750000`), `Ezra Grinder {runId}` (`3100000`), `anggur Press {runId}` (`4500000`), `3D Printer {runId}` (`6400000`), `Elan Mixer {runId}` (`9800000`), `Forklift Kecil {runId}` (`12000000`)
61. Klik header `Purchase Cost`
62. Verifikasi urutan baris dari atas ke bawah menurut nilai numerik dari besar ke kecil, dimulai `Forklift Kecil {runId}` dan diakhiri `#Gudang Rak {runId}`
63. Klik `(←)` pada kotak Search

### Sort Last Seen dari pemindaian terlama dan terbaru dengan baris tanpa pemindaian di ujung
64. Ganti isi kotak search dengan `Gudang Uji {runId}`, tekan Enter
65. Klik header `Last Seen`
66. Verifikasi urutan baris dari atas ke bawah menurut Oldest First: `Élan Mixer {runId}` lalu `anggur Press {runId}` lalu `Apel Slicer {runId}`, lalu lima baris tanpa pemindaian menurut urutan default: `Ezra Grinder {runId}`, `Forklift Kecil {runId}`, `#Gudang Rak {runId}`, `Elan Mixer {runId}` yang Last Seen-nya `Unknown`, dan `3D Printer {runId}` yang Last Seen-nya `—` karena asetnya tanpa TAG
67. Klik header `Last Seen`
68. Verifikasi urutan baris dari atas ke bawah menurut Newest First: lima baris tanpa pemindaian lebih dulu menurut urutan default, yaitu `Ezra Grinder {runId}`, `Forklift Kecil {runId}`, `#Gudang Rak {runId}`, `Elan Mixer {runId}`, dan `3D Printer {runId}`, lalu `Apel Slicer {runId}` lalu `anggur Press {runId}` lalu `Élan Mixer {runId}`

### Sort Labels menurut label pertama secara alfabetis
69. Klik header kolom Actions
70. Klik `Setup Column...`
71. Centang kolom `Labels`
72. Klik `[Save]`
73. Klik header `Labels`
74. Verifikasi urutan baris dari atas ke bawah menurut label pertama A–Z: `anggur Press {runId}` (`Audit {runId}` dan `Zebra {runId}`) lalu `Apel Slicer {runId}` (`Berat {runId}`) lalu `Élan Mixer {runId}` (`Cadangan {runId}`, `Fragile {runId}`, dan `Priority {runId}`), lalu lima baris tanpa Labels menurut urutan default: `Ezra Grinder {runId}`, `Forklift Kecil {runId}`, `#Gudang Rak {runId}`, `Elan Mixer {runId}`, dan `3D Printer {runId}`
75. Klik header `Labels`
76. Verifikasi urutan baris dari atas ke bawah menurut label pertama Z–A: lima baris tanpa Labels lebih dulu menurut urutan default, yaitu `Ezra Grinder {runId}`, `Forklift Kecil {runId}`, `#Gudang Rak {runId}`, `Elan Mixer {runId}`, dan `3D Printer {runId}`, lalu `Élan Mixer {runId}` lalu `Apel Slicer {runId}` lalu `anggur Press {runId}`
77. Klik `(←)` pada kotak Search
