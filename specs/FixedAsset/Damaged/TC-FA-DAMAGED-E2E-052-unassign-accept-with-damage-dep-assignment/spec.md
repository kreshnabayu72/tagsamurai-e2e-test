---
id: TC-FA-DAMAGED-E2E-052-unassign-accept-with-damage-dep-assignment
title: "Unassign Accept with damage membuat record Source Assign return; laporan pemegang aset ditugaskan tetap diputuskan Aktor Damaged dan Unassign menautkan laporan ke Assess Damage"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r46", "§Aturan Logika Modul#r56", "§9.2#b7", "§8.3#r2", "§8.1#r7", "§Aturan Logika Modul#r34", "§Aturan Logika Modul#r41", "§9.7#r3", "T-DMG-01"]
smoke: []
dependsOn:
  - "Assignment: Unassign (Accept with damage, Assess Damage)"
trace:
  "§Aturan Logika Modul#r46": [15, 16]
  "§Aturan Logika Modul#r56": [28, 29, 33, 34, 36]
  "§9.2#b7": [15, 16]
  "§8.3#r2": [14]
  "§8.1#r7": [14, 15, 16]
  "§Aturan Logika Modul#r34": [25, 29]
  "§Aturan Logika Modul#r41": [7, 25]
  "§9.7#r3": [10, 12]
  "T-DMG-01": [10, 11, 12, 29, 36]
anchor: []
coverage:
  web: automated
---

# Unassign Accept with damage membuat record Source Assign return; laporan pemegang aset ditugaskan tetap diputuskan Aktor Damaged dan Unassign menautkan laporan ke Assess Damage

## Prerequisites
- Aktor: Total Control, yang bertindak sebagai Aktor Assignment dan sebagai Aktor Damaged.
- Layar awal: halaman Assignment.
- Data:
  - DU-052-1: aset Name `Webcam Logitech C920 {runId}`, Group `Head Office`, tanpa TAG, sedang ditugaskan kepada `Citra Maharani {runId}` lewat baris Assignment berstatus `Assigned`, belum punya record Damage.
  - DU-052-2: aset Name `Tablet Lenovo Tab M10 {runId}`, Group `Head Office`, tanpa TAG, sedang ditugaskan kepada `Dani Ramadhan {runId}` lewat baris Assignment berstatus `Assigned`, dengan record `Waiting for Confirmation` Source `Reported by holder` dari laporan pemegang dengan What happened `Layar tablet muncul bintik hitam dan sentuhan lambat`.

## Test Steps

### Unassign Accept with damage atas aset tanpa record membuat record Damaged Source Assign return
1. Ketik Search `Webcam Logitech C920 {runId}`, tekan Enter
2. Klik `Unassign` pada baris Assignment aset `Webcam Logitech C920 {runId}`
3. Pilih `Accept with damage`
4. Isi Description `Lensa webcam tergores dan gambar buram`
5. Pilih foto Return `webcam-lensa-tergores.jpg`
6. Submit form Unassign
7. Verifikasi baris Assignment aset `Webcam Logitech C920 {runId}` tidak lagi berstatus `Assigned`
8. Buka halaman Assets, tab `Damaged`
9. Ketik Search `Webcam Logitech C920 {runId}`, tekan Enter
10. Verifikasi baris aset `Webcam Logitech C920 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`, tanpa Confirm
11. Verifikasi kolom Source pada baris itu `Assign return`
12. Verifikasi kolom Last Holder pada baris itu terisi nama pemegang saat Unassign, dalam bentuk nama depan dan inisial nama belakang
13. Klik nama aset pada baris aset `Webcam Logitech C920 {runId}`
14. Verifikasi node `Reported damaged by [Reporter Name]` tampil atas nama Aktor Assignment yang melakukan Unassign
15. Verifikasi baris detail What happened pada node itu `Lensa webcam tergores dan gambar buram`
16. Verifikasi baris detail Damaged Photo pada node itu memuat foto Return `webcam-lensa-tergores.jpg`
17. Tutup dialog Damage Log

### Unassign atas aset dengan laporan pemegang: laporan tetap diputuskan Aktor Damaged
18. Buka halaman Assignment
19. Ketik Search `Tablet Lenovo Tab M10 {runId}`, tekan Enter
20. Klik `Unassign` pada baris Assignment aset `Tablet Lenovo Tab M10 {runId}`
21. Pilih `Accept with damage`
22. Isi Description `Layar tablet bintik hitam seperti yang dilaporkan pemegang`
23. Pilih foto Return `tablet-layar-bintik.jpg`
24. Submit form Unassign
25. Verifikasi baris Assignment aset `Tablet Lenovo Tab M10 {runId}` tidak lagi berstatus `Assigned`
26. Buka halaman Assets, tab `Damaged`
27. Ketik Search `Tablet Lenovo Tab M10 {runId}`, tekan Enter
28. Verifikasi tepat satu baris aset `Tablet Lenovo Tab M10 {runId}` tampil di sub-tab `Active`
29. Verifikasi Status baris itu tetap `Waiting for Confirmation`
30. Klik `⋯` pada baris aset `Tablet Lenovo Tab M10 {runId}`
31. Klik `Review`
32. Klik `[Confirm]` pada footer dialog Damage Log
33. Verifikasi node `Report confirmed by [Admin Name]` tampil di dialog Damage Log
34. Verifikasi baris detail What happened pada node `Reported damaged by [Reporter Name]` tetap `Layar tablet muncul bintik hitam dan sentuhan lambat`
35. Tutup dialog Damage Log
36. Verifikasi Status baris aset `Tablet Lenovo Tab M10 {runId}` `Damaged`
