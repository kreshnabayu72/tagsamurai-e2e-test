---
id: TC-GS-UOM-E2E-048-changelog-filter-dropdown-search-dan-or
title: "Changelog Measurement: Filter per Field, Opsi Dropdown, dan Logika AND/OR"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-178
  - TC-GS-UOM-179
  - TC-GS-UOM-180
  - TC-GS-UOM-181
  - TC-GS-UOM-182
coverage:
  web: automated
---

# Changelog Measurement: Filter per Field, Opsi Dropdown, dan Logika AND/OR

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` suite (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Layar awal Global Settings > Master Reference > Measurement dibuka di hook `beforeEach` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel true oleh hook suite (lihat bagian "Hook suite" di `suite.md`).
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.
- Seeding (lewat API oleh Sari Dewi di hook `before`, urutan sebagai berikut):
  - Population D-01 (setara TC-GS-UOM-36), idempotent (nama yang sudah ada dilewati): `Centimeter`, `Foot`, `Gallon`, `Inch`, `Milliliter`, `Millimeter`, `Ounce`, `Pound`, `Roll`, `Set`, `Sheet`, `Ton`. Menghasilkan entri Create oleh `Sari D` (dipakai TC-GS-UOM-180 dan 181).
  - Unit milik spec `Gallon {runId}-048` (Symbol `gl`) dibuat, lalu Symbol-nya diubah menjadi `oz.` (entri Create dan entri Edit, Field `Symbol`; dipakai TC-GS-UOM-180 dan 181).
  - Unit milik spec `Hapus {runId}-048` dibuat lalu dihapus (entri Create dan entri Delete; menjamin opsi Action `Delete` ada pada Changelog; dipakai TC-GS-UOM-180). Aksi ini dilakukan paling akhir sehingga entri Delete bukan Create/Edit terbaru yang dibutuhkan TC-GS-UOM-181.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Gallon {runId}-048` dan unit Population yang dibuat spec ini (yang sudah ada sebelum spec dilewati). Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: memilih rentang tanggal pada date range picker (hari uji); membuka dropdown multi-select dan membaca daftar opsinya; membaca teks tanggal pada kolom Date.
- Akun yang hanya dirujuk sebagai nama (tidak login): `Maya Putri` (`Maya P`, Read Only, `readOnly_automated_qaTeam1@qwertysystem.net`), akun yang tidak pernah mengubah Measurement Client A; dipakai langkah 24 (syarat: Maya Putri tidak pernah memutasi Measurement Client A).
- Precondition TC-GS-UOM-178, 179, 180, 181, 182: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement. TC-GS-UOM-180 dan 182 bergantung pada Population (TC-GS-UOM-36); TC-GS-UOM-181 bergantung pada Edit (TC-GS-UOM-71) yang dipenuhi seeding `Gallon {runId}-048`.

## Test Steps

### TC-GS-UOM-178: Screening Filter Panel Modal Changelog

1. Klik icon Changelog di halaman Global Settings > Master Reference > Measurement
2. Klik Filter
3. Verifikasi field `Date` tampil di Filter Panel
4. Verifikasi field `Action` dengan placeholder `All actions`
5. Verifikasi field `Unit Name` dengan placeholder `All units`
6. Verifikasi field `Field` dengan placeholder `All fields`
7. Verifikasi field `Modified By` dengan placeholder `All users`

### TC-GS-UOM-179: Placeholder field Date Filter Modal Changelog

8. Verifikasi placeholder field Date `Select date`

### TC-GS-UOM-180 dan TC-GS-UOM-178 butir b: Opsi dropdown dan jenis field

9. Buka dropdown Action
10. Verifikasi dropdown Action bertipe multi-select searchable (TC-GS-UOM-178 butir b)
11. Verifikasi opsi Action hanya `Create`, `Edit`, dan `Delete`
12. Tutup dropdown Action
13. Buka dropdown Unit Name
14. Verifikasi dropdown Unit Name bertipe multi-select searchable (TC-GS-UOM-178 butir b)
15. Verifikasi opsi Unit Name memuat `Centimeter` dan `Gallon {runId}-048` (nilai yang muncul di Changelog)
16. Tutup dropdown Unit Name
17. Buka dropdown Field
18. Verifikasi dropdown Field bertipe multi-select searchable (TC-GS-UOM-178 butir b)
19. Verifikasi opsi Field hanya `Unit Name` dan `Symbol`
20. Tutup dropdown Field
21. Buka dropdown Modified By
22. Verifikasi dropdown Modified By bertipe multi-select searchable (TC-GS-UOM-178 butir b)
23. Verifikasi opsi Modified By memuat `Sari D`
24. Verifikasi opsi Modified By tidak memuat `Maya P`
25. Tutup dropdown Modified By

### TC-GS-UOM-181: Filter Changelog: OR dalam satu field dan AND antar field

26. Pilih Action `Create` dan `Edit`
27. Klik [Apply]
28. Verifikasi hasil memuat baris Action `Create`
29. Verifikasi hasil memuat baris Action `Edit`
30. Pilih Field `Symbol`
31. Klik [Apply]
32. Verifikasi hasil memuat baris Action `Edit`, Field `Symbol`, Unit Name `Gallon {runId}-048`
33. Verifikasi setiap baris yang tampil memiliki Action `Edit` dan Field `Symbol`

### TC-GS-UOM-182: Filter Date Changelog menyaring berdasarkan rentang

34. Kosongkan field Action dan field Field
35. Pilih Date hari uji (tanggal awal dan akhir rentang sama dengan hari uji)
36. Klik [Apply]
37. Verifikasi sedikitnya satu baris tampil di tabel Changelog
38. Verifikasi setiap baris yang tampil bertanggal hari uji pada kolom Date

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Modal Changelog dan Filter Panel dibuka sekali (langkah 1 dan 2). TC-GS-UOM-178 butir b (field multi-select searchable) diasersi pada pembukaan dropdown TC-GS-UOM-180 (langkah 10, 14, 18, 22), supaya tiap dropdown dibuka sekali; TC-GS-UOM-178 butir a ada di langkah 4 sampai 7. TC-GS-UOM-178 dan 180 tetap punya `Verifikasi` sendiri-sendiri.
- Urutan TC sumber dipertahankan kecuali TC-GS-UOM-179 (placeholder Date, pengamatan tanpa aksi) setelah TC-GS-UOM-178 sebagai screening Filter Panel.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12, 16, 20, 25 (menutup dropdown), dan langkah 34 (mengosongkan filter TC-GS-UOM-181 sebelum TC-GS-UOM-182).
- Langkah 28 sampai 29 mengasersi OR (keduanya tampil). Langkah 32 adalah pembanding positif bagi langkah 33 (asersi universal AND). Langkah 37 adalah pembanding positif bagi langkah 38.
- Spec ini di atas batas 35 langkah (38): seluruhnya satu kelas (filter Changelog) pada satu modal Changelog yang dibuka sekali dan satu dataset entri; memecahnya hanya menambah pembukaan modal dan seeding yang sama.
- Temuan untuk QA:
  - TC-GS-UOM-180 Expected a menyatakan opsi Unit Name dan Modified By "hanya" berisi nilai yang muncul di Changelog. Untuk Unit Name tidak ada nilai pembanding negatif yang deterministik, sehingga spec hanya mengasersi kehadiran `Centimeter` dan `Gallon {runId}-048`; untuk Modified By mengasersi kehadiran `Sari D` dan ketidakhadiran `Maya P` (Read Only tidak pernah memutasi). Opsi Field dan Action diasersi persis.
  - TC-GS-UOM-182: kata "hanya entri hari ini" diasersi sebagai semua baris yang tampil bertanggal hari uji; tidak ada jaminan di TC bahwa Changelog Client A berisi entri bertanggal selain hari uji, sehingga pengecualian entri non-hari-ini tidak teruji.
  - TC-GS-UOM-181 tidak menyebut tombol atau cara "Clear Filter"; spec mengosongkan field lalu [Apply].
  - Panel Filter sesudah `[Apply]`: langkah 30 dan 34 tidak membuka ulang panel karena spec mengasumsikan panel tetap terbuka sesudah `[Apply]` (langkah 27 dan 31). TC-GS-UOM-181 langkah 2 ("Tambah Field `Symbol`, Apply") mengisyaratkan hal yang sama. Asumsi kerja ini belum diamati di aplikasi: prd-conventions §9.8 hanya menyebut penutupan panel lewat klik luar panel atau klik ulang icon Filter dan tidak menyatakan keadaan panel sesudah `[Apply]`. Spec 037, 038, 039, dan 045 memakai asumsi yang sama. Bila aplikasi menutup panel sesudah `[Apply]`, langkah 30 dan 34 perlu diawali `Klik Filter`.
