---
id: TC-AC-LCS-E2E-009-resilience-error-load-tab-trial-sampai-client-lifecycle
title: "Resilience Error Load 500 Tab Trial Settings, Free Plan Settings, License Timing, dan Client Lifecycle"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-25
  - TC-AC-LCS-26
  - TC-AC-LCS-27
  - TC-AC-LCS-28
coverage:
  web: automated
---

# Resilience Error Load 500 Tab Trial Settings, Free Plan Settings, License Timing, dan Client Lifecycle

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); `Spectra.intercept` untuk memaksa respons pengambilan data tiap tab gagal 500 di atas backend nyata (Mode FE+BE karena asersi tab lain mengandalkan backend nyata); intercept dilepas segera setelah asersi tiap blok (S-09).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-25: Error load tab Trial Settings: pengambilan data gagal 500

1. Pasang intercept yang memaksa respons pengambilan data Trial Settings gagal 500
2. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
3. Verifikasi State gagal muat tampil: "Unable to load this data." (bukan empty state dan bukan field kosong)
4. Verifikasi Tombol `[Try Again]` tampil pada state gagal muat
5. Verifikasi Field, `[Reset to Default]`, dan `[Save]` tidak tampil
6. Klik tab Free Plan Settings dan amati panel tab
7. Verifikasi Tab Free Plan Settings termuat normal dengan field dan footer (kegagalan memuat tab Trial Settings tidak memengaruhi tab lain)
8. Lepas intercept pengambilan data Trial Settings

### TC-AC-LCS-26: Error load tab Free Plan Settings: pengambilan data gagal 500

9. Pasang intercept yang memaksa respons pengambilan data Free Plan Settings gagal 500
10. Klik tab Free Plan Settings pada tab bar
11. Verifikasi State gagal muat tampil: "Unable to load this data." (bukan empty state dan bukan field kosong)
12. Verifikasi Tombol `[Try Again]` tampil pada state gagal muat
13. Verifikasi Field, `[Reset to Default]`, dan `[Save]` tidak tampil
14. Klik tab Trial Settings dan amati panel tab
15. Verifikasi Tab Trial Settings termuat normal dengan field dan footer (kegagalan memuat tab Free Plan Settings tidak memengaruhi tab lain)
16. Lepas intercept pengambilan data Free Plan Settings

### TC-AC-LCS-27: Error load tab License Timing: pengambilan data gagal 500

17. Pasang intercept yang memaksa respons pengambilan data License Timing gagal 500
18. Klik tab License Timing pada tab bar
19. Verifikasi State gagal muat tampil: "Unable to load this data." (bukan empty state dan bukan field kosong)
20. Verifikasi Tombol `[Try Again]` tampil pada state gagal muat
21. Verifikasi Field, `[Reset to Default]`, dan `[Save]` tidak tampil
22. Lepas intercept pengambilan data License Timing

### TC-AC-LCS-28: Error load tab Client Lifecycle: pengambilan data gagal 500

23. Pasang intercept yang memaksa respons pengambilan data Client Lifecycle gagal 500
24. Klik tab Client Lifecycle pada tab bar
25. Verifikasi State gagal muat tampil: "Unable to load this data." (bukan empty state dan bukan field kosong)
26. Verifikasi Tombol `[Try Again]` tampil pada state gagal muat
27. Verifikasi Field, `[Reset to Default]`, dan `[Save]` tidak tampil
28. Lepas intercept pengambilan data Client Lifecycle

## Notes

- Langkah penghubung (S-03, S-09): klik tab pada blok TC 26 sampai 28 (TC memuat tab itu dari tab bar) dan pelepasan intercept di akhir tiap blok. Pada TC 25 intercept dipasang sebelum klik menu sidebar karena Precondition TC. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Endpoint pengambilan data per tab tidak disebut di TC; spec hanya menyebut "respons pengambilan data tab" tanpa URL karangan (S-13).
- Temuan untuk QA: TC 25 butir c dan d mengasersi absence field dan footer; spec menempatkannya sesudah `Verifikasi` state gagal muat dan `[Try Again]` sebagai anchor positif (bagian 8b butir 2).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
