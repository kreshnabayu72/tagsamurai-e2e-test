---
id: TC-FA-DAMAGED-E2E-025-plan-disposal-none
title: "Pada level Feature Suite Disposal None, Report Disposal, Bulk Report Disposal, dan Cancel Disposal Report tampil Disabled dengan tooltip Upgrade to unlock"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [EC-DMG-36, §9.4.4#r28, §9.10#p1, §9.4.1#r2, T-DMG-01]
smoke: []
dependsOn: []
trace:
  EC-DMG-36: [6, 8, 10, 11, 12, 16, 18, 24, 26, 28]
  §9.4.4#r28: [11, 12, 28]
  §9.10#p1: [6, 16, 24, 33, 37, 42, 46, 50, 51, 53]
  §9.4.1#r2: [6, 8, 18, 24, 26]
  T-DMG-01: [4, 16, 22, 33, 37, 42, 46]
anchor: []
coverage:
  web: automated
---

# Pada level Feature Suite Disposal None, Report Disposal, Bulk Report Disposal, dan Cancel Disposal Report tampil Disabled dengan tooltip Upgrade to unlock

## Prerequisites
- Aktor: Total Control pada entitas level None (DU-025-4), entitas level Full pada plan Growth (DU-025-5), entitas level Full pada plan Professional (DU-025-6), dan entitas plan Starter (DU-025-10); spec ini memakai entitas khusus yang tidak dipakai spec lain.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-025-1: Entitas `Client None {runId}` dengan level Feature Suite Disposal `None`.
  - DU-025-2: Entitas `Client Growth {runId}` dengan plan Growth dan level Feature Suite Disposal `Full`.
  - DU-025-3: Entitas `Client Full {runId}` dengan plan Professional dan level Feature Suite Disposal `Full`.
  - DU-025-4: User `Rina Wijaya {runId}`, role Total Control pada entitas `Client None {runId}`; cakupan: seluruh entitas itu.
  - DU-025-5: User `Agus Pratama {runId}`, role Total Control pada entitas `Client Growth {runId}`; cakupan: seluruh entitas itu.
  - DU-025-6: User `Dewi Anggraeni {runId}`, role Total Control pada entitas `Client Full {runId}`; cakupan: seluruh entitas itu.
  - DU-025-7: Pada setiap entitas: Damage record aset `Projector Epson EB-X06 {runId}` di Group `Head Office {runId}`, status `Damaged`, Source `Manual`, dilaporkan aktor entitas itu.
  - DU-025-8: Pada setiap entitas: Damage record aset `Printer HP LaserJet M404 {runId}` di Group `Head Office {runId}`, status `Reported Disposal`, Source `Stock opname`, dilaporkan aktor entitas itu.
  - DU-025-9: Entitas `Client Starter {runId}` dengan plan Starter.
  - DU-025-10: User `Budi Santoso {runId}`, role Total Control pada entitas `Client Starter {runId}`; cakupan: seluruh entitas itu.

## Test Steps

### Level None mengunci Report Disposal, Bulk Report Disposal, dan Cancel Disposal Report
1. Masuk sebagai Rina Wijaya {runId} pada entitas `Client None {runId}`
2. Klik tab `Damaged`
3. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
4. Verifikasi baris aset `Projector Epson EB-X06 {runId}` tampil di tabel dengan status `Damaged`
5. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
6. Verifikasi item `Report Disposal` tampil dalam keadaan Disabled
7. Arahkan kursor ke item `Report Disposal` yang Disabled
8. Verifikasi alasan `Upgrade to unlock` tersampaikan pada item `Report Disposal` yang Disabled
9. Klik item `Report Disposal` yang Disabled
10. Verifikasi item `Report Disposal` tetap tampil dalam keadaan Disabled
11. Verifikasi dialog `D-DISP-13` tidak tampil
12. Verifikasi baris aset `Projector Epson EB-X06 {runId}` tetap berstatus `Damaged`
13. Tekan Esc untuk menutup menu baris
14. Centang baris `Projector Epson EB-X06 {runId}`
15. Klik `Bulk Action`
16. Verifikasi item `Report Disposal` tampil dalam keadaan Disabled pada menu `Bulk Action`
17. Arahkan kursor ke item `Report Disposal` yang Disabled
18. Verifikasi alasan `Upgrade to unlock` tersampaikan pada item `Report Disposal` di menu `Bulk Action`
19. Tekan Esc untuk menutup menu `Bulk Action`
20. Klik ikon `×` pada bar bulk
21. Ganti isi kotak search dengan `Printer HP LaserJet M404 {runId}`, tekan Enter
22. Verifikasi baris aset `Printer HP LaserJet M404 {runId}` tampil di tabel dengan status `Reported Disposal`
23. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
24. Verifikasi item `Cancel Disposal Report` tampil dalam keadaan Disabled
25. Arahkan kursor ke item `Cancel Disposal Report` yang Disabled
26. Verifikasi alasan `Upgrade to unlock` tersampaikan pada item `Cancel Disposal Report` yang Disabled
27. Klik item `Cancel Disposal Report` yang Disabled
28. Verifikasi baris aset `Printer HP LaserJet M404 {runId}` tetap berstatus `Reported Disposal`

### Level Full pada plan Growth membuka aksi Disposal
29. Masuk sebagai Agus Pratama {runId} pada entitas `Client Growth {runId}`
30. Klik tab `Damaged`
31. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
32. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
33. Verifikasi item `Report Disposal` tampil dan aktif pada menu baris
34. Tekan Esc untuk menutup menu baris
35. Ganti isi kotak search dengan `Printer HP LaserJet M404 {runId}`, tekan Enter
36. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
37. Verifikasi item `Cancel Disposal Report` tampil dan aktif pada menu baris

### Level Full pada plan Professional membuka aksi Disposal
38. Masuk sebagai Dewi Anggraeni {runId} pada entitas `Client Full {runId}`
39. Klik tab `Damaged`
40. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
41. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
42. Verifikasi item `Report Disposal` tampil dan aktif pada menu baris
43. Tekan Esc untuk menutup menu baris
44. Ganti isi kotak search dengan `Printer HP LaserJet M404 {runId}`, tekan Enter
45. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
46. Verifikasi item `Cancel Disposal Report` tampil dan aktif pada menu baris

### Plan Starter membuka tipe TAG QR dan mengunci tipe TAG RFID
47. Masuk sebagai Budi Santoso {runId} pada entitas `Client Starter {runId}`
48. Klik tab `Damaged`
49. Klik `Search by Scan`
50. Verifikasi pilihan `QR` tampil dan aktif pada overlay `Search by Scan`
51. Verifikasi pilihan `RFID` tampil dalam keadaan terkunci pada overlay `Search by Scan`
52. Arahkan kursor ke pilihan `RFID` yang terkunci
53. Verifikasi alasan `Upgrade to unlock` tersampaikan pada pilihan `RFID` yang terkunci
54. Tekan Esc untuk menutup overlay `Search by Scan`
