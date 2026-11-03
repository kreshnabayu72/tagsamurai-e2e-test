---
id: TC-AC-LCS-E2E-001-screening-tab-trial-free-license
title: "Screening Halaman Lifecycle Settings: Tab Trial Settings, Free Plan Settings, dan License Timing"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-1
  - TC-AC-LCS-2
  - TC-AC-LCS-3
coverage:
  web: automated
---

# Screening Halaman Lifecycle Settings: Tab Trial Settings, Free Plan Settings, dan License Timing

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

### TC-AC-LCS-1: Screening landing Lifecycle Settings: tab default Trial Settings aktif dengan Breadcrumb, tab bar, field, dan footer

1. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
2. Verifikasi halaman Lifecycle Settings terbuka
3. Susuri halaman dari atas ke bawah tanpa mengklik elemen lain
4. Verifikasi Header: Breadcrumb "Plans & Licensing > Lifecycle Settings > Trial Settings"
5. Verifikasi Header: segmen pertama dan segmen terakhir Breadcrumb bukan link
6. Verifikasi Header: tombol replay `[?]` tepat di sebelah kanan Breadcrumb
7. Hover tombol replay `[?]`
8. Verifikasi tooltip "Show guide" tampil pada tombol `[?]`
9. Verifikasi Header: tab `Trial Settings (aktif) | Free Plan Settings | License Timing | Client Lifecycle | Recycle Bin | Approval Settings | System Limits`
10. Verifikasi Header: icon Changelog di pojok kanan atas panel tab
11. Verifikasi Body: Max Trial Duration nilai `30`, addon `day(s)`
12. Verifikasi Body: Max Trial Asset Quota nilai `50`, addon `assets`
13. Verifikasi Body: Max Trial Concurrent User Quota nilai `10`, addon `users`
14. Verifikasi Body: Require Approval for Trial Activation Switch berstatus `OFF`
15. Verifikasi Body: First Notification nilai `7`, addon `day(s) before expiry`
16. Verifikasi Body: Second Notification nilai `1`, addon `day(s) before expiry`
17. Verifikasi Footer: `[Reset to Default]` (Text, primary) tampil enabled
18. Verifikasi Footer: `[Save]` (filled, success) tampil disabled, kedua tombol rata kanan dengan urutan `[Reset to Default]` lalu `[Save]`

### TC-AC-LCS-2: Screening tab Free Plan Settings: Breadcrumb, tab bar, field, addon, dan footer

19. Klik tab Free Plan Settings pada tab bar
20. Susuri halaman dari atas ke bawah tanpa mengklik elemen lain
21. Verifikasi Header: Breadcrumb "Plans & Licensing > Lifecycle Settings > Free Plan Settings"
22. Verifikasi Header: segmen pertama dan segmen terakhir Breadcrumb bukan link
23. Verifikasi Header: tab `Trial Settings | Free Plan Settings (aktif) | License Timing | Client Lifecycle | Recycle Bin | Approval Settings | System Limits`
24. Verifikasi Header: icon Changelog di pojok kanan atas panel tab
25. Verifikasi Body: Free Plan Duration nilai `365`, addon `day(s)`
26. Verifikasi Footer: `[Reset to Default]` (Text, primary) tampil enabled
27. Verifikasi Footer: `[Save]` (filled, success) tampil disabled, kedua tombol rata kanan dengan urutan `[Reset to Default]` lalu `[Save]`

### TC-AC-LCS-3: Screening tab License Timing: Breadcrumb, tab bar, field, addon, dan footer

28. Klik tab License Timing pada tab bar
29. Susuri halaman dari atas ke bawah tanpa mengklik elemen lain
30. Verifikasi Header: Breadcrumb "Plans & Licensing > Lifecycle Settings > License Timing"
31. Verifikasi Header: segmen pertama dan segmen terakhir Breadcrumb bukan link
32. Verifikasi Header: tab `Trial Settings | Free Plan Settings | License Timing (aktif) | Client Lifecycle | Recycle Bin | Approval Settings | System Limits`
33. Verifikasi Header: icon Changelog di pojok kanan atas panel tab
34. Verifikasi Body: Managed Transition Time nilai `24`, addon `hour(s)`
35. Verifikasi Body: Managed Action Retry Delay nilai `2`, addon `day(s)`
36. Verifikasi Body: Addon Reactivation Delay nilai `2`, addon `day(s)`
37. Verifikasi Footer: `[Reset to Default]` (Text, primary) tampil enabled
38. Verifikasi Footer: `[Save]` (filled, success) tampil disabled, kedua tombol rata kanan dengan urutan `[Reset to Default]` lalu `[Save]`

## Notes

- Langkah penghubung (S-03): klik tab pada blok TC 2 dan TC 3 adalah langkah sumber TC; langkah hover tombol `[?]` ada untuk mengamati tooltip "Show guide" yang disebut Expected TC 1. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Langkah "Susuri halaman" adalah langkah observasi TC tanpa aksi lain; asersi tiap bagian halaman ditulis sebagai `Verifikasi` terpisah per klausa (S-01). Baris field dengan nilai dan addon ditulis satu `Verifikasi` per field karena TC menyebutnya satu butir.
- Alasan di atas sekitar 35 langkah: seluruh blok memuat TC fungsional kelas yang sama (screening landing), tiap blok memeriksa satu tab dengan keadaan awal sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
