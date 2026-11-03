---
id: TC-FA-GRP-E2E-171-tab-users-filter-custom-field-multi-dropdown-date-dan-kombinasi-and
title: "Tab Users Filter Custom Field Multi-Dropdown dan Date serta Kombinasi AND (Group Role + Activation Status, Position + Division)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-610
  - TC-FA-GRP-1016
  - TC-FA-GRP-1105
  - TC-FA-GRP-1106
coverage:
  web: automated
---

# Tab Users Filter Custom Field Multi-Dropdown dan Date serta Kombinasi AND (Group Role + Activation Status, Position + Division)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role. Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Opsi A dan opsi B: dua nilai distinct dari kolom yang difilter pada tabel Warehouse A (diambil dari data tabel saat spec berjalan).
- Data Custom Field (S-11; di-seed sendiri oleh spec ini di hook `before` lewat sesi API aktor, bersuffix `{runId}`; hook `after` menghapus kedua Custom Field itu dan preferensi kolom): `Keahlian {runId}` (multi-dropdown: Forklift, Crane, Welding) dengan user U1 Forklift, U2 Crane dan Welding, U3 Welding, U4 Forklift dan Crane, U5 tanpa nilai; `Tanggal Bergabung {runId}` (date) dengan U1 05/01/26, U2 10/01/26, U3 15/01/26, U4 tanpa nilai; Date Format General Settings = dd/MM/yy (default, tidak diubah spec). Kode U1..U5 dikenali lewat email fixture baru `Fixture.groupsTabUsers.u1..u5.email`.
- Untuk kombinasi AND: pilihan Position dan Division yang beririsan dengan sedikitnya satu baris dan tidak semua baris; satu Group Role dan satu Activation Status dengan hasil serupa (nilai ditetapkan tim FE sebagai `Fixture.groupsTabUsers.andPosition`, `andDivision`, `andGroupRole`, `andActivation`).

## Test Steps

1. Klik angka Total User Warehouse A
2. Klik icon Filter

### TC-610: Kombinasi Position + Division (AND)

3. Isi Position dan Division dengan nilai dari fixture, klik [Apply]
4. Verifikasi sedikitnya satu baris tampil pada tabel
5. Verifikasi hanya baris yang memenuhi kedua kriteria tampil (AND antar-field)
6. Buka Filter, klik [Clear Field], klik [Apply]

### TC-1016: Kombinasi Group Role + Activation Status (AND)

7. Klik icon Filter
8. Pilih satu Group Role dan satu Activation Status dari fixture, klik [Apply]
9. Verifikasi sedikitnya satu baris tampil pada tabel
10. Verifikasi hanya baris yang memenuhi kedua kriteria tampil (AND antar-field)
11. Verifikasi baris yang hanya memenuhi salah satu kriteria tidak tampil
12. Buka Filter, klik [Clear Field], klik [Apply]

### TC-1105: Custom Field Multi-Dropdown

13. Klik icon Filter
14. Verifikasi field filter `Keahlian {runId}` tampil sebagai multi-select searchable dengan placeholder `All [plural noun]`
15. Pada field `Keahlian {runId}` pilih Forklift dan Crane, klik [Apply]
16. Verifikasi baris U1, U2, dan U4 tampil (nilai memuat Forklift atau Crane)
17. Verifikasi baris U3 dan U5 tidak tampil
18. Buka Filter, klik [Clear Field], klik [Apply]

### TC-1106: Custom Field Date

19. Klik icon Filter
20. Buka date range picker `Tanggal Bergabung {runId}`, pilih tanggal awal 05/01/26 dan tanggal akhir 10/01/26
21. Verifikasi tanggal terpilih ditampilkan dengan format Date Format General Settings (dd/MM/yy)
22. Klik [Apply]
23. Verifikasi baris U1 dan U2 tampil (tanggal awal dan akhir inklusif)
24. Verifikasi baris U3 dan U4 tidak tampil
25. Buka Filter, pilih tanggal awal 10/01/26 dan tanggal akhir 10/01/26, klik [Apply]
26. Verifikasi hanya baris U2 yang tampil (tanggal awal sama dengan tanggal akhir)
27. Verifikasi user tanpa nilai tidak tampil pada kedua penerapan
28. Buka Filter, klik [Clear Field], klik [Apply]

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): `Buka Filter, klik [Clear Field], klik [Apply]` antar TC dan di akhir spec (S-09).
- Asersi tambahan (S-03, 8b.2): `Verifikasi sedikitnya satu baris tampil pada tabel` ditambahkan sebelum asersi hasil Search atau Filter yang bersifat universal ("hanya baris ...", "nilai lain tidak tampil") agar asersi tidak vacuous; bukan klausa Expected TC.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - Custom Field User beserta nilainya pada user Warehouse A tidak tertulis di Tabel Pre-setup TC; spec men-seed Custom Field sendiri di hook `before` (bersuffix `{runId}`) dan menghapusnya di hook `after` (S-11).
  - TC-610 menyebut "Isi Position dan Division" tanpa nilai; spec memakai nilai beririsan dari fixture. Asersi tambahan "baris yang hanya memenuhi salah satu kriteria tidak tampil" hanya ada di TC-1016.
