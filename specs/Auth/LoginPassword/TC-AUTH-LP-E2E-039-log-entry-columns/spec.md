---
id: TC-AUTH-LP-E2E-039-log-entry-columns
title: "Kolom Entri Login pada Activity Log Session dan User Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-125
  - TC-AUTH-LP-126
  - TC-AUTH-LP-127
  - TC-AUTH-LP-129
  - TC-AUTH-LP-128
  - TC-AUTH-LP-162
coverage:
  web: automated
---

# Kolom Entri Login pada Activity Log Session dan User Log

## Prerequisites

- Mode: FE+BE.
- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dan dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Hook `before` login akun aktor di browser kedua (jendela terpisah dari browser pertama) dan sesi itu tetap terbuka sepanjang spec; browser pertama dipakai subjek sebagai guest.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua browser terpisah (subjek dan aktor pengamat log); browser subjek Chrome pada Windows (asersi Device / Browser "Chrome on Windows"); reCAPTCHA mode uji di environment; fixture BE untuk menetapkan device terpercaya dan tanpa pemicu Agreement dan MFA pada user subjek; kemampuan mengirim request login ke server tanpa header User-Agent (TC-AUTH-LP-162; disediakan fixture BE, tanpa endpoint khusus yang dikarang, dan memenuhi reCAPTCHA di sisi fixture).
- Pencarian baris log memakai nama tampilan dari TC ("Budi S", "Winarsih K"; kolom User menampilkan nama singkat, bukan email) dan membaca "baris terbaru" sesudah aksi login pada langkah itu. Suite berjalan serial (`parallel: false`), sehingga tidak ada spec lain yang menulis baris untuk nama yang sama selama spec ini berjalan; asersi baris hanya menghitung baris yang lebih baru dari penanda waktu yang dicatat sebelum login pada TC itu (S-12), dan daftar dimuat ulang sampai baris baru tampil karena penulisan log bisa terlambat (NC-18).
- Master data: Position `HR Business Partner` tersedia di `Global Settings > Master Reference > Position`.
- State global dan pemulihan: Position user Budi Santoso diubah di TC-AUTH-LP-128 dan dikembalikan ke `Finance Manager` pada langkah akhir TC itu; hook `after` mengembalikannya sebagai cadangan.
- TC-AUTH-LP-125: Tanpa login (guest); browser web (Chrome pada Windows)
- TC-AUTH-LP-125: User `Budi Santoso` (`budisantoso+{runId}-039@qwertysystem.net`; Employee ID `EMP-1021`, Position `Finance Manager`, Division `Finance`) berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA
- TC-AUTH-LP-125 data: Email `budisantoso+{runId}-039@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-126: Tanpa login (guest); browser web (Chrome pada Windows)
- TC-AUTH-LP-126: User `Budi Santoso` (`budisantoso+{runId}-039@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA
- TC-AUTH-LP-126 data: Email `budisantoso+{runId}-039@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-127: Tanpa login (guest); browser web
- TC-AUTH-LP-127: User `Winarsih Kusuma` (`winarsih+{runId}-039@qwertysystem.net`) berstatus Activated dan Active tanpa Employee ID, Position, dan Division; device terpercaya; tidak ada gate Agreement dan MFA
- TC-AUTH-LP-127 data: Email `winarsih+{runId}-039@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-129: User `Budi Santoso` (`budisantoso+{runId}-039@qwertysystem.net`) sudah memiliki baris login di Activity Log Session (dihasilkan TC-AUTH-LP-125 dan TC-AUTH-LP-126 pada spec ini)
- TC-AUTH-LP-128: Tanpa login (guest); browser web
- TC-AUTH-LP-128: User `Budi Santoso` (`budisantoso+{runId}-039@qwertysystem.net`; Position `Finance Manager`) berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA; Position `HR Business Partner` tersedia
- TC-AUTH-LP-128 data: Email `budisantoso+{runId}-039@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-162: User `Winarsih Kusuma` (`winarsih+{runId}-039@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA; request login dikirim tanpa header User-Agent (fixture BE)
- TC-AUTH-LP-162 data: Email `winarsih+{runId}-039@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`; User-Agent: kosong

## Test Steps

### TC-AUTH-LP-125: Kolom entri login pada Activity Log Session

1. Buka halaman Login with Password (browser pertama, subjek guest)
2. Catat penanda waktu sebelum login (baseline, S-12)
3. Isi Email "budisantoso+{runId}-039@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
4. Ganti akun: beralih ke browser kedua (sesi akun aktor dari hook `before`), buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris baru untuk user "Budi S" yang lebih baru dari penanda waktu langkah 2 tampil
5. Verifikasi kolom Date baris baru itu menampilkan waktu percobaan login
6. Verifikasi kolom User "Budi S", Employee ID "EMP-1021", Position "Finance Manager", dan Division "Finance"
7. Verifikasi kolom Activity "Login", Status "Success" (teks biasa, bukan badge), dan Note "Login with password"
8. Verifikasi kolom IP Address menampilkan alamat IP perangkat uji dan kolom Device / Browser "Chrome on Windows"

### TC-AUTH-LP-126: Kolom entri login pada User Log

9. Ganti akun: beralih ke browser pertama, lalu logout dari Portal — Product Hub
10. Buka halaman Login with Password
11. Catat penanda waktu sebelum login (baseline, S-12)
12. Isi Email "budisantoso+{runId}-039@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
13. Ganti akun: beralih ke browser kedua, buka `Global Settings > User > Detail > User Log` untuk user "Budi S", buka tab User Log, lalu muat ulang daftar sampai baris baru yang lebih baru dari penanda waktu langkah 11 tampil
14. Verifikasi baris baru itu menampilkan kolom Date, Activity "Login", Status "Success", dan Note "Login with password"
15. Verifikasi kolom IP Address dan Device / Browser "Chrome on Windows" pada baris baru itu
16. Verifikasi kolom User, Employee ID, Position, dan Division tidak tampil di User Log

### TC-AUTH-LP-127: Kolom identitas organisasi kosong pada entri login Activity Log Session

17. Ganti akun: beralih ke browser pertama, lalu logout dari Portal — Product Hub
18. Buka halaman Login with Password
19. Catat penanda waktu sebelum login (baseline, S-12)
20. Isi Email "winarsih+{runId}-039@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
21. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris baru untuk user "Winarsih K" yang lebih baru dari penanda waktu langkah 19 tampil
22. Verifikasi kolom Employee ID "—", Position "—", dan Division "—" pada baris baru itu

### TC-AUTH-LP-129: Hover kolom User pada Activity Log Session menampilkan nama lengkap

23. Pada browser kedua, buka `Global Settings > Activity Log > Session`
24. Arahkan kursor ke sel User "Budi S" pada baris login user tersebut
25. Verifikasi tooltip menampilkan nama lengkap "Budi Santoso"

### TC-AUTH-LP-128: Entri log login lama tidak berubah setelah data user diubah

26. Ganti akun: beralih ke browser pertama, lalu logout dari Portal — Product Hub
27. Buka halaman Login with Password
28. Catat penanda waktu sebelum login (baseline, S-12)
29. Isi Email "budisantoso+{runId}-039@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
30. Ganti akun: beralih ke browser kedua, buka `Global Settings > User`, ubah Position user "Budi Santoso" menjadi "HR Business Partner", lalu simpan
31. Buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris login untuk user "Budi S" yang lebih baru dari penanda waktu langkah 28 (dibuat pada langkah 29) tampil
32. Verifikasi baris login dari langkah 29 tetap menampilkan Position "Finance Manager" (nilai saat percobaan login), bukan "HR Business Partner"
33. Pada `Global Settings > User`, kembalikan Position user "Budi Santoso" ke "Finance Manager", lalu simpan

### TC-AUTH-LP-162: Device / Browser tampil — bila User-Agent kosong pada entri login Activity Log Session

34. Catat penanda waktu sebelum login (baseline, S-12)
35. Kirim login dengan Email "winarsih+{runId}-039@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD` tanpa header User-Agent (fixture BE)
36. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris baru untuk user "Winarsih K" yang lebih baru dari penanda waktu langkah 34 tampil
37. Verifikasi kolom Device / Browser menampilkan "—" (bukan teks "[Browser] on [OS]" dan bukan sel kosong)

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Urutan dalam spec: asersi tampilan (TC-AUTH-LP-125, 126, 127, 129) di depan, TC-AUTH-LP-128 yang mengubah data user sesudahnya, dan TC-AUTH-LP-162 di akhir. TC-AUTH-LP-129 ditempatkan sebelum TC-AUTH-LP-128 karena TC-AUTH-LP-128 mengubah Position user yang barisnya dicek.
- Langkah penghubung (S-03): langkah 9, 17, dan 26 mengakhiri sesi subjek dari TC sebelumnya agar browser pertama kembali guest (S-09); langkah 2, 11, 19, 28, dan 34 mencatat penanda waktu baseline sebelum tiap login (S-12); langkah 33 memulihkan Position user Budi Santoso.
- Spec ini memakai satu user Budi Santoso untuk TC-AUTH-LP-125, 126, 128, dan 129 serta satu user Winarsih Kusuma untuk TC-AUTH-LP-127 dan 162; setiap TC menambah baris login baru sehingga asersi memakai baris yang lebih baru dari penanda waktu.
- Langkah "Ganti akun" memakai dua browser yang tetap terbuka (subjek guest dan aktor pengamat); sesi aktor dibuat di hook `before` (S-07).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- P-2: request login tanpa header User-Agent pada TC-AUTH-LP-162 (langkah 35, fixture BE atau request langsung) adalah pemicu kelas a yang hanya dipakai untuk mencapai state; request itu bukan objek asersi. Objek asersi adalah kolom Device / Browser "—" pada baris log (langkah 37). Pemakaian pemicu kelas a ini tercakup P-2 di konvensi §3; spec kelas a terpisah untuk perilaku request tanpa User-Agent tidak diperlukan karena TC tidak mengharapkan hasil apa pun di sisi request itu.
- Temuan untuk QA:
  - TC memakai nama tampilan tetap ("Budi S", "Winarsih K") untuk mencari baris log; nama itu tidak unik antar run atau antar spec. Spec memakai suite serial dan "baris terbaru" sesudah login pada langkah itu.
  - TC-AUTH-LP-125 dan TC-AUTH-LP-126 mengharapkan Device / Browser "Chrome on Windows"; nilai ini hanya benar bila runner memakai Chrome pada Windows (dicatat di Prerequisites).
  - TC-AUTH-LP-162 langkah 1 ("Kirim login ... tanpa header User-Agent (fixture BE)") tidak menjelaskan cara memenuhi reCAPTCHA pada request langsung ke server (TC-AUTH-LP-139 menyatakan web tanpa token ditolak); spec menuliskannya sebagai kemampuan fixture BE tanpa mengarang mekanisme.
  - TC-AUTH-LP-128 Post Condition (Position user Budi Santoso kembali "Finance Manager") tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition itu hanya terpenuhi lewat aksi pemulihan di langkah 33 (hook `after` sebagai cadangan).
  - Tanggal dan jam kolom Date pada TC-AUTH-LP-125 tidak diberi nilai acuan; asersi hanya memeriksa kolom menampilkan waktu percobaan login.
