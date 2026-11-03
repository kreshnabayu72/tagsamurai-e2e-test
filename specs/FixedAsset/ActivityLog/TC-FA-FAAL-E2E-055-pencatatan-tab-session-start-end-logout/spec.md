---
id: TC-FA-FAAL-E2E-055-pencatatan-tab-session-start-end-logout
title: "Pencatatan Tab Session: Session started dan Session ended (Logout, Password, Keluar Produk)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-209
  - TC-FA-FAAL-210
  - TC-FA-FAAL-212
  - TC-FA-FAAL-213
coverage:
  web: automated
---

# Pencatatan Tab Session: Session started dan Session ended (Logout, Password, Keluar Produk)

## Prerequisites

- Mode: FE+BE.
- Akun observer dan aktor: Total Control (Pre-setup #1, Admin Alpha), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, tab Session).
- Pelaku: John Doe (Pre-setup #16) dengan App Access Fixed Asset dan seat subscription tersedia; email dari `Fixture.activity-log.userJohnDoe.email` (fixture belum ada, disediakan tim FE). Password awal `Spectra.env.FA_JOHNDOE_PASSWORD`; password baru untuk TC-FA-FAAL-212 `Spectra.env.FA_JOHNDOE_PASSWORD_NEW`. Kedua env var tidak tercantum di butir "Env var" `suite.md`; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Kemampuan teknis disediakan tim BE/FE: sesi API aktor untuk John Doe (butir "Sesi API aktor" di `suite.md`) yang menghasilkan sesi-produk Fixed Asset dengan Device/Browser `Chrome on Windows`, dapat login dengan password, membuka produk, logout platform, keluar ke Product Hub, dan mengubah password akun sendiri.
- Baseline (S-12): total baris Tab Session dibaca dari teks pagination `Showing x–y of N entries` sebelum tiap aksi pemicu; Tab Session tidak menyaring dan tidak memakai Search selama spec.
- State yang diubah dan pemulihannya: password John Doe (TC-FA-FAAL-212) dikembalikan ke `Spectra.env.FA_JOHNDOE_PASSWORD` pada langkah 19 dan di hook `after`; sesi-produk John Doe yang masih aktif ditutup di hook `after`.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun observer.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-209: Membuka produk Fixed Asset mencatat Session started

1. Catat total baris Tab Session dari teks pagination (N0)
2. Pelaku John Doe (sesi API aktor, Chrome pada Windows) login dengan password dan membuka produk Fixed Asset dari Product Hub hingga Session started tersimpan
3. Verifikasi tanpa memuat ulang halaman: baris baru muncul otomatis di baris paling atas Tab Session: User `John D`, Activity `Session`, Status `—`, Note `Session started`, Device/Browser `Chrome on Windows`
4. Verifikasi tanpa memuat ulang halaman: total baris Tab Session menjadi N0 + 1

### TC-FA-FAAL-210: Session ended tercatat saat logout platform

5. Catat total baris Tab Session dari teks pagination (N0); sesi-produk John Doe dari langkah 2 masih aktif
6. Pelaku John Doe (sesi API aktor) melakukan Logout dari platform hingga Session ended tersimpan
7. Verifikasi tanpa memuat ulang halaman: baris baru muncul otomatis di baris paling atas: User `John D`, Activity `Session`, Status `—`, Note `Session ended`
8. Verifikasi tanpa memuat ulang halaman: tidak ada baris dengan Note `Logged out by admin` untuk sesi-produk yang sama; total baris Tab Session N0 + 1, yaitu hanya baris Session ended pada langkah 7

### TC-FA-FAAL-213: Session ended tercatat saat keluar dari produk Fixed Asset secara eksplisit

9. Pelaku John Doe (sesi API aktor) login dengan password dan membuka produk Fixed Asset hingga Session started tersimpan
10. Catat total baris Tab Session dari teks pagination (N0)
11. Pelaku John Doe (sesi API aktor) keluar dari produk Fixed Asset ke Product Hub hingga Session ended tersimpan
12. Verifikasi tanpa memuat ulang halaman: baris baru muncul otomatis di baris paling atas: User `John D`, Activity `Session`, Status `—`, Note `Session ended`
13. Verifikasi tanpa memuat ulang halaman: tidak ada baris dengan Note `Logged out by admin` untuk sesi-produk yang sama; total baris Tab Session N0 + 1, yaitu hanya baris Session ended pada langkah 12

### TC-FA-FAAL-212: Session ended tercatat saat perubahan password

14. Pelaku John Doe (sesi API aktor) login dengan password dan membuka produk Fixed Asset hingga Session started tersimpan
15. Catat total baris Tab Session dari teks pagination (N0)
16. Pelaku John Doe (sesi API aktor) mengubah password di Global Settings > My Profile menjadi `Spectra.env.FA_JOHNDOE_PASSWORD_NEW` hingga perubahan tersimpan
17. Verifikasi tanpa memuat ulang halaman: baris baru muncul otomatis di baris paling atas: User `John D`, Activity `Session`, Status `—`, Note `Session ended`
18. Verifikasi tanpa memuat ulang halaman: tidak ada baris dengan Note `Logged out by admin` untuk sesi-produk yang sama; total baris Tab Session N0 + 1, yaitu hanya baris Session ended pada langkah 17
19. Pulihkan password John Doe ke `Spectra.env.FA_JOHNDOE_PASSWORD` lewat sesi API aktor hingga tersimpan

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 209, 210, 213, 212. TC-FA-FAAL-212 diletakkan terakhir karena mengubah password John Doe; TC lain memakai password awal.
- Langkah penghubung (S-03): langkah 9 dan 14 (sesi-produk aktif sebagai precondition TC-213 dan TC-212; precondition TC-210 dipenuhi oleh sesi-produk dari langkah 2), langkah 19 (pemulihan password).
- Baseline total (langkah 1, 5, 10, 15) dan Verifikasi total N0 + 1 (langkah 4, 8, 13, 18) ditambahkan untuk S-12; kolom Expected TC tidak menyebut hitungan.
- P-1 (TC-FA-FAAL-210, 213, 212 butir b): asersi "tidak ada baris dengan Note `Logged out by admin`" bergantung pada sesi-produk aktif yang baru dibangun langkah sebelumnya (login dan buka produk). Asersi dibaca dari baris paling atas (langkah 7, 12, 17) sebagai anchor positif dan total N0 + 1; tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05).
- Temuan untuk QA:
  - TC-FA-FAAL-209 sampai 213 berlabel "Manual Only — (d) dua sesi paralel"; spec memakai sesi UI observer dan pelaku John Doe lewat sesi API aktor. TC, PRD, dan LLD tidak menyatakan apakah sesi API menghasilkan Session started dengan Device/Browser `Chrome on Windows`; kemampuan itu disediakan tim BE/FE.
  - Email dan password John Doe tidak tertulis di Pre-setup TC; nama env var diusulkan di Prerequisites.
  - TC-FA-FAAL-212 langkah 1 menyebut ubah password di Global Settings > My Profile tanpa nilai password baru; spec memakai `Spectra.env.FA_JOHNDOE_PASSWORD_NEW`.
  - TC-FA-FAAL-210, 212, 213 butir b ("tidak ada baris dengan Note `Logged out by admin`") tidak punya langkah observasi selain amati Tab Session; spec memakai total baris.
