---
id: TC-GS-UCF-E2E-072-sinkronisasi-ke-form-user-detail-user-dan-my-profile
title: "Sinkronisasi Custom Field ke Form Create User, Create Non-Login User, Detail User, dan My Profile: Field Baru, Rename, Placeholder, Required, Activate dan Deactivate, serta Form yang Sedang Terbuka"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-294
  - TC-GS-UCF-295
  - TC-GS-UCF-296
  - TC-GS-UCF-301
  - TC-GS-UCF-362
  - TC-GS-UCF-363
  - TC-GS-UCF-534
  - TC-GS-UCF-535
  - TC-GS-UCF-537
coverage:
  web: automated
---

# Sinkronisasi Custom Field ke Form Create User, Create Non-Login User, Detail User, dan My Profile: Field Baru, Rename, Placeholder, Required, Activate dan Deactivate, serta Form yang Sedang Terbuka

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC) sebagai sesi A. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Login User Client A Rahmat Hidayat `rahmatHidayat_automated_qaTeam1@qwertysystem.net` (Pre-setup TC) untuk TC-GS-UCF-296 dan 537, login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_RAHMAT_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Pelaku kedua (sesi B pada TC-GS-UCF-301, 362, 363, dan 535, hanya memicu perubahan definisi): Total Control Client A Admin kedua Nadia Pratama `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup TC) lewat sesi API (P-2) dengan `Spectra.env.GS_TC2_PASSWORD`; TC hanya menyebut "sesi B: Total Control pada Client A" tanpa akun, dan mekanisme sesi API disediakan tim FE/BE. Hasil di sesi B tidak diasersi, sehingga tidak ada sesi UI kedua.
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control Client A.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah pertama spec berpindah ke Global Settings > User > User List (sub-tab Login User).
- Data Pre-setup (baca-saja): 6 Custom Field Pre-setup Client A (`Cost Center` Dropdown Required Yes, `Employee Grade` Text Required No, dan lainnya), Login User Rahmat Hidayat dengan nilai Custom Field Pre-setup, Non-Login User Budi Kurniawan (Pre-setup `tc-non-login-user.md`, tidak diubah). Field Wajib Create User tidak diisi karena popup Create User/Non-Login User hanya dibuka dan ditutup tanpa Submit.
- Data Dinamis (nama bersuffix `{runId}-072`; fixture baru `Fixture.customFieldUser.sync072`), di-seed lewat API oleh Sari Dewi di hook `before`:
  - `Consumer Probe {runId}-072` (Text, Active; nilai User Rahmat Hidayat = `Probe Value`; D-89) untuk TC-GS-UCF-294, 295, dan 296.
  - `Realtime Meta {runId}-072` (Text, Placeholder kosong, Required No; D-135) untuk TC-GS-UCF-362.
  - `Realtime Toggle {runId}-072` (Text, Active; D-136) untuk TC-GS-UCF-363.
  - `Req Detail Probe {runId}-072` (Text, Required No, tanpa nilai User; D-240) untuk TC-GS-UCF-534.
  - `Lifecycle Probe {runId}-072` (Text, Active; nilai User Rahmat Hidayat = `Lifecycle Value`; D-236) untuk TC-GS-UCF-537.
  - Dibuat oleh sesi B (API) selama spec: `Realtime Probe {runId}-072` (Text; belum ada saat sesi A membuka popup pertama kali; D-90, TC-GS-UCF-301) lalu di-rename menjadi `Realtime Probe 2 {runId}-072`; `Open Form Probe {runId}-072` (Text; D-239, TC-GS-UCF-535).
  - Mekanisme seeding nilai User (Rahmat Hidayat) disediakan tim FE/BE.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-072` yang masih ada; kembalikan sesi ke Sari Dewi.
- Menunggu waktu nyata: 10 detik pada TC-GS-UCF-535 (nilai 10 detik bertanda `PRD?` di TC; jeda pendek di bawah 30 detik, konvensi bagian 6).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (Sari Dewi dan Rahmat Hidayat) dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: sesi API Nadia Pratama untuk mengubah definisi Custom Field; ganti akun (logout lalu login); muat ulang halaman (F5); popup Create User dan Create Non-Login User dibuka lalu ditutup tanpa perubahan (tanpa dialog `Unsaved Changes`).
- State global: tidak ada yang diubah selain flag Guided Tooltip, sesi akun, dan definisi Custom Field milik spec.

## Test Steps

### Pembuka

1. Buka Global Settings > User > User List (sub-tab Login User)

### TC-GS-UCF-294: Field baru tampil pada form Create User dan Detail User Login

2. Klik `[+ User]`
3. Verifikasi section Custom Field dinamis pada popup Create User memuat field `Consumer Probe {runId}-072`
4. Verifikasi placeholder field `Consumer Probe {runId}-072` adalah `Enter consumer probe {runId}-072`
5. Tutup popup lewat `✕`
6. Ketik Search `Rahmat Hidayat` pada User List, tekan Enter
7. Buka Detail Rahmat Hidayat > section Custom Fields
8. Verifikasi Detail Rahmat Hidayat menampilkan `Consumer Probe {runId}-072: Probe Value`

### TC-GS-UCF-295: Field baru tampil pada form Create Non-Login User

9. Buka Global Settings > User > User List (sub-tab Non-Login User)
10. Klik `[+ Non-Login User]`
11. Verifikasi section Custom Field popup Create Non-Login User memuat field `Consumer Probe {runId}-072` (katalog sama dengan Login User)
12. Tutup popup lewat `✕`
13. Ketik Search `Budi Kurniawan` pada User List, tekan Enter
14. Buka Detail Budi Kurniawan
15. Expand section Custom Fields
16. Verifikasi section Custom Fields Detail Non-Login User Budi Kurniawan memuat field `Consumer Probe {runId}-072`

### TC-GS-UCF-534: Perubahan Required ditandai pada label field di Detail User Login

17. Buka Global Settings > User > Custom Field
18. Ketik Search `Req Detail Probe {runId}-072`, tekan Enter
19. Klik `⋯` pada baris `Req Detail Probe {runId}-072`, pilih `Edit`
20. Ubah Required menjadi `Yes`
21. Klik `[Save]`
22. Verifikasi toast sukses: "Success, custom field has been updated."
23. Buka Global Settings > User > User List (sub-tab Login User)
24. Ketik Search `Rahmat Hidayat` pada User List, tekan Enter
25. Buka Detail Rahmat Hidayat > section Custom Fields
26. Verifikasi label `Req Detail Probe {runId}-072` memuat tanda Required
27. Verifikasi label `Employee Grade` tidak memuat tanda Required

### TC-GS-UCF-301: Perubahan definisi tercermin pada form User yang dibuka kembali tanpa memuat ulang halaman

28. Sesi A klik `[+ User]`, lalu tutup popup lewat `✕`
29. Sesi B (Nadia Pratama, sesi API) membuat field `Realtime Probe {runId}-072` (Text) hingga tersimpan
30. Sesi A klik `[+ User]` tanpa memuat ulang halaman
31. Verifikasi field `Realtime Probe {runId}-072` tampil di popup sesi A tanpa reload halaman
32. Sesi A menutup popup lewat `✕`
33. Sesi B mengganti nama field menjadi `Realtime Probe 2 {runId}-072` hingga tersimpan
34. Sesi A klik `[+ User]` lagi tanpa memuat ulang halaman
35. Verifikasi label field berubah menjadi `Realtime Probe 2 {runId}-072` di popup sesi A tanpa reload halaman
36. Sesi A menutup popup lewat `✕`

### TC-GS-UCF-362: Perubahan Placeholder dan Required tercermin pada form User yang dibuka kembali tanpa memuat ulang halaman

37. Sesi A klik `[+ User]`
38. Verifikasi field `Realtime Meta {runId}-072` tampil di popup (state sebelum perubahan)
39. Sesi A menutup popup lewat `✕`
40. Sesi B (sesi API) mengubah `Realtime Meta {runId}-072`: Placeholder `Fresh hint`, Required `Yes`, hingga tersimpan
41. Sesi A klik `[+ User]` tanpa memuat ulang halaman
42. Verifikasi input `Realtime Meta {runId}-072` pada sesi A menampilkan placeholder `Fresh hint` tanpa reload halaman
43. Verifikasi label `Realtime Meta {runId}-072` pada sesi A ditandai Required tanpa reload halaman
44. Sesi A menutup popup lewat `✕`

### TC-GS-UCF-363: Activate dan Deactivate tercermin pada form User yang dibuka kembali tanpa memuat ulang halaman

45. Sesi A klik `[+ User]`
46. Verifikasi field `Realtime Toggle {runId}-072` tampil di popup (state sebelum Deactivate)
47. Sesi A menutup popup lewat `✕`
48. Sesi B (sesi API) menonaktifkan `Realtime Toggle {runId}-072` hingga tersimpan
49. Sesi A klik `[+ User]` tanpa memuat ulang halaman
50. Verifikasi field `Cost Center` tampil di popup sesi A (pembanding: popup sudah termuat)
51. Verifikasi field `Realtime Toggle {runId}-072` tidak tampil di popup sesi A setelah Deactivate tanpa reload halaman
52. Sesi A menutup popup lewat `✕`
53. Sesi B (sesi API) mengaktifkan `Realtime Toggle {runId}-072` kembali hingga tersimpan
54. Sesi A klik `[+ User]` tanpa memuat ulang halaman
55. Verifikasi field `Realtime Toggle {runId}-072` tampil kembali di popup sesi A setelah Activate tanpa reload halaman
56. Sesi A menutup popup lewat `✕`

### TC-GS-UCF-535: Form Create User yang sedang terbuka tidak diperbarui saat definisi Custom Field berubah

57. Sesi A klik `[+ User]` dan biarkan popup terbuka
58. Sesi B (sesi API) membuat field `Open Form Probe {runId}-072` (Text) hingga tersimpan
59. Sesi A menunggu 10 detik tanpa memuat ulang halaman
60. Verifikasi field `Cost Center` tampil di popup sesi A (pembanding: popup sudah termuat)
61. Verifikasi popup sesi A yang sedang terbuka tidak memuat field `Open Form Probe {runId}-072`
62. Sesi A menutup popup lewat `✕`
63. Sesi A klik `[+ User]` lagi tanpa memuat ulang halaman
64. Verifikasi field `Open Form Probe {runId}-072` tampil
65. Sesi A menutup popup lewat `✕`

### TC-GS-UCF-537 bagian pertama: Deactivate field tercermin pada My Profile

66. Buka Global Settings > User > Custom Field
67. Ketik Search `Lifecycle Probe {runId}-072`, tekan Enter
68. Matikan switch Active baris `Lifecycle Probe {runId}-072`
69. Klik `[Deactivate]`
70. Tunggu aksi selesai (dialog tertutup)
71. Ganti akun: logout dari Total Control Client A Sari Dewi
72. Login sebagai Login User Rahmat Hidayat (`Spectra.env.GS_RAHMAT_PASSWORD`)
73. Klik icon Profile di navbar, buka My Profile
74. Verifikasi section Custom Field My Profile memuat `Consumer Probe {runId}-072` (pembanding: section sudah termuat)
75. Verifikasi section Custom Field tidak memuat `Lifecycle Probe {runId}-072`

### TC-GS-UCF-296: Field dan nilai tampil read-only di My Profile

76. Verifikasi section Custom Field menampilkan `Consumer Probe {runId}-072` dengan nilai `Probe Value`
77. Verifikasi nilai `Probe Value` bersifat read-only
78. Verifikasi tidak ada kontrol ubah pada field `Consumer Probe {runId}-072`

### TC-GS-UCF-537 bagian kedua: Activate field mengembalikan nilai lama pada My Profile

79. Ganti akun: logout dari Login User Rahmat Hidayat
80. Login sebagai Total Control Client A Sari Dewi (`Spectra.env.GS_TC_PASSWORD`)
81. Buka Global Settings > User > Custom Field
82. Ketik Search `Lifecycle Probe {runId}-072`, tekan Enter
83. Nyalakan switch Active baris `Lifecycle Probe {runId}-072`
84. Klik `[Activate]`
85. Tunggu aksi selesai (dialog tertutup)
86. Ganti akun: logout dari Total Control Client A Sari Dewi
87. Login sebagai Login User Rahmat Hidayat (`Spectra.env.GS_RAHMAT_PASSWORD`)
88. Klik icon Profile di navbar, buka My Profile
89. Muat ulang halaman (F5)
90. Verifikasi section Custom Field memuat `Lifecycle Probe {runId}-072`
91. Verifikasi nilai `Lifecycle Value` tampil read-only pada `Lifecycle Probe {runId}-072` (nilai lama kembali utuh)

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-GS-UCF-537 dibagi dua subjudul (bagian pertama dan kedua) karena langkah Rahmat Hidayat disisipi TC-GS-UCF-296 pada sesi login yang sama.
- Urutan TC dalam spec: 294, 295, 534, 301, 362, 363, 535, 537 (bagian pertama), 296, 537 (bagian kedua). Urutan menyimpang dari urutan TC sumber: seluruh TC dengan akun Sari Dewi dikerjakan lebih dulu, lalu TC dengan akun Rahmat Hidayat (TC-GS-UCF-296 dan 537) digabung pada sesi login yang sama dengan tiga kali ganti akun (dua sesi Rahmat Hidayat, dipisah Activate oleh Sari Dewi) (bagian 3 prinsip 3 dan 5; bagian 3 "Beda akun ... kecuali ada Step ganti akun eksplisit dan bagian sesudahnya tetap bermakna").
- Sesi A adalah sesi utama (browser) dan sesi B hanya memicu perubahan definisi lewat sesi API (P-2): hasil di sesi B tidak diasersi pada TC-GS-UCF-301, 362, 363, dan 535, sehingga tidak ada sesi UI kedua dan spec tetap satu konteks UI. Pada TC-GS-UCF-537 pengamat adalah Rahmat Hidayat (objek asersi); pengamatan itu dilakukan lewat ganti akun berurutan di sesi utama, bukan sesi UI paralel, dan aksi pemicu Sari Dewi dilakukan lewat UI sesuai langkah TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah pertama spec (pindah ke User List), penutupan popup Create User atau Create Non-Login User lewat `✕` (popup tidak dirty sehingga tanpa dialog `Unsaved Changes`), pengisian Search User List dan Search tabel Custom Field, `Tunggu aksi selesai (dialog tertutup)`, ganti akun, dan menunggu 10 detik. Langkah "Verifikasi field `Cost Center` tampil" sebelum asersi absence adalah pembanding yang menjadi anchor positif (bagian 8b butir 2).
- Verifikasi tambahan di luar Expected TC (S-03): langkah 38 dan 46 (field tampil di popup sebelum perubahan/Deactivate) berasal dari langkah "perhatikan" TC-GS-UCF-362 dan 363, bukan dari Expected; keduanya pembanding state sebelum perubahan untuk asersi langkah 42, 43, dan sesudah Deactivate.
- TC-GS-UCF-537 bagian kedua menutup dengan hook `after` yang mengembalikan sesi ke Sari Dewi; spec berakhir di akun Rahmat Hidayat.
- Spec melewati sekitar 35 langkah (91 langkah). Seluruhnya satu topik (sinkronisasi definisi Custom Field ke konsumen User, Non-Login User, Detail User, dan My Profile), tiap blok TC memakai field bersuffix sendiri sehingga berdiri sendiri. Ganti akun memakai langkah eksplisit dan bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal.
- Pembagian TC lintas spec: konsumen Fixed Asset dan Admin Console ada di spec 073; Staging Table Import ada di spec 074.
- Temuan untuk QA:
  - TC-GS-UCF-301, 362, 363, dan 535 menyebut "sesi B: Total Control pada Client A" tanpa akun; spec memakai Nadia Pratama (Pre-setup TC, admin kedua) lewat sesi API dan menyatakan mekanismenya sebagai disediakan tim FE/BE. TC-GS-UCF-537 menyebut sesi B sebagai Login User Rahmat Hidayat; spec memakai ganti akun berurutan, bukan sesi paralel.
  - TC-GS-UCF-294 Expected a menyebut placeholder `Enter consumer probe`; karena field bersuffix, spec mengasersi `Enter consumer probe {runId}-072` dengan asumsi default placeholder diturunkan dari nama field.
  - TC-GS-UCF-294 menyebut "section Custom Fields" (Detail) dan TC-GS-UCF-296 "section Custom Field" (My Profile) dan "accordion Custom Field" (Admin Console, TC-GS-UCF-298); spec memakai teks per TC, dan penamaan section di PRD konsumen tidak diperiksa ulang oleh penulis spec.
  - TC-GS-UCF-534 dan 362 menyebut "tanda Required" dan "ditandai Required" tanpa wujudnya (mis. tanda bintang); spec mengasersi keberadaan tanda tanpa menyebut bentuk.
  - TC-GS-UCF-295 mengasumsikan Non-Login User Budi Kurniawan ada (Pre-setup `tc-non-login-user.md`) dan tombol `[+ Non-Login User]` ada di sub-tab Non-Login User; Pre-setup TC modul ini tidak memuat Budi Kurniawan.
  - TC-GS-UCF-296 precondition "User berada di halaman mana pun" dan langkah "klik icon Profile di navbar" tanpa teks menu; spec mengikuti TC.
  - Nilai 10 detik (TC-GS-UCF-535) bertanda `PRD?` di TC; spec memakai jeda nyata 10 detik.
  - TC-GS-UCF-537 langkah 2 (pengamatan sesudah Deactivate) tidak menyebut muat ulang My Profile, sedangkan langkah 4 menyebutnya; spec mengikuti TC.
  - Post Condition TC-GS-UCF-534 (`Req Detail Probe` Required Yes) dan TC-GS-UCF-535 (`Open Form Probe` ada) tidak punya langkah observasi tambahan.
