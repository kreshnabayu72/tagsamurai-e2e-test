---
id: TC-AC-LCS-E2E-105-filter-modal-changelog-field-modified-by-date
title: "Filter Modal Changelog: Field, Modified By, Rentang Date, dan Satu Hari"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-390
  - TC-AC-LCS-391
  - TC-AC-LCS-392
  - TC-AC-LCS-393
  - TC-AC-LCS-394
coverage:
  web: automated
---

# Filter Modal Changelog: Field, Modified By, Rentang Date, dan Satu Hari

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

### TC-AC-LCS-390: Filter Field tunggal Grace Period Duration menyaring baris

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Klik icon Filter, pilih `Grace Period Duration` pada field `Field`, tutup dropdown, klik `[Apply]`
4. Verifikasi footer `1–3 of 3`
5. Verifikasi baris 1: `23 May 26` jam `10:00`, Edit, Grace Period Duration, 115, 118, Sarah T
6. Verifikasi baris 2: `14 May 26` jam `10:00`, Edit, Grace Period Duration, 70, 73, Sarah T
7. Verifikasi baris 3: `05 May 26` jam `10:00`, Edit, Grace Period Duration, 25, 28, Sarah T
8. Verifikasi icon Filter menampilkan badge titik indikator filter aktif

### TC-AC-LCS-391: Filter Field dua nilai menampilkan gabungan kedua field

9. Klik `[Clear Field]`, klik `[Apply]`
10. Pilih `Grace Period Duration` dan `Archive Period Duration` pada field `Field`, klik `[Apply]`
11. Verifikasi footer `1–6 of 6`
12. Verifikasi seluruh baris (sedikitnya satu baris tampil) hanya bernilai Field Grace Period Duration atau Archive Period Duration; tidak ada field lain

### TC-AC-LCS-392: Filter Modified By John Doe menyaring baris

13. Klik `[Clear Field]`, klik `[Apply]`
14. Pilih `John Doe` pada field `Modified By`, klik `[Apply]`
15. Verifikasi footer `1–9 of 9`
16. Verifikasi seluruh baris pada halaman (sedikitnya satu baris tampil) bernilai Modified By `John D`

### TC-AC-LCS-393: Filter Date rentang 05 May 26 sampai 09 May 26 inklusif di kedua ujung

17. Klik `[Clear Field]`, klik `[Apply]`
18. Pilih rentang `05 May 26` sampai `09 May 26` pada field `Date`, klik `[Apply]`
19. Verifikasi footer `1–5 of 5`
20. Verifikasi baris 1: `09 May 26` jam `10:00`, Edit, Post-Purge Retention, 45, 48, Budi S
21. Verifikasi baris 2: `08 May 26` jam `10:00`, Edit, Purge Urgent Warning Email, 40, 43, Sarah T
22. Verifikasi baris 3: `07 May 26` jam `10:00`, Edit, Purge Warning Email, 35, 38, John D
23. Verifikasi baris 4: `06 May 26` jam `10:00`, Edit, Archive Period Duration, 30, 33, Budi S
24. Verifikasi baris 5: `05 May 26` jam `10:00`, Edit, Grace Period Duration, 25, 28, Sarah T

### TC-AC-LCS-394: Filter Date satu hari (Start sama dengan End) menampilkan entri pada hari itu

25. Klik `[Clear Field]`, klik `[Apply]`
26. Pilih rentang `12 May 26` sampai `12 May 26` pada field `Date`, klik `[Apply]`
27. Verifikasi footer `1–1 of 1`
28. Verifikasi baris 1: `12 May 26` jam `10:00`, Edit, Second Reminder Before Event, 60, 63, Budi S

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1 (membuka tab Client Lifecycle, karena hook `beforeEach` membuka tab Trial Settings); klik `[Clear Field]` lalu `[Apply]` sebelum TC berikutnya membersihkan filter TC sebelumnya (S-09); panel Filter tetap terbuka sesudah `[Apply]` (TC-AC-LCS-397 mengamati panel sesudah `[Apply]`), sehingga langkah TC "Klik icon Filter" dilakukan sekali pada TC pertama.
- Pengecualian A-15: total absolut Changelog (footer, jumlah baris, empty state) diasersi pada riwayat hasil overwrite lewat Fixture BE di hook `before`; spec tidak mereset riwayat di tengah langkah.
- Temuan untuk QA:
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
