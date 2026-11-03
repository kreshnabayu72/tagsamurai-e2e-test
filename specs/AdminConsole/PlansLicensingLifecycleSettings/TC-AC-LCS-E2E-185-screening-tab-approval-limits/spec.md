---
id: TC-AC-LCS-E2E-185-screening-tab-approval-limits
title: "Screening Tab Approval Settings dan System Limits"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-6
  - TC-AC-LCS-7
coverage:
  web: automated
---

# Screening Tab Approval Settings dan System Limits

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

### TC-AC-LCS-6: Screening tab Approval Settings: Breadcrumb, tab bar, field, addon, dan footer

1. Klik tab Approval Settings pada tab bar
2. Susuri halaman dari atas ke bawah tanpa mengklik elemen lain
3. Verifikasi Header: Breadcrumb "Plans & Licensing > Lifecycle Settings > Approval Settings"
4. Verifikasi Header: segmen pertama dan segmen terakhir Breadcrumb bukan link
5. Verifikasi Header: tab `Trial Settings | Free Plan Settings | License Timing | Client Lifecycle | Recycle Bin | Approval Settings (aktif) | System Limits`
6. Verifikasi Header: icon Changelog di pojok kanan atas panel tab
7. Verifikasi Body: Approval Timeout nilai `3`, addon `day(s)`
8. Verifikasi Footer: `[Reset to Default]` (Text, primary) tampil enabled
9. Verifikasi Footer: `[Save]` (filled, success) tampil disabled, kedua tombol rata kanan dengan urutan `[Reset to Default]` lalu `[Save]`

### TC-AC-LCS-7: Screening tab System Limits: Breadcrumb, tab bar, field, addon, dan footer

10. Klik tab System Limits pada tab bar
11. Susuri halaman dari atas ke bawah tanpa mengklik elemen lain
12. Verifikasi Header: Breadcrumb "Plans & Licensing > Lifecycle Settings > System Limits"
13. Verifikasi Header: segmen pertama dan segmen terakhir Breadcrumb bukan link
14. Verifikasi Header: tab `Trial Settings | Free Plan Settings | License Timing | Client Lifecycle | Recycle Bin | Approval Settings | System Limits (aktif)`
15. Verifikasi Header: icon Changelog di pojok kanan atas panel tab
16. Verifikasi Body: Bulk Transaction Row Limit nilai `1000`, addon `row(s)`
17. Verifikasi Body: Selection Limit nilai `1000`, addon `row(s)`
18. Verifikasi Body: Register Asset Bulk Limit nilai `1000`, addon `row(s)`
19. Verifikasi Body: Hierarchy Depth Limit nilai `50`, addon `level(s)`
20. Verifikasi Body: Master Data Count Limit nilai `10000`, addon `record(s)`
21. Verifikasi Body: Max Visible Columns nilai `20`, addon `column(s)`
22. Verifikasi Footer: `[Reset to Default]` (Text, primary) tampil enabled
23. Verifikasi Footer: `[Save]` (filled, success) tampil disabled, kedua tombol rata kanan dengan urutan `[Reset to Default]` lalu `[Save]`

## Notes

- Langkah penghubung (S-03): klik tab pada tiap blok TC adalah langkah sumber TC. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
