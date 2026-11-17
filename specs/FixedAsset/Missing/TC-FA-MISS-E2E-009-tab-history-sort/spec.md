---
id: TC-FA-MISS-E2E-009-tab-history-sort
title: "Tab History: urutan sort Duration, Resolved Date, dan kolom teks"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§9.5#r3, §4.1b#r14, §4.1b#r16]
smoke: []
dependsOn: []
trace:
  §9.5#r3: [4, 14, 16, 18, 26, 28]
  §4.1b#r14: [6, 8]
  §4.1b#r16: [4, 10, 12]
anchor: []
coverage:
  web: automated
---

# Tab History: urutan sort Duration, Resolved Date, dan kolom teks

## Prerequisites
- Aktor: Total Control `Rina Wijaya {runId}`.
- Layar awal: halaman Assets.
- Data:
  - DU-009-1: User `Rina Wijaya {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-009-2: User `Citra Lestari {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing.
  - DU-009-3: User `Dodi Wibowo {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing.
  - DU-009-4: User `Eka Saputra {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing.
  - DU-009-5: User `Fajar Nugroho {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing.
  - DU-009-6: Record `Found` untuk aset `Server Rak Lama {runId}` (Labels `Audit {runId}` dan `Zebra {runId}`), Source `Borrow`, Last Holder `Citra Lestari {runId}`, Reported Date T0 − 30 hari pukul `09:00`, Resolved Date T0 − 24 hari pukul `14:10`, Duration `6 days`, dari selisih 6 hari kalender.
  - DU-009-7: Record `Disposed` untuk aset `Genset Portabel {runId}`, Source `Manual`, tanpa Last Holder, Reported Date T0 − 70 hari pukul `08:00`, Resolved Date T0 − 8 hari pukul `00:00`, Duration `62 days`, dari selisih 62 hari kalender.
  - DU-009-8: Record `Rejected` untuk aset `Printer Label {runId}` (Labels `Berat {runId}`), Source `Reported by holder`, Last Holder `Dodi Wibowo {runId}`, Reported Date T0 − 10 hari pukul `08:30`, Resolved Date T0 − 9 hari pukul `09:15`, Duration `1 day`, dari selisih 1 hari kalender.
  - DU-009-9: Record `Canceled` untuk aset `Scanner Gudang {runId}`, Source `Reported by holder`, Last Holder `Eka Saputra {runId}`, Reported Date T0 − 12 hari pukul `13:00`, Resolved Date T0 − 11 hari pukul `08:20`, Duration `1 day`, sama dengan DU-009-8.
  - DU-009-10: Record `Found` untuk aset `Kompresor Mini {runId}` (Labels `Cadangan {runId}`, `Fragile {runId}`, dan `Priority {runId}`), Source `Manual`, Last Holder `Fajar Nugroho {runId}`, Reported Date T0 − 45 hari pukul `10:00`, Resolved Date T0 − 25 hari pukul `14:10`, Duration `20 days`, dari selisih 20 hari kalender.
  - Reported By setiap record DU-009-6 sampai DU-009-10 adalah `Rina Wijaya {runId}`.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - T0 adalah waktu spec dijalankan; tanggal pada entri di atas dihitung relatif terhadap T0.

## Test Steps

### Urutan default Resolved Date terbaru dulu
1. Klik tab `Missing` pada halaman Assets
2. Klik sub-tab `History`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi urutan baris dari atas ke bawah: `Genset Portabel {runId}` lalu `Printer Label {runId}` lalu `Scanner Gudang {runId}` lalu `Server Rak Lama {runId}` lalu `Kompresor Mini {runId}`, yaitu Resolved Date terbaru dulu yang berbeda dari urutan Duration naik maupun turun

### Sort Duration numerik dengan nilai sama diurutkan menurut default
5. Klik header `Duration`
6. Verifikasi urutan baris dari atas ke bawah: `Printer Label {runId}` lalu `Scanner Gudang {runId}` lalu `Server Rak Lama {runId}` lalu `Kompresor Mini {runId}` lalu `Genset Portabel {runId}` dengan Duration `1 day`, `1 day`, `6 days`, `20 days`, dan `62 days`, dan `Printer Label {runId}` sebelum `Scanner Gudang {runId}` menurut urutan default
7. Klik header `Duration`
8. Verifikasi urutan baris dari atas ke bawah: `Genset Portabel {runId}` lalu `Kompresor Mini {runId}` lalu `Server Rak Lama {runId}` lalu `Printer Label {runId}` lalu `Scanner Gudang {runId}`, dengan `Printer Label {runId}` dan `Scanner Gudang {runId}` yang Duration-nya sama tetap menurut urutan default

### Sort Resolved Date dari yang terlama dan terbaru
9. Klik header `Resolved Date`
10. Verifikasi urutan baris dari atas ke bawah menurut Oldest First: `Kompresor Mini {runId}` lalu `Server Rak Lama {runId}` lalu `Scanner Gudang {runId}` lalu `Printer Label {runId}` lalu `Genset Portabel {runId}`
11. Klik header `Resolved Date`
12. Verifikasi urutan baris dari atas ke bawah menurut Newest First: `Genset Portabel {runId}` lalu `Printer Label {runId}` lalu `Scanner Gudang {runId}` lalu `Server Rak Lama {runId}` lalu `Kompresor Mini {runId}`

### Sort kolom teks Last Holder dengan nilai kosong di akhir saat ascending dan di awal saat descending
13. Klik header `Last Holder`
14. Verifikasi urutan baris dari atas ke bawah: `Server Rak Lama {runId}` lalu `Printer Label {runId}` lalu `Scanner Gudang {runId}` lalu `Kompresor Mini {runId}` dengan Last Holder `Citra L`, `Dodi W`, `Eka S`, dan `Fajar N`, lalu `Genset Portabel {runId}` yang Last Holder-nya `—`
15. Klik header `Last Holder`
16. Verifikasi urutan baris dari atas ke bawah: `Genset Portabel {runId}` yang Last Holder-nya `—`, lalu `Kompresor Mini {runId}` lalu `Scanner Gudang {runId}` lalu `Printer Label {runId}` lalu `Server Rak Lama {runId}`
17. Klik header `Last Holder`
18. Verifikasi urutan baris kembali ke urutan default Resolved Date terbaru dulu: `Genset Portabel {runId}` lalu `Printer Label {runId}` lalu `Scanner Gudang {runId}` lalu `Server Rak Lama {runId}` lalu `Kompresor Mini {runId}`
19. Klik `(←)` pada kotak Search

### Sort Labels menurut label pertama secara alfabetis
20. Ketik Search `{runId}`, tekan Enter
21. Klik header kolom Actions
22. Klik `Setup Column...`
23. Centang kolom `Labels`
24. Klik `[Save]`
25. Klik header `Labels`
26. Verifikasi urutan baris dari atas ke bawah menurut label pertama A-Z: `Server Rak Lama {runId}` (`Audit {runId}` dan `Zebra {runId}`) lalu `Printer Label {runId}` (`Berat {runId}`) lalu `Kompresor Mini {runId}` (`Cadangan {runId}`, `Fragile {runId}`, dan `Priority {runId}`), lalu `Genset Portabel {runId}` dan `Scanner Gudang {runId}` yang tanpa Labels menurut urutan default
27. Klik header `Labels`
28. Verifikasi urutan baris dari atas ke bawah menurut label pertama Z-A: `Genset Portabel {runId}` dan `Scanner Gudang {runId}` yang tanpa Labels lebih dulu menurut urutan default, lalu `Kompresor Mini {runId}` lalu `Printer Label {runId}` lalu `Server Rak Lama {runId}`
29. Klik `(←)` pada kotak Search
