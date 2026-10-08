---
id: TC-AUTH-ACT-E2E-001-screening-set-password-valid-link
title: "Screening Halaman Set Password dari Link Aktivasi Valid"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-01
  - TC-AUTH-ACT-07
  - TC-AUTH-ACT-08
coverage:
  web: automated
---

# Screening Halaman Set Password dari Link Aktivasi Valid

## Prerequisites

- Seeding: setiap user Pending Activation dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`). Link aktivasi (token Active) diambil dari respons seeding API. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}` (contoh `budiaditya+{runId}-001@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: jendela privat (browser tanpa sesi login); membuka tab baru.
- TC-AUTH-ACT-01: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-01: User `Budi Aditya` (`budiaditya+{runId}-001@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-01 data: Link aktivasi user `Budi Aditya` (token Active)
- TC-AUTH-ACT-07: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-07: User `Agus Wijaya` (`aguswijaya+{runId}-001@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-07 data: Link aktivasi user `Agus Wijaya`, dibuka 2 kali
- TC-AUTH-ACT-08: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-08: User `Rina Handayani` (`rinahandayani+{runId}-001@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-08 data: Link aktivasi user `Rina Handayani`

## Test Steps

### TC-AUTH-ACT-01: Screening halaman Set Password saat link aktivasi valid dibuka

1. Buka link aktivasi user `Budi Aditya` di browser → halaman `Auth > Account Activation > Set Password` tampil
2. Susuri halaman dari atas ke bawah tanpa mengisi atau mengklik apa pun
3. Verifikasi bagian Header sesuai butir berikut
4. Verifikasi Card (Elevated) single-column, terpusat horizontal dan vertikal
5. Verifikasi Logo TAG Samurai di tengah atas
6. Verifikasi Title: "Set Your Password"
7. Verifikasi Subtitle: "Set a password to log in for budiaditya+{runId}-001@qwertysystem.net." — email tampil penuh, tidak di-mask
8. Verifikasi bagian Body sesuai butir berikut
9. Verifikasi Field Password: label "Password", placeholder "Enter your password", teks tersembunyi (masked) secara default, ikon toggle show/hide `EyeLine` di dalam field
10. Verifikasi Password Policy checklist di bawah field Password, 6 baris berurutan: "Minimum 8 characters" | "One uppercase (A-Z)" | "One lowercase (a-z)" | "One number (0-9)" | "One special character" | "Password cannot contain spaces" — semua baris abu-abu (disabled) dengan ikon ○
11. Verifikasi Field Confirm Password: label "Confirm Password", placeholder "Re-enter your password", masked secara default, ikon toggle show/hide `EyeLine` di dalam field
12. Verifikasi Tidak ada pesan error inline di kedua field
13. Verifikasi bagian Footer sesuai butir berikut
14. Verifikasi Satu button "Set Password" full-width, enabled
15. Verifikasi Tidak ada button [Submit], [Clear Field], atau [Cancel], tidak ada link Resend Activation Email, dan tidak ada widget CAPTCHA di halaman
16. Verifikasi Token aktivasi user `Budi Aditya` tetap Active (halaman hanya membaca)

### TC-AUTH-ACT-07: Membuka link valid dua kali tanpa submit tetap menampilkan form Set Password

17. Buka link aktivasi user `Agus Wijaya` di browser → halaman `Auth > Account Activation > Set Password` tampil
18. Tutup tab tanpa mengisi atau submit apa pun
19. Buka kembali link aktivasi yang sama di tab baru
20. Verifikasi Pembukaan pertama dan kedua sama-sama menampilkan `Auth > Account Activation > Set Password` dengan Subtitle "Set a password to log in for aguswijaya+{runId}-001@qwertysystem.net."
21. Verifikasi Pembukaan kedua tidak menampilkan halaman Invalid Link (membuka link tidak meng-consume token)
22. Verifikasi Token aktivasi user `Agus Wijaya` tetap Active

### TC-AUTH-ACT-08: Link valid dibuka tanpa sesi login menampilkan Set Password tanpa redirect ke Login

23. Pastikan browser tidak memiliki sesi login (jendela privat baru)
24. Buka link aktivasi user `Rina Handayani` di browser → halaman `Auth > Account Activation > Set Password` tampil
25. Verifikasi `Auth > Account Activation > Set Password` tampil langsung
26. Verifikasi Tidak ada redirect ke halaman Login dan tidak ada pesan sesi habis atau akses ditolak
27. Verifikasi Token aktivasi user `Rina Handayani` tetap Active

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-ACT-01 terbagi lintas spec: asersi "tidak ada entri pencatatan dari Auth" (Expected Result b) diuji di spec `TC-AUTH-ACT-E2E-017-zero-logging-absence` (kelas g, prinsip 10).
