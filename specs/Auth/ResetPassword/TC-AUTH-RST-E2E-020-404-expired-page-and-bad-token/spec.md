---
id: TC-AUTH-RST-E2E-020-404-expired-page-and-bad-token
title: "Halaman 404 Varian Expired, Request New Link, dan Token Tidak Dikenal atau Kosong"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-52
  - TC-AUTH-RST-53
  - TC-AUTH-RST-58
  - TC-AUTH-RST-59
coverage:
  web: automated
---

# Halaman 404 Varian Expired, Request New Link, dan Token Tidak Dikenal atau Kosong

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-020@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`. Di hook `before`, token A diterbitkan lewat API Request, lalu setelah jam server dimajukan 61 detik token B diterbitkan lewat API Resend (token A berstatus invalidated); tautan A dan B diambil dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: pengatur jam server uji (hanya di hook `before`, untuk melewati cooldown Resend lewat API); mail-catcher; jendela privat tanpa sesi login; menyunting URL di address bar (mengubah dua karakter terakhir token, membuang parameter token, mengosongkan parameter token).
- State global yang diubah: jam server uji (hanya di hook `before`). Suite berjalan serial (`parallel: false`). Pemulihan: jam server dikembalikan ke waktu nyata di hook `after` (tetap berjalan walau spec gagal di tengah).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-52, TC-AUTH-RST-53, TC-AUTH-RST-58, TC-AUTH-RST-59: User belum login (guest); browser web.

## Test Steps

### TC-AUTH-RST-52: Screening Halaman 404 varian Expired

1. Buka jendela privat baru lalu buka tautan token A
2. Susuri halaman dari atas ke bawah tanpa klik apa pun
3. Verifikasi **Header**: illustration link-broken
4. Verifikasi **Header**: Title "Reset Link Expired"
5. Verifikasi **Body**: Message "This password reset link has expired. Reset links are valid for 24 hours."
6. Verifikasi **Footer**: Button [Request New Link] tampil
7. Verifikasi **Footer**: Button [Request New Link] bergaya solid
8. Verifikasi **Footer**: Button [Request New Link] berseverity primary
9. Verifikasi **Footer**: Button [Request New Link] berlebar penuh
10. Verifikasi **Must NOT**: Button [Go to Login], penyebab teknis (ID token, status token, alasan invalidasi), dan form Setup New Password tidak tampil (anchor: Button [Request New Link] tampil)

### TC-AUTH-RST-53: Button Request New Link menuju halaman Reset Password

11. Klik Button [Request New Link]
12. Verifikasi browser menuju halaman Reset Password (Request)

### TC-AUTH-RST-58: Token tidak dikenal atau dimanipulasi

13. Buka tautan token B lalu ubah dua karakter terakhir token pada URL
14. Tekan Enter untuk membuka URL hasil ubahan
15. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
16. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
17. Verifikasi copy dan tombol sama dengan varian Expired
18. Verifikasi tidak ada penyebab teknis yang ditampilkan
19. Verifikasi varian "Reset Link Already Used" tidak tampil

### TC-AUTH-RST-59: URL Setup New Password tanpa parameter token

20. Buka alamat halaman Setup New Password tanpa parameter token pada URL
21. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
22. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
23. Verifikasi Setup New Password tidak dirender
24. Buka alamat halaman Setup New Password dengan parameter token kosong
25. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
26. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
27. Verifikasi Setup New Password tidak dirender

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- TC-AUTH-RST-52 dan 53 di TC sumber bergantung pada TC-AUTH-RST-42; langkah Request dan Resend disalin sebagai seeding API di hook `before` (S-04). TC-AUTH-RST-58 di TC sumber mulai dari tautan "reset dari email"; di sini dipakai tautan B (token aktif).
- Temuan untuk QA: bagian "tidak ada perubahan token" pada Post Condition TC-AUTH-RST-58 dan TC-AUTH-RST-59 tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Langkah penghubung (S-03): membuka jendela privat baru (langkah 1) dan menyunting URL (langkah 13, 14, 20, 24) bukan asersi TC.
