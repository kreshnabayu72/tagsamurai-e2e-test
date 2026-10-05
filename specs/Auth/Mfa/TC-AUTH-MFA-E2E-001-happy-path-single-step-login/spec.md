---
id: TC-AUTH-MFA-E2E-001-happy-path-single-step-login
title: Single-step login tanpa kondisi MFA terpicu langsung menghasilkan sesi penuh
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-1
  - TC-AUTH-MFA-4
coverage:
  web: automated
---

# Single-step login tanpa kondisi MFA terpicu langsung menghasilkan sesi penuh

## Prerequisites

- Mode: FE+BE
- User reguler dengan akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Kondisi login normal: device dikenal (terdaftar di `trusted_device`), lokasi dalam radius <100km, negara sama
- Bukan login pertama (`first_login_at` terisi) dan bukan idle ≥30 hari (`last_logout_at` <30 hari lalu)

## Test Steps

### Login Normal Tanpa Terpicu MFA (Happy Path)
1. Buka halaman Login TAG Samurai
2. Masukkan email dan password valid akun reguler, lalu klik `[Login]`
3. Verifikasi sistem tidak menampilkan layar MFA (Choose Verification Method / OTP / Authenticator)
4. Verifikasi pengguna langsung mendarat di Portal / Dashboard aplikasi
5. Verifikasi sesi login aktif terbentuk penuh di browser
6. Verifikasi entri login tercatat di Activity Log Session dengan Status "Success" dan Note "Login with password"

### Variasi Evaluasi Dimensi Idle <30 Hari
7. Lakukan logout dari aplikasi
8. Simulasikan login kembali dengan riwayat logout terakhir <30 hari yang lalu
9. Verifikasi dimensi idle tidak memicu MFA dan sesi login langsung aktif

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-01`
- Merepresentasikan `TC-AUTH-MFA-1` dan `TC-AUTH-MFA-4` (FE Ref: `TC-AUTH-MFA-FE-01`).
- Alur login satu langkah (single-step) standar saat seluruh dimensi anomali dan kebijakan keamanan normal.
