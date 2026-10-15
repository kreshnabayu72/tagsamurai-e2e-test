---
id: TC-AUTH-MFA-E2E-054-window-90-hari-pasangan-negara
title: "Window 90 Hari Pasangan Negara"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-40
  - TC-AUTH-MFA-215
coverage:
  web: automated
---

# Window 90 Hari Pasangan Negara

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user berpassword `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi yang di-seed BE untuk semua user: Activated, Active ON, sudah pernah login sukses di web dari browser uji A (ID device browser uji A terdaftar sebagai trusted device web), login terakhir dari IP uji Batam (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar, persetujuan Privacy Policy versi terbaru sudah tersimpan. Waktu pada data pasangan negara ID-SG di-seed relatif terhadap T0, yaitu waktu jam server uji saat dibekukan di hook `before`:
  - TC-AUTH-MFA-40: `Anisa Fitriani` (`anisafitriani+{runId}-054@qwertysystem.net`), profil XC (Tabel Data Uji Pre-setup #9): pasangan ID-SG tersimpan dengan hitungan 2 dan window dimulai T0 - 91 hari.
  - TC-AUTH-MFA-215: `Fikri Hamdani` (`fikrihamdani+{runId}-054@qwertysystem.net`), profil XC: pasangan ID-SG tersimpan dengan hitungan 2 dan window dimulai tepat T0 - 90 hari.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela baru browser uji A tanpa sesi login; TC pertama berjalan di browser awal.
- Manipulasi jam: hook `before` membekukan jam server uji pada T0 sebelum seeding, sehingga usia window tidak bergeser selama spec berjalan dan batas tepat 90 hari pada TC-AUTH-MFA-215 deterministik. Pembekuan hanya di hook dan tidak diulang per TC. Jam browser/klien tidak diubah: window 90 hari dihitung murni di server dan tidak diamati lewat countdown UI, sehingga jam server saja yang diatur.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji dan IP uji (lokasi koneksi); hook `after` memulihkan jam server uji dan IP uji.
- Hook `after`: lepaskan pembekuan dan kembalikan jam server uji ke waktu nyata, kembalikan IP uji ke nilai semula, lalu hapus kedua user. Hook `after` tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Manipulasi jam server uji (bekukan di T0, lepaskan) serta seeding hitungan, awal window, dan waktu terakhir terlihat pasangan negara per user.
  - Seeding state BE per user: akun Activated, trusted device web ber-ID device browser uji A, lokasi dan waktu login terakhir (Batam (ID)), Authenticator terdaftar, persetujuan Privacy Policy, dan data pasangan negara ID-SG (hitungan dan awal window); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Browser uji A: konteks browser dengan cookie ID device persisten yang trusted untuk user TC itu; setiap TC memakai konteks baru.
  - IP uji: IP sumber permintaan login dapat ditetapkan ke IP uji geo-IP Singapura (SG) dan Batam (ID) (Tabel Data Uji Pre-setup #19); geo-IP service aktif.
  - Mail-catcher lingkungan uji untuk membaca kode OTP faktor-2 dan email alert "New sign-in to your TAG Samurai account", dengan penyaringan per alamat email bersuffix dan subject; jumlah email alert dicatat sebagai baseline sebelum aksi pemicu.
  - reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-MFA-40: Window 90 hari bersifat tumbling: hitungan pasangan di-reset ke 1 saat window berumur lebih dari 90 hari

1. Atur IP uji ke Singapura (SG); login terakhir `Anisa Fitriani` dari Batam (ID)
2. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
3. Ketik `anisafitriani+{runId}-054@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in]
7. Verifikasi Perpindahan pertama (Batam ke Singapura): halaman `Auth > MFA > Choose Verification Method` tampil (hitungan tersimpan 2 di window berumur 91 hari; pasangan belum trusted)
8. Pilih opsi "OTP via email" pada halaman Choose Verification Method
9. Klik button [Login] → halaman OTP Verification tampil
10. Ketik 6 digit kode OTP faktor-2 dari email `anisafitriani+{runId}-054@qwertysystem.net` pada kotak digit → Portal — Product Hub tampil (perpindahan pertama selesai)
11. Logout dari akun `Anisa Fitriani`
12. Atur IP uji ke Batam (ID)
13. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
14. Ketik `anisafitriani+{runId}-054@qwertysystem.net` pada field Email
15. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
16. Centang widget reCAPTCHA "I'm not a robot"
17. Klik button [Log in]
18. Amati halaman setelah klik [Log in]
19. Verifikasi Perpindahan berikutnya (Singapura ke Batam): halaman Choose Verification Method tampil lagi (hitungan baru 1 sehingga perpindahan ini baru ke-2, pasangan belum trusted)
20. Verifikasi Setelah MFA sukses pada perpindahan pertama, hitungan pasangan ID-SG menjadi 1 dengan window baru (teramati lewat Verifikasi langkah 19: bila window tidak di-reset, hitungan menjadi 3 dan pasangan trusted sehingga MFA tidak tampil)

### TC-AUTH-MFA-215: Window 90 hari yang berumur tepat 90 hari tidak di-reset sehingga hitungan menjadi 3 dan pasangan negara trusted

21. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
22. Atur IP uji ke Singapura (SG); login terakhir `Fikri Hamdani` dari Batam (ID)
23. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `fikrihamdani+{runId}-054@qwertysystem.net` (baseline email alert)
24. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
25. Ketik `fikrihamdani+{runId}-054@qwertysystem.net` pada field Email
26. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
27. Centang widget reCAPTCHA "I'm not a robot"
28. Klik button [Log in]
29. Verifikasi Halaman Choose Verification Method tampil (hitungan 2, pasangan belum trusted; window berumur tepat 90 hari tidak di-reset karena reset hanya bila lebih dari 90 hari)
30. Periksa mail-catcher lingkungan uji untuk `fikrihamdani+{runId}-054@qwertysystem.net`
31. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `fikrihamdani+{runId}-054@qwertysystem.net` (jumlah email alert bertambah satu dari baseline langkah 23)
32. Pilih opsi "OTP via email" pada halaman Choose Verification Method
33. Klik button [Login] → halaman OTP Verification tampil
34. Ketik 6 digit kode OTP faktor-2 dari email `fikrihamdani+{runId}-054@qwertysystem.net` pada kotak digit → perpindahan (Batam ke Singapura) selesai di Portal — Product Hub
35. Logout dari akun `Fikri Hamdani`
36. Atur IP uji ke Batam (ID)
37. Catat jumlah email alert "New sign-in to your TAG Samurai account" di mail-catcher untuk `fikrihamdani+{runId}-054@qwertysystem.net` (baseline email alert perpindahan kedua)
38. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
39. Ketik `fikrihamdani+{runId}-054@qwertysystem.net` pada field Email
40. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
41. Centang widget reCAPTCHA "I'm not a robot"
42. Klik button [Log in]
43. Amati halaman setelah klik [Log in]
44. Verifikasi Halaman MFA tidak tampil (hitungan menjadi 3 setelah MFA sukses sehingga pasangan ID-SG trusted; bila window ter-reset hitungan hanya 1 dan MFA akan tampil lagi)
45. Verifikasi Browser dialihkan ke Portal — Product Hub
46. Periksa mail-catcher lingkungan uji untuk `fikrihamdani+{runId}-054@qwertysystem.net`
47. Verifikasi Tidak ada email alert baru di mail-catcher (jumlah email alert sama dengan baseline langkah 37)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness d (time-travel / manipulasi jam server): window 90 hari adalah batas waktu yang diuji. Jam server uji dibekukan di T0 oleh hook `before` supaya batas tepat 90 hari (TC-AUTH-MFA-215) deterministik; semua seed dihitung relatif terhadap T0.
- Pembagian TC lintas spec: TC-AUTH-MFA-39 di spec `TC-AUTH-MFA-E2E-053-siklus-trust-pasangan-negara-mfa-ketiga` (tanpa batas waktu); TC-AUTH-MFA-41, TC-AUTH-MFA-216, TC-AUTH-MFA-42, TC-AUTH-MFA-43, dan TC-AUTH-MFA-44 (decay 180 hari) di spec `TC-AUTH-MFA-E2E-025-decay-dan-refresh-trust-pasangan-negara`. Spec ini memuat TC-AUTH-MFA-40 dan TC-AUTH-MFA-215.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru browser uji A, atur IP uji, logout, catat baseline email alert) bukan asersi tambahan (S-03).
- Temuan untuk QA: (1) TC-AUTH-MFA-40 Expected butir a menyebut "setelah MFA sukses hitungan menjadi 1 dengan window baru", tetapi Post Condition menyebut hitungan bernilai 2 setelah perpindahan berikutnya; spec mengasersi butir a lewat efeknya pada perpindahan berikutnya (Verifikasi langkah 19 dan 20). (2) TC-AUTH-MFA-215 Expected butir a (email alert diterima setelah langkah 5) hanya punya pemeriksaan mail-catcher pada langkah 8 setelah login kedua; spec memeriksa mail-catcher segera setelah login pertama dan sekali lagi sesudah login kedua, masing-masing dengan baseline jumlah email alert. (3) TC-AUTH-MFA-40 tidak menyebut IP uji untuk login pertama; spec memakai Singapura (SG) sesuai profil XC (login terakhir Batam (ID)) dan Langkah Uji yang menyebut perpindahan Batam ke Singapura. (4) Post Condition tanpa langkah observasi di TC tidak diasersi: TC-AUTH-MFA-40 "Hitungan pasangan ID-SG untuk `Anisa Fitriani` bernilai 2 dengan window yang dimulai pada perpindahan pertama setelah reset"; TC-AUTH-MFA-215 "Pasangan ID-SG milik `Fikri Hamdani` trusted dengan hitungan 3" (status trusted teramati lewat Expected butir b, nilai hitungan 3 tidak diasersi). (5) Mekanisme seeding state BE per user (trusted device ber-ID device browser uji A, lokasi dan waktu login terakhir, Authenticator terdaftar, persetujuan Privacy Policy, hitungan dan awal window pasangan negara) belum ada di Tabel Data Uji Pre-setup (#20/#21) dan tidak didefinisikan di TC, PRD, atau LLD; tim FE/BE perlu menyediakannya.
