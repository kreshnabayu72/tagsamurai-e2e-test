---
id: TC-AC-LCS-E2E-115-download-changelog-xlsx-dan-mengikuti-search-dan-kolom-visible
title: "Download Changelog XLSX dan Download Mengikuti Search serta Kolom Visible"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-423
  - TC-AC-LCS-424
coverage:
  web: automated
---

# Download Changelog XLSX dan Download Mengikuti Search serta Kolom Visible

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed Dataset L (27 entri Changelog tab Client Lifecycle, Pre-setup 8: entri ke-n pada n May 26 pukul 10:00, Action Edit, Old Value 5n, New Value 5n+3, Modified By berputar John Doe, Sarah Thompson, Budi Santoso) lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- Kemampuan teknis: pembacaan isi berkas hasil unduhan (nama sheet, header, jumlah baris) lewat buffer, disediakan tim FE (spec ini memeriksa isi berkas, kelas binary buffer).
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Preferensi kolom modal Changelog (Column Visibility dan Setup Column) yang tersimpan di browser dihapus di hook `after` (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-423: Download as XLSX riwayat Client Lifecycle menghasilkan file .xlsx dengan kolom visible

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Klik icon Download
4. Pilih "Download as XLSX"
5. Verifikasi tidak ada toast sukses
6. Verifikasi berkas terunduh dengan nama `Changelog-Lifecycle-Settings-Client-Lifecycle.xlsx`
7. Buka berkas hasil unduhan
8. Verifikasi berkas memuat satu sheet bernama `Sheet1`
9. Verifikasi `Sheet1` memuat header `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
10. Verifikasi `Sheet1` memuat 27 baris data

### TC-AC-LCS-424: Download mengikuti Search dan Filter aktif serta kolom yang visible

11. Klik header Column Visibility `(⋯)`
12. Uncheck `Old Value`
13. Ketik Search `Grace`, tekan Enter
14. Klik icon Download
15. Pilih "Download as CSV"
16. Buka berkas hasil unduhan
17. Verifikasi berkas memuat tiga baris data (Field Grace Period Duration) dari seluruh hasil Search, bukan seluruh 27 entri
18. Verifikasi kolom `Date`, `Action`, `Field`, `New Value`, dan `Modified By` ada pada berkas
19. Verifikasi kolom `Old Value` tidak ada pada berkas

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Isi berkas diamati lewat pembacaan buffer. Spec mengikuti Langkah Uji TC-AC-LCS-424 yang hanya memakai Search dan Column Visibility (lihat Temuan untuk QA).
- Langkah penghubung: tidak ada selain langkah TC; konfigurasi kolom TC-AC-LCS-424 dihapus di hook `after`.
- Temuan untuk QA:
  - TC-AC-LCS-424: judul menyebut "Search dan Filter aktif" tetapi Langkah Uji dan Expected hanya memakai Search dan kolom visible; Filter tidak diuji.
  - TC-AC-LCS-423: Expected butir c ("Tidak ada toast sukses") ditulis di depan asersi berkas (bagian 8b butir 11).
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
