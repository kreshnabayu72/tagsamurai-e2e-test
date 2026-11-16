---
id: TC-FA-FATR-UI-060-area-assign
title: "Area utama: field tab Assign"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules:
  - §4.1#r55
  - §4.1#r99
  - §4.1#r100
  - §4.1#r101
  - §4.1#r102
  - §4.1#r103
  - §4.1#r161
  - §4.1#r163
  - §4.1#r179
  - §4.1#r184
  - §4.1#r200
  - §4.1#r212
  - §9.2#b424
smoke: []
dependsOn: []
trace:
  §4.1#r55: [2, 4]
  §4.1#r99: [6, 8]
  §4.1#r100: [9, 11, 36, 42]
  §4.1#r101: 12
  §4.1#r102: [13, 15, 37, 43]
  §4.1#r103: [17, 19, 38, 44]
  §4.1#r161: [22, 48, 52]
  §4.1#r163: [23, 49, 53]
  §4.1#r179: [25, 27, 39, 45]
  §4.1#r184: [28, 30, 50, 55]
  §4.1#r200: 33
  §4.1#r212: [34, 40, 46]
  §9.2#b424: [22, 23]
anchor: []
coverage:
  web: automated
---

# Area utama: field tab Assign

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-060-1: Pengaturan Company default tab Assign pada All categories: Allow Assign `Allow`, Allowed assignee: Employee `ON`, Allowed assignee: Division `ON`, Max assets per assignee (concurrent) `0`, Recipient acceptance `Required`, Direct handover between holders `Allow`, Photo at start `ON`, Photo at end `ON`, Require approval `OFF`, Approval type `Any one approver`, Transaction timeout `7`, Send email notifications `OFF`.
  - DU-060-2: Pengaturan Company default tab Assign pada All categories yang berbeda dari nilai awal: Allowed assignee: Employee `ON`, Allowed assignee: Division `OFF`, Recipient acceptance `Optional`, Direct handover between holders `Deny`, Photo at start `OFF`, Photo at end `OFF`, Require approval `ON`, Approval type `All approvers (AND)`, Send email notifications `ON`.
- Kondisi:
  - K1: node All categories terpilih, tab Assign aktif, nilai Company default memakai DU-060-1.
  - K2: node All categories terpilih, tab Assign aktif, nilai Company default memakai DU-060-2.

## Test Steps

### Eligibility dan Limits Assign
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi `Allow Assign` bernilai `Allow`
3. Buka daftar pilihan `Allow Assign`
4. Verifikasi pilihan `Allow Assign` adalah `Allow` dan `Deny`
5. Tutup daftar pilihan dengan Escape
6. Verifikasi `Allowed assignee: Employee` bernilai `ON`
7. Matikan `Allowed assignee: Employee`
8. Verifikasi `Allowed assignee: Employee` bernilai `OFF`
9. Verifikasi `Allowed assignee: Division` bernilai `ON`
10. Matikan `Allowed assignee: Division`
11. Verifikasi `Allowed assignee: Division` bernilai `OFF`
12. Verifikasi `Max assets per assignee (concurrent)` bernilai `0`
13. Verifikasi `Recipient acceptance` bernilai `Required`
14. Buka daftar pilihan `Recipient acceptance`
15. Verifikasi pilihan `Recipient acceptance` adalah `Required` dan `Optional`
16. Tutup daftar pilihan dengan Escape
17. Verifikasi `Direct handover between holders` bernilai `Allow`
18. Buka daftar pilihan `Direct handover between holders`
19. Verifikasi pilihan `Direct handover between holders` adalah `Allow` dan `Deny`
20. Tutup daftar pilihan dengan Escape

### Evidence Assign
21. Tampilkan Area utama dengan kondisi K1
22. Verifikasi `Photo at start` bernilai `ON` pada bagian `Evidence`
23. Verifikasi `Photo at end` bernilai `ON` pada bagian `Evidence`

### Approval Assign
24. Tampilkan Area utama dengan kondisi K1
25. Verifikasi `Require approval` bernilai `OFF`
26. Nyalakan `Require approval`
27. Verifikasi `Require approval` bernilai `ON`
28. Verifikasi `Approval type` bernilai `Any one approver`
29. Buka daftar pilihan `Approval type`
30. Verifikasi pilihan `Approval type` adalah `Any one approver` dan `All approvers (AND)`
31. Tutup daftar pilihan dengan Escape

### Reminders dan Notifications Assign
32. Tampilkan Area utama dengan kondisi K1
33. Verifikasi `Transaction timeout` bernilai `7`
34. Verifikasi `Send email notifications` bernilai `OFF`

### Reset to Default mengembalikan field tab Assign ke nilai awal
35. Tampilkan Area utama dengan kondisi K2
36. Verifikasi `Allowed assignee: Division` bernilai `OFF`
37. Verifikasi `Recipient acceptance` bernilai `Optional`
38. Verifikasi `Direct handover between holders` bernilai `Deny`
39. Verifikasi `Require approval` bernilai `ON`
40. Verifikasi `Send email notifications` bernilai `ON`
41. Klik `Reset to Default`
42. Verifikasi `Allowed assignee: Division` kembali ke nilai awal `ON`
43. Verifikasi `Recipient acceptance` kembali ke nilai awal `Required`
44. Verifikasi `Direct handover between holders` kembali ke nilai awal `Allow`
45. Verifikasi `Require approval` kembali ke nilai awal `OFF`
46. Verifikasi `Send email notifications` kembali ke nilai awal `OFF`

### Reset to Default mengembalikan Evidence dan Approval type Assign ke nilai awal
47. Tampilkan Area utama dengan kondisi K2
48. Verifikasi `Photo at start` bernilai `OFF` pada bagian `Evidence`
49. Verifikasi `Photo at end` bernilai `OFF` pada bagian `Evidence`
50. Verifikasi `Approval type` bernilai `All approvers (AND)`
51. Klik `Reset to Default`
52. Verifikasi `Photo at start` kembali ke nilai awal `ON` pada bagian `Evidence`
53. Verifikasi `Photo at end` kembali ke nilai awal `ON` pada bagian `Evidence`
54. Nyalakan `Require approval`
55. Verifikasi `Approval type` kembali ke nilai awal `Any one approver`
