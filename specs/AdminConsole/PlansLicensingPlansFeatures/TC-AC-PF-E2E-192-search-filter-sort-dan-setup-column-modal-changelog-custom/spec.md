---
id: TC-AC-PF-E2E-192-search-filter-sort-dan-setup-column-modal-changelog-custom
title: Search, Filter, Sort, dan Setup Column modal Changelog Custom berfungsi sama dengan modal Default
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-497
  - TC-AC-PF-498
coverage:
  web: automated
---

# Search, Filter, Sort, dan Setup Column modal Changelog Custom berfungsi sama dengan modal Default

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log C, Changelog Custom Principal enam entri, terbaru dahulu: `29 Jun 26, 10:00` Push Update `Region Jawa Client` (Plan Version, Old `v3`, New `v20`, Sarah T); `28 Jun 26, 16:00` Edit `Growth Tier` (API call quota, Old `100K/month`, New `1M/month`, John D); `28 Jun 26, 09:10` Edit `Growth Tier` (Custom Report Builder, Old `No`, New `Yes`, John D); `17 Jun 26, 14:30` Create `Growth Tier` (Plan Name, Old `—`, New `Growth Tier`, John D); `12 Jun 26, 16:00` Delete `Pilot Reseller` (Plan Name, Old `Pilot Reseller`, New `—`, Jane S); `10 Jun 26, 09:15` Archive `Enterprise Reseller` (Status, Old `Active`, New `Archived`, Jane S). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Custom Principal tepat sama dengan Dataset Log C di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: blok TC-AC-PF-498 menyimpan lalu mereset preferensi kolom modal Changelog Custom (cache sendiri per modal). Hook `after` menghapus preferensi kolom itu di browser, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Search, Filter, dan Sort (TC-AC-PF-497)

1. Klik tab Custom
2. Klik ikon Changelog pada toolbar
3. Klik ikon Search
4. Verifikasi input Search menampilkan placeholder `Search action, field, or value...`
5. Ketik `tier`, tekan Enter
6. Verifikasi tiga entri `Growth Tier` (`Edit` API call quota, `Edit` Custom Report Builder, `Create`)
7. Klik `(←)` pada kotak Search
8. Buka Filter Panel, pilih Action `Edit`, klik `[Apply]`
9. Verifikasi dua entri `Growth Tier` (API call quota dan Custom Report Builder)
10. Verifikasi kedua entri berurutan terbaru dahulu
11. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`
12. Klik header `Date` satu kali
13. Verifikasi entri tertua `Archive Enterprise Reseller` paling atas

### Setup Column memiliki cache sendiri (TC-AC-PF-498)

14. Buka Popup Setup Column dari header kolom Actions (`⋯`)
15. Uncheck kolom `Field`
16. Klik `[Save]`
17. Tutup modal dengan icon (X)
18. Klik ikon Changelog pada toolbar
19. Verifikasi kolom `Field` tetap tersembunyi
20. Buka Popup Setup Column
21. Klik `[Reset to Default]`
22. Klik `[Save]`
23. Verifikasi seluruh tujuh kolom tampil kembali

## Notes

- Langkah penghubung (S-03): langkah 7 menutup input Search; langkah 11 membersihkan Filter sebelum Sort (lihat Temuan untuk QA); langkah 17 menutup modal untuk membuka ulang.
- Pembagian TC lintas spec: TC-AC-PF-619, 620, dan 621 (Search, Filter, Sort per anggota modal Custom) ada di spec 193 dan 194.
- Temuan untuk QA:
  - TC-AC-PF-497 Expected c menyebut entri tertua `Archive Enterprise Reseller` paling atas setelah Sort Date, padahal langkah 4 TC masih menerapkan Filter Action `Edit` sehingga entri `Archive` tidak tampil; spec menambah langkah penghubung yang membersihkan Filter sebelum Sort.
  - TC menetapkan enam entri sebagai seluruh isi Changelog Custom. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
  - `suite.md` belum mendaftarkan pemulihan preferensi kolom di hook `after` (bagian 4 konvensi).
