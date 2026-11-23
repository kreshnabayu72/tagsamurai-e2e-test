---
id: TC-FA-DAMAGED-E2E-009-review-confirm
title: "Review laporan Waiting for Confirmation: Confirm dari footer Damage Log mengubah record menjadi Damaged tanpa dialog kedua, termasuk laporan yang dibuat Aktor Damaged itu sendiri sebelum memiliki hak"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, D-DMG-11, §4.4#r4, §4.4#r5, §4.4#p1, §8.1#b1, §8.1#r6, §8.1#r8, TS-DMG-04, EC-DMG-08, §Aturan Logika Modul#r53, §Aturan Logika Modul#r89, §Aturan Logika Modul#r19, §2.1#b8, §9.7#r5, F-DMG-04, §3#p4, §9.6#r2, §9.4.3#b6, EB-FB-1@confirm]
smoke: [EB-FB-1@confirm]
dependsOn: []
trace:
  T-DMG-01: [2, 4, 19, 21, 22, 25, 27, 35]
  D-DMG-11: [6, 7, 12, 13, 30]
  §4.4#r4: [6, 7, 29, 30]
  §4.4#r5: [10, 11, 12]
  §4.4#p1: [11, 13, 14, 15, 18]
  §8.1#b1: [11, 13, 15]
  §8.1#r6: [7, 30]
  §8.1#r8: [15, 16, 33]
  TS-DMG-04: 10
  EC-DMG-08: [27, 30, 32, 33, 35]
  §Aturan Logika Modul#r53: [14, 18]
  §Aturan Logika Modul#r89: [27, 30, 32, 35]
  §Aturan Logika Modul#r19: [8, 14]
  §2.1#b8: [27, 30]
  §9.7#r5: 18
  F-DMG-04: [10, 14, 18]
  §3#p4: [8, 14]
  §9.6#r2: [10, 14, 15]
  §9.4.3#b6: [27, 30]
  EB-FB-1@confirm: 10
anchor: []
coverage:
  web: automated
---

# Review laporan Waiting for Confirmation: Confirm dari footer Damage Log mengubah record menjadi Damaged tanpa dialog kedua, termasuk laporan yang dibuat Aktor Damaged itu sendiri sebelum memiliki hak

## Prerequisites
- Aktor: Total Control (DU-009-4).
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-009-1: Damage record aset `Laptop Dell Latitude 5420 {runId}` di Group `Head Office`, status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pemegang aset DU-009-3 dengan What happened `Layar laptop retak setelah terjatuh dari meja kerja`; Damage Log hanya memuat node `Reported damaged by`.
  - DU-009-2: Damage record aset `Printer HP LaserJet M404 {runId}` di Group `Head Office`, status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan oleh DU-009-4 sebelum ia memegang role Total Control, dengan What happened `Cartridge printer bocor dan hasil cetak bergaris`; Damage Log hanya memuat node `Reported damaged by`.
  - DU-009-3: User `Budi Santoso {runId}`, pelapor umum pemegang aset DU-009-1, tanpa hak Aktor Damaged; cakupan: aset yang ia pegang.
  - DU-009-4: User `Rina Wijaya {runId}`, role Total Control; cakupan: seluruh client.

## Test Steps

### Review membuka Damage Log dengan footer Reject dan Confirm
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` tampil di tabel dengan status `Waiting for Confirmation`
3. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
4. Verifikasi item `Review` tampil dan aktif pada menu baris
5. Klik `Review`
6. Verifikasi dialog `Damage Log` terbuka untuk aset `Laptop Dell Latitude 5420 {runId}`
7. Verifikasi footer dialog memuat tombol `[Reject]` dan `[Confirm]` yang aktif
8. Verifikasi badge status record pada dialog `Waiting for Confirmation`

### Confirm langsung menjadikan record Damaged tanpa dialog kedua
9. Klik `[Confirm]`
10. Verifikasi toast `Success, report has been confirmed.` tampil
11. Verifikasi dialog `Damage Log` tetap terbuka
12. Verifikasi tidak ada dialog konfirmasi kedua yang tampil
13. Verifikasi tombol `[Reject]` dan `[Confirm]` tidak lagi tampil di footer dialog
14. Verifikasi badge status record pada dialog `Damaged`
15. Verifikasi timeline memuat node `Report confirmed by` dengan aktor yang sedang masuk sebagai pelaku
16. Verifikasi timeline memuat tepat satu node `Report confirmed by`
17. Klik `✕` pada dialog `Damage Log`
18. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` di tabel Active berstatus `Damaged`
19. Verifikasi hasil Search memuat tepat satu baris
20. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
21. Verifikasi item `Damage Log` tampil pada menu baris
22. Verifikasi item `Review` tidak tampil pada menu baris
23. Tekan Esc untuk menutup menu baris

### Aktor Damaged dapat Confirm laporan yang ia buat sendiri sebelum memiliki hak
24. Ganti isi kotak search dengan `Printer HP LaserJet M404 {runId}`, tekan Enter
25. Verifikasi baris aset `Printer HP LaserJet M404 {runId}` tampil di tabel dengan status `Waiting for Confirmation`
26. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
27. Verifikasi item `Review` tampil dan aktif pada menu baris laporan buatan aktor sendiri
28. Klik `Review`
29. Verifikasi dialog `Damage Log` terbuka untuk aset `Printer HP LaserJet M404 {runId}`
30. Verifikasi footer dialog memuat tombol `[Reject]` dan `[Confirm]` yang aktif untuk laporan buatan aktor sendiri
31. Klik `[Confirm]`
32. Verifikasi badge status record `Printer HP LaserJet M404 {runId}` pada dialog `Damage Log` berubah menjadi `Damaged`
33. Verifikasi timeline memuat node `Report confirmed by` dengan aktor yang sedang masuk sebagai pelaku atas laporan buatannya sendiri
34. Klik `✕` pada dialog `Damage Log`
35. Verifikasi baris aset `Printer HP LaserJet M404 {runId}` di tabel Active berstatus `Damaged`
