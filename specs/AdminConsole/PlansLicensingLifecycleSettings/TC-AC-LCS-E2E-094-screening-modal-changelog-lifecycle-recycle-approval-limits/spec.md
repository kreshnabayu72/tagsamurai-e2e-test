---
id: TC-AC-LCS-E2E-094-screening-modal-changelog-lifecycle-recycle-approval-limits
title: "Screening Modal Changelog Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-361
  - TC-AC-LCS-363
  - TC-AC-LCS-365
  - TC-AC-LCS-367
coverage:
  web: automated
---

# Screening Modal Changelog Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk menimpa atau mengosongkan riwayat Changelog per tab, idempotent (Lampiran A-15; dinyatakan di `suite.md`).
- Hook `before` men-seed dataset Changelog kecil (3 entri, Pre-setup 9) untuk tab pada tabel parameter lewat Fixture BE (menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- Parameter tab (diulang di langkah 2 sampai 15):
  | TC | Tab | Title modal | Baris 1 (12 May 26, 10:00) | Baris 2 (11 May 26, 10:00) | Baris 3 (10 May 26, 10:00) |
  |---|---|---|---|---|---|
  | TC-AC-LCS-361 | Client Lifecycle | Changelog: Lifecycle Settings > Client Lifecycle | Edit, Notify Plan Owner Before Event, 46, 47, John D | Edit, Post-Purge Retention, 730, 731, Sarah T | Edit, Notify Plan Owner Before Event, 45, 46, John D |
  | TC-AC-LCS-363 | Recycle Bin | Changelog: Lifecycle Settings > Recycle Bin | Edit, Permanently Delete Recycle Bin, 32, 33, John D | Edit, Permanently Delete Recycle Bin, 31, 32, Sarah T | Edit, Permanently Delete Recycle Bin, 30, 31, John D |
  | TC-AC-LCS-365 | Approval Settings | Changelog: Lifecycle Settings > Approval Settings | Edit, Approval Timeout, 5, 6, John D | Edit, Approval Timeout, 4, 5, Sarah T | Edit, Approval Timeout, 3, 4, John D |
  | TC-AC-LCS-367 | System Limits | Changelog: Lifecycle Settings > System Limits | Edit, Bulk Transaction Row Limit, 1001, 1002, John D | Edit, Max Visible Columns, 20, 21, Sarah T | Edit, Bulk Transaction Row Limit, 1000, 1001, John D |
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`: nilai default tiap tab dan dataset Changelog).
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

1. Untuk setiap baris tabel "Parameter tab" pada Prerequisites, lakukan langkah 2 sampai 15
2. Klik tab sesuai kolom `Tab`
3. Klik icon Changelog di pojok kanan atas panel tab tersebut
4. Verifikasi Header: Title modal sesuai kolom `Title modal`
5. Verifikasi Header: tombol close `[✕]`
6. Verifikasi Header: Table Tools `Search | Filter | Download`
7. Verifikasi Body: kolom `Date (sortable) | Action (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable — header klik = buka overlay Column Visibility)`
8. Verifikasi Body: tidak ada kolom Tab dan tidak ada kolom Object
9. Verifikasi Body: baris 1 (urutan Newest First) `12 May 26` jam `10:00` dengan nilai kolom `Baris 1`
10. Verifikasi Body: baris 2 (urutan Newest First) `11 May 26` jam `10:00` dengan nilai kolom `Baris 2`
11. Verifikasi Body: baris 3 (urutan Newest First) `10 May 26` jam `10:00` dengan nilai kolom `Baris 3`
12. Verifikasi Body: kolom Action tampil plain text `Edit` (bukan badge)
13. Verifikasi Body: Modified By tampil plain text format `[first name lengkap] [huruf pertama last name]`
14. Verifikasi Footer: Pagination default 10 per halaman: `1–3 of 3`
15. Tutup modal dengan `[✕]`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` tidak dipakai karena seluruh TC berbentuk satu blok yang diulang per tab.
- Langkah yang diulang per tab: langkah 2 sampai 15 (4 tab: Client Lifecycle, Recycle Bin, Approval Settings, System Limits); parameter tiap iterasi ada di tabel "Parameter tab" pada Prerequisites. Tiap `Verifikasi` tetap satu per klausa (S-01).
- Langkah penghubung: langkah 2 (pindah tab) dan langkah 15 (menutup modal).
- Pengecualian A-15: total absolut `1–3 of 3` diasersi karena riwayat tiap tab ditimpa lewat Fixture BE di hook `before` sebelum modal dibuka; hook `after` mengembalikan dataset Changelog.
- Setelah ekspansi blok ulang spec ini melewati sekitar 35 langkah (di atas smell): 4 tab x 14 langkah = 56 langkah ekspansi. Alasan mempertahankan satu spec: seluruh blok satu kelas (screening modal Changelog), identik, dan berdiri sendiri; kegagalan satu tab tidak membuat blok tab lain kehilangan makna.
