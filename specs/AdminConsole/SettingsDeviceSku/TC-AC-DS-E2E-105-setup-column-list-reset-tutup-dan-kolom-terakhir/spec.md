---
id: TC-AC-DS-E2E-105-setup-column-list-reset-tutup-dan-kolom-terakhir
title: "Setup Column List: Reset to Default, Tutup Tanpa Save, dan Kolom Terakhir Tidak Dapat Di-uncheck"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-354
  - TC-AC-DS-355
  - TC-AC-DS-356
coverage:
  web: automated
---

# Setup Column List: Reset to Default, Tutup Tanpa Save, dan Kolom Terakhir Tidak Dapat Di-uncheck

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`.
- Konfigurasi kolom awal: delapan kolom bawaan (`Photo | Device Name | SKU | Category | Brand | Model/Type | Current Stock | Last Modified`) dengan `Hardware Type`, `Range Type`, dan `TAG Type` Hidden.
- Preferensi kolom List: langkah 7 menyimpan konfigurasi kolom di cache browser. Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global lain yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-354: Reset to Default

1. Klik header kolom Actions (⋯)
2. Klik `Setup Column...` pada overlay
3. Hilangkan centang `Brand`, centang `TAG Type`, dan geser `SKU` ke posisi akhir daftar
4. Klik `[Reset to Default]`
5. Verifikasi preview kembali ke default: delapan kolom bawaan tampil dengan urutan awal
6. Verifikasi `Hardware Type`, `Range Type`, dan `TAG Type` Hidden pada preview
7. Klik `[Save]`
8. Muat ulang halaman dengan F5
9. Verifikasi tabel tetap pada konfigurasi default: delapan kolom bawaan dengan urutan awal dan `Hardware Type`, `Range Type`, serta `TAG Type` Hidden

### TC-AC-DS-355: Menutup popup tanpa Save

10. Klik header kolom Actions (⋯)
11. Klik `Setup Column...` pada overlay
12. Hilangkan centang `Brand`
13. Klik ikon close `[✕]`
14. Verifikasi perubahan preview dibuang dan kolom Brand tetap tampil pada tabel
15. Klik header kolom Actions (⋯)
16. Klik `Setup Column...` pada overlay
17. Hilangkan centang `Brand`
18. Tekan Esc
19. Verifikasi perubahan preview dibuang dan kolom Brand tetap tampil pada tabel
20. Verifikasi konfigurasi tersimpan terakhir tetap dipakai: delapan kolom bawaan dengan urutan awal

### TC-AC-DS-356: Kolom terakhir tidak dapat di-uncheck

21. Klik header kolom Actions (⋯)
22. Klik `Setup Column...` pada overlay
23. Hilangkan centang kolom satu per satu (`Photo`, `Device Name`, `SKU`, `Category`, `Brand`, `Model/Type`, `Current Stock`) sampai tersisa satu kolom `Last Modified`
24. Verifikasi checkbox kolom `Last Modified` disabled dan tidak dapat di-uncheck
25. Hover checkbox kolom `Last Modified`
26. Verifikasi tooltip "At least one column must remain visible." tampil
27. Centang kolom `Photo`
28. Verifikasi semua checkbox kembali enabled
29. Klik ikon close `[✕]`

## Notes

- Langkah penghubung (S-03, S-09): langkah 1 sampai 2, 10 sampai 11, 15 sampai 16, dan 21 sampai 22 membuka overlay dan popup; langkah 29 menutup popup tanpa Save sehingga perubahan tidak tersimpan; tanpa asersi tambahan.
- Langkah 3 mengubah tiga hal sekaligus agar `[Reset to Default]` di langkah 4 diuji terhadap perubahan hideable, curated, dan urutan.
- Temuan untuk QA:
  - TC-AC-DS-356 menyebut "hilangkan centang semua kolom satu per satu sampai tersisa satu kolom" tanpa menetapkan kolom yang tersisa; spec menyisakan `Last Modified` dan memakai pilihan itu pada seluruh bagian.
  - S-12: asersi bergantung pada Pre-setup #29 dan #30. Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - `suite.md` belum mendaftarkan pemulihan konfigurasi kolom yang disimpan spec (konvensi bagian 4); pemulihan lewat penghapusan preferensi kolom di browser membutuhkan kemampuan dari tim FE.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
