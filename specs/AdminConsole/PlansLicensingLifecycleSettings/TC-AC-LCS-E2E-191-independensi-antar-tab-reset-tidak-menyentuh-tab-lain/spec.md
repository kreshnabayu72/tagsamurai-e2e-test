---
id: TC-AC-LCS-E2E-191-independensi-antar-tab-reset-tidak-menyentuh-tab-lain
title: "Independensi Antar Tab: Reset to Default Tab Free Plan Settings Tidak Menyentuh Tab Trial Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-352
coverage:
  web: automated
---

# Independensi Antar Tab: Reset to Default Tab Free Plan Settings Tidak Menyentuh Tab Trial Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: Fixture BE mengatur nilai tersimpan Free Plan Duration `400` dan Max Trial Duration `45` di langkah 1 (precondition TC, tidak diasersi); kemampuan menangani dialog `beforeunload` saat muat ulang halaman dengan form dirty (langkah 12) disediakan tim FE.
- Data uji: Free Plan Duration `400` tersimpan, Max Trial Duration `45` tersimpan, Max Trial Asset Quota `75` (belum disimpan).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-352: Reset to Default pada satu tab tidak menyentuh tab lain dan tidak membuang perubahan belum disimpan di tab lain

1. Atur lewat Fixture BE: Free Plan Duration tersimpan `400` dan Max Trial Duration tersimpan `45`
2. Muat ulang halaman dengan F5
3. Klik tab Trial Settings
4. Ubah Max Trial Asset Quota dari `50` menjadi `75` (belum disimpan)
5. Klik tab Free Plan Settings
6. Klik `[Reset to Default]`
7. Verifikasi toast sukses "Success, free plan settings have been reset to default."
8. Verifikasi Free Plan Duration `365`
9. Klik tab Trial Settings
10. Verifikasi Max Trial Asset Quota tetap `75` (belum disimpan)
11. Verifikasi Max Trial Duration tetap `45`
12. Muat ulang halaman dengan F5
13. Klik tab Trial Settings
14. Verifikasi Max Trial Duration `45`
15. Verifikasi Max Trial Asset Quota `50`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Langkah penghubung: langkah 1 sampai 3 (menyiapkan precondition TC), langkah 12 (muat ulang saat form Trial dirty dengan dialog `beforeunload` dikonfirmasi, S-08), langkah 13 (kembali ke tab Trial Settings sesudah muat ulang).
- TC-AC-LCS-350 dan TC-AC-LCS-351 ada di spec 092 (`TC-AC-LCS-E2E-092-independensi-antar-tab-save-in-flight-dan-save-berhasil`).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-352 (Free Plan Duration tersimpan `365`; Trial Settings tidak berubah oleh Reset Free Plan Settings) dipenuhi oleh Expected langkah 12 sampai akhir; Post Condition tidak diasersi tersendiri.
