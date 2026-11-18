---
id: TC-FA-DAMAGED-E2E-023-guided-tooltip
title: "Guided Tooltip tab Damaged tampil pada kunjungan pertama dan flag selesai bertahan antar sesi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-TBL-10, §4.7#r1, §4.7#r2, §4.7#r3]
smoke: []
dependsOn: []
trace:
  EB-TBL-10: [2, 4, 6, 8, 9, 13, 14, 17, 18, 21, 23, 27, 28, 31]
  §4.7#r1: 2
  §4.7#r2: 4
  §4.7#r3: 6
anchor: []
coverage:
  web: automated
---

# Guided Tooltip tab Damaged tampil pada kunjungan pertama dan flag selesai bertahan antar sesi

## Prerequisites
- Aktor: Total Control yang belum pernah menyelesaikan Guided Tooltip tab Damaged (DU-023-1); aktor kedua: Total Control yang flag Guided Tooltip-nya sudah diset dari perangkat lain (DU-023-2); aktor ketiga: Total Control yang belum pernah menyelesaikan Guided Tooltip tab Damaged dan memakai jalur Skip (DU-023-3); aktor keempat: Total Control dengan akses sama yang belum mengubah preferensinya (DU-023-4).
- Layar awal: halaman Assets, tab Assets.
- Data:
  - DU-023-1: User `Rina Wijaya {runId}`, role Total Control, flag Guided Tooltip tab Damaged belum diset; cakupan: seluruh client.
  - DU-023-2: User `Agus Pratama {runId}`, role Total Control, flag Guided Tooltip tab Damaged sudah diset dari perangkat lain; cakupan: seluruh client.
  - DU-023-3: User `Budi Santoso {runId}`, role Total Control, flag Guided Tooltip tab Damaged belum diset; cakupan: seluruh client.
  - DU-023-4: User `Sari Wulandari {runId}`, role Total Control, flag Guided Tooltip tab Damaged belum diset dan belum pernah diubah; cakupan: seluruh client.

## Test Steps

### Kunjungan pertama menampilkan Guided Tooltip otomatis dan Done menyetel flag
1. Klik tab `Damaged`
2. Verifikasi langkah `Step 1 of 3` tampil dengan judul `Focus on what needs action` dan deskripsi `Narrow down the list to the records that need your attention.`
3. Klik `[Next]`
4. Verifikasi langkah `Step 2 of 3` tampil dengan judul `Track damaged assets` dan deskripsi `Every asset stays here until its report is resolved.`
5. Klik `[Next]`
6. Verifikasi langkah `Step 3 of 3` tampil dengan judul `Review closed records` dan deskripsi `Closed records stay here for reference.`
7. Klik `[Done]`
8. Verifikasi sub-tab `Active` dan `History` tampil sesudah `[Done]`
9. Verifikasi Guided Tooltip tidak tampil lagi

### Flag yang sudah diset bertahan sesudah keluar dan masuk kembali
10. Keluar dari aplikasi
11. Masuk kembali sebagai aktor yang sama
12. Klik tab `Damaged`
13. Verifikasi sub-tab `Active` dan `History` tampil pada sesi berikutnya
14. Verifikasi Guided Tooltip tidak tampil pada kunjungan berikutnya

### Flag yang diset dari perangkat lain berlaku pada sesi browser baru
15. Masuk sebagai Agus Pratama {runId} dari sesi browser baru
16. Klik tab `Damaged`
17. Verifikasi sub-tab `Active` dan `History` tampil pada sesi browser baru
18. Verifikasi Guided Tooltip tidak tampil untuk aktor yang flag-nya diset dari perangkat lain

### Skip menyetel flag sehingga Guided Tooltip tidak tampil lagi
19. Masuk sebagai Budi Santoso {runId} dari sesi browser baru
20. Klik tab `Damaged`
21. Verifikasi Guided Tooltip tampil otomatis pada kunjungan pertama dengan langkah `Step 1 of 3`
22. Klik `[Skip]`
23. Verifikasi sub-tab `Active` dan `History` tampil sesudah `[Skip]`
24. Keluar dari aplikasi
25. Masuk kembali sebagai aktor yang sama
26. Klik tab `Damaged`
27. Verifikasi sub-tab `Active` dan `History` tampil pada kunjungan berikutnya sesudah Skip
28. Verifikasi Guided Tooltip tidak tampil pada kunjungan berikutnya sesudah Skip

### Preferensi aktor lain tidak berlaku bagi aktor yang belum mengubahnya
29. Masuk sebagai Sari Wulandari {runId} dari sesi browser baru
30. Klik tab `Damaged`
31. Verifikasi Guided Tooltip tampil otomatis dengan langkah `Step 1 of 3` dan judul `Focus on what needs action` pada kunjungan pertama aktor ini, walau aktor lain sudah menyelesaikannya
