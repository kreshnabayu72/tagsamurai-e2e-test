---
id: TC-AUTH-LP-E2E-038-log-success-and-consent
title: "Pencatatan Log Consent Tidak Diberikan dan Login Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-114
  - TC-AUTH-LP-115
  - TC-AUTH-LP-116
coverage:
  web: automated
---

# Pencatatan Log Consent Tidak Diberikan dan Login Berhasil

## Prerequisites

- Mode: FE+BE.
- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dan dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Hook `before` login akun aktor di browser kedua (jendela terpisah dari browser pertama) dan sesi itu tetap terbuka sepanjang spec; browser pertama dipakai subjek sebagai guest.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua browser terpisah (subjek dan aktor pengamat log); reCAPTCHA mode uji di environment; fixture BE untuk menetapkan device terpercaya, tanpa pemicu MFA, dan versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui pada user yang membutuhkannya.
- Pemulihan state: sesi subjek yang aktif di browser pertama diakhiri di hook `after`.
- Pencarian baris log memakai nama tampilan dari TC ("Ratna D", "Budi S", "Surya D"; kolom User menampilkan nama singkat, bukan email) dan dibedakan antar run lewat baseline jumlah baris awal (langkah 1 dan 2, S-12). Suite berjalan serial (`parallel: false`), sehingga tidak ada spec lain yang menulis baris untuk nama yang sama selama spec ini berjalan.
- TC-AUTH-LP-114: Tanpa login (guest); browser web
- TC-AUTH-LP-114: User `Ratna Dewi` (`ratnadewi+{runId}-038@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya; tidak memicu MFA
- TC-AUTH-LP-114 data: Email `ratnadewi+{runId}-038@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-115: Tanpa login (guest); browser web
- TC-AUTH-LP-115: User `Budi Santoso` (`budisantoso+{runId}-038@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA
- TC-AUTH-LP-115 data: Email `budisantoso+{runId}-038@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-116: Tanpa login (guest); browser web
- TC-AUTH-LP-116: User `Surya Dharma` (`suryadharma+{runId}-038@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui; device terpercaya; tidak memicu MFA
- TC-AUTH-LP-116 data: Email `suryadharma+{runId}-038@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`

## Test Steps

### Jumlah baris log awal

1. Ganti akun: beralih ke browser kedua (sesi akun aktor Total Control Global Settings dari hook `before`), buka `Global Settings > Activity Log > Session`, lalu catat jumlah baris awal untuk user "Ratna D", "Budi S", dan "Surya D"
2. Buka `Global Settings > User > Detail > User Log` untuk masing-masing dari ketiga user itu, lalu catat jumlah baris awal

### TC-AUTH-LP-114: Pencatatan Continue tanpa centang pada layar Confirm to Continue

3. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
4. Isi Email "ratnadewi+{runId}-038@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in] sampai layar Confirm to Continue tampil
5. Biarkan checkbox unchecked, klik [Continue ➔]
6. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Ratna D" tampil
7. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Ratna D", Activity "Login", Status "Failed" (teks biasa), Note "Consent not given"
8. Verifikasi tepat 0 baris dengan Note "Login with password" untuk percobaan ini pada `Global Settings > Activity Log > Session`: jumlah baris untuk user "Ratna D" bertambah tepat 1 dibandingkan jumlah awal pada langkah 1, yaitu baris Note "Consent not given" saja
9. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
10. Buka `Global Settings > User > Detail > User Log` untuk user "Ratna D", buka tab User Log, lalu cari baris terbaru
11. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Failed", Note "Consent not given"
12. Verifikasi tepat 0 baris dengan Note "Login with password" untuk percobaan ini pada User Log: jumlah baris untuk user "Ratna D" bertambah tepat 1 dibandingkan jumlah awal pada langkah 2, yaitu baris Note "Consent not given" saja
13. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji

### TC-AUTH-LP-115: Pencatatan login berhasil tanpa gate

14. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
15. Isi Email "budisantoso+{runId}-038@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in] sampai Portal — Product Hub tampil
16. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Budi S" tampil
17. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Budi S", Activity "Login", Status "Success" (teks biasa), Note "Login with password"
18. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
19. Buka `Global Settings > User > Detail > User Log` untuk user "Budi S", buka tab User Log, lalu cari baris terbaru
20. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Success", Note "Login with password"
21. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji

### TC-AUTH-LP-116: Pencatatan login berhasil dengan Agreement ditulis sekali di titik akhir

22. Ganti akun: beralih ke browser pertama, lalu logout dari Portal — Product Hub
23. Buka halaman Login with Password
24. Isi Email "suryadharma+{runId}-038@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD`, selesaikan reCAPTCHA, klik [Log in] sampai layar Confirm to Continue tampil
25. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar untuk user "Surya D" saat layar Confirm to Continue masih terbuka
26. Verifikasi tidak ada baris baru untuk user "Surya D" dibandingkan jumlah awal pada langkah 1 (sebelum Continue)
27. Ganti akun: beralih ke browser pertama (layar Confirm to Continue masih terbuka), centang checkbox persetujuan, lalu klik [Continue ➔]
28. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Surya D" tampil
29. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Surya D", Activity "Login", Status "Success" (teks biasa), Note "Login with password"
30. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
31. Buka `Global Settings > User > Detail > User Log` untuk user "Surya D", buka tab User Log, lalu cari baris terbaru
32. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Success", Note "Login with password"
33. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji
34. Verifikasi setelah Continue tidak ada baris terpisah untuk konfirmasi Agreement, hanya 1 baris dengan Note "Login with password"

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah penghubung (S-03): langkah 1 dan 2 mencatat jumlah baris awal sebagai acuan "tepat 1 baris baru"; langkah 22 mengakhiri sesi Budi Santoso dari TC-AUTH-LP-115 sebelum TC-AUTH-LP-116 memakai browser pertama sebagai guest (S-09).
- Expected c TC-AUTH-LP-114 (tepat 0 baris dengan Note "Login with password" untuk percobaan ini; langkah 8 dan 12) dan Expected c TC-AUTH-LP-116 (belum ada baris baru sebelum Continue; langkah 26) adalah asersi jumlah atau state dengan baseline jumlah baris awal (langkah 1 dan 2, S-12), bukan kelas g: kedua TC punya aksi fungsional (Continue tanpa centang, lalu Continue dengan centang) dalam alurnya (konvensi §3 prinsip 13g).
- Langkah "Ganti akun" memakai dua browser yang tetap terbuka (subjek guest dan aktor pengamat); sesi aktor dibuat di hook `before` (S-07).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pencatatan login MFA tertunda (TC-AUTH-LP-124) diuji di spec `TC-AUTH-LP-E2E-043-absence-state-based`.
- Temuan untuk QA:
  - TC-AUTH-LP-116 langkah 3 meminta mencatat jumlah baris saat layar Confirm to Continue terbuka tetapi tidak menyebut baseline-nya; spec memakai jumlah baris awal dari langkah 1.
  - TC memakai nama tampilan tetap ("Ratna D", "Budi S", "Surya D") untuk mencari baris log; nama itu tidak unik antar run atau antar spec. Spec memakai baseline (S-12) dan suite serial.
  - Nilai "terisi sesuai perangkat uji" pada IP Address dan Device / Browser tidak menyebut nilai pasti; asersi memeriksa kolom terisi dan sesuai perangkat runner.
