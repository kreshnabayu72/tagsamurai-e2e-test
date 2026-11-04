---
id: TC-FA-TDC-E2E-007-tampilan-kolom-modified-by-last-updated-baris-example-data-dan-row-action
title: "Tampilan Kolom Modified By, Last Updated, Baris Example Data, dan Row Action"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-28
  - TC-FA-TDC-29
  - TC-FA-TDC-30
  - TC-FA-TDC-31
  - TC-FA-TDC-33
coverage:
  web: automated
---

# Tampilan Kolom Modified By, Last Updated, Baris Example Data, dan Row Action

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), dua isi tabel berurutan:
  - Isi tabel A (TC-FA-TDC-28 dan 29), kunci `exampleDataWithSeedBldP`: delapan class Example Data (BLD-NP, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) ditambah class seed `BLD-P` (Building; nilai sesuai Data Seed PRD §4.1.5) yang dibuat oleh seed dan belum pernah diubah (terpisah dari baris `BLD-P` Example Data); NB-SL terakhir diubah oleh user bernama lengkap `Rina Putri` (user penyunting disediakan tim FE). Format tanggal General Settings company sudah diatur (nilai formatnya dari fixture).
  - Isi tabel B (TC-FA-TDC-30, 31, 33), kunci `exampleData`: sembilan class Example Data (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data: NB-1 (Active On, `Bukan bangunan – Kelompok 1`, Non-building, 4, 25%, 50%, `Straight Line · Declining Balance`, Used By 5, `Jan 2026`); NB-2 (`Bukan bangunan – Kelompok 2`, Non-building, 8, 12.5%, 25%, Used By 3, `—`); NB-SL (`Kelompok khusus Straight Line`, Non-building, 16, 6.25%, `—`, `Straight Line`, Used By 4, `—`); NB-4 (`Bukan bangunan – Kelompok 4`, Non-building, 20, 5%, 10%, Used By 0, `Jan 2026`); BLD-P (`Bangunan permanen`, Building, 20, 5%, `—`, `Straight Line`, Used By 1, `—`); BLD-NP (`Bangunan tidak permanen`, Building, 10, 10%, `—`, `Straight Line`, Used By 0, `—`); LAND (`Tanah`, Land, `—`, `—`, `—`, `—`, Used By 0, `—`); NB-KHS (`Kelompok khusus pernah diposting`, Non-building, 10, 10%, 20%, `Straight Line · Declining Balance`, Used By 0, `—`); NB-OLD (Active Off, `Kelompok khusus lama`, Non-building, 5, 20%, `—`, `Straight Line`, Used By 0, `—`).
- Kemampuan teknis: seeding isi tabel lewat API; user penyunting untuk Modified By; Overlay Column Visibility; mengarahkan kursor untuk tooltip; pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: konfigurasi kolom tabel (Modified By dan Last Updated ditampilkan lalu disembunyikan kembali dalam spec). Dipulihkan di hook `after` (hapus preferensi kolom di browser) sebagai cadangan.

## Test Steps

### TC-FA-TDC-28: Kolom Modified By: format nama, System untuk seed, dan tooltip nama lengkap

1. Klik header Actions `⋯`
2. Centang kolom Modified By
3. Tutup Overlay Column Visibility
4. Verifikasi Modified By baris NB-SL menampilkan `Rina P` (format `[First Name] [Last Initial]`)
5. Verifikasi Modified By baris BLD-P menampilkan `System` (record seed yang belum pernah diubah)
6. Arahkan kursor ke Modified By baris NB-SL
7. Verifikasi tooltip nama lengkap `Rina Putri` tampil

### TC-FA-TDC-29: Kolom Last Updated: format tanggal mengikuti General Settings

8. Klik header Actions `⋯`
9. Centang kolom Last Updated
10. Tutup Overlay Column Visibility
11. Verifikasi Last Updated baris NB-SL menampilkan tanggal terakhir diubah dalam format tanggal General Settings
12. Verifikasi Last Updated baris seed BLD-P menampilkan waktu record dibuat dalam format yang sama
13. Verifikasi kolom Last Updated tidak pernah kosong

### Pemulihan kolom dan penggantian isi tabel

14. Klik header Actions `⋯`
15. Hapus centang kolom Modified By
16. Hapus centang kolom Last Updated
17. Tutup Overlay Column Visibility
18. Ganti isi tabel menjadi sembilan class Example Data lewat seeding API, lalu muat ulang halaman

### TC-FA-TDC-30: Tabel menampilkan baris normal sesuai Example Data

19. Verifikasi baris NB-1: Active On, `Bukan bangunan – Kelompok 1`, Non-building, 4, 25%, 50%, `Straight Line · Declining Balance`, Used By 5, `Jan 2026`
20. Verifikasi baris NB-2: Active On, `Bukan bangunan – Kelompok 2`, Non-building, 8, 12.5%, 25%, `Straight Line · Declining Balance`, Used By 3, `—`
21. Verifikasi baris NB-SL: Active On, `Kelompok khusus Straight Line`, Non-building, 16, 6.25%, `—`, `Straight Line`, Used By 4, `—`
22. Verifikasi baris NB-4: Active On, `Bukan bangunan – Kelompok 4`, Non-building, 20, 5%, 10%, `Straight Line · Declining Balance`, Used By 0, `Jan 2026`
23. Verifikasi baris BLD-P: Active On, `Bangunan permanen`, Building, 20, 5%, `—`, `Straight Line`, Used By 1, `—`
24. Verifikasi baris BLD-NP: Active On, `Bangunan tidak permanen`, Building, 10, 10%, `—`, `Straight Line`, Used By 0, `—`

### TC-FA-TDC-31: Tabel menampilkan baris edge sesuai Example Data

25. Verifikasi baris LAND: Active On, `Tanah`, Land, `—`, `—`, `—`, `—`, Used By 0, `—`
26. Verifikasi baris NB-KHS: Active On, `Kelompok khusus pernah diposting`, Non-building, 10, 10%, 20%, `Straight Line · Declining Balance`, Used By 0, `—`
27. Verifikasi baris NB-OLD: Active Off, `Kelompok khusus lama`, Non-building, 5, 20%, `—`, `Straight Line`, Used By 0, `—`

### TC-FA-TDC-33: Screening Overlay row action: Edit dan Delete dengan icon dan severity

28. Klik ikon `⋯` pada baris NB-4
29. Verifikasi Overlay row action tampil menempel pada pemicu tanpa backdrop
30. Verifikasi opsi `Edit` dengan icon Edit2Line (severity dark)
31. Verifikasi opsi `Delete` dengan icon DeleteBin6Line (severity danger)
32. Verifikasi tidak ada opsi `Activate`, `Deactivate`, atau `Detail`
33. Tutup Overlay row action

## Notes

- Urutan TC dalam spec: TC-FA-TDC-28, 29, 30, 31, 33. Blok kolom tambahan (28 dan 29) di awal karena memakai isi tabel A; kolom dipulihkan (langkah 14 sampai 17) dan isi tabel diganti (langkah 18) sebelum TC yang memakai isi tabel B. Kolom Hidden default tidak diperlukan oleh TC-FA-TDC-30 dan 31.
- Langkah penghubung (S-03): langkah 3, 10, 17, dan 33 (menutup overlay atau menu), langkah 14 sampai 16 (pemulihan Setup Column; 8b.14, R-24; TC tidak menyebut `[Save]` sehingga tidak ditulis), langkah 18 (mengganti isi tabel lewat seeding API). Hook `after` hanya cadangan.
- Asersi absence langkah 32 didahului anchor positif langkah 30 dan 31 (opsi lain pada Overlay yang sama tampil; 8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-28 dan 29 mensyaratkan class seed `BLD-P` terpisah dari baris `BLD-P` pada Example Data; spec memakai dua isi tabel berurutan dan mengganti isinya sebelum TC-FA-TDC-30.
  - TC-FA-TDC-29 Expected a dan b tidak menyebut nilai tanggal persis (hanya "format tanggal General Settings"); spec mengasersi format dari nilai fixture General Settings dan waktu ubah NB-SL tidak diketahui TC.
  - TC-FA-TDC-29 mengandalkan format tanggal General Settings yang sudah diatur tanpa menyebut formatnya.
  - TC-FA-TDC-33 Expected a menyebut "tanpa backdrop" tanpa langkah observasi spesifik; spec mengasersinya apa adanya.
  - Email akun Total Control dan nama user penyunting selain `Rina Putri` tidak tertulis di TC.
