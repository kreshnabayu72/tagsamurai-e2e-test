---
id: TC-AUTH-RST-E2E-037-resilience-backend-provider-failure
title: "Ketahanan terhadap Kegagalan Sisi Server dan Penyedia: reCAPTCHA, Log, Email, dan Rollback Submit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-21
  - TC-AUTH-RST-103
  - TC-AUTH-RST-144
  - TC-AUTH-RST-92
coverage:
  web: automated
---

# Ketahanan terhadap Kegagalan Sisi Server dan Penyedia: reCAPTCHA, Log, Email, dan Rollback Submit

## Prerequisites

- Mode: FE+BE (kelas b: failure injection di sisi server atau penyedia yang tidak dapat di-intercept di browser).
- Seeding: empat user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD`. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Kemampuan teknis: failure injection oleh tim BE: (a) layanan verifikasi reCAPTCHA tidak terjangkau dari server BE sementara widget di browser normal; (b) penulisan log dipaksa gagal; (c) enqueue atau pengiriman email dipaksa gagal setelah commit; (d) kegagalan setelah langkah penyimpanan password dan sebelum commit transaksi Submit. Fixture BE untuk lock permanen dan token aktif pada user TC-AUTH-RST-92. Pengaturan jam server dan jam browser bersama (cooldown ditegakkan di server, countdown [Resend email] berjalan di jam klien). Mail-catcher dengan pembacaan jumlah email per alamat; reCAPTCHA mode uji; jendela privat tanpa sesi login.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- State global yang diubah: injeksi kegagalan reCAPTCHA, penulisan log, email, dan transaksi di sisi server; jam server dan jam browser. Suite berjalan serial (`parallel: false`). Pemulihan: setiap injeksi dipulihkan dan kedua jam dipulihkan di hook `after` (tetap berjalan walau spec gagal di tengah).
- TC-AUTH-RST-21, 103, 144, 92: User belum login (guest); browser web.
- TC-AUTH-RST-21: User `Budi Santoso` (`budisantoso+{runId}-037a@qwertysystem.net`) Active.
- TC-AUTH-RST-103: User `Citra Dewi` (`citradewi+{runId}-037b@qwertysystem.net`) Active.
- TC-AUTH-RST-144: User `Dewi Lestari` (`dewilestari+{runId}-037c@qwertysystem.net`) Active; belum ada token reset aktif dan tidak dalam cooldown.
- TC-AUTH-RST-92: User `Yuni Astuti` (`yuniastuti+{runId}-037d@qwertysystem.net`) Active dengan lock permanen (fixture BE) dan token reset aktif; Password dan Confirm Password `Spectra.env.RST_PASSWORD_NEW`.

## Test Steps

### TC-AUTH-RST-21: Layanan reCAPTCHA tidak terjangkau saat Request

1. Aktifkan injeksi: layanan verifikasi reCAPTCHA tidak terjangkau dari server BE
2. Buka jendela privat baru lalu buka halaman Reset Password (Request)
3. Ketik `budisantoso+{runId}-037a@qwertysystem.net` pada field Email
4. Selesaikan reCAPTCHA (centang "I'm not a robot") lalu klik Button [Reset Password]
5. Verifikasi toast error muncul: "Error, failed to send reset link."
6. Verifikasi browser tetap di halaman Reset Password
7. Verifikasi input Email dipertahankan

### TC-AUTH-RST-103: Kegagalan penulisan log membatalkan aksi

8. Pulihkan injeksi sebelumnya lalu aktifkan injeksi: penulisan log dipaksa gagal
9. Buka halaman Reset Password (Request) di jendela privat baru
10. Catat jumlah email di mail-catcher untuk `citradewi+{runId}-037b@qwertysystem.net` sebagai baseline M1
11. Ketik `citradewi+{runId}-037b@qwertysystem.net` pada field Email, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
12. Verifikasi toast error muncul: "Error, failed to send reset link."
13. Verifikasi browser tetap di halaman Reset Password
14. Verifikasi input Email dipertahankan
15. Periksa mail-catcher
16. Verifikasi tidak ada email terkirim di mail-catcher: jumlah email untuk `citradewi+{runId}-037b@qwertysystem.net` sama dengan baseline M1

### TC-AUTH-RST-144: Kegagalan enqueue email setelah token tersimpan tidak terlihat user

17. Pulihkan injeksi sebelumnya lalu aktifkan injeksi: enqueue atau pengiriman email dipaksa gagal setelah commit
18. Buka halaman Reset Password (Request) di jendela privat baru
19. Ketik `dewilestari+{runId}-037c@qwertysystem.net` pada field Email, selesaikan reCAPTCHA, lalu klik Button [Reset Password]
20. Verifikasi halaman Email Sent! tampil, sama seperti Request yang emailnya terkirim
21. Verifikasi tidak ada toast pada halaman Email Sent!
22. Majukan jam server dan jam browser 61 detik sampai Button [Resend email] tampil
23. Klik [Resend email]
24. Verifikasi toast sukses muncul "Success, email has been sent to dewilestari+{runId}-037c@qwertysystem.net."
25. Verifikasi tidak ada toast error

### TC-AUTH-RST-92: Kegagalan di tengah transaksi Submit tidak meninggalkan perubahan sebagian

26. Pulihkan injeksi sebelumnya lalu aktifkan injeksi: kegagalan setelah langkah penyimpanan password dan sebelum commit transaksi Submit
27. Buka tautan reset milik `yuniastuti+{runId}-037d@qwertysystem.net` dari mail-catcher sehingga Setup New Password tampil
28. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password lalu klik Button [Reset Password]
29. Verifikasi toast error "Error, failed to reset password." tampil
30. Verifikasi form tetap terbuka
31. Pulihkan layanan lalu buka halaman Login with Password
32. Login dengan Email `yuniastuti+{runId}-037d@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD` (password lama, selesaikan reCAPTCHA)
33. Verifikasi akun masih terkunci permanen: Alert "For security reasons, your account has been locked. Please reset your password to regain access." (password lama masih berlaku dan lock belum dibersihkan)

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md` (semua Manual Only karena membutuhkan failure injection BE; kebutuhan ditulis di Prerequisites). Kegagalan sisi server atau penyedia tidak dapat di-intercept di browser (konvensi bagian 6).
- Pemulihan injeksi antar-TC adalah langkah penghubung (S-09, S-03). Langkah 22 memajukan jam menggantikan menunggu 61 detik (konvensi bagian 6).
- Temuan untuk QA: Post Condition tanpa langkah observasi di TC tidak diasersi lewat UI: tidak ada token baru, tidak ada entri log, dan counter tidak bertambah (TC-AUTH-RST-21, 103), token reset aktif digantikan token baru (TC-AUTH-RST-144), password tidak berubah, token tetap active, lock progression tidak berubah, dan tidak ada entri log Success (TC-AUTH-RST-92) (S-01, S-15).
- Temuan untuk QA: pada TC-AUTH-RST-92 teks Alert lock permanen diambil dari TC-AUTH-RST-110 karena TC-AUTH-RST-92 hanya menulis "akun masih terkunci permanen" (S-15).
- Urutan TC dalam spec (21, 103, 144, 92) berbeda dari urutan di TC sumber; TC-AUTH-RST-92 dipindah ke akhir karena memerlukan injeksi transaksi yang paling berat dan pemulihan layanan sebelum login ulang (S-05).
