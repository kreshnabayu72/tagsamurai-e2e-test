---
id: TC-AUTH-LP-E2E-004-password-validation
title: "Validasi Field Password: Kosong, Beda Huruf Besar-Kecil, Karakter Khusus, dan Spasi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-19
  - TC-AUTH-LP-20
  - TC-AUTH-LP-21
  - TC-AUTH-LP-22
  - TC-AUTH-LP-23
coverage:
  web: automated
---

# Validasi Field Password: Kosong, Beda Huruf Besar-Kecil, Karakter Khusus, dan Spasi

## Prerequisites

- Mode: FE+BE.
- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dengan status Activated dan Active, hitungan gagal 0. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-004` (contoh `jokosusilo+{runId}-004@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG_SPECIAL`, `LP_PASSWORD_SPACED`. Password akun tidak ditulis di spec atau fixture. `LP_PASSWORD_WRONG_SPECIAL` adalah password salah (bukan password milik akun mana pun) yang berisi karakter khusus `x'"<>&%$#@!`; nilainya diambil dari TC-AUTH-LP-23.
- Kemampuan teknis (fixture BE): password akun `Tika Wulandari` di-set langsung oleh tim BE ke nilai `Spectra.env.LP_PASSWORD_SPACED` (spasi di awal dan akhir), karena policy Set/Reset Password melarang spasi (`auth-foundation.md` §1) sehingga kondisi ini tidak dapat dibuat lewat UI; akun ini device terpercaya dan tanpa gate Agreement dan MFA (versi Privacy Policy yang disetujui sama dengan versi aktif, logout terakhir kurang dari 30 hari); reCAPTCHA mode uji di environment.
- Pemulihan: sesi login yang dibuat TC-AUTH-LP-21 ditutup lewat logout di akhir TC; hook `after` menutup sesi yang tersisa bila spec gagal di tengah.
- TC-AUTH-LP-19: Tanpa login (guest); browser web
- TC-AUTH-LP-19: User `Joko Susilo` (`jokosusilo+{runId}-004@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 (di-seed lewat API di hook `before`)
- TC-AUTH-LP-19 data: Email: `jokosusilo+{runId}-004@qwertysystem.net`; Password: (kosong)
- TC-AUTH-LP-20: Tanpa login (guest); browser web
- TC-AUTH-LP-20: User `Budi Santoso` (`budisantoso+{runId}-004@qwertysystem.net`) berstatus Activated dan Active dengan password `Spectra.env.LP_PASSWORD`, hitungan gagal 0 (di-seed lewat API di hook `before`)
- TC-AUTH-LP-20 data: Email: `budisantoso+{runId}-004@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD` diubah ke huruf kecil semua
- TC-AUTH-LP-23: Tanpa login (guest); browser web
- TC-AUTH-LP-23: User `Joko Susilo` (`jokosusilo+{runId}-004@qwertysystem.net`, sama seperti TC-AUTH-LP-19) berstatus Activated dan Active, hitungan gagal 0
- TC-AUTH-LP-23 data: Email: `jokosusilo+{runId}-004@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD_WRONG_SPECIAL`
- TC-AUTH-LP-22: Tanpa login (guest); browser web
- TC-AUTH-LP-22: User `Tika Wulandari` (`tikawulandari+{runId}-004@qwertysystem.net`) berstatus Activated dan Active dengan password `Spectra.env.LP_PASSWORD_SPACED` (di-seed lewat API di hook `before`, password di-set BE), hitungan gagal 0
- TC-AUTH-LP-22 data: Email: `tikawulandari+{runId}-004@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD_SPACED` tanpa spasi di awal dan akhir
- TC-AUTH-LP-21: Tanpa login (guest); browser web
- TC-AUTH-LP-21: User `Tika Wulandari` (`tikawulandari+{runId}-004@qwertysystem.net`, sama seperti TC-AUTH-LP-22); device terpercaya; tanpa gate Agreement dan MFA
- TC-AUTH-LP-21 data: Email: `tikawulandari+{runId}-004@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD_SPACED` (dengan spasi di awal dan akhir)

## Test Steps

### TC-AUTH-LP-19: Submit dengan Password kosong untuk Email terdaftar

1. Buka halaman Login with Password
2. Isi field Email dengan "jokosusilo+{runId}-004@qwertysystem.net"
3. Kosongkan field Password
4. Selesaikan reCAPTCHA
5. Klik [Log in]
6. Verifikasi caption "Password must not be empty" tampil di bawah field Password
7. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-20: Password dibedakan huruf besar dan kecil

8. Muat ulang halaman Login with Password
9. Isi field Email dengan "budisantoso+{runId}-004@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD` yang diubah ke huruf kecil semua
10. Selesaikan reCAPTCHA
11. Klik [Log in]
12. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
13. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-23: Password berisi karakter khusus yang salah diperlakukan sebagai kredensial salah biasa

14. Muat ulang halaman Login with Password
15. Isi field Email dengan "jokosusilo+{runId}-004@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD_WRONG_SPECIAL`
16. Selesaikan reCAPTCHA
17. Klik [Log in]
18. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
19. Verifikasi tidak ada pesan error teknis atau halaman error

### TC-AUTH-LP-22: Password tanpa spasi awal dan akhir ditolak untuk akun yang password-nya memakai spasi

20. Muat ulang halaman Login with Password
21. Isi field Email dengan "tikawulandari+{runId}-004@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD_SPACED` tanpa spasi di awal dan akhir
22. Selesaikan reCAPTCHA
23. Klik [Log in]
24. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
25. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-21: Password yang mengandung spasi di awal dan akhir diverifikasi apa adanya

26. Muat ulang halaman Login with Password
27. Isi field Email dengan "tikawulandari+{runId}-004@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD_SPACED` (dengan spasi di awal dan akhir)
28. Selesaikan reCAPTCHA
29. Klik [Log in]
30. Verifikasi login berhasil: browser menuju Portal — Product Hub
31. Logout dari Portal — Product Hub

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan dalam spec: submit yang diblokir (TC-AUTH-LP-19, 20, 23, 22) lebih dulu, login yang berhasil (TC-AUTH-LP-21) di akhir (prinsip 3 dan S-10), sehingga TC-AUTH-LP-22 berada di depan TC-AUTH-LP-21. TC-AUTH-LP-23 berada sebelum TC-AUTH-LP-22 karena submit diblokir didahulukan dari login berhasil. User berurutan: TC-AUTH-LP-19 (Joko Susilo), TC-AUTH-LP-20 (Budi Santoso), TC-AUTH-LP-23 (Joko Susilo), lalu TC-AUTH-LP-22 dan 21 (Tika Wulandari); urutan TC dipertahankan seperti ini sehingga Joko dipakai dua kali tidak berurutan.
- Langkah penghubung (S-03): "Muat ulang halaman Login with Password" sebelum tiap TC setelah yang pertama (S-09), dan logout di akhir TC-AUTH-LP-21; tanpa `Verifikasi`.
- TC-AUTH-LP-21 dan TC-AUTH-LP-22 berstatus Manual Only di TC sumber karena password berspasi tidak dapat dibuat lewat UI. Sesuai bagian 2 konvensi keduanya tetap masuk spec; kebutuhan fixture BE tertulis di Prerequisites sebagai sumber resmi bagi tim FE.
- Temuan untuk QA: tidak ada.
