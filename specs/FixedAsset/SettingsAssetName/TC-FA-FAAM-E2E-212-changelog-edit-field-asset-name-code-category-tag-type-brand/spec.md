---
id: TC-FA-FAAM-E2E-212-changelog-edit-field-asset-name-code-category-tag-type-brand
title: "Pencatatan Changelog Edit: Field Asset Name, Code, Category, TAG Type, dan Brand"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-560
  - TC-FA-FAAM-561
  - TC-FA-FAAM-562
  - TC-FA-FAAM-563
  - TC-FA-FAAM-564
coverage:
  web: automated
---

# Pencatatan Changelog Edit: Field Asset Name, Code, Category, TAG Type, dan Brand

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 22 (Category `IT Equipment`, `Office Equipment`), No. 23 (Brand `Dell`, `Lenovo`, `Apple`), No. 24 (UoM `Unit`). Fixture 13d (`Edit Target Item`) dipakai sebagai dasar salinan.
- Data Dinamis, di-seed lewat API di hook `before` (Tabel Data Uji Dinamis No. 37 sampai 41; salinan fixture 13d, Total Asset 0, Category `IT Equipment`, TAG `QR`, Brand `Dell` model `5420`, UoM `Unit`). Nama bersuffix `{runId}-212`; Code mengikuti literal Tabel Dinamis karena batas panjang Code (hook `before` menghapus sisa Code yang sama dari run lama):
  - `Edit Target Item 560 {runId}-212` (Code `ETI560`), `Edit Target Item 561 {runId}-212` (Code `ETI561`), `Edit Target Item 562 {runId}-212` (Code `ETI562`), `Edit Target Item 563 {runId}-212` (Code `ETI563`), `Edit Target Item 564 {runId}-212` (Code `ETI564`).
  - Nama hasil rename TC-FA-FAAM-560: `Edit Renamed {runId}-212`.
- Kemampuan teknis: membuka Modal Changelog dan memakai Search di dalamnya. Changelog adalah audit trail permanen sehingga total entri tidak diasersi; entri dicari lewat Search atas nama bersuffix unik (baseline nol).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lima Asset Name seed di atas lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-560 sampai 564: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### Pembukaan

1. Ketik Search `{runId}-212`, tekan Enter

### TC-FA-FAAM-560: Changelog Edit Field Asset Name

2. Klik `⋯` baris `Edit Target Item 560 {runId}-212` lalu `Edit`
3. Ubah Asset Name menjadi `Edit Renamed {runId}-212`
4. Klik `[Save]`
5. Klik icon Changelog
6. Ketik Search `Edit Renamed {runId}-212`, tekan Enter
7. Verifikasi satu baris: Action `Edit`, Asset Name `Edit Renamed {runId}-212`, Field `Asset Name`, Old `Edit Target Item 560 {runId}-212`, New `Edit Renamed {runId}-212`, Modified By aktor
8. Tutup Modal Changelog

### TC-FA-FAAM-561: Changelog Edit Field Code

9. Klik `⋯` baris `Edit Target Item 561 {runId}-212` lalu `Edit`
10. Ubah Code menjadi `ETI561-2`
11. Klik `[Save]`
12. Klik icon Changelog
13. Ketik Search `Edit Target Item 561 {runId}-212`, tekan Enter
14. Verifikasi satu baris Field `Code`, Old `ETI561`, New `ETI561-2`
15. Tutup Modal Changelog

### TC-FA-FAAM-562: Changelog Edit Field Category

16. Klik `⋯` baris `Edit Target Item 562 {runId}-212` lalu `Edit`
17. Ganti Category ke `Office Equipment`
18. Klik `[Save]`
19. Klik icon Changelog
20. Ketik Search `Edit Target Item 562 {runId}-212`, tekan Enter
21. Verifikasi satu baris Field `Category`, Old `IT Equipment`, New `Office Equipment`
22. Tutup Modal Changelog

### TC-FA-FAAM-563: Changelog Edit Field TAG Type memakai urutan enum tetap

23. Klik `⋯` baris `Edit Target Item 563 {runId}-212` lalu `Edit`
24. Tambahkan TAG Type `RFID` dan `BLE`
25. Klik `[Save]`
26. Klik icon Changelog
27. Ketik Search `Edit Target Item 563 {runId}-212`, tekan Enter
28. Verifikasi satu baris Field `TAG Type`, Old `QR`, New `RFID, QR, BLE` (urutan enum RFID, NFC, QR, BLE, GPS dipisah `, `)
29. Tutup Modal Changelog

### TC-FA-FAAM-564: Changelog Edit Field Brand diurut A→Z

30. Klik `⋯` baris `Edit Target Item 564 {runId}-212` lalu `Edit`
31. Tambahkan Brand `Lenovo` dan `Apple`
32. Klik `[Save]`
33. Klik icon Changelog
34. Ketik Search `Edit Target Item 564 {runId}-212`, tekan Enter
35. Verifikasi satu baris Field `Brand`, Old `Dell`, New `Apple, Dell, Lenovo`
36. Tutup Modal Changelog

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search untuk mempersempit tabel utama ke lima seed spec ini), langkah 6, 13, 20, 27, 34 (Search di Modal Changelog untuk menemukan entri target, karena Changelog tumbuh permanen dan entri tidak dicari lewat posisi teratas; S-12, S-14), dan langkah 8, 15, 22, 29, 36 (menutup Modal Changelog).
- Di atas smell 35 langkah. Spec berisi 36 langkah, sedikit di atas ~35. Alasan: lima blok memakai pola identik (Edit satu field, baca entri), tiap blok memakai seed sendiri dan berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pencatatan hanya diasersi sebagai kehadiran entri (kolom satu baris log disebut utuh dalam satu `Verifikasi`). Pernyataan Expected TC-FA-FAAM-560 "nama sesudah kejadian" ditulis pada kolom Asset Name baris.
- Temuan untuk QA:
  - TC-FA-FAAM-560 sampai 564 menulis "lihat entri teratas" tanpa cara menemukan entri pada audit trail permanen; spec memakai Search di Modal Changelog (kolom yang dicakup Search Changelog tidak disebut TC).
  - TC-FA-FAAM-560 menyebut "Modified By aktor" tanpa format; spec mengasersi baris memuat aktor, format `[First Name] [Last Initial]` tidak diasersi karena tidak ada di Expected.
