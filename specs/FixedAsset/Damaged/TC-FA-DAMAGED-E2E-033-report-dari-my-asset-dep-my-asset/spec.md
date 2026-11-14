---
id: TC-FA-DAMAGED-E2E-033-report-dari-my-asset-dep-my-asset
title: "Pemegang melapor rusak dari My Asset: record Waiting for Confirmation, status global Damaged, toast laporan terkirim, dan status laporan tampil di My Asset"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-01, §4.2.3#p1, FI-DMG-04, TS-DMG-02, §Aturan Logika Modul#r43, §Aturan Logika Modul#r27, §Aturan Logika Modul#r28, §9.7#r2, §3#p4, §4.2.2#p3, §4.8#r4, §2.1#r3, §2#b7, §9.1#r1, T-DMG-01, EB-FB-1@report-damaged]
smoke: [EB-FB-1@report-damaged]
dependsOn:
  - "My Asset: kartu aset yang dipegang (Report Damaged, status laporan)"
trace:
  D-DMG-01: 19
  §4.2.3#p1: 9
  FI-DMG-04: 10
  TS-DMG-02: 14
  §Aturan Logika Modul#r43: 19
  §Aturan Logika Modul#r27: 25
  §Aturan Logika Modul#r28: 25
  §9.7#r2: [3, 25, 26]
  §3#p4: [19, 25]
  §4.2.2#p3: 15
  §4.8#r4: 7
  §2.1#r3: 7
  §2#b7: [7, 19]
  §9.1#r1: 19
  T-DMG-01: [20, 21, 22]
  EB-FB-1@report-damaged: 14
anchor: [6]
coverage:
  web: automated
---

# Pemegang melapor rusak dari My Asset: record Waiting for Confirmation, status global Damaged, toast laporan terkirim, dan status laporan tampil di My Asset

## Prerequisites
- Aktor: pelapor umum, yaitu pemegang aset lewat Assignment tanpa role Damaged. Total Control mencatat jumlah badge tab Damaged sebelum laporan, lalu membaca hasil di tab Damaged dan Asset List.
- Layar awal: halaman Assets, tab Assets.
- Data:
  - DU-033-1: aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, status global `Assigned`, dipegang aktor, tanpa record Damage.
  - DU-033-2: isian laporan, What happened `Keyboard laptop tidak merespons tombol`, foto `keyboard-rusak.jpg`.

## Test Steps

### Jumlah badge tab Damaged dicatat sebelum laporan
1. Masuk sebagai Total Control
2. Buka halaman Assets
3. Verifikasi badge jumlah pada tab `Damaged` tampil, lalu catat jumlahnya sebagai jumlah awal

### Pemegang melapor rusak dari My Asset
4. Masuk sebagai pemegang aset `Laptop Dell Latitude 5420 {runId}`
5. Buka halaman My Asset
6. Verifikasi kartu aset `Laptop Dell Latitude 5420 {runId}` tampil di My Asset
7. Verifikasi aksi `Report Damaged` tersedia pada kartu aset `Laptop Dell Latitude 5420 {runId}`
8. Klik `[Report Damaged]` pada kartu aset `Laptop Dell Latitude 5420 {runId}`
9. Verifikasi dialog berjudul `Report Damaged` tampil dengan blok aset `Laptop Dell Latitude 5420 {runId}`
10. Verifikasi kotak dampak `The asset admins will review your report.` tidak tampil pada dialog
11. Isi `What happened` dengan `Keyboard laptop tidak merespons tombol`
12. Unggah foto `keyboard-rusak.jpg` pada `Damaged Photo`
13. Klik `[Report Damaged]` pada footer dialog
14. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil

### Status laporan tampil di My Asset
15. Verifikasi status laporan `Waiting for Confirmation` tampil pada kartu aset `Laptop Dell Latitude 5420 {runId}`

### Hasil laporan dibaca Total Control
16. Masuk sebagai Total Control
17. Buka tab `Damaged` pada halaman Assets
18. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
19. Verifikasi tepat satu baris `Laptop Dell Latitude 5420 {runId}` tampil dengan Status `Waiting for Confirmation`
20. Verifikasi Source baris itu `Reported by holder`
21. Verifikasi Last Holder baris itu adalah nama pemegang aset
22. Verifikasi Reported By baris itu adalah nama pemegang yang melapor
23. Buka tab `Assets` pada halaman Assets
24. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
25. Verifikasi status global aset `Damaged` pada baris `Laptop Dell Latitude 5420 {runId}`

### Badge jumlah tab Damaged bertambah satu
26. Verifikasi jumlah pada badge tab `Damaged` bertambah satu dari jumlah awal yang dicatat sebelum laporan
