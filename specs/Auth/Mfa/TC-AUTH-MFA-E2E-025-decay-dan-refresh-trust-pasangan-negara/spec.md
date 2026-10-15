---
id: TC-AUTH-MFA-E2E-025-decay-dan-refresh-trust-pasangan-negara
title: "Decay 180 Hari dan Refresh Trust Pasangan Negara"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-41
  - TC-AUTH-MFA-216
  - TC-AUTH-MFA-42
  - TC-AUTH-MFA-43
  - TC-AUTH-MFA-44
coverage:
  web: automated
---

# Decay 180 Hari dan Refresh Trust Pasangan Negara

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user berpassword `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi yang di-seed BE untuk semua user: Activated, Active ON, sudah pernah login sukses di web dari browser uji A (ID device browser uji A terdaftar sebagai trusted device web), login terakhir dari IP uji Batam (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar, persetujuan Privacy Policy versi terbaru sudah tersimpan. Waktu pada data pasangan negara ID-SG di-seed relatif terhadap T0, yaitu waktu jam server uji saat dibekukan di hook `before`:
  - TC-AUTH-MFA-41: `Reza Alamsyah` (`rezaalamsyah+{runId}-025@qwertysystem.net`), profil XCT (Tabel Data Uji Pre-setup #10): pasangan ID-SG trusted, waktu terakhir terlihat T0 - 181 hari.
  - TC-AUTH-MFA-216: `Gita Permata` (`gitapermata+{runId}-025@qwertysystem.net`), profil XCT: pasangan ID-SG trusted, waktu terakhir terlihat tepat T0 - 180 hari.
  - TC-AUTH-MFA-42: `Lia Wulandari` (`liawulandari+{runId}-025@qwertysystem.net`), profil XCT: pasangan ID-SG trusted, waktu terakhir terlihat T0 - 179 hari.
  - TC-AUTH-MFA-43: `Hari Purnomo` (`haripurnomo+{runId}-025@qwertysystem.net`), profil XCT: pasangan ID-SG trusted, window dimulai T0 - 100 hari, waktu terakhir terlihat T0 - 20 hari.
  - TC-AUTH-MFA-44: `Vina Melati` (`vinamelati+{runId}-025@qwertysystem.net`), profil XCT: pasangan ID-SG trusted, waktu terakhir terlihat T0 - 170 hari.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela baru browser uji A tanpa sesi login.
- Manipulasi jam: hook `before` membekukan jam server uji pada T0 sebelum seeding, sehingga usia data pasangan negara tidak bergeser selama spec berjalan dan batas tepat 180 hari pada TC-AUTH-MFA-216 deterministik. Pembekuan hanya di hook dan tidak diulang per TC. TC-AUTH-MFA-44 mengatur jam server uji secara absolut ke T0 + 20 hari (tetap beku), lalu memulihkannya dengan langkah di akhir TC itu. Jam browser/klien tidak diubah: decay 180 hari dan waktu terakhir terlihat dihitung murni di server dan tidak diamati lewat countdown UI, sehingga jam server saja yang diatur.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji dan IP uji (lokasi koneksi); hook `after` memulihkan jam server uji dan IP uji.
- Hook `after`: lepaskan pembekuan dan kembalikan jam server uji ke waktu nyata, kembalikan IP uji ke nilai semula, lalu hapus kelima user. Hook `after` tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Manipulasi jam server uji (bekukan di T0, atur absolut ke T0 + 20 hari pada TC-AUTH-MFA-44, lepaskan) serta seeding awal window dan waktu terakhir terlihat pasangan negara per user.
  - Seeding state BE per user: akun Activated, trusted device web ber-ID device browser uji A, lokasi dan waktu login terakhir (Batam (ID)), Authenticator terdaftar, persetujuan Privacy Policy, dan data pasangan negara ID-SG (status trusted, awal window, waktu terakhir terlihat); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Browser uji A: konteks browser dengan cookie ID device persisten yang trusted untuk user TC itu; setiap TC memakai konteks baru.
  - IP uji: IP sumber permintaan login dapat ditetapkan ke IP uji geo-IP Singapura (SG) dan Batam (ID) (Tabel Data Uji Pre-setup #19); geo-IP service aktif.
  - Mail-catcher lingkungan uji untuk membaca kode OTP faktor-2 dan email alert "New sign-in to your TAG Samurai account", dengan penyaringan per alamat email bersuffix dan subject; jumlah email alert dicatat sebagai baseline sebelum aksi pemicu.
  - reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-MFA-41: Trust pasangan negara gugur bila tidak terlihat lebih dari 180 hari dan hitungan dimulai ulang dari 1

1. Atur IP uji ke Singapura (SG); login terakhir `Reza Alamsyah` dari Batam (ID)
2. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `rezaalamsyah+{runId}-025@qwertysystem.net` (baseline email alert)
3. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
4. Ketik `rezaalamsyah+{runId}-025@qwertysystem.net` pada field Email
5. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
6. Centang widget reCAPTCHA "I'm not a robot"
7. Klik button [Log in]
8. Amati halaman setelah klik [Log in]
9. Verifikasi Halaman Choose Verification Method tampil (trust gugur karena pasangan terakhir terlihat 181 hari yang lalu)
10. Periksa mail-catcher lingkungan uji untuk `rezaalamsyah+{runId}-025@qwertysystem.net`
11. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `rezaalamsyah+{runId}-025@qwertysystem.net` (jumlah email alert bertambah satu dari baseline langkah 2)
12. Pilih opsi "OTP via email" pada halaman Choose Verification Method
13. Klik button [Login] → halaman OTP Verification tampil
14. Ketik 6 digit kode OTP faktor-2 dari email `rezaalamsyah+{runId}-025@qwertysystem.net` pada kotak digit → login selesai di Portal — Product Hub
15. Logout dari akun `Reza Alamsyah`
16. Atur IP uji ke Batam (ID)
17. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
18. Ketik `rezaalamsyah+{runId}-025@qwertysystem.net` pada field Email
19. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
20. Centang widget reCAPTCHA "I'm not a robot"
21. Klik button [Log in]
22. Amati halaman setelah klik [Log in]
23. Verifikasi Halaman Choose Verification Method tampil lagi (hitungan dimulai ulang dari 1 dan window 90 hari baru; perpindahan ini baru ke-2)

### TC-AUTH-MFA-216: Trust pasangan negara yang terakhir terlihat tepat 180 hari lalu masih berlaku (decay hanya bila lebih dari 180 hari)

24. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
25. Atur IP uji ke Singapura (SG); login terakhir `Gita Permata` dari Batam (ID)
26. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `gitapermata+{runId}-025@qwertysystem.net` (baseline email alert)
27. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
28. Ketik `gitapermata+{runId}-025@qwertysystem.net` pada field Email
29. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
30. Centang widget reCAPTCHA "I'm not a robot"
31. Klik button [Log in]
32. Amati halaman setelah klik [Log in]
33. Verifikasi Halaman MFA tidak tampil
34. Verifikasi Browser dialihkan ke Portal — Product Hub
35. Periksa mail-catcher lingkungan uji untuk `gitapermata+{runId}-025@qwertysystem.net`
36. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" baru di mail-catcher untuk `gitapermata+{runId}-025@qwertysystem.net` (jumlah email alert sama dengan baseline langkah 26)

### TC-AUTH-MFA-42: Trust pasangan negara yang terakhir terlihat 179 hari lalu masih berlaku

37. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
38. Atur IP uji ke Singapura (SG); login terakhir `Lia Wulandari` dari Batam (ID)
39. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `liawulandari+{runId}-025@qwertysystem.net` (baseline email alert)
40. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
41. Ketik `liawulandari+{runId}-025@qwertysystem.net` pada field Email
42. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
43. Centang widget reCAPTCHA "I'm not a robot"
44. Klik button [Log in]
45. Amati halaman setelah klik [Log in]
46. Verifikasi Halaman MFA tidak tampil
47. Verifikasi Browser dialihkan ke Portal — Product Hub
48. Periksa mail-catcher lingkungan uji untuk `liawulandari+{runId}-025@qwertysystem.net`
49. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" baru di mail-catcher untuk `liawulandari+{runId}-025@qwertysystem.net` (jumlah email alert sama dengan baseline langkah 39)

### TC-AUTH-MFA-43: Reset window 90 hari tidak mencabut status trusted pasangan negara

50. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
51. Atur IP uji ke Singapura (SG); login terakhir `Hari Purnomo` dari Batam (ID)
52. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `haripurnomo+{runId}-025@qwertysystem.net` (baseline email alert)
53. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
54. Ketik `haripurnomo+{runId}-025@qwertysystem.net` pada field Email
55. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
56. Centang widget reCAPTCHA "I'm not a robot"
57. Klik button [Log in]
58. Amati halaman setelah klik [Log in]
59. Verifikasi Halaman MFA tidak tampil
60. Verifikasi Browser dialihkan ke Portal — Product Hub
61. Periksa mail-catcher lingkungan uji untuk `haripurnomo+{runId}-025@qwertysystem.net`
62. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" baru di mail-catcher untuk `haripurnomo+{runId}-025@qwertysystem.net` (jumlah email alert sama dengan baseline langkah 52)

### TC-AUTH-MFA-44: Login single-step dari pasangan trusted memperbarui waktu terakhir terlihat sehingga trust tidak gugur

63. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
64. Atur IP uji ke Singapura (SG); login terakhir `Vina Melati` dari Batam (ID)
65. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
66. Ketik `vinamelati+{runId}-025@qwertysystem.net` pada field Email
67. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
68. Centang widget reCAPTCHA "I'm not a robot"
69. Klik button [Log in]
70. Amati halaman setelah klik [Log in]
71. Verifikasi Halaman MFA tidak tampil
72. Verifikasi Portal — Product Hub tampil (pasangan trusted; login single-step)
73. Logout dari akun `Vina Melati`
74. Atur jam server uji ke T0 + 20 hari (absolut, tetap beku; total 190 hari sejak waktu terakhir terlihat seed awal)
75. Atur IP uji ke Batam (ID)
76. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
77. Ketik `vinamelati+{runId}-025@qwertysystem.net` pada field Email
78. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
79. Centang widget reCAPTCHA "I'm not a robot"
80. Klik button [Log in]
81. Amati halaman setelah klik [Log in]
82. Verifikasi Halaman MFA tidak tampil
83. Verifikasi Portal — Product Hub tampil (login single-step pada langkah 69 memperbarui waktu terakhir terlihat pasangan ID-SG sehingga trust tidak gugur)
84. Pulihkan jam server uji ke waktu nyata dan lepaskan pembekuan

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness d (time-travel / manipulasi jam server): decay 180 hari adalah batas waktu yang diuji. Jam server uji dibekukan di T0 oleh hook `before` supaya batas tepat 180 hari (TC-AUTH-MFA-216) deterministik; semua seed dihitung relatif terhadap T0.
- Penyimpangan urutan (S-05): urutan di spec ini TC-AUTH-MFA-41, TC-AUTH-MFA-216, TC-AUTH-MFA-42, TC-AUTH-MFA-43, TC-AUTH-MFA-44, berbeda dari urutan TC sumber. TC-AUTH-MFA-216 ditaruh tepat setelah TC-AUTH-MFA-41 supaya kedua batas decay (181 hari gugur, tepat 180 hari berlaku) berurutan. TC-AUTH-MFA-44 ditaruh paling akhir karena mengatur jam server uji ke T0 + 20 hari (langkah 74); TC lain bergantung pada jam beku di T0 untuk usia data yang tepat. Langkah 84 dan hook `after` memulihkan jam server uji.
- Pembagian TC lintas spec: TC-AUTH-MFA-39 di spec `TC-AUTH-MFA-E2E-053-siklus-trust-pasangan-negara-mfa-ketiga` (tanpa batas waktu); TC-AUTH-MFA-40 dan TC-AUTH-MFA-215 (window 90 hari) di spec `TC-AUTH-MFA-E2E-054-window-90-hari-pasangan-negara`. Spec ini memuat TC-AUTH-MFA-41, TC-AUTH-MFA-216, TC-AUTH-MFA-42, TC-AUTH-MFA-43, dan TC-AUTH-MFA-44.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru browser uji A, atur jam server uji dan IP uji, catat baseline email alert, logout, pulihkan jam) bukan asersi tambahan (S-03).
- Batas ukuran: jumlah langkah melewati ±35 karena lima TC independen dengan prefix login faktor-1 yang identik (tidak dihitung ke ±35) dan login berulang pada TC-AUTH-MFA-41 dan TC-AUTH-MFA-44. Tiap TC memakai user dan jendela sendiri, sehingga tidak ada data yang dipakai bersama; bagian sesudah tetap bermakna bila bagian sebelumnya gagal, jadi spec tidak dipecah lagi.
- Temuan untuk QA: (1) TC-AUTH-MFA-41 Expected butir a (email alert diterima) tidak punya langkah periksa mail-catcher di Langkah Uji; spec menambah langkah 10 dan 11 dengan baseline jumlah email alert (S-12). (2) TC-AUTH-MFA-41 tidak menyebut IP uji untuk login pertama; spec memakai Singapura (SG) sesuai profil XCT (login terakhir Batam (ID)) dan Langkah Uji yang menyebut perpindahan Batam ke Singapura. (3) Post Condition tanpa langkah observasi di TC tidak diasersi: TC-AUTH-MFA-41 "Pasangan ID-SG milik `Reza Alamsyah` berstatus belum trusted dengan hitungan 2" (status belum trusted teramati lewat Expected butir b, nilai hitungan 2 tidak diasersi); TC-AUTH-MFA-42 "Satu sesi web aktif untuk `Lia Wulandari`" (teramati sebagai Portal — Product Hub tampil); TC-AUTH-MFA-43 "Pasangan ID-SG milik `Hari Purnomo` tetap trusted; waktu terakhir terlihat diperbarui" (trusted teramati lewat Expected butir a, pembaruan waktu terakhir terlihat tidak diasersi); TC-AUTH-MFA-216 "Satu sesi web aktif untuk `Gita Permata`; pasangan ID-SG tetap trusted" (teramati lewat Expected butir a dan Portal — Product Hub tampil); TC-AUTH-MFA-44 "Pasangan ID-SG milik `Vina Melati` tetap trusted dengan waktu terakhir terlihat diperbarui" (teramati lewat Expected butir b). (4) Mekanisme seeding state BE per user (trusted device ber-ID device browser uji A, lokasi dan waktu login terakhir, Authenticator terdaftar, persetujuan Privacy Policy, data pasangan negara) belum ada di Tabel Data Uji Pre-setup (#20/#21) dan tidak didefinisikan di TC, PRD, atau LLD; tim FE/BE perlu menyediakannya.
