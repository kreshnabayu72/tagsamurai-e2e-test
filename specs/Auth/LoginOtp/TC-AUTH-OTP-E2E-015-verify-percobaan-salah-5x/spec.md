---
id: TC-AUTH-OTP-E2E-015-verify-percobaan-salah-5x
title: "Batas 5 Kali Verify Salah pada Kode yang Sama dan Dampaknya terhadap Login with Password"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-65
  - TC-AUTH-OTP-66
  - TC-AUTH-OTP-68
coverage:
  web: automated
---

# Batas 5 Kali Verify Salah pada Kode yang Sama dan Dampaknya terhadap Login with Password

## Prerequisites

- Mode: FE+BE.
- Tidak ada akun aktor. Browser tanpa sesi login (halaman Login with OTP adalah halaman publik).
- Environment variable: `OTP_PASSWORD` (password user uji yang dipasang saat seeding dan dipakai login pada TC-AUTH-OTP-68; tidak ada password atau token di spec atau fixture). Nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-015`, profil BASE (Activated, Active ON, sudah login sukses di web pada device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru ada; Agreement dan MFA tidak terpicu), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-65: `Lestari Wulandari` (`lestariwulandari+{runId}-015@qwertysystem.net`)
  - TC-AUTH-OTP-66: `Bayu Puspita` (`bayupuspita+{runId}-015@qwertysystem.net`)
  - TC-AUTH-OTP-68: `Yoga Wibowo` (`yogawibowo+{runId}-015@qwertysystem.net`), password `Spectra.env.OTP_PASSWORD`, lock progression password pada nilai awal
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji di environment (centang tanpa tantangan) pada halaman Login with OTP dan Login with Password; countdown Resend 60 detik (TC-AUTH-OTP-65, langkah 11) dilewati dengan memajukan jam server dan jam browser (countdown UI berjalan di jam klien) bersama sebesar 60 detik, lalu menunggu UI menyegarkan tombol Resend (§6); jam keduanya dipulihkan di hook `after`, dan suite yang memanipulasi jam berjalan serial.
- Kode salah yang diketik adalah `000000` (kode yang berbeda dari kode yang diterbitkan untuk user itu).
- State yang berubah: ketiga TC diakhiri dengan login sukses; langkah logout dari Portal — Product Hub ada di antara TC dan hook `after` menutup sesi yang tersisa.

## Test Steps

### TC-AUTH-OTP-65: Kode benar ditolak setelah 5 kali verify salah pada kode yang sama

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser tanpa sesi
2. Ketik `lestariwulandari+{runId}-015@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
3. Ketik 5 kali berturut-turut 6 digit kode yang salah (`000000`) pada kotak digit; setiap percobaan ditolak
4. Verifikasi setiap dari 5 percobaan ditolak dengan caption "Invalid code"
5. Ketik 6 digit kode OTP dari email (mail-catcher `lestariwulandari+{runId}-015@qwertysystem.net`) pada kotak digit
6. Verifikasi percobaan ke-6 dengan kode yang benar ditolak: kotak digit menampilkan shake animation
7. Verifikasi kotak digit berborder severity danger
8. Verifikasi caption error di bawah kotak digit: "Invalid code"
9. Verifikasi tidak ada sesi yang dibuat
10. Verifikasi tidak ada teks atau tombol baru yang muncul selain tombol Resend yang mengikuti state timernya
11. Tunggu countdown 60 detik selesai
12. Klik [Resend code]
13. Ketik 6 digit kode baru dari email Resend pada kotak digit
14. Verifikasi kode baru dari Resend diterima: verifikasi berhasil
15. Verifikasi browser dialihkan ke Portal — Product Hub
16. Verifikasi sesi aktif untuk `Lestari Wulandari`

### TC-AUTH-OTP-66: Kode benar diterima setelah 4 kali verify salah

17. Logout dari Portal — Product Hub dan buka halaman `Auth > Login with OTP > Request OTP`
18. Ketik `bayupuspita+{runId}-015@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
19. Ketik 4 kali berturut-turut 6 digit kode yang salah (`000000`) pada kotak digit; setiap percobaan ditolak
20. Verifikasi setiap dari 4 percobaan ditolak dengan caption "Invalid code"
21. Ketik 6 digit kode OTP dari email (mail-catcher `bayupuspita+{runId}-015@qwertysystem.net`) pada kotak digit
22. Verifikasi percobaan ke-5 dengan kode benar berhasil: browser dialihkan ke Portal — Product Hub
23. Verifikasi sesi aktif untuk `Bayu Puspita`

### TC-AUTH-OTP-68: Kegagalan OTP tidak menambah lock progression Login with Password

24. Logout dari Portal — Product Hub dan buka halaman `Auth > Login with OTP > Request OTP`
25. Ketik `yogawibowo+{runId}-015@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
26. Ketik 5 kali berturut-turut 6 digit kode yang salah (`000000`) pada kotak digit
27. Klik tautan [Back to Login with Password]
28. Isi Email `yogawibowo+{runId}-015@qwertysystem.net` dan Password `Spectra.env.OTP_PASSWORD`, selesaikan reCAPTCHA, lalu klik [Log in]
29. Verifikasi Login with Password berhasil tanpa caption akun terkunci
30. Verifikasi browser dialihkan ke Portal — Product Hub
31. Verifikasi sesi aktif untuk `Yoga Wibowo`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- caseType Negative: alur dominan spec ini adalah penolakan kode benar setelah 5 kali salah (TC-AUTH-OTP-65, P0, Negative); TC-AUTH-OTP-66 (Boundary) dan TC-AUTH-OTP-68 (Positive) mengikuti pemilihan jenis TC berprioritas tertinggi.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 17 dan 24 adalah langkah penghubung antar-TC (S-03, S-09): logout dari sesi hasil TC sebelumnya lalu buka ulang halaman Request OTP agar konteks bersih. Langkah 2, 18, dan 25 menggabungkan ketik email, centang reCAPTCHA, dan klik [Request OTP] menjadi satu baris karena persis sama dengan prasyarat TC.
- Langkah 4 dan 20 (caption "Invalid code" pada tiap percobaan salah di tengah rangkaian) adalah asersi state perantara yang tidak ada di Expected TC; ditambahkan agar jumlah percobaan salah terbukti benar-benar tertolak sebelum kode benar dicoba (S-03, S-14).
- Asersi absence TC-AUTH-OTP-68 Expected c dan Post Condition butir b ("tidak ada entri `Locked 15 minutes`, `Locked 1 hour`, `Locked requires reset`, atau `Account locked` pada log `Yoga Wibowo`") dipindah ke spec 047 (prinsip 13g, S-05); spec ini membuktikan lock progression tidak berubah lewat login password yang tetap berhasil tanpa caption akun terkunci. Pembagian TC dicatat juga di Notes spec 047.
- Pencatatan Failed `Incorrect OTP` pada percobaan ke-5 dan setelahnya diuji di spec pencatatan Failed Verify OTP (TC-AUTH-OTP-122).
- Temuan untuk QA: (1) TC-AUTH-OTP-65 Expected b/c tidak menyebut apakah kotak digit dikosongkan setelah penolakan kode benar yang di-invalidasi; spec tidak mengasersinya. (2) TC-AUTH-OTP-68 langkah 7 menyebut "login dengan email ... dan password yang benar" tanpa menyebut reCAPTCHA di Login with Password; spec menambahkan "selesaikan reCAPTCHA" mengikuti pola spec Auth lain.
