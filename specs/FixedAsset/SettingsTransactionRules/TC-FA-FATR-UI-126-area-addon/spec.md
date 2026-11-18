---
id: TC-FA-FATR-UI-126-area-addon
title: "Area utama: tab dan field bergerbang addon"
layer: ui-client
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: ["§4.3#r21", "§4.3#r22", "§4.3#r23", "§4.1#r241", "§Aturan Logika Modul#r115", "§Aturan Logika Modul#r119", "§Aturan Logika Modul#r123", "§9.4.2#r66", "§9.4.2#r69", "§9.4.2#r72", "§9.10.5#b1", "§9.10.5#b2", "§9.10.5#b3", "§9.10.5#b4", "§4.1#r235", "§Aturan Logika Modul#r77", "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f", "§4.3#r24", "§Aturan Logika Modul#r113", "§9.4.2#r67", "§9.10.5#b5"]
smoke: []
dependsOn: []
trace:
  "§4.3#r21": [31, 35]
  "§4.3#r22": [3, 5, 7]
  "§4.3#r23": [9, 11, 13]
  "§4.1#r241": [30, 31, 34, 35, 38, 39]
  "§Aturan Logika Modul#r115": [30, 31, 34, 35, 38, 39]
  "§Aturan Logika Modul#r119": [3, 7, 15, 17]
  "§Aturan Logika Modul#r123": [9, 13, 18, 20]
  "§9.4.2#r66": 35
  "§9.4.2#r69": [3, 5, 7]
  "§9.4.2#r72": [9, 11, 13, 31]
  "§9.10.5#b1": [3, 7, 35]
  "§9.10.5#b2": [9, 13, 31]
  "§9.10.5#b3": [41, 43, 44, 45, 47, 48, 50, 52]
  "§9.10.5#b4": [29, 30, 33, 34, 37, 38, 39]
  "§4.1#r235": [50, 52, 53]
  "§Aturan Logika Modul#r77": [41, 43, 44, 50, 52, 53]
  "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f": [23, 24]
  "§4.3#r24": 27
  "§Aturan Logika Modul#r113": [27, 29, 33, 37]
  "§9.4.2#r67": 27
  "§9.10.5#b5": 27
anchor: [2, 22, 26]
coverage:
  web: automated
---

# Area utama: tab dan field bergerbang addon

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-126-1: Status addon: Audit dan Maintenance tidak aktif pada subscription FAMS; level Feature Suite Transfer `None`.
  - DU-126-2: Status addon: hanya Audit yang aktif pada subscription FAMS; nilai tersimpan Require location Audit `ON` dan Require location Maintenance `ON`.
  - DU-126-3: Status addon: hanya Maintenance yang aktif pada subscription FAMS; nilai tersimpan Require location Audit `ON` dan Require location Maintenance `ON`.
  - DU-126-4: Status addon: Audit dan Maintenance aktif pada subscription FAMS; Require location Audit `OFF` dan Require location Maintenance `OFF`.
  - DU-126-5: Status addon Audit aktif; Approval Workflow tidak tersedia di plan; nilai tersimpan tab Audit: Require approval `ON`, Approval type `All approvers (AND)`.
  - DU-126-6: Status addon Maintenance aktif; Approval Workflow tidak tersedia di plan; nilai tersimpan tab Maintenance: Require approval to close `ON`.
- Kondisi:
  - K1: node All categories terpilih, tab Borrow aktif, status addon dan level plan memakai DU-126-1.
  - K2: node All categories terpilih, tab Geolocation aktif, status addon dan nilai tersimpan memakai DU-126-2.
  - K3: node All categories terpilih, tab Geolocation aktif, status addon dan nilai tersimpan memakai DU-126-3.
  - K4: node All categories terpilih, tab Geolocation aktif, status addon dan nilai memakai DU-126-4.
  - K5: node All categories terpilih, tab Audit aktif, status addon, plan, dan nilai tersimpan memakai DU-126-5.
  - K6: node All categories terpilih, tab Maintenance aktif, status addon, plan, dan nilai tersimpan memakai DU-126-6.

## Test Steps

### Tab Audit disabled dan tidak dapat dibuka saat addon Audit tidak aktif
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi tab `Borrow` menjadi tab aktif
3. Verifikasi tab `Audit` disabled
4. Arahkan pointer ke tab `Audit`
5. Verifikasi alasan `Requires the Audit add-on.` tersampaikan pada tab `Audit` yang disabled
6. Klik tab `Audit`
7. Verifikasi tab `Audit` tidak menjadi tab aktif

### Tab Maintenance disabled dan tidak dapat dibuka saat addon Maintenance tidak aktif
8. Tampilkan Area utama dengan kondisi K1
9. Verifikasi tab `Maintenance` disabled
10. Arahkan pointer ke tab `Maintenance`
11. Verifikasi alasan `Requires the Maintenance add-on.` tersampaikan pada tab `Maintenance` yang disabled
12. Klik tab `Maintenance`
13. Verifikasi tab `Maintenance` tidak menjadi tab aktif

### Tab Audit dan Maintenance dapat dibuka saat addon aktif
14. Tampilkan Area utama dengan kondisi K4
15. Verifikasi tab `Audit` tidak disabled
16. Klik tab `Audit`
17. Verifikasi tab `Audit` menjadi tab aktif
18. Verifikasi tab `Maintenance` tidak disabled
19. Klik tab `Maintenance`
20. Verifikasi tab `Maintenance` menjadi tab aktif

### Gerbang addon pada tab tidak memakai chip Upgrade
21. Tampilkan Area utama dengan kondisi K1
22. Verifikasi tab `Transfer` tidak tampil pada daftar tab
23. Verifikasi tab `Audit` tanpa ikon 🔒 dan tanpa chip `Upgrade`
24. Verifikasi tab `Maintenance` tanpa ikon 🔒 dan tanpa chip `Upgrade`

### Tab Geolocation tidak tampil saat addon Audit dan Maintenance tidak aktif
25. Tampilkan Area utama dengan kondisi K1
26. Verifikasi tab `Borrow` tampil di daftar tab
27. Verifikasi tab `Geolocation` tidak tampil di daftar tab

### Hanya addon Audit aktif: tab Geolocation tampil dengan baris Audit saja
28. Tampilkan Area utama dengan kondisi K2
29. Verifikasi tab `Geolocation` tampil di daftar tab
30. Verifikasi baris `Audit` pada Require location tampil
31. Verifikasi baris `Maintenance` pada Require location tidak tampil

### Hanya addon Maintenance aktif: tab Geolocation tampil dengan baris Maintenance saja
32. Tampilkan Area utama dengan kondisi K3
33. Verifikasi tab `Geolocation` tampil di daftar tab
34. Verifikasi baris `Maintenance` pada Require location tampil
35. Verifikasi baris `Audit` pada Require location tidak tampil

### Addon Audit dan Maintenance aktif: tab Geolocation tampil dengan kedua baris
36. Tampilkan Area utama dengan kondisi K4
37. Verifikasi tab `Geolocation` tampil di daftar tab
38. Verifikasi baris `Audit` pada Require location tampil
39. Verifikasi baris `Maintenance` pada Require location tampil

### Field approval tab Audit disabled saat Approval Workflow tidak tersedia
40. Tampilkan Area utama dengan kondisi K5
41. Verifikasi `Require approval` disabled
42. Arahkan pointer ke kontrol `Require approval`
43. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada kontrol `Require approval` yang disabled
44. Verifikasi `Require approval` bernilai `ON`
45. Verifikasi `Approval type` disabled
46. Arahkan pointer ke kontrol `Approval type`
47. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada kontrol `Approval type` yang disabled
48. Verifikasi `Approval type` bernilai `All approvers (AND)`

### Field approval tab Maintenance disabled saat Approval Workflow tidak tersedia
49. Tampilkan Area utama dengan kondisi K6
50. Verifikasi `Require approval to close` disabled
51. Arahkan pointer ke kontrol `Require approval to close`
52. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada kontrol `Require approval to close` yang disabled
53. Verifikasi `Require approval to close` bernilai `ON`
