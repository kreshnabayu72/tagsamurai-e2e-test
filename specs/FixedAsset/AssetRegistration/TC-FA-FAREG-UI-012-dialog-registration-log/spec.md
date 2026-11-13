---
id: TC-FA-FAREG-UI-012-dialog-registration-log
title: "Dialog Registration Log: struktur, ringkasan, dan empty state"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["D-REG-24", "S-REG-30", "§4.1#r16", "§5#r7", "§8#r5", "§8.3#p1", "§8.3#p2", "§8.3#p3"]
smoke: []
dependsOn: []
trace:
  D-REG-24: [3, 5, 7, 53, 60, 63, 64, 67, 70]
  S-REG-30: [55, 57, 61]
  "§4.1#r16": [2, 71]
  "§5#r7": [27, 72]
  "§8#r5": [35, 72]
  "§8.3#p1": [4, 8, 9, 10, 12, 14, 28, 29, 30, 31, 32, 33, 34, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 54]
  "§8.3#p2": [8, 9, 10, 15, 16, 17, 18, 20, 22, 25, 35]
  "§8.3#p3": [55, 57, 61]
anchor: [6, 11, 19, 21, 56, 69]
coverage:
  web: automated
---

# Dialog Registration Log: struktur, ringkasan, dan empty state

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Komponen: Dialog `Registration Log` (`D-REG-24`)
- Data:
  - DU-012-1: batch Draft Group `Gudang 1`, Total Asset `12`, Requested By `Rina Wulandari`, Status `Draft`, tanpa Registration ID, Last Updated `2026-11-09T08:15:00Z`; peristiwa: `Draft edited by Rina Wulandari` pada `2026-11-09T08:15:00Z` dan `Draft created by Rina Wulandari` pada `2026-11-08T14:30:00Z` dengan Total Asset `12`.
  - DU-012-2: batch Draft Group `Gudang 7`, Total Asset `3`, Requested By `Budi Santoso`, Status `Draft`, tanpa Registration ID, Last Updated `2026-11-02T08:00:00Z`; tanpa peristiwa.
  - DU-012-3: pengajuan Waiting for Approval Registration ID `REG-20261109-00001`, Group `Gudang 2`, Total Asset `5`, Requested By `Siti Nurbaya`; peristiwa: `Submitted by Siti Nurbaya` pada `2026-11-09T10:00:00Z`.
  - DU-012-4: pengajuan History Registration ID `REG-20261105-00007`, Group `Kantor Pusat`, Total Asset `30`, Requested By `Agus Prasetyo`, Status `Approved`; peristiwa: `Approved by Dewi Anggraini` pada `2026-11-06T09:00:00Z`.
  - DU-012-5: pengajuan History Registration ID `REG-20261104-00003`, Group `Gudang 3`, Total Asset `8`, Requested By `Agus Prasetyo`, Status `Partially Approved`; peristiwa: `Partially approved by Dewi Anggraini` pada `2026-11-05T09:00:00Z`.
  - DU-012-6: pengajuan History Registration ID `REG-20261103-00002`, Group `Gudang 4`, Total Asset `6`, Requested By `Agus Prasetyo`, Status `Rejected`; peristiwa: `Rejected by Dewi Anggraini` pada `2026-11-04T09:00:00Z`.
  - DU-012-7: pengajuan History Registration ID `REG-20261102-00001`, Group `Gudang 5`, Total Asset `4`, Requested By `Siti Nurbaya`, Status `Canceled`; peristiwa: `Canceled by Siti Nurbaya` pada `2026-11-03T09:00:00Z`.
  - Nama singkat yang diharapkan: `Rina Wulandari` menjadi `Rina W`, `Siti Nurbaya` menjadi `Siti N`, `Dewi Anggraini` menjadi `Dewi A`, `Budi Santoso` menjadi `Budi S`.
  - Waktu node yang diharapkan dengan Date Format `dd/MM/yy` dan Time Format `24h`: `09/11/26, 08:15` dari `2026-11-09T08:15:00Z`; `08/11/26, 14:30` dari `2026-11-08T14:30:00Z`.
- Kondisi:
  - K1: dialog dibuka dari row action `Registration Log` pada baris `Gudang 1` (DU-012-1) di sub tab Draft; daftar Draft berisi DU-012-1 lalu DU-012-2 sebagai baris berikutnya; Date Format General Settings `dd/MM/yy`, Time Format `24h`, Time Zone `UTC`.
  - K2: dialog dibuka dari baris `Gudang 7` (DU-012-2) di sub tab Draft; daftar sama dengan K1.
  - K3: dialog dibuka dari baris DU-012-3 di sub tab Waiting for Approval.
  - K4: dialog dibuka dari baris DU-012-4 di sub tab History.
  - K5: dialog dibuka dari baris DU-012-5 di sub tab History.
  - K6: dialog dibuka dari baris DU-012-6 di sub tab History.
  - K7: dialog dibuka dari baris DU-012-7 di sub tab History.

## Test Steps

### Struktur dialog untuk batch Draft
1. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K1
2. Verifikasi dialog berukuran MD
3. Verifikasi judul `Registration Log`
4. Verifikasi Badge status `Draft` dengan severity `dark` di samping judul
5. Verifikasi tombol `Prev` dan `Next` tampil di header
6. Verifikasi ikon `[X]` tampil di pojok kanan-atas header
7. Verifikasi tombol teks `Close` tidak tampil
8. Verifikasi ringkasan memuat `Group` dengan nilai `Gudang 1`
9. Verifikasi ringkasan memuat `Requested By`
10. Verifikasi ringkasan memuat `Total Asset` dengan nilai `12`
11. Verifikasi ringkasan memuat `Status` dengan nilai `Draft`
12. Verifikasi baris Registration ID dan ikon salin tidak tampil

### Timeline dan format node batch Draft
13. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K1
14. Verifikasi timeline tampil kronologis dengan node terbaru di atas
15. Verifikasi node teratas berjudul `Draft edited by Rina W`
16. Verifikasi node berikutnya berjudul `Draft created by Rina W`
17. Verifikasi node `Draft edited by Rina W` menampilkan waktu `09/11/26, 08:15`
18. Verifikasi node `Draft created by Rina W` menampilkan waktu `08/11/26, 14:30`
19. Verifikasi node `Draft created by Rina W` memuat baris `Total Asset` dengan nilai `12`
20. Verifikasi baris isi entri pada node `Draft edited by Rina W` tidak tampil
21. Verifikasi node `Draft edited by Rina W` hanya memuat judul dan waktu
22. Verifikasi baris `Requested By` terpisah pada node tidak tampil

### Nama lengkap tampil saat hover
23. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K1
24. Arahkan kursor ke nama `Rina W` pada judul node `Draft created by Rina W`
25. Verifikasi tooltip `Rina Wulandari`

### Pengajuan Waiting for Approval memuat Registration ID
26. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K3
27. Verifikasi judul `Registration Log`
28. Verifikasi Badge status `Waiting for Approval` dengan severity `primary` di samping judul
29. Verifikasi baris `REG-20261109-00001` tampil di bawah judul
30. Verifikasi ikon salin tampil di samping `REG-20261109-00001`
31. Verifikasi ringkasan memuat `Group` dengan nilai `Gudang 2`
32. Verifikasi ringkasan memuat `Requested By` dengan nilai `Siti N`
33. Verifikasi ringkasan memuat `Total Asset` dengan nilai `5`
34. Verifikasi ringkasan memuat `Status` dengan nilai `Waiting for Approval`
35. Verifikasi node teratas berjudul `Submitted by Siti N`

### Badge status Approved
36. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K4
37. Verifikasi Badge status `Approved` dengan severity `success` di samping judul
38. Verifikasi ringkasan memuat `Status` dengan nilai `Approved`
39. Verifikasi node teratas berjudul `Approved by Dewi A`

### Badge status Partially Approved
40. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K5
41. Verifikasi Badge status `Partially Approved` dengan severity `warning` di samping judul
42. Verifikasi ringkasan memuat `Status` dengan nilai `Partially Approved`
43. Verifikasi node teratas berjudul `Partially approved by Dewi A`

### Badge status Rejected
44. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K6
45. Verifikasi Badge status `Rejected` dengan severity `danger` di samping judul
46. Verifikasi ringkasan memuat `Status` dengan nilai `Rejected`
47. Verifikasi node teratas berjudul `Rejected by Dewi A`

### Badge status Canceled
48. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K7
49. Verifikasi Badge status `Canceled` dengan severity `dark` di samping judul
50. Verifikasi ringkasan memuat `Status` dengan nilai `Canceled`
51. Verifikasi node teratas berjudul `Canceled by Siti N`

### Empty state tanpa peristiwa
52. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K2
53. Verifikasi judul `Registration Log`
54. Verifikasi ringkasan memuat `Group` dengan nilai `Gudang 7`
55. Verifikasi teks `No history yet`
56. Verifikasi teks `Activity for this registration will appear here.`
57. Verifikasi node timeline tidak tampil

### Prev dan Next berpindah antar baris tabel
58. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K1
59. Klik `Next`
60. Verifikasi ringkasan memuat `Group` dengan nilai `Gudang 7`
61. Verifikasi teks `No history yet`
62. Klik `Prev`
63. Verifikasi ringkasan memuat `Group` dengan nilai `Gudang 1`
64. Verifikasi node teratas berjudul `Draft edited by Rina W`

### Dialog ditutup hanya lewat ikon X
65. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K1
66. Klik area backdrop di luar dialog
67. Verifikasi dialog `Registration Log` tetap tampil
68. Klik `[X]`
69. Verifikasi tabel sub tab Draft tampil kembali setelah dialog `Registration Log` ditutup
70. Verifikasi dialog `Registration Log` tidak tampil
71. Verifikasi aksi `Registration Log` tampil pada baris `Gudang 1`
72. Verifikasi aksi `Changelog` tidak tampil pada baris `Gudang 1`
