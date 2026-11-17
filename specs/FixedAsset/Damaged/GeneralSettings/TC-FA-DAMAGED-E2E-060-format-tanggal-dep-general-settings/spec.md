---
id: TC-FA-DAMAGED-E2E-060-format-tanggal-dep-general-settings
title: "Perubahan Date Format, Time Format, dan Time Zone di General Settings tercermin pada kolom tanggal tab Damaged"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-XM-1", "§4.1#p4"]
smoke: []
dependsOn:
  - "General Settings: Date Format, Time Format, Time Zone"
trace:
  "EB-XM-1": [3, 4, 10, 11, 17, 24, 25, 31, 37, 43, 52, 60]
  "§4.1#p4": [3, 4, 10, 17, 31, 37]
anchor: []
coverage:
  web: automated
---

# Perubahan Date Format, Time Format, dan Time Zone di General Settings tercermin pada kolom tanggal tab Damaged

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Assets, tab Damaged.
- Data:
  - DU-060-1: aset Name `Mesin Fotokopi Canon iR2625 {runId}`, Group `Head Office`, tanpa TAG, dengan record `Damaged` Source `Manual`, Reported Date `T0 − 3 hari, pukul 17:10`.
  - DU-060-2: aset Name `Mesin Laminating GBC Fusion {runId}`, Group `Head Office`, tanpa TAG, dengan record `Damaged` Source `Manual`, Reported Date `T0 − 2 hari, pukul 09:30`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.
  - Time Zone bernilai `Asia/Jakarta`.
  - After photo required bernilai `OFF`.

## Test Steps

### Nilai bawaan: kolom tanggal record yang sudah ada mengikuti Date Format dan Time Format
1. Buka halaman Assets, tab `Damaged`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi kolom Reported Date pada baris aset `Mesin Fotokopi Canon iR2625 {runId}` memakai Date Format `dd/MM/yy` dan Time Format `24h`
4. Verifikasi kolom Last Updated pada baris aset `Mesin Fotokopi Canon iR2625 {runId}` memakai Date Format `dd/MM/yy` dan Time Format `24h`

### Date Format `M/d/yy` tercermin pada record yang sudah ada
5. Buka halaman General Settings
6. Pilih Date Format `M/d/yy`
7. Simpan General Settings
8. Buka halaman Assets, tab `Damaged`
9. Ketik Search `{runId}`, tekan Enter
10. Verifikasi kolom Reported Date pada baris aset `Mesin Fotokopi Canon iR2625 {runId}` memakai Date Format `M/d/yy` dan Time Format `24h`
11. Verifikasi kolom Last Updated pada baris aset `Mesin Fotokopi Canon iR2625 {runId}` memakai Date Format `M/d/yy` dan Time Format `24h`

### Date Format `dd MMM yy` tercermin pada record yang sudah ada dan pada waktu selesai record yang diselesaikan sesudah perubahan
12. Buka halaman General Settings
13. Pilih Date Format `dd MMM yy`
14. Simpan General Settings
15. Buka halaman Assets, tab `Damaged`
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi kolom Reported Date pada baris aset `Mesin Fotokopi Canon iR2625 {runId}` memakai Date Format `dd MMM yy` dan Time Format `24h`
18. Klik `⋯` pada baris aset `Mesin Laminating GBC Fusion {runId}`
19. Klik `Mark as Repaired`
20. Isi Repair note `Elemen pemanas sudah diganti dan hasil laminasi rata`
21. Klik `[Mark as Repaired]`
22. Klik sub-tab `History`
23. Ketik Search `{runId}`, tekan Enter
24. Verifikasi kolom Reported Date pada baris aset `Mesin Laminating GBC Fusion {runId}` memakai Date Format `dd MMM yy` dan Time Format `24h`
25. Verifikasi kolom Resolved Date pada baris aset `Mesin Laminating GBC Fusion {runId}` memakai Date Format `dd MMM yy` dan Time Format `24h`

### Date Format `DDD, MMM dd, yy` tercermin pada kolom tanggal
26. Buka halaman General Settings
27. Pilih Date Format `DDD, MMM dd, yy`
28. Simpan General Settings
29. Buka halaman Assets, tab `Damaged`
30. Ketik Search `{runId}`, tekan Enter
31. Verifikasi kolom Reported Date pada baris aset `Mesin Fotokopi Canon iR2625 {runId}` memakai Date Format `DDD, MMM dd, yy` dan Time Format `24h`

### Date Format `DDD, MMM dd, yyyy` tercermin pada kolom tanggal
32. Buka halaman General Settings
33. Pilih Date Format `DDD, MMM dd, yyyy`
34. Simpan General Settings
35. Buka halaman Assets, tab `Damaged`
36. Ketik Search `{runId}`, tekan Enter
37. Verifikasi kolom Reported Date pada baris aset `Mesin Fotokopi Canon iR2625 {runId}` memakai Date Format `DDD, MMM dd, yyyy` dan Time Format `24h`

### Time Format `12h` tercermin pada kolom tanggal
38. Buka halaman General Settings
39. Pilih Time Format `12h`
40. Simpan General Settings
41. Buka halaman Assets, tab `Damaged`
42. Ketik Search `{runId}`, tekan Enter
43. Verifikasi kolom Reported Date pada baris aset `Mesin Fotokopi Canon iR2625 {runId}` memakai Date Format `DDD, MMM dd, yyyy` dan Time Format `12h`

### Time Zone `Asia/Jayapura` menggeser waktu pada kolom tanggal
44. Buka halaman Assets, tab `Damaged`
45. Ketik Search `{runId}`, tekan Enter
46. Catat waktu pada kolom Reported Date baris aset `Mesin Fotokopi Canon iR2625 {runId}`
47. Buka halaman General Settings
48. Pilih Time Zone `Asia/Jayapura`
49. Simpan General Settings
50. Buka halaman Assets, tab `Damaged`
51. Ketik Search `{runId}`, tekan Enter
52. Verifikasi waktu pada kolom Reported Date baris aset `Mesin Fotokopi Canon iR2625 {runId}` dua jam lebih lambat daripada waktu yang dicatat

### Date Format `dd/MM/yy`, Time Format `24h`, dan Time Zone `Asia/Jakarta` tercermin pada kolom tanggal
53. Buka halaman General Settings
54. Pilih Date Format `dd/MM/yy`
55. Pilih Time Format `24h`
56. Pilih Time Zone `Asia/Jakarta`
57. Simpan General Settings
58. Buka halaman Assets, tab `Damaged`
59. Ketik Search `{runId}`, tekan Enter
60. Verifikasi kolom Reported Date pada baris aset `Mesin Fotokopi Canon iR2625 {runId}` memakai Date Format `dd/MM/yy` dan Time Format `24h`
