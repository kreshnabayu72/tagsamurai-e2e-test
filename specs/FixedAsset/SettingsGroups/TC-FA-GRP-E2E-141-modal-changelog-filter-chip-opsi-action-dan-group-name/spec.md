---
id: TC-FA-GRP-E2E-141-modal-changelog-filter-chip-opsi-action-dan-group-name
title: "Modal Changelog Filter: Chip Opsi Action dan Group Name (Hapus via X dan via Uncheck)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-447
  - TC-FA-GRP-448
  - TC-FA-GRP-453
  - TC-FA-GRP-454
coverage:
  web: automated
---

# Modal Changelog Filter: Chip Opsi Action dan Group Name (Hapus via X dan via Uncheck)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-141`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-141` sampai `Log4 {runId}-141` adalah group level 1; Description awal group `Log2 {runId}-141` dan `Log3 {runId}-141` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-141` | Group Name | `—` | `Log1 {runId}-141` | ModA | 1 |
| 2 | Create | `Log2 {runId}-141` | Group Name | `—` | `Log2 {runId}-141` | ModA | 1 |
| 3 | Create | `Log3 {runId}-141` | Group Name | `—` | `Log3 {runId}-141` | ModB | 1 |
| 4 | Create | `Log4 {runId}-141` | Group Name | `—` | `Log4 {runId}-141` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-141` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-141` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-141` | Code | `LA141` | `LB141` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-141` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-141` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-141` | Code | `LC141` | `LD141` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-141` | Group Name | `Log4 {runId}-141` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-141` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-141` sampai `Log4 {runId}-141` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- Parameter iterasi TC-FA-GRP-447, 448, 453, 454 (satu iterasi memuat dua TC: hapus chip via (X), lalu hapus chip via uncheck), urutan baris = urutan iterasi:

| Field | Opsi A | Opsi B | Baris yang harus tampil (hanya opsi B) | Baris yang tidak boleh tampil (opsi A) |
|---|---|---|---|---|
| Action | `Create` | `Delete` | baris Action Delete Group Name `Log4 {runId}-141` | baris Action Create Group Name `Log1 {runId}-141` |
| Group Name | `Log1 {runId}-141` | `Log3 {runId}-141` | baris Action Create Group Name `Log3 {runId}-141` | baris Action Create Group Name `Log1 {runId}-141` |

## Test Steps

1. Klik icon Changelog
2. Ketik Search `{runId}-141`, tekan Enter

### TC-FA-GRP-447, 448, 453, 454: Chip opsi Filter per field (iterasi per field)

3. Untuk setiap baris tabel parameter iterasi (langkah 4 sampai 29): jalankan langkah berikut dengan field dan opsi pada baris itu
4. Klik icon Filter
5. Klik [Clear Field]
6. Centang opsi A lalu opsi B pada dropdown field baris tabel
7. Tutup dropdown
8. Verifikasi chip opsi A dan chip opsi B tampil di dalam field (chip opsi B tidak menggantikan chip opsi A)
9. Klik (X) pada chip opsi A
10. Verifikasi chip opsi A hilang dari field
11. Buka dropdown field baris tabel
12. Verifikasi checkbox opsi A di dropdown ter-uncheck
13. Verifikasi chip opsi B tetap ada
14. Tutup dropdown
15. Klik [Apply]
16. Verifikasi baris yang harus tampil pada baris tabel tampil (tabel hanya menyaring opsi B)
17. Verifikasi baris yang tidak boleh tampil pada baris tabel tidak tampil
18. Klik icon Filter
19. Klik [Clear Field]
20. Centang opsi A lalu opsi B pada dropdown field baris tabel
21. Buka lagi dropdown field baris tabel dan hilangkan centang opsi A dari dalam dropdown
22. Verifikasi chip opsi A hilang dari field
23. Verifikasi chip opsi B tetap ada
24. Klik [Apply]
25. Verifikasi baris yang harus tampil pada baris tabel tampil (tabel hanya menyaring opsi B)
26. Verifikasi baris yang tidak boleh tampil pada baris tabel tidak tampil
27. Klik icon Filter
28. Klik [Clear Field]
29. Klik [Apply]
30. Klik `(←)` pada kotak Search
31. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 4 sampai 29 diulang untuk tiap baris tabel parameter iterasi (2 field x 24 langkah). Tiap `Verifikasi` tetap satu per klausa.
- Opsi A dan opsi B untuk tiap field ditentukan spec dari dataset (TC menyebut "opsi A lalu opsi B" tanpa nilai); Modified By dan Group Name memakai nama opsi pada kolom tabel parameter iterasi.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka dan menutup Modal Changelog, membatasi tabel dengan Search suffix spec, membuka/menutup dropdown, serta [Clear Field] + [Apply] sebagai pemulihan state antar TC (S-03, S-09, R-16).
- Spec 31 langkah (ekspansi iterasi ± 53 langkah), di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah per kolom/field memakai tabel di Prerequisites (bagian 8b butir 7).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
