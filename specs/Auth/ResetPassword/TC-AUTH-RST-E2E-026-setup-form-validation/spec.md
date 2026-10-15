---
id: TC-AUTH-RST-E2E-026-setup-form-validation
title: "Validasi Form Setup New Password: Field Wajib dan Konfirmasi Cocok"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-71
  - TC-AUTH-RST-72
  - TC-AUTH-RST-73
  - TC-AUTH-RST-74
coverage:
  web: automated
---

# Validasi Form Setup New Password: Field Wajib dan Konfirmasi Cocok

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-026@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`; satu token reset aktif diterbitkan di hook `before` lewat API Request, tautan diambil dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`, `RST_PASSWORD_ALT`.
- Kemampuan teknis: mail-catcher; jendela privat tanpa sesi login.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat suite.md); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-71, TC-AUTH-RST-72, TC-AUTH-RST-73, TC-AUTH-RST-74: User belum login (guest); browser web; Setup New Password terbuka dari tautan reset; semua kasus berakhir pada submit yang diblokir sehingga token tetap active dan password tidak berubah.
- TC-AUTH-RST-71 data: Confirm Password `Spectra.env.RST_PASSWORD_NEW`.
- TC-AUTH-RST-72 data: Password `Spectra.env.RST_PASSWORD_NEW`.
- TC-AUTH-RST-74 data: Password `Spectra.env.RST_PASSWORD_NEW`; Confirm Password `Spectra.env.RST_PASSWORD_ALT`.

## Test Steps

### TC-AUTH-RST-73: Password dan Confirm Password kosong sekaligus

1. Buka jendela privat baru lalu buka tautan reset milik `budisantoso+{runId}-026@qwertysystem.net` dari mail-catcher sehingga Setup New Password tampil
2. Klik Button [Reset Password]
3. Verifikasi caption inline pada field Password: "Password must not be empty"
4. Verifikasi caption inline pada field Confirm Password: "Confirm password must not be empty" tampil bersamaan dengan caption field Password
5. Verifikasi kedua field berstatus Invalid
6. Verifikasi browser tetap di halaman Setup New Password

### TC-AUTH-RST-71: Password kosong dan Confirm Password terisi

7. Muat ulang halaman Setup New Password (F5)
8. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Confirm Password
9. Klik Button [Reset Password]
10. Verifikasi caption inline pada field Password: "Password must not be empty"
11. Verifikasi field Password berstatus Invalid
12. Verifikasi browser tetap di halaman Setup New Password

### TC-AUTH-RST-72: Password terisi dan Confirm Password kosong

13. Muat ulang halaman Setup New Password (F5)
14. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password
15. Klik Button [Reset Password]
16. Verifikasi caption inline pada field Confirm Password: "Confirm password must not be empty"
17. Verifikasi field Confirm Password berstatus Invalid
18. Verifikasi browser tetap di halaman Setup New Password

### TC-AUTH-RST-74: Confirm Password berbeda dari Password

19. Muat ulang halaman Setup New Password (F5)
20. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password
21. Ketik `Spectra.env.RST_PASSWORD_ALT` pada field Confirm Password
22. Klik Button [Reset Password]
23. Verifikasi caption inline pada field Confirm Password: "Passwords do not match"
24. Verifikasi field Confirm Password berstatus Invalid
25. Verifikasi browser tetap di halaman Setup New Password

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Semua kasus adalah validasi yang diblokir; satu token dipakai bersama dan tidak dikonsumsi. Muat ulang halaman antar-TC adalah langkah penghubung (S-09, S-03).
- Urutan TC: TC-AUTH-RST-73 sebelum 71, 72, dan 74 (kosong sekaligus lebih dulu); perubahan urutan dari TC sumber hanya untuk mengelompokkan validasi tanpa isi lebih dulu (S-05).
- Temuan untuk QA: Post Condition TC-AUTH-RST-71 sampai 74 (token tetap active, password user tidak berubah) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Temuan untuk QA: Post Condition "tidak ada entri log" TC-AUTH-RST-71, 72, 73, dan 74 tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-05, S-15).
