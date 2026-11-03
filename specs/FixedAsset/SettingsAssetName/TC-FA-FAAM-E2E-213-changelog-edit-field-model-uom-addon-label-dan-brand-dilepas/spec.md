---
id: TC-FA-FAAM-E2E-213-changelog-edit-field-model-uom-addon-label-dan-brand-dilepas
title: "Pencatatan Changelog Edit: Field Model/Type, Brand Dilepas, UoM, Default Addon, dan Default Label"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-565
  - TC-FA-FAAM-566
  - TC-FA-FAAM-567
  - TC-FA-FAAM-568
  - TC-FA-FAAM-569
coverage:
  web: automated
---

# Pencatatan Changelog Edit: Field Model/Type, Brand Dilepas, UoM, Default Addon, dan Default Label

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 23 (Brand `Dell`, `Lenovo`), No. 24 (UoM `Unit`, `Pcs`), No. 25 (Label `Finance`, `Fragile`), No. 10b (lisensi addon `Audit` untuk Default Addon; lihat Temuan untuk QA).
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-213`, Code literal Tabel Dinamis (batas panjang Code; hook `before` menghapus sisa Code yang sama dari run lama):
  - `Edit Target Item 565 {runId}-213` (Code `ETI565`), `Edit Target Item 567 {runId}-213` (Code `ETI567`), `Edit Target Item 568 {runId}-213` (Code `ETI568`), `Edit Target Item 569 {runId}-213` (Code `ETI569`): salinan fixture 13d (Tabel Dinamis No. 42, 44, 45, 46), Total Asset 0, Category `IT Equipment`, TAG `QR`, Brand `Dell` model `5420`, UoM `Unit`.
  - `Two Brand Item 566 {runId}-213` (Code `TBI566`): salinan fixture 13g (Tabel Dinamis No. 43), Brand `Dell` model `5420` dan `Lenovo` model `X1`, Total Asset 0.
- Kemampuan teknis: membuka Modal Changelog dan memakai Search di dalamnya. Changelog adalah audit trail permanen sehingga total entri tidak diasersi; entri dicari lewat Search atas nama bersuffix unik (baseline nol).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lima Asset Name seed di atas lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-565 sampai 569: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### Pembukaan

1. Ketik Search `{runId}-213`, tekan Enter

### TC-FA-FAAM-565: Changelog Edit Field Model/Type satu baris per Brand

2. Klik `⋯` baris `Edit Target Item 565 {runId}-213` lalu `Edit`
3. Tambahkan model `7420` pada Brand `Dell`
4. Tambahkan Brand `Lenovo` dengan model `X1`
5. Klik `[Save]`
6. Klik icon Changelog
7. Ketik Search `Edit Target Item 565 {runId}-213`, tekan Enter
8. Verifikasi baris `Model/Type — Dell`: Old `5420`, New `5420, 7420`
9. Verifikasi baris `Model/Type — Lenovo`: Old `—`, New `X1`
10. Verifikasi baris `Brand`: Old `Dell`, New `Dell, Lenovo`
11. Tutup Modal Changelog

### TC-FA-FAAM-566: Brand dilepas bersama modelnya

12. Klik `⋯` baris `Two Brand Item 566 {runId}-213` lalu `Edit`
13. Lepas Brand `Lenovo` (dengan model `X1`) dari Asset Name yang sudah memiliki Dell dan Lenovo
14. Klik `[Save]`
15. Klik icon Changelog
16. Ketik Search `Two Brand Item 566 {runId}-213`, tekan Enter
17. Verifikasi baris `Brand`: Old `Dell, Lenovo`, New `Dell`
18. Verifikasi baris `Model/Type — Lenovo`: Old `X1`, New `—`
19. Tutup Modal Changelog

### TC-FA-FAAM-567: Changelog Edit Field UoM

20. Klik `⋯` baris `Edit Target Item 567 {runId}-213` lalu `Edit`
21. Ubah UoM menjadi `Pcs`
22. Klik `[Save]`
23. Klik icon Changelog
24. Ketik Search `Edit Target Item 567 {runId}-213`, tekan Enter
25. Verifikasi satu baris Field `UoM`, Old `Unit`, New `Pcs`
26. Tutup Modal Changelog

### TC-FA-FAAM-568: Changelog Edit Field Default Addon

27. Klik `⋯` baris `Edit Target Item 568 {runId}-213` lalu `Edit`
28. Tambahkan Default Addon `Audit`
29. Klik `[Save]`
30. Klik icon Changelog
31. Ketik Search `Edit Target Item 568 {runId}-213`, tekan Enter
32. Verifikasi satu baris Field `Default Addon`, Old `—`, New `Audit`
33. Tutup Modal Changelog

### TC-FA-FAAM-569: Changelog Edit Field Default Label

34. Klik `⋯` baris `Edit Target Item 569 {runId}-213` lalu `Edit`
35. Tambahkan Default Label `Finance` dan `Fragile`
36. Klik `[Save]`
37. Klik icon Changelog
38. Ketik Search `Edit Target Item 569 {runId}-213`, tekan Enter
39. Verifikasi satu baris Field `Default Label`, Old `—`, New `Finance, Fragile`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search untuk mempersempit tabel utama ke lima seed spec ini), langkah 7, 16, 24, 31, 38 (Search di Modal Changelog untuk menemukan entri target pada audit trail permanen; S-12, S-14), dan langkah 11, 19, 26, 33 (menutup Modal Changelog).
- Di atas smell 35 langkah. Spec berisi 39 langkah, di atas ~35. Alasan: lima blok memakai pola identik (Edit satu field atau satu pasangan Brand dan Model, lalu baca entri), tiap blok memakai seed sendiri dan berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-FAAM-568 menambah Default Addon `Audit` pada fixture 13d tanpa menyatakan lisensi `Audit` tersedia, dan TC-FA-FAAM-569 tidak menyatakan kuota label; Pre-setup No. 10b hanya menyebut lisensi `Maps` tidak teralokasi. Spec mengasumsikan lisensi `Audit` aktif pada client uji (disediakan tim FE/BE).
  - Dialog dampak Default Addon (Change Default Addon) tidak disebut TC-FA-FAAM-568; karena Total Asset 0 spec tidak menulis langkah dialog.
  - "Lihat entri teratas" pada audit trail permanen diganti Search atas nama bersuffix (kolom yang dicakup Search Changelog tidak disebut TC).
