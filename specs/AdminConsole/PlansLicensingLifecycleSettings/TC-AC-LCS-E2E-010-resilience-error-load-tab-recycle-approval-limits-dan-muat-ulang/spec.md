---
id: TC-AC-LCS-E2E-010-resilience-error-load-tab-recycle-approval-limits-dan-muat-ulang
title: "Resilience Error Load 500 Tab Recycle Bin, Approval Settings, System Limits, dan Muat Ulang dari State Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-29
  - TC-AC-LCS-30
  - TC-AC-LCS-31
  - TC-AC-LCS-32
coverage:
  web: automated
---

# Resilience Error Load 500 Tab Recycle Bin, Approval Settings, System Limits, dan Muat Ulang dari State Gagal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); `Spectra.intercept` untuk memaksa respons pengambilan data tiap tab gagal 500 (TC 32: gagal pada percobaan pertama, sukses pada percobaan berikutnya) di atas backend nyata; intercept dilepas segera setelah asersi tiap blok (S-09).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-29: Error load tab Recycle Bin: pengambilan data gagal 500

1. Pasang intercept yang memaksa respons pengambilan data Recycle Bin gagal 500
2. Klik tab Recycle Bin pada tab bar
3. Verifikasi State gagal muat tampil: "Unable to load this data." (bukan empty state dan bukan field kosong)
4. Verifikasi Tombol `[Try Again]` tampil pada state gagal muat
5. Verifikasi Field, `[Reset to Default]`, dan `[Save]` tidak tampil
6. Lepas intercept pengambilan data Recycle Bin

### TC-AC-LCS-30: Error load tab Approval Settings: pengambilan data gagal 500

7. Pasang intercept yang memaksa respons pengambilan data Approval Settings gagal 500
8. Klik tab Approval Settings pada tab bar
9. Verifikasi State gagal muat tampil: "Unable to load this data." (bukan empty state dan bukan field kosong)
10. Verifikasi Tombol `[Try Again]` tampil pada state gagal muat
11. Verifikasi Field, `[Reset to Default]`, dan `[Save]` tidak tampil
12. Lepas intercept pengambilan data Approval Settings

### TC-AC-LCS-31: Error load tab System Limits: pengambilan data gagal 500

13. Pasang intercept yang memaksa respons pengambilan data System Limits gagal 500
14. Klik tab System Limits pada tab bar
15. Verifikasi State gagal muat tampil: "Unable to load this data." (bukan empty state dan bukan field kosong)
16. Verifikasi Tombol `[Try Again]` tampil pada state gagal muat
17. Verifikasi Field, `[Reset to Default]`, dan `[Save]` tidak tampil
18. Lepas intercept pengambilan data System Limits

### TC-AC-LCS-32: Muat ulang dari state gagal muat memulihkan tab Client Lifecycle

19. Pasang intercept yang memaksa respons pengambilan data Client Lifecycle gagal 500 pada percobaan pertama dan sukses pada percobaan berikutnya
20. Klik tab Client Lifecycle pada tab bar
21. Verifikasi State gagal muat tampil pada tab Client Lifecycle
22. Klik tombol muat ulang `[Try Again]` pada state gagal muat
23. Verifikasi Loading component tampil sesaat
24. Verifikasi Field Client Lifecycle tampil dengan nilai default `45`, `30`, `7`, `1`, `30`, `30`, `10`, `2`, `730`
25. Verifikasi Footer `[Reset to Default]` dan `[Save]` (disabled) tampil
26. Lepas intercept pengambilan data Client Lifecycle

## Notes

- Langkah penghubung (S-03, S-09): pelepasan intercept di akhir tiap blok. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Temuan untuk QA: TC 32 menyebut "tombol muat ulang" sedangkan TC 25 sampai 31 menyebut `[Try Again]` pada state gagal muat yang sama; spec memakai `[Try Again]` dan mengasumsikan keduanya tombol yang sama.
- Temuan untuk QA: TC 32 butir a ("Loading component tampil sesaat") rawan terlewat karena respons sukses cepat; TC tidak menyatakan penahanan respons percobaan kedua. Spec mengikuti TC dan tidak menambah penahanan respons.
- Temuan untuk QA: TC 32 langkah 1 menyebut "state gagal muat tampil" sebagai hasil langkah (tanpa butir Expected); spec menulis `Verifikasi` sebagai anchor sebelum klik `[Try Again]`.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
