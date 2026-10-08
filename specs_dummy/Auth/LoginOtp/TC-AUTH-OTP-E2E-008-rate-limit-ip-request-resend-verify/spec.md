---
id: TC-AUTH-OTP-E2E-008-rate-limit-ip-request-resend-verify
title: "Batasan IP Rate Limit pada Request, Resend, dan Verify OTP"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-33
  - TC-AUTH-OTP-34
  - TC-AUTH-OTP-63
  - TC-AUTH-OTP-85
  - TC-AUTH-OTP-135
coverage:
  web: automated
---

# Batasan IP Rate Limit pada Request, Resend, dan Verify OTP

## Prerequisites

- Mode: mock / rate-limit threshold simulation. Digunakan intercept atau konfigurasi mock threshold IP rate limit untuk memicu respons HTTP 429.
- Belum login dan session kosong. Halaman `Auth > Login with OTP` terbuka di browser.
- User `Wulan Hakim` (`wulanhakim@qwertysystem.net`) profil BASE.
- User `Fajar Harahap` (`fajarharahap@qwertysystem.net`) profil BASE.
- User `Mega Setiawan` (`megasetiawan@qwertysystem.net`) profil BASE.
- User alternatif `Bambang Kusuma` (`bambang@qwertysystem.net`) profil BASE.
- Akun Total Control Global Settings disiapkan untuk memverifikasi entri log.

## Test Steps

### IP Rate Limit pada Request OTP

1. Buka halaman Request OTP di browser
2. Masukkan email `wulanhakim@qwertysystem.net`
3. Simulasikan pengiriman request berulang dari alamat IP yang sama hingga mencapai threshold rate limit
4. Kirim satu request tambahan dengan klik [Request OTP]
5. Verifikasi server mengembalikan status HTTP 429 Too Many Requests
6. Verifikasi alert inline di atas button [Request OTP] menampilkan pesan "Too many requests. Please try again later."
7. Verifikasi tidak ada pengiriman email kode OTP baru

### Blokir IP bersifat agnostik terhadap pergantian email

8. Tanpa mengubah koneksi jaringan (IP tetap sama yang terblokir), ganti input email menjadi `bambang@qwertysystem.net`
9. Centang reCAPTCHA dan klik button [Request OTP]
10. Verifikasi request tetap ditolak dengan pesan "Too many requests. Please try again later."
11. Verifikasi sistem menegakkan rate limit berbasis IP origin, bukan berbasis akun email

### IP Rate Limit pada aksi Resend Code

12. Buka halaman Verify OTP untuk user `megasetiawan@qwertysystem.net`
13. Tunggu hingga tombol [Resend code] aktif (setelah 60 detik)
14. Simulasikan batas IP rate limit terlampaui pada endpoint resend (`POST /auth/otp/resend`)
15. Klik button [Resend code]
16. Verifikasi muncul notifikasi/caption error "Too many requests. Please try again later."
17. Verifikasi kuota resend pengguna tidak berkurang dan counter resend tidak bertambah karena penolakan terjadi di layer IP

### IP Rate Limit pada aksi Verify OTP dan preservasi input digit

18. Pada halaman Verify OTP untuk user `fajarharahap@qwertysystem.net`, masukkan 6 digit angka sembarang (misal: "123456")
19. Simulasikan batas IP rate limit terlampaui pada endpoint verify (`POST /auth/otp/verify`)
20. Picu verifikasi kode
21. Verifikasi muncul caption error "Too many requests. Please try again later."
22. Verifikasi 6 digit yang sudah diketik di kotak digit TIDAK dikosongkan (tetap bertahan) sehingga pengguna tidak perlu mengetik ulang setelah jeda waktu

### Pencatatan log untuk insiden IP Rate Limit

23. Buka sesi Total Control Global Settings di tab terpisah
24. Buka `Global Settings > Activity Log > Session`
25. Verifikasi insiden penolakan rate limit tercatat dengan status "Failed" dan catatan Note "IP rate limit exceeded" bersama IP address yang bersangkutan

## Notes

- Threshold IP rate limit saat ini ditandai sebagai implementasi engineering per-environment (GAP-OTP-E2E-001).
- Sesuai konsensus NC-10, saat penolakan rate limit terjadi pada layar Verify OTP, kotak digit TIDAK boleh dikosongkan, berbeda dari skenario kode salah atau kadaluwarsa.
