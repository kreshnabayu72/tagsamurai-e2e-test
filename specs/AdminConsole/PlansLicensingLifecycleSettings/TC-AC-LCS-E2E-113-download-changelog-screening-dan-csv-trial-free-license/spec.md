---
id: TC-AC-LCS-E2E-113-download-changelog-screening-dan-csv-trial-free-license
title: "Download Changelog: Screening Overlay dan CSV Tab Trial Settings, Free Plan Settings, dan License Timing"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-415
  - TC-AC-LCS-416
  - TC-AC-LCS-417
  - TC-AC-LCS-418
coverage:
  web: automated
---

# Download Changelog: Screening Overlay dan CSV Tab Trial Settings, Free Plan Settings, dan License Timing

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed dataset Changelog kecil (3 entri, Pre-setup 9: 10, 11, 12 May 26; John Doe dan Sarah Thompson) untuk tab pada tabel "Parameter tab" lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- Spec hanya memeriksa nama berkas dan overlay Download; isi berkas diperiksa spec lain (binary buffer).
- Parameter tab (diulang di langkah 10 sampai 16):
  | Tab | Nama file |
  |---|---|
  | Trial Settings | Changelog-Lifecycle-Settings-Trial-Settings.csv |
  | Free Plan Settings | Changelog-Lifecycle-Settings-Free-Plan-Settings.csv |
  | License Timing | Changelog-Lifecycle-Settings-License-Timing.csv |
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-415: Screening overlay Download di toolbar modal Changelog

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Hover icon Download
4. Verifikasi tooltip "Download" tampil
5. Klik icon Download
6. Verifikasi overlay berisi dua opsi: "Download as CSV" dan "Download as XLSX"
7. Klik icon Download untuk menutup overlay
8. Tutup modal dengan `[✕]`

### TC-AC-LCS-416, TC-AC-LCS-417, TC-AC-LCS-418: Download as CSV riwayat tab Trial Settings, Free Plan Settings, dan License Timing menghasilkan berkas bernama sesuai tab tanpa toast sukses

9. Untuk setiap baris tabel "Parameter tab" pada Prerequisites, lakukan langkah 10 sampai 16
10. Klik tab sesuai kolom `Tab`
11. Klik icon Changelog di pojok kanan atas panel tab tersebut
12. Klik icon Download
13. Pilih "Download as CSV"
14. Verifikasi tidak ada toast sukses atau toast lain
15. Verifikasi berkas terunduh dengan nama sesuai kolom `Nama file`
16. Tutup modal dengan `[✕]`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah yang diulang per tab: langkah 10 sampai 16 (3 tab: Trial Settings, Free Plan Settings, License Timing); parameter tiap iterasi ada di tabel "Parameter tab" pada Prerequisites.
- Langkah penghubung: langkah 10 (pindah tab), menutup overlay Download dan menutup modal.
- Urutan langkah pada tiap blok: asersi absence toast (state sementara) ditulis tepat sesudah pemicu dan sebelum asersi berkas terunduh yang menjadi anchor-nya (bagian 8b butir 11), berbeda dari urutan butir Expected TC.
- Temuan untuk QA:
  - TC-AC-LCS-415 menyebut Dataset L tersedia pada modal Client Lifecycle, sedangkan TC-AC-LCS-419 (spec 114) memakai dataset kecil Client Lifecycle; screening overlay Download tidak bergantung jumlah entri sehingga spec ini memakai dataset kecil dan tidak mengasersi jumlah entri.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
