---
id: TC-AUTH-LP-E2E-005-login-berhasil-happy-path-tanpa-gate
title: Login berhasil tanpa trigger Agreement maupun MFA lintas tier plan
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-09
  - TC-AUTH-LP-18
  - TC-AUTH-LP-69
  - TC-AUTH-LP-76
coverage:
  web: automated
---

# Login berhasil tanpa trigger Agreement maupun MFA lintas tier plan

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `budisantoso@qwertysystem.net` berstatus Activated dan Active; device terpercaya; login dan logout terakhir kurang dari 30 hari lalu; versi Privacy Policy yang disetujui identik dengan versi aktif saat ini.
- Akun perwakilan dari 5 tier plan: `starter.user@qwertysystem.net` (Starter), `growth.user@qwertysystem.net` (Growth), `professional.user@qwertysystem.net` (Professional), `enterprise.user@qwertysystem.net` (Enterprise), `custom.user@qwertysystem.net` (Custom) aktif dan terkonfigurasi.

## Test Steps

### Login berhasil dengan penanganan whitespace pada Email

1. Buka halaman Login with Password di browser web
2. Masukkan email dengan spasi di awal dan di akhir ` budisantoso@qwertysystem.net ` pada field Email
3. Masukkan password `QaLogin#2026` pada field Password
4. Selesaikan reCAPTCHA
5. Klik tombol [Log in]
6. Verifikasi sistem melakukan trim whitespace pada email dan browser dialihkan ke Portal — Product Hub
7. Verifikasi sesi penuh berhasil dibuat dan cookies / storage sesi autentikasi tersimpan
8. Muat ulang (F5) halaman Portal — Product Hub
9. Verifikasi sesi tetap bertahan dan user tetap berada di Portal tanpa diminta login ulang

### Direct navigasi ke halaman Login saat sesi aktif dialihkan ke Portal

10. Buka tab baru atau ubah URL browser secara langsung ke `/login`
11. Tekan tombol Enter
12. Verifikasi sistem mendeteksi sesi aktif dan langsung me-redirect browser kembali ke Portal — Product Hub
13. Verifikasi form login tidak dirender untuk user yang sudah memiliki sesi aktif
14. Lakukan logout dari Portal

### Paritas alur login tanpa perbedaan perlakuan lintas tier plan

15. Buka kembali halaman Login with Password
16. Login menggunakan akun plan Starter (`starter.user@qwertysystem.net`) dan verifikasi berhasil masuk ke Portal tanpa dialog upsell
17. Lakukan logout
18. Login menggunakan akun plan Growth (`growth.user@qwertysystem.net`) dan verifikasi berhasil masuk ke Portal
19. Lakukan logout
20. Login menggunakan akun plan Professional (`professional.user@qwertysystem.net`) dan verifikasi berhasil masuk ke Portal
21. Lakukan logout
22. Login menggunakan akun plan Enterprise (`enterprise.user@qwertysystem.net`) dan verifikasi berhasil masuk ke Portal
23. Lakukan logout
24. Login menggunakan akun plan Custom (`custom.user@qwertysystem.net`) dan verifikasi berhasil masuk ke Portal
25. Lakukan logout

## Notes

- Modul login bersifat agnostik terhadap paket langganan (PRD §9.10); semua tingkatan plan memiliki pengalaman form dan validasi login yang identik tanpa plan-gating pra-login.
- Email dengan spasi di awal atau akhir otomatis di-trim oleh sistem saat pencocokan akun (TC-AUTH-LP-18).
