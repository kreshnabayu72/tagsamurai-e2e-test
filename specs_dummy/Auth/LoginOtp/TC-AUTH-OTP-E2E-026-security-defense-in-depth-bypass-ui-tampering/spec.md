---
id: TC-AUTH-OTP-E2E-026-security-defense-in-depth-bypass-ui-tampering
title: "Keamanan dan Defense-in-Depth: Bypass UI, Direct API, Token Tampering, dan Injection"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-153
  - TC-AUTH-OTP-154
  - TC-AUTH-OTP-155
  - TC-AUTH-OTP-156
  - TC-AUTH-OTP-158
  - TC-AUTH-OTP-159
  - TC-AUTH-OTP-160
  - TC-AUTH-OTP-161
  - TC-AUTH-OTP-162
  - TC-AUTH-OTP-163
  - TC-AUTH-OTP-171
  - TC-AUTH-OTP-172
  - TC-AUTH-OTP-178
coverage:
  web: automated
---

# Keamanan dan Defense-in-Depth: Bypass UI, Direct API, Token Tampering, dan Injection

## Prerequisites

- Mode: mock / direct API client / security penetration harness.
- Belum login dan session kosong.
- User `Sec Target` (`sectarget@qwertysystem.net`) profil BASE.
- User `Sec Attacker` (`secattacker@qwertysystem.net`) profil BASE.
- Akun Total Control Global Settings aktif.

## Test Steps

### Proteksi Direct API Request OTP tanpa token reCAPTCHA yang sah

1. Kirim langsung HTTP POST ke endpoint `POST /auth/otp/request` tanpa menyertakan parameter token reCAPTCHA
2. Verifikasi backend menolak permintaan dengan status `400 Bad Request` atau `403 Forbidden`
3. Kirim HTTP POST dengan token reCAPTCHA palsu / string sembarang
4. Verifikasi backend memvalidasi token ke Google API dan menolak permintaan
5. Kirim HTTP POST menggunakan token reCAPTCHA yang sudah pernah berhasil dipakai sebelumnya (Replay Attack)
6. Verifikasi backend menolak penggunaan ulang token CAPTCHA (token sekali pakai ditegakkan di backend)

### Proteksi Direct API Verify OTP terhadap tampering dan urutan alur

7. Kirim langsung HTTP POST ke `POST /auth/otp/verify` untuk email `sectarget@qwertysystem.net` tanpa melalui tahap Request OTP
8. Verifikasi backend menolak permintaan karena tidak ada sesi/rekaman OTP aktif
9. Kirim HTTP POST ke `POST /auth/otp/verify` dengan memodifikasi signature atau identifier sesi pra-autentikasi (tampered session token)
10. Verifikasi backend menolak dengan `401 Unauthorized`
11. Lakukan verifikasi sukses dengan kode OTP yang valid, lalu kirim ulang payload verifikasi yang sama persis untuk kedua kalinya (OTP Token Replay)
12. Verifikasi penolakan: kode OTP yang sudah di-consume berstatus terpakai dan tidak dapat di-replay

### Pelanggaran urutan gerbang keamanan (Gate Bypassing)

13. Coba kirim langsung HTTP POST ke endpoint persetujuan `POST /auth/confirm-agreement` tanpa menyelesaikan verifikasi OTP
14. Verifikasi permintaan ditolak `401 Unauthorized` karena token pra-autentikasi belum diterbitkan
15. Dapatkan token pra-autentikasi persetujuan milik `Sec Target`, lalu gunakan token tersebut untuk mengonfirmasi persetujuan atas nama `Sec Attacker`
16. Verifikasi backend menolak dengan `403 Forbidden` karena subject token tidak cocok dengan identitas user yang dikonfirmasi
17. Coba tembak langsung endpoint penyelesaian MFA tanpa memvalidasi OTP terlebih dahulu
18. Verifikasi sistem memblokir akses ke tahap MFA sebelum tahap OTP sukses

### Ketahanan terhadap Injection pada kotak digit OTP

19. Pada layar Verify OTP, suntikkan payload SQL Injection seperti `' OR '1'='1` atau payload NoSQL `{"$gt": ""}` ke dalam input digit
20. Verifikasi input di-sanitize secara ketat di sisi klien dan server, hanya mengekstrak angka, serta ditolak dengan "Incorrect verification code. Please try again." tanpa menimbulkan celah eksekusi database

### Perlindungan endpoint internal terhadap pengguna yang belum menyelesaikan seluruh gerbang

21. Saat berada di layar Verify OTP atau layar Confirm to Continue (sebelum Product Hub terbuka), kirim request HTTP GET ke endpoint data internal (contoh: `/api/v1/users` atau `/api/v1/assets`)
22. Verifikasi seluruh endpoint internal menolak request dengan status `401 Unauthorized` dan tidak ada data aplikasi yang bocor sebelum sesi penuh diterbitkan

### Perilaku Atribut entry=edit_email Informatif Tanpa Verifikasi Riwayat (EC-54, TC-178)

23. Setelah kuota resend untuk suatu email habis pada sesi tertentu, kirim langsung HTTP POST ke endpoint Request OTP dengan menyertakan atribut `entry` = `edit_email` tanpa melalui alur UI Edit Email
24. Verifikasi backend menerima permintaan apa adanya (karena atribut `entry` bersifat informatif dan server tidak memverifikasi riwayat Edit Email di client sesuai PRD EC-54)
25. Verifikasi email OTP baru berhasil dikirimkan, kuota resend ter-reset (memulai sesi resend baru), dan IP rate limit tetap berlaku

## Notes

- TAG Samurai menerapkan prinsip *Defense-in-Depth* (Pertahanan Berlapis): validasi UI selalu didukung oleh pemeriksaan server-side yang ketat pada setiap transisi gerbang autentikasi.
- Seluruh token transisional (CAPTCHA token, OTP session, agreement token, MFA pre-auth) dilindungi oleh tanda tangan kriptografis, time-to-live terbatas, dan pencegahan replay.
- Sesuai PRD §9.2 F-AUTHOTP-07 dan EC-54, atribut `entry` bersifat informatif dan tidak diverifikasi oleh backend terhadap riwayat alur pengguna; jika `entry=edit_email` dikirim langsung, server menerimanya apa adanya dan memulai sesi resend baru dengan IP rate limit tetap aktif sebagai pelindung anti-spam.
