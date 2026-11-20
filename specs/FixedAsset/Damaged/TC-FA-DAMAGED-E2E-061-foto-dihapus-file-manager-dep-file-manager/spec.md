---
id: TC-FA-DAMAGED-E2E-061-foto-dihapus-file-manager-dep-file-manager
title: "Damaged Photo dan After photo tercatat di File Manager dengan Source dari modul Damaged, dan saat dihapus lewat Delete File Manager foto tampil kosong tanpa mengubah status record maupun status global aset"
layer: ui-e2e
priority: Critical
caseType: Edge
status: ready-for-automation
sourceRules: [DAMAGED-LOGIC-10a, DAMAGED-LOGIC-10f, EC-DMG-40, F-DMG-03.k2]
smoke: []
dependsOn:
  - "File Manager: Delete File dan daftar Source di tab Files"
trace:
  DAMAGED-LOGIC-10a: [3, 5]
  DAMAGED-LOGIC-10f: [21, 22, 25, 26, 29, 36, 39, 43]
  EC-DMG-40: [14, 18, 19, 21, 22, 25, 29, 34, 36, 39, 43]
  F-DMG-03.k2: [22, 25, 39]
anchor: [8, 10, 40]
coverage:
  web: automated
---

# Damaged Photo dan After photo tercatat di File Manager dengan Source dari modul Damaged, dan saat dihapus lewat Delete File Manager foto tampil kosong tanpa mengubah status record maupun status global aset

## Prerequisites
- Aktor: Total Control `Agus Pratama {runId}`, Aktor Damaged dan pemegang hak Delete di File Manager atas Group `Head Office`.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-061-1: aset `Genset Cadangan {runId} Satu`, Group `Head Office`, tanpa foto aset, status global `Damaged`, record `Damaged` dengan What happened `Genset mati total saat uji beban` dan Damaged Photo `genset-rusak-{runId}.jpg`.
  - DU-061-2: aset `Genset Cadangan {runId} Dua`, Group `Head Office`, tanpa foto aset, status global `Normal`, record `Repaired` dengan What happened `Genset bocor oli` dan Damaged Photo `genset-rusak-dua-{runId}.jpg`, Repair note `Seal oli sudah diganti` dan After photo `genset-perbaikan-{runId}.jpg`.

## Test Steps

### DAMAGED-LOGIC-10a: Damaged Photo dan After photo terdaftar di File Manager dengan Source dari modul ini
1. Buka halaman Settings > File Manager pada sidebar FAMS, tab `Files`
2. Ketik Search `genset-rusak-{runId}`, tekan Enter
3. Verifikasi baris `genset-rusak-{runId}.jpg` tampil dengan Source `Damaged Photo` dan Asset `Genset Cadangan {runId} Satu`
4. Ganti isi kotak search dengan `genset-perbaikan-{runId}`, tekan Enter
5. Verifikasi baris `genset-perbaikan-{runId}.jpg` tampil dengan Source `Repair Photo` dan Asset `Genset Cadangan {runId} Dua`

### Sebelum dihapus foto tampil di tabel dan Damage Log
6. Buka halaman Assets, tab `Damaged`, ketik Search `Genset Cadangan {runId} Satu`, tekan Enter
7. Verifikasi baris `Genset Cadangan {runId} Satu` tampil dengan Status `Damaged`
8. Verifikasi kolom Photo baris itu menampilkan thumbnail Damaged Photo, bukan avatar inisial
9. Klik nama aset `Genset Cadangan {runId} Satu` untuk membuka dialog Damage Log
10. Verifikasi `Damaged Photo` `genset-rusak-{runId}.jpg` tampil pada node `Reported damaged by`
11. Klik `✕` pada dialog Damage Log

### Delete File Manager atas Damaged Photo tidak diblokir
12. Buka halaman Settings > File Manager pada sidebar FAMS, tab `Files`
13. Ketik Search `genset-rusak-{runId}`, tekan Enter
14. Verifikasi aksi `Delete` pada baris `genset-rusak-{runId}.jpg` tampil dan aktif walau file dirujuk record Damage
15. Klik `Delete` pada baris `genset-rusak-{runId}.jpg`
16. Verifikasi dialog `Delete File` tampil dengan pesan `The file will be removed from the record that uses it and moved to the recycle bin.`
17. Klik `[Delete]`
18. Verifikasi toast `Success, genset-rusak-{runId}.jpg has been deleted.` tampil
19. Verifikasi baris `genset-rusak-{runId}.jpg` tidak lagi tampil di tab `Files`

### Damaged Photo yang dihapus tampil kosong dan record tidak berubah
20. Buka halaman Assets, tab `Damaged`, ketik Search `Genset Cadangan {runId} Satu`, tekan Enter
21. Verifikasi baris `Genset Cadangan {runId} Satu` tetap tampil dengan Status `Damaged`
22. Verifikasi kolom Photo baris itu menampilkan avatar inisial karena aset belum punya foto aset
23. Klik nama aset `Genset Cadangan {runId} Satu` untuk membuka dialog Damage Log
24. Verifikasi node `Reported damaged by` tampil dengan What happened `Genset mati total saat uji beban`
25. Verifikasi baris `Damaged Photo` tidak tampil pada node `Reported damaged by`
26. Verifikasi tidak ada caption `Damaged photo must not be empty` yang tampil saat record dibaca
27. Klik `✕` pada dialog Damage Log
28. Buka tab `Assets` pada halaman Assets, ketik Search `Genset Cadangan {runId} Satu`, tekan Enter
29. Verifikasi status global aset `Genset Cadangan {runId} Satu` tetap `Damaged`

### After photo yang dihapus tampil kosong dan hasil Mark as Repaired tidak berubah
30. Buka halaman Settings > File Manager pada sidebar FAMS, tab `Files`
31. Ketik Search `genset-perbaikan-{runId}`, tekan Enter
32. Klik `Delete` pada baris `genset-perbaikan-{runId}.jpg`
33. Klik `[Delete]` pada dialog `Delete File`
34. Verifikasi toast `Success, genset-perbaikan-{runId}.jpg has been deleted.` tampil
35. Buka halaman Assets, tab `Damaged`, sub-tab `History`, ketik Search `Genset Cadangan {runId} Dua`, tekan Enter
36. Verifikasi baris `Genset Cadangan {runId} Dua` tetap tampil dengan Status `Repaired`
37. Klik nama aset `Genset Cadangan {runId} Dua` untuk membuka dialog Damage Log
38. Verifikasi node `Marked as repaired by` tampil dengan Repair note `Seal oli sudah diganti`
39. Verifikasi baris `After photo` tidak tampil pada node `Marked as repaired by`
40. Verifikasi baris `Damaged Photo` `genset-rusak-dua-{runId}.jpg` tetap tampil pada node `Reported damaged by` karena file itu tidak dihapus
41. Klik `✕` pada dialog Damage Log
42. Buka tab `Assets` pada halaman Assets, ketik Search `Genset Cadangan {runId} Dua`, tekan Enter
43. Verifikasi status global aset `Genset Cadangan {runId} Dua` tetap `Normal`

## Notes
- Spec ini bersumber dari PRD `damaged.md` (DAMAGED-LOGIC-10a, DAMAGED-LOGIC-10f, EC-DMG-40, F-DMG-03.k2); belum ada TestCase untuk aturan File Manager, sehingga keterlacakan memakai ID aturan PRD.
- Hasil Delete di sisi File Manager (dialog `D-01`, toast `T-01`, Recycle Bin) dimiliki `file-manager.md` (`FAFM-LOGIC-02`); spec ini hanya memakai Delete sebagai pemicu dan mengasersi efeknya pada record Damaged.
- Langkah 6 sampai 11 menjadi anchor positif (foto tampil) bagi asersi absence foto pada langkah 22 dan 25; langkah 38 sampai 40 menjadi anchor bagi langkah 39.
- Damage Log My Asset milik pelapor ikut mengosongkan foto (PRD §9.7) tetapi tidak diasersi di sini karena membutuhkan aktor pelapor umum terpisah.
- Di atas 35 langkah (43) karena dua jenis foto (Damaged Photo dan After photo) dihapus bergantian pada data yang sama.
