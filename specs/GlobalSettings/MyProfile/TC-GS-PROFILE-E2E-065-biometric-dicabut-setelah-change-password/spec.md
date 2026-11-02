---
id: TC-GS-PROFILE-E2E-065-biometric-dicabut-setelah-change-password
title: "Change Password Mencabut Kredensial Biometric Lintas Device"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-250
coverage:
  web: automated
  mobile: automated
---

# Change Password Mencabut Kredensial Biometric Lintas Device

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #7 (Maya Anggraini) `passwordProfile_automated_{namaCompany}@qwertysystem.net`, password aktif `Spectra.env.GS_PROFILE_PWD_PASSWORD`; password baru `Spectra.env.PROFILE_PASSWORD_NEW` (Data Dinamis #3). Login sesi web di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Perangkat: perangkat Android uji dengan aplikasi mobile terpasang dan biometric aktif untuk akun #7 (kelas d, hardware biometrik; disediakan tim FE). Spec berjalan di web dan di perangkat Android, sehingga `coverage.web` dan `coverage.mobile` keduanya `automated`. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): pemasangan kredensial biometric aktif akun #7 di perangkat Android uji di hook `before` spec ini; prompt biometric OS diselesaikan oleh perangkat uji; fixture BE yang memulihkan password akun #7 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`).
- State global yang diubah: password akun #7 dan kredensial biometric akun #7 (dicabut oleh Change Password). Dipulihkan oleh langkah pemulihan di akhir spec dan hook `after` suite; kredensial biometric dipasang ulang di hook `before` spec yang membutuhkannya.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.

## Test Steps

### TC-GS-PROFILE-250: Change Password mencabut kredensial biometric lintas device

1. Di web klik [Change Password]
2. Di web isi Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`, klik [Save]
3. Tunggu aksi selesai di web: modal Change Password tertutup
4. Di perangkat Android uji buka aplikasi mobile, lalu coba login ulang dengan biometric
5. Verifikasi login ulang biometric ditolak
6. Verifikasi pengguna diminta login dengan password

### Pemulihan state

7. Fixture BE memulihkan password akun #7 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`) hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 3 menunggu aksi selesai sebelum berpindah ke perangkat (bagian 8b butir 8); langkah 7 memulihkan password (R-08).
- Temuan untuk QA:
  - TC-GS-PROFILE-250 menyebut kredensial biometric "sudah di-revoke" sebagai alasan penolakan; spec mengasersi penolakan dan permintaan login password, bukan status revoke di server (tidak ada cara cek di TC).
