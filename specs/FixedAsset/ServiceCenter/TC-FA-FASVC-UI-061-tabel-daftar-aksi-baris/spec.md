---
id: TC-FA-FASVC-UI-061-tabel-daftar-aksi-baris
title: "Aksi Baris: Detail, Edit, Inactivate, Activate, Delete; Hidden dan Disabled dengan Tooltip"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["RA-FASVC-06", "RA-FASVC-07", "RA-FASVC-08", "RA-FASVC-09", "RA-FASVC-10", "RA-FASVC-11", "RA-FASVC-12", "S-FASVC-11", "S-FASVC-12", "S-FASVC-14", "EB-TBL-5@row-action-delete", "EB-TBL-5@row-action-activate", "EB-FB-2@guard-delete-dipakai", "§4.8#p1"]
smoke: []
dependsOn: []
trace:
  "RA-FASVC-06": [43, 44, 47, 51, 52, 55, 56]
  "RA-FASVC-07": [4, 6, 62]
  "RA-FASVC-08": [20, 22, 23, 25]
  "RA-FASVC-09": [34]
  "RA-FASVC-10": [3, 7, 14, 17, 37, 59]
  "RA-FASVC-11": [30, 31, 32]
  "RA-FASVC-12": [3, 14, 28]
  "S-FASVC-11": [4, 6, 16, 38, 40, 60, 62]
  "S-FASVC-12": [15, 20, 22, 23, 25]
  "S-FASVC-14": [44, 48, 65, 66]
  "EB-TBL-5@row-action-delete": [4, 6, 60]
  "EB-TBL-5@row-action-activate": [20, 22]
  "EB-FB-2@guard-delete-dipakai": [9, 10, 11]
  "§4.8#p1": [20, 22, 38, 40, 60, 62]
anchor: []
coverage:
  web: automated
---
# Aksi Baris: Detail, Edit, Inactivate, Activate, Delete; Hidden dan Disabled dengan Tooltip

## Prerequisites
- Aktor: Total Control, Asset Admin (Maintenance Routine, cakupan `Branch Surabaya`), Group Manager (cakupan `Branch Surabaya`), Read Only, dan Monitoring & Report; tiap kondisi menyebut aktor yang dipakai.
- Layar awal: Add-ons > Service Center, halaman daftar Service Center.
- Komponen: Tabel Service Center
- Data:
  - DU-061-1: Service Center `CV Genset Prima`, Service Type `Routine`, Specialization `Generator`, Available To `Branch Surabaya, Branch Malang`, City `Surabaya`, Brands `All brands`, Usage `24`, Status `Active`, Modified By `Rina W`.
  - DU-061-2: Service Center `Bengkel Maju Motor`, Service Type `Repair`, Specialization `Vehicle`, Available To `Head Office`, City `Bandung`, Brands `All brands`, Usage `0`, Status `Inactive`, Modified By `Rina W`.
  - DU-061-3: Service Center `UD Cahaya Servis`, Service Type `Repair`, Specialization `Vehicle`, Available To kosong, City `Malang`, Brands `All brands`, Usage `0`, Status `Inactive`, Modified By `System`.
  - DU-061-4: Service Center `Teknik Mandiri Utama`, Service Type `Routine`, Specialization `Generator`, Available To `Branch Surabaya`, City `Surabaya`, Brands `LG`, Usage `12`, Status `Active`, Modified By `Rina W`.
  - DU-061-5: Service Center `Servis Gabungan Jawa`, Service Type `Routine`, Specialization `AC`, Available To `Branch Surabaya, Branch Malang`, City `Malang`, Brands `Daikin`, Usage `0`, Status `Active`, Modified By `Rina W`.
  - DU-061-6: Service Center `PT Sejuk Abadi Teknik`, Service Type `Routine, Repair`, Specialization `AC, Refrigeration`, Available To `All groups`, City `Jakarta Selatan`, Brands `Daikin`, Usage `148`, Status `Active`, Modified By `Rina W`.
  - DU-061-7: Service Center `Bengkel Karya Sentosa`, Service Type `Repair`, Specialization `Vehicle`, Available To `Branch Surabaya, Branch Malang`, City `Malang`, Brands `All brands`, Usage `0`, Status `Inactive`, Modified By `Rina W`.
- Kondisi:
  - K1: aktor Total Control; daftar memuat DU-061-1, DU-061-2, DU-061-3, dan DU-061-6; Activate atas DU-061-3 diblok klien karena Available to Service Center itu kosong, tanpa permintaan ke server.
  - K2: aktor Asset Admin dengan cakupan `Branch Surabaya`; daftar memuat DU-061-4, DU-061-5, dan DU-061-6.
  - K3: aktor Read Only; daftar memuat DU-061-1.
  - K4: aktor Monitoring & Report; daftar memuat DU-061-1.
  - K5: aktor Group Manager dengan cakupan `Branch Surabaya`; daftar memuat DU-061-4.
  - K6: aktor Asset Admin dengan cakupan `Branch Surabaya`; daftar memuat DU-061-7.

## Test Steps

### Menu aksi baris Service Center yang sudah dipakai: Delete nonaktif dengan alasan
1. Tampilkan Tabel Service Center dengan kondisi K1
2. Klik `⋯` pada baris `CV Genset Prima`
3. Verifikasi menu aksi baris memuat `Detail`, `Edit`, `Inactivate`, dan `Delete` berurutan
4. Verifikasi `Delete` nonaktif
5. Arahkan kursor ke `Delete`
6. Verifikasi alasan `This service center has been used. Inactivate it instead.` tersampaikan
7. Verifikasi `Activate` tidak tampil di menu aksi baris
8. Klik `Delete`
9. Verifikasi menu aksi baris tetap terbuka
10. Verifikasi dialog `Delete Service Center` tidak tampil
11. Verifikasi toast tidak tampil

### Menu aksi baris Service Center Inactive dengan Usage 0
12. Tampilkan Tabel Service Center dengan kondisi K1
13. Klik `⋯` pada baris `Bengkel Maju Motor`
14. Verifikasi menu aksi baris memuat `Detail`, `Edit`, `Activate`, dan `Delete` berurutan
15. Verifikasi `Activate` aktif
16. Verifikasi `Delete` aktif
17. Verifikasi `Inactivate` tidak tampil di menu aksi baris

### Activate pada Service Center tanpa Available to menampilkan dialog blok
18. Tampilkan Tabel Service Center dengan kondisi K1
19. Klik `⋯` pada baris `UD Cahaya Servis`
20. Verifikasi `Activate` aktif
21. Klik `Activate`
22. Verifikasi dialog blok dengan pesan `Add at least one group before activating.` tampil
23. Verifikasi tombol `[OK]` tampil di dialog blok
24. Klik `[OK]` pada dialog blok
25. Verifikasi baris `UD Cahaya Servis` tetap menampilkan Status `Inactive`

### Kolom Actions memuat pemicu Column Visibility
26. Tampilkan Tabel Service Center dengan kondisi K1
27. Klik header kolom Actions `⋯`
28. Verifikasi daftar kolom Column Visibility tampil dengan kolom `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`, dan `Last Updated`

### Tabel tidak punya Bulk action
29. Tampilkan Tabel Service Center dengan kondisi K1
30. Verifikasi baris `CV Genset Prima` tampil di tabel
31. Verifikasi kolom checkbox untuk memilih baris tidak ada
32. Verifikasi tombol `Bulk Action` tidak tampil

### Badge pada baris berupa fill
33. Tampilkan Tabel Service Center dengan kondisi K1
34. Verifikasi badge Service Type, Specialization, Available To, dan Status pada baris `CV Genset Prima` bervarian fill, bukan outline

### Asset Admin dalam cakupan: Delete tetap nonaktif dengan alasan yang sama
35. Tampilkan Tabel Service Center dengan kondisi K2
36. Klik `⋯` pada baris `Teknik Mandiri Utama`
37. Verifikasi menu aksi baris memuat `Detail`, `Edit`, `Inactivate`, dan `Delete` berurutan
38. Verifikasi `Delete` nonaktif
39. Arahkan kursor ke `Delete`
40. Verifikasi alasan `This service center has been used. Inactivate it instead.` tersampaikan

### Asset Admin: aksi kelola Hidden bila Available to sebagian di luar cakupan
41. Tampilkan Tabel Service Center dengan kondisi K2
42. Klik `⋯` pada baris `Servis Gabungan Jawa`
43. Verifikasi menu aksi baris memuat `Detail`
44. Verifikasi `Edit`, `Inactivate`, `Activate`, dan `Delete` tidak tampil di menu aksi baris

### Asset Admin: aksi kelola Hidden pada Service Center All groups
45. Tampilkan Tabel Service Center dengan kondisi K2
46. Klik `⋯` pada baris `PT Sejuk Abadi Teknik`
47. Verifikasi menu aksi baris memuat `Detail`
48. Verifikasi `Edit`, `Inactivate`, `Activate`, dan `Delete` tidak tampil di menu aksi baris

### Read Only hanya melihat Detail
49. Tampilkan Tabel Service Center dengan kondisi K3
50. Klik `⋯` pada baris `CV Genset Prima`
51. Verifikasi menu aksi baris memuat `Detail`
52. Verifikasi `Edit`, `Inactivate`, `Activate`, dan `Delete` tidak tampil di menu aksi baris

### Monitoring & Report hanya melihat Detail
53. Tampilkan Tabel Service Center dengan kondisi K4
54. Klik `⋯` pada baris `CV Genset Prima`
55. Verifikasi menu aksi baris memuat `Detail`
56. Verifikasi `Edit`, `Inactivate`, `Activate`, dan `Delete` tidak tampil di menu aksi baris


### Group Manager dalam cakupan: Delete tetap nonaktif dengan alasan yang sama
57. Tampilkan Tabel Service Center dengan kondisi K5
58. Klik `⋯` pada baris `Teknik Mandiri Utama`
59. Verifikasi menu aksi baris memuat `Detail`, `Edit`, `Inactivate`, dan `Delete` berurutan
60. Verifikasi `Delete` nonaktif
61. Arahkan kursor ke `Delete`
62. Verifikasi alasan `This service center has been used. Inactivate it instead.` tersampaikan

### Asset Admin: Activate Hidden pada Service Center Inactive yang Available to-nya sebagian di luar cakupan
63. Tampilkan Tabel Service Center dengan kondisi K6
64. Klik `⋯` pada baris `Bengkel Karya Sentosa`
65. Verifikasi menu aksi baris memuat `Detail`
66. Verifikasi `Activate`, `Edit`, dan `Delete` tidak tampil di menu aksi baris
