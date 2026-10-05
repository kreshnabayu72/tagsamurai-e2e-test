---
id: TC-AUTH-MFA-E2E-010-location-detection-distance-haversine
title: Lokasi login dalam radius 100km lolos dan jarak lebih dari 100km memicu MFA
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-13
  - TC-AUTH-MFA-14
coverage:
  web: automated
---

# Lokasi login dalam radius 100km lolos dan jarak lebih dari 100km memicu MFA

## Prerequisites

- Mode: FE+BE
- Riwayat login terakhir tercatat pada koordinat geografis A (misalnya Jakarta)
- Device yang digunakan adalah device dikenal

## Test Steps

### Login dari Lokasi Berjarak Dekat (≤100km)
1. Simulasikan IP login dari koordinat yang berjarak 30km dari lokasi A (dalam radius 100km)
2. Masukkan kredensial valid dan klik `[Login]`
3. Verifikasi dimensi jarak tidak memicu MFA dan pengguna langsung masuk

### Login dari Lokasi Berjarak Jauh (>100km)
4. Lakukan logout
5. Simulasikan IP login dari koordinat lokasi B yang berjarak >100km dari lokasi A (misalnya Bandung >140km)
6. Masukkan kredensial valid dan klik `[Login]`
7. Verifikasi sistem menghitung formula Haversine (>100km) dan mewajibkan verifikasi faktor kedua (MFA)
8. Verifikasi email alert Unusual Login dikirimkan ke alamat email user

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-10`
- Merepresentasikan `TC-AUTH-MFA-13` dan `TC-AUTH-MFA-14` (FE Ref: `TC-AUTH-MFA-FE-10`).
