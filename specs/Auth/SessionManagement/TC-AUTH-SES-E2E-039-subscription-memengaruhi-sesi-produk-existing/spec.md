---
id: TC-AUTH-SES-E2E-039-subscription-memengaruhi-sesi-produk-existing
title: "Perubahan Status Subscription terhadap Sesi-Produk yang Sudah Berjalan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-119
  - TC-AUTH-SES-120
  - TC-AUTH-SES-121
  - TC-AUTH-SES-122
  - TC-AUTH-SES-123
  - TC-AUTH-SES-280
coverage:
  web: automated
---

# Perubahan Status Subscription terhadap Sesi-Produk yang Sudah Berjalan

## Prerequisites

- Mode: FE+BE.
- Tiga Client dengan subscription Fixed Asset Active di awal spec: Client Q2 (Tabel Data Uji Pre-setup #12; user TC-AUTH-SES-119, 120, 121, dan 280), Client Purge uji (user TC-AUTH-SES-122), dan Client Deleted uji (user TC-AUTH-SES-123) (Tabel Data Uji Pre-setup #14). Purge dan Deleted adalah status terminal yang tidak dapat dipulihkan (rantai status PRD License Allocation Subscription satu arah), sehingga masing-masing memakai Client sendiri yang disediakan tim BE per run, tidak dipulihkan, dan tidak dipakai ulang. Status subscription Fixed Asset dikondisikan per TC lewat langkah eksplisit oleh akun aktor principal Admin Console (Tabel Data Uji Pre-setup #4) `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD` (aksi Admin Console atau lifecycle subscription di-seed BE). Status Expired, Grace, dan Archive pada Client Q2 serta pemulihannya ke Active antar-TC memakai seed yang disediakan tim BE. Jam server uji tidak digeser karena menggeser jam membuat sesi platform semua user uji melewati batas idle 15 menit sebelum perubahan status teramati. Status Archive mengakhiri setiap sesi-produk aktif subscription Client Q2 sekaligus, sehingga sesi-produk user Client Q2 dibuat di langkah pembuka tiap TC dan yang tidak diakhiri oleh aksi TC itu diakhiri di akhir TC (langkah 15 dan 32); hitungan seat aktif tiap TC dihitung dari state TC itu sendiri.
- Kuota concurrent Fixed Asset Client Q2 tetap 2 (Tabel Data Uji Pre-setup #12) dan cukup karena paling banyak satu sesi-produk Client Q2 aktif pada satu waktu. Client Purge uji dan Client Deleted uji masing-masing berkuota Fixed Asset minimal 1 (disediakan tim BE).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) untuk user Client Q2 dan scope Client Expired/uji (Tabel Data Uji Pre-setup #31) untuk user Client Purge uji dan Client Deleted uji, kredensial `Spectra.env.GS_TC_PASSWORD`): delapan user profil BASE (Activated, Active ON, MFA dan Agreement tidak terpicu) dengan App Access Fixed Asset dan Supply Asset; `Andi Anggraini` milik Client Purge uji, `Dewi Wibowo` milik Client Deleted uji, keenam user lain milik Client Q2, password `Spectra.env.SES_PASSWORD`, email bersuffix per run. `Andi Anggraini` dan `Dewi Wibowo` memegang sesi platform web aktif dan sesi-produk Fixed Asset Active di Browser A sejak hook `before` (dibuat lewat login API lalu pembukaan Fixed Asset, seat terpakai 1 per user). Empat user Client Q2 (`Tari Utami`, `Budi Damayanti`, `Siti Rahayu`, `Dimas Puspita`) di hook `before` hanya dibuat sebagai akun; sesi platform web dan sesi-produk Fixed Asset Active mereka di Browser A dibuat dengan cara yang sama pada langkah pembuka TC masing-masing (langkah 1, 17, 34, dan 84), disediakan tim FE/BE. Dua user terakhir adalah user pembanding "user lain milik client yang sama" untuk Browser C dan hanya memegang akun (tanpa sesi):
  - TC-AUTH-SES-119: `Tari Utami` (`tariutami+{runId}-039@qwertysystem.net`); pembanding Browser C `Yusuf Hartono` (`yusufhartono+{runId}-039@qwertysystem.net`)
  - TC-AUTH-SES-120: `Budi Damayanti` (`budidamayanti+{runId}-039@qwertysystem.net`); pembanding Browser C `Mira Hartono` (`mirahartono+{runId}-039@qwertysystem.net`)
  - TC-AUTH-SES-121: `Siti Rahayu` (`sitirahayu+{runId}-039@qwertysystem.net`)
  - TC-AUTH-SES-122: `Andi Anggraini` (`andianggraini+{runId}-039@qwertysystem.net`)
  - TC-AUTH-SES-123: `Dewi Wibowo` (`dewiwibowo+{runId}-039@qwertysystem.net`)
  - TC-AUTH-SES-280: `Dimas Puspita` (`dimaspuspita+{runId}-039@qwertysystem.net`)
- Browser A pada tiap TC = konteks browser yang memuat sesi platform dan sesi-produk Fixed Asset user TC bersangkutan (satu konteks per user; dibuat di `before` untuk `Andi Anggraini` dan `Dewi Wibowo`, dan pada langkah pembuka TC untuk user Client Q2). Browser C = konteks browser baru tanpa sesi.
- Akun aktor lain (login di hook `before`, satu konteks browser per akun):
  - Browser License: Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2, Global Role Manage Global License di Client Q2; untuk Client Purge uji dan Client Deleted uji scope akun mencakup Client tersebut), kredensial `Spectra.env.FA_MGL_PASSWORD`, membuka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset).
  - Browser Admin: akun Total Control (Global Settings) di atas (`Spectra.env.GS_TC_PASSWORD`; scope Client Q2, Tabel Data Uji Pre-setup #26; scope Client Expired/uji, #31, untuk Client Purge uji dan Client Deleted uji), membaca `Activity Log > Session` milik Fixed Asset dan `Global Settings > User > Detail > User Log`.
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): pulihkan status subscription Fixed Asset Client Q2 ke Active (seed yang disediakan tim BE), akhiri semua sesi seed dan sesi-produk baru yang dibuat spec (termasuk milik `Yusuf Hartono` dan `Mira Hartono`), tutup semua konteks browser, hapus kedelapan user (Client Purge uji dan Client Deleted uji tidak dipulihkan; pembersihan user di dua Client itu mengikuti seed yang disediakan tim BE).
- Suite berjalan serial (`parallel: false`); state global yang diubah: status subscription Fixed Asset Client Q2 (Expired, Grace, Archive), dipulihkan di hook `after`; status Purge dan Deleted pada Client Purge uji dan Client Deleted uji tidak dipulihkan (habis pakai per run). Antar-TC pada Client Q2 status dipulihkan ke Active lewat langkah eksplisit (seed yang disediakan tim BE).
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness h: state tenant): pengaturan status subscription per langkah oleh akun principal Admin Console (Expired, Grace, dan Archive pada Client Q2; Purge pada Client Purge uji; Deleted pada Client Deleted uji) dan pemulihan status non-terminal ke Active lewat seed yang disediakan tim BE; pembuatan sesi platform web dan sesi-produk Fixed Asset Active user Client Q2 di awal TC (login API lalu pembukaan Fixed Asset; langkah 1, 17, 34, dan 84) serta pengakhiran sesi-produk dan sesi platform user seed lewat API (langkah 15 dan 32), disediakan tim FE/BE tanpa endpoint; tiga konteks browser tambahan (Browser License, Browser Admin, Browser C); pembacaan hitungan seat aktif dan baris sesi-produk di License > Concurrent User; pembacaan status HTTP response request di Browser A (Request ditolak 403; disediakan tim FE/BE); pembacaan status dan ID sesi-produk Fixed Asset milik user uji dari BE (Active, Ended, ID sama, tidak dibuat; disediakan tim FE/BE); reCAPTCHA mode uji di environment (login Browser C).
- Akun yang dipakai: user uji pada Browser A dan Browser C; Browser License dan Browser Admin memakai akun aktor di atas; akun aktor principal Admin Console untuk mengatur status subscription.

## Test Steps

### TC-AUTH-SES-119: Subscription Expired tidak memutus sesi-produk existing dan reload tetap me-reuse

1. Siapkan sesi platform web dan sesi-produk Fixed Asset Active `Tari Utami` di Browser A (login API lalu buka Fixed Asset; seat terpakai 1)
2. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan catat hitungan seat aktif serta baris `Tari Utami`
3. Ubah status subscription Fixed Asset Client Q2 menjadi Expired
4. Di Browser A (sesi `Tari Utami`) reload halaman Fixed Asset (F5)
5. Verifikasi Reload tetap masuk Fixed Asset
6. Verifikasi Reload memakai sesi-produk yang sama (ID sesi-produk sama)
7. Verifikasi Sesi-produk existing `Tari Utami` tidak di-terminate (tetap Active)
8. Di Browser License muat ulang daftar License > Concurrent User
9. Verifikasi Baris `Tari Utami` masih ada pada daftar
10. Verifikasi Hitungan seat aktif tidak berubah (seat tidak dilepas)
11. Di Browser C buka `Auth > Login with Password`, ketik email `yusufhartono+{runId}-039@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
12. Di Browser C klik card Fixed Asset
13. Verifikasi Browser C membuka halaman Fixed Asset tanpa Popup "Subscription Not Active"
14. Verifikasi Sesi-produk baru dibuat untuk `Yusuf Hartono` (limit concurrent Client Q2 belum tercapai)

### TC-AUTH-SES-120: Subscription Grace tidak memutus sesi-produk existing dan reload tetap me-reuse

15. Akhiri sesi-produk Fixed Asset dan sesi platform `Tari Utami` lewat API (disediakan tim FE/BE)
16. Pulihkan status subscription Fixed Asset Client Q2 dari Expired menjadi Active (seed yang disediakan tim BE)
17. Siapkan sesi platform web dan sesi-produk Fixed Asset Active `Budi Damayanti` di Browser A (login API lalu buka Fixed Asset; seat terpakai 1)
18. Di Browser License muat ulang daftar License > Concurrent User dan catat hitungan seat aktif serta baris `Budi Damayanti`
19. Ubah status subscription Fixed Asset Client Q2 menjadi Grace
20. Di Browser A (sesi `Budi Damayanti`) reload halaman Fixed Asset (F5)
21. Verifikasi Reload tetap masuk Fixed Asset
22. Verifikasi Reload memakai sesi-produk yang sama (ID sesi-produk sama)
23. Verifikasi Sesi-produk existing `Budi Damayanti` tidak di-terminate (tetap Active)
24. Di Browser License muat ulang daftar License > Concurrent User
25. Verifikasi Baris `Budi Damayanti` masih ada pada daftar
26. Verifikasi Hitungan seat aktif tidak berubah (seat tidak dilepas)
27. Tutup konteks Browser C sebelumnya dan buka konteks Browser C baru yang belum login
28. Di Browser C buka `Auth > Login with Password`, ketik email `mirahartono+{runId}-039@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
29. Di Browser C klik card Fixed Asset
30. Verifikasi Browser C membuka halaman Fixed Asset tanpa Popup "Subscription Not Active"
31. Verifikasi Sesi-produk baru dibuat untuk `Mira Hartono` (limit concurrent Client Q2 belum tercapai)

### TC-AUTH-SES-121: Subscription Archive menerminasi sesi-produk existing secara senyap

32. Akhiri sesi-produk Fixed Asset dan sesi platform `Budi Damayanti` lewat API (disediakan tim FE/BE)
33. Pulihkan status subscription Fixed Asset Client Q2 dari Grace menjadi Active (seed yang disediakan tim BE)
34. Siapkan sesi platform web dan sesi-produk Fixed Asset Active `Siti Rahayu` di Browser A (login API lalu buka Fixed Asset; seat terpakai 1)
35. Di Browser License muat ulang daftar License > Concurrent User dan catat hitungan seat aktif serta baris `Siti Rahayu`; catat penanda waktu dasar Activity Log (waktu server) sebelum status diubah
36. Ubah status subscription Fixed Asset Client Q2 menjadi Archive
37. Di Browser A (sesi `Siti Rahayu`) klik menu apa pun di dalam Fixed Asset sehingga request dikirim
38. Verifikasi Request ditolak 403
39. Verifikasi Browser A diarahkan ke Portal — Product Hub
40. Verifikasi Tidak ada dialog yang tampil di Browser A
41. Di Browser License muat ulang daftar License > Concurrent User
42. Verifikasi Sesi-produk Fixed Asset `Siti Rahayu` berstatus Ended
43. Verifikasi Tidak ada dialog ke user `Siti Rahayu`
44. Verifikasi Seat dilepas
45. Verifikasi Hitungan seat aktif berkurang 1
46. Verifikasi Baris `Siti Rahayu` hilang dari daftar
47. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset → halaman log tampil
48. Verifikasi Entri `Session ended` untuk `Siti Rahayu` tercatat di `Activity Log > Session` milik Fixed Asset dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas) [DEFERRED]
49. Di Browser Admin buka `Global Settings > User > Detail > User Log` milik `Siti Rahayu`
50. Verifikasi User Log `Siti Rahayu` menampilkan entri `Session ended (Fixed Asset)` dengan waktu setelah penanda waktu dasar (dicari lewat Note, bukan lewat posisi teratas) [DEFERRED]

### TC-AUTH-SES-122: Subscription Purge menerminasi sesi-produk existing secara senyap

51. Di Browser License muat ulang daftar License > Concurrent User (Client Purge uji) dan catat hitungan seat aktif serta baris `Andi Anggraini`; catat penanda waktu dasar Activity Log (waktu server) sebelum status diubah
52. Ubah status subscription Fixed Asset Client Purge uji menjadi Purge
53. Di Browser A (sesi `Andi Anggraini`) klik menu apa pun di dalam Fixed Asset sehingga request dikirim
54. Verifikasi Request ditolak 403
55. Verifikasi Browser A diarahkan ke Portal — Product Hub
56. Verifikasi Tidak ada dialog yang tampil di Browser A
57. Di Browser License muat ulang daftar License > Concurrent User
58. Verifikasi Sesi-produk Fixed Asset `Andi Anggraini` berstatus Ended
59. Verifikasi Tidak ada dialog ke user `Andi Anggraini`
60. Verifikasi Seat dilepas
61. Verifikasi Hitungan seat aktif berkurang 1
62. Verifikasi Baris `Andi Anggraini` hilang dari daftar
63. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset → halaman log tampil
64. Verifikasi Entri `Session ended` untuk `Andi Anggraini` tercatat di `Activity Log > Session` milik Fixed Asset dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas) [DEFERRED]
65. Di Browser Admin buka `Global Settings > User > Detail > User Log` milik `Andi Anggraini`
66. Verifikasi User Log `Andi Anggraini` menampilkan entri `Session ended (Fixed Asset)` dengan waktu setelah penanda waktu dasar (dicari lewat Note, bukan lewat posisi teratas) [DEFERRED]

### TC-AUTH-SES-123: Subscription Deleted menerminasi sesi-produk existing secara senyap

67. Di Browser License muat ulang daftar License > Concurrent User (Client Deleted uji) dan catat hitungan seat aktif serta baris `Dewi Wibowo`; catat penanda waktu dasar Activity Log (waktu server) sebelum status diubah
68. Ubah status subscription Fixed Asset Client Deleted uji menjadi Deleted
69. Di Browser A (sesi `Dewi Wibowo`) klik menu apa pun di dalam Fixed Asset sehingga request dikirim
70. Verifikasi Request ditolak 403
71. Verifikasi Browser A diarahkan ke Portal — Product Hub
72. Verifikasi Tidak ada dialog yang tampil di Browser A
73. Di Browser License muat ulang daftar License > Concurrent User
74. Verifikasi Sesi-produk Fixed Asset `Dewi Wibowo` berstatus Ended
75. Verifikasi Tidak ada dialog ke user `Dewi Wibowo`
76. Verifikasi Seat dilepas
77. Verifikasi Hitungan seat aktif berkurang 1
78. Verifikasi Baris `Dewi Wibowo` hilang dari daftar
79. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset → halaman log tampil
80. Verifikasi Entri `Session ended` untuk `Dewi Wibowo` tercatat di `Activity Log > Session` milik Fixed Asset dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas) [DEFERRED]
81. Di Browser Admin buka `Global Settings > User > Detail > User Log` milik `Dewi Wibowo`
82. Verifikasi User Log `Dewi Wibowo` menampilkan entri `Session ended (Fixed Asset)` dengan waktu setelah penanda waktu dasar (dicari lewat Note, bukan lewat posisi teratas) [DEFERRED]

### TC-AUTH-SES-280: Rantai Active ke Expired ke Grace ke Archive: sesi existing selamat sampai Archive lalu diterminasi senyap

83. Pulihkan status subscription Fixed Asset Client Q2 dari Archive menjadi Active (seed yang disediakan tim BE)
84. Siapkan sesi platform web dan sesi-produk Fixed Asset Active `Dimas Puspita` di Browser A (login API lalu buka Fixed Asset; seat terpakai 1)
85. Di Browser License muat ulang daftar License > Concurrent User dan catat hitungan seat aktif serta baris `Dimas Puspita`
86. Ubah status subscription Fixed Asset Client Q2 menjadi Expired
87. Di Browser A (sesi `Dimas Puspita`) reload halaman Fixed Asset
88. Verifikasi Pada Expired reload tetap masuk Fixed Asset
89. Verifikasi Pada Expired reload memakai sesi yang sama
90. Di Browser License muat ulang daftar License > Concurrent User
91. Verifikasi Pada Expired Baris `Dimas Puspita` masih ada pada daftar
92. Verifikasi Pada Expired Hitungan seat aktif tidak berubah (seat tidak dilepas)
93. Ubah status subscription Fixed Asset Client Q2 menjadi Grace
94. Di Browser A reload halaman Fixed Asset lagi
95. Verifikasi Pada Grace reload tetap masuk Fixed Asset
96. Verifikasi Pada Grace reload memakai sesi yang sama
97. Di Browser License muat ulang daftar License > Concurrent User
98. Verifikasi Pada Grace Baris `Dimas Puspita` masih ada pada daftar
99. Verifikasi Pada Grace Hitungan seat aktif tidak berubah (seat tidak dilepas)
100. Ubah status subscription Fixed Asset Client Q2 menjadi Archive
101. Di Browser A klik menu apa pun di dalam Fixed Asset
102. Verifikasi Pada Archive request ditolak 403
103. Verifikasi Browser A diarahkan ke Portal — Product Hub
104. Verifikasi Tidak ada dialog yang tampil di Browser A
105. Di Browser License muat ulang daftar License > Concurrent User dan periksa baris `Dimas Puspita`
106. Verifikasi Sesi-produk `Dimas Puspita` berstatus Ended
107. Verifikasi Baris `Dimas Puspita` hilang dari daftar
108. Verifikasi Seat dilepas
109. Verifikasi Hitungan seat aktif berkurang 1

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness h (state tenant). Spec ini melewati batas sekitar 35 langkah; enam TC berbagi Browser License dan Browser Admin (TC-AUTH-SES-119, 120, 121, dan 280 memakai Client Q2; TC-AUTH-SES-122 dan 123 masing-masing Client sendiri), dan bagian sesudah tiap TC tidak bergantung pada TC sebelumnya (state dipulihkan ke Active dan sesi-produk user Client Q2 dibuat di awal tiap TC, lalu diakhiri di akhir TC bila tidak diakhiri oleh aksi TC itu).
- Urutan mengikuti TC sumber (119, 120, 121, 122, 123, 280); tidak ada penyimpangan (S-05, S-10). Aksi yang menerminasi sesi-produk berada di TC 121, 122, 123, dan 280 (akhir spec).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): "Ubah status subscription ..." (langkah 3, 19, 36, 52, 68, 86, 93, 100) mengondisikan state tenant per TC; "Pulihkan status subscription ..." (langkah 16, 33, 83, pada Client Q2) menjaga precondition Active tiap TC (S-09); menyiapkan sesi platform dan sesi-produk user Client Q2 di awal TC (langkah 1, 17, 34, 84) dan mengakhirinya di akhir TC-AUTH-SES-119 dan 120 (langkah 15 dan 32) lewat API yang disediakan tim FE/BE; mencatat penanda waktu dasar log (langkah 35, 51, 67); membuka halaman log (langkah 47, 49, 63, 65, 79, 81); langkah 27 menutup konteks Browser C sebelumnya dan membuka konteks baru saat user Browser C berganti dari `Yusuf Hartono` ke `Mira Hartono`; langkah "catat hitungan seat aktif" dan "muat ulang daftar" di Browser License membentuk keadaan yang dibandingkan asersi seat (S-14).
- Dependensi data: "user lain milik client yang sama" pada TC-AUTH-SES-119 dan 120 diwujudkan dua user pembanding bernama `Yusuf Hartono` dan `Mira Hartono` (nama ditetapkan spec karena TC tidak menyebut nama); keduanya hanya login di Browser C dan tidak membentuk sesi-produk.
- Expected c TC-AUTH-SES-121, 122, 123 dibaca di `Activity Log > Session` milik Fixed Asset dan `Global Settings > User > Detail > User Log` (akun Total Control Global Settings, Browser Admin); surface produk itu adalah forward-dependency bertanda `[DEFERRED]` (NC-15). Asersi absence tidak ada di spec ini (S-05). Purge dan Deleted memakai Client sendiri (Client Purge uji dan Client Deleted uji) karena kedua status terminal dan tidak dapat dipulihkan; status non-terminal pada Client Q2 dipulihkan lewat seed yang disediakan tim BE.
- Expired dan Grace bukan penolak gerbang produk (`AUTHSES-LOGIC-03d`): pada TC-AUTH-SES-119 dan TC-AUTH-SES-120 pembanding di Browser C membuat sesi-produk baru dan mengambil seat; Client Q2 harus punya sisa seat saat TC ini berjalan (seat Client Q2 tidak sedang dipenuhi spec lain, suite serial).
- Temuan untuk QA: (1) TC-AUTH-SES-121 s.d. 123 dan 280 menawarkan "majukan waktu server atau aksi Admin Console" untuk mengubah status subscription; menggeser jam server membuat semua sesi platform (idle 15 menit) kedaluwarsa sehingga Archive dan seterusnya tidak dapat dibedakan dari idle timeout, jadi spec memakai aksi Admin Console dan jam server uji tidak dipakai. (2) TC-AUTH-SES-119 dan 120 tidak menyebut identitas user di Browser C; spec menambahkan dua user pembanding. (3) TC-AUTH-SES-119, 120, 280 menyebut "seat tidak dilepas" tanpa cara membacanya; spec memakai License > Concurrent User (cara membaca daftar mengikuti `fixed-asset/license/PRD/license.md` §3.2). (4) TC-AUTH-SES-119 s.d. 123 menyebut Client generik (Tabel Data Uji Pre-setup #14) sedangkan TC-AUTH-SES-280 dan pembacaan License > Concurrent User memakai Client Q2 (#12) dan akun `manageGlobalLicenseFixedAsset`; spec memakai Client Q2 untuk TC-AUTH-SES-119, 120, 121, dan 280, serta Client Purge uji dan Client Deleted uji untuk TC-AUTH-SES-122 dan 123 (status terminal tidak dapat dipulihkan), dengan asumsi scope akun aktor License dan Total Control mencakup dua Client itu. (5) TC-AUTH-SES-121 s.d. 123 Expected a memuat tiga klausa (Ended, seat dilepas, tanpa dialog); "tanpa dialog" diasersikan di langkah 40, 56, 72 (Browser A) dan 43, 59, 75 (ke user), terpisah dari pengalihan ke Portal di langkah 39, 55, 71. (6) TC-AUTH-SES-119 s.d. 123 dan 280 tidak menyebut cara membaca status HTTP 403 serta status dan ID sesi-produk; spec memakai kemampuan yang disediakan tim FE/BE tanpa endpoint (Prerequisites). (7) TC-AUTH-SES-121 dan 280 tidak menyebut bahwa Archive mengakhiri setiap sesi-produk aktif Client Q2 (LLD), padahal itu menentukan hitungan seat "berkurang 1"; spec membuat sesi-produk user Client Q2 di awal tiap TC dan mengakhiri sesi TC-AUTH-SES-119 dan 120 di akhir TC itu (langkah 15 dan 32), sehingga paling banyak satu seat Client Q2 terpakai pada satu waktu dan kuota 2 (TC-AUTH-SES-280) cukup. (8) Pemulihan status subscription ke Active antar-TC tidak didefinisikan TC maupun PRD License Allocation Subscription (rantai status satu arah, Archive hanya Detail); spec menuliskannya sebagai seed yang disediakan tim BE untuk status non-terminal, dan memakai Client terpisah untuk Purge dan Deleted. (9) TC-AUTH-SES-121 s.d. 123 tidak menyebut aktor pembaca `Activity Log > Session` milik Fixed Asset; spec memakai akun Total Control Global Settings di Browser Admin (seperti TC-AUTH-SES-127 dan 128).
