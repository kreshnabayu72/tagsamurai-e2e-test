---
id: TC-FA-ASTL-E2E-018-manage-aset
title: "Manage aset Unmanaged dengan kuota Available"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-15b", "ASTL-LOGIC-15c", "ASTL-LOGIC-15d", "ASTL-LOGIC-15e", "ASTL-LOGIC-15f", "ASTL-LOGIC-15g", "ASTL-LOGIC-15o", "ASTL-LOGIC-15r", "DO-02", "EB-FRM-1@manage-asset", "EB-FB-1@manage-asset"]
smoke: ["EB-FB-1@manage-asset"]
dependsOn: []
trace:
  "ASTL-LOGIC-15b": [2, 4, 8, 55, 56, 61]
  "ASTL-LOGIC-15c": 8
  "ASTL-LOGIC-15d": 12
  "ASTL-LOGIC-15e": 18
  "ASTL-LOGIC-15f": 28
  "ASTL-LOGIC-15g": 18
  "ASTL-LOGIC-15o": [40, 53]
  "ASTL-LOGIC-15r": [46, 50]
  "DO-02": [20, 22, 28]
  "EB-FRM-1@manage-asset": [39, 42]
  "EB-FB-1@manage-asset": 39
anchor: []
coverage:
  web: automated
---
# Manage aset Unmanaged dengan kuota Available

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-018-1: Group `Cabang Bandung {runId}`, Available license `2`.
  - DU-018-2: Group `Cabang Medan {runId}`, Available license `0`.
  - DU-018-3: aset Active Unmanaged, Asset Name `Kamera Mirrorless {runId}`, tampil `Kamera Mirrorless {runId} - 1`, Brand `Sony`, Model/Type `A6400`, Category `Peralatan Foto`, Group `Cabang Bandung {runId}`, Status `Available, Unmanaged`.
  - DU-018-4: aset Active Unmanaged, Asset Name `Tablet Inventaris {runId}`, tampil `Tablet Inventaris {runId} - 1`, Brand `Samsung`, Model/Type `Tab A8`, Category `Peralatan IT`, Group `Cabang Bandung {runId}`, Status `Available, Unmanaged`.
  - DU-018-5: aset Active Unmanaged, Asset Name `Proyektor X2 {runId}`, tampil `Proyektor X2 {runId} - 1`, Brand `Epson`, Model/Type `EB-X06`, Category `Peralatan Presentasi`, Group `Cabang Medan {runId}`, Status `Available, Unmanaged`.
  - DU-018-6: aset Active managed, Asset Name `Printer Laser {runId}`, tampil `Printer Laser {runId} - 1`, Brand `Brother`, Model/Type `HL-L2375DW`, Category `Peralatan Kantor`, Group `Cabang Medan {runId}`, Status `Available`.
  - DU-018-7: aset Active managed, Asset Name `Laptop Pro 16 {runId}`, tampil `Laptop Pro 16 {runId} - 1`, Brand `Lenovo`, Model/Type `ThinkPad T14`, Category `Peralatan IT`, Group `Cabang Bandung {runId}`, Status `Available`.
  - DU-018-8: aset Active Unmanaged dengan Activity Lock `In Audit`, Asset Name `Radio Panggil {runId}`, tampil `Radio Panggil {runId} - 1`, Brand `Motorola`, Model/Type `T82`, Category `Peralatan Komunikasi`, Group `Cabang Bandung {runId}`, Status `Available, Unmanaged, In Audit`.
- Kondisi:
  - Managed Transition Time dan Managed Action Retry Delay bernilai nilai License Timing yang berlaku di Lifecycle Settings.

## Test Steps

### Aksi Manage tampil untuk aset Unmanaged
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Kamera Mirrorless {runId} - 1` memuat badge `Unmanaged`
3. Klik menu `⋯` pada baris `Kamera Mirrorless {runId} - 1`
4. Verifikasi `Manage` tersedia sebagai Row Action dan tidak `Disabled`
5. Tutup menu aksi baris dengan `Esc`
6. Centang baris `Kamera Mirrorless {runId} - 1` dan baris `Tablet Inventaris {runId} - 1`
7. Klik `Bulk Action`
8. Verifikasi `Manage` tersedia sebagai Bulk Action dan tidak `Disabled` karena kedua aset berasal dari satu group
9. Tutup menu Bulk Action dengan `Esc`
10. Centang baris `Proyektor X2 {runId} - 1`
11. Klik `Bulk Action`
12. Verifikasi `Manage` tampil `Disabled` karena aset terpilih berasal dari lebih dari satu group
13. Tutup menu Bulk Action dengan `Esc`
14. Klik `×` pada Bar Bulk

### Available lebih dari 0 menawarkan dua sumber dan sumber Switch
15. Centang baris `Kamera Mirrorless {runId} - 1`
16. Klik `Bulk Action`
17. Pilih `Manage`
18. Verifikasi dialog `Manage Asset` tampil dengan pilihan sumber `Available quota` dan `Switch with a managed asset`
19. Pilih `Switch with a managed asset`
20. Verifikasi tombol `[Next]` tampil sebagai pengganti `[Manage]`
21. Klik `[Next]`
22. Verifikasi dialog `Switch Manage Asset` tampil dan memuat baris `Laptop Pro 16 {runId} - 1`
23. Klik `[Cancel]`
24. Klik `×` pada Bar Bulk

### Available sama dengan 0 langsung membuka Switch Manage Asset
25. Centang baris `Proyektor X2 {runId} - 1`
26. Klik `Bulk Action`
27. Pilih `Manage`
28. Verifikasi dialog `Switch Manage Asset` tampil langsung dan memuat baris `Printer Laser {runId} - 1`
29. Klik `[Cancel]`
30. Klik `×` pada Bar Bulk

### Manage dengan sumber Available quota
31. Centang baris `Kamera Mirrorless {runId} - 1`
32. Klik ikon `Changelog` pada toolbar
33. Catat entri Changelog teratas
34. Tutup modal Changelog
35. Klik `Bulk Action`
36. Pilih `Manage`
37. Pilih `Available quota`
38. Klik `[Manage]`
39. Verifikasi toast `Success, asset has been sent to be managed.` tampil
40. Verifikasi baris `Kamera Mirrorless {runId} - 1` memuat badge `Pending Activation`
41. Klik ikon `Changelog` pada toolbar
42. Verifikasi Changelog memuat tepat satu entri baru field `License` dari `Unmanaged` ke `Pending Activation` untuk `Kamera Mirrorless {runId} - 1`
43. Tutup modal Changelog

### Jeda antar aksi Manage pada group yang sama
44. Centang baris `Tablet Inventaris {runId} - 1`
45. Klik `Bulk Action`
46. Verifikasi `Manage` tampil `Disabled` selama Managed Action Retry Delay
47. Tutup menu Bulk Action dengan `Esc`
48. Managed Action Retry Delay group `Cabang Bandung {runId}` berlalu
49. Klik `Bulk Action`
50. Verifikasi `Manage` tersedia lagi dan tidak `Disabled`
51. Tutup menu Bulk Action dengan `Esc`
52. Managed Transition Time berlalu sejak Manage `Kamera Mirrorless {runId} - 1` diajukan
53. Verifikasi baris `Kamera Mirrorless {runId} - 1` tidak lagi memuat badge `Pending Activation` maupun `Unmanaged`

### Activity Lock tidak membatasi Manage
54. Klik menu `⋯` pada baris `Radio Panggil {runId} - 1`
55. Verifikasi baris memuat badge `In Audit`
56. Verifikasi `Manage` tersedia sebagai Row Action dan tidak `Disabled` walaupun aset terkunci Activity Lock `In Audit`
57. Tutup menu aksi baris dengan `Esc`

### Activity Lock tidak membatasi Bulk Manage
58. Klik `×` pada Bar Bulk
59. Centang baris `Radio Panggil {runId} - 1` dan baris `Tablet Inventaris {runId} - 1`
60. Klik `Bulk Action`
61. Verifikasi `Manage` tersedia sebagai Bulk Action dan tidak `Disabled` walaupun seleksi memuat aset terkunci Activity Lock `In Audit`
62. Tutup menu Bulk Action dengan `Esc`
