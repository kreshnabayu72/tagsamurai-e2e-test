---
id: TC-AC-LCS-E2E-096-empty-state-modal-changelog-lifecycle-recycle-approval-limits
title: "Empty State Modal Changelog Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-362
  - TC-AC-LCS-364
  - TC-AC-LCS-366
  - TC-AC-LCS-368
coverage:
  web: automated
---

# Empty State Modal Changelog Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` mengosongkan Changelog tab pada tabel parameter lewat Fixture BE (precondition TC: tab belum pernah di-Save; kemampuan disediakan tim FE/BE); hook `after` mengembalikan dataset Changelog ke keadaan awal.
- Parameter tab (diulang di langkah 2 sampai 6):
  | Tab | Title modal |
  |---|---|
  | Client Lifecycle | Changelog: Lifecycle Settings > Client Lifecycle |
  | Recycle Bin | Changelog: Lifecycle Settings > Recycle Bin |
  | Approval Settings | Changelog: Lifecycle Settings > Approval Settings |
  | System Limits | Changelog: Lifecycle Settings > System Limits |
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

1. Untuk setiap baris tabel "Parameter tab" pada Prerequisites, lakukan langkah 2 sampai 6
2. Klik tab sesuai kolom `Tab`
3. Klik icon Changelog di pojok kanan atas panel tab tersebut
4. Verifikasi Title modal sesuai kolom `Title modal`
5. Verifikasi Empty state: Illustration, Title "No changelog yet", Description "Activities and changes will appear here."
6. Tutup modal dengan `[✕]`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`.
- Langkah yang diulang per tab: langkah 2 sampai 6 (4 tab: Client Lifecycle, Recycle Bin, Approval Settings, System Limits); parameter ada di tabel "Parameter tab" pada Prerequisites.
- Langkah penghubung: langkah 2 (pindah tab) dan langkah 6 (menutup modal).
