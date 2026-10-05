---
id: TC-AUTH-OTP-E2E-015-concurrency-parallel-request-two-tabs
title: Penanganan dua permintaan Request OTP paralel pada dua tab browser untuk email yang sama
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-78
coverage:
  web: automated
---

# Penanganan dua permintaan Request OTP paralel pada dua tab browser untuk email yang sama

## Prerequisites

- Akun aktif terdaftar siap menerima permintaan OTP paralel (`Fixture.auth.concurrencyUserEmail`)
- Dua konteks tab browser independen dapat dikontrol (Tab A dan Tab B)

## Test Steps

1. Buka halaman Input Email Login with OTP pada Tab A dan Tab B untuk alamat email yang sama (`Fixture.auth.concurrencyUserEmail`)
2. Selesaikan verifikasi reCAPTCHA pada kedua tab
3. Klik tombol `[Request OTP]` di Tab A
4. Sesaat setelahnya (dalam hitungan beberapa detik), klik tombol `[Request OTP]` di Tab B
5. Ambil data kode OTP yang dikirimkan untuk request Tab A (Kode A) dan request Tab B (Kode B)
6. Verifikasi kode OTP dari Tab A langsung menjadi tidak aktif / hangus (`invalidated = true`) begitu request Tab B diproses server
7. Coba gunakan Kode A pada halaman verifikasi mana pun
8. Verifikasi Kode A ditolak dengan pesan "Invalid code"
9. Masukkan Kode B (terakhir diterbitkan) pada halaman Input OTP Tab B
10. Verifikasi hanya Kode B yang diterima dan berhasil memicu verifikasi sukses

## Notes

- TAG Samurai menegakkan invariant sistem: hanya ada maksimal 1 kode OTP aktif per akun pada satu waktu. Permintaan baru secara otomatis menganulir masa berlaku kode sebelumnya.
