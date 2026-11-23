---
id: TC-FA-MISS-E2E-060-penanda-asset-missing-dep-maintenance-routine
title: "Task Maintenance aset dengan record Missing: penanda Asset missing tampil dan Start Maintenance diblokir saat aset dilaporkan Missing, penanda hilang sesudah Mark as Found"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§11#r10", "§9.7#r1", "§9.7#r4"]
smoke: []
dependsOn: ["Maintenance Routine: Task Maintenance (penanda Asset missing, Start Maintenance)", "My Asset: aksi Cancel Report"]
trace:
  "§11#r10": [8, 10, 20, 22, 24, 33, 36, 38, 40, 49, 51]
  "§9.7#r1": [6, 8]
  "§9.7#r4": [17, 20]
anchor: [19, 35, 45, 48]
coverage:
  web: automated
---

# Task Maintenance aset dengan record Missing: penanda Asset missing tampil dan Start Maintenance diblokir saat aset dilaporkan Missing, penanda hilang sesudah Mark as Found

## Prerequisites
- Aktor: Total Control `Rina W`. Aktor lain: pemegang `Joko Santoso {runId}` tanpa hak Aktor Missing.
- Layar awal: Assets.
- Data:
  - DU-060-1: Task Maintenance `Servis Printer {runId}` atas aset `Printer HP LaserJet M404 {runId}` yang belum dimulai.
  - DU-060-2: Asset `Printer HP LaserJet M404 {runId}`, Group `Warehouse`, Asset Status `Normal`, tanpa TAG, tanpa record Missing.
  - DU-060-3: Pengguna `Rina W`, Total Control.
  - DU-060-4: What happened `Printer tidak ada di ruang cetak saat pengecekan`.
  - DU-060-5: Task Maintenance `Servis Scanner {runId}` atas aset `Scanner Zebra DS2208 {runId}` yang belum dimulai.
  - DU-060-6: Asset `Scanner Zebra DS2208 {runId}`, Group `Warehouse`, ditugaskan ke `Joko Santoso {runId}`, dengan record Missing berstatus `Waiting for Confirmation` yang dilaporkan `Joko Santoso {runId}`.
  - DU-060-7: Pengguna `Joko Santoso {runId}`, pemegang tanpa hak Aktor Missing.
  - DU-060-8: Reason `Aset terlihat kembali di gudang`.
  - DU-060-9: Task Maintenance `Servis Proyektor {runId}` atas aset `Proyektor Epson EB-X06 {runId}` yang belum dimulai.
  - DU-060-10: Asset `Proyektor Epson EB-X06 {runId}`, Group `Warehouse`, ditugaskan ke `Joko Santoso {runId}`, dengan record Missing berstatus `Waiting for Confirmation` yang dilaporkan `Joko Santoso {runId}`.
- Kondisi:
  - Akun `Rina W` dan `Joko Santoso {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Report Missing menandai Task Maintenance dan memblokir Start Maintenance
1. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
2. Buka menu `⋯` pada baris `Printer HP LaserJet M404 {runId}`
3. Klik `Report Missing`
4. Isi What happened `Printer tidak ada di ruang cetak saat pengecekan`
5. Klik `[Report Missing]` pada dialog
6. Verifikasi toast `Success, asset has been reported missing.` tampil
7. Buka Task Maintenance `Servis Printer {runId}`
8. Verifikasi penanda `Asset missing` tampil pada Task Maintenance `Servis Printer {runId}`
9. Coba jalankan `Start Maintenance` pada Task Maintenance `Servis Printer {runId}`
10. Verifikasi Task Maintenance `Servis Printer {runId}` belum dimulai

### Mark as Found menghapus penanda Asset missing
11. Buka halaman `Assets`
12. Klik tab `Missing`
13. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
14. Buka menu `⋯` pada baris `Printer HP LaserJet M404 {runId}`
15. Klik `Mark as Found`
16. Klik `[Mark as Found]` pada dialog
17. Verifikasi toast `Success, [Asset Name] is available again.` tampil dengan Asset Name `Printer HP LaserJet M404 {runId}`
18. Buka Task Maintenance `Servis Printer {runId}`
19. Verifikasi Task Maintenance `Servis Printer {runId}` tampil
20. Verifikasi penanda `Asset missing` tidak tampil pada Task Maintenance `Servis Printer {runId}`

### Laporan pemegang Waiting for Confirmation memblokir Start Maintenance dan Reject menghapus penanda
21. Buka Task Maintenance `Servis Scanner {runId}`
22. Verifikasi penanda `Asset missing` tampil pada Task Maintenance `Servis Scanner {runId}`
23. Coba jalankan `Start Maintenance` pada Task Maintenance `Servis Scanner {runId}`
24. Verifikasi Task Maintenance `Servis Scanner {runId}` belum dimulai
25. Buka halaman `Assets`
26. Klik tab `Missing`
27. Ketik Search `Scanner Zebra DS2208 {runId}`, tekan Enter
28. Buka menu `⋯` pada baris `Scanner Zebra DS2208 {runId}`
29. Klik `Review`
30. Klik `[Reject]` pada footer dialog `Missing Log`
31. Isi Reason `Aset terlihat kembali di gudang`
32. Klik `[Reject]` pada dialog `Reject Report`
33. Verifikasi toast `Success, report has been rejected.` tampil
34. Buka Task Maintenance `Servis Scanner {runId}`
35. Verifikasi Task Maintenance `Servis Scanner {runId}` tampil
36. Verifikasi penanda `Asset missing` tidak tampil pada Task Maintenance `Servis Scanner {runId}`
37. Klik `Start Maintenance` pada Task Maintenance `Servis Scanner {runId}`
38. Verifikasi Task Maintenance `Servis Scanner {runId}` sudah dimulai

### Cancel Report pemegang menghapus penanda Asset missing
39. Buka Task Maintenance `Servis Proyektor {runId}`
40. Verifikasi penanda `Asset missing` tampil pada Task Maintenance `Servis Proyektor {runId}`
41. Masuk sebagai `Joko Santoso {runId}`
42. Buka halaman `My Asset`
43. Klik `Cancel Report` pada aset `Proyektor Epson EB-X06 {runId}`
44. Klik `[Cancel Report]` pada dialog
45. Verifikasi toast `Success, report has been canceled.` tampil
46. Masuk sebagai `Rina W`
47. Buka Task Maintenance `Servis Proyektor {runId}`
48. Verifikasi Task Maintenance `Servis Proyektor {runId}` tampil
49. Verifikasi penanda `Asset missing` tidak tampil pada Task Maintenance `Servis Proyektor {runId}`
50. Klik `Start Maintenance` pada Task Maintenance `Servis Proyektor {runId}`
51. Verifikasi Task Maintenance `Servis Proyektor {runId}` sudah dimulai
