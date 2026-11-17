---
id: TC-FA-DAMAGED-E2E-053-transfer-dep-transfer
title: "Aset Damaged dapat di-Transfer dengan peringatan, record aktif ikut Group tujuan saat Received tanpa node, dan Report Damaged saat Receive membuat record Source Transfer receive"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["EC-DMG-29", "EC-DMG-18", "§9.4.4#r12", "§9.4.4#r8", "§9.7#r17", "§8.3#r6", "§8.3#r2", "§2.1#b2", "§2#b6", "§4.8#r3", "§Aturan Logika Modul#r34", "T-DMG-01"]
smoke: []
dependsOn:
  - "Transfer: form Transfer dan Receive (Report Damaged saat Receive)"
trace:
  "EC-DMG-29": [19, 20, 22]
  "EC-DMG-18": [3, 14]
  "§9.4.4#r12": [19, 20, 22]
  "§9.4.4#r8": [3]
  "§9.7#r17": [19, 25]
  "§8.3#r6": [22]
  "§8.3#r2": [27, 29, 30, 31]
  "§2.1#b2": [26, 29]
  "§2#b6": [26, 29]
  "§4.8#r3": [26]
  "§Aturan Logika Modul#r34": [15, 24]
  "T-DMG-01": [18, 19, 20, 26, 27]
anchor: []
coverage:
  web: automated
---

# Aset Damaged dapat di-Transfer dengan peringatan, record aktif ikut Group tujuan saat Received tanpa node, dan Report Damaged saat Receive membuat record Source Transfer receive

## Prerequisites
- Aktor: Aktor Transfer pada Group `Head Office` dan Group `Branch Surabaya`, tanpa hak Update Manage asset & TAG pada Group aset, yang juga memegang role Read Only.
- Layar awal: halaman Transfer.
- Data:
  - DU-053-1: aset Name `Printer Epson L3250 {runId}`, Group `Head Office`, tanpa TAG, dengan record `Damaged` Source `Manual` dan What happened `Tinta merembes dan head printer macet`.
  - DU-053-2: aset Name `Scanner Canon DR-C225 {runId}`, Group `Head Office`, tanpa TAG, belum punya record Damage.
  - DU-053-3: aset Name `Router Cisco RV340 {runId}`, Group `Head Office`, tanpa TAG, dengan record `Waiting for Confirmation` Source `Reported by scan` dari laporan scan dengan What happened `Port LAN tiga mati sejak kemarin`.

## Test Steps

### Transfer aset ber-record Damaged, aset ber-laporan scan, dan aset normal sampai Received
1. Buka form Transfer
2. Pilih aset `Printer Epson L3250 {runId}` pada form Transfer
3. Verifikasi peringatan `This asset is damaged.` tampil untuk aset `Printer Epson L3250 {runId}`
4. Pilih aset `Scanner Canon DR-C225 {runId}` pada form Transfer
5. Pilih aset `Router Cisco RV340 {runId}` pada form Transfer
6. Pilih Group tujuan `Branch Surabaya`
7. Submit form Transfer
8. Receive aset `Printer Epson L3250 {runId}` di Group tujuan `Branch Surabaya`
9. Receive aset `Router Cisco RV340 {runId}` di Group tujuan `Branch Surabaya`
10. Mulai Receive aset `Scanner Canon DR-C225 {runId}` di Group tujuan `Branch Surabaya`
11. Isi What happened pada form Receive aset `Scanner Canon DR-C225 {runId}` dengan `Casing scanner retak selama pengiriman`
12. Pilih Damaged Photo `scanner-casing-retak.jpg`
13. Selesaikan Receive aset `Scanner Canon DR-C225 {runId}`
14. Verifikasi Transfer aset `Printer Epson L3250 {runId}` berstatus `Received`
15. Verifikasi Transfer aset `Router Cisco RV340 {runId}` berstatus `Received`

### Record aktif ikut Group tujuan tanpa node baru
16. Buka halaman Assets, tab `Damaged`
17. Ketik Search `{runId}`, tekan Enter
18. Verifikasi baris aset `Printer Epson L3250 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`
19. Verifikasi kolom Group pada baris itu `Branch Surabaya`
20. Verifikasi kolom Source pada baris itu tetap `Manual`
21. Klik nama aset pada baris aset `Printer Epson L3250 {runId}`
22. Verifikasi dialog Damage Log memuat tepat satu node `Reported damaged by [Reporter Name]`, tanpa node dari Transfer
23. Tutup dialog Damage Log
24. Verifikasi Status baris aset `Router Cisco RV340 {runId}` tetap `Waiting for Confirmation`
25. Verifikasi kolom Group pada baris aset `Router Cisco RV340 {runId}` `Branch Surabaya`

### Report Damaged saat Receive membuat record langsung Damaged Source Transfer receive
26. Verifikasi baris aset `Scanner Canon DR-C225 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`, tanpa Confirm
27. Verifikasi kolom Source pada baris itu `Transfer receive`
28. Klik nama aset pada baris aset `Scanner Canon DR-C225 {runId}`
29. Verifikasi node `Reported damaged by [Reporter Name]` tampil atas nama Aktor Transfer yang melakukan Receive
30. Verifikasi baris detail What happened pada node itu `Casing scanner retak selama pengiriman`
31. Verifikasi baris detail Damaged Photo pada node itu memuat foto `scanner-casing-retak.jpg`
32. Tutup dialog Damage Log
