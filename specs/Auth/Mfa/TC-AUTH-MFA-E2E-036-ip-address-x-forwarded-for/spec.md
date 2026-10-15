---
id: TC-AUTH-MFA-E2E-036-ip-address-x-forwarded-for
title: "Kolom IP Address Entri Login Final Mengikuti X-Forwarded-For"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-174
coverage:
  web: automated
---

# Kolom IP Address Entri Login Final Mengikuti X-Forwarded-For

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): user `Intan Rahmawati` (`intanrahmawati+{runId}-036@qwertysystem.net`), password `Spectra.env.MFA_PASSWORD`, profil BASE (Tabel Data Uji Pre-setup #2: Activated, Active ON, device browser uji A dikenali sebagai trusted device, login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar; tidak ada pemicu MFA sehingga login single-step).
- Aktor observer log: akun aktor Total Control (Global Settings) di atas login di browser kedua pada hook `before` dan membaca `Global Settings > Activity Log > Session` serta `Global Settings > User > Detail > User Log`. Browser pertama dipakai sebagai user uji tanpa login (halaman publik) dan dibuka sebagai browser uji A (ID device dikenali, konteks browser dengan ID device persisten yang terdaftar untuk user di atas).
- Hook `after`: hapus user, lepas header X-Forwarded-For dari proxy uji, dan tutup browser kedua. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- State global: header `X-Forwarded-For` yang disisipkan proxy uji dilepas pada langkah 13 dan di hook `after` sebagai cadangan; tidak ada state global lain (jam server, geo-IP, email service, dan counter rate limit tidak diubah) karena proxy uji khusus spec ini.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: proxy uji yang terdaftar sebagai trusted hop di backend dan dapat menyisipkan header `X-Forwarded-For` pada request login dari browser uji A; dua sesi browser bersamaan; reCAPTCHA mode uji di environment.
- Seeding state BE per user: profil BASE (trusted device ber-ID device browser uji A, login sukses sebelumnya, lokasi dan waktu login terakhir dari IP uji Jakarta, logout web terakhir kurang dari 30 hari, dan Authenticator terdaftar); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-174: Kolom IP Address entri login final mengikuti IP terkiri dari X-Forwarded-For hop terpercaya

1. Buka browser uji A (ID device dikenali) sebagai jendela baru tanpa sesi login
2. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
3. Ketik `intanrahmawati+{runId}-036@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Atur proxy uji (trusted hop terdaftar) agar menyisipkan header X-Forwarded-For `203.0.113.7, 10.0.0.5` pada request login
7. Catat penanda waktu (baseline) Activity Log Session dan User Log `Intan Rahmawati` sebelum klik [Log in]
8. Klik button [Log in] melalui proxy uji (login single-step)
9. Pindah ke browser kedua (sesi Total Control Global Settings), buka `Global Settings > Activity Log > Session`, dan cari entri `Intan Rahmawati` yang dibuat sesudah penanda waktu langkah 7
10. Verifikasi Entri `Intan Rahmawati` sesudah penanda waktu pada `Global Settings > Activity Log > Session`: Activity `Login`, Status `Success`, IP Address `203.0.113.7` (IP terpercaya terkiri)
11. Buka `Global Settings > User > Detail > User Log` untuk `Intan Rahmawati` dan cari entri yang dibuat sesudah penanda waktu langkah 7
12. Verifikasi Entri yang sama pada `Global Settings > User > Detail > User Log` menampilkan IP Address `203.0.113.7`
13. Lepas header X-Forwarded-For dari proxy uji

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness d (proxy uji dengan header X-Forwarded-For). Spec ini hanya satu TC.
- Baseline log (S-12): langkah 7 mencatat penanda waktu sebelum login; asersi langkah 10 dan 12 hanya membaca entri sesudah penanda itu.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah 1 (membuka browser uji A), perpindahan ke browser kedua, dan langkah 13 (melepas header X-Forwarded-For sebagai pemulihan state, dengan hook `after` sebagai cadangan).
- Temuan untuk QA:
  - TC-AUTH-MFA-174 Langkah Uji 5 menggabungkan penyisipan header di proxy dan klik [Log in] dalam satu langkah; spec memecahnya menjadi langkah 6 dan 8 tanpa mengubah isinya.
  - TC-AUTH-MFA-174 tidak menyebut Browser pada Data Uji; spec memakai browser uji A karena profil BASE berarti device dikenali dan login single-step.
  - Mekanisme seeding state BE profil BASE (trusted device ber-ID device browser uji A, riwayat login sukses, lokasi dan waktu login terakhir, Authenticator terdaftar) belum ada di Pre-setup (#20/#21) TC dan tidak didefinisikan di PRD atau LLD; spec tidak menyebut endpoint seeding.
  - Konfigurasi trusted hop pada backend dianggap sudah terpasang untuk proxy uji; TC tidak menyebut cara mendaftarkannya (dicatat di Prerequisites).
