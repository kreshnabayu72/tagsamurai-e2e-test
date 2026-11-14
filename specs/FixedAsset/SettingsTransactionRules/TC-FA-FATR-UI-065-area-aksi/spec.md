---
id: TC-FA-FATR-UI-065-area-aksi
title: "Area utama: Set own value, Reset to inherit, Reset to Default, dan tombol Save"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - §4.1#r118
  - §4.1#r218
  - §4.1#r219
  - §4.1#r221
  - §4.1#r223
  - §4.1#r224
  - §4.1#r227
  - §4.1#r228
  - §4.2#r5
  - §4.3#r2
  - §4.3#r6
  - §4.4#r3
  - §4.4#r4
  - §4.4#r5
  - §4.4#r6
  - AU-BAGIAN-asampaiAU-BAGIAN-o,AU-NILAI-asampaiAU-NILAI-j,AU-TOOLTIP-asampaiAU-TOOLTIP-d
  - §9.2#b26
  - §9.2#b27
  - §9.4.2#r97
  - §9.4.2#r98
  - §9.4.2#r99
  - §9.4.4#r4
  - §9.10.1#b4
  - §9.10.2#b4
  - §9.10.3#b4
  - EB-TBL-5@tombol-save
  - EB-TBL-5@tombol-reset-to-default
smoke: []
dependsOn: []
trace:
  §4.1#r118: [53, 54, 55]
  §4.1#r218: [47, 48]
  §4.1#r219: 29
  §4.1#r221: 23
  §4.1#r223: 16
  §4.1#r224: [6, 19]
  §4.1#r227: [27, 28, 34, 38, 39]
  §4.1#r228: [41, 44]
  §4.2#r5: [10, 21]
  §4.3#r2: [4, 5]
  §4.3#r6: 2
  §4.4#r3: [4, 6]
  §4.4#r4: 9
  §4.4#r5: [25, 26, 47]
  §4.4#r6: 16
  AU-BAGIAN-asampaiAU-BAGIAN-o,AU-NILAI-asampaiAU-NILAI-j,AU-TOOLTIP-asampaiAU-TOOLTIP-d: [25, 26, 43]
  §9.2#b26: [14, 81]
  §9.2#b27: [31, 36, 50]
  §9.4.2#r97: [59, 65, 71]
  §9.4.2#r98: [59, 65, 66, 71]
  §9.4.2#r99: [60, 61, 67, 72]
  §9.4.4#r4: 61
  §9.10.1#b4: [57, 59]
  §9.10.2#b4: [63, 65, 66]
  §9.10.3#b4: [69, 71]
  EB-TBL-5@tombol-save: [74, 76]
  EB-TBL-5@tombol-reset-to-default: [77, 79]
anchor: []
coverage:
  web: automated
---

# Area utama: Set own value, Reset to inherit, Reset to Default, dan tombol Save

## Prerequisites
- Aktor: Total Control; Read Only pada K11.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-065-1: Pengaturan Category leaf `Machinery` tab Borrow: semua field Inherit, Company default Max duration `14` dengan Duration unit `Days`.
  - DU-065-2: Pengaturan Company default tab Borrow pada All categories sama dengan nilai awal: Max duration `14`.
  - DU-065-3: Pengaturan tab Borrow pada All categories: Max duration `30`, Max extensions `3`, Transaction timeout `10`, Send email notifications `OFF`; tab Transfer: In-transit overdue after `10`.
  - DU-065-4: Pengaturan Company default pada All categories: tab Transfer Change Cost Center with Group `Always`; tab Damaged & Missing Long missing after `60` dan After photo required `ON`.
  - DU-065-5: Pengaturan Company default tab Borrow pada All categories: Allow Borrow `Deny`, Max duration `30`.
  - DU-065-6: Pengaturan Category leaf `Machinery`: tab Borrow Max duration bernilai sendiri `21` dan Max extensions bernilai sendiri `2`; tab Assign Max assets per assignee (concurrent) bernilai sendiri `5`.
  - DU-065-7: Pengaturan Company default tab Assign pada All categories: Allowed assignee: Employee `OFF`, Allowed assignee: Division `ON`, Max assets per assignee (concurrent) `5`.
  - DU-065-8: Pengaturan Company default tab Assign pada All categories: Require approval tersimpan `ON`, Max assets per assignee (concurrent) `5`.
  - DU-065-9: Pengaturan Company default tab Borrow pada All categories: Duration unit tersimpan `Hours`, Self service tersimpan `ON`, Max duration `30`.
  - DU-065-10: Pengaturan Company default tab Assign pada All categories: Direct handover between holders tersimpan `Deny`, Max assets per assignee (concurrent) `5`.
  - DU-065-11: Nilai Max duration yang dicoba: `20`.
  - DU-065-12: Draft perubahan di node Category leaf `Machinery`: tab Borrow Max duration bernilai sendiri `20`. Node All categories yang dilihat tidak punya draft perubahan.
- Kondisi:
  - K1: node Category leaf `Machinery` terpilih, tab Borrow aktif, nilai memakai DU-065-1.
  - K2: node All categories terpilih, tab Borrow aktif, nilai memakai DU-065-2.
  - K3: node All categories terpilih, tab Borrow aktif, nilai memakai DU-065-3.
  - K4: node All categories terpilih, tab Transfer aktif, nilai memakai DU-065-4.
  - K5: node All categories terpilih, tab Borrow aktif, nilai memakai DU-065-5.
  - K6: node Category leaf `Machinery` terpilih, tab Borrow aktif, nilai memakai DU-065-6.
  - K7: node All categories terpilih, tab Assign aktif, nilai memakai DU-065-7.
  - K8: node All categories terpilih, tab Assign aktif, Approval Workflow tidak tersedia di plan, nilai memakai DU-065-8.
  - K9: node All categories terpilih, tab Borrow aktif, level Feature Suite Borrowing Basic, nilai memakai DU-065-9.
  - K10: node All categories terpilih, tab Assign aktif, level Feature Suite Assignment Basic, nilai memakai DU-065-10.
  - K11: aktor Read Only, node All categories terpilih, tab Borrow aktif, nilai Company default memakai DU-065-2.
  - K12: node All categories terpilih, tab Borrow aktif, nilai Company default memakai DU-065-2, draft perubahan ada di node Category leaf `Machinery` sesuai DU-065-12.

## Test Steps

### Set own value dan Reset to inherit pada Category
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi tombol `Save` disabled karena belum ada perubahan
3. Klik `Set own value` pada `Max duration`
4. Verifikasi `Max duration` menjadi kontrol aktif yang terisi nilai warisan `14`
5. Verifikasi tombol `Reset to inherit` tampil pada baris `Max duration`
6. Verifikasi tombol `Save` aktif karena nilai sendiri yang sama dengan nilai warisan tetap perubahan
7. Ganti `Max duration` menjadi `20`
8. Klik `Reset to inherit` pada `Max duration`
9. Verifikasi `Max duration` kembali menampilkan `Inherit — 14 days (from Company default)`
10. Verifikasi tombol `Save` kembali disabled karena draft sama dengan nilai tersimpan

### Save aktif lintas tab dan membuka dialog Save Changes
11. Tampilkan Area utama dengan kondisi K1
12. Klik `Set own value` pada `Max duration`
13. Klik tab `Assign`
14. Verifikasi tombol `Save` tetap aktif pada tab `Assign`
15. Klik `Save`
16. Verifikasi dialog `Save Changes` tampil

### Draft kembali clean di All categories
17. Tampilkan Area utama dengan kondisi K2
18. Ganti `Max duration` menjadi `20`
19. Verifikasi tombol `Save` aktif
20. Ganti `Max duration` menjadi `14`
21. Verifikasi tombol `Save` disabled karena nilai dikembalikan ke nilai semula

### Reset to Default di All categories
22. Tampilkan Area utama dengan kondisi K3
23. Verifikasi tombol `Reset to Default` aktif
24. Klik `Reset to Default`
25. Verifikasi `Max duration` kembali ke nilai awal `14`
26. Verifikasi `Max extensions` kembali ke nilai awal `1`
27. Verifikasi `Transaction timeout` kembali ke nilai awal `7`
28. Verifikasi `Send email notifications` kembali ke nilai awal `ON`
29. Verifikasi tombol `Save` aktif karena perubahan masuk draft
30. Klik tab `Transfer`
31. Verifikasi `In-transit overdue after` tetap bernilai `10` pada tab yang tidak sedang dilihat saat Reset to Default

### Reset to Default pada field khusus All categories di tab Transfer dan Damaged & Missing
32. Tampilkan Area utama dengan kondisi K4
33. Klik `Reset to Default`
34. Verifikasi `Change Cost Center with Group` kembali ke nilai awal `Never`
35. Klik tab `Damaged & Missing`
36. Verifikasi `Long missing after` tetap bernilai `60` pada tab yang tidak sedang dilihat saat Reset to Default
37. Klik `Reset to Default`
38. Verifikasi `Long missing after` kembali ke nilai awal `30`
39. Verifikasi `After photo required` kembali ke nilai awal `OFF`

### Reset to Default mengembalikan nilai bagian yang disembunyikan karena Deny
40. Tampilkan Area utama dengan kondisi K5
41. Verifikasi `Allow Borrow` bernilai `Deny`
42. Klik `Reset to Default`
43. Verifikasi `Allow Borrow` kembali ke nilai awal `Allow`
44. Verifikasi `Max duration` pada bagian yang sebelumnya tersembunyi kembali ke nilai awal `14`

### Reset to Default di Category leaf
45. Tampilkan Area utama dengan kondisi K6
46. Klik `Reset to Default`
47. Verifikasi `Max duration` setelah Reset to Default menampilkan `Inherit — 14 days (from Company default)`
48. Verifikasi `Max extensions` kembali menampilkan teks `Inherit`
49. Klik tab `Assign`
50. Verifikasi `Max assets per assignee (concurrent)` tetap bernilai sendiri `5` pada tab yang tidak sedang dilihat saat Reset to Default

### Reset to Default tidak menghasilkan Allowed assignee keduanya OFF
51. Tampilkan Area utama dengan kondisi K7
52. Klik `Reset to Default`
53. Verifikasi `Allowed assignee: Employee` kembali bernilai `ON`
54. Verifikasi `Allowed assignee: Division` tetap bernilai `ON` setelah Reset to Default
55. Verifikasi pesan `At least one assignee type must be enabled` tidak ada

### Reset to Default tidak menyentuh field bergerbang Approval Workflow
56. Tampilkan Area utama dengan kondisi K8
57. Verifikasi `Require approval` disabled dengan nilai tersimpan `ON`
58. Klik `Reset to Default`
59. Verifikasi `Require approval` tetap bernilai `ON`
60. Verifikasi `Max assets per assignee (concurrent)` kembali ke nilai awal `0`
61. Verifikasi tombol `Save` aktif karena perubahan lain masuk draft

### Reset to Default tidak menyentuh field bergerbang Borrowing
62. Tampilkan Area utama dengan kondisi K9
63. Verifikasi `Duration unit` disabled dengan nilai tersimpan `Hours`
64. Klik `Reset to Default`
65. Verifikasi `Duration unit` tetap bernilai `Hours`
66. Verifikasi `Self service` tetap bernilai `ON`
67. Verifikasi `Max duration` kembali ke nilai awal `14`

### Reset to Default tidak menyentuh field bergerbang Assignment
68. Tampilkan Area utama dengan kondisi K10
69. Verifikasi `Direct handover between holders` disabled dengan nilai tersimpan `Deny`
70. Klik `Reset to Default`
71. Verifikasi `Direct handover between holders` tetap bernilai `Deny`
72. Verifikasi `Max assets per assignee (concurrent)` kembali ke nilai awal `0`

### Alasan tombol disabled untuk Read Only
73. Tampilkan Area utama dengan kondisi K11
74. Verifikasi tombol `Save` disabled
75. Arahkan kursor ke tombol `Save` yang disabled
76. Verifikasi alasan tombol `Save` disabled tersampaikan
77. Verifikasi tombol `Reset to Default` disabled
78. Arahkan kursor ke tombol `Reset to Default` yang disabled
79. Verifikasi alasan tombol `Reset to Default` disabled tersampaikan

### Save aktif oleh draft di node lain
80. Tampilkan Area utama dengan kondisi K12
81. Verifikasi tombol `Save` aktif karena ada draft perubahan di node Category lain
