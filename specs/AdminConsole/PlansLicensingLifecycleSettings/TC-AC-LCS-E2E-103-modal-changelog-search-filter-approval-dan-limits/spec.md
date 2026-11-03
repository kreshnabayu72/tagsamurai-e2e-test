---
id: TC-AC-LCS-E2E-103-modal-changelog-search-filter-approval-dan-limits
title: "Modal Changelog Tab Approval Settings dan System Limits: Search dan Filter pada Dataset Kecil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-668
  - TC-AC-LCS-669
  - TC-AC-LCS-670
  - TC-AC-LCS-671
  - TC-AC-LCS-672
coverage:
  web: automated
---

# Modal Changelog Tab Approval Settings dan System Limits: Search dan Filter pada Dataset Kecil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed dataset Changelog kecil (3 entri, Pre-setup 9: 10, 11, 12 May 26; John Doe dan Sarah Thompson) untuk tab Approval Settings dan System Limits lewat Fixture BE; hook `after` mengembalikan dataset ke keadaan awal.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-668: Search kata kunci Thompson pada modal Changelog tab Approval Settings menyaring satu entri dan urutan awal Newest First

1. Klik tab Approval Settings
2. Klik icon Changelog di pojok kanan atas panel tab Approval Settings
3. Verifikasi urutan baris dari atas: `12 May 26` jam `10:00`, Edit, Approval Timeout, 5, 6, John D; `11 May 26` jam `10:00`, Edit, Approval Timeout, 4, 5, Sarah T; `10 May 26` jam `10:00`, Edit, Approval Timeout, 3, 4, John D
4. Ketik Search `Thompson`, tekan Enter
5. Verifikasi footer `1–1 of 1`
6. Verifikasi baris: `11 May 26` jam `10:00`, Edit, Approval Timeout, 4, 5, Sarah T
7. Klik `(←)` pada kotak Search

### TC-AC-LCS-669: Filter Panel modal Changelog tab Approval Settings tidak menampilkan filter Field karena hanya ada satu nilai Field

8. Klik icon Filter
9. Verifikasi panel berisi field berurutan: `Date` (date range picker, placeholder "Select date") | `Modified By` (multi-select searchable, placeholder "All users")
10. Verifikasi tidak ada field filter Field dan tidak ada field filter Action
11. Verifikasi tombol berurutan: `[Clear Field]` (kiri, Text) lalu `[Apply]` (kanan, filled)
12. Tutup modal dengan `[✕]`

### TC-AC-LCS-670: Search kata kunci Thompson pada modal Changelog tab System Limits menyaring satu entri dan urutan awal Newest First

13. Klik tab System Limits
14. Klik icon Changelog di pojok kanan atas panel tab System Limits
15. Verifikasi urutan baris dari atas: `12 May 26` jam `10:00`, Edit, Bulk Transaction Row Limit, 1001, 1002, John D; `11 May 26` jam `10:00`, Edit, Max Visible Columns, 20, 21, Sarah T; `10 May 26` jam `10:00`, Edit, Bulk Transaction Row Limit, 1000, 1001, John D
16. Ketik Search `Thompson`, tekan Enter
17. Verifikasi footer `1–1 of 1`
18. Verifikasi baris: `11 May 26` jam `10:00`, Edit, Max Visible Columns, 20, 21, Sarah T
19. Klik `(←)` pada kotak Search

### TC-AC-LCS-671: Opsi filter Field dan Modified By modal Changelog tab System Limits dipopulasi dari riwayat tab itu

20. Klik icon Filter
21. Klik field `Field`
22. Verifikasi dropdown Field menampilkan tepat dua opsi: Bulk Transaction Row Limit, Max Visible Columns (urutan opsi tidak diasersi)
23. Klik field `Modified By`
24. Verifikasi dropdown Modified By menampilkan tepat dua opsi nama lengkap: John Doe, Sarah Thompson

### TC-AC-LCS-672: Filter Field Max Visible Columns pada modal Changelog tab System Limits menyaring satu entri

25. Pilih `Max Visible Columns` pada field `Field`, tutup dropdown, klik `[Apply]`
26. Verifikasi footer `1–1 of 1`
27. Verifikasi baris 1: `11 May 26` jam `10:00`, Edit, Max Visible Columns, 20, 21, Sarah T
28. Tutup modal dengan `[✕]`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: klik `(←)` pada kotak Search sesudah tiap TC Search (menutup input dan mereset tabel, S-09) dan menutup modal sebelum berpindah tab.
- Filter tab dengan satu nilai Field (Free Plan Settings, Recycle Bin, Approval Settings) tidak menampilkan field filter Field (NC-18); asersi absence field Field memakai panel yang sudah termuat (field Date dan Modified By tampil) sebagai anchor.
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
