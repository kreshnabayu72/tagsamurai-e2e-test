---
id: TC-AUTH-RST-E2E-017-resend-success-old-link
title: "Resend Sukses Menerbitkan Token Baru dan Membatalkan Tautan Lama"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-42
  - TC-AUTH-RST-51
  - TC-AUTH-RST-43
  - TC-AUTH-RST-44
coverage:
  web: automated
---

# Resend Sukses Menerbitkan Token Baru dan Membatalkan Tautan Lama

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-017@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`, tanpa token dan tanpa percobaan reset. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher dengan pembacaan jumlah email per alamat (dua email berurutan dan tautan masing-masing, baseline jumlah email); reCAPTCHA mode uji; jendela privat tanpa sesi login; pengatur jam server uji dan jam browser/perangkat (digeser bersama 61 detik, karena countdown UI berjalan di jam klien); pembeku jam browser (dibekukan sebelum klik [Resend email] dan dilepas setelah asersi countdown dan hilangnya [Resend email], supaya nilai awal 1:00 tidak berkurang selama asersi toast).
- State global yang diubah: jam server uji dan jam browser/perangkat. Suite berjalan serial (`parallel: false`). Pemulihan: keduanya dikembalikan ke waktu nyata di hook `after` (tetap berjalan walau spec gagal di tengah). Tunggu nyata 4 detik pada langkah 13 (toast hilang otomatis); jam browser sudah dilepas dan tidak digeser pada langkah itu.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-42, TC-AUTH-RST-51, TC-AUTH-RST-43, TC-AUTH-RST-44: User belum login (guest); browser web.

## Test Steps

### TC-AUTH-RST-42 dan TC-AUTH-RST-51: Resend setelah cooldown menerbitkan token baru dan email baru; toast di kanan bawah

1. Buka jendela privat baru lalu buka halaman Reset Password (Request)
2. Ketik `budisantoso+{runId}-017@qwertysystem.net` pada field Email, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password] sampai halaman Email Sent! tampil (token A, tautan A di email 1)
3. Majukan jam server dan jam browser 61 detik sampai Button [Resend email] tampil
4. Periksa mail-catcher dan catat jumlah email untuk `budisantoso+{runId}-017@qwertysystem.net` sebagai baseline B1
5. Bekukan jam browser pada waktu saat ini
6. Klik [Resend email]
7. Verifikasi toast sukses muncul: "Success, email has been sent to budisantoso+{runId}-017@qwertysystem.net."
8. Verifikasi toast sukses tampil di kanan bawah layar (bottom-right)
9. Verifikasi teks countdown "Resend in [m:ss]" tampil kembali dari 1:00
10. Verifikasi [Resend email] hilang (cooldown dimulai ulang)
11. Verifikasi halaman tetap Email Sent! (tidak berpindah halaman)
12. Lepaskan pembekuan jam browser
13. Verifikasi toast hilang otomatis setelah 4 detik
14. Periksa mail-catcher
15. Verifikasi jumlah email bertambah satu dibanding baseline B1 (email 2, tautan B)

### TC-AUTH-RST-43: Tautan lama membuka Halaman 404 varian Expired setelah Resend

16. Buka tautan A dari email 1
17. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
18. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
19. Verifikasi Setup New Password tidak dirender

### TC-AUTH-RST-44: Tautan baru setelah Resend membuka Setup New Password

20. Buka tautan B dari email 2
21. Verifikasi Setup New Password tampil dengan Subtitle "Set a new password to log in for budisantoso+{runId}-017@qwertysystem.net."

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. TC-AUTH-RST-51 dan TC-AUTH-RST-42 memakai aksi yang sama (klik Resend); asersi posisi toast TC-AUTH-RST-51 (langkah 8) dilakukan pada toast yang sama dengan TC-AUTH-RST-42.
- Urutan: asersi posisi toast TC-AUTH-RST-51 dilakukan tepat sesudah toast muncul dan sebelum toast hilang otomatis; asersi countdown "dari 1:00" (langkah 9) dan hilangnya [Resend email] (langkah 10) dilakukan saat jam browser dibekukan (langkah 5 sampai 12) dan sebelum asersi toast hilang otomatis (langkah 13) supaya nilai awal countdown belum berkurang (S-14).
- TC-AUTH-RST-43 dan TC-AUTH-RST-44 di TC sumber bergantung pada TC-AUTH-RST-42; langkah Request dan Resend disalin utuh di sini (S-04).
- Langkah penghubung (S-03): membuka jendela privat baru (langkah 1) bukan asersi TC.
- Temuan untuk QA: Post Condition TC-AUTH-RST-42 butir a ("Token baru berstatus active; token sebelumnya berstatus invalidated") tidak punya langkah observasi di TC; padanannya hanya teramati lewat TC-AUTH-RST-43 dan TC-AUTH-RST-44. Post Condition butir b ("Tidak ada entri log baru") juga tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini maupun di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (S-01, S-05, S-15).
