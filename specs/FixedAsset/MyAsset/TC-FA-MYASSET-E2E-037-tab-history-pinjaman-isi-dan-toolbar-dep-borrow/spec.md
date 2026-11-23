---
id: TC-FA-MYASSET-E2E-037-tab-history-pinjaman-isi-dan-toolbar-dep-borrow
title: "Tab History pada data nyata pinjaman: status akhir, Type Borrow, urutan default, dan toolbar"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r18", "§1.2#r20", "§4.1c#r1", "§4.1c#r2", "§4.1c#r3", "§4.1c#r4", "§4.1c#r5", "§4.1c#r6", "§4.1c#r7", "§4.1c#r8", "§4.1c#r11", "§4.1c#r12", "§4.1c#r13", "§4.1c#r14", "§4.1c#r18", "§4.1c#p4", "§5#r4", "§5#r6", "§9.2#r20", "§9.2#r21", "§9.7#r16", "EB-SRC-5@tabel-history", "§9.7#r15"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§1.2#r18": [6, 24, 26, 61, 62]
  "§1.2#r20": 16
  "§4.1c#r1": 8
  "§4.1c#r2": [9, 34]
  "§4.1c#r3": 10
  "§4.1c#r4": 11
  "§4.1c#r5": 12
  "§4.1c#r6": 13
  "§4.1c#r7": [14, 21, 22, 36]
  "§4.1c#r8": 15
  "§4.1c#r11": 16
  "§4.1c#r12": 17
  "§4.1c#r13": [18, 25]
  "§4.1c#r14": [19, 20, 23, 38]
  "§4.1c#r18": [29, 31]
  "§4.1c#p4": 7
  "§5#r4": 7
  "§5#r6": 49
  "§9.2#r20": [21, 22]
  "§9.2#r21": [27, 31]
  "§9.7#r16": [5, 52, 55, 57]
  "EB-SRC-5@tabel-history": [40, 45]
  "§9.7#r15": [55, 57]
anchor: [51]
coverage:
  web: automated
---

# Tab History pada data nyata pinjaman: status akhir, Type Borrow, urutan default, dan toolbar

## Prerequisites
- Aktor: Borrower `Kartika Dewi {runId}`, pengguna karyawan ber-akun login tanpa role admin. Aktor Borrow `Rina Wulandari {runId}` hanya memicu tiga Return, pada langkah pertama, langkah 53, dan langkah 58 (LK-8).
- Layar awal: halaman Fixed Asset (FAMS) dengan navbar.
- Data:
  - DU-037-1: User `Kartika Dewi {runId}`, tanpa role admin, cakupan Group `Head Office`.
  - DU-037-2: User `Rina Wulandari {runId}`, role Asset Admin dengan hak Aktor Borrow, cakupan Group `Head Office`.
  - DU-037-3: pinjaman Admin atas nama `Kartika Dewi {runId}`, aset `Tripod Manfrotto {runId}`, Group `Head Office`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0 − 1 hari`. Di-Return Aktor Borrow pada langkah pertama sehingga Status menjadi `Returned` dan Closed At `T0`.
  - DU-037-4: pinjaman atas nama `Kartika Dewi {runId}`, aset `Meja Rapat Kayu {runId}`, Group `Head Office`, Status `Canceled` (dibatalkan Borrower), Handed Over At `—`, Closed At `T0 − 1 hari`.
  - DU-037-5: pinjaman atas nama `Kartika Dewi {runId}`, aset `Kamera Canon EOS 90D {runId}`, Group `Head Office`, Status `Rejected`, Handed Over At `—`, Closed At `T0 − 2 hari`.
  - DU-037-6: pinjaman Admin atas nama `Kartika Dewi {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Brand `Dell`, Model/Type `Latitude 5420`, TAG `RFID`, Group `Head Office`, Status `Returned`, Duration `4 days`, Handed Over At `T0 − 10 hari`, Due Date `T0 − 6 hari`, Closed At `T0 − 4 hari`, dikembalikan lewat Return sehingga caption `late 2 days`.
  - DU-037-7: pinjaman Admin atas nama `Kartika Dewi {runId}`, aset `Monitor Dell 24 inci {runId}`, Group `Head Office`, Status `Returned` dengan marker `Damaged`, Handed Over At `T0 − 8 hari`, Closed At `T0 − 5 hari`.
  - DU-037-8: pinjaman Admin atas nama `Kartika Dewi {runId}`, aset `Proyektor Epson EB-X06 {runId}`, Group `Head Office`, Status `Returned` dengan marker `Missing`, Handed Over At `T0 − 9 hari`, Closed At `T0 − 7 hari`.
  - DU-037-13: pinjaman Admin atas nama `Kartika Dewi {runId}`, aset `Speaker Bluetooth {runId}`, Group `Head Office`, Status `Overdue`, Duration `2 days`, Handed Over At `T0 − 5 hari`, Due Date `T0 − 3 hari`. Di-Return Aktor Borrow pada langkah 53 sehingga Status menjadi `Returned`.
  - DU-037-14: 2 aset `Printer Epson L3250 {n} {runId}` dengan n dari 1 sampai 2 dalam satu pinjaman Admin atas nama `Kartika Dewi {runId}`, Group `Head Office`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0 − 1 hari`, Due Date `T0 + 2 hari`. Transaction ID dibentuk server dan sama untuk kedua aset. Di-Return Aktor Borrow pada langkah 58 sehingga Status kedua aset menjadi `Returned`.
  - Kata kunci Search: DU-037-9 `Kamera`, DU-037-10 `Rejected`, DU-037-11 tanggal Closed At DU-037-6 berformat `dd/MM/yy`, DU-037-12 `RFID`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24 jam`.
  - Tab History `Kartika Dewi {runId}` berisi 5 baris aset, dari DU-037-4 sampai DU-037-8, sebelum DU-037-3 di-Return. Tab Borrowed `Kartika Dewi {runId}` berisi 4 baris aset, DU-037-3, DU-037-13, dan kedua aset DU-037-14, sebelum DU-037-3 di-Return.
  - Kolom `TAG` tidak tampil pada tabel History (kolom tambahan, tersembunyi pada konfigurasi bawaan).

## Test Steps

### Return oleh Aktor Borrow memindahkan baris ke tab History
1. Aktor Borrow `Rina Wulandari {runId}` melakukan Return aset `Tripod Manfrotto {runId}` milik `Kartika Dewi {runId}`
2. Klik avatar di navbar untuk membuka menu profil
3. Klik `My Asset`
4. Klik tab `History`
5. Verifikasi baris `Tripod Manfrotto {runId}` tampil di tab History dengan Status `Returned`
6. Verifikasi tabel History memuat 6 baris, satu baris per aset

### Urutan default Closed At terbaru dulu
7. Verifikasi baris tampil dari atas ke bawah `Tripod Manfrotto {runId}`, `Meja Rapat Kayu {runId}`, `Kamera Canon EOS 90D {runId}`, `Laptop Dell Latitude 5420 {runId}`, `Monitor Dell 24 inci {runId}`, lalu `Proyektor Epson EB-X06 {runId}`

### Nilai sel baris Returned terlambat
8. Verifikasi kolom Photo baris `Laptop Dell Latitude 5420 {runId}` menampilkan placeholder gambar standar
9. Verifikasi kolom Name baris `Laptop Dell Latitude 5420 {runId}` memuat Asset Name `Laptop Dell Latitude 5420 {runId}` beserta increment dari server
10. Verifikasi kolom Asset ID baris `Laptop Dell Latitude 5420 {runId}` menampilkan kode aset milik DU-037-6
11. Verifikasi kolom Brand baris `Laptop Dell Latitude 5420 {runId}` bernilai `Dell`
12. Verifikasi kolom Model/Type baris `Laptop Dell Latitude 5420 {runId}` bernilai `Latitude 5420`
13. Verifikasi kolom Group baris `Laptop Dell Latitude 5420 {runId}` bernilai `Head Office`
14. Verifikasi kolom Status baris `Laptop Dell Latitude 5420 {runId}` bernilai `Returned`
15. Verifikasi kolom Holder baris `Laptop Dell Latitude 5420 {runId}` bernilai `Me`
16. Verifikasi kolom Type baris `Laptop Dell Latitude 5420 {runId}` bernilai `Borrow`
17. Verifikasi kolom Transaction ID baris `Laptop Dell Latitude 5420 {runId}` berformat `BRW-YYYY-NNNN`
18. Verifikasi kolom Handed Over At baris `Laptop Dell Latitude 5420 {runId}` menampilkan tanggal dan jam `T0 − 10 hari` berformat `dd/MM/yy` dengan jam 24 jam
19. Verifikasi kolom Closed At baris `Laptop Dell Latitude 5420 {runId}` menampilkan tanggal dan jam `T0 − 4 hari` berformat `dd/MM/yy` dengan jam 24 jam
20. Verifikasi caption `late 2 days` tampil di bawah Closed At baris `Laptop Dell Latitude 5420 {runId}`

### Status akhir, marker, Rejected, Canceled, dan tanpa kolom Reason
21. Verifikasi kolom Status baris `Monitor Dell 24 inci {runId}` bernilai `Returned` dengan badge kedua `Damaged`
22. Verifikasi kolom Status baris `Proyektor Epson EB-X06 {runId}` bernilai `Returned` dengan badge kedua `Missing`
23. Verifikasi caption late tidak tampil di bawah Closed At baris `Proyektor Epson EB-X06 {runId}`
24. Verifikasi kolom Status baris `Kamera Canon EOS 90D {runId}` bernilai `Rejected`
25. Verifikasi kolom Handed Over At baris `Kamera Canon EOS 90D {runId}` bernilai `—`
26. Verifikasi kolom Status baris `Meja Rapat Kayu {runId}` bernilai `Canceled`
27. Verifikasi kolom `Reason` tidak tampil di tabel History
28. Klik `⋯` pada baris `Meja Rapat Kayu {runId}`
29. Verifikasi menu baris memuat `Borrow Log`
30. Klik `Borrow Log`
31. Verifikasi dialog `Borrow Log` tampil dengan riwayat penutupan `Canceled by Kartika Dewi {runId}`
32. Klik `✕` pada dialog `Borrow Log`

### Search per kelas kolom, kolom tanggal, dan kolom tersembunyi
33. Ketik Search `Kamera`, tekan Enter
34. Verifikasi tabel hanya memuat baris `Kamera Canon EOS 90D {runId}` karena kolom Name cocok dengan kata kunci
35. Ganti isi kotak search dengan `Rejected`, tekan Enter
36. Verifikasi tabel hanya memuat baris `Kamera Canon EOS 90D {runId}` karena badge Status cocok dengan kata kunci
37. Ganti isi kotak search dengan tanggal Closed At baris `Laptop Dell Latitude 5420 {runId}` berformat `dd/MM/yy`, tekan Enter
38. Verifikasi empty state `No results found` tampil karena kolom Closed At tidak ikut dicari
39. Ganti isi kotak search dengan `RFID`, tekan Enter
40. Verifikasi empty state `No results found` tampil karena kolom `TAG` tabel History tersembunyi
41. Klik header kolom Actions `⋯` pada tabel History untuk membuka Column Visibility
42. Centang kolom `TAG` pada Column Visibility tabel History
43. Tekan `Esc` untuk menutup Column Visibility tabel History
44. Ketik ulang Search `RFID`, tekan Enter
45. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil dengan TAG `RFID` setelah kolom `TAG` ditampilkan
46. Klik `(←)` pada kotak Search

### Nama berkas Download tab History
47. Klik ikon `Download` pada toolbar
48. Klik `Download as CSV`
49. Verifikasi berkas `My-Asset-History.csv` terunduh

### Return pinjaman Overdue dan baris Returned meninggalkan tab Borrowed
50. Klik tab `Borrowed`
51. Verifikasi baris `Speaker Bluetooth {runId}` tampil di tab Borrowed dengan Status `Overdue`
52. Verifikasi baris `Tripod Manfrotto {runId}` tidak tampil di tab Borrowed
53. Aktor Borrow `Rina Wulandari {runId}` melakukan Return aset `Speaker Bluetooth {runId}` milik `Kartika Dewi {runId}`
54. Muat ulang halaman
55. Verifikasi baris `Speaker Bluetooth {runId}` tidak tampil di tab Borrowed
56. Klik tab `History`
57. Verifikasi baris `Speaker Bluetooth {runId}` tampil di tab History dengan Status `Returned`

### Pinjaman multi-aset yang ditutup tampil sebagai satu baris per aset
58. Aktor Borrow `Rina Wulandari {runId}` melakukan Return atas kedua aset pinjaman DU-037-14 milik `Kartika Dewi {runId}`
59. Muat ulang halaman
60. Klik tab `History`
61. Verifikasi kedua baris `Printer Epson L3250 {n} {runId}` tampil sebagai baris terpisah di tab History dengan Status `Returned`
62. Verifikasi kedua baris `Printer Epson L3250 {n} {runId}` memiliki Transaction ID yang sama karena berasal dari satu pinjaman
