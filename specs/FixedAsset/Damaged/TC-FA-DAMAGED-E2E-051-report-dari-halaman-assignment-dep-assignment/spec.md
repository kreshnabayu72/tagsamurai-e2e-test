---
id: TC-FA-DAMAGED-E2E-051-report-dari-halaman-assignment-dep-assignment
title: "Aktor Assignment melapor rusak dari halaman transaksi Assignment: record langsung Damaged Source Assigned asset dan baris Assignment tidak berubah"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#b2", "§2#b6", "§4.8#r3", "§Aturan Logika Modul#r42", "§Aturan Logika Modul#r37", "§9.4.2#r3", "§4.2.3#p1", "T-DMG-01"]
smoke: []
dependsOn:
  - "Assignment: Detail Assignment (tombol Report Damaged)"
trace:
  "§2.1#b2": [8, 9, 11, 12, 18, 23, 24]
  "§2#b6": [18, 20]
  "§4.8#r3": [4]
  "§Aturan Logika Modul#r42": [18]
  "§Aturan Logika Modul#r37": [14, 15]
  "§9.4.2#r3": [14, 15]
  "§4.2.3#p1": [4]
  "T-DMG-01": [18, 19, 22, 23, 24]
anchor: []
coverage:
  web: automated
---

# Aktor Assignment melapor rusak dari halaman transaksi Assignment: record langsung Damaged Source Assigned asset dan baris Assignment tidak berubah

## Prerequisites
- Aktor: Aktor Assignment Group `Head Office`, tanpa hak Update Manage asset & TAG pada Group aset, yang juga memegang role Read Only.
- Layar awal: halaman Assignment.
- Data:
  - DU-051-1: aset Name `Headset Jabra Evolve2 {runId}`, Group `Head Office`, tanpa TAG, belum punya record Damage, sedang ditugaskan kepada `Maya Lestari {runId}` lewat baris Assignment berstatus `Assigned`.

## Test Steps

### Report Damaged dari Detail Assignment membuat record langsung Damaged
1. Ketik Search `{runId}`, tekan Enter
2. Buka Detail Assignment aset `Headset Jabra Evolve2 {runId}`
3. Klik `Report Damaged` pada Detail Assignment
4. Verifikasi dialog `Report Damaged` tampil
5. Isi What happened `Earcup kiri retak dan bantalan terlepas`
6. Pilih Damaged Photo `headset-earcup-retak.jpg`
7. Klik `[Report Damaged]`
8. Verifikasi toast `Success, asset has been reported damaged.` tampil

### Damage Log terbuka dari penanda di halaman transaksi
9. Verifikasi penanda `Damage reported` tampil di Detail Assignment
10. Klik penanda `Damage reported`
11. Verifikasi dialog `Damage Log` tampil
12. Verifikasi node `Reported damaged by [Reporter Name]` memuat baris detail What happened `Earcup kiri retak dan bantalan terlepas`
13. Tutup dialog Damage Log

### Baris Assignment tidak berubah oleh laporan
14. Verifikasi baris Assignment aset `Headset Jabra Evolve2 {runId}` tetap berstatus `Assigned`
15. Verifikasi pemegang pada baris itu tetap `Maya Lestari {runId}`

### Record langsung Damaged di tab Damaged dan tanpa aksi tulis bagi Aktor Assignment
16. Buka halaman Assets, tab `Damaged`
17. Ketik Search `{runId}`, tekan Enter
18. Verifikasi baris aset `Headset Jabra Evolve2 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`, tanpa Confirm
19. Verifikasi kolom Source pada baris itu `Assigned asset`
20. Verifikasi kolom Reported By pada baris itu memuat nama Aktor Assignment yang melapor, dalam bentuk nama depan dan inisial nama belakang
21. Klik `⋯` pada baris aset `Headset Jabra Evolve2 {runId}`
22. Verifikasi aksi `Damage Log` tampil pada menu baris
23. Verifikasi aksi `Mark as Repaired` tidak tampil pada menu baris
24. Verifikasi aksi `Report Missing` tidak tampil pada menu baris
