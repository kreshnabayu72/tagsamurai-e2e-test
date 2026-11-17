---
id: TC-FA-MYASSET-E2E-031-tab-borrowed-search-dep-borrow
title: "Search tab Borrowed: substring, huruf besar kecil, spasi tepi, kolom tersembunyi, dan tanpa hasil"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#r3", "EB-SRC-2@tabel-borrowed", "EB-SRC-3@tabel-borrowed", "EB-SRC-5@tabel-borrowed", "EB-TBL-1@tabel-borrowed", "EB-SRC-1"]
smoke: ["EB-TBL-1@tabel-borrowed", "EB-SRC-1"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§5#r3": [3, 4, 6, 36, 43]
  "EB-SRC-2@tabel-borrowed": [30, 32, 34]
  "EB-SRC-3@tabel-borrowed": [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
  "EB-SRC-5@tabel-borrowed": [38, 43]
  "EB-TBL-1@tabel-borrowed": 8
  "EB-SRC-1": [3, 6, 8]
anchor: [1]
coverage:
  web: automated
---

# Search tab Borrowed: substring, huruf besar kecil, spasi tepi, kolom tersembunyi, dan tanpa hasil

## Prerequisites
- Aktor: Borrower `Maya Anggraini {runId}`, pengguna karyawan ber-akun login tanpa role admin.
- Layar awal: halaman My Asset, tab `Borrowed`.
- Data:
  - DU-031-1: User `Maya Anggraini {runId}`, tanpa role admin, cakupan Group `Head Office`.
  - DU-031-2: pinjaman Admin atas nama `Maya Anggraini {runId}`, aset `Printer Canon G3010 {runId}`, Brand `Canon`, Model/Type `G3010`, Category `Elektronik`, TAG `RFID`, Group `Head Office`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0`, Due Date `T0 + 3 hari`.
  - DU-031-3: pinjaman Admin atas nama `Maya Anggraini {runId}`, aset `Proyektor Epson EB-X06 {runId}`, Brand `BenQ`, Model/Type `MX550`, Category `Elektronik`, tanpa TAG, Group `Head Office`, Status `Overdue`, Duration `2 days`, Handed Over At `T0 − 5 hari`.
  - DU-031-4: pinjaman Admin atas nama `Maya Anggraini {runId}`, aset `Scanner Dokumen {runId}`, Brand `Epson`, Model/Type `DS-530`, Category `Elektronik`, tanpa TAG, Group `Head Office`, Status `Waiting for Handover`, Duration `3 days`.
  - DU-031-5: pinjaman Admin atas nama `Maya Anggraini {runId}`, aset `Laptop Staf Keuangan {runId}`, Brand `Dell`, Model/Type `Latitude`, Category `Elektronik`, tanpa TAG, Group `Head Office`, Status `Waiting for Handover`, Duration `3 days`.
  - DU-031-6: pinjaman Admin atas nama `Maya Anggraini {runId}`, aset `Laptop Direksi {runId}`, Brand `Dell`, Model/Type `Latitude Pro`, Category `Elektronik`, tanpa TAG, Group `Head Office`, Status `Waiting for Handover`, Duration `3 days`.
  - DU-031-7: pinjaman Admin atas nama `Maya Anggraini {runId}`, aset `Adaptor 100% Original {runId}`, Brand `Anker`, Model/Type `PowerPort`, Category `Elektronik`, tanpa TAG, Group `Head Office`, Status `Waiting for Handover`, Duration `3 days`.
  - DU-031-8: pinjaman Admin atas nama `Maya Anggraini {runId}`, aset `Kabel_Roll 5 Meter {runId}`, Brand `Ugreen`, Model/Type `Roll5`, Category `Elektronik`, tanpa TAG, Group `Head Office`, Status `Waiting for Handover`, Duration `3 days`.
  - DU-031-9: pinjaman Admin atas nama `Maya Anggraini {runId}`, aset `Meja Head Office Room {runId}`, Brand `Informa`, Model/Type `Meja Rapat`, Category `Furnitur`, tanpa TAG, Group `Head Office`, Status `Waiting for Handover`, Duration `3 days`.
  - Kata kunci Search: DU-031-10 `Canon G3010`, DU-031-11 `canon g3010`, DU-031-12 `Tidak Ada Barang Ini`, DU-031-13 `Canon G3010` diapit dua spasi di awal dan dua spasi di akhir, DU-031-14 `Printer  Canon` dengan dua spasi di tengah, DU-031-15 `Head Office Room`, DU-031-16 `Head Room`, DU-031-17 `%`, DU-031-18 `_`, DU-031-19 `.*`, DU-031-20 `<script>alert(1)</script>`, DU-031-21 `' OR '1'='1`, DU-031-22 `{"$ne": null}`, DU-031-23 `Overdue`, DU-031-24 tanggal Due Date DU-031-2 berformat `dd/MM/yy`, DU-031-25 `Epson`, DU-031-26 `Latitude`, DU-031-27 `RFID`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Tab Borrowed `Maya Anggraini {runId}` hanya berisi 8 baris aset, dari DU-031-2 sampai DU-031-9.
  - Kolom `TAG` tidak tampil pada tabel Borrowed (kolom tambahan, tersembunyi pada konfigurasi bawaan).

## Test Steps

### Substring di tengah dan huruf besar kecil
1. Verifikasi tabel Borrowed memuat 8 baris
2. Ketik Search `Canon G3010`, tekan Enter
3. Verifikasi baris `Printer Canon G3010 {runId}` tampil karena `Canon G3010` berada di tengah Name
4. Verifikasi tabel memuat 1 baris
5. Ganti isi kotak search dengan `canon g3010`, tekan Enter
6. Verifikasi baris `Printer Canon G3010 {runId}` tampil walau huruf besar dan kecil berbeda
7. Ganti isi kotak search dengan `Tidak Ada Barang Ini`, tekan Enter
8. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil untuk kata kunci tanpa kecocokan

### Spasi tepi dibuang dan spasi tengah dipertahankan
9. Ganti isi kotak search dengan `Canon G3010` yang diapit dua spasi di awal dan dua spasi di akhir, tekan Enter
10. Verifikasi baris `Printer Canon G3010 {runId}` tampil walau kata kunci diapit spasi
11. Ganti isi kotak search dengan `Printer  Canon` yang memuat dua spasi di tengah, tekan Enter
12. Verifikasi empty state `No results found` tampil untuk kata kunci dengan dua spasi di tengah
13. Ganti isi kotak search dengan `Head Office Room`, tekan Enter
14. Verifikasi baris `Meja Head Office Room {runId}` tampil untuk kata kunci utuh
15. Ganti isi kotak search dengan `Head Room`, tekan Enter
16. Verifikasi empty state `No results found` tampil untuk kata yang tidak bersebelahan

### Karakter khusus dan payload dicari sebagai teks
17. Ganti isi kotak search dengan `%`, tekan Enter
18. Verifikasi hanya baris `Adaptor 100% Original {runId}` yang tampil
19. Ganti isi kotak search dengan `_`, tekan Enter
20. Verifikasi hanya baris `Kabel_Roll 5 Meter {runId}` yang tampil
21. Ganti isi kotak search dengan `.*`, tekan Enter
22. Verifikasi empty state `No results found` tampil untuk kata kunci `.*`
23. Ganti isi kotak search dengan `<script>alert(1)</script>`, tekan Enter
24. Verifikasi empty state `No results found` tampil untuk kata kunci bermarkup
25. Ganti isi kotak search dengan `' OR '1'='1`, tekan Enter
26. Verifikasi empty state `No results found` tampil untuk kata kunci berpola SQL
27. Ganti isi kotak search dengan `{"$ne": null}`, tekan Enter
28. Verifikasi empty state `No results found` tampil untuk kata kunci berpola operator

### Nilai badge cocok, nilai tanggal tidak cocok, dan kata kunci lintas kolom
29. Ganti isi kotak search dengan `Overdue`, tekan Enter
30. Verifikasi hanya baris `Proyektor Epson EB-X06 {runId}` yang tampil karena badge Status bernilai `Overdue`
31. Ganti isi kotak search dengan tanggal Due Date baris `Printer Canon G3010 {runId}` berformat `dd/MM/yy`, tekan Enter
32. Verifikasi empty state `No results found` tampil untuk kata kunci tanggal
33. Ganti isi kotak search dengan `Epson`, tekan Enter
34. Verifikasi baris `Proyektor Epson EB-X06 {runId}` dan baris `Scanner Dokumen {runId}` tampil, masing-masing karena kolom Name dan kolom Brand
35. Ganti isi kotak search dengan `Latitude`, tekan Enter
36. Verifikasi baris `Laptop Staf Keuangan {runId}` dan baris `Laptop Direksi {runId}` tampil, masing-masing karena Model/Type `Latitude` dan `Latitude Pro`

### Kolom TAG tersembunyi tidak dicari
37. Ganti isi kotak search dengan `RFID`, tekan Enter
38. Verifikasi empty state `No results found` tampil karena kolom `TAG` tersembunyi
39. Klik header kolom Actions `⋯` untuk membuka Column Visibility
40. Centang kolom `TAG`
41. Tekan `Esc` untuk menutup Column Visibility
42. Ganti isi kotak search dengan `RFID`, tekan Enter
43. Verifikasi baris `Printer Canon G3010 {runId}` tampil dengan TAG `RFID` setelah kolom `TAG` ditampilkan
44. Klik `(←)` pada kotak Search
