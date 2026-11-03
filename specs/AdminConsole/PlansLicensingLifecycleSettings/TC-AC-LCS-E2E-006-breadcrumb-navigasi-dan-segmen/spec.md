---
id: TC-AC-LCS-E2E-006-breadcrumb-navigasi-dan-segmen
title: "Breadcrumb Lifecycle Settings: Navigasi, State Aktif, dan Segmen Bukan Link"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-17
  - TC-AC-LCS-18
  - TC-AC-LCS-19
coverage:
  web: automated
---

# Breadcrumb Lifecycle Settings: Navigasi, State Aktif, dan Segmen Bukan Link

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-17: Klik segmen Breadcrumb "Lifecycle Settings" dari tab Free Plan Settings membuka Trial Settings tanpa dialog dan mempertahankan perubahan

1. Klik tab Free Plan Settings pada tab bar
2. Ubah Free Plan Duration dari `365` menjadi `100` (belum disimpan)
3. Klik segmen "Lifecycle Settings" pada Breadcrumb
4. Verifikasi Tab Trial Settings aktif
5. Verifikasi Tidak ada dialog Unsaved Changes
6. Klik tab Free Plan Settings
7. Verifikasi Free Plan Duration tetap `100`
8. Verifikasi `[Save]` tab Free Plan Settings tetap enabled
9. Kembalikan Free Plan Duration ke nilai tersimpan `365`

### TC-AC-LCS-18: Klik segmen Breadcrumb "Lifecycle Settings" saat tab Trial Settings sudah aktif tidak mengubah apa pun

10. Klik tab Trial Settings pada tab bar
11. Ubah Max Trial Duration dari `30` menjadi `45` (belum disimpan)
12. Klik segmen "Lifecycle Settings" pada Breadcrumb
13. Verifikasi Tab Trial Settings tetap aktif
14. Verifikasi Max Trial Duration tetap `45`
15. Verifikasi Tidak ada dialog Unsaved Changes
16. Verifikasi Tidak ada reload halaman (perubahan belum disimpan tetap ada pada field)
17. Kembalikan Max Trial Duration ke nilai tersimpan `30`

### TC-AC-LCS-19: Segmen pertama dan segmen terakhir Breadcrumb pada tab License Timing bukan link

18. Klik tab License Timing pada tab bar
19. Hover segmen "License Timing" pada Breadcrumb
20. Verifikasi Segmen "License Timing" tampil sebagai label statis (kursor bukan link)
21. Klik segmen "License Timing"
22. Verifikasi Klik pada segmen "License Timing" tidak memicu navigasi apa pun
23. Verifikasi Tab License Timing tetap aktif
24. Hover segmen "Plans & Licensing" pada Breadcrumb
25. Verifikasi Segmen "Plans & Licensing" tampil sebagai label statis (kursor bukan link)
26. Klik segmen "Plans & Licensing"
27. Verifikasi Klik pada segmen "Plans & Licensing" tidak memicu navigasi apa pun
28. Verifikasi Tab License Timing tetap aktif

## Notes

- Langkah penghubung (S-03, S-09): klik tab agar tiap blok TC dimulai dari tab menurut Precondition; langkah "Kembalikan ... ke nilai tersimpan" memulihkan field yang dirty sebelum blok berikutnya dan sebelum spec berakhir (S-09). Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Temuan untuk QA: TC 18 butir b ("tidak ada reload halaman") tidak punya langkah observasi langsung; spec mengamatinya lewat perubahan belum disimpan yang tetap ada pada field (turunan dari butir a) dan tidak menambah mekanisme pengamat navigasi.
- Temuan untuk QA: TC 19 mengasersi kursor "bukan link" tanpa cara pengamatan yang ditentukan TC; spec menulisnya sebagai label statis yang tidak memicu navigasi.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
