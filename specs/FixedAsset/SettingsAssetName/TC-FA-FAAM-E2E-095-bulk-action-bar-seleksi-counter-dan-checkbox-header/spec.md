---
id: TC-FA-FAAM-E2E-095-bulk-action-bar-seleksi-counter-dan-checkbox-header
title: "Bulk Action Bar: Screening, Counter, Checkbox Header, dan Cancel Dialog Tidak Mereset Seleksi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-276
  - TC-FA-FAAM-277
  - TC-FA-FAAM-278
  - TC-FA-FAAM-294
coverage:
  web: automated
---

# Bulk Action Bar: Screening, Counter, Checkbox Header, dan Cancel Dialog Tidak Mereset Seleksi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; seed API per TC mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Dinamis (suffix `{runId}-095`, seed di hook `before`, cleanup di hook `after`):
  - `Bulk Clean A {runId}-095` dan `Bulk Clean B {runId}-095`: salinan Pre-setup #13c (Total Asset 0). Tidak ada yang dihapus spec ini karena dialog Bulk Delete hanya dibuka lalu dibatalkan.
- Data Pre-setup yang hanya dibaca: Pre-setup #15 (`Seed Item 01` sampai `Seed Item 30`, Total Asset 0) dan Pre-setup #10 serta #13 sebagai isi katalog, sehingga halaman pertama List tanpa Search berisi 10 baris (TC-FA-FAAM-278).
- Nilai [N] pada tombol `Select All ([N] records)` diturunkan dari seeding: dengan Search `{runId}-095` hanya dua baris cocok sehingga tombol tampil `Select All (2 records)`.
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-276: Screening Bulk Action Bar saat baris dicentang

1. Ketik Search `{runId}-095`, tekan Enter
2. Centang baris `Bulk Clean A {runId}-095`
3. Verifikasi bar bulk di atas tabel rata kiri berurutan: tombol `Bulk Action`, teks `1 asset name selected`, tombol `Select All (2 records)`, icon `×`
4. Klik `Bulk Action`
5. Verifikasi dropdown `Bulk Action` hanya memuat `Delete`
6. Tekan Esc untuk menutup dropdown

### TC-FA-FAAM-277: Counter bulk bentuk tunggal dan jamak serta siklus clear

7. Klik icon `×`
8. Centang `Bulk Clean A {runId}-095`
9. Verifikasi teks `1 asset name selected`
10. Centang `Bulk Clean B {runId}-095`
11. Verifikasi teks `2 asset names selected`
12. Uncheck `Bulk Clean B {runId}-095`
13. Verifikasi teks `1 asset name selected`
14. Klik icon `×`
15. Verifikasi baris `Bulk Clean A {runId}-095` tidak tercentang
16. Verifikasi bar bulk tidak tampil

### TC-FA-FAAM-294: Cancel pada dialog Bulk Delete tidak mereset seleksi

17. Centang baris `Bulk Clean A {runId}-095`, `Bulk Clean B {runId}-095`
18. Klik `Bulk Action` lalu `Delete`
19. Klik `[Cancel]`
20. Verifikasi dialog tertutup
21. Verifikasi dua baris `Bulk Clean A {runId}-095` dan `Bulk Clean B {runId}-095` tetap tercentang
22. Verifikasi bar bulk tetap tampil
23. Klik icon `×`
24. Klik `(←)` pada kotak Search

### TC-FA-FAAM-278: Checkbox header memilih halaman aktif, indeterminate, dan deselect

25. Centang 1 baris pertama pada tabel
26. Verifikasi checkbox header indeterminate `[-]`
27. Klik checkbox header
28. Verifikasi 10 baris halaman aktif tercentang
29. Klik checkbox header lagi
30. Verifikasi seluruh baris halaman aktif tidak tercentang
31. Verifikasi bar bulk tidak tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 1), menutup dropdown dengan Esc (langkah 6), serta membatalkan seleksi dan mengosongkan Search sebelum TC berikutnya (langkah 7, 23, 24; S-09).
- TC-FA-FAAM-278 ditaruh paling akhir karena membutuhkan List tanpa Search dengan sedikitnya 10 baris di halaman pertama.
- Asersi absence pada langkah 16 dan 31 memakai tabel yang sudah menampilkan baris (langkah 15 dan 30) sebagai anchor.
- Temuan untuk QA:
  - TC-FA-FAAM-276 Expected a menulis `Select All ([N] records)` tanpa nilai N; spec memakai `Select All (2 records)` karena Search `{runId}-095` membatasi hasil menjadi dua baris.
  - TC-FA-FAAM-278 langkah 1 tidak menyebut baris mana yang dicentang; spec memilih baris pertama tabel.
  - TC-FA-FAAM-294 Expected tidak menyebut bahwa tidak ada toast atau entri Changelog baru sesudah Cancel; tidak diasersi.
