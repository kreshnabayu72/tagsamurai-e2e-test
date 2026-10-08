---
id: TC-AUTH-LP-E2E-016-pencatatan-audit-log-login-berhasil-dan-agreement
title: Pencatatan login berhasil dan agreement pada Activity Log Session dan User Log
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-115
  - TC-AUTH-LP-116
  - TC-AUTH-LP-124
  - TC-AUTH-LP-125
  - TC-AUTH-LP-126
  - TC-AUTH-LP-127
  - TC-AUTH-LP-128
  - TC-AUTH-LP-129
  - TC-AUTH-LP-135
  - TC-AUTH-LP-136
  - TC-AUTH-LP-137
  - TC-AUTH-LP-162
coverage:
  web: automated
---

# Pencatatan login berhasil dan agreement pada Activity Log Session dan User Log

## Prerequisites

- Pengujian memerlukan dua sesi browser:
  - Sesi 1: User yang melakukan login di form Login with Password.
  - Sesi 2: Administrator dengan role Total Control (Global Settings) yang memantau surface `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`.
- User subjek: `budisantoso@qwertysystem.net` (nama Budi Santoso, Employee ID `EMP-1021`, Position `Finance Manager`, Division `Finance`), `suryadharma@qwertysystem.net` (dengan Agreement), `taufanaditya@qwertysystem.net` (dengan MFA), `winarsih@qwertysystem.net` (tanpa atribut organisasi).
- Fixture BE untuk mengirim request login tanpa header User-Agent.

## Test Steps

### Pencatatan login berhasil tanpa gate di kedua surface

1. Pada Sesi 1: Buka halaman Login with Password, masukkan email `budisantoso@qwertysystem.net` dan password `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
2. Verifikasi login berhasil dan browser menuju Portal — Product Hub
3. Pada Sesi 2: Buka halaman `Global Settings > Activity Log > Session` dan muat ulang tabel
4. Verifikasi terdapat tepat 1 baris entri baru untuk user "Budi S" dengan nilai kolom:
   - Date: waktu eksekusi login
   - User: "Budi S"
   - Employee ID: "EMP-1021"
   - Position: "Finance Manager"
   - Division: "Finance"
   - Activity: "Login"
   - Status: "Success" (teks biasa, bukan badge)
   - Note: "Login with password"
   - IP Address: alamat IP perangkat uji
   - Device / Browser: format platform misal "Chrome on Windows"
5. Pada Sesi 2: Arahkan kursor mouse (hover) ke nama user "Budi S"
6. Verifikasi tooltip menampilkan nama lengkap "Budi Santoso"
7. Pada Sesi 2: Buka halaman `Global Settings > User`, cari user "Budi Santoso", buka halaman Detail, lalu klik tab User Log
8. Verifikasi pada User Log terdapat tepat 1 baris entri baru dengan kolom Date, Activity "Login", Status "Success", Note "Login with password", IP Address, dan Device / Browser
9. Verifikasi kolom User, Employee ID, Position, dan Division tidak tampil di tabel User Log

### Penanganan nilai organisasi kosong

10. Pada Sesi 1: Login menggunakan user `winarsih@qwertysystem.net` yang tidak memiliki Employee ID, Position, dan Division
11. Pada Sesi 2: Buka `Global Settings > Activity Log > Session`
12. Verifikasi baris terbaru untuk "Winarsih K" menampilkan nilai "—" pada kolom Employee ID, Position, dan Division

### Snapshot integritas data log historis

13. Pada Sesi 2: Masuk ke `Global Settings > User`, edit user "Budi Santoso", ubah Position dari "Finance Manager" menjadi "HR Business Partner", lalu simpan
14. Pada Sesi 2: Kembali ke `Global Settings > Activity Log > Session`
15. Verifikasi baris log historis yang dibuat pada langkah 4 tetap menampilkan Position "Finance Manager" (snapshot lama tidak ikut berubah)
16. Pada Sesi 2: Kembalikan Position user "Budi Santoso" ke "Finance Manager"

### Pencatatan login dengan Agreement: ditulis sekali di titik akhir

17. Pada Sesi 1: Login menggunakan `suryadharma@qwertysystem.net` sampai layar Confirm to Continue tampil
18. Pada Sesi 2: Periksa `Global Settings > Activity Log > Session` saat layar Confirm to Continue masih terbuka
19. Verifikasi belum ada baris log baru untuk "Surya D"
20. Pada Sesi 1: Centang checkbox persetujuan lalu klik tombol [Continue ➔]
21. Pada Sesi 2: Muat ulang `Global Settings > Activity Log > Session` dan tab User Log milik Surya Dharma
22. Verifikasi tepat 1 baris baru tercipta dengan Status "Success" dan Note "Login with password" (tidak ada baris terpisah untuk langkah confirm agreement)

### Login dialihkan ke MFA belum dicatat Success pada langkah password

23. Pada Sesi 1: Login menggunakan `taufanaditya@qwertysystem.net` yang memicu MFA
24. Verifikasi browser dialihkan ke halaman MFA
25. Pada Sesi 2: Periksa `Global Settings > Activity Log > Session` dan User Log
26. Verifikasi tidak ada baris baru dengan Status "Success" maupun Note "Login with password", membuktikan pencatatan sukses baru dilakukan di titik final modul MFA

### Sinkronisasi Date/Time Format dan Timezone dari General Settings

27. Pada Sesi 2: Buka `Global Settings > General Settings`, ubah Date Format menjadi `dd MMM yy` dan Time Format menjadi `hh:mm a`, simpan
28. Pada Sesi 1: Lakukan login dengan user uji
29. Pada Sesi 2: Muat ulang `Global Settings > Activity Log > Session` dan User Log
30. Verifikasi kolom Date pada kedua surface menampilkan format tanggal `dd MMM yy` dan jam 12 jam `hh:mm a`
31. Pada Sesi 2: Ubah Time Zone di General Settings menjadi `(UTC+08:00)`, simpan
32. Verifikasi jam pada baris log yang sama bergeser maju tepat 1 jam
33. Kembalikan seluruh pengaturan General Settings ke default

### Nilai Device / Browser saat header User-Agent kosong

34. Pada Sesi 1: Kirim request login `winarsih@qwertysystem.net` dengan password `QaLogin#2026` tanpa header User-Agent (fixture BE)
35. Pada Sesi 2: Muat ulang `Global Settings > Activity Log > Session`
36. Verifikasi kolom Device / Browser pada baris terbaru untuk "Winarsih K" menampilkan nilai "—" (bukan teks format "[Browser] on [OS]" dan bukan sel kosong)

## Notes

- Sesuai `AUTHLP-LOGIC-04a`, 04b, 04c, status `Success` hanya dicatat satu kali di titik final keberhasilan autentikasi (setelah Agreement/MFA selesai).
- Data identitas organisasi pada log bersifat snapshot nilai saat login terjadi (`NC-15`, TC-AUTH-LP-128).
