---
id: TC-AC-LCS-E2E-003-deep-link-tab-trial-sampai-client-lifecycle
title: "Deep Link Tab Trial Settings, Free Plan Settings, License Timing, dan Client Lifecycle"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-8
  - TC-AC-LCS-9
  - TC-AC-LCS-10
  - TC-AC-LCS-11
coverage:
  web: automated
---

# Deep Link Tab Trial Settings, Free Plan Settings, License Timing, dan Client Lifecycle

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

### TC-AC-LCS-8: Deep link tab Trial Settings: route tab dibuka langsung dari tab browser baru

1. Pada tab Trial Settings, salin alamat URL halaman dari address bar
2. Buka tab browser baru, tempel alamat URL tersebut, tekan Enter
3. Verifikasi Halaman Lifecycle Settings terbuka dengan tab Trial Settings aktif
4. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Trial Settings"
5. Tutup tab browser baru dan kembali ke tab browser awal

### TC-AC-LCS-9: Deep link tab Free Plan Settings: route tab dibuka langsung dari tab browser baru

6. Klik tab Free Plan Settings pada tab bar
7. Pada tab Free Plan Settings, salin alamat URL halaman dari address bar
8. Buka tab browser baru, tempel alamat URL tersebut, tekan Enter
9. Verifikasi Halaman Lifecycle Settings terbuka dengan tab Free Plan Settings aktif
10. Verifikasi Tab default Trial Settings tidak aktif
11. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Free Plan Settings"
12. Tutup tab browser baru dan kembali ke tab browser awal

### TC-AC-LCS-10: Deep link tab License Timing: route tab dibuka langsung dari tab browser baru

13. Klik tab License Timing pada tab bar
14. Pada tab License Timing, salin alamat URL halaman dari address bar
15. Buka tab browser baru, tempel alamat URL tersebut, tekan Enter
16. Verifikasi Halaman Lifecycle Settings terbuka dengan tab License Timing aktif
17. Verifikasi Tab default Trial Settings tidak aktif
18. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > License Timing"
19. Tutup tab browser baru dan kembali ke tab browser awal

### TC-AC-LCS-11: Deep link tab Client Lifecycle: route tab dibuka langsung dari tab browser baru

20. Klik tab Client Lifecycle pada tab bar
21. Pada tab Client Lifecycle, salin alamat URL halaman dari address bar
22. Buka tab browser baru, tempel alamat URL tersebut, tekan Enter
23. Verifikasi Halaman Lifecycle Settings terbuka dengan tab Client Lifecycle aktif
24. Verifikasi Tab default Trial Settings tidak aktif
25. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Client Lifecycle"
26. Tutup tab browser baru dan kembali ke tab browser awal

## Notes

- Langkah penghubung (S-03): klik tab sebelum menyalin URL (TC 9 sampai 11 memulai dari tab yang sudah aktif menurut Precondition), dan menutup tab browser baru sesudah tiap blok (S-09). Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Tab browser baru hanya memuat URL yang disalin dan tidak memakai konteks login baru; sesi login dipakai bersama (bukan konteks kelas c).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
