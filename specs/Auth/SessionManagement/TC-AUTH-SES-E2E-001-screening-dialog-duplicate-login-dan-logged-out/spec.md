---
id: TC-AUTH-SES-E2E-001-screening-dialog-duplicate-login-dan-logged-out
title: "Screening Dialog Duplicate Login Attempt dan Dialog Logged Out"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-1
  - TC-AUTH-SES-2
  - TC-AUTH-SES-37
  - TC-AUTH-SES-38
coverage:
  web: automated
---

# Screening Dialog Duplicate Login Attempt dan Dialog Logged Out

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-1: `Budi Santoso` (`budisantoso+{runId}-001@qwertysystem.net`)
  - TC-AUTH-SES-2: `Siti Kusuma` (`sitikusuma+{runId}-001@qwertysystem.net`)
  - TC-AUTH-SES-37: `Agus Setiawan` (`agussetiawan+{runId}-001@qwertysystem.net`)
  - TC-AUTH-SES-38: `Rina Santoso` (`rinasantoso+{runId}-001@qwertysystem.net`)
- Sesi web aktif di Browser A untuk tiap user (status Active) dibuat di hook `before` lewat login API pada konteks Browser A: TC-AUTH-SES-1 dan 2 Chrome on Windows, TC-AUTH-SES-37 Firefox on Windows, TC-AUTH-SES-38 sesi dengan info device kosong (Tabel Data Uji Pre-setup #27, di-seed BE).
- Untuk TC-AUTH-SES-2, Browser A menampilkan Portal — Product Hub sebagai `Siti Kusuma` sebelum Browser B login (langkah penghubung 23).
- Browser A dan Browser B adalah konteks terpisah per user uji. Browser B untuk tiap TC adalah konteks baru yang belum login, dibuka pada langkah pembuka TC: TC-AUTH-SES-1, 2, dan 38 Firefox on macOS; TC-AUTH-SES-37 Chrome on Windows.
- Hook `after`: akhiri semua sesi seed, tutup konteks Browser A dan B, hapus keempat user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua konteks browser bersamaan dengan user agent yang dapat ditetapkan (Chrome on Windows, Firefox on Windows, Firefox on macOS) supaya info device pada dialog deterministik; seeding sesi dengan info device kosong; reCAPTCHA mode uji di environment (halaman Login with Password).
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A dan B.

## Test Steps

### TC-AUTH-SES-1: Screening Dialog Duplicate Login Attempt di device baru

1. Di Browser B (konteks baru, Firefox on macOS, belum login) buka halaman `Auth > Login with Password` → halaman Login with Password tampil
2. Ketik email `budisantoso+{runId}-001@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog Duplicate Login Attempt muncul
3. Susuri dialog dari atas ke bawah tanpa mengklik tombol apa pun
4. Verifikasi **Header**: Title "Duplicate Login Attempt"
5. Verifikasi **Header**: Dialog modal
6. Verifikasi **Header**: Severity warning
7. Verifikasi **Header**: Dialog memblokir halaman di belakangnya
8. Verifikasi **Body**: Body "You are already signed in on another device: Chrome on Windows. Confirm to log out that session and continue here."
9. Verifikasi Body hanya memuat nama browser dan sistem operasi sesi aktif; tidak memuat alamat IP dan tidak memuat nama user
10. Verifikasi **Footer**: [Confirm] (variant solid, severity warning)
11. Verifikasi **Footer**: [Cancel] (variant text, severity contrast) di sebelah [Confirm]
12. Verifikasi Kedua tombol enabled

### TC-AUTH-SES-37: Body Dialog Duplicate Login Attempt memuat browser dan OS sesi aktif tanpa IP dan nama user

13. Tutup konteks Browser B TC sebelumnya, buka konteks Browser B baru (Chrome on Windows, belum login), lalu buka `Auth > Login with Password` → halaman Login with Password tampil
14. Ketik email `agussetiawan+{runId}-001@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog Duplicate Login Attempt muncul
15. Verifikasi Body "You are already signed in on another device: Firefox on Windows. Confirm to log out that session and continue here."
16. Verifikasi Body tidak memuat alamat IP dan tidak memuat nama user

### TC-AUTH-SES-38: Dialog Duplicate Login Attempt saat info device sesi aktif kosong

17. Tutup konteks Browser B TC sebelumnya, buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka `Auth > Login with Password` → halaman Login with Password tampil
18. Ketik email `rinasantoso+{runId}-001@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog Duplicate Login Attempt muncul
19. Verifikasi Body "You are already signed in on another device: —. Confirm to log out that session and continue here." (Device Info kosong ditampilkan sebagai `—`)
20. Verifikasi Title "Duplicate Login Attempt" tetap tampil
21. Verifikasi [Confirm] tetap tampil
22. Verifikasi [Cancel] tetap tampil

### TC-AUTH-SES-2: Screening Dialog Logged Out di device lama

23. Pastikan Browser A menampilkan Portal — Product Hub sebagai `Siti Kusuma` (sesi seed di Browser A, Chrome on Windows)
24. Tutup konteks Browser B TC sebelumnya, buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka `Auth > Login with Password` → halaman Login with Password tampil
25. Ketik email `sitikusuma+{runId}-001@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog Duplicate Login Attempt muncul
26. Klik [Confirm] pada Dialog Duplicate Login Attempt
27. Pindah ke Browser A dan amati tanpa interaksi selama 10 detik (event push SSE) → Dialog Logged Out muncul
28. Susuri dialog dari atas ke bawah
29. Verifikasi **Header**: Title "Logged Out"
30. Verifikasi **Header**: Dialog modal
31. Verifikasi **Header**: Severity danger
32. Verifikasi **Header**: Tanpa tombol silang (X)
33. Verifikasi **Body**: Body "You have been logged out because another session was started on a different device."
34. Verifikasi **Footer**: [OK] (variant text, severity contrast) sebagai satu-satunya tombol

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-1, 37, 38, lalu 2 (urutan TC sumber 1, 2, 37, 38). TC-AUTH-SES-2 mengonfirmasi dialog sehingga mengakhiri sesi di Browser A; ditaruh paling akhir. Tiap TC memakai user dan pasangan Browser A/B sendiri, jadi urutan tidak membuat TC saling bergantung.
- TC-AUTH-SES-2 berdependensi pada TC-AUTH-SES-26 (Confirm mengaktifkan sesi baru dan meng-logout sesi lama); langkah 24–27 menyalin langkah dependensi itu (S-04). Asersi hasil Confirm itu sendiri diuji di spec `TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web`.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): perpindahan antar Browser A dan B; menyusuri dialog tanpa klik; menutup konteks Browser B TC sebelumnya dan membuka konteks Browser B baru di langkah pembuka TC (langkah 13, 17, dan 24); memastikan Browser A menampilkan Portal — Product Hub sebelum Browser B login (langkah 23), karena Dialog Logged Out harus tiba lewat push SSE ke halaman app yang terbuka dan Browser A hasil seeding API belum membuka halaman app.
- Temuan untuk QA: (1) TC-AUTH-SES-1, 2, 37, 38 menulis "klik [Log in]" tanpa menyebut widget reCAPTCHA pada halaman Login with Password (TC modul Auth lain mencentangnya); spec mengikuti TC dan mengandalkan reCAPTCHA mode uji di Prerequisites. (2) TC-AUTH-SES-1 menyebut "password yang benar" tanpa nilai; spec memakai `Spectra.env.SES_PASSWORD`.
