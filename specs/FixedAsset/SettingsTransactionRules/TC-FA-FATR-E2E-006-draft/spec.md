---
id: TC-FA-FATR-E2E-006-draft
title: "Draft Settings bertahan lintas node dan dijaga dialog Unsaved Changes"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2#b4", "§4.2#r1", "§4.2#r2", "§4.2#r3", "§4.2#r4", "§4.2#r5", "§4.2#r6", "§9.2#b3", "§9.2#b27", "§9.2#b30", "§9.4.2#r15", "§9.5#r16", "§9.5#r17"]
smoke: []
dependsOn: []
trace:
  "§4.2#b4": 11
  "§4.2#r1": [33, 37, 71, 73, 77, 80]
  "§4.2#r2": 34
  "§4.2#r3": 35
  "§4.2#r4": [42, 45]
  "§4.2#r5": [54, 55]
  "§4.2#r6": [64, 65]
  "§9.2#b3": 11
  "§9.2#b27": [16, 18, 21]
  "§9.2#b30": 30
  "§9.4.2#r15": 11
  "§9.5#r16": 40
  "§9.5#r17": [39, 40]
coverage:
  web: automated
---

# Draft Settings bertahan lintas node dan dijaga dialog Unsaved Changes

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-006-1: Category leaf `Conveyor {runId}`, tanpa sub-Category, ada di entitas aktor. Semua field Inherit.
  - DU-006-2: Category leaf `Pallet {runId}`, tanpa sub-Category, ada di entitas aktor. Semua field Inherit.
- Kondisi:
  - Company default entitas aktor bernilai bawaan: Max duration `14`, Max extensions `1`, Max assets per assignee (concurrent) `0`.
  - Halaman dibuka dari halaman lain di aplikasi, sehingga riwayat browser memuat halaman sebelumnya.

## Test Steps

### Perubahan yang belum disimpan tetap di draft saat pindah node
1. Ketik Search Sidebar Category Tree `Conveyor {runId}`, tekan Enter
2. Klik Category leaf `Conveyor {runId}`
3. Klik `[Set own value]` pada field `Max duration`
4. Isi `Max duration` `20`
5. Ganti isi kotak search Sidebar Category Tree dengan `Pallet {runId}`, tekan Enter
6. Klik Category leaf `Pallet {runId}`
7. Klik `[Set own value]` pada field `Max extensions`
8. Isi `Max extensions` `3`
9. Ganti isi kotak search Sidebar Category Tree dengan `Conveyor {runId}`, tekan Enter
10. Klik Category leaf `Conveyor {runId}`
11. Verifikasi field `Max duration` bernilai `20`

### Reset to Default hanya memengaruhi node dan tab yang sedang dilihat
12. Klik tab `Assign`
13. Klik `[Set own value]` pada field `Max assets per assignee (concurrent)`
14. Isi `Max assets per assignee (concurrent)` `7`
15. Klik `[Reset to Default]`
16. Verifikasi field `Max assets per assignee (concurrent)` menampilkan teks `Inherit — Unlimited (from Company default)`
17. Klik tab `Borrow`
18. Verifikasi field `Max duration` bernilai `20`
19. Ganti isi kotak search Sidebar Category Tree dengan `Pallet {runId}`, tekan Enter
20. Klik Category leaf `Pallet {runId}`
21. Verifikasi field `Max extensions` bernilai `3`

### Draft tidak valid di node atau tab lain membuka node dan tab pertama yang tidak valid
22. Klik tab `Assign`
23. Klik `[Set own value]` pada field `Max assets per assignee (concurrent)`
24. Kosongkan `Max assets per assignee (concurrent)`
25. Ganti isi kotak search Sidebar Category Tree dengan `Conveyor {runId}`, tekan Enter
26. Klik Category leaf `Conveyor {runId}`
27. Klik tab `Borrow`
28. Kosongkan kotak Search Sidebar Category Tree, tekan Enter
29. Klik `[Save]`
30. Verifikasi node `Pallet {runId}` terpilih dan tab `Assign` aktif
31. Isi `Max assets per assignee (concurrent)` `7`

### Dialog Unsaved Changes mencegat perpindahan route
32. Klik tombol Back browser
33. Verifikasi dialog `Unsaved Changes` tampil
34. Verifikasi body `You have unsaved changes. Are you sure you want to leave?`
35. Verifikasi tombol `[Cancel]` dan `[Leave]` tampil pada dialog Unsaved Changes
36. Klik `[Cancel]` pada dialog Unsaved Changes
37. Verifikasi field `Max assets per assignee (concurrent)` bernilai `7`

### Menu sidebar Transaction Settings tidak memuat ulang halaman dan tidak mengubah draft
38. Klik menu sidebar `Transaction Settings`
39. Verifikasi node `Pallet {runId}` terpilih dan tab `Assign` aktif
40. Verifikasi field `Max assets per assignee (concurrent)` bernilai `7`

### Muat ulang dan tutup tab memakai konfirmasi bawaan browser
41. Muat ulang halaman
42. Verifikasi konfirmasi bawaan browser untuk meninggalkan halaman tampil
43. Tolak konfirmasi bawaan browser
44. Tutup tab browser
45. Verifikasi konfirmasi bawaan browser untuk meninggalkan halaman tampil
46. Tolak konfirmasi bawaan browser

### Draft yang kembali ke nilai tersimpan tidak mencegat navigasi
47. Klik `[Reset to inherit]` pada field `Max assets per assignee (concurrent)`
48. Klik tab `Borrow`
49. Klik `[Reset to inherit]` pada field `Max extensions`
50. Ketik Search Sidebar Category Tree `Conveyor {runId}`, tekan Enter
51. Klik Category leaf `Conveyor {runId}`
52. Klik `[Reset to inherit]` pada field `Max duration`
53. Klik tombol Back browser
54. Verifikasi halaman Transaction Settings tidak lagi tampil
55. Verifikasi dialog `Unsaved Changes` tidak tampil
56. Klik tombol Forward browser

### Guard dilepas sesudah Save sukses
57. Ketik Search Sidebar Category Tree `Conveyor {runId}`, tekan Enter
58. Klik Category leaf `Conveyor {runId}`
59. Klik `[Set own value]` pada field `Max duration`
60. Isi `Max duration` `25`
61. Klik `[Save]`
62. Klik `[Save]` pada dialog Save Changes
63. Klik tombol Back browser
64. Verifikasi halaman Transaction Settings tidak lagi tampil
65. Verifikasi dialog `Unsaved Changes` tidak tampil

### Dialog Unsaved Changes mencegat menu sidebar halaman lain dan Leave melanjutkan navigasi
66. Klik tombol Forward browser
67. Ketik Search Sidebar Category Tree `Conveyor {runId}`, tekan Enter
68. Klik Category leaf `Conveyor {runId}`
69. Isi `Max duration` `30`
70. Klik menu sidebar `Dashboard`
71. Verifikasi dialog `Unsaved Changes` tampil
72. Klik `[Leave]` pada dialog Unsaved Changes
73. Verifikasi halaman Transaction Settings tidak lagi tampil
74. Klik tombol Back browser
75. Ketik Search Sidebar Category Tree `Conveyor {runId}`, tekan Enter
76. Klik Category leaf `Conveyor {runId}`
77. Verifikasi field `Max duration` bernilai `25`

### Dialog Unsaved Changes mencegat tombol Forward browser
78. Isi `Max duration` `30`
79. Klik tombol Forward browser
80. Verifikasi dialog `Unsaved Changes` tampil
81. Klik `[Cancel]` pada dialog Unsaved Changes
