---
id: TC-FA-FAAM-E2E-001-screening-tab-asset-name-breadcrumb-dan-navigasi
title: "Screening Tab Asset Name: 3 Zona, Breadcrumb, Navigasi Masuk, dan Urutan Default"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-1
  - TC-FA-FAAM-2
  - TC-FA-FAAM-3
  - TC-FA-FAAM-4
  - TC-FA-FAAM-5
  - TC-FA-FAAM-36
coverage:
  web: automated
---

# Screening Tab Asset Name: 3 Zona, Breadcrumb, Navigasi Masuk, dan Urutan Default

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; spec ini tidak memakai seed API per TC dan tidak memakai sesi API aktor.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): Pre-setup #10 s.d. #14 tersedia, termasuk `Dell Latitude` (#10), `Ergonomic Chair` (#11), dan `MacBook Pro` (#12) sebagai satu-satunya Asset Name Category Locked pada client utama (hitungan Needs Update 1). Katalog client utama memuat Seed Item 01 s.d. 30 (#15), sehingga lebih dari satu halaman.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-1: Screening halaman tab Asset Name saat pertama dibuka (3 zona)

1. Amati halaman Fixed Asset > Settings > Asset Master > Asset Name yang dibuka hook `beforeEach` tanpa mengisi atau mengklik apa pun
2. Verifikasi Zona Header: Breadcrumb `Settings > Asset Master > Asset Name`
3. Verifikasi Zona Header: Tab `Asset Name (aktif) | Custom Asset ID | Labels`
4. Verifikasi Zona Header: Table Tools `Search | Filter | Download | Changelog | [+ Asset Name]` tampil
5. Verifikasi Zona Header: Notice Category Locked di bawah Table Tools dan di atas tabel dengan teks `1 asset name needs a category update.` dan aksi `Show only this`
6. Verifikasi Zona Body: kolom `Checkbox | Asset Name (sortable) | Code (sortable) | Category (sortable) | TAG Type (sortable) | Brand (sortable) | Model/Type (sortable) | Default Addon (sortable) | Default Label (sortable) | UoM (sortable) | Total Asset (sortable) | Modified By (sortable) | Last Updated (sortable) | Column Visibility (⋯) (unsortable, header klik membuka overlay Column Visibility, body per baris = row action menu)`
7. Verifikasi Zona Footer: pagination default 10 data per halaman
8. Verifikasi sedikitnya dua baris tampil pada tabel
9. Verifikasi baris tampil urut Asset Name A-Z (default sort)

### TC-FA-FAAM-36: Urutan default List adalah Asset Name A-Z case-insensitive

10. Amati tab Asset Name yang dibuka hook `beforeEach` tanpa Sort aktif
11. Verifikasi baris pada halaman pertama urut Asset Name A-Z tanpa membedakan huruf besar-kecil
12. Verifikasi header Asset Name menampilkan indikator sort default

### TC-FA-FAAM-2: Breadcrumb tab Asset Name: teks path dan state tiap segmen

13. Amati Breadcrumb di atas halaman
14. Hover segmen `Settings`
15. Hover segmen `Asset Master`
16. Hover segmen `Asset Name`
17. Verifikasi Breadcrumb tampil `Settings > Asset Master > Asset Name`
18. Verifikasi segmen pertama `Settings` berupa label statis yang tidak dapat diklik
19. Verifikasi segmen terakhir `Asset Name` berupa label statis yang tidak dapat diklik
20. Verifikasi segmen tengah `Asset Master` dapat diklik

### TC-FA-FAAM-4: Halaman tab Asset Name tanpa Page Title terpisah dan tanpa tombol Back to

21. Amati area di bawah Breadcrumb sampai Table Tools
22. Verifikasi Breadcrumb dan Table Tools tampil
23. Verifikasi tidak ada elemen Page Title (mis. teks `Asset Name` sebagai heading) di bawah Breadcrumb
24. Verifikasi tidak ada tombol atau link `← Back to`

### TC-FA-FAAM-3: Klik segmen tengah Breadcrumb membuka tab default Asset Name

25. Klik tab `Labels`
26. Klik segmen `Asset Master` pada Breadcrumb
27. Verifikasi halaman Settings > Asset Master terbuka pada tab `Asset Name` (tab default)
28. Verifikasi Breadcrumb tampil `Settings > Asset Master > Asset Name`

### TC-FA-FAAM-5: Masuk ke Settings > Asset Master tanpa segmen tab membuka tab Asset Name

29. Buka halaman utama FAMS
30. Klik menu sidebar `Settings > Asset Master`
31. Verifikasi tab `Asset Name` aktif
32. Verifikasi entri `Asset Master` tampil di sidebar sebagai satu-satunya entri Asset Master
33. Verifikasi tidak ada entri sidebar terpisah `Asset Name`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 1, 36, 2, 4, 3, 5 (screening dahulu, S-10). TC-5 diletakkan terakhir karena berpindah ke halaman utama FAMS.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 10, 13, 21 (mengamati halaman), langkah 14 sampai 16 (hover segmen sesuai langkah uji TC-2), dan langkah 29 (membuka halaman utama FAMS sebagai precondition TC-5; hook `beforeEach` membuka tab Asset Name sehingga TC-5 perlu berpindah dulu).
- Langkah 1 dan 10 mengganti langkah "Buka ..." TC-1 dan TC-36 karena halaman sudah dibuka hook `beforeEach` suite.
- Langkah 8 dan 22 adalah anchor positif (8b butir 2): sedikitnya dua baris tampil sebelum asersi urutan; Breadcrumb dan Table Tools tampil sebelum asersi absence Page Title (Table Tools dan halaman termuat menjadi anchor permukaan).
- Langkah 5: kalimat dalam kurung TC-1 iv ("hanya `MacBook Pro` berstatus Category Locked, Pre-setup #12") adalah dasar data dan tidak diasersi terpisah, karena TC-1 tidak memberi langkah klik `Show only this`.
- Langkah 9 (TC-1 d) dan langkah 11 (TC-36 a) memuat klaim urutan yang sama dan dituliskan terpisah untuk menjaga satu `Verifikasi` per Expected tiap TC.
- Temuan untuk QA:
  - TC-36 a memberi contoh `Dell Latitude` sebelum `Ergonomic Chair` pada urutan A-Z. Katalog client utama memuat Seed Item 01 s.d. 30 dan fixture lain sehingga kedua baris itu belum tentu berada di halaman pertama; spec mengasersi urutan A-Z baris pada halaman pertama dan tidak mengasersi kedua nama sebagai pasangan.
  - TC-1 Langkah 1 "Buka Fixed Asset > Settings > Asset Master" tidak menyebut URL; spec memakai pembukaan halaman oleh hook `beforeEach` suite.
