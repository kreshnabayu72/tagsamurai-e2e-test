---
id: TC-AUTH-SES-E2E-054-web-tidak-menawarkan-biometric
title: "Aplikasi Web Tidak Menawarkan Biometric"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-151
coverage:
  web: automated
---

# Aplikasi Web Tidak Menawarkan Biometric

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): satu user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`:
  - TC-AUTH-SES-151: `Dewi Utami` (`dewiutami+{runId}-054@qwertysystem.net`)
- Browser A (web, Chrome on Windows) belum login di awal spec.
- Hook `after`: akhiri sesi seed, tutup konteks Browser A, hapus user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji pada Browser A; akun aktor hanya di hook.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: satu konteks browser web; reCAPTCHA mode uji di environment (halaman Login with Password).

## Test Steps

### TC-AUTH-SES-151: Aplikasi web tidak menawarkan biometric setelah login

1. Di Browser A buka halaman `Auth > Login with Password` → halaman Login with Password tampil
2. Verifikasi Tidak ada opsi sign-in biometric di halaman Login web
3. Ketik email `dewiutami+{runId}-054@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
4. Verifikasi Tidak ada Prompt Enable Biometric
5. Verifikasi Tidak ada opsi sign-in biometric di Portal — Product Hub
6. Verifikasi Biometric hanya tersedia di aplikasi mobile: tidak ada kontrol biometric di halaman Login maupun Portal — Product Hub

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-14): TC-AUTH-SES-151 memeriksa halaman Login setelah login; setelah login halaman Login tidak lagi terlihat, sehingga spec memeriksa halaman Login sebelum login (langkah 1 sampai 2) lalu Portal — Product Hub sesudahnya.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): membuka halaman Login dan mengisi kredensial.
- Temuan untuk QA: (1) TC-AUTH-SES-151 menulis "Login web" tanpa menyebut tombol maupun widget reCAPTCHA pada halaman Login with Password (TC modul Auth lain mencentangnya); spec memakai tombol [Log in] sesuai label web TC lain dan mengandalkan reCAPTCHA mode uji di Prerequisites. (2) TC-AUTH-SES-151 menyebut "password yang benar" tanpa nilai; spec memakai `Spectra.env.SES_PASSWORD`. (3) TC-AUTH-SES-151 Expected b ("biometric hanya tersedia di aplikasi mobile") bukan hasil yang dapat diamati langsung di web; spec mengasersinya sebagai tidak adanya kontrol biometric di halaman Login dan Portal — Product Hub. (4) TC-AUTH-SES-151 tidak menyebut apakah Settings > Security web diperiksa; spec tidak memeriksanya.
