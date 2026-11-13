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
  D-REG-24: [3, 5, 7, 58, 65, 68, 69, 72, 75]
  S-REG-30: [60, 62, 66]
  "§4.1#r16": [2, 76]
  "§5#r7": [32, 77]
  "§8#r5": [40, 77]
  "§8.3#p1": [4, 9, 10, 11, 13, 15, 33, 34, 35, 36, 37, 38, 39, 42, 43, 44, 46, 47, 48, 50, 51, 52, 54, 55, 56, 59]
  "§8.3#p2": [8, 9, 10, 11, 16, 17, 18, 19, 20, 21, 23, 25, 28, 30, 40]
  "§8.3#p3": [60, 62, 66]
anchor: [6, 12, 22, 24, 61, 74]
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
  - Nama singkat yang diharapkan: `Rina Wulandari` menjadi `Rina W.`, `Siti Nurbaya` menjadi `Siti N.`, `Dewi Anggraini` menjadi `Dewi A.`, `Budi Santoso` menjadi `Budi S.`. Nama singkat berakhir titik.
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
5. Verifikasi tombol `Prev` dan `Next` berikon panah `<` dan `>` tampil di header
6. Verifikasi ikon `[X]` tampil di pojok kanan-atas header
7. Verifikasi tombol teks `Close` tidak tampil
8. Verifikasi ringkasan tampil sebagai grid `Label: Value`
9. Verifikasi ringkasan memuat `Group` dengan nilai `Gudang 1`
10. Verifikasi ringkasan memuat `Requested By` dengan nilai `Rina W.`[^drift-1]
11. Verifikasi ringkasan memuat `Total Asset` dengan nilai `12`
12. Verifikasi ringkasan memuat `Status` dengan nilai `Draft`
13. Verifikasi baris Registration ID dan ikon salin tidak tampil

### Timeline dan format node batch Draft
14. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K1
15. Verifikasi timeline tampil kronologis dengan node terbaru di atas
16. Verifikasi node teratas berjudul `Draft edited by Rina W.`[^drift-1]
17. Verifikasi node berikutnya berjudul `Draft created by Rina W.`[^drift-1]
18. Verifikasi judul node tampil sebagai teks, bukan Badge
19. Verifikasi ikon user tampil di depan nama singkat pada judul node
20. Verifikasi waktu `09/11/26, 08:15` rata kanan di baris yang sama dengan judul node `Draft edited by Rina W.`[^drift-1]
21. Verifikasi waktu `08/11/26, 14:30` rata kanan di baris yang sama dengan judul node `Draft created by Rina W.`[^drift-1]
22. Verifikasi node `Draft created by Rina W.` memuat baris `Total Asset` dengan nilai `12`[^drift-1]
23. Verifikasi baris isi entri pada node `Draft edited by Rina W.` tidak tampil[^drift-1]
24. Verifikasi node `Draft edited by Rina W.` hanya memuat judul dan waktu[^drift-1]
25. Verifikasi baris `Requested By` terpisah pada node tidak tampil

### Nama lengkap tampil saat hover
26. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K1
27. Arahkan kursor ke nama `Rina W.` pada judul node `Draft created by Rina W.`[^drift-1]
28. Verifikasi tooltip `Rina Wulandari`
29. Arahkan kursor ke nama `Rina W.` pada ringkasan `Requested By`[^drift-1]
30. Verifikasi tooltip `Rina Wulandari`

### Pengajuan Waiting for Approval memuat Registration ID
31. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K3
32. Verifikasi judul `Registration Log`
33. Verifikasi Badge status `Waiting for Approval` dengan severity `primary` di samping judul
34. Verifikasi baris `REG-20261109-00001` tampil di bawah judul
35. Verifikasi ikon salin tampil di samping `REG-20261109-00001`
36. Verifikasi ringkasan memuat `Group` dengan nilai `Gudang 2`
37. Verifikasi ringkasan memuat `Requested By` dengan nilai `Siti N.`[^drift-1]
38. Verifikasi ringkasan memuat `Total Asset` dengan nilai `5`
39. Verifikasi ringkasan memuat `Status` dengan nilai `Waiting for Approval`
40. Verifikasi node teratas berjudul `Submitted by Siti N.`[^drift-1]

### Badge status Approved
41. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K4
42. Verifikasi Badge status `Approved` dengan severity `success` di samping judul
43. Verifikasi ringkasan memuat `Status` dengan nilai `Approved`
44. Verifikasi node teratas berjudul `Approved by Dewi A.`[^drift-1]

### Badge status Partially Approved
45. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K5
46. Verifikasi Badge status `Partially Approved` dengan severity `warning` di samping judul
47. Verifikasi ringkasan memuat `Status` dengan nilai `Partially Approved`
48. Verifikasi node teratas berjudul `Partially approved by Dewi A.`[^drift-1]

### Badge status Rejected
49. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K6
50. Verifikasi Badge status `Rejected` dengan severity `danger` di samping judul
51. Verifikasi ringkasan memuat `Status` dengan nilai `Rejected`
52. Verifikasi node teratas berjudul `Rejected by Dewi A.`[^drift-1]

### Badge status Canceled
53. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K7
54. Verifikasi Badge status `Canceled` dengan severity `dark` di samping judul
55. Verifikasi ringkasan memuat `Status` dengan nilai `Canceled`
56. Verifikasi node teratas berjudul `Canceled by Siti N.`[^drift-1]

### Empty state tanpa peristiwa
57. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K2
58. Verifikasi judul `Registration Log`
59. Verifikasi ringkasan memuat `Group` dengan nilai `Gudang 7`
60. Verifikasi teks `No history yet`
61. Verifikasi teks `Activity for this registration will appear here.`
62. Verifikasi node timeline tidak tampil

### Prev dan Next berpindah antar baris tabel
63. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K1
64. Klik `Next`
65. Verifikasi ringkasan memuat `Group` dengan nilai `Gudang 7`
66. Verifikasi teks `No history yet`
67. Klik `Prev`
68. Verifikasi ringkasan memuat `Group` dengan nilai `Gudang 1`
69. Verifikasi node teratas berjudul `Draft edited by Rina W.`[^drift-1]

### Dialog ditutup hanya lewat ikon X
70. Tampilkan Dialog `Registration Log` (`D-REG-24`) dengan kondisi K1
71. Klik area backdrop di luar dialog
72. Verifikasi dialog `Registration Log` tetap tampil
73. Klik `[X]`
74. Verifikasi tabel sub tab Draft tampil kembali setelah dialog `Registration Log` ditutup
75. Verifikasi dialog `Registration Log` tidak tampil
76. Verifikasi aksi `Registration Log` tampil pada baris `Gudang 1`
77. Verifikasi aksi `Changelog` tidak tampil pada baris `Gudang 1`

[^drift-1]: Drift PRD vs foundation vs override. PRD §8.3: judul node dan ringkasan memuat nama singkat user. foundation `prd-conventions.md` §9.13: nama singkat `[First Name] [Last Initial]`, contoh tanpa titik (`John L`, `Alexander G`). Override O-4: nama singkat mengakhiri inisial dengan titik (`John L.`, `Alexander G.`). Diasersi: O-4, karena override menang atas foundation (SB-6).
