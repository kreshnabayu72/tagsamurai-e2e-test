---
id: TC-AUTH-OTP-E2E-003-request-otp-email-field-validation
title: Validasi format field Email pada Request OTP (kosong, format salah, 120 char boundary, auto-trim, aria-describedby)
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-5
  - TC-AUTH-OTP-6
  - TC-AUTH-OTP-9
  - TC-AUTH-OTP-10
  - TC-AUTH-OTP-71
  - TC-AUTH-OTP-95
coverage:
  web: automated
---

# Validasi format field Email pada Request OTP (kosong, format salah, 120 char boundary, auto-trim, aria-describedby)

## Prerequisites

- Browser berada pada status publik (belum login)
- Halaman Input Email Login with OTP dapat diakses

## Test Steps

### Email Kosong

1. Buka halaman Input Email Login with OTP
2. Klik tombol `[Request OTP]` dalam kondisi field Email kosong
3. Verifikasi submit diblokir, pesan error inline "Email must not be empty" muncul di bawah field Email, dan tidak ada pengiriman OTP
4. Verifikasi elemen error terasosiasi dengan atribut `aria-describedby` serta `aria-invalid="true"` pada field Email

### Format Email Tidak Valid

5. Ketik format email tidak valid "notanemail" ke dalam field Email lalu klik `[Request OTP]`
6. Verifikasi submit diblokir dan pesan error inline "Email format is incorrect" muncul

### Batas Maksimal 120 Karakter (Boundary Ditolak pada Karakter ke-121)

7. Masukkan string email sepanjang 121 karakter ke dalam field Email
8. Verifikasi pesan error "Max. 120 characters" langsung muncul secara real-time saat mengetik sebelum tombol ditekan

### Auto-Trim Whitespace Awal dan Akhir

9. Masukkan email valid dengan spasi di awal dan akhir "  user@example.com  "
10. Verifikasi spasi di awal dan akhir di-trim secara otomatis sehingga diproses sebagai email valid tanpa error format

### Zero Audit Log

11. Periksa Activity Log Session dan User Log
12. Verifikasi bahwa seluruh kegagalan validasi format email di atas tidak menghasilkan entri baru pada surface log

## Notes

- Validasi format email diidentifikasi identik dengan alur Login with Password.
- Kasus email belum terdaftar dan proteksi reCAPTCHA gate dipisahkan ke `TC-AUTH-OTP-E2E-004`.
