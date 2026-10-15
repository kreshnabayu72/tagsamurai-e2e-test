---
id: TC-AUTH-LP-E2E-036-log-lock-stages
title: "Pencatatan Log Tahap Lock 15 Menit, 1 Jam, dan Requires Reset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-110
  - TC-AUTH-LP-111
  - TC-AUTH-LP-112
coverage:
  web: automated
---

# Pencatatan Log Tahap Lock 15 Menit, 1 Jam, dan Requires Reset

## Prerequisites

- Mode: FE+BE.
- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dan dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Hook `before` login akun aktor di browser kedua (jendela terpisah dari browser pertama) dan sesi itu tetap terbuka sepanjang spec; browser pertama dipakai subjek sebagai guest.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD_WRONG`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua browser terpisah (subjek dan aktor pengamat log); reCAPTCHA mode uji di environment; fixture BE untuk menetapkan hitungan gagal hari ini (web) pada tiap user subjek tanpa menghasilkan baris log tambahan.
- TC-AUTH-LP-110: Tanpa login (guest); browser web
- TC-AUTH-LP-110: User `Nur Aini` (`nuraini+{runId}-036@qwertysystem.net`) berstatus Activated dan Active, sudah 2 kali salah password hari ini (web)
- TC-AUTH-LP-110 data: Email `nuraini+{runId}-036@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-111: Tanpa login (guest); browser web
- TC-AUTH-LP-111: User `Oka Pratama` (`okapratama+{runId}-036@qwertysystem.net`) berstatus Activated dan Active, sudah 5 kali salah password hari ini dan tidak sedang terkunci (web)
- TC-AUTH-LP-111 data: Email `okapratama+{runId}-036@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-112: Tanpa login (guest); browser web
- TC-AUTH-LP-112: User `Prita Sari` (`pritasari+{runId}-036@qwertysystem.net`) berstatus Activated dan Active, sudah 8 kali salah password hari ini dan tidak sedang terkunci (web)
- TC-AUTH-LP-112 data: Email `pritasari+{runId}-036@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD_WRONG`

## Test Steps

### Jumlah baris log awal

1. Ganti akun: beralih ke browser kedua (sesi akun aktor Total Control Global Settings dari hook `before`), buka `Global Settings > Activity Log > Session`, lalu catat jumlah baris awal untuk user "Nur A", "Oka P", dan "Prita S"
2. Buka `Global Settings > User > Detail > User Log` untuk masing-masing dari ketiga user itu, lalu catat jumlah baris awal

### TC-AUTH-LP-110: Pencatatan lock 15 menit pada kegagalan password ke-3

3. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
4. Isi Email "nuraini+{runId}-036@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD_WRONG`, selesaikan reCAPTCHA, klik [Log in]
5. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Nur A" tampil
6. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Nur A", Activity "Login", Status "Failed" (teks biasa), Note "Locked 15 minutes"
7. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
8. Buka `Global Settings > User > Detail > User Log` untuk user "Nur A", buka tab User Log, lalu cari baris terbaru
9. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Failed", Note "Locked 15 minutes"
10. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji
11. Verifikasi kegagalan ke-3 hanya menghasilkan 1 baris dengan Note "Locked 15 minutes" di kedua surface
12. Verifikasi tidak ada baris tambahan dengan Note "Incorrect password" untuk percobaan yang sama di kedua surface

### TC-AUTH-LP-111: Pencatatan lock 1 jam pada kegagalan password ke-6

13. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
14. Isi Email "okapratama+{runId}-036@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD_WRONG`, selesaikan reCAPTCHA, klik [Log in]
15. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Oka P" tampil
16. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Oka P", Activity "Login", Status "Failed" (teks biasa), Note "Locked 1 hour"
17. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
18. Buka `Global Settings > User > Detail > User Log` untuk user "Oka P", buka tab User Log, lalu cari baris terbaru
19. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Failed", Note "Locked 1 hour"
20. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji
21. Verifikasi kegagalan ke-6 hanya menghasilkan 1 baris dengan Note "Locked 1 hour" di kedua surface
22. Verifikasi tidak ada baris tambahan dengan Note "Incorrect password" untuk percobaan yang sama di kedua surface

### TC-AUTH-LP-112: Pencatatan Requires Reset pada kegagalan password ke-9

23. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
24. Isi Email "pritasari+{runId}-036@qwertysystem.net" dan Password `Spectra.env.LP_PASSWORD_WRONG`, selesaikan reCAPTCHA, klik [Log in]
25. Ganti akun: beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, lalu muat ulang daftar sampai baris terbaru untuk user "Prita S" tampil
26. Verifikasi tepat 1 baris baru pada `Global Settings > Activity Log > Session`: User "Prita S", Activity "Login", Status "Failed" (teks biasa), Note "Locked requires reset"
27. Verifikasi IP Address dan Device / Browser pada baris itu terisi sesuai perangkat uji
28. Buka `Global Settings > User > Detail > User Log` untuk user "Prita S", buka tab User Log, lalu cari baris terbaru
29. Verifikasi tepat 1 baris baru pada User Log: Activity "Login", Status "Failed", Note "Locked requires reset"
30. Verifikasi IP Address dan Device / Browser pada baris User Log itu terisi sesuai perangkat uji
31. Verifikasi kegagalan ke-9 hanya menghasilkan 1 baris dengan Note "Locked requires reset" di kedua surface
32. Verifikasi tidak ada baris tambahan dengan Note "Incorrect password" untuk percobaan yang sama di kedua surface

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Langkah penghubung (S-03): langkah 1 dan 2 mencatat jumlah baris awal sebagai acuan "tepat 1 baris baru".
- Klausa "tidak ada baris tambahan dengan Note "Incorrect password" untuk percobaan yang sama" (langkah 12, 22, 32) diperlakukan sebagai asersi jumlah ("hanya 1 baris untuk percobaan ini"), bukan asersi absence kelas g (konvensi §3 prinsip 13g), karena membuktikan satu percobaan menghasilkan tepat satu baris.
- Hitungan gagal awal di-seed lewat fixture BE (bukan dengan mengulang percobaan salah) supaya baris log tambahan dari percobaan sebelumnya tidak mengacaukan hitungan "tepat 1 baris baru"; TC sumber hanya menyebut "sudah N kali salah password hari ini".
- Langkah "Ganti akun" memakai dua browser yang tetap terbuka (subjek guest dan aktor pengamat); sesi aktor dibuat di hook `before` (S-07).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - Nilai "terisi sesuai perangkat uji" pada IP Address dan Device / Browser tidak menyebut nilai pasti; asersi memeriksa kolom terisi dan sesuai perangkat runner.
  - TC-AUTH-LP-111 dan TC-AUTH-LP-112 tidak menyebut cara menghasilkan hitungan gagal awal (5 dan 8 kali) selain "sudah N kali"; spec mengasumsikan fixture BE.
