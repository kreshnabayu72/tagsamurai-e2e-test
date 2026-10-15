---
id: TC-AUTH-OTP-E2E-013-paste-dan-auto-submit
title: "Paste Kode OTP dan Verifikasi Otomatis pada Digit ke-6"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-42
  - TC-AUTH-OTP-43
  - TC-AUTH-OTP-44
  - TC-AUTH-OTP-45
coverage:
  web: automated
---

# Paste Kode OTP dan Verifikasi Otomatis pada Digit ke-6

## Prerequisites

- Mode: FE+BE (Verify OTP terhadap backend nyata; penahanan respons memakai intercept parsial di atas backend nyata).
- Tidak ada akun aktor. Browser tanpa sesi login (halaman Login with OTP adalah halaman publik).
- Environment variable: `OTP_PASSWORD` (password user uji yang dipasang saat seeding; tidak ada password atau token di spec atau fixture). Nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-013`, profil BASE (Activated, Active ON, sudah login sukses di web pada device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru ada; Agreement dan MFA tidak terpicu), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-44: `Nadia Kartika` (`nadiakartika+{runId}-013@qwertysystem.net`)
  - TC-AUTH-OTP-45: `Teguh Firmansyah` (`teguhfirmansyah+{runId}-013@qwertysystem.net`)
  - TC-AUTH-OTP-42: `Mega Kusuma` (`megakusuma+{runId}-013@qwertysystem.net`)
  - TC-AUTH-OTP-43: `Surya Saputra` (`suryasaputra+{runId}-013@qwertysystem.net`)
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji di environment (centang tanpa tantangan); `Spectra.intercept()` untuk menahan respons Verify OTP 5 detik (TC-AUTH-OTP-42), dilepas di langkah spec dan dipulihkan di hook `after` bila spec gagal di tengah; pengamatan permintaan jaringan browser (jumlah permintaan Verify OTP dan kode yang dikirim); penulisan clipboard browser.
- Kode yang dipaste pada TC-AUTH-OTP-44 (`481902`) dan TC-AUTH-OTP-45 (`123456`) adalah kode uji yang diasumsikan tidak sama dengan kode yang diterbitkan untuk user itu (lihat Temuan untuk QA).
- State yang berubah: TC-AUTH-OTP-42 dan TC-AUTH-OTP-43 menghasilkan sesi web aktif; langkah logout dari Portal — Product Hub ada di antara TC, dan hook `after` menutup sesi yang tersisa.

## Test Steps

### TC-AUTH-OTP-44: Paste teks berisi spasi dan tanda hubung hanya mengambil karakter angka

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser tanpa sesi
2. Ketik `nadiakartika+{runId}-013@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
3. Salin teks `48 19-02` ke clipboard
4. Klik kotak 1 dan tekan Ctrl+V
5. Verifikasi kotak 1 sampai 6 terisi `4`, `8`, `1`, `9`, `0`, `2`
6. Verifikasi spasi dan tanda hubung dibuang
7. Verifikasi verifikasi otomatis terpicu satu kali dengan kode `481902`

### TC-AUTH-OTP-45: Paste lebih dari 6 digit mengisi 6 digit pertama dan membuang sisanya

8. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
9. Ketik `teguhfirmansyah+{runId}-013@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
10. Salin teks `12345678` ke clipboard
11. Klik kotak 1 dan tekan Ctrl+V
12. Verifikasi kotak 1 sampai 6 terisi `1`, `2`, `3`, `4`, `5`, `6`
13. Verifikasi digit `7` dan `8` dibuang
14. Verifikasi verifikasi otomatis terpicu satu kali dengan kode `123456`
15. Verifikasi tidak ada kotak ke-7

### TC-AUTH-OTP-42: Kotak digit dibekukan dengan indikator loading saat digit ke-6 memicu verifikasi

16. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
17. Ketik `megakusuma+{runId}-013@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
18. Tahan respons Verify OTP selama 5 detik (delay network)
19. Ketik 6 digit kode OTP dari email (mail-catcher `megakusuma+{runId}-013@qwertysystem.net`) pada kotak digit
20. Verifikasi setelah digit ke-6 diketik, verifikasi berjalan otomatis tanpa klik tombol apa pun
21. Amati kotak digit selama 5 detik
22. Verifikasi selama menunggu respons, 6 kotak digit dibekukan (kursor disabled)
23. Verifikasi selama menunggu respons, indikator loading subtle tampil
24. Lepaskan respons yang ditahan
25. Verifikasi browser dialihkan ke Portal — Product Hub
26. Verifikasi sesi aktif untuk `Mega Kusuma`

### TC-AUTH-OTP-43: Paste 6 digit di kotak 1 mengisi semua kotak dan memicu verifikasi otomatis

27. Logout dari Portal — Product Hub dan buka halaman `Auth > Login with OTP > Request OTP`
28. Ketik `suryasaputra+{runId}-013@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
29. Salin kode OTP dari email (mail-catcher `suryasaputra+{runId}-013@qwertysystem.net`) ke clipboard
30. Klik kotak 1 dan tekan Ctrl+V
31. Verifikasi 6 kotak terisi sesuai urutan digit pada clipboard
32. Verifikasi verifikasi otomatis terpicu satu kali tanpa tombol tambahan
33. Verifikasi browser dialihkan ke Portal — Product Hub
34. Verifikasi sesi aktif untuk `Surya Saputra`
35. Logout dari Portal — Product Hub

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC menyimpang dari TC sumber: TC-AUTH-OTP-44 dan TC-AUTH-OTP-45 (paste kode yang pasti ditolak, tidak membuat sesi) dijalankan lebih dulu, lalu TC-AUTH-OTP-42 dan TC-AUTH-OTP-43 (login sukses, membuat sesi) di akhir (prinsip 3: aksi yang membuat sesi di belakang validasi).
- Langkah 8, 16, dan 27 adalah langkah penghubung antar-TC (S-03): buka ulang halaman Request OTP dan, pada langkah 27, logout dari sesi hasil TC-AUTH-OTP-42 supaya konteks bersih (S-09). Langkah 35 adalah langkah penghubung penutup: logout dari sesi hasil TC-AUTH-OTP-43 (S-09), dengan hook `after` sebagai cadangan.
- Langkah 2, 9, 17, dan 28 menggabungkan ketik email, centang reCAPTCHA, dan klik [Request OTP] menjadi satu baris karena persis sama dengan prasyarat TC.
- Temuan untuk QA: (1) TC-AUTH-OTP-44 dan TC-AUTH-OTP-45 menyatakan verifikasi otomatis terpicu dengan kode `481902` dan `123456` tetapi tidak menyebut hasil penolakan atau state layar sesudahnya (caption "Invalid code", kotak dikosongkan); spec hanya mengasersi yang tertulis. (2) Kedua TC itu mengasumsikan kode paste tidak sama dengan kode yang diterbitkan; TC tidak menyebut cara menjamin itu. (3) TC-AUTH-OTP-42 butir b menyebut "indikator loading subtle" tanpa definisi visual yang dapat diasersi; spec menulisnya apa adanya. (4) TC-AUTH-OTP-43 butir b "terpicu satu kali" dan TC-AUTH-OTP-44/45 butir "satu kali" memerlukan pengamatan permintaan jaringan yang tidak disebut di TC.
