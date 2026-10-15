---
id: TC-AUTH-LP-E2E-046-cross-module-user-status-sync
title: "Sinkron Status User dari Global Settings ke Login with Password"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-131
  - TC-AUTH-LP-132
  - TC-AUTH-LP-134
  - TC-AUTH-LP-133
coverage:
  web: automated
---

# Sinkron Status User dari Global Settings ke Login with Password

## Prerequisites

- Mode: FE+BE.
- Seeding: semua user dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`), lalu dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh. Link aktivasi user Pending Activation diambil dari respons seeding API.
- Aktor Global Settings: akun aktor Total Control di atas login di browser kedua pada hook `before`; browser kedua ditutup di hook `after`. Browser pertama dipakai untuk sisi subjek (guest).
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: fixture BE untuk user Yuni dan Bambang berupa device terpercaya tanpa gate Agreement dan MFA, bukan login pertama, dan tidak idle, serta user Eni yang di-seed Pending Activation dan belum pernah login di web; dua sesi browser bersamaan; reCAPTCHA mode uji di environment; jendela privat baru (tanpa sesi login) untuk membuka tautan aktivasi pada TC-AUTH-LP-134 (langkah 26).
- TC-AUTH-LP-131: User `Yuni Astuti` (`yuniastuti+{runId}-046@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA
- TC-AUTH-LP-131 data: Email `yuniastuti+{runId}-046@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-132: User `Yuni Astuti` yang sama berstatus Activated dengan Toggle Global OFF (hasil TC-AUTH-LP-131 dalam spec ini); device terpercaya; tidak ada gate Agreement dan MFA
- TC-AUTH-LP-132 data: Email `yuniastuti+{runId}-046@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-134: User `Eni Raharyu` (`eniraharyu+{runId}-046@qwertysystem.net`) berstatus Pending Activation dengan tautan aktivasi yang masih berlaku (di-seed lewat API); belum pernah login di web
- TC-AUTH-LP-134 data: Email `eniraharyu+{runId}-046@qwertysystem.net`; Password dan Confirm Password aktivasi `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-133: User `Bambang Irawan` (`bambangirawan+{runId}-046@qwertysystem.net`) berstatus Activated dan Active
- TC-AUTH-LP-133 data: Email `bambangirawan+{runId}-046@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-131: User yang dinonaktifkan di Global Settings > User langsung ditolak saat login

1. Pindah ke browser kedua (sesi aktor Total Control Global Settings) dan buka `Global Settings > User`
2. Matikan Toggle Global user "Yuni Astuti"
3. Pindah ke browser pertama dan buka halaman Login with Password
4. Ketik "yuniastuti+{runId}-046@qwertysystem.net" di field Email
5. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
6. Selesaikan reCAPTCHA
7. Klik [Log in]
8. Verifikasi Alert Danger "Your account is inactive" tampil di atas Button [Log in]
9. Verifikasi browser kedua tetap berada di `Global Settings > User` tanpa memuat ulang sesi admin
10. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-132: User yang diaktifkan kembali di Global Settings > User dapat login lagi

11. Pindah ke browser kedua dan nyalakan Toggle Global user "Yuni Astuti" di `Global Settings > User`
12. Pindah ke browser pertama dan muat ulang halaman Login with Password
13. Ketik "yuniastuti+{runId}-046@qwertysystem.net" di field Email
14. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
15. Selesaikan reCAPTCHA
16. Klik [Log in]
17. Verifikasi Alert "Your account is inactive" tidak tampil
18. Verifikasi login berhasil dan browser menuju Portal — Product Hub
19. Logout dari Portal — Product Hub

### TC-AUTH-LP-134: Akun yang baru diaktivasi dapat login dan menuju layar Confirm to Continue

20. Buka halaman Login with Password di browser pertama
21. Ketik "eniraharyu+{runId}-046@qwertysystem.net" di field Email
22. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
23. Selesaikan reCAPTCHA
24. Klik [Log in]
25. Verifikasi Alert Danger "Your account has not been activated" tampil
26. Buka link aktivasi user `Eni Raharyu` di jendela privat baru (tanpa sesi login)
27. Verifikasi halaman `Auth > Account Activation > Set Password` tampil
28. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password dan field Confirm Password
29. Klik button "Set Password"
30. Buka halaman Login with Password di browser pertama
31. Ketik "eniraharyu+{runId}-046@qwertysystem.net" di field Email
32. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
33. Selesaikan reCAPTCHA
34. Klik [Log in]
35. Verifikasi Alert "Your account has not been activated" tidak tampil
36. Verifikasi layar Confirm to Continue tampil (login pertama)

### TC-AUTH-LP-133: User yang dihapus di Global Settings > User diperlakukan sebagai Email belum terdaftar

37. Pindah ke browser kedua dan buka `Global Settings > User`
38. Hapus user "Bambang Irawan"
39. Pindah ke browser pertama dan buka halaman Login with Password
40. Ketik "bambangirawan+{runId}-046@qwertysystem.net" di field Email
41. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
42. Selesaikan reCAPTCHA
43. Klik [Log in]
44. Verifikasi caption "Email is not registered yet" tampil di bawah field Email
45. Verifikasi tidak ada sesi dibuat

## Notes

- Sumber: `auth/login-password/TestCases/tc-login-password.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan spec: TC-AUTH-LP-131 lalu TC-AUTH-LP-132 (user yang sama berurutan, Toggle Global OFF lalu ON), TC-AUTH-LP-134 (aktivasi) dan TC-AUTH-LP-133 (aksi menghapus data) paling akhir (S-10, prinsip 5); urutan di TC sumber 131, 132, 133, 134.
- Langkah penghubung (S-03): perpindahan antar browser, pemuatan ulang halaman Login with Password, dan logout pada langkah 19 hanya menyiapkan konteks (S-09). Langkah 26 sampai 29 menyalin alur Account Activation sebagai dependensi TC-AUTH-LP-134 (S-04), memakai nama halaman dan tombol yang sama dengan suite Account Activation (`specs/Auth/AccountActivation`); link aktivasi dibuka di jendela privat baru sebagai konteks tanpa sesi.
- Asersi tambahan di luar Expected TC (S-03): langkah 27 memverifikasi halaman Set Password tampil. Alasan: TC-AUTH-LP-134 langkah 3 hanya menyebut "selesaikan aktivasi"; pembuktian halaman tampil dibutuhkan agar langkah 28 sampai 29 (isi password dan klik Set Password) punya konteks, dan nama halaman mengikuti suite Account Activation.
- Temuan untuk QA:
  - TC-AUTH-LP-131 Expected butir a ("tanpa memuat ulang sesi admin") tidak jelas apa yang diamati; spec menerjemahkannya sebagai browser aktor Global Settings tetap di halaman tanpa muat ulang (langkah 9).
  - TC-AUTH-LP-134 langkah 3 menyebut "Selesaikan aktivasi akun lewat tautan aktivasi dan set password ... (alur modul Account Activation)" tanpa merinci langkah alur itu (halaman, tombol); langkah 26 sampai 29 dilengkapi dari modul Account Activation. Hasil login pertama sesudah Confirm to Continue (mis. MFA) juga tidak dijelaskan lebih jauh di TC.
  - Post Condition tanpa langkah observasi di TC sehingga tidak diasersi di spec ini (S-01): TC-AUTH-LP-131 "Toggle Global user berstatus OFF", TC-AUTH-LP-132 "Toggle Global user berstatus ON", dan TC-AUTH-LP-133 "user terhapus". Spec tidak menambah langkah observasi sendiri.
