---
id: TC-FA-FASVC-BE-067-be-validasi-name-dan-normalisasi
title: "Server: Validasi Name: Wajib, Unik Case-insensitive Setelah Trim, Maks 120, dan Emoji"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["V-FASVC-01", "V-FASVC-02", "V-FASVC-03", "V-FASVC-36", "FLD-FASVC-01", "FASVC-LOGIC-02a", "FASVC-LOGIC-02b", "§9.2#p2", "EC-FASVC-01", "EC-FASVC-20a", "EC-FASVC-20b", "EC-FASVC-20c", "F-FASVC-02.k2", "F-FASVC-02.k9", "EB-FRM-4@name", "EB-FRM-5@name-service-center"]
smoke: []
dependsOn: []
trace:
  "V-FASVC-01": [4, 8]
  "V-FASVC-02": [11, 13, 15, 50, 52, 54, 56]
  "V-FASVC-03": [46, 48]
  "V-FASVC-36": [34]
  "FLD-FASVC-01": [4, 11, 26, 27, 42, 46]
  "FASVC-LOGIC-02a": [11, 13, 15, 17, 22, 23, 50, 52, 54, 56, 58]
  "FASVC-LOGIC-02b": [6]
  "§9.2#p2": [6, 13, 15, 27, 42, 60, 63, 65, 67, 69, 71]
  "EC-FASVC-01": [13, 15, 52, 54]
  "EC-FASVC-20a": [31, 32]
  "EC-FASVC-20b": [43]
  "EC-FASVC-20c": [34, 36]
  "F-FASVC-02.k2": [13, 15, 19, 52, 54]
  "F-FASVC-02.k9": [31, 32, 34]
  "EB-FRM-4@name": [41, 46]
  "EB-FRM-5@name-service-center": [11, 50]
anchor: []
---

# Server: Validasi Name: Wajib, Unik Case-insensitive Setelah Trim, Maks 120, dan Emoji

## Prerequisites
- Aktor: Total Control pada client suite.
- Data:
  - DU-067-1: Service Center `PT Sejuk Abadi Teknik {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, Company email `admin@sejukabadi.co.id`, Status `Active`, ada di client suite.
  - DU-067-2: Service Center `Bengkel Maju Motor {runId}`, Service type `Repair`, Available to `All groups`, Country `Indonesia`, City `Bandung`, Company email `servis@majumotor.co.id`, Status `Active`, ada di client suite.
  - DU-067-3: Service Center `Sinar Mitra Teknik {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `info@sinarmitra.co.id`, Status `Active`, ada di client lain dan tidak ada di client suite.
  - Setiap Create yang dikirim memuat field wajib lain bernilai Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan {runId}`, dan Company email `admin@sejukabadi.co.id`; Name dikirim sesuai langkah.
  - Setiap Edit yang dikirim memuat versi data terkini dan nilai tersimpan untuk semua field selain Name.
- Kondisi:
  - Lisensi addon Maintenance aktif pada client suite.

## Test Steps

### Name kosong dan hanya spasi ditolak
1. Baca daftar Service Center client suite dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N0
2. Baca baris `PT Sejuk Abadi Teknik {runId}` dan `Bengkel Maju Motor {runId}` di hasil pencarian, yang termasuk dalam N0
3. Kirim Create dengan Name dikosongkan dan City `Jakarta Selatan {runId}`
4. Verifikasi permintaan ditolak dengan pesan `Name must not be empty`
5. Kirim Create dengan Name `"   "` (tiga spasi saja) dan City `Jakarta Selatan {runId}`
6. Verifikasi permintaan ditolak dengan pesan `Name must not be empty` karena Name yang hanya berisi spasi dianggap kosong
7. Baca ulang daftar Service Center client suite dengan pencarian `{runId}`
8. Verifikasi jumlah baris tetap N0, sehingga kedua permintaan tidak membuat Service Center

### Name duplikat ditolak tanpa membedakan huruf besar-kecil dan spasi tepi
9. Baca Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}` dan catat jumlah entrinya sebagai L0
10. Kirim Create dengan Name `PT Sejuk Abadi Teknik {runId}`, sama persis dengan DU-067-1
11. Verifikasi permintaan ditolak dengan pesan `Name already exists`
12. Kirim Create dengan Name `PT SEJUK ABADI TEKNIK {runId}`, hanya beda huruf besar-kecil dari DU-067-1
13. Verifikasi permintaan ditolak dengan pesan `Name already exists`
14. Kirim Create dengan Name `"  PT Sejuk Abadi Teknik {runId}  "`, yaitu DU-067-1 yang diapit dua spasi di awal dan di akhir
15. Verifikasi permintaan ditolak dengan pesan `Name already exists`
16. Baca ulang daftar Service Center client suite dengan pencarian `{runId}`
17. Verifikasi jumlah baris tetap N0, sehingga tidak ada Service Center ganda
18. Baca ulang Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}`
19. Verifikasi jumlah entri tetap L0, sehingga penolakan tidak menulis log

### Name yang sama di client lain diterima
20. Kirim Create dengan Name `Sinar Mitra Teknik {runId}`, sama dengan DU-067-3 yang ada di client lain
21. Baca daftar Service Center client suite dengan pencarian `Sinar Mitra Teknik {runId}`
22. Verifikasi hasil memuat tepat satu baris dengan Name `Sinar Mitra Teknik {runId}`
23. Verifikasi Name itu tidak ditolak `Name already exists`, karena keunikan Name hanya berlaku per client

### Name tersimpan sesuai ketikan setelah trim
24. Kirim Create dengan Name `"  Citra Servis Mandiri {runId}  "`, yaitu diapit dua spasi di awal dan di akhir
25. Baca daftar Service Center client suite dengan pencarian `Citra Servis Mandiri {runId}`
26. Verifikasi hasil memuat tepat satu baris dengan Name `Citra Servis Mandiri {runId}`
27. Verifikasi Name tersimpan tanpa spasi di awal dan di akhir

### Karakter non-Latin dan simbol diterima, emoji ditolak
28. Kirim Create dengan Name `Pusat Servis 東京 {runId}`
29. Kirim Create dengan Name `Servis & Teknik (Jaya) #1 {runId}`
30. Baca daftar Service Center client suite dengan pencarian `{runId}` dan catat jumlah barisnya sebagai K1
31. Verifikasi Service Center dengan Name `Pusat Servis 東京 {runId}` tersimpan
32. Verifikasi Service Center dengan Name `Servis & Teknik (Jaya) #1 {runId}` tersimpan
33. Kirim Create dengan Name `Servis Cepat 🔧 {runId}`
34. Verifikasi permintaan ditolak dengan pesan `Name contains invalid characters`
35. Baca ulang daftar Service Center client suite dengan pencarian `{runId}`
36. Verifikasi jumlah baris tetap K1, sehingga Name berisi emoji tidak tersimpan

### Panjang Name tepat di batas diterima dan di atas batas ditolak
37. Kirim Create dengan Name `Layanan Perbaikan Peralatan Industri Terpadu Nusantara Cabang Wilayah Jawa Barat Sentosa Makmur Lestari Mandiri Jaya Eka` (120 karakter) dan City `Jakarta Selatan {runId}`
38. Kirim Create dengan Name `Pusat Kalibrasi Instrumen Presisi Laboratorium Uji Mutu Nasional Cabang Medan Sumatera Utara Kawasan Industri Terpadu 01` (120 karakter) diapit dua spasi di awal dan di akhir, dan City `Jakarta Selatan {runId}`
39. Kirim Create dengan Name `Kantor Layanan Teknik Cabang Medan Élan Sumatera Utara 𝒜 Perawatan Mesin Pabrik Terpadu Kawasan Industri Medan Deli Raya` (120 karakter, memuat huruf beraksen `É` dan karakter non-BMP `𝒜`) dan City `Jakarta Selatan {runId}`
40. Baca daftar Service Center client suite dengan pencarian `{runId}`
41. Verifikasi Service Center dengan Name `Layanan Perbaikan Peralatan Industri Terpadu Nusantara Cabang Wilayah Jawa Barat Sentosa Makmur Lestari Mandiri Jaya Eka` tersimpan utuh
42. Verifikasi Service Center dengan Name `Pusat Kalibrasi Instrumen Presisi Laboratorium Uji Mutu Nasional Cabang Medan Sumatera Utara Kawasan Industri Terpadu 01` tersimpan tanpa spasi di awal dan di akhir
43. Verifikasi Service Center dengan Name `Kantor Layanan Teknik Cabang Medan Élan Sumatera Utara 𝒜 Perawatan Mesin Pabrik Terpadu Kawasan Industri Medan Deli Raya` tersimpan utuh, karena batas dihitung per karakter Unicode
44. Catat jumlah baris hasil pencarian `{runId}` sebagai K2
45. Kirim Create dengan Name `Bengkel Resmi Alat Berat Konstruksi dan Pertambangan Wilayah Kalimantan Timur Samarinda Balikpapan Kutai Kartanegara Raya` (121 karakter) dan City `Jakarta Selatan {runId}`
46. Verifikasi permintaan ditolak dengan pesan `Max. 120 characters` pada Name, karena panjang Name 121 karakter melebihi batas
47. Baca ulang daftar Service Center client suite dengan pencarian `{runId}`
48. Verifikasi jumlah baris tetap K2, sehingga Name 121 karakter tidak tersimpan

### Edit: Name duplikat ditolak dan nama sendiri tidak dianggap duplikat
49. Kirim Edit atas `Bengkel Maju Motor {runId}` dengan Name diganti `PT Sejuk Abadi Teknik {runId}`
50. Verifikasi permintaan ditolak dengan pesan `Name already exists`
51. Kirim Edit atas `Bengkel Maju Motor {runId}` dengan Name diganti `PT SEJUK ABADI TEKNIK {runId}`
52. Verifikasi permintaan ditolak dengan pesan `Name already exists`
53. Kirim Edit atas `Bengkel Maju Motor {runId}` dengan Name diganti `"  PT Sejuk Abadi Teknik {runId}  "`, yaitu diapit dua spasi di awal dan di akhir
54. Verifikasi permintaan ditolak dengan pesan `Name already exists`
55. Baca Service Center `Bengkel Maju Motor {runId}` dari daftar dengan pencarian `Bengkel Maju Motor {runId}`
56. Verifikasi Name tersimpan tetap `Bengkel Maju Motor {runId}`
57. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan Name hanya diubah kapitalisasinya menjadi `PT SEJUK ABADI TEKNIK {runId}`
58. Verifikasi permintaan tidak ditolak `Name already exists`, karena Service Center itu tidak dihitung sebagai duplikat dirinya sendiri
59. Baca Service Center `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
60. Verifikasi Name tersimpan tetap `PT Sejuk Abadi Teknik {runId}`, karena Edit yang hanya mengubah kapitalisasi adalah Edit No-Op

### Edit No-Op: kapitalisasi dan spasi tepi tidak mengubah data dan tidak mencatat log
61. Baca Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}` dan catat jumlah entrinya sebagai L1
62. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan Name hanya diubah kapitalisasinya menjadi `PT SEJUK ABADI TEKNIK {runId}`
63. Verifikasi permintaan dijawab No-Op dengan pesan `No changes to save.`
64. Baca ulang Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}`
65. Verifikasi jumlah entri tetap L1, sehingga Edit No-Op kapitalisasi tidak menulis log
66. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan Name `"  PT Sejuk Abadi Teknik {runId}  "`, yaitu diapit dua spasi di awal dan di akhir, tanpa perubahan field lain
67. Verifikasi permintaan dijawab No-Op dengan pesan `No changes to save.`
68. Baca Service Center `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
69. Verifikasi Name tersimpan tetap `PT Sejuk Abadi Teknik {runId}` tanpa spasi di awal dan di akhir, karena Edit yang hanya mengubah spasi tepi adalah Edit No-Op
70. Baca ulang Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}`
71. Verifikasi jumlah entri tetap L1, sehingga Edit No-Op spasi tepi tidak menulis log
