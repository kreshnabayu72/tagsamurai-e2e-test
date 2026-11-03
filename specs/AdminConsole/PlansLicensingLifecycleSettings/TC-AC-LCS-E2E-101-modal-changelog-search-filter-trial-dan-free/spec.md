---
id: TC-AC-LCS-E2E-101-modal-changelog-search-filter-trial-dan-free
title: "Modal Changelog Tab Trial Settings dan Free Plan Settings: Search dan Filter pada Dataset Kecil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-658
  - TC-AC-LCS-659
  - TC-AC-LCS-660
  - TC-AC-LCS-661
  - TC-AC-LCS-662
coverage:
  web: automated
---

# Modal Changelog Tab Trial Settings dan Free Plan Settings: Search dan Filter pada Dataset Kecil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed dataset Changelog kecil (3 entri, Pre-setup 9: 10, 11, 12 May 26; John Doe dan Sarah Thompson) untuk tab Trial Settings dan Free Plan Settings lewat Fixture BE; hook `after` mengembalikan dataset ke keadaan awal.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-658: Search kata kunci Thompson pada modal Changelog tab Trial Settings menyaring satu entri dan urutan awal Newest First

1. Klik icon Changelog di pojok kanan atas panel tab Trial Settings
2. Verifikasi urutan baris dari atas: `12 May 26` jam `10:00`, Edit, Max Trial Duration, 31, 32, John D; `11 May 26` jam `10:00`, Edit, Require Approval for Trial Activation, Off, On, Sarah T; `10 May 26` jam `10:00`, Edit, Max Trial Duration, 30, 31, John D
3. Ketik Search `Thompson`, tekan Enter
4. Verifikasi footer `1–1 of 1`
5. Verifikasi baris: `11 May 26` jam `10:00`, Edit, Require Approval for Trial Activation, Off, On, Sarah T
6. Klik `(←)` pada kotak Search

### TC-AC-LCS-659: Opsi filter Field dan Modified By modal Changelog tab Trial Settings dipopulasi dari riwayat tab itu

7. Klik icon Filter
8. Klik field `Field`
9. Verifikasi dropdown Field menampilkan tepat dua opsi: Max Trial Duration, Require Approval for Trial Activation (urutan opsi tidak diasersi)
10. Klik field `Modified By`
11. Verifikasi dropdown Modified By menampilkan tepat dua opsi nama lengkap: John Doe, Sarah Thompson

### TC-AC-LCS-660: Filter Field Require Approval for Trial Activation pada modal Changelog tab Trial Settings menyaring satu entri

12. Pilih `Require Approval for Trial Activation` pada field `Field`, tutup dropdown, klik `[Apply]`
13. Verifikasi footer `1–1 of 1`
14. Verifikasi baris 1: `11 May 26` jam `10:00`, Edit, Require Approval for Trial Activation, Off, On, Sarah T
15. Tutup modal dengan `[✕]`

### TC-AC-LCS-661: Search kata kunci Thompson pada modal Changelog tab Free Plan Settings menyaring satu entri dan urutan awal Newest First

16. Klik tab Free Plan Settings
17. Klik icon Changelog di pojok kanan atas panel tab Free Plan Settings
18. Verifikasi urutan baris dari atas: `12 May 26` jam `10:00`, Edit, Free Plan Duration, 367, 368, John D; `11 May 26` jam `10:00`, Edit, Free Plan Duration, 366, 367, Sarah T; `10 May 26` jam `10:00`, Edit, Free Plan Duration, 365, 366, John D
19. Ketik Search `Thompson`, tekan Enter
20. Verifikasi footer `1–1 of 1`
21. Verifikasi baris: `11 May 26` jam `10:00`, Edit, Free Plan Duration, 366, 367, Sarah T
22. Klik `(←)` pada kotak Search

### TC-AC-LCS-662: Filter Panel modal Changelog tab Free Plan Settings tidak menampilkan filter Field karena hanya ada satu nilai Field

23. Klik icon Filter
24. Verifikasi panel berisi field berurutan: `Date` (date range picker, placeholder "Select date") | `Modified By` (multi-select searchable, placeholder "All users")
25. Verifikasi tidak ada field filter Field dan tidak ada field filter Action
26. Verifikasi tombol berurutan: `[Clear Field]` (kiri, Text) lalu `[Apply]` (kanan, filled)
27. Tutup modal dengan `[✕]`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: klik `(←)` pada kotak Search sesudah tiap TC Search (menutup input dan mereset tabel, S-09) dan menutup modal sebelum berpindah tab.
- Filter tab dengan satu nilai Field (Free Plan Settings, Recycle Bin, Approval Settings) tidak menampilkan field filter Field (NC-18); asersi absence field Field memakai panel yang sudah termuat (field Date dan Modified By tampil) sebagai anchor.
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
