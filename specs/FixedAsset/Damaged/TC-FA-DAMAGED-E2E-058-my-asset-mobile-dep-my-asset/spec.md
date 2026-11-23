---
id: TC-FA-DAMAGED-E2E-058-my-asset-mobile-dep-my-asset
title: "Di mobile pemegang melapor rusak dari kartu My Asset lewat bottom sheet dengan kamera, membatalkan laporannya, dan melihat status laporan termasuk laporan scan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§4.6#p1, §4.6#b3, §4.2.2#p3, §4.8#r7, D-DMG-01, D-DMG-08, TS-DMG-02, TS-DMG-07, §Aturan Logika Modul#r55, §4.2.4#p6, §3#p4, §4.2.4#r17, §4.2.4#p8, §4.2.4#r13]
smoke: []
dependsOn:
  - "My Asset: kartu aset di mobile (Report Damaged, Cancel Report)"
trace:
  §4.6#p1: 1
  §4.6#b3: [3, 4]
  §4.2.2#p3: [9, 16, 17]
  §4.8#r7: 10
  D-DMG-01: [3, 8]
  D-DMG-08: [12, 13]
  TS-DMG-02: 8
  TS-DMG-07: 15
  §Aturan Logika Modul#r55: [10, 16]
  §4.2.4#p6: [21, 23]
  §3#p4: [15, 16]
  §4.2.4#r17: 21
  §4.2.4#p8: [12, 13]
  §4.2.4#r13: [15, 16]
coverage:
  android: manual
---

# Di mobile pemegang melapor rusak dari kartu My Asset lewat bottom sheet dengan kamera, membatalkan laporannya, dan melihat status laporan termasuk laporan scan

## Prerequisites
- Aktor: pelapor umum, yaitu pemegang aset lewat Assignment tanpa role Damaged. Admin B (Total Control) hanya memicu Confirm atas laporan lain.
- Layar awal: layar My Asset di aplikasi mobile.
- Data:
  - DU-058-1: aset `Handphone Samsung Galaxy A54 {runId}`, Group `Head Office`, status global `Assigned`, dipegang aktor, tanpa record Damage.
  - DU-058-2: isian laporan, What happened `Layar ponsel retak setelah terjatuh`, foto kamera `foto-layar-retak`.
  - DU-058-3: aset `Tablet Lenovo Tab M10 {runId}`, Group `Head Office`, tidak dipegang aktor, record Damage laporan aktor lewat scan berstatus `Waiting for Confirmation`.
  - DU-058-4: aset `Speaker Bluetooth JBL {runId}`, Group `Head Office`, dipegang aktor, record Damage laporan aktor berstatus `Waiting for Confirmation`.

## Test Steps

### Pemegang melapor rusak dari kartu My Asset lewat bottom sheet
1. Verifikasi aksi `[Report Damaged]` tersedia pada kartu aset `Handphone Samsung Galaxy A54 {runId}`
2. Klik `[Report Damaged]` pada kartu aset `Handphone Samsung Galaxy A54 {runId}`
3. Verifikasi field `What happened` dan `Damaged Photo` tersedia pada dialog `Report Damaged`
4. Verifikasi kamera langsung terbuka untuk `Damaged Photo`
5. Ambil foto dengan kamera untuk `Damaged Photo` (`foto-layar-retak`)
6. Isi `What happened` dengan `Layar ponsel retak setelah terjatuh`
7. Klik `[Report Damaged]` pada bottom sheet
8. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil
9. Verifikasi status laporan `Waiting for Confirmation` tampil pada kartu aset `Handphone Samsung Galaxy A54 {runId}`

### Pelapor membatalkan laporannya
10. Verifikasi aksi `Cancel Report` tersedia pada kartu laporan aset `Handphone Samsung Galaxy A54 {runId}`
11. Klik `Cancel Report` pada kartu laporan aset `Handphone Samsung Galaxy A54 {runId}`
12. Verifikasi dialog `Cancel Report` tampil dengan aset `Handphone Samsung Galaxy A54 {runId}`
13. Verifikasi pertanyaan `Are you sure you want to cancel it?` tampil pada dialog
14. Klik `[Cancel Report]` pada dialog
15. Verifikasi toast `Success, report has been canceled.` tampil
16. Verifikasi status laporan `Canceled` tampil pada kartu aset `Handphone Samsung Galaxy A54 {runId}`

### Status laporan lewat scan tampil untuk aset yang tidak dipegang
17. Verifikasi status laporan `Waiting for Confirmation` tampil untuk aset `Tablet Lenovo Tab M10 {runId}` yang tidak dipegang aktor

### Laporan yang sudah diputuskan admin menampilkan Already Changed
18. Admin B melakukan Confirm atas laporan aset `Speaker Bluetooth JBL {runId}`
19. Klik `Cancel Report` pada kartu laporan aset `Speaker Bluetooth JBL {runId}`
20. Klik `[Cancel Report]` pada dialog
21. Verifikasi dialog `Already Changed` tampil
22. Klik `[Reload]` pada dialog
23. Verifikasi status laporan `Damaged` tampil pada kartu aset `Speaker Bluetooth JBL {runId}`
