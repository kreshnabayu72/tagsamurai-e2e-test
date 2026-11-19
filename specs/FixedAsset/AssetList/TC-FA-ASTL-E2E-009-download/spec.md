---
id: TC-FA-ASTL-E2E-009-download
title: "Download hasil tabel All Assets"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#r6", "§9.6#r7", "EB-DL-1@tabel-all-assets", "EB-DL-2@tabel-all-assets", "EB-DL-3@tabel-all-assets", EB-DL-4]
smoke: [EB-DL-4]
dependsOn: []
trace:
  "§5#r6": [9, 14, 15, 16, 18, 35]
  "§9.6#r7": [8, 13]
  "EB-DL-1@tabel-all-assets": [9, 10, 11, 26, 43, 50, 42, 49]
  "EB-DL-2@tabel-all-assets": [12, 28]
  "EB-DL-3@tabel-all-assets": [8, 24]
  EB-DL-4: [16, 17, 19, 20, 27]
anchor: [25, 34]
coverage:
  web: automated
---

# Download hasil tabel All Assets

## Prerequisites
- Aktor: Total Control `Hendra Wijaya {runId}`.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-009-1: User `Hendra Wijaya {runId}`, role Total Control, cakupan seluruh client, memakai konfigurasi kolom bawaan.
  - DU-009-2: 12 aset `Printer Epson - {n} {runId}` dengan `n` dari 1 sampai 12, Brand `Epson`, Purchase Cost `8500000` (tampil `Rp 8.500.000,00`), tanpa Division, tanpa Asset Class dan Tax Depreciation Class, berstatus `Available`.
  - DU-009-3: Aset `Printer Epson - 1 {runId}` memiliki tiga label: `Aset Kantor`, `Kalibrasi`, dan `Prioritas`.
  - DU-009-4: Aset `Printer Epson - 12 {runId}` belum diisi Purchase Cost-nya (sel `Purchase Cost` bernilai `Pending`).
  - DU-009-5: Berkas hasil Download dengan nama dari nama berkas `All-Assets`: `All-Assets.csv` untuk pilihan CSV dan `All-Assets.xlsx` untuk pilihan XLSX.
  - DU-009-6: Aset `Printer Canon - 1 {runId}`, Brand `Canon`, berstatus `Borrowed`.
  - Tabel menampilkan 10 baris per halaman, jadi 12 aset DU-009-2 tidak muat dalam satu halaman.
- Kondisi:
  - Akun `Hendra Wijaya {runId}` aktif dan kredensialnya tersedia.
  - Date Format bernilai `dd/MM/yy`.

## Test Steps

### Berkas CSV memuat seluruh baris dan kolom yang tampil
1. Masuk sebagai `Hendra Wijaya {runId}`
2. Klik menu `Fixed Asset > Assets` pada sidebar
3. Klik header kolom `Actions`
4. Centang kolom `Purchase Cost` pada panel Column Visibility
5. Hilangkan centang kolom `Brand` pada panel Column Visibility
6. Klik ikon Download
7. Pilih `Download as CSV`
8. Verifikasi berkas `All-Assets.csv` terunduh
9. Verifikasi berkas memuat 12 baris `Printer Epson - {n} {runId}`, termasuk baris yang tidak tampil pada halaman aktif
10. Verifikasi berkas memuat kolom `Purchase Cost`
11. Verifikasi berkas tidak memuat kolom `Brand` yang disembunyikan
12. Verifikasi tidak ada toast sukses sesudah berkas terunduh
13. Verifikasi tombol Download dapat diklik kembali sesudah berkas terunduh

### Isi berkas menurut tipe kolom
14. Verifikasi sel `Purchase Cost` baris `Printer Epson - 1 {runId}` ditulis angka mentah `8500000`, bukan `Rp 8.500.000,00`
15. Verifikasi sel `Purchase Cost` baris `Printer Epson - 12 {runId}` ditulis kosong, bukan `-` dan bukan `Pending`
16. Verifikasi sel `Division` baris `Printer Epson - 1 {runId}` ditulis `-`
17. Verifikasi sel `Labels` baris `Printer Epson - 1 {runId}` memuat `Aset Kantor`, `Kalibrasi`, dan `Prioritas` seluruhnya, dipisah koma dan spasi
18. Verifikasi kolom `Register Date` ditulis menurut Date Format `dd/MM/yy`
19. Verifikasi kolom `Photo` tidak ikut tertulis di berkas
20. Verifikasi berkas CSV berenkode UTF-8 dengan BOM

### Berkas XLSX hanya memuat hasil Search
21. Ketik Search `Printer Epson - 12 {runId}`, tekan Enter
22. Klik ikon Download
23. Pilih `Download as XLSX`
24. Verifikasi berkas `All-Assets.xlsx` terunduh
25. Verifikasi berkas memuat baris `Printer Epson - 12 {runId}`
26. Verifikasi berkas tidak memuat baris `Printer Epson - 1 {runId}` yang tersaring oleh Search
27. Verifikasi berkas XLSX memuat satu sheet bernama `Sheet1`
28. Verifikasi tidak ada toast sukses sesudah berkas terunduh

### Kolom Tax Depreciation Class kosong ditulis tanda hubung di berkas
29. Ketik Search `Printer Epson - 1 {runId}`, tekan Enter
30. Klik header kolom `Actions`
31. Centang kolom `Tax Depreciation Class` pada panel Column Visibility
32. Klik ikon Download
33. Pilih `Download as CSV`
34. Verifikasi berkas `All-Assets.csv` terunduh
35. Verifikasi sel `Tax Depreciation Class` baris `Printer Epson - 1 {runId}` ditulis `-`

### Download mengikuti Filter Panel dan kartu aktif
36. Ketik Search `{runId}`, tekan Enter
37. Klik ikon Filter
38. Isi Min pada Purchase Cost dengan `8500000`
39. Klik `[Apply]`
40. Klik ikon Download
41. Pilih `Download as CSV`
42. Verifikasi berkas memuat baris `Printer Epson - 1 {runId}` yang Purchase Cost-nya `8500000`
43. Verifikasi berkas tidak memuat baris `Printer Epson - 12 {runId}` yang Purchase Cost-nya `Pending` dan tidak cocok dengan saringan
44. Klik `[Clear Field]`
45. Klik `[Apply]`
46. Klik kartu `Available`
47. Klik ikon Download
48. Pilih `Download as CSV`
49. Verifikasi berkas memuat baris `Printer Epson - 1 {runId}` yang berstatus `Available`
50. Verifikasi berkas tidak memuat baris `Printer Canon - 1 {runId}` yang berstatus `Borrowed` di luar kartu `Available`
51. Klik kartu `All`
