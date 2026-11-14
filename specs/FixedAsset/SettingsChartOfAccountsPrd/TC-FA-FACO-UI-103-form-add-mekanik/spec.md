---
id: TC-FA-FACO-UI-103-form-add-mekanik
title: "Form Add Account: Saving, menutup form, Clear Field, dan Stay on this form"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [§3.1#p1, §4.1.2#p2, §4.2f#b3, §4.5#b1, §4.5#b2, §9.4.2#r32, §9.5#r7, EB-FRM-1@form-add-account, EB-FRM-2@form-add-account, EB-FRM-3@form-add-account]
smoke: []
dependsOn: []
trace:
  §3.1#p1: [3, 4, 11, 14, 19, 20, 21, 22, 27]
  §4.1.2#p2: [40, 43, 47, 54, 56, 59]
  §4.2f#b3: [47, 48, 56, 59]
  §4.5#b1: [43, 63, 67]
  §4.5#b2: 70
  §9.4.2#r32: 37
  §9.5#r7: 6
  EB-FRM-1@form-add-account: [33, 34, 35, 36, 37]
  EB-FRM-2@form-add-account: [40, 43, 47, 48, 50, 52, 54]
  EB-FRM-3@form-add-account: [77, 78, 79, 80, 81]
anchor: []
coverage:
  web: automated
---

# Form Add Account: Saving, menutup form, Clear Field, dan Stay on this form

## Prerequisites
- Aktor: Total Control.
- Layar awal: Modal Add Account pada Settings > Accounting > Chart of Accounts.
- Komponen: Modal Add Account.
- Kondisi:
  - K1: modal Add Account terbuka dan belum ada isian.
  - K2: seperti K1, dan penyimpanan akun berhasil.
  - K3: seperti K1, dan penyimpanan akun berjalan lambat sehingga respons belum diterima.

## Test Steps

### Validasi gagal menahan Submit
1. Tampilkan Modal Add Account dengan kondisi K1
2. Klik `[Submit]`
3. Verifikasi tidak ada permintaan Create Account yang dikirim sesudah validasi gagal
4. Verifikasi modal Add Account tetap terbuka sesudah validasi gagal

### Submit berhasil menutup form
5. Tampilkan Modal Add Account dengan kondisi K2
6. Verifikasi checkbox `Stay on this form after submitting` tidak tercentang
7. Ketik Account Code `6-3001-GD`
8. Ketik Account Name `Biaya Pemeliharaan Gedung {runId}`
9. Pilih Account Function `Capitalization Offset`
10. Klik `[Submit]`
11. Verifikasi modal Add Account tertutup sesudah Submit berhasil tanpa checkbox Stay tercentang

### Stay on this form mengosongkan form untuk entri berikutnya
12. Tampilkan Modal Add Account dengan kondisi K2
13. Centang checkbox `Stay on this form after submitting`
14. Verifikasi checkbox `Stay on this form after submitting` tercentang
15. Ketik Account Code `6-3002-GD`
16. Ketik Account Name `Biaya Kebersihan Gedung {runId}`
17. Pilih Account Function `Disposal Proceeds`
18. Klik `[Submit]`
19. Verifikasi modal Add Account tetap terbuka sesudah Submit berhasil dengan checkbox Stay tercentang
20. Verifikasi field `Account Code` kosong sesudah form di-reset
21. Verifikasi field `Account Name` kosong sesudah form di-reset
22. Verifikasi field `Account Function` belum terpilih sesudah form di-reset
23. Ketik Account Code `6-3003-GD`
24. Ketik Account Name `Biaya Keamanan Gedung {runId}`
25. Pilih Account Function `Gain on Disposal`
26. Klik `[Submit]`
27. Verifikasi modal Add Account tetap terbuka dan field `Account Code` kosong sesudah entri kedua disimpan

### Saving mencegah klik ganda
28. Tampilkan Modal Add Account dengan kondisi K3
29. Ketik Account Code `6-3001-GD`
30. Ketik Account Name `Biaya Pemeliharaan Gedung {runId}`
31. Pilih Account Function `Capitalization Offset`
32. Klik ganda `[Submit]`
33. Verifikasi tombol `[Submit]` tidak bisa diklik selama permintaan berjalan
34. Verifikasi tombol `[Clear Field]` tidak bisa diklik selama permintaan berjalan
35. Verifikasi tombol `✕` tidak bisa diklik selama permintaan berjalan
36. Verifikasi field `Account Code`, `Account Name`, dan `Account Function` tidak bisa diubah selama permintaan berjalan
37. Verifikasi hanya satu permintaan Create Account yang dikirim sesudah klik ganda

### Menutup form yang belum diubah
38. Tampilkan Modal Add Account dengan kondisi K1
39. Klik `✕` pada form yang belum diubah
40. Verifikasi modal Add Account tertutup langsung tanpa dialog Unsaved Changes sesudah `✕` diklik

### Esc menutup form yang belum diubah
41. Tampilkan Modal Add Account dengan kondisi K1
42. Tekan `Esc` pada form yang belum diubah
43. Verifikasi modal Add Account tertutup langsung tanpa dialog Unsaved Changes sesudah `Esc` ditekan

### Menutup form yang sudah diisi memunculkan Unsaved Changes
44. Tampilkan Modal Add Account dengan kondisi K1
45. Ketik Account Name `Biaya Listrik Kantor`
46. Klik `✕` pada form yang sudah diisi
47. Verifikasi dialog `Unsaved Changes` tampil dengan pesan `You have unsaved changes. Are you sure you want to leave?`
48. Verifikasi dialog Unsaved Changes memiliki tombol `[Leave]` dan `[Cancel]`
49. Tekan `Esc`
50. Verifikasi dialog Unsaved Changes tertutup dan modal Add Account tetap terbuka dengan Account Name `Biaya Listrik Kantor`, sama seperti `[Cancel]`
51. Klik area backdrop di luar modal Add Account
52. Verifikasi modal Add Account tetap terbuka dengan Account Name `Biaya Listrik Kantor` tanpa dialog Unsaved Changes
53. Tekan `Esc` pada form yang sudah diisi
54. Verifikasi dialog Unsaved Changes tampil sesudah `Esc` ditekan pada form yang sudah diisi
55. Klik `[Cancel]` pada dialog Unsaved Changes
56. Verifikasi dialog Unsaved Changes tertutup dan modal Add Account tetap terbuka dengan Account Name `Biaya Listrik Kantor` sesudah `[Cancel]`
57. Klik `✕` pada form yang sudah diisi
58. Klik `[Leave]` pada dialog Unsaved Changes
59. Verifikasi modal Add Account tertutup tanpa menyimpan sesudah `[Leave]`

### Navigasi keyboard di modal
60. Tampilkan Modal Add Account dengan kondisi K1
61. Tekan Tab sampai fokus berada pada checkbox `Stay on this form after submitting`
62. Tekan Space
63. Verifikasi checkbox `Stay on this form after submitting` tercentang lewat keyboard
64. Ketik Account Name `Biaya Listrik Kantor`
65. Tekan Tab sampai fokus berada pada `[Clear Field]`
66. Tekan Enter
67. Verifikasi field `Account Name` kosong sesudah `[Clear Field]` diaktifkan lewat keyboard

### Fokus ter-trap di modal
68. Tampilkan Modal Add Account dengan kondisi K1
69. Tekan Shift+Tab pada elemen interaktif pertama di modal Add Account
70. Verifikasi fokus berpindah ke elemen interaktif terakhir di modal Add Account dan tidak keluar ke halaman di belakangnya

### Clear Field mengosongkan form Add
71. Tampilkan Modal Add Account dengan kondisi K1
72. Ketik Account Code `6-3004-GD`
73. Ketik Account Name `Biaya Asuransi Gedung {runId}`
74. Pilih Account Function `Gain on Disposal`
75. Centang checkbox `Stay on this form after submitting`
76. Klik `[Clear Field]`
77. Verifikasi field `Account Code` dikosongkan oleh `[Clear Field]`
78. Verifikasi field `Account Name` dikosongkan oleh `[Clear Field]`
79. Verifikasi field `Account Function` kembali belum terpilih oleh `[Clear Field]`
80. Verifikasi tidak ada dialog konfirmasi yang tampil sesudah `[Clear Field]` diklik
81. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang sesudah `[Clear Field]` diklik
