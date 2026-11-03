---
id: TC-AC-LCS-E2E-008-aksesibilitas-tab-bar-dan-viewport-sempit
title: "Aksesibilitas Tab Bar dan Scroll Horizontal pada Viewport Sempit"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-22
  - TC-AC-LCS-23
coverage:
  web: automated
---

# Aksesibilitas Tab Bar dan Scroll Horizontal pada Viewport Sempit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); pengaturan ukuran viewport browser (perkecil dan pulihkan).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI. Ukuran viewport browser dipulihkan oleh langkah pemulihan di akhir TC 23.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-22: Accessibility tab bar: navigasi keyboard panah kiri/kanan dan aktivasi dengan Enter/Space

1. Fokuskan tab Trial Settings dengan tombol Tab
2. Tekan panah kanan
3. Verifikasi Fokus berpindah ke tab Free Plan Settings
4. Tekan Enter
5. Verifikasi Tab Free Plan Settings aktif
6. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Free Plan Settings"
7. Tekan panah kanan lalu tekan Space
8. Verifikasi Tab License Timing aktif
9. Tekan panah kiri
10. Verifikasi Fokus berpindah ke tab Free Plan Settings

### TC-AC-LCS-23: Tab bar dapat di-scroll horizontal saat lebar viewport sempit

11. Perkecil lebar jendela browser hingga seluruh tab tidak muat dalam satu baris
12. Verifikasi Tab bar tidak membungkus ke baris kedua
13. Scroll tab bar secara horizontal ke kanan
14. Verifikasi Tab bar dapat di-scroll horizontal
15. Klik tab System Limits
16. Verifikasi Tab System Limits terjangkau dan terbuka
17. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > System Limits"
18. Pulihkan lebar jendela browser ke ukuran semula

## Notes

- Langkah penghubung (S-03, S-09): pemulihan lebar jendela browser di akhir TC 23. TC 22 memakai fokus keyboard dari tab Trial Settings yang dibuka hook `beforeEach` suite. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Lebar viewport "sempit" pada TC 23 tidak diberi angka oleh TC; spec memakai ukuran yang membuat tujuh tab tidak muat satu baris (ditentukan tim FE saat script).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
