---
id: TC-AUTH-RST-E2E-024-screening-setup-new-password
title: "Screening Halaman Setup New Password, State Awal, ARIA, Tab, dan Toggle Intip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-63
  - TC-AUTH-RST-64
  - TC-AUTH-RST-65
  - TC-AUTH-RST-66
  - TC-AUTH-RST-70
coverage:
  web: automated
---

# Screening Halaman Setup New Password, State Awal, ARIA, Tab, dan Toggle Intip

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-024@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`; satu token reset aktif diterbitkan di hook `before` lewat API Request, tautan diambil dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Kemampuan teknis: mail-catcher; jendela privat tanpa sesi login; tombol Tab keyboard; inspeksi atribut DOM (`aria-describedby`, `aria-live`).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat suite.md); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-63, TC-AUTH-RST-64, TC-AUTH-RST-65, TC-AUTH-RST-66, TC-AUTH-RST-70: User belum login (guest); browser web.
- TC-AUTH-RST-70 data: Password dan Confirm Password: `Spectra.env.RST_PASSWORD_NEW`.

## Test Steps

### TC-AUTH-RST-63: Screening halaman Setup New Password di web

1. Buka jendela privat baru lalu buka tautan reset milik `budisantoso+{runId}-024@qwertysystem.net` dari mail-catcher
2. Susuri halaman dari atas ke bawah tanpa klik apa pun
3. Verifikasi **Header**: Logo TAG Samurai di tengah atas
4. Verifikasi **Header**: Title "Setup New Password"
5. Verifikasi **Header**: Subtitle "Set a new password to log in for budisantoso+{runId}-024@qwertysystem.net."
6. Verifikasi **Body**: field Password (wajib) berlabel "New Password"
7. Verifikasi **Body**: field Password memiliki placeholder "Enter new password"
8. Verifikasi **Body**: field Password memiliki ikon toggle intip
9. Verifikasi **Body**: Password Policy Checklist 6 baris: "Minimum 8 characters", "One uppercase (A-Z)", "One lowercase (a-z)", "One number (0-9)", "One special character", "Password cannot contain spaces"
10. Verifikasi **Body**: field Confirm Password (wajib) berlabel "Confirm Password"
11. Verifikasi **Body**: field Confirm Password memiliki placeholder "Confirm new password"
12. Verifikasi **Body**: field Confirm Password memiliki ikon toggle intip
13. Verifikasi **Footer**: Button [Reset Password] tampil
14. Verifikasi **Footer**: Button [Reset Password] bergaya solid
15. Verifikasi **Footer**: Button [Reset Password] bergaya primary
16. Verifikasi **Footer**: Button [Reset Password] berlebar penuh
17. Verifikasi **Must NOT**: widget reCAPTCHA, tombol [Clear Field], tombol tutup [✕], dan dialog Unsaved Changes tidak ada (anchor: Button [Reset Password] tampil)

### TC-AUTH-RST-64: State awal form Setup New Password

18. Amati field, checklist, dan Button [Reset Password]
19. Verifikasi field Password dan Confirm Password kosong dengan placeholder masing-masing
20. Verifikasi karakter pada field Password dan Confirm Password tersembunyi (masked)
21. Verifikasi keenam item checklist berstatus belum terpenuhi
22. Verifikasi ikon keenam item checklist berupa lingkaran kosong abu-abu
23. Verifikasi teks keenam item checklist berwarna abu-abu
24. Verifikasi Button [Reset Password] enabled
25. Verifikasi Button [Reset Password] tanpa spinner
26. Verifikasi tidak ada caption error pada kedua field

### TC-AUTH-RST-66: Accessibility field Password dan checklist

27. Periksa atribut DOM field Password dan item checklist
28. Verifikasi input Password memiliki `aria-describedby="password-policy-checklist"`
29. Verifikasi item checklist memiliki `aria-live="polite"`

### TC-AUTH-RST-65: Urutan Tab keyboard pada halaman Setup New Password

30. Klik field Password
31. Tekan Tab berulang kali sambil mencatat elemen yang fokus
32. Verifikasi urutan fokus: field Password, toggle intip Password, field Confirm Password, toggle intip Confirm Password, Button [Reset Password]

### TC-AUTH-RST-70: Toggle intip pada Password dan Confirm Password bekerja independen

33. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan `Spectra.env.RST_PASSWORD_NEW` pada field Confirm Password
34. Verifikasi kedua field masked
35. Klik ikon toggle pada field Password
36. Verifikasi field Password menampilkan teks password
37. Verifikasi field Confirm Password tetap masked
38. Klik ikon toggle pada field Confirm Password
39. Verifikasi kedua field menampilkan teks password
40. Klik ikon toggle pada field Password sekali lagi
41. Verifikasi field Password kembali masked
42. Verifikasi field Confirm Password tetap terlihat

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Screening di awal, lalu state awal, ARIA, dan Tab sebelum mengetik; toggle intip di akhir karena mengisi field. Tidak ada submit sehingga token tidak dikonsumsi.
- Urutan TC di spec: TC-AUTH-RST-66 sebelum TC-AUTH-RST-65 (keduanya tanpa input); TC-AUTH-RST-70 terakhir karena mengisi field. Perubahan urutan dari TC sumber dicatat di sini (S-05).
- Temuan untuk QA: TC-AUTH-RST-70 expected "Setelah langkah 1: kedua field masked" mengacu ke langkah 1 yang hanya membuka tautan; maksudnya setelah mengetik (langkah 2) (S-15).
- Jumlah langkah 42 melampaui ±35: alasan Verifikasi dipecah per klausa sesuai S-01 (32 dari 42 langkah adalah Verifikasi; 10 sisanya aksi mengamati, mengetik, menekan Tab, dan klik toggle). Satu topik (halaman Setup New Password), satu kelas harness (fungsional, tanpa submit, satu form), tanpa prefix login berulang (tidak ada login).
