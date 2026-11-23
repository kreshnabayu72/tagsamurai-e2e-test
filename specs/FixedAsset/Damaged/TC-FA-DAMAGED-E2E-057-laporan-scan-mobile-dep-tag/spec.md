---
id: TC-FA-DAMAGED-E2E-057-laporan-scan-mobile-dep-tag
title: "Hasil scan TAG di mobile menampilkan Report Damaged bagi pengguna aktif; aset ber-record berjalan atau Disposed/Missing menampilkan keterangan tanpa aksi"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [§4.6#p1, §4.6#b1, §4.6#b2, F-DMG-08, §Aturan Logika Modul#r30, §Aturan Logika Modul#r15, §4.2.3#b2, EC-DMG-04, §4.8#r4, §2.1#r3, §2#b7, D-DMG-01, TS-DMG-02, §10#r5, §4.2.3#p1]
smoke: []
dependsOn:
  - "Tag: hasil scan TAG di mobile"
trace:
  §4.6#p1: 19
  §4.6#b1: [10, 11]
  §4.6#b2: [13, 14, 16, 17]
  F-DMG-08: [2, 10, 13, 16]
  §Aturan Logika Modul#r30: 9
  §Aturan Logika Modul#r15: [10, 11]
  §4.2.3#b2: [13, 14, 16, 17]
  EC-DMG-04: [13, 14, 16, 17]
  §4.8#r4: 2
  §2.1#r3: 2
  §2#b7: [2, 7]
  D-DMG-01: [7, 10]
  TS-DMG-02: 7
  §10#r5: 19
  §4.2.3#p1: 7
anchor: [18]
coverage:
  android: manual
---

# Hasil scan TAG di mobile menampilkan Report Damaged bagi pengguna aktif; aset ber-record berjalan atau Disposed/Missing menampilkan keterangan tanpa aksi

## Prerequisites
- Aktor: pengguna aktif tanpa role Damaged (pelapor umum).
- Layar awal: layar pindai TAG di aplikasi mobile.
- Data:
  - DU-057-1: aset ber-TAG `Proyektor BenQ MW535 {runId}`, Group `Head Office`, status global `Normal`, tanpa record Damage.
  - DU-057-2: aset ber-TAG `Printer Brother HL-L2375DW {runId}`, Group `Head Office`, status `Disposed`.
  - DU-057-3: aset ber-TAG `Mesin Cuci Industri {runId}`, Group `Head Office`, status `Missing`, tanpa record Damage.
  - DU-057-4: isian laporan, What happened `Lensa proyektor berembun dan gambar buram`, foto `lensa-berembun.jpg`.

## Test Steps

### Hasil scan aset layak menampilkan Report Damaged dan laporan terkirim
1. Pindai TAG aset `Proyektor BenQ MW535 {runId}`
2. Verifikasi aksi `[Report Damaged]` tampil pada hasil scan
3. Klik `[Report Damaged]` pada hasil scan
4. Isi `What happened` dengan `Lensa proyektor berembun dan gambar buram`
5. Unggah foto `lensa-berembun.jpg` pada `Damaged Photo`
6. Klik `[Report Damaged]` pada footer dialog
7. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil

### Aset yang sudah dilaporkan menampilkan keterangan tanpa aksi dan status global tidak berubah
8. Pindai TAG aset `Proyektor BenQ MW535 {runId}`
9. Verifikasi status global aset `Normal` tetap tampil pada hasil scan
10. Verifikasi keterangan `Already reported damaged` tampil pada hasil scan
11. Verifikasi aksi `[Report Damaged]` tidak tampil (Hidden) pada hasil scan

### Aset Disposed dan Missing menampilkan keterangan tanpa aksi
12. Pindai TAG aset `Printer Brother HL-L2375DW {runId}`
13. Verifikasi keterangan `Can't be reported damaged` tampil pada hasil scan
14. Verifikasi aksi `[Report Damaged]` tidak tampil (Hidden) pada hasil scan
15. Pindai TAG aset `Mesin Cuci Industri {runId}`
16. Verifikasi keterangan `Can't be reported damaged` tampil pada hasil scan
17. Verifikasi aksi `[Report Damaged]` tidak tampil (Hidden) pada hasil scan

### Halaman Damaged tidak tersedia di mobile
18. Verifikasi menu `My Asset` tampil pada navigasi aplikasi
19. Verifikasi halaman `Damaged` dengan sub-tab `Active` dan `History` tidak tersedia di aplikasi
