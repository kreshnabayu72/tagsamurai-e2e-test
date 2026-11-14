---
id: TC-FA-FACO-E2E-098-mobile-card-list
title: "Card list, bottom sheet, dan seleksi long-press Chart of Accounts di aplikasi mobile"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.6#p1", "§4.6#b1", "§4.6#b2", "§4.6#b4", "§4.6#b5", "§4.6#b6", "§4.6#b7", "§4.6#b8", "§4.7#b1"]
smoke: []
dependsOn: []
trace:
  "§4.6#p1": 4
  "§4.6#b1": [4, 5, 6, 7, 8]
  "§4.6#b2": [21, 27]
  "§4.6#b4": [9, 10, 12, 13, 15]
  "§4.6#b5": [19, 23, 25]
  "§4.6#b6": [29, 31, 32, 33, 34, 35, 37, 38, 40, 43, 47, 51, 57]
  "§4.6#b7": 17
  "§4.6#b8": 59
  "§4.7#b1": [59, 60]
anchor: [3, 42, 46, 50, 55, 56]
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

## Test Steps

### Card list menampilkan isi akun
1. Buka halaman Chart of Accounts di aplikasi Android
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi card dengan Account Code `5-6001-{runId}` tampil
4. Verifikasi judul card memuat Account Code `5-6001-{runId}`
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
40. Verifikasi counter menunjukkan 4 card terpilih, sama dengan seluruh card yang dimuat
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

### Guided Tooltip tidak berjalan
58. Buka ulang halaman Chart of Accounts
59. Verifikasi Guided Tooltip tidak berjalan di aplikasi Android[^drift-1]
60. Verifikasi tombol `[?]` tidak tampil di header halaman[^drift-1]

[^drift-1]: Drift PRD vs foundation. PRD §4.7: «Guided Tooltip tidak berjalan di aplikasi Android; tur dan tombol `[?]` hanya tampil pada tampilan desktop». foundation `guided-tooltip.md` §16.3: «Mobile | Tooltip muncul sebagai bottom sheet mini; spotlight tetap ada; swipe left/right = Next/Back». Diasersi: PRD, karena target step 1 sampai 5 tidak ada di card list dan ini konfigurasi khusus modul (SB-4).
