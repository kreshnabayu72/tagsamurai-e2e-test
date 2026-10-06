---
id: TC-AUTH-OTP-E2E-010-screening-verify-otp-dan-input-keystroke
title: "Screening Halaman Verify OTP, Perilaku Keystroke, Auto-Advance, Paste, dan Backspace"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-07
  - TC-AUTH-OTP-40
  - TC-AUTH-OTP-41
  - TC-AUTH-OTP-42
  - TC-AUTH-OTP-43
  - TC-AUTH-OTP-44
  - TC-AUTH-OTP-45
  - TC-AUTH-OTP-46
  - TC-AUTH-OTP-47
  - TC-AUTH-OTP-69
coverage:
  web: automated
---

# Screening Halaman Verify OTP, Perilaku Keystroke, Auto-Advance, Paste, dan Backspace

## Prerequisites

- Belum login dan session kosong.
- User `Dewi Puspita` (`dewipuspita@qwertysystem.net`) profil BASE.
- User `Tiara Siregar` (`tiarasiregar@qwertysystem.net`) profil BASE.
- User `Rafi Cahyono` (`raficahyono@qwertysystem.net`) profil BASE.
- User `Mega Kusuma` (`megakusuma@qwertysystem.net`) profil BASE.
- User `Surya Saputra` (`suryasaputra@qwertysystem.net`) profil BASE.
- User `Nadia Kartika` (`nadiakartika@qwertysystem.net`) profil BASE.
- User `Teguh Firmansyah` (`teguhfirmansyah@qwertysystem.net`) profil BASE.
- User `Laras Nasution` (`larasnasution@qwertysystem.net`) profil BASE.
- User `Irfan Halim` (`irfanhalim@qwertysystem.net`) profil BASE.
- User `Sari Wijaya` (`sariwijaya@qwertysystem.net`) profil BASE.
- Mail-catcher aktif.

## Test Steps

### Screening UI halaman Verify OTP

1. Buka halaman Request OTP, masukkan `dewipuspita@qwertysystem.net`, centang reCAPTCHA, lalu klik [Request OTP]
2. Verifikasi halaman Verify OTP tampil di browser
3. Verifikasi title halaman adalah "Enter verification code"
4. Verifikasi subtitle menampilkan email lengkap tanpa sensor: "Enter the 6-digit code sent to: dewipuspita@qwertysystem.net"
5. Verifikasi tautan [Edit email] tampil di bawah subtitle
6. Verifikasi terdapat 6 kotak digit kosong berjajar dalam satu baris, kursor aktif di kotak digit 1
7. Verifikasi tombol [Verify] tersembunyi (Hidden pada happy path auto-submit)
8. Verifikasi teks Resend berada pada State A disabled: "Resend code in (00:59)"
9. Verifikasi tautan [Back to Login with Password] tampil di bagian footer

### Perilaku pengetikan digit tunggal dan auto-advance

10. Buka halaman Verify OTP untuk `tiarasiregar@qwertysystem.net`
11. Ketik karakter non-numerik seperti huruf "a", "Z", atau simbol "#" pada kotak 1
12. Verifikasi karakter non-numerik diabaikan dan kotak 1 tetap kosong
13. Ketik angka "1" pada kotak 1
14. Verifikasi kotak 1 terisi angka "1" dan fokus kursor otomatis berpindah ke kotak 2
15. Ketik angka "2", "3", "4", "5" berturut-turut pada kotak 2 hingga kotak 5
16. Verifikasi fokus berpindah secara otomatis ke kotak berikutnya dan tidak ada request verifikasi yang terpicu

### Digit ke-6 memicu verifikasi otomatis dan pembekuan form

17. Ketik digit ke-6 "6" pada kotak 6
18. Verifikasi pengisian kotak ke-6 seketika memicu auto-submit ke backend
19. Verifikasi seluruh 6 kotak digit dibekukan (disabled) dengan indikator loading aktif saat verifikasi berjalan

### Navigasi Backspace pada kotak digit

20. Buka kembali halaman Verify OTP untuk `irfanhalim@qwertysystem.net`
21. Ketik angka "1", "2", "3" sehingga kotak 1, 2, dan 3 terisi, kursor berada di kotak 4
22. Tekan tombol [Backspace] pada keyboard saat kursor berada di kotak 4 yang kosong
23. Verifikasi fokus kursor otomatis mundur ke kotak 3 dan nilai pada kotak 3 langsung terhapus

### Dukungan Paste (Tempel) kode lengkap 6 digit

24. Buka halaman Verify OTP untuk `suryasaputra@qwertysystem.net`
25. Tempel (Paste) string "123456" pada kotak digit 1
26. Verifikasi seluruh 6 kotak langsung terisi angka "1", "2", "3", "4", "5", "6" dan auto-submit terpicu secara instan

### Dukungan Paste string dengan spasi dan tanda hubung

27. Buka halaman Verify OTP untuk `nadiakartika@qwertysystem.net`
28. Tempel string berformat terpisah: "123-456" atau "12 34 56" pada kotak digit 1
29. Verifikasi sistem mengekstrak hanya karakter angka (sanitasi regex) sehingga 6 kotak terisi "123456" secara tepat

### Paste string lebih dari 6 digit

30. Buka halaman Verify OTP untuk `teguhfirmansyah@qwertysystem.net`
31. Tempel string 8 digit: "12345678" pada kotak digit 1
32. Verifikasi hanya 6 digit pertama ("123456") yang dimasukkan ke dalam form, sisa digit dibuang, dan auto-submit terpicu

### Paste pada kotak tengah (kotak 3)

33. Buka halaman Verify OTP untuk `larasnasution@qwertysystem.net`
34. Pindahkan kursor ke kotak digit 3 lalu tempel string "123456"
35. Verifikasi kotak 3, 4, 5, dan 6 terisi digit "1", "2", "3", "4", sementara kotak 1 dan 2 tetap kosong
36. Verifikasi auto-submit TIDAK terpicu karena kode belum lengkap 6 digit

### Pembersihan error state saat mengetik ulang (NC-10)

37. Buka halaman Verify OTP untuk `sariwijaya@qwertysystem.net`
38. Masukkan 6 digit salah (misal "000000") sehingga auto-submit memicu error "Incorrect verification code. Please try again." dan border kotak berubah merah (danger)
39. Verifikasi kotak digit dikosongkan otomatis dan kursor kembali ke kotak 1
40. Ketik satu digit sembarang pada kotak 1
41. Verifikasi caption error "Incorrect verification code. Please try again." dan border merah seketika hilang saat karakter pertama mulai diketik ulang

## Notes

- Kotak OTP dirancang dengan interaksi auto-advance demi kelancaran UX, di mana perpindahan fokus antar elemen input dikelola melalui event listener keystroke.
- Sesuai konsensus NC-10, caption error dan border bahaya dihapus segera pada keystroke pertama pengguna yang mencoba memasukkan kode baru.
