---
id: TC-AC-LCS-E2E-107-sort-modal-changelog-default-date-field-action
title: "Sort Modal Changelog: Urutan Default, Siklus Tiga Klik Date, Field, dan Action"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-399
  - TC-AC-LCS-400
  - TC-AC-LCS-401
  - TC-AC-LCS-402
coverage:
  web: automated
---

# Sort Modal Changelog: Urutan Default, Siklus Tiga Klik Date, Field, dan Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Hook `before` men-seed Dataset L (27 entri Changelog tab Client Lifecycle, Pre-setup 8: entri ke-n pada n May 26 pukul 10:00, Action Edit, Old Value 5n, New Value 5n+3, Modified By berputar John Doe, Sarah Thompson, Budi Santoso) lewat Fixture BE (kemampuan disediakan tim FE/BE; menimpa riwayat tab itu); hook `after` mengembalikan dataset ke keadaan awal.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Pengecualian A-15: Fixture BE menyediakan kemampuan overwrite dan clear riwayat Changelog per tab (disediakan tim FE/BE, idempotent); total absolut Changelog (footer `1-N of N`, jumlah baris, empty state) diasersi pada riwayat yang dibentuk di hook `before` spec ini dan dikembalikan di hook `after` suite; suite berjalan serial (`parallel: false`).
- Data uji mengacu ke berkas `fixtures/lifecycle-settings.json` (`Fixture.lifecycleSettings`: nilai default tiap tab dan dataset Changelog).
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-399: Urutan default modal Changelog adalah Date Newest First

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Verifikasi footer `1–10 of 27`
4. Verifikasi baris 1: `27 May 26` jam `10:00`, Edit, Post-Purge Retention, 135, 138, Budi S
5. Verifikasi baris 10: `18 May 26` jam `10:00`, Edit, Post-Purge Retention, 90, 93, Budi S

### TC-AC-LCS-400: Siklus 3 klik pada header Date: Oldest First, Newest First, netral

6. Klik header `Date` satu kali
7. Verifikasi ascending (Oldest First) baris 1: `01 May 26` jam `10:00`, Edit, Notify Plan Owner Before Event, 5, 8, John D
8. Klik header `Date` kedua kali
9. Verifikasi descending (Newest First) baris 1: `27 May 26` jam `10:00`, Edit, Post-Purge Retention, 135, 138, Budi S
10. Klik header `Date` ketiga kali
11. Verifikasi indikator sort pada Date non-aktif
12. Verifikasi urutan kembali ke default dengan baris 1: `27 May 26` jam `10:00`, Edit, Post-Purge Retention, 135, 138, Budi S

### TC-AC-LCS-401: Sort kolom Field alfabetis A–Z lalu Z–A

13. Klik header `Field` satu kali
14. Verifikasi A–Z baris 1 bernilai Field `Archive Period Duration`
15. Klik header `Field` kedua kali
16. Verifikasi Z–A baris 1 bernilai Field `Second Reminder Before Event`
17. Klik header `Field` ketiga kali (kembali netral)

### TC-AC-LCS-402: Sort kolom Action alfabetis tidak mengubah isi karena seluruh nilai Edit

18. Klik header `Action` satu kali
19. Verifikasi seluruh baris (sedikitnya satu baris tampil) bernilai `Edit`
20. Verifikasi indikator panah pada header Action aktif naik
21. Klik header `Action` kedua kali
22. Verifikasi seluruh baris (sedikitnya satu baris tampil) bernilai `Edit`
23. Verifikasi indikator panah pada header Action aktif turun
24. Klik header `Action` ketiga kali (kembali netral)

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1 (membuka tab Client Lifecycle, karena hook `beforeEach` membuka tab Trial Settings); klik ketiga pada header Field dan Action mengembalikan sort ke netral sebelum TC berikutnya (S-09).
- Pengecualian A-15: total absolut Changelog (footer, jumlah baris, empty state) diasersi pada riwayat hasil overwrite lewat Fixture BE di hook `before`; spec tidak mereset riwayat di tengah langkah.
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
