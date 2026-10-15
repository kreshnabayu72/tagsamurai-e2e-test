---
id: TC-AUTH-RST-E2E-033-biometric-refresh-token-revoked
title: "Reset Sukses Mencabut Refresh Token Biometric"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-140
coverage:
  web: automated
  mobile: automated
---

# Reset Sukses Mencabut Refresh Token Biometric

## Prerequisites

- Mode: FE+BE (kelas d: hardware biometrik).
- Seeding: user subjek `Rina Kartika` (`rinakartika+{runId}-033@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`. Opt-in biometric aktif di aplikasi native Android TAG Samurai Mobile dengan refresh token biometric aktif (fixture BE); satu token reset aktif diterbitkan lewat API Request, tautan dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Kemampuan teknis: perangkat Android dengan sensor biometrik (atau emulator yang mensimulasikan biometrik) dan aplikasi TAG Samurai Mobile; browser web tanpa sesi login; mail-catcher.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat suite.md); mekanisme reset disediakan tim FE/BE.
- Hook `after` menutup semua jendela privat, menghapus sesi browser, mereset opt-in biometric di aplikasi Android, dan mengembalikan sesi ke akun default suite.
- TC-AUTH-RST-140: User belum login di web (guest); Password baru `Spectra.env.RST_PASSWORD_NEW` pada Password dan Confirm Password.

## Test Steps

### TC-AUTH-RST-140: Reset sukses mencabut refresh token biometric

1. Di browser web tanpa sesi login, buka tautan reset milik `rinakartika+{runId}-033@qwertysystem.net` dari mail-catcher
2. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password lalu klik Button [Reset Password]
3. Verifikasi halaman Password Reset Successful tampil
4. Di aplikasi mobile, buka layar login lalu coba login dengan biometric
5. Verifikasi login biometric ditolak
6. Verifikasi aplikasi meminta login ulang dengan password

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md` (Manual Only; kemampuan hardware ditulis di Prerequisites).
