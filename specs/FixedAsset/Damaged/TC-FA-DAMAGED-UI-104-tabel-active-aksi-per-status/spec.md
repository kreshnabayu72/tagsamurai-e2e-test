---
id: TC-FA-DAMAGED-UI-104-tabel-active-aksi-per-status
title: "Menu aksi baris sub-tab Active per status, penanda, dan hak: Review Show saat Waiting for Confirmation, aksi Hidden pada penanda Missing, Reported Disposal, In Disposal Process, Cancel Disposal Report, tooltip plan None, dan dialog Already Changed, serta Mark as Repaired dan Report Disposal Disabled saat Custody In Transfer Process atau Report Disposal Disabled saat Custody bukan Available"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, D-DMG-06, "§4.2.4#p6", "§4.4#r10", S-DMG-04, S-DMG-05, S-DMG-06, V-DMG-07, EC-DMG-36, "§2.1#b8", EB-TBL-5@aksi-disposal-plan-none, S-DMG-23, EC-DMG-37, "§Aturan Logika Modul#r45", "§4.2.4#r17"]
smoke: []
dependsOn: []
trace:
  T-DMG-01: [3, 8, 9, 10, 13, 17, 76, 83, 86]
  D-DMG-06: [52, 53, 54, 62]
  "§4.2.4#p6": [53, 56, 57, 63, 69, 70]
  "§4.4#r10": [52]
  S-DMG-04: [22, 23, 26, 27]
  S-DMG-05: [14, 18]
  S-DMG-06: [5, 19, 30, 31]
  V-DMG-07: [52, 62]
  EC-DMG-36: [34, 36, 39, 41, 45, 47]
  "§2.1#b8": [4]
  EB-TBL-5@aksi-disposal-plan-none: [36, 41, 47]
  S-DMG-23: [73, 75]
  EC-DMG-37: [73, 75]
  "§Aturan Logika Modul#r45": [73, 75, 76, 77, 80]
  "§4.2.4#r17": [52, 53, 62, 63]
anchor: []
coverage:
  web: automated
---

# Menu aksi baris sub-tab Active per status, penanda, dan hak: Review Show saat Waiting for Confirmation, aksi Hidden pada penanda Missing, Reported Disposal, In Disposal Process, Cancel Disposal Report, tooltip plan None, dan dialog Already Changed, serta Mark as Repaired dan Report Disposal Disabled saat Custody In Transfer Process atau Report Disposal Disabled saat Custody bukan Available

## Prerequisites
- Aktor: pemegang Manage asset & TAG (Update) pada Group aset (Aktor Damaged), dengan hak lain menurut Kondisi.
- Layar awal: halaman Assets, tab `Damaged`, sub-tab `Active`.
- Komponen: Tabel T-DMG-01 (sub-tab Active)
- Data:
  - DU-104-1: Record `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Status `Waiting for Confirmation`, Reported By `Budi Santoso`.
  - DU-104-3: Record `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Group `Head Office`, Status `Damaged`, dilaporkan Pelapor admin.
  - DU-104-4: Record `Printer HP LaserJet M404 - 8`, Asset ID `PRN-2026-0008`, Group `Head Office`, Status `Reported Disposal`.
  - DU-104-5: Record `Monitor Dell P2422H - 6`, Asset ID `MON-2026-0006`, Group `Head Office`, Status `In Disposal Process`.
  - DU-104-6: Record `Camera Canon EOS - 3`, Asset ID `CAM-2026-0003`, Group `Head Office`, Status `Damaged` dengan penanda `Missing`.
  - DU-104-7: Record `Drill Bosch GSB - 6`, Asset ID `DRL-2026-0006`, Group `Warehouse`, Status `Damaged` dengan penanda `Reported Missing`.
  - DU-104-8: Pelaku perubahan status terakhir `Rina Wijaya` pada DU-104-1 yang kini berstatus `Damaged`.
  - DU-104-9: Pelaku perubahan status terakhir `System` pada DU-104-1 yang kini berstatus `Damaged`.
  - DU-104-11: Record `Scanner Fujitsu fi-7160 - 2`, Asset ID `SCN-2026-0002`, Group `Head Office`, Status `Damaged`, Custody aset `In Transfer Process` dengan baris Transfer `Waiting for Approval`.
  - DU-104-12: Record `Tablet Samsung Galaxy Tab A8 - 5`, Asset ID `TAB-2026-0005`, Group `Head Office`, Status `Damaged`, Custody aset `In Transfer Process` dengan baris Transfer `In Transit`.
  - DU-104-13: Record `Laptop Lenovo ThinkPad E14 - 7`, Asset ID `LPT-2026-0007`, Group `Head Office`, Status `Damaged`, Custody aset `Borrowed`.
  - DU-104-14: Record `Handheld Zebra TC21 - 9`, Asset ID `HHD-2026-0009`, Group `Head Office`, Status `Damaged`, Custody aset `Assigned`.
- Kondisi:
  - K1: daftar memuat DU-104-1 sampai DU-104-7; aktor memegang hak Report Disposal dan hak Cancel Disposal Report; Level Feature Suite Disposal bernilai `Full`.
  - K2: daftar seperti K1; aktor tidak memegang hak Cancel Disposal Report.
  - K3: daftar seperti K1; Level Feature Suite Disposal bernilai `None`.
  - K4: daftar seperti K1; konfirmasi atas DU-104-1 ditolak karena status sudah diubah oleh pelaku pada DU-104-8; sesudah muat ulang DU-104-1 berstatus `Damaged`.
  - K5: daftar seperti K1; konfirmasi atas DU-104-1 ditolak karena status sudah diubah oleh pelaku pada DU-104-9; sesudah muat ulang DU-104-1 berstatus `Damaged`.
  - K6: daftar seperti K1; permintaan Report Disposal diterima server dengan sebagian record dilewati.
  - K7: daftar memuat DU-104-11 sampai DU-104-14; aktor memegang hak Report Disposal dan hak Report Missing; Level Feature Suite Disposal bernilai `Full`.

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

### Menu aksi record Reported Disposal
11. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
12. Klik `⋯` pada baris `Printer HP LaserJet M404 - 8`
13. Verifikasi menu memuat `Damage Log` lalu `Cancel Disposal Report`
14. Verifikasi aksi `Mark as Repaired` tidak dirender

### Menu aksi record In Disposal Process
15. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
16. Klik `⋯` pada baris `Monitor Dell P2422H - 6`
17. Verifikasi menu memuat `Damage Log`
18. Verifikasi aksi `Mark as Repaired` tidak dirender
19. Verifikasi aksi `Cancel Disposal Report` tidak dirender

### Record berpenanda Missing hanya menyisakan Damage Log
20. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K1
21. Klik `⋯` pada baris `Camera Canon EOS - 3`
22. Verifikasi menu memuat `Damage Log`
23. Verifikasi aksi `Review`, `Mark as Repaired`, `Report Disposal`, `Report Missing`, dan `Cancel Disposal Report` tidak dirender
24. Tekan `Esc`
25. Klik `⋯` pada baris `Drill Bosch GSB - 6`
26. Verifikasi menu memuat `Damage Log`
27. Verifikasi aksi `Review`, `Mark as Repaired`, `Report Disposal`, `Report Missing`, dan `Cancel Disposal Report` tidak dirender

### Cancel Disposal Report Hidden bagi aktor tanpa hak
28. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K2
29. Klik `⋯` pada baris `Printer HP LaserJet M404 - 8`
30. Verifikasi menu memuat `Damage Log`
31. Verifikasi aksi `Cancel Disposal Report` tidak dirender

### Aksi disposal terkunci pada level Feature Suite Disposal None
32. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K3
33. Klik `⋯` pada baris `Projector Epson EB-X06 - 2`
34. Verifikasi aksi `Report Disposal` tampil Disabled
35. Arahkan pointer ke aksi `Report Disposal`
36. Verifikasi alasan `Upgrade to unlock` tersampaikan pada aksi yang Disabled
37. Tekan `Esc`
38. Klik `⋯` pada baris `Printer HP LaserJet M404 - 8`
39. Verifikasi aksi `Cancel Disposal Report` tampil Disabled
40. Arahkan pointer ke aksi `Cancel Disposal Report`
41. Verifikasi alasan `Upgrade to unlock` tersampaikan pada aksi yang Disabled
42. Tekan `Esc`
43. Centang baris `Projector Epson EB-X06 - 2`
44. Klik `Bulk Action`
45. Verifikasi item `Report Disposal` tampil Disabled
46. Arahkan pointer ke item `Report Disposal`
47. Verifikasi alasan `Upgrade to unlock` tersampaikan pada item yang Disabled

### Confirm ditolak karena status sudah diubah pengguna lain
48. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K4
49. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 4`
50. Klik `Review`
51. Klik `[Confirm]`
52. Verifikasi dialog `Already Changed` tampil
53. Verifikasi pesan `This record was changed by Rina Wijaya. Reload to see the latest status.` tampil
54. Verifikasi tombol `[Reload]` tampil
55. Klik `[Reload]`
56. Verifikasi dialog `Already Changed` tertutup
57. Verifikasi baris `Laptop Dell Latitude 5420 - 4` menampilkan badge status `Damaged` sesudah tabel dimuat ulang

### Pelaku perubahan terakhir tanpa user aktor tampil sebagai System
58. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K5
59. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 4`
60. Klik `Review`
61. Klik `[Confirm]`
62. Verifikasi dialog `Already Changed` tampil
63. Verifikasi pesan `This record was changed by System. Reload to see the latest status.` tampil

### Aksi bulk tidak memakai dialog Already Changed
64. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K6
65. Centang baris `Projector Epson EB-X06 - 2`
66. Klik `Bulk Action`
67. Klik `Report Disposal`
68. Kirim dialog `D-DISP-13` dengan Reason `Kerusakan tidak dapat diperbaiki`
69. Verifikasi toast `Success, asset has been reported for disposal. Some items were skipped.` tampil
70. Verifikasi dialog `Already Changed` tidak tampil

### Aset Custody In Transfer Process: Mark as Repaired dan Report Disposal Disabled
71. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K7
72. Klik `⋯` pada baris `Scanner Fujitsu fi-7160 - 2`
73. Verifikasi aksi `Mark as Repaired` tampil Disabled
74. Arahkan pointer ke aksi `Mark as Repaired`
75. Verifikasi alasan `This asset is in transfer.` tersampaikan pada aksi yang Disabled
76. Verifikasi aksi `Report Disposal` tampil Disabled
77. Verifikasi aksi `Report Missing` aktif

### Report Missing Disabled hanya selama baris Transfer In Transit
78. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K7
79. Klik `⋯` pada baris `Tablet Samsung Galaxy Tab A8 - 5`
80. Verifikasi aksi `Report Missing` tampil Disabled

### Report Disposal Disabled pada aset Borrowed dan Assigned
81. Tampilkan Tabel T-DMG-01 (sub-tab Active) dengan kondisi K7
82. Klik `⋯` pada baris `Laptop Lenovo ThinkPad E14 - 7`
83. Verifikasi aksi `Report Disposal` tampil Disabled
84. Tekan `Esc`
85. Klik `⋯` pada baris `Handheld Zebra TC21 - 9`
86. Verifikasi aksi `Report Disposal` tampil Disabled
