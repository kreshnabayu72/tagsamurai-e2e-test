---
id: TC-AC-LCS-E2E-007-pindah-tab-dan-dirty-state-antar-tab
title: "Pindah Tab Mempertahankan Perubahan dan Independensi Dirty State Antar Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-20
  - TC-AC-LCS-21
coverage:
  web: automated
---

# Pindah Tab Mempertahankan Perubahan dan Independensi Dirty State Antar Tab

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

### TC-AC-LCS-20: Pindah tab mempertahankan perubahan yang belum disimpan pada tab yang ditinggalkan

1. Ubah Max Trial Duration dari `30` menjadi `45`
2. Klik tab Free Plan Settings
3. Klik tab Trial Settings kembali
4. Verifikasi Max Trial Duration tetap `45`
5. Verifikasi `[Save]` tab Trial Settings enabled
6. Verifikasi Tab Trial Settings aktif (anchor untuk asersi dialog)
7. Verifikasi Tidak ada dialog Unsaved Changes saat berpindah tab
8. Kembalikan Max Trial Duration ke nilai tersimpan `30`

### TC-AC-LCS-21: Perubahan field di tab Trial Settings tidak meng-enable Save di tab lain

9. Ubah Max Trial Duration dari `30` menjadi `45`
10. Klik tab Free Plan Settings
11. Verifikasi `[Save]` tab Free Plan Settings disabled
12. Klik tab License Timing
13. Verifikasi `[Save]` tab License Timing disabled
14. Klik tab Client Lifecycle
15. Verifikasi `[Save]` tab Client Lifecycle disabled
16. Klik tab Recycle Bin
17. Verifikasi `[Save]` tab Recycle Bin disabled
18. Klik tab Approval Settings
19. Verifikasi `[Save]` tab Approval Settings disabled
20. Klik tab System Limits
21. Verifikasi `[Save]` tab System Limits disabled
22. Klik tab Trial Settings
23. Kembalikan Max Trial Duration ke nilai tersimpan `30`

## Notes

- Langkah penghubung (S-03, S-09): "Kembalikan Max Trial Duration ke nilai tersimpan `30`" memulihkan field yang dirty sebelum TC 21 dan sebelum spec berakhir; klik tab Trial Settings sebelum pemulihan terakhir mengembalikan tab yang dirty ke layar. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Satu `Verifikasi` Unsaved Changes pada TC 20 mengasersi seluruh perpindahan tab (dua klik) karena dialog akan menahan klik berikutnya; `Verifikasi` tab Trial Settings aktif menjadi anchor positifnya (bagian 8b butir 2) dan bukan asersi tambahan TC.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
