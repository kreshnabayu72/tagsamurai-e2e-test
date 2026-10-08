---
id: TC-AUTH-OTP-E2E-014-invalidasi-kode-setelah-5x-verify-salah
title: "Invalidasi Kode OTP Setelah 5 Kali Percobaan Salah dan Reset Counter per Kode"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-65
  - TC-AUTH-OTP-66
  - TC-AUTH-OTP-67
  - TC-AUTH-OTP-122
coverage:
  web: automated
---

# Invalidasi Kode OTP Setelah 5 Kali Percobaan Salah dan Reset Counter per Kode

## Prerequisites

- Belum login dan session kosong.
- User `Lestari Wulandari` (`lestariwulandari@qwertysystem.net`) profil BASE.
- User `Bayu Puspita` (`bayupuspita@qwertysystem.net`) profil BASE.
- User `Intan Damayanti` (`intandamayanti@qwertysystem.net`) profil BASE.
- Mail-catcher aktif untuk mencatat kode asli yang dikirimkan.
- Akun admin Total Control Global Settings aktif untuk memeriksa entri audit log.

## Test Steps

### Batas toleransi: Percobaan salah ke-4 masih mengizinkan kode benar

1. Buka Request OTP untuk user `bayupuspita@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik [Request OTP]
2. Catat kode OTP asli yang diterima di mail-catcher (contoh: "888222")
3. Pada layar Verify OTP, masukkan kode salah ("000001") sebanyak 4 kali berturut-turut
4. Verifikasi setiap kegagalan ke-1 sampai ke-4 menampilkan caption "Incorrect verification code. Please try again."
5. Pada percobaan ke-5, masukkan kode OTP asli yang benar ("888222")
6. Verifikasi sistem menerima kode benar tersebut dan berhasil mengalihkan pengguna ke Product Hub

### Percobaan salah ke-5 memicu invalidasi permanen kode (NC-05)

7. Buka Request OTP untuk `lestariwulandari@qwertysystem.net`, kirim kode OTP, catat kode asli (contoh: "111333")
8. Pada layar Verify OTP, masukkan kode salah berturut-turut sebanyak 5 kali ("000001", "000002", "000003", "000004", "000005")
9. Verifikasi pada kesalahan ke-5 kode OTP langsung dinyatakan invalid oleh backend
10. Masukkan kode asli yang benar ("111333") pada percobaan berikutnya
11. Verifikasi kode asli yang benar ditolak oleh server dengan pesan error penolakan
12. Periksa audit trail di User Log / Activity Log Session: verifikasi tercatat entri "Failed" dengan Note "OTP invalidated due to max attempts"

### Reset counter kesalahan saat menerbitkan kode baru via Resend (NC-05)

13. Buka Request OTP untuk `intandamayanti@qwertysystem.net`, kirim kode pertama (Kode A)
14. Masukkan kode salah sebanyak 4 kali pada Kode A
15. Tunggu hingga tombol [Resend code] aktif (setelah 60 detik)
16. Klik button [Resend code] untuk menerbitkan kode baru (Kode B)
17. Verifikasi counter kesalahan 5x di-reset ke 0 untuk Kode B
18. Masukkan kode salah sebanyak 2 kali pada Kode B
19. Masukkan kode asli Kode B yang benar
20. Verifikasi Kode B diterima dan login berhasil, membuktikan bahwa counter kesalahan dihitung strictly per kode dan di-reset saat kode baru terbit

## Notes

- Sesuai konsensus NC-05, batas toleransi verifikasi salah adalah 5 kali. Pada kegagalan ke-5, kode yang bersangkutan di-invalidate di server-side, sehingga input kode yang benar sesudahnya tetap akan ditolak.
- Counter percobaan salah melekat pada instance kode OTP, bukan pada user secara permanen. Penerbitan kode baru melalui Resend atau Request baru memulai counter dari nol.
