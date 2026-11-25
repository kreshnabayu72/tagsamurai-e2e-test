---
id: TC-FA-DAMAGED-E2E-047-mark-repaired-aset-dipinjam-dep-borrow
title: "Mark as Repaired atas aset yang sedang dipinjam berjalan tanpa menunggu Return: baris Borrow tetap Borrowed dan pemegang tidak berubah; sebelum repair aset Damaged ditolak form Borrow"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r41", "§Aturan Logika Modul#r42", "§Aturan Logika Modul#r43", "EC-DMG-09", "EC-DMG-18", "§9.4.4#r21", "§9.4.4#r8", "§9.2#b19", "T-DMG-01", "§9.7#r9"]
smoke: []
dependsOn:
  - "Borrow: baris Borrow, form Borrow"
trace:
  "§Aturan Logika Modul#r41": [15, 25]
  "§Aturan Logika Modul#r42": [31, 32]
  "§Aturan Logika Modul#r43": [33]
  "EC-DMG-09": [25, 31, 32, 36]
  "EC-DMG-18": [3]
  "§9.4.4#r21": [27]
  "§9.4.4#r8": [3]
  "§9.2#b19": [31, 32]
  "T-DMG-01": [13, 15, 16, 17, 22]
  "§9.7#r9": [31, 33, 36]
anchor: [8, 9, 10, 21]
coverage:
  web: automated
---

# Mark as Repaired atas aset yang sedang dipinjam berjalan tanpa menunggu Return: baris Borrow tetap Borrowed dan pemegang tidak berubah; sebelum repair aset Damaged ditolak form Borrow

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-047-1: aset Name `Tablet Samsung Tab A8 {runId}`, Group `Head Office`, tanpa TAG, sedang dipinjam `Dewi Anggraini {runId}` lewat baris Borrow berstatus `Borrowed`, status global `Borrowed`, dengan record `Damaged` Source `Manual` dan What happened `Layar tablet tidak merespons sentuhan di sisi kanan`.
  - DU-047-2: aset Name `Camera Canon EOS {runId}`, Group `Head Office`, tanpa TAG, tanpa pemegang, dengan record `Damaged` Source `Manual` dan What happened `Lensa tidak bisa fokus otomatis`.
- Kondisi:
  - After photo required bernilai `OFF`.

## Test Steps

### Form Borrow menolak aset Damaged
1. Buka form Borrow
2. Pilih aset `Camera Canon EOS {runId}` pada form Borrow
3. Verifikasi form Borrow menolak aset `Camera Canon EOS {runId}` karena berstatus Damaged
4. Klik `✕` pada form Borrow
5. Klik `[Leave]` pada dialog Unsaved Changes

### Keadaan baris Borrow sebelum Mark as Repaired
6. Buka halaman Borrow
7. Ketik Search `{runId}`, tekan Enter
8. Verifikasi baris Borrow aset `Tablet Samsung Tab A8 {runId}` berstatus `Borrowed`
9. Verifikasi pemegang pada baris itu `Dewi Anggraini {runId}`
10. Verifikasi baris itu memuat penanda `Damaged`

### Mark as Repaired atas aset yang sedang dipinjam
11. Buka halaman Assets, tab `Damaged`
12. Ketik Search `{runId}`, tekan Enter
13. Verifikasi baris aset `Tablet Samsung Tab A8 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`
14. Klik `⋯` pada baris aset `Tablet Samsung Tab A8 {runId}`
15. Verifikasi aksi `Mark as Repaired` tampil pada menu baris
16. Verifikasi aksi `Report Disposal` pada menu itu Disabled
17. Verifikasi aksi `Report Missing` pada menu itu aktif dan bisa diklik
18. Klik `Mark as Repaired`
19. Isi Repair note `Sentuhan layar sudah dikalibrasi ulang dan berfungsi normal`
20. Klik `[Mark as Repaired]`
21. Verifikasi baris aset `Camera Canon EOS {runId}` tetap tampil di sub-tab `Active`
22. Verifikasi baris aset `Tablet Samsung Tab A8 {runId}` tidak tampil lagi di sub-tab `Active`
23. Klik sub-tab `History`
24. Ketik Search `{runId}`, tekan Enter
25. Verifikasi baris aset `Tablet Samsung Tab A8 {runId}` tampil di sub-tab `History` dengan Status `Repaired`
26. Klik nama aset pada baris aset `Tablet Samsung Tab A8 {runId}`
27. Verifikasi node `Marked as repaired by [Admin Name]` tampil di dialog Damage Log dengan baris detail Repair note `Sentuhan layar sudah dikalibrasi ulang dan berfungsi normal`
28. Tutup dialog Damage Log

### Baris Borrow tetap Borrowed, pemegang tidak berubah, dan penanda Damaged hilang bersama record
29. Buka halaman Borrow
30. Ketik Search `{runId}`, tekan Enter
31. Verifikasi baris Borrow aset `Tablet Samsung Tab A8 {runId}` tetap berstatus `Borrowed`
32. Verifikasi pemegang pada baris itu tetap `Dewi Anggraini {runId}`
33. Verifikasi baris itu tidak lagi memuat penanda `Damaged`

### Status global aset tetap Borrowed sesudah Mark as Repaired
34. Buka halaman Assets, tab `Assets`
35. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
36. Verifikasi status global aset `Borrowed` pada baris `Tablet Samsung Tab A8 {runId}`
