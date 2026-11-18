---
id: TC-FA-ASTL-E2E-035-state-tenant-aksi-tulis-ditolak
title: "Aksi tulis ditolak saat entitas Suspended atau Expired"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["EC-19", "EB-AKS-7"]
smoke: []
dependsOn: []
trace:
  "EC-19": [2, 9, 13, 19, 22, 27, 30, 34, 37, 42, 45, 49, 55, 59, 65, 70, 73, 76]
  "EB-AKS-7": [2, 9, 12, 13, 19, 22, 27, 30, 34, 37, 42, 45, 49, 55, 59, 65, 70, 73, 76, 77]
anchor: []
coverage:
  web: automated
---

# Aksi tulis ditolak saat entitas Suspended atau Expired

## Prerequisites
- Aktor: `Hendra Saputra {runId}`, pemegang role Total Control; operator Admin Console yang mengubah status entitas adalah `Operator Platform`.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - Memakai entitas khusus yang tidak dipakai spec lain.
  - DU-035-1: Entitas, Name `PT Maju Sentosa {runId}`, Status `Suspended`
  - DU-035-2: User, Name `Hendra Saputra {runId}`, Role `Total Control`, Cakupan `Seluruh client`
  - DU-035-3: Group, Name `IT {runId}`
  - DU-035-4: Label, Name `Aset Kantor {runId}`
  - DU-035-5: Label, Name `Prioritas Tinggi {runId}`
  - DU-035-6: Asset, Name `Laptop Pro 16 {runId}`, Group `IT {runId}`, Status `Available`, Purchase Date `T0 − 30 hari`, Purchase Cost `18500000`, Label `Prioritas Tinggi {runId}`
  - DU-035-7: Asset, Name `Kamera Mirrorless {runId}`, Group `IT {runId}`, Status `Available`, License `Unmanaged`
  - DU-035-8: Asset, Name `Switch Jaringan {runId}`, Group `IT {runId}`, Status `Available`
  - DU-035-10: Group, Name `Cabang Medan {runId}`, Available license `0`
  - DU-035-11: Asset, Name `Printer Laser {runId}`, Group `Cabang Medan {runId}`, Status `Available`
  - DU-035-12: Asset, Name `Server Rack {runId}`, Group `Cabang Medan {runId}`, Status `Available`, License `Unmanaged`
  - Nama baris yang diharapkan untuk Asset Name `Laptop Pro 16 {runId}` adalah `Laptop Pro 16 {runId} - 1`, dari Asset Name `Laptop Pro 16 {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Kamera Mirrorless {runId}` adalah `Kamera Mirrorless {runId} - 1`, dari Asset Name `Kamera Mirrorless {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Switch Jaringan {runId}` adalah `Switch Jaringan {runId} - 1`, dari Asset Name `Switch Jaringan {runId}`.
  - Purchase Cost yang diharapkan untuk Purchase Cost `18500000` adalah `Rp 18.500.000,00`, dari Purchase Cost `18500000`.
  - Nama baris yang diharapkan untuk Asset Name `Printer Laser {runId}` adalah `Printer Laser {runId} - 1`, dari Asset Name `Printer Laser {runId}`.
  - Nama baris yang diharapkan untuk Asset Name `Server Rack {runId}` adalah `Server Rack {runId} - 1`, dari Asset Name `Server Rack {runId}`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Lisensi `FA-7` aktif pada entitas.
  - Entitas berstatus `Suspended`.

## Test Steps

### Modul tetap terbuka dan terbaca
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Laptop Pro 16 {runId} - 1`, `Kamera Mirrorless {runId} - 1`, dan `Switch Jaringan {runId} - 1` tampil di tabel
3. Tampilkan kolom `Purchase Cost`

### Add Label ditolak saat Suspended
4. Centang baris `Laptop Pro 16 {runId} - 1`
5. Klik tombol Bulk Action
6. Klik `Add Label`
7. Pilih label `Aset Kantor {runId}` pada dialog Add Label
8. Klik `[Apply]`
9. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
10. Muat ulang halaman
11. Ketik Search `{runId}`, tekan Enter
12. Verifikasi kolom Labels baris `Laptop Pro 16 {runId} - 1` memuat chip `Prioritas Tinggi {runId}`
13. Verifikasi kolom Labels baris `Laptop Pro 16 {runId} - 1` tidak memuat chip `Aset Kantor {runId}`

### Remove Label ditolak saat Suspended
14. Centang baris `Laptop Pro 16 {runId} - 1`
15. Klik tombol Bulk Action
16. Klik `Remove Label`
17. Pilih label `Prioritas Tinggi {runId}` pada dialog Remove Label
18. Klik `[Apply]`
19. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
20. Muat ulang halaman
21. Ketik Search `{runId}`, tekan Enter
22. Verifikasi kolom Labels baris `Laptop Pro 16 {runId} - 1` tetap memuat chip `Prioritas Tinggi {runId}`

### Edit Purchase ditolak saat Suspended
23. Klik `⋯` pada baris `Laptop Pro 16 {runId} - 1`
24. Klik `Edit Purchase`
25. Ganti isi Purchase Cost dengan `19200000`
26. Klik `[Save]`
27. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
28. Muat ulang halaman
29. Ketik Search `{runId}`, tekan Enter
30. Verifikasi sel `Purchase Cost` baris `Laptop Pro 16 {runId} - 1` tetap menampilkan `Rp 18.500.000,00`

### Manage ditolak saat Suspended
31. Klik `⋯` pada baris `Kamera Mirrorless {runId} - 1`
32. Klik `Manage`
33. Klik `[Manage]` pada dialog Manage Asset
34. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
35. Muat ulang halaman
36. Ketik Search `{runId}`, tekan Enter
37. Verifikasi baris `Kamera Mirrorless {runId} - 1` tetap menampilkan status `Unmanaged`

### Delete Asset Data ditolak saat Suspended
38. Klik `⋯` pada baris `Switch Jaringan {runId} - 1`
39. Klik `Delete Asset Data`
40. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
41. Klik `[Delete]`
42. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
43. Muat ulang halaman
44. Ketik Search `{runId}`, tekan Enter
45. Verifikasi baris `Switch Jaringan {runId} - 1` tetap tampil di tabel

### Add Label ditolak saat Expired
46. Operator Platform mengubah status entitas `PT Maju Sentosa {runId}` menjadi `Expired` di Admin Console
47. Muat ulang halaman
48. Ketik Search `{runId}`, tekan Enter
49. Verifikasi baris `Laptop Pro 16 {runId} - 1` masih tampil di tabel
50. Centang baris `Laptop Pro 16 {runId} - 1`
51. Klik tombol Bulk Action
52. Klik `Add Label`
53. Pilih label `Aset Kantor {runId}` pada dialog Add Label
54. Klik `[Apply]`
55. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil

### Add Label ditolak saat Grace
56. Operator Platform mengubah status entitas `PT Maju Sentosa {runId}` menjadi masa `Grace` di Admin Console
57. Muat ulang halaman
58. Ketik Search `{runId}`, tekan Enter
59. Verifikasi baris `Laptop Pro 16 {runId} - 1` masih tampil di tabel
60. Centang baris `Laptop Pro 16 {runId} - 1`
61. Klik tombol Bulk Action
62. Klik `Add Label`
63. Pilih label `Aset Kantor {runId}` pada dialog Add Label
64. Klik `[Apply]`
65. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil

### Switch Manage ditolak saat Grace
66. Muat ulang halaman
67. Ketik Search `{runId}`, tekan Enter
68. Klik `⋯` pada baris `Server Rack {runId} - 1`
69. Klik `Manage`
70. Verifikasi dialog `Switch Manage Asset` tampil karena Available license group `Cabang Medan {runId}` bernilai `0`
71. Centang baris `Printer Laser {runId} - 1` di dalam dialog
72. Klik `[Switch]`
73. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
74. Muat ulang halaman
75. Ketik Search `{runId}`, tekan Enter
76. Verifikasi baris `Server Rack {runId} - 1` tetap menampilkan status `Unmanaged`
77. Verifikasi baris `Printer Laser {runId} - 1` tidak menampilkan status `Unmanaged`
