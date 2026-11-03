---
id: TC-AC-LCS-E2E-028-capability-dicabut-saat-form-terbuka
title: "Capability Update Dicabut Saat Form Terbuka: Save Trial Settings dan Reset Recycle Bin Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-93
  - TC-AC-LCS-94
coverage:
  web: automated
---

# Capability Update Dicabut Saat Form Terbuka: Save Trial Settings dan Reset Recycle Bin Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage plans & licensing (Read dan Update) `managePlansLicensingAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Kusuma`), password dari `Spectra.env.AC_MPL_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Role yang diuji:

| Role | Akun | Env var password |
|---|---|---|
| Manage plans & licensing (Read dan Update) | `managePlansLicensingAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_MPL_PASSWORD` |

- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`).
- Pelaku kedua: administrator Total Control (akun default suite, `Spectra.env.AC_TC_PASSWORD`) lewat sesi API untuk mencabut dan memulihkan capability Update "Manage plans & licensing" pada role aktor; sesi API tidak mengusir sesi UI aktor (bagian 5, KEPUTUSAN 2026-10-30). Mekanisme pencabutan dan pemulihan capability tidak didefinisikan di TC, PRD, atau LLD: disediakan tim FE/BE tanpa endpoint karangan (S-13). Hook `after` spec ini memulihkan capability bila spec gagal di tengah.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings serta penyetelan nilai tersimpan Permanently Delete Recycle Bin untuk TC 94, disediakan tim FE/BE); sesi API administrator Total Control untuk mencabut dan memulihkan capability (disediakan tim FE/BE).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI. Capability role aktor dipulihkan di akhir tiap blok TC dan di hook `after` spec ini.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-93: Save ditolak saat capability Update dicabut ketika form tab Trial Settings masih terbuka

1. Aktor mengubah Max Trial Duration dari `30` menjadi `45` (belum disimpan)
2. Cabut capability Update "Manage plans & licensing" dari role aktor lewat sesi API administrator Total Control hingga pencabutan tersimpan
3. Tunggu aksi selesai (pencabutan capability tersimpan)
4. Klik `[Save]` pada sesi aktor
5. Verifikasi Toast error: "You don't have permission to do this."
6. Verifikasi Antarmuka dimuat ulang
7. Verifikasi Field tab Trial Settings Disabled
8. Verifikasi `[Save]` dan `[Reset to Default]` Hidden
9. Verifikasi Max Trial Duration bernilai tersimpan `30`
10. Pulihkan capability Update "Manage plans & licensing" pada role aktor lewat sesi API administrator Total Control hingga pemulihan tersimpan
11. Tunggu aksi selesai (pemulihan capability tersimpan)

### TC-AC-LCS-94: Reset to Default ditolak saat capability Update dicabut ketika form tab Recycle Bin masih terbuka

12. Atur Permanently Delete Recycle Bin tersimpan `31` lewat Fixture BE
13. Muat ulang halaman dengan F5 pada sesi aktor
14. Klik tab Recycle Bin pada tab bar
15. Cabut capability Update "Manage plans & licensing" dari role aktor lewat sesi API administrator Total Control hingga pencabutan tersimpan
16. Tunggu aksi selesai (pencabutan capability tersimpan)
17. Klik `[Reset to Default]` pada sesi aktor
18. Verifikasi Toast error: "You don't have permission to do this."
19. Verifikasi Antarmuka dimuat ulang
20. Verifikasi Field tab Recycle Bin Disabled
21. Verifikasi `[Save]` dan `[Reset to Default]` Hidden
22. Verifikasi Permanently Delete Recycle Bin bernilai tersimpan `31`
23. Pulihkan capability Update "Manage plans & licensing" pada role aktor lewat sesi API administrator Total Control hingga pemulihan tersimpan
24. Tunggu aksi selesai (pemulihan capability tersimpan)

## Notes

- TC 93 dan 94 bertanda `Manual Only` (dua sesi pengguna paralel) di TC; sesuai bagian 2 konvensi tetap ditulis. Pelaku kedua lewat sesi API bukan konteks UI kedua dan tidak memakai `P-2` (KEPUTUSAN 2026-10-30).
- Langkah penghubung (S-03, S-09): "Tunggu aksi selesai" sesudah pencabutan dan pemulihan capability (aksi tanpa asersi sebelum pindah aktor); pemulihan capability di akhir tiap blok; "Muat ulang halaman dengan F5" dan klik tab Recycle Bin memulai TC 94 dari tab Recycle Bin dengan capability aktif (Precondition TC). Aktor mengubah nilai pada TC 93 sebelum capability dicabut sesuai urutan TC.
- Langkah penghubung (S-03, S-04): langkah 12 membentuk Precondition d TC 94 (nilai tersimpan Permanently Delete Recycle Bin `31`, bukan default `30`) lewat Fixture BE sebelum muat ulang, sehingga Reset to Default yang ditolak dapat dibedakan dari yang berhasil.
- Temuan untuk QA: TC 93 dan 94 menyebut "sesi administrator kedua" tanpa menyebut akun dan sarananya; spec memakai Total Control lewat sesi API. TC 94 Precondition tidak menyatakan capability sudah dipulihkan sesudah TC 93 (spec memulihkannya).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
