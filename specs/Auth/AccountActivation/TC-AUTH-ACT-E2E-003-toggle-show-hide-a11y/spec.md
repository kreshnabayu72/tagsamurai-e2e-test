---
id: TC-AUTH-ACT-E2E-003-toggle-show-hide-a11y
title: "Toggle Show/Hide Password dan Aksesibilitas Form Set Password"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-19
  - TC-AUTH-ACT-20
  - TC-AUTH-ACT-21
  - TC-AUTH-ACT-60
  - TC-AUTH-ACT-61
  - TC-AUTH-ACT-62
coverage:
  web: automated
---

# Toggle Show/Hide Password dan Aksesibilitas Form Set Password

## Prerequisites

- Konteks browser: spec berjalan di konteks browser baru tanpa sesi login (jendela privat), sesuai precondition "Tanpa login" semua TC di spec ini.
- Seeding: setiap user Pending Activation dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`). Link aktivasi (token Active) diambil dari respons seeding API. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}` (contoh `budiaditya+{runId}-003@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: hover pada ikon toggle untuk membaca tooltip; navigasi keyboard dengan Tab; inspeksi atribut aksesibilitas lewat DOM atau screen reader.
- TC-AUTH-ACT-19: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-19: User `Yoga Mulyadi` (`yogamulyadi+{runId}-003@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-19 data: Password: `Aman#Sandi8`; Confirm Password: `Aman#Sandi8`
- TC-AUTH-ACT-20: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-20: User `Sari Wulandari` (`sariwulandari+{runId}-003@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-20 data: Password: `Aman#Sandi8`; Confirm Password: `Aman#Sandi8`
- TC-AUTH-ACT-21: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-21: User `Eko Kusuma` (`ekokusuma+{runId}-003@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-60: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-60: User `Sari Aditya` (`sariaditya+{runId}-003@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-61: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-61: User `Eko Lestari` (`ekolestari+{runId}-003@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-62: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-62: User `Ratna Saputra` (`ratnasaputra+{runId}-003@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-62 data: Password: `Abcdefg1`

## Test Steps

### TC-AUTH-ACT-19: Toggle show/hide pada field Password menampilkan dan menyembunyikan teks tanpa mengubah field Confirm Password

1. Buka link aktivasi user `Yoga Mulyadi` di browser → halaman `Auth > Account Activation > Set Password` tampil
2. Ketik `Aman#Sandi8` di field Password dan `Aman#Sandi8` di field Confirm Password
3. Klik ikon toggle di field Password
4. Verifikasi Teks field Password terlihat sebagai `Aman#Sandi8`; teks field Confirm Password tetap tersembunyi (masked)
5. Klik ikon toggle di field Password sekali lagi
6. Verifikasi Teks field Password kembali tersembunyi (masked); field Confirm Password tidak berubah

### TC-AUTH-ACT-20: Toggle show/hide pada field Confirm Password bekerja independen dari field Password

7. Buka link aktivasi user `Sari Wulandari` di browser → halaman `Auth > Account Activation > Set Password` tampil
8. Ketik `Aman#Sandi8` di field Password dan `Aman#Sandi8` di field Confirm Password
9. Klik ikon toggle di field Confirm Password
10. Verifikasi Teks field Confirm Password terlihat sebagai `Aman#Sandi8`; teks field Password tetap tersembunyi (masked)
11. Klik ikon toggle di field Confirm Password sekali lagi
12. Verifikasi Teks field Confirm Password kembali tersembunyi (masked); field Password tidak berubah

### TC-AUTH-ACT-21: Ikon dan tooltip toggle show/hide sesuai state field

13. Buka link aktivasi user `Eko Kusuma` di browser → halaman `Auth > Account Activation > Set Password` tampil
14. Hover ikon toggle di field Password saat teks tersembunyi
15. Verifikasi Ikon `EyeLine` dengan tooltip "Show password" (field tersembunyi)
16. Klik ikon toggle di field Password, lalu hover ikon yang sama saat teks terlihat
17. Verifikasi Ikon `EyeOffLine` dengan tooltip "Hide password" (field terlihat)
18. Ulangi hover pada ikon toggle di field Confirm Password dalam kedua state
19. Verifikasi Field Confirm Password menampilkan pasangan ikon dan tooltip yang sama dengan field Password pada tiap state

### TC-AUTH-ACT-60: Accessibility — ikon toggle show/hide pada kedua field dapat difokuskan dengan keyboard

20. Buka link aktivasi user `Sari Aditya` di browser → halaman `Auth > Account Activation > Set Password` tampil
21. Tekan Tab berulang sampai fokus mencapai ikon toggle di field Password
22. Tekan Tab sampai fokus mencapai ikon toggle di field Confirm Password
23. Verifikasi Ikon toggle di field Password menerima fokus keyboard dan menampilkan tooltip "Show password"
24. Verifikasi Ikon toggle di field Confirm Password menerima fokus keyboard dan menampilkan tooltip "Show password"

### TC-AUTH-ACT-61: Accessibility — inline error berupa teks dan terhubung ke field-nya

25. Buka link aktivasi user `Eko Lestari` di browser → halaman `Auth > Account Activation > Set Password` tampil
26. Klik button "Set Password" dengan kedua field kosong
27. Periksa atribut aksesibilitas kedua field dengan screen reader atau inspeksi DOM
28. Verifikasi Pesan error tampil sebagai teks (bukan hanya perubahan warna)
29. Verifikasi Field Password terhubung ke "Password must not be empty" dan field Confirm Password terhubung ke "Confirm password must not be empty" (dibacakan pembaca layar saat field fokus)

### TC-AUTH-ACT-62: Accessibility — status checklist dibedakan oleh ikon, bukan hanya warna

30. Buka link aktivasi user `Ratna Saputra` di browser → halaman `Auth > Account Activation > Set Password` tampil
31. Ketik `Abcdefg1` di field Password
32. Amati ikon di setiap baris checklist
33. Verifikasi Baris yang terpenuhi menampilkan ikon ✓ dan baris yang belum terpenuhi menampilkan ikon ○ (status terbaca tanpa bergantung warna)

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
