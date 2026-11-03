---
id: TC-FA-GRP-E2E-143-modal-changelog-kombinasi-search-filter-irisan-dan-search-filter-sort-pagination
title: "Modal Changelog Kombinasi: Search lalu Filter, Filter lalu Search, dan Search + Filter + Sort + Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-469
  - TC-FA-GRP-470
  - TC-FA-GRP-478
coverage:
  web: automated
---

# Modal Changelog Kombinasi: Search lalu Filter, Filter lalu Search, dan Search + Filter + Sort + Pagination

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-143`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-143` sampai `Log4 {runId}-143` adalah group level 1; Description awal group `Log2 {runId}-143` dan `Log3 {runId}-143` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-143` | Group Name | `—` | `Log1 {runId}-143` | ModA | 1 |
| 2 | Create | `Log2 {runId}-143` | Group Name | `—` | `Log2 {runId}-143` | ModA | 1 |
| 3 | Create | `Log3 {runId}-143` | Group Name | `—` | `Log3 {runId}-143` | ModB | 1 |
| 4 | Create | `Log4 {runId}-143` | Group Name | `—` | `Log4 {runId}-143` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-143` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-143` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-143` | Code | `LA143` | `LB143` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-143` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-143` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-143` | Code | `LC143` | `LD143` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-143` | Group Name | `Log4 {runId}-143` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-143` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-143` sampai `Log4 {runId}-143` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- Kombinasi filter lengkap (dipakai TC-FA-GRP-469 dan 470): Date tanggal hari ini s.d. tanggal hari ini; Action `Edit`; Group Name `Log2 {runId}-143`; Field `Description`; Modified By `ModA`. Irisan dengan Search suffix spec: satu baris (baris Action Edit Group Name `Log2 {runId}-143` Field Description). Di luar irisan (alasan): baris Action Edit Group Name `Log3 {runId}-143` Field Description (Group Name dan Modified By), baris Action Edit Group Name `Log2 {runId}-143` Field Function (Field).
- Kombinasi TC-FA-GRP-478: Search suffix spec, filter Action `Edit` (7 entri: batch 2 = 4 entri, batch 3 = 3 entri), sort Date Newest First, page size 25.

## Test Steps

1. Klik icon Changelog

### TC-FA-GRP-469: Search lalu Filter (irisan)

2. Ketik Search `{runId}-143`, tekan Enter
3. Klik icon Filter
4. Isi Date tanggal hari ini sampai tanggal hari ini
5. Pilih `Edit` pada dropdown Action
6. Pilih `Log2 {runId}-143` pada dropdown Group Name
7. Pilih `Description` pada dropdown Field
8. Pilih `ModA` pada dropdown Modified By
9. Klik [Apply]
10. Verifikasi baris Action Edit Group Name `Log2 {runId}-143` Field Description tampil (satu-satunya irisan Search dan Filter)
11. Verifikasi baris Action Edit Group Name `Log3 {runId}-143` Field Description tidak tampil
12. Verifikasi baris Action Edit Group Name `Log2 {runId}-143` Field Function tidak tampil
13. Verifikasi keyword Search `{runId}-143` tetap terpasang pada kotak Search

### TC-FA-GRP-470: Filter lalu Search (irisan)

14. Klik `(←)` pada kotak Search
15. Klik icon Filter
16. Klik [Clear Field]
17. Klik [Apply]
18. Klik icon Filter
19. Isi Date tanggal hari ini sampai tanggal hari ini
20. Pilih `Edit` pada dropdown Action
21. Pilih `Log2 {runId}-143` pada dropdown Group Name
22. Pilih `Description` pada dropdown Field
23. Pilih `ModA` pada dropdown Modified By
24. Klik [Apply]
25. Ketik Search `{runId}-143`, tekan Enter
26. Verifikasi baris Action Edit Group Name `Log2 {runId}-143` Field Description tampil (satu-satunya irisan Search dan Filter)
27. Verifikasi baris Action Edit Group Name `Log3 {runId}-143` Field Description tidak tampil
28. Verifikasi baris Action Edit Group Name `Log2 {runId}-143` Field Function tidak tampil
29. Verifikasi kriteria filter tetap aktif: indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-478: Kombinasi Search + Filter + Sort + Pagination

30. Klik `(←)` pada kotak Search
31. Klik icon Filter
32. Klik [Clear Field]
33. Klik [Apply]
34. Ketik Search `{runId}-143`, tekan Enter
35. Klik icon Filter
36. Pilih `Edit` pada dropdown Action
37. Klik [Apply]
38. Klik header Date dua kali sampai sort Newest First
39. Ubah page size ke 25
40. Verifikasi keyword Search `{runId}-143` tetap terpasang pada kotak Search
41. Verifikasi indikator filter aktif tampil pada icon Filter
42. Verifikasi page size 25 tetap terpilih
43. Verifikasi urutan Newest First pada himpunan irisan: baris 1 sampai 3 adalah entri batch 3 dan baris 4 sampai 7 adalah entri batch 2
44. Klik header Date satu kali sampai sort netral
45. Klik `(←)` pada kotak Search
46. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): mengisi kombinasi filter pada Prerequisites, membersihkan Search dan filter antar TC, mengembalikan sort ke netral di akhir (S-03, S-09, R-16).
- Kombinasi filter dan Search K ditentukan spec karena TC menyebut "nilai yang beririsan" tanpa nilai.
- Spec 46 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
