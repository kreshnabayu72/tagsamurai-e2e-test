---
id: TC-AUTH-MFA-E2E-010-deteksi-device-baru-dan-reset-storage
title: "Deteksi Device Baru, Pembersihan Local Storage, dan Independensi Device Lintas Platform"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-30
  - TC-AUTH-MFA-31
  - TC-AUTH-MFA-32
  - TC-AUTH-MFA-50
coverage:
  web: automated
---
# Deteksi Device Baru, Pembersihan Local Storage, dan Independensi Device Lintas Platform

## Prerequisites

- Browser uji A (device dikenali) dan browser uji B (device baru / incognito).
- User `Anwar Sanusi` (`anwarsanusi@qwertysystem.net`) profil NEWDEV (pernah login dari browser uji A, browser uji B belum pernah).
- User `Eko Prasetyo` (`ekoprasetyo@qwertysystem.net`) profil NEWDEV.
- User `Maya Indah` (`mayaindah@qwertysystem.net`) profil MOB (sudah trusted di web, belum di mobile).
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Login dari browser baru memicu MFA dan email alert

1. Buka browser uji B (incognito / profil baru) pada halaman login
2. Masukkan email `anwarsanusi@qwertysystem.net` dan password valid lalu klik [Log in]
3. Verifikasi device identifier (fingerprint / cookie) tidak ditemukan pada daftar trusted device
4. Verifikasi halaman `Auth > MFA > Choose Verification Method` tampil
5. Periksa kotak masuk mail-catcher untuk `anwarsanusi@qwertysystem.net`
6. Verifikasi email alert "TAG Samurai - Unusual Login Attempt Detected" terkirim dengan informasi browser baru

### Pembersihan localStorage browser dikenali memicu deteksi device baru

7. Buka browser uji A yang sebelumnya berstatus trusted device untuk user `ekoprasetyo@qwertysystem.net`
8. Buka Developer Tools browser dan hapus seluruh `localStorage` serta cookie token device
9. Lakukan login ulang dengan kredensial user tersebut
10. Verifikasi sistem tidak mengenali device identifier dan memperlakukan login sebagai device baru
11. Verifikasi halaman Choose Verification Method tampil dan email alert dikirimkan

### Independensi per platform: Trusted di Web tidak membebaskan Mobile

12. Gunakan user `mayaindah@qwertysystem.net` yang sudah memiliki trusted device aktif di browser web
13. Buka aplikasi mobile TAG Samurai pada perangkat Android baru dan login dengan akun tersebut
14. Verifikasi aplikasi mobile memicu MFA dan mengirim email alert karena token trust web tidak berlaku di mobile

## Notes

- Sesuai `AUTHMFA-LOGIC-02a`, identitas device diverifikasi melalui secure storage token / fingerprint per platform.
- Penghapusan storage browser menyebabkan perangkat diperlakukan sebagai perangkat baru.
