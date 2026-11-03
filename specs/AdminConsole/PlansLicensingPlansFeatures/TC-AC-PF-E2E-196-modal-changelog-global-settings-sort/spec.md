---
id: TC-AC-PF-E2E-196-modal-changelog-global-settings-sort
title: Sort modal Changelog Global Settings numerik natural, Date, Modified By, Field, dan Action
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-505
  - TC-AC-PF-506
  - TC-AC-PF-654
coverage:
  web: automated
---

# Sort modal Changelog Global Settings numerik natural, Date, Modified By, Field, dan Action

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log G, Changelog Global Settings lima entri, terbaru dahulu: `30 Jun 26, 11:21` Edit `Max depreciation methods (Multi Depreciation tier)` (Old `3`, New `4`, John D); `30 Jun 26, 11:20` Edit `Max custom fields per asset name` (Old `8`, New `10`, John D); `22 Jun 26, 09:05` Edit `Max custom fields per asset name` (Old `5`, New `8`, Sarah T); `15 Jun 26, 14:40` Edit `Max depreciation methods (Multi Depreciation tier)` (Old `2`, New `3`, Sarah T); `02 Jun 26, 10:00` Edit `Max custom fields per asset name` (Old `3`, New `5`, John D). Modified By John D = John Doe, Sarah T = Sarah Tan. Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Global Settings Principal tepat sama dengan Dataset Log G di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Sort numerik natural (TC-AC-PF-505)

1. Klik tab Global Settings
2. Klik ikon Changelog di pojok kanan atas Card
3. Klik header `New Value` satu kali
4. Verifikasi New Value ascending: `3`, `4`, `5`, `8`, `10` (10 setelah 8, bukan setelah 1)
5. Klik header `New Value` kedua kali
6. Verifikasi New Value descending kebalikan: `10`, `8`, `5`, `4`, `3`
7. Klik header `Old Value` satu kali
8. Verifikasi Old Value ascending: `2`, `3`, `3`, `5`, `8`
9. Klik header `Old Value` kedua kali
10. Verifikasi Old Value descending kebalikan: `8`, `5`, `3`, `3`, `2`

### Sort Date dan Modified By (TC-AC-PF-506)

11. Klik header `Date` satu kali
12. Verifikasi Date ascending: entri `02 Jun 26` paling atas
13. Klik header `Modified By` satu kali
14. Verifikasi Modified By ascending berdasarkan nama lengkap: `John D` (John Doe) lalu `Sarah T` (Sarah Tan)

### Sort Field dan Action (TC-AC-PF-654)

15. Klik header `Field` satu kali
16. Verifikasi Field ascending: tiga baris `Max custom fields per asset name` lebih dulu, lalu dua baris `Max depreciation methods (Multi Depreciation tier)`
17. Klik header `Field` kedua kali
18. Verifikasi Field descending: dua baris `Max depreciation methods (Multi Depreciation tier)` lebih dulu, lalu tiga baris `Max custom fields per asset name`
19. Klik header `Action` satu kali
20. Verifikasi Action ascending: urutan tetap `30 Jun 26, 11:21`, `30 Jun 26, 11:20`, `22 Jun 26, 09:05`, `15 Jun 26, 14:40`, `02 Jun 26, 10:00`
21. Klik header `Action` kedua kali
22. Verifikasi Action descending: urutan tetap `30 Jun 26, 11:21`, `30 Jun 26, 11:20`, `22 Jun 26, 09:05`, `15 Jun 26, 14:40`, `02 Jun 26, 10:00`

## Notes

- Urutan sort tiap blok bergantung pada klik header kolom baru yang menggantikan sort kolom sebelumnya (satu sort aktif); TC tidak menyatakan reset sort antar kolom.
- Temuan untuk QA:
  - Sort Action pada TC-AC-PF-654 tidak punya dua nilai distinct (seluruh baris `Edit`, S-11); TC menyatakan urutan tetap pada kedua arah, dan spec mengasersi persis itu (urutan stabil), bukan hasil sort.
  - TC menetapkan lima entri sebagai seluruh isi Changelog Global Settings. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
