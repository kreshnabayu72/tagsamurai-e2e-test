---
id: TC-AUTH-LP-E2E-023-konsumsi-persetujuan-lintas-modul
title: Persetujuan Privacy Policy dari Login with Password berlaku di Login with OTP dan Biometric Re-login
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-159
  - TC-AUTH-LP-160
coverage:
  web: automated
  mobile: automated
---

# Persetujuan Privacy Policy dari Login with Password berlaku di Login with OTP dan Biometric Re-login

## Prerequisites

- User belum login (guest) di web maupun di aplikasi native TAG Samurai Mobile.
- User `bimosetiawan@qwertysystem.net` berstatus aktif; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui akun ini; device terpercaya; bukan login pertama dan tidak idle; tidak memicu MFA.
- User `citrakirana@qwertysystem.net` berstatus aktif dengan profil biometric re-login aktif di aplikasi native Android; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui akun ini; device terpercaya; bukan login pertama dan tidak idle; tidak memicu MFA.
- Akses ke mock mailbox atau service inspeksi email untuk mengambil kode OTP `bimosetiawan@qwertysystem.net`.

## Test Steps

### Persetujuan via Login with Password dikonsumsi oleh Login with OTP (web)

1. Buka halaman Login with Password di browser web
2. Masukkan email `bimosetiawan@qwertysystem.net` dan password `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
3. Verifikasi layar Confirm to Continue tampil
4. Centang checkbox persetujuan lalu klik tombol [Continue ➔]
5. Verifikasi browser menuju Portal — Product Hub
6. Lakukan logout lalu buka halaman Login with OTP
7. Isi email `bimosetiawan@qwertysystem.net`, minta kode OTP, isi kode OTP dari kotak masuk email, lalu verifikasi
8. Verifikasi layar Confirm to Continue TIDAK tampil lagi dan browser menuju Portal — Product Hub

### Persetujuan via Login with Password dikonsumsi oleh Biometric Re-login (mobile Android)

9. Buka layar Login with Password pada aplikasi TAG Samurai Mobile (Android)
10. Isi email `citrakirana@qwertysystem.net` dan password `QaLogin#2026`, lalu ketuk [Log in]
11. Verifikasi layar Confirm to Continue tampil
12. Centang checkbox persetujuan lalu ketuk tombol [Continue ➔]
13. Verifikasi aplikasi menuju Portal — Product Hub
14. Lakukan logout lalu buka kembali aplikasi dan ketuk opsi Biometric Re-login
15. Verifikasi identitas dengan biometrik
16. Verifikasi layar Confirm to Continue TIDAK tampil lagi dan aplikasi menuju Portal — Product Hub

## Notes

- Persetujuan Privacy Policy berlaku lintas modul auth: versi yang disetujui lewat Login with Password juga dikonsumsi oleh Login with OTP dan Biometric Re-login sehingga layar Confirm to Continue tidak muncul kembali untuk versi policy yang sama (PRD §11 Dampak ke modul lain Agreement Gate, `auth-foundation.md` §11.1).
- Verifikasi pemakaian ulang persetujuan pada modul Login with Password diuji di E2E-011; spec ini melengkapi sisi konsumennya (Login with OTP dan Biometric Re-login).
