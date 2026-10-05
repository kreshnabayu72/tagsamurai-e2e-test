---
id: TC-AUTH-MFA-E2E-006-device-detection-known-vs-new
title: Device dikenal tidak memicu MFA sedangkan device baru memicu MFA dan email alert
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-8
  - TC-AUTH-MFA-9
coverage:
  web: automated
---

# Device dikenal tidak memicu MFA sedangkan device baru memicu MFA dan email alert

## Prerequisites

- Mode: FE+BE
- Akun aktif terdaftar dengan satu perangkat tepercaya (`trusted_device`) yang sudah tersimpan

## Test Steps

### Login dari Device Dikenal
1. Buka browser dengan identifier `device_id` yang cocok persis dengan data di `trusted_device`
2. Masukkan email dan password valid, lalu klik `[Login]`
3. Verifikasi MFA tidak terpicu oleh dimensi device dan pengguna langsung masuk ke aplikasi
4. Verifikasi kolom `trusted_device.last_used_at` diperbarui ke timestamp saat ini

### Login dari Device Baru
5. Lakukan logout dan ganti identitas perangkat (`device_id` baru yang belum terdaftar)
6. Masukkan kredensial login akun yang sama, lalu klik `[Login]`
7. Verifikasi sistem mendeteksi device baru dan mewajibkan verifikasi faktor kedua (MFA)
8. Verifikasi sistem mengirimkan email notifikasi Unusual Login Alert ke mailbox akun

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-06`
- Merepresentasikan `TC-AUTH-MFA-8` dan `TC-AUTH-MFA-9` (FE Ref: `TC-AUTH-MFA-FE-06`).
