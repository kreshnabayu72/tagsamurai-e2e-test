---
id: TC-FA-DAMAGED-E2E-050-mark-repaired-aset-ditugaskan-dep-assignment
title: "Mark as Repaired atas aset yang sedang ditugaskan berjalan tanpa Unassign: baris Assignment tetap Assigned dan pemegang tidak berubah; sebelum repair aset Damaged ditolak form Assign"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r41", "§Aturan Logika Modul#r42", "EC-DMG-10", "EC-DMG-18", "§9.4.4#r22", "§9.4.4#r8", "§9.2#b19", "T-DMG-01", "§9.7#r9"]
smoke: []
dependsOn:
  - "Assignment: baris Assignment, form Assign"
trace:
  "§Aturan Logika Modul#r41": [14, 24]
  "§Aturan Logika Modul#r42": [30, 31]
  "EC-DMG-10": [24, 30, 31, 34]
  "EC-DMG-18": [3]
  "§9.4.4#r22": [26]
  "§9.4.4#r8": [3]
  "§9.2#b19": [30, 31]
  "T-DMG-01": [12, 14, 15, 16, 21]
  "§9.7#r9": [30, 34]
anchor: [8, 9, 20]
coverage:
  web: automated
---

# Mark as Repaired atas aset yang sedang ditugaskan berjalan tanpa Unassign: baris Assignment tetap Assigned dan pemegang tidak berubah; sebelum repair aset Damaged ditolak form Assign

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-050-1: aset Name `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, tanpa TAG, sedang ditugaskan kepada `Bima Prakoso {runId}` lewat baris Assignment berstatus `Assigned`, status global `Assigned`, dengan record `Damaged` Source `Manual` dan What happened `Engsel laptop longgar dan layar tidak bisa berdiri tegak`.
  - DU-050-2: aset Name `Monitor Dell P2422H {runId}`, Group `Head Office`, tanpa TAG, tanpa pemegang, dengan record `Damaged` Source `Manual` dan What happened `Layar monitor berkedip dan garis vertikal muncul`.
- Kondisi:
  - After photo required bernilai `OFF`.

## Test Steps

### Form Assign menolak aset Damaged
1. Buka form Assign
2. Pilih aset `Monitor Dell P2422H {runId}` pada form Assign
3. Verifikasi form Assign menolak aset `Monitor Dell P2422H {runId}` karena berstatus Damaged
4. Klik `✕` pada form Assign
5. Klik `[Leave]` pada dialog Unsaved Changes

### Keadaan baris Assignment sebelum Mark as Repaired
6. Buka halaman Assignment
7. Ketik Search `{runId}`, tekan Enter
8. Verifikasi baris Assignment aset `Laptop Dell Latitude 5420 {runId}` berstatus `Assigned`
9. Verifikasi pemegang pada baris itu `Bima Prakoso {runId}`

### Mark as Repaired atas aset yang sedang ditugaskan
10. Buka halaman Assets, tab `Damaged`
11. Ketik Search `{runId}`, tekan Enter
12. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`
13. Klik `⋯` pada baris aset `Laptop Dell Latitude 5420 {runId}`
14. Verifikasi aksi `Mark as Repaired` tampil pada menu baris
15. Verifikasi aksi `Report Disposal` pada menu itu Disabled
16. Verifikasi aksi `Report Missing` pada menu itu aktif dan bisa diklik
17. Klik `Mark as Repaired`
18. Isi Repair note `Engsel laptop sudah diganti dan layar bisa berdiri tegak`
19. Klik `[Mark as Repaired]`
20. Verifikasi baris aset `Monitor Dell P2422H {runId}` tetap tampil di sub-tab `Active`
21. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` tidak tampil lagi di sub-tab `Active`
22. Klik sub-tab `History`
23. Ketik Search `{runId}`, tekan Enter
24. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` tampil di sub-tab `History` dengan Status `Repaired`
25. Klik nama aset pada baris aset `Laptop Dell Latitude 5420 {runId}`
26. Verifikasi node `Marked as repaired by [Admin Name]` tampil di dialog Damage Log dengan baris detail Repair note `Engsel laptop sudah diganti dan layar bisa berdiri tegak`
27. Tutup dialog Damage Log

### Baris Assignment tetap Assigned dan pemegang tidak berubah
28. Buka halaman Assignment
29. Ketik Search `{runId}`, tekan Enter
30. Verifikasi baris Assignment aset `Laptop Dell Latitude 5420 {runId}` tetap berstatus `Assigned`
31. Verifikasi pemegang pada baris itu tetap `Bima Prakoso {runId}`

### Status global aset tetap Assigned sesudah Mark as Repaired
32. Buka halaman Assets, tab `Assets`
33. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
34. Verifikasi status global aset `Assigned` pada baris `Laptop Dell Latitude 5420 {runId}`
