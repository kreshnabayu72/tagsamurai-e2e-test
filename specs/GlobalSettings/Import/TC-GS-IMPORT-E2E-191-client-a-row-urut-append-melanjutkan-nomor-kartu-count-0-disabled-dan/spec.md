---
id: TC-GS-IMPORT-E2E-191-client-a-row-urut-append-melanjutkan-nomor-kartu-count-0-disabled-dan
title: "Client A: Row # urut, Append melanjutkan nomor, kartu count 0 Disabled, dan kolom Staging Table tiap Sub-Tab (Measurement, Position, Division, User Login, User Non Login)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-465
  - TC-GS-IMPORT-477
  - TC-GS-IMPORT-487
  - TC-GS-IMPORT-766
  - TC-GS-IMPORT-767
  - TC-GS-IMPORT-768
  - TC-GS-IMPORT-770
coverage:
  web: automated
---

# Client A: Row # urut, Append melanjutkan nomor, kartu count 0 Disabled, dan kolom Staging Table tiap Sub-Tab (Measurement, Position, Division, User Login, User Non Login)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec dan Custom Field Client A dibaca (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD` (TC tidak menyebut password per akun, lihat Temuan untuk QA).
- Layar awal: hook `beforeEach` membuka Import > Brand Client A; pindah Sub-Tab dilakukan di langkah.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis (draft Population Client A, disiapkan lewat skrip seed di hook `before`, Kontrak Fixture R2): D-01 (Brand 12 baris `pending` dari `brand-12.csv`), D-02 (Measurement 6 baris `pending`), D-03 (Position 6 baris `pending`), D-04 (Division 6 baris `pending`, termasuk `Operations` dengan Code kosong), D-05 (User Login 8 baris `pending` dengan Shift dan Overtime Hours terpetakan), D-06 (User Non Login 5 baris `pending`). D-08 (Brand 18 baris setelah Append, Row # 13 sampai 18 hasil Append, Row # 13 `Nikon`) dibuat ulang lewat skrip seed sebelum TC-GS-IMPORT-477 (menggantikan D-01 di Sub-Tab Brand). Spec hanya membaca.
- Custom Field Client A: Shift (Dropdown: Pagi, Siang, Malam), Shift Notes (Text Area), Overtime Hours (Numeric 2 desimal), Emergency Phone (Phone), Join Date (Date), seluruhnya Optional dan Active; Old Badge nonaktif (Pre-setup).
- Cleanup (hook `after`): draft Client A dipulihkan ke kondisi Population (R2).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Kartu count 0 (TC-GS-IMPORT-465), Sub-Tab Brand dengan D-01

1. Hover kartu Errors
2. Verifikasi kartu Errors menampilkan angka `0` pudar
3. Verifikasi hover kartu Errors tidak memunculkan tooltip
4. Hover kartu Duplicates
5. Verifikasi kartu Duplicates menampilkan angka `0` pudar
6. Verifikasi hover kartu Duplicates tidak memunculkan tooltip
7. Klik kartu Errors
8. Klik kartu Duplicates
9. Verifikasi kartu Total Rows tetap Active
10. Verifikasi tabel tetap menampilkan 10 baris pertama dengan pagination "Showing 1 - 10 of 12 items"
11. Verifikasi kartu Ready to Import (12) tetap Enabled

### Row # urut dan Append (TC-GS-IMPORT-477), Sub-Tab Brand dengan D-08

12. Buat ulang draft Brand D-08 (18 baris) lewat skrip seed, lalu muat ulang halaman
13. Verifikasi halaman 1 menampilkan Row # 1 sampai 10
14. Klik halaman 2
15. Verifikasi halaman 2 menampilkan "Showing 11 - 18 of 18 items" dan Row # 11 sampai 18
16. Verifikasi baris hasil Append dimulai pada Row # 13 (`Nikon`)

### Kolom Staging Table per Sub-Tab (TC-GS-IMPORT-766, 767, 768, 770, 487)

17. Pindah ke Sub-Tab Measurement
18. Verifikasi header kolom `Checkbox | # | Unit Name | Symbol | Status | Actions`
19. Verifikasi Checkbox dan `#` pinned kiri
20. Verifikasi Actions pinned kanan
21. Pindah ke Sub-Tab Position
22. Verifikasi header kolom `Checkbox | # | Position Name | Status | Actions`
23. Verifikasi Checkbox dan `#` pinned kiri
24. Verifikasi Actions pinned kanan
25. Pindah ke Sub-Tab Division
26. Verifikasi header kolom `Checkbox | # | Division Name | Code | Status | Actions`
27. Verifikasi sel Code baris `Operations` menampilkan `—`
28. Pindah ke Sub-Tab User Login
29. Verifikasi kolom Shift dan Overtime Hours tampil setelah kolom atribut standar (`Active Period`)
30. Verifikasi kolom Shift dan Overtime Hours tampil sebelum kolom `Status`
31. Verifikasi sel Shift dan Overtime Hours yang tidak berisi nilai pada baris terkait tampil `—`
32. Pindah ke Sub-Tab User Non Login
33. Verifikasi header kolom: Checkbox, #, First Name, Last Name, Email, Division, Position, Employee ID, Represented By, Active Period, lalu kolom Custom Field Active Emergency Phone, Join Date, Overtime Hours, Shift, dan Shift Notes, lalu Status dan Actions
34. Verifikasi tidak ada kolom Access

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec read-only: tidak ada mutasi draft; hanya langkah 12 yang mengganti draft Brand dengan D-08 lewat skrip seed (penghubung, S-03).
- Urutan di dalam spec mengikuti dataset: TC-465 memakai D-01 di Sub-Tab Brand lebih dulu, lalu D-08 menggantikan D-01 untuk TC-477, lalu pindah Sub-Tab untuk kolom.
- Hasil TC-GS-IMPORT-487 diasersi pada Sub-Tab User Login (langkah 29-31) dan berada sesudah Sub-Tab Division karena satu spec membaca Sub-Tab berurutan.
- Temuan untuk QA:
  - TC-GS-IMPORT-477 menyebut halaman 2 dengan "Showing 11 - 18 of 18 items" sedangkan TC-GS-IMPORT-465 memakai ukuran halaman 10 per halaman; spec mengikuti ukuran halaman default 10 dan tidak mengubahnya.
  - TC-GS-IMPORT-487 Expected a menyebut kolom atribut standar `Active Period`; spec mengasersi posisi kolom Custom Field relatif terhadap kolom itu.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
