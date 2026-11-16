---
id: TC-FA-FATR-UI-061-area-transfer
title: "Area utama: field tab Transfer"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules:
  - §4.1#r55
  - §4.1#r125
  - §4.1#r126
  - §4.1#r128
  - §4.1#r127
  - §4.1#r129
  - §4.1#r161
  - §4.1#r163
  - §4.1#r179
  - §4.1#r184
  - §4.1#r181
  - §4.1#r183
  - §4.1#r185
  - §4.1#r197
  - §4.1#r200
  - §4.1#r212
  - §9.2#b424
smoke: []
dependsOn: []
trace:
  §4.1#r55: [2, 4]
  §4.1#r125: [6, 8, 42, 46]
  §4.1#r126: [10, 12]
  §4.1#r128: [15, 17, 43, 47]
  §4.1#r127: [14, 19]
  §4.1#r129: 20
  §4.1#r161: [22, 60, 64]
  §4.1#r163: [23, 61, 65]
  §4.1#r179: [25, 56, 58]
  §4.1#r184: [26, 28, 68, 70]
  §4.1#r181: [30, 33, 62, 66]
  §4.1#r183: [31, 50, 53]
  §4.1#r185: [34, 36, 51, 54]
  §4.1#r197: 36
  §4.1#r200: 39
  §4.1#r212: [40, 44, 48]
  §9.2#b424: [22, 23]
anchor: []
coverage:
  web: automated
---

# Area utama: field tab Transfer

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-061-1: Pengaturan Company default tab Transfer pada All categories: Allow Transfer `Allow`, Destination scope `Any Group`, Change Cost Center with Group `Never`, In-transit overdue after `7`, Destination quota check `ON`, Photo at start `ON`, Photo at end `ON`, Require approval `ON`, Approval type `Any one approver`, Auto-approve `ON`, Auto-approve when destination in same parent Group `ON`, Approval scope `Both`, Transaction timeout `7`, Send email notifications `OFF`.
  - DU-061-2: Pengaturan Category leaf `Machinery`: semua field Inherit, Change Cost Center with Group Company default `Never`.
  - DU-061-3: Pengaturan Company default tab Transfer pada All categories yang berbeda dari nilai awal: Destination scope `Within same parent Group`, Destination quota check `OFF`, Send email notifications `ON`.
  - DU-061-4: Pengaturan Company default tab Transfer pada All categories yang berbeda dari nilai awal: Require approval `ON`, Auto-approve `ON`, Auto-approve when destination in same parent Group `OFF`, Approval scope `Origin only`, Approval type `All approvers (AND)`.
  - DU-061-6: Pengaturan Company default tab Transfer pada All categories yang berbeda dari nilai awal: Photo at start `OFF`, Photo at end `OFF`, Require approval `ON`, Auto-approve `OFF`.
  - DU-061-5: Pengaturan Company default tab Transfer pada All categories yang berbeda dari nilai awal: Require approval `OFF`.
- Kondisi:
  - K1: node All categories terpilih, tab Transfer aktif, nilai Company default memakai DU-061-1.
  - K2: node Category leaf `Machinery` terpilih, tab Transfer aktif, nilai memakai DU-061-2.
  - K3: node All categories terpilih, tab Transfer aktif, nilai Company default memakai DU-061-3.
  - K4: node All categories terpilih, tab Transfer aktif, Approval Workflow tersedia di plan, nilai Company default memakai DU-061-4.
  - K5: node All categories terpilih, tab Transfer aktif, nilai Company default memakai DU-061-5.
  - K6: node All categories terpilih, tab Transfer aktif, nilai Company default memakai DU-061-6.

## Test Steps

### Eligibility dan Limits Transfer
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi `Allow Transfer` bernilai `Allow`
3. Buka daftar pilihan `Allow Transfer`
4. Verifikasi pilihan `Allow Transfer` adalah `Allow` dan `Deny`
5. Tutup daftar pilihan dengan Escape
6. Verifikasi `Destination scope` bernilai `Any Group`
7. Buka daftar pilihan `Destination scope`
8. Verifikasi pilihan `Destination scope` adalah `Within same parent Group` dan `Any Group`
9. Tutup daftar pilihan dengan Escape
10. Verifikasi `Change Cost Center with Group` bernilai `Never`
11. Buka daftar pilihan `Change Cost Center with Group`
12. Verifikasi pilihan `Change Cost Center with Group` adalah `Never` dan `Always`
13. Tutup daftar pilihan dengan Escape
14. Verifikasi `In-transit overdue after` bernilai `7`
15. Verifikasi `Destination quota check` bernilai `ON`
16. Matikan `Destination quota check`
17. Verifikasi `Destination quota check` bernilai `OFF`

### Change Cost Center with Group hanya di All categories
18. Tampilkan Area utama dengan kondisi K2
19. Verifikasi tab `Transfer` memuat field `In-transit overdue after` dengan tombol `Set own value`
20. Verifikasi `Change Cost Center with Group` di Category leaf `Machinery` tidak punya kontrol dan tidak punya tombol `Set own value`

### Evidence Transfer
21. Tampilkan Area utama dengan kondisi K1
22. Verifikasi `Photo at start` bernilai `ON` pada bagian `Evidence`
23. Verifikasi `Photo at end` bernilai `ON` pada bagian `Evidence`

### Approval Transfer
24. Tampilkan Area utama dengan kondisi K1
25. Verifikasi `Require approval` bernilai `ON`
26. Verifikasi `Approval type` bernilai `Any one approver`
27. Buka daftar pilihan `Approval type`
28. Verifikasi pilihan `Approval type` adalah `Any one approver` dan `All approvers (AND)`
29. Tutup daftar pilihan dengan Escape
30. Verifikasi `Auto-approve` bernilai `ON`
31. Verifikasi `Auto-approve when destination in same parent Group` bernilai `ON`
32. Matikan `Auto-approve`
33. Verifikasi `Auto-approve` bernilai `OFF`
34. Verifikasi `Approval scope` bernilai `Both`
35. Buka daftar pilihan `Approval scope`
36. Verifikasi pilihan `Approval scope` adalah `Origin only`, `Destination only`, dan `Both`
37. Tutup daftar pilihan dengan Escape

### Reminders dan Notifications Transfer
38. Tampilkan Area utama dengan kondisi K1
39. Verifikasi `Transaction timeout` bernilai `7`
40. Verifikasi `Send email notifications` bernilai `OFF`

### Reset to Default mengembalikan Destination dan Notifications Transfer ke nilai awal
41. Tampilkan Area utama dengan kondisi K3
42. Verifikasi `Destination scope` bernilai `Within same parent Group`
43. Verifikasi `Destination quota check` bernilai `OFF`
44. Verifikasi `Send email notifications` bernilai `ON`
45. Klik `Reset to Default`
46. Verifikasi `Destination scope` kembali ke nilai awal `Any Group`
47. Verifikasi `Destination quota check` kembali ke nilai awal `ON`
48. Verifikasi `Send email notifications` kembali ke nilai awal `OFF`

### Reset to Default mengembalikan Approval scope Transfer ke nilai awal
49. Tampilkan Area utama dengan kondisi K4
50. Verifikasi `Auto-approve when destination in same parent Group` bernilai `OFF`
51. Verifikasi `Approval scope` tampil dengan nilai `Origin only` sebelum Reset to Default
52. Klik `Reset to Default`
53. Verifikasi `Auto-approve when destination in same parent Group` kembali ke nilai awal `ON`
54. Verifikasi `Approval scope` kembali ke nilai awal `Both`

### Reset to Default mengembalikan Require approval Transfer ke nilai awal
55. Tampilkan Area utama dengan kondisi K5
56. Verifikasi `Require approval` bernilai `OFF`
57. Klik `Reset to Default`
58. Verifikasi `Require approval` kembali ke nilai awal `ON`

### Reset to Default mengembalikan Evidence dan Auto-approve Transfer ke nilai awal
59. Tampilkan Area utama dengan kondisi K6
60. Verifikasi `Photo at start` bernilai `OFF` pada bagian `Evidence`
61. Verifikasi `Photo at end` bernilai `OFF` pada bagian `Evidence`
62. Verifikasi `Auto-approve` bernilai `OFF`
63. Klik `Reset to Default`
64. Verifikasi `Photo at start` kembali ke nilai awal `ON` pada bagian `Evidence`
65. Verifikasi `Photo at end` kembali ke nilai awal `ON` pada bagian `Evidence`
66. Verifikasi `Auto-approve` kembali ke nilai awal `ON`

### Reset to Default mengembalikan Approval type Transfer ke nilai awal
67. Tampilkan Area utama dengan kondisi K4
68. Verifikasi `Approval type` bernilai `All approvers (AND)`
69. Klik `Reset to Default`
70. Verifikasi `Approval type` kembali ke nilai awal `Any one approver`
