---
id: TC-AUTH-OTP-E2E-017-edit-email-dan-kode-email-lama
title: "Edit Email dari Layar Verify OTP dan Penolakan Kode dari Request OTP Sebelumnya"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-54
  - TC-AUTH-OTP-64
  - TC-AUTH-OTP-86
  - TC-AUTH-OTP-88
  - TC-AUTH-OTP-89
coverage:
  web: automated
---

# Edit Email dari Layar Verify OTP dan Penolakan Kode dari Request OTP Sebelumnya

## Prerequisites

- Mode: FE+BE.
- Tidak ada akun aktor. Browser tanpa sesi login (halaman Login with OTP adalah halaman publik); tidak ada akun admin karena asersi absence log dipindah ke spec 040 dan 047 (lihat Notes).
- Environment variable: `OTP_PASSWORD` (password user uji yang dipasang saat seeding; tidak ada password atau token di spec atau fixture). Nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-017`, profil BASE (Activated, Active ON, sudah login sukses di web pada device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru ada; Agreement dan MFA tidak terpicu), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-86: `Surya Utami` (`suryautami+{runId}-017@qwertysystem.net`)
  - TC-AUTH-OTP-89: `Irfan Rahmawati` (`irfanrahmawati+{runId}-017@qwertysystem.net`)
  - TC-AUTH-OTP-88: `Teguh Hakim` (`teguhhakim+{runId}-017@qwertysystem.net`) dan `Laras Tanjung` (`larastanjung+{runId}-017@qwertysystem.net`)
  - TC-AUTH-OTP-54: `Siti Saputra` (`sitisaputra+{runId}-017@qwertysystem.net`)
  - TC-AUTH-OTP-64: `Putri Santoso` (`putrisantoso+{runId}-017@qwertysystem.net`) dan `Dimas Lestari` (`dimaslestari+{runId}-017@qwertysystem.net`)
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP 6 digit dan memeriksa ada tidaknya email baru per alamat; reCAPTCHA mode uji di environment (centang tanpa tantangan).
- State yang berubah: tidak ada TC yang membuat sesi login; kode yang diketik pada Verify OTP selalu ditolak.

## Test Steps

### TC-AUTH-OTP-86: Klik Edit email membuka halaman Request OTP dengan email terisi dan dapat diubah

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser tanpa sesi
2. Ketik `suryautami+{runId}-017@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
3. Klik tautan [Edit email]
4. Verifikasi halaman Request OTP tampil dengan field Email berisi `suryautami+{runId}-017@qwertysystem.net`
5. Verifikasi field Email dapat diubah
6. Verifikasi widget reCAPTCHA belum dicentang
7. Verifikasi kotak digit OTP tidak tampil
8. Verifikasi area Resend tidak tampil
9. Verifikasi tautan [Edit email] tidak tampil

### TC-AUTH-OTP-89: Edit email lalu Request OTP dengan email kosong menampilkan validasi Request OTP biasa

10. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
11. Ketik `irfanrahmawati+{runId}-017@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
12. Klik tautan [Edit email]
13. Kosongkan field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
14. Verifikasi caption error di bawah field Email: "Email must not be empty"
15. Verifikasi halaman tetap di Request OTP
16. Buka mail-catcher untuk `irfanrahmawati+{runId}-017@qwertysystem.net` (alamat yang diketik pada langkah 11) dan hitung jumlah email OTP
17. Verifikasi mail-catcher `irfanrahmawati+{runId}-017@qwertysystem.net` hanya memuat 1 email OTP (dari langkah 11)

### TC-AUTH-OTP-54: Kode lama ditolak setelah Request OTP baru melalui Edit email dengan email yang sama

18. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
19. Ketik `sitisaputra+{runId}-017@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
20. Catat kode OTP pertama dari mail-catcher `sitisaputra+{runId}-017@qwertysystem.net`
21. Klik tautan [Edit email]
22. Biarkan email `sitisaputra+{runId}-017@qwertysystem.net` tidak berubah, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
23. Pada halaman Verify OTP ketik kode OTP pertama
24. Verifikasi kode pertama ditolak walau belum lewat 5 menit
25. Verifikasi caption error di bawah kotak digit: "Invalid code"
26. Verifikasi tidak ada sesi yang dibuat

### TC-AUTH-OTP-64: Kode dari email sebelumnya dimasukkan pada layar Verify OTP email baru

27. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
28. Ketik `putrisantoso+{runId}-017@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
29. Catat kode OTP dari mail-catcher `putrisantoso+{runId}-017@qwertysystem.net`
30. Klik tautan [Edit email]
31. Ubah email menjadi `dimaslestari+{runId}-017@qwertysystem.net`, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
32. Pada halaman Verify OTP untuk `dimaslestari+{runId}-017@qwertysystem.net` ketik kode OTP milik `putrisantoso+{runId}-017@qwertysystem.net`
33. Verifikasi kode ditolak: kotak digit menampilkan shake animation
34. Verifikasi kotak digit berborder severity danger
35. Verifikasi caption error di bawah kotak digit: "Invalid code"
36. Verifikasi tidak ada sesi yang dibuat untuk `Putri Santoso` maupun `Dimas Lestari`

### TC-AUTH-OTP-88: Edit email ke email terdaftar lain memulai sesi baru untuk email tersebut

37. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
38. Ketik `teguhhakim+{runId}-017@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
39. Klik tautan [Edit email]
40. Ubah email menjadi `larastanjung+{runId}-017@qwertysystem.net`, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
41. Verifikasi toast sukses "Success, the code has been sent." tampil
42. Verifikasi halaman Verify OTP tampil dengan Subtitle "Enter the 6-digit code sent to: larastanjung+{runId}-017@qwertysystem.net"
43. Verifikasi area Resend menampilkan "Resend code in (00:59)"
44. Verifikasi area Resend dalam keadaan disabled
45. Buka mail-catcher untuk `larastanjung+{runId}-017@qwertysystem.net`
46. Verifikasi email OTP diterima di `larastanjung+{runId}-017@qwertysystem.net`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC menyimpang dari TC sumber (54, 64, 86, 88, 89) mengikuti prinsip 3: TC yang hanya menampilkan layar (86), lalu validasi yang diblokir (89), lalu penolakan kode lama (54, 64), dan TC-AUTH-OTP-88 terakhir karena satu-satunya yang berujung sukses (Request OTP diterima untuk email lain). Tidak ada TC yang membuat sesi login; tiap TC memakai user dan sesi email-request sendiri sehingga urutan tidak menimbulkan ketergantungan state.
- Asersi absence log TC-AUTH-OTP-86 butir d dan TC-AUTH-OTP-89 butir c ("tidak ada entri log baru" di `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`) dipindah ke spec absence (prinsip 13g, S-05): TC-AUTH-OTP-86 ke spec 047 dan TC-AUTH-OTP-89 ke spec 040; spec ini hanya memuat asersi fungsional. Pembagian TC dicatat juga di Notes spec 047 dan 040.
- Langkah 10, 18, 27, dan 37 adalah langkah penghubung antar-TC (S-03): buka ulang halaman Request OTP agar tiap TC memakai user dan sesi email-request sendiri. Langkah 2, 11, 19, 28, dan 38 menggabungkan ketik email, centang reCAPTCHA, dan klik [Request OTP] menjadi satu baris karena persis sama dengan prasyarat TC.
- Langkah 16 dan 17 menghitung email di mail-catcher alamat yang diketik pada langkah 11 (TC-AUTH-OTP-89 langkah 8 menyebut alamat itu; field Email kosong pada langkah 13 sehingga tidak ada alamat lain yang diharapkan menerima email); pembacaan kode tidak diperlukan.
- Temuan untuk QA: (1) TC-AUTH-OTP-86 Expected c menyebut area Resend dan tautan [Edit email] "tidak tampil" tanpa menjelaskan status sesi email-request setelah Edit email (apakah kode pertama masih valid); tidak diasersi. (2) TC-AUTH-OTP-54 langkah 5 "Catat kode OTP pertama" dan langkah 8 tidak menyebut kode kedua; spec hanya memakai kode pertama untuk Verify. (3) TC-AUTH-OTP-64 Expected c "tidak ada sesi yang dibuat untuk `Putri Santoso` maupun `Dimas Lestari`" hanya dapat dibuktikan lewat halaman tetap di Verify OTP; spec mengasersi kalimat Expected itu apa adanya di langkah 36 tanpa langkah observasi tambahan. (4) TC-AUTH-OTP-88 Post Condition a ("Sesi email-request baru dimulai untuk `Laras Tanjung` dengan jumlah resend 0") tidak punya langkah observasi di TC; spec tidak mengasersinya (S-01), sedangkan Expected c (area Resend "Resend code in (00:59)", langkah 43) hanya padanannya. Mohon QA menambah langkah observasi bila jumlah resend 0 perlu dibuktikan.
