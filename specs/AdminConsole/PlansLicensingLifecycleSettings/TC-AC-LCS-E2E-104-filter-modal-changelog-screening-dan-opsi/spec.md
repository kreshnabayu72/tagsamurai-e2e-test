---
id: TC-AC-LCS-E2E-104-filter-modal-changelog-screening-dan-opsi
title: "Filter Panel Modal Changelog: Screening, Opsi Dropdown Field dan Modified By, serta Search dalam Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-386
  - TC-AC-LCS-387
  - TC-AC-LCS-388
  - TC-AC-LCS-389
coverage:
  web: automated
---

# Filter Panel Modal Changelog: Screening, Opsi Dropdown Field dan Modified By, serta Search dalam Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed Dataset L (27 entri Changelog tab Client Lifecycle, Pre-setup 8: entri ke-n pada n May 26 pukul 10:00, Action Edit, Old Value 5n, New Value 5n+3, Modified By berputar John Doe, Sarah Thompson, Budi Santoso) lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-386: Screening Filter Panel modal Changelog: tiga field filter tanpa filter Action

1. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
2. Hover icon Filter di toolbar modal
3. Verifikasi tooltip "Filter" tampil
4. Klik icon Filter
5. Susuri panel tanpa mengklik apa pun
6. Verifikasi panel berisi field berurutan: `Date` (date range picker) | `Field` (multi-select searchable, placeholder "All fields") | `Modified By` (multi-select searchable, placeholder "All users")
7. Verifikasi placeholder field `Date`: "Select date"
8. Verifikasi tidak ada field filter Action
9. Verifikasi tombol berurutan: `[Clear Field]` (kiri, Text) lalu `[Apply]` (kanan, filled)

### TC-AC-LCS-387: Opsi dropdown Field dipopulasi dari field yang tercatat pada log Client Lifecycle

10. Klik field `Field`
11. Verifikasi dropdown menampilkan tepat sembilan opsi: Notify Plan Owner Before Event, First Reminder Before Event, Second Reminder Before Event, Final Reminder Before Event, Grace Period Duration, Archive Period Duration, Purge Warning Email, Purge Urgent Warning Email, Post-Purge Retention (urutan opsi tidak diasersi)
12. Verifikasi tidak ada opsi untuk field yang tidak tercatat pada log (tidak ada opsi selain kesembilan opsi tersebut)
13. Tutup dropdown Field dengan klik area kosong pada panel Filter

### TC-AC-LCS-388: Opsi dropdown Modified By dipopulasi dari modifier yang ada pada baris log

14. Klik field `Modified By`
15. Verifikasi dropdown menampilkan tepat tiga opsi nama lengkap: Budi Santoso, John Doe, Sarah Thompson (bukan bentuk singkat `John D`)
16. Verifikasi tidak ada opsi untuk user yang tidak pernah melakukan Save (tidak ada opsi selain ketiga nama tersebut)
17. Tutup dropdown Modified By dengan klik area kosong pada panel Filter

### TC-AC-LCS-389: Search di dalam dropdown Field mempersempit opsi

18. Klik field `Field`
19. Ketik `Reminder` pada kotak search di dalam dropdown
20. Verifikasi tiga opsi tampil: First Reminder Before Event, Second Reminder Before Event, Final Reminder Before Event
21. Ketik `zz` pada kotak search yang sama
22. Verifikasi tidak ada opsi yang tampil
23. Verifikasi tabel modal tidak berubah selama pencarian di dalam dropdown (footer tetap `1–10 of 27`)

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: menutup dropdown dengan klik area kosong pada panel Filter antar TC (S-09).
- Kuantitas opsi dropdown ('tepat sembilan', 'tepat tiga') diturunkan dari Dataset L hasil seeding; urutan opsi tidak diasersi sesuai Expected TC.
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
