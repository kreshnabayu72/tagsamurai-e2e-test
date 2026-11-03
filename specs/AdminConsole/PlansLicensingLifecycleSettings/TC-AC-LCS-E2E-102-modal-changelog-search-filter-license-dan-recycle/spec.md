---
id: TC-AC-LCS-E2E-102-modal-changelog-search-filter-license-dan-recycle
title: "Modal Changelog Tab License Timing dan Recycle Bin: Search dan Filter pada Dataset Kecil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-663
  - TC-AC-LCS-664
  - TC-AC-LCS-665
  - TC-AC-LCS-666
  - TC-AC-LCS-667
coverage:
  web: automated
---

# Modal Changelog Tab License Timing dan Recycle Bin: Search dan Filter pada Dataset Kecil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed dataset Changelog kecil (3 entri, Pre-setup 9: 10, 11, 12 May 26; John Doe dan Sarah Thompson) untuk tab License Timing dan Recycle Bin lewat Fixture BE; hook `after` mengembalikan dataset ke keadaan awal.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Pengecualian A-15: Fixture BE menyediakan kemampuan overwrite dan clear riwayat Changelog per tab (disediakan tim FE/BE, idempotent); total absolut Changelog (footer `1-N of N`, jumlah baris, empty state) diasersi pada riwayat yang dibentuk di hook `before` spec ini dan dikembalikan di hook `after` suite; suite berjalan serial (`parallel: false`).
- Data uji mengacu ke berkas `fixtures/lifecycle-settings.json` (`Fixture.lifecycleSettings`: nilai default tiap tab dan dataset Changelog).
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-663: Search kata kunci Thompson pada modal Changelog tab License Timing menyaring satu entri dan urutan awal Newest First

1. Klik tab License Timing
2. Klik icon Changelog di pojok kanan atas panel tab License Timing
3. Verifikasi urutan baris dari atas: `12 May 26` jam `10:00`, Edit, Managed Transition Time, 25, 26, John D; `11 May 26` jam `10:00`, Edit, Addon Reactivation Delay, 2, 3, Sarah T; `10 May 26` jam `10:00`, Edit, Managed Transition Time, 24, 25, John D
4. Ketik Search `Thompson`, tekan Enter
5. Verifikasi footer `1–1 of 1`
6. Verifikasi baris: `11 May 26` jam `10:00`, Edit, Addon Reactivation Delay, 2, 3, Sarah T
7. Klik `(←)` pada kotak Search

### TC-AC-LCS-664: Opsi filter Field dan Modified By modal Changelog tab License Timing dipopulasi dari riwayat tab itu

8. Klik icon Filter
9. Klik field `Field`
10. Verifikasi dropdown Field menampilkan tepat dua opsi: Managed Transition Time, Addon Reactivation Delay (urutan opsi tidak diasersi)
11. Klik field `Modified By`
12. Verifikasi dropdown Modified By menampilkan tepat dua opsi nama lengkap: John Doe, Sarah Thompson

### TC-AC-LCS-665: Filter Field Addon Reactivation Delay pada modal Changelog tab License Timing menyaring satu entri

13. Pilih `Addon Reactivation Delay` pada field `Field`, tutup dropdown, klik `[Apply]`
14. Verifikasi footer `1–1 of 1`
15. Verifikasi baris 1: `11 May 26` jam `10:00`, Edit, Addon Reactivation Delay, 2, 3, Sarah T
16. Tutup modal dengan `[✕]`

### TC-AC-LCS-666: Search kata kunci Thompson pada modal Changelog tab Recycle Bin menyaring satu entri dan urutan awal Newest First

17. Klik tab Recycle Bin
18. Klik icon Changelog di pojok kanan atas panel tab Recycle Bin
19. Verifikasi urutan baris dari atas: `12 May 26` jam `10:00`, Edit, Permanently Delete Recycle Bin, 32, 33, John D; `11 May 26` jam `10:00`, Edit, Permanently Delete Recycle Bin, 31, 32, Sarah T; `10 May 26` jam `10:00`, Edit, Permanently Delete Recycle Bin, 30, 31, John D
20. Ketik Search `Thompson`, tekan Enter
21. Verifikasi footer `1–1 of 1`
22. Verifikasi baris: `11 May 26` jam `10:00`, Edit, Permanently Delete Recycle Bin, 31, 32, Sarah T
23. Klik `(←)` pada kotak Search

### TC-AC-LCS-667: Filter Panel modal Changelog tab Recycle Bin tidak menampilkan filter Field karena hanya ada satu nilai Field

24. Klik icon Filter
25. Verifikasi panel berisi field berurutan: `Date` (date range picker, placeholder "Select date") | `Modified By` (multi-select searchable, placeholder "All users")
26. Verifikasi tidak ada field filter Field dan tidak ada field filter Action
27. Verifikasi tombol berurutan: `[Clear Field]` (kiri, Text) lalu `[Apply]` (kanan, filled)
28. Tutup modal dengan `[✕]`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: klik `(←)` pada kotak Search sesudah tiap TC Search (menutup input dan mereset tabel, S-09) dan menutup modal sebelum berpindah tab.
- Filter tab dengan satu nilai Field (Free Plan Settings, Recycle Bin, Approval Settings) tidak menampilkan field filter Field (NC-18); asersi absence field Field memakai panel yang sudah termuat (field Date dan Modified By tampil) sebagai anchor.
- Pengecualian A-15: total absolut Changelog (footer, jumlah baris, empty state) diasersi pada riwayat hasil overwrite lewat Fixture BE di hook `before`; spec tidak mereset riwayat di tengah langkah.
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
