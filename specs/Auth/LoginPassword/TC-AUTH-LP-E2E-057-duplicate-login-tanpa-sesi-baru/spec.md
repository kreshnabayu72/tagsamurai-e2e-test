---
id: TC-AUTH-LP-E2E-057-duplicate-login-tanpa-sesi-baru
title: "Password Benar saat Sesi Web Lain Aktif: Duplicate Login tanpa Sesi Baru dan tanpa Log Success"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-164
coverage:
  web: automated
---

# Password Benar saat Sesi Web Lain Aktif: Duplicate Login tanpa Sesi Baru dan tanpa Log Success

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`) dan dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Aktor observer log: akun aktor Total Control (Global Settings) di atas login di browser kedua pada hook `before`; browser kedua tetap terbuka sepanjang spec dan ditutup di hook `after`. Browser pertama dipakai subjek sebagai guest.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password tidak ditulis di spec atau fixture; nilai password yang ditulis TC-AUTH-LP-164 diisikan lewat `LP_PASSWORD`.
- Kemampuan teknis: dua browser terpisah (subjek guest dan aktor pengamat log); reCAPTCHA mode uji di environment; pengamatan respons jaringan browser untuk membaca body respons API login; pembacaan cookie browser pertama (cookie `sid`); kemampuan membaca daftar sesi milik satu user beserta statusnya (API sesi atau DB lingkungan uji; bentuk pastinya ditentukan di tahap script) untuk Expected b; fixture BE sesi aktif yang sudah ada.
- TC-AUTH-LP-164: User `Budi Santoso` (`budisantoso+{runId}-057@qwertysystem.net`) berstatus Activated dan Active; sudah memiliki sesi aktif di web dari login sebelumnya (fixture BE di hook `before`: sesi `active` platform `web`, belum `expires_at`, tidak dipegang browser pertama maupun browser kedua); device terpercaya; tidak ada gate Agreement dan MFA; versi Privacy Policy terakhir yang disetujui sama dengan versi aktif. Browser pertama guest tanpa sesi aktif.
- TC-AUTH-LP-164 data: Email `budisantoso+{runId}-057@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- Pencarian baris log memakai nama tampilan dari TC ("Budi S"; kolom User menampilkan nama singkat, bukan email) dan dibedakan antar run lewat baseline jumlah baris awal (langkah 1, S-12). Suite berjalan serial (`parallel: false`), sehingga tidak ada spec lain yang menulis baris untuk nama yang sama selama spec ini berjalan.
- Pemulihan state: sesi fixture milik user subjek diakhiri bersama penghapusan user di hook `after`.

## Test Steps

### Jumlah baris log awal

1. Ganti akun: beralih ke browser kedua (sesi akun aktor Total Control Global Settings dari hook `before`), buka `Global Settings > Activity Log > Session`, lalu catat jumlah baris awal untuk user "Budi S"

### TC-AUTH-LP-164: Password benar pada akun yang sudah punya sesi aktif di platform yang sama menghasilkan duplicate login tanpa sesi baru dan tanpa log Success

2. Ganti akun: beralih ke browser pertama (subjek guest), lalu buka halaman Login with Password
3. Isi field Email dengan "budisantoso+{runId}-057@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
4. Selesaikan reCAPTCHA
5. Klik [Log in]
6. Verifikasi respons API login berisi `outcome: duplicate_detected`
7. Verifikasi respons API login memuat `existingSession` dengan field `platform`, `deviceInfo`, `lastActivityAt`, dan `existingSessionId`
8. Verifikasi browser tidak menuju Portal — Product Hub
9. Verifikasi cookie `sid` baru tidak diset di browser pertama
10. Verifikasi tidak ada sesi baru untuk `Budi Santoso` dan sesi web aktif sebelumnya (fixture) tetap berstatus `active`
11. Ganti akun: beralih ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, lalu cari baris user "Budi S"
12. Verifikasi tepat 0 baris baru Activity "Login", Status "Success", Note "Login with password" untuk percobaan ini dibanding jumlah baris awal langkah 1

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Kelas harness c (multi-konteks: sesi web lama milik user dari fixture BE dan percobaan login baru di browser pertama, ditambah browser kedua sebagai pengamat log). Pola spec mengikuti `TC-AUTH-OTP-E2E-041-duplicate-login-attempt` untuk Login with OTP.
- Langkah penghubung (S-03): langkah 1 mencatat jumlah baris awal sebagai acuan langkah 12; langkah 2 dan 11 berpindah antara browser subjek dan browser pengamat (S-07), ditulis sebagai aksi tanpa `Verifikasi`.
- Asersi "tepat 0 baris Success" pada Expected c (langkah 12) adalah asersi jumlah atau state atas percobaan login yang berhenti di duplicate detection (konvensi bagian 3: asersi jumlah atau state bukan kelas g; S-05 keputusan 2026-11-05), bukan asersi absence untuk kondisi yang ditolak tanpa aksi: alurnya punya aksi login fungsional yang menghasilkan `duplicate_detected` dan memakai baseline jumlah baris dari langkah 1 (S-12). Karena itu asersi tetap di spec ini dan tidak dipindah ke spec absence `TC-AUTH-LP-E2E-043-absence-state-based`.
- Isi dialog Duplicate Login Attempt, pilihan Confirm atau Cancel, dan perilaku sesi lama dimiliki fitur session-management; spec ini hanya mengasersi respons login, tidak adanya sesi baru, dan pencatatan Login with password.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - Expected b ("tidak ada sesi baru dibuat; sesi aktif sebelumnya tetap") tidak menyebut cara sesi diamati; spec memerlukan kemampuan membaca sesi per user (API sesi atau DB) tanpa menyebut endpoint karena tidak tertulis di TC.
  - Langkah 3 TC ("Periksa respons API login (Network) dan halaman yang tampil") tidak menyebut layar yang tampil sesudah `duplicate_detected` (dialog Duplicate Login Attempt atau tetap di halaman login); spec hanya mengasersi browser tidak menuju Portal — Product Hub.
  - TC memakai nama tampilan tetap ("Budi S") untuk mencari baris log; nama itu tidak unik antar run atau antar spec. Spec memakai baseline (S-12) dan suite serial.
