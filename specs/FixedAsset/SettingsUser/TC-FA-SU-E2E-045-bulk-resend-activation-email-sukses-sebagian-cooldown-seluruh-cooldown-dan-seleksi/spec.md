---
id: TC-FA-SU-E2E-045-bulk-resend-activation-email-sukses-sebagian-cooldown-seluruh-cooldown-dan-seleksi
title: "Bulk Resend Activation Email: Sukses, Sebagian Cooldown, Seluruh Cooldown, dan Seleksi Campuran"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-153
  - TC-FA-SU-154
  - TC-FA-SU-155
  - TC-FA-SU-157
coverage:
  web: automated
---

# Bulk Resend Activation Email: Sukses, Sebagian Cooldown, Seluruh Cooldown, dan Seleksi Campuran

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; layanan #37): Hana Kusuma dan Kartika Sari (Pending Activation; Kartika Inactive), Indra Wijaya (Pending Email Confirmation), dan Gita Permata (Activated). Cooldown Resend belum berjalan saat tiap blok dimulai; dipulihkan lewat seed API di hook `before`, langkah 20, dan langkah 34.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri log Resend per pengguna di Tab Changelog target dan di Tab System Log aktor (baseline, bagian 8b butir 10); jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC); seed API untuk mereset cooldown.
- Baseline log: hook `before` mencatat jumlah entri `Resend Activation Email` Hana dan Kartika pada Tab Changelog target, Tab System Log aktor, dan Activity Log. Entri log muncul eventual (NC-03): pemeriksaan surface log memuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- Jam: jam server dan jam browser dibekukan bersama pada langkah 1 supaya tooltip cooldown bernilai tepat 60 detik, dilepas pada langkah 11 (sebelum surface log dibuka, S-09). Pada blok TC-FA-SU-154 dan TC-FA-SU-155 hanya jam server yang dibekukan (langkah 21 sampai 29 dan langkah 35 sampai 43, R-10) supaya cooldown 60 detik tidak habis selama aksi Resend, seleksi, dan toast; jam browser tetap berjalan supaya muat ulang surface log dapat menunggu entri. Hook `after` memulihkan jam.
- State global dan pemulihan: jam; cooldown Hana dan Kartika dipulihkan lewat seed API di hook `after`; entri log Resend bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-153: Bulk Resend Activation Email seluruh baris Pending Activation

1. Bekukan jam server dan jam browser bersamaan
2. Ketik Search `Hana Kusuma`, tekan Enter, lalu centang baris Hana Kusuma
3. Ganti isi kotak search dengan `Kartika Sari`, tekan Enter, lalu centang baris Kartika Sari
4. Verifikasi Bulk Actions Bar memuat aksi `Resend Activation Email`
5. Klik Bulk Action, pilih `Resend Activation Email`
6. Verifikasi toast "Success, activation email has been sent." tampil tanpa nama pengguna
7. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu klik ⋯ pada baris Hana Kusuma, hover `Resend Activation Email`
8. Verifikasi `Resend Activation Email` baris Hana Kusuma Disabled dengan tooltip "Please wait 60 seconds before resending."
9. Ganti isi kotak search dengan `Kartika Sari`, tekan Enter, lalu klik ⋯ pada baris Kartika Sari, hover `Resend Activation Email`
10. Verifikasi `Resend Activation Email` baris Kartika Sari Disabled dengan tooltip "Please wait 60 seconds before resending."
11. Lepaskan pembekuan jam
12. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu buka Detail Hana Kusuma > Tab Changelog, muat ulang sampai entri tampil
13. Verifikasi satu entri `Resend Activation Email` Hana Kusuma tercatat (selisih 1 dari baseline) di Tab Changelog Hana Kusuma
14. Kembali ke User List, ganti isi kotak search dengan `Kartika Sari`, tekan Enter, lalu buka Detail Kartika Sari > Tab Changelog, muat ulang sampai entri tampil
15. Verifikasi satu entri `Resend Activation Email` Kartika Sari tercatat (selisih 1 dari baseline) di Tab Changelog Kartika Sari
16. Buka Tab System Log aktor, muat ulang sampai entri tampil
17. Verifikasi satu entri `Resend Activation Email` per pengguna (Hana Kusuma dan Kartika Sari) tercatat (selisih 1 dari baseline masing-masing) di Tab System Log aktor
18. Buka Activity Log, muat ulang sampai entri tampil
19. Verifikasi satu entri `Resend Activation Email` per pengguna (Hana Kusuma dan Kartika Sari) tercatat (selisih 1 dari baseline masing-masing) di Activity Log

### TC-FA-SU-154: Bulk Resend sebagian baris dalam cooldown

20. Pulihkan Hana Kusuma dan Kartika Sari tanpa cooldown lewat seed API, lalu muat ulang halaman User List
21. Bekukan jam server
22. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu klik ⋯ pada baris Hana Kusuma, kemudian `Resend Activation Email`
23. Buka Detail Hana Kusuma > Tab Changelog, muat ulang sampai entri `Resend Activation Email` dari langkah 22 tampil, lalu catat baseline jumlah entri `Resend Activation Email` Hana Kusuma
24. Kembali ke User List, ganti isi kotak search dengan `Kartika Sari`, tekan Enter, lalu buka Detail Kartika Sari > Tab Changelog dan catat baseline jumlah entri `Resend Activation Email` Kartika Sari
25. Kembali ke User List, ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu centang baris Hana Kusuma (dalam masa cooldown)
26. Ganti isi kotak search dengan `Kartika Sari`, tekan Enter, lalu centang baris Kartika Sari
27. Klik Bulk Action, pilih `Resend Activation Email`
28. Verifikasi toast "Success, activation email has been sent. Some items were skipped (cooldown not finished)."
29. Lepaskan pembekuan jam server
30. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu buka Detail Hana Kusuma > Tab Changelog
31. Verifikasi jumlah entri `Resend Activation Email` Hana Kusuma sama dengan baseline langkah 23 (baris cooldown di-skip tanpa entri log)
32. Kembali ke User List, ganti isi kotak search dengan `Kartika Sari`, tekan Enter, lalu buka Detail Kartika Sari > Tab Changelog, muat ulang sampai entri tampil
33. Verifikasi jumlah entri `Resend Activation Email` Kartika Sari bertambah tepat satu dibanding baseline langkah 24

### TC-FA-SU-155: Bulk Resend seluruh baris dalam cooldown

34. Pulihkan Hana Kusuma dan Kartika Sari tanpa cooldown lewat seed API, lalu muat ulang halaman User List
35. Bekukan jam server
36. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu klik ⋯ pada baris Hana Kusuma, kemudian `Resend Activation Email`
37. Ganti isi kotak search dengan `Kartika Sari`, tekan Enter, lalu klik ⋯ pada baris Kartika Sari, kemudian `Resend Activation Email`
38. Buka Tab System Log aktor, muat ulang sampai kedua entri `Resend Activation Email` dari langkah 36 dan 37 tampil, lalu catat baseline jumlah entri `Resend Activation Email` di Tab System Log aktor
39. Kembali ke User List, ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu centang baris Hana Kusuma (dalam masa cooldown)
40. Ganti isi kotak search dengan `Kartika Sari`, tekan Enter, lalu centang baris Kartika Sari (dalam masa cooldown)
41. Klik Bulk Action, pilih `Resend Activation Email`
42. Verifikasi toast "Error, failed to send activation email. Please wait a moment before resending."
43. Lepaskan pembekuan jam server
44. Buka Tab System Log aktor, muat ulang sampai entri langkah 36 dan 37 tampil
45. Verifikasi jumlah entri `Resend Activation Email` di Tab System Log aktor sama dengan baseline langkah 38 (tidak ada entri log baru)

### TC-FA-SU-157: Bulk Resend Activation Email Hidden pada seleksi campuran

46. Muat ulang halaman User List, ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu centang baris Hana Kusuma
47. Ganti isi kotak search dengan `Gita Permata`, tekan Enter, lalu centang baris Gita Permata
48. Verifikasi Bulk Actions Bar tampil
49. Verifikasi `Resend Activation Email` tidak ada di Bulk Actions Bar pada seleksi Hana Kusuma dan Gita Permata
50. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu hapus centang Hana Kusuma
51. Ganti isi kotak search dengan `Gita Permata`, tekan Enter, lalu hapus centang Gita Permata
52. Ganti isi kotak search dengan `Indra Wijaya`, tekan Enter, lalu centang baris Indra Wijaya
53. Verifikasi Bulk Actions Bar tampil pada seleksi Indra Wijaya
54. Verifikasi aksi `Resend Confirmation Email` tidak ada di Bulk Actions Bar

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1 dan 11 (pembekuan dan pelepasan jam server dan jam browser), langkah 21, 29, 35, dan 43 (membekukan dan melepas jam server saja pada blok TC-FA-SU-154 dan TC-FA-SU-155, R-10), langkah 12, 14, 16, 18, 30, 32, dan 44 (membuka surface log), langkah 20 dan 34 (memulihkan cooldown lewat seed API dan memuat ulang halaman), langkah 22 dan 36 (prasyarat cooldown yang disebut Langkah Uji TC-FA-SU-154 dan TC-FA-SU-155), langkah 23 dan 38 (membuka surface log, memuat ulang sampai entri langkah 22 dan 36 tampil, lalu mencatat baseline; baseline tidak dicatat sebelum entri eventual tampil, NC-03), langkah 25 dan 39 (kembali ke User List sebelum seleksi), langkah 46 dan 50 (membersihkan dan mengganti seleksi, S-09).
- Langkah penghubung Search (R-16, S-03; bagian 8b butir 9 dan 13): langkah 2, 3, 7, 9, 12, 14, 22, 24, 25, 26, 30, 32, 36, 37, 39, 40, 46, 47, 50, 51, dan 52 mencari baris target dengan nama persis sebelum aksi pada baris itu (dilebur ke langkah aksi yang menyusul), tanpa `Verifikasi`; tabel User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman).
- Asersi tambahan di luar Expected TC: langkah 48 dan 53 (Bulk Actions Bar tampil) adalah anchor positif bagi asersi absence langkah 49 dan 54 (bagian 8b butir 2); toast langkah 28 dan 42 menjadi anchor bagi asersi jumlah entri log langkah 31, 33, dan 45.
- Spec ini 54 langkah. Alasan di atas smell 35 langkah (kelebihan berasal dari Search per baris target, R-16, dan pembekuan jam per blok, R-10): keempat blok satu topik (Bulk Resend Activation Email) dengan dataset yang sama (Hana, Kartika, Indra, Gita) dan satu pembukaan halaman User List; tiap blok berdiri sendiri karena cooldown dipulihkan lewat seed API di antara blok, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - Expected a TC-FA-SU-154 ("di-skip server-side tanpa entri log") dan Expected b TC-FA-SU-155 ("tidak ada entri log baru") tidak menyebut surface log; spec memakai Tab Changelog target (TC-FA-SU-154) dan Tab System Log aktor (TC-FA-SU-155) sebagai surface asersi jumlah dengan baseline (bagian 3 prinsip 13g).
  - Post Condition TC-FA-SU-153 (cooldown dan tiga permukaan log) hanya diasersi lewat Expected c; Post Condition TC-FA-SU-154 dan TC-FA-SU-155 tidak punya langkah observasi dan tidak diasersi (S-01).
  - Expected a TC-FA-SU-157 menyebut aksi Bulk `Resend Activation Email` Hidden pada seleksi campuran; seleksi hanya Indra Wijaya tidak memuat langkah "Hidden" untuk `Resend Activation Email` pada Expected b, sehingga spec hanya mengasersi `Resend Confirmation Email` tidak ada sesuai Expected b.
  - TC tidak menyebut cara menghapus seleksi sebelum seleksi berikutnya; spec memuat ulang halaman atau menghapus centang secara eksplisit.
