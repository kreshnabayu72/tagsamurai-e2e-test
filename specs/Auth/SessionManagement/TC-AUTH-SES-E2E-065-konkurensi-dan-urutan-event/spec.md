---
id: TC-AUTH-SES-E2E-065-konkurensi-dan-urutan-event
title: "Konkurensi dan Urutan Event: Aksi Paralel, Push Terlewat, dan Reconnect SSE"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-SES-238
  - TC-AUTH-SES-239
  - TC-AUTH-SES-240
  - TC-AUTH-SES-241
  - TC-AUTH-SES-242
  - TC-AUTH-SES-243
  - TC-AUTH-SES-265
coverage:
  web: automated
---

# Konkurensi dan Urutan Event: Aksi Paralel, Push Terlewat, dan Reconnect SSE

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`; akun ini sudah login di Browser Admin pada hook; user dan seat milik Client Q2 (TC-AUTH-SES-239 dan 240) oleh akun aktor Total Control (Global Settings) dengan scope Client Q2, Tabel Data Uji Pre-setup #26, yang sudah login di Browser Admin Q2 pada hook; user Client Suspend (TC-AUTH-SES-241) oleh akun aktor Total Control (Global Settings) dengan scope Client Suspend, Tabel Data Uji Pre-setup #32), password semua user `Spectra.env.SES_PASSWORD`, email bersuffix per run. Semua user Activated, Active ON, profil BASE, MFA dan Agreement tidak terpicu:
  - TC-AUTH-SES-238, 242, 243, 265 (Client `Alpha Logistik`, Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5): `Budi Pratama` (`budipratama+{runId}-065@qwertysystem.net`, tanpa sesi aktif), `Rizky Utami` (`rizkyutami+{runId}-065@qwertysystem.net`), `Nur Puspita` (`nurpuspita+{runId}-065@qwertysystem.net`), `Nadia Firmansyah` (`nadiafirmansyah+{runId}-065@qwertysystem.net`)
  - TC-AUTH-SES-239 dan 240 (Client Q2, Tabel Data Uji Pre-setup #12: subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2; App Access Fixed Asset dan Supply Asset): `Siti Ramadhan` (`sitiramadhan+{runId}-065@qwertysystem.net`) dengan sesi platform dan sesi-produk Fixed Asset Active di-seed lewat login API dan pembukaan produk API; user seed pemegang seat `Gunawan Prakoso` (`gunawanprakoso+{runId}-065@qwertysystem.net`, pola Tabel Data Uji Pre-setup #7) dengan sesi-produk Fixed Asset Active di-seed lewat API; `Andi Wulandari` (`andiwulandari+{runId}-065@qwertysystem.net`) dan `Dewi Hidayat` (`dewihidayat+{runId}-065@qwertysystem.net`) masing-masing dengan sesi platform Active di Portal — Product Hub
  - TC-AUTH-SES-241 (Client Suspend, Tabel Data Uji Pre-setup #16, App Access Fixed Asset): `Sari Firmansyah` (`sarifirmansyah+{runId}-065@qwertysystem.net`)
- Akun aktor lain (login eksplisit di langkah, ganti konteks): Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2), `Spectra.env.FA_MGL_PASSWORD`, di Browser Lisensi (TC-AUTH-SES-239, 240, 243); Principal Admin Console `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #4), `Spectra.env.AC_PRINCIPAL_PASSWORD`, di Browser Principal untuk Suspend dan Unsuspend Client Suspend (TC-AUTH-SES-241).
- Password baru hasil Reset Password: `Spectra.env.SES_PASSWORD_NEW` (TC-AUTH-SES-243). Mail-catcher lingkungan uji (Tabel Data Uji Pre-setup #19) dapat membaca email reset `nurpuspita+{runId}-065@qwertysystem.net`.
- Suite berjalan serial (`parallel: false`); state global yang diubah: koneksi SSE Browser A diputus lalu dipulihkan (TC-AUTH-SES-242, 243, 265); jam server dan jam browser/perangkat dimajukan bersama pada TC-AUTH-SES-243 dan keduanya dipulihkan dengan langkah eksplisit; Client Suspend di-Suspend lalu di-Unsuspend (TC-AUTH-SES-241); seat Fixed Asset Client Q2 dipakai dan dilepas. Semuanya dipulihkan juga di hook `after`.
- Hook `after`: pulihkan koneksi SSE; kembalikan jam server dan jam browser/perangkat ke waktu nyata; Unsuspend Client Suspend bila masih Suspended; akhiri semua sesi dan sesi-produk seed sehingga seat Client Q2 kembali seperti semula; tutup semua konteks browser; hapus seluruh user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`, `SES_PASSWORD_NEW`, `AC_PRINCIPAL_PASSWORD`, `FA_MGL_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness c: multi-konteks dan race): banyak konteks browser bersamaan (Browser Admin, Browser Admin Q2, Browser A Chrome on Windows, Browser B Firefox on Windows dan Firefox on macOS, Browser C, Browser Lisensi, Browser Principal); memicu klik di dua konteks pada saat yang sama (selisih kurang dari 1 detik), termasuk [Confirm Logout] di Browser Lisensi bersamaan dengan Log Out di Browser A (TC-AUTH-SES-239); pemutus dan pemulih koneksi SSE per Browser A (Tabel Data Uji Pre-setup #18); pembacaan panel Network untuk menghitung heartbeat dan event; pembacaan jumlah entri dan stempel waktu entri log di `Global Settings > Activity Log > Session` dan User Log untuk baseline (TC-AUTH-SES-239); pengatur waktu server uji dan jam browser/perangkat yang dimajukan bersama (Tabel Data Uji Pre-setup #18); mail-catcher; mengakhiri semua sesi-produk Client Q2 dan membuat sesi-produk Fixed Asset lewat API oleh akun aktor Total Control scope Client Q2 pada langkah 23 (disediakan tim BE, tanpa endpoint tertentu); reCAPTCHA mode uji di environment (halaman Login with Password).

## Test Steps

### TC-AUTH-SES-238: Dua login bersamaan di platform yang sama menghasilkan satu sesi aktif

1. Buka Browser A (konteks baru, Chrome on Windows) dan Browser B (konteks baru, Firefox on Windows) di halaman `Auth > Login with Password`
2. Di Browser A dan Browser B ketik email `budipratama+{runId}-065@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`
3. Klik [Log in] di Browser A dan Browser B pada saat yang sama (selisih kurang dari 1 detik)
4. Verifikasi Hanya satu sesi web Active milik `Budi Pratama` yang terbentuk: tepat satu dari Browser A dan Browser B masuk Portal — Product Hub
5. Verifikasi Login yang diproses server lebih dulu mendapat sesi dan masuk Portal — Product Hub
6. Verifikasi Login lainnya menerima Dialog Duplicate Login Attempt (browser yang tidak masuk Portal menampilkan dialog itu)
7. Verifikasi Tidak pernah ada dua sesi web Active: Browser A dan Browser B tidak sama-sama berada di Portal — Product Hub
8. Klik [Cancel] pada Dialog Duplicate Login Attempt

### TC-AUTH-SES-239: Admin force-logout dan user manual logout bersamaan menghasilkan satu hasil dan tanpa row log tambahan

9. Tutup konteks Browser A dan Browser B sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) muat sesi web seed milik `sitiramadhan+{runId}-065@qwertysystem.net` → Portal — Product Hub tampil
10. Di Browser A buka Fixed Asset → sesi-produk Fixed Asset seed aktif dan seat terpakai
11. Buka Browser Lisensi (konteks baru) dan login sebagai `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_MGL_PASSWORD`
12. Di Browser Admin Q2 (akun aktor Total Control scope Client Q2, Tabel Data Uji Pre-setup #26) buka `Global Settings > Activity Log > Session` dan User Log `Siti Ramadhan`, lalu catat baseline: jumlah entri `Siti Ramadhan` (dicari lewat Note dan email `sitiramadhan+{runId}-065@qwertysystem.net`) dan stempel waktu entri terbaru di kedua surface
13. Di Browser Lisensi buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), pilih `Siti Ramadhan`, lalu klik [Force Logout] sampai dialog konfirmasi "Force Logout User" tampil
14. Di Browser A buka menu Profile
15. Klik [Confirm Logout] di Browser Lisensi dan Log Out di Browser A pada saat yang sama (klik bersamaan di kedua browser, selisih kurang dari 1 detik)
16. Verifikasi Sesi berakhir tepat sekali dan hasilnya mengikuti pemenang (first-write-wins): status akhir hanya salah satu dari Force Logged Out atau Logged Out, tidak keduanya
17. Di Browser Admin Q2 buka `Global Settings > Activity Log > Session` dan User Log `Siti Ramadhan`, lalu cari entri lewat Note dan email `sitiramadhan+{runId}-065@qwertysystem.net` yang bertambah dibanding baseline langkah 12
18. Verifikasi Bila force-logout menang: sesi-produk dan sesi platform berstatus Force Logged Out dan selisih entri terhadap baseline langkah 12 memuat dua row `Logged out by admin` (LOG-17 dan LOG-25)
19. Verifikasi Bila manual logout menang: sesi berstatus Logged Out dan selisih entri terhadap baseline langkah 12 memuat `Logged out` dan `Session ended` per sesi-produk anak
20. Verifikasi Sisi yang kalah dari klik bersamaan menerima respons idempotent (panel Network)
21. Verifikasi Tidak ada toast error di Browser A
22. Verifikasi Tidak ada toast error di Browser Lisensi

### TC-AUTH-SES-240: Dua user membuka produk bersamaan saat tersisa satu seat hanya satu yang berhasil

23. Lewat API (akun aktor Total Control Client Q2, Tabel Data Uji Pre-setup #26) akhiri semua sesi-produk Client Q2 lalu buat sesi-produk Fixed Asset untuk `Gunawan Prakoso` sehingga tersisa tepat satu seat
24. Tutup konteks Browser A sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) muat sesi web seed milik `andiwulandari+{runId}-065@qwertysystem.net` → Portal — Product Hub tampil
25. Tutup konteks Browser B sebelumnya (hapus sesi login browser), lalu di Browser B (konteks baru, Firefox on Windows) muat sesi web seed milik `dewihidayat+{runId}-065@qwertysystem.net` → Portal — Product Hub tampil
26. Klik card Fixed Asset di Browser A dan Browser B pada saat yang sama (selisih kurang dari 1 detik)
27. Verifikasi Tepat satu user masuk Fixed Asset
28. Verifikasi User lain menerima Popup "Concurrent session limit reached"
29. Di Browser Lisensi muat ulang `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
30. Verifikasi Seat aktif menjadi 2
31. Verifikasi Seat aktif tidak pernah melebihi kuota 2

### TC-AUTH-SES-241: Dialog lifecycle push saat user sedang mengisi form tidak menyimpan data form

32. Tutup konteks Browser A dan Browser B sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `sarifirmansyah+{runId}-065@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
33. Di Browser A klik card Fixed Asset → sesi-produk Fixed Asset aktif
34. Di Browser A buka form Create pada Fixed Asset dan isi sebagian field tanpa Submit
35. Buka Browser Principal (konteks baru) dan login sebagai `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_PRINCIPAL_PASSWORD`
36. Di Browser Principal buka `Admin Console > Client`, buka menu elipsis Client Suspend, dan pilih Suspend
37. Pindah ke Browser A → Dialog "Access Restricted" muncul walau form sedang diisi
38. Klik [OK] pada Dialog Access Restricted
39. Muat ulang halaman di Browser A
40. Buka kembali form Create yang sama di Fixed Asset
41. Verifikasi Data form yang belum di-submit tidak tersimpan: semua field kosong
42. Di Browser Principal buka menu elipsis Client Suspend dan pilih Unsuspend

### TC-AUTH-SES-242: Push Logged Out terlewat: request berikutnya ditolak dengan alasan duplicate login

43. Tutup konteks Browser A sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `rizkyutami+{runId}-065@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
44. Putuskan koneksi SSE Browser A
45. Tutup konteks Browser B sebelumnya (hapus sesi login browser), lalu di Browser B (konteks baru, Firefox on macOS) login dengan akun yang sama dan klik [Log in] → Dialog Duplicate Login Attempt muncul
46. Klik [Confirm] pada Dialog Duplicate Login Attempt di Browser B
47. Pulihkan koneksi SSE Browser A
48. Di Browser A klik menu apa pun
49. Verifikasi Server menjawab 401 dengan alasan duplicate login
50. Verifikasi Dialog "Logged Out" tampil di Browser A dengan Body "You have been logged out because another session was started on a different device."

### TC-AUTH-SES-265: Reconnect SSE memicu heartbeat dan pemeriksaan status tanpa memutar ulang event yang terlewat

51. Tutup konteks Browser A dan Browser B sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `nadiafirmansyah+{runId}-065@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
52. Putuskan koneksi SSE Browser A
53. Di Browser Admin buka `Global Settings > User`, cari `Nadia Firmansyah`, dan matikan Toggle Active
54. Pulihkan koneksi SSE Browser A dan amati panel Network
55. Verifikasi Reconnect memicu satu heartbeat atau pemeriksaan status
56. Verifikasi Event yang terlewat tidak diputar ulang (panel Network tidak memuat pengiriman ulang event)
57. Verifikasi Status terkini direkonstruksi dari server: Dialog "Account Deactivated" tampil tepat satu kali

### TC-AUTH-SES-243: Alasan berakhirnya sesi pada respons 401 menentukan dialog yang tampil

58. Tutup konteks Browser A dan Browser B sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `nurpuspita+{runId}-065@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
59. Di Browser A klik card Fixed Asset → sesi-produk Fixed Asset aktif
60. Putuskan koneksi SSE Browser A
61. Di Browser Lisensi buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), pilih `Nur Puspita`, lalu klik [Force Logout]
62. Klik [Confirm Logout] pada dialog konfirmasi "Force Logout User"
63. Pulihkan koneksi SSE Browser A
64. Di Browser A klik menu apa pun
65. Verifikasi Admin force-logout menampilkan Dialog "Log Out" dengan Body "You have been logged out by an administrator."
66. Tutup konteks Browser A sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `nurpuspita+{runId}-065@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil (sesi baru)
67. Putuskan koneksi SSE Browser A
68. Biarkan Browser A tanpa aktivitas dan majukan jam server dan jam browser/perangkat bersama 16 menit (melewati batas idle 15 menit)
69. Pulihkan koneksi SSE Browser A
70. Di Browser A klik menu apa pun
71. Verifikasi Idle expired menampilkan Dialog "Session Expired" dengan Body "Your session has expired due to inactivity."
72. Pulihkan jam server dan jam browser/perangkat ke waktu nyata
73. Tutup konteks Browser A sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `nurpuspita+{runId}-065@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil (sesi baru)
74. Putuskan koneksi SSE Browser A
75. Di Browser C (konteks baru, belum login) buka `Auth > Login with Password` dan jalankan Forgot Password untuk `nurpuspita+{runId}-065@qwertysystem.net`
76. Buka email reset password di mail-catcher dan buka tautan Reset Password-nya di Browser C
77. Isi password baru `Spectra.env.SES_PASSWORD_NEW` yang valid dan selesaikan Reset Password
78. Pulihkan koneksi SSE Browser A
79. Di Browser A klik menu apa pun
80. Verifikasi Password diganti menampilkan Dialog "Password Changed" dengan Body "Your password has been changed. Please log in again."
81. Verifikasi Salah memilih dialog tidak terjadi: tiap alasan hanya menampilkan dialog yang sesuai (langkah 65, 71, dan 80) dan tidak ada dialog lain pada masing-masing skenario

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec melewati sekitar 35 langkah karena tujuh TC multi-konteks masing-masing butuh user dan konteksnya sendiri; bagian sesudah sebuah TC tetap bermakna walau TC sebelumnya gagal.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-238, 239, 240, 241, 242, 265, 243 (urutan TC sumber 238, 239, 240, 241, 242, 243, 265). TC-AUTH-SES-239 mendahului TC-AUTH-SES-240 mengikuti urutan seed; TC-AUTH-SES-240 diawali langkah API (langkah 23) yang mengakhiri semua sesi-produk Client Q2 dan membuat sesi-produk `Gunawan Prakoso`, sehingga tidak bergantung pada TC-AUTH-SES-239. TC-AUTH-SES-243 memajukan waktu server dan mereset password sehingga ditaruh paling akhir; di dalamnya skenario disusun force-logout, idle expired, lalu password diganti (urutan TC sumber: password diganti, force-logout, idle expired) supaya password tidak berubah sebelum skenario lain. TC-AUTH-SES-243 memakai sesi baru untuk tiap skenario sesuai precondition.
- Dependensi disalin sebagai langkah (S-04): TC-AUTH-SES-241 menyalin langkah TC-AUTH-SES-86 (Client Suspend, form Create terisi sebagian, [OK] pada Dialog Access Restricted, muat ulang) dan menaruh asersi pada data form seperti Expected TC-AUTH-SES-241; langkah TC-AUTH-SES-58 (idle tercapai saat mengetik form) tidak disalin karena TC-AUTH-SES-241 memilih satu pemicu dialog (lihat Temuan 1).
- Baseline TC-AUTH-SES-239 (S-12): jumlah entri dan stempel waktu entri terbaru `Siti Ramadhan` di `Global Settings > Activity Log > Session` dan User Log dicatat pada langkah 12, sebelum pemicu force-logout dan Log Out bersamaan (langkah 15). Entri dicari lewat Note dan email bersuffix `-065` (bukan nama literal), sehingga entri user lain atau run lama yang bernama sama tidak ikut terhitung; asersi langkah 18 dan 19 dibaca sebagai selisih terhadap baseline itu.
- Pencatatan: TC-AUTH-SES-239 Expected d ("tanpa row log tambahan") adalah asersi absence dan ditaruh di spec absence `TC-AUTH-SES-E2E-069-absence-penolakan-force-logout-dan-aksi-admin`; spec ini hanya mengasersi bagian respons idempotent tanpa toast error dan jumlah row yang dicatat (S-05).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): login user uji; memuat sesi web seed (`Siti Ramadhan`, `Andi Wulandari`, `Dewi Hidayat`, tanpa login kedua untuk user yang sama); langkah API pada langkah 23; ganti akun ke Admin License dan Principal; memutus dan memulihkan koneksi SSE; memajukan dan memulihkan jam server dan jam browser/perangkat; membuka Browser C dan mail-catcher; menutup dialog dengan [Cancel] atau [OK]; membuka Concurrent User; Unsuspend Client Suspend (langkah 42); mencatat baseline entri log sebelum pemicu (langkah 12); menutup konteks Browser A dan Browser B sebelumnya sebelum membuka konteks baru (S-09).
- Asersi Body dialog pada langkah 65, 71, dan 80 mengambil teks dari Expected TC-AUTH-SES-8 (Dialog "Log Out" oleh admin), TC-AUTH-SES-46 (Dialog "Session Expired"), dan TC-AUTH-SES-5 (Dialog "Password Changed"); Expected dan Dependensi TC-AUTH-SES-243 hanya menyebut nama dialog (S-03).
- TC-AUTH-SES-239 memicu force-logout dan manual logout lewat UI di dua browser (langkah 13 sampai 15); asersi "tanpa toast error" (langkah 21 dan 22) diamati di Browser A dan Browser Lisensi yang melakukan aksi itu. Pencatatan absence TC-AUTH-SES-239 di spec `TC-AUTH-SES-E2E-069-absence-penolakan-force-logout-dan-aksi-admin` memakai pemicu yang sama.
- Temuan untuk QA: (1) TC-AUTH-SES-241 menulis "Picu dialog push (mis. Log Out)" dan precondition "Lihat TC-AUTH-SES-58 dan TC-AUTH-SES-86" tanpa menentukan satu pemicu; spec memilih Dialog Access Restricted (TC-AUTH-SES-86) dan tidak menyebut form Create yang dipakai di Fixed Asset (TC-AUTH-SES-86 hanya "form Create"), sehingga langkah 34 dan 40 perlu penentuan form oleh QA. (2) TC-AUTH-SES-239 Expected b dan c bercabang menurut pemenang (first-write-wins); spec menuliskannya sebagai dua `Verifikasi` bersyarat hasil (langkah 18 dan 19) karena pemenang tidak dapat ditentukan sebelumnya. (3) TC-AUTH-SES-239 Expected b, c membaca log Client Q2, spec memakai akun aktor Total Control (Global Settings) scope Client Q2 (Tabel Data Uji Pre-setup #26). Akun Admin License (Tabel Data Uji Pre-setup #2) dipakai untuk Client Q2 (TC-AUTH-SES-239, 240) dan Client `Alpha Logistik` (TC-AUTH-SES-243) tanpa pernyataan kepemilikan; perlu konfirmasi akun per Client. (4) TC-AUTH-SES-240 menyebut "seat aktif menjadi 2" tanpa menyebut tempat membacanya; spec membaca di `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset). (5) TC-AUTH-SES-238 menyebut "kirim login ... pada saat yang sama" tanpa menyebut cara memicunya; spec mengklik [Log in] di dua browser dalam selisih kurang dari 1 detik. (6) TC-AUTH-SES-243 menyebut "password diganti" tanpa menyebut sumber perubahan; spec memakai Reset Password dari Browser C yang belum login (aturan `AUTHSES-LOGIC-07d`) karena Change Password dari Browser A tidak meng-invalidate sesi pemicu. (7) TC-AUTH-SES-265 "satu heartbeat atau pemeriksaan status" bercabang pada kalimat "atau"; spec mengasersi bahwa tepat salah satu dari keduanya terpicu pada reconnect.
