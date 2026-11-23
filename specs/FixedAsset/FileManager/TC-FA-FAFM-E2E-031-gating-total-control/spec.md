---
id: TC-FA-FAFM-E2E-031-gating-total-control
title: "Gating Total Control: seluruh elemen tampil dan Delete tersimpan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02a, ACT-02b, ACT-03c, ACT-04a, ACT-05a, ACT-05b, ACT-06a, FAFM-LOGIC-05a, "§2#r5", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§9.3#r1", "§9.3#r2", "§9.3#r3", "§9.3#r4", "§9.11#r1"]
smoke: []
dependsOn: []
trace:
  ACT-02a: [21]
  ACT-02b: [21]
  ACT-03c: [28]
  ACT-04a: [33]
  ACT-05a: [46]
  ACT-05b: [46]
  ACT-06a: [44, 50]
  FAFM-LOGIC-05a: [13, 14, 36]
  "§2#r5": [14, 25, 26, 36, 42, 53]
  "§4.8#r1": [1]
  "§4.8#r2": [2]
  "§4.8#r3": [3, 4]
  "§4.8#r4": [5, 6, 7, 8, 10, 17]
  "§4.8#r5": [28, 32]
  "§4.8#r6": [33, 44, 50]
  "§4.8#r7": [43]
  "§4.8#r8": [21]
  "§4.8#r9": [38]
  "§4.8#r10": [46, 50]
  "§9.3#r1": [13, 17, 20]
  "§9.3#r2": [2, 25]
  "§9.3#r3": [36, 37, 41]
  "§9.3#r4": [53, 55]
  "§9.11#r1": [13, 14, 15, 25]
anchor: [54]
coverage:
  web: automated
---

# Gating Total Control: seluruh elemen tampil dan Delete tersimpan

## Prerequisites
- Aktor: Tari Pengelola Pusat `{runId}` (Total Control, seluruh group).
- Layar awal: Settings > File Manager, tab Kategori `Asset Photo` aktif.
- Data:
  - DU-031-1: User `Tari Pengelola Pusat {runId}`, role `Total Control`, cakupan seluruh group.
  - DU-031-2: File `foto-printer-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Printer HP M404 {runId}` (Increment dibentuk server), Group `Head Office`, Size `820.4 KB`, Uploaded By `Budi S`, Upload Date `T0 − 3 hari, pukul 14:30`, ada di tab `Asset Photo`.
  - DU-031-3: File `foto-scanner-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Scanner Epson DS-530 {runId}` (Increment dibentuk server), Group `Branch Bandung`, Size `300.0 KB`, Uploaded By `Rina A`, Upload Date `T0 − 5 hari, pukul 08:45`, ada di tab `Asset Photo`.
  - DU-031-4: Aset `Monitor LG 24 {runId}` (Increment dibentuk server), Status `Disposed`, Group `Branch Bandung`, ada di tab `Disposed & Unmanaged Assets`.

## Test Steps

### Seluruh elemen tab Files tampil untuk Total Control
1. Verifikasi item `File Manager` tampil pada sidebar grup `Settings`
2. Verifikasi kartu `Storage Usage` tampil
3. Verifikasi tab Kategori `Asset Photo` tampil
4. Verifikasi tab `Disposed & Unmanaged Assets` tampil
5. Verifikasi kotak Search tampil
6. Verifikasi tombol `Filter` tampil
7. Verifikasi tombol `Download` tampil
8. Verifikasi tombol `Changelog` tampil pada header kartu Storage Usage
9. Klik `⋯` pada header tabel
10. Verifikasi item `Setup Column...` tampil
11. Tutup panel Column Visibility
12. Ketik Search `{runId}`, tekan Enter
13. Verifikasi baris `foto-printer-{runId}.jpg` tampil pada tabel
14. Verifikasi baris `foto-scanner-{runId}.jpg` tampil pada tabel
15. Verifikasi baris `foto-scanner-{runId}.jpg` menampilkan File Format `JPG`, Group `Branch Bandung`, Size `300.0 KB`, dan Uploaded By `Rina A`
16. Klik nama file `foto-printer-{runId}.jpg`
17. Verifikasi file `foto-printer-{runId}.jpg` terbuka pada tab browser baru
18. Kembali ke tab File Manager
19. Klik `⋯` pada baris `foto-scanner-{runId}.jpg`
20. Verifikasi menu baris memuat `Download`
21. Verifikasi menu baris memuat `Delete`
22. Tutup menu baris

### Tab Asset Data hanya baca untuk Total Control
23. Klik tab `Disposed & Unmanaged Assets`
24. Ketik Search `{runId}`, tekan Enter
25. Verifikasi baris aset `Monitor LG 24 {runId}` tampil pada tabel
26. Verifikasi kolom kotak centang tidak ada pada tabel (Hidden)

### Bulk Delete lintas group tersimpan
27. Klik tab Kategori `Asset Photo`
28. Verifikasi kotak centang tampil pada baris `foto-printer-{runId}.jpg`
29. Centang baris `foto-printer-{runId}.jpg`
30. Centang baris `foto-scanner-{runId}.jpg`
31. Klik `Bulk Action` pada bulk action bar
32. Verifikasi menu bulk memuat `Download (ZIP)`
33. Verifikasi menu bulk memuat `Delete`
34. Klik `Delete`
35. Klik `[Delete]` pada dialog `Delete Files`
36. Verifikasi toast `Success, file has been deleted.` tampil
37. Verifikasi tabel menampilkan `No results found`

### File terhapus ada di Recycle Bin dan Permanently Delete tersedia
38. Verifikasi tombol `Recycle Bin` tampil pada header kartu Storage Usage
39. Klik `Recycle Bin` pada header kartu Storage Usage
40. Ketik Search `{runId}`, tekan Enter
41. Verifikasi baris `foto-printer-{runId}.jpg` tampil pada Recycle Bin
42. Verifikasi baris `foto-scanner-{runId}.jpg` tampil pada Recycle Bin
43. Verifikasi kotak centang tampil pada baris `foto-scanner-{runId}.jpg`
44. Verifikasi bar aksi bulk tidak tampil pada Recycle Bin selama belum ada baris yang dicentang
45. Klik `⋯` pada baris `foto-scanner-{runId}.jpg`
46. Verifikasi menu baris memuat `Permanently Delete`
47. Tutup menu baris
48. Centang baris `foto-scanner-{runId}.jpg`
49. Klik `Bulk Action` pada bulk action bar
50. Verifikasi menu bulk memuat `Permanently Delete`
51. Klik `Permanently Delete`
52. Klik `[Permanently Delete]` pada dialog `Permanently Delete File`
53. Verifikasi toast `Success, [File Name] has been permanently deleted.` tampil dengan File Name `foto-scanner-{runId}.jpg`
54. Verifikasi baris `foto-printer-{runId}.jpg` tetap tampil pada Recycle Bin
55. Verifikasi baris `foto-scanner-{runId}.jpg` tidak ada pada Recycle Bin
