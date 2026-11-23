---
id: TC-FA-DAMAGED-E2E-062-hapus-foto-bukti-dep-file-manager
title: "Damaged Photo dan After photo tercatat di File Manager sebagai Source Damaged Photo dan Repair Photo; sesudah dihapus lewat File Manager foto tampil kosong di kolom Photo dan Damage Log, tanpa mengubah status record, status global aset, dan hasil Mark as Repaired"
layer: ui-e2e
priority: Critical
caseType: Edge
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r91", "§Aturan Logika Modul#r96", "EC-DMG-40", "§9.4.4#r17", "§9.2#b22", "§9.7#r18", "FLD-DMG-04", "§8.1#r12", "§8.1#r7", "§9.4.1#r14"]
smoke: []
dependsOn:
  - "File Manager: daftar file Source Damaged Photo dan Repair Photo, Delete file"
trace:
  "§Aturan Logika Modul#r91": [3, 5]
  "§Aturan Logika Modul#r96": [22, 23, 26, 27, 31, 40, 43, 44, 49, 58, 59, 61, 62]
  "EC-DMG-40": [15, 18, 19, 22, 23, 26, 31, 36, 40, 43, 44, 49, 54, 58, 59, 61, 62]
  "§9.4.4#r17": [23, 26, 44, 59, 61]
  "§9.2#b22": [23, 26, 44, 59, 61]
  "§9.7#r18": [23, 26, 31, 44, 49, 59, 61]
  "FLD-DMG-04": [5]
  "§8.1#r12": [44]
  "§8.1#r7": [26, 61]
  "§9.4.1#r14": [23, 26, 44, 59, 61]
anchor: [8, 9, 11, 25, 41, 45]
coverage:
  web: automated
---

# Damaged Photo dan After photo tercatat di File Manager sebagai Source Damaged Photo dan Repair Photo; sesudah dihapus lewat File Manager foto tampil kosong di kolom Photo dan Damage Log, tanpa mengubah status record, status global aset, dan hasil Mark as Repaired

## Prerequisites
- Aktor: Total Control, Aktor Damaged dan pemegang hak Delete di File Manager atas Group `Head Office`.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-062-1: aset Name `Genset Cadangan {runId} Satu`, Group `Head Office`, tanpa foto aset, status global `Damaged`, record `Damaged` Source `Manual` dengan What happened `Genset mati total saat uji beban` dan Damaged Photo `genset-rusak-{runId}.jpg`, kata kunci Search File Manager `genset-rusak-{runId}`.
  - DU-062-2: aset Name `Genset Cadangan {runId} Dua`, Group `Head Office`, tanpa foto aset, status global `Normal`, record `Repaired` Source `Manual` dengan What happened `Genset bocor oli`, Damaged Photo `genset-rusak-dua-{runId}.jpg`, Repair note `Seal oli sudah diganti`, dan After photo `genset-perbaikan-{runId}.jpg`, kata kunci Search File Manager untuk Damaged Photo `genset-rusak-dua-{runId}` dan untuk After photo `genset-perbaikan-{runId}`.
- Kondisi:
  - After photo required bernilai `OFF`.

## Test Steps

### Damaged Photo dan After photo terdaftar di File Manager dengan Source dari modul Damaged
1. Buka halaman Settings > File Manager pada sidebar FAMS, tab `Files`
2. Ketik Search `genset-rusak-{runId}`, tekan Enter
3. Verifikasi baris `genset-rusak-{runId}.jpg` tampil dengan Source `Damaged Photo` dan merujuk aset `Genset Cadangan {runId} Satu`
4. Ganti isi kotak search dengan `genset-perbaikan-{runId}`, tekan Enter
5. Verifikasi baris `genset-perbaikan-{runId}.jpg` tampil dengan Source `Repair Photo` dan merujuk aset `Genset Cadangan {runId} Dua`

### Sebelum dihapus foto tampil di tabel dan Damage Log
6. Buka halaman Assets, tab `Damaged`
7. Ketik Search `Genset Cadangan {runId} Satu`, tekan Enter
8. Verifikasi baris `Genset Cadangan {runId} Satu` tampil di sub-tab `Active` dengan Status `Damaged`
9. Verifikasi kolom Photo baris itu menampilkan thumbnail Damaged Photo, bukan avatar inisial
10. Klik nama aset `Genset Cadangan {runId} Satu` untuk membuka dialog Damage Log
11. Verifikasi `Damaged Photo` `genset-rusak-{runId}.jpg` tampil pada node `Reported damaged by`
12. Klik `✕` pada dialog Damage Log

### Delete File Manager atas Damaged Photo tidak diblokir
13. Buka halaman Settings > File Manager pada sidebar FAMS, tab `Files`
14. Ketik Search `genset-rusak-{runId}`, tekan Enter
15. Verifikasi aksi `Delete` pada baris `genset-rusak-{runId}.jpg` tampil dan aktif walau file dirujuk record Damage
16. Klik `Delete` pada baris `genset-rusak-{runId}.jpg`
17. Klik `[Delete]` pada dialog konfirmasi penghapusan file
18. Verifikasi toast sukses penghapusan file tampil
19. Verifikasi baris `genset-rusak-{runId}.jpg` tidak lagi tampil di tab `Files`

### Damaged Photo yang dihapus tampil kosong dan record tidak berubah
20. Buka halaman Assets, tab `Damaged`
21. Ketik Search `Genset Cadangan {runId} Satu`, tekan Enter
22. Verifikasi baris `Genset Cadangan {runId} Satu` tetap tampil di sub-tab `Active` dengan Status `Damaged`
23. Verifikasi kolom Photo baris itu menampilkan avatar inisial karena aset belum punya foto aset
24. Klik nama aset `Genset Cadangan {runId} Satu` untuk membuka dialog Damage Log
25. Verifikasi node `Reported damaged by` tampil dengan What happened `Genset mati total saat uji beban`
26. Verifikasi baris `Damaged Photo` tidak tampil pada node `Reported damaged by`
27. Verifikasi tidak ada caption `Damaged photo must not be empty` yang tampil saat record dibaca
28. Klik `✕` pada dialog Damage Log
29. Buka tab `Assets` pada halaman Assets
30. Ketik Search `Genset Cadangan {runId} Satu`, tekan Enter
31. Verifikasi status global aset `Genset Cadangan {runId} Satu` tetap `Damaged`

### After photo yang dihapus tampil kosong dan hasil Mark as Repaired tidak berubah
32. Buka halaman Settings > File Manager pada sidebar FAMS, tab `Files`
33. Ketik Search `genset-perbaikan-{runId}`, tekan Enter
34. Klik `Delete` pada baris `genset-perbaikan-{runId}.jpg`
35. Klik `[Delete]` pada dialog konfirmasi penghapusan file
36. Verifikasi toast sukses penghapusan file tampil
37. Buka halaman Assets, tab `Damaged`
38. Klik sub-tab `History`
39. Ketik Search `Genset Cadangan {runId} Dua`, tekan Enter
40. Verifikasi baris `Genset Cadangan {runId} Dua` tetap tampil di sub-tab `History` dengan Status `Repaired`
41. Verifikasi kolom Photo baris itu tetap menampilkan thumbnail Damaged Photo, bukan avatar inisial
42. Klik nama aset `Genset Cadangan {runId} Dua` untuk membuka dialog Damage Log
43. Verifikasi node `Marked as repaired by` tampil dengan Repair note `Seal oli sudah diganti`
44. Verifikasi baris `After photo` tidak tampil pada node `Marked as repaired by`
45. Verifikasi baris `Damaged Photo` `genset-rusak-dua-{runId}.jpg` tetap tampil pada node `Reported damaged by` karena file itu tidak dihapus
46. Klik `✕` pada dialog Damage Log
47. Buka tab `Assets` pada halaman Assets
48. Ketik Search `Genset Cadangan {runId} Dua`, tekan Enter
49. Verifikasi status global aset `Genset Cadangan {runId} Dua` tetap `Normal`

### Damaged Photo record Repaired yang dihapus tampil kosong di sub-tab History
50. Buka halaman Settings > File Manager pada sidebar FAMS, tab `Files`
51. Ketik Search `genset-rusak-dua-{runId}`, tekan Enter
52. Klik `Delete` pada baris `genset-rusak-dua-{runId}.jpg`
53. Klik `[Delete]` pada dialog konfirmasi penghapusan file
54. Verifikasi toast sukses penghapusan file tampil
55. Buka halaman Assets, tab `Damaged`
56. Klik sub-tab `History`
57. Ketik Search `Genset Cadangan {runId} Dua`, tekan Enter
58. Verifikasi baris `Genset Cadangan {runId} Dua` tetap tampil di sub-tab `History` dengan Status `Repaired`
59. Verifikasi kolom Photo baris itu menampilkan avatar inisial karena aset belum punya foto aset
60. Klik nama aset `Genset Cadangan {runId} Dua` untuk membuka dialog Damage Log
61. Verifikasi baris `Damaged Photo` tidak tampil pada node `Reported damaged by`
62. Verifikasi node `Marked as repaired by` tetap tampil dengan Repair note `Seal oli sudah diganti`
63. Klik `✕` pada dialog Damage Log
