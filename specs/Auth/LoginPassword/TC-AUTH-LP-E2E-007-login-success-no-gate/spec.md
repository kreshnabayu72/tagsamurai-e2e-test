---
id: TC-AUTH-LP-E2E-007-login-success-no-gate
title: "Login Berhasil Tanpa Gate Agreement dan MFA Menuju Portal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-69
  - TC-AUTH-LP-09
  - TC-AUTH-LP-81
coverage:
  web: automated
---

# Login Berhasil Tanpa Gate Agreement dan MFA Menuju Portal

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dengan status Activated dan Active. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-007` (contoh `budisantoso+{runId}-007@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis (fixture BE): user bertanda device terpercaya, lokasi sama seperti login sebelumnya, pernah login dan logout kurang dari 30 hari lalu di web, dan versi Privacy Policy terakhir yang disetujui sama dengan versi aktif, sehingga tidak ada gate Agreement dan MFA; reCAPTCHA mode uji di environment; ubah alamat tab browser lalu tekan Enter.
- Pemulihan: sesi login ditutup lewat logout di akhir spec; hook `after` menutup sesi yang tersisa bila spec gagal di tengah.
- TC-AUTH-LP-69: Tanpa login (guest); browser web
- TC-AUTH-LP-69: User `Budi Santoso` (`budisantoso+{runId}-007@qwertysystem.net`) berstatus Activated dan Active (di-seed lewat API di hook `before`; kondisi fixture BE di atas)
- TC-AUTH-LP-69 data: Email: `budisantoso+{runId}-007@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-09: User `Budi Santoso` (`budisantoso+{runId}-007@qwertysystem.net`) sudah login di web (sesi penuh aktif, dilanjutkan dari sesi TC-AUTH-LP-69 dalam spec yang sama)
- TC-AUTH-LP-81: Tanpa login (guest); browser web
- TC-AUTH-LP-81: User `Budi Santoso` (`budisantoso+{runId}-007@qwertysystem.net`, sama seperti TC-AUTH-LP-69); tidak ada kondisi Agreement
- TC-AUTH-LP-81 data: Email: `budisantoso+{runId}-007@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-69: Login berhasil tanpa gate Agreement dan MFA menuju Portal — Product Hub

1. Buka halaman Login with Password
2. Isi field Email dengan "budisantoso+{runId}-007@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
3. Selesaikan reCAPTCHA
4. Klik [Log in]
5. Verifikasi browser menuju Portal — Product Hub
6. Verifikasi Alert pesan server tidak tampil
7. Verifikasi layar Confirm to Continue dan halaman MFA tidak tampil
8. Muat ulang halaman Portal — Product Hub
9. Verifikasi user tetap berada di Portal — Product Hub (sesi penuh aktif)

### TC-AUTH-LP-09: User yang sudah login membuka halaman Login diarahkan ke Portal

10. Pada tab yang sama, ubah alamat ke halaman Login with Password
11. Tekan Enter
12. Verifikasi browser menuju Portal — Product Hub
13. Verifikasi form Login with Password, field Email, field Password, widget reCAPTCHA, link [Log in with OTP], dan link [Reset here] tidak tampil

### TC-AUTH-LP-81: Tanpa kondisi Agreement layar Confirm to Continue tidak tampil

14. Logout dari Portal — Product Hub
15. Buka halaman Login with Password
16. Isi field Email dengan "budisantoso+{runId}-007@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
17. Selesaikan reCAPTCHA
18. Klik [Log in]
19. Verifikasi layar Confirm to Continue tidak tampil
20. Verifikasi browser menuju Portal — Product Hub
21. Logout dari Portal — Product Hub

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-LP-09 membutuhkan sesi penuh aktif; sesi itu berasal dari login TC-AUTH-LP-69 dalam spec yang sama (bukan dari spec lain), sehingga urutan TC-AUTH-LP-69, 09, 81 dipertahankan dan sesuai rencana (S-06 tetap terpenuhi karena user di-seed oleh spec ini).
- Langkah penghubung (S-03): logout pada langkah 14 dan 21 (mengembalikan konteks ke guest sesuai precondition TC-AUTH-LP-81 dan membersihkan sesi); tanpa `Verifikasi`.
- Temuan untuk QA: tidak ada.
