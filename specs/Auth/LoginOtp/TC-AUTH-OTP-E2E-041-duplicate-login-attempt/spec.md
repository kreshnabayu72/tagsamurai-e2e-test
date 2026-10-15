---
id: TC-AUTH-OTP-E2E-041-duplicate-login-attempt
title: "Login with OTP saat Sesi Web Lain Aktif: Duplicate Login Attempt Dikonfirmasi atau Dibatalkan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-143
  - TC-AUTH-OTP-175
  - TC-AUTH-OTP-176
coverage:
  web: automated
---

# Login with OTP saat Sesi Web Lain Aktif: Duplicate Login Attempt Dikonfirmasi atau Dibatalkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`; dipakai membaca Activity Log Session (TC-AUTH-OTP-175 dan 176).
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API). Tidak ada password atau token di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: tiga konteks browser (browser admin, browser lain yang memegang sesi web lama milik user uji, dan jendela privat publik untuk login baru); mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji.
- Hook `before` (seeding API) membuat user profil BASE (Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada) dengan suffix per run `+{runId}-041`, lalu membuka sesi web aktif milik tiap user di browser lain (konteks "browser lain") dan menghapus user di hook `after` (tetap jalan walau seeding gagal sebagian). Jumlah baris awal Activity Log Session tiap user dicatat di hook:
  - TC-AUTH-OTP-143: `Putri Setiawan` (`putrisetiawan+{runId}-041@qwertysystem.net`)
  - TC-AUTH-OTP-175: `Kartika Wijaya` (`kartikawijaya+{runId}-041@qwertysystem.net`)
  - TC-AUTH-OTP-176: `Budi Handayani` (`budihandayani+{runId}-041@qwertysystem.net`)
- Isi dialog Duplicate Login Attempt dan perilaku sesi lama dimiliki fitur session-management; spec ini hanya mengasersi bahwa penanganan itu dijalankan, pilihan Confirm atau Cancel, dan pencatatan Login with OTP.

## Test Steps

### TC-AUTH-OTP-143: Login with OTP saat sesi web lain aktif diteruskan ke penanganan Duplicate Login Attempt

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `putrisetiawan+{runId}-041@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Ketik 6 digit kode OTP dari email pada kotak digit
6. Verifikasi sesi baru tidak langsung dibuat
7. Verifikasi penanganan Duplicate Login Attempt dijalankan (dialog Duplicate Login Attempt tampil; isi dialog di-assert pada TC session-management)
8. Ganti konteks ke browser lain (sesi web lama `Putri Setiawan`), muat ulang halaman Portal — Product Hub
9. Verifikasi sesi web lama tetap aktif: muat ulang Portal tidak mengalihkan ke halaman login

### TC-AUTH-OTP-175: Duplicate Login Attempt dikonfirmasi: sesi lama berakhir dan sesi baru dibuat dengan satu entri Success

10. Tutup jendela privat sebelumnya, buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
11. Ketik `kartikawijaya+{runId}-041@qwertysystem.net` pada field Email
12. Centang widget reCAPTCHA "I'm not a robot"
13. Klik button [Request OTP]
14. Ketik 6 digit kode OTP dari email pada kotak digit
15. Pada dialog Duplicate Login Attempt pilih Confirm
16. Verifikasi browser dialihkan ke Portal — Product Hub
17. Verifikasi sesi aktif untuk `Kartika Wijaya`
18. Ganti konteks ke browser lain (sesi web lama `Kartika Wijaya`), muat ulang halaman Portal — Product Hub
19. Verifikasi sesi web di browser lain berakhir (isi dialog dan perilaku sesi lama dimiliki session-management)
20. Ganti konteks ke browser admin Total Control (Global Settings), buka `Global Settings > Activity Log > Session` untuk `Kartika Wijaya`
21. Verifikasi tepat satu baris baru Activity `Login`, Status `Success`, Note `Login with OTP` untuk percobaan ini

### TC-AUTH-OTP-176: Duplicate Login Attempt dibatalkan: kembali ke halaman login tanpa sesi dan tanpa entri Success

22. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
23. Ketik `budihandayani+{runId}-041@qwertysystem.net` pada field Email
24. Centang widget reCAPTCHA "I'm not a robot"
25. Klik button [Request OTP]
26. Ketik 6 digit kode OTP dari email pada kotak digit
27. Pada dialog Duplicate Login Attempt pilih Cancel
28. Verifikasi browser kembali ke halaman login
29. Verifikasi tidak ada sesi baru untuk `Budi Handayani`
30. Ganti konteks ke browser lain (sesi web lama `Budi Handayani`), muat ulang halaman Portal — Product Hub
31. Verifikasi sesi web di browser lain tetap aktif
32. Ganti konteks ke browser admin Total Control (Global Settings), buka `Global Settings > Activity Log > Session` untuk `Budi Handayani`
33. Verifikasi tepat 0 baris Success `Login with OTP` baru untuk percobaan ini (jumlah baris `Budi Handayani` sama dengan baseline hook)

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Kelas harness c (multi-konteks: dua sesi web untuk user yang sama).
- Langkah penghubung (S-03): ganti konteks antara jendela privat, browser lain, dan browser admin, serta menutup jendela privat sebelum TC berikutnya, ditulis sebagai aksi tanpa `Verifikasi`. Sesi web lama tiap user dibuka di hook `before` (seeding), bukan lewat TC dependensi lain.
- Asersi "tepat 0 baris Success" pada TC-AUTH-OTP-176 adalah asersi state atas percobaan yang dibatalkan (konvensi bagian 3: asersi jumlah atau state bukan kelas g), bukan asersi absence untuk kondisi yang ditolak tanpa aksi: alurnya punya aksi Cancel dan memakai baseline jumlah baris dari hook (S-12). Karena itu tetap di spec ini dan bukan di E2E-047.
- Temuan untuk QA: (1) TC-AUTH-OTP-143 menyebut nama layar "Duplicate Login Attempt" tanpa teks dialog, tombol, dan judul; spec hanya mengasersi bahwa dialog tampil karena isinya dimiliki TC `session-management`. (2) TC-AUTH-OTP-175 dan 176 menyebut pilihan "Confirm" dan "Cancel" tanpa label tombol persis; spec memakai kedua kata itu apa adanya. (3) Precondition "sesi web aktif di browser lain" tidak menyebut cara membukanya; spec menyiapkannya lewat seeding sesi di hook.
