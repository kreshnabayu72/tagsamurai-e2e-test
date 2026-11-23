---
id: TC-FA-FAFM-E2E-032-gating-read-only
title: "Gating Read Only: baca, Preview, dan Download tanpa kontrol tulis"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02a, ACT-02b, ACT-03c, ACT-04a, ACT-05a, ACT-05b, ACT-06a, FAFM-LOGIC-05c, S-15, "§2#r6", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§9.3#r1", "§9.3#r2", "§9.3#r3", "§9.3#r4", "§9.11#r2", EB-AKS-4]
smoke: []
dependsOn: []
trace:
  ACT-02a: [39]
  ACT-02b: [39]
  ACT-03c: [42]
  ACT-04a: [46]
  ACT-05a: [56]
  ACT-05b: [56]
  ACT-06a: [57]
  FAFM-LOGIC-05c: [11, 12, 38, 39, 41, 45, 46, 56]
  S-15: [39, 46]
  "§2#r6": [11, 12, 35, 41, 50, 51, 54, 56]
  "§4.8#r1": [1]
  "§4.8#r2": [2]
  "§4.8#r3": [3, 4]
  "§4.8#r4": [5, 7, 8, 9, 29, 35]
  "§4.8#r5": [42, 45]
  "§4.8#r6": [46, 57]
  "§4.8#r7": [55]
  "§4.8#r8": [39]
  "§4.8#r9": [6]
  "§4.8#r10": [56, 57]
  "§9.3#r1": [11, 12, 35, 38, 41]
  "§9.3#r2": [2, 50]
  "§9.3#r3": [39]
  "§9.3#r4": [56]
  "§9.11#r2": [11, 12, 13, 50]
  EB-AKS-4: [8, 9, 11, 12, 14, 16, 19, 23, 24, 27, 29, 32]
anchor: [17, 31]
coverage:
  web: automated
---

# Gating Read Only: baca, Preview, dan Download tanpa kontrol tulis

## Prerequisites
- Aktor: Rio Pembaca File `{runId}` (Read Only, seluruh group).
- Layar awal: Settings > File Manager, tab Kategori `Asset Photo` aktif.
- Data:
  - DU-032-1: User `Rio Pembaca File {runId}`, role `Read Only`, cakupan seluruh group.
  - DU-032-2: File `foto-rak-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Rak Arsip {runId}` (Increment dibentuk server), Group `Head Office`, Size `640.0 KB`, Uploaded By `Budi S`, Upload Date `T0 − 3 hari, pukul 14:30`, ada di tab `Asset Photo`.
  - DU-032-3: File `foto-lemari-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Lemari Besi {runId}` (Increment dibentuk server), Group `Branch Bandung`, Size `300.0 KB`, Uploaded By `Rina A`, Upload Date `T0 − 8 hari, pukul 09:00`, ada di tab `Asset Photo`.
  - DU-032-4: File `foto-bin-{runId}.jpg`, File Format `JPG`, Category `Asset Photo`, Source `Asset Photo`, Asset `Rak Arsip {runId}` (Increment dibentuk server), Group `Head Office`, Size `450.0 KB`, Deleted By `Rina A`, Deleted Date `T0 − 2 hari, pukul 10:00`, ada di Recycle Bin.
  - DU-032-5: Aset `Monitor LG 24 {runId}` (Increment dibentuk server), Status `Disposed`, Group `Head Office`, ada di tab `Disposed & Unmanaged Assets`.

## Test Steps

### Elemen baca tampil untuk Read Only
1. Verifikasi item `File Manager` tampil pada sidebar grup `Settings`
2. Verifikasi kartu `Storage Usage` tampil
3. Verifikasi tab Kategori `Asset Photo` tampil
4. Verifikasi tab `Disposed & Unmanaged Assets` tampil
5. Verifikasi tombol `Changelog` tampil pada header kartu Storage Usage
6. Verifikasi tombol `Recycle Bin` tampil pada header kartu Storage Usage
7. Verifikasi tombol `Download` tampil
8. Verifikasi tombol `Filter` tampil
9. Verifikasi kotak Search tampil

### Search dan Pagination aktif, Read Only membaca file lintas group
10. Ketik Search `{runId}`, tekan Enter
11. Verifikasi baris `foto-rak-{runId}.jpg` tampil pada tabel
12. Verifikasi baris `foto-lemari-{runId}.jpg` tampil pada tabel
13. Verifikasi baris `foto-lemari-{runId}.jpg` menampilkan File Format `JPG`, Group `Branch Bandung`, Size `300.0 KB`, dan Uploaded By `Rina A`
14. Verifikasi laporan paginasi `Showing 1 to 2 of 2` tampil
15. Pilih rows per page `25`
16. Verifikasi rows per page menampilkan `25`

### Sort aktif untuk Read Only
17. Verifikasi urutan baris: `foto-rak-{runId}.jpg` lalu `foto-lemari-{runId}.jpg`
18. Klik header kolom `File Name`
19. Verifikasi urutan baris: `foto-lemari-{runId}.jpg` lalu `foto-rak-{runId}.jpg`

### Filter aktif untuk Read Only
20. Klik tombol `Filter`
21. Pilih `Branch Bandung` pada filter `Group`
22. Klik `[Apply]`
23. Verifikasi baris `foto-lemari-{runId}.jpg` tampil pada tabel
24. Verifikasi baris `foto-rak-{runId}.jpg` tidak ada pada tabel
25. Klik `[Clear Field]`
26. Klik `[Apply]`
27. Verifikasi baris `foto-rak-{runId}.jpg` tampil kembali pada tabel

### Setup Column aktif untuk Read Only
28. Klik `⋯` pada header tabel
29. Verifikasi item `Setup Column...` tampil
30. Klik `Size` pada panel Column Visibility
31. Verifikasi header kolom `File Name` tampil
32. Verifikasi header kolom `Size` tidak tampil
33. Tutup panel Column Visibility

### Preview dan Download tersedia, Delete tersembunyi pada baris
34. Klik nama file `foto-rak-{runId}.jpg`
35. Verifikasi file `foto-rak-{runId}.jpg` terbuka pada tab browser baru
36. Kembali ke tab File Manager
37. Klik `⋯` pada baris `foto-rak-{runId}.jpg`
38. Verifikasi menu baris memuat `Download`
39. Verifikasi menu baris tidak memuat `Delete` (Hidden, bukan Disabled)
40. Klik `Download`
41. Verifikasi berkas `foto-rak-{runId}.jpg` terunduh

### Aksi bulk tulis tersembunyi
42. Verifikasi kotak centang tampil pada baris `foto-rak-{runId}.jpg`
43. Centang baris `foto-rak-{runId}.jpg`
44. Klik `Bulk Action` pada bulk action bar
45. Verifikasi menu bulk memuat `Download (ZIP)`
46. Verifikasi menu bulk tidak memuat `Delete` (Hidden, bukan Disabled)
47. Tutup menu bulk

### Tab Asset Data hanya baca
48. Klik tab `Disposed & Unmanaged Assets`
49. Ketik Search `{runId}`, tekan Enter
50. Verifikasi baris aset `Monitor LG 24 {runId}` tampil pada tabel
51. Verifikasi kolom kotak centang tidak ada pada tabel (Hidden)

### Recycle Bin hanya lihat
52. Klik `Recycle Bin` pada header kartu Storage Usage
53. Ketik Search `{runId}`, tekan Enter
54. Verifikasi baris `foto-bin-{runId}.jpg` tampil pada Recycle Bin
55. Verifikasi kotak centang tidak ada pada baris `foto-bin-{runId}.jpg` (Hidden)
56. Verifikasi aksi `Permanently Delete` tidak tersedia pada baris `foto-bin-{runId}.jpg` (Hidden)
57. Verifikasi bar aksi bulk tidak tampil pada Recycle Bin (Hidden)
