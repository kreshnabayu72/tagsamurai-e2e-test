---
id: TC-AC-LCS-E2E-011-nilai-default-instalasi-baru-trial-free-license
title: "Nilai Default Instalasi Baru: Tab Trial Settings, Free Plan Settings, dan License Timing"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-33
  - TC-AC-LCS-34
  - TC-AC-LCS-35
coverage:
  web: automated
---

# Nilai Default Instalasi Baru: Tab Trial Settings, Free Plan Settings, dan License Timing

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`).
- Data: platform baru (FRESH): tab yang diuji belum pernah disimpan, dibentuk lewat Fixture BE pada langkah penghubung di awal tiap blok TC (sesudah hook `beforeEach` suite memulihkan default, sehingga keadaan itu tidak tertimpa); hook `after` mengembalikan keadaan tab ke default tersimpan.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); Fixture BE untuk membuat keadaan tab belum pernah disimpan.
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-33: Tab Trial Settings pada instalasi baru menampilkan nilai default

1. Atur tab Trial Settings ke keadaan belum pernah disimpan lewat Fixture BE
2. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
3. Amati nilai seluruh field pada tab
4. Verifikasi Field Max Trial Duration berisi `30`
5. Verifikasi Field Max Trial Asset Quota berisi `50`
6. Verifikasi Field Max Trial Concurrent User Quota berisi `10`
7. Verifikasi Field First Notification berisi `7`
8. Verifikasi Field Second Notification berisi `1`
9. Verifikasi Switch Require Approval for Trial Activation berstatus `OFF`
10. Verifikasi Tidak ada pesan error dan tidak ada empty state field
11. Verifikasi `[Save]` disabled

### TC-AC-LCS-34: Tab Free Plan Settings pada instalasi baru menampilkan nilai default

12. Atur tab Free Plan Settings ke keadaan belum pernah disimpan lewat Fixture BE
13. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
14. Klik tab Free Plan Settings pada tab bar
15. Amati nilai seluruh field pada tab
16. Verifikasi Field Free Plan Duration berisi `365`
17. Verifikasi Tidak ada pesan error dan tidak ada empty state field
18. Verifikasi `[Save]` disabled

### TC-AC-LCS-35: Tab License Timing pada instalasi baru menampilkan nilai default

19. Atur tab License Timing ke keadaan belum pernah disimpan lewat Fixture BE
20. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
21. Klik tab License Timing pada tab bar
22. Amati nilai seluruh field pada tab
23. Verifikasi Field Managed Transition Time berisi `24`
24. Verifikasi Field Managed Action Retry Delay berisi `2`
25. Verifikasi Field Addon Reactivation Delay berisi `2`
26. Verifikasi Tidak ada pesan error dan tidak ada empty state field
27. Verifikasi `[Save]` disabled

## Notes

- Langkah penghubung (S-03): TC 34 dan 35 menulis "klik menu ..., lalu klik tab ..." sebagai dua langkah. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Langkah penghubung (S-03, S-11): langkah 1, 12, dan 19 membentuk keadaan FRESH tab yang diuji lewat Fixture BE sesudah `beforeEach` suite memulihkan default.
- Absence "tidak ada pesan error dan tidak ada empty state field" ditulis sesudah `Verifikasi` seluruh nilai field (anchor positif, bagian 8b butir 2).
- Temuan untuk QA: cara membuat keadaan "tab belum pernah disimpan" tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan Fixture BE yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
