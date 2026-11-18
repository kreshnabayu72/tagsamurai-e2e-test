---
id: TC-FA-DAMAGED-E2E-053-transfer-dep-transfer
title: "Aset Damaged dapat di-Transfer dengan peringatan; selama In Transfer Process Mark as Repaired dan Report Disposal Disabled, Report Missing Disabled selama In Transit, dan record tetap di Active; saat Received record aktif ikut Group tujuan tanpa node dan Mark as Repaired aktif lagi; Report Damaged saat Receive membuat record Source Transfer receive"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["EC-DMG-29", "EC-DMG-18", "§9.4.4#r12", "§9.4.4#r8", "§9.7#r17", "§8.3#r6", "§8.3#r2", "§2.1#b2", "§2#b6", "§4.8#r3", "§Aturan Logika Modul#r34", "T-DMG-01", "S-DMG-23", "§9.4.2#r33", "§Aturan Logika Modul#r43"]
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
  "T-DMG-01": [18, 19, 20, 26, 27, 43, 44, 45, 53, 54, 55, 67]
  "S-DMG-23": [43]
  "§9.4.2#r33": [41, 43, 51, 53]
  "§Aturan Logika Modul#r43": [38, 41, 43, 44, 45, 48, 51, 53, 54, 55, 61, 64, 65, 67]
anchor: []
coverage:
  web: automated
---

# Aset Damaged dapat di-Transfer dengan peringatan; selama In Transfer Process Mark as Repaired dan Report Disposal Disabled, Report Missing Disabled selama In Transit, dan record tetap di Active; saat Received record aktif ikut Group tujuan tanpa node dan Mark as Repaired aktif lagi; Report Damaged saat Receive membuat record Source Transfer receive

## Prerequisites
- Aktor: Aktor Transfer pada Group `Head Office` dan Group `Branch Surabaya`, tanpa hak Update Manage asset & TAG pada Group aset, yang juga memegang role Read Only. Untuk kelompok terakhir: Aktor Damaged yang juga Aktor Transfer, role Total Control.
- Layar awal: halaman Transfer.
- Data:
  - DU-053-1: aset Name `Printer Epson L3250 {runId}`, Group `Head Office`, tanpa TAG, dengan record `Damaged` Source `Manual` dan What happened `Tinta merembes dan head printer macet`.
  - DU-053-2: aset Name `Scanner Canon DR-C225 {runId}`, Group `Head Office`, tanpa TAG, belum punya record Damage.
  - DU-053-3: aset Name `Router Cisco RV340 {runId}`, Group `Head Office`, tanpa TAG, dengan record `Waiting for Confirmation` Source `Reported by scan` dari laporan scan dengan What happened `Port LAN tiga mati sejak kemarin`.
  - DU-053-6: aset Name `Plotter HP DesignJet T630 {runId}`, Group `Head Office`, tanpa TAG, Custody `Available`, dengan record `Damaged` Source `Manual` dan What happened `Roller kertas plotter macet dan hasil cetak bergaris`.
  - DU-053-7: aset Name `Proyektor BenQ MW550 {runId}`, Group `Head Office`, tanpa TAG, Custody `Available`, dengan record `Damaged` Source `Manual` dan What happened `Lampu proyektor redup dan kipas berisik`.
- Kondisi:
  - Approval Transfer bernilai `OFF`: Transfer yang di-Submit tidak menunggu persetujuan.

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

### Aksi aset Damaged selama In Transfer Process dan setelah Received
33. Masuk sebagai Total Control
34. Buka form Transfer
35. Pilih aset `Plotter HP DesignJet T630 {runId}` pada form Transfer
36. Pilih Group tujuan `Branch Surabaya`
37. Submit form Transfer
38. Verifikasi Transfer aset `Plotter HP DesignJet T630 {runId}` berstatus `In Transit`
39. Buka halaman Assets, tab `Damaged`
40. Ketik Search `Plotter HP DesignJet T630 {runId}`, tekan Enter
41. Verifikasi baris aset `Plotter HP DesignJet T630 {runId}` tetap tampil di sub-tab `Active` dengan Status `Damaged`
42. Buka menu `⋯` pada baris aset `Plotter HP DesignJet T630 {runId}`
43. Verifikasi aksi `Mark as Repaired` pada menu itu Disabled, dengan alasan `This asset is in transfer.` tersampaikan
44. Verifikasi aksi `Report Disposal` pada menu itu Disabled
45. Verifikasi aksi `Report Missing` pada menu itu Disabled
46. Tutup menu `⋯`
47. Receive aset `Plotter HP DesignJet T630 {runId}` di Group tujuan `Branch Surabaya`
48. Verifikasi Transfer aset `Plotter HP DesignJet T630 {runId}` berstatus `Received`
49. Buka halaman Assets, tab `Damaged`
50. Ketik Search `Plotter HP DesignJet T630 {runId}`, tekan Enter
51. Verifikasi baris aset `Plotter HP DesignJet T630 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`
52. Buka menu `⋯` pada baris aset `Plotter HP DesignJet T630 {runId}`
53. Verifikasi aksi `Mark as Repaired` pada menu itu aktif dan bisa diklik
54. Verifikasi aksi `Report Missing` pada menu itu aktif dan bisa diklik
55. Verifikasi aksi `Report Disposal` pada menu itu aktif dan bisa diklik

### Setelah Returned to Origin record tetap di Group asal dan Mark as Repaired aktif lagi
56. Buka form Transfer
57. Pilih aset `Proyektor BenQ MW550 {runId}` pada form Transfer
58. Pilih Group tujuan `Branch Surabaya`
59. Submit form Transfer
60. Aktor Transfer mengembalikan pemindahan atas aset `Proyektor BenQ MW550 {runId}` ke asal sehingga baris Transfer menjadi `Returned to Origin`
61. Verifikasi Transfer aset `Proyektor BenQ MW550 {runId}` berstatus `Returned to Origin`
62. Buka halaman Assets, tab `Damaged`
63. Ketik Search `Proyektor BenQ MW550 {runId}`, tekan Enter
64. Verifikasi baris aset `Proyektor BenQ MW550 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`
65. Verifikasi kolom Group pada baris aset `Proyektor BenQ MW550 {runId}` `Head Office`
66. Buka menu `⋯` pada baris aset `Proyektor BenQ MW550 {runId}`
67. Verifikasi aksi `Mark as Repaired` pada menu itu aktif dan bisa diklik
