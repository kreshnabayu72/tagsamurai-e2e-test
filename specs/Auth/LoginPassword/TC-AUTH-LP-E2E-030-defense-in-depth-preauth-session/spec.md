---
id: TC-AUTH-LP-E2E-030-defense-in-depth-preauth-session
title: "Defense-in-Depth Sesi dan Token Pra-Autentikasi: Akses Portal Langsung, Token Dimodifikasi, dan Token Dipakai Ulang"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-141
  - TC-AUTH-LP-142
  - TC-AUTH-LP-143
  - TC-AUTH-LP-149
coverage:
  web: automated
---

# Defense-in-Depth Sesi dan Token Pra-Autentikasi: Akses Portal Langsung, Token Dimodifikasi, dan Token Dipakai Ulang

## Prerequisites

- Seeding: setiap user Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`; autentikasi API, bukan sesi browser). User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-030` (contoh `tonokurniawan+{runId}-030@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: intersepsi dan modifikasi isi permintaan konfirmasi Agreement lewat `Spectra.intercept()` (mengganti nilai token pra-autentikasi dengan teks acak); tombol Back dan navigasi history browser; mengubah alamat browser pada tab yang sama; jendela privat baru per TC; reCAPTCHA mode uji di environment; fixture BE untuk kondisi per user (lihat daftar TC di bawah).
- Pemulihan: intersepsi dimatikan pada akhir TC yang memakainya dan di hook `after` (tetap jalan walau spec gagal).
- Mode: FE+BE
- TC-AUTH-LP-141: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-141: User `Tono Kurniawan` (`tonokurniawan+{runId}-030@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya (di-seed lewat API dan fixture BE di hook `before`)
- TC-AUTH-LP-141 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-142: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-142: User `Wati Handayani` (`watihandayani+{runId}-030@qwertysystem.net`) berstatus Activated dan Active; browser yang dipakai belum dikenal sebagai device terpercaya; tidak ada gate Agreement (di-seed lewat API dan fixture BE di hook `before`)
- TC-AUTH-LP-142 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-143: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-143: User `Wahyu Hidayat` (`wahyuhidayat+{runId}-030@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya; tidak memicu MFA (di-seed lewat API dan fixture BE di hook `before`)
- TC-AUTH-LP-143 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-149: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-149: User `Rahmat Hidayat` (`rahmathidayat+{runId}-030@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya; tidak memicu MFA (di-seed lewat API dan fixture BE di hook `before`)
- TC-AUTH-LP-149 data: Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-141: Sesi penuh tidak dibuat sebelum Agreement dikonfirmasi

1. Buka jendela privat baru (tanpa sesi login)
2. Buka halaman Login with Password
3. Isi Email `tonokurniawan+{runId}-030@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
4. Selesaikan reCAPTCHA
5. Klik [Log in] → layar Confirm to Continue tampil
6. Pada tab yang sama, ubah alamat browser ke Portal — Product Hub lalu tekan Enter
7. Verifikasi browser kembali ke halaman Login with Password
8. Verifikasi tidak ada sesi aktif
9. Verifikasi Portal — Product Hub tidak tampil
10. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-142: Sesi penuh tidak dibuat sebelum MFA tuntas

11. Buka jendela privat baru (tanpa sesi login)
12. Buka halaman Login with Password
13. Isi Email `watihandayani+{runId}-030@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
14. Selesaikan reCAPTCHA
15. Klik [Log in] → halaman MFA tampil
16. Pada tab yang sama, ubah alamat browser ke Portal — Product Hub lalu tekan Enter
17. Verifikasi browser kembali ke halaman Login with Password
18. Verifikasi tidak ada sesi aktif
19. Verifikasi Portal — Product Hub tidak tampil
20. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-143: Token pra-autentikasi yang dimodifikasi ditolak saat konfirmasi Agreement

21. Buka jendela privat baru (tanpa sesi login)
22. Buka halaman Login with Password
23. Isi Email `wahyuhidayat+{runId}-030@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
24. Selesaikan reCAPTCHA
25. Klik [Log in] → layar Confirm to Continue tampil
26. Centang checkbox persetujuan
27. Aktifkan intersepsi permintaan konfirmasi Agreement dan ganti nilai token pra-autentikasi dengan teks acak
28. Klik [Continue ➔] dan teruskan permintaan yang sudah dimodifikasi
29. Verifikasi browser kembali ke halaman Login with Password
30. Verifikasi tidak ada sesi aktif
31. Verifikasi browser tidak menuju Portal — Product Hub
32. Verifikasi tidak ada toast, Alert, atau pesan lain yang tampil
33. Verifikasi field Email kosong dan menampilkan placeholder "Enter your email"
34. Matikan intersepsi permintaan konfirmasi Agreement
35. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-149: Token pra-autentikasi yang sudah dipakai tidak dapat dipakai lagi

36. Buka jendela privat baru (tanpa sesi login)
37. Buka halaman Login with Password
38. Isi Email `rahmathidayat+{runId}-030@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
39. Selesaikan reCAPTCHA
40. Klik [Log in] → layar Confirm to Continue tampil
41. Centang checkbox persetujuan
42. Klik [Continue ➔] → Portal — Product Hub tampil
43. Logout
44. Tekan tombol Back browser berulang sampai layar Confirm to Continue tampil kembali
45. Centang checkbox persetujuan
46. Klik [Continue ➔]
47. Verifikasi browser kembali ke halaman Login with Password
48. Verifikasi browser tidak menuju Portal — Product Hub
49. Verifikasi tidak ada sesi aktif
50. Verifikasi tidak ada toast, Alert, atau pesan lain yang tampil
51. Verifikasi field Email kosong dan menampilkan placeholder "Enter your email"

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Kelas harness: defense-in-depth tanpa harness eksternal (prinsip 13a), satu spec untuk sesi dan token pra-autentikasi. Defense-in-depth pada request login (TC-AUTH-LP-139, 140, 144, 145) ada di spec `TC-AUTH-LP-E2E-029-defense-in-depth-login-request`.
- Langkah login pada TC sumber ("Login dengan Email … sampai layar Confirm to Continue tampil") disalin utuh menjadi langkah 2–5, 12–15, 22–25, dan 37–40 (S-04). "Buka alat pengembang browser" pada TC-AUTH-LP-143 dijalankan lewat `Spectra.intercept()`; "Buka jendela privat baru" dan "Matikan intersepsi" adalah langkah penghubung (S-03, S-09).
- TC-AUTH-LP-141, 142 tidak menyebut alamat Portal — Product Hub; langkah 6 dan 16 memakai Portal — Product Hub apa adanya.
- Spec ini melewati sekitar 35 langkah (smell menurut konvensi bagian 3, bukan kriteria): satu kelas harness (defense-in-depth tanpa harness eksternal, prinsip 13a) dan satu topik (sesi penuh tidak dibuat sebelum token pra-autentikasi sah); empat TC memakai user, jendela privat, dan intersepsi sendiri, jadi bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal. Memecahnya hanya menambah login, hook, dan cleanup.
- Langkah 10, 20, dan 35 (menutup semua jendela privat dan menghapus sesi browser terkait) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai dari konteks browser bersih (S-03; S-09).
- Temuan untuk QA:
  - TC-AUTH-LP-149 langkah 3 bergantung pada perilaku history/cache browser ("tekan Back … sampai layar Confirm to Continue tampil kembali") tanpa Expected untuk langkah itu; spec mengikuti TC dan tidak mengasersi tampilnya layar tersebut.
  - TC-AUTH-LP-141/142 tidak menyebut mekanisme "tidak ada sesi aktif" selain kembali ke halaman Login; spec mengasersi lewat hasil navigasi ke Portal.
  - TC-AUTH-LP-143 memakai Expected yang sama dengan TC-AUTH-LP-88 (token kedaluwarsa) dan TC-AUTH-LP-149; tidak ada selisih perilaku yang tertulis antara token kedaluwarsa, dimodifikasi, dan dipakai ulang.
