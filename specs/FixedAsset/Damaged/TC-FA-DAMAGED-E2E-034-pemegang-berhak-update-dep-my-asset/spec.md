---
id: TC-FA-DAMAGED-E2E-034-pemegang-berhak-update-dep-my-asset
title: "Pemegang yang memegang Update pada Group aset melapor dari My Asset: record langsung Damaged tanpa Review; aset di luar Group Update menjadi Waiting for Confirmation"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§9.4.2#r23, §9.4.4#r7, §Aturan Logika Modul#r42, §2.1#r3, §2#b6, §2.1#b7, T-DMG-01]
smoke: []
dependsOn:
  - "My Asset: kartu aset yang dipegang (Report Damaged)"
trace:
  §9.4.2#r23: [7, 10]
  §9.4.4#r7: [7, 10, 21, 22]
  §Aturan Logika Modul#r42: 7
  §2.1#r3: 18
  §2#b6: 7
  §2.1#b7: 10
  T-DMG-01: [7, 8, 18]
anchor: [9]
coverage:
  web: automated
---

# Pemegang yang memegang Update pada Group aset melapor dari My Asset: record langsung Damaged tanpa Review; aset di luar Group Update menjadi Waiting for Confirmation

## Prerequisites
- Aktor: pemegang aset lewat Assignment yang juga memegang Manage asset & TAG dengan Update pada Group `Head Office` dan Read pada Group `Branch Surabaya`.
- Layar awal: halaman My Asset.
- Data:
  - DU-034-1: aset `Tablet Samsung Tab A8 {runId} Pusat`, Group `Head Office`, status global `Assigned`, dipegang aktor, tanpa record Damage.
  - DU-034-2: aset `Tablet Samsung Tab A8 {runId} Cabang`, Group `Branch Surabaya`, status global `Assigned`, dipegang aktor, tanpa record Damage.
  - DU-034-3: isian laporan aset Pusat, What happened `Layar tablet pecah di sudut kanan atas`, foto `tablet-pusat-pecah.jpg`.
  - DU-034-4: isian laporan aset Cabang, What happened `Baterai tablet menggembung`, foto `tablet-cabang-baterai.jpg`.

## Test Steps

### Aset di Group Update langsung berstatus Damaged tanpa aksi Review
1. Klik `[Report Damaged]` pada kartu aset `Tablet Samsung Tab A8 {runId} Pusat`
2. Isi `What happened` dengan `Layar tablet pecah di sudut kanan atas`
3. Unggah foto `tablet-pusat-pecah.jpg` pada `Damaged Photo`
4. Klik `[Report Damaged]` pada footer dialog
5. Buka tab `Damaged` pada halaman Assets
6. Ketik Search `Tablet Samsung Tab A8 {runId} Pusat`, tekan Enter
7. Verifikasi baris `Tablet Samsung Tab A8 {runId} Pusat` tampil dengan Status `Damaged`
8. Verifikasi Source baris itu `Reported by holder`
9. Verifikasi aksi `Damage Log` tampil pada baris `Tablet Samsung Tab A8 {runId} Pusat`
10. Verifikasi aksi `Review` tidak tampil (Hidden) pada baris `Tablet Samsung Tab A8 {runId} Pusat`

### Aset di luar Group Update menjadi Waiting for Confirmation
11. Buka halaman My Asset
12. Klik `[Report Damaged]` pada kartu aset `Tablet Samsung Tab A8 {runId} Cabang`
13. Isi `What happened` dengan `Baterai tablet menggembung`
14. Unggah foto `tablet-cabang-baterai.jpg` pada `Damaged Photo`
15. Klik `[Report Damaged]` pada footer dialog
16. Buka tab `Damaged` pada halaman Assets
17. Ganti isi kotak search dengan `Tablet Samsung Tab A8 {runId} Cabang`, tekan Enter
18. Verifikasi baris `Tablet Samsung Tab A8 {runId} Cabang` tampil dengan Status `Waiting for Confirmation`

### Node Reported damaged by tercatat pada laporan pemegang
19. Ganti isi kotak search dengan `Tablet Samsung Tab A8 {runId} Pusat`, tekan Enter
20. Klik aksi `Damage Log` pada baris `Tablet Samsung Tab A8 {runId} Pusat`
21. Verifikasi node `Reported damaged by` tampil pada dialog Damage Log
22. Verifikasi `What happened` `Layar tablet pecah di sudut kanan atas` tampil pada node `Reported damaged by`
23. Klik `✕` pada dialog Damage Log
