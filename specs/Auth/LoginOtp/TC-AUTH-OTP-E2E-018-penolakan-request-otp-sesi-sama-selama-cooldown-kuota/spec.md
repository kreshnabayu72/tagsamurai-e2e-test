---
id: TC-AUTH-OTP-E2E-018-penolakan-request-otp-sesi-sama-selama-cooldown-kuota
title: "Penolakan Request OTP Sesi Sama Selama Cooldown dan Kuota Habis"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-90
  - TC-AUTH-OTP-91
  - TC-AUTH-OTP-92
  - TC-AUTH-OTP-93
  - TC-AUTH-OTP-134
  - TC-AUTH-OTP-166
  - TC-AUTH-OTP-169
  - TC-AUTH-OTP-170
  - TC-AUTH-OTP-182
coverage:
  web: automated
---

# Penolakan Request OTP Sesi Sama Selama Cooldown dan Kuota Habis

## Prerequisites

- Belum login dan session kosong.
- User `Teguh Wulandari` (`teguhwulandari@qwertysystem.net`) profil BASE.
- User `Laras Puspita` (`laraspuspita@qwertysystem.net`) profil BASE.
- User `Irfan Damayanti` (`irfandamayanti@qwertysystem.net`) profil BASE.
- Akun Total Control Global Settings aktif untuk membaca log.

## Test Steps

### Penolakan Request OTP saat cooldown 10 menit aktif (NC-03)

1. Buka Request OTP untuk `teguhwulandari@qwertysystem.net`, habiskan kuota resend hingga masuk ke cooldown 10 menit
2. Buka URL langsung `/login/otp` di tab yang sama atau kembali ke Login with Password lalu masuk lagi ke Request OTP
3. Masukkan kembali email `teguhwulandari@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik [Request OTP]
4. Verifikasi request ditolak oleh backend
5. Verifikasi alert inline di atas button [Request OTP] menampilkan pesan: "Too many requests. Please try again later."
6. Verifikasi timer cooldown server tidak di-reset dan penolakan ini dicatat di log dengan Note "Request limit exceeded"

### Navigasi bolak-balik tidak mereset sesi server-side (NC-03)

7. Dari kondisi di atas, klik tautan [Use password instead] menuju halaman Login with Password
8. Dari Login with Password, klik tautan [Log in with OTP] kembali ke Request OTP
9. Coba kirimkan kembali Request OTP untuk email yang sama
10. Verifikasi sistem server-side tetap mengenali sesi email-request yang aktif dan menolak request dengan pesan yang sama

### Penghapusan data browser/storage tidak dapat membobol cooldown server (NC-03)

11. Buka jendela browser penyamaran baru (Incognito / clean storage)
12. Buka halaman Request OTP dan masukkan email `laraspuspita@qwertysystem.net` yang sedang dalam masa cooldown
13. Selesaikan reCAPTCHA dan klik [Request OTP]
14. Verifikasi backend menolak request berdasarkan identitas email dan status server-side, bukan berdasarkan cookie/storage lokal klien

### Penerimaan Request OTP setelah masa cooldown berakhir (NC-03)

15. Tunggu atau simulasikan waktu server hingga cooldown 10 menit untuk user `irfandamayanti@qwertysystem.net` selesai
16. Kirim [Request OTP] kembali untuk user tersebut
17. Verifikasi request diterima dan kode baru berhasil dikirimkan
18. Verifikasi counter server-side melanjutkan tracking sesi yang benar

## Notes

- Sesuai keputusan NC-03, sesi email-request melekat di sisi server per kombinasi email dan klien. Menutup tab, menghapus storage browser, atau berpindah ke halaman login password tidak mereset masa cooldown maupun kuota pengiriman.
- Penolakan di layar Request OTP menampilkan alert inline di atas tombol submit dengan teks `Too many requests. Please try again later.`
