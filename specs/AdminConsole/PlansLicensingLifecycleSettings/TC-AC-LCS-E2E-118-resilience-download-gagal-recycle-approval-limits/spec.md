---
id: TC-AC-LCS-E2E-118-resilience-download-gagal-recycle-approval-limits
title: "Resilience Download Changelog Gagal: Toast Error Tab Recycle Bin, Approval Settings, dan System Limits"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-429
  - TC-AC-LCS-430
  - TC-AC-LCS-431
coverage:
  web: automated
---

# Resilience Download Changelog Gagal: Toast Error Tab Recycle Bin, Approval Settings, dan System Limits

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed dataset Changelog kecil (3 entri, Pre-setup 9: 10, 11, 12 May 26; John Doe dan Sarah Thompson) untuk tab pada tabel "Parameter tab" lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- Kemampuan teknis: `Spectra.intercept` memaksa permintaan Download Changelog gagal dengan respons HTTP 500 (langkah 1); intercept dilepas di langkah 10 dan dipulihkan di hook `after` suite.
- Parameter tab (diulang di langkah 3 sampai 9):
  | Tab | Toast |
  |---|---|
  | Recycle Bin | Error, failed to download Changelog-Lifecycle-Settings-Recycle-Bin. |
  | Approval Settings | Error, failed to download Changelog-Lifecycle-Settings-Approval-Settings. |
  | System Limits | Error, failed to download Changelog-Lifecycle-Settings-System-Limits. |
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

1. Atur intercept: paksa permintaan Download Changelog gagal 500 (HTTP 500)
2. Untuk setiap baris tabel "Parameter tab" pada Prerequisites, lakukan langkah 3 sampai 9
3. Klik tab sesuai kolom `Tab`
4. Klik icon Changelog di pojok kanan atas panel tab tersebut
5. Klik icon Download
6. Pilih "Download as CSV"
7. Verifikasi toast error sesuai kolom `Toast`
8. Tunggu toast lama hilang otomatis
9. Tutup modal dengan `[✕]`
10. Lepas intercept permintaan Download Changelog

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` tidak dipakai karena seluruh TC berbentuk satu blok yang diulang per tab.
- Langkah yang diulang per tab: langkah 3 sampai 9 (3 tab: Recycle Bin, Approval Settings, System Limits); parameter tiap iterasi ada di tabel "Parameter tab" pada Prerequisites.
- Langkah penghubung: langkah 3 (pindah tab), "Tunggu toast lama hilang otomatis" supaya toast tab berikutnya tidak tertukar, menutup modal, dan melepas intercept.
- Intercept hanya memaksa kegagalan Download sebagai objek uji (kelas fault injection); spec tidak memuat TC kelas lain.
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
