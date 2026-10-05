---
id: TC-AUTH-OTP-E2E-017-otp-fields-keyboard-accessibility
title: Aksesibilitas keyboard, navigasi urutan fokus Tab, dan atribut aria-label pada 6 digit OTP
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-94
coverage:
  web: automated
---

# Aksesibilitas keyboard, navigasi urutan fokus Tab, dan atribut aria-label pada 6 digit OTP

## Prerequisites

- Halaman Input OTP telah terbuka dengan 6 kotak digit kosong

## Test Steps

1. Lakukan inspeksi elemen antarmuka pada ke-6 kotak input digit OTP
2. Verifikasi setiap kotak input memiliki label aksesibilitas yang deskriptif untuk pembaca layar (screen reader) secara berurutan:
   - Box 1: `aria-label="Digit 1 of 6"`
   - Box 2: `aria-label="Digit 2 of 6"`
   - Box 3: `aria-label="Digit 3 of 6"`
   - Box 4: `aria-label="Digit 4 of 6"`
   - Box 5: `aria-label="Digit 5 of 6"`
   - Box 6: `aria-label="Digit 6 of 6"`
3. Pastikan fokus awal berada pada Box 1
4. Tekan tombol `Tab` pada keyboard
5. Verifikasi fokus berpindah ke Box 2
6. Tekan tombol `Tab` secara berurutan hingga Box 6
7. Verifikasi urutan perpindahan fokus (tab order) berjalan mulus dari Box 1 sampai Box 6 tanpa ada lompatan elemen
8. Tekan kombinasi tombol `Shift + Tab` dari Box 6
9. Verifikasi fokus berpindah mundur secara teratur ke Box 5

## Notes

- Aksesibilitas keyboard memastikan form verifikasi OTP dapat dioperasikan sepenuhnya oleh pengguna keyboard-only dan alat bantu disabilitas sesuai WCAG 2.1 AA.
