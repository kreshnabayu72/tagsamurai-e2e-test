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
  - TC-AUTH-LP-154
  - TC-AUTH-LP-157
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
- User `rinaseptiani@qwertysystem.net` berstatus aktif, logout terakhir di web >30 hari lalu (fixture BE), versi Privacy Policy yang disetujui sama dengan versi aktif, dan kotak masuk email dapat diakses.
- Fixture BE untuk mensimulasikan versi Privacy Policy aktif yang tidak ter-resolve / belum ada versi terpublikasi.

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

### Idle ≥30 hari: Agreement dievaluasi lebih dulu lalu handoff ke MFA

28. Buka jendela browser baru dan lakukan login dengan `rinaseptiani@qwertysystem.net` (logout terakhir >30 hari)
29. Verifikasi setelah submit password benar, layar Confirm to Continue tampil — halaman MFA dan Portal — Product Hub tidak tampil, dan sesi penuh belum dibuat
30. Centang checkbox persetujuan lalu klik tombol [Continue ➔]
31. Verifikasi browser menuju halaman MFA (bukan Portal — Product Hub) dan sesi penuh belum dibuat
32. Buka kotak masuk email `rinaseptiani@qwertysystem.net`
33. Verifikasi tidak ada email alert login tak biasa yang dikirimkan (idle ≥30 hari bukan kondisi login tak biasa)

### Versi Privacy Policy tidak dapat ditentukan: login ditolak (fail-closed)

34. Aktifkan fixture BE sehingga versi Privacy Policy aktif tidak ter-resolve / belum ada versi terpublikasi
35. Buka halaman Login with Password, masukkan `sitirahmawati@qwertysystem.net` dan password benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
36. Verifikasi toast error muncul dengan pesan persis: "Error, failed to log in."
37. Verifikasi layar Confirm to Continue tidak tampil dan browser tidak menuju Portal — Product Hub
38. Verifikasi form Login tetap terbuka dengan nilai Email dipertahankan
39. Verifikasi tidak ada entri log baru untuk percobaan ini
40. Nonaktifkan fixture dan kembalikan versi Privacy Policy aktif ke keadaan semula

## Notes

- Checkbox Agreement tidak pernah diletakkan di form login awal (`AUTHLP-LOGIC-03b`).
- Tiga kondisi pemicu Agreement: (a) login pertama di web, (b) idle >30 hari sejak logout terakhir, (c) versi Privacy Policy aktif lebih baru (`AUTHLP-LOGIC-03a`, PRD §9.2 F-AUTHLP-05).
- Untuk kondisi idle ≥30 hari, Agreement dievaluasi lebih dulu; MFA baru menyusul setelah Continue ditekan (GAP-451, `TC-AUTH-LP-154`) — idle bukan kondisi login tak biasa sehingga tidak ada email alert.
- Jika versi Privacy Policy aktif tidak dapat ditentukan, login gagal-closed dengan toast "Error, failed to log in.", tanpa sesi dan tanpa pencatatan log (`TC-AUTH-LP-157`, PRD §9.2 F-AUTHLP-05, `auth-foundation.md` §11.1).
- Teks persetujuan dan label checkbox mengikuti NC-09.
