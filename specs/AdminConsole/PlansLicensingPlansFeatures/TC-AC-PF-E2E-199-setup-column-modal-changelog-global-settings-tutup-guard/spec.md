---
id: TC-AC-PF-E2E-199-setup-column-modal-changelog-global-settings-tutup-guard
title: Setup Column modal Changelog Global Settings tutup popup tanpa Save, guard satu kolom tersisa, dan batas pin tiga kolom
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-513
  - TC-AC-PF-514
  - TC-AC-PF-515
coverage:
  web: automated
---

# Setup Column modal Changelog Global Settings tutup popup tanpa Save, guard satu kolom tersisa, dan batas pin tiga kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log G, Changelog Global Settings lima entri Edit (`Max depreciation methods (Multi Depreciation tier)` dan `Max custom fields per asset name`, 02 Jun 26 sampai 30 Jun 26, John D dan Sarah T). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Global Settings Principal tepat sama dengan Dataset Log G di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang disimpan; semua perubahan di Popup Setup Column dibuang tanpa `[Save]`.

## Test Steps

### Tutup popup lewat icon (X) atau Esc membuang perubahan (TC-AC-PF-513)

1. Klik tab Global Settings
2. Klik ikon Changelog di pojok kanan atas Card
3. Buka Popup Setup Column dari header kolom Actions (`⋯`)
4. Uncheck kolom `Old Value`
5. Klik icon close `(X)`
6. Verifikasi Popup Setup Column tertutup
7. Verifikasi modal Changelog Global Settings di bawahnya tetap terbuka
8. Verifikasi tabel tetap menampilkan kolom `Old Value` (perubahan preview dibuang)
9. Buka Popup Setup Column lagi
10. Uncheck kolom `Old Value`
11. Tekan Esc
12. Verifikasi Popup Setup Column tertutup
13. Verifikasi modal Changelog Global Settings di bawahnya tetap terbuka
14. Verifikasi tabel tetap menampilkan kolom `Old Value` (perubahan preview dibuang)

### Guard satu kolom tersisa (TC-AC-PF-514)

15. Buka Popup Setup Column
16. Uncheck semua kolom kecuali `Old Value`
17. Hover checkbox kolom `Old Value`
18. Verifikasi checkbox `Old Value` Disabled (tetap tampil)
19. Verifikasi tooltip "At least one column must remain visible."
20. Coba uncheck kolom `Old Value`
21. Verifikasi checkbox `Old Value` tidak bisa di-uncheck
22. Centang kembali satu kolom lain
23. Verifikasi semua checkbox enabled
24. Klik icon close `(X)`

### Batas pin tiga kolom (TC-AC-PF-515)

25. Buka Popup Setup Column
26. Pin kolom `Date`, `Action`, `Field`
27. Hover icon Pin kolom `Old Value`
28. Verifikasi icon Pin `Old Value` Disabled
29. Verifikasi tooltip "Maximum 3 columns can be pinned at once. Unpin another column first."
30. Klik icon Pin kolom `Old Value`
31. Verifikasi kolom `Old Value` tidak membeku
32. Unpin satu kolom
33. Verifikasi icon Pin kolom lain kembali aktif
34. Klik icon close `(X)`

## Notes

- Langkah penghubung (S-03): langkah 24 dan 34 menutup Popup Setup Column dengan icon `(X)` tanpa `[Save]` supaya perubahan preview dibuang.
- Temuan untuk QA:
  - TC-AC-PF-513, 514, dan 515 bertipe UI Only atau tidak menyimpan data, tetapi spec ini FE+BE karena dataset Changelog berasal dari backend nyata.
  - TC menetapkan lima entri sebagai seluruh isi Changelog Global Settings. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
