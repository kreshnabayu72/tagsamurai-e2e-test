---
id: TC-AUTH-MFA-E2E-051-mobile-biometric-relogin
title: "Biometric Re-login sebagai Faktor-1 di Android"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-54
  - TC-AUTH-MFA-167
coverage:
  mobile: automated
  web: automated
---

# Biometric Re-login sebagai Faktor-1 di Android

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) untuk langkah login dan pilihan faktor kedua; browser web untuk membaca pencatatan log oleh akun aktor (TC-AUTH-MFA-167).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil MOB (Tabel Data Uji Pre-setup #11: Activated, Active ON, Authenticator sudah terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Untuk kedua user: Biometric Re-login sudah diaktifkan di aplikasi mobile perangkat uji dan MFA terpicu pada login ini (kondisi yang di-seed BE):
  - TC-AUTH-MFA-54: `Naufal Hakim` (`naufalhakim+{runId}-051@qwertysystem.net`)
  - TC-AUTH-MFA-167: `Zulfa Nabila` (`zulfanabila+{runId}-051@qwertysystem.net`), Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji
- Sesi akun aktor di web: hook `before` login akun aktor Total Control (Global Settings) di browser web uji (kredensial `Spectra.env.GS_TC_PASSWORD`); sesi ini dipakai pada langkah ganti konteks ke web. Akun aktor dapat login ke web tanpa tahap MFA.
- Hook `after`: hapus kedua user, nonaktifkan Biometric Re-login yang di-seed, dan kembalikan sesi browser web ke akun default suite. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: TC-AUTH-MFA-54 dan langkah mobile TC-AUTH-MFA-167 tanpa sesi aktif di aplikasi (biometric sign-in); langkah pencatatan TC-AUTH-MFA-167 memakai akun aktor Total Control (Global Settings) di web.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: driver otomasi Android (aplikasi native); perangkat atau emulator Android uji dengan biometrik terdaftar yang dapat dikonfirmasi otomatis pada prompt OS (simulasi biometrik); aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk kode TOTP faktor kedua; browser web dengan sesi akun aktor.
- Seeding state BE per user (kemampuan teknis): Biometric Re-login aktif di aplikasi mobile perangkat uji (Naufal Hakim dan Zulfa Nabila), ID device aplikasi saat instal (dikenali BE untuk login ini), pemicu MFA pada login ini, dan Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji (Zulfa Nabila); mekanisme seeding (endpoint atau skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-54: Faktor-1 Biometric Re-login (mobile) menampilkan halaman pilihan faktor kedua

1. Buka aplikasi mobile TAG Samurai → layar biometric sign-in tampil
2. Konfirmasi biometric pada prompt OS perangkat uji → halaman `Auth > MFA > Choose Verification Method` tampil
3. Verifikasi Halaman Choose Verification Method menampilkan opsi "OTP via email"
4. Verifikasi Halaman Choose Verification Method menampilkan opsi "Authenticator app"
5. Verifikasi Tidak ada opsi Biometric sebagai faktor kedua

### TC-AUTH-MFA-167: Pencatatan login final via MFA setelah Biometric Re-login dicatat Success dengan Note Login with biometric

6. Tutup paksa aplikasi mobile TAG Samurai agar sesi pre-auth TC sebelumnya tidak dilanjutkan
7. Catat penanda waktu baseline (waktu saat ini) sebelum attempt login `Zulfa Nabila`; entri log yang waktunya sebelum penanda ini (termasuk login seed profil MOB) tidak dihitung
8. Buka aplikasi mobile TAG Samurai → layar biometric sign-in tampil
9. Konfirmasi biometric pada prompt OS perangkat uji → halaman Choose Verification Method tampil
10. Pilih opsi "Authenticator app"
11. Klik button [Login]
12. Ketik kode TOTP valid dari aplikasi authenticator uji pada field kode
13. Klik button [Login]
14. Ganti konteks dari aplikasi mobile ke browser web dengan sesi akun aktor Total Control (Global Settings) dari hook `before`
15. Buka `Global Settings > Activity Log > Session` dan cari entri untuk `Zulfa Nabila` yang waktunya sesudah penanda waktu baseline (langkah 7)
16. Verifikasi Tampil tepat satu entri baru (waktu sesudah penanda baseline) untuk `Zulfa Nabila` untuk attempt ini
17. Verifikasi Activity entri tersebut `Login`
18. Verifikasi Status entri tersebut `Success`
19. Verifikasi Note entri tersebut `Login with biometric`
20. Verifikasi Jumlah entri Success dari session-management untuk attempt ini pada Activity Log > Session tetap satu (bukan dua)
21. Buka `Global Settings > User > Detail > User Log` untuk `Zulfa Nabila` dan cari entri yang waktunya sesudah penanda waktu baseline (langkah 7)
22. Verifikasi Tampil tepat satu entri baru (waktu sesudah penanda baseline) dengan Status `Success`
23. Verifikasi Note entri tersebut `Login with biometric`
24. Verifikasi Jumlah entri Success dari session-management untuk attempt ini pada User Log tetap satu (bukan dua)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi` (langkah 6 menutup paksa aplikasi; langkah 7 mencatat penanda waktu baseline log; langkah 14 ganti konteks ke web dengan sesi akun aktor) bukan asersi tambahan (S-03). Login akun aktor di web dilakukan di hook `before` (S-07).
- Urutan mengikuti TC sumber: TC-AUTH-MFA-54 lalu TC-AUTH-MFA-167; tidak ada penyimpangan (S-05, S-10).
- TC-AUTH-MFA-167 Expected c ("tidak ada entri Success kedua") ditulis sebagai asersi jumlah (langkah 20 dan 24), bukan asersi absence; asersi absence pencatatan log ada di spec absence.
- Temuan untuk QA: (1) TC-AUTH-MFA-54 precondition d menulis contoh pemicu MFA "device baru atau idle ≥30 hari" tanpa menetapkan salah satu; spec men-seed pemicu MFA tanpa memilih penyebabnya. (2) TC-AUTH-MFA-54 dan 167 sama-sama mensyaratkan layar biometric sign-in untuk user berbeda di perangkat uji yang sama; TC tidak menyatakan apakah dua user dapat memiliki Biometric Re-login aktif bersamaan di satu perangkat. (3) TC-AUTH-MFA-54 precondition c dan TC-AUTH-MFA-167 precondition c (mail-catcher) tidak dipakai oleh Langkah Uji. (4) TC-AUTH-MFA-167 langkah 3 tidak menyebut cara mendapatkan kode TOTP dan hasil akhir login; spec memakai aplikasi authenticator uji dan tidak menambah asersi halaman tujuan. (5) TC-AUTH-MFA-54 dan 167 tidak menyebut cara keluar dari sesi pre-auth antar TC; langkah 6 mengandaikan menutup paksa aplikasi mengembalikan layar biometric sign-in. (6) TC-AUTH-MFA-54 Post Condition "Sesi pre-auth MFA aktif untuk `Naufal Hakim` di platform mobile" tidak punya Expected padanan atau langkah observasi di TC (state BE) dan tidak diasersi. (7) Profil MOB sudah memiliki login seed, sehingga "tepat satu entri baru" pada TC-AUTH-MFA-167 tidak dapat dibaca tanpa baseline; TC tidak menyebut baseline, jadi spec memakai penanda waktu sebelum attempt (langkah 7) dan hanya menghitung entri sesudahnya. (8) Mekanisme seeding state BE (Biometric Re-login aktif di perangkat uji, ID device aplikasi saat instal, Authenticator terdaftar dengan secret yang dikenal authenticator uji, pemicu MFA) belum ada di Pre-setup (#20/#21) TC dan tidak didefinisikan di PRD atau LLD; spec tidak menyebut endpoint seeding.
