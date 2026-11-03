---
id: TC-AC-PF-E2E-187-setup-column-modal-changelog-default-tutup-guard-batas-pin
title: Setup Column modal Changelog Default tutup popup tanpa Save, guard satu kolom tersisa, dan batas pin tiga kolom
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-481
  - TC-AC-PF-482
  - TC-AC-PF-483
coverage:
  web: automated
---

# Setup Column modal Changelog Default tutup popup tanpa Save, guard satu kolom tersisa, dan batas pin tiga kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Principal tepat sama dengan Dataset Log D di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang disimpan; semua perubahan di Popup Setup Column dibuang tanpa `[Save]`.

## Test Steps

### Tutup popup lewat icon (X) atau Esc membuang perubahan (TC-AC-PF-481)

1. Klik ikon Changelog pada toolbar tab Default
2. Buka Popup Setup Column
3. Uncheck kolom `Old Value`
4. Klik icon close `(X)`
5. Verifikasi Popup Setup Column tertutup
6. Verifikasi modal Changelog Default di bawahnya tetap terbuka
7. Verifikasi tabel tetap menampilkan kolom `Old Value` (perubahan preview dibuang)
8. Buka Popup Setup Column lagi
9. Uncheck kolom `Old Value`
10. Tekan Esc
11. Verifikasi Popup Setup Column tertutup
12. Verifikasi modal Changelog Default di bawahnya tetap terbuka
13. Verifikasi tabel tetap menampilkan kolom `Old Value` (perubahan preview dibuang)

### Guard satu kolom tersisa (TC-AC-PF-482)

14. Buka Popup Setup Column
15. Uncheck semua kolom kecuali `Old Value`
16. Hover checkbox kolom `Old Value`
17. Verifikasi checkbox `Old Value` Disabled (tetap tampil)
18. Verifikasi tooltip "At least one column must remain visible."
19. Coba uncheck kolom `Old Value`
20. Verifikasi checkbox `Old Value` tidak bisa di-uncheck
21. Centang kembali satu kolom lain
22. Verifikasi semua checkbox enabled
23. Klik icon close `(X)`

### Batas pin tiga kolom (TC-AC-PF-483)

24. Buka Popup Setup Column
25. Pin kolom `Date`, `Action`, `Plan Name`
26. Hover icon Pin kolom `Field`
27. Verifikasi icon Pin `Field` Disabled
28. Verifikasi tooltip "Maximum 3 columns can be pinned at once. Unpin another column first."
29. Klik icon Pin kolom `Field`
30. Verifikasi kolom `Field` tidak membeku
31. Unpin satu kolom
32. Verifikasi icon Pin kolom lain kembali aktif
33. Klik icon close `(X)`

## Notes

- Langkah penghubung (S-03): langkah 23 dan 33 menutup Popup Setup Column dengan icon `(X)` tanpa `[Save]` supaya perubahan preview dibuang.
- Pembagian TC lintas spec: TC-AC-PF-484 dan TC-AC-PF-707 (cache Setup Column independen dan Esc berlapis) ada di spec 204.
- Temuan untuk QA:
  - TC-AC-PF-481, 482, dan 483 bertipe UI Only atau tidak menyimpan data, tetapi spec ini FE+BE karena dataset Changelog berasal dari backend nyata.
  - TC menetapkan lima baris sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
