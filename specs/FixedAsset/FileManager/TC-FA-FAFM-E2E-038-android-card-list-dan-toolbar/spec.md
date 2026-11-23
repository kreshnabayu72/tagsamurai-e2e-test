---
id: TC-FA-FAFM-E2E-038-android-card-list-dan-toolbar
title: "Mobile: kartu Storage Usage, Card List file dan aset, serta toolbar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-FAFM-01", "T-FAFM-02", "§4.6#p1", "§4.6#p2"]
smoke: []
dependsOn: []
trace:
  "T-FAFM-01": [21, 22, 23, 30, 33, 34, 35]
  "T-FAFM-02": [39, 40, 41, 42, 43, 44, 45]
  "§4.6#p1": [21, 39]
  "§4.6#p2": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 16, 17, 18, 25, 26, 35, 46, 47, 48, 52, 53, 56, 57, 61, 62, 66, 67]
anchor: []
coverage:
  android: automated
---

# Mobile: kartu Storage Usage, Card List file dan aset, serta toolbar

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Data:
  - DU-038-1: Asset `Laptop Dell Latitude {runId}`, status `Active`, Group `Fleet`, ada di entitas aktor.
  - DU-038-2: File `laptop-front-{runId}.jpg`, Source `Asset Photo`, Category `Asset Photo`, Size `820.4 KB` dari 840090 byte, milik DU-038-1.
  - DU-038-3: File `warranty-card-{runId}.pdf`, Source `Attachment`, Category `Asset Documents`, Size `310.0 KB` dari 317440 byte, milik DU-038-1.
  - DU-038-4: Asset `Printer HP M404 {runId}`, status `Disposed`, Group `Fleet`, ada di entitas aktor.
  - DU-038-5: File `dsp-auction-receipt-{runId}.pdf`, Source `Disposal Document`, Category `Disposal`, Size `3.2 MB` dari 3355443 byte, milik DU-038-4.
  - DU-038-6: Asset `Monitor LG 24 {runId}`, status `Unmanaged`, Group `Fleet`, tanpa file, ada di entitas aktor.
  - DU-038-7: File `found-photo-{runId}.jpg`, Source `Found Photo`, Category `Missing`, Size `45.0 KB` dari 46080 byte, milik DU-038-1.
  - Total Size aset adalah Data & Log Size ditambah Files Size. `Printer HP M404 {runId}` memiliki Data & Log Size `50.0 KB` dan Files Size `3.2 MB`; `Monitor LG 24 {runId}` memiliki Data & Log Size `50.0 KB` dan Files Size `0.0 KB`. Karena itu Total Size `Printer HP M404 {runId}` lebih besar daripada Total Size `Monitor LG 24 {runId}`.
- Kondisi:
  - Storage Quota pada kartu Storage Usage terisi dan lebih besar dari `0.0 GB`.

## Test Steps

### Header halaman dan kartu Storage Usage
1. Verifikasi header halaman menampilkan Breadcrumb `Settings > File Manager`
2. Verifikasi header halaman menampilkan tombol bantuan `[?]`
3. Verifikasi kartu `Storage Usage` tampil
4. Verifikasi kartu memuat `Total Used`
5. Verifikasi kartu memuat `Storage Quota`
6. Verifikasi kartu memuat `Fixed Asset` beserta ukurannya
7. Verifikasi header kartu memuat ikon dengan label aksesibel `Changelog`
8. Verifikasi header kartu memuat ikon dengan label aksesibel `Recycle Bin`

### Tab Kategori dan tab Disposed & Unmanaged Assets
9. Verifikasi tab Kategori `Asset Photo`, `Asset Documents`, `Damaged`, `Missing`, `Maintenance`, `Disposal`, `Borrow`, `Assignment`, dan `Transfer` tampil
10. Gulir daftar tab ke kanan sampai tab `Disposed & Unmanaged Assets` terlihat
11. Verifikasi tab `Disposed & Unmanaged Assets` tampil
12. Gulir daftar tab ke kiri sampai tab `Asset Photo` terlihat

### Toolbar dan bottom sheet
13. Verifikasi toolbar memuat `[🔍]`
14. Verifikasi toolbar memuat `[⋯]`
15. Ketuk `[⋯]` pada toolbar
16. Verifikasi bottom sheet memuat `Column Visibility`
17. Verifikasi bottom sheet memuat `Filter`
18. Verifikasi bottom sheet memuat `Download`
19. Tutup bottom sheet

### Card List file pada tab Asset Photo
20. Ketik Search `{runId}`, tekan Enter
21. Verifikasi daftar file tampil sebagai Card List dengan kartu `laptop-front-{runId}.jpg`
22. Verifikasi kartu `laptop-front-{runId}.jpg` menampilkan Asset milik DU-038-1
23. Verifikasi kartu `laptop-front-{runId}.jpg` menampilkan Size `820.4 KB`
24. Ketuk `[⋯]` pada kartu `laptop-front-{runId}.jpg`
25. Verifikasi menu aksi kartu memuat `Download`
26. Verifikasi menu aksi kartu memuat `Delete`
27. Tutup menu aksi kartu

### Source pada Card List per Kategori
28. Ketuk tab `Asset Documents`
29. Ketik Search `{runId}`, tekan Enter
30. Verifikasi kartu `warranty-card-{runId}.pdf` menampilkan Source `Attachment`
31. Ketuk tab `Disposal`
32. Ketik Search `{runId}`, tekan Enter
33. Verifikasi kartu `dsp-auction-receipt-{runId}.pdf` menampilkan Size `3.2 MB`
34. Verifikasi kartu `dsp-auction-receipt-{runId}.pdf` menampilkan Asset milik DU-038-4
35. Verifikasi kartu `dsp-auction-receipt-{runId}.pdf` tidak menampilkan Source `Disposal Document`

### Card List aset pada tab Disposed & Unmanaged Assets
36. Gulir daftar tab ke kanan sampai tab `Disposed & Unmanaged Assets` terlihat
37. Ketuk tab `Disposed & Unmanaged Assets`
38. Ketik Search `{runId}`, tekan Enter
39. Verifikasi daftar aset tampil sebagai Card List dengan kartu `Printer HP M404 {runId}`
40. Verifikasi kartu `Monitor LG 24 {runId}` tampil
41. Verifikasi kartu `Printer HP M404 {runId}` menampilkan Status `Disposed`
42. Verifikasi kartu `Printer HP M404 {runId}` menampilkan Group `Fleet`
43. Verifikasi kartu `Printer HP M404 {runId}` menampilkan Total Size
44. Verifikasi kartu `Monitor LG 24 {runId}` menampilkan Status `Unmanaged`
45. Verifikasi kartu `Printer HP M404 {runId}` berada di atas kartu `Monitor LG 24 {runId}`
46. Verifikasi kartu `Printer HP M404 {runId}` tidak memiliki `[⋯]` row action

### Isi kartu Storage Usage: ProgressBar dan urutan elemen
47. Verifikasi kartu `Storage Usage` memuat ProgressBar dengan label `[Percent]%`
48. Verifikasi isi kartu `Storage Usage` berurutan: `Total Used`, `Storage Quota`, ProgressBar, lalu `Fixed Asset`

### Source disembunyikan pada kartu Kategori Asset Photo dan Missing
49. Gulir daftar tab ke kiri sampai tab `Asset Photo` terlihat
50. Ketuk tab `Asset Photo`
51. Ketik Search `{runId}`, tekan Enter
52. Verifikasi kartu `laptop-front-{runId}.jpg` menampilkan Asset milik DU-038-1
53. Verifikasi kartu `laptop-front-{runId}.jpg` tidak menampilkan Source `Asset Photo`
54. Ketuk tab `Missing`
55. Ketik Search `{runId}`, tekan Enter
56. Verifikasi kartu `found-photo-{runId}.jpg` menampilkan Asset milik DU-038-1
57. Verifikasi kartu `found-photo-{runId}.jpg` tidak menampilkan Source `Found Photo`

### Name pada kartu aset berupa teks biasa
58. Gulir daftar tab ke kanan sampai tab `Disposed & Unmanaged Assets` terlihat
59. Ketuk tab `Disposed & Unmanaged Assets`
60. Ketik Search `{runId}`, tekan Enter
61. Verifikasi kartu aset menampilkan Name `Printer HP M404 {runId}`
62. Verifikasi Name `Printer HP M404 {runId}` pada kartunya berupa teks biasa, bukan tautan

### Kolom lain hanya di desktop tidak tampil pada kartu file
63. Gulir daftar tab ke kiri sampai tab `Asset Documents` terlihat
64. Ketuk tab `Asset Documents`
65. Ketik Search `{runId}`, tekan Enter
66. Verifikasi kartu `warranty-card-{runId}.pdf` menampilkan Asset milik DU-038-1
67. Verifikasi kartu `warranty-card-{runId}.pdf` tidak menampilkan kolom `Asset ID`, `Group`, `Uploaded By`, `Upload Date`, `File Format`, dan `Reference`
