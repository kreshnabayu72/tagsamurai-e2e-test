---
id: TC-FA-FAFM-E2E-039-android-selection-mode-bulk-download
title: "Mobile: selection mode dan Bulk Download ZIP"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.6#p3"]
smoke: []
dependsOn: []
trace:
  "§4.6#p3": [4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 20, 23, 24, 26, 29, 30, 32, 35, 36, 43, 44, 48, 52, 54, 55, 56, 57, 58, 62, 63, 64, 66, 69, 71, 72, 73, 75, 77, 78, 79, 80, 81, 83]
anchor: [3, 22, 28, 34, 40, 42, 70]
coverage:
  android: automated
---

# Mobile: selection mode dan Bulk Download ZIP

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Data:
  - DU-039-1: Asset `Laptop Dell Latitude {runId}`, status `Active`, Group `Fleet`, ada di entitas aktor.
  - DU-039-2: File `warranty-card-{runId}.pdf`, Source `Attachment`, Category `Asset Documents`, Size `310.0 KB` dari 317440 byte, milik DU-039-1.
  - DU-039-3: File `service-manual-{runId}.pdf`, Source `Attachment`, Category `Asset Documents`, Size `1.2 MB` dari 1258291 byte, milik DU-039-1.
  - DU-039-4: File `insurance-letter-{runId}.pdf`, Source `Attachment`, Category `Asset Documents`, Size `450.2 KB` dari 461005 byte, milik DU-039-1.
  - DU-039-5: File `handover-note-{runId}.pdf`, Source `Attachment`, Category `Asset Documents`, Size `120.0 KB` dari 122880 byte, milik DU-039-1.
  - DU-039-6: Asset `Printer HP M404 {runId}`, status `Disposed`, Group `Fleet`, ada di entitas aktor.
- Kondisi:
  - Retensi Recycle Bin bernilai `30 hari`.
  - Penghitung seleksi tampil `2 Selected` untuk dua kartu terpilih dan `4 Selected` untuk empat kartu terpilih.

## Test Steps

### Kartu pada keadaan normal tanpa kotak seleksi
1. Ketuk tab `Asset Documents`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi kartu `warranty-card-{runId}.pdf` tampil
4. Verifikasi kartu `warranty-card-{runId}.pdf` tidak menampilkan kotak seleksi

### Masuk selection mode dengan tekan lama
5. Tekan lama kartu `warranty-card-{runId}.pdf`
6. Verifikasi kartu `warranty-card-{runId}.pdf` terpilih
7. Verifikasi kartu `service-manual-{runId}.pdf` menampilkan kotak seleksi belum terpilih `[ ]`
8. Verifikasi penghitung seleksi `1 Selected` tampil
9. Verifikasi Floating Bottom Bulk Bar memuat `[✕]`
10. Verifikasi Floating Bottom Bulk Bar memuat `[Select All]`
11. Verifikasi Floating Bottom Bulk Bar memuat `Download (ZIP)`
12. Verifikasi Floating Bottom Bulk Bar memuat `Delete`

### Ketukan memilih dan membatalkan pilihan kartu
13. Ketuk kartu `service-manual-{runId}.pdf`
14. Verifikasi kartu `service-manual-{runId}.pdf` terpilih
15. Verifikasi penghitung seleksi `2 Selected`
16. Ketuk kartu `service-manual-{runId}.pdf`
17. Verifikasi kartu `service-manual-{runId}.pdf` menampilkan kotak seleksi belum terpilih `[ ]`
18. Verifikasi penghitung seleksi `1 Selected`

### Select All memilih seluruh kartu yang dimuat
19. Ketuk `[Select All]`
20. Verifikasi penghitung seleksi `4 Selected`

### Keluar dari selection mode lewat tombol tutup
21. Ketuk `[✕]`
22. Verifikasi kartu `warranty-card-{runId}.pdf` tampil
23. Verifikasi Floating Bottom Bulk Bar tidak tampil
24. Verifikasi kartu `warranty-card-{runId}.pdf` tidak menampilkan kotak seleksi

### Keluar dari selection mode lewat pembatalan seluruh pilihan
25. Tekan lama kartu `service-manual-{runId}.pdf`
26. Verifikasi penghitung seleksi `1 Selected`
27. Ketuk kartu `service-manual-{runId}.pdf`
28. Verifikasi kartu `service-manual-{runId}.pdf` tampil
29. Verifikasi Floating Bottom Bulk Bar tidak tampil
30. Verifikasi kartu `service-manual-{runId}.pdf` tidak menampilkan kotak seleksi

### Keluar dari selection mode lewat tombol Back
31. Tekan lama kartu `service-manual-{runId}.pdf`
32. Verifikasi penghitung seleksi `1 Selected`
33. Tekan tombol Back pada perangkat
34. Verifikasi kartu `service-manual-{runId}.pdf` tampil
35. Verifikasi Floating Bottom Bulk Bar tidak tampil
36. Verifikasi kartu `service-manual-{runId}.pdf` tidak menampilkan kotak seleksi

### Tab Disposed & Unmanaged Assets tanpa selection mode
37. Gulir daftar tab ke kanan sampai tab `Disposed & Unmanaged Assets` terlihat
38. Ketuk tab `Disposed & Unmanaged Assets`
39. Ketik Search `{runId}`, tekan Enter
40. Verifikasi kartu `Printer HP M404 {runId}` tampil
41. Tekan lama kartu `Printer HP M404 {runId}`
42. Verifikasi kartu `Printer HP M404 {runId}` tampil
43. Verifikasi Floating Bottom Bulk Bar tidak tampil
44. Verifikasi kartu `Printer HP M404 {runId}` tidak menampilkan kotak seleksi

### File Preview tampil sebagai bottom sheet
45. Gulir daftar tab ke kiri sampai tab `Asset Documents` terlihat
46. Ketuk tab `Asset Documents`
47. Ketuk File Name `warranty-card-{runId}.pdf` pada kartunya
48. Verifikasi File Preview tampil sebagai bottom sheet berjudul `File Preview`
49. Ketuk `[Close]`

### Bulk Download ZIP dari selection mode
50. Tekan lama kartu `warranty-card-{runId}.pdf`
51. Ketuk kartu `service-manual-{runId}.pdf`
52. Verifikasi penghitung seleksi `2 Selected`
53. Ketuk `Download (ZIP)`
54. Verifikasi berkas `File-Manager-Files.zip` terunduh tanpa dialog
55. Verifikasi berkas ZIP memuat entri `warranty-card-{runId}.pdf`
56. Verifikasi berkas ZIP memuat entri `service-manual-{runId}.pdf`
57. Verifikasi berkas ZIP tidak memuat entri `insurance-letter-{runId}.pdf`
58. Verifikasi Floating Bottom Bulk Bar tidak tampil

### Bulk Delete dari selection mode
59. Tekan lama kartu `insurance-letter-{runId}.pdf`
60. Ketuk kartu `handover-note-{runId}.pdf`
61. Ketuk `Delete` pada Floating Bottom Bulk Bar
62. Verifikasi dialog konfirmasi `Delete Files` tampil sebagai bottom sheet
63. Verifikasi dialog konfirmasi memuat nama `insurance-letter-{runId}.pdf`
64. Verifikasi dialog konfirmasi memuat nama `handover-note-{runId}.pdf`
65. Ketuk `[Cancel]` pada dialog konfirmasi
66. Verifikasi penghitung seleksi `2 Selected`
67. Ketuk `Delete` pada Floating Bottom Bulk Bar
68. Ketuk `[Delete]` pada dialog konfirmasi
69. Verifikasi toast `Success, file has been deleted.` tampil
70. Verifikasi kartu `warranty-card-{runId}.pdf` tampil
71. Verifikasi kartu `insurance-letter-{runId}.pdf` tidak tampil
72. Verifikasi kartu `handover-note-{runId}.pdf` tidak tampil
73. Verifikasi Floating Bottom Bulk Bar tidak tampil

### Recycle Bin sebagai bottom sheet dengan kartu dan seleksi
74. Ketuk ikon dengan label aksesibel `Recycle Bin` pada header kartu Storage Usage
75. Verifikasi Recycle Bin tampil sebagai bottom sheet berjudul `Recycle Bin`
76. Ketik Search `{runId}`, tekan Enter
77. Verifikasi kartu Recycle Bin menampilkan File Name `insurance-letter-{runId}.pdf`
78. Verifikasi kartu `insurance-letter-{runId}.pdf` menampilkan Source `Attachment`
79. Verifikasi kartu `insurance-letter-{runId}.pdf` menampilkan Asset milik DU-039-1
80. Verifikasi kartu `insurance-letter-{runId}.pdf` menampilkan Size `450.2 KB`
81. Verifikasi kartu `insurance-letter-{runId}.pdf` menampilkan Auto-Purge In `30 days`
82. Tekan lama kartu `insurance-letter-{runId}.pdf`
83. Verifikasi Floating Bottom Bulk Bar memuat `Permanently Delete`
84. Ketuk `[✕]`
85. Tutup bottom sheet Recycle Bin
