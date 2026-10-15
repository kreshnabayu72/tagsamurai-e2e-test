---
id: TC-AUTH-OTP-E2E-010-request-otp-sukses-loading-klik-ganda
title: "Request OTP Berhasil, Indikator Loading, dan Klik Ganda pada Button Request OTP"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-28
  - TC-AUTH-OTP-29
  - TC-AUTH-OTP-30
coverage:
  web: automated
---

# Request OTP Berhasil, Indikator Loading, dan Klik Ganda pada Button Request OTP

## Prerequisites

- Mode: FE+BE.
- Tidak ada akun aktor. Browser tanpa sesi login (halaman Login with OTP adalah halaman publik); tidak ada akun admin karena asersi absence log dipindah ke spec 040 dan 047 (lihat Notes).
- Environment variable: `OTP_PASSWORD` (password user uji yang dipasang saat seeding; tidak ada password atau token di spec atau fixture). Nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-010`, profil BASE (Activated, Active ON, sudah login sukses di web pada device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru ada; Agreement dan MFA tidak terpicu), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-28: `Yoga Simanjuntak` (`yogasimanjuntak+{runId}-010@qwertysystem.net`)
  - TC-AUTH-OTP-29: `Sari Mulyadi` (`sarimulyadi+{runId}-010@qwertysystem.net`)
  - TC-AUTH-OTP-30: `Eko Setiawan` (`ekosetiawan+{runId}-010@qwertysystem.net`)
- Kemampuan teknis: mail-catcher lingkungan uji yang dapat dibaca per alamat (kode OTP dan jumlah email yang masuk); reCAPTCHA mode uji di environment (centang tanpa tantangan); `Spectra.intercept()` untuk menahan respons Request OTP 5 detik (TC-AUTH-OTP-29), dilepas kembali di langkah spec dan dipulihkan di hook `after` bila spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-28: Request OTP dengan email terdaftar dan aktif berhasil

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser tanpa sesi
2. Ketik `yogasimanjuntak+{runId}-010@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Verifikasi toast sukses "Success, the code has been sent." tampil
6. Verifikasi toast tampil di kanan bawah layar
7. Verifikasi browser berpindah otomatis ke halaman `Auth > Login with OTP > Verify OTP`
8. Verifikasi Subtitle "Enter the 6-digit code sent to: yogasimanjuntak+{runId}-010@qwertysystem.net"
9. Buka mail-catcher untuk `yogasimanjuntak+{runId}-010@qwertysystem.net`
10. Verifikasi email OTP berisi kode 6 digit numerik diterima di `yogasimanjuntak+{runId}-010@qwertysystem.net`

### TC-AUTH-OTP-29: Button Request OTP nonaktif dengan indikator loading selama permintaan berjalan

11. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
12. Ketik `sarimulyadi+{runId}-010@qwertysystem.net` pada field Email
13. Centang widget reCAPTCHA "I'm not a robot"
14. Tahan respons Request OTP selama 5 detik (delay network)
15. Klik button [Request OTP]
16. Amati button [Request OTP] selama 5 detik
17. Verifikasi button [Request OTP] nonaktif
18. Verifikasi button [Request OTP] menampilkan indikator loading
19. Lepaskan respons yang ditahan
20. Verifikasi setelah respons diterima, halaman Verify OTP tampil

### TC-AUTH-OTP-30: Klik ganda cepat pada button Request OTP hanya menerbitkan satu kode

21. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
22. Ketik `ekosetiawan+{runId}-010@qwertysystem.net` pada field Email
23. Centang widget reCAPTCHA "I'm not a robot"
24. Klik button [Request OTP] dua kali berturut-turut dalam waktu kurang dari 1 detik
25. Buka mail-catcher untuk `ekosetiawan+{runId}-010@qwertysystem.net`
26. Verifikasi hanya satu email OTP diterima, bukan dua
27. Verifikasi halaman Verify OTP tampil satu kali (tidak ada halaman Verify OTP kedua atau transisi ganda)

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Asersi absence TC-AUTH-OTP-28 butir d ("tidak ada entri log baru" di `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`) dipindah ke spec 040 (kelas g, S-05), sedangkan TC-AUTH-OTP-30 butir c ("tidak ada entri log ganda") dipindah ke spec 047; spec ini hanya memuat asersi fungsional. Pembagian TC dicatat juga di Notes spec 040 dan 047.
- Langkah 11 dan 21 (buka ulang halaman Request OTP) adalah langkah penghubung antar-TC (S-03); tiap TC memakai user sendiri sehingga sesi email-request tidak saling terpengaruh.
- Temuan untuk QA: (1) TC-AUTH-OTP-28 Post Condition a (kode berlaku 5 menit dan sekali pakai) dan b (tombol Resend State A disabled) tidak punya langkah observasi di TC; spec tidak mengasersikannya (S-01). Post Condition a dicakup spec 026 dan 043 lewat TC lain. Mohon QA menambah Expected padanan untuk b bila cakupan itu diinginkan. (2) TC-AUTH-OTP-30 Expected b "Halaman Verify OTP tampil satu kali" tidak menyebut cara mengamati "satu kali"; spec memverifikasi tidak ada transisi atau halaman Verify OTP ganda. (3) TC-AUTH-OTP-29 tidak menyebut apakah field Email dan widget reCAPTCHA ikut nonaktif selama loading; hanya button yang diasersi.
