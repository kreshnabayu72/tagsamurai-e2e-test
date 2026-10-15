---
id: TC-AUTH-OTP-E2E-012-kotak-digit-input-ui
title: "Perilaku Input Kotak 6 Digit OTP: Perpindahan Kursor, Filter Angka, Paste Parsial, dan Backspace"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-40
  - TC-AUTH-OTP-41
  - TC-AUTH-OTP-46
  - TC-AUTH-OTP-47
coverage:
  web: automated
---

# Perilaku Input Kotak 6 Digit OTP: Perpindahan Kursor, Filter Angka, Paste Parsial, dan Backspace

## Prerequisites

- Mode: FE+BE (halaman Verify OTP dicapai lewat Request OTP nyata; tidak ada kode yang diverifikasi di spec ini).
- Tidak ada akun aktor. Browser tanpa sesi login (halaman Login with OTP adalah halaman publik).
- Environment variable: `OTP_PASSWORD` (password user uji yang dipasang saat seeding; tidak ada password atau token di spec atau fixture). Nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-012`, profil BASE (Activated, Active ON, sudah login sukses di web pada device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru ada; Agreement dan MFA tidak terpicu), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-40: `Tiara Siregar` (`tiarasiregar+{runId}-012@qwertysystem.net`)
  - TC-AUTH-OTP-41: `Rafi Cahyono` (`raficahyono+{runId}-012@qwertysystem.net`)
  - TC-AUTH-OTP-46: `Laras Nasution` (`larasnasution+{runId}-012@qwertysystem.net`)
  - TC-AUTH-OTP-47: `Irfan Halim` (`irfanhalim+{runId}-012@qwertysystem.net`)
- Kemampuan teknis: mail-catcher tidak dibaca di spec ini (email OTP terkirim, tetapi kodenya tidak dipakai); reCAPTCHA mode uji di environment (centang tanpa tantangan); pengamatan permintaan jaringan browser (untuk memastikan tidak ada permintaan verifikasi pada TC-AUTH-OTP-40 dan TC-AUTH-OTP-46); penulisan clipboard browser (TC-AUTH-OTP-46).

## Test Steps

### TC-AUTH-OTP-40: Mengetik digit 1 sampai 5 memindahkan kursor ke kotak berikutnya tanpa memicu verifikasi

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser tanpa sesi
2. Ketik `tiarasiregar+{runId}-012@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
3. Ketik digit `4`, `8`, `1`, `9`, `0` satu per satu pada kotak yang aktif
4. Verifikasi setiap digit mengisi satu kotak berurutan dari kotak 1 sampai kotak 5
5. Verifikasi kursor berpindah otomatis ke kotak berikutnya setelah tiap digit
6. Verifikasi kursor berada di kotak 6
7. Verifikasi kotak 6 masih kosong
8. Verifikasi tidak ada permintaan verifikasi yang dikirim
9. Verifikasi tidak ada caption error

### TC-AUTH-OTP-41: Kotak digit hanya menerima angka 0-9

10. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
11. Ketik `raficahyono+{runId}-012@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
12. Ketik huruf `a` pada kotak 1
13. Verifikasi huruf `a` tidak masuk ke kotak 1 dan kotak 1 tetap kosong
14. Ketik simbol `#` pada kotak 1
15. Verifikasi simbol `#` tidak masuk ke kotak 1 dan kotak 1 tetap kosong
16. Verifikasi tidak ada caption error
17. Ketik digit `7` pada kotak 1
18. Verifikasi digit `7` masuk ke kotak 1
19. Verifikasi kursor berpindah ke kotak 2

### TC-AUTH-OTP-46: Paste 6 digit pada kotak 3 mengisi mulai kotak 3 dan tidak memicu verifikasi

20. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
21. Ketik `larasnasution+{runId}-012@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
22. Salin teks `123456` ke clipboard
23. Klik kotak 3 dan tekan Ctrl+V
24. Verifikasi kotak 3 sampai 6 terisi `1`, `2`, `3`, `4`
25. Verifikasi digit `5` dan `6` dibuang
26. Verifikasi kotak 1 dan kotak 2 tetap kosong
27. Verifikasi verifikasi otomatis tidak terpicu selama 6 kotak belum terisi
28. Verifikasi fokus berada di kotak 1 (kotak kosong pertama)

### TC-AUTH-OTP-47: Backspace pada kotak kosong memindahkan fokus ke kotak sebelumnya dan menghapus nilainya

29. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
30. Ketik `irfanhalim+{runId}-012@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
31. Ketik digit `4`, `8`, `1` pada kotak 1 sampai 3
32. Verifikasi kursor berada di kotak 4 yang kosong
33. Tekan Backspace satu kali
34. Verifikasi fokus pindah ke kotak 3
35. Verifikasi nilai `1` pada kotak 3 terhapus
36. Verifikasi kotak 1 dan 2 tetap berisi `4` dan `8`
37. Verifikasi tidak ada caption error

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 2, 11, 21, dan 30 menggabungkan tiga aksi form yang berurutan (ketik email, centang reCAPTCHA, klik [Request OTP]) menjadi satu baris karena persis sama dengan prasyarat TC; langkah 10, 20, dan 29 (buka ulang halaman Request OTP) adalah langkah penghubung antar-TC (S-03) agar tiap TC memakai user dan sesi email-request sendiri.
- Urutan TC mengikuti TC sumber (40, 41, 46, 47); tidak ada penyimpangan urutan.
- Spec ini 37 langkah (melewati smell sekitar 35) karena empat TC kotak digit yang satu topik, satu layar, dan satu harness (tanpa mail-catcher); tiap TC berdiri sendiri lewat buka ulang halaman dan user sendiri sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal. Tidak ada pengecualian P-1, P-2, atau P-3 yang dipakai.
- Temuan untuk QA: (1) TC-AUTH-OTP-40 dan TC-AUTH-OTP-46 menyebut "tidak ada permintaan verifikasi" tanpa menyebut cara mengamatinya; spec memakai pengamatan permintaan jaringan browser dan mencatatnya sebagai kemampuan teknis. (2) TC-AUTH-OTP-46 Expected b menulis "fokus berada di kotak 1 (kotak kosong pertama)" sehingga paste pada kotak 3 menempatkan fokus di kotak 1, sedangkan kotak 3 sampai 6 sudah terisi; konsisten dengan NC-18 dan diikuti apa adanya.
