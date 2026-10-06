---
id: TC-AUTH-LP-E2E-010-agreement-gate-screening-dan-kondisi-pemicu
title: Screening layar Confirm to Continue dan tiga kondisi pemicu Agreement
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-07
  - TC-AUTH-LP-08
  - TC-AUTH-LP-77
  - TC-AUTH-LP-78
  - TC-AUTH-LP-79
  - TC-AUTH-LP-80
  - TC-AUTH-LP-81
  - TC-AUTH-LP-91
  - TC-AUTH-LP-141
coverage:
  web: automated
---

# Screening layar Confirm to Continue dan tiga kondisi pemicu Agreement

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `tonokurniawan@qwertysystem.net` berstatus aktif, versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui (kondisi c).
- User `sitirahmawati@qwertysystem.net` berstatus aktif dan belum pernah login di web (kondisi a - login pertama).
- User `ekosaputra@qwertysystem.net` berstatus aktif dan logout terakhir >30 hari lalu (kondisi b - idle >30 hari).
- User `budisantoso@qwertysystem.net` berstatus aktif tanpa kondisi pemicu agreement.

## Test Steps

### Ketiadaan checkbox Agreement di form Login

1. Buka halaman Login with Password di browser web
2. Masukkan email `tonokurniawan@qwertysystem.net`
3. Masukkan password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in]
4. Verifikasi Alert Danger "Incorrect email or password" tampil
5. Verifikasi tidak ada checkbox Agreement yang dirender di form Login dalam kondisi apa pun sebelum password benar diverifikasi

### Screening layar Confirm to Continue dan urutan Tab keyboard

6. Masukkan password benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
7. Verifikasi layar Confirm to Continue tampil
8. Verifikasi title layar adalah "Confirm to Continue"
9. Verifikasi Content Box scrollable memuat teks lengkap: "By accessing TAG Samurai, you agree to comply with our Privacy Policy. Please read the full document before continuing. Your continued use of the platform means you accept the terms described in the Privacy Policy."
10. Verifikasi tautan "Read the full Privacy Policy" tampil di dalam Content Box
11. Verifikasi Checkbox tampil dalam status unchecked dengan label "I have read and agree to the Privacy Policy *"
12. Verifikasi tombol [Continue ➔] tampil dalam keadaan solid, primary, lebar penuh, dan enabled
13. Verifikasi field Email, Password, tombol [Log in], dan link navigasi footer form login tidak tampil
14. Tekan tombol Tab berulang kali pada layar Confirm to Continue
15. Verifikasi urutan fokus keyboard berpindah dari Checkbox persetujuan, ke tautan dokumen, lalu ke tombol [Continue ➔]

### Interaksi tautan dokumen Privacy Policy

16. Klik tautan "Read the full Privacy Policy"
17. Verifikasi dokumen Privacy Policy terbuka pada tab baru browser
18. Kembali ke tab utama dan verifikasi layar Confirm to Continue tetap terbuka dengan checkbox tetap unchecked

### Verifikasi ketiga kondisi pemicu Agreement gate

19. Buka jendela browser baru dan lakukan login dengan `sitirahmawati@qwertysystem.net` (login pertama)
20. Verifikasi setelah submit password benar, layar Confirm to Continue langsung tampil sebelum halaman MFA atau Portal
21. Buka jendela browser baru dan lakukan login dengan `ekosaputra@qwertysystem.net` (logout terakhir >30 hari)
22. Verifikasi layar Confirm to Continue tampil
23. Buka jendela browser baru dan lakukan login dengan `budisantoso@qwertysystem.net` (tanpa ketiga kondisi pemicu)
24. Verifikasi layar Confirm to Continue TIDAK tampil dan browser langsung menuju Portal — Product Hub

### Sesi penuh tidak dibuat sebelum Agreement dikonfirmasi (Security)

25. Saat layar Confirm to Continue masih terbuka untuk `tonokurniawan@qwertysystem.net`, ubah URL browser secara manual ke URL Portal
26. Tekan Enter
27. Verifikasi browser me-redirect kembali ke halaman Login with Password karena sesi penuh belum terbentuk

## Notes

- Checkbox Agreement tidak pernah diletakkan di form login awal (`AUTHLP-LOGIC-03b`).
- Tiga kondisi pemicu Agreement: (a) login pertama di web, (b) idle >30 hari sejak logout terakhir, (c) versi Privacy Policy aktif lebih baru (`AUTHLP-LOGIC-03a`, PRD §9.2 F-AUTHLP-05).
- Teks persetujuan dan label checkbox mengikuti NC-09.
