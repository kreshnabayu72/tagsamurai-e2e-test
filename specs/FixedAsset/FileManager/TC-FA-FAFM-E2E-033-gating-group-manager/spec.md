---
id: TC-FA-FAFM-E2E-033-gating-group-manager
title: "Gating Group Manager: akses penuh pada group yang dikelola dan descendant"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02a, ACT-02b, ACT-03c, ACT-04a, ACT-05a, ACT-05b, ACT-06a, FAFM-LOGIC-05b, "§2#r7", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§9.3#r1", "§9.3#r2", "§9.3#r3", "§9.3#r4", "§9.11#r3", "§9.11#r6"]
smoke: []
dependsOn: []
trace:
  ACT-02a: [23]
  ACT-02b: [23]
  ACT-03c: [30]
  ACT-04a: [35]
  ACT-05a: [47]
  ACT-05b: [47]
  ACT-06a: [51]
  FAFM-LOGIC-05b: [13, 14, 38, 54]
  "§2#r7": [13, 14, 27, 28, 38, 43, 44, 54]
  "§4.8#r1": [1]
  "§4.8#r2": [2]
  "§4.8#r3": [3, 4]
  "§4.8#r4": [5, 6, 7, 8, 10, 19]
  "§4.8#r5": [30, 34]
  "§4.8#r6": [35, 51]
  "§4.8#r7": [45]
  "§4.8#r8": [23]
  "§4.8#r9": [40]
  "§4.8#r10": [47, 51]
  "§9.3#r1": [13, 14, 19, 22]
  "§9.3#r2": [2, 27]
  "§9.3#r3": [38, 39, 43, 44]
  "§9.3#r4": [54, 56]
  "§9.11#r3": [13, 14, 15, 16, 17, 27]
  "§9.11#r6": [13, 14, 16]
anchor: [55]
coverage:
  web: automated
---

# Gating Group Manager: akses penuh pada group yang dikelola dan descendant

## Prerequisites
- Aktor: Gita Manajer Group `{runId}` (Group Manager untuk group `Head Office` beserta descendant `Fleet`).
- Layar awal: Settings > File Manager, tab Kategori `Asset Photo` aktif.
- Data:
  - DU-033-1: User `Gita Manajer Group {runId}`, role `Group Manager`, group yang dikelola `Head Office` beserta descendant `Fleet`.
  - DU-033-2: File `foto-genset-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Genset Cadangan {runId}` (Increment dibentuk server), Group `Head Office`, Size `700.0 KB`, Uploaded By `Budi S`, Upload Date `T0 − 4 hari, pukul 10:00`, ada di tab `Asset Photo`.
  - DU-033-3: File `foto-forklift-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Forklift Gudang {runId}` (Increment dibentuk server), Group `Fleet` (descendant `Head Office`), Size `900.0 KB`, Uploaded By `Dodi P`, Upload Date `T0 − 6 hari, pukul 13:15`, ada di tab `Asset Photo`.
  - DU-033-4: File `foto-ruang-rapat-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Proyektor Ruang Rapat {runId}` (Increment dibentuk server), Group `Branch Bandung` (di luar group yang dikelola), Size `500.0 KB`, Uploaded By `Rina A`, Upload Date `T0 − 7 hari, pukul 09:30`, ada di tab `Asset Photo`.
  - DU-033-5: File `foto-gudang-entitas-lain-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Rak Gudang {runId}` (Increment dibentuk server), Group `Head Office`, Size `400.0 KB`, Uploaded By `Rina A`, Upload Date `T0 − 9 hari, pukul 11:00`, milik entitas lain, bukan entitas aktor.
  - DU-033-6: Aset `Truk Box {runId}` (Increment dibentuk server), Status `Disposed`, Group `Fleet`, ada di tab `Disposed & Unmanaged Assets`.

## Test Steps

### Seluruh elemen tab Files tampil untuk Group Manager
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

### Scope Group Manager: group yang dikelola dan descendant
12. Ketik Search `{runId}`, tekan Enter
13. Verifikasi baris `foto-genset-{runId}.jpg` tampil pada tabel
14. Verifikasi baris `foto-forklift-{runId}.jpg` tampil pada tabel
15. Verifikasi baris `foto-forklift-{runId}.jpg` menampilkan File Format `JPG`, Group `Fleet`, Size `900.0 KB`, dan Uploaded By `Dodi P`
16. Verifikasi baris `foto-ruang-rapat-{runId}.jpg` tidak ada pada tabel
17. Verifikasi baris `foto-gudang-entitas-lain-{runId}.jpg` tidak ada pada tabel

### Preview dan Download pada group yang dikelola
18. Klik nama file `foto-genset-{runId}.jpg`
19. Verifikasi file `foto-genset-{runId}.jpg` terbuka pada tab browser baru
20. Kembali ke tab File Manager
21. Klik `⋯` pada baris `foto-forklift-{runId}.jpg`
22. Verifikasi menu baris memuat `Download`
23. Verifikasi menu baris memuat `Delete`
24. Tutup menu baris

### Tab Asset Data hanya baca untuk Group Manager
25. Klik tab `Disposed & Unmanaged Assets`
26. Ketik Search `{runId}`, tekan Enter
27. Verifikasi baris aset `Truk Box {runId}` tampil pada tabel
28. Verifikasi kolom kotak centang tidak ada pada tabel (Hidden)

### Bulk Delete lintas group yang dikelola tersimpan
29. Klik tab Kategori `Asset Photo`
30. Verifikasi kotak centang tampil pada baris `foto-genset-{runId}.jpg`
31. Centang baris `foto-genset-{runId}.jpg`
32. Centang baris `foto-forklift-{runId}.jpg`
33. Klik `Bulk Action` pada bulk action bar
34. Verifikasi menu bulk memuat `Download (ZIP)`
35. Verifikasi menu bulk memuat `Delete`
36. Klik `Delete`
37. Klik `[Delete]` pada dialog `Delete Files`
38. Verifikasi toast `Success, file has been deleted.` tampil
39. Verifikasi tabel menampilkan `No results found`

### File terhapus ada di Recycle Bin dan Permanently Delete tersedia
40. Verifikasi tombol `Recycle Bin` tampil pada header kartu Storage Usage
41. Klik `Recycle Bin` pada header kartu Storage Usage
42. Ketik Search `{runId}`, tekan Enter
43. Verifikasi baris `foto-genset-{runId}.jpg` tampil pada Recycle Bin
44. Verifikasi baris `foto-forklift-{runId}.jpg` tampil pada Recycle Bin
45. Verifikasi kotak centang tampil pada baris `foto-forklift-{runId}.jpg`
46. Klik `⋯` pada baris `foto-forklift-{runId}.jpg`
47. Verifikasi menu baris memuat `Permanently Delete`
48. Tutup menu baris
49. Centang baris `foto-forklift-{runId}.jpg`
50. Klik `Bulk Action` pada bulk action bar
51. Verifikasi menu bulk memuat `Permanently Delete`
52. Klik `Permanently Delete`
53. Klik `[Permanently Delete]` pada dialog `Permanently Delete File`
54. Verifikasi toast `Success, [File Name] has been permanently deleted.` tampil dengan File Name `foto-forklift-{runId}.jpg`
55. Verifikasi baris `foto-genset-{runId}.jpg` tetap tampil pada Recycle Bin
56. Verifikasi baris `foto-forklift-{runId}.jpg` tidak ada pada Recycle Bin
