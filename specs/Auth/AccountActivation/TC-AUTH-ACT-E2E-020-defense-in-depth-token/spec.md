---
id: TC-AUTH-ACT-E2E-020-defense-in-depth-token
title: "Cakupan Token, Pola Injeksi, dan Request Langsung ke Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-119
  - TC-AUTH-ACT-120
  - TC-AUTH-ACT-129
  - TC-AUTH-ACT-130
  - TC-AUTH-ACT-131
  - TC-AUTH-ACT-132
  - TC-AUTH-ACT-113
coverage:
  web: automated
---

# Cakupan Token, Pola Injeksi, dan Request Langsung ke Server

## Prerequisites

- Mode: FE+BE.
- Kemampuan teknis: klien HTTP untuk request langsung ke `POST /v2/iam/auth/activation/{token}/set-password` (melewati form); akses fixture BE untuk membentuk state user; jendela privat browser.
- Hook `before` (lewat API, email bersuffix per run):
  - TC-AUTH-ACT-129: user `Dimas Pratama` (`dimaspratama+{runId}-020@qwertysystem.net`) Pending Activation dengan token Active, lalu status user diubah menjadi Activated tanpa mengonsumsi token (fixture BE).
  - TC-AUTH-ACT-130: user `Eka Wulandari` (`ekawulandari+{runId}-020@qwertysystem.net`) Pending Activation dengan token Active, lalu kredensialnya diisi password (fixture BE).
  - TC-AUTH-ACT-113: user `Nina Permana` (`ninapermana+{runId}-020@qwertysystem.net`) dan `Galih Purnama` (`galihpurnama+{runId}-020@qwertysystem.net`) Pending Activation dengan token Active; link aktivasi diambil lewat API seeding.
- Hook `after`: hapus semua user yang dibuat spec ini.
- Password diambil dari environment variable `ACT_PASSWORD` (`Spectra.env.ACT_PASSWORD`). Kredensial akun aktor Total Control (Global Settings) diambil dari environment variable `GS_TC_PASSWORD` (`Spectra.env.GS_TC_PASSWORD`).
- TC-AUTH-ACT-119, 120, 129–132: tanpa login (halaman publik). TC-AUTH-ACT-113: aktivasi di jendela privat, verifikasi di browser admin yang login sbg Role: Total Control (Global Settings).
- Data token: `' OR '1'='1` (TC-AUTH-ACT-119), `<script>alert(1)</script>` (TC-AUTH-ACT-120), `tokenacaktidakdikenal123` (TC-AUTH-ACT-131).

## Test Steps

### TC-AUTH-ACT-119: Token berisi pola injeksi SQL diperlakukan sebagai token tidak valid

1. Buka link aktivasi dengan nilai token `' OR '1'='1` (di-URL-encode)
2. Verifikasi Halaman `Auth > Account Activation > Invalid Link` varian Expired tampil: Title "Activation Link Expired", Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
3. Verifikasi Tidak ada button CTA (tidak ada "Go to Login") pada halaman dan form Set Password tidak ditampilkan
4. Verifikasi Tidak ada pesan error teknis atau detail sistem pada halaman

### TC-AUTH-ACT-120: Token berisi skrip HTML tidak dieksekusi dan dianggap tidak valid

5. Buka link aktivasi dengan nilai token `<script>alert(1)</script>` (di-URL-encode)
6. Verifikasi Halaman `Auth > Account Activation > Invalid Link` varian Expired tampil: Title "Activation Link Expired", Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
7. Verifikasi Tidak ada button CTA (tidak ada "Go to Login") pada halaman dan form Set Password tidak ditampilkan
8. Verifikasi Tidak ada dialog skrip yang muncul dan teks token tidak ditampilkan di halaman

### TC-AUTH-ACT-129: User bukan lagi Pending Activation walau token masih Active: link dan submit ditolak

9. Buka link aktivasi user `Dimas Pratama`
10. Verifikasi Halaman `Auth > Account Activation > Invalid Link` varian Expired tampil; form Set Password tidak dirender
11. Kirim request Set Password langsung ke server dengan token yang sama, Password dan Confirm Password `Spectra.env.ACT_PASSWORD`
12. Verifikasi Server menolak 409 (request langsung tidak melewati FE sehingga tidak ada pengalihan halaman); password dan token tidak berubah (diperiksa lewat fixture BE)
13. Verifikasi Status user `Dimas Pratama` tetap Activated; token tidak berubah

### TC-AUTH-ACT-130: Kredensial user sudah memiliki password walau token masih Active: submit ditolak dan password tidak ditimpa

14. Kirim request Set Password langsung ke server dengan token user `Eka Wulandari`, Password dan Confirm Password `Spectra.env.ACT_PASSWORD`
15. Verifikasi Server menolak 409
16. Verifikasi Password yang sudah ada tidak berubah (kredensial diperiksa lewat fixture BE)
17. Verifikasi Token tidak berubah menjadi Consumed oleh request ini

### TC-AUTH-ACT-131: Submit dengan token yang tidak dikenal dijawab 404 dan diarahkan ke halaman Invalid Link

18. Kirim request Set Password langsung ke server dengan token `tokenacaktidakdikenal123`, Password dan Confirm Password `Spectra.env.ACT_PASSWORD`
19. Verifikasi Server menjawab 404 (bukan 409)
20. Verifikasi Tidak ada data yang berubah

### TC-AUTH-ACT-132: Submit dengan body tanpa token atau salah bentuk ditolak 400 dan ditampilkan sebagai S-20

21. Kirim request Set Password langsung ke server tanpa field token, dengan Password dan Confirm Password `Spectra.env.ACT_PASSWORD`
22. Verifikasi Request ditolak server dengan 400
23. Kirim request kedua dengan body bukan JSON yang valid
24. Verifikasi Request kedua ditolak server dengan 400
25. Verifikasi Tidak ada data yang berubah

### TC-AUTH-ACT-113: Token milik user A tidak dapat mengaktifkan user B

26. Buka jendela privat (tanpa sesi), buka link aktivasi user `Nina Permana` (token A), lakukan Set Password dengan `Spectra.env.ACT_PASSWORD`
27. Pindah ke browser admin: login sbg Role: Total Control (Global Settings), buka `Global Settings > User > Login User` dan cari user `Nina Permana` dan user `Galih Purnama`
28. Verifikasi Hanya user `Nina Permana` yang tidak lagi berbadge Pending Activation; user `Galih Purnama` tetap berbadge Pending Activation
29. Pindah kembali ke jendela privat dan buka link aktivasi user `Galih Purnama` (token B)
30. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for galihpurnama+{runId}-020@qwertysystem.net." (token B tetap valid)
31. Verifikasi Hanya user `Nina Permana` Activated; user `Galih Purnama` tetap Pending Activation dan token B Active

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness a (defense-in-depth: injeksi, request langsung, state dipaksa lewat fixture BE). TC-AUTH-ACT-129 dan 130 berasal dari E2E-015 (dihapus); TC-AUTH-ACT-131 dan 132 berasal dari E2E-019.
- TC-AUTH-ACT-113 mengaktifkan user (mengubah data), jadi ditaruh paling akhir. Browser admin di TC ini hanya dipakai untuk mengecek data (badge user), bukan untuk menguji race, sehingga TC tetap di kelas harness a.
- Tampilan state S-20 untuk respons 400 di form tidak diasersi di TC-AUTH-ACT-132 (request langsung tidak melewati form); tampilan itu diuji di spec 019 (TC-AUTH-ACT-118).
- Asersi pengalihan FE ke Invalid Link untuk request langsung (TC-AUTH-ACT-129, 130, 131) tidak dipakai: klien HTTP tidak memiliki FE, sehingga yang diasersi hanya respons server dan state data. TC sumber sudah disesuaikan 2026-10-08. Tampilan Invalid Link untuk token tidak dikenal diuji di spec 012 (TC-AUTH-ACT-79); untuk token yang sudah tidak berlaku diuji di spec 013 dan 014.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
