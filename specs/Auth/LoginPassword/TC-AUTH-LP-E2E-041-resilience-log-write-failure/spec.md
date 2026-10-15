---
id: TC-AUTH-LP-E2E-041-resilience-log-write-failure
title: "Ketahanan Login terhadap Kegagalan Layanan Penulisan Log"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-130
  - TC-AUTH-LP-153
coverage:
  web: automated
---

# Ketahanan Login terhadap Kegagalan Layanan Penulisan Log

## Prerequisites

- Mode: FE+BE. Kegagalan layanan penulisan log dipicu di sisi server oleh tim BE (failure injection), bukan lewat `Spectra.intercept`.
- Seeding: user Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`), lalu dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run dan nomor spec: `budisantoso+{runId}-041@qwertysystem.net`.
- Aktor observer log: akun aktor Total Control (Global Settings) di atas login di browser kedua pada hook `before`; browser kedua ditutup di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua sesi browser bersamaan; failure injection layanan penulisan log yang dapat dimatikan (untuk TC-AUTH-LP-153 selama lebih dari 13 menit) dan dipulihkan oleh tim BE; reCAPTCHA mode uji di environment. Hook `after` memulihkan layanan penulisan log walau spec gagal di tengah dan mengakhiri sesi subjek.
- Waktu tunggu nyata 15 menit pada TC-AUTH-LP-153 (langkah 20): TC menyebut seluruh retry penulisan log habis setelah 15 menit, dan tidak menyatakan bahwa timer retry mengikuti jam server; karena itu jam server tidak digeser (konvensi §6) dan spec menunggu 15 menit nyata. Timeout spec harus lebih panjang dari 15 menit. Bila BE memastikan timer retry mengikuti jam server, tunggu diganti pergeseran jam server dengan pemulihan di `after`.
- State global: layanan penulisan log (failure injection) dipulihkan di langkah 10 dan 20 serta di hook `after`; suite berjalan serial (`parallel: false`).
- Pencarian baris log memakai nama tampilan dari TC ("Budi S"; kolom User menampilkan nama singkat, bukan email) dan dibedakan antar run lewat baseline jumlah baris (langkah 1 dan 15, S-12).
- TC-AUTH-LP-130: User `Budi Santoso` (`budisantoso+{runId}-041@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA; layanan penulisan log tidak tersedia sementara (failure injection oleh tim BE)
- TC-AUTH-LP-130 data: Email `budisantoso+{runId}-041@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-153: User `Budi Santoso` yang sama (`budisantoso+{runId}-041@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; tidak ada gate Agreement dan MFA; layanan penulisan log tidak tersedia selama lebih dari 13 menit (failure injection oleh tim BE)
- TC-AUTH-LP-153 data: Email `budisantoso+{runId}-041@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-130: Kegagalan penulisan log tidak menggagalkan login dan entri muncul setelah layanan log pulih

1. Pindah ke browser kedua (sesi aktor Total Control Global Settings), buka `Global Settings > Activity Log > Session`, lalu catat jumlah baris awal untuk user "Budi S"
2. Ganti akun: pindah ke browser pertama (subjek guest)
3. Matikan layanan penulisan log (failure injection oleh tim BE)
4. Buka halaman Login with Password
5. Ketik "budisantoso+{runId}-041@qwertysystem.net" di field Email
6. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
7. Selesaikan reCAPTCHA
8. Klik [Log in]
9. Verifikasi login berhasil dan browser menuju Portal — Product Hub
10. Pulihkan layanan penulisan log
11. Pindah ke browser kedua dan buka `Global Settings > Activity Log > Session`
12. Muat ulang daftar sampai baris terbaru untuk user "Budi S" tampil
13. Verifikasi tepat 1 baris baru (dibandingkan jumlah awal pada langkah 1) dengan Activity "Login", Status "Success", Note "Login with password" tampil

### TC-AUTH-LP-153: Seluruh retry penulisan log gagal tidak menggagalkan login dan entri tidak ditulis

14. Ganti akun: pindah ke browser pertama, lalu logout dari Portal — Product Hub
15. Pindah ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, lalu catat jumlah baris dengan Note "Login with password" untuk user "Budi S" (sesudah logout) sebagai baseline TC-AUTH-LP-153
16. Matikan layanan penulisan log selama lebih dari 13 menit (failure injection oleh tim BE)
17. Ganti akun: pindah ke browser pertama, lalu buka halaman Login with Password
18. Ketik "budisantoso+{runId}-041@qwertysystem.net" di field Email, ketik nilai `Spectra.env.LP_PASSWORD` di field Password, selesaikan reCAPTCHA, lalu klik [Log in]
19. Verifikasi login berhasil dan browser menuju Portal — Product Hub
20. Tunggu 15 menit sampai seluruh retry penulisan log habis, lalu pulihkan layanan penulisan log
21. Ganti akun: pindah ke browser kedua, muat ulang daftar `Global Settings > Activity Log > Session`, lalu cari baris untuk user "Budi S" yang dibuat pada langkah 18
22. Verifikasi tidak ada baris baru dengan Note "Login with password" untuk percobaan pada langkah 18 (jumlah baris dengan Note "Login with password" untuk user "Budi S" sama dengan baseline pada langkah 15)
23. Verifikasi baris login sebelumnya untuk user "Budi S" tetap tampil

## Notes

- Sumber: `auth/login-password/TestCases/tc-login-password.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: fault injection (prinsip 13b). TC-AUTH-LP-153 (seluruh retry penulisan log gagal) ada di spec ini dan bukan di spec absence: ia punya aksi fungsional (login berhasil, langkah 19) dan asersi absence-nya memakai baseline jumlah baris (langkah 15, S-12), sehingga bukan kelas g murni (konvensi §3, asersi jumlah atau state memakai baseline).
- Urutan: TC-AUTH-LP-130 lebih dulu, lalu TC-AUTH-LP-153 karena menunggu 15 menit nyata (S-10); keduanya memakai user Budi Santoso yang sama sehingga TC-AUTH-LP-153 diawali logout (langkah 14) dan baseline jumlah baris sendiri sesudah logout (langkah 15).
- Langkah penghubung (S-03): langkah 1, 2, 14, 15, dan 17 (baseline dan perpindahan browser); pemulihan layanan penulisan log pada langkah 10 dan 20 juga dijamin oleh hook `after`.
- Waktu tunggu 15 menit pada langkah 20 adalah waktu nyata dengan alasan di Prerequisites (timer retry tidak dinyatakan mengikuti jam server).
- Temuan untuk QA:
  - TC-AUTH-LP-130 langkah 4 menyuruh memuat ulang daftar "sampai baris terbaru tampil" tanpa batas waktu tunggu; NC-18 menyebut entri dapat muncul terlambat karena retry. Batas waktu tunggu untuk muncul tidak ditetapkan.
  - TC-AUTH-LP-130 Expected "tepat 1 baris" tidak menyebut baseline; spec memakai jumlah baris awal pada langkah 1 (S-12).
  - TC memakai nama tampilan tetap ("Budi S") untuk mencari baris log; nama itu tidak unik antar run atau antar spec. Spec memakai baseline (S-12) dan suite serial.
  - TC-AUTH-LP-153 menyebut layanan log mati "lebih dari 13 menit" tetapi langkah menunggu 15 menit; asal angka 13 menit tidak dijelaskan di TC, dan TC tidak menyatakan apakah timer retry mengikuti jam server (spec menunggu 15 menit nyata).
  - TC-AUTH-LP-153 tidak menyebut baris log sebelumnya sebagai anchor pada precondition; spec memakai baseline jumlah baris sesudah logout, difilter Note "Login with password" (langkah 15), agar asersi absence bermakna dan baris logout tidak ikut terhitung.
