---
id: TC-AC-LCS-E2E-005-refresh-riwayat-browser-dan-loading-awal
title: "Refresh F5, Tombol Back dan Forward, dan State Loading Awal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-15
  - TC-AC-LCS-16
  - TC-AC-LCS-24
coverage:
  web: automated
---

# Refresh F5, Tombol Back dan Forward, dan State Loading Awal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); `Spectra.intercept` untuk menahan respons pengambilan data Trial Settings (menahan respons hanya untuk mengamati state Loading, bukan kelas b); intercept dilepas segera setelah asersi.
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-15: Refresh F5 pada tab Client Lifecycle tetap memuat tab Client Lifecycle

1. Klik tab Client Lifecycle pada tab bar
2. Tekan F5 pada tab Client Lifecycle
3. Verifikasi Tab Client Lifecycle tetap aktif setelah halaman dimuat ulang
4. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Client Lifecycle"

### TC-AC-LCS-16: Tombol Back dan Forward browser berpindah antar tab yang pernah dibuka

5. Klik tab Trial Settings pada tab bar
6. Klik tab Free Plan Settings
7. Klik tab License Timing
8. Klik tombol Back browser
9. Verifikasi Tab Free Plan Settings aktif
10. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Free Plan Settings"
11. Klik tombol Back browser lagi
12. Verifikasi Tab Trial Settings aktif
13. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Trial Settings"
14. Klik tombol Forward browser
15. Verifikasi Tab Free Plan Settings aktif
16. Verifikasi Halaman Lifecycle Settings tetap tampil (anchor untuk asersi dialog)
17. Verifikasi Tidak ada dialog Unsaved Changes pada seluruh langkah

### TC-AC-LCS-24: State Loading tab Trial Settings saat data awal belum diterima

18. Pasang intercept yang menahan respons pengambilan data Trial Settings selama 5 detik
19. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
20. Verifikasi Loading component tampil pada panel tab
21. Lepaskan penahanan respons dan lepas intercept
22. Verifikasi Loading component hilang dari panel tab
23. Verifikasi Field Trial Settings tampil dengan nilai tersimpan

## Notes

- Langkah penghubung (S-03): klik tab Client Lifecycle sebelum F5 (TC 15 memulai dari tab itu) dan klik tab Trial Settings sebelum urutan Back/Forward (TC 16 memulai dari tab itu). Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- TC 24 berasal dari section 1b TC dan ditempatkan di spec ini karena topiknya pemuatan awal halaman. Penahanan respons memenuhi `Verifikasi` Loading sebelum respons dilepas (bagian 8b butir 5); TC tidak memuat Expected selain state Loading dan field termuat.
- Temuan untuk QA: TC 16 butir d ("tidak ada dialog Unsaved Changes pada seluruh langkah") adalah asersi absence; spec memakai `Verifikasi` halaman Lifecycle Settings tetap tampil sebagai anchor (bagian 8b butir 2) dan satu asersi di akhir, bukan per langkah.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
