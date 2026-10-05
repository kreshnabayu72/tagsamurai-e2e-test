---
id: TC-AUTH-OTP-E2E-026-error-handling-otp-verify-failure-and-fallback
title: Penanganan kegagalan server saat verifikasi OTP, tombol fallback Verify, dan validasi field kosong
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-43
  - TC-AUTH-OTP-46
  - TC-AUTH-OTP-72
  - TC-AUTH-OTP-83
coverage:
  web: automated
---

# Penanganan kegagalan server saat verifikasi OTP, tombol fallback Verify, dan validasi field kosong

## Prerequisites

- Mode: mock (intersep HTTP pada endpoint `POST /v2/iam/auth/otp/verify`)
- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Halaman Input OTP telah terbuka dengan kode yang valid

## Test Steps

### Kegagalan Jaringan saat Auto-Submit & Kemunculan Fallback Tombol "Verify"

1. Pada halaman Input OTP yang terbuka dengan kode valid, konfigurasikan intersep endpoint `POST /v2/iam/auth/otp/verify` untuk mengembalikan status HTTP 500 saat verifikasi dipanggil
2. Ketik 6 digit kode yang benar ke dalam field OTP
3. Verifikasi auto-submit terpanggil dan gagal karena server error
4. Verifikasi toast notifikasi muncul dengan teks "Error, failed to log in. Please try again."
5. Verifikasi browser tetap berada di halaman Input OTP dan kode OTP yang benar TIDAK hangus (`used` tetap `false`)
6. Verifikasi tombol fallback "Verify" kini MUNCUL pada antarmuka untuk memungkinkan user mencoba kembali secara manual tanpa harus mengetik ulang
7. Verifikasi kegagalan transport/server ini tidak dicatat ke surface audit log

### Klik Fallback Tombol "Verify" dengan Field Belum Lengkap

8. Kosongkan salah satu kotak digit OTP sehingga hanya terisi 5 digit
9. Klik tombol fallback "Verify"
10. Verifikasi submit diblokir dengan pesan error inline dan dicatat ke log Failed dengan Note "Empty OTP"

### Penegakan Validasi Server (FE Tidak Boleh Menyimpulkan Sukses)

11. Masukkan kembali digit ke-6 dan tahan response server dalam status pending
12. Verifikasi frontend tetap menampilkan status loading dan tidak mengalihkan halaman ke Portal sebelum ada konfirmasi HTTP 200 dari backend

## Notes

- Tombol "Verify" merupakan fallback UI yang hanya muncul jika auto-submit mengalami kegagalan teknis/jaringan.
- Penanganan kegagalan server saat aksi Resend OTP dipisahkan ke `TC-AUTH-OTP-E2E-030`.
