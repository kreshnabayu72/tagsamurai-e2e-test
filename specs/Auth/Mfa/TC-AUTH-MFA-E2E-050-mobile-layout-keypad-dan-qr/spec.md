---
id: TC-AUTH-MFA-E2E-050-mobile-layout-keypad-dan-qr
title: "Layout Mobile Android: Keypad Numerik dan QR Enrollment"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-17
  - TC-AUTH-MFA-18
coverage:
  mobile: automated
---

# Layout Mobile Android: Keypad Numerik dan QR Enrollment

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android), terpasang di perangkat atau emulator uji, tanpa sesi aktif di aplikasi.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-17: `Dewi Santoso` (`dewisantoso+{runId}-050@qwertysystem.net`)
  - TC-AUTH-MFA-18: `Rizky Santoso` (`rizkysantoso+{runId}-050@qwertysystem.net`)
- Hook `after`: hapus kedua user dan pastikan aplikasi mobile tidak menyimpan sesi. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik di aplikasi) untuk kedua TC.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: driver otomasi Android (aplikasi native), deteksi keyboard numerik dan posisi kursor, pengukuran tata letak (lebar card dan QR terhadap lebar layar, posisi button di bawah layar), akses clipboard sistem Android, dan aplikasi authenticator uji di perangkat Android yang sama untuk menempel secret key (TC-AUTH-MFA-18).
- Semua user berprofil FIRST, jadi tiap login melewati layar Confirm to Continue sebelum Choose Verification Method.

## Test Steps

### TC-AUTH-MFA-17: Halaman OTP Verification di aplikasi mobile menampilkan keypad numerik dan kursor di kotak 1

1. Buka aplikasi mobile TAG Samurai → halaman Login with Password tampil
2. Ketik `dewisantoso+{runId}-050@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Klik button [Log in] → layar Confirm to Continue tampil
5. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "OTP via email"
7. Klik button [Login] → halaman OTP Verification tampil
8. Verifikasi Kursor aktif di kotak 1
9. Verifikasi Keypad numerik terbuka
10. Verifikasi Card mengisi lebar layar
11. Verifikasi Button [Login] tersemat di bagian bawah layar

### TC-AUTH-MFA-18: Enrollment di aplikasi mobile: QR code diskalakan dan secret key dapat disalin untuk input manual

12. Tutup paksa aplikasi mobile TAG Samurai agar sesi pre-auth TC sebelumnya tidak dilanjutkan
13. Buka aplikasi mobile TAG Samurai → halaman Login with Password tampil
14. Ketik `rizkysantoso+{runId}-050@qwertysystem.net` pada field Email
15. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
16. Klik button [Log in] → layar Confirm to Continue tampil
17. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
18. Pilih opsi "Authenticator app"
19. Klik button [Login] → halaman Enrollment tampil
20. Verifikasi QR code tampil proporsional terhadap lebar layar tanpa terpotong
21. Klik CopyButton "Copy key"
22. Tempel isi clipboard pada input manual aplikasi authenticator uji
23. Verifikasi Secret key berhasil disalin
24. Verifikasi Secret key dapat ditempel pada aplikasi authenticator uji

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi` (langkah 12 menutup paksa aplikasi; langkah 22 menempel clipboard ke aplikasi authenticator uji) bukan asersi tambahan (S-03).
- Urutan mengikuti TC sumber: TC-AUTH-MFA-17 lalu TC-AUTH-MFA-18; tidak ada penyimpangan (S-05, S-10).
- Temuan untuk QA: (1) TC-AUTH-MFA-17 precondition c (mail-catcher membaca email uji) tidak dipakai oleh Langkah Uji maupun Expected; spec tidak membaca mail-catcher. (2) TC-AUTH-MFA-18 Expected b ("dapat ditempel pada aplikasi authenticator uji") tidak punya langkah di Langkah Uji; langkah 22 ditambahkan sebagai langkah penghubung agar asersinya dapat dijalankan (S-14, S-15). (3) TC-AUTH-MFA-17 dan 18 tidak menyebut cara keluar dari sesi pre-auth antar TC; langkah 12 mengandaikan menutup paksa aplikasi membuat halaman Login with Password tampil kembali. (4) TC-AUTH-MFA-17 Post Condition "Sesi pre-auth MFA aktif untuk `Dewi Santoso` di platform mobile" dan TC-AUTH-MFA-18 Post Condition "Secret Authenticator pending untuk sesi pre-auth ini; enrollment belum aktif" tidak punya Expected padanan atau langkah observasi di TC (state BE) dan tidak diasersi.
