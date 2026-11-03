---
id: TC-AC-LCS-E2E-099-search-modal-changelog-pencocokan-per-kolom
title: "Search Modal Changelog: Pencocokan per Kolom Action, Field, Old Value, New Value, Modified By, dan Kolom Date"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-375
  - TC-AC-LCS-376
  - TC-AC-LCS-377
  - TC-AC-LCS-378
  - TC-AC-LCS-379
  - TC-AC-LCS-380
coverage:
  web: automated
---

# Search Modal Changelog: Pencocokan per Kolom Action, Field, Old Value, New Value, Modified By, dan Kolom Date

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

### TC-AC-LCS-375: Search kolom Action mencocokkan nilai homogen Edit

1. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
2. Ketik Search `Edit`, tekan Enter
3. Verifikasi footer `1–10 of 27` (seluruh 27 entri cocok)
4. Verifikasi seluruh baris pada halaman (sedikitnya satu baris tampil) bernilai Action `Edit`

### TC-AC-LCS-376: Search kolom Field mencocokkan nama field Grace Period Duration

5. Ganti isi kotak search dengan `Grace`, tekan Enter
6. Verifikasi footer `1–3 of 3`
7. Verifikasi baris 1: `23 May 26` jam `10:00`, Edit, Grace Period Duration, 115, 118, Sarah T
8. Verifikasi baris 2: `14 May 26` jam `10:00`, Edit, Grace Period Duration, 70, 73, Sarah T
9. Verifikasi baris 3: `05 May 26` jam `10:00`, Edit, Grace Period Duration, 25, 28, Sarah T

### TC-AC-LCS-377: Search kolom Old Value mencocokkan angka `100`

10. Ganti isi kotak search dengan `100`, tekan Enter
11. Verifikasi footer `1–1 of 1`
12. Verifikasi baris 1: `20 May 26` jam `10:00`, Edit, First Reminder Before Event, 100, 103, Sarah T

### TC-AC-LCS-378: Search kolom New Value mencocokkan angka `103`

13. Ganti isi kotak search dengan `103`, tekan Enter
14. Verifikasi footer `1–1 of 1`
15. Verifikasi baris 1: `20 May 26` jam `10:00`, Edit, First Reminder Before Event, 100, 103, Sarah T

### TC-AC-LCS-379: Search kolom Modified By mencocokkan nama lengkap snapshot Sarah Thompson

16. Ganti isi kotak search dengan `Thompson`, tekan Enter
17. Verifikasi footer `1–9 of 9`
18. Verifikasi seluruh baris (sedikitnya satu baris tampil) bernilai Modified By `Sarah T`
19. Verifikasi baris teratas: `26 May 26` jam `10:00`, Edit, Purge Urgent Warning Email, 130, 133, Sarah T
20. Verifikasi baris terbawah: `02 May 26` jam `10:00`, Edit, First Reminder Before Event, 10, 13, Sarah T

### TC-AC-LCS-380: Search tidak mencari kolom Date

21. Ganti isi kotak search dengan `May`, tekan Enter
22. Verifikasi empty state filtered: Illustration, Title "No results found", Description "Try adjusting your search or filter."
23. Klik `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah terakhir (klik `(←)` pada kotak Search menutup input dan mereset tabel, S-09); mengganti isi kotak search antar TC mengikuti butir 9 bagian 8b.
- Search dipakai sebagai objek uji pada seluruh TC spec ini, bukan untuk menemukan baris target.
- Temuan untuk QA:
  - TC-AC-LCS-375: Expected "seluruh 27 entri cocok" hanya teramati lewat footer `1–10 of 27` dan nilai Action pada halaman pertama; baris halaman 2 dan 3 tidak diamati TC.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tidak punya langkah observasi dan tidak diasersi.
