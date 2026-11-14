---
id: TC-FA-DAMAGED-UI-104-tabel-active-aksi-per-status
title: "Menu aksi baris sub-tab Active per status, penanda, dan hak: Review Disabled bagi pelapor, aksi Hidden pada penanda Missing, Reported Disposal, In Disposal Process, Cancel Disposal Report, tooltip plan None, dan dialog Already Changed"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, D-DMG-06, "§4.2.4#p5", "§4.4#r10", S-DMG-03, S-DMG-04, S-DMG-05, S-DMG-06, V-DMG-01, V-DMG-07, "§9.4.2#r8", "§9.4.2#r32", "§2.1#b7", EB-TBL-5@review, EB-TBL-5@aksi-disposal-plan-none]
smoke: []
dependsOn: []
trace:
  T-DMG-01: [3, 8, 9, 10, 23, 27]
  D-DMG-06: [62, 63, 64, 72]
  "§4.2.4#p5": [63, 66, 67, 73, 79, 80]
  "§4.4#r10": [62]
  S-DMG-03: [13, 18]
  S-DMG-04: [32, 33, 36, 37]
  S-DMG-05: [24, 28]
  S-DMG-06: [5, 29, 40, 41]
  V-DMG-01: [15, 20]
  V-DMG-07: [62, 72]
  "§9.4.2#r8": [13]
  "§9.4.2#r32": [44, 46, 49, 51, 55, 57]
  "§2.1#b7": [4, 13]
  EB-TBL-5@review: [15]
  EB-TBL-5@aksi-disposal-plan-none: [46, 51, 57]
anchor: []
coverage:
  web: automated
---

# Menu aksi baris sub-tab Active per status, penanda, dan hak: Review Disabled bagi pelapor, aksi Hidden pada penanda Missing, Reported Disposal, In Disposal Process, Cancel Disposal Report, tooltip plan None, dan dialog Already Changed

## Prerequisites
- Aktor: pemegang Manage asset & TAG (Update) pada Group aset (Aktor Damaged), dengan hak lain menurut Kondisi.
- Layar awal: halaman Assets, tab `Damaged`, sub-tab `Active`.
- Komponen: Tabel T-DMG-01 (sub-tab Active)
- Data:
  - DU-104-1: Record `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Status `Waiting for Confirmation`, Reported By `Budi Santoso`.
  - DU-104-2: Record `Scanner Fujitsu fi-7160 - 2`, Asset ID `SCN-2026-0002`, Group `Head Office`, Status `Waiting for Confirmation`, Reported By aktor sendiri.
  - DU-104-3: Record `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Group `Head Office`, Status `Damaged`, dilaporkan Pelapor admin.
  - DU-104-4: Record `Printer HP LaserJet M404 - 8`, Asset ID `PRN-2026-0008`, Group `Head Office`, Status `Reported Disposal`.
  - DU-104-5: Record `Monitor Dell P2422H - 6`, Asset ID `MON-2026-0006`, Group `Head Office`, Status `In Disposal Process`.
  - DU-104-6: Record `Camera Canon EOS - 3`, Asset ID `CAM-2026-0003`, Group `Head Office`, Status `Damaged` dengan penanda `Missing`.
  - DU-104-7: Record `Drill Bosch GSB - 6`, Asset ID `DRL-2026-0006`, Group `Warehouse`, Status `Damaged` dengan penanda `Reported Missing`.
  - DU-104-8: Pelaku perubahan status terakhir `Rina Wijaya` pada DU-104-1 yang kini berstatus `Damaged`.
  - DU-104-9: Pelaku perubahan status terakhir `System` pada DU-104-1 yang kini berstatus `Damaged`.
- Kondisi:
  - K1: daftar memuat DU-104-1 sampai DU-104-7; aktor memegang hak Report Disposal dan hak Cancel Disposal Report; Level Feature Suite Disposal bernilai `Basic`.
  - K2: daftar seperti K1; aktor tidak memegang hak Cancel Disposal Report.
  - K3: daftar seperti K1; Level Feature Suite Disposal bernilai `None`.
  - K4: daftar seperti K1; konfirmasi atas DU-104-1 ditolak karena status sudah diubah oleh pelaku pada DU-104-8; sesudah muat ulang DU-104-1 berstatus `Damaged`.
  - K5: daftar seperti K1; konfirmasi atas DU-104-1 ditolak karena status sudah diubah oleh pelaku pada DU-104-9; sesudah muat ulang DU-104-1 berstatus `Damaged`.
  - K6: daftar seperti K1; permintaan Report Disposal diterima server dengan sebagian record dilewati.

## Test Steps

### Menu aksi record Damaged
1. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
2. Klik `⋯` pada baris `Projector Epson EB-X06 - 2`
3. Verifikasi menu memuat `Damage Log`, `Mark as Repaired`, `Report Disposal`, lalu `Report Missing` dalam urutan itu
4. Verifikasi aksi `Review` tidak dirender
5. Verifikasi aksi `Cancel Disposal Report` tidak dirender

### Menu aksi record Waiting for Confirmation
6. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
7. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 4`
8. Verifikasi menu memuat `Damage Log` dan `Review`
9. Verifikasi aksi `Review` aktif
10. Verifikasi aksi `Mark as Repaired`, `Report Disposal`, dan `Report Missing` tidak dirender

### Review Disabled bagi pelapor
11. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
12. Klik `⋯` pada baris `Scanner Fujitsu fi-7160 - 2`
13. Verifikasi aksi `Review` tampil Disabled
14. Arahkan pointer ke aksi `Review`
15. Verifikasi alasan `You reported this. Ask another admin.` tersampaikan pada aksi yang Disabled
16. Tekan `Esc`
17. Klik `Scanner Fujitsu fi-7160 - 2` pada kolom `Name`
18. Verifikasi tombol `[Reject]` dan `[Confirm]` pada footer dialog `Damage Log` tampil Disabled
19. Arahkan pointer ke tombol `[Confirm]`
20. Verifikasi alasan `You reported this. Ask another admin.` tersampaikan pada tombol yang Disabled

### Menu aksi record Reported Disposal
21. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
22. Klik `⋯` pada baris `Printer HP LaserJet M404 - 8`
23. Verifikasi menu memuat `Damage Log` lalu `Cancel Disposal Report`
24. Verifikasi aksi `Mark as Repaired` tidak dirender

### Menu aksi record In Disposal Process
25. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
26. Klik `⋯` pada baris `Monitor Dell P2422H - 6`
27. Verifikasi menu memuat `Damage Log`
28. Verifikasi aksi `Mark as Repaired` tidak dirender
29. Verifikasi aksi `Cancel Disposal Report` tidak dirender

### Record berpenanda Missing hanya menyisakan Damage Log
30. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
31. Klik `⋯` pada baris `Camera Canon EOS - 3`
32. Verifikasi menu memuat `Damage Log`
33. Verifikasi aksi `Review`, `Mark as Repaired`, `Report Disposal`, `Report Missing`, dan `Cancel Disposal Report` tidak dirender
34. Tekan `Esc`
35. Klik `⋯` pada baris `Drill Bosch GSB - 6`
36. Verifikasi menu memuat `Damage Log`
37. Verifikasi aksi `Review`, `Mark as Repaired`, `Report Disposal`, `Report Missing`, dan `Cancel Disposal Report` tidak dirender

### Cancel Disposal Report Hidden bagi aktor tanpa hak
38. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K2
39. Klik `⋯` pada baris `Printer HP LaserJet M404 - 8`
40. Verifikasi menu memuat `Damage Log`
41. Verifikasi aksi `Cancel Disposal Report` tidak dirender

### Aksi disposal terkunci pada level Feature Suite Disposal None
42. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K3
43. Klik `⋯` pada baris `Projector Epson EB-X06 - 2`
44. Verifikasi aksi `Report Disposal` tampil Disabled
45. Arahkan pointer ke aksi `Report Disposal`
46. Verifikasi alasan `Upgrade to unlock` tersampaikan pada aksi yang Disabled
47. Tekan `Esc`
48. Klik `⋯` pada baris `Printer HP LaserJet M404 - 8`
49. Verifikasi aksi `Cancel Disposal Report` tampil Disabled
50. Arahkan pointer ke aksi `Cancel Disposal Report`
51. Verifikasi alasan `Upgrade to unlock` tersampaikan pada aksi yang Disabled
52. Tekan `Esc`
53. Centang baris `Projector Epson EB-X06 - 2`
54. Klik `Bulk Action`
55. Verifikasi item `Report Disposal` tampil Disabled
56. Arahkan pointer ke item `Report Disposal`
57. Verifikasi alasan `Upgrade to unlock` tersampaikan pada item yang Disabled

### Confirm ditolak karena status sudah diubah pengguna lain
58. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K4
59. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 4`
60. Klik `Review`
61. Klik `[Confirm]`
62. Verifikasi dialog `Already Changed` tampil
63. Verifikasi pesan `This record was changed by Rina Wijaya. Reload to see the latest status.` tampil
64. Verifikasi tombol `[Reload]` tampil
65. Klik `[Reload]`
66. Verifikasi dialog `Already Changed` tertutup
67. Verifikasi baris `Laptop Dell Latitude 5420 - 4` menampilkan badge status `Damaged` sesudah tabel dimuat ulang

### Pelaku perubahan terakhir tanpa user aktor tampil sebagai System
68. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K5
69. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 4`
70. Klik `Review`
71. Klik `[Confirm]`
72. Verifikasi dialog `Already Changed` tampil
73. Verifikasi pesan `This record was changed by System. Reload to see the latest status.` tampil

### Aksi bulk tidak memakai dialog Already Changed
74. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K6
75. Centang baris `Projector Epson EB-X06 - 2`
76. Klik `Bulk Action`
77. Klik `Report Disposal`
78. Kirim dialog `D-DISP-13` dengan Reason `Kerusakan tidak dapat diperbaiki`
79. Verifikasi toast `Success, asset has been reported for disposal. Some items were skipped.` tampil
80. Verifikasi dialog `Already Changed` tidak tampil

