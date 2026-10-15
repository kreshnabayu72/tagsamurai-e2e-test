---
id: TC-AUTH-RST-E2E-022-account-status-vs-link-and-form
title: "Akun Inactive atau Dihapus saat Tautan Dibuka dan saat Form Setup Terbuka"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-60
  - TC-AUTH-RST-61
  - TC-AUTH-RST-132
coverage:
  web: automated
---

# Akun Inactive atau Dihapus saat Tautan Dibuka dan saat Form Setup Terbuka

## Prerequisites

- Mode: FE+BE.
- Seeding: tiga user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD` dan tanpa gate Agreement dan MFA (fixture BE); satu token reset aktif per user diterbitkan di hook `before` lewat API Request, tautan dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Kemampuan teknis: mail-catcher; reCAPTCHA mode uji; jendela guest dan jendela admin terpisah (admin menonaktifkan, mengaktifkan, atau menghapus user di Global Settings > User dan membaca Activity Log Session dan User Log; user diidentifikasi lewat email bersuffix).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-60, TC-AUTH-RST-61, TC-AUTH-RST-132: User belum login (guest); browser web.
- TC-AUTH-RST-60: User `Budi Santoso` (`budisantoso+{runId}-022a@qwertysystem.net`) dengan token aktif; dinonaktifkan admin setelah token terbit.
- TC-AUTH-RST-61: User `Citra Dewi` (`citradewi+{runId}-022b@qwertysystem.net`) dengan token aktif; dihapus admin setelah token terbit.
- TC-AUTH-RST-132: User `Dewi Lestari` (`dewilestari+{runId}-022c@qwertysystem.net`) dengan token aktif; Password dan Confirm Password: `Spectra.env.RST_PASSWORD_NEW`.

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login) dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password"

### TC-AUTH-RST-60: Tautan dibuka setelah akun menjadi Inactive

2. Pindah ke jendela admin, buka Global Settings > User lalu nonaktifkan user `budisantoso+{runId}-022a@qwertysystem.net`
3. Muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password" lalu catat jumlah entri sebagai baseline B1; buka User Log user `budisantoso+{runId}-022a@qwertysystem.net` (cari lewat email) lalu catat jumlah entri sebagai baseline B2
4. Pindah ke jendela guest lalu buka tautan reset milik `budisantoso+{runId}-022a@qwertysystem.net` dari mail-catcher
5. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
6. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
7. Verifikasi penyebab (akun nonaktif) tidak ditampilkan
8. Pindah ke jendela admin, muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password", dan muat ulang User Log user `budisantoso+{runId}-022a@qwertysystem.net`
9. Verifikasi Activity Log Session dan User Log masing-masing bertambah satu entri dibanding baseline B1 dan B2
10. Verifikasi entri baru dengan Note `Reset link expired` untuk user dengan email `budisantoso+{runId}-022a@qwertysystem.net` pada kedua surface: Status Failed (dicari berdasarkan Note dan email, bukan posisi teratas)
11. Aktifkan kembali user `budisantoso+{runId}-022a@qwertysystem.net` di Global Settings > User
12. Pindah ke jendela guest lalu buka tautan yang sama sekali lagi
13. Verifikasi Halaman 404 varian Expired tetap tampil (token sudah di-invalidate)

### TC-AUTH-RST-61: Tautan dibuka setelah akun dihapus

14. Pindah ke jendela admin, buka Global Settings > User lalu hapus user `citradewi+{runId}-022b@qwertysystem.net`
15. Muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password" lalu catat jumlah entri sebagai baseline B3
16. Pindah ke jendela guest lalu buka tautan reset milik `citradewi+{runId}-022b@qwertysystem.net` dari mail-catcher
17. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
18. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
19. Verifikasi penyebab (akun dihapus) tidak ditampilkan
20. Pindah ke jendela admin dan muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password"
21. Verifikasi Activity Log Session bertambah satu entri dibanding baseline B3
22. Verifikasi entri baru dengan Note `Reset link expired` untuk user dengan email `citradewi+{runId}-022b@qwertysystem.net` pada Activity Log Session: Status Failed (dicari berdasarkan Note dan email, bukan posisi teratas)

### TC-AUTH-RST-132: Akun menjadi Inactive setelah Setup New Password terbuka lalu submit

23. Pindah ke jendela guest lalu buka tautan reset milik `dewilestari+{runId}-022c@qwertysystem.net` dari mail-catcher sehingga Setup New Password tampil
24. Pindah ke jendela admin, buka Global Settings > User lalu nonaktifkan user `dewilestari+{runId}-022c@qwertysystem.net`
25. Muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password" lalu catat jumlah entri sebagai baseline B4; buka User Log user `dewilestari+{runId}-022c@qwertysystem.net` (cari lewat email) lalu catat jumlah entri sebagai baseline B5
26. Pindah ke jendela guest, ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password lalu klik Button [Reset Password]
27. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
28. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
29. Pindah ke jendela admin, muat ulang Activity Log Session lalu terapkan ulang Filter Activity = "Reset Password", dan muat ulang User Log user `dewilestari+{runId}-022c@qwertysystem.net`
30. Verifikasi Activity Log Session dan User Log masing-masing bertambah satu entri dibanding baseline B4 dan B5
31. Verifikasi entri baru dengan Note `Reset link expired` untuk user dengan email `dewilestari+{runId}-022c@qwertysystem.net` pada kedua surface: Status Failed (dicari berdasarkan Note dan email, bukan posisi teratas)
32. Aktifkan kembali user `dewilestari+{runId}-022c@qwertysystem.net` di Global Settings > User
33. Pindah ke jendela guest, buka halaman Login with Password lalu login dengan Email `dewilestari+{runId}-022c@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD` (selesaikan reCAPTCHA)
34. Verifikasi login berhasil dengan password lama (password user tetap tidak berubah)

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Langkah penghubung (S-03, S-07): langkah "pindah ke jendela ..." dan Persiapan konteks (langkah 1) adalah penghubung antar-konteks. Mengaktifkan kembali user (langkah 11 dan 32) adalah pemulihan state; pada TC-AUTH-RST-132 pengaktifan ditaruh sesudah verifikasi log supaya entri aktivasi tidak tercampur dalam hitungan User Log.
- Asersi log memakai selisih jumlah entri terhadap baseline dan pencarian entri berdasarkan Note dan email, bukan posisi teratas, karena spec lain dalam suite yang menggeser atau membekukan jam server meninggalkan entri bercap waktu di masa depan yang berada di atas entri baru di Activity Log Session (S-12).
- Login dengan password lama (langkah 33 dan 34) dipakai sebagai cara memverifikasi password tidak berubah; TC-AUTH-RST-132 butir b tidak menyebut caranya (S-03).
- Pencatatan TC-AUTH-RST-100 (Validate Link dan Submit pada akun Inactive atau Deleted) dicakup di spec `TC-AUTH-RST-E2E-042-log-token-states`.
- TC-AUTH-RST-61 butir b hanya diasersi pada Activity Log Session (langkah 20 sampai 22), sesuai Expected TC: User Log user yang sudah dihapus tidak diperiksa.
- Temuan untuk QA: Post Condition TC-AUTH-RST-60, TC-AUTH-RST-61, dan TC-AUTH-RST-132 ("Token berstatus invalidated") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
