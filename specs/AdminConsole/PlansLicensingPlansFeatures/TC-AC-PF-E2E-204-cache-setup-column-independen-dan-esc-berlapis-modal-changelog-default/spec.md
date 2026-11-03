---
id: TC-AC-PF-E2E-204-cache-setup-column-independen-dan-esc-berlapis-modal-changelog-default
title: Cache Setup Column modal Changelog Default independen dari modal Custom dan Global Settings, dan Esc berlapis
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-484
  - TC-AC-PF-707
coverage:
  web: automated
---

# Cache Setup Column modal Changelog Default independen dari modal Custom dan Global Settings, dan Esc berlapis

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S). Changelog Custom dan Changelog Global Settings Principal memakai dataset baseline Pre-setup (Dataset Log C dan Dataset Log G) agar modal keduanya memuat kolom `Old Value`. Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Principal tepat sama dengan Dataset Log D, Log C, dan Log G di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: blok TC-AC-PF-484 menyimpan preferensi kolom modal Changelog Default (kolom `Old Value` disembunyikan) di browser (localStorage, cache sendiri per modal). Hook `after` menghapus preferensi kolom itu di browser, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Independensi cache Setup Column (TC-AC-PF-484)

1. Klik ikon Changelog pada toolbar tab Default
2. Buka Popup Setup Column dari header kolom Actions (`⋯`)
3. Uncheck kolom `Old Value`
4. Klik `[Save]`
5. Tutup modal dengan icon (X)
6. Klik tab Custom
7. Klik ikon Changelog pada toolbar
8. Verifikasi modal Changelog Custom tetap menampilkan kolom `Old Value`
9. Tutup modal dengan icon (X)
10. Klik tab Global Settings
11. Klik ikon Changelog di pojok kanan atas Card
12. Verifikasi modal Changelog Global Settings tetap menampilkan kolom `Old Value`
13. Tutup modal dengan icon (X)
14. Klik tab Default
15. Klik ikon Changelog pada toolbar
16. Verifikasi modal Changelog Default tetap menyembunyikan kolom `Old Value`

### Esc berlapis (TC-AC-PF-707)

17. Buka Popup Setup Column dari modal
18. Tekan Esc
19. Verifikasi Popup Setup Column tertutup
20. Verifikasi modal Changelog Default tetap terbuka dengan tabelnya
21. Tekan Esc sekali lagi
22. Verifikasi modal Changelog Default tertutup

## Notes

- Langkah penghubung (S-03): penutupan modal dengan icon (X) dan perpindahan tab pada langkah 5 sampai 15.
- Pembagian TC lintas spec: TC-AC-PF-481, 482, dan 483 ada di spec 187.
- Blok TC-AC-PF-707 melanjutkan modal Changelog Default yang terbuka dari langkah 15.
- Temuan untuk QA:
  - TC-AC-PF-484 tidak menyatakan Expected sesudah `[Save]` pada modal Default; spec langsung beralih ke modal Custom dan Global Settings sesuai Expected TC.
  - TC menetapkan lima baris sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
  - `suite.md` belum mendaftarkan pemulihan preferensi kolom di hook `after` (bagian 4 konvensi).
