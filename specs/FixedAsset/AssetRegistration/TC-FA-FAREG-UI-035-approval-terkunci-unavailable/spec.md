---
id: TC-FA-FAREG-UI-035-approval-terkunci-unavailable
title: "Halaman Approval: pengajuan sendiri terkunci dan aset Unavailable"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [S-REG-13, S-REG-17, S-REG-24, S-REG-29, §4.1#r8, §4.1#r9, §4.2.4#b6, §4.2.4#b7, §4.2.4#b9, §4.8#r22, §4.8#r27, EB-TBL-5@halaman-approval]
smoke: []
dependsOn: []
trace:
  S-REG-13: [2, 3, 8, 22]
  S-REG-17: [12, 14, 17]
  S-REG-24: [29, 30, 41, 46, 47, 53]
  S-REG-29: [26, 31, 33, 37, 44, 48, 51, 54, 55, 57]
  §4.1#r8: [2, 24]
  §4.1#r9: [30, 41, 47, 53, 61, 62]
  §4.2.4#b6: [2, 3, 5]
  §4.2.4#b7: [12, 17, 18, 19, 20]
  §4.2.4#b9: [28, 29, 31, 34, 35, 39, 40, 42, 46, 48, 49]
  §4.8#r22: [3, 4, 22]
  §4.8#r27: [5, 10, 12, 17, 23]
  EB-TBL-5@halaman-approval: [8, 10, 14, 33]
anchor: []
coverage:
  web: automated
---
# Halaman Approval: pengajuan sendiri terkunci dan aset Unavailable

## Prerequisites
- Aktor: Dewi A (approver, role Group Manager, cakupan Group binaan + sub-group termasuk Gudang 1, Gudang 3, dan Gudang 4), yang pada K1 juga pengaju pengajuan; serta pengguna lain dengan hak mengelola master Brand, Model, dan Group yang memicu perubahan master.
- Layar awal: Halaman Approval pengajuan yang dibuka dari antrean Approvals tab Active.
- Komponen: Halaman Approval
- Data:
  - DU-035-1: pengajuan Registration ID `REG-20261111-00014`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Dewi A`, Total Asset `3`.
  - DU-035-2: aset Name `Laptop - 128`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason; di panel koreksi: Custom field `Serial Number` bernilai `SN-128-0001`.
  - DU-035-3: aset Name `Laptop - 129`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Skipped`, Condition `Damaged`, Corrections `1`, Decision `Approve`, tanpa Reason.
  - DU-035-4: aset Name `Office Desk - 12`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 1`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-5: pengajuan Registration ID `REG-20261109-00003`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `5`.
  - DU-035-6: aset Name `Laptop - 129`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Skipped`, Condition `Damaged`, Corrections `1`, Decision `Return to Draft`, Reason `Photo is missing`.
  - DU-035-7: aset Name `Laptop - 130`, Category `Computers`, Brand `Dell`, Model `Latitude 5450`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-8: aset Name `Laptop - 131`, Category `Computers`, Brand `Dell`, Model `Latitude 5450`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-9: aset Name `Office Desk - 12`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 1`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision `Reject`, Reason `Duplicate entry`.
  - DU-035-10: pengajuan Registration ID `REG-20261110-00012`, Status `Waiting for Approval`, Group `Gudang 3`, Requested By `Siti N`, Total Asset `4`.
  - DU-035-11: aset Name `Monitor - 21`, Category `Computers`, Brand `Samsung`, Model `U28`, Group `Gudang 3`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-12: aset Name `Monitor - 22`, Category `Computers`, Brand `Samsung`, Model `U28`, Group `Gudang 4`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-13: aset Name `Monitor - 23`, Category `Computers`, Brand `Samsung`, Model `U28`, Group `Gudang 4`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-035-14: aset Name `Monitor - 24`, Category `Computers`, Brand `Samsung`, Model `U28`, Group `Gudang 3`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Reject`, Reason `Duplicate entry`.
  - DU-035-15: pengajuan Registration ID `REG-20261112-00015`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `3`.
  - DU-035-16: aset Name `Monitor - 25`, Category `Computers`, Brand `Samsung`, Model `S24`, Group `Gudang 3`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - Teks Alert yang diharapkan: `1 asset uses master data that is no longer available. Correct it, return it to Draft, or reject it before deciding.` (satu aset Brand atau Model tidak tersedia), `2 assets use master data that is no longer available. Correct them, return them to Draft, or reject them before deciding.` (dua aset), `1 asset uses master data that is no longer available. Return it to Draft or reject it before deciding.` (satu aset Asset Name atau Group tidak tersedia), dan `2 assets use master data that is no longer available. Return them to Draft or reject them before deciding.` (dua aset), dari template `[N] assets use master data that is no longer available.` dengan N sesuai jumlah aset.
- Kondisi:
  - K1: pengajuan DU-035-1 milik Dewi A berisi aset DU-035-2 dan DU-035-3 dalam grup Accordion `Laptop` dan DU-035-4 dalam grup Accordion `Office Desk`, dengan Decision awal `Approve`.
  - K2: pengajuan DU-035-5 milik Rina W berisi aset DU-035-2, DU-035-6, DU-035-7, dan DU-035-8 dalam grup Accordion `Laptop` dan DU-035-9 dalam grup Accordion `Office Desk`, dan approver berhak memutuskan.
  - K3: pengajuan DU-035-10 milik Siti N berisi aset DU-035-11 sampai DU-035-14 dalam grup Accordion `Monitor`, dan approver berhak memutuskan.
  - K4: pengajuan DU-035-15 milik Rina W berisi aset DU-035-2 dalam grup Accordion `Laptop` serta DU-035-11 dan DU-035-16 dalam grup Accordion `Monitor`, dan approver berhak memutuskan.

## Test Steps

### Pengajuan sendiri: notice dan kontrol keputusan disabled
1. Tampilkan Halaman Approval dengan kondisi K1
2. Verifikasi notice `You cannot decide a registration you submitted.` tampil di atas tabel aset
3. Verifikasi Decision pada setiap baris aset disabled
4. Verifikasi Bulk Action pada grup `Laptop` disabled
5. Verifikasi `[Submit]` disabled

### Alasan disabled tampil saat hover
6. Tampilkan Halaman Approval dengan kondisi K1
7. Arahkan kursor ke Decision pada baris `Laptop - 128`
8. Verifikasi tooltip `You cannot decide a registration you submitted.` tampil
9. Arahkan kursor ke `[Submit]`
10. Verifikasi tooltip alasan tampil pada `[Submit]` yang disabled
11. Klik row option (titik tiga) pada baris `Laptop - 128`
12. Verifikasi pilihan `Edit` disabled
13. Arahkan kursor ke pilihan `Edit`
14. Verifikasi tooltip `You cannot decide a registration you submitted.` tampil

### Link Name tetap aktif dan membuka panel view-only
15. Tampilkan Halaman Approval dengan kondisi K1
16. Klik nama `Laptop - 128`
17. Verifikasi panel koreksi terbuka
18. Verifikasi field `Brand`, `Model`, `Condition`, dan `Serial Number` pada panel nonaktif
19. Verifikasi panel tidak memuat tombol `[Clear Field]`
20. Verifikasi panel tidak memuat tombol `[Save correction]`

### Pengajuan bukan milik approver tidak terkunci
21. Tampilkan Halaman Approval dengan kondisi K2
22. Verifikasi Decision pada baris `Laptop - 128` aktif
23. Verifikasi `[Submit]` aktif
24. Verifikasi notice `You cannot decide a registration you submitted.` tidak tampil

### Satu aset Brand atau Model tidak tersedia
25. Tampilkan Halaman Approval dengan kondisi K2
26. Verifikasi Decision pada baris `Laptop - 128` aktif
27. Pengguna lain menghapus Model `Latitude 5440` dari master
28. Verifikasi Badge Model pada baris `Laptop - 128` menampilkan `Unavailable`
29. Verifikasi Alert Warning tampil tanpa muat ulang halaman
30. Verifikasi Alert memuat `1 asset uses master data that is no longer available. Correct it, return it to Draft, or reject it before deciding.`
31. Verifikasi Decision pada baris `Laptop - 128` disabled
32. Arahkan kursor ke Decision pada baris `Laptop - 128`
33. Verifikasi tooltip `This asset uses master data that is no longer available.` tampil
34. Verifikasi Badge Model pada baris `Laptop - 129` tidak menampilkan `Unavailable`
35. Verifikasi Decision pada baris `Laptop - 129` aktif

### Dua aset Brand atau Model tidak tersedia
36. Tampilkan Halaman Approval dengan kondisi K2
37. Verifikasi Decision pada baris `Laptop - 130` aktif
38. Pengguna lain menghapus Model `Latitude 5450` dari master
39. Verifikasi Badge Model pada baris `Laptop - 130` menampilkan `Unavailable`
40. Verifikasi Badge Model pada baris `Laptop - 131` menampilkan `Unavailable`
41. Verifikasi Alert memuat `2 assets use master data that is no longer available. Correct them, return them to Draft, or reject them before deciding.`
42. Verifikasi Decision pada baris `Office Desk - 12` dengan Decision `Reject` aktif

### Satu aset Asset Name atau Group tidak tersedia
43. Tampilkan Halaman Approval dengan kondisi K3
44. Verifikasi Decision pada baris `Monitor - 21` aktif
45. Pengguna lain menghapus Group `Gudang 3` dari master
46. Verifikasi Alert Warning tampil tanpa muat ulang halaman
47. Verifikasi Alert memuat `1 asset uses master data that is no longer available. Return it to Draft or reject it before deciding.`
48. Verifikasi Decision pada baris `Monitor - 21` disabled
49. Verifikasi Decision pada baris `Monitor - 24` dengan Decision `Reject` aktif

### Dua aset Asset Name atau Group tidak tersedia
50. Tampilkan Halaman Approval dengan kondisi K3
51. Verifikasi Decision pada baris `Monitor - 22` aktif
52. Pengguna lain menghapus Group `Gudang 4` dari master
53. Verifikasi Alert memuat `2 assets use master data that is no longer available. Return them to Draft or reject them before deciding.`
54. Verifikasi Decision pada baris `Monitor - 22` disabled
55. Verifikasi Decision pada baris `Monitor - 23` disabled

### Dua jenis aset tidak tersedia tampil sebagai dua baris Alert
56. Tampilkan Halaman Approval dengan kondisi K4
57. Verifikasi Decision pada baris `Laptop - 128` aktif
58. Pengguna lain menghapus Model `Latitude 5440` dari master
59. Pengguna lain menghapus Model `S24` dari master
60. Pengguna lain menghapus Group `Gudang 3` dari master
61. Verifikasi baris Alert pertama `1 asset uses master data that is no longer available. Correct it, return it to Draft, or reject it before deciding.`
62. Verifikasi baris Alert kedua `2 assets use master data that is no longer available. Return them to Draft or reject them before deciding.`
