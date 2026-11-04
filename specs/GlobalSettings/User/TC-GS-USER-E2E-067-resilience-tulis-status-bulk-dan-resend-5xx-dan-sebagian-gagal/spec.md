---
id: TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal
title: "Resilience Tulis User: Toggle Active, Bulk Activate dan Deactivate, Resend Activation dan Confirmation Email, serta Bulk Resend Gagal 5xx Total atau Sebagian dengan Cooldown Tidak Dimulai"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-245
  - TC-GS-USER-249
  - TC-GS-USER-1048
  - TC-GS-USER-1049
  - TC-GS-USER-294
  - TC-GS-USER-308
  - TC-GS-USER-310
  - TC-GS-USER-1037
  - TC-GS-USER-1038
  - TC-GS-USER-1050
coverage:
  web: automated
---

# Resilience Tulis User: Toggle Active, Bulk Activate dan Deactivate, Resend Activation dan Confirmation Email, serta Bulk Resend Gagal 5xx Total atau Sebagian dengan Cooldown Tidak Dimulai

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas harness b: fault injection, bagian 3 prinsip 13 dan bagian 6 konvensi).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Division `Finance` (No. 23) dan produk `Fixed Asset` (No. 26) untuk user seed. Dewi Lestari, Jane Smith, Budi Santoso, Joko Susilo, Mike Tan, Rina Putri, dan user lain di Tabel Pre-setup No. 10-22 diganti user seed milik spec karena menjadi target aksi tulis (S-06).
- Data Dinamis, di-seed lewat API di hook `before` (HK1), Division `Finance`, Access `Fixed Asset`, dan dibersihkan di hook `after`:
  - Active: `Dewi Lestari {runId}-067` (Email `dewilestari+{runId}-067@qwertysystem.net`; TC-GS-USER-245 dan 1049) dan `Joko Susilo {runId}-067` (Email `jokosusilo+{runId}-067@qwertysystem.net`; TC-GS-USER-1049).
  - Inactive manual: `Jane Smith {runId}-067` (Email `janesmith+{runId}-067@qwertysystem.net`; TC-GS-USER-249, 1048, 294), `Budi Santoso {runId}-067` (Email `budisantoso+{runId}-067@qwertysystem.net`; TC-GS-USER-1048, 294), dan `Citra Dewanti {runId}-067` (Email `citradewanti+{runId}-067@qwertysystem.net`; TC-GS-USER-294).
  - Pending Activation: `Mike Tan {runId}-067` (Email `miketan+{runId}-067@qwertysystem.net`; TC-GS-USER-308, 1037, 1038, 1050), `Andre Kurniawan {runId}-067` (Email `andrekurniawan+{runId}-067@qwertysystem.net`; TC-GS-USER-1037, 1038, 1050), `Maya Anggraini {runId}-067` (Email `mayaanggraini+{runId}-067@qwertysystem.net`; TC-GS-USER-1038), dan `Rahmat Hidayat {runId}-067` (Email `rahmathidayat+{runId}-067@qwertysystem.net`; TC-GS-USER-1050). Activation Email awal tiap user memulai cooldown 60 detik pada waktu terbit.
  - Activated dengan email pending: `Rina Putri {runId}-067` (Email `rinaputri+{runId}-067@qwertysystem.net`, email pending `rinaputri.new+{runId}-067@qwertysystem.net`; TC-GS-USER-310). Confirmation Email awal memulai cooldown 60 detik pada waktu terbit.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint ditentukan tim FE di tahap script (tidak disebut di TC dan PRD). Semua jawaban 5xx (500) diberikan tanpa meneruskan request ke backend:
  - Respons perubahan status user: jawab 5xx untuk semua request (TC-GS-USER-245, 249, 1048, 1049); jawab 5xx hanya untuk request baris `Citra Dewanti {runId}-067`, request baris lain diteruskan (TC-GS-USER-294).
  - Respons Resend Activation Email: jawab 5xx (TC-GS-USER-308); jawab 5xx untuk semua request (TC-GS-USER-1037); jawab 5xx hanya untuk request baris `Andre Kurniawan {runId}-067` (TC-GS-USER-1038) atau `Rahmat Hidayat {runId}-067` (TC-GS-USER-1050), request baris lain diteruskan.
  - Respons Resend Confirmation Email: jawab 5xx (TC-GS-USER-310).
  - Tiap intercept dilepas segera setelah toast hasilnya tampil.
- Kemampuan teknis, disediakan tim FE/BE (tidak ada mekanisme di TC, PRD, atau LLD; endpoint tidak disebut):
  - Seeding user Pending Activation dan user Activated dengan email pending lewat API.
  - Mail-catcher: membaca waktu terbit email aktivasi dan konfirmasi seed per alamat (HK4).
  - Manipulasi jam: jam server dan jam browser diatur bersama dengan nilai absolut atau dibekukan, dan dipulihkan ke waktu nyata (HK5). Cooldown dihitung di server dan countdown tooltip berjalan di jam browser.
- Rumus jam (cooldown 60 detik; margin terhadap batas 60 detik):
  - `T_s` = waktu terbit terbesar di antara Activation Email seed (Mike Tan, Andre Kurniawan, Maya Anggraini, Rahmat Hidayat) dan Confirmation Email seed (Rina Putri), dibaca dari mail-catcher.
  - `F1` = `T_s` + 120 detik; jam server dan jam browser diatur bersama ke `F1` absolut lalu dibekukan, sehingga cooldown semua email seed sudah lewat dengan margin 60 detik. Cooldown yang dimulai oleh Resend yang berhasil pada jam yang dibekukan di `F1` berlaku sampai `F1` + 60 detik dan tidak berakhir selama jam tetap dibekukan di `F1`.
  - Jam dibekukan kembali di `F1` sebelum TC-GS-USER-1038 dan TC-GS-USER-1050 sehingga cooldown Mike Tan dari TC-GS-USER-1038 masih berjalan pada TC-GS-USER-1050.
- State global yang diubah: jam server dan jam browser. Suite berjalan serial (`parallel: false`, lihat `suite.md`). Jam dipulihkan ke waktu nyata lewat langkah eksplisit sebelum Modal Changelog User dibuka (S-09) dan di hook `after`, yang tetap berjalan walau spec gagal di tengah.
- Cleanup di hook `after` (tanpa mengandalkan setup berhasil penuh): lepas semua intercept; pulihkan jam server dan jam browser; hapus lewat API semua user seed di atas; kembalikan sesi ke akun default suite. Entri Changelog tidak dihapus (immutable).

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Pilih 100 baris per halaman pada Pagination
3. Klik icon Search, ketik `{runId}-067`, tekan Enter

### TC-GS-USER-245: Deactivate gagal 5xx, switch dikembalikan

4. Pasang intercept pada respons perubahan status user: jawab 5xx
5. Klik switch Active baris `Dewi Lestari {runId}-067`
6. Klik `[Deactivate]` pada dialog konfirmasi
7. Verifikasi toast error: "Error, failed to deactivate user."
8. Lepas intercept respons perubahan status user
9. Verifikasi switch Active baris `Dewi Lestari {runId}-067` kembali ON
10. Klik `[Cancel]` pada dialog Deactivate

### TC-GS-USER-249: Activate gagal 5xx, switch dikembalikan OFF

11. Pasang intercept pada respons perubahan status user: jawab 5xx
12. Klik switch Active baris `Jane Smith {runId}-067`
13. Klik `[Activate]` pada dialog konfirmasi
14. Verifikasi toast error: "Error, failed to activate user."
15. Lepas intercept respons perubahan status user
16. Verifikasi switch Active baris `Jane Smith {runId}-067` tetap OFF
17. Klik `[Cancel]` pada dialog Activate

### TC-GS-USER-1048: Bulk Activate dengan seluruh baris gagal server memakai toast gagal Activate

18. Pasang intercept pada respons perubahan status user: jawab 5xx untuk semua request
19. Centang baris `Jane Smith {runId}-067` dan `Budi Santoso {runId}-067`
20. Bulk Action → `Activate`
21. Tunggu toast lama hilang otomatis
22. Klik `[Activate]` pada dialog konfirmasi
23. Verifikasi toast error: "Error, failed to activate user."
24. Verifikasi toast ringkasan "Success, user has been activated. Some items failed." tidak tampil
25. Lepas intercept respons perubahan status user
26. Verifikasi switch Active baris `Jane Smith {runId}-067` dan `Budi Santoso {runId}-067` tetap OFF
27. Klik `[Cancel]` pada dialog Activate
28. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-1049: Bulk Deactivate dengan seluruh baris gagal server memakai toast gagal Deactivate

29. Pasang intercept pada respons perubahan status user: jawab 5xx untuk semua request
30. Centang baris `Dewi Lestari {runId}-067` dan `Joko Susilo {runId}-067`
31. Bulk Action → `Deactivate`
32. Tunggu toast lama hilang otomatis
33. Klik `[Deactivate]` pada dialog konfirmasi
34. Verifikasi toast error: "Error, failed to deactivate user."
35. Verifikasi toast ringkasan "Success, user has been deactivated. Some items failed." tidak tampil
36. Lepas intercept respons perubahan status user
37. Verifikasi switch Active baris `Dewi Lestari {runId}-067` dan `Joko Susilo {runId}-067` tetap ON
38. Klik `[Cancel]` pada dialog Deactivate
39. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-294: Bulk Activate dengan sebagian gagal server, toast ringkasan melaporkan baris gagal

40. Pasang intercept pada respons perubahan status user untuk baris `Citra Dewanti {runId}-067`: jawab 5xx, request baris lain diteruskan
41. Centang baris `Jane Smith {runId}-067`, `Budi Santoso {runId}-067`, dan `Citra Dewanti {runId}-067`
42. Bulk Action → `Activate`
43. Klik `[Activate]` pada dialog konfirmasi
44. Verifikasi toast: "Success, user has been activated. Some items failed."
45. Lepas intercept respons perubahan status user

### Persiapan Resend: baseline Changelog dan jam

46. Klik icon Changelog di Table Tools
47. Verifikasi Modal Changelog User memuat entri (pembanding sebelum Search)
48. Klik icon Search pada Modal Changelog, ketik `{runId}-067`, tekan Enter
49. Catat jumlah baris `Resend Activation Email` untuk `Mike Tan {runId}-067`, `Andre Kurniawan {runId}-067`, `Maya Anggraini {runId}-067`, dan `Rahmat Hidayat {runId}-067` sebagai baseline B_Mike, B_Andre, B_Maya, dan B_Rahmat
50. Tutup Modal Changelog User dengan klik `✕`
51. Baca `T_s` dari mail-catcher untuk alamat seed (waktu terbit terbesar)
52. Atur jam server dan jam browser ke `F1` = `T_s` + 120 detik dan bekukan

### TC-GS-USER-308: Resend Activation Email gagal tidak memulai cooldown

53. Pasang intercept pada respons Resend Activation Email: jawab 5xx
54. Klik (⋯) baris `Mike Tan {runId}-067` → `Resend Activation Email`
55. Verifikasi toast error: "Error, failed to send activation email to Mike Tan {runId}-067."
56. Lepas intercept respons Resend Activation Email
57. Klik (⋯) baris `Mike Tan {runId}-067` lagi
58. Hover opsi `Resend Activation Email`
59. Verifikasi opsi `Resend Activation Email` enabled (cooldown tidak dimulai)
60. Tekan Esc untuk menutup menu row action

### TC-GS-USER-310: Resend Confirmation Email gagal

61. Pasang intercept pada respons Resend Confirmation Email: jawab 5xx
62. Klik (⋯) baris `Rina Putri {runId}-067` → `Resend Confirmation Email`
63. Verifikasi toast error: "Error, failed to send confirmation email to Rina Putri {runId}-067."
64. Lepas intercept respons Resend Confirmation Email

### TC-GS-USER-1037: Bulk Resend Activation Email, semua baris gagal server menampilkan toast error

65. Pasang intercept pada respons Resend Activation Email: jawab 5xx untuk semua request
66. Centang baris `Mike Tan {runId}-067` dan `Andre Kurniawan {runId}-067`
67. Bulk Action → `Resend Activation Email`
68. Verifikasi toast error: "Error, failed to send activation email."
69. Lepas intercept respons Resend Activation Email
70. Klik icon `×` pada Bulk Action Bar
71. Klik (⋯) baris `Mike Tan {runId}-067`
72. Hover opsi `Resend Activation Email`
73. Verifikasi opsi `Resend Activation Email` enabled (cooldown Mike Tan tidak dimulai)
74. Tekan Esc untuk menutup menu row action
75. Klik (⋯) baris `Andre Kurniawan {runId}-067`
76. Hover opsi `Resend Activation Email`
77. Verifikasi opsi `Resend Activation Email` enabled (cooldown Andre Kurniawan tidak dimulai)
78. Tekan Esc untuk menutup menu row action
79. Pulihkan jam server dan jam browser ke waktu nyata
80. Klik icon Changelog di Table Tools
81. Verifikasi Modal Changelog User memuat entri (pembanding sebelum Search)
82. Klik icon Search pada Modal Changelog, ketik `{runId}-067`, tekan Enter
83. Verifikasi jumlah baris `Resend Activation Email` untuk `Mike Tan {runId}-067` sama dengan B_Mike (tidak ada baris baru)
84. Verifikasi jumlah baris `Resend Activation Email` untuk `Andre Kurniawan {runId}-067` sama dengan B_Andre (tidak ada baris baru)
85. Tutup Modal Changelog User dengan klik `✕`

### TC-GS-USER-1038: Bulk Resend Activation Email, sebagian baris gagal server menampilkan toast partial

86. Atur jam server dan jam browser ke `F1` dan bekukan
87. Pasang intercept pada respons Resend Activation Email untuk baris `Andre Kurniawan {runId}-067`: jawab 5xx, request baris lain diteruskan
88. Centang baris `Mike Tan {runId}-067`, `Andre Kurniawan {runId}-067`, dan `Maya Anggraini {runId}-067`
89. Bulk Action → `Resend Activation Email`
90. Verifikasi toast: "Success, activation email has been sent. Some items failed."
91. Lepas intercept respons Resend Activation Email
92. Pulihkan jam server dan jam browser ke waktu nyata
93. Klik icon Changelog di Table Tools
94. Verifikasi Modal Changelog User memuat entri (pembanding sebelum Search)
95. Klik icon Search pada Modal Changelog, ketik `{runId}-067`, tekan Enter
96. Verifikasi jumlah baris `Resend Activation Email` untuk `Mike Tan {runId}-067` bertambah 1 dari B_Mike
97. Verifikasi jumlah baris `Resend Activation Email` untuk `Maya Anggraini {runId}-067` bertambah 1 dari B_Maya
98. Verifikasi jumlah baris `Resend Activation Email` untuk `Andre Kurniawan {runId}-067` sama dengan B_Andre (tidak ada baris baru)
99. Tutup Modal Changelog User dengan klik `✕`

### TC-GS-USER-1050: Bulk Resend Activation Email dengan baris cooldown dan baris gagal server sekaligus

100. Atur jam server dan jam browser ke `F1` dan bekukan, sehingga cooldown `Mike Tan {runId}-067` dari TC-GS-USER-1038 masih berjalan sedangkan cooldown `Andre Kurniawan {runId}-067` dan `Rahmat Hidayat {runId}-067` sudah lewat
101. Pasang intercept pada respons Resend Activation Email untuk baris `Rahmat Hidayat {runId}-067`: jawab 5xx, request baris lain diteruskan
102. Centang baris `Mike Tan {runId}-067`, `Andre Kurniawan {runId}-067`, dan `Rahmat Hidayat {runId}-067`
103. Bulk Action → `Resend Activation Email`
104. Verifikasi toast: "Success, activation email has been sent. Some items failed."
105. Verifikasi toast "Success, activation email has been sent. Some items were skipped (cooldown not finished)." tidak tampil
106. Lepas intercept respons Resend Activation Email
107. Pulihkan jam server dan jam browser ke waktu nyata
108. Klik icon Changelog di Table Tools
109. Verifikasi Modal Changelog User memuat entri (pembanding sebelum Search)
110. Klik icon Search pada Modal Changelog, ketik `{runId}-067`, tekan Enter
111. Verifikasi jumlah baris `Resend Activation Email` untuk `Andre Kurniawan {runId}-067` bertambah 1 dari B_Andre
112. Verifikasi jumlah baris `Resend Activation Email` untuk `Mike Tan {runId}-067` sama dengan B_Mike + 1 (hanya baris dari TC-GS-USER-1038, tidak ada baris baru dari Bulk Resend ini)
113. Verifikasi jumlah baris `Resend Activation Email` untuk `Rahmat Hidayat {runId}-067` sama dengan B_Rahmat (tidak ada baris baru)
114. Tutup Modal Changelog User dengan klik `✕`

## Notes

- Mode: FE+BE (intercept parsial, kelas harness b: fault injection; bagian 6 konvensi). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (114 langkah). Alasan: kesepuluh TC berada di satu kelas harness (b, kegagalan 5xx aksi tulis status dan Resend), satu akun, dan satu layar (User List); tiap blok TC berdiri sendiri (intercept sendiri, dilepas di dalam blok) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Penambah langkah terbesar adalah pembacaan Changelog per blok Resend dan pemulihan jam sebelum Modal Changelog dibuka (S-09).
- Urutan TC sumber diubah: TC-GS-USER-294 ditaruh sesudah TC-GS-USER-1048 dan TC-GS-USER-1049 karena TC-GS-USER-294 mengaktifkan dua user (aksi yang mengubah data), sedangkan TC-GS-USER-1048 dan 1049 memakai user yang sama dan membutuhkan keadaan awal tidak berubah. Blok Resend (TC-GS-USER-308, 310, 1037, 1038, 1050) mengikuti blok status; TC-GS-USER-1050 paling akhir karena cooldown Mike Tan dibentuk oleh TC-GS-USER-1038 (user dan jam dipakai berurutan).
- Langkah penghubung (aksi tanpa `Verifikasi`): `Tunggu toast lama hilang otomatis` sebelum `[Activate]` bulk (langkah 21) dan `[Deactivate]` bulk (langkah 32) agar toast gagal Activate/Deactivate pada langkah 14 dan 7 tidak dibaca ulang sebagai toast bulk, pembukaan layar dan Search `{runId}-067`, memasang dan melepas intercept, `[Cancel]` yang menutup dialog konfirmasi, klik icon `×` pada Bulk Action Bar, Esc menutup menu row action, hover opsi, mencatat baseline Changelog, membaca `T_s`, dan mengatur, membekukan, serta memulihkan jam. Verifikasi "Modal Changelog User memuat entri" adalah anchor positif sebelum Search (bagian 8b butir 2).
- Jam dipulihkan ke waktu nyata sebelum Modal Changelog User dibuka (S-09). Log yang dibuat saat jam digeser bercap waktu di luar waktu nyata, sehingga asersi Changelog memakai selisih jumlah baris terhadap baseline per user (nama user bersuffix), bukan posisi teratas (S-12). Asersi "sama dengan baseline" adalah asersi jumlah, bukan asersi absence kelas g.
- P-1: asersi "tidak ada baris log `Resend Activation Email` baru" TC-GS-USER-1037 (Expected b) dan "log hanya untuk baris yang terkirim" TC-GS-USER-1038 dan TC-GS-USER-1050 (Expected b) ditulis di spec ini sebagai selisih jumlah baris terhadap baseline, karena konteksnya bergantung pada state berat (user Pending Activation seed, jam dibekukan, cooldown yang dibentuk blok sebelumnya, dan intercept per baris) dan tidak ada spec absence yang memuat aksi nyata untuk TC-GS-USER-1037.
- Pembagian TC lintas spec: Toggle Active sukses diverifikasi di spec 047, Bulk Activate dan Deactivate sukses di spec 054, Resend sukses, cooldown, dan Bulk Resend di spec 056; spec ini hanya memuat jalur kegagalan.
- Temuan untuk QA:
  - TC-GS-USER-245, 249, 308, 310, 1048, 1049, dan 1050 menulis precondition "dibuat gagal 5xx" atau "server error" tanpa nama endpoint dan TC-GS-USER-294, 1037, dan 1038 menulis "(mock)"; spec memicu lewat `Spectra.intercept()` di atas backend nyata dan nama endpoint ditentukan tim FE di tahap script.
  - TC-GS-USER-294, 1038, dan 1050 tidak menyebut baris mana yang gagal; spec memilih `Citra Dewanti {runId}-067` (TC-GS-USER-294), `Andre Kurniawan {runId}-067` (TC-GS-USER-1038), dan `Rahmat Hidayat {runId}-067` (TC-GS-USER-1050). TC-GS-USER-1050 menyebut "satu user Pending Activation lain" tanpa nama; spec memakai Rahmat Hidayat dan membentuk cooldown Mike Tan lewat TC-GS-USER-1038 (jam dibekukan di `F1`).
  - TC-GS-USER-308, 310, 1037, 1038, dan 1050 mensyaratkan "cooldown lewat" tanpa cara membuatnya; spec mengatur jam server dan jam browser bersama (bagian 6 konvensi). Seeding user Pending Activation, pembacaan waktu terbit email, dan manipulasi jam tidak punya sumber di TC, PRD, dan LLD; disediakan tim FE/BE.
  - TC-GS-USER-1037, 1038, dan 1050 menyebut "log `Resend Activation Email`" tanpa menyebut surface; spec memakai Modal Changelog User (selaras spec 056).
  - TC-GS-USER-1037 Expected c ("Cooldown tidak dimulai") tidak menyebut cara mengamatinya; spec mengasersi opsi `Resend Activation Email` enabled pada menu row action Mike Tan dan Andre Kurniawan.
  - TC-GS-USER-1048 dan 1049 Expected a ("bukan toast ringkasan T-39") diasersi sebagai toast ringkasan tidak tampil, didahului `Verifikasi` toast error pada surface yang sama.
  - TC-GS-USER-1050 Expected a ("T-41 didahulukan dari T-15") diasersi sebagai toast T-15 `Success, activation email has been sent. Some items were skipped (cooldown not finished).` tidak tampil; teks T-15 mengikuti Expected TC-GS-USER-303 di spec 056.
  - TC-GS-USER-308, 310, 1037, 1038, dan 1050: toast yang memuat nama user memakai nama lengkap user seed bersuffix (`Mike Tan {runId}-067`, `Rina Putri {runId}-067`).
  - TC-GS-USER-245, 249, 1048, dan 1049 tidak menyebut apakah dialog konfirmasi tetap terbuka setelah kegagalan; spec mengikuti error-handling-convention bagian 2 (dialog tetap terbuka pada 5xx) dan menutupnya dengan `[Cancel]`. TC-GS-USER-1048, 1049, dan 1037 tidak menyebut keadaan seleksi sesudah kegagalan total; spec mengosongkan seleksi dengan icon `×` pada Bulk Action Bar. TC-GS-USER-294, 1038, dan 1050 tidak menyebut keadaan seleksi sesudah partial; spec mengikuti TC-GS-USER-1016 (seleksi reset) dan tidak mengosongkan seleksi.
  - TC-GS-USER-1048 dan 1049 menyebut Jane Smith, Budi Santoso, Dewi Lestari, dan Joko Susilo dari Tabel Pre-setup; spec memakai user seed bersuffix milik spec (S-06).
