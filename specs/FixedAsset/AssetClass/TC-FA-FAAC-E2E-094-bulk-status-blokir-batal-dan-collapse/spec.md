---
id: TC-FA-FAAC-E2E-094-bulk-status-blokir-batal-dan-collapse
title: "Bulk Status: Diblokir, Batal, dan Dialog Single untuk Satu Asset Class"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-246
  - TC-FA-FAAC-247
  - TC-FA-FAAC-248
  - TC-FA-FAAC-252
  - TC-FA-FAAC-667
  - TC-FA-FAAC-668
coverage:
  web: automated
---

# Bulk Status: Diblokir, Batal, dan Dialog Single untuk Satu Asset Class

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Asset Class (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): `B-NAMES` "Names Fixture" dan `B-ONE` "One Name Fixture" masing-masing dengan Asset Name; `B-FREE8` dan `B-FREE9` Active tanpa Asset Name; `B-FREE4` "Free Four" Active tanpa Asset Name; `B-IN3` "Inactive Three" Inactive; `B-IN12` dan `B-IN13` Inactive; `B-FREE16` Active tanpa Asset Name. Spec ini hanya membuka dialog Bulk Action dan menutupnya, tidak mengubah data.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-246: Bulk Deactivate semua diblokir

1. Ketik Search `B-NAMES`, tekan Enter
2. Centang baris `B-NAMES`
3. Ganti isi kotak search dengan `B-ONE`, tekan Enter
4. Centang baris `B-ONE` (seleksi `B-NAMES` bertahan antar Search)
5. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
6. Klik Bulk Action `Deactivate`
7. Verifikasi Dialog Blok `Cannot Deactivate Asset Classes` berisi bullet `• B-NAMES – Names Fixture — has asset names` dan `• B-ONE – One Name Fixture — has asset names` lalu `These asset classes cannot be deactivated.` dengan tombol `OK`
8. Klik `OK`
9. Verifikasi tidak ada perubahan: toggle Active pada baris `B-ONE` tetap On
10. Verifikasi seleksi dipertahankan: baris `B-ONE` tetap tercentang setelah dialog ditutup
11. Ganti isi kotak search dengan `B-NAMES`, tekan Enter
12. Verifikasi tidak ada perubahan: toggle Active pada baris `B-NAMES` tetap On
13. Verifikasi seleksi dipertahankan: baris `B-NAMES` tetap tercentang setelah dialog ditutup
14. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)
15. Klik `Unselect All`

### TC-FA-FAAC-252: Cancel pada dialog bulk mempertahankan seleksi dan tidak mengubah data

16. Ganti isi kotak search dengan `B-FREE8`, tekan Enter
17. Centang baris `B-FREE8`
18. Ganti isi kotak search dengan `B-FREE9`, tekan Enter
19. Centang baris `B-FREE9` (seleksi `B-FREE8` bertahan antar Search)
20. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
21. Klik Bulk Action `Deactivate`
22. Klik `Cancel`
23. Verifikasi tidak ada toast yang tampil
24. Verifikasi dialog menutup
25. Verifikasi baris `B-FREE9` tetap Active dan tetap tercentang
26. Ganti isi kotak search dengan `B-FREE8`, tekan Enter
27. Verifikasi baris `B-FREE8` tetap Active dan tetap tercentang
28. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)
29. Klik `Unselect All`

### TC-FA-FAAC-247: Bulk Deactivate dengan satu Asset Class collapse ke dialog single

30. Ganti isi kotak search dengan `B-FREE4`, tekan Enter
31. Centang baris `B-FREE4`
32. Klik Bulk Action `Deactivate`
33. Verifikasi Dialog versi single `Deactivate Asset Class` (D-01) berisi `• B-FREE4 – Free Four` dan `Are you sure you want to deactivate it?` (bukan versi jamak)
34. Klik `Cancel`
35. Klik `Unselect All`

### TC-FA-FAAC-248: Bulk Activate dengan satu Asset Class collapse ke dialog single

36. Ganti isi kotak search dengan `B-IN3`, tekan Enter
37. Centang baris `B-IN3`
38. Klik Bulk Action `Activate`
39. Verifikasi Dialog versi single `Activate Asset Class` (D-08) berisi `• B-IN3 – Inactive Three` dan `Are you sure you want to activate it?`
40. Klik `Cancel`
41. Klik `Unselect All`

### TC-FA-FAAC-667: Cancel pada dialog Bulk Activate mempertahankan seleksi dan tidak mengubah data

42. Ganti isi kotak search dengan `B-IN12`, tekan Enter
43. Centang baris `B-IN12`
44. Ganti isi kotak search dengan `B-IN13`, tekan Enter
45. Centang baris `B-IN13` (seleksi `B-IN12` bertahan antar Search)
46. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
47. Klik Bulk Action `Activate`
48. Verifikasi Dialog `Activate Asset Classes` tampil dengan tombol `Cancel` dan `Activate`
49. Klik `Cancel`
50. Verifikasi tidak ada toast yang tampil
51. Verifikasi dialog menutup
52. Verifikasi baris `B-IN13` tetap Inactive dan tetap tercentang
53. Ganti isi kotak search dengan `B-IN12`, tekan Enter
54. Verifikasi baris `B-IN12` tetap Inactive dan tetap tercentang
55. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)
56. Klik `Unselect All`

### TC-FA-FAAC-668: Cancel pada dialog Bulk Deactivate campuran mempertahankan seleksi dan tidak mengubah data

57. Ganti isi kotak search dengan `B-FREE16`, tekan Enter
58. Centang baris `B-FREE16`
59. Ganti isi kotak search dengan `B-NAMES`, tekan Enter
60. Centang baris `B-NAMES` (seleksi `B-FREE16` bertahan antar Search)
61. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
62. Klik Bulk Action `Deactivate`
63. Verifikasi Dialog `Deactivate Asset Classes` tampil dengan daftar yang akan dinonaktifkan (`B-FREE16`), daftar yang dilewati (`B-NAMES`), dan tombol `Cancel` dan `Continue`
64. Klik `Cancel`
65. Verifikasi tidak ada toast yang tampil
66. Verifikasi dialog menutup
67. Verifikasi baris `B-NAMES` tetap Active dan tetap tercentang
68. Ganti isi kotak search dengan `B-FREE16`, tekan Enter
69. Verifikasi baris `B-FREE16` tetap Active dan tetap tercentang
70. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)
71. Klik `Unselect All`
72. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: blokir (TC-246) dan batal (TC-252, TC-667, TC-668) lebih dulu, lalu kedua kasus collapse ke dialog single (TC-247 dan TC-248); semua dibatalkan sehingga data tidak berubah.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 15, 29, 35, 41, 56, dan 71 (membersihkan seleksi dengan `Unselect All`, S-09), langkah 5, 20, 46, dan 61 (baseline Changelog, S-12), langkah 1, 3, 11, 16, 18, 26, 30, 36, 42, 44, 53, 57, 59, dan 68 (Search kode untuk menemukan baris target, R-16; seleksi bertahan antar Search menurut prd-conventions, sehingga baris yang sudah dicentang tetap terpilih saat kotak Search diganti), dan langkah 72 (menutup input Search dan mereset tabel, S-09).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. S-05 dan P-1: Expected "tanpa log" pada TC-246, TC-252, TC-667, dan TC-668 diasersi di spec ini (langkah 14, 28, 55, dan 70) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class.
5. Pembagian TC: Bulk Activate dan Deactivate yang berhasil ada di spec 095.
6. Alasan melebihi sekitar 35 langkah (72 langkah): spec berisi enam blok dialog Bulk Action yang masing-masing berdiri sendiri pada baris Asset Class berbeda, satu topik aksi (Bulk Status) tanpa perubahan data; kegagalan satu blok tidak membuat blok lain kehilangan makna.
