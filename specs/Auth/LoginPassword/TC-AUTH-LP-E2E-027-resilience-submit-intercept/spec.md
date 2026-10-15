---
id: TC-AUTH-LP-E2E-027-resilience-submit-intercept
title: "Ketahanan Submit Login dan Konfirmasi Agreement: Loading, Error Server, dan Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-92
  - TC-AUTH-LP-97
  - TC-AUTH-LP-98
  - TC-AUTH-LP-99
coverage:
  web: automated
---

# Ketahanan Submit Login dan Konfirmasi Agreement: Loading, Error Server, dan Timeout

## Prerequisites

- Seeding: setiap user Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`; autentikasi API, bukan sesi browser). User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-027` (contoh `jokosusilo+{runId}-027@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: `Spectra.intercept()` pada respons HTTP di atas backend nyata untuk (a) menahan respons permintaan login, (b) mengembalikan status 500 pada permintaan login, (c) menahan permintaan login tanpa respons, dan (d) mengembalikan status 500 pada permintaan konfirmasi Agreement, masing-masing bisa dinyalakan dan dimatikan; kontrol jam klien (jam browser dimajukan melewati batas waktu timeout FE untuk TC-AUTH-LP-99, tanpa menunggu waktu nyata; batas timeout adalah konfigurasi FE yang tidak disebut TC, lihat Temuan untuk QA); jendela privat baru per TC; reCAPTCHA mode uji di environment; fixture BE untuk kondisi versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui, device terpercaya, dan tidak memicu MFA (TC-AUTH-LP-92).
- Pemulihan: intersepsi dimatikan dan jam klien dipulihkan pada akhir tiap TC dan di hook `after` (tetap jalan walau spec gagal).
- Mode mengikuti bagian 6 konvensi: intersepsi parsial di atas backend nyata dan asersi state backend (tidak ada sesi), jadi FE+BE.
- Mode: FE+BE
- TC-AUTH-LP-97: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-97: User `Joko Susilo` (`jokosusilo+{runId}-027@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 (di-seed lewat API di hook `before`)
- TC-AUTH-LP-97 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-98: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-98: User yang sama dengan TC-AUTH-LP-97 (`jokosusilo+{runId}-027@qwertysystem.net`), hitungan gagal tetap 0 karena kegagalan server tidak dihitung sebagai password salah
- TC-AUTH-LP-98 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-99: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-99: User yang sama dengan TC-AUTH-LP-97 (`jokosusilo+{runId}-027@qwertysystem.net`), hitungan gagal tetap 0
- TC-AUTH-LP-99 data: Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-92: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-92: User `Taufik Hidayat` (`taufikhidayat+{runId}-027@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya; tidak memicu MFA (di-seed lewat API di hook `before`)
- TC-AUTH-LP-92 data: Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-97: State loading saat submit sedang diproses

1. Buka jendela privat baru (tanpa sesi login)
2. Buka halaman Login with Password
3. Isi Email `jokosusilo+{runId}-027@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
4. Selesaikan reCAPTCHA
5. Perlambat respons jaringan untuk permintaan login (intersepsi menahan respons)
6. Klik [Log in] dan amati halaman sebelum respons diterima
7. Verifikasi Button [Log in] menampilkan spinner
8. Verifikasi field Email disabled
9. Verifikasi field Password disabled
10. Lepaskan perlambatan jaringan (matikan intersepsi)
11. Verifikasi spinner hilang
12. Verifikasi hasil login tampil
13. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-98: Kesalahan server (5xx) saat submit login

14. Buka jendela privat baru (tanpa sesi login)
15. Buka halaman Login with Password
16. Isi Email `jokosusilo+{runId}-027@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
17. Selesaikan reCAPTCHA
18. Aktifkan intersepsi jaringan agar permintaan login mengembalikan status 500
19. Klik [Log in]
20. Verifikasi Toast error "Error, failed to log in." tampil
21. Verifikasi field Email tetap terisi `jokosusilo+{runId}-027@qwertysystem.net`
22. Verifikasi field Password tetap terisi (password tidak dikosongkan)
23. Verifikasi widget reCAPTCHA kembali Unsolved
24. Verifikasi Button [Log in] enabled kembali
25. Verifikasi Alert pesan server tidak tampil
26. Verifikasi tidak ada sesi dibuat
27. Matikan intersepsi jaringan
28. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-99: Timeout jaringan saat submit login

29. Buka jendela privat baru (tanpa sesi login)
30. Buka halaman Login with Password
31. Isi Email `jokosusilo+{runId}-027@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
32. Selesaikan reCAPTCHA
33. Aktifkan intersepsi jaringan agar permintaan login tidak mendapat respons
34. Klik [Log in]
35. Majukan jam browser melewati batas waktu timeout FE tanpa menunggu waktu nyata
36. Verifikasi Toast error "Error, failed to log in." tampil
37. Verifikasi field Email tetap terisi `jokosusilo+{runId}-027@qwertysystem.net`
38. Verifikasi field Password tetap terisi
39. Verifikasi widget reCAPTCHA kembali Unsolved
40. Verifikasi Button [Log in] enabled kembali
41. Verifikasi tidak ada sesi dibuat
42. Matikan intersepsi jaringan dan pulihkan jam browser
43. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-92: Kesalahan server saat konfirmasi Agreement

44. Buka jendela privat baru (tanpa sesi login)
45. Buka halaman Login with Password
46. Isi Email `taufikhidayat+{runId}-027@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
47. Selesaikan reCAPTCHA
48. Klik [Log in] → layar Confirm to Continue tampil
49. Centang checkbox persetujuan
50. Aktifkan intersepsi jaringan agar permintaan konfirmasi Agreement mengembalikan status 500
51. Klik [Continue ➔]
52. Verifikasi Toast error "Error, failed to log in." tampil
53. Verifikasi layar Confirm to Continue tetap terbuka
54. Nonaktifkan intersepsi jaringan
55. Klik [Continue ➔]
56. Verifikasi browser menuju Portal — Product Hub

## Notes

- Mode: FE+BE (intersepsi parsial di atas backend nyata). Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Kelas harness: fault injection (prinsip 13b), satu spec per kelas per modul. TC-AUTH-LP-97 menahan respons hanya untuk mengamati state loading dan bukan kelas b; ditaruh paling awal sebagai screening state sebelum kasus kegagalan (S-10). Kegagalan sisi penyedia/server yang tidak bisa di-intercept (reCAPTCHA, geo-IP, versi policy) ada di spec `TC-AUTH-LP-E2E-028-resilience-provider-failure-injection`.
- Langkah login pada TC-AUTH-LP-92 ("Login dengan Email … sampai layar Confirm to Continue tampil") disalin utuh menjadi langkah 45–48 (S-04). "Buka jendela privat baru" dan "Matikan intersepsi" adalah langkah penghubung supaya TC berikutnya mulai dari state bersih (S-03, S-09).
- Langkah 35 (memajukan jam browser) memicu timeout TC-AUTH-LP-99 secara deterministik tanpa menunggu waktu nyata (konvensi bagian 6); pemulihan jam di langkah 42 dan hook `after` (S-03, S-09).
- Langkah 26 dan 41 hanya mengasersi "tidak ada sesi dibuat" sesuai Expected TC-AUTH-LP-98/99; klausa tambahan "tetap di halaman Login dan tidak menuju Portal" tidak ada di TC sehingga tidak diasersi (S-03). Sesi web teramati sebagai Portal tidak tampil (S-01).
- Spec ini melewati sekitar 35 langkah (menurut konvensi bagian 3 sebuah smell, bukan kriteria): satu kelas harness (fault injection, prinsip 13b) dan satu topik (ketahanan submit login dan konfirmasi Agreement); empat TC masing-masing berdiri sendiri (jendela privat baru, intersepsi dimatikan di akhir tiap TC), sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal. Dipecah per TC hanya menambah login, hook, dan cleanup tanpa manfaat isolasi.
- Langkah 13, 28, dan 43 (menutup semua jendela privat dan menghapus sesi browser terkait) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai dari konteks browser bersih (S-03; S-09).
- Temuan untuk QA:
  - TC-AUTH-LP-97 Expected "hasil login tampil" tidak menyebut hasil yang mana (Portal, Confirm to Continue, atau MFA) dan precondition tidak menyebut device/gate Agreement; spec mengasersi apa adanya ("hasil login tampil").
  - TC-AUTH-LP-99 tidak menyebut nilai batas waktu (timeout); durasi bergantung konfigurasi FE, sehingga timeout dipicu dengan memajukan jam browser (konvensi bagian 6) dan bukan menunggu waktu nyata.
  - TC-AUTH-LP-92 langkah 5 menekan [Continue ➔] lagi tanpa menyebut apakah checkbox masih tercentang setelah kegagalan; spec mengikuti TC (tidak mencentang ulang).
  - TC-AUTH-LP-98/99 memakai user yang sama dengan TC-AUTH-LP-97, dengan klaim hitungan gagal 0 di awal tiap TC; spec mengandalkan kegagalan server tidak menambah hitungan, yang tidak dinyatakan eksplisit di TC.
