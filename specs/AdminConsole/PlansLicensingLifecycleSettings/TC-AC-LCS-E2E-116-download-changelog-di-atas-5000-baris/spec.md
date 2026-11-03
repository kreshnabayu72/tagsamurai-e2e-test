---
id: TC-AC-LCS-E2E-116-download-changelog-di-atas-5000-baris
title: "Download Changelog di Atas 5.000 Baris: Loading Screen lalu Langsung Terunduh"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-684
coverage:
  web: automated
---

# Download Changelog di Atas 5.000 Baris: Loading Screen lalu Langsung Terunduh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed Changelog tab Client Lifecycle dengan 5.001 entri lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- Kemampuan teknis: kueri antrean job background lewat Fixture BE (disediakan tim FE/BE) untuk asersi bahwa tidak ada job background.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-684: Download Changelog dengan data di atas 5.000 baris menampilkan loading screen lalu langsung terunduh

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Klik icon Download
4. Pilih "Download as CSV"
5. Verifikasi loading screen tampil sampai berkas siap
6. Verifikasi tidak ada notifikasi yang tampil
7. Tunggu berkas siap
8. Verifikasi berkas `Changelog-Lifecycle-Settings-Client-Lifecycle.csv` langsung terunduh
9. Verifikasi berkas memuat 5.001 baris data
10. Verifikasi tidak ada job background (kueri antrean job lewat Fixture BE)

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah "Tunggu berkas siap" (menunggu berkas tanpa jeda waktu tetap).
- Urutan langkah pada tiap blok: asersi absence toast (state sementara) ditulis tepat sesudah pemicu dan sebelum asersi berkas terunduh yang menjadi anchor-nya (bagian 8b butir 11), berbeda dari urutan butir Expected TC.
- Temuan untuk QA:
  - TC-AC-LCS-684: Expected "tidak ada notifikasi maupun job background" tidak menyebut cara mengamati job background; spec memakai kemampuan kueri antrean job yang disediakan tim FE/BE tanpa endpoint karangan.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
