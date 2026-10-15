---
id: TC-AUTH-LP-E2E-040-log-format-general-settings
title: "Format Tanggal, Jam, dan Zona Waktu Mengikuti General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-135
  - TC-AUTH-LP-136
  - TC-AUTH-LP-137
  - TC-AUTH-LP-138
coverage:
  web: automated
---

# Format Tanggal, Jam, dan Zona Waktu Mengikuti General Settings

## Prerequisites

- Mode: FE+BE.
- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dan dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Hook `before` login akun aktor di browser kedua (jendela terpisah dari browser pertama) dan sesi itu tetap terbuka sepanjang spec; browser pertama dipakai subjek sebagai guest. Akun aktor berhak mengubah `Global Settings > General Settings`.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua browser terpisah (subjek dan aktor pengamat); reCAPTCHA mode uji di environment; fixture BE untuk menetapkan device terpercaya dan tanpa pemicu Agreement dan MFA pada user Budi Santoso, serta fixture BE yang membentuk lock 15 menit (web) pada user Nur Aini; fixture itu dijalankan pada langkah 34, tepat sebelum langkah yang membutuhkannya, bukan di hook `before`, karena lock berakhir 15 menit sejak dibentuk dan TC-AUTH-LP-138 berada di akhir spec.
- State global: General Settings entitas diubah oleh spec ini. Nilai awal yang diasumsikan dan dipulihkan: Date Format "dd/MM/yy", Time Format "HH:mm", Time Zone "(UTC+07:00) Bangkok, Hanoi, Jakarta". Suite berjalan serial (`parallel: false`) karena General Settings entitas adalah state global bersama. Pemulihan (Date Format, Time Format, dan Time Zone kembali ke nilai awal di atas) dilakukan pada langkah akhir tiap TC dan di hook `after` sebagai cadangan yang tetap berjalan walau spec gagal di tengah.
- Pencarian baris log memakai nama tampilan dari TC ("Budi S"; kolom User menampilkan nama singkat, bukan email) dan hanya menghitung baris yang lebih baru dari penanda waktu yang dicatat sebelum login pada TC itu (S-12); daftar dimuat ulang sampai baris baru tampil karena penulisan log bisa terlambat (NC-18). Suite serial sehingga tidak ada spec lain yang menulis baris untuk nama yang sama.
- TC-AUTH-LP-135: Tanpa login (guest); browser web
- TC-AUTH-LP-135: User `Budi Santoso` (`budisantoso+{runId}-040@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA; General Settings entitas memakai Date Format default dan Time Format default
- TC-AUTH-LP-135 data: Email `budisantoso+{runId}-040@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-136: Tanpa login (guest); browser web
- TC-AUTH-LP-136: User `Budi Santoso` (`budisantoso+{runId}-040@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA; General Settings entitas memakai Date Format default dan Time Format default
- TC-AUTH-LP-136 data: Email `budisantoso+{runId}-040@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-137: Tanpa login (guest); browser web
- TC-AUTH-LP-137: User `Budi Santoso` (`budisantoso+{runId}-040@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA; General Settings entitas memakai Time Zone "(UTC+07:00) Bangkok, Hanoi, Jakarta" dan Time Format "HH:mm"
- TC-AUTH-LP-137 data: Email `budisantoso+{runId}-040@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-138: Tanpa login (guest); browser web
- TC-AUTH-LP-138: User `Nur Aini` (`nuraini+{runId}-040@qwertysystem.net`) terkunci 15 menit di web (lock dibentuk fixture BE pada langkah 34); General Settings entitas memakai Time Zone "(UTC+07:00) Bangkok, Hanoi, Jakarta"
- TC-AUTH-LP-138 data: Email `nuraini+{runId}-040@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD_WRONG`

## Test Steps

### TC-AUTH-LP-135: Format tanggal dan jam pada Activity Log Session mengikuti General Settings

1. Ganti akun: beralih ke browser kedua (sesi akun aktor dari hook `before`), buka `Global Settings > General Settings`, ubah Date Format menjadi "dd MMM yy" dan Time Format menjadi "hh:mm a", lalu simpan
2. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
3. Catat penanda waktu sebelum login (baseline, S-12)
4. Isi Email "budisantoso+{runId}-040@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
5. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, muat ulang daftar sampai baris baru untuk user "Budi S" yang lebih baru dari penanda waktu langkah 3 tampil, lalu baca kolom Date baris itu
6. Verifikasi tanggal pada kolom Date baris tersebut tampil dalam pola dd MMM yy
7. Verifikasi jam pada kolom Date baris tersebut tampil dalam pola hh:mm a (12 jam dengan AM atau PM)
8. Pada `Global Settings > General Settings`, kembalikan Date Format ke "dd/MM/yy" dan Time Format ke "HH:mm", lalu simpan
9. Pada `Global Settings > Activity Log > Session`, muat ulang daftar lalu baca kolom Date baris yang sama
10. Verifikasi tanggal pada baris yang sama tampil dalam pola dd/MM/yy
11. Verifikasi jam pada baris yang sama tampil dalam pola HH:mm

### TC-AUTH-LP-136: Format tanggal dan jam pada User Log mengikuti General Settings

12. Pada browser kedua, buka `Global Settings > General Settings`, ubah Date Format menjadi "dd MMM yy" dan Time Format menjadi "hh:mm a", lalu simpan
13. Ganti akun: beralih ke browser pertama, lalu logout dari Portal — Product Hub
14. Buka halaman Login with Password
15. Catat penanda waktu sebelum login (baseline, S-12)
16. Isi Email "budisantoso+{runId}-040@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
17. Ganti akun: beralih ke browser kedua, buka `Global Settings > User > Detail > User Log` untuk user "Budi S", buka tab User Log, muat ulang daftar sampai baris baru yang lebih baru dari penanda waktu langkah 15 tampil, lalu baca kolom Date baris itu
18. Verifikasi tanggal pada kolom Date baris tersebut tampil dalam pola dd MMM yy
19. Verifikasi jam pada kolom Date baris tersebut tampil dalam pola hh:mm a (12 jam dengan AM atau PM)
20. Pada `Global Settings > General Settings`, kembalikan Date Format ke "dd/MM/yy" dan Time Format ke "HH:mm", lalu simpan
21. Pada `Global Settings > User > Detail > User Log` untuk user "Budi S", muat ulang lalu baca kolom Date baris yang sama
22. Verifikasi tanggal pada baris yang sama tampil dalam pola dd/MM/yy
23. Verifikasi jam pada baris yang sama tampil dalam pola HH:mm

### TC-AUTH-LP-137: Zona waktu General Settings menggeser jam yang tampil pada Activity Log Session

24. Ganti akun: beralih ke browser pertama, lalu logout dari Portal — Product Hub
25. Buka halaman Login with Password
26. Catat penanda waktu sebelum login (baseline, S-12)
27. Isi Email "budisantoso+{runId}-040@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
28. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, muat ulang daftar sampai baris baru untuk user "Budi S" yang lebih baru dari penanda waktu langkah 26 tampil, lalu baca jam kolom Date baris itu
29. Pada `Global Settings > General Settings`, ubah Time Zone menjadi "(UTC+08:00) Kuala Lumpur, Singapore, Makassar", lalu simpan
30. Pada `Global Settings > Activity Log > Session`, muat ulang daftar lalu baca jam kolom Date baris yang sama
31. Verifikasi jam pada langkah 30 lebih maju tepat 1 jam daripada jam pada langkah 28 untuk baris yang sama
32. Pada `Global Settings > General Settings`, kembalikan Time Zone ke "(UTC+07:00) Bangkok, Hanoi, Jakarta", lalu simpan

### TC-AUTH-LP-138: Waktu pada caption lock mengikuti Time Format dan zona waktu General Settings

33. Ganti akun: beralih ke browser pertama, lalu logout dari Portal — Product Hub
34. Bentuk lock 15 menit (web) untuk user "Nur Aini" lewat fixture BE (tepat sebelum login yang membutuhkannya)
35. Buka halaman Login with Password
36. Isi Email "nuraini+{runId}-040@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD_WRONG`, selesaikan reCAPTCHA, klik [Log in], lalu catat nilai {time} pada Alert
37. Verifikasi nilai {time} pada Alert berformat HH:mm sesuai Time Zone entitas
38. Verifikasi nilai {time} pada Alert hanya jam, tanpa tanggal
39. Ganti akun: beralih ke browser kedua, buka `Global Settings > General Settings`, ubah Time Format menjadi "hh:mm a", lalu simpan
40. Ganti akun: beralih ke browser pertama, muat ulang halaman Login with Password, lalu ulangi langkah 36 dan catat nilai {time}
41. Verifikasi nilai {time} pada Alert berformat hh:mm a sesuai Time Zone entitas
42. Verifikasi nilai {time} pada Alert hanya jam, tanpa tanggal
43. Ganti akun: beralih ke browser kedua, buka `Global Settings > General Settings`, kembalikan Time Format ke "HH:mm", lalu simpan

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah penghubung (S-03): langkah 13, 24, dan 33 mengakhiri sesi subjek dari TC sebelumnya agar browser pertama kembali guest (S-09); langkah 8, 20, 32, dan 43 memulihkan General Settings sebagai aksi tanpa `Verifikasi` (S-09); langkah 3, 15, dan 26 mencatat penanda waktu baseline sebelum tiap login yang barisnya dibaca (S-12).
- Spec ini memuat 43 langkah karena 4 TC masing-masing mengubah lalu memulihkan General Settings; tetap satu spec karena satu topik (format waktu mengikuti General Settings) dan harness yang sama.
- Pemecahan `Verifikasi` tanggal dan jam (langkah 6-7, 10-11, 18-19, 22-23) serta klausa format dan klausa "hanya jam, tanpa tanggal" pada TC-AUTH-LP-138 (langkah 37-38 dan 41-42) mengikuti S-01 (expected bermajemuk dipecah per klausa).
- Langkah "Ganti akun" memakai dua browser yang tetap terbuka (subjek guest dan aktor pengamat); sesi aktor dibuat di hook `before` (S-07).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 34 (fixture lock 15 menit) ditempatkan tepat sebelum login Nur Aini agar lock belum berakhir saat dibaca; langkah ini aksi tanpa `Verifikasi` (S-03).
- Teks Alert Danger lock 15 menit pada langkah 36 hanya konteks tempat nilai {time} dibaca (S-03); TC-AUTH-LP-138 tidak mengharapkan teks Alert itu, sehingga langkah 37, 38, 41, dan 42 hanya memverifikasi format {time}.
- Temuan untuk QA:
  - TC memakai nama tampilan tetap ("Budi S") untuk mencari baris log; nama itu tidak unik antar run atau antar spec. Spec memakai suite serial dan baris yang lebih baru dari penanda waktu sebelum login pada TC itu.
  - TC-AUTH-LP-138 hanya memverifikasi format {time}, bukan nilai jam terhadap waktu berakhirnya lock; "sesuai Time Zone entitas" tidak diberi nilai acuan.
  - TC-AUTH-LP-138 langkah TC 4 ("ulangi langkah 2") mengirim ulang password salah saat lock aktif; TC tidak menyebut apakah percobaan itu menambah baris log atau counter, sehingga asersi hanya pada format {time}.
  - Post Condition General Settings kembali ke nilai awal pada TC-AUTH-LP-135 (langkah spec 8), TC-AUTH-LP-136 (langkah spec 20), dan TC-AUTH-LP-137 (langkah spec 32) tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition itu hanya terpenuhi lewat aksi pemulihan pada langkah-langkah tersebut (hook `after` sebagai cadangan). TC-AUTH-LP-138 tidak punya Post Condition General Settings (kolom Post Condition "-"); langkah 43 hanya memulihkan Time Format yang diubah langkah 39 agar tidak bocor ke spec lain (S-09).
  - TC-AUTH-LP-135 dan TC-AUTH-LP-136 mengasumsikan nilai default "dd/MM/yy" dan "HH:mm" untuk pemulihan; TC tidak menyebut nilai awal entitas selain "default".
