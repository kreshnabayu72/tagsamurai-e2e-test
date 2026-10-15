---
id: TC-AUTH-LP-E2E-035-log-failed-attempts-basic
title: "Pencatatan Log Login Gagal: Password Kosong, reCAPTCHA, Status Akun, dan Password Salah"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-105
  - TC-AUTH-LP-106
  - TC-AUTH-LP-107
  - TC-AUTH-LP-108
  - TC-AUTH-LP-109
coverage:
  web: automated
---

# Pencatatan Log Login Gagal: Password Kosong, reCAPTCHA, Status Akun, dan Password Salah

## Prerequisites

- Mode: FE+BE.
- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dan dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Hook `before` login akun aktor di browser kedua (jendela terpisah dari browser pertama) dan sesi itu tetap terbuka sepanjang spec; browser pertama dipakai subjek sebagai guest.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua browser terpisah (subjek dan aktor pengamat log); reCAPTCHA mode uji di environment; aktor dapat membuka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`.
- Baris log awal: user `Joko Susilo` memiliki sedikitnya satu baris login sebelumnya (anchor) di kedua surface, dibuat di hook `before` lewat fixture BE; jumlah baris awal tiap user dicatat di langkah 1 dan 2, dan jumlah baris Joko S pada kedua surface sesudah TC-AUTH-LP-105 dicatat lagi di langkah 11 sebagai baseline TC-AUTH-LP-106.
- Baris log dikenali lewat nama tampilan dari TC ("Joko S", "Dewi L", "Agus S", "Joni W"), bukan email dengan suffix run. Spec log ini berjalan serial (`parallel: false`) dengan spec log lain di suite dan memakai baseline jumlah baris (S-12) agar nama tampilan yang sama dari run atau spec lain tidak mengaburkan hitungan "tepat 1 baris baru".
- TC-AUTH-LP-105: Tanpa login (guest); browser web
- TC-AUTH-LP-105: User `Joko Susilo` (`jokosusilo+{runId}-035@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0
- TC-AUTH-LP-105 data: Email `jokosusilo+{runId}-035@qwertysystem.net`; Password (kosong)
- TC-AUTH-LP-106: Tanpa login (guest); browser web
- TC-AUTH-LP-106: User `Joko Susilo` (`jokosusilo+{runId}-035@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0
- TC-AUTH-LP-106 data: Email `jokosusilo+{runId}-035@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-107: Tanpa login (guest); browser web
- TC-AUTH-LP-107: User `Dewi Lestari` (`dewilestari+{runId}-035@qwertysystem.net`) berstatus Pending Activation
- TC-AUTH-LP-107 data: Email `dewilestari+{runId}-035@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-108: Tanpa login (guest); browser web
- TC-AUTH-LP-108: User `Agus Setiawan` (`agussetiawan+{runId}-035@qwertysystem.net`) berstatus Activated dengan Toggle Global OFF
- TC-AUTH-LP-108 data: Email `agussetiawan+{runId}-035@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-109: Tanpa login (guest); browser web
- TC-AUTH-LP-109: User `Joni Widodo` (`joniwidodo+{runId}-035@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0
- TC-AUTH-LP-109 data: Email `joniwidodo+{runId}-035@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD_WRONG`

## Test Steps

### Jumlah baris log awal

1. Ganti akun: beralih ke browser kedua (sesi akun aktor Total Control Global Settings dari hook `before`), buka `Global Settings > Activity Log > Session`, lalu catat jumlah baris awal untuk user "Joko S", "Dewi L", "Agus S", dan "Joni W"
2. Buka `Global Settings > User > Detail > User Log` untuk masing-masing dari keempat user itu, lalu catat jumlah baris awal

### TC-AUTH-LP-105: Pencatatan Password kosong

3. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
4. Isi Email "jokosusilo+{runId}-035@qwertysystem.net", kosongkan Password, selesaikan reCAPTCHA, klik [Log in]
5. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Joko S" tampil
6. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Joko S", Activity "Login", Status "Failed" (teks biasa), Note "Empty password"
7. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
8. Buka `Global Settings > User > Detail > User Log` untuk user "Joko S", buka tab User Log, lalu cari baris terbaru
9. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Failed", Note "Empty password"
10. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji

### TC-AUTH-LP-106: Pencatatan reCAPTCHA belum diselesaikan

11. Catat jumlah baris untuk user "Joko S" pada `Global Settings > Activity Log > Session` dan pada User Log (browser kedua) sebagai baseline TC-AUTH-LP-106, setelah baris TC-AUTH-LP-105
12. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
13. Isi Email "jokosusilo+{runId}-035@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, lalu tanpa menyelesaikan reCAPTCHA klik [Log in]
14. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Joko S" tampil
15. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Joko S", Activity "Login", Status "Failed" (teks biasa), Note "Captcha not completed"
16. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
17. Buka `Global Settings > User > Detail > User Log` untuk user "Joko S", buka tab User Log, lalu cari baris terbaru
18. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Failed", Note "Captcha not completed"
19. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji

### TC-AUTH-LP-107: Pencatatan akun belum diaktivasi

20. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
21. Isi Email "dewilestari+{runId}-035@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
22. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Dewi L" tampil
23. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Dewi L", Activity "Login", Status "Failed" (teks biasa), Note "Account is not activated"
24. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
25. Buka `Global Settings > User > Detail > User Log` untuk user "Dewi L", buka tab User Log, lalu cari baris terbaru
26. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Failed", Note "Account is not activated"
27. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji

### TC-AUTH-LP-108: Pencatatan akun inactive

28. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
29. Isi Email "agussetiawan+{runId}-035@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
30. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Agus S" tampil
31. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Agus S", Activity "Login", Status "Failed" (teks biasa), Note "Account is inactive"
32. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
33. Buka `Global Settings > User > Detail > User Log` untuk user "Agus S", buka tab User Log, lalu cari baris terbaru
34. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Failed", Note "Account is inactive"
35. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji

### TC-AUTH-LP-109: Pencatatan password salah (percobaan ke-1)

36. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
37. Isi Email "joniwidodo+{runId}-035@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD_WRONG`, selesaikan reCAPTCHA, klik [Log in]
38. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Joni W" tampil
39. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Joni W", Activity "Login", Status "Failed" (teks biasa), Note "Incorrect password"
40. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
41. Buka `Global Settings > User > Detail > User Log` untuk user "Joni W", buka tab User Log, lalu cari baris terbaru
42. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Failed", Note "Incorrect password"
43. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah penghubung (S-03): langkah 1 dan 2 mencatat jumlah baris awal sebagai acuan "tepat 1 baris baru" (TC-AUTH-LP-105 menyebut baris sebelumnya sebagai anchor). Untuk user yang sama pada TC-AUTH-LP-105 dan TC-AUTH-LP-106, acuan TC-AUTH-LP-106 adalah jumlah baris setelah TC-AUTH-LP-105, dicatat di langkah 11 (juga langkah penghubung tanpa awalan `Verifikasi`).
- Langkah "Ganti akun" memakai dua browser yang tetap terbuka (subjek guest dan aktor pengamat); tidak ada login ulang di Test Steps karena sesi aktor dibuat di hook `before` (S-07).
- Spec ini memuat lebih dari 35 langkah karena 5 TC masing-masing menuntut verifikasi di dua surface; ditinjau dan tetap satu spec karena satu topik aksi (pencatatan login gagal) dengan akun aktor yang sama.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - TC mengenali baris log lewat nama tampilan tetap ("Joko S", "Dewi L", "Agus S", "Joni W"), bukan email dengan suffix run; spec dijalankan serial dengan baseline jumlah baris untuk menghindari bentrok nama (Prerequisites).
  - Nilai "terisi sesuai perangkat uji" pada IP Address dan Device / Browser (semua TC) tidak menyebut nilai pasti; asersi memeriksa kolom terisi dan sesuai perangkat runner.
  - Pre-setup TC (baris 21) mencatat user Joko Susilo dipakai di TC-AUTH-LP-105 dan TC-AUTH-LP-106 dengan "hitungan gagal 0 di awal tiap TC"; kedua TC tidak menambah hitungan gagal sehingga satu user cukup di spec ini.
