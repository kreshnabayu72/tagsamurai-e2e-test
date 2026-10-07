---
id: TC-AUTH-MFA-E2E-007-evaluasi-single-step-tanpa-mfa
title: "Evaluasi Login Normal: Single-Step Tanpa MFA pada Device Dikenali dan Lokasi Sama"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-22
  - TC-AUTH-MFA-23
  - TC-AUTH-MFA-34
  - TC-AUTH-MFA-148
coverage:
  web: automated
---
# Evaluasi Login Normal: Single-Step Tanpa MFA pada Device Dikenali dan Lokasi Sama

## Prerequisites

- Browser uji A (sudah berstatus trusted device untuk user uji).
- User `Bayu Pratama` (`bayupratama@qwertysystem.net`) profil NORM (login terakhir dari Jakarta ID 2 hari yang lalu, lokasi saat ini Jakarta ID, jarak ≤100 km).
- User `Ratna Sari` (`ratnasari@qwertysystem.net`) profil NORM (login terakhir dari Bandung ID, login saat ini dari Cimahi ID, jarak ~15 km ≤100 km).
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Login normal dari device dan lokasi yang sama berakhir single-step

1. Buka browser uji A pada halaman `Auth > Login with Password` (`/login`)
2. Masukkan email `bayupratama@qwertysystem.net` dan password valid
3. Centang reCAPTCHA dan klik button [Log in]
4. Verifikasi sistem mengevaluasi kriteria MFA:
   - Bukan login pertama (first_login = false)
   - Bukan idle ≥30 hari (last_login = 2 hari lalu)
   - Device dikenali (trusted_device = true)
   - Jarak ≤100 km dan negara sama
5. Verifikasi halaman MFA TIDAK ditampilkan sama sekali
6. Verifikasi browser langsung mendarat di Portal — Product Hub (`/product-hub`) dengan sesi web penuh

### Single-step login tidak mengirimkan email alert dan memperbarui last_login

7. Periksa kotak masuk mail-catcher untuk `bayupratama@qwertysystem.net`
8. Verifikasi TIDAK ADA email alert "TAG Samurai - Unusual Login Attempt Detected" yang terkirim
9. Buka database/audit log dan verifikasi catatan `last_login_at` dan koordinat `last_login_location` user diperbarui dengan waktu login single-step saat ini (sesuai NC-02)

### Login dalam jarak ≤100 km (Bandung ke Cimahi) tetap berakhir single-step

10. Buka browser uji A dengan user `ratnasari@qwertysystem.net` (login terakhir di Bandung)
11. Simulasikan request dari alamat IP Cimahi (jarak geografis ~15 km < 100 km)
12. Masukkan kredensial yang valid dan klik [Log in]
13. Verifikasi login langsung berhasil menuju Portal — Product Hub (single-step) tanpa intervensi MFA dan tanpa email alert

## Notes

- Sesuai `AUTHMFA-LOGIC-01a` dan keputusan NC-02, login single-step yang berhasil memperbarui lokasi login terakhir user.
- Jarak antar-lokasi dihitung menggunakan formula Haversine.
