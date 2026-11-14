---
id: TC-FA-DAMAGED-E2E-022-already-changed-konflik-status
title: "Aksi atas record yang statusnya sudah diubah admin lain ditolak dengan dialog Already Changed dan Reload memuat ulang tabel"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-06, §4.2.4#p5, §4.2.4#r14, §4.4#r10, V-DMG-07, §9.4.2#r7, §9.4.4#r17, §9.4.4#r25, V-DMG-05, EB-ERR-4]
smoke: [EB-ERR-4]
dependsOn: []
trace:
  D-DMG-06: [7, 8, 9, 32, 33]
  §4.2.4#p5: [7, 8, 9, 11, 12]
  §4.2.4#r14: 7
  §4.4#r10: [2, 7]
  V-DMG-07: [7, 8]
  §9.4.2#r7: [7, 8, 14]
  §9.4.4#r17: [7, 12, 14]
  §9.4.4#r25: [7, 14, 32, 38]
  V-DMG-05: [18, 19, 23, 24, 32, 35]
  EB-ERR-4: [7, 12, 14]
anchor: [37]
coverage:
  web: automated
---

# Aksi atas record yang statusnya sudah diubah admin lain ditolak dengan dialog Already Changed dan Reload memuat ulang tabel

## Prerequisites
- Aktor: Total Control (DU-022-5); aktor kedua yang hanya memicu perubahan: Total Control (DU-022-6).
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-022-1: Damage record aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office {runId}`, status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pelapor umum DU-022-4; Damage Log hanya memuat node `Reported damaged by`.
  - DU-022-2: Damage record aset `Printer HP LaserJet M404 {runId}` di Group `Head Office {runId}`, status `Reported Disposal`, Source `Stock opname`, dilaporkan DU-022-5.
  - DU-022-3: Damage record aset `Monitor Dell P2422H {runId}` di Group `Head Office {runId}`, status `In Disposal Process`, Source `Manual`, dilaporkan DU-022-5.
  - DU-022-4: User `Dewi Anggraeni {runId}`, pelapor umum tanpa hak Aktor Damaged; cakupan: aset yang ia pegang.
  - DU-022-5: User `Rina Wijaya {runId}`, role Total Control; cakupan: seluruh client.
  - DU-022-6: User `Agus Pratama {runId}`, role Total Control; cakupan: seluruh client.
  - DU-022-7: Damage record aset `Projector Epson EB-X06 {runId}` tanpa TAG di Group `Head Office {runId}`, status `Damaged`, Source `Manual`, dilaporkan DU-022-5.
  - DU-022-8: Input Repair note oleh DU-022-5 atas `Projector Epson EB-X06 {runId}`: Repair note `Lampu proyektor diganti dan unit sudah diuji menyala normal`.
  - DU-022-9: Input Reason oleh DU-022-6 atas `Projector Epson EB-X06 {runId}`: Reason `Unit sudah dilaporkan lebih dulu oleh admin lain`.
- Kondisi:
  - After photo required bernilai `OFF`.
  - Level Feature Suite Disposal bernilai `Basic`.

## Test Steps

### Confirm atas record yang sudah dikonfirmasi admin lain ditolak dengan Already Changed
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` tampil di tabel dengan status `Waiting for Confirmation`
3. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
4. Klik `Review`
5. Agus Pratama {runId} mengonfirmasi laporan aset `Laptop Dell Latitude 5420 {runId}` dari sesi lain
6. Klik `[Confirm]`
7. Verifikasi dialog `Already Changed` terbuka
8. Verifikasi dialog memuat pesan `This record was changed by [User Name]. Reload to see the latest status.` dengan `[User Name]` berisi nama admin yang lebih dulu mengubah status
9. Verifikasi dialog memuat tombol `[Reload]`

### Reload memuat ulang tabel dan record tidak berubah oleh aksi yang ditolak
10. Klik `[Reload]` pada dialog `Already Changed`
11. Verifikasi dialog `Already Changed` tidak lagi tampil
12. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` tampil di tabel dengan status `Damaged`
13. Klik nama aset `Laptop Dell Latitude 5420 {runId}` pada kolom Name
14. Verifikasi timeline memuat tepat satu node `Report confirmed by` dengan admin yang lebih dulu mengubah status sebagai pelaku
15. Klik `✕` pada dialog `Damage Log`

### Mark as Repaired tidak ditawarkan pada record Reported Disposal dan In Disposal Process
16. Ganti isi kotak search dengan `Printer HP LaserJet M404 {runId}`, tekan Enter
17. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
18. Verifikasi item `Damage Log` tampil pada menu baris `Printer HP LaserJet M404 {runId}`
19. Verifikasi item `Mark as Repaired` tidak tampil pada menu baris `Printer HP LaserJet M404 {runId}`
20. Tekan Esc untuk menutup menu baris
21. Ganti isi kotak search dengan `Monitor Dell P2422H {runId}`, tekan Enter
22. Klik `⋯` pada baris `Monitor Dell P2422H {runId}`
23. Verifikasi item `Damage Log` tampil pada menu baris `Monitor Dell P2422H {runId}`
24. Verifikasi item `Mark as Repaired` tidak tampil pada menu baris `Monitor Dell P2422H {runId}`

### Mark as Repaired atas record yang sudah dipindah ke Reported Disposal ditolak dengan Already Changed
25. Tekan Esc untuk menutup menu baris
26. Ganti isi kotak search dengan `Projector Epson EB-X06 {runId}`, tekan Enter
27. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
28. Klik `Mark as Repaired`
29. Isi Repair note `Lampu proyektor diganti dan unit sudah diuji menyala normal`
30. Agus Pratama {runId} menjalankan Report Disposal atas record `Projector Epson EB-X06 {runId}` dengan Reason `Unit sudah dilaporkan lebih dulu oleh admin lain` dari sesi lain
31. Klik `[Mark as Repaired]` pada dialog `Mark as Repaired`
32. Verifikasi dialog `Already Changed` terbuka
33. Verifikasi dialog memuat tombol `[Reload]`
34. Klik `[Reload]` pada dialog `Already Changed`
35. Verifikasi baris aset `Projector Epson EB-X06 {runId}` tampil di tabel dengan status `Reported Disposal`
36. Klik nama aset `Projector Epson EB-X06 {runId}` pada kolom Name
37. Verifikasi timeline memuat tepat satu node `Disposal reported by` dengan pelaku `Agus Pratama {runId}`
38. Verifikasi tidak ada node `Marked as repaired by` pada timeline
39. Klik `✕` pada dialog `Damage Log`
