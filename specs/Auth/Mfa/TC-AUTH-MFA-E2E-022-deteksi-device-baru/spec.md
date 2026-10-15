---
id: TC-AUTH-MFA-E2E-022-deteksi-device-baru
title: "Deteksi Device Baru"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-30
  - TC-AUTH-MFA-31
  - TC-AUTH-MFA-50
coverage:
  web: automated
---

# Deteksi Device Baru

## Prerequisites

- Mode: FE+BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah IP uji (lokasi koneksi login ditetapkan ke Jakarta (ID)); hook `after` memulihkan IP uji ke IP default lingkungan uji.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user berpassword `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi yang di-seed BE untuk semua user: Activated, Active ON, sudah pernah login sukses di web dari browser uji A, login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar, persetujuan Privacy Policy versi terbaru sudah tersimpan:
  - TC-AUTH-MFA-30: `Citra Dewanti` (`citradewanti+{runId}-022@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5); ID device browser uji B tidak ada di daftar trusted device.
  - TC-AUTH-MFA-31: `Wawan Kurniawan` (`wawankurniawan+{runId}-022@qwertysystem.net`), profil BASE (Tabel Data Uji Pre-setup #2); ID device browser uji A trusted.
  - TC-AUTH-MFA-50: `Eko Rahmawati` (`ekorahmawati+{runId}-022@qwertysystem.net`), profil BASE; ID device browser uji A trusted.
- Hook `after`: kembalikan IP uji ke IP default lingkungan uji, lalu hapus ketiga user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela baru browser uji tanpa sesi login; TC pertama berjalan di browser awal.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Seeding state BE per user: trusted device (ID device browser uji A trusted untuk TC-AUTH-MFA-31 dan 50; ID device browser uji B tidak terdaftar untuk TC-AUTH-MFA-30), lokasi dan waktu login terakhir (Jakarta (ID)), `last_logout_at` kurang dari 30 hari, Authenticator terdaftar, dan persetujuan Privacy Policy; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Browser uji A (ID device terdaftar trusted untuk user TC itu) dan browser uji B (ID device belum dikenali): konteks browser dengan cookie ID device persisten; setiap TC memakai konteks baru sehingga penghapusan (TC-AUTH-MFA-31) dan pengubahan (TC-AUTH-MFA-50) ID device tidak memengaruhi TC lain.
  - Menghapus cookies dan penyimpanan situs TAG Samurai di browser uji A, serta mengubah satu karakter nilai ID device di penyimpanan browser uji A.
  - IP uji Jakarta (ID) untuk semua TC (Tabel Data Uji Pre-setup #19).
  - Mail-catcher lingkungan uji untuk membaca email alert "New sign-in to your TAG Samurai account". Asersi email memakai baseline jumlah email alert untuk alamat user yang dicatat sebelum login.
  - reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-MFA-30: Login dari device baru memicu MFA dan email alert

1. Atur IP uji ke Jakarta (ID)
2. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `citradewanti+{runId}-022@qwertysystem.net` sebagai baseline
3. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
4. Ketik `citradewanti+{runId}-022@qwertysystem.net` pada field Email
5. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
6. Centang widget reCAPTCHA "I'm not a robot"
7. Klik button [Log in]
8. Amati halaman setelah klik [Log in]
9. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib karena device baru)
10. Periksa mail-catcher lingkungan uji untuk `citradewanti+{runId}-022@qwertysystem.net`
11. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `citradewanti+{runId}-022@qwertysystem.net` (jumlah bertambah dibanding baseline langkah 2)
12. Verifikasi Pilihan halaman Choose Verification Method sama dengan alasan MFA lain: opsi "OTP via email" dan "Authenticator app"

### TC-AUTH-MFA-31: Menghapus penyimpanan browser membuat browser yang sama dianggap device baru

13. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
14. Atur IP uji ke Jakarta (ID)
15. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `wawankurniawan+{runId}-022@qwertysystem.net` sebagai baseline
16. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
17. Ketik `wawankurniawan+{runId}-022@qwertysystem.net` pada field Email
18. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
19. Centang widget reCAPTCHA "I'm not a robot"
20. Klik button [Log in]
21. Verifikasi Portal — Product Hub tampil tanpa MFA (login pertama pada TC ini dari browser uji A yang dikenali)
22. Pada halaman Portal — Product Hub, logout dari akun `Wawan Kurniawan`
23. Hapus cookies dan penyimpanan situs TAG Samurai di browser uji A
24. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
25. Ketik `wawankurniawan+{runId}-022@qwertysystem.net` pada field Email
26. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
27. Centang widget reCAPTCHA "I'm not a robot"
28. Klik button [Log in]
29. Amati halaman setelah klik [Log in]
30. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (device baru walau browser dan perangkat fisik sama)
31. Periksa mail-catcher lingkungan uji untuk `wawankurniawan+{runId}-022@qwertysystem.net`
32. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `wawankurniawan+{runId}-022@qwertysystem.net` (jumlah bertambah dibanding baseline langkah 15)

### TC-AUTH-MFA-50: ID device yang berbeda satu karakter dari ID trusted dianggap device baru (exact match, bukan kemiripan)

33. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
34. Atur IP uji ke Jakarta (ID)
35. Ubah satu karakter pada nilai ID device di penyimpanan browser uji A (ID device yang di-trust untuk `Eko Rahmawati`)
36. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `ekorahmawati+{runId}-022@qwertysystem.net` sebagai baseline
37. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
38. Ketik `ekorahmawati+{runId}-022@qwertysystem.net` pada field Email
39. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
40. Centang widget reCAPTCHA "I'm not a robot"
41. Klik button [Log in]
42. Amati halaman setelah klik [Log in]
43. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib karena ID device tidak sama persis dengan ID yang di-trust)
44. Periksa mail-catcher lingkungan uji untuk `ekorahmawati+{runId}-022@qwertysystem.net`
45. Verifikasi Email alert "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `ekorahmawati+{runId}-022@qwertysystem.net` (jumlah bertambah dibanding baseline langkah 36)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru browser uji, atur IP uji, catat baseline email, logout pada TC-AUTH-MFA-31) bukan asersi tambahan (S-03). Langkah 2, 15, dan 36 mencatat baseline jumlah email alert (S-12) supaya "email alert diterima" diasersi sebagai bertambah.
- Urutan TC mengikuti TC sumber; TC-AUTH-MFA-31 dan 50 memodifikasi ID device sehingga memakai konteks browser uji A baru per TC (S-09).
- Sesi teramati lewat halaman yang tampil: sesi pre-auth MFA = halaman Choose Verification Method tampil. Post Condition sesi tidak diasersi terpisah.
- Temuan untuk QA:
  1. TC-AUTH-MFA-31 Langkah Uji tidak menyebut IP uji; spec memakai Jakarta (ID) sesuai profil BASE.
  2. TC-AUTH-MFA-31 Expected butir a memakai penomoran "langkah 5" dan butir b "langkah 9" yang tidak sama dengan Langkah Uji (login pertama di langkah 5, login ulang di langkah 8); spec menaruh Verifikasi langsung setelah aksi yang bersangkutan (langkah 21 dan 30).
  3. Post Condition berupa state BE tidak diasersi (S-01, S-15): TC-AUTH-MFA-30 "Sesi pre-auth MFA aktif untuk `Citra Dewanti`; ID device browser baru belum masuk daftar trusted device (baru masuk setelah MFA sukses)" (tanpa langkah pengecekan lewat UI), serta TC-AUTH-MFA-31 dan 50 "Sesi pre-auth MFA aktif untuk <user>" (teramati lewat halaman Choose Verification Method tampil pada Expected). QA menambah Expected atau langkah observasi di TC bila ada yang harus diuji lebih jauh.
  4. Mekanisme seeding state BE (trusted device per ID device browser A/B, lokasi dan waktu login terakhir, consent) belum ada di Tabel Data Uji Pre-setup (#20 dan #21 hanya memuat manipulasi jam server, seed `last_logout_at`, pasangan negara, `first_login_at`, dan failure injection); tim FE/BE menyediakan dan QA melengkapi Pre-setup.
