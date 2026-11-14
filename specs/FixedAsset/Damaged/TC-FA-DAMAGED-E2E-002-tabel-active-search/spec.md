---
id: TC-FA-DAMAGED-E2E-002-tabel-active-search
title: "Search sub-tab Active mencocokkan kolom searchable, mengabaikan tanggal dan kolom tersembunyi, dan menampilkan No results found"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, "§5#r3", "§7.1#r1", EB-SRC-2@tabel-active, EB-SRC-3@tabel-active, EB-SRC-5@tabel-active, EB-TBL-1@tabel-active, EB-SRC-1]
smoke: [EB-SRC-1]
dependsOn: []
trace:
  T-DMG-01: [4, 5, 7, 8, 10, 11, 56, 57, 61, 62]
  "§5#r3": [4, 17, 18]
  "§7.1#r1": [43, 44]
  EB-SRC-2@tabel-active: [10, 39, 41, 46]
  EB-SRC-3@tabel-active: [20, 22, 24, 26, 28, 29, 31, 33, 35, 37]
  EB-SRC-5@tabel-active: [50, 51, 54]
  EB-TBL-1@tabel-active: [41, 43]
  EB-SRC-1: [13, 15, 43]
anchor: []
coverage:
  web: automated
---

# Search sub-tab Active mencocokkan kolom searchable, mengabaikan tanggal dan kolom tersembunyi, dan menampilkan No results found

## Prerequisites
- Aktor: Total Control, user `Admin T`.
- Layar awal: halaman Assets.
- Data:
  - DU-002-1: Name `Delta {runId} Genset - 1`, Asset ID `GEN-0001-{runId}`, Group `Head Office {runId}`, Status `Damaged`, TAG `RFID`, Source `Manual`, Reported By `Agus P`, Reported Date `T0 − 3 hari, pukul 10:00`.
  - DU-002-2: Name `Valve Aura {runId} - 2`, Asset ID `VLV-0002-{runId}`, Group `Delta {runId}`, Status `Waiting for Confirmation`, Source `Manual`, Reported By `Agus P`, Reported Date `T0 − 3 hari, pukul 10:00`.
  - DU-002-3: Name `Valve A {runId} - 1`, Asset ID `VLV-0001-{runId}`, Group `Head Office {runId}`, Status `Reported Disposal`, Source `Manual`, Reported By `Agus P`, Reported Date `T0 − 3 hari, pukul 10:00`.
  - DU-002-4: Name `Valve A {runId} - 12`, Asset ID `VLV-0012-{runId}`, Group `Head Office {runId}`, Status `In Disposal Process`, Source `Manual`, Reported By `Agus P`, Reported Date `T0 − 3 hari, pukul 10:00`.
  - DU-002-5: Name `Panel 100% {runId} - 3`, Asset ID `PNL-0003-{runId}`, Group `Head Office {runId}`, Status `Damaged`, Source `Manual`, Reported By `Agus P`, Reported Date `T0 − 3 hari, pukul 10:00`.
  - DU-002-6: Name `Panel 1005 {runId} - 4`, Asset ID `PNL-0004-{runId}`, Group `Head Office {runId}`, Status `Damaged`, Source `Manual`, Reported By `Agus P`, Reported Date `T0 − 3 hari, pukul 10:00`.
  - DU-002-7: Name `<b>Finance</b> {runId} - 5`, Asset ID `FIN-0005-{runId}`, Group `Head Office {runId}`, Status `Damaged`, Source `Manual`, Reported By `Agus P`, Reported Date `T0 − 3 hari, pukul 10:00`.
  - Seluruh record di atas adalah record berjalan dengan Last Holder `—`; pengguna `Agus P` adalah user ber-runId, Pelapor admin.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps

### Kata kunci cocok per kelas kolom searchable
1. Buka tab `Damaged` pada halaman Assets
2. Klik ikon `Search`
3. Ketik Search `Valve Aura {runId}`, tekan Enter
4. Verifikasi baris `Valve Aura {runId} - 2` tampil karena Name cocok
5. Verifikasi baris `Delta {runId} Genset - 1` tidak tampil
6. Ganti isi kotak search dengan `GEN-0001-{runId}`, tekan Enter
7. Verifikasi baris `Delta {runId} Genset - 1` tampil karena Asset ID cocok
8. Verifikasi baris `Valve Aura {runId} - 2` tidak tampil
9. Ganti isi kotak search dengan `Reported Disposal`, tekan Enter
10. Verifikasi baris `Valve A {runId} - 1` tampil karena badge status cocok
11. Verifikasi baris `Delta {runId} Genset - 1` tidak tampil

### Pencocokan substring tanpa membedakan huruf besar dan kecil
12. Ganti isi kotak search dengan `ura {runId}`, tekan Enter
13. Verifikasi baris `Valve Aura {runId} - 2` tampil karena kata kunci cocok di tengah nilai
14. Ganti isi kotak search dengan `VALVE AURA {runId}`, tekan Enter
15. Verifikasi baris `Valve Aura {runId} - 2` tampil walau huruf besar dan kecil berbeda
16. Ganti isi kotak search dengan `Valve A {runId} - 1`, tekan Enter
17. Verifikasi baris `Valve A {runId} - 1` dan `Valve A {runId} - 12` tampil karena satu nilai adalah substring nilai lain
18. Verifikasi baris `Valve Aura {runId} - 2` tidak tampil

### Spasi tepi dibuang dan spasi tengah dipertahankan
19. Ganti isi kotak search dengan ` Valve Aura {runId} `, tekan Enter
20. Verifikasi baris `Valve Aura {runId} - 2` tampil karena spasi di awal dan akhir kata kunci dibuang
21. Ganti isi kotak search dengan `Delta Genset`, tekan Enter
22. Verifikasi baris `Delta {runId} Genset - 1` tidak tampil karena kata kunci dicocokkan sebagai satu rangkaian dan tidak dipecah per kata
23. Ganti isi kotak search dengan `Valve Aura {runId}`, tekan Enter
24. Verifikasi baris `Valve Aura {runId} - 2` tampil karena spasi di tengah kata kunci menjadi bagian dari substring
25. Ganti isi kotak search dengan `   `, tekan Enter
26. Verifikasi tabel memuat lebih dari satu baris karena kata kunci yang hanya berisi spasi diperlakukan sebagai input kosong

### Karakter pola dan payload dicari sebagai teks
27. Ganti isi kotak search dengan `100%`, tekan Enter
28. Verifikasi baris `Panel 100% {runId} - 3` tampil
29. Verifikasi baris `Panel 1005 {runId} - 4` tidak tampil karena `%` dicari sebagai teks
30. Ganti isi kotak search dengan `<script>alert(1)</script>`, tekan Enter
31. Verifikasi tabel menampilkan `No results found`
32. Ganti isi kotak search dengan `' OR '1'='1`, tekan Enter
33. Verifikasi tabel menampilkan `No results found`
34. Ganti isi kotak search dengan `{"$ne": null}`, tekan Enter
35. Verifikasi tabel menampilkan `No results found`
36. Ganti isi kotak search dengan `<b>Finance</b>`, tekan Enter
37. Verifikasi baris `<b>Finance</b> {runId} - 5` tampil dengan teks Name apa adanya, tanpa dirender sebagai HTML

### Kolom tanggal tidak dicari dan kata kunci tanpa hasil
38. Ganti isi kotak search dengan `Valve A {runId} - 1`, tekan Enter
39. Verifikasi kolom Reported Date baris `Valve A {runId} - 1` menampilkan tanggal `T0 − 3 hari` menurut Date Format `dd/MM/yy` dan pukul `10:00` menurut Time Format `24h`
40. Ganti isi kotak search dengan `10:00`, tekan Enter
41. Verifikasi tabel menampilkan `No results found` karena kolom tanggal tidak ikut dicari, walau jam `10:00` tampil di kolom Reported Date
42. Ganti isi kotak search dengan `Tidak Ada Hasil {runId}`, tekan Enter
43. Verifikasi tabel menampilkan `No results found`
44. Verifikasi tabel menampilkan `Try adjusting your search or filter.`

### Kata kunci cocok di dua kolom dan pada kolom yang disembunyikan
45. Ganti isi kotak search dengan `Delta {runId}`, tekan Enter
46. Verifikasi baris `Delta {runId} Genset - 1` tampil karena Name cocok dan baris `Valve Aura {runId} - 2` tampil karena Group cocok
47. Klik header kolom Actions `⋯`
48. Hapus centang `Group`
49. Ganti isi kotak search dengan `Delta {runId}`, tekan Enter
50. Verifikasi baris `Delta {runId} Genset - 1` tampil
51. Verifikasi baris `Valve Aura {runId} - 2` tidak tampil karena kolom Group disembunyikan
52. Centang `Group`
53. Ganti isi kotak search dengan `Delta {runId}`, tekan Enter
54. Verifikasi baris `Valve Aura {runId} - 2` tampil kembali karena kolom Group ditampilkan lagi
55. Ganti isi kotak search dengan `Head Office {runId}`, tekan Enter
56. Verifikasi baris `Delta {runId} Genset - 1`, `Valve A {runId} - 1`, `Valve A {runId} - 12`, `Panel 100% {runId} - 3`, `Panel 1005 {runId} - 4`, dan `<b>Finance</b> {runId} - 5` tampil karena nilai kolom Group sama di semua baris itu
57. Verifikasi baris `Valve Aura {runId} - 2` tidak tampil

### Kolom ikon dicari lewat label aksesibilitasnya
58. Klik header kolom Actions `⋯`
59. Centang `TAG`
60. Ganti isi kotak search dengan `RFID`, tekan Enter
61. Verifikasi baris `Delta {runId} Genset - 1` tampil karena label ikon TAG `RFID` cocok
62. Verifikasi baris `Valve Aura {runId} - 2` tidak tampil
