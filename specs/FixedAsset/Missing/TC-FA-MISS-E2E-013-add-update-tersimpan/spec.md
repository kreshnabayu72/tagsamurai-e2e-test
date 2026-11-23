---
id: TC-FA-MISS-E2E-013-add-update-tersimpan
title: "Add Update: node Update added by tersimpan, toast, dan Last Updated berubah"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.1#r9", "§9.2#b64", "§4.1a#r30", "§4.4#r8", "§7.3#r9", "§8.1#r10", "§9.6#r5", "§9.7#r9", "§2.1#r5", "§4.8#r5", "§4.1a#r28", "§4.1a#r27", "EB-FRM-1@add-update", "EB-FB-1@add-update"]
smoke: []
dependsOn: []
trace:
  "§9.1#r9": 17
  "§9.2#b64": [7, 17]
  "§4.1a#r30": [10, 12, 15, 38, 43, 46, 49, 55, 59, 63]
  "§4.4#r8": [12, 15, 17]
  "§7.3#r9": 15
  "§8.1#r10": 17
  "§9.6#r5": [26, 28, 29]
  "§9.7#r9": 17
  "§2.1#r5": 10
  "§4.8#r5": 10
  "§4.1a#r28": 20
  "§4.1a#r27": [21, 33]
  "EB-FRM-1@add-update": 18
  "EB-FB-1@add-update": 15
anchor: [3, 4, 6, 32, 37, 54, 58, 62]
coverage:
  web: automated
---

# Add Update: node Update added by tersimpan, toast, dan Last Updated berubah

## Prerequisites
- Aktor: Rina W, Total Control, tidak menjadi Last Holder record di bawah.
- Layar awal: halaman Missing, sub-tab Active.
- Data:
  - DU-013-1: Record Missing `Printer HP LaserJet M404 {runId}`, Asset ID `PRN-013-0001`, Group `Head Office`, Status `Missing`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 5 hari, pukul 10:00`, Days Missing `5 days`. Node: `Reported missing by Rina W` dengan What happened `Printer tidak ada di meja layanan setelah jam kerja` pada node `Reported missing by Rina W`; `Update added by Dewi A` pada `T0 − 3 hari, pukul 10:00` dengan Update `Printer sudah dicek di ruang server, tidak ada`. Modified By `Dewi A` dan Last Updated `T0 − 3 hari, pukul 10:00`, dari node Update terakhir.
  - DU-013-4: Record Found `Monitor LG 27UL500 {runId}`, Asset ID `MON-013-0004`, Group `Head Office`, Status `Found`, Source `Manual`, Last Holder `—`, Reported By `Rina W`.
  - DU-013-5: Record Waiting for Confirmation `Forklift Toyota 8FG25 {runId}`, Asset ID `FKL-013-0005`, Group `Head Office`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari D`, Reported By `Sari D`, Reported Date `T0 − 1 hari, pukul 08:30`.
  - DU-013-6: Record Reported Disposal `Compressor Atlas Copco GA30 {runId}`, Asset ID `CMP-013-0006`, Group `Head Office`, Status `Reported Disposal`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 8 hari, pukul 09:10`.
  - DU-013-7: Record In Disposal Process `Genset Perkins 40kVA {runId}`, Asset ID `GEN-013-0007`, Group `Head Office`, Status `In Disposal Process`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 12 hari, pukul 14:00`.
  - DU-013-8: Record Rejected `Tablet Samsung Galaxy Tab A8 {runId}`, Asset ID `TAB-013-0008`, Group `Head Office`, Status `Rejected`, Source `Reported by holder`, Last Holder `Sari D`, Reported By `Sari D`, Reported Date `T0 − 9 hari, pukul 11:15`.
  - DU-013-9: Record Canceled `Scanner Honeywell Voyager 1450g {runId}`, Asset ID `SCN-013-0009`, Group `Head Office`, Status `Canceled`, Source `Reported by holder`, Last Holder `Sari D`, Reported By `Sari D`, Reported Date `T0 − 7 hari, pukul 10:45`.
  - DU-013-10: Record Disposed `Mesin Fotokopi Ricoh MP 2555 {runId}`, Asset ID `FTK-013-0010`, Group `Head Office`, Status `Disposed`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 20 hari, pukul 15:30`.
  - Pengguna pada data: Rina W, Total Control, seluruh client; Dewi A, Manage asset & TAG dengan Update pada Group Head Office; Sari D, pemegang yang memakai akun sendiri.
  - Waktu pada data ditulis relatif terhadap waktu run `T0`, dan ditampilkan menurut Date Format dan Time Format di bawah.
- Kondisi:
  - Date Format bernilai `DD/MM/YY`
  - Time Format bernilai `HH:mm`

## Test Steps

### Keadaan record sebelum Add Update
1. Ketik Search `{runId}`, tekan Enter
2. Centang `Modified By` pada Setup Column
3. Verifikasi Modified By baris `Printer HP LaserJet M404 {runId}` menampilkan `Dewi A`
4. Verifikasi Last Updated baris `Printer HP LaserJet M404 {runId}` menampilkan `T0 − 3 hari, pukul 10:00` menurut Date Format dan Time Format
5. Klik nama `Printer HP LaserJet M404 {runId}` pada kolom Name
6. Verifikasi dialog `Missing Log` terbuka untuk record `Printer HP LaserJet M404 {runId}`
7. Verifikasi node `Update added by Rina W` belum ada pada record
8. Klik `✕` pada dialog Missing Log

### Add Update pada record berjalan
9. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
10. Verifikasi menu baris memuat `Add Update` bagi Total Control
11. Klik `Add Update`
12. Verifikasi dialog `Add Update` terbuka
13. Isi Update `Pemeriksaan lapangan: printer terakhir terlihat di gudang cabang Bekasi`
14. Klik `[Add Update]`
15. Verifikasi toast `Success, update has been added.` tampil

### Node tersimpan dan baris diperbarui
16. Klik nama `Printer HP LaserJet M404 {runId}` pada kolom Name
17. Verifikasi node `Update added by Rina W` memuat Update `Pemeriksaan lapangan: printer terakhir terlihat di gudang cabang Bekasi`
18. Verifikasi hanya satu node `Update added by Rina W` dengan Update `Pemeriksaan lapangan: printer terakhir terlihat di gudang cabang Bekasi` pada record
19. Klik `✕` pada dialog Missing Log
20. Verifikasi Last Updated baris `Printer HP LaserJet M404 {runId}` tidak lagi `T0 − 3 hari, pukul 10:00`, melainkan waktu Add Update tadi menurut Date Format dan Time Format
21. Verifikasi Modified By baris `Printer HP LaserJet M404 {runId}` menampilkan `Rina W`

### Setiap Submit membuat node baru
22. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
23. Klik `Add Update`
24. Isi Update `Update kedua: pengelola gudang Bekasi mengonfirmasi printer tidak ada di lokasi`
25. Klik `[Add Update]`
26. Verifikasi toast `Success, update has been added.` tampil untuk Submit kedua
27. Klik nama `Printer HP LaserJet M404 {runId}` pada kolom Name
28. Verifikasi node `Update added by Rina W` memuat Update `Update kedua: pengelola gudang Bekasi mengonfirmasi printer tidak ada di lokasi`
29. Verifikasi node `Update added by Rina W` dengan Update `Pemeriksaan lapangan: printer terakhir terlihat di gudang cabang Bekasi` tetap tampil
30. Klik `✕` pada dialog Missing Log

### Kolom Modified By disembunyikan kembali
31. Hapus centang `Modified By` pada Setup Column
32. Verifikasi kolom `Last Updated` tetap tampil di tabel
33. Verifikasi kolom `Modified By` tidak tampil di tabel

### Add Update tidak tersedia pada record selesai
34. Klik sub-tab `History`
35. Ketik Search `{runId}`, tekan Enter
36. Klik `⋯` pada baris `Monitor LG 27UL500 {runId}`
37. Verifikasi menu baris memuat `Missing Log`
38. Verifikasi `Add Update` tidak tampil pada menu baris karena status record sudah selesai
39. Tekan Esc untuk menutup menu baris
### Add Update tersedia pada setiap status record berjalan
40. Klik sub-tab `Active`
41. Ketik Search `{runId}`, tekan Enter
42. Klik `⋯` pada baris `Forklift Toyota 8FG25 {runId}`
43. Verifikasi menu baris memuat `Add Update` bagi Total Control pada record berstatus `Waiting for Confirmation`
44. Tekan Esc untuk menutup menu baris
45. Klik `⋯` pada baris `Compressor Atlas Copco GA30 {runId}`
46. Verifikasi menu baris memuat `Add Update` bagi Total Control pada record berstatus `Reported Disposal`
47. Tekan Esc untuk menutup menu baris
48. Klik `⋯` pada baris `Genset Perkins 40kVA {runId}`
49. Verifikasi menu baris memuat `Add Update` bagi Total Control pada record berstatus `In Disposal Process`
50. Tekan Esc untuk menutup menu baris
### Add Update tidak tersedia pada setiap status record selesai
51. Klik sub-tab `History`
52. Ketik Search `{runId}`, tekan Enter
53. Klik `⋯` pada baris `Tablet Samsung Galaxy Tab A8 {runId}`
54. Verifikasi menu baris memuat `Missing Log`
55. Verifikasi `Add Update` tidak tampil pada menu baris karena status record `Rejected` sudah selesai
56. Tekan Esc untuk menutup menu baris
57. Klik `⋯` pada baris `Scanner Honeywell Voyager 1450g {runId}`
58. Verifikasi menu baris memuat `Missing Log`
59. Verifikasi `Add Update` tidak tampil pada menu baris karena status record `Canceled` sudah selesai
60. Tekan Esc untuk menutup menu baris
61. Klik `⋯` pada baris `Mesin Fotokopi Ricoh MP 2555 {runId}`
62. Verifikasi menu baris memuat `Missing Log`
63. Verifikasi `Add Update` tidak tampil pada menu baris karena status record `Disposed` sudah selesai
64. Tekan Esc untuk menutup menu baris
