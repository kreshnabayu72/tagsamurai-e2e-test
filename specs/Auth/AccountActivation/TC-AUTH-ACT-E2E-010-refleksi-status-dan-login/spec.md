---
id: TC-AUTH-ACT-E2E-010-refleksi-status-dan-login
title: "Refleksi Status Activated dan Login Setelah Aktivasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-98
  - TC-AUTH-ACT-106
  - TC-AUTH-ACT-107
  - TC-AUTH-ACT-108
coverage:
  web: automated
---

# Refleksi Status Activated dan Login Setelah Aktivasi

## Prerequisites

- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`.
- Password user uji dari `Spectra.env.ACT_PASSWORD`. Tidak ada password atau token di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD` (akun aktor), `ACT_PASSWORD` (password user uji).
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}`, lalu menghapusnya di hook `after` bersama logout sesi Login yang terbentuk pada TC-AUTH-ACT-108 (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-ACT-98: `Maya Ramadhan` (`mayaramadhan+{runId}-010@qwertysystem.net`), Pending Activation, token Active
  - TC-AUTH-ACT-106: `Ratna Safitri` (`ratnasafitri+{runId}-010@qwertysystem.net`), Pending Activation, token Active; link aktivasi diambil dari seeding API
  - TC-AUTH-ACT-107: `Wahyu Firmansyah` (`wahyufirmansyah+{runId}-010@qwertysystem.net`), Pending Activation, token Active
  - TC-AUTH-ACT-108: `Wahyu Maharani` (`wahyumaharani+{runId}-010@qwertysystem.net`), sudah Activated dengan token Consumed dan password `Spectra.env.ACT_PASSWORD`; disiapkan sendiri oleh spec ini lewat API (tidak bergantung pada aktivasi di TC lain)
- Kemampuan teknis: dua konteks browser (browser admin dan jendela privat publik); reCAPTCHA mode uji di environment.
- Hook `before` membuka browser admin dan login sebagai akun aktor Total Control (Global Settings); langkah uji hanya berpindah konteks ke browser itu.

## Test Steps

### TC-AUTH-ACT-98: Penolakan login user belum aktivasi dicatat oleh modul Login, bukan oleh Auth Account Activation

1. Buka jendela privat (tanpa sesi), buka `Auth > Login > Login with Password`, isi Email `mayaramadhan+{runId}-010@qwertysystem.net`, isi Password `Spectra.env.ACT_PASSWORD`, selesaikan reCAPTCHA, lalu klik [Log in]
2. Verifikasi pesan "Your account has not been activated" tampil
3. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`)
4. Buka `Global Settings > Activity Log > Session` dan cari entri untuk email `mayaramadhan+{runId}-010@qwertysystem.net`
5. Verifikasi Activity Log (Session) memuat entri Failed dengan Note `Account is not activated` yang berasal dari modul Login
6. Verifikasi Status user `Maya Ramadhan` tetap Pending Activation

### TC-AUTH-ACT-106: Aktivasi berhasil merefleksikan status Activated di Global Settings > User

7. Ganti konteks ke jendela privat, buka link aktivasi user `Ratna Safitri` → halaman `Auth > Account Activation > Set Password` tampil
8. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
9. Klik button "Set Password"
10. Ganti konteks ke browser admin, muat ulang `Global Settings > User > Login User` dan cari user `Ratna Safitri`
11. Buka `Global Settings > User > Detail` untuk user `Ratna Safitri`
12. Verifikasi user `Ratna Safitri` tidak lagi berbadge Pending Activation pada tabel
13. Verifikasi Status Badge pada Detail tidak lagi menampilkan Pending Activation
14. Verifikasi Status user `Ratna Safitri` Activated (milik Global Settings > User)

### TC-AUTH-ACT-107: User yang belum aktivasi ditolak login

15. Ganti konteks ke jendela privat baru (tanpa sesi), buka `Auth > Login > Login with Password`
16. Isi Email `wahyufirmansyah+{runId}-010@qwertysystem.net` dan Password `Spectra.env.ACT_PASSWORD`, selesaikan reCAPTCHA, lalu klik [Log in]
17. Verifikasi Pesan "Your account has not been activated" tampil dan login tidak diproses
18. Verifikasi Halaman tetap `Auth > Login > Login with Password`
19. Verifikasi Status user `Wahyu Firmansyah` tetap Pending Activation

### TC-AUTH-ACT-108: Setelah aktivasi, login dengan password baru tidak lagi ditolak karena belum aktivasi

20. Buka jendela privat baru (tanpa sesi login), buka `Auth > Login > Login with Password`
21. Isi Email `wahyumaharani+{runId}-010@qwertysystem.net` dan Password `Spectra.env.ACT_PASSWORD` (password yang ditetapkan saat aktivasi), selesaikan reCAPTCHA, lalu klik [Log in]
22. Verifikasi Pesan "Your account has not been activated" tidak tampil
23. Verifikasi Kredensial diterima: form kredensial Login with Password tidak ditampilkan lagi dan user diarahkan ke Confirm Agreement, MFA, atau Portal — Product Hub sesuai konfigurasi akun (detail tiap layar di-assert pada TC modul Login)
24. Verifikasi Status user `Wahyu Maharani` Activated

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Asersi absence TC-AUTH-ACT-98 ("tidak ada entri dari Auth Account Activation") dipindah ke E2E-029 (prinsip 13g); spec ini hanya memuat asersi pencatatan oleh modul Login. Pembagian TC dicatat juga di Notes E2E-029.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
