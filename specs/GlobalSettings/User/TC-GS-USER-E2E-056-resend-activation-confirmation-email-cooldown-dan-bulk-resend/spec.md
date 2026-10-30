---
id: TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend
title: "Resend Activation/Confirmation Email: Cooldown 60 Detik dengan Jam Server dan Browser, Tombol Resend di Detail, Edit Email Pending Activation, dan Bulk Resend dengan Baris Cooldown Di-skip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-305
  - TC-GS-USER-306
  - TC-GS-USER-307
  - TC-GS-USER-309
  - TC-GS-USER-311
  - TC-GS-USER-312
  - TC-GS-USER-238
  - TC-GS-USER-239
  - TC-GS-USER-302
  - TC-GS-USER-303
coverage:
  web: automated
---

# Resend Activation/Confirmation Email: Cooldown 60 Detik dengan Jam Server dan Browser, Tombol Resend di Detail, Edit Email Pending Activation, dan Bulk Resend dengan Baris Cooldown Di-skip

## Prerequisites

- Mode: FE+BE (kelas harness d: mail-catcher dan manipulasi jam server dan jam browser).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Dewi Lestari (No. 12, Activated tanpa email pending) untuk TC-GS-USER-312; Division `Finance` (No. 23) untuk form Create TC-GS-USER-307.
- Data Dinamis, di-seed lewat API di hook `before` (HK1) dan dibersihkan di hook `after`; semua Activation Email/Confirmation Email seed memulai cooldown 60 detik pada waktu terbit:
  - `Mike Tan {runId}-056`, Email `miketan+{runId}-056@qwertysystem.net`, Pending Activation, Access `Fixed Asset`, Division `Finance`.
  - `Andre Kurniawan {runId}-056`, Email `andrekurniawan+{runId}-056@qwertysystem.net`, Pending Activation, Access `Fixed Asset`, Division `Finance`.
  - `Rina Putri {runId}-056`, Email `rinaputri+{runId}-056@qwertysystem.net`, Activated dengan email pending `rinaputri.new+{runId}-056@qwertysystem.net`, Access `Fixed Asset`, Division `Finance`.
  - `Lukman Hakim {runId}-056` (First Name `Lukman`, Last Name `Hakim {runId}-056`, Email `lukmanhakim+{runId}-056@qwertysystem.net`, Division `Finance`, Access `Fixed Asset`) dibuat lewat UI di TC-GS-USER-307 dan dihapus di hook `after`.
  - Alamat penerima email tanpa user: `miketan.new+{runId}-056@qwertysystem.net` (TC-GS-USER-238) dan `miketan.second+{runId}-056@qwertysystem.net` (TC-GS-USER-239).
- Kemampuan teknis, semuanya disediakan tim FE/BE (tidak ada mekanisme di TC, PRD, atau LLD; endpoint tidak disebut):
  - Mail-catcher: membaca daftar email per alamat (jumlah, waktu terbit, tautan di badan email) dan membuka tautan aktivasi; baseline jumlah email dicatat per alamat sebelum aksi yang diasersi.
  - Manipulasi jam: jam server dan jam browser diatur bersama, dengan nilai absolut atau dibekukan, dan dipulihkan ke waktu nyata (countdown tooltip berjalan di jam browser, cooldown dihitung di server).
  - Seeding user Pending Activation dan user Activated dengan email pending lewat API.
  - Membaca waktu terbit artefak dari timestamp email di mail-catcher.
- Rumus jam (batas eksak 60 detik; margin terhadap batas 0 detik, karena jam diset absolut, bukan digeser relatif):
  - `T_L` = waktu terbit Activation Email awal `Lukman Hakim {runId}-056`, dibaca dari mail-catcher.
  - `T_1` = waktu terbit email hasil Resend `Mike Tan {runId}-056` di TC-GS-USER-305, dibaca dari mail-catcher.
  - `F0` = nilai jam server saat jam dibekukan sebelum `[Save]` di TC-GS-USER-238.
  - Tiap "atur jam ke X" berarti jam server dan jam browser diatur bersama ke X absolut; "bekukan" berarti jam berhenti di nilai itu sampai diatur lagi.
- State global yang diubah: jam server dan jam browser. Suite berjalan serial (`parallel: false`, lihat `suite.md`). Jam dipulihkan ke waktu nyata lewat langkah eksplisit sebelum Modal Changelog User dibuka (S-09) dan di hook `after` yang tetap berjalan walau spec gagal di tengah.
- Cleanup di hook `after`: pulihkan jam, hapus `Mike Tan {runId}-056`, `Andre Kurniawan {runId}-056`, `Rina Putri {runId}-056`, dan `Lukman Hakim {runId}-056` lewat API tanpa mengandalkan setup berhasil penuh.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-312: Button Resend tidak tampil untuk user Activated tanpa email pending

3. Klik Name `Dewi Lestari` di User List
4. Verifikasi User Detail `Dewi Lestari` tampil
5. Verifikasi Detail tidak memuat Button `Resend Activation Email` maupun Button `Resend Confirmation Email`
6. Kembali ke User List dengan klik Back

### TC-GS-USER-307: Cooldown resend dimulai sejak Activation Email awal saat Create

7. Klik `[+ User]` di Table Tools
8. Isi First Name `Lukman`, Last Name `Hakim {runId}-056`, Division `Finance`, Email `lukmanhakim+{runId}-056@qwertysystem.net`, centang Access `Fixed Asset`
9. Klik `[Submit]`
10. Tunggu aksi selesai (popup tertutup dan baris `Lukman Hakim {runId}-056` tampil di User List)
11. Klik (⋯) baris `Lukman Hakim {runId}-056`
12. Hover opsi `Resend Activation Email`
13. Verifikasi opsi `Resend Activation Email` tampil dan disabled
14. Verifikasi tooltip `"Please wait {X} seconds before resending."` tampil dengan X berupa angka 1 sampai 60
15. Tekan Esc untuk menutup menu row action
16. Baca `T_L` dari mail-catcher untuk alamat `lukmanhakim+{runId}-056@qwertysystem.net`, lalu atur jam ke `T_L` + 60 detik sehingga cooldown semua user seed dan Lukman Hakim berakhir

### TC-GS-USER-305: Resend Activation Email dari row action memulai cooldown

17. Klik (⋯) baris `Mike Tan {runId}-056` → `Resend Activation Email`
18. Verifikasi toast sukses: "Success, activation email has been sent."
19. Klik (⋯) baris `Mike Tan {runId}-056` lagi
20. Hover opsi `Resend Activation Email`
21. Verifikasi opsi tetap berlabel `Resend Activation Email`
22. Verifikasi opsi tampil dan disabled
23. Verifikasi tooltip `"Please wait {X} seconds before resending."` tampil; catat X sebagai X1
24. Baca `T_1` dari mail-catcher untuk alamat `miketan+{runId}-056@qwertysystem.net`
25. Atur jam ke `T_1` + 30 detik
26. Hover ulang opsi `Resend Activation Email`
27. Verifikasi tooltip `"Please wait {X} seconds before resending."` menampilkan X lebih kecil dari X1 (menghitung mundur)

### TC-GS-USER-306: Cooldown resend berakhir setelah 60 detik

28. Atur jam ke `T_1` + 60 detik
29. Tekan Esc untuk menutup menu row action
30. Klik (⋯) baris `Mike Tan {runId}-056`
31. Hover opsi `Resend Activation Email`
32. Verifikasi opsi `Resend Activation Email` enabled
33. Verifikasi tooltip countdown tidak tampil

### TC-GS-USER-309: Resend Confirmation Email dari row action

34. Tekan Esc untuk menutup menu row action
35. Klik (⋯) baris `Rina Putri {runId}-056` → `Resend Confirmation Email`
36. Verifikasi toast sukses: "Success, confirmation email has been sent to Rina Putri {runId}-056."
37. Klik (⋯) baris `Rina Putri {runId}-056` lagi
38. Hover opsi `Resend Confirmation Email`
39. Verifikasi opsi `Resend Confirmation Email` disabled
40. Verifikasi tooltip `"Please wait {X} seconds before resending."` tampil

### TC-GS-USER-238: Edit email user Pending Activation langsung tersimpan dan Activation Email dikirim ulang

41. Tekan Esc untuk menutup menu row action
42. Catat tautan aktivasi pada email terbaru di mail-catcher untuk alamat `miketan+{runId}-056@qwertysystem.net` sebagai tautan aktivasi lama
43. Bekukan jam di nilai saat ini dan catat nilainya sebagai `F0`
44. Klik (⋯) baris `Mike Tan {runId}-056` → `Edit`
45. Ubah Email ke `miketan.new+{runId}-056@qwertysystem.net`
46. Klik `[Save]`
47. Verifikasi toast sukses: "Success, user has been updated."
48. Verifikasi kolom Email baris `Mike Tan {runId}-056` menampilkan `miketan.new+{runId}-056@qwertysystem.net`
49. Verifikasi kolom Email baris `Mike Tan {runId}-056` tanpa badge `Pending Email Confirmation`
50. Buka tautan aktivasi lama di tab baru
51. Verifikasi halaman menolak tautan aktivasi lama sebagai kedaluwarsa
52. Tutup tab tautan aktivasi lama
53. Klik (⋯) baris `Mike Tan {runId}-056`
54. Hover opsi `Resend Activation Email`
55. Verifikasi opsi `Resend Activation Email` disabled (masuk cooldown)
56. Verifikasi tooltip `"Please wait {X} seconds before resending."` tampil

### TC-GS-USER-311: Button Resend di User Detail tampil kondisional dengan cooldown

57. Tekan Esc untuk menutup menu row action
58. Klik Name `Andre Kurniawan {runId}-056` di User List
59. Verifikasi Button `Resend Activation Email` tampil di Detail
60. Klik `Resend Activation Email`
61. Verifikasi toast sukses: "Success, activation email has been sent."
62. Hover tombol `Resend Activation Email`
63. Verifikasi tombol `Resend Activation Email` disabled
64. Verifikasi tooltip `"Please wait {X} seconds before resending."` tampil
65. Kembali ke User List dengan klik Back

### TC-GS-USER-239: Edit email user Pending Activation saat cooldown masih berjalan tetap mengirim email

66. Atur jam ke `F0` + 30 detik dan bekukan, sehingga cooldown `Mike Tan {runId}-056` dari TC-GS-USER-238 masih berjalan
67. Catat baseline jumlah email di mail-catcher untuk alamat `miketan.second+{runId}-056@qwertysystem.net`
68. Klik (⋯) baris `Mike Tan {runId}-056` → `Edit`
69. Ubah Email ke `miketan.second+{runId}-056@qwertysystem.net`
70. Klik `[Save]`
71. Verifikasi toast sukses: "Success, user has been updated."
72. Verifikasi jumlah email di mail-catcher untuk alamat `miketan.second+{runId}-056@qwertysystem.net` bertambah 1 dari baseline dan email itu adalah Activation Email
73. Klik (⋯) baris `Mike Tan {runId}-056`
74. Hover opsi `Resend Activation Email`
75. Verifikasi tooltip `"Please wait 60 seconds before resending."` (countdown mulai lagi dari 60 detik)

### TC-GS-USER-303: Bulk Resend Activation Email, sebagian dalam cooldown di-skip

76. Tekan Esc untuk menutup menu row action
77. Pulihkan jam server dan jam browser ke waktu nyata
78. Buka Modal Changelog User
79. Catat baseline: jumlah baris `Resend Activation Email` untuk `Andre Kurniawan {runId}-056` dan jumlah baris `Resend Activation Email` untuk `Mike Tan {runId}-056`
80. Tutup Modal Changelog User dengan klik `✕`
81. Atur jam ke `F0` + 60 detik, sehingga cooldown `Andre Kurniawan {runId}-056` berakhir dan cooldown `Mike Tan {runId}-056` (sampai `F0` + 90 detik) masih berjalan
82. Centang baris `Mike Tan {runId}-056` dan `Andre Kurniawan {runId}-056`
83. Bulk Action → `Resend Activation Email`
84. Verifikasi toast: "Success, activation email has been sent. Some items were skipped (cooldown not finished)."
85. Pulihkan jam server dan jam browser ke waktu nyata
86. Buka Modal Changelog User
87. Verifikasi jumlah baris `Resend Activation Email` untuk `Andre Kurniawan {runId}-056` bertambah 1 dari baseline
88. Verifikasi jumlah baris `Resend Activation Email` untuk `Mike Tan {runId}-056` sama dengan baseline
89. Tutup Modal Changelog User dengan klik `✕`
90. Klik `Unselect All` pada Bulk Action Bar

### TC-GS-USER-302: Bulk Resend Activation Email, semua terkirim

91. Atur jam ke `F0` + 120 detik, sehingga cooldown kedua user berakhir
92. Centang baris `Mike Tan {runId}-056` dan `Andre Kurniawan {runId}-056`
93. Bulk Action → `Resend Activation Email`
94. Verifikasi toast sukses: "Success, activation email has been sent."
95. Verifikasi Bulk Action Bar hilang

## Notes

- Mode: FE+BE (kelas harness d). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (95 langkah). Alasan: seluruh blok satu kelas harness (d: mail-catcher dan jam) dan satu layar (User List dan Detail), serta state cooldown Mike Tan dan Andre Kurniawan dibangun berurutan dari blok ke blok dan tidak bisa diulang tanpa biaya besar (P-3): cooldown Mike Tan dari TC-GS-USER-238 menjadi precondition TC-GS-USER-239 dan TC-GS-USER-303, dan cooldown Andre Kurniawan dari TC-GS-USER-311 menjadi precondition TC-GS-USER-303 dan TC-GS-USER-302. Tiap blok tetap diawali keadaan data yang ditulis di langkah pembuka blok.
- Urutan TC sumber diubah: TC-GS-USER-312 (screening tanpa aksi) di awal; TC-GS-USER-307 (butuh Create dan cooldown berjalan) sebelum jam diubah; TC-GS-USER-309 dan TC-GS-USER-238 sebelum TC-GS-USER-311 dan TC-GS-USER-239 supaya cooldown Mike Tan dan Andre Kurniawan berbeda waktu mulai; TC-GS-USER-303 sebelum TC-GS-USER-302, karena TC-GS-USER-303 membutuhkan Mike Tan dalam cooldown dan Andre Kurniawan sudah lewat, sedangkan TC-GS-USER-302 membutuhkan keduanya lewat.
- Rumus waktu TC-GS-USER-303: Mike Tan disimpan ulang pada `F0` + 30 detik (TC-GS-USER-239), jadi cooldown-nya berakhir `F0` + 90 detik; Andre Kurniawan di-resend pada `F0` (TC-GS-USER-311), jadi cooldown-nya berakhir `F0` + 60 detik. Jam diatur absolut ke `F0` + 60 detik. State "Mike Tan baru di-resend" pada TC-GS-USER-303 dibentuk oleh Edit email (TC-GS-USER-239) yang juga mengirim Activation Email dan memulai cooldown.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): pembukaan layar, Esc menutup menu row action, Back ke User List, "Tunggu aksi selesai", membaca `T_L`, `T_1`, dan tautan aktivasi lama dari mail-catcher, mengatur, membekukan, dan memulihkan jam, mencatat baseline, menutup tab dan Modal Changelog User, dan `Unselect All`. Verifikasi User Detail `Dewi Lestari` tampil adalah anchor positif untuk asersi ketiadaan Button Resend (bagian 8b butir 2).
- Jam dipulihkan ke waktu nyata sebelum Modal Changelog User dibuka (S-09). Log yang dibuat saat jam digeser bercap waktu masa depan, sehingga asersi Changelog memakai selisih jumlah baris terhadap baseline per user (nama user bersuffix), bukan posisi teratas (S-12). Asersi "Mike Tan sama dengan baseline" adalah asersi jumlah, bukan asersi absence kelas g.
- Email aktivasi lama TC-GS-USER-238 diidentifikasi sebagai email terbaru di alamat lama sebelum Edit (hasil Resend di TC-GS-USER-305).
- Tooltip "Please wait {X} seconds before resending." ditulis persis seperti Expected TC, termasuk tanda kutip ganda. Pada nama bersuffix, toast TC-GS-USER-309 memuat nama lengkap `Rina Putri {runId}-056`.
- Temuan untuk QA:
  - TC-GS-USER-238: kolom Automation bernilai Manual Only, sedangkan Expected dapat diasersi lewat mail-catcher; spec memasukkannya (bagian 2 konvensi).
  - TC-GS-USER-238: Expected c ("ditolak sebagai kedaluwarsa") tidak menyebut teks atau tampilan halaman penolakan; spec hanya mengasersi bahwa halaman menolak tautan sebagai kedaluwarsa.
  - TC-GS-USER-238: Post Condition (Activation Email baru terkirim ke `miketan.new@qwertysystem.net`) tanpa langkah observasi di TC; tidak diasersi di blok ini (pengiriman ke alamat baru diasersi di TC-GS-USER-239). TC-GS-USER-305: Post Condition (Activation Email terkirim ulang) tanpa langkah observasi; tidak diasersi. TC-GS-USER-309: Post Condition (masa berlaku tautan konfirmasi 24 jam dari sekarang) tanpa langkah observasi; tidak diasersi.
  - TC-GS-USER-305, 309, 239: tooltip tertulis dengan tanda kutip ganda (`"Please wait {X} seconds before resending."`); tidak jelas apakah tanda kutip bagian dari teks tooltip atau pembatas.
  - TC-GS-USER-305 dan 309: precondition "cooldown lewat" tidak menyebut cara membuatnya; spec mengatur jam server dan jam browser. Seeding user Pending Activation dan Activated dengan email pending, pembacaan waktu terbit email, serta manipulasi jam tidak punya sumber di TC, PRD, dan LLD; disediakan tim FE/BE.
  - TC-GS-USER-306: langkah "Tunggu 60 detik" dipenuhi dengan mengatur jam ke `T_1` + 60 detik (bagian 6 konvensi), bukan menunggu waktu nyata.
  - TC-GS-USER-239: Expected c ("mulai lagi dari 60 detik") hanya terukur bila jam dibekukan; spec membekukan jam sebelum `[Save]`.
  - TC-GS-USER-239 dan 303: precondition "baru saja menerima Resend" / "baru di-resend" untuk Mike Tan dipenuhi lewat Edit email, bukan lewat aksi Resend.
  - TC-GS-USER-303: Expected b ("Changelog hanya memuat baris Resend Activation Email untuk Andre Kurniawan") tidak menyebut baseline; spec mengasersi selisih jumlah baris per user terhadap baseline.
  - TC-GS-USER-307: langkah "Create user `Lukman Hakim` (valid)" tidak menyebut field; spec memakai field wajib dari TC-GS-USER-117 (First Name, Last Name, Division, Email, Access).
  - TC-GS-USER-311: Expected a ("tampil di Detail") tidak menyebut posisi atau kondisi tampil selain Pending Activation.
