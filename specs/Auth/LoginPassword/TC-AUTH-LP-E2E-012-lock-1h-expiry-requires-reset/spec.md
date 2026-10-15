---
id: TC-AUTH-LP-E2E-012-lock-1h-expiry-requires-reset
title: "Lock 1 Jam Berakhir dan Status Requires Reset"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-48
  - TC-AUTH-LP-49
  - TC-AUTH-LP-50
  - TC-AUTH-LP-51
  - TC-AUTH-LP-52
coverage:
  web: automated
---

# Lock 1 Jam Berakhir dan Status Requires Reset

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) lalu diaktivasi. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`.
- Kemampuan teknis: geser jam server uji maju; fixture BE yang menaruh user pada status terkunci 1 jam di web setelah 6 kegagalan hari ini; reCAPTCHA mode uji; halaman Reset Password dapat dibuka dari tautan [Reset password]. Pemulihan: hook `after` mengembalikan jam server uji ke waktu nyata dan menghapus user.
- State global: suite berjalan serial (`parallel: false`) karena jam server uji diubah; hook `after` memulihkan jam server uji ke waktu nyata (tetap jalan walau spec gagal di tengah).
- TC-AUTH-LP-48: Tanpa login (guest, browser web)
- TC-AUTH-LP-48: User `Rina Putri` (`rinaputri+{runId}-012@qwertysystem.net`) berstatus Activated dan Active, terkunci 1 jam di web setelah 6 kegagalan hari ini, belum ada kegagalan sesudahnya (di-seed oleh fixture BE)
- TC-AUTH-LP-48 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-49: Tanpa login (guest); user yang sama sudah 7 kali salah password hari ini dan tidak sedang terkunci (hasil TC-AUTH-LP-48 dalam spec ini)
- TC-AUTH-LP-50: Tanpa login (guest); user yang sama sudah 8 kali salah password hari ini dan tidak sedang terkunci (hasil TC-AUTH-LP-49 dalam spec ini)
- TC-AUTH-LP-51: Tanpa login (guest); user yang sama berstatus Requires Reset di web (hasil TC-AUTH-LP-50 dalam spec ini) dengan password benar `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-52: Tanpa login (guest); user yang sama berstatus Requires Reset di web

## Test Steps

### TC-AUTH-LP-48: Password salah ke-7 setelah lock 1 jam berakhir tidak mengunci

1. Buka halaman Login with Password
2. Majukan jam server uji melebihi durasi lock 1 jam user `rinaputri+{runId}-012@qwertysystem.net`
3. Isi Email `rinaputri+{runId}-012@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
4. Selesaikan reCAPTCHA
5. Klik [Log in]
6. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
7. Verifikasi caption lock tidak tampil

### TC-AUTH-LP-49: Password salah ke-8 belum memicu Requires Reset

8. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
9. Selesaikan reCAPTCHA
10. Klik [Log in]
11. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
12. Verifikasi caption lock tidak tampil

### TC-AUTH-LP-50: Password salah ke-9 memicu status Requires Reset

13. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
14. Selesaikan reCAPTCHA
15. Klik [Log in]
16. Verifikasi Alert Danger di atas Button [Log in]: "Please reset your password"
17. Verifikasi tautan [Reset password] tampil satu baris di bawah teks Alert
18. Verifikasi Link "Forgot your password? " [Reset here] di footer tetap tampil
19. Verifikasi field Email tetap enabled
20. Verifikasi field Password tetap enabled
21. Verifikasi Button [Log in] tetap enabled

### TC-AUTH-LP-51: Submit password benar saat status Requires Reset tetap ditolak

22. Isi Password `Spectra.env.LP_PASSWORD`
23. Selesaikan reCAPTCHA
24. Klik [Log in]
25. Verifikasi Alert Danger "Please reset your password" tampil
26. Verifikasi tautan [Reset password] tampil di bawah teks Alert
27. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-52: Tautan [Reset password] pada Alert membuka halaman Reset Password

28. Muat ulang halaman Login with Password
29. Isi Email `rinaputri+{runId}-012@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
30. Selesaikan reCAPTCHA
31. Klik [Log in]
32. Klik tautan [Reset password] pada Alert
33. Verifikasi halaman Reset Password terbuka
34. Verifikasi field Email pada halaman Reset Password terisi "rinaputri+{runId}-012@qwertysystem.net"

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-LP-48 sampai TC-AUTH-LP-52 bergantung berantai di TC sumber (kolom Dependensi). State awal rantai (terkunci 1 jam setelah 6 kegagalan) disiapkan lewat seeding fixture BE (S-04); progresi yang membangunnya diuji di spec `TC-AUTH-LP-E2E-011-lock-15m-expiry-and-1h-stage`.
- Aksi yang membuka halaman lain (klik tautan [Reset password], TC-AUTH-LP-52) ditaruh paling akhir (prinsip bagian 3): setelah itu form Login tidak lagi dapat dipakai.
- Langkah penghubung (S-03): langkah 28 (muat ulang halaman Login with Password) mengembalikan form ke keadaan awal sebelum TC-AUTH-LP-52; pengisian ulang Password dan reCAPTCHA sebelum tiap submit karena field Password dikosongkan dan reCAPTCHA kembali Unsolved setelah respons.
- Temuan untuk QA (TC-AUTH-LP-48): Langkah Uji 2 "Tunggu sampai waktu {time} terlewati" untuk lock 1 jam tidak praktis tanpa geser jam; spec memakai geser jam server uji. Precondition juga meminta "waktu lock sudah terlewat" yang bertentangan dengan langkah menunggu; spec memperlakukan precondition sebagai state terkunci 1 jam yang belum berakhir.
- Temuan untuk QA (TC-AUTH-LP-48, TC-AUTH-LP-49): Post Condition "Hitungan gagal hari ini = 7" dan "= 8" tidak punya langkah observasi di TC (UI tidak menampilkan hitungan) sehingga tidak diasersi.
- Temuan untuk QA (TC-AUTH-LP-52): Langkah Uji 2 memakai password salah (`Spectra.env.LP_PASSWORD_WRONG`) padahal data uji hanya menyebut Email; spec mengikuti langkah TC.
