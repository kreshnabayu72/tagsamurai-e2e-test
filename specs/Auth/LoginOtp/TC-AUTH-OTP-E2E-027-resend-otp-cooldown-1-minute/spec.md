---
id: TC-AUTH-OTP-E2E-027-resend-otp-cooldown-1-minute
title: Alur Resend OTP dengan cooldown 1 menit dan timer aksesibilitas
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-48
  - TC-AUTH-OTP-49
  - TC-AUTH-OTP-96
coverage:
  web: automated
---

# Alur Resend OTP dengan cooldown 1 menit dan timer aksesibilitas

## Prerequisites

- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Halaman Input OTP telah terbuka setelah pengiriman kode OTP pertama (`resend_count = 0`)
- Environment testing memiliki kontrol simulasi waktu/clock

## Test Steps

1. Amati tombol "Resend code" segera setelah halaman Input OTP terbuka
2. Verifikasi tombol "Resend code" dalam status disabled
3. Verifikasi label tombol menampilkan hitung mundur (countdown) dengan format "Resend code in (00:59)" yang berjalan mundur hingga "(00:00)"
4. Verifikasi elemen countdown memiliki atribut aksesibilitas `role="timer"` atau `aria-live="polite"`
5. Tunggu atau majukan waktu simulasi hingga countdown 1 menit selesai (mencapai 00:00)
6. Verifikasi tombol "Resend code" berubah menjadi enabled (aktif dan dapat diklik) tanpa perlu refresh halaman

## Notes

- Cooldown 1 menit berlaku antar pengiriman resend ke-1 sampai ke-4.
- Pengujian aksi klik resend, pengiriman kode baru, persistensi F5, dan zero log dipisahkan ke `TC-AUTH-OTP-E2E-028`.
- Batas maksimal resend ke-5 dan cooldown 10 menit dipisahkan ke `TC-AUTH-OTP-E2E-029`.
