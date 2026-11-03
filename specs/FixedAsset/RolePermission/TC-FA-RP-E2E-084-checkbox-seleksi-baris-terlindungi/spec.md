---
id: TC-FA-RP-E2E-084-checkbox-seleksi-baris-terlindungi
title: "Checkbox seleksi baris terlindungi"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-292
  - TC-FA-RP-293
  - TC-FA-RP-294
coverage:
  web: automated
---

# Checkbox seleksi baris terlindungi

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`; akun kedua untuk TC-FA-RP-294: Default User Admin Utama (Pre-setup #1), `defaultUser_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun ke Default User pada langkah 16 dan 17; hook `after` mengembalikan sesi ke akun default suite (Total Control Siti Rahmawati).
- Environment variable: `FA_TC_PASSWORD`, `FA_DU_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #1 (Admin Utama, Default User) dan pool #15 (Siti Rahmawati sebagai aktor dan Budi Santoso sebagai baris Standard). Admin Utama, Siti Rahmawati, dan Budi Santoso memegang Global Role `Manage Open API`; Budi Santoso tidak disebut TC sebagai baris Standard dan dipakai sebagai baris Standard pembanding (disiapkan lewat seed API di hook `before`, lihat Temuan untuk QA).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Global Role `Manage Open API` untuk Admin Utama, Siti Rahmawati, dan Budi Santoso), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-292: Checkbox seleksi baris Default User (Admin Utama) Disabled dan tidak ikut Select All

1. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
2. Hover checkbox baris Default User (Admin Utama)
3. Verifikasi checkbox baris Default User (Admin Utama) Disabled dengan tooltip `Default User cannot be modified.`
4. Centang satu baris Standard (Budi Santoso)
5. Klik `Select All` pada bar
6. Verifikasi counter seleksi tidak menghitung baris Default User (jumlah terpilih sama dengan jumlah baris Standard yang checkbox-nya aktif)
7. Verifikasi baris Default User tidak tercentang
8. Klik ikon `(✕)` pada bar untuk membatalkan seluruh seleksi

### TC-FA-RP-293: Checkbox seleksi baris sendiri (Siti Rahmawati) Disabled dan tidak ikut Select All

9. Hover checkbox baris sendiri (Siti Rahmawati)
10. Verifikasi checkbox baris sendiri (Siti Rahmawati) Disabled dengan tooltip `You can't manage your own account from here.`
11. Centang satu baris Standard (Budi Santoso)
12. Klik `Select All` pada bar
13. Verifikasi counter seleksi tidak menghitung baris sendiri (jumlah terpilih sama dengan jumlah baris Standard yang checkbox-nya aktif)
14. Verifikasi baris sendiri tidak tercentang
15. Klik ikon `(✕)` pada bar untuk membatalkan seluruh seleksi

### TC-FA-RP-294: Checkbox baris Default User saat aktor adalah Default User tetap Disabled

16. Ganti akun: Logout dari akun Total Control Siti Rahmawati
17. Login sebagai Default User Admin Utama
18. Buka Fixed Asset > Settings > Role & Permission > Tab System, klik Role Name `Manage Open API` pada section Global Role
19. Hover checkbox baris milik sendiri (Admin Utama)
20. Verifikasi checkbox baris Admin Utama Disabled dengan tooltip `Default User cannot be modified.`

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-292, TC-FA-RP-293, TC-FA-RP-294).
- Langkah penghubung (S-03): membuka Tab System dan Detail Role; membatalkan seleksi lewat `(✕)` antar blok (S-09); ganti akun pada langkah 16 dan 17 (Logout lalu login sebagai Default User).
- Temuan untuk QA:
  - TC-FA-RP-292 dan TC-FA-RP-293 menyebut "satu baris Standard" tanpa nama; spec memakai Budi Santoso (pool #15) sebagai baris Standard dan mengasumsikan penugasan `Manage Open API`.
  - Expected b TC-FA-RP-292 dan TC-FA-RP-293 ("Select All dan counter tidak menghitung baris tersebut") tidak menyebut angka counter; spec mengasersi jumlah terpilih sama dengan jumlah baris Standard dengan checkbox aktif.
