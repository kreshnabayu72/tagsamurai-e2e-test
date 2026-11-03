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
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab dan dataset Changelog); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-399: Urutan default modal Changelog adalah Date Newest First

1. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
2. Verifikasi footer `1–10 of 27`
3. Verifikasi baris 1: `27 May 26` jam `10:00`, Edit, Post-Purge Retention, 135, 138, Budi S
4. Verifikasi baris 10: `18 May 26` jam `10:00`, Edit, Post-Purge Retention, 90, 93, Budi S

### TC-AC-LCS-400: Siklus 3 klik pada header Date: Oldest First, Newest First, netral

5. Klik header `Date` satu kali
6. Verifikasi ascending (Oldest First) baris 1: `01 May 26` jam `10:00`, Edit, Notify Plan Owner Before Event, 5, 8, John D
7. Klik header `Date` kedua kali
8. Verifikasi descending (Newest First) baris 1: `27 May 26` jam `10:00`, Edit, Post-Purge Retention, 135, 138, Budi S
9. Klik header `Date` ketiga kali
10. Verifikasi indikator sort pada Date non-aktif
11. Verifikasi urutan kembali ke default dengan baris 1: `27 May 26` jam `10:00`, Edit, Post-Purge Retention, 135, 138, Budi S

### TC-AC-LCS-401: Sort kolom Field alfabetis A–Z lalu Z–A

12. Klik header `Field` satu kali
13. Verifikasi A–Z baris 1 bernilai Field `Archive Period Duration`
14. Klik header `Field` kedua kali
15. Verifikasi Z–A baris 1 bernilai Field `Second Reminder Before Event`
16. Klik header `Field` ketiga kali (kembali netral)

### TC-AC-LCS-402: Sort kolom Action alfabetis tidak mengubah isi karena seluruh nilai Edit

17. Klik header `Action` satu kali
18. Verifikasi seluruh baris (sedikitnya satu baris tampil) bernilai `Edit`
19. Verifikasi indikator panah pada header Action aktif naik
20. Klik header `Action` kedua kali
21. Verifikasi seluruh baris (sedikitnya satu baris tampil) bernilai `Edit`
22. Verifikasi indikator panah pada header Action aktif turun
23. Klik header `Action` ketiga kali (kembali netral)

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: klik ketiga pada header Field dan Action mengembalikan sort ke netral sebelum TC berikutnya (S-09).
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
