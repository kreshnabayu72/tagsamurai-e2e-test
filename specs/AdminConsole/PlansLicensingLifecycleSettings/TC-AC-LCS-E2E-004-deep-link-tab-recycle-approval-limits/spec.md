---
id: TC-AC-LCS-E2E-004-deep-link-tab-recycle-approval-limits
title: "Deep Link Tab Recycle Bin, Approval Settings, dan System Limits"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-12
  - TC-AC-LCS-13
  - TC-AC-LCS-14
coverage:
  web: automated
---

# Deep Link Tab Recycle Bin, Approval Settings, dan System Limits

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); tab browser kedua pada sesi yang sama (buka tab baru dan tutup).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-12: Deep link tab Recycle Bin: route tab dibuka langsung dari tab browser baru

1. Klik tab Recycle Bin pada tab bar
2. Pada tab Recycle Bin, salin alamat URL halaman dari address bar
3. Buka tab browser baru, tempel alamat URL tersebut, tekan Enter
4. Verifikasi Halaman Lifecycle Settings terbuka dengan tab Recycle Bin aktif
5. Verifikasi Tab default Trial Settings tidak aktif
6. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Recycle Bin"
7. Tutup tab browser baru dan kembali ke tab browser awal

### TC-AC-LCS-13: Deep link tab Approval Settings: route tab dibuka langsung dari tab browser baru

8. Klik tab Approval Settings pada tab bar
9. Pada tab Approval Settings, salin alamat URL halaman dari address bar
10. Buka tab browser baru, tempel alamat URL tersebut, tekan Enter
11. Verifikasi Halaman Lifecycle Settings terbuka dengan tab Approval Settings aktif
12. Verifikasi Tab default Trial Settings tidak aktif
13. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Approval Settings"
14. Tutup tab browser baru dan kembali ke tab browser awal

### TC-AC-LCS-14: Deep link tab System Limits: route tab dibuka langsung dari tab browser baru

15. Klik tab System Limits pada tab bar
16. Pada tab System Limits, salin alamat URL halaman dari address bar
17. Buka tab browser baru, tempel alamat URL tersebut, tekan Enter
18. Verifikasi Halaman Lifecycle Settings terbuka dengan tab System Limits aktif
19. Verifikasi Tab default Trial Settings tidak aktif
20. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > System Limits"
21. Tutup tab browser baru dan kembali ke tab browser awal

## Notes

- Langkah penghubung (S-03): klik tab sebelum menyalin URL dan menutup tab browser baru sesudah tiap blok (S-09). Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
