---
id: TC-AUTH-OTP-E2E-037-agreement-gate-cancellation-and-audit-log
title: Pembatalan sesi login pada layar Agreement (tutup tab / navigasi keluar) dan pencatatan audit log "Consent not given"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-21
coverage:
  web: automated
---

# Pembatalan sesi login pada layar Agreement (tutup tab / navigasi keluar) dan pencatatan audit log "Consent not given"

## Prerequisites

- User yang memenuhi pemicu layar Agreement (misalnya login pertama kali, `Fixture.auth.firstLoginUser`)
- Alur Request OTP dan verifikasi OTP telah berhasil dilakukan hingga browser berada di layar "Confirm to Continue"
- Layar menampilkan checkbox persetujuan kebijakan privasi yang belum dicentang

## Test Steps

1. Pastikan browser berada di layar "Confirm to Continue"
2. Tanpa mencentang checkbox dan tanpa mengklik tombol `[Continue]`, lakukan salah satu aksi pembatalan:
   - Menutup tab/jendela browser, ATAU
   - Menavigasikan browser ke URL lain (contoh: kembali ke `/login-password` atau halaman luar)
3. Buka tab baru dan akses halaman utama aplikasi (`/portal` atau dashboard)
4. Verifikasi bahwa sesi autentikasi penuh BELUM terbentuk dan browser langsung di-redirect kembali ke halaman login
5. Menggunakan sesi admin, periksa Activity Log Session dan User Log
6. Verifikasi percobaan login yang ditinggalkan ini dicatat dengan status Failed dan Note "Consent not given"
7. Verifikasi identitas user (`user_id` dan email) teridentifikasi secara tepat pada log Failed tersebut karena telah tervalidasi pada langkah OTP sebelumnya

## Notes

- Jika user menutup layar persetujuan sebelum memberikan consent, token sementara (preAuthToken) hangus dan status login dicatat Failed ("Consent not given") guna keperluan audit kepatuhan (compliance).
