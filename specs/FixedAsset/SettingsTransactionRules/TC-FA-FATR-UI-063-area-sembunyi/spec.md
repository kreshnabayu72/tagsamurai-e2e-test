---
id: TC-FA-FATR-UI-063-area-sembunyi
title: "Area utama: aturan sembunyi bagian dan field"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules:
  - §Aturan Logika Modul#r20
  - §Aturan Logika Modul#r21
  - §Aturan Logika Modul#r22
  - §Aturan Logika Modul#r23
  - §Aturan Logika Modul#r24
  - §4.1#r192
  - §4.3#r9
  - §4.3#r10
  - §4.3#r17
  - §4.3#r21
  - §4.3#r22
  - §4.3#r23
  - §4.3#r24
  - §4.3#r25
  - §4.3#r26
  - §4.3#r27
  - §4.3#r28
  - §9.2#b17
  - §9.2#r10
  - §9.4.2#r18
  - §9.4.2#r100
  - §9.4.2#r103
smoke: []
dependsOn: []
trace:
  §Aturan Logika Modul#r20: [7, 13]
  §Aturan Logika Modul#r21: [8, 14]
  §Aturan Logika Modul#r22: [4, 5, 11]
  §Aturan Logika Modul#r23: [2, 16, 17]
  §Aturan Logika Modul#r24: [10, 11]
  §4.1#r192: [39, 40, 41]
  §4.3#r9: [22, 26, 32, 41, 44, 46, 49, 51, 54, 57, 59]
  §4.3#r10: [29, 34]
  §4.3#r17: [39, 40]
  §4.3#r21: [5, 11]
  §4.3#r22: [7, 13]
  §4.3#r23: [8, 14]
  §4.3#r24: [6, 12]
  §4.3#r25: [20, 30]
  §4.3#r26: [24, 25, 35, 36]
  §4.3#r27: [21, 25]
  §4.3#r28: [31, 36]
  §9.2#b17: [5, 7, 8]
  §9.2#r10: [20, 30]
  §9.4.2#r18: [20, 24]
  §9.4.2#r100: 5
  §9.4.2#r103: [7, 8]
anchor: [19, 28, 38, 43, 48, 56]
coverage:
  web: automated
---

# Area utama: aturan sembunyi bagian dan field

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-063-1: Pengaturan Category leaf `Machinery` tab Borrow: Allow Borrow bernilai sendiri `Allow`, Max duration bernilai sendiri `21`, Company default Allow Borrow `Allow`.
  - DU-063-2: Pengaturan Category leaf `Machinery` tab Borrow: Allow Borrow Inherit, Company default Allow Borrow `Deny`.
  - DU-063-3: Pengaturan Category leaf `Machinery` tab Borrow: Allow Borrow bernilai sendiri `Allow`, Company default Allow Borrow `Deny`.
  - DU-063-4: Pengaturan Company default tab Borrow pada All categories: Require approval `OFF`, Auto-approve `ON`, Auto-approve when duration ≤ `3`, Approval type `All approvers (AND)`, Self service `OFF`.
  - DU-063-5: Pengaturan Company default tab Transfer pada All categories: Require approval `OFF`, Auto-approve `ON`, Auto-approve when destination in same parent Group `ON`, Approval scope `Origin only`, Approval type `All approvers (AND)`.
  - DU-063-6: Pengaturan Company default tab Borrow pada All categories: Self service `ON`, Require approval `ON`, Auto-approve `ON`, Auto-approve when duration ≤ `3`, Approval type `Any one approver`.
  - DU-063-7: Pengaturan Company default tab Assign pada All categories: Require approval `OFF`, Approval type `All approvers (AND)`.
  - DU-063-8: Pengaturan Company default tab Disposal pada All categories: Require approval `OFF`, Approval type `All approvers (AND)`.
  - DU-063-9: Pengaturan Company default tab Borrow pada All categories: Self service `ON`, Require approval `ON`, Auto-approve `ON`, Approval type `All approvers (AND)`.
- Kondisi:
  - K1: node Category leaf `Machinery` terpilih, tab Borrow aktif, nilai memakai DU-063-1.
  - K2: node Category leaf `Machinery` terpilih, tab Borrow aktif, nilai memakai DU-063-2.
  - K3: node Category leaf `Machinery` terpilih, tab Borrow aktif, nilai memakai DU-063-3.
  - K4: node All categories terpilih, tab Borrow aktif, nilai Company default memakai DU-063-4.
  - K5: node All categories terpilih, tab Transfer aktif, nilai Company default memakai DU-063-5.
  - K6: node All categories terpilih, tab Borrow aktif, level Feature Suite Borrowing Full, nilai Company default memakai DU-063-6.
  - K7: node All categories terpilih, tab Assign aktif, nilai Company default memakai DU-063-7.
  - K8: node All categories terpilih, tab Disposal aktif, nilai Company default memakai DU-063-8.
  - K9: node All categories terpilih, tab Borrow aktif, level Feature Suite Borrowing Full, nilai Company default memakai DU-063-9.

## Test Steps

### Deny pada Category menyembunyikan bagian selain Eligibility
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi bagian `Limits` memuat `Max duration` bernilai `21`
3. Pilih `Deny` pada `Allow Borrow`
4. Verifikasi bagian `Eligibility` tetap tampil dengan `Allow Borrow` bernilai `Deny`
5. Verifikasi bagian `Limits`, `Evidence`, `Approval`, `Reminders`, dan `Notifications` tidak ada
6. Verifikasi keterangan `Other sections are hidden while this transaction is denied. Their values are kept.` tampil
7. Verifikasi bagian `Overrides` dengan toolbar, tabel, dan tombol `+ Override` tampil dan aktif
8. Verifikasi tombol `Reset to Default` dan tombol `Save` tampil dan aktif

### Deny yang di-Inherit dari Company default
9. Tampilkan Area utama dengan kondisi K2
10. Verifikasi `Allow Borrow` menampilkan `Inherit — Deny (from Company default)`
11. Verifikasi bagian `Limits`, `Evidence`, `Approval`, `Reminders`, dan `Notifications` tidak ada
12. Verifikasi keterangan `Other sections are hidden while this transaction is denied. Their values are kept.` tampil
13. Verifikasi bagian `Overrides` dengan toolbar, tabel, dan tombol `+ Override` tampil dan aktif
14. Verifikasi tombol `Reset to Default` tampil dan aktif

### Nilai efektif Allow menentukan bagian yang disembunyikan
15. Tampilkan Area utama dengan kondisi K3
16. Verifikasi `Allow Borrow` bernilai `Allow`
17. Verifikasi bagian `Limits`, `Evidence`, `Approval`, `Reminders`, dan `Notifications` tampil

### Auto-approve Borrow disembunyikan saat Require approval OFF
18. Tampilkan Area utama dengan kondisi K4
19. Verifikasi `Require approval` bernilai `OFF`
20. Verifikasi `Auto-approve` tidak ada
21. Verifikasi field `Auto-approve when duration ≤` ikut tersembunyi bersama `Auto-approve`
22. Verifikasi `Approval type` tidak ada
23. Nyalakan `Require approval`
24. Verifikasi `Auto-approve` bernilai `ON`
25. Verifikasi nilai tersimpan `Auto-approve when duration ≤` tetap `3`
26. Verifikasi `Approval type` bernilai `All approvers (AND)`

### Field Approval Transfer saat Require approval OFF
27. Tampilkan Area utama dengan kondisi K5
28. Verifikasi `Require approval` bernilai `OFF`
29. Verifikasi `Approval scope` tampil dengan nilai `Origin only`
30. Verifikasi `Auto-approve` tidak ada
31. Verifikasi `Auto-approve when destination in same parent Group` tidak ada
32. Verifikasi `Approval type` tidak ada
33. Nyalakan `Require approval`
34. Verifikasi `Approval scope` bernilai `Origin only`
35. Verifikasi `Auto-approve` bernilai `ON`
36. Verifikasi nilai tersimpan `Auto-approve when destination in same parent Group` tetap `ON`

### Self service ON menyembunyikan field Approval Borrow
37. Tampilkan Area utama dengan kondisi K6
38. Verifikasi `Self service` bernilai `ON`
39. Verifikasi `Require approval` tidak ada
40. Verifikasi `Auto-approve` tidak ada
41. Verifikasi `Approval type` tidak ada

### Approval type Assign disembunyikan saat Require approval OFF
42. Tampilkan Area utama dengan kondisi K7
43. Verifikasi `Require approval` tampil dengan nilai `OFF` pada tab `Assign`
44. Verifikasi `Approval type` tidak ada pada tab `Assign`
45. Nyalakan `Require approval`
46. Verifikasi `Approval type` bernilai tersimpan `All approvers (AND)` pada tab `Assign`

### Approval type Disposal disembunyikan saat Require approval OFF
47. Tampilkan Area utama dengan kondisi K8
48. Verifikasi `Require approval` tampil dengan nilai `OFF` pada tab `Disposal`
49. Verifikasi `Approval type` tidak ada pada tab `Disposal`
50. Nyalakan `Require approval`
51. Verifikasi `Approval type` bernilai tersimpan `All approvers (AND)` pada tab `Disposal`

### Nilai Approval type Transfer dipertahankan
52. Tampilkan Area utama dengan kondisi K5
53. Nyalakan `Require approval`
54. Verifikasi `Approval type` bernilai tersimpan `All approvers (AND)` pada tab `Transfer`

### Nilai Approval type Borrow dipertahankan sesudah Self service dimatikan
55. Tampilkan Area utama dengan kondisi K9
56. Verifikasi `Self service` tampil dengan nilai `ON` sebelum dimatikan
57. Verifikasi `Approval type` tidak ada pada tab `Borrow`
58. Matikan `Self service`
59. Verifikasi `Approval type` bernilai tersimpan `All approvers (AND)` pada tab `Borrow`
