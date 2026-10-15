---
id: TC-AUTH-RST-E2E-035-multi-tab
title: "Multi-Tab: Submit Ganda pada Token yang Sama dan Resend di Tab Lain"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-129
  - TC-AUTH-RST-130
coverage:
  web: automated
---

# Multi-Tab: Submit Ganda pada Token yang Sama dan Resend di Tab Lain

## Prerequisites

- Mode: FE+BE (kelas c: multi-tab).
- Seeding: dua user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD`, tanpa gate Agreement dan MFA (fixture BE). Untuk TC-AUTH-RST-129, satu token reset aktif diterbitkan di hook `before` lewat API Request, tautan dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`, `RST_PASSWORD_ALT2`.
- Kemampuan teknis: dua tab browser dalam satu konteks tanpa sesi login; mail-catcher; reCAPTCHA mode uji; jendela admin terpisah (admin membaca Activity Log Session dan User Log); pengaturan jam server dan jam browser bersama (cooldown ditegakkan di server, countdown [Resend email] berjalan di jam klien).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- State global yang diubah: jam server dan jam browser. Suite berjalan serial (`parallel: false`). Pemulihan: kedua jam dipulihkan di hook `after` (tetap berjalan walau spec gagal di tengah).
- TC-AUTH-RST-129, TC-AUTH-RST-130: User belum login (guest); browser web.
- TC-AUTH-RST-129: User `Budi Santoso` (`budisantoso+{runId}-035a@qwertysystem.net`) dengan token aktif; Password tab 1 `Spectra.env.RST_PASSWORD_NEW`; Password tab 2 `Spectra.env.RST_PASSWORD_ALT2`.
- TC-AUTH-RST-130: User `Citra Dewi` (`citradewi+{runId}-035b@qwertysystem.net`) Active tanpa percobaan reset dalam 24 jam; Password `Spectra.env.RST_PASSWORD_NEW`.

## Test Steps

### Persiapan konteks

1. Buka jendela privat admin; login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password"
2. Buka jendela privat guest (tanpa sesi login) dengan dua tab: tab 1 dan tab 2

### TC-AUTH-RST-129: Dua tab Setup New Password: submit kedua ditolak sebagai token already used

3. Buka tautan reset milik `budisantoso+{runId}-035a@qwertysystem.net` yang sama di tab 1 dan tab 2
4. Verifikasi kedua tab menampilkan Setup New Password
5. Pada tab 1, ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password lalu klik Button [Reset Password]
6. Verifikasi tab 1 menuju halaman Password Reset Successful
7. Pada tab 2, ketik `Spectra.env.RST_PASSWORD_ALT2` pada field Password dan field Confirm Password lalu klik Button [Reset Password]
8. Verifikasi tab 2 menampilkan Halaman 404 dengan Title "Reset Link Already Used"
9. Verifikasi tidak ada reset kedua
10. Buka halaman Login with Password lalu login dengan Email `budisantoso+{runId}-035a@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_ALT2` (selesaikan reCAPTCHA)
11. Verifikasi login dengan `Spectra.env.RST_PASSWORD_ALT2` ditolak
12. Login dengan Email `budisantoso+{runId}-035a@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_NEW`
13. Verifikasi login berhasil

### TC-AUTH-RST-130: Resend di tab lain saat Setup New Password terbuka: submit menghasilkan Halaman 404 Expired

14. Tutup jendela guest sebelumnya lalu buka jendela privat guest baru (tanpa sesi login) dengan dua tab: tab 1 dan tab 2
15. Pada tab 2, buka halaman Reset Password (Request), ketik `citradewi+{runId}-035b@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password] sampai halaman Email Sent! tampil
16. Pada tab 1, buka tautan reset dari email di mail-catcher
17. Verifikasi tab 1 menampilkan Setup New Password
18. Majukan jam server dan jam browser 61 detik
19. Pada tab 2, klik [Resend email]
20. Pulihkan jam server dan jam browser ke waktu nyata
21. Pindah ke jendela admin, muat ulang Activity Log Session, buka User Log user "Citra Dewi", terapkan Filter Activity = "Reset Password" pada kedua surface, lalu catat jumlah baris ber-Activity `Reset Password` dan entri teratas kedua surface sebagai baseline B1 (sudah memuat entri dari Request dan Resend)
22. Pindah ke jendela guest, pada tab 1 ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password lalu klik Button [Reset Password]
23. Verifikasi tab 1 menampilkan Halaman 404 dengan Title "Reset Link Expired"
24. Verifikasi tab 1 menampilkan Halaman 404 dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
25. Buka halaman Login with Password lalu login dengan Email `citradewi+{runId}-035b@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_NEW` (selesaikan reCAPTCHA)
26. Verifikasi login ditolak (password user tidak berubah menjadi `Spectra.env.RST_PASSWORD_NEW`)
27. Pindah ke jendela admin, muat ulang Activity Log Session dan User Log user "Citra Dewi", lalu terapkan Filter Activity = "Reset Password" pada kedua surface
28. Verifikasi jumlah baris ber-Activity `Reset Password` pada kedua surface bertambah tepat satu dibanding baseline B1
29. Verifikasi entri baru pada kedua surface: Status Failed, Note `Reset link expired`

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Temuan untuk QA: TC-AUTH-RST-129 menomori hasil "Setelah langkah 1/2/3" bergeser satu dari langkah sebenarnya (langkah 1 hanya membuka tab; hasil submit tab 1 seharusnya setelah langkah 2, hasil tab 2 setelah langkah 3, hasil login setelah langkah 4). Spec mengikuti urutan aksi sebenarnya (S-15).
- Temuan untuk QA: Post Condition TC-AUTH-RST-129 (token berstatus consumed) dan TC-AUTH-RST-130 (token lama invalidated, token baru active) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Entri log Failed `Reset link already used` untuk submit tab 2 (Post Condition TC-AUTH-RST-129) diasersi di spec `TC-AUTH-RST-E2E-042-log-token-states` (TC-AUTH-RST-135).
- Langkah penghubung (S-03): langkah 1 dan 2 (persiapan jendela), langkah 14 (jendela guest baru agar sesi login Budi dari langkah 12 tidak terbawa ke bagian TC-AUTH-RST-130, karena user bersesi aktif dialihkan ke Portal sesuai TC-AUTH-RST-10), langkah 18 (jam dimajukan menggantikan menunggu 61 detik, konvensi bagian 6), langkah 20 (jam dipulihkan sebelum admin membuka log, S-09), dan pindah antar jendela admin dan guest.
- Asersi tambahan di luar Expected TC (S-03): langkah 12 dan 13 (login `Spectra.env.RST_PASSWORD_NEW` berhasil) adalah Expected c TC-AUTH-RST-129; langkah 21 dan 27 sampai 29 memuat surface User Log di samping Activity Log Session karena TC-AUTH-RST-130 butir c tidak menyebut surface dan TC-AUTH-RST-136 (bergantung pada TC ini) menyebut kedua surface; baseline B1 ditambahkan agar entri "baru" terbukti (S-12). Baseline dan asersi jumlah pada langkah 21 dan 28 hanya menghitung entri ber-Activity `Reset Password` (Filter Activity pada kedua surface), sehingga entri percobaan login pada langkah 25 dan 26 tidak memengaruhi hitungan (S-12).
