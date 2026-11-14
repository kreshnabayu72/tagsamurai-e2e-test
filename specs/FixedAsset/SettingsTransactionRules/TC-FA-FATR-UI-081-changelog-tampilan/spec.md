---
id: TC-FA-FATR-UI-081-changelog-tampilan
title: "Dialog Changelog: kolom, format, dan empty state"
layer: ui-client
priority: High
caseType: Positive
status: draft
sourceRules:
  - "§4.1#r12"
  - "§4.1#r41"
  - "§4.1#r398"
  - "§4.1#r399"
  - "§4.1#r402"
  - "§4.1#r403"
  - "§4.1#r400"
  - "§4.1#r401"
  - "§4.1#r404"
  - "§4.1#p88"
  - "§4.5#b4"
  - "§5#r1"
  - "§7#r18"
  - "D-08"
  - "S-08"
  - "§9.2#b376"
  - "§9.4.2#r53"
  - "§9.4.4#r44"
  - "§9.5#r29"
  - "EB-TBL-1@changelog"
  - "EB-TBL-4@modified-by-changelog"
  - "EB-TBL-8@changelog"
  - "EB-XM-1"
smoke: []
dependsOn: []
trace:
  §4.1#r12: 3
  §4.1#r41: [31, 32]
  §4.1#r398: [16, 18, 20, 21, 27, 43]
  §4.1#r399: [16, 18, 22, 27, 47]
  §4.1#r402: [16, 18, 27, 29, 30, 32, 47]
  §4.1#r403: [16, 18, 27, 29, 31, 47]
  §4.1#r400: [16, 18, 23, 24, 27, 44]
  §4.1#r401: [16, 18, 25, 26, 27, 45]
  §4.1#r404: [16, 18, 27, 34, 35, 38, 46]
  §4.1#p88: [5, 11, 13, 14]
  §4.5#b4: [50, 52]
  §5#r1: [5, 7, 9, 11]
  §7#r18: [54, 55]
  D-08: 2
  S-08: [58, 59, 69]
  §9.2#b376: [54, 55, 58, 59]
  §9.4.2#r53: [54, 58, 69]
  §9.4.4#r44: [54, 58]
  §9.5#r29: [54, 55]
  EB-TBL-1@changelog: [54, 58, 60, 62, 63, 64]
  EB-TBL-4@modified-by-changelog: [34, 35, 37]
  EB-TBL-8@changelog: 40
  EB-XM-1: [20, 21]
anchor: []
coverage:
  web: automated
---

# Dialog Changelog: kolom, format, dan empty state

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings, Dialog Changelog dibuka dari tombol `[Changelog]` di header halaman.
- Komponen: Dialog Changelog
- Data:
  - DU-081-1: entri Date `2026-06-15 14:05` (tampil `15/06/26 14:05`), Action `Edit`, Category `Vehicle > Pool car`, Field `Borrow (Max duration)`, Old Value `14 days`, New Value `30 days`, Modified By `Budi Santoso` (tampil `Budi S`).
  - DU-081-2: entri Date `2026-06-12 09:30` (tampil `12/06/26 09:30`), Action `Edit`, Category `All categories`, Field `Borrow (Allow Borrow)`, Old Value `Allow`, New Value `Deny`, Modified By `Siti Nurbaya` (tampil `Siti N`).
  - DU-081-3: entri Date `2026-06-10 16:45` (tampil `10/06/26 16:45`), Action `Edit`, Category `Machinery`, Field `Borrow (Max extensions)`, Old Value `1`, New Value `No extension`, Modified By `Alexander Graham Bell` (tampil `Alexander G`).
  - DU-081-4: entri Date `2026-06-08 08:15` (tampil `08/06/26 08:15`), Action `Edit`, Category `Vehicle > Pool car`, Field `Borrow (Max duration)`, Old Value `Inherit`, New Value `30 days`, Modified By `Siti Nurbaya` (tampil `Siti N`).
  - DU-081-5: entri Date `2026-06-05 11:20` (tampil `05/06/26 11:20`), Action `Edit`, Category `Vehicle > <b>Pool</b> car`, Field `Borrow (Max duration)`, Old Value `7 days`, New Value `14 days`, Modified By `Budi Santoso` (tampil `Budi S`).
  - DU-081-6: entri Date `2026-06-01 15:50` (tampil `01/06/26 15:50`), Action `Edit`, Category `Machinery`, Field `Borrow (Max extensions)`, Old Value `No extension`, New Value `1`, Modified By `Rina Wulandari` (tampil `Rina W`), pengguna itu kemudian dihapus.
  - DU-081-7: kata kunci Search `Zebra Tidak Ada`, tidak cocok dengan baris mana pun.
  - DU-081-8: filter Date rentang dari `01/01/25` sampai `31/01/25`, di luar semua entri, tidak menghasilkan baris.
- Kondisi:
  - K1: tabel berisi DU-081-1 sampai DU-081-6; Date Format bernilai `dd/MM/yy`; Time Format bernilai `24h`; waktu pada respons sudah dalam Time Zone entitas.
  - K2: belum ada entri changelog.
  - K3: sama dengan K1; respons atas Search DU-081-7 dan atas filter Date DU-081-8 tidak memuat baris; kedua saringan dipakai pada tampilan terpisah.
  - K4: memuat tabel gagal karena error server.

## Test Steps

### Judul dan komponen dialog
1. Tampilkan Dialog Changelog dengan kondisi K1
2. Verifikasi judul dialog `Changelog: Transaction Settings`
3. Verifikasi dialog memuat tabel changelog, ikon Search, tombol filter, Filter Panel yang dapat dibuka, ikon Download, dan Column Visibility yang memuat `Setup Column...`

### Toolbar dan tabel tanpa row action
4. Tampilkan Dialog Changelog dengan kondisi K1
5. Verifikasi toolbar memuat ikon Search, tombol filter, lalu ikon Download berurutan dari kiri ke kanan
6. Arahkan kursor ke ikon Search di toolbar
7. Verifikasi ikon Search menyampaikan nama fungsinya `Search`
8. Arahkan kursor ke tombol filter di toolbar
9. Verifikasi tombol filter menyampaikan nama fungsinya `Filter`
10. Arahkan kursor ke ikon Download di toolbar
11. Verifikasi ikon Download menyampaikan tooltip `Download`
12. Klik ikon Search di toolbar
13. Verifikasi kotak Search memuat placeholder `Search changelog...`
14. Verifikasi baris tabel tidak memiliki menu aksi baris

### Susunan kolom dan Column Visibility
15. Tampilkan Dialog Changelog dengan kondisi K1
16. Verifikasi header tabel berurutan dari kiri: `Date`, `Action`, `Category`, `Field`, `Old Value`, `New Value`, `Modified By`
17. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
18. Verifikasi daftar Column Visibility hanya memuat kolom `Date`, `Action`, `Category`, `Field`, `Old Value`, `New Value`, `Modified By`, tanpa kolom tambahan yang belum tercentang, seluruhnya tercentang dan tidak disabled

### Format kolom Date, Action, Category, dan Field
19. Tampilkan Dialog Changelog dengan kondisi K1
20. Verifikasi sel Date pada baris Old Value `14 days` memuat tanggal `15/06/26` dan jam `14:05`
21. Verifikasi sel Date pada baris Field `Borrow (Allow Borrow)` memuat tanggal `12/06/26` dan jam `09:30`
22. Verifikasi sel Action pada setiap baris berisi `Edit`
23. Verifikasi sel Category pada baris Date `15/06/26 14:05` berisi `Vehicle > Pool car`
24. Verifikasi sel Category pada baris Date `12/06/26 09:30` berisi `All categories`
25. Verifikasi sel Field pada baris Date `15/06/26 14:05` berisi `Borrow (Max duration)`
26. Verifikasi sel Field pada baris Date `12/06/26 09:30` berisi `Borrow (Allow Borrow)`
27. Verifikasi sel Date, Action, Category, Field, Old Value, New Value, dan Modified By di setiap baris berisi nilai dan tidak menampilkan `—`

### Format kolom Old Value dan New Value
28. Tampilkan Dialog Changelog dengan kondisi K1
29. Verifikasi sel Old Value `14 days` dan New Value `30 days` pada baris Field `Borrow (Max duration)` Date `15/06/26 14:05`, nilai ditulis dengan satuannya
30. Verifikasi sel Old Value pada baris Date `08/06/26 08:15` berisi `Inherit`
31. Verifikasi sel New Value pada baris Date `10/06/26 16:45` berisi `No extension`, nilai 0 tampil sebagai teks maknanya
32. Verifikasi sel Old Value pada baris Date `01/06/26 15:50` berisi `No extension`, nilai 0 tampil sebagai teks maknanya

### Format kolom Modified By
33. Tampilkan Dialog Changelog dengan kondisi K1
34. Verifikasi sel Modified By pada baris Date `15/06/26 14:05` berisi `Budi S`
35. Verifikasi sel Modified By pada baris Date `10/06/26 16:45` berisi `Alexander G`
36. Arahkan kursor ke sel Modified By pada baris Date `15/06/26 14:05`
37. Verifikasi nama lengkap `Budi Santoso` tersampaikan pada sel Modified By
38. Verifikasi sel Modified By pada baris Date `01/06/26 15:50` tetap berisi `Rina W` walau pengguna itu sudah dihapus

### Teks sel berisi markup
39. Tampilkan Dialog Changelog dengan kondisi K1
40. Verifikasi sel Category pada baris Date `05/06/26 11:20` menampilkan `Vehicle > <b>Pool</b> car` apa adanya sebagai teks

### Field Filter Panel
41. Tampilkan Dialog Changelog dengan kondisi K1
42. Klik tombol filter di toolbar
43. Verifikasi field filter `Date` berupa pemilih rentang tanggal dengan placeholder `Select date`
44. Verifikasi field filter `Category` berupa multi-select dengan placeholder `All categories`
45. Verifikasi field filter `Field` berupa multi-select dengan placeholder `All fields`
46. Verifikasi field filter `Modified By` berupa multi-select dengan placeholder `All users`
47. Verifikasi Filter Panel tidak memuat field filter `Action`, `Old Value`, dan `New Value`

### Menutup dialog
48. Tampilkan Dialog Changelog dengan kondisi K1
49. Klik backdrop di luar dialog
50. Verifikasi Dialog Changelog tetap terbuka
51. Tekan `Esc`
52. Verifikasi Dialog Changelog tertutup

### Empty state belum ada entri
53. Tampilkan Dialog Changelog dengan kondisi K2
54. Verifikasi judul empty state `No changelog yet` tampil
55. Verifikasi deskripsi `Activities and changes will appear here.` tampil

### Empty state hasil Search dan Filter tanpa hasil
56. Tampilkan Dialog Changelog dengan kondisi K3
57. Ketik Search `Zebra Tidak Ada`, tekan Enter
58. Verifikasi judul empty state `No results found` tampil pada tabel Changelog
59. Verifikasi deskripsi empty state `Try adjusting your search or filter.` tampil pada tabel Changelog
60. Verifikasi `No changelog yet` tidak tampil

### Gagal memuat tabel
61. Tampilkan Dialog Changelog dengan kondisi K4
62. Verifikasi pesan `Unable to load this data.` tampil pada tabel Changelog
63. Verifikasi tombol `[Try Again]` tampil pada tabel Changelog
64. Verifikasi `No changelog yet` tidak tampil

### Empty state hasil Filter tanpa hasil
65. Tampilkan Dialog Changelog dengan kondisi K3
66. Klik tombol filter di toolbar
67. Pada field `Date`, pilih rentang dari `01/01/25` sampai `31/01/25`
68. Klik `[Apply]`
69. Verifikasi judul empty state `No results found` tampil pada tabel Changelog sesudah filter
