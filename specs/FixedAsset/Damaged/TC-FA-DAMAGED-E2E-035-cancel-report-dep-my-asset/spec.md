---
id: TC-FA-DAMAGED-E2E-035-cancel-report-dep-my-asset
title: "Pelapor membatalkan laporannya dari My Asset lewat D-DMG-08: record Canceled di History dengan node Report canceled by, dan laporan yang sudah diputuskan admin menampilkan Already Changed"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-08, §4.2.4#p7, §4.2.4#r12, TS-DMG-07, §Aturan Logika Modul#r51, §Aturan Logika Modul#r23, §Aturan Logika Modul#r32, §Aturan Logika Modul#r35, §8.1#r9, §9.7#r7, §4.8#r7, §2.1#r5, §4.2.4#p5, EC-DMG-07, §9.4.4#r16, §9.6#r4, F-DMG-04, T-DMG-02, EB-FB-1@cancel-report]
smoke: [EB-FB-1@cancel-report]
dependsOn:
  - "My Asset: status laporan dan Cancel Report"
trace:
  D-DMG-08: [3, 5]
  §4.2.4#p7: [3, 4, 5]
  §4.2.4#r12: [3, 7]
  TS-DMG-07: 7
  §Aturan Logika Modul#r51: [1, 8]
  §Aturan Logika Modul#r23: [8, 23]
  §Aturan Logika Modul#r32: 19
  §Aturan Logika Modul#r35: [1, 37]
  §8.1#r9: 25
  §9.7#r7: [19, 23]
  §4.8#r7: [1, 30, 32, 34, 36]
  §2.1#r5: 1
  §4.2.4#p5: [12, 13, 15]
  EC-DMG-07: [12, 15]
  §9.4.4#r16: 12
  §9.6#r4: 7
  F-DMG-04: [7, 8]
  T-DMG-02: 23
  EB-FB-1@cancel-report: 7
anchor: [29, 31, 33, 35]
coverage:
  web: automated
---

# Pelapor membatalkan laporannya dari My Asset lewat D-DMG-08: record Canceled di History dengan node Report canceled by, dan laporan yang sudah diputuskan admin menampilkan Already Changed

## Prerequisites
- Aktor: pelapor umum, yaitu pemegang aset lewat Assignment tanpa role Damaged. Admin B (Total Control) memicu Confirm atas laporan lain. Total Control membaca hasil di Asset List dan tab Damaged.
- Layar awal: halaman My Asset.
- Data:
  - DU-035-1: aset `Kamera Canon EOS R10 {runId} A`, Group `Head Office`, dipegang aktor lewat Assignment, status global `Damaged`, record Damage berstatus `Waiting for Confirmation` yang dilaporkan aktor.
  - DU-035-2: aset `Kamera Canon EOS R10 {runId} B`, Group `Head Office`, dipegang aktor lewat Assignment, status global `Damaged`, record Damage berstatus `Waiting for Confirmation` yang dilaporkan aktor.
  - DU-035-3: aset `Proyektor BenQ MH733 {runId} Ditolak`, Group `Head Office`, dipegang aktor lewat Assignment, status global `Assigned`, record Damage berstatus `Rejected` yang dilaporkan aktor.
  - DU-035-4: aset `Speaker JBL Eon {runId} Selesai`, Group `Head Office`, dipegang aktor lewat Assignment, status global `Assigned`, record Damage berstatus `Repaired` yang dilaporkan aktor.
  - DU-035-5: aset `Mikrofon Shure SM58 {runId} Dilepas`, Group `Head Office`, pernah dipegang aktor lewat Assignment dan sekarang tidak lagi dipegangnya, status global `Damaged`, record Damage berstatus `Waiting for Confirmation` yang dilaporkan aktor.

## Test Steps

### Pelapor membatalkan laporan lewat dialog Cancel Report
1. Verifikasi aksi `Cancel Report` tersedia pada kartu laporan aset `Kamera Canon EOS R10 {runId} A`
2. Klik `Cancel Report` pada kartu laporan aset `Kamera Canon EOS R10 {runId} A`
3. Verifikasi dialog `Cancel Report` tampil dengan aset `Kamera Canon EOS R10 {runId} A`
4. Verifikasi pertanyaan `Are you sure you want to cancel it?` tampil pada dialog
5. Verifikasi tombol `[Go Back]` dan `[Cancel Report]` tampil pada dialog
6. Klik `[Cancel Report]` pada dialog
7. Verifikasi toast `Success, report has been canceled.` tampil
8. Verifikasi status laporan `Canceled` tampil pada kartu aset `Kamera Canon EOS R10 {runId} A`

### Laporan yang sudah diputuskan admin menampilkan Already Changed
9. Admin B melakukan Confirm atas laporan aset `Kamera Canon EOS R10 {runId} B`
10. Klik `Cancel Report` pada kartu laporan aset `Kamera Canon EOS R10 {runId} B`
11. Klik `[Cancel Report]` pada dialog
12. Verifikasi dialog `Already Changed` tampil
13. Verifikasi pesan `This record was changed by [User Name]. Reload to see the latest status.` tampil dengan [User Name] berisi nama Admin B
14. Klik `[Reload]` pada dialog
15. Verifikasi status laporan `Damaged` tampil pada kartu aset `Kamera Canon EOS R10 {runId} B`

### Hasil pembatalan dibaca Total Control
16. Masuk sebagai Total Control
17. Buka tab `Assets` pada halaman Assets
18. Ketik Search `Kamera Canon EOS R10 {runId} A`, tekan Enter
19. Verifikasi status global aset `Assigned` pada baris `Kamera Canon EOS R10 {runId} A`
20. Buka tab `Damaged` pada halaman Assets
21. Buka sub-tab `History`
22. Ketik Search `Kamera Canon EOS R10 {runId} A`, tekan Enter
23. Verifikasi baris `Kamera Canon EOS R10 {runId} A` tampil dengan Status `Canceled`
24. Klik nama aset `Kamera Canon EOS R10 {runId} A` untuk membuka dialog Damage Log
25. Verifikasi node `Report canceled by` tampil
26. Klik `✕` pada dialog Damage Log

### Cancel Report tidak ditawarkan pada laporan yang bukan Waiting for Confirmation
27. Masuk sebagai pelapor umum
28. Buka halaman My Asset
29. Verifikasi status laporan `Canceled` tampil pada kartu aset `Kamera Canon EOS R10 {runId} A`
30. Verifikasi aksi `Cancel Report` tidak tampil (Hidden) pada kartu laporan aset `Kamera Canon EOS R10 {runId} A`
31. Verifikasi status laporan `Damaged` tampil pada kartu aset `Kamera Canon EOS R10 {runId} B`
32. Verifikasi aksi `Cancel Report` tidak tampil (Hidden) pada kartu laporan aset `Kamera Canon EOS R10 {runId} B`
33. Verifikasi status laporan `Rejected` tampil pada kartu aset `Proyektor BenQ MH733 {runId} Ditolak`
34. Verifikasi aksi `Cancel Report` tidak tampil (Hidden) pada kartu laporan aset `Proyektor BenQ MH733 {runId} Ditolak`
35. Verifikasi status laporan `Repaired` tampil pada kartu aset `Speaker JBL Eon {runId} Selesai`
36. Verifikasi aksi `Cancel Report` tidak tampil (Hidden) pada kartu laporan aset `Speaker JBL Eon {runId} Selesai`

### Cancel Report tetap tersedia setelah aset tidak lagi dipegang
37. Verifikasi aksi `Cancel Report` tersedia pada kartu laporan aset `Mikrofon Shure SM58 {runId} Dilepas` yang tidak lagi dipegang aktor
