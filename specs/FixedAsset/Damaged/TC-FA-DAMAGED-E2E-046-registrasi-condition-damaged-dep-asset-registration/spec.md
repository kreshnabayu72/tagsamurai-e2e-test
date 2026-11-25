---
id: TC-FA-DAMAGED-E2E-046-registrasi-condition-damaged-dep-asset-registration
title: "Aset yang didaftarkan dengan Condition Damaged mendapat record Damaged Source Registration tanpa Damaged Photo begitu aset Active"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r82", "§Aturan Logika Modul#r83", "§Aturan Logika Modul#r84", "§Aturan Logika Modul#r85", "§Aturan Logika Modul#r86", "§Aturan Logika Modul#r87", "§8.3#r1", "§8.1#r7", "§9.2#b5", "§9.7#r8", "EC-DMG-28", "EC-DMG-32", "§9.4.4#r6", "EC-DMG-31", "T-DMG-01", "T-DMG-02"]
smoke: []
dependsOn: ["Asset Registration: registrasi aset ber-Condition Damaged dan Activate"]
trace:
  "§Aturan Logika Modul#r82": [6]
  "§Aturan Logika Modul#r83": [7]
  "§Aturan Logika Modul#r84": [6]
  "§Aturan Logika Modul#r85": [13]
  "§Aturan Logika Modul#r86": [14]
  "§Aturan Logika Modul#r87": [12]
  "§8.3#r1": [12]
  "§8.1#r7": [12, 13, 14]
  "§9.2#b5": [3, 6]
  "§9.7#r8": [6, 10]
  "EC-DMG-28": [6, 7, 13]
  "EC-DMG-32": [3, 12]
  "§9.4.4#r6": [12]
  "EC-DMG-31": [14]
  "T-DMG-01": [8, 9]
  "T-DMG-02": [22, 23, 24, 25, 26]
anchor: []
coverage:
  web: automated
---

# Aset yang didaftarkan dengan Condition Damaged mendapat record Damaged Source Registration tanpa Damaged Photo begitu aset Active

## Prerequisites
- Aktor: Total Control, yang melakukan Activate atas aset.
- Layar awal: halaman Assets, tab Registration.
- Data:
  - DU-046-1: draft registrasi aset Name `Laptop Lenovo ThinkPad E14 {runId}`, Condition `Damaged`, Damage note `Layar retak dan engsel patah setelah terjatuh saat pemindahan unit`, Group `Head Office`, tanpa TAG, tanpa foto aset, siap di-Activate.
- Kondisi:
  - Approval registrasi aset bernilai `OFF`.

## Test Steps

### Activate aset ber-Condition Damaged membuat record Damaged otomatis
1. Catat jumlah pada badge tab `Damaged`
2. Activate aset `Laptop Lenovo ThinkPad E14 {runId}` dari tab `Registration`
3. Verifikasi dialog `Report Damaged` tidak tampil
4. Klik tab `Damaged`
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi baris aset `Laptop Lenovo ThinkPad E14 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`, tanpa Confirm
7. Verifikasi kolom Source pada baris itu `Registration`
8. Verifikasi kolom Last Holder pada baris itu `—`
9. Verifikasi kolom Reported By pada baris itu memuat nama aktor yang melakukan Activate, dalam bentuk nama depan dan inisial nama belakang
10. Verifikasi badge jumlah tab `Damaged` bertambah satu dari jumlah yang dicatat

### Damage Log record registrasi: node pertama atas nama pelaku Activate, What happened dari Damage note, tanpa Damaged Photo
11. Klik nama aset pada baris itu
12. Verifikasi node pertama `Reported damaged by [Reporter Name]` tampil atas nama aktor yang melakukan Activate
13. Verifikasi baris detail What happened pada node itu `Layar retak dan engsel patah setelah terjatuh saat pemindahan unit`
14. Verifikasi node itu tidak memuat Damaged Photo
15. Tutup dialog Damage Log

### Mark as Repaired atas record registrasi memindahkan baris ke History
16. Klik `⋯` pada baris aset `Laptop Lenovo ThinkPad E14 {runId}`
17. Klik `Mark as Repaired`
18. Isi Repair note `Layar sudah diganti dan unit berfungsi normal`
19. Klik `[Mark as Repaired]`
20. Klik sub-tab `History`
21. Ketik Search `{runId}`, tekan Enter
22. Verifikasi baris aset `Laptop Lenovo ThinkPad E14 {runId}` tampil di sub-tab `History` dengan Status `Repaired`
23. Verifikasi kolom Source pada baris itu `Registration`
24. Verifikasi kolom Last Holder pada baris itu `—`
25. Verifikasi kolom Reported By pada baris itu memuat nama aktor yang melakukan Activate
26. Verifikasi kolom Photo pada baris itu menampilkan avatar inisial, karena record tanpa Damaged Photo dan aset tanpa foto
