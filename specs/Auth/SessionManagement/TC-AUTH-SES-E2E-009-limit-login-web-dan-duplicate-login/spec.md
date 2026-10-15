---
id: TC-AUTH-SES-E2E-009-limit-login-web-dan-duplicate-login
title: "Limit Login Web: Login Pertama dan Dialog Duplicate Login Attempt via Password, OTP, dan MFA"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-20
  - TC-AUTH-SES-21
  - TC-AUTH-SES-24
  - TC-AUTH-SES-25
coverage:
  web: automated
---

# Limit Login Web: Login Pertama dan Dialog Duplicate Login Attempt via Password, OTP, dan MFA

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-20: `Citra Setiawan` (`citrasetiawan+{runId}-009@qwertysystem.net`), profil BASE; tidak ada sesi aktif di platform web maupun mobile
  - TC-AUTH-SES-21: `Yoga Santoso` (`yogasantoso+{runId}-009@qwertysystem.net`), profil BASE
  - TC-AUTH-SES-24: `Mega Lestari` (`megalestari+{runId}-009@qwertysystem.net`), profil BASE
  - TC-AUTH-SES-25: `Reza Pratama` (`rezapratama+{runId}-009@qwertysystem.net`), profil NEWDEV (Tabel Data Uji Pre-setup #6: seperti BASE, tetapi device Browser B belum dikenali; Authenticator terdaftar sehingga hanya MFA yang terpicu)
- Sesi web aktif di Browser A (Chrome on Windows, status Active) untuk TC-AUTH-SES-21, 24, dan 25 dibuat di hook `before` lewat login API pada konteks Browser A masing-masing user sebagai kondisi yang di-seed BE. Untuk TC-AUTH-SES-21, konteks Browser A dibuka ulang dengan sesi seed itu dan menampilkan Portal — Product Hub pada langkah 6 (sebelum Browser B login).
- Browser B untuk tiap TC adalah konteks baru Firefox on macOS yang belum login; tiap TC memakai konteks Browser B sendiri.
- Hook `after`: akhiri semua sesi seed dan sesi yang dibuat spec, tutup konteks Browser A dan B, hapus keempat user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (multi-konteks; mail-catcher dan TOTP sebagai pemicu rutin, §3 prinsip 13 d):
  - dua konteks browser bersamaan dengan user agent yang dapat ditetapkan (Chrome on Windows, Firefox on macOS) supaya info device pada dialog deterministik;
  - mail-catcher lingkungan uji (Tabel Data Uji Pre-setup #19) yang dapat membaca email OTP `megalestari+{runId}-009@qwertysystem.net` (TC-AUTH-SES-24);
  - aplikasi authenticator uji (TOTP) (Tabel Data Uji Pre-setup #18) untuk user `Reza Pratama` (TC-AUTH-SES-25);
  - reCAPTCHA mode uji di environment (halaman Login with Password dan Request OTP);
  - pembacaan data sesi platform per user dari BE uji (status Active dan ada tidaknya sesi web baru) untuk asersi status sesi, disediakan tim FE/BE.
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A dan B.

## Test Steps

### TC-AUTH-SES-20: Login web pertama tanpa sesi aktif membuat sesi dan mengarahkan ke Portal

1. Di Browser A (Chrome on Windows) buka halaman `Auth > Login with Password` → halaman Login with Password tampil
2. Ketik email `citrasetiawan+{runId}-009@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → halaman Portal — Product Hub tampil
3. Verifikasi Halaman Portal — Product Hub tampil
4. Verifikasi Dialog "Duplicate Login Attempt" tidak tampil
5. Verifikasi Sesi web milik `Citra Setiawan` berstatus Active

### TC-AUTH-SES-21: Login web kedua saat sudah ada sesi web aktif memunculkan Dialog Duplicate Login Attempt

6. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), buka konteks Browser A baru (Chrome on Windows) dengan sesi seed milik `yogasantoso+{runId}-009@qwertysystem.net`, lalu pastikan Browser A menampilkan Portal — Product Hub → halaman Portal — Product Hub tampil
7. Buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
8. Ketik email `yogasantoso+{runId}-009@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
9. Verifikasi Dialog "Duplicate Login Attempt" tampil di Browser B
10. Verifikasi Body "You are already signed in on another device: Chrome on Windows. Confirm to log out that session and continue here."
11. Verifikasi Sesi web baru belum dibuat
12. Verifikasi Browser B belum masuk Portal
13. Pindah ke Browser A (tanpa mengklik apa pun)
14. Verifikasi Sesi web di Browser A tetap Active
15. Verifikasi Browser A tidak menampilkan dialog apa pun

### TC-AUTH-SES-24: Login with OTP saat sesi web aktif memunculkan Dialog Duplicate Login Attempt

16. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka `Auth > Login with OTP > Request OTP` → halaman Request OTP tampil
17. Ketik `megalestari+{runId}-009@qwertysystem.net` pada field email
18. Centang reCAPTCHA
19. Klik [Request OTP]
20. Baca kode OTP 6 digit dari mail-catcher untuk `megalestari+{runId}-009@qwertysystem.net`
21. Ketik kode OTP pada layar Verify OTP → Dialog "Duplicate Login Attempt" muncul
22. Verifikasi Dialog "Duplicate Login Attempt" tampil di Browser B
23. Verifikasi Body "You are already signed in on another device: Chrome on Windows. Confirm to log out that session and continue here."
24. Verifikasi Sesi web baru belum dibuat
25. Pindah ke Browser A (tanpa mengklik apa pun)
26. Verifikasi Sesi web Browser A tetap Active

### TC-AUTH-SES-25: Login yang melewati MFA memunculkan Dialog Duplicate Login Attempt setelah MFA tuntas

27. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login; device belum dikenali untuk `rezapratama+{runId}-009@qwertysystem.net` sesuai profil NEWDEV), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
28. Ketik email `rezapratama+{runId}-009@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → halaman MFA tampil
29. Verifikasi Sebelum MFA tuntas tidak ada sesi web baru
30. Verifikasi Sebelum MFA tuntas tidak ada dialog yang tampil
31. Ketik kode TOTP yang benar dari aplikasi authenticator uji untuk `rezapratama+{runId}-009@qwertysystem.net`, lalu verifikasi → Dialog "Duplicate Login Attempt" muncul
32. Verifikasi Setelah MFA tuntas Dialog "Duplicate Login Attempt" tampil di Browser B
33. Pindah ke Browser A (tanpa mengklik apa pun)
34. Verifikasi Sesi web di Browser A tetap Active

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembagian TC lintas spec: TC-AUTH-SES-22 dan 23 (limit login mobile) ada di `TC-AUTH-SES-E2E-010-limit-login-mobile-dan-duplicate-login`; Confirm, Cancel, Escape, backdrop, dan klik ganda ada di `TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web`; screening isi dialog ada di `TC-AUTH-SES-E2E-001-screening-dialog-duplicate-login-dan-logged-out`.
- Urutan mengikuti TC sumber (20, 21, 24, 25); tidak ada penyimpangan (S-05, S-10). Tidak ada TC yang memutus sesi Browser A, sehingga tidak ada aksi merusak yang perlu ditaruh paling akhir. Tiap TC memakai user dan pasangan Browser A/B sendiri, jadi TC tidak saling bergantung.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menutup konteks TC sebelumnya (hapus sesi login browser) dan membuka konteks baru (langkah 6, 16, dan 27); memastikan Browser A menampilkan Portal — Product Hub sebelum Browser B login (langkah 6), karena asersi "Browser A tidak menampilkan dialog apa pun" (langkah 15) hanya bermakna bila Browser A hasil seeding API sedang membuka halaman app; berpindah antar Browser A dan B; membaca kode OTP dari mail-catcher.
- Mail-catcher dan aplikasi authenticator TOTP pada TC-AUTH-SES-24 dan 25 hanya pemicu rutin untuk mencapai Dialog Duplicate Login Attempt (§3 prinsip 13 d), bukan objek uji, sehingga kedua TC berada di spec yang sama dengan TC password.
- Pencatatan: TC sumber tidak memuat asersi "tidak ada pencatatan" pada TC batch ini.
- Temuan untuk QA: (1) TC-AUTH-SES-20, 21, dan 25 menulis "klik [Log in]" tanpa menyebut widget reCAPTCHA pada halaman Login with Password (TC-AUTH-SES-24 menyebutnya untuk Request OTP); spec mengikuti TC dan mengandalkan reCAPTCHA mode uji di Prerequisites. (2) TC-AUTH-SES-20 menyebut "password yang benar" tanpa nilai; spec memakai `Spectra.env.SES_PASSWORD`. (3) TC-AUTH-SES-24 langkah 2 tidak menyebut tombol pengiriman kode pada layar Verify OTP; spec mengikuti TC (mengetik kode memunculkan dialog). (4) TC-AUTH-SES-25 hanya menulis "halaman MFA tampil" tanpa menyebut layar Choose Verification Method atau pemilihan metode Authenticator; spec mengikuti TC. (5) TC-AUTH-SES-20, 21, 24, dan 25 tidak menyebut cara membaca status sesi Active dan ada tidaknya sesi web baru; kebutuhan pembacaan data sesi BE dicatat di Prerequisites.
