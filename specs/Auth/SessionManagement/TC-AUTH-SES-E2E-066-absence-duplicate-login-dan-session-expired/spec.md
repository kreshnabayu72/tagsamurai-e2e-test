---
id: TC-AUTH-SES-E2E-066-absence-duplicate-login-dan-session-expired
title: "Absence Pencatatan Duplicate Login dan Session Expired: Kondisi yang Tidak Menulis Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-29
  - TC-AUTH-SES-30
  - TC-AUTH-SES-31
  - TC-AUTH-SES-34
  - TC-AUTH-SES-35
  - TC-AUTH-SES-49
  - TC-AUTH-SES-256
  - TC-AUTH-SES-294
coverage:
  web: automated
  mobile: automated
---

# Absence Pencatatan Duplicate Login dan Session Expired: Kondisi yang Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): delapan user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-29: `Irfan Utami` (`irfanutami+{runId}-066@qwertysystem.net`)
  - TC-AUTH-SES-30: `Tari Puspita` (`taripuspita+{runId}-066@qwertysystem.net`)
  - TC-AUTH-SES-31: `Budi Rahayu` (`budirahayu+{runId}-066@qwertysystem.net`)
  - TC-AUTH-SES-294: `Galih Lestari` (`galihlestari+{runId}-066@qwertysystem.net`)
  - TC-AUTH-SES-256: `Joko Permata` (`jokopermata+{runId}-066@qwertysystem.net`)
  - TC-AUTH-SES-34: `Dewi Nugroho` (`dewinugroho+{runId}-066@qwertysystem.net`)
  - TC-AUTH-SES-35: `Rizky Maulana` (`rizkymaulana+{runId}-066@qwertysystem.net`)
  - TC-AUTH-SES-49: `Joko Firmansyah` (`jokofirmansyah+{runId}-066@qwertysystem.net`)
- Sesi aktif (status Active) tiap user TIDAK dibuat di hook `before`, melainkan di awal tiap TC lewat login API (kondisi yang di-seed BE): sesi web di Browser A (Chrome on Windows) untuk TC-AUTH-SES-29, 30, 31, 256, 34, 35, dan 49, serta sesi mobile di perangkat Android uji A untuk TC-AUTH-SES-294 (login nyata di perangkat A, [Not now] pada Prompt Enable Biometric). Alasannya: batas idle 15 menit berjalan di waktu nyata selama spec berlangsung, dan jam server dimajukan kumulatif pada TC-AUTH-SES-34, 35, dan 49, sehingga sesi yang dibuat di `before` bisa melewati batas idle sebelum TC-nya berjalan.
- Browser B (Firefox on macOS) adalah konteks baru yang belum login; tiap TC yang memakainya membuka konteks Browser B sendiri. Perangkat Android uji B (Tabel Data Uji Pre-setup #10) belum login pada TC-AUTH-SES-294.
- Konteks dan akun (dibuka di hook `before`, login pertama tiap konteks ada di hook): Browser Admin dengan akun aktor Total Control (Global Settings) di atas, dipakai membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik user tiap TC.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server dan jam browser/perangkat dimajukan bersama pada TC-AUTH-SES-34, 35, dan 49, dipulihkan dengan langkah eksplisit sebelum Browser Admin membuka log dan di hook `after` (tetap jalan walau spec gagal di tengah).
- Hook `after`: akhiri semua sesi seed dan sesi yang dibuat spec (web dan mobile), pastikan aplikasi mobile di perangkat A dan B tidak menyimpan sesi, tutup konteks Browser A, B, dan Admin, lalu hapus kedelapan user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - dua konteks browser bersamaan dengan user agent yang dapat ditetapkan (Chrome on Windows, Firefox on macOS), serta dua tab (Tab A dan Tab B) dalam satu konteks Browser A (TC-AUTH-SES-49);
  - jam server uji dapat dimajukan dengan presisi detik, jam browser/perangkat uji (timer idle dan Toast di client) dimajukan sebesar yang sama, dan keduanya dipulihkan ke waktu nyata (Tabel Data Uji Pre-setup #18; TC-AUTH-SES-34, 35, 49);
  - alat uji dapat mengirim ulang request Confirm dengan token pra-autentikasi yang sama (TC-AUTH-SES-256; Tabel Data Uji Pre-setup #18);
  - driver otomasi Android untuk dua perangkat atau emulator bersamaan (A dan B), menutup paksa aplikasi, menghapus sesi lokal aplikasi, dan login nyata di perangkat A dengan [Not now] pada Prompt Enable Biometric (TC-AUTH-SES-294; Tabel Data Uji Pre-setup #10);
  - pembacaan stempel waktu dan isi entri log (Activity, Note) di `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk membedakan entri baru dari entri seeding;
  - reCAPTCHA mode uji di environment (halaman Login with Password).
- Akun yang dipakai: user uji masing-masing TC di Browser A, B, dan perangkat Android A dan B; akun aktor Total Control (Global Settings) di Browser Admin.

## Test Steps

### TC-AUTH-SES-29 (bagian absence, Expected d): Cancel pada Dialog Duplicate Login Attempt tidak dicatat

1. Siapkan sesi web aktif milik `Irfan Utami` di Browser A (Chrome on Windows) lewat login API → status Active
2. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Irfan Utami`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
3. Buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
4. Ketik email `irfanutami+{runId}-066@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
5. Klik [Cancel]
6. Pindah ke Browser A dan klik area mana pun
7. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri `Irfan Utami` lewat Note dan email yang bertambah dibanding baseline sejak klik [Log in] pada langkah 4
8. Verifikasi Tidak ada entri baru untuk `Irfan Utami` di `Global Settings > Activity Log > Session` untuk kondisi Cancel pada Dialog Duplicate Login Attempt
9. Buka `Global Settings > User > Detail > User Log` milik `Irfan Utami` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak klik [Log in] pada langkah 4
10. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Cancel pada Dialog Duplicate Login Attempt

### TC-AUTH-SES-30 (bagian absence, Expected b): Tombol Escape pada Dialog Duplicate Login Attempt tidak dicatat

11. Siapkan sesi web aktif milik `Tari Puspita` di Browser A (Chrome on Windows) lewat login API → status Active
12. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Tari Puspita`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
13. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), lalu buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
14. Ketik email `taripuspita+{runId}-066@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
15. Tekan tombol Escape
16. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri `Tari Puspita` lewat Note dan email yang bertambah dibanding baseline sejak klik [Log in] pada langkah 14
17. Verifikasi Tidak ada entri baru untuk `Tari Puspita` di `Global Settings > Activity Log > Session` untuk kondisi penutupan Dialog Duplicate Login Attempt dengan Escape
18. Buka `Global Settings > User > Detail > User Log` milik `Tari Puspita` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak klik [Log in] pada langkah 14
19. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi penutupan Dialog Duplicate Login Attempt dengan Escape

### TC-AUTH-SES-31 (bagian absence, Expected b): Klik backdrop pada Dialog Duplicate Login Attempt tidak dicatat

20. Siapkan sesi web aktif milik `Budi Rahayu` di Browser A (Chrome on Windows) lewat login API → status Active
21. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Budi Rahayu`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
22. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), lalu buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
23. Ketik email `budirahayu+{runId}-066@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
24. Klik area gelap di luar dialog
25. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri `Budi Rahayu` lewat Note dan email yang bertambah dibanding baseline sejak klik [Log in] pada langkah 23
26. Verifikasi Tidak ada entri baru untuk `Budi Rahayu` di `Global Settings > Activity Log > Session` untuk kondisi penutupan Dialog Duplicate Login Attempt dengan klik backdrop
27. Buka `Global Settings > User > Detail > User Log` milik `Budi Rahayu` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak klik [Log in] pada langkah 23
28. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi penutupan Dialog Duplicate Login Attempt dengan klik backdrop

### TC-AUTH-SES-294 (bagian absence, Expected c): Cancel pada Dialog Duplicate Login Attempt di mobile tidak dicatat

29. Tutup paksa aplikasi mobile di perangkat Android uji A dan B, lalu hapus sesi lokal aplikasi
30. Di perangkat Android uji A login dengan `galihlestari+{runId}-066@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] pada Prompt Enable Biometric → app masuk Portal — Product Hub (sesi mobile aktif di perangkat A)
31. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Galih Lestari`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
32. Di perangkat Android uji B buka aplikasi mobile TAG Samurai, ketik email `galihlestari+{runId}-066@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu ketuk [Login] → Dialog "Duplicate Login Attempt" muncul
33. Ketuk [Cancel]
34. Di perangkat Android uji A ketuk layar
35. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri `Galih Lestari` lewat Note dan email yang bertambah dibanding baseline sejak ketuk [Login] pada langkah 32
36. Verifikasi Tidak ada entri baru untuk `Galih Lestari` di `Global Settings > Activity Log > Session` untuk kondisi Cancel pada Dialog Duplicate Login Attempt di mobile
37. Buka `Global Settings > User > Detail > User Log` milik `Galih Lestari` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak ketuk [Login] pada langkah 32
38. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Cancel pada Dialog Duplicate Login Attempt di mobile

### TC-AUTH-SES-256 (bagian absence, Expected b): Confirm kedua dengan token pra-autentikasi yang sudah dipakai tidak dicatat

39. Siapkan sesi web aktif milik `Joko Permata` di Browser A (Chrome on Windows) lewat login API → status Active
40. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Joko Permata`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
41. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), lalu buka konteks Browser B baru (belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
42. Ketik email `jokopermata+{runId}-066@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
43. Klik [Confirm] → sesi baru di Browser B aktif
44. Kirim ulang request Confirm dengan token pra-autentikasi yang sama (alat uji) → server menolak dengan 422
45. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri `Joko Permata` lewat Note dan email yang bertambah dibanding baseline sejak pengiriman ulang pada langkah 44
46. Verifikasi Tidak ada entri baru untuk `Joko Permata` di `Global Settings > Activity Log > Session` untuk kondisi Confirm kedua dengan token yang sudah dipakai
47. Buka `Global Settings > User > Detail > User Log` milik `Joko Permata` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak pengiriman ulang pada langkah 44
48. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Confirm kedua dengan token yang sudah dipakai

### TC-AUTH-SES-34 (bagian absence, Expected d): Confirm setelah token pra-autentikasi kedaluwarsa tidak dicatat

49. Siapkan sesi web aktif milik `Dewi Nugroho` di Browser A (Chrome on Windows) lewat login API → status Active
50. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Dewi Nugroho`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
51. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), lalu buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
52. Ketik email `dewinugroho+{runId}-066@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
53. Biarkan dialog terbuka dan majukan jam server dan jam browser/perangkat bersama 10 menit 30 detik
54. Klik [Confirm] → server menolak dengan 422 dan Browser B kembali ke halaman Login
55. Pulihkan jam server dan jam browser/perangkat ke waktu nyata
56. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri `Dewi Nugroho` lewat Note dan email yang bertambah dibanding baseline sejak klik [Log in] pada langkah 52
57. Verifikasi Tidak ada entri baru untuk `Dewi Nugroho` di `Global Settings > Activity Log > Session` untuk kondisi Confirm setelah token pra-autentikasi kedaluwarsa
58. Buka `Global Settings > User > Detail > User Log` milik `Dewi Nugroho` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak klik [Log in] pada langkah 52
59. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Confirm setelah token pra-autentikasi kedaluwarsa

### TC-AUTH-SES-35 (bagian absence, Expected d): Confirm saat sesi lama sudah kedaluwarsa tidak mencatat Logged out (new device login)

60. Siapkan sesi web aktif milik `Rizky Maulana` di Browser A (Chrome on Windows) lewat login API → status Active
61. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Rizky Maulana`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
62. Majukan jam server dan jam browser/perangkat bersama 6 menit tanpa aktivitas di Browser A (Browser A idle 6 menit)
63. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), lalu buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
64. Ketik email `rizkymaulana+{runId}-066@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul (token pra-autentikasi berumur 0)
65. Majukan jam server dan jam browser/perangkat bersama 9 menit tanpa aktivitas di Browser A (Browser A idle tepat 15 menit; token pra-autentikasi berumur 9 menit)
66. Klik [Confirm] di Browser B → Browser B masuk Portal — Product Hub
67. Pindah ke Browser A dan amati tanpa interaksi selama 10 detik
68. Pulihkan jam server dan jam browser/perangkat ke waktu nyata
69. Di Browser Admin login ulang dengan akun aktor `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.GS_TC_PASSWORD` (jam digeser kumulatif melewati batas idle)
70. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri `Rizky Maulana` lewat Note dan email yang bertambah dibanding baseline sejak klik [Log in] pada langkah 64
71. Verifikasi Tidak ada entri `Logged out (new device login)` untuk `Rizky Maulana` di `Global Settings > Activity Log > Session` untuk kondisi Confirm saat sesi lama sudah kedaluwarsa
72. Buka `Global Settings > User > Detail > User Log` milik `Rizky Maulana` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak klik [Log in] pada langkah 64
73. Verifikasi Tidak ada entri `Logged out (new device login)` di `Global Settings > User > Detail > User Log` untuk kondisi Confirm saat sesi lama sudah kedaluwarsa

### TC-AUTH-SES-49 (bagian absence, Expected c): Refresh pada Dialog Session Expired saat sesi sudah valid tidak dicatat

74. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), lalu buka konteks Browser A baru dan buat sesi web aktif `Joko Firmansyah` lewat login API (seeding BE) → sesi berstatus Active
75. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Joko Firmansyah`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
76. Di Browser A buka dua tab (Tab A dan Tab B) pada Portal — Product Hub → kedua tab menampilkan Portal — Product Hub
77. Biarkan Browser A tanpa aktivitas dan majukan jam server dan jam browser/perangkat bersama 10 menit → Toast Idle Warning tampil
78. Majukan jam server dan jam browser/perangkat bersama 6 menit lagi (idle 16 menit) → Tab A dan Tab B sama-sama menampilkan Dialog Session Expired
79. Di Tab A klik [Refresh] → halaman Login with Password tampil
80. Di Tab A ketik email `jokofirmansyah+{runId}-066@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil dengan sesi baru Active
81. Pindah ke Tab B → Tab B masih menampilkan Dialog Session Expired
82. Di Tab B klik [Refresh]
83. Pulihkan jam server dan jam browser/perangkat ke waktu nyata
84. Di Browser Admin login ulang dengan akun aktor `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.GS_TC_PASSWORD` (jam digeser kumulatif melewati batas idle)
85. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri `Joko Firmansyah` lewat Note dan email yang bertambah dibanding baseline sejak klik [Refresh] pada langkah 82
86. Verifikasi Tidak ada entri baru untuk `Joko Firmansyah` di `Global Settings > Activity Log > Session` untuk kondisi Refresh pada Dialog Session Expired saat sesi sudah valid
87. Buka `Global Settings > User > Detail > User Log` milik `Joko Firmansyah` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak klik [Refresh] pada langkah 82
88. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Refresh pada Dialog Session Expired saat sesi sudah valid

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness: asersi absence (kelas g, "tidak ada entri"), bersama spec `TC-AUTH-SES-E2E-060-absence-pencatatan-sesi` yang memuat TC absence lain. Pemicu kelas lain (multi-konteks, mobile, time-travel) hanya membentuk kondisi yang diasersi tidak tercatat (`P-5` (a)); jumlah langkah dan campuran harness (multi-konteks, mobile, time-travel) melewati batas smell bagian 3 konvensi karena tiap TC berdiri sendiri dengan user sendiri, sehingga kegagalan satu bagian tidak membuat bagian lain tidak bermakna.
- Pembagian TC lintas spec (prinsip 10): asersi fungsional TC-AUTH-SES-29, 30, dan 31 (dialog tertutup, Browser B kembali ke halaman Login, tidak ada sesi baru, sesi Browser A tetap Active) ada di `TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web`; TC-AUTH-SES-294 di `TC-AUTH-SES-E2E-010-limit-login-mobile-dan-duplicate-login`; TC-AUTH-SES-34, 35 (bagian dicatat `Session expired`, Dialog Logged Out tidak tampil), dan 256 di `TC-AUTH-SES-E2E-013-token-pra-auth-dan-sesi-lama-expired-saat-confirm`; TC-AUTH-SES-49 (Tab B tetap di halaman, sesi baru tidak di-logout) di `TC-AUTH-SES-E2E-019-session-expired-multi-tab`. Spec ini hanya mengasersi klausa absence log dan tidak mengulang asersi fungsional itu.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-29, 30, 31, 294, 256, 34, 35, lalu 49 (urutan TC sumber 29, 30, 31, 34, 35, 49, 256, 294). Jalur yang menutup dialog tanpa memutus sesi lama (Cancel, Escape, backdrop) lebih dulu, Confirm yang ditolak sesudahnya, dan TC yang memajukan jam (34, 35, 49) paling akhir; jam dipulihkan dalam TC masing-masing sebelum Browser Admin membuka log. Tiap TC memakai user dan sesi sendiri, jadi urutan tidak membuat TC saling bergantung.
- Langkah dependensi disalin (S-04): TC-AUTH-SES-29, 30, 31, 34, 35, dan 256 dari TC-AUTH-SES-21 atau TC-AUTH-SES-26 (login di Browser B hingga Dialog "Duplicate Login Attempt" muncul, dan [Confirm] pada TC-AUTH-SES-256); TC-AUTH-SES-294 dari TC-AUTH-SES-22 (login di perangkat B hingga dialog muncul); TC-AUTH-SES-49 dari TC-AUTH-SES-55 dan 46 (idle sampai Dialog Session Expired di dua tab, Tab A [Refresh] dan login ulang). Asersi hasil dependensi diuji di spec pemilik TC dependensi.
- Penentuan "entri baru": baseline (jumlah entri dan stempel waktu entri terbaru di kedua surface) dicatat sebelum langkah pemicu; entri dicari lewat Note dan email user, dan yang diasersi adalah selisih terhadap baseline, bukan posisi teratas. Hanya entri sesudah langkah pemicu TC itu yang dihitung, yaitu klik [Log in] atau ketuk [Login] yang memunculkan dialog (langkah 4, 14, 23, 32, 52, 64), pengiriman ulang Confirm (langkah 44), dan klik [Refresh] di Tab B (langkah 82). Pada TC-AUTH-SES-35 yang diasersikan adalah tidak adanya entri `Logged out (new device login)`; entri lain milik user yang sama (sesi lama `Session expired`, Login sesi baru) boleh ada dan diuji di spec 013.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menutup konteks Browser B TC sebelumnya dan membuka konteks Browser B baru (S-09); perpindahan antar Browser A, Tab A, Tab B, perangkat Android A dan B, dan Browser Admin; menutup paksa aplikasi mobile dan login nyata di perangkat A dengan [Not now] (langkah 29 dan 30); memulihkan jam server dan jam browser/perangkat sebelum Browser Admin membuka log; login ulang akun aktor di Browser Admin pada TC-AUTH-SES-35 dan 49 karena jam digeser kumulatif melewati batas idle; mengamati Browser A selama 10 detik (langkah 67). Hook `after` memulihkan jam sebagai cadangan.
- Temuan untuk QA:
  - TC-AUTH-SES-29 Expected d, TC-AUTH-SES-30 dan 31 Expected b ("tidak dicatat"), dan TC-AUTH-SES-256 Expected b tidak menyebut surface log; spec memakai `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` seperti TC-AUTH-SES-34, 35, 49, dan 294.
  - TC-AUTH-SES-29 Expected d merujuk TC-AUTH-SES-190 yang sudah mengasersi absence Cancel pada Dialog Duplicate Login Attempt web di spec 060; kedua TC dipertahankan sebagai bagian terpisah dengan user terpisah. TC-AUTH-SES-49 Expected c dan TC-AUTH-SES-196 (spec 060) juga mengasersi absence untuk alur Refresh yang sama.
  - TC-AUTH-SES-256 Expected b ("tidak ada entri log baru") tidak menyebut batas waktu entri, padahal Confirm pertama yang berhasil menulis entri sendiri; spec membatasi pencarian ke entri sesudah pengiriman ulang Confirm (langkah 44).
  - TC-AUTH-SES-35 Expected d tidak menyebut apakah `Logged out (new device login)` tercatat sebagai Activity atau Note, dan di surface mana saja; spec mencari teks itu di kedua surface log.
  - TC-AUTH-SES-35 precondition b ("sudah idle 6 menit") tidak menyebut cara mencapainya; spec memajukan jam server dan jam browser/perangkat bersama 6 menit (langkah 62).
  - TC sumber menulis "klik [Log in]" dan "password yang benar" tanpa menyebut reCAPTCHA; spec mengikuti TC dan mengandalkan reCAPTCHA mode uji.
  - TC-AUTH-SES-256 langkah 4 mengirim ulang Confirm lewat alat uji dan tidak menyebut cara FE mengetahui penolakan; spec mengikuti TC (hanya menulis penolakan 422 sebagai hasil pemicu, tanpa `Verifikasi`).
