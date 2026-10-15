---
id: TC-AUTH-RST-E2E-034-double-submit
title: "Klik Ganda Button Reset Password pada Request dan Setup New Password"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-89
  - TC-AUTH-RST-93
coverage:
  web: automated
---

# Klik Ganda Button Reset Password pada Request dan Setup New Password

## Prerequisites

- Mode: FE+BE.
- Seeding: dua user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD`. Untuk TC-AUTH-RST-93, satu token reset aktif diterbitkan di hook `before` lewat API Request, tautan dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Hook `before` (akun aktor): membuka jendela privat guest dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA) lalu membuka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password". Hook `after` menutup kedua jendela dan mengembalikan sesi ke akun default suite.
- Kemampuan teknis: klik ganda cepat (dua klik beruntun dalam waktu sangat singkat); mail-catcher dengan pembacaan jumlah email per alamat; reCAPTCHA mode uji; jendela guest dan jendela admin terpisah (admin membaca Activity Log Session).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat suite.md); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-89, TC-AUTH-RST-93: User belum login (guest); browser web.
- TC-AUTH-RST-89: User `Budi Santoso` (`budisantoso+{runId}-034a@qwertysystem.net`) Active.
- TC-AUTH-RST-93: User `Citra Dewi` (`citradewi+{runId}-034b@qwertysystem.net`) Active; Password dan Confirm Password `Spectra.env.RST_PASSWORD_NEW`.

## Test Steps

### TC-AUTH-RST-89: Klik ganda Button Reset Password hanya menerbitkan satu token dan satu email

1. Di jendela guest buka halaman Reset Password (Request)
2. Ketik `budisantoso+{runId}-034a@qwertysystem.net` pada field Email dan selesaikan reCAPTCHA (centang "I'm not a robot")
3. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-034a@qwertysystem.net` sebagai baseline
4. Klik dua kali cepat pada Button [Reset Password]
5. Verifikasi hanya satu permintaan diproses
6. Verifikasi browser menuju halaman Email Sent!
7. Periksa mail-catcher
8. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-034a@qwertysystem.net` bertambah tepat 1 dibanding baseline

### TC-AUTH-RST-93: Klik ganda Button Reset Password pada Setup New Password hanya memproses satu submit

9. Pindah ke jendela admin, muat ulang Activity Log Session, dan catat jumlah baris Success `Password updated successfully` milik user `Citra Dewi` sebagai baseline
10. Pindah ke jendela guest
11. Buka tautan reset milik `citradewi+{runId}-034b@qwertysystem.net` dari mail-catcher sehingga Setup New Password tampil
12. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password
13. Klik dua kali cepat pada Button [Reset Password]
14. Verifikasi browser menuju halaman Password Reset Successful
15. Verifikasi Halaman 404 tidak tampil
16. Pindah ke jendela admin dan muat ulang Activity Log Session
17. Verifikasi jumlah baris Success `Password updated successfully` untuk user `Citra Dewi` bertambah tepat 1 dibanding baseline

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Langkah penghubung (S-03): pindah jendela guest dan admin, muat ulang log, dan pencatatan baseline (S-12).
- Temuan untuk QA: Post Condition TC-AUTH-RST-89 (tepat satu token berstatus active, counter per email bertambah 1) dan TC-AUTH-RST-93 (token berstatus consumed, password user menjadi baru) tidak punya langkah observasi di TC sehingga tidak diasersi; satu email dan satu entri log tidak membuktikan status token, counter, atau password (S-01, S-15).
