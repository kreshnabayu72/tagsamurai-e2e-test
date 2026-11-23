---
id: TC-FA-FAFM-UI-075-halaman-file-manager
title: "Halaman File Manager: Breadcrumb, struktur, dan aksesibilitas dasar"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["INV-01a", "§4.2#p3", "§4.2#p4", "§4.5#b2", "§4.5#b4", "EB-TBL-11"]
smoke: []
dependsOn: []
trace:
  "INV-01a": [16, 19]
  "§4.2#p3": [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 26, 27, 30, 34]
  "§4.2#p4": [2, 6, 8, 31, 32]
  "§4.5#b2": [37, 38]
  "§4.5#b4": [40, 41, 42, 43, 44, 45, 47, 48, 50, 52, 53]
  "EB-TBL-11": [3, 4]
anchor: [33, 36]
coverage:
  web: automated
---

# Halaman File Manager: Breadcrumb, struktur, dan aksesibilitas dasar

## Prerequisites
- Aktor: Total Control.
- Layar awal: Halaman File Manager.
- Komponen: Halaman File Manager.
- Data:
  - DU-075-1: kartu Storage Usage di bawah kuota, Total Used `4.8 GB`, Storage Quota `50.0 GB`, Fixed Asset `3.2 GB`.
  - DU-075-2: file `laptop-front.jpg`, File Format `JPG`, Source `Asset Photo`, Reference `—`, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `820.4 KB`, Uploaded By `Budi S`, Upload Date `02/11/26 14:30`.
  - DU-075-3: aset Asset Data `Printer HP M404 - 1`, Asset ID `PRN-2026-0001`, Group `Branch Bandung`, Status `Disposed`, Data & Log Size `1.2 MB`, Files Size `5.8 MB`, Total Size `7.0 MB`.
  - DU-075-4: aset Asset Data `Monitor LG 24 - 7`, Asset ID `MON-2026-0007`, Group `Head Office`, Status `Unmanaged`, Data & Log Size `412.0 KB`, Files Size `0.0 KB`, Total Size `412.0 KB`.
  - DU-075-5: kartu Storage Usage penuh, Total Used `50.4 GB`, Storage Quota `50.0 GB`, Fixed Asset `48.8 GB`.
- Kondisi:
  - K1: kartu Storage Usage berisi DU-075-1, tab Kategori pertama berisi DU-075-2, tab Asset Data berisi DU-075-3 dan DU-075-4, lebar tampilan lebar.
  - K2: sama dengan K1, lebar tampilan sempit.
  - K3: kartu Storage Usage berisi DU-075-5.

## Test Steps

### Breadcrumb statis dan tanpa judul halaman terpisah
1. Tampilkan Halaman File Manager dengan kondisi K1
2. Verifikasi Breadcrumb `Settings > File Manager` tampil
3. Verifikasi segmen pertama `Settings` pada Breadcrumb bukan tautan yang bisa diklik
4. Verifikasi segmen terakhir `File Manager` pada Breadcrumb bukan tautan yang bisa diklik
5. Verifikasi tombol bantuan `[?]` tampil pada baris Breadcrumb
6. Verifikasi tidak ada elemen judul halaman terpisah di antara Breadcrumb dan konten halaman
7. Klik tab Kategori `Damaged`
8. Verifikasi Breadcrumb tetap `Settings > File Manager`

### Isi halaman: kartu Storage Usage, tab, toolbar, dan tabel
9. Tampilkan Halaman File Manager dengan kondisi K1
10. Verifikasi kartu `Storage Usage` tampil
11. Verifikasi tombol Changelog tampil pada header kartu Storage Usage
12. Verifikasi tombol Recycle Bin tampil pada header kartu Storage Usage
13. Verifikasi `Total Used` tampil pada kartu Storage Usage
14. Verifikasi `Storage Quota` tampil pada kartu Storage Usage
15. Verifikasi `Fixed Asset` tampil pada kartu Storage Usage
16. Verifikasi tab Kategori tampil sebagai himpunan `Asset Photo`, `Asset Documents`, `Damaged`, `Missing`, `Maintenance`, `Disposal`, `Borrow`, `Assignment`, dan `Transfer`
17. Verifikasi tab `Disposed & Unmanaged Assets` tampil
18. Verifikasi ikon Search, ikon Filter, dan ikon Download tampil pada toolbar tabel
19. Verifikasi header kolom `File Name` tampil pada tabel Files
20. Verifikasi kontrol Pagination tampil di bawah tabel Files
21. Klik ikon Filter
22. Verifikasi Filter Panel tampil

### Bulk Action tab Files
23. Tampilkan Halaman File Manager dengan kondisi K1
24. Centang baris `laptop-front.jpg`
25. Klik `[Bulk Action]`
26. Verifikasi pilihan `Download (ZIP)` tampil
27. Verifikasi pilihan `Delete` tampil

### Tab Asset Data: caption, Changelog, Recycle Bin, dan tanpa pemilih baris
28. Tampilkan Halaman File Manager dengan kondisi K1
29. Klik tab `Disposed & Unmanaged Assets`
30. Verifikasi caption `Asset data can only be deleted from the Asset menu.` tampil
31. Verifikasi tombol Changelog tetap tampil pada header kartu Storage Usage
32. Verifikasi tombol Recycle Bin tetap tampil pada header kartu Storage Usage
33. Verifikasi header kolom `Name` tampil pada tabel Asset Data
34. Verifikasi tidak ada kolom checkbox pemilih baris pada tabel Asset Data

### Lebar sempit tetap tabel
35. Tampilkan Halaman File Manager dengan kondisi K2
36. Verifikasi header kolom `File Name` tampil pada tabel Files
37. Verifikasi tidak ada `Card List` yang menggantikan tabel Files
38. Verifikasi tabel Files dapat digulir horizontal

### Kontrol hanya-ikon punya label aksesibel
39. Tampilkan Halaman File Manager dengan kondisi K1
40. Verifikasi tombol Changelog memiliki label aksesibel `Changelog`
41. Verifikasi tombol Recycle Bin memiliki label aksesibel `Recycle Bin`
42. Verifikasi ikon Search memiliki label aksesibel `Search`
43. Verifikasi ikon Filter memiliki label aksesibel `Filter`
44. Verifikasi ikon Download memiliki label aksesibel `Download`
45. Verifikasi trigger Column Visibility pada header kolom Actions memiliki label aksesibel `Column Visibility`
46. Klik tab `Disposed & Unmanaged Assets`
47. Verifikasi badge Status baris `Printer HP M404 - 1` bertuliskan `Disposed`
48. Verifikasi badge Status baris `Monitor LG 24 - 7` bertuliskan `Unmanaged`

### Alert Storage penuh memuat teks
49. Tampilkan Halaman File Manager dengan kondisi K3
50. Verifikasi teks penjelasan tampil di dalam Alert Storage penuh

### Tombol bantuan dan tombol aksi baris punya label aksesibel
51. Tampilkan Halaman File Manager dengan kondisi K1
52. Verifikasi tombol bantuan `[?]` memiliki label aksesibel
53. Verifikasi tombol `⋯` pada baris `laptop-front.jpg` memiliki label aksesibel `Action`
