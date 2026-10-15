---
id: TC-AUTH-LP-E2E-042-absence-input-rejections
title: "Tidak Ada Pencatatan Log untuk Penolakan Input pada Login with Password"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-117
  - TC-AUTH-LP-118
  - TC-AUTH-LP-119
  - TC-AUTH-LP-121
  - TC-AUTH-LP-161
coverage:
  web: automated
---

# Tidak Ada Pencatatan Log untuk Penolakan Input pada Login with Password

## Prerequisites

- Mode: FE+BE.
- Seeding: user Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`), lalu dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Baris log awal (anchor) untuk tiap user subjek di `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` disiapkan di hook `before` (kemampuan fixture BE: satu entri log awal per user).
- Aktor observer log: akun aktor Total Control (Global Settings) di atas login di browser kedua pada hook `before`; browser kedua ditutup di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua sesi browser bersamaan; reCAPTCHA mode uji di environment.
- Pencarian baris log memakai nama tampilan dari TC ("Joko S", "Budi S"; kolom User menampilkan nama singkat, bukan email). Suite berjalan serial (`parallel: false`) dan baseline-nya adalah baris anchor per user dari hook `before` serta penanda waktu sesudah langkah pembuka tiap TC (S-12), sehingga tidak ada spec lain yang menulis baris untuk nama yang sama selama spec ini berjalan.
- TC-AUTH-LP-117: User `Joko Susilo` (`jokosusilo+{runId}-042@qwertysystem.net`) berstatus Activated dan Active; sudah ada baris log sebelumnya (anchor)
- TC-AUTH-LP-117 data: Email dikosongkan; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-118: User `Joko Susilo` yang sama; sudah ada baris log sebelumnya (anchor)
- TC-AUTH-LP-118 data: Email "jokosusilo@qwertysystem" (format salah, literal uji validasi yang diblokir); Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-119: Email `tidakada@qwertysystem.net` belum terdaftar; user `Joko Susilo` yang sama sudah punya baris log sebelumnya (anchor)
- TC-AUTH-LP-119 data: Email "tidakada@qwertysystem.net"; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-121: User `Budi Santoso` (`budisantoso+{runId}-042@qwertysystem.net`) berstatus Activated dan Active; sudah ada baris log sebelumnya (anchor)
- TC-AUTH-LP-121 data: Email `budisantoso+{runId}-042@qwertysystem.net`
- TC-AUTH-LP-161: Tanpa login (halaman publik)
- TC-AUTH-LP-161 data: Email 121 karakter "a" tanpa tanda @ (literal uji validasi yang diblokir); Password `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-117: Email kosong tidak dicatat

1. Buka halaman Login with Password di browser pertama
2. Kosongkan field Email
3. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
4. Selesaikan reCAPTCHA
5. Klik [Log in]
6. Verifikasi caption "Email must not be empty" tampil di halaman Login
7. Pindah ke browser kedua (sesi aktor Total Control Global Settings) dan buka `Global Settings > Activity Log > Session`
8. Cari baris untuk user "Joko S" yang dibuat sesudah langkah 1 dimulai
9. Verifikasi tidak ada baris baru untuk user "Joko S" di `Global Settings > Activity Log > Session` (anchor: baris login sebelumnya tetap tampil)
10. Buka `Global Settings > User > Detail > User Log` untuk user "Joko S" dan buka tab User Log
11. Verifikasi tidak ada baris baru di `Global Settings > User > Detail > User Log` (anchor: baris sebelumnya tetap tampil)

### TC-AUTH-LP-118: Format Email salah tidak dicatat

12. Pindah ke browser pertama dan buka halaman Login with Password
13. Ketik "jokosusilo@qwertysystem" di field Email
14. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
15. Selesaikan reCAPTCHA
16. Klik [Log in]
17. Verifikasi caption "Email format is incorrect" tampil di halaman Login
18. Pindah ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, lalu cari baris untuk user "Joko S" yang dibuat sesudah langkah 12 dimulai
19. Verifikasi tidak ada baris baru untuk user "Joko S" di `Global Settings > Activity Log > Session` (anchor: baris login sebelumnya tetap tampil)
20. Buka `Global Settings > User > Detail > User Log` untuk user "Joko S", buka tab User Log, dan cari baris yang dibuat sesudah langkah 12 dimulai
21. Verifikasi tidak ada baris baru di `Global Settings > User > Detail > User Log` (anchor: baris sebelumnya tetap tampil)

### TC-AUTH-LP-119: Email belum terdaftar tidak dicatat

22. Pindah ke browser pertama dan buka halaman Login with Password
23. Ketik "tidakada@qwertysystem.net" di field Email
24. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
25. Selesaikan reCAPTCHA
26. Klik [Log in]
27. Verifikasi caption "Email is not registered yet" tampil di bawah field Email
28. Pindah ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, lalu cari baris untuk user "Joko S" yang dibuat sesudah langkah 22 dimulai
29. Verifikasi tidak ada baris baru untuk user "Joko S" di `Global Settings > Activity Log > Session` (anchor: baris login sebelumnya tetap tampil)
30. Buka `Global Settings > User > Detail > User Log` untuk user "Joko S", buka tab User Log, dan cari baris yang dibuat sesudah langkah 22 dimulai
31. Verifikasi tidak ada baris baru di `Global Settings > User > Detail > User Log` (anchor: baris sebelumnya tetap tampil)
32. Verifikasi tidak ada baris log baru untuk email "tidakada@qwertysystem.net" di surface mana pun (`Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`)

### TC-AUTH-LP-121: Navigasi ke Login with OTP dan Reset Password tidak dicatat

33. Pindah ke browser pertama dan buka halaman Login with Password
34. Ketik "budisantoso+{runId}-042@qwertysystem.net" di field Email
35. Klik link [Log in with OTP]
36. Verifikasi halaman Login with OTP terbuka
37. Kembali ke halaman Login with Password
38. Klik link [Reset here]
39. Verifikasi halaman Reset Password terbuka
40. Pindah ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, lalu cari baris untuk user "Budi S" yang dibuat sesudah langkah 33 dimulai
41. Verifikasi tidak ada baris baru untuk user "Budi S" di `Global Settings > Activity Log > Session` (anchor: baris login sebelumnya tetap tampil)
42. Buka `Global Settings > User > Detail > User Log` untuk user "Budi S", buka tab User Log, dan cari baris yang dibuat sesudah langkah 33 dimulai
43. Verifikasi tidak ada baris baru di `Global Settings > User > Detail > User Log` (anchor: baris sebelumnya tetap tampil)

### TC-AUTH-LP-161: Email 121 karakter tanpa tanda @ tidak dicatat

44. Pindah ke browser pertama dan buka halaman Login with Password
45. Ketik 121 karakter "a" tanpa tanda @ di field Email
46. Pindahkan fokus ke field Password (field Email blur)
47. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
48. Selesaikan reCAPTCHA
49. Klik [Log in]
50. Pindah ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, lalu cari baris yang dibuat sesudah langkah 44 dimulai
51. Verifikasi tidak ada entri log baru untuk percobaan pada langkah 49 di `Global Settings > Activity Log > Session`

## Notes

- Sumber: `auth/login-password/TestCases/tc-login-password.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: asersi absence (prinsip 13g); asersi pencatatan ada di spec pencatatan log. Semua kasus di spec ini hanya membutuhkan dua sesi browser tanpa harness tambahan.
- TC-AUTH-LP-161 terbagi lintas spec: asersi caption "Email format is incorrect", "Max. 120 characters", dan "Email is not registered yet" diuji di spec `TC-AUTH-LP-E2E-002-email-validation-blocked`; di spec ini hanya asersi tidak adanya entri log (Expected butir c, S-05, prinsip 10).
- Langkah penghubung (S-03): perpindahan antar browser, pemuatan ulang daftar log, dan kembali ke halaman Login with Password pada langkah 37 hanya menyiapkan konteks; tidak ada asersi tambahan di luar Expected TC.
- Temuan untuk QA:
  - TC-AUTH-LP-119 memeriksa log user "Joko S" padahal percobaan memakai email tidak terdaftar yang tidak terkait user tersebut; Expected butir c menambah "tidak ada baris log baru untuk email tersebut di surface mana pun" (langkah 32) tanpa menyebut cara mencari baris untuk email yang bukan milik user mana pun.
  - TC-AUTH-LP-121 langkah 3 ("kembali ke halaman Login with Password") tidak menyebut cara kembali (tombol Back browser atau navigasi langsung); spec memakai "Kembali ke halaman Login with Password".
  - TC-AUTH-LP-161 Expected butir c ("Tidak ada entri log baru untuk percobaan ini") tidak menyebut surface atau user yang diperiksa; email tidak memetakan ke user mana pun. Spec memeriksa `Global Settings > Activity Log > Session` saja.
  - TC-AUTH-LP-117, 118, 119 mengamati log "Joko S" sedangkan TC-AUTH-LP-121 mengamati "Budi S"; kedua user diseed di spec ini sehingga nama tampilan "Joko S" dan "Budi S" harus unik dalam data run; TC memakai nama tampilan tetap itu, sehingga spec mengandalkan suite serial dan baseline (S-12).
