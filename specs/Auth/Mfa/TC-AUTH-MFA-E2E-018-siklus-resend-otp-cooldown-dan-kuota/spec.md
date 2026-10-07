---
id: TC-AUTH-MFA-E2E-018-siklus-resend-otp-cooldown-dan-kuota
title: "Siklus Resend OTP: Cooldown 60 Detik, Batas Kuota 5 Kali, dan Interaksi Antar-Layar"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-77
  - TC-AUTH-MFA-78
  - TC-AUTH-MFA-79
  - TC-AUTH-MFA-80
  - TC-AUTH-MFA-81
  - TC-AUTH-MFA-82
  - TC-AUTH-MFA-85
  - TC-AUTH-MFA-200
coverage:
  web: automated
---
# Siklus Resend OTP: Cooldown 60 Detik, Batas Kuota 5 Kali, dan Interaksi Antar-Layar

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- User `Dimas Rahmawati` (`dimasrahmawati@qwertysystem.net`) profil NEWDEV.
- User `Rian Hidayat` (`rianhidayat@qwertysystem.net`) profil NEWDEV.
- Mail-catcher lingkungan uji aktif.
- Mock interceptor jaringan untuk pengujian kegagalan timeout pada request resend.

## Test Steps

### Cooldown 60 detik dengan hitung mundur di dalam label tombol

1. Buka alur OTP Verification untuk user `rianhidayat@qwertysystem.net`
2. Verifikasi tombol Resend dalam keadaan disabled dengan label menampilkan hitung mundur ("Resend code in 59s" ... "Resend code in 1s")
3. Verifikasi server menolak jika request API resend ditembak sebelum 60 detik (sesuai NC-08 dan TC-85)
4. Tunggu hitung mundur 60 detik berakhir
5. Verifikasi label tombol berubah menjadi "Resend code" dan status tombol berubah menjadi enabled

### Resend berhasil menerbitkan kode baru dan menampilkan toast sukses

6. Klik tombol [Resend code]
7. Verifikasi toast "Success, the code has been sent." tampil di pojok kanan bawah
8. Verifikasi tombol kembali berstatus disabled dengan hitung mundur "Resend code in 59s"
9. Periksa mail-catcher dan verifikasi kode OTP baru diterima serta dapat dipakai untuk verifikasi

### Penanganan retry setelah timeout pada request Resend

10. Siapkan interceptor untuk memicu timeout pada request resend berikutnya untuk `dimasrahmawati@qwertysystem.net`
11. Klik [Resend code] saat ready
12. Verifikasi setelah timeout toast error tampil: "Error, failed to send the code." dan kode OTP sebelumnya tetap berlaku
13. Hentikan simulasi timeout dan lakukan resend ulang setelah hitung mundur
14. Verifikasi resend berhasil memunculkan toast "Success, the code has been sent." dan dihitung sebagai percobaan baru terhadap kuota 5 kali

### Batas kuota 5 kali Resend per sesi pre-auth

15. Lakukan resend berturut-turut hingga mencapai batas 5 kali pengiriman ulang (total 6 kode OTP)
16. Verifikasi setelah resend ke-5, tombol [Resend code] menjadi disabled permanen tanpa hitung mundur
17. Verifikasi teks statis pendamping tampil: "You've used all your resend attempts. Use a different method." (sesuai keputusan NC-14)

### Interaksi memilih OTP lagi dari Choose Verification Method saat cooldown atau kuota habis

18. Saat cooldown resend masih berjalan, klik button Text [Use a different method]
19. Pada halaman Choose Verification Method, pilih kembali opsi "OTP via email" lalu klik [Login]
20. Verifikasi sesuai NC-08, sistem TIDAK mengirim email baru; pengguna kembali ke halaman OTP Verification dengan kode terakhir yang tetap berlaku dan hitung mundur cooldown dilanjutkan
21. Saat kuota 5 kali resend telah habis, kembali ke Choose Method dan pilih "OTP via email"
22. Verifikasi email baru tidak dikirim dan halaman OTP Verification menampilkan tombol resend yang tetap disabled dengan teks batas kuota

## Notes

- Sesuai PRD §9.2 F-AUTHMFA-04 dan keputusan NC-08 & NC-14, batas resend 5 kali berlaku per sesi pre-auth.
- Navigasi bolak-balik antara Choose Method dan OTP Verification tidak mereset kuota atau cooldown.
