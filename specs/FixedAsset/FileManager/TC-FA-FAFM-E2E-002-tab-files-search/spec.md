---
id: TC-FA-FAFM-E2E-002-tab-files-search
title: "Search tab Files: hasil pencarian dari data nyata"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-FAFM-01", "TBL-03c", "EB-SRC-1", "EB-SRC-2@tabel-files", "EB-SRC-3@tabel-files", "EB-SRC-5@tabel-files"]
smoke: []
dependsOn: []
trace:
  "T-FAFM-01": [3, 6, 8, 10, 41, 58, 60, 61, 63, 65, 71, 77, 83]
  "TBL-03c": [3, 5, 25, 27]
  "EB-SRC-1": [3, 5, 17]
  "EB-SRC-2@tabel-files": [10, 12, 13, 15]
  "EB-SRC-3@tabel-files": [19, 21, 23, 29, 30, 32, 34, 35, 37, 39, 41]
  "EB-SRC-5@tabel-files": [43, 44, 48, 50, 55]
anchor: [69, 75, 81]
coverage:
  web: automated
---

# Search tab Files: hasil pencarian dari data nyata

## Prerequisites
- Aktor: Total Control, user `Dewi Lestari {runId}` (tampil `Dewi L`), akun aktif dengan kredensial disediakan fase 2.
- Layar awal: halaman Settings > File Manager.
- Data:
  - Group `Divisi Umum {runId}`, `Divisi Aset {runId}`, `Cabang {runId}`, dan `Cabang {runId} Utara` ada di entitas aktor.
  - Aset `Laptop Dell Latitude 5420 {runId}` dan `Printer lintas-{runId}` ada di entitas aktor, dan aset `Mesin Fotokopi Canon {runId}` berstatus Disposed ada di entitas aktor.
  - DU-002-1: File File Name `Procurement-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `150.0 KB`, Uploaded By `Dewi L`.
  - DU-002-2: File File Name `numerik-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `412.7 KB`, Uploaded By `Dewi L`.
  - DU-002-3: File File Name `divisi-aset-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Aset {runId}`, Size `100.0 KB`, Uploaded By `Dewi L`.
  - DU-002-4: File File Name `lintas-{runId}-a.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `100.0 KB`, Uploaded By `Dewi L`.
  - DU-002-5: File File Name `scan-dokumen-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Printer lintas-{runId}`, Group `Divisi Umum {runId}`, Size `100.0 KB`, Uploaded By `Dewi L`.
  - DU-002-6: File File Name `laporan_100%-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `100.0 KB`, Uploaded By `Dewi L`.
  - DU-002-7: File File Name `laporanA1000-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `100.0 KB`, Uploaded By `Dewi L`.
  - DU-002-8: File File Name `budget-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `100.0 KB`, Uploaded By `Dewi L`.
  - DU-002-9: File File Name `annual report-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `100.0 KB`, Uploaded By `Dewi L`.
  - DU-002-10: File File Name `Head Office Room-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `100.0 KB`, Uploaded By `Dewi L`.
  - DU-002-11: File File Name `cabang-utama-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Cabang {runId}`, Size `100.0 KB`, Uploaded By `Dewi L`.
  - DU-002-12: File File Name `cabang-utara-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Cabang {runId} Utara`, Size `100.0 KB`, Uploaded By `Dewi L`.
  - DU-002-13: File File Name `garansi-{runId}.pdf`, File Format `PDF`, Source `Custom Field Document`, Reference `Kartu Garansi {runId}`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `100.0 KB`, Uploaded By `Dewi L`.
  - DU-002-14: File File Name `<b>Finance</b>-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `100.0 KB`, Uploaded By `Dewi L` (nama berkas ber-markup).
  - DU-002-38: File File Name `foto-depan-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `800.0 KB`, Uploaded By `Dewi L`.
  - DU-002-39: File File Name `penemuan-{runId}.jpg`, File Format `JPG`, Source `Found Photo`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Divisi Umum {runId}`, Size `700.0 KB`, Uploaded By `Dewi L`.
  - DU-002-40: File File Name `dsp-bukti-{runId}.pdf`, File Format `PDF`, Source `Disposal Document`, Asset `Mesin Fotokopi Canon {runId}`, Group `Divisi Umum {runId}`, Size `300.0 KB`, Uploaded By `Dewi L`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.

## Test Steps

### Search cocok di tengah nilai dan tidak peka huruf besar-kecil
1. Klik tab `Asset Documents`
2. Ketik Search `curement-{runId}`, tekan Enter
3. Verifikasi baris `Procurement-{runId}.pdf` tampil
4. Ganti isi kotak search dengan `procurement-{runId}`, tekan Enter
5. Verifikasi baris `Procurement-{runId}.pdf` tampil
6. Verifikasi baris `numerik-{runId}.pdf` tidak tampil

### Search cocok pada kolom Size dan kolom Group
7. Ganti isi kotak search dengan `412.7`, tekan Enter
8. Verifikasi baris `numerik-{runId}.pdf` dengan Size `412.7 KB` tampil
9. Ganti isi kotak search dengan `Divisi Aset {runId}`, tekan Enter
10. Verifikasi baris `divisi-aset-{runId}.pdf` dengan Group `Divisi Aset {runId}` tampil

### Kata kunci yang cocok di dua kolom berbeda menampilkan kedua baris
11. Ganti isi kotak search dengan `lintas-{runId}`, tekan Enter
12. Verifikasi baris `lintas-{runId}-a.pdf` yang cocok di kolom File Name tampil
13. Verifikasi baris `scan-dokumen-{runId}.pdf` yang cocok di kolom Asset tampil

### Tanggal tidak cocok lewat Search
14. Ganti isi kotak search dengan bagian tanggal dari Upload Date baris lintas-{runId}-a.pdf, dibaca dari tabel dalam Date Format `dd/MM/yy`, tekan Enter
15. Verifikasi `No results found` tampil

### Kata kunci tanpa kecocokan dan reset oleh query hanya spasi
16. Ganti isi kotak search dengan `zzqx-{runId}`, tekan Enter
17. Verifikasi `No results found` tampil
18. Ganti isi kotak search dengan `   ` (tiga spasi), tekan Enter
19. Verifikasi tabel menampilkan baris data

### Spasi awal dan akhir dibuang, spasi di tengah dipertahankan
20. Ganti isi kotak search dengan ` budget-{runId} `, tekan Enter
21. Verifikasi baris `budget-{runId}.pdf` tampil
22. Ganti isi kotak search dengan `annual report-{runId}`, tekan Enter
23. Verifikasi baris `annual report-{runId}.pdf` tampil
24. Ganti isi kotak search dengan `Head Room-{runId}`, tekan Enter
25. Verifikasi `No results found` tampil karena kata tidak dicari terpisah dari `Head Office Room-{runId}.pdf`

### Nilai yang menjadi substring nilai lain
26. Ganti isi kotak search dengan `Cabang {runId}`, tekan Enter
27. Verifikasi baris `cabang-utama-{runId}.pdf` dengan Group `Cabang {runId}` tampil

### Karakter khusus dicari sebagai teks
28. Ganti isi kotak search dengan `_100%-{runId}`, tekan Enter
29. Verifikasi baris `laporan_100%-{runId}.pdf` tampil
30. Verifikasi baris `laporanA1000-{runId}.pdf` tidak tampil
31. Ganti isi kotak search dengan `.*-{runId}`, tekan Enter
32. Verifikasi `No results found` tampil

### Payload skrip dan injeksi dicari sebagai teks biasa
33. Ganti isi kotak search dengan `<script>alert(1)</script>`, tekan Enter
34. Verifikasi `No results found` tampil
35. Verifikasi tidak ada dialog skrip yang muncul
36. Ganti isi kotak search dengan `' OR '1'='1`, tekan Enter
37. Verifikasi `No results found` tampil
38. Ganti isi kotak search dengan `{"$ne": null}`, tekan Enter
39. Verifikasi `No results found` tampil

### Nama berkas ber-markup tampil sebagai teks
40. Ganti isi kotak search dengan `<b>Finance</b>-{runId}`, tekan Enter
41. Verifikasi baris `<b>Finance</b>-{runId}.pdf` tampil dengan teks nama berkas apa adanya tanpa cetak tebal

### Kolom searchable yang disembunyikan tidak lagi cocok dan cocok lagi saat ditampilkan
42. Ganti isi kotak search dengan `Kartu Garansi {runId}`, tekan Enter
43. Verifikasi baris `garansi-{runId}.pdf` dengan Reference `Kartu Garansi {runId}` tampil
44. Verifikasi kolom `Reference` tampil di tabel
45. Klik header kolom `Actions` (`⋯`) pada tabel
46. Hilangkan centang kolom `Reference` pada panel Column Visibility
47. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
48. Verifikasi kolom `Reference` tidak tampil di tabel
49. Ganti isi kotak search dengan `Kartu Garansi {runId}`, tekan Enter
50. Verifikasi `No results found` tampil
51. Klik header kolom `Actions` (`⋯`) pada tabel
52. Centang kolom `Reference` pada panel Column Visibility
53. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
54. Ganti isi kotak search dengan `Kartu Garansi {runId}`, tekan Enter
55. Verifikasi baris `garansi-{runId}.pdf` tampil kembali
56. Klik `(←)` pada kotak Search

### Search cocok pada kolom File Format, Source, Asset ID, dan Uploaded By
57. Ketik Search `PDF`, tekan Enter
58. Verifikasi baris `Procurement-{runId}.pdf` dengan File Format `PDF` tampil
59. Ganti isi kotak search dengan `Custom Field Document`, tekan Enter
60. Verifikasi baris `garansi-{runId}.pdf` dengan Source `Custom Field Document` tampil
61. Verifikasi baris `Procurement-{runId}.pdf` dengan Source `Attachment` tidak tampil
62. Ganti isi kotak search dengan Asset ID milik DU-002-5, tekan Enter
63. Verifikasi baris `scan-dokumen-{runId}.pdf` dengan Asset ID milik aset `Printer lintas-{runId}` tampil
64. Ganti isi kotak search dengan `Dewi L`, tekan Enter
65. Verifikasi baris `Procurement-{runId}.pdf` dengan Uploaded By `Dewi L` tampil
66. Klik `(←)` pada kotak Search

### Source tidak dicari di tab yang tidak punya kolom Source
67. Klik tab `Asset Photo`
68. Ketik Search `foto-depan-{runId}`, tekan Enter
69. Verifikasi baris `foto-depan-{runId}.jpg` tampil
70. Ganti isi kotak search dengan `Asset Photo`, tekan Enter
71. Verifikasi `No results found` tampil
72. Klik `(←)` pada kotak Search
73. Klik tab `Missing`
74. Ketik Search `penemuan-{runId}`, tekan Enter
75. Verifikasi baris `penemuan-{runId}.jpg` tampil
76. Ganti isi kotak search dengan `Found Photo`, tekan Enter
77. Verifikasi `No results found` tampil
78. Klik `(←)` pada kotak Search
79. Klik tab `Disposal`
80. Ketik Search `dsp-bukti-{runId}`, tekan Enter
81. Verifikasi baris `dsp-bukti-{runId}.pdf` tampil
82. Ganti isi kotak search dengan `Disposal Document`, tekan Enter
83. Verifikasi `No results found` tampil
84. Klik `(←)` pada kotak Search
