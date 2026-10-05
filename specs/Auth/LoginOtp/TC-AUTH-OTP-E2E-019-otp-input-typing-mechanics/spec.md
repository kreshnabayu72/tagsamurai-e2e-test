---
id: TC-AUTH-OTP-E2E-019-otp-input-typing-mechanics
title: Mekanisme pengetikan digit OTP, backward deletion, auto-advance, dan blokir non-angka
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-33
  - TC-AUTH-OTP-34
  - TC-AUTH-OTP-35
coverage:
  web: automated
---

# Mekanisme pengetikan digit OTP, backward deletion, auto-advance, dan blokir non-angka

## Prerequisites

- Halaman Input OTP telah terbuka dengan sesi kode OTP aktif
- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)

## Test Steps

### Penolakan Karakter Non-numerik di Level Input

1. Pastikan kursor berada pada kotak Box 1
2. Ketik karakter alfabet atau simbol seperti `a`, `B`, `@`, `#`, `$`
3. Verifikasi seluruh karakter non-numerik ditolak secara mutlak dan tidak masuk ke dalam kotak (Box 1 tetap kosong)

### Pengetikan Angka & Auto-Advance

4. Ketik angka `5` pada Box 1
5. Verifikasi angka `5` tampil pada Box 1 dan kursor otomatis berpindah (auto-advance) ke Box 2
6. Ketik angka `8` pada Box 2
7. Verifikasi angka `8` tampil pada Box 2 dan kursor berpindah ke Box 3

### Backward Deletion via Backspace

8. Tekan tombol `Backspace` pada keyboard saat kursor berada di Box 3 (yang masih kosong)
9. Verifikasi kursor otomatis mundur ke Box 2 dan nilai `8` pada Box 2 terhapus secara bersamaan
10. Tekan tombol `Backspace` lagi
11. Verifikasi kursor mundur ke Box 1 dan nilai `5` pada Box 1 ikut terhapus sehingga semua kotak kembali kosong

## Notes

- Aturan allowed chars `0-9 only` berlaku ketat pada pengetikan keyboard manual.
- Mekanisme paste string, pemotongan >6 digit, dan sanitasi non-angka dipisahkan ke `TC-AUTH-OTP-E2E-020`.
