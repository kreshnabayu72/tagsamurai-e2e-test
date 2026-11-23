---
id: TC-FA-FAFM-E2E-043-delete-asset-data-dep-asset-list
title: "Delete Asset Data dari menu Asset menghapus file aset dan memperbarui tab Asset Data"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [ARS-04f, F-FAFM-05a, F-FAFM-07.k2, F-FAFM-07e, F-FAFM-07f, F-FAFM-07g, F-FAFM-07h, FAFM-LOGIC-04a, FAFM-LOGIC-04c, FAFM-LOGIC-05j, FAFM-LOGIC-08e, SYN-05a, SYN-05b, SYN-05d, SYN-05e, SYN-05f, SYN-05g, "§8.1#b2", "§9.2#p19", "§9.4.3#b9"]
smoke: []
dependsOn: ["Asset List: Delete Asset Data"]
trace:
  ARS-04f: 41
  F-FAFM-05a: 22
  F-FAFM-07.k2: 22
  F-FAFM-07e: [4, 5, 22]
  F-FAFM-07f: 22
  F-FAFM-07g: 27
  F-FAFM-07h: [30, 33, 36]
  FAFM-LOGIC-04a: [30, 33, 36]
  FAFM-LOGIC-04c: 41
  FAFM-LOGIC-05j: 22
  FAFM-LOGIC-08e: [4, 5]
  SYN-05a: 22
  SYN-05b: 27
  SYN-05d: [27, 43]
  SYN-05e: [30, 33, 43]
  SYN-05f: [36, 43]
  SYN-05g: 22
  "§8.1#b2": 41
  "§9.2#p19": [27, 43]
  "§9.4.3#b9": 22
anchor: [3, 8, 11, 14, 19, 40]
coverage:
  web: automated
---

# Delete Asset Data dari menu Asset menghapus file aset dan memperbarui tab Asset Data

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-043-1: Aset `Printer HP M404 {runId}`, Status `Disposed`, Group `Branch Bandung`, ada di entitas aktor.
  - DU-043-2: File `dsp-receipt-{runId}.pdf`, Source `Disposal Document`, Size `3.2 MB`, aktif, milik aset DU-043-1.
  - DU-043-3: File `maint-after-{runId}.jpg`, Source `Maintenance After Photo`, Size `1.9 MB`, aktif, milik aset DU-043-1.
  - DU-043-4: File `maint-before-{runId}.jpg`, Source `Maintenance Before Photo`, Size `700.0 KB`, ada di Recycle Bin milik aset DU-043-1, dihapus lewat Delete di File Manager sehingga Changelog File Manager memuat entri Action `Delete` untuk file itu.

## Test Steps

### Aset Disposed terdaftar di tab Asset Data tanpa aksi hapus
1. Klik tab `Disposed & Unmanaged Assets`
2. Ketik Search `Printer HP M404 {runId}`, tekan Enter
3. Verifikasi baris aset `Printer HP M404 {runId}` tampil dengan Status `Disposed`
4. Verifikasi caption di atas toolbar tab Asset Data mengarahkan penghapusan ke menu Asset dengan teks `Asset data can only be deleted from the Asset menu.`
5. Verifikasi baris aset `Printer HP M404 {runId}` tidak menyediakan aksi Delete Asset Data (Hidden)

### File aset terdaftar di tab Files dan Recycle Bin
6. Klik tab `Disposal`
7. Ketik Search `Printer HP M404 {runId}`, tekan Enter
8. Verifikasi baris file `dsp-receipt-{runId}.pdf` milik aset `Printer HP M404 {runId}` tampil
9. Klik tab `Maintenance`
10. Ketik Search `Printer HP M404 {runId}`, tekan Enter
11. Verifikasi baris file dengan Source `Maintenance After Photo` milik aset `Printer HP M404 {runId}` tampil
12. Klik tombol Recycle Bin pada header kartu Storage Usage
13. Ketik Search `Printer HP M404 {runId}`, tekan Enter
14. Verifikasi baris file dengan Source `Maintenance Before Photo` milik aset `Printer HP M404 {runId}` tampil di Recycle Bin
15. Tutup modal Recycle Bin
16. Catat nilai `Fixed Asset` pada kartu Storage Usage

### Delete Asset Data dilakukan dari menu Asset
17. Buka menu Asset
18. Ketik Search `Printer HP M404 {runId}`, tekan Enter
19. Verifikasi aset `Printer HP M404 {runId}` tampil di daftar Asset
20. Lakukan aksi Delete Asset Data pada aset `Printer HP M404 {runId}`
21. Konfirmasi dialog Delete Asset Data
22. Verifikasi hasil Search `Printer HP M404 {runId}` di daftar Asset menampilkan `No results found`

### Tab Asset Data, tab Files, dan Recycle Bin sesudah cascade purge
23. Cascade purge atas file aset `Printer HP M404 {runId}` selesai
24. Buka Settings > File Manager
25. Klik tab `Disposed & Unmanaged Assets`
26. Ganti isi kotak Search dengan `Printer HP M404 {runId}`, tekan Enter
27. Verifikasi hasil Search `Printer HP M404 {runId}` di tab Asset Data menampilkan `No results found`
28. Klik tab `Disposal`
29. Ganti isi kotak Search dengan `Printer HP M404 {runId}`, tekan Enter
30. Verifikasi hasil Search `Printer HP M404 {runId}` di tab `Disposal` menampilkan `No results found`
31. Klik tab `Maintenance`
32. Ganti isi kotak Search dengan `Printer HP M404 {runId}`, tekan Enter
33. Verifikasi hasil Search `Printer HP M404 {runId}` di tab `Maintenance` menampilkan `No results found`
34. Klik tombol Recycle Bin pada header kartu Storage Usage
35. Ketik Search `Printer HP M404 {runId}`, tekan Enter
36. Verifikasi hasil Search `Printer HP M404 {runId}` di Recycle Bin menampilkan `No results found`
37. Tutup modal Recycle Bin

### Changelog File Manager tidak mencatat cascade purge
38. Klik tombol Changelog pada header kartu Storage Usage
39. Ketik Search `{runId}`, tekan Enter
40. Verifikasi entri dengan Action `Delete` untuk File Name `maint-before-{runId}.jpg` tampil
41. Verifikasi hasil Search `{runId}` tidak memuat entri dengan Action `Permanently Delete`
42. Tutup modal Changelog

### Kartu Storage Usage turun sesudah penghapusan
43. Verifikasi nilai `Fixed Asset` pada kartu Storage Usage lebih kecil dari nilai yang dicatat pada langkah 16
