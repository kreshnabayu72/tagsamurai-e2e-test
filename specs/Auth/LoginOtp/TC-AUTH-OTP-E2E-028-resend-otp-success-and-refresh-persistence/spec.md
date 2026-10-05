---
id: TC-AUTH-OTP-E2E-028-resend-otp-success-and-refresh-persistence
title: Pengiriman ulang OTP sukses (resend 1-4), persistensi countdown pasca refresh F5, dan zero audit log
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-50
  - TC-AUTH-OTP-55
  - TC-AUTH-OTP-56
coverage:
  web: automated
---

# Pengiriman ulang OTP sukses (resend 1-4), persistensi countdown pasca refresh F5, dan zero audit log

## Prerequisites

- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Halaman Input OTP telah terbuka dengan countdown 1 menit pertama yang telah selesai (tombol "Resend code" telah enabled)
- Environment testing memiliki kontrol waktu/clock

## Test Steps

### Eksekusi Resend Sukses (Jatah 1-4)

1. Klik tombol "Resend code" yang sedang berstatus enabled
2. Verifikasi toast notifikasi muncul dengan teks "Success, the code has been sent."
3. Verifikasi kode OTP sebelumnya di-invalidate dan kode OTP baru diterbitkan dalam sesi OTP yang sama
4. Verifikasi counter `resend_count` bertambah (misalnya dari 0 menjadi 1)
5. Verifikasi tombol "Resend code" kembali berstatus disabled dan countdown 1 menit ("Resend code in (00:59)") dimulai ulang

### Persistensi Countdown & Kuota Pasca Refresh Halaman (F5)

6. Saat countdown sedang berjalan (misalnya tersisa 40 detik), lakukan refresh halaman browser (F5)
7. Verifikasi setelah halaman termuat ulang, counter jatah resend TIDAK di-reset ke 0
8. Verifikasi sisa waktu cooldown dipertahankan sesuai status server (tombol tetap disabled dengan hitung mundur yang melanjutkan sisa waktu, bukan kembali ke 00:59 baru atau langsung enabled)

### Zero Audit Log untuk Aksi Resend

9. Menggunakan sesi admin, periksa Activity Log Session dan User Log
10. Verifikasi bahwa aksi Resend OTP sama sekali TIDAK menghasilkan entri audit log baru pada surface log sistem

## Notes

- Resend OTP murni merupakan fungsi transport komunikasi dan tidak dicatat di audit log sistem autentikasi.
- Persistensi state server-side mencegah pembobolan cooldown resend via manipulasi refresh browser.
