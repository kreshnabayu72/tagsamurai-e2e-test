---
id: TC-AC-LCS-E2E-114-download-changelog-csv-client-lifecycle-recycle-approval-limits
title: "Download Changelog CSV Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-419
  - TC-AC-LCS-420
  - TC-AC-LCS-421
  - TC-AC-LCS-422
coverage:
  web: automated
---

# Download Changelog CSV Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed dataset Changelog kecil (3 entri, Pre-setup 9: 10, 11, 12 May 26; John Doe dan Sarah Thompson) untuk tab pada tabel "Parameter tab" lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- Spec hanya memeriksa nama berkas; isi berkas diperiksa spec lain (binary buffer).
- Parameter tab (diulang di langkah 2 sampai 8):
  | Tab | Nama file |
  |---|---|
  | Client Lifecycle | Changelog-Lifecycle-Settings-Client-Lifecycle.csv |
  | Recycle Bin | Changelog-Lifecycle-Settings-Recycle-Bin.csv |
  | Approval Settings | Changelog-Lifecycle-Settings-Approval-Settings.csv |
  | System Limits | Changelog-Lifecycle-Settings-System-Limits.csv |
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

1. Untuk setiap baris tabel "Parameter tab" pada Prerequisites, lakukan langkah 2 sampai 8
2. Klik tab sesuai kolom `Tab`
3. Klik icon Changelog di pojok kanan atas panel tab tersebut
4. Klik icon Download
5. Pilih "Download as CSV"
6. Verifikasi tidak ada toast sukses atau toast lain
7. Verifikasi berkas terunduh dengan nama sesuai kolom `Nama file`
8. Tutup modal dengan `[✕]`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` tidak dipakai karena seluruh TC berbentuk satu blok yang diulang per tab.
- Langkah yang diulang per tab: langkah 2 sampai 8 (4 tab: Client Lifecycle, Recycle Bin, Approval Settings, System Limits); parameter tiap iterasi ada di tabel "Parameter tab" pada Prerequisites.
- Langkah penghubung: langkah 2 (pindah tab) dan langkah 8 (menutup modal).
- Urutan langkah pada tiap blok: asersi absence toast (state sementara) ditulis tepat sesudah pemicu dan sebelum asersi berkas terunduh yang menjadi anchor-nya (bagian 8b butir 11), berbeda dari urutan butir Expected TC.
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
