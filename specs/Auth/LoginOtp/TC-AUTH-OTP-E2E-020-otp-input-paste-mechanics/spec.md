---
id: TC-AUTH-OTP-E2E-020-otp-input-paste-mechanics
title: Mekanisme auto-paste pada field OTP (paste 6 digit, truncation >6 karakter, dan sanitasi non-angka)
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-109
  - TC-AUTH-OTP-110
  - TC-AUTH-OTP-111
coverage:
  web: automated
---

# Mekanisme auto-paste pada field OTP (paste 6 digit, truncation >6 karakter, dan sanitasi non-angka)

## Prerequisites

- Halaman Input OTP telah terbuka dengan sesi kode OTP aktif
- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)

## Test Steps

### Paste Tepat 6 Digit Numerik & Auto-Submit

1. Salin teks 6 digit numerik "481902" ke clipboard
2. Lakukan aksi tempel (Paste / `Ctrl+V`) ke dalam Box 1
3. Verifikasi ke-6 digit terdistribusi secara otomatis ke masing-masing Box 1 sampai Box 6 ("4", "8", "1", "9", "0", "2")
4. Verifikasi auto-submit terpicu secara otomatis begitu digit ke-6 terisi tanpa perlu mengklik tombol

### Paste String Melebihi 6 Karakter (Truncation)

5. Bersihkan kembali isi seluruh kotak OTP
6. Salin string numerik panjang "481902999" (9 digit) ke clipboard
7. Lakukan aksi tempel (Paste) ke dalam Box 1
8. Verifikasi hanya 6 digit pertama ("481902") yang dimasukkan ke Box 1–6 dan 3 digit sisanya dibuang (truncated)
9. Verifikasi auto-submit terpicu secara otomatis

### Paste String Alfanumerik Campuran (Sanitasi Non-Angka)

10. Bersihkan kembali isi seluruh kotak OTP
11. Salin string alfanumerik campuran "48A902" (terdapat 5 angka dan 1 huruf) ke clipboard
12. Lakukan aksi tempel (Paste) ke dalam Box 1
13. Verifikasi karakter huruf "A" dibersihkan/dibuang sehingga hanya 5 digit angka yang masuk ke dalam kotak (Box 1 sampai Box 5 terisi)
14. Verifikasi Box 6 tetap kosong, kursor berada di Box 6, dan auto-submit TIDAK terpicu

## Notes

- Sanitasi paste memfilter karakter non-angka secara otomatis sebelum mendistribusikan ke input boxes.
- Auto-submit hanya terpicu jika setelah proses sanitasi menghasilkan tepat 6 digit numerik lengkap.
