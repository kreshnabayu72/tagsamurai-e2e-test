---
id: TC-AUTH-OTP-E2E-006-request-otp-sukses-dan-template-email
title: "Request OTP Berhasil, State Loading, Idempotensi Double-Submit, dan Integritas Template Email"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-28
  - TC-AUTH-OTP-29
  - TC-AUTH-OTP-30
  - TC-AUTH-OTP-37
  - TC-AUTH-OTP-38
  - TC-AUTH-OTP-39
coverage:
  web: automated
---

# Request OTP Berhasil, State Loading, Idempotensi Double-Submit, dan Integritas Template Email

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP > Request OTP` (`/login/otp`) terbuka di browser.
- User `Yoga Simanjuntak` (`yogasimanjuntak@qwertysystem.net`) profil BASE.
- User `Sari Mulyadi` (`sarimulyadi@qwertysystem.net`) profil BASE.
- User `Eko Setiawan` (`ekosetiawan@qwertysystem.net`) profil BASE.
- User `Joko Nugroho` (`jokonugroho@qwertysystem.net`) profil BASE.
- User `Anisa Aditya` (`anisaaditya@qwertysystem.net`) profil BASE.
- User `Bagas Maulana` (`bagasmaulana@qwertysystem.net`) profil BASE.
- Layanan mail-catcher lingkungan uji aktif untuk inspeksi email keluar dan pengukuran latency.

## Test Steps

### Request OTP berhasil dan transisi ke halaman Verify OTP

1. Buka halaman Request OTP di browser
2. Masukkan email `yogasimanjuntak@qwertysystem.net`
3. Selesaikan reCAPTCHA v2 "I'm not a robot"
4. Klik button [Request OTP]
5. Verifikasi toast banner sukses muncul dengan pesan "Success, the code has been sent."
6. Verifikasi halaman berpindah ke rute Verify OTP
7. Verifikasi subtitle menampilkan email tujuan "Enter the 6-digit code sent to: yogasimanjuntak@qwertysystem.net"

### State loading dan tombol dinonaktifkan selama pemrosesan

8. Buka kembali halaman Request OTP dalam sesi baru
9. Masukkan email `sarimulyadi@qwertysystem.net` dan selesaikan reCAPTCHA
10. Klik button [Request OTP] dengan jaringan throttled (simulasi latency backend)
11. Verifikasi seketika setelah klik, button [Request OTP] menjadi disabled dan menampilkan ikon spinner loading
12. Verifikasi field Email menjadi read-only selama proses request berlangsung sehingga tidak dapat disunting

### Guard idempotensi: Double-click cepat hanya menerbitkan satu kode

13. Buka halaman Request OTP dalam sesi baru
14. Masukkan email `ekosetiawan@qwertysystem.net` dan selesaikan reCAPTCHA
15. Lakukan double-click atau triple-click dengan cepat pada button [Request OTP]
16. Verifikasi sistem menerapkan debounce/in-flight lock sehingga hanya 1 payload request yang terkirim ke endpoint server
17. Verifikasi pada mail-catcher hanya terdapat 1 email OTP baru yang diterima untuk `ekosetiawan@qwertysystem.net`, bukan ganda

### Integritas subject dan konten template email OTP

18. Buka halaman Request OTP, masukkan email `jokonugroho@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik [Request OTP]
19. Buka pesan email yang diterima di mail-catcher untuk `jokonugroho@qwertysystem.net`
20. Verifikasi subject email adalah "Your TAG Samurai one-time password (OTP)"
21. Verifikasi body email memuat logo TAG Samurai
22. Verifikasi body email memuat teks kode verifikasi 6 digit yang diformat jelas/tebal
23. Verifikasi terdapat keterangan masa berlaku kode adalah 5 menit
24. Verifikasi terdapat pesan peringatan keamanan untuk tidak membagikan kode kepada siapa pun

### Verifikasi SLA penerimaan email di bawah 2 menit

25. Catat timestamp saat button [Request OTP] diklik untuk `bagasmaulana@qwertysystem.net`
26. Polling inbox mail-catcher hingga email tiba
27. Verifikasi selisih waktu antara pengiriman request dan waktu email diterima di inbox tidak melebihi 120 detik (2 menit)

## Notes

- Subject email resmi yang disepakati adalah `Your TAG Samurai one-time password (OTP)` sesuai dengan konsensus NC-06.
- Idempotensi tombol request mencegah penembakan multi-request yang berpotensi menghabiskan kuota resend/request pengguna secara tidak sengaja.
