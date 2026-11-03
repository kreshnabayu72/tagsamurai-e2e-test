---
id: TC-AC-PF-E2E-189-isi-berkas-download-modal-changelog-default-bom-sheet
title: Isi berkas Download modal Changelog Default CSV dan XLSX, encoding BOM, nama sheet, dan format sel
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-487
  - TC-AC-PF-488
  - TC-AC-PF-651
coverage:
  web: automated
---

# Isi berkas Download modal Changelog Default CSV dan XLSX, encoding BOM, nama sheet, dan format sel

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Principal tepat sama dengan Dataset Log D di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; pembaca buffer biner berkas CSV dan XLSX yang terunduh (encoding, BOM, pemisah, nama sheet, nilai sel); sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Isi berkas CSV (TC-AC-PF-487)

1. Klik ikon Changelog pada toolbar tab Default
2. Klik ikon Download
3. Pilih `Download as CSV`
4. Buka berkas CSV
5. Verifikasi baris header sama dengan kolom yang tampil tanpa kolom Actions (`Date`, `Action`, `Plan Name`, `Field`, `Old Value`, `New Value`, `Modified By`)
6. Verifikasi berkas memuat lima baris data
7. Verifikasi berkas berencoding UTF-8 dengan BOM
8. Verifikasi berkas berpemisah koma
9. Verifikasi nilai yang ditampilkan sebagai badge ditulis sebagai teks labelnya

### Isi berkas XLSX (TC-AC-PF-488)

10. Klik ikon Download
11. Pilih `Download as XLSX`
12. Buka berkas XLSX
13. Verifikasi berkas memuat satu sheet bernama `Sheet1`
14. Verifikasi header dan baris data pada `Sheet1` sama dengan tabel modal

### Format sel CSV (TC-AC-PF-651)

15. Verifikasi di modal Old Value baris Create tampil `—`
16. Verifikasi di modal New Value baris Delete tampil `—`
17. Verifikasi di modal Old Value baris Push Update tampil `v1`
18. Klik ikon Download
19. Pilih `Download as CSV`
20. Verifikasi tidak ada toast sukses
21. Buka berkas CSV
22. Verifikasi header CSV berurutan sama dengan kolom modal: `Date`, `Action`, `Plan Name`, `Field`, `Old Value`, `New Value`, `Modified By`
23. Verifikasi baris data `12 Aug 26, 09:00` | Create | Enterprise | `Plan Name` | `-` | `Enterprise` | Jane S
24. Verifikasi baris data `01 Aug 26, 08:00` | Archive | Growth Plus (old) | `Status` | `Active` | `Archived` | Jane S
25. Verifikasi baris data `20 Jul 26, 10:00` | Push Update | PT Wahana Nusantara | `Plan Version` | `1` | `5` | Sarah T
26. Verifikasi baris data `10 Jul 26, 12:00` | Delete | Pilot Default | `Plan Name` | `Pilot Default` | `-` | John D
27. Verifikasi baris data `05 Jun 26, 15:40` | Edit | Growth | `Group count` | `3` | `5` | Jane S
28. Verifikasi sel kosong ditulis `-` (hyphen tunggal), bukan `—` dan bukan sel kosong
29. Verifikasi Plan Version baris Push Update bernilai `1` dan `5` tanpa awalan `v`
30. Verifikasi nilai Date sama dengan tampilan modal (format General Settings `dd MMM yy`, 24-hour)

## Notes

- Verifikasi "tidak ada toast sukses" pada langkah 20 diletakkan segera setelah pemicu Download dan sebelum Verifikasi berkas (bagian 8b butir 11).
- Urutan baris data pada langkah 23 sampai 27 tidak dinilai (TC-AC-PF-651); tiap baris diverifikasi sebagai kehadiran baris.
- Pengecualian kelas f: isi berkas diasersi di spec ini; nama berkas, jumlah baris, dan header juga diasersi di spec 188.
- Temuan untuk QA:
  - TC-AC-PF-487 butir b menyebut "badge ditulis sebagai teks labelnya", sedangkan TC-AC-PF-455 menyatakan kolom Action, Old Value, dan New Value berupa plain text (bukan badge); spec mengasersi nilai kolom itu ditulis sebagai teks, sesuai TC-AC-PF-487.
  - TC-AC-PF-487 tidak menyebut cara memeriksa UTF-8 BOM dan pemisah koma; spec mengandalkan kemampuan pembaca buffer biner yang disediakan tim FE/BE.
  - TC menetapkan lima baris sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
