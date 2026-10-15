---
id: TC-AUTH-MFA-E2E-053-siklus-trust-pasangan-negara-mfa-ketiga
title: "Siklus Trust Pasangan Negara Setelah MFA Ketiga"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-39
coverage:
  web: automated
---

# Siklus Trust Pasangan Negara Setelah MFA Ketiga

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): satu user berpassword `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi yang di-seed BE: Activated, Active ON, sudah pernah login sukses di web dari browser uji A (ID device browser uji A terdaftar sebagai trusted device web), login terakhir dari IP uji Batam (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar, persetujuan Privacy Policy versi terbaru sudah tersimpan:
  - TC-AUTH-MFA-39: `Taufik Hidayat` (`taufikhidayat+{runId}-053@qwertysystem.net`), profil XC (Tabel Data Uji Pre-setup #9): belum ada hitungan pasangan ID-SG (hitungan awal 0).
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser). TC ini dimulai di browser uji A tanpa sesi login.
- Tidak ada manipulasi jam: TC-AUTH-MFA-39 tidak menguji batas waktu (keempat perpindahan terjadi berurutan dalam satu run, jauh di dalam window 90 hari), sehingga jam server uji dan jam browser tetap waktu nyata.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah IP uji (lokasi koneksi); hook `after` memulihkan IP uji ke nilai semula.
- Hook `after`: kembalikan IP uji ke nilai semula, lalu hapus user. Hook `after` tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Seeding state BE per user: akun Activated, trusted device web ber-ID device browser uji A, lokasi dan waktu login terakhir (Batam (ID)), Authenticator terdaftar, persetujuan Privacy Policy, dan hitungan pasangan negara ID-SG (hitungan awal 0); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Browser uji A: konteks browser dengan cookie ID device persisten yang trusted untuk user TC itu.
  - IP uji: IP sumber permintaan login dapat ditetapkan ke IP uji geo-IP Singapura (SG) dan Batam (ID) (Tabel Data Uji Pre-setup #19); geo-IP service aktif.
  - Mail-catcher lingkungan uji untuk membaca kode OTP faktor-2 dan email alert "New sign-in to your TAG Samurai account", dengan penyaringan per alamat email bersuffix dan subject; jumlah email alert dicatat sebagai baseline sebelum aksi pemicu.
  - reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-MFA-39: Pasangan negara menjadi trusted setelah MFA ketiga berhasil dan perpindahan keempat tidak memicu MFA

1. Atur IP uji ke Singapura (SG); login terakhir `Taufik Hidayat` dari Batam (ID); hitungan awal pasangan ID-SG adalah 0
2. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `taufikhidayat+{runId}-053@qwertysystem.net` (baseline email alert)
3. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
4. Ketik `taufikhidayat+{runId}-053@qwertysystem.net` pada field Email
5. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
6. Centang widget reCAPTCHA "I'm not a robot"
7. Klik button [Log in]
8. Verifikasi Perpindahan ke-1 (Batam ke Singapura): halaman `Auth > MFA > Choose Verification Method` tampil (pasangan belum trusted saat dievaluasi)
9. Periksa mail-catcher lingkungan uji untuk `taufikhidayat+{runId}-053@qwertysystem.net`
10. Verifikasi Email alert ke-1 dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher (jumlah email alert bertambah satu dari baseline langkah 2)
11. Pilih opsi "OTP via email" pada halaman Choose Verification Method
12. Klik button [Login] → halaman OTP Verification tampil
13. Ketik 6 digit kode OTP faktor-2 dari email `taufikhidayat+{runId}-053@qwertysystem.net` pada kotak digit → Portal — Product Hub tampil (perpindahan ke-1 selesai)
14. Logout dari akun `Taufik Hidayat`
15. Atur IP uji ke Batam (ID)
16. Catat jumlah email alert "New sign-in to your TAG Samurai account" di mail-catcher untuk `taufikhidayat+{runId}-053@qwertysystem.net` (baseline email alert ke-2)
17. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
18. Ketik `taufikhidayat+{runId}-053@qwertysystem.net` pada field Email
19. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
20. Centang widget reCAPTCHA "I'm not a robot"
21. Klik button [Log in]
22. Verifikasi Perpindahan ke-2 (Singapura ke Batam): halaman Choose Verification Method tampil (pasangan belum trusted saat dievaluasi)
23. Periksa mail-catcher lingkungan uji untuk `taufikhidayat+{runId}-053@qwertysystem.net`
24. Verifikasi Email alert ke-2 diterima di mail-catcher (jumlah email alert bertambah satu dari baseline langkah 16)
25. Pilih opsi "OTP via email" pada halaman Choose Verification Method
26. Klik button [Login] → halaman OTP Verification tampil
27. Ketik 6 digit kode OTP faktor-2 terbaru dari email `taufikhidayat+{runId}-053@qwertysystem.net` pada kotak digit → Portal — Product Hub tampil (perpindahan ke-2 selesai)
28. Logout dari akun `Taufik Hidayat`
29. Atur IP uji ke Singapura (SG)
30. Catat jumlah email alert "New sign-in to your TAG Samurai account" di mail-catcher untuk `taufikhidayat+{runId}-053@qwertysystem.net` (baseline email alert ke-3)
31. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
32. Ketik `taufikhidayat+{runId}-053@qwertysystem.net` pada field Email
33. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
34. Centang widget reCAPTCHA "I'm not a robot"
35. Klik button [Log in]
36. Verifikasi Perpindahan ke-3 (Batam ke Singapura): halaman Choose Verification Method tampil (pasangan belum trusted saat dievaluasi)
37. Periksa mail-catcher lingkungan uji untuk `taufikhidayat+{runId}-053@qwertysystem.net`
38. Verifikasi Email alert ke-3 diterima di mail-catcher (jumlah email alert bertambah satu dari baseline langkah 30)
39. Pilih opsi "OTP via email" pada halaman Choose Verification Method
40. Klik button [Login] → halaman OTP Verification tampil
41. Ketik 6 digit kode OTP faktor-2 terbaru dari email `taufikhidayat+{runId}-053@qwertysystem.net` pada kotak digit → Portal — Product Hub tampil (perpindahan ke-3 selesai)
42. Logout dari akun `Taufik Hidayat`
43. Atur IP uji ke Batam (ID)
44. Catat jumlah email alert "New sign-in to your TAG Samurai account" di mail-catcher untuk `taufikhidayat+{runId}-053@qwertysystem.net` (baseline email alert perpindahan ke-4)
45. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
46. Ketik `taufikhidayat+{runId}-053@qwertysystem.net` pada field Email
47. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
48. Centang widget reCAPTCHA "I'm not a robot"
49. Klik button [Log in]
50. Amati halaman setelah klik [Log in]
51. Verifikasi Perpindahan ke-4 (Singapura ke Batam): halaman MFA tidak tampil (pasangan ID-SG trusted; urutan arah tidak berpengaruh)
52. Verifikasi Browser dialihkan ke Portal — Product Hub
53. Periksa mail-catcher lingkungan uji untuk `taufikhidayat+{runId}-053@qwertysystem.net`
54. Verifikasi Tidak ada email alert baru di mail-catcher (jumlah email alert sama dengan baseline langkah 44)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembagian TC lintas spec: TC-AUTH-MFA-39 ada di spec ini (tidak menguji batas waktu, sehingga tidak butuh pembekuan jam), TC-AUTH-MFA-40 dan TC-AUTH-MFA-215 di spec `TC-AUTH-MFA-E2E-054-window-90-hari-pasangan-negara`, TC-AUTH-MFA-41, TC-AUTH-MFA-216, TC-AUTH-MFA-42, TC-AUTH-MFA-43, dan TC-AUTH-MFA-44 di spec `TC-AUTH-MFA-E2E-025-decay-dan-refresh-trust-pasangan-negara`.
- Langkah penghubung tanpa awalan `Verifikasi` (atur IP uji, logout, catat baseline email alert) bukan asersi tambahan (S-03). Langkah 14 sampai 16, 28 sampai 30, dan 42 sampai 44 menjabarkan "logout, ubah IP uji, login ulang" pada Langkah Uji 8 sampai 10 TC-AUTH-MFA-39.
- Login ulang pada Langkah Uji 8 dan 9 TC-AUTH-MFA-39 ("selesaikan MFA OTP") dijabarkan memakai langkah yang sama dengan Langkah Uji 6 dan 7 (pilih "OTP via email", klik [Login], ketik kode OTP faktor-2 terbaru).
- Temuan untuk QA: (1) TC-AUTH-MFA-39 Expected butir a menyebut email alert diterima pada tiap perpindahan, tetapi Langkah Uji tidak memuat pemeriksaan mail-catcher; spec menambah langkah periksa mail-catcher dengan baseline jumlah email alert (S-12). (2) Post Condition TC-AUTH-MFA-39 "Pasangan negara ID-SG berstatus trusted untuk `Taufik Hidayat`; hitungan 3 dalam window 90 hari" tidak punya langkah observasi di TC; status trusted teramati lewat Expected butir b (perpindahan ke-4 tanpa MFA), sedangkan hitungan 3 dan window 90 hari tidak diasersi. (3) Mekanisme seeding state BE per user (trusted device ber-ID device browser uji A, lokasi dan waktu login terakhir, Authenticator terdaftar, persetujuan Privacy Policy, hitungan pasangan negara) belum ada di Tabel Data Uji Pre-setup (#20/#21) dan tidak didefinisikan di TC, PRD, atau LLD; tim FE/BE perlu menyediakannya.
