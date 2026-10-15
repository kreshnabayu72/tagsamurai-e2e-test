---
id: TC-AUTH-RST-E2E-029-login-with-new-password
title: "Login dengan Password Baru, Password Lama Ditolak, dan Sifat Case-Sensitive"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-111
  - TC-AUTH-RST-112
coverage:
  web: automated
---

# Login dengan Password Baru, Password Lama Ditolak, dan Sifat Case-Sensitive

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-029@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD` dan tanpa gate Agreement dan MFA (fixture BE). Di hook `before`, satu token reset aktif diterbitkan lewat API Request (Request dari hook ikut dihitung pada counter rate limit per IP penguji) dan tautannya diambil dari mail-catcher, lalu Submit New Password sukses dijalankan lewat API dengan password baru `Spectra.env.RST_PASSWORD_NEW` (setara TC-AUTH-RST-82). User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`, `RST_PASSWORD_LOWER`.
- Kemampuan teknis: mail-catcher dengan pencatatan jumlah email per alamat dan pembacaan tautan reset dari email (dipakai hook `before`); reCAPTCHA mode uji; jendela privat tanpa sesi login.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- Hook `after` menutup semua jendela privat, menghapus sesi browser, dan mengembalikan sesi ke akun default suite.
- TC-AUTH-RST-111, TC-AUTH-RST-112: User belum login (guest); browser web.
- TC-AUTH-RST-112 data: Password `Spectra.env.RST_PASSWORD_LOWER` = varian huruf kecil dari `Spectra.env.RST_PASSWORD_NEW` (nilai diisi di env).

## Test Steps

### TC-AUTH-RST-112: Password baru bersifat case-sensitive

1. Buka jendela privat baru lalu buka halaman Login with Password
2. Login dengan Email `budisantoso+{runId}-029@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_LOWER` (varian huruf kecil, selesaikan reCAPTCHA)
3. Verifikasi Alert Danger "Incorrect email or password" tampil
4. Verifikasi login ditolak

### TC-AUTH-RST-111: Login dengan password baru berhasil dan password lama ditolak

5. Muat ulang halaman Login with Password (F5)
6. Login dengan Email `budisantoso+{runId}-029@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD` (password lama, selesaikan reCAPTCHA)
7. Verifikasi Alert Danger "Incorrect email or password" tampil
8. Verifikasi login ditolak
9. Login dengan Email `budisantoso+{runId}-029@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_NEW`
10. Verifikasi login berhasil
11. Verifikasi browser menuju Portal — Product Hub

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Urutan: TC-AUTH-RST-112 lebih dulu karena login berhasil di TC-AUTH-RST-111 mengakhiri spec; dua kegagalan login berturut-turut tidak mencapai ambang lock. Alur Submit disalin sebagai seeding API (S-04).
- Nilai `Spectra.env.RST_PASSWORD_LOWER` didaftarkan sebagai env var terpisah supaya password tidak ditulis di spec; `RST_PASSWORD_WRONG` khusus spec 031 (password salah format valid). `RST_PASSWORD_LOWER` terdaftar di `spectra.config.ts` dan `.env.example`.
