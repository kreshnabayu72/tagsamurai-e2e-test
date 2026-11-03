---
id: TC-FA-LIC-E2E-074-allocation-history-column-visibility-dan-setup-column
title: "Allocation History: Screening Overlay Column Visibility dan Popup Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-249
  - TC-FA-LIC-250
coverage:
  web: automated
---
# Allocation History: Screening Overlay Column Visibility dan Popup Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Allocation History, hanya dibaca): enam alokasi lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 (urutan default Last Updated terbaru lebih dulu; Plan Owner seluruhnya PT Maju Bersama (Distributor); LALC-20250210-00001 berstatus Expired, SUBS-20250101-00001; Quantity LALC-20260101-00001 = 3000 dan LALC-20260312-00002 = +1500).
- Daftar kolom Hideable Visible default (dibaca langkah 3): `Allocation ID`, `Subscription ID`, `License Type`, `Quantity`, `Status`, `Date`, `End Date`, `Plan Owner`, `Last Updated` (sembilan kolom).
- Spec ini hanya membuka dan menutup overlay dan popup tanpa menyimpan perubahan kolom, sehingga tidak ada konfigurasi kolom yang perlu dipulihkan.

## Test Steps

1. Klik sub-tab `Allocation History`

### TC-FA-LIC-249: Screening overlay Column Visibility

2. Klik header kolom Actions `⋯`
3. Verifikasi overlay menampilkan daftar kolom berurutan: `Allocation ID`, `Subscription ID`, `License Type`, `Quantity`, `Status`, `Date`, `End Date`, `Plan Owner`, `Last Updated`
4. Verifikasi tiap kolom pada daftar memiliki checkbox tercentang dan drag handle
5. Verifikasi item `Setup Column...` di bagian bawah panel
6. Tutup overlay Column Visibility

### TC-FA-LIC-250: Screening Popup Setup Column

7. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
8. Verifikasi Title header popup `Setup Column`
9. Verifikasi deskripsi header `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
10. Verifikasi tombol `(×)` pada header
11. Verifikasi body memuat daftar kolom dengan checkbox, drag handle, dan ikon Pin
12. Verifikasi body memuat Live Preview tabel
13. Verifikasi footer memuat `[Reset to Default]` dan `[Save]`
14. Verifikasi footer tidak memuat `[Cancel]`
15. Klik `(×)` untuk menutup popup

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE. Ceklis per kolom (TC-FA-LIC-251) ada di spec `TC-FA-LIC-E2E-150` dan geser per kolom (TC-FA-LIC-252) di spec `TC-FA-LIC-E2E-151`.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 6 dan 15 (menutup overlay dan popup).
- Temuan untuk QA:
  - TC-FA-LIC-249 dan 250 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
