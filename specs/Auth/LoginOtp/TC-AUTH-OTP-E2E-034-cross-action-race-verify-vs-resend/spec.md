---
id: TC-AUTH-OTP-E2E-034-cross-action-race-verify-vs-resend
title: Penanganan balapan lintas aksi: Verify OTP auto-submit vs Resend OTP secara simultan
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-106
coverage:
  web: automated
---

# Penanganan balapan lintas aksi: Verify OTP auto-submit vs Resend OTP secara simultan

## Prerequisites

- Akun aktif terdaftar dengan sesi OTP aktif (`Fixture.auth.concurrencyUserEmail`)
- Dua tab browser dibuka pada sesi OTP yang sama (Tab A dan Tab B)

## Test Steps

1. Buka sesi OTP yang sama di Tab A dan Tab B dengan kode yang valid
2. Pada Tab A, masukkan 6 digit kode yang benar (siap auto-submit)
3. Pada Tab B, pastikan cooldown 1 menit telah selesai dan tombol "Resend code" siap diklik
4. Eksekusi klik "Resend code" di Tab B dan auto-submit di Tab A secara simultan
5. Verifikasi integritas atomic server:
   - Jika Resend (Tab B) ter-commit lebih dahulu: kode lama di-invalidate sehingga submit Tab A ditolak dengan pesan "Invalid code" dan tercatat Failed Note "Incorrect OTP"
   - Jika Verify (Tab A) ter-commit lebih dahulu: login berhasil, sesi dibuat, dan aksi Resend di Tab B menjadi moot tanpa menimbulkan error tak tertangani
6. Verifikasi tidak ada kondisi campuran (race condition) yang menghasilkan sesi ganda atau status tak konsisten

## Notes

- Kasus cross-action race Verify OTP vs Edit Email dipisahkan ke `TC-AUTH-OTP-E2E-035`.
