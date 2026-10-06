---
id: TC-AUTH-OTP-E2E-019-preservasi-state-verify-otp-f5-back-url
title: "Preservasi State Verify OTP: Refresh (F5), Tombol Back Browser, dan Akses URL Langsung"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-70
  - TC-AUTH-OTP-71
  - TC-AUTH-OTP-73
  - TC-AUTH-OTP-179
coverage:
  web: automated
---

# Preservasi State Verify OTP: Refresh (F5), Tombol Back Browser, dan Akses URL Langsung

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP` terbuka di browser.
- User `Eko Permata` (`ekopermata@qwertysystem.net`) profil BASE.
- User `Ratna Fitriani` (`ratnafitriani@qwertysystem.net`) profil BASE.
- Mail-catcher aktif.

## Test Steps

### Perilaku Refresh / Muat Ulang Halaman (F5) di layar Verify OTP (NC-08)

1. Buka halaman Request OTP, masukkan `ekopermata@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik [Request OTP]
2. Verifikasi halaman Verify OTP tampil dengan subtitle "Enter the 6-digit code sent to: ekopermata@qwertysystem.net"
3. Biarkan timer countdown berjalan beberapa detik (misal hingga (00:45))
4. Lakukan reload / refresh halaman browser (tekan F5 atau reload browser)
5. Verifikasi browser TETAP berada pada halaman Verify OTP (tidak ditendang ke halaman login awal)
6. Verifikasi email tujuan pada subtitle tetap terisi `ekopermata@qwertysystem.net`
7. Verifikasi nilai timer countdown melanjutkan sisa waktu aktual yang sinkron dengan server
8. Ambil kode OTP asli yang dikirim di awal dari mail-catcher, masukkan ke kotak digit
9. Verifikasi kode tetap valid dan verifikasi sukses, membuktikan refresh tidak meng-invalidate kode

### Perilaku tombol Back browser dari Verify OTP (NC-08)

10. Buka Request OTP untuk `ratnafitriani@qwertysystem.net`, kirim kode OTP hingga halaman Verify OTP tampil
11. Klik tombol [Back] pada browser
12. Verifikasi browser kembali ke halaman Request OTP
13. Verifikasi field Email di Request OTP tetap terisi `ratnafitriani@qwertysystem.net`
14. Klik tombol [Forward] kembali ke Verify OTP, lalu masukkan kode OTP dari mail-catcher
15. Verifikasi kode OTP belum di-invalidate dan login berhasil

### Akses langsung ke URL Verify OTP tanpa state / sesi pra-autentikasi (NC-08)

16. Buka tab browser baru yang bersih tanpa session storage
17. Masukkan langsung URL Verify OTP (`/login/otp/verify`) pada address bar browser
18. Verifikasi layar Verify OTP tidak ditampilkan dan browser otomatis dialihkan (redirect) ke halaman Request OTP (`/login/otp`)
19. Verifikasi field Email dalam keadaan kosong dengan placeholder "Enter your email"

## Notes

- Sesuai konsensus NC-08, halaman Verify OTP menyimpan identitas sesi sementara di sessionStorage untuk menoleransi ketidaksengajaan refresh halaman (F5) oleh pengguna.
- Akses langsung tanpa context state otomatis diarahkan kembali ke gerbang awal (Request OTP).
