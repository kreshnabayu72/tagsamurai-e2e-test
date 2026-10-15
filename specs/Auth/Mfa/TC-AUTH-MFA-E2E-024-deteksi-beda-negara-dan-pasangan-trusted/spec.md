---
id: TC-AUTH-MFA-E2E-024-deteksi-beda-negara-dan-pasangan-trusted
title: "Deteksi Beda Negara dan Pasangan Trusted"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-35
  - TC-AUTH-MFA-36
  - TC-AUTH-MFA-37
coverage:
  web: automated
---

# Deteksi Beda Negara dan Pasangan Trusted

## Prerequisites

- Mode: FE+BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah IP uji (lokasi koneksi login ditetapkan ke Singapura (SG)); hook `after` memulihkan IP uji ke IP default lingkungan uji.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user berpassword `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi yang di-seed BE untuk semua user: Activated, Active ON, logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar, persetujuan Privacy Policy versi terbaru sudah tersimpan, login terakhir dari IP uji Batam (ID):
  - TC-AUTH-MFA-35: `Irfan Maulana` (`irfanmaulana+{runId}-024@qwertysystem.net`), profil XC (Tabel Data Uji Pre-setup #9): ID device browser uji A trusted; pasangan negara ID-SG belum trusted (hitungan kurang dari 3).
  - TC-AUTH-MFA-36: `Sekar Ayu` (`sekarayu+{runId}-024@qwertysystem.net`), profil XCT (Tabel Data Uji Pre-setup #10): ID device browser uji A trusted; pasangan negara ID-SG sudah trusted (hitungan 3 dalam window 90 hari, terakhir terlihat kurang dari 180 hari).
  - TC-AUTH-MFA-37: `Yoga Pranata` (`yogapranata+{runId}-024@qwertysystem.net`), profil XCT: pasangan negara ID-SG sudah trusted seperti `Sekar Ayu`; ID device browser uji B tidak ada di daftar trusted device.
- Hook `after`: kembalikan IP uji ke IP default lingkungan uji, lalu hapus ketiga user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela baru browser uji tanpa sesi login; TC pertama berjalan di browser awal.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Seeding state BE per user: trusted device (ID device browser uji A trusted untuk TC-AUTH-MFA-35 dan 36; ID device browser uji B tidak terdaftar untuk TC-AUTH-MFA-37), lokasi dan waktu login terakhir (Batam (ID)), hitungan pasangan negara ID-SG (kurang dari 3 untuk `Irfan Maulana`; 3 dalam window 90 hari, terakhir terlihat kurang dari 180 hari untuk `Sekar Ayu` dan `Yoga Pranata`), `last_logout_at` kurang dari 30 hari, Authenticator terdaftar, dan persetujuan Privacy Policy; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Browser uji A (ID device trusted untuk user TC itu) dan browser uji B (ID device belum dikenali): konteks browser dengan cookie ID device persisten; setiap TC memakai konteks baru.
  - IP uji: IP sumber permintaan login dapat ditetapkan ke IP uji geo-IP Singapura (SG) (Tabel Data Uji Pre-setup #19); geo-IP service aktif.
  - Mail-catcher lingkungan uji untuk membaca email alert "New sign-in to your TAG Samurai account". Asersi email memakai baseline jumlah email alert untuk alamat user yang dicatat sebelum login.
  - reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-MFA-35: Login dari negara berbeda walau jarak kurang dari 100 km memicu MFA dan email alert

1. Atur IP uji ke Singapura (SG); login terakhir `Irfan Maulana` dari Batam (ID), jarak kurang dari 100 km
2. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `irfanmaulana+{runId}-024@qwertysystem.net` sebagai baseline
3. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
4. Ketik `irfanmaulana+{runId}-024@qwertysystem.net` pada field Email
5. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
6. Centang widget reCAPTCHA "I'm not a robot"
7. Klik button [Log in]
8. Amati halaman setelah klik [Log in]
9. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib karena beda negara; pasangan ID-SG belum trusted)
10. Periksa mail-catcher lingkungan uji untuk `irfanmaulana+{runId}-024@qwertysystem.net`
11. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `irfanmaulana+{runId}-024@qwertysystem.net` (jumlah bertambah dibanding baseline langkah 2)

### TC-AUTH-MFA-36: Beda negara pada pasangan negara trusted tidak memicu MFA dan tidak mengirim email alert

12. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
13. Atur IP uji ke Singapura (SG); login terakhir `Sekar Ayu` dari Batam (ID)
14. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `sekarayu+{runId}-024@qwertysystem.net` sebagai baseline
15. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
16. Ketik `sekarayu+{runId}-024@qwertysystem.net` pada field Email
17. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
18. Centang widget reCAPTCHA "I'm not a robot"
19. Klik button [Log in]
20. Amati halaman setelah klik [Log in]
21. Verifikasi Halaman MFA tidak tampil
22. Verifikasi Browser dialihkan ke Portal — Product Hub
23. Periksa mail-catcher lingkungan uji untuk `sekarayu+{runId}-024@qwertysystem.net`
24. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" di mail-catcher untuk `sekarayu+{runId}-024@qwertysystem.net` (jumlah sama dengan baseline langkah 14)

### TC-AUTH-MFA-37: Pasangan negara trusted tidak membebaskan device baru dari MFA dan email alert

25. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji B (konteks bersih tanpa sesi login; ID device belum dikenali)
26. Atur IP uji ke Singapura (SG); login terakhir `Yoga Pranata` dari Batam (ID)
27. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `yogapranata+{runId}-024@qwertysystem.net` sebagai baseline
28. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
29. Ketik `yogapranata+{runId}-024@qwertysystem.net` pada field Email
30. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
31. Centang widget reCAPTCHA "I'm not a robot"
32. Klik button [Log in]
33. Amati halaman setelah klik [Log in]
34. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib karena device baru walau pasangan negara trusted)
35. Periksa mail-catcher lingkungan uji untuk `yogapranata+{runId}-024@qwertysystem.net`
36. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `yogapranata+{runId}-024@qwertysystem.net` (jumlah bertambah dibanding baseline langkah 27)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru browser uji, atur IP uji, catat baseline email) bukan asersi tambahan (S-03). Langkah 2, 14, dan 27 mencatat baseline jumlah email alert (S-12) supaya "email alert diterima" diasersi sebagai bertambah dan "tidak ada email alert" sebagai tidak bertambah.
- Urutan TC mengikuti TC sumber; TC-AUTH-MFA-37 ditaruh terakhir karena memakai browser uji B (S-10).
- Sesi teramati lewat halaman yang tampil: sesi pre-auth MFA = halaman Choose Verification Method tampil; sesi web aktif = Portal — Product Hub tampil. Post Condition sesi tidak diasersi terpisah.
- Temuan untuk QA:
  1. TC-AUTH-MFA-35 sampai 37 tidak menyatakan nilai hitungan pasangan negara dan waktu terakhir terlihat setelah login (Post Condition hanya sesi); perubahan hitungan atau waktu terlihat tidak diasersi di spec ini.
  2. TC-AUTH-MFA-35 sampai 37 tidak menyatakan layar Confirm to Continue pada login; spec mengikuti Expected (profil XC/XCT sudah pernah login sehingga persetujuan sudah tersimpan).
  3. Post Condition berupa state BE tidak diasersi (S-01, S-15): TC-AUTH-MFA-35 dan 37 "Sesi pre-auth MFA aktif untuk <user>" (teramati lewat halaman Choose Verification Method tampil pada Expected) dan TC-AUTH-MFA-36 "Satu sesi web aktif untuk `Sekar Ayu`; tidak ada sesi pre-auth MFA" (teramati lewat halaman MFA tidak tampil dan Portal tampil pada Expected). QA menambah Expected atau langkah observasi di TC bila ada yang harus diuji lebih jauh.
  4. Mekanisme seeding state BE (trusted device per ID device browser A/B, lokasi dan waktu login terakhir, hitungan pasangan negara dan waktu terakhir terlihat, consent) belum ada di Tabel Data Uji Pre-setup (#20 dan #21 hanya memuat manipulasi jam server, seed `last_logout_at`, pasangan negara, `first_login_at`, dan failure injection); tim FE/BE menyediakan dan QA melengkapi Pre-setup.
