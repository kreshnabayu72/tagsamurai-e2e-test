---
id: TC-AUTH-OTP-E2E-018-mobile-responsive-input-otp-mechanics
title: Tampilan mobile responsive halaman Input OTP, numeric keyboard inputmode, dan tap target >= 44px
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-32
  - TC-AUTH-OTP-99
coverage:
  web: automated
---

# Tampilan mobile responsive halaman Input OTP, numeric keyboard inputmode, dan tap target >= 44px

## Prerequisites

- Mode: mock (pengujian tampilan responsive dan emulasi mobile)
- Konfigurasi viewport mobile app / layar kecil (375x812 atau setara)
- Sesi Input OTP aktif terbuka pada perangkat mobile uji

## Test Steps

### Layout Mobile Halaman OTP & Keyboard Numerik Langsung Muncul

1. Atur viewport browser ke ukuran mobile (contoh: 375x812)
2. Buka halaman Input OTP pada perangkat mobile uji
3. Verifikasi tata letak form disusun secara vertikal terpusat yang proporsional dengan layar mobile
4. Lakukan inspeksi elemen pada kotak digit OTP
5. Verifikasi setiap kotak input memiliki atribut `inputmode="numeric"`
6. Verifikasi keyboard numerik virtual pada perangkat mobile otomatis muncul saat kotak input difokuskan

### Verifikasi Dimensi Minimum Tap Target (>= 44px x 44px)

7. Lakukan pengukuran dimensi area sentuh (bounding box) pada seluruh elemen interaktif pada halaman:
   - Kotak digit input OTP (Box 1–6)
   - Tombol "Resend code"
   - Link "Edit email"
   - Link "Back to Login with Password"
8. Verifikasi seluruh elemen interaktif tersebut memiliki ukuran area sentuh minimal >= 44px x 44px sesuai standar kenyamanan aksesibilitas layar sentuh (touch target guidelines)

## Notes

- Atribut `inputmode="numeric"` menjamin pengalaman pengguna mobile langsung disuguhkan keyboard angka tanpa perlu berganti mode manual.
- Dimensi tap target >= 44px mencegah salah sentuh (mis-click) pada tombol-tombol yang berdekatan.
