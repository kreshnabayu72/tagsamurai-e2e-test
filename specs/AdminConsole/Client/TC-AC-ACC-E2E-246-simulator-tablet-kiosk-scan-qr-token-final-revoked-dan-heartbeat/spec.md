---
id: TC-AC-ACC-E2E-246-simulator-tablet-kiosk-scan-qr-token-final-revoked-dan-heartbeat
title: "Simulator Tablet Kiosk: Scan QR, Token Final Tidak Dapat Dipakai Ulang, Tablet Revoked Tidak Dapat Sync, dan Last Active Heartbeat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-322
  - TC-AC-ACC-323
  - TC-AC-ACC-895
  - TC-AC-ACC-900
coverage:
  web: automated
---

# Simulator Tablet Kiosk: Scan QR, Token Final Tidak Dapat Dipakai Ulang, Tablet Revoked Tidak Dapat Sync, dan Last Active Heartbeat

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net` (Manage active client C/R/U/D pada Area Jakarta dan Cabang Menteng), password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (TC-AC-ACC-322, 323, 900). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite. Akun kedua (langkah ganti akun): Total Control A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (TC-AC-ACC-895). Nama env `AC_CLIENT_ACTIVE_FULL_PASSWORD` baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Dinamis milik spec (skrip seed di hook `before`, bukan lewat UI, dihapus di hook `after`; TC memakai Client Pre-setup yang kuota dan Last Active-nya akan berubah sehingga spec memakai Client sendiri): Client "PT Tablet Kiosk {runId}-246" (Active, FAMS Active) dengan Asset Control Total 5 dan Used 0, SFR bertipe Asset Control "Reader Kiosk A", "Reader Kiosk B", "Reader Kiosk C" tanpa station aktif (eligible), satu Station Active dengan Tablet "Tablet Heartbeat {runId}-246" (Active) untuk TC-AC-ACC-895, dan satu Tablet "Tablet Revoked {runId}-246" berstatus Revoked pada Station Active untuk TC-AC-ACC-900 (hasil Revoke lewat seed, dependensi TC-AC-ACC-330 dipenuhi lewat seed). Nama dan jumlah SFR/Station/Tablet tidak tertulis di TC (lihat Temuan untuk QA).
- Kemampuan teknis (kelas harness d): simulator tablet dengan aplikasi kiosk yang memindai QR Enrollment, mengirim heartbeat, mencoba sync atau login kiosk ke Station (disediakan tim FE; hardware tablet fisik pada TC bertanda Manual Only); kemampuan baca status token Enrollment QR (Active, Used, Expired, Invalidated) lewat fixture BE (disediakan tim FE/BE); jam server uji dapat dimajukan (pemulihan token dan pembuatan token berstatus Expired); baca Last Active tablet lewat UI.
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser)
- State global: jam server dimajukan lalu dipulihkan di langkah penghubung dan hook `after`; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-322: Tablet scan QR: token Used dan slot terpakai

1. Ketik Search "PT Tablet Kiosk {runId}-246" di List Client, tekan Enter, klik Company Name hasilnya, lalu klik Tab Asset Control
2. Catat Station Quota (Used U1)
3. Klik [Generate Enrollment QR], pilih SFR "Reader Kiosk A" pada dropdown "Select Smart Fixed Reader", lalu verifikasi QR Code tampil
4. Simulator tablet kiosk memindai QR itu
5. Verifikasi status token Enrollment QR berubah menjadi `Used` (dibaca lewat fixture BE)
6. Klik [Close], lalu muat ulang Tab Asset Control
7. Verifikasi Used kuota = U1 + 1
8. Verifikasi tablet terdaftar pada Tablet List Station baru

### TC-AC-ACC-323: Token status final tidak dapat diaktifkan kembali

9. Simulator tablet kiosk memindai ulang QR yang sudah `Used` (token langkah 3)
10. Verifikasi pemindaian ditolak
11. Verifikasi status token tetap `Used` (dibaca lewat fixture BE)
12. Klik [Generate Enrollment QR], pilih SFR "Reader Kiosk B" pada dropdown "Select Smart Fixed Reader", verifikasi QR Code tampil, lalu klik [Close]
13. Majukan jam server uji 15 menit 1 detik sejak QR tampil hingga token menjadi Expired, lalu pulihkan jam server dan jam browser
14. Simulator tablet kiosk memindai ulang QR yang sudah `Expired`
15. Verifikasi pemindaian ditolak
16. Verifikasi status token tetap `Expired` (dibaca lewat fixture BE)
17. Klik [Generate Enrollment QR], pilih SFR "Reader Kiosk C" pada dropdown "Select Smart Fixed Reader", verifikasi QR Code pertama tampil, lalu klik [Close]
18. Klik [Generate Enrollment QR] lagi, klik [Generate New QR] pada dialog "Active Enrollment QR", pilih SFR "Reader Kiosk C" pada dropdown "Select Smart Fixed Reader", verifikasi QR Code baru tampil, lalu klik [Close]
19. Simulator tablet kiosk memindai ulang QR pertama (token `Invalidated`)
20. Verifikasi pemindaian ditolak
21. Verifikasi status token pertama tetap `Invalidated` (dibaca lewat fixture BE)
22. Majukan jam server uji 15 menit hingga token Active langkah 18 menjadi Expired, lalu pulihkan jam server dan jam browser

### TC-AC-ACC-900: Tablet Revoked tidak dapat sync dan Enrollment QR lama tidak dapat dipakai ulang

23. Buka aplikasi kiosk (simulator) pada tablet "Tablet Revoked {runId}-246"
24. Coba sync atau login kiosk ke Station tablet itu
25. Verifikasi sesi kiosk Station User tablet sudah berakhir
26. Verifikasi tablet tidak dapat sync dengan Station dan tidak dapat dipakai lagi
27. Simulator tablet kiosk memindai ulang Enrollment QR yang dulu dipakai mendaftarkan tablet itu
28. Verifikasi pemindaian Enrollment QR lama ditolak

### Ganti akun

29. Logout, lalu login sebagai Total Control A-01 (`totalControlPrincipal_automated_qaTeam1@qwertysystem.net`)

### TC-AC-ACC-895: Last Active tablet ter-update setelah heartbeat

30. Ketik Search "PT Tablet Kiosk {runId}-246" di List Client, tekan Enter, klik Company Name hasilnya, lalu klik Tab Asset Control
31. Klik row Station yang berisi "Tablet Heartbeat {runId}-246" untuk expand Tablet List
32. Catat nilai Last Active "Tablet Heartbeat {runId}-246" (LA1)
33. Simulator tablet kiosk mengirim heartbeat untuk "Tablet Heartbeat {runId}-246" hingga heartbeat tercatat
34. Muat ulang Tab Asset Control, lalu klik row Station yang sama untuk expand Tablet List
35. Verifikasi Last Active "Tablet Heartbeat {runId}-246" lebih baru daripada LA1
36. Verifikasi Last Active ditulis dalam Date Format dan Time Format General Settings

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 dan 30 (Search dan buka Detail Client; hook suite hanya membuka List Client), langkah 3, 12, 17, 18 (memilih SFR eligible berbeda per Generate karena dropdown tidak terisi otomatis bila SFR eligible lebih dari satu, TC-AC-ACC-991), langkah 6 dan 12 sampai 13, 17 sampai 18, 22 (menutup dialog, membuat token tambahan, dan memajukan jam untuk membentuk token berstatus Expired, Invalidated, dan Active, dibutuhkan oleh Expected TC-AC-ACC-323 "Used/Expired/Invalidated"), langkah 31 sampai 34 (expand row dan muat ulang).
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu kelas harness (d, simulator tablet kiosk) dan tiap blok memakai token atau tablet sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pengamat Admin Console hanya membaca (tanpa konteks kedua kelas c).
- TC-AC-ACC-323 memuat tiga status token dalam satu TC; spec menyusunnya berurutan Used, Expired, Invalidated dengan token baru pada tiap status karena token final tidak dapat dipakai ulang.
- Temuan untuk QA:
  - TC-AC-ACC-322 dan 323 memakai Client "PT Sejahtera Abadi" Pre-setup (kuota Total 3 / Used 2 / Available 1); pemindaian QR mengubah Used menjadi 3 dan merusak asersi TC lain (mis. TC-AC-ACC-308), serta TC-AC-ACC-895 mengubah Last Active tablet Pre-setup (mempengaruhi TC-AC-ACC-792). Spec memakai Client milik sendiri; nama SFR, Station, dan Tablet-nya tidak tertulis di Tabel A.
  - TC-AC-ACC-322 dan 323 tidak menyebut langkah Generate Enrollment QR yang menghasilkan QR yang dipindai (precondition hilang); spec menambahkan Generate sebagai langkah penghubung. Observasi status token Used/Expired/Invalidated tidak punya cara cek di UI; spec memakai kemampuan baca fixture BE tanpa endpoint karangan.
  - TC-AC-ACC-900 mensyaratkan tablet fisik Revoked "hasil Revoke" dari TC-AC-ACC-330 tanpa menyebut cara menyiapkan; spec men-seed tablet Revoked sendiri. TC-AC-ACC-895 menyebut Total Control sedangkan TC lain di spec memakai Active-Full; ganti akun memakai Step eksplisit.
