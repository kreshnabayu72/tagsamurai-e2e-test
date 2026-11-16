---
id: TC-FA-FACO-E2E-098-mobile-card-list
title: "Card list, bottom sheet, dan seleksi long-press Chart of Accounts di aplikasi mobile"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.6#b1", "§4.6#b2", "§4.6#b4", "§4.6#b5", "§4.6#b6", "§4.6#b7", "§4.6#b8", "§4.7#b1", "§4.2b#p3"]
smoke: []
dependsOn: []
trace:
  "§4.6#b1": [4, 5, 6, 7, 8]
  "§4.6#b2": [21, 27]
  "§4.6#b4": [9, 10, 12, 13, 15]
  "§4.6#b5": [19, 23, 25]
  "§4.6#b6": [29, 31, 32, 33, 34, 35, 37, 38, 40, 43, 47, 51, 57, 64, 65]
  "§4.6#b7": 17
  "§4.6#b8": [72, 73]
  "§4.7#b1": [61, 62, 72, 73]
  "§4.2b#p3": 69
anchor: [3, 42, 46, 50, 55, 56, 60, 68, 71]
coverage:
  android: automated
---

# Card list, bottom sheet, dan seleksi long-press Chart of Accounts di aplikasi mobile

## Prerequisites
- Aktor: User `Bagus Prasetyo {runId}` (Default User, Total Control permanen) di aplikasi Android.
- Layar awal: Beranda aplikasi Fixed Asset di perangkat Android.
- Data:
  - DU-098-1: User `Bagus Prasetyo {runId}` dengan access level Default User (Total Control permanen), scope seluruh client.
  - DU-098-2: akun Account Code `5-6001-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status Active, Used By `0`, belum pernah diekspor.
  - DU-098-3: akun Account Code `4-7001-{runId}`, Account Name `Gain on Disposal {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-098-4: akun Account Code `1-1001-{runId}`, Account Name `Fixed Assets – Equipment {runId}`, Account Function `Asset Cost`, Status Active, Used By `3`, belum pernah diekspor.
  - DU-098-5: akun Account Code `4-7301-{runId}`, Account Name `Gain on Disposal – Vehicles {runId}`, Account Function `Gain on Disposal`, Status Inactive, Used By `0`, belum pernah diekspor.
  - DU-098-6: 8 akun Active dengan Account Code `9-80{n}-{runId}` (n dari 1 sampai 8), Account Name `Operating Expense Cabang {n} {runId}`, Account Function `Asset Cost`, Used By `0`, belum pernah diekspor. Bersama DU-098-2 sampai DU-098-5, hasil Search atas data spec ini berjumlah 12 akun; Account Code `9-80{n}-{runId}` terurut sesudah akun DU-098-2 sampai DU-098-5.
- Kondisi:
  - Daftar Chart of Accounts memuat `10` card per muatan, sehingga 12 akun hasil Search tidak seluruhnya dimuat sekaligus.
  - User `Bagus Prasetyo {runId}` belum pernah membuka halaman Chart of Accounts; flag Guided Tooltip belum disetel.

## Test Steps

### Card list menampilkan isi akun
1. Buka halaman Chart of Accounts di aplikasi Android
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi card dengan Account Code `5-6001-{runId}` tampil
4. Verifikasi card menampilkan Account Code `5-6001-{runId}`
5. Verifikasi card memuat Account Name `Depreciation Expense – Admin {runId}`
6. Verifikasi card memuat badge Function `Depreciation Expense`
7. Verifikasi card memuat switch Status
8. Verifikasi card dengan Account Code `1-1001-{runId}` memuat Used By `3`

### Toolbar, titik masuk Changelog, dan tombol tambah
9. Verifikasi `[🔍]` tampil di toolbar
10. Verifikasi `[⋯]` tampil di toolbar
11. Klik `[⋯]` di toolbar
12. Verifikasi `Column Visibility`, `Filter`, dan `Download` tampil di dalam `[⋯]`
13. Verifikasi `Changelog` tidak ada di dalam `[⋯]`
14. Tutup `[⋯]`
15. Verifikasi ikon Changelog tampil di header halaman
16. Klik ikon Changelog di header halaman
17. Verifikasi modal `Changelog: Chart of Accounts` terbuka
18. Klik ikon close pada modal `Changelog: Chart of Accounts`
19. Verifikasi tombol `+ Account` tampil

### Form tambah dan ubah akun serta aksi per card
20. Klik `+ Account`
21. Verifikasi form `Add Account` tampil dengan field Account Code, Account Name, dan Account Function
22. Klik `[✕]` pada form; form belum diubah sehingga dialog Unsaved Changes tidak muncul
23. Verifikasi ikon `⋯` tampil pada card dengan Account Code `5-6001-{runId}`
24. Klik ikon `⋯` pada card dengan Account Code `5-6001-{runId}`
25. Verifikasi aksi `Edit` dan `Delete` tampil
26. Klik `Edit`
27. Verifikasi form `Edit Account` tampil dengan field Account Code, Account Name, dan Account Function
28. Klik `[✕]` pada form; form belum diubah sehingga dialog Unsaved Changes tidak muncul

### Seleksi long-press masuk dan keluar selection mode
29. Verifikasi card tidak menampilkan checkbox sebelum seleksi dimulai
30. Long-press card dengan Account Code `5-6001-{runId}`
31. Verifikasi counter `1 Selected` tampil pada Floating Bottom Bulk Action Bar
32. Verifikasi kotak seleksi kosong tampil pada card dengan Account Code `4-7001-{runId}`
33. Verifikasi `[Select All]` tampil pada Floating Bottom Bulk Action Bar
34. Verifikasi aksi bulk `Deactivate` dan `Delete` tampil
35. Verifikasi aksi bulk `Activate` tidak tampil
36. Ketuk card dengan Account Code `4-7001-{runId}`
37. Verifikasi counter menunjukkan 2 card terpilih
38. Verifikasi aksi bulk `Activate`, `Deactivate`, dan `Delete` tampil
39. Klik `[Select All]`
40. Verifikasi counter menunjukkan `10` card terpilih, sebanyak card yang sedang dimuat di daftar dan lebih kecil dari `12` akun hasil Search
41. Klik `[✕]` pada Floating Bottom Bulk Action Bar
42. Verifikasi card dengan Account Code `5-6001-{runId}` tampil
43. Verifikasi card tidak menampilkan checkbox dan Floating Bottom Bulk Action Bar tidak tampil
44. Long-press card dengan Account Code `5-6001-{runId}`
45. Ketuk card dengan Account Code `5-6001-{runId}` untuk membatalkan centangnya
46. Verifikasi card dengan Account Code `5-6001-{runId}` tampil
47. Verifikasi card tidak menampilkan checkbox dan Floating Bottom Bulk Action Bar tidak tampil
48. Long-press card dengan Account Code `5-6001-{runId}`
49. Tekan tombol Back perangkat
50. Verifikasi card dengan Account Code `5-6001-{runId}` tampil
51. Verifikasi card tidak menampilkan checkbox dan Floating Bottom Bulk Action Bar tidak tampil
52. Long-press card dengan Account Code `4-7301-{runId}`
53. Klik `Activate` pada Floating Bottom Bulk Action Bar
54. Klik `[Activate]` pada dialog `Activate Account`
55. Verifikasi toast `Success, account has been activated.` tampil
56. Verifikasi card dengan Account Code `5-6001-{runId}` tampil
57. Verifikasi card tidak menampilkan checkbox dan Floating Bottom Bulk Action Bar tidak tampil

### Card list tanpa header kolom dan tanpa Last Used in Journal
58. Buka ulang halaman Chart of Accounts
59. Ketik Search `{runId}`, tekan Enter
60. Verifikasi card dengan Account Code `5-6001-{runId}` tampil
61. Verifikasi card list tidak memiliki header kolom
62. Verifikasi card dengan Account Code `5-6001-{runId}` tidak memuat `Last Used in Journal`

### Aksi bulk untuk seleksi yang seluruhnya Inactive
63. Long-press card dengan Account Code `4-7001-{runId}`
64. Verifikasi aksi bulk `Activate` dan `Delete` tampil
65. Verifikasi aksi bulk `Deactivate` tidak tampil
66. Klik `[✕]` pada Floating Bottom Bulk Action Bar

### Badge Function pada card tanpa tooltip
67. Ketuk badge Function `Depreciation Expense` pada card dengan Account Code `5-6001-{runId}`
68. Verifikasi badge Function `Depreciation Expense` tampil pada card dengan Account Code `5-6001-{runId}`
69. Verifikasi tidak ada tooltip yang tampil pada badge Function `Depreciation Expense`

### Guided Tooltip tidak berjalan di aplikasi Android
70. Buka ulang halaman Chart of Accounts
71. Verifikasi card dengan Account Code `5-6001-{runId}` tampil
72. Verifikasi Guided Tooltip tidak tampil
73. Verifikasi tombol `[?]` tidak tampil
