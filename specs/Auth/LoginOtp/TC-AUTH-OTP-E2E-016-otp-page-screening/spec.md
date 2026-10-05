---
id: TC-AUTH-OTP-E2E-016-otp-page-screening
title: Screening elemen halaman Input OTP (judul, unmasked email subtitle, 6 box, autofocus, tanpa tombol Verify)
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-31
  - TC-AUTH-OTP-36
  - TC-AUTH-OTP-37
coverage:
  web: automated
---

# Screening elemen halaman Input OTP (judul, unmasked email subtitle, 6 box, autofocus, tanpa tombol Verify)

## Prerequisites

- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Alur Request OTP telah berhasil dilakukan untuk user tersebut

## Test Steps

1. Amati tampilan antarmuka halaman Input OTP segera setelah pengalihan dari halaman Request OTP
2. Verifikasi judul halaman menampilkan teks "Enter verification code"
3. Verifikasi subtitle halaman menampilkan teks "A verification code has been sent to " diikuti alamat email lengkap user `Fixture.auth.standardUserEmail` secara transparan (tanpa masking/sensor)
4. Verifikasi terdapat 6 kotak input digit numerik terpisah yang berada dalam kondisi kosong
5. Verifikasi kursor fokus secara otomatis (autofocus) pada kotak input pertama (Box 1)
6. Verifikasi pada kondisi normal ini (tanpa error jaringan), tombol "Verify" TIDAK ditampilkan sama sekali pada antarmuka
7. Verifikasi tombol "Resend code", link "Edit email", dan link "Back to Login with Password" tersedia di halaman

## Notes

- Subtitle halaman Input OTP menampilkan email lengkap tanpa masking sesuai ketetapan spesifikasi PRD.
- Auto-submit menggantikan fungsi tombol Verify konvensional pada kondisi normal.
