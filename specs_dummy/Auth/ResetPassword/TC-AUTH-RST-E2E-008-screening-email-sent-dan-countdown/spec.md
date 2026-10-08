---
id: TC-AUTH-RST-E2E-008-screening-email-sent-dan-countdown
title: "Screening halaman Email Sent!, countdown timer Resend, dan navigasi kembali"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-39
  - TC-AUTH-RST-40
  - TC-AUTH-RST-41
  - TC-AUTH-RST-45
  - TC-AUTH-RST-51
coverage:
  web: automated
---

# Screening halaman Email Sent!, countdown timer Resend, dan navigasi kembali

## Prerequisites

- User belum login (guest); baru saja menyelesaikan Request Reset untuk `budisantoso@qwertysystem.net` dan mendarat di `/email-sent`.
- Environment uji terisolasi khusus pengujian otomatis.

## Test Steps

### Screening elemen halaman Email Sent!

1. Amati tampilan halaman Email Sent! dari atas ke bawah
2. Verifikasi logo TAG Samurai tampil di bagian tengah atas
3. Verifikasi title halaman adalah "Email Sent!"
4. Verifikasi subtitle halaman berbunyi: "We've sent a link to budisantoso@qwertysystem.net to reset your password. Please check your inbox and follow the instructions."
5. Verifikasi bagian Resend memuat teks pengantar "Didn't receive the email? "
6. Verifikasi tombol [Resend email] tampil dalam keadaan disabled dengan label teks countdown "Resend in 1:00"
7. Verifikasi tombol [Back to Login] tampil dengan styling secondary / outline di bagian bawah

### Countdown timer Resend dan pencegahan klik

8. Amati teks countdown pada tombol [Resend email] selama cooldown berjalan
9. Verifikasi angka detik berkurang secara berurutan (misal: "Resend in 0:59", "Resend in 0:58", dst.)
10. Lakukan klik pada tombol [Resend email] saat countdown masih aktif
11. Verifikasi tombol tidak dapat diklik (non-clickable) dan tidak ada panggilan request baru yang dikirimkan

### Pengaktifan tombol [Resend email] setelah 60 detik

12. Tunggu hingga durasi cooldown 60 detik selesai penuh
13. Verifikasi label tombol berubah menjadi teks murni "[Resend email]" tanpa embel-embel countdown
14. Verifikasi tombol [Resend email] berubah status menjadi enabled (dapat diklik)

### Posisi Toast notifikasi

15. Klik tombol [Resend email] yang telah aktif
16. Verifikasi toast notifikasi muncul di sudut kanan bawah layar (bottom-right viewport)
17. Verifikasi toast menampilkan pesan hasil operasi dengan styling yang sesuai

### Navigasi tombol [Back to Login]

18. Klik tombol [Back to Login] pada halaman Email Sent!
19. Verifikasi browser berpindah kembali ke halaman Login with Password (`/login`)
20. Verifikasi field Email di form Login terisi dengan alamat email user

## Notes

- Sesuai PRD §4.1 S-AUTHRST-02, §4.2 Halaman 2, dan FI-AUTHRST-05/06, tombol Resend email dinonaktifkan dengan countdown format `[m:ss]` selama 60 detik dan aktif kembali secara otomatis saat waktu habis.
- Sesuai PRD §7 T-AUTHRST-01 dan `TC-AUTH-RST-51`, seluruh toast hasil operasi Resend dirender di posisi standar pojok kanan bawah layar.
