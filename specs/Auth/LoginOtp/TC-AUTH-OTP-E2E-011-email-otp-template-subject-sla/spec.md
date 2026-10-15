---
id: TC-AUTH-OTP-E2E-011-email-otp-template-subject-sla
title: "Isi, Subject, dan Waktu Penerimaan Email OTP"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-37
  - TC-AUTH-OTP-38
  - TC-AUTH-OTP-39
coverage:
  web: automated
---

# Isi, Subject, dan Waktu Penerimaan Email OTP

## Prerequisites

- Mode: FE+BE (kelas harness eksternal: pembacaan isi dan waktu email di mail-catcher).
- Tidak ada akun aktor. Browser tanpa sesi login (halaman Login with OTP adalah halaman publik).
- Environment variable: `OTP_PASSWORD` (password user uji yang dipasang saat seeding; tidak ada password atau token di spec atau fixture). Nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-011`, profil BASE (Activated, Active ON, sudah login sukses di web pada device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru ada; Agreement dan MFA tidak terpicu), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-37: `Joko Nugroho` (`jokonugroho+{runId}-011@qwertysystem.net`); nama tampilan user harus `Joko Nugroho` karena dipakai pada sapaan email
  - TC-AUTH-OTP-38: `Anisa Aditya` (`anisaaditya+{runId}-011@qwertysystem.net`)
  - TC-AUTH-OTP-39: `Bagas Maulana` (`bagasmaulana+{runId}-011@qwertysystem.net`)
- Kemampuan teknis: mail-catcher lingkungan uji yang dapat membaca subject, isi (teks dan ada tidaknya button atau tautan), dan waktu masuk email per alamat; pencatatan waktu klik [Request OTP] dengan jam yang sama dengan waktu masuk email; reCAPTCHA mode uji di environment (centang tanpa tantangan).

## Test Steps

### TC-AUTH-OTP-37: Isi email OTP sesuai template Verification Code

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser tanpa sesi
2. Ketik `jokonugroho+{runId}-011@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Buka email OTP yang masuk di mail-catcher untuk `jokonugroho+{runId}-011@qwertysystem.net`
6. Verifikasi sapaan: "Hi Joko Nugroho,"
7. Verifikasi paragraf pembuka: "We received a request to sign in to your TAG Samurai account. Use the one-time password (OTP) below to complete your login:"
8. Verifikasi kode OTP 6 digit numerik tampil menonjol sebagai teks
9. Verifikasi tidak ada button dan tidak ada tautan untuk diklik pada email
10. Verifikasi paragraf masa berlaku: "This one-time password is valid for 5 minutes and can only be used once. If it expires before you enter it, go back to the login page and request a new code."
11. Verifikasi paragraf penutup: "To keep your data secure, please don't share this code with anyone. If you didn't request this, you can safely ignore this email."
12. Verifikasi penutup: "— TAG Samurai"

### TC-AUTH-OTP-38: Subject email OTP

13. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
14. Ketik `anisaaditya+{runId}-011@qwertysystem.net` pada field Email
15. Centang widget reCAPTCHA "I'm not a robot"
16. Klik button [Request OTP]
17. Buka email OTP yang masuk di mail-catcher untuk `anisaaditya+{runId}-011@qwertysystem.net` dan baca subject-nya
18. Verifikasi subject email OTP: "Your TAG Samurai one-time password (OTP)"

### TC-AUTH-OTP-39: Email OTP diterima dalam 2 menit setelah Request OTP

19. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
20. Ketik `bagasmaulana+{runId}-011@qwertysystem.net` pada field Email
21. Centang widget reCAPTCHA "I'm not a robot"
22. Klik button [Request OTP] dan catat waktu klik
23. Buka mail-catcher untuk `bagasmaulana+{runId}-011@qwertysystem.net` dan catat waktu email OTP masuk
24. Verifikasi email OTP masuk paling lambat 2 menit setelah [Request OTP] diklik

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 13 dan 19 (buka ulang halaman Request OTP) adalah langkah penghubung antar-TC (S-03); tiap TC memakai user sendiri.
- TC-AUTH-OTP-37 butir c dipecah menjadi dua `Verifikasi` (langkah 8 dan 9) dan butir a sampai f masing-masing satu `Verifikasi` (S-01).
- Temuan untuk QA: (1) TC-AUTH-OTP-39 hanya menyatakan batas 2 menit tanpa menyebut sumber waktu masuk email (waktu mail-catcher atau header email); spec memakai waktu masuk di mail-catcher. (2) TC-AUTH-OTP-37 tidak menyebut apakah kode OTP pada email harus sama dengan kode yang diterima layar Verify OTP; hanya format 6 digit numerik yang diasersi.
