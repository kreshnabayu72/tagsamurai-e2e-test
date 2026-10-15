---
id: TC-AUTH-LP-E2E-029-defense-in-depth-login-request
title: "Defense-in-Depth Request Login: Token reCAPTCHA Dihapus, Bypass Lock, SQL Injection, dan XSS"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-139
  - TC-AUTH-LP-140
  - TC-AUTH-LP-144
  - TC-AUTH-LP-145
coverage:
  web: automated
---

# Defense-in-Depth Request Login: Token reCAPTCHA Dihapus, Bypass Lock, SQL Injection, dan XSS

## Prerequisites

- Seeding: setiap user Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`; autentikasi API, bukan sesi browser). User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-029` (contoh `jokosusilo+{runId}-029@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama. Email uji injeksi (TC-AUTH-LP-144 dan TC-AUTH-LP-145) tetap literal karena submit-nya diblokir.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: intersepsi dan modifikasi isi permintaan login lewat `Spectra.intercept()` (menghapus field token reCAPTCHA dari isi permintaan, meneruskan permintaan tanpa perubahan); pemantauan dialog browser (untuk memastikan tidak ada dialog yang dipicu skrip); jendela privat baru per TC; reCAPTCHA mode uji di environment; fixture BE untuk user terkunci 1 jam di web (TC-AUTH-LP-140).
- Pemulihan: intersepsi dimatikan pada akhir tiap TC yang memakainya dan di hook `after` (tetap jalan walau spec gagal).
- Mode: FE+BE
- TC-AUTH-LP-139: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-139: User `Joko Susilo` (`jokosusilo+{runId}-029@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 (di-seed lewat API di hook `before`)
- TC-AUTH-LP-139 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-140: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-140: User `Vina Melati` (`vinamelati+{runId}-029@qwertysystem.net`) berstatus Activated dan Active, password `Spectra.env.LP_PASSWORD`, sedang terkunci 1 jam di web (di-seed lewat API dan fixture BE di hook `before`)
- TC-AUTH-LP-140 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-144: Tanpa login (halaman publik, tidak ada sesi aktif di browser); tidak butuh user terdaftar
- TC-AUTH-LP-144 data: Email: `' OR 1=1 --` (literal, submit diblokir); Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-145: Tanpa login (halaman publik, tidak ada sesi aktif di browser); tidak butuh user terdaftar
- TC-AUTH-LP-145 data: Email: `<script>alert(1)</script>` (literal, submit diblokir); Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-139: Permintaan login web tanpa token reCAPTCHA ditolak server

1. Buka jendela privat baru (tanpa sesi login)
2. Buka halaman Login with Password
3. Isi Email `jokosusilo+{runId}-029@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD` tanpa menyelesaikan reCAPTCHA
4. Aktifkan intersepsi permintaan login dan hapus field token reCAPTCHA dari isi permintaan
5. Klik [Log in] dan teruskan permintaan yang sudah dimodifikasi
6. Verifikasi Caption "Please verify that you are not a robot" tampil tepat di bawah widget reCAPTCHA
7. Verifikasi tidak ada sesi dibuat
8. Verifikasi browser tidak menuju Portal — Product Hub
9. Matikan intersepsi permintaan login
10. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-140: Permintaan login langsung saat lock aktif tetap ditolak server

11. Buka jendela privat baru (tanpa sesi login)
12. Buka halaman Login with Password
13. Isi Email `vinamelati+{runId}-029@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
14. Selesaikan reCAPTCHA
15. Aktifkan intersepsi permintaan login
16. Klik [Log in] dan teruskan permintaan tanpa perubahan
17. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 1 hour. You can try again at {time}." tampil ({time} = jam berakhirnya lock)
18. Matikan intersepsi permintaan login
19. Ubah alamat browser ke Portal — Product Hub
20. Verifikasi browser kembali ke halaman Login with Password karena tidak ada sesi aktif
21. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-144: Email berisi pola injeksi SQL ditolak sebagai format salah

22. Buka jendela privat baru (tanpa sesi login)
23. Buka halaman Login with Password
24. Isi Email `' OR 1=1 --` dan Password nilai `Spectra.env.LP_PASSWORD`
25. Selesaikan reCAPTCHA
26. Klik [Log in]
27. Verifikasi Caption "Email format is incorrect" tampil di bawah field Email
28. Verifikasi tidak ada sesi dibuat
29. Verifikasi tidak ada pesan error teknis
30. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-145: Email berisi tag script ditolak sebagai format salah tanpa dieksekusi

31. Buka jendela privat baru (tanpa sesi login)
32. Buka halaman Login with Password
33. Isi Email `<script>alert(1)</script>` dan Password nilai `Spectra.env.LP_PASSWORD`
34. Selesaikan reCAPTCHA
35. Klik [Log in]
36. Verifikasi Caption "Email format is incorrect" tampil di bawah field Email
37. Verifikasi teks pada field Email dan caption ditampilkan sebagai teks biasa
38. Verifikasi tidak ada dialog atau skrip yang berjalan

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Kelas harness: defense-in-depth tanpa harness eksternal (prinsip 13a), satu spec untuk request login. Defense-in-depth pada sesi dan token pra-autentikasi (TC-AUTH-LP-141, 142, 143, 149) ada di spec `TC-AUTH-LP-E2E-030-defense-in-depth-preauth-session`.
- "Buka alat pengembang browser" pada TC-AUTH-LP-139 dan TC-AUTH-LP-140 dijalankan lewat `Spectra.intercept()` (langkah 4 dan 15); "Matikan intersepsi" adalah langkah penghubung (S-03, S-09).
- TC-AUTH-LP-139 dan TC-AUTH-LP-140 tidak menyebut alamat Portal — Product Hub; langkah 19 memakai Portal — Product Hub apa adanya.
- Langkah 10, 21, dan 30 (menutup semua jendela privat dan menghapus sesi browser terkait) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai dari konteks browser bersih (S-03; S-09).
- Temuan untuk QA:
  - Judul TC-AUTH-LP-139 menyebut "ditolak server", tetapi Expected hanya mengasersi caption di bawah widget reCAPTCHA dan tidak ada sesi; respons penolakan server tidak diasersi. Tambahan: langkah 3 menyebut reCAPTCHA tidak diselesaikan sementara langkah 4 menghapus token dari permintaan, sehingga caption bisa berasal dari sisi FE, bukan dari penolakan server.
  - Langkah 4 TC-AUTH-LP-140 meneruskan permintaan tanpa perubahan, sehingga hasilnya sama dengan submit biasa saat lock aktif (TC-AUTH-LP-47); nilai defense-in-depth-nya bergantung pada intersepsi yang ada, yang tidak mengubah permintaan.
  - TC-AUTH-LP-145 tidak menyebut cara memantau dialog yang dipicu skrip; spec mencantumkan pemantauan dialog browser sebagai kemampuan teknis.
