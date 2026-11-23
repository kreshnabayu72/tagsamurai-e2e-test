---
id: TC-FA-FAFM-E2E-045-change-photo-attachment-dep-asset-detail
title: "Asset Detail: Change photo, Attachment, dan tab Documents"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02e, ARS-01c, DIM-14a, DIM-14b, F-FAFM-04b, FAFM-LOGIC-01c, FAFM-LOGIC-02c, FAFM-LOGIC-02e, FAFM-LOGIC-02f, FAFM-LOGIC-07a, FAFM-LOGIC-07b, FAFM-LOGIC-07d, FAFM-LOGIC-07e, FAFM-LOGIC-07c, SRC-01, SRC-03, SYN-01b, SYN-01e, SYN-01h, "§9.2#p12", "§9.2#p13", "§9.4.3#b4", "§11#r4"]
smoke: []
dependsOn: ["Asset Detail: Change photo, tab Documents, dan Attachment"]
trace:
  ACT-02e: [48, 51]
  ARS-01c: 51
  DIM-14a: 51
  DIM-14b: 52
  F-FAFM-04b: [9, 14]
  FAFM-LOGIC-01c: [9, 28]
  FAFM-LOGIC-02c: [48, 51]
  FAFM-LOGIC-02e: 51
  FAFM-LOGIC-02f: 52
  FAFM-LOGIC-07a: [10, 13]
  FAFM-LOGIC-07b: [35, 39]
  FAFM-LOGIC-07d: 14
  FAFM-LOGIC-07e: 40
  FAFM-LOGIC-07c: [5, 33]
  SRC-01: 9
  SRC-03: [28, 29, 30]
  SYN-01b: 51
  SYN-01e: 51
  SYN-01h: 54
  "§9.2#p12": [9, 14]
  "§9.2#p13": 5
  "§9.4.3#b4": [5, 33]
  "§11#r4": 28
anchor: [4, 24]
coverage:
  web: automated
---

# Asset Detail: Change photo, Attachment, dan tab Documents

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Asset > Asset Detail aset `Laptop Dell Latitude 5420 {runId}`.
- Data:
  - DU-045-1: Aset `Laptop Dell Latitude 5420 {runId}`, Status `Active`, Group `Head Office`, ada di entitas aktor.
  - DU-045-2: File `laptop-old-{runId}.png`, foto aktif aset DU-045-1.
  - DU-045-3: File `laptop-front-{runId}.jpg`, foto pengganti yang dipilih di Change photo.
  - DU-045-4: File `warranty-card-{runId}.pdf`, dokumen yang diunggah ke section `General` tab Documents.
  - DU-045-5: File `invoice-{runId}.pdf`, dokumen yang diunggah ke section `Purchase` tab Documents.
  - DU-045-6: Aset `Scanner Epson DS-530 {runId}`, Status `Active`, Group `Branch Bandung`, ada di entitas aktor.
  - DU-045-7: File `scanner-photo-{runId}.jpg`, foto aktif aset DU-045-6.

## Test Steps

### Change photo mengganti foto tanpa pertanyaan ke pengguna
1. Klik menu `Change photo` pada header Asset Detail
2. Pilih file `laptop-front-{runId}.jpg` sebagai foto baru
3. Simpan foto baru
4. Verifikasi header Asset Detail menampilkan foto baru aset `Laptop Dell Latitude 5420 {runId}`
5. Verifikasi tidak ada dialog yang menanyakan apakah file lama juga dihapus dari File Manager

### File baru tampil di tab Files dan file lama masuk Recycle Bin dengan Deleted By System
6. Buka Settings > File Manager
7. Klik tab `Asset Photo`
8. Ketik Search `{runId}`, tekan Enter
9. Verifikasi baris file `laptop-front-{runId}.jpg` milik aset `Laptop Dell Latitude 5420 {runId}` tampil
10. Verifikasi tidak ada baris file `laptop-old-{runId}.png` di tab `Asset Photo`
11. Klik tombol Recycle Bin pada header kartu Storage Usage
12. Ketik Search `laptop-old-{runId}.png`, tekan Enter
13. Verifikasi baris file `laptop-old-{runId}.png` tampil di Recycle Bin
14. Verifikasi baris file `laptop-old-{runId}.png` menampilkan Deleted By `System`
15. Tutup modal Recycle Bin

### Upload Attachment dari tab Documents tampil di tab Asset Documents
16. Buka Asset Detail aset `Laptop Dell Latitude 5420 {runId}`
17. Klik tab `Documents`
18. Klik `Upload` pada section `General`
19. Pilih file `warranty-card-{runId}.pdf` pada dialog Upload document
20. Konfirmasi dialog Upload document
21. Klik `Upload` pada section `Purchase`
22. Pilih file `invoice-{runId}.pdf` pada dialog Upload document
23. Konfirmasi dialog Upload document
24. Verifikasi file `warranty-card-{runId}.pdf` tampil di section `General` tab Documents
25. Buka Settings > File Manager
26. Klik tab `Asset Documents`
27. Ketik Search `{runId}`, tekan Enter
28. Verifikasi baris file `warranty-card-{runId}.pdf` tampil dengan Source `Attachment`
29. Verifikasi baris file `warranty-card-{runId}.pdf` menampilkan Reference `General`
30. Verifikasi baris file `invoice-{runId}.pdf` menampilkan Reference `Purchase`

### Remove photo mengosongkan foto dan file masuk Recycle Bin dengan Deleted By aktor
31. Buka Asset Detail aset `Scanner Epson DS-530 {runId}`
32. Klik menu `Remove photo` pada header Asset Detail
33. Verifikasi dialog konfirmasi Remove photo tidak menanyakan apakah file juga dihapus dari File Manager dan tidak menawarkan pilihan mempertahankan file
34. Konfirmasi Remove photo
35. Verifikasi header Asset Detail aset `Scanner Epson DS-530 {runId}` menampilkan gambar placeholder generik
36. Buka Settings > File Manager
37. Klik tombol Recycle Bin pada header kartu Storage Usage
38. Ketik Search `scanner-photo-{runId}.jpg`, tekan Enter
39. Verifikasi baris file `scanner-photo-{runId}.jpg` tampil di Recycle Bin
40. Verifikasi baris file `scanner-photo-{runId}.jpg` menampilkan Deleted By nama aktor yang melakukan Remove photo
41. Tutup modal Recycle Bin

### Delete file Asset Photo dari File Manager mengosongkan foto aset tanpa mengubah statusnya
42. Klik tab `Asset Photo`
43. Ketik Search `laptop-front-{runId}.jpg`, tekan Enter
44. Klik aksi Delete pada baris file `laptop-front-{runId}.jpg`
45. Klik `[Delete]` pada dialog Delete File
46. Klik tombol Recycle Bin pada header kartu Storage Usage
47. Ketik Search `laptop-front-{runId}.jpg`, tekan Enter
48. Verifikasi baris file `laptop-front-{runId}.jpg` tampil di Recycle Bin
49. Tutup modal Recycle Bin
50. Buka Asset Detail aset `Laptop Dell Latitude 5420 {runId}`
51. Verifikasi header Asset Detail menampilkan gambar placeholder generik untuk foto aset
52. Verifikasi Status aset `Laptop Dell Latitude 5420 {runId}` tetap `Active`
53. Buka Changelog aset `Laptop Dell Latitude 5420 {runId}`
54. Verifikasi entri dengan Action `Edit`, Old Value `laptop-front-{runId}.jpg`, dan New Value `—` tampil
55. Tutup Changelog aset
