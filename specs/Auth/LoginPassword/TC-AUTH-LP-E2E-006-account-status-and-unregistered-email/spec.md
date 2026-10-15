---
id: TC-AUTH-LP-E2E-006-account-status-and-unregistered-email
title: "Penolakan Email Belum Terdaftar dan Pembedaan Pesan Kredensial Salah"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-28
  - TC-AUTH-LP-37
  - TC-AUTH-LP-103
coverage:
  web: automated
---

# Penolakan Email Belum Terdaftar dan Pembedaan Pesan Kredensial Salah

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-006` (contoh `jokosusilo+{runId}-006@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama. Email `tidakada@qwertysystem.net` sengaja tidak pernah didaftarkan dan tetap literal.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: reCAPTCHA mode uji di environment.
- TC-AUTH-LP-28: Tanpa login (guest); browser web; Email `tidakada@qwertysystem.net` belum terdaftar
- TC-AUTH-LP-28 data: Email: `tidakada@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-37: Tanpa login (guest); browser web; Email `tidakada@qwertysystem.net` belum terdaftar
- TC-AUTH-LP-37: User `Joko Susilo` (`jokosusilo+{runId}-006@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 (di-seed lewat API di hook `before`)
- TC-AUTH-LP-37 data: Email 1: `tidakada@qwertysystem.net` dengan password `Spectra.env.LP_PASSWORD`; Email 2: `jokosusilo+{runId}-006@qwertysystem.net` dengan password `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-103: Tanpa login (guest); browser web; User `Joko Susilo` (`jokosusilo+{runId}-006@qwertysystem.net`, sama seperti TC-AUTH-LP-37) berstatus Activated dan Active; hitungan gagal sesudah TC-AUTH-LP-37 adalah 1 sehingga satu kegagalan lagi tidak memicu lock
- TC-AUTH-LP-103 data: Email: `jokosusilo+{runId}-006@qwertysystem.net`; Password salah: nilai `Spectra.env.LP_PASSWORD_WRONG`; Password pada submit berikutnya: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-28: Login dengan Email yang belum terdaftar

1. Buka halaman Login with Password
2. Isi field Email dengan "tidakada@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
3. Selesaikan reCAPTCHA
4. Klik [Log in]
5. Verifikasi caption "Email is not registered yet" tampil di bawah field Email
6. Verifikasi field Email tetap berisi "tidakada@qwertysystem.net"
7. Verifikasi field Password dikosongkan
8. Verifikasi widget reCAPTCHA kembali Unsolved
9. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-37: Pesan Email belum terdaftar dan password salah dibedakan

10. Muat ulang halaman Login with Password
11. Isi field Email dengan "tidakada@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
12. Selesaikan reCAPTCHA
13. Klik [Log in]
14. Catat pesan yang tampil, lalu verifikasi caption "Email is not registered yet" tampil di bawah field Email
15. Muat ulang halaman Login with Password
16. Isi field Email dengan "jokosusilo+{runId}-006@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD_WRONG`
17. Selesaikan reCAPTCHA
18. Klik [Log in]
19. Catat pesan yang tampil, lalu verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
20. Verifikasi pesan pada langkah 14 dan pesan pada langkah 19 berbeda
21. Verifikasi pesan password salah pada langkah 19 tidak menyebut apakah email terdaftar

### TC-AUTH-LP-103: Alert pesan server saat submit berikutnya menghasilkan caption inline

22. Muat ulang halaman Login with Password
23. Isi field Email dengan "jokosusilo+{runId}-006@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD_WRONG`
24. Selesaikan reCAPTCHA
25. Klik [Log in]
26. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
27. Kosongkan field Email dan isi field Password dengan nilai `Spectra.env.LP_PASSWORD`
28. Selesaikan reCAPTCHA
29. Klik [Log in]
30. Verifikasi caption "Email must not be empty" tampil di bawah field Email
31. Verifikasi Alert Danger dari langkah 25 tidak tampil lagi

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penolakan karena kondisi data akun (Pending Activation dan Inactive: TC-AUTH-LP-31, 32, 33, 34, 35, 36) ada di spec `TC-AUTH-LP-E2E-049-account-status-pending-inactive` (prinsip 12). Spec ini memuat penolakan email tak terdaftar dan kredensial salah, yang tidak butuh data prasyarat khusus.
- Urutan: TC-AUTH-LP-28, 37, 103. Urutan ini sama dengan urutan TC sumber (28, 37, 103); TC-AUTH-LP-103 ditaruh paling akhir karena mengandalkan akun `Joko Susilo` yang sama dengan TC-AUTH-LP-37 (hitungan gagal tetap di bawah ambang lock).
- Langkah penghubung (S-03): "Muat ulang halaman Login with Password" sebelum tiap TC setelah yang pertama (S-09); tanpa `Verifikasi`.
- Asersi tambahan (S-03): langkah 26 (TC-AUTH-LP-103) memverifikasi Alert Danger dari submit pertama tampil, sebagai keadaan yang diperlukan agar asersi "Alert tidak tampil lagi" pada langkah 31 bermakna (S-14); Expected TC hanya memuat asersi langkah 30 dan 31.
- Temuan untuk QA: kolom Data Uji TC-AUTH-LP-103 hanya memuat Password salah, sedangkan langkah 3 memakai password benar dan Email dikosongkan.
