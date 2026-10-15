---
id: TC-AUTH-SES-E2E-010-limit-login-mobile-dan-duplicate-login
title: "Limit Login Mobile: Dialog Duplicate Login Attempt Lintas Perangkat Android dan Login Mobile saat Sesi Web Aktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-22
  - TC-AUTH-SES-23
  - TC-AUTH-SES-293
  - TC-AUTH-SES-294
coverage:
  web: automated
  mobile: automated
---

# Limit Login Mobile: Dialog Duplicate Login Attempt Lintas Perangkat Android dan Login Mobile saat Sesi Web Aktif

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-22: `Ayu Kusuma` (`ayukusuma+{runId}-010@qwertysystem.net`)
  - TC-AUTH-SES-23: `Taufik Permata` (`taufikpermata+{runId}-010@qwertysystem.net`)
  - TC-AUTH-SES-293: `Sari Permata` (`saripermata+{runId}-010@qwertysystem.net`)
  - TC-AUTH-SES-294: `Galih Lestari` (`galihlestari+{runId}-010@qwertysystem.net`)
- Sesi web aktif milik `Taufik Permata` (Browser A, Chrome on Windows, status Active) dibuat di hook `before` lewat login API; `Taufik Permata` tidak punya sesi mobile. Sesi mobile aktif (status Active) milik `Ayu Kusuma`, `Sari Permata`, dan `Galih Lestari` dibuat di langkah pembuka TC masing-masing lewat login nyata di perangkat Android uji A dengan email dan password user, lalu mengetuk [Not now] pada Prompt Enable Biometric (Tabel Data Uji Pre-setup #28), karena perangkat A menampung satu user pada satu waktu.
- Perangkat (Tabel Data Uji Pre-setup #10): Android uji A dan Android uji B dengan aplikasi mobile TAG Samurai terpasang. Perangkat A menampung sesi mobile seed secara bergantian: tiap TC diawali langkah menutup paksa aplikasi di perangkat A dan B, lalu login nyata di perangkat A sebagai user TC itu (kecuali TC-AUTH-SES-23, yang membutuhkan perangkat A belum login).
- Hook `after`: akhiri semua sesi seed web dan mobile, tutup konteks Browser A, pastikan aplikasi mobile di perangkat A dan B tidak menyimpan sesi, hapus keempat user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: perangkat fisik bersama (Android uji A dan B) yang menampung satu sesi lokal aplikasi pada satu waktu, dibersihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness c: multi-perangkat):
  - driver otomasi Android untuk dua perangkat atau emulator bersamaan (A dan B) beserta satu konteks browser (Browser A, Chrome on Windows, untuk TC-AUTH-SES-23);
  - menutup paksa aplikasi dan menghapus sesi lokal aplikasi;
  - mengetuk [Not now] pada Prompt Enable Biometric setelah login di perangkat A, sehingga aplikasi di perangkat A menerima push SSE;
  - pembacaan data sesi platform per user dari BE uji (status Active dan ada tidaknya sesi mobile baru) untuk asersi status sesi, disediakan tim FE/BE.
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada perangkat Android A dan B, serta Browser A untuk TC-AUTH-SES-23.

## Test Steps

### TC-AUTH-SES-22: Login mobile kedua saat sudah ada sesi mobile aktif memunculkan Dialog Duplicate Login Attempt

1. Tutup paksa aplikasi mobile di perangkat Android uji A dan B, lalu hapus sesi lokal aplikasi
2. Di perangkat Android uji A buka aplikasi mobile TAG Samurai, login dengan `ayukusuma+{runId}-010@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu ketuk [Not now] pada Prompt Enable Biometric → Portal — Product Hub tampil di perangkat A
3. Di perangkat Android uji B buka aplikasi mobile TAG Samurai → halaman Login tampil
4. Ketik email `ayukusuma+{runId}-010@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu ketuk [Login] → Dialog "Duplicate Login Attempt" muncul
5. Verifikasi Dialog "Duplicate Login Attempt" tampil di perangkat B dengan Title "Duplicate Login Attempt"
6. Verifikasi Body berisi "You are already signed in on another device:" diikuti `TAG Samurai App on Android` (nama aplikasi dan OS perangkat A)
7. Verifikasi [Confirm] tampil pada dialog
8. Verifikasi [Cancel] tampil pada dialog
9. Verifikasi Sesi mobile baru belum dibuat
10. Pindah ke perangkat Android uji A (tanpa mengetuk apa pun)
11. Verifikasi Sesi mobile di perangkat A tetap Active
12. Verifikasi Perangkat A tidak menampilkan dialog apa pun

### TC-AUTH-SES-294: Cancel pada Dialog Duplicate Login Attempt di mobile menjaga sesi lama tetap aktif

13. Tutup paksa aplikasi mobile di perangkat Android uji A dan B, lalu hapus sesi lokal aplikasi
14. Di perangkat Android uji A buka aplikasi mobile TAG Samurai, login dengan `galihlestari+{runId}-010@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu ketuk [Not now] pada Prompt Enable Biometric → Portal — Product Hub tampil di perangkat A
15. Di perangkat Android uji B buka aplikasi mobile TAG Samurai, ketik email `galihlestari+{runId}-010@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu ketuk [Login] → Dialog "Duplicate Login Attempt" muncul
16. Ketuk [Cancel]
17. Verifikasi Perangkat B kembali ke halaman Login
18. Verifikasi Tidak ada sesi mobile baru di perangkat B
19. Pindah ke perangkat Android uji A dan ketuk layar
20. Verifikasi Sesi mobile di perangkat A tetap Active
21. Verifikasi Perangkat A tidak menampilkan dialog apa pun

### TC-AUTH-SES-23: Login mobile saat sesi web aktif diizinkan tanpa dialog

22. Tutup paksa aplikasi mobile di perangkat Android uji A dan B, lalu hapus sesi lokal aplikasi sehingga perangkat A belum login
23. Buka Browser A (Chrome on Windows) dengan sesi web aktif milik `Taufik Permata` (sesi seed hook `before`) → Portal — Product Hub tampil
24. Di perangkat Android uji A buka aplikasi mobile TAG Samurai → halaman Login tampil
25. Ketik email `taufikpermata+{runId}-010@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu ketuk [Login] → Portal — Product Hub tampil di perangkat A
26. Verifikasi Halaman Portal — Product Hub tampil di perangkat Android uji A
27. Verifikasi Dialog "Duplicate Login Attempt" tidak tampil di perangkat A
28. Pindah ke Browser A (tanpa mengklik apa pun)
29. Verifikasi Dialog "Duplicate Login Attempt" tidak tampil di Browser A
30. Verifikasi Sesi web di Browser A tetap Active

### TC-AUTH-SES-293: Confirm pada Dialog Duplicate Login Attempt di mobile mengaktifkan sesi baru dan meng-logout perangkat lama

31. Tutup paksa aplikasi mobile di perangkat Android uji A dan B, lalu hapus sesi lokal aplikasi
32. Di perangkat Android uji A buka aplikasi mobile TAG Samurai, login dengan `saripermata+{runId}-010@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu ketuk [Not now] pada Prompt Enable Biometric → Portal — Product Hub tampil di perangkat A
33. Di perangkat Android uji B buka aplikasi mobile TAG Samurai, ketik email `saripermata+{runId}-010@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu ketuk [Login] → Dialog "Duplicate Login Attempt" muncul
34. Ketuk [Confirm]
35. Verifikasi Perangkat B masuk Portal — Product Hub
36. Verifikasi Sesi mobile baru di perangkat B berstatus Active
37. Pindah ke perangkat Android uji A dan amati tanpa interaksi selama 10 detik (event push SSE)
38. Verifikasi Perangkat A menerima Dialog "Logged Out" dengan Body "You have been logged out because another session was started on a different device."
39. Di perangkat A ketuk [OK]
40. Verifikasi Setelah [OK] perangkat A diarahkan ke halaman Login

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembagian TC lintas spec: login web (TC-AUTH-SES-20, 21, 24, 25) ada di `TC-AUTH-SES-E2E-009-limit-login-web-dan-duplicate-login`; Confirm, Cancel, dan klik ganda di web ada di `TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web`.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-22, 294, 23, lalu 293 (urutan TC sumber 22, 23, 293, 294). Cancel diletakkan sebelum Confirm, dan TC-AUTH-SES-293 yang meng-logout perangkat lama diletakkan paling akhir. Tiap TC memakai user dan sesi seed sendiri, jadi urutan tidak membuat TC saling bergantung.
- TC-AUTH-SES-293 dan 294 berdependensi pada TC-AUTH-SES-22 (login di perangkat B hingga dialog muncul); langkah itu disalin utuh pada langkah 15 dan 33 (S-04). Spec ini memuat 40 langkah, di atas batas sekitar 35: satu kelas harness (c: multi-perangkat) yang bila dipecah mengulang penyiapan dua perangkat Android dan Browser A, sehingga dipertahankan satu spec.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03, S-09): menutup paksa aplikasi dan menghapus sesi lokal antar-TC, login nyata di perangkat A dengan [Not now] pada Prompt Enable Biometric, serta perpindahan antar perangkat dan Browser A.
- Pencatatan: asersi "tidak ada entri log baru" pada TC-AUTH-SES-294 (Expected c) tidak diasersikan di spec ini; dirujuk ke spec absence `TC-AUTH-SES-E2E-066-absence-duplicate-login-dan-session-expired` sesuai S-05.
- Temuan untuk QA: (1) TC-AUTH-SES-22, 23, 293, dan 294 berlabel `Manual Only` karena membutuhkan perangkat fisik; spec tetap memuatnya dan kebutuhan perangkat dicatat di Prerequisites. (2) TC-AUTH-SES-22 dan 293 menulis "login dengan ... dan password yang benar" tanpa nilai; spec memakai `Spectra.env.SES_PASSWORD`. (3) TC-AUTH-SES-22 dan 293 tidak menyebut cara sesi mobile di perangkat A dibuat (hanya TC-AUTH-SES-294 merujuk Tabel Data Uji Pre-setup #28); spec memakai cara itu untuk ketiganya. (4) TC-AUTH-SES-23 tidak menyebut bahwa Browser A harus terbuka dan terhubung ke sesi web aktif untuk mengamati "dialog tidak tampil di perangkat mana pun"; spec membuka Browser A dengan sesi seed. (5) Halaman Login mobile tidak disebut namanya di TC; spec memakai "halaman Login". (6) Pembacaan data sesi platform dari BE uji untuk asersi status sesi tidak punya mekanisme di TC, PRD, dan LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE tanpa menyebut endpoint (S-11, S-13).
