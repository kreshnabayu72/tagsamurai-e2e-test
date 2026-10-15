---
id: TC-AUTH-OTP-E2E-019-verify-setelah-perubahan-akun-oleh-admin
title: "Verify OTP Setelah Akun Diubah di Global Settings: Belum Aktivasi, Email Diganti, Dihapus, dan Dinonaktifkan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-61
  - TC-AUTH-OTP-62
  - TC-AUTH-OTP-141
  - TC-AUTH-OTP-184
coverage:
  web: automated
---

# Verify OTP Setelah Akun Diubah di Global Settings: Belum Aktivasi, Email Diganti, Dihapus, dan Dinonaktifkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`.
- Environment variable: `GS_TC_PASSWORD` (akun aktor), `OTP_PASSWORD` (password user uji yang dipasang saat seeding). Tidak ada password atau token di spec atau fixture. Nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-019`, profil BASE (Activated, Active ON, sudah login sukses di web pada device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru ada; Agreement dan MFA tidak terpicu), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian atau user sudah dihapus oleh spec):
  - TC-AUTH-OTP-184: `Rudi Hartono` (`rudihartono+{runId}-019@qwertysystem.net`)
  - TC-AUTH-OTP-141: `Maya Simanjuntak` (`mayasimanjuntak+{runId}-019@qwertysystem.net`); email baru untuk perubahan oleh admin: `mayasimanjuntak.baru+{runId}-019@qwertysystem.net` (nilai ditetapkan spec; TC tidak menyebutnya)
  - TC-AUTH-OTP-62: `Maya Purnama` (`mayapurnama+{runId}-019@qwertysystem.net`)
  - TC-AUTH-OTP-61: `Hendra Prasetyo` (`hendraprasetyo+{runId}-019@qwertysystem.net`)
- Kemampuan teknis: dua konteks browser (browser admin dan jendela privat publik); mail-catcher lingkungan uji untuk membaca kode OTP serta email konfirmasi perubahan email di alamat baru (TC-AUTH-OTP-141); reCAPTCHA mode uji di environment (centang tanpa tantangan); fixture BE yang dapat mengembalikan status user ke Pending Activation setelah kode OTP diterbitkan tanpa meng-invalidasi kode (TC-AUTH-OTP-184, sesuai precondition TC).
- Hook `before` membuka browser admin dan login sebagai akun aktor Total Control (Global Settings); langkah uji hanya berpindah konteks ke browser itu.
- State yang berubah: TC-AUTH-OTP-141 mengubah email user, TC-AUTH-OTP-62 menghapus user, TC-AUTH-OTP-61 menonaktifkan lalu mengaktifkan kembali user, dan TC-AUTH-OTP-184 mengubah status user; semuanya hanya pada user milik spec ini. TC-AUTH-OTP-61 diakhiri login sukses (sesi web aktif untuk `Hendra Prasetyo`) yang ditutup di hook `after`.

## Test Steps

### TC-AUTH-OTP-184: Verify OTP untuk akun yang belum aktivasi ditolak dan dicatat Account is not activated

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `rudihartono+{runId}-019@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
3. Kembalikan status user `Rudi Hartono` ke Pending Activation lewat fixture BE tanpa meng-invalidasi kode yang sudah diterbitkan
4. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session`, lalu catat jumlah entri serta entri terbaru user `Rudi Hartono` sebagai baseline
5. Ganti konteks ke jendela privat dan ketik 6 digit kode OTP dari email (mail-catcher `rudihartono+{runId}-019@qwertysystem.net`) pada kotak digit
6. Verifikasi verifikasi ditolak tanpa membuat sesi
7. Verifikasi caption error di bawah kotak digit: "Your account has not been activated"
8. Verifikasi kotak digit dikosongkan
9. Verifikasi kursor kembali ke kotak 1
10. Ganti konteks ke browser admin
11. Muat ulang `Global Settings > Activity Log > Session` dan bandingkan dengan baseline langkah 4 untuk user `Rudi Hartono`
12. Verifikasi dibanding baseline langkah 4, tepat 1 entri baru dengan Activity "Login", Status "Failed", Note "Account is not activated"

### TC-AUTH-OTP-141: Admin mengubah email user saat ada kode OTP aktif lalu kode lama dipakai

13. Ganti konteks ke jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
14. Ketik `mayasimanjuntak+{runId}-019@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
15. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Maya Simanjuntak`, lalu catat jumlah entri serta entri terbaru user `Maya Simanjuntak` di keduanya sebagai baseline
16. Di browser admin, buka `Global Settings > User`, ubah email `Maya Simanjuntak` menjadi `mayasimanjuntak.baru+{runId}-019@qwertysystem.net`, dan selesaikan konfirmasi perubahan email
17. Ganti konteks ke jendela privat dan ketik 6 digit kode OTP yang diterbitkan sebelum email diubah (mail-catcher `mayasimanjuntak+{runId}-019@qwertysystem.net`) pada kotak digit
18. Verifikasi kode ditolak tanpa membuat sesi
19. Verifikasi caption error di bawah kotak digit: "Invalid code"
20. Ganti konteks ke browser admin, muat ulang `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Maya Simanjuntak`, lalu bandingkan dengan baseline langkah 15
21. Verifikasi dibanding baseline langkah 15, tepat 1 entri baru dicatat Failed `OTP invalid — email changed` pada user `Maya Simanjuntak` (user yang sama setelah email diubah)

### TC-AUTH-OTP-62: Verify OTP setelah akun dihapus di Global Settings

22. Ganti konteks ke jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
23. Ketik `mayapurnama+{runId}-019@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
24. Ganti konteks ke browser admin, buka `Global Settings > User`, dan hapus user `Maya Purnama`
25. Ganti konteks ke jendela privat dan ketik 6 digit kode OTP dari email (mail-catcher `mayapurnama+{runId}-019@qwertysystem.net`) pada kotak digit
26. Verifikasi verifikasi ditolak tanpa membuat sesi
27. Verifikasi caption error di bawah kotak digit: "Email is not registered yet"
28. Verifikasi kotak digit dikosongkan
29. Verifikasi kursor kembali ke kotak 1

### TC-AUTH-OTP-61: Verify OTP setelah akun dinonaktifkan di Global Settings

30. Ganti konteks ke jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
31. Ketik `hendraprasetyo+{runId}-019@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
32. Ganti konteks ke browser admin, buka `Global Settings > User`, dan matikan Toggle Active untuk `Hendra Prasetyo`
33. Ganti konteks ke jendela privat dan ketik 6 digit kode OTP dari email (mail-catcher `hendraprasetyo+{runId}-019@qwertysystem.net`) pada kotak digit
34. Verifikasi verifikasi ditolak tanpa membuat sesi
35. Verifikasi caption error di bawah kotak digit: "Your account is inactive"
36. Verifikasi kotak digit dikosongkan
37. Verifikasi kursor kembali ke kotak 1
38. Ganti konteks ke browser admin dan nyalakan kembali Toggle Active untuk `Hendra Prasetyo`
39. Ganti konteks ke jendela privat dan ketik ulang kode OTP yang sama pada kotak digit
40. Verifikasi verifikasi berhasil
41. Verifikasi browser dialihkan ke Portal — Product Hub
42. Verifikasi sesi aktif untuk `Hendra Prasetyo`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC menyimpang dari TC sumber (61, 62, 141, 184): TC yang berakhir penolakan (184, 141, 62) lebih dulu, dan TC-AUTH-OTP-61 terakhir karena diakhiri login sukses (prinsip 3).
- Asersi absence log TC-AUTH-OTP-62 (Post Condition a, yang diamati TC pada langkah 7: "tidak ada entri log untuk percobaan ini karena tidak ada subjek user"; Expected TC hanya butir a dan b) dipindah ke spec 047 (prinsip 13g, S-05; skenario serupa TC-AUTH-OTP-133 ada di spec 040); spec ini hanya memuat asersi fungsional. Pembagian TC dicatat juga di Notes spec 047.
- Pencatatan `OTP invalid — email changed` yang termuat di Expected TC-AUTH-OTP-141 butir c tetap diasersi di sini (langkah 21) karena merupakan Expected TC ini, dan diuji ulang pada spec 038 (TC-AUTH-OTP-125, kode dari email sebelumnya via Edit email).
- Baseline TC-AUTH-OTP-184 dicatat setelah Request OTP dan fixture BE (langkah 4), mengikuti Pre-condition TC bahwa kode OTP valid sudah diterbitkan dan status user sudah dikembalikan ke Pending Activation sebelum langkah 1 TC; Request OTP tidak menambah entri yang dibandingkan.
- Baseline TC-AUTH-OTP-141 dicatat di browser admin setelah Request OTP dan sebelum email diubah (langkah 15), lalu dibandingkan pada langkah 20 dan 21 (S-12).
- Langkah ganti konteks (4, 5, 10, 13, 15, 17, 20, 22, 24, 25, 30, 32, 33, 38, 39) adalah langkah penghubung eksplisit antara browser admin dan jendela privat (S-03, S-07).
- Browser admin sebagai konteks kedua memenuhi pengecualian P-2 (`docs/e2e-conventions.md` §3): konteks itu hanya pemicu perubahan state akun (ubah email, hapus, nonaktifkan, status Pending Activation) dan tempat membaca Activity Log dan User Log, bukan objek asersi perilaku multi-konteks. Perilaku halaman publik saat admin bertindak diasersi di jendela privat.
- Temuan untuk QA: (1) TC-AUTH-OTP-184 langkah 2 "Buka halaman Verify OTP untuk `rudihartono@...` dengan kode yang sudah diterbitkan" ambigu: alamat langsung Verify OTP dialihkan ke Request OTP (TC-AUTH-OTP-73), sehingga halaman Verify hanya dicapai lewat Request OTP; spec memakai Request OTP lalu mengembalikan status user ke Pending Activation lewat fixture BE (precondition TC), dan mekanisme fixture tidak dijelaskan di TC. (2) TC-AUTH-OTP-141 tidak menyebut email baru yang dipakai admin dan cara menyelesaikan konfirmasi perubahan email (hanya "selesaikan konfirmasi perubahan email"); spec menetapkan `mayasimanjuntak.baru+{runId}-019@qwertysystem.net` dan mengandalkan mail-catcher. (3) TC-AUTH-OTP-141 Expected c memakai "user yang sama setelah email diubah" tanpa menyebut kolom pencarian log (email lama atau baru); spec mencari lewat Detail user `Maya Simanjuntak`. (4) TC-AUTH-OTP-61 menyebut "ketik ulang kode OTP yang sama" setelah penolakan; TC tidak menyebut apakah kode masih dalam masa berlaku 5 menit bila toggle dikembalikan lambat (diasumsikan ya). (5) Post Condition TC-AUTH-OTP-61 a (Failed `Account is inactive`, detail pada TC Logging) tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini; pencatatan itu diuji di spec pencatatan (TC-AUTH-OTP-124). (6) Post Condition TC-AUTH-OTP-184 ("Kode OTP tidak di-consume") tidak punya langkah observasi di TC dan tidak dapat diasersi dari UI, sehingga tidak diasersi.
