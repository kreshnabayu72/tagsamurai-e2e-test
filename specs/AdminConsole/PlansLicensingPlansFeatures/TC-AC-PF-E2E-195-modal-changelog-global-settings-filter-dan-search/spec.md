---
id: TC-AC-PF-E2E-195-modal-changelog-global-settings-filter-dan-search
title: Filter dan Search modal Changelog Global Settings per kolom dan rentang Date inklusif
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-502
  - TC-AC-PF-503
  - TC-AC-PF-504
coverage:
  web: automated
---

# Filter dan Search modal Changelog Global Settings per kolom dan rentang Date inklusif

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log G, Changelog Global Settings lima entri, terbaru dahulu: `30 Jun 26, 11:21` Edit `Max depreciation methods (Multi Depreciation tier)` (Old `3`, New `4`, John D); `30 Jun 26, 11:20` Edit `Max custom fields per asset name` (Old `8`, New `10`, John D); `22 Jun 26, 09:05` Edit `Max custom fields per asset name` (Old `5`, New `8`, Sarah T); `15 Jun 26, 14:40` Edit `Max depreciation methods (Multi Depreciation tier)` (Old `2`, New `3`, Sarah T); `02 Jun 26, 10:00` Edit `Max custom fields per asset name` (Old `3`, New `5`, John D). Modified By Sarah T = Sarah Tan, John D = John Doe. Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Global Settings Principal tepat sama dengan Dataset Log G di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Filter Field dan Modified By (TC-AC-PF-502)

1. Klik tab Global Settings
2. Klik ikon Changelog di pojok kanan atas Card
3. Buka Filter Panel, pilih Field `Max depreciation methods (Multi Depreciation tier)`, klik `[Apply]`
4. Verifikasi dua entri (`3` ke `4` dan `2` ke `3`)
5. Buka Filter Panel, klik `[Clear Field]`, pilih Modified By `Sarah Tan`, klik `[Apply]`
6. Verifikasi dua entri (22 Jun dan 15 Jun)
7. Buka Filter Panel, lalu buka dropdown Field
8. Verifikasi opsi Field hanya dua setting: `Max custom fields per asset name` dan `Max depreciation methods (Multi Depreciation tier)`

### Filter Date inklusif (TC-AC-PF-503)

9. Buka Filter Panel, klik `[Clear Field]`, pilih rentang `15 Jun 26` sampai `22 Jun 26`, klik `[Apply]`
10. Verifikasi dua entri `22 Jun 26` dan `15 Jun 26` (batas inklusif)

### Search kelas teks dan angka serta guard Date (TC-AC-PF-504)

11. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`
12. Klik ikon Search
13. Verifikasi input Search menampilkan placeholder `Search action, field, or value...`
14. Ketik `depreciation`, tekan Enter
15. Verifikasi dua entri Field `Max depreciation methods (Multi Depreciation tier)`
16. Ganti isi kotak search dengan `10`, tekan Enter
17. Verifikasi entri `30 Jun 26, 11:20` (New Value `10`)
18. Ganti isi kotak search dengan `Jun`, tekan Enter
19. Verifikasi "No results found" (kolom Date tidak dicari)
20. Ganti isi kotak search dengan `2`, tekan Enter
21. Verifikasi entri `15 Jun 26, 14:40` (Old Value `2`)
22. Ganti isi kotak search dengan `john`, tekan Enter
23. Verifikasi tiga entri John D (`30 Jun 26, 11:21`, `30 Jun 26, 11:20`, `02 Jun 26, 10:00`)

## Notes

- Langkah penghubung (S-03): `[Clear Field]` pada langkah 5, 9, dan 11 membersihkan filter sebelumnya; langkah 11 membersihkan filter Date sebelum blok Search.
- Verifikasi langkah 19 memakai empty state "No results found" sebagai anchor positif hasil Search; langkah 23 memakai entri John D sebagai anchor kehadiran data.
- Temuan untuk QA:
  - TC-AC-PF-504 tidak menyatakan apakah Search mencocokkan substring (mis. `10` pada angka lain) atau nilai utuh; spec mengikuti hasil yang ditulis TC untuk dataset ini.
  - TC menetapkan lima entri sebagai seluruh isi Changelog Global Settings. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
