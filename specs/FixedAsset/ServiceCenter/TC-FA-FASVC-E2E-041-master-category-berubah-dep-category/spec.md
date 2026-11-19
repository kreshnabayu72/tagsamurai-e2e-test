---
id: TC-FA-FASVC-E2E-041-master-category-berubah-dep-category
title: "Category Dihapus atau Dipindah: Specialization Dilepas dan Cakupan Melebar"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [MR-FASVC-03, MR-FASVC-04a, MR-FASVC-04b, MR-FASVC-04c, EC-FASVC-14a, EC-FASVC-14b, F-FASVC-08.k4, "§8#r17", "§9.7#r5", "§9.2#p7", MR-FASVC-08a, MR-FASVC-08b, MR-FASVC-08c, EC-FASVC-57a, EC-FASVC-57b, EC-FASVC-57c, F-FASVC-08.k8, "§9.4.3#b4", MR-FASVC-09a]
smoke: []
dependsOn: ["Category: pohon Category dan master Category"]
trace:
  MR-FASVC-03: [17, 26, 28, 29, 32]
  MR-FASVC-04a: [7, 42]
  MR-FASVC-04b: [6, 42]
  MR-FASVC-04c: [10, 46, 47]
  EC-FASVC-14a: [6, 42]
  EC-FASVC-14b: [10, 46, 47]
  F-FASVC-08.k4: [6, 10]
  "§8#r17": 10
  "§9.7#r5": [7, 28]
  "§9.2#p7": [42, 46, 47]
  MR-FASVC-08a: 76
  MR-FASVC-08b: 72
  MR-FASVC-08c: [64, 65, 67]
  EC-FASVC-57a: 72
  EC-FASVC-57b: [64, 65, 67]
  EC-FASVC-57c: 75
  F-FASVC-08.k8: [75, 76]
  "§9.4.3#b4": 72
  MR-FASVC-09a: [6, 43]
anchor: [2, 13, 38, 50, 55, 58]
coverage:
  web: automated
---

# Category Dihapus atau Dipindah: Specialization Dilepas dan Cakupan Melebar

## Prerequisites
- Aktor: Total Control `Rina Wulandari {runId}` (cakupan seluruh Group) menguji layarnya. Admin Category `Dimas Pratama {runId}` (Total Control, cakupan seluruh Group) memicu perubahan di master Category dari sesinya sendiri.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-041-1: Category `Pendingin {runId}`, parent root pohon Category, ada di entitas aktor.
  - DU-041-2: Category `AC {runId}`, parent `Pendingin {runId}`.
  - DU-041-3: Category `Mesin {runId}`, parent root pohon Category.
  - DU-041-4: Category `Genset {runId}`, parent `Mesin {runId}`.
  - DU-041-5: Service Center `Servis Pendingin Mitra {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization `AC {runId}` (satu-satunya Category), Brands kosong (`All brands`), Country `Indonesia`, City `Surabaya`, Company phone Dial Code `+62` nomor `81234500411`, Company email `pendingin@mitrapendingin.example`, Usage `0`, Status `Active`.
  - DU-041-6: Service Center `Servis Genset Mitra {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization `Genset {runId}`, Brands kosong (`All brands`), Country `Indonesia`, City `Gresik`, Company phone Dial Code `+62` nomor `81234500412`, Company email `genset@mitragenset.example`, Usage `0`, Status `Active`.
  - DU-041-7: User Total Control `Rina Wulandari {runId}`, cakupan seluruh Group.
  - DU-041-8: User Admin Category `Dimas Pratama {runId}`, role Total Control, cakupan seluruh Group.
  - DU-041-9: Category `Kelistrikan {runId}`, parent root pohon Category.
  - DU-041-10: Category `Panel Listrik {runId}`, parent `Kelistrikan {runId}`.
  - DU-041-11: Category `Kabel Daya {runId}`, parent `Kelistrikan {runId}`.
  - DU-041-12: Service Center `Servis Kelistrikan Mitra {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization `Kabel Daya {runId}` dan `Panel Listrik {runId}`, Brands kosong (`All brands`), Country `Indonesia`, City `Kediri`, Company phone Dial Code `+62` nomor `81234500413`, Company email `kelistrikan@mitrakelistrikan.example`, Usage `0`, Status `Active`.
  - DU-041-13: Category `Peralatan Bengkel {runId}`, parent root pohon Category. Nama Category ini kemudian diubah menjadi `Peralatan Servis {runId}`.
  - DU-041-14: Category `Perkakas {runId}`, parent root pohon Category.
  - DU-041-15: Service Center `Servis Perkakas Mitra {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization `Peralatan Bengkel {runId}`, Brands kosong (`All brands`), Country `Indonesia`, City `Malang`, Company phone Dial Code `+62` nomor `81234500414`, Company email `perkakas@mitraperkakas.example`, Usage `0`, Status `Active`.
  - Category pada DU-041-1 sampai DU-041-4, DU-041-9 sampai DU-041-11, DU-041-13, dan DU-041-14 belum dipakai aset.

## Test Steps

### Category satu-satunya di Specialization dihapus: cakupan melebar ke semua Category
1. Ketik Search `Servis Pendingin Mitra {runId}`, tekan Enter
2. Verifikasi baris `Servis Pendingin Mitra {runId}` tampil dengan Specialization `AC {runId}`
3. Admin Category menghapus Category `AC {runId}` dari master Category
4. Muat ulang halaman
5. Ganti isi kotak Search dengan `Servis Pendingin Mitra {runId}`, tekan Enter
6. Verifikasi Specialization baris `Servis Pendingin Mitra {runId}` tampil `All categories`
7. Verifikasi Specialization baris `Servis Pendingin Mitra {runId}` tidak memuat `AC {runId}`
8. Klik `Changelog` pada toolbar
9. Ketik Search `Servis Pendingin Mitra {runId}` pada modal `Changelog: Service Center`, tekan Enter
10. Verifikasi entri dengan Action `Updated`, Field `Specialization`, Old Value `AC {runId}`, New Value `All categories`, dan Modified By `System` tampil
11. Tutup modal `Changelog: Service Center` lewat icon close

### Category dipindah ke parent lain: Specialization mengikuti posisi baru tanpa perubahan data
12. Ganti isi kotak Search dengan `Servis Genset Mitra {runId}`, tekan Enter
13. Verifikasi baris `Servis Genset Mitra {runId}` tampil dengan Specialization `Genset {runId}`
14. Klik `Filter` pada toolbar
15. Centang `Pendingin {runId}` pada field Specialization di Filter Panel
16. Klik `[Apply]`
17. Verifikasi pesan `No results found` tampil karena `Genset {runId}` belum berada di bawah `Pendingin {runId}`
18. Klik `Changelog` pada toolbar
19. Ketik Search `Servis Genset Mitra {runId}` pada modal `Changelog: Service Center`, tekan Enter
20. Catat jumlah baris yang tampil di modal sebagai jumlah awal
21. Tutup modal `Changelog: Service Center` lewat icon close
22. Admin Category memindahkan Category `Genset {runId}` dari parent `Mesin {runId}` ke parent `Pendingin {runId}`
23. Muat ulang halaman
24. Ganti isi kotak Search dengan `Servis Genset Mitra {runId}`, tekan Enter
25. Klik `Filter` pada toolbar
26. Verifikasi `Pendingin {runId}` sudah tercentang pada field Specialization di Filter Panel
27. Klik `[Apply]`
28. Verifikasi baris `Servis Genset Mitra {runId}` tampil karena `Genset {runId}` kini berada di bawah `Pendingin {runId}`
29. Verifikasi Specialization baris `Servis Genset Mitra {runId}` tetap `Genset {runId}`
30. Klik `Changelog` pada toolbar
31. Ketik Search `Servis Genset Mitra {runId}` pada modal `Changelog: Service Center`, tekan Enter
32. Verifikasi jumlah baris untuk `Servis Genset Mitra {runId}` di modal sama dengan jumlah awal
33. Tutup modal `Changelog: Service Center` lewat icon close

### Category induk dihapus beserta subtree: seluruh node dilepas dalam satu event dan cakupan melebar sekali
34. Klik `Filter` pada toolbar
35. Klik `[Clear Field]`
36. Klik `[Apply]`
37. Ganti isi kotak Search dengan `Servis Kelistrikan Mitra {runId}`, tekan Enter
38. Verifikasi baris `Servis Kelistrikan Mitra {runId}` tampil dengan Specialization `Kabel Daya {runId}` dan `Panel Listrik {runId}`
39. Admin Category menghapus Category `Kelistrikan {runId}` beserta subtree-nya (`Panel Listrik {runId}` dan `Kabel Daya {runId}`) dari master Category
40. Muat ulang halaman
41. Ganti isi kotak Search dengan `Servis Kelistrikan Mitra {runId}`, tekan Enter
42. Verifikasi Specialization baris `Servis Kelistrikan Mitra {runId}` tampil `All categories`
43. Verifikasi tidak ada dialog konfirmasi yang meminta persetujuan pengguna atas pelebaran Specialization `Servis Kelistrikan Mitra {runId}`
44. Klik `Changelog` pada toolbar
45. Ketik Search `Servis Kelistrikan Mitra {runId}` pada modal `Changelog: Service Center`, tekan Enter
46. Verifikasi entri dengan Action `Updated`, Field `Specialization`, Old Value `Kabel Daya {runId}, Panel Listrik {runId}`, New Value `All categories`, dan Modified By `System` tampil
47. Verifikasi hanya ada satu entri dengan Action `Updated` dan Field `Specialization` untuk `Servis Kelistrikan Mitra {runId}`
48. Tutup modal `Changelog: Service Center` lewat icon close

### Category di-rename: nama terkini tampil di tabel dan form, pencocokan memakai ID, Changelog lama tetap nama snapshot
49. Ganti isi kotak Search dengan `Servis Perkakas Mitra {runId}`, tekan Enter
50. Verifikasi baris `Servis Perkakas Mitra {runId}` tampil dengan Specialization `Peralatan Bengkel {runId}`
51. Klik `⋯` pada baris `Servis Perkakas Mitra {runId}`, lalu klik `Edit`
52. Klik field Specialization untuk membuka tree Category
53. Centang `Perkakas {runId}` pada tree Specialization
54. Klik `[Save]`
55. Verifikasi Specialization baris `Servis Perkakas Mitra {runId}` memuat `Peralatan Bengkel {runId}` dan `Perkakas {runId}`
56. Klik `Changelog` pada toolbar
57. Ketik Search `Servis Perkakas Mitra {runId}` pada modal `Changelog: Service Center`, tekan Enter
58. Verifikasi entri dengan Action `Updated`, Field `Specialization`, Old Value `Peralatan Bengkel {runId}`, dan New Value `Peralatan Bengkel {runId}, Perkakas {runId}` tampil
59. Catat jumlah baris yang tampil di modal sebagai jumlah awal
60. Tutup modal `Changelog: Service Center` lewat icon close
61. Admin Category mengubah nama Category `Peralatan Bengkel {runId}` menjadi `Peralatan Servis {runId}` di master Category
62. Muat ulang halaman
63. Ganti isi kotak Search dengan `Servis Perkakas Mitra {runId}`, tekan Enter
64. Verifikasi Specialization baris `Servis Perkakas Mitra {runId}` memuat `Peralatan Servis {runId}` dan `Perkakas {runId}`
65. Verifikasi Specialization baris `Servis Perkakas Mitra {runId}` tidak memuat `Peralatan Bengkel {runId}`
66. Klik `⋯` pada baris `Servis Perkakas Mitra {runId}`, lalu klik `Edit`
67. Verifikasi field Specialization di dialog `Edit Service Center` memuat `Peralatan Servis {runId}`
68. Klik `✕` pada form yang belum diubah
69. Klik `Filter` pada toolbar
70. Centang `Peralatan Servis {runId}` pada field Specialization di Filter Panel
71. Klik `[Apply]`
72. Verifikasi baris `Servis Perkakas Mitra {runId}` tampil karena Category `Peralatan Servis {runId}` dicocokkan lewat ID
73. Klik `Changelog` pada toolbar
74. Ketik Search `Servis Perkakas Mitra {runId}` pada modal `Changelog: Service Center`, tekan Enter
75. Verifikasi entri dengan Action `Updated`, Field `Specialization`, dan New Value `Peralatan Bengkel {runId}, Perkakas {runId}` tetap tampil dengan nama lama
76. Verifikasi jumlah baris untuk `Servis Perkakas Mitra {runId}` di modal sama dengan jumlah awal
77. Tutup modal `Changelog: Service Center` lewat icon close
