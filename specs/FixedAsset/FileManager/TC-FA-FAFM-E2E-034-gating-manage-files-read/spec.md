---
id: TC-FA-FAFM-E2E-034-gating-manage-files-read
title: "Gating Manage files Read: baca dan Download pada group yang di-assign"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02a, ACT-02b, ACT-03c, ACT-04a, ACT-05a, ACT-05b, ACT-06a, FAFM-LOGIC-05d, S-15, "§2#r2", "§2#r8", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§9.3#r1", "§9.3#r2", "§9.3#r3", "§9.3#r4", "§9.11#r4"]
smoke: []
dependsOn: []
trace:
  ACT-02a: [22]
  ACT-02b: [22]
  ACT-03c: [25]
  ACT-04a: [29]
  ACT-05a: [39]
  ACT-05b: [39]
  ACT-06a: [40]
  FAFM-LOGIC-05d: [14, 16, 21, 24, 42, 48]
  S-15: [22, 29]
  "§2#r2": [14, 16, 33, 37, 48, 49]
  "§2#r8": [14, 18, 21, 24, 28, 33, 34, 37, 42, 45, 48]
  "§4.8#r1": [1]
  "§4.8#r2": [2]
  "§4.8#r3": [3, 4]
  "§4.8#r4": [5, 6, 7, 8, 10, 18]
  "§4.8#r5": [25, 28]
  "§4.8#r6": [29, 40]
  "§4.8#r7": [38]
  "§4.8#r8": [22]
  "§4.8#r9": [12]
  "§4.8#r10": [39, 40]
  "§9.3#r1": [14, 18, 21, 24]
  "§9.3#r2": [2, 33]
  "§9.3#r3": [22]
  "§9.3#r4": [39]
  "§9.11#r4": [14, 15, 16, 33, 42, 45, 48, 49]
anchor: []
coverage:
  web: automated
---

# Gating Manage files Read: baca dan Download pada group yang di-assign

## Prerequisites
- Aktor: Maya Pembaca File `{runId}` (pemegang capability Group Role Manage files dengan Read saja, di-assign pada group `Fleet`).
- Layar awal: Settings > File Manager, tab Kategori `Asset Photo` aktif.
- Data:
  - DU-034-1: User `Maya Pembaca File {runId}`, role `Pengelola File Fleet Baca {runId}`, capability `Manage files: Read`, group yang di-assign `Fleet`.
  - DU-034-2: File `foto-truk-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Truk Pengangkut {runId}` (Increment dibentuk server), Group `Fleet`, Size `880.0 KB`, Uploaded By `Dodi P`, Upload Date `T0 − 2 hari, pukul 15:00`, ada di tab `Asset Photo`.
  - DU-034-3: File `foto-kantor-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Meja Kantor {runId}` (Increment dibentuk server), Group `Head Office` (di luar group yang di-assign), Size `600.0 KB`, Uploaded By `Budi S`, Upload Date `T0 − 6 hari, pukul 10:30`, ada di tab `Asset Photo`.
  - DU-034-4: File `foto-bin-truk-{runId}.jpg`, File Format `JPG`, Category `Asset Photo`, Source `Asset Photo`, Asset `Truk Pengangkut {runId}` (Increment dibentuk server), Group `Fleet`, Size `450.0 KB`, Deleted By `Rina A`, Deleted Date `T0 − 1 hari, pukul 09:00`, ada di Recycle Bin.
  - DU-034-5: Aset `Mobil Operasional {runId}` (Increment dibentuk server), Status `Disposed`, Group `Fleet`, ada di tab `Disposed & Unmanaged Assets`.
  - DU-034-6: Group `Fleet Workshop {runId}`, group turunan langsung dari `Fleet`.
  - DU-034-7: File `foto-ban-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Ban Cadangan Truk {runId}` (Increment dibentuk server), Group `Fleet Workshop {runId}` (turunan dari group yang di-assign), Size `520.0 KB`, Uploaded By `Dodi P`, Upload Date `T0 − 4 hari, pukul 10:45`, ada di tab `Asset Photo`.
  - DU-034-8: File `foto-bin-bengkel-{runId}.jpg`, File Format `JPG`, Category `Asset Photo`, Source `Asset Photo`, Asset `Ban Cadangan Truk {runId}` (Increment dibentuk server), Group `Fleet Workshop {runId}` (turunan dari group yang di-assign), Size `380.0 KB`, Deleted By `Rina A`, Deleted Date `T0 − 2 hari, pukul 13:00`, ada di Recycle Bin.
  - DU-034-9: Aset `Forklift Bengkel {runId}` (Increment dibentuk server), Status `Disposed`, Group `Fleet Workshop {runId}` (turunan dari group yang di-assign), ada di tab `Disposed & Unmanaged Assets`.

## Test Steps

### Elemen baca tampil untuk pemegang Manage files Read
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
12. Verifikasi tombol `Recycle Bin` tampil pada header kartu Storage Usage

### Scope group yang di-assign
13. Ketik Search `{runId}`, tekan Enter
14. Verifikasi baris `foto-truk-{runId}.jpg` tampil pada tabel
15. Verifikasi baris `foto-truk-{runId}.jpg` menampilkan File Format `JPG`, Group `Fleet`, Size `880.0 KB`, dan Uploaded By `Dodi P`
16. Verifikasi baris `foto-kantor-{runId}.jpg` tidak ada pada tabel

### Preview dan Download tersedia, Delete tersembunyi pada baris
17. Klik nama file `foto-truk-{runId}.jpg`
18. Verifikasi file `foto-truk-{runId}.jpg` terbuka pada tab browser baru
19. Kembali ke tab File Manager
20. Klik `⋯` pada baris `foto-truk-{runId}.jpg`
21. Verifikasi menu baris memuat `Download`
22. Verifikasi menu baris tidak memuat `Delete` (Hidden, bukan Disabled)
23. Klik `Download`
24. Verifikasi berkas `foto-truk-{runId}.jpg` terunduh

### Aksi bulk tulis tersembunyi
25. Verifikasi kotak centang tampil pada baris `foto-truk-{runId}.jpg`
26. Centang baris `foto-truk-{runId}.jpg`
27. Klik `Bulk Action` pada bulk action bar
28. Verifikasi menu bulk memuat `Download (ZIP)`
29. Verifikasi menu bulk tidak memuat `Delete` (Hidden, bukan Disabled)
30. Tutup menu bulk

### Tab Asset Data hanya baca
31. Klik tab `Disposed & Unmanaged Assets`
32. Ketik Search `{runId}`, tekan Enter
33. Verifikasi baris aset `Mobil Operasional {runId}` tampil pada tabel
34. Verifikasi kolom kotak centang tidak ada pada tabel (Hidden)

### Recycle Bin hanya lihat
35. Klik `Recycle Bin` pada header kartu Storage Usage
36. Ketik Search `{runId}`, tekan Enter
37. Verifikasi baris `foto-bin-truk-{runId}.jpg` tampil pada Recycle Bin
38. Verifikasi kotak centang tidak ada pada baris `foto-bin-truk-{runId}.jpg` (Hidden)
39. Verifikasi aksi `Permanently Delete` tidak tersedia pada baris `foto-bin-truk-{runId}.jpg` (Hidden)
40. Verifikasi bar aksi bulk tidak tampil pada Recycle Bin (Hidden)

### Recycle Bin memuat file di group turunan dari group yang di-assign
41. Ketik Search `{runId}`, tekan Enter
42. Verifikasi baris `foto-bin-bengkel-{runId}.jpg` tampil pada Recycle Bin
43. Tutup dialog Recycle Bin

### Tab Asset Data dan tab Files memuat group turunan dari group yang di-assign
44. Ketik Search `{runId}`, tekan Enter
45. Verifikasi baris aset `Forklift Bengkel {runId}` tampil pada tabel
46. Klik tab Kategori `Asset Photo`
47. Ketik Search `{runId}`, tekan Enter
48. Verifikasi baris `foto-ban-{runId}.jpg` tampil pada tabel
49. Verifikasi baris `foto-ban-{runId}.jpg` menampilkan File Format `JPG`, Group `Fleet Workshop {runId}`, Size `520.0 KB`, dan Uploaded By `Dodi P`
