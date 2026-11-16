---
id: TC-FA-DAMAGED-E2E-049-return-accept-with-damage-dep-borrow
title: "Report Damaged dari halaman Return Borrow oleh Aktor Borrow berhak Aktor Damaged membuat record Damaged Source Borrow return dari Description dan foto Return; Return aset ber-record Waiting for Confirmation selesai sebagai Returned bermarker Damaged tanpa laporan baru"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r46", "§Aturan Logika Modul#r34", "§Aturan Logika Modul#r41", "§9.2#b7", "§8.1#r7", "EC-DMG-06", "§9.4.4#r4", "T-DMG-01", "§Aturan Logika Modul#r42", "§2#b6", "§3#p2"]
smoke: []
dependsOn:
  - "Borrow: Return (Report Damaged di halaman Return, status Returned bermarker Damaged)"
trace:
  "§Aturan Logika Modul#r46": [19, 20]
  "§Aturan Logika Modul#r34": [29, 32]
  "§Aturan Logika Modul#r41": [9, 29, 42]
  "§9.2#b7": [19, 20]
  "§8.1#r7": [18, 19, 20]
  "EC-DMG-06": [29, 32, 34, 35, 37, 38, 43]
  "§9.4.4#r4": [34]
  "T-DMG-01": [13, 14, 15, 16, 32, 38]
  "§Aturan Logika Modul#r42": [13]
  "§2#b6": [13, 16]
  "§3#p2": [8, 10, 13, 24]
anchor: []
coverage:
  web: automated
---

# Report Damaged dari halaman Return Borrow oleh Aktor Borrow berhak Aktor Damaged membuat record Damaged Source Borrow return dari Description dan foto Return; Return aset ber-record Waiting for Confirmation selesai sebagai Returned bermarker Damaged tanpa laporan baru

## Prerequisites
- Aktor: Aktor Borrow Group `Head Office` yang juga memegang hak Aktor Damaged pada Group aset (Manage asset & TAG dengan Update pada `Head Office`), sehingga Pelapor admin.
- Layar awal: halaman Borrow.
- Data:
  - DU-049-1: aset Name `Printer Brother HL-L2375 {runId}`, Group `Head Office`, tanpa TAG, sedang dipinjam `Hana Pratiwi {runId}` lewat baris Borrow berstatus `Borrowed`, belum punya record Damage.
  - DU-049-2: aset Name `Scanner Fujitsu fi-7160 {runId}`, Group `Head Office`, tanpa TAG, sedang dipinjam `Rudi Hartono {runId}` lewat baris Borrow berstatus `Borrowed`, dengan record `Waiting for Confirmation` Source `Reported by holder` dari laporan pemegang dengan What happened `Roller pemindai macet dan kertas sering tersangkut`.

## Test Steps

### Report Damaged dari halaman Return atas aset tanpa record membuat record Damaged Source Borrow return
1. Buka halaman Borrow
2. Ketik Search `Printer Brother HL-L2375 {runId}`, tekan Enter
3. Klik `Return` pada baris Borrow aset `Printer Brother HL-L2375 {runId}`
4. Klik `Report Damaged` pada halaman Return
5. Isi Description `Casing printer retak setelah terjatuh saat dikembalikan`
6. Pilih foto Return `printer-casing-retak.jpg`
7. Submit form Return
8. Verifikasi dialog `Report Damaged` tidak tampil
9. Verifikasi baris Borrow aset `Printer Brother HL-L2375 {runId}` berstatus `Returned`
10. Verifikasi baris Borrow aset `Printer Brother HL-L2375 {runId}` memuat penanda `Damaged`
11. Buka halaman Assets, tab `Damaged`
12. Ketik Search `Printer Brother HL-L2375 {runId}`, tekan Enter
13. Verifikasi baris aset `Printer Brother HL-L2375 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`, tanpa Confirm
14. Verifikasi kolom Source pada baris itu `Borrow return`
15. Verifikasi kolom Last Holder pada baris itu terisi nama pemegang saat Return, dalam bentuk nama depan dan inisial nama belakang
16. Verifikasi kolom Reported By pada baris itu memuat nama Aktor Borrow yang melakukan Return, dalam bentuk nama depan dan inisial nama belakang
17. Klik nama aset pada baris aset `Printer Brother HL-L2375 {runId}`
18. Verifikasi node `Reported damaged by [Reporter Name]` tampil atas nama Aktor Borrow yang melakukan Return
19. Verifikasi baris detail What happened pada node itu `Casing printer retak setelah terjatuh saat dikembalikan`
20. Verifikasi baris detail Damaged Photo pada node itu memuat foto Return `printer-casing-retak.jpg`
21. Tutup dialog Damage Log

### Status global aset Damaged sejak Return dengan laporan
22. Buka halaman Assets, tab `Assets`
23. Ketik Search `Printer Brother HL-L2375 {runId}`, tekan Enter
24. Verifikasi status global aset `Damaged` pada baris `Printer Brother HL-L2375 {runId}`

### Return atas aset ber-record Waiting for Confirmation selesai tanpa laporan baru
25. Buka halaman Borrow
26. Ketik Search `Scanner Fujitsu fi-7160 {runId}`, tekan Enter
27. Klik `Return` pada baris Borrow aset `Scanner Fujitsu fi-7160 {runId}`
28. Submit form Return
29. Verifikasi baris Borrow aset `Scanner Fujitsu fi-7160 {runId}` berstatus `Returned`
30. Buka halaman Assets, tab `Damaged`
31. Ketik Search `Scanner Fujitsu fi-7160 {runId}`, tekan Enter
32. Verifikasi tepat satu baris aset `Scanner Fujitsu fi-7160 {runId}` tampil di sub-tab `Active` dengan Status `Waiting for Confirmation`
33. Klik nama aset pada baris aset `Scanner Fujitsu fi-7160 {runId}`
34. Verifikasi timeline dialog Damage Log memuat tepat satu node, yaitu `Reported damaged by [Reporter Name]`
35. Verifikasi baris detail What happened pada node itu tetap `Roller pemindai macet dan kertas sering tersangkut`

### Confirm oleh Aktor Damaged menentukan penanda Damaged pada baris Borrow yang sudah Returned
36. Klik `[Confirm]` pada footer dialog Damage Log
37. Verifikasi toast `Success, report has been confirmed.` tampil
38. Verifikasi badge status record pada dialog `Damaged`
39. Tutup dialog Damage Log
40. Buka halaman Borrow
41. Ketik Search `Scanner Fujitsu fi-7160 {runId}`, tekan Enter
42. Verifikasi baris Borrow aset `Scanner Fujitsu fi-7160 {runId}` tetap berstatus `Returned`
43. Verifikasi baris Borrow aset `Scanner Fujitsu fi-7160 {runId}` memuat penanda `Damaged`
