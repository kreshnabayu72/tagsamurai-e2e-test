---
id: TC-FA-FAREG-E2E-085-gating-total-control
title: "Gating Total Control"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§4.1#r1", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r17"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [7, 20]
  "§4.1#r1": 2
  "§4.8#r1": 2
  "§4.8#r2": 3
  "§4.8#r3": 4
  "§4.8#r4": 26
  "§4.8#r5": [10, 12]
  "§4.8#r6": 8
  "§4.8#r7": [30, 39]
  "§4.8#r8": 9
  "§4.8#r9": [32, 59]
  "§4.8#r10": 41
  "§4.8#r11": [44, 46, 48, 49, 52]
  "§4.8#r12": [35, 61]
  "§4.8#r13": [18, 22, 25]
  "§4.8#r14": 5
  "§4.8#r17": [15, 31, 40]
anchor: [34]
coverage:
  web: automated
---

# Gating Total Control

## Prerequisites
- Aktor: Agus P (Total Control, seluruh client).
- Layar awal: Fixed Asset > Assets.
- Data:
  - DU-085-1: Batch Draft dengan Group `Gudang 1 {runId}`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`, Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `12`.
  - DU-085-2: Pengajuan Waiting for Approval `REG-20261109-08502` di Group `Gudang 1 {runId}`, diajukan Rina W, Total Asset `5`, Last Updated `T0 − 2 hari` (Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `5`, TAG `Verified`).
  - DU-085-3: Pengajuan Approved `REG-20261108-08503` di Group `Gudang 1 {runId}`, diajukan Rina W, Approver Agus P, Total Asset `3`, Last Updated `T0 − 3 hari`.
  - DU-085-4: Agus P (Total Control, seluruh client).
  - DU-085-5: Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`).
  - DU-085-6: Pengajuan Waiting for Approval di Group `Gudang 2 {runId}`, diajukan Agus P, Total Asset `2`, Last Updated `T0 − 1 hari` (Item `Monitor` Brand `Dell` Model `P2422H` Quantity `2`).
- Kondisi:
  - Group `Gudang 1 {runId}` dan Group `Gudang 2 {runId}` ber-toggle `Require Approval for Registration` ON.
  - Kunci sesi edit batch DU-085-1 sedang dipegang Rina W.

## Test Steps

### Tab Registration dan sub tab Draft tampil
1. Klik tab `Registration`
2. Verifikasi tab `Registration` tampil
3. Verifikasi sub tab `Draft` tampil
4. Verifikasi `[+ Register Asset]` tampil pada toolbar sub tab `Draft`
5. Verifikasi `Download` tampil pada toolbar sub tab `Draft`

### Total Control melihat dan menindak batch Draft
6. Ketik Search `Gudang 1 {runId}`, tekan Enter
7. Verifikasi baris Group `Gudang 1 {runId}` dengan Requested By `Rina W` tampil di sub tab `Draft` bagi Total Control
8. Verifikasi row action `Edit` tampil pada baris `Gudang 1 {runId}`
9. Verifikasi row action `Registration Log` tampil pada baris `Gudang 1 {runId}`
10. Verifikasi row action `Delete` tampil pada baris `Gudang 1 {runId}`
11. Centang baris `Gudang 1 {runId}`
12. Verifikasi Bulk Action `Delete` tampil
13. Hilangkan centang baris `Gudang 1 {runId}`

### Registration Log terbuka sebagai dialog read-only
14. Klik row action `Registration Log` pada baris `Gudang 1 {runId}`
15. Verifikasi dialog `Registration Log` terbuka
16. Tutup dialog lewat ikon X

### Edit batch Draft: Take over, Remove from List, Bulk Scan, dan Submit tampil
17. Klik row action `Edit` pada baris `Gudang 1 {runId}`
18. Verifikasi dialog `Draft Is Being Edited` tampil dengan tombol `[Take over]`
19. Klik `[Take over]`
20. Verifikasi form `Register Asset` terbuka dalam mode Edit untuk batch `Gudang 1 {runId}` bagi Total Control
21. Buka row option pada baris Item `Laptop` di tab `General Information`
22. Verifikasi row option `Remove from List` tampil
23. Tutup menu row option
24. Klik tab `Asset`
25. Verifikasi tombol `Bulk Scan` tampil pada Item `Laptop`
26. Verifikasi tombol `[Submit]` tampil pada footer form
27. Klik `[Cancel]` pada footer form yang belum diubah, tanpa dialog Unsaved Changes

### Sub tab Waiting for Approval dan Detail pengajuan
28. Klik sub tab `Waiting for Approval`
29. Ketik Search `Gudang 1 {runId}`, tekan Enter
30. Verifikasi row action `Detail` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `5`
31. Verifikasi row action `Registration Log` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `5`
32. Verifikasi row action `Cancel registration` tidak tampil pada baris pengajuan `Rina W`
33. Klik row action `Detail` pada baris Group `Gudang 1 {runId}` dengan Total Asset `5`
34. Verifikasi tombol `[Close]` tampil pada footer halaman Detail pengajuan bagi Total Control
35. Verifikasi tombol `[Cancel Registration]` tidak tampil pada halaman Detail pengajuan
36. Klik `[Close]`

### Sub tab History
37. Klik sub tab `History`
38. Ketik Search `Gudang 1 {runId}`, tekan Enter
39. Verifikasi row action `Detail` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `3`
40. Verifikasi row action `Registration Log` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `3`

### Menu Approvals > Registration dan halaman Approval tampil bagi Total Control
41. Verifikasi menu `Approvals` > `Registration` tampil pada sidebar
42. Klik menu `Approvals` > `Registration`
43. Ketik Search `Gudang 1 {runId}`, tekan Enter
44. Verifikasi row action `Review` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `5`
45. Klik row action `Review` pada baris Group `Gudang 1 {runId}` dengan Total Asset `5`
46. Verifikasi kolom Decision tampil dengan nilai `Approve` pada aset ke-1 grup `Laptop`
47. Centang aset ke-1 pada grup `Laptop`
48. Verifikasi Bulk Action dengan pilihan `Approve`, `Return to Draft`, dan `Reject` tampil
49. Verifikasi tombol `[Submit]` tampil pada footer halaman Approval
50. Buka row option pada aset ke-1 grup `Laptop`
51. Klik `Edit`
52. Verifikasi panel koreksi tampil
53. Klik `Close` pada panel koreksi yang belum diubah
54. Klik `[Cancel]` pada footer halaman Approval yang Decision dan isian panelnya belum diubah, tanpa dialog Unsaved Changes

### Total Control sebagai pengaju: Cancel registration tampil
55. Buka layar Fixed Asset > Assets
56. Klik tab `Registration`
57. Klik sub tab `Waiting for Approval`
58. Ketik Search `Gudang 2 {runId}`, tekan Enter
59. Verifikasi row action `Cancel registration` tampil pada baris Group `Gudang 2 {runId}` yang diajukan Agus P
60. Klik row action `Detail` pada baris Group `Gudang 2 {runId}`
61. Verifikasi tombol `[Cancel Registration]` tampil pada halaman Detail pengajuan bagi Total Control sebagai pengaju
62. Klik `[Close]`
