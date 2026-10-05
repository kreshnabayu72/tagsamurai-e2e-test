---
id: TC-AUTH-OTP-E2E-035-cross-action-race-verify-vs-edit-email
title: Penanganan balapan lintas aksi: Verify OTP auto-submit vs Edit Email secara simultan
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-107
coverage:
  web: automated
---

# Penanganan balapan lintas aksi: Verify OTP auto-submit vs Edit Email secara simultan

## Prerequisites

- Akun aktif terdaftar dengan sesi OTP aktif (`Fixture.auth.concurrencyUserEmail`)
- Dua tab browser dibuka pada sesi OTP yang sama (Tab A dan Tab B)

## Test Steps

1. Buka sesi OTP yang sama di Tab A dan Tab B dengan kode yang valid
2. Pada Tab A, siapkan auto-submit kode 6 digit benar
3. Pada Tab B, siapkan klik link "Edit email"
4. Eksekusi klik "Edit email" di Tab B dan auto-submit di Tab A secara simultan
5. Verifikasi penanganan atomic server:
   - Jika Edit Email (Tab B) ter-commit lebih dahulu: kode lama di-invalidate sehingga submit Tab A ditolak dengan pesan "Invalid code" dan dicatat Failed Note "OTP invalid — email changed"
   - Jika Verify (Tab A) ter-commit lebih dahulu: verifikasi sukses, sesi dibuat, dan aksi navigasi Tab B tidak membatalkan login yang sudah berhasil
6. Verifikasi integritas data tetap konsisten dan tidak menghasilkan status ambigu

## Notes

- P8-8b-1 menegaskan perlindungan terhadap kondisi balapan (race condition) antar-aksi yang saling bertolak belakang dalam siklus hidup sesi OTP.
