---
id: TC-FA-DAMAGED-E2E-011-mark-as-repaired
title: "Mark as Repaired atas record Damaged aset tanpa TAG menyelesaikan record sebagai Repaired di History dengan node Marked as repaired by"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, T-DMG-02, D-DMG-02, §4.2.4#p2, §4.4#r7, TS-DMG-05, S-DMG-01, S-DMG-04, S-DMG-05, §8.1#r12, §Aturan Logika Modul#r54, §Aturan Logika Modul#r55, §Aturan Logika Modul#r85, §Aturan Logika Modul#r18, EC-DMG-31, §9.6#r5, §3#p6, F-DMG-05, FLD-DMG-04, FLD-DMG-05, §4.2.1#b2, EB-FB-1@mark-as-repaired, EB-FRM-1@mark-as-repaired]
smoke: [EB-FB-1@mark-as-repaired, EB-FRM-1@mark-as-repaired]
dependsOn: []
trace:
  T-DMG-01: [3, 5, 36, 42]
  T-DMG-02: [19, 21]
  D-DMG-02: [7, 14]
  §4.2.4#p2: [7, 8]
  §4.4#r7: [7, 13]
  TS-DMG-05: 13
  S-DMG-01: 16
  S-DMG-04: [30, 32, 33]
  S-DMG-05: [38, 39, 44, 45]
  §8.1#r12: [24, 25, 26]
  §Aturan Logika Modul#r54: 5
  §Aturan Logika Modul#r55: [15, 19, 23]
  §Aturan Logika Modul#r85: [19, 21]
  §Aturan Logika Modul#r18: 19
  EC-DMG-31: 9
  §9.6#r5: [13, 19]
  §3#p6: 19
  F-DMG-05: [15, 23]
  FLD-DMG-04: 26
  FLD-DMG-05: 25
  §4.2.1#b2: 16
  EB-FB-1@mark-as-repaired: 13
  EB-FRM-1@mark-as-repaired: [20, 24]
anchor: []
coverage:
  web: automated
---

# Mark as Repaired atas record Damaged aset tanpa TAG menyelesaikan record sebagai Repaired di History dengan node Marked as repaired by

## Prerequisites
- Aktor: Total Control (DU-011-6).
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-011-1: Damage record aset `Projector Epson EB-X06 {runId}` tanpa TAG di Group `Head Office`, status `Damaged`, Source `Manual`, dilaporkan DU-011-6 sebagai Pelapor admin dengan What happened `Lampu proyektor mati dan gambar tidak muncul`.
  - DU-011-3: Damage record aset `Camera Canon EOS {runId}` di Group `Head Office`, status `Damaged` dengan penanda `Missing`, Source `Manual`, dilaporkan DU-011-6.
  - DU-011-4: Damage record aset `Printer HP LaserJet M404 {runId}` di Group `Head Office`, status `Reported Disposal`, Source `Stock opname`, dilaporkan DU-011-6.
  - DU-011-5: Damage record aset `Monitor Dell P2422H {runId}` di Group `Head Office`, status `In Disposal Process`, Source `Manual`, dilaporkan DU-011-6.
  - DU-011-6: User `Agus Pratama {runId}`, role Total Control; cakupan: seluruh client.
- Kondisi: After photo required bernilai `OFF`.

## Test Steps

### Mark as Repaired ditawarkan pada record Damaged dan dialognya tidak meminta Scan TAG
1. Catat jumlah pada badge tab `Damaged` sebagai jumlah awal
2. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
3. Verifikasi baris aset `Projector Epson EB-X06 {runId}` tampil di tabel dengan status `Damaged`
4. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
5. Verifikasi item `Mark as Repaired` tampil pada menu baris
6. Klik `Mark as Repaired`
7. Verifikasi dialog `Mark as Repaired` terbuka untuk aset `Projector Epson EB-X06 {runId}`
8. Verifikasi header dialog menampilkan badge status record `Damaged`
9. Verifikasi dialog tidak memuat field Scan TAG

### Mark as Repaired menyelesaikan record sebagai Repaired
10. Isi Repair note `Lampu proyektor diganti dan unit sudah diuji menyala normal`
11. Unggah After photo `proyektor-setelah-diperbaiki.jpg`
12. Klik `[Mark as Repaired]` pada dialog `Mark as Repaired`
13. Verifikasi toast `Success, [Asset Name] has been marked as repaired.` tampil dengan `[Asset Name]` berisi nama aset `Projector Epson EB-X06 {runId}`
14. Verifikasi dialog `Mark as Repaired` tidak lagi tampil
15. Verifikasi sub-tab Active menampilkan `No results found` untuk Search `Projector Epson EB-X06 {runId}`
16. Verifikasi badge tab `Damaged` berkurang satu dari jumlah awal

### Record Repaired tampil di History dengan node Marked as repaired by
17. Klik sub-tab `History`
18. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
19. Verifikasi baris aset `Projector Epson EB-X06 {runId}` tampil di tabel History dengan status `Repaired`
20. Verifikasi History memuat satu baris untuk Search `Projector Epson EB-X06 {runId}`
21. Verifikasi kolom Resolved By memuat nama aktor yang sedang masuk
22. Klik nama aset `Projector Epson EB-X06 {runId}` pada kolom Name
23. Verifikasi badge status record pada dialog `Damage Log` `Repaired`
24. Verifikasi timeline memuat tepat satu node `Marked as repaired by` dengan aktor yang sedang masuk sebagai pelaku
25. Verifikasi node `Marked as repaired by` memuat baris detail Repair note `Lampu proyektor diganti dan unit sudah diuji menyala normal`
26. Verifikasi node `Marked as repaired by` memuat baris detail After photo yang menampilkan foto yang diunggah
27. Klik `✕` pada dialog `Damage Log`

### Aksi baris record berpenanda Missing dan record dalam proses Disposal
28. Klik sub-tab `Active`
29. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
30. Verifikasi baris aset `Camera Canon EOS {runId}` tampil dengan status `Damaged` dan penanda `Missing`
31. Klik `⋯` pada baris `Camera Canon EOS {runId}`
32. Verifikasi item `Damage Log` tampil pada menu baris
33. Verifikasi item `Mark as Repaired`, `Report Disposal`, dan `Report Missing` tidak tampil pada menu baris
34. Tekan Esc untuk menutup menu baris
35. Ganti isi kotak search dengan `Printer HP LaserJet M404 {runId}`, tekan Enter
36. Verifikasi baris aset `Printer HP LaserJet M404 {runId}` tampil dengan status `Reported Disposal`
37. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
38. Verifikasi item `Cancel Disposal Report` tampil pada menu baris
39. Verifikasi item `Mark as Repaired` tidak tampil pada menu baris
40. Tekan Esc untuk menutup menu baris
41. Ganti isi kotak search dengan `Monitor Dell P2422H {runId}`, tekan Enter
42. Verifikasi baris aset `Monitor Dell P2422H {runId}` tampil dengan status `In Disposal Process`
43. Klik `⋯` pada baris `Monitor Dell P2422H {runId}`
44. Verifikasi item `Damage Log` tampil pada menu baris
45. Verifikasi item `Mark as Repaired` tidak tampil pada menu baris
