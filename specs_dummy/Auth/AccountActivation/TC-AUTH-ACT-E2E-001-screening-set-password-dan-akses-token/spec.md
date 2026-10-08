---
id: TC-AUTH-ACT-E2E-001-screening-set-password-dan-akses-token
title: "Screening halaman Set Password, pembukaan link berulang, dan akses berbasis token"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-01
  - TC-AUTH-ACT-07
  - TC-AUTH-ACT-08
  - TC-AUTH-ACT-10
coverage:
  web: automated
---

# Screening halaman Set Password, pembukaan link berulang, dan akses berbasis token

## Prerequisites

- Browser publik tanpa sesi login untuk langkah screening; sesi admin Global Settings disiapkan di browser yang sama untuk kasus link dibuka dengan sesi aktif.
- User seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (3 user dengan email unik per run: `emailPrefix+<timestamp>+<rand>@example.com`).
- Admin Total Control Global Settings tersedia (`Spectra.env.ADMIN_USERNAME` / `Spectra.env.ADMIN_PASSWORD`).
- Akses API read-only untuk memverifikasi status token (`active`), status user (`Pending Activation`), dan jumlah entri log.
- Link aktivasi (raw token 43 karakter Base64URL) diambil dari Activation Email tiap user seeding.

## Test Steps

### Screening halaman Set Password (TC-AUTH-ACT-01)

1. Dalam keadaan tanpa sesi login, buka link aktivasi user seeding pertama.
2. Verifikasi card single-column (Elevated) tampil terpusat horizontal dan vertikal dengan logo TAG Samurai di tengah atas.
3. Verifikasi title halaman adalah "Set Your Password".
4. Verifikasi subtitle berbunyi "Set a password to log in for <email user seeding pertama>." dengan email tampil penuh tanpa di-mask.
5. Verifikasi field Password memiliki label "Password", placeholder "Enter your password", teks tersembunyi (masked) secara default, dan ikon toggle show/hide `EyeLine` di dalam field.
6. Verifikasi Password Policy di bawah field Password menampilkan 6 baris berurutan: "Minimum 8 characters", "One uppercase (A-Z)", "One lowercase (a-z)", "One number (0-9)", "One special character", "Password cannot contain spaces" — semua abu-abu (disabled) dengan ikon ○.
7. Verifikasi field Confirm Password memiliki label "Confirm Password", placeholder "Re-enter your password", teks tersembunyi (masked) secara default, dan ikon toggle `EyeLine` di dalam field.
8. Verifikasi tidak ada pesan error inline pada kedua field.
9. Verifikasi footer hanya berisi satu button "Set Password" full-width dalam keadaan enabled.
10. Verifikasi tidak ada button [Submit], [Clear Field], atau [Cancel], tidak ada link Resend Activation Email, dan tidak ada widget CAPTCHA di halaman.
11. Verifikasi token user seeding pertama tetap berstatus Active dan status user tetap Pending Activation (halaman hanya membaca).
12. Verifikasi tidak ada entri pencatatan baru dari Auth pada keempat surface log (Activity Log, User Log, System Log, Changelog).

### Pembukaan link valid dua kali tanpa submit (TC-AUTH-ACT-07)

13. Tutup tab tanpa mengisi atau mengklik apa pun.
14. Buka link aktivasi yang sama di tab baru.
15. Verifikasi pembukaan kedua tetap menampilkan halaman Set Password dengan subtitle email yang sama.
16. Verifikasi halaman Invalid Link tidak tampil (membuka link tidak meng-consume token) dan token masih Active.

### Akses tanpa sesi login (TC-AUTH-ACT-08)

17. Buka jendela browser baru tanpa sesi login, lalu buka link aktivasi user seeding kedua.
18. Verifikasi halaman Set Password tampil langsung tanpa redirect ke halaman Login.
19. Verifikasi tidak ada pesan sesi habis atau akses ditolak.

### Link valid dibuka dengan sesi login aktif milik user lain (TC-AUTH-ACT-10)

20. Pada browser yang sama, login sebagai Total Control Global Settings.
21. Buka link aktivasi user seeding ketiga di tab baru.
22. Verifikasi halaman Set Password untuk user seeding ketiga tampil normal tanpa redirect ke beranda sesi aktif.
23. Verifikasi sesi login aktif tidak berubah (browser masih login sebagai admin) dan status user seeding ketiga tetap Pending Activation dengan token Active.

## Notes

- Ketiga kasus memakai topik yang sama (membuka link aktivasi) sehingga digabung dalam satu spec; kasus dengan sesi login aktif ditambahkan sebagai langkah terakhir karena membutuhkan konteks akun berbeda.
- Kebutuhan teknis (sesi admin, API verifikasi token dan log) dicatat di Prerequisites, bukan di Notes.
- Id TC disebut pada subjudul blok agar report per langkah dapat dipetakan ke TC granular.
