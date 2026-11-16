---
id: TC-FA-DAMAGED-E2E-047-mark-repaired-aset-dipinjam-dep-borrow
title: "Mark as Repaired atas aset yang sedang dipinjam berjalan tanpa menunggu Return: baris Borrow tetap Borrowed dan pemegang tidak berubah; sebelum repair aset Damaged ditolak form Borrow"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r38", "§Aturan Logika Modul#r39", "§Aturan Logika Modul#r40", "EC-DMG-09", "EC-DMG-18", "§9.4.4#r19", "§9.4.4#r8", "§9.2#b17", "T-DMG-01"]
smoke: []
dependsOn:
  - "Borrow: baris Borrow, form Borrow"
trace:
  "§Aturan Logika Modul#r38": [15, 23]
  "§Aturan Logika Modul#r39": [29, 30]
  "§Aturan Logika Modul#r40": [31]
  "EC-DMG-09": [23, 29, 30]
  "EC-DMG-18": [3]
  "§9.4.4#r19": [25]
  "§9.4.4#r8": [3]
  "§9.2#b17": [29, 30]
  "T-DMG-01": [13, 15, 20]
anchor: [8, 9, 10, 19]
coverage:
  web: automated
---

# Mark as Repaired atas aset yang sedang dipinjam berjalan tanpa menunggu Return: baris Borrow tetap Borrowed dan pemegang tidak berubah; sebelum repair aset Damaged ditolak form Borrow

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-047-1: aset Name `Tablet Samsung Tab A8 {runId}`, Group `Head Office`, tanpa TAG, sedang dipinjam `Dewi Anggraini {runId}` lewat baris Borrow berstatus `Borrowed`, dengan record `Damaged` Source `Manual` dan What happened `Layar tablet tidak merespons sentuhan di sisi kanan`.
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
16. Klik `Mark as Repaired`
17. Isi Repair note `Sentuhan layar sudah dikalibrasi ulang dan berfungsi normal`
18. Klik `[Mark as Repaired]`
19. Verifikasi baris aset `Camera Canon EOS {runId}` tetap tampil di sub-tab `Active`
20. Verifikasi baris aset `Tablet Samsung Tab A8 {runId}` tidak tampil lagi di sub-tab `Active`
21. Klik sub-tab `History`
22. Ketik Search `{runId}`, tekan Enter
23. Verifikasi baris aset `Tablet Samsung Tab A8 {runId}` tampil di sub-tab `History` dengan Status `Repaired`
24. Klik nama aset pada baris aset `Tablet Samsung Tab A8 {runId}`
25. Verifikasi node `Marked as repaired by [Admin Name]` tampil di dialog Damage Log dengan baris detail Repair note `Sentuhan layar sudah dikalibrasi ulang dan berfungsi normal`
26. Tutup dialog Damage Log

### Baris Borrow tetap Borrowed, pemegang tidak berubah, dan penanda Damaged hilang bersama record
27. Buka halaman Borrow
28. Ketik Search `{runId}`, tekan Enter
29. Verifikasi baris Borrow aset `Tablet Samsung Tab A8 {runId}` tetap berstatus `Borrowed`
30. Verifikasi pemegang pada baris itu tetap `Dewi Anggraini {runId}`
31. Verifikasi baris itu tidak lagi memuat penanda `Damaged`
