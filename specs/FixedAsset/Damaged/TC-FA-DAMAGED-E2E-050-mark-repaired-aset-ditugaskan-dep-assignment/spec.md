---
id: TC-FA-DAMAGED-E2E-050-mark-repaired-aset-ditugaskan-dep-assignment
title: "Mark as Repaired atas aset yang sedang ditugaskan berjalan tanpa Unassign: baris Assignment tetap Assigned dan pemegang tidak berubah; sebelum repair aset Damaged ditolak form Assign"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r38", "§Aturan Logika Modul#r39", "§9.4.2#r10", "§9.4.2#r15", "§9.4.4#r21", "§9.4.4#r8", "§9.2#b17", "T-DMG-01"]
smoke: []
dependsOn:
  - "Assignment: baris Assignment, form Assign"
trace:
  "§Aturan Logika Modul#r38": [14, 22]
  "§Aturan Logika Modul#r39": [28, 29]
  "§9.4.2#r10": [22, 28, 29]
  "§9.4.2#r15": [3]
  "§9.4.4#r21": [24]
  "§9.4.4#r8": [3]
  "§9.2#b17": [28, 29]
  "T-DMG-01": [12, 14, 19]
anchor: [8, 9, 18]
coverage:
  web: automated
---

# Mark as Repaired atas aset yang sedang ditugaskan berjalan tanpa Unassign: baris Assignment tetap Assigned dan pemegang tidak berubah; sebelum repair aset Damaged ditolak form Assign

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-050-1: aset Name `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, tanpa TAG, sedang ditugaskan kepada `Bima Prakoso {runId}` lewat baris Assignment berstatus `Assigned`, dengan record `Damaged` Source `Manual` dan What happened `Engsel laptop longgar dan layar tidak bisa berdiri tegak`.
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
15. Klik `Mark as Repaired`
16. Isi Repair note `Engsel laptop sudah diganti dan layar bisa berdiri tegak`
17. Klik `[Mark as Repaired]`
18. Verifikasi baris aset `Monitor Dell P2422H {runId}` tetap tampil di sub-tab `Active`
19. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` tidak tampil lagi di sub-tab `Active`
20. Klik sub-tab `History`
21. Ketik Search `{runId}`, tekan Enter
22. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` tampil di sub-tab `History` dengan Status `Repaired`
23. Klik nama aset pada baris aset `Laptop Dell Latitude 5420 {runId}`
24. Verifikasi node `Marked as repaired by [Admin Name]` tampil di dialog Damage Log dengan baris detail Repair note `Engsel laptop sudah diganti dan layar bisa berdiri tegak`
25. Tutup dialog Damage Log

### Baris Assignment tetap Assigned dan pemegang tidak berubah
26. Buka halaman Assignment
27. Ketik Search `{runId}`, tekan Enter
28. Verifikasi baris Assignment aset `Laptop Dell Latitude 5420 {runId}` tetap berstatus `Assigned`
29. Verifikasi pemegang pada baris itu tetap `Bima Prakoso {runId}`
