---
id: TC-FA-DAMAGED-E2E-059-report-tag-saat-mark-as-repaired-dep-tag
title: "Tautan I Can't Scan the TAG pada Mark as Repaired membuka Report TAG; setelah tersimpan badge TAG Reported tampil, Submit berlanjut, dan node mencatat Manual identification"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: [FI-DMG-09, FI-DMG-10, §9.4.2#r13, §9.4.4#r22, §9.2#b16, §8.1#r12, D-DMG-02, §4.1#r9, §8.2#b3]
smoke: []
dependsOn:
  - "Tag: dialog Report TAG (identifikasi manual)"
trace:
  FI-DMG-09: 5
  FI-DMG-10: [7, 8, 11]
  §9.4.2#r13: [7, 17]
  §9.4.4#r22: [14, 17]
  §9.2#b16: [5, 7, 17]
  §8.1#r12: [16, 17]
  D-DMG-02: 3
  §4.1#r9: 5
  §8.2#b3: 20
coverage:
  web: automated
---

# Tautan I Can't Scan the TAG pada Mark as Repaired membuka Report TAG; setelah tersimpan badge TAG Reported tampil, Submit berlanjut, dan node mencatat Manual identification

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-059-1: aset ber-TAG `Kamera Sony ZV-E10 {runId}`, Group `Head Office`, TAG `RFID` yang tidak dapat dipindai, status global `Damaged`, sudah punya record Damage berjalan berstatus `Damaged`.
  - DU-059-2: Repair note `Antena RFID diganti dan diuji ulang`; After photo tidak diisi.
- Kondisi: After photo required bernilai `OFF`.

## Test Steps

### Tautan I Can't Scan the TAG membuka Report TAG dan Submit berlanjut
1. Ketik Search `Kamera Sony ZV-E10 {runId}`, tekan Enter
2. Klik aksi `Mark as Repaired` pada baris `Kamera Sony ZV-E10 {runId}`
3. Verifikasi dialog `Mark as Repaired` tampil
4. Klik tautan `I Can't Scan the TAG` pada field `Scan TAG`
5. Verifikasi dialog Report TAG varian identifikasi manual tampil
6. Simpan dialog Report TAG varian identifikasi manual
7. Verifikasi badge `TAG Reported` tampil pada field `Scan TAG`
8. Verifikasi tombol `[Scan TAG]` tetap aktif
9. Isi `Repair note` dengan `Antena RFID diganti dan diuji ulang`
10. Klik `[Mark as Repaired]` pada footer dialog
11. Verifikasi dialog `Mark as Repaired` tertutup tanpa pesan `Scan TAG must not be empty`

### Node Damage Log mencatat Manual identification
12. Buka sub-tab `History`
13. Ketik Search `Kamera Sony ZV-E10 {runId}`, tekan Enter
14. Verifikasi baris `Kamera Sony ZV-E10 {runId}` tampil dengan Status `Repaired`
15. Klik nama aset `Kamera Sony ZV-E10 {runId}` untuk membuka dialog Damage Log
16. Verifikasi node `Marked as repaired by` tampil
17. Verifikasi `Manual identification` tampil pada node `Marked as repaired by`
18. Klik `✕` pada dialog Damage Log

### TAG Log mencatat Report TAG
19. Buka TAG Log aset `Kamera Sony ZV-E10 {runId}`
20. Verifikasi TAG Log memuat satu entri dari Report TAG
