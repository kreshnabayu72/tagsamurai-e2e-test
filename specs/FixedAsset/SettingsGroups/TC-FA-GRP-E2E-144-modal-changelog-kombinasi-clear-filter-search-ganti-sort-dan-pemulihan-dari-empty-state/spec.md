---
id: TC-FA-GRP-E2E-144-modal-changelog-kombinasi-clear-filter-search-ganti-sort-dan-pemulihan-dari-empty-state
title: "Modal Changelog Kombinasi: Clear Filter/Search Saat Lainnya Aktif, Ganti Target Sort, dan Pemulihan dari Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-479
  - TC-FA-GRP-480
  - TC-FA-GRP-481
  - TC-FA-GRP-482
coverage:
  web: automated
---

# Modal Changelog Kombinasi: Clear Filter/Search Saat Lainnya Aktif, Ganti Target Sort, dan Pemulihan dari Empty State

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-144`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-144` sampai `Log4 {runId}-144` adalah group level 1; Description awal group `Log2 {runId}-144` dan `Log3 {runId}-144` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-144` | Group Name | `—` | `Log1 {runId}-144` | ModA | 1 |
| 2 | Create | `Log2 {runId}-144` | Group Name | `—` | `Log2 {runId}-144` | ModA | 1 |
| 3 | Create | `Log3 {runId}-144` | Group Name | `—` | `Log3 {runId}-144` | ModB | 1 |
| 4 | Create | `Log4 {runId}-144` | Group Name | `—` | `Log4 {runId}-144` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-144` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-144` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-144` | Code | `LA144` | `LB144` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-144` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-144` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-144` | Code | `LC144` | `LD144` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-144` | Group Name | `Log4 {runId}-144` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-144` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-144` sampai `Log4 {runId}-144` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- State awal untuk TC-FA-GRP-479, 480, 481: Search suffix spec, filter Action `Edit`, sort Date Newest First (Edit = 7 entri seeding).

## Test Steps

1. Klik icon Changelog

### TC-FA-GRP-479: Clear Filter saat Search dan Sort aktif

2. Ketik Search `{runId}-144`, tekan Enter
3. Klik icon Filter
4. Pilih `Edit` pada dropdown Action
5. Klik [Apply]
6. Klik header Date dua kali sampai sort Newest First
7. Klik icon Filter
8. Klik [Clear Field]
9. Klik [Apply]
10. Verifikasi keyword Search `{runId}-144` tetap terpasang pada kotak Search
11. Verifikasi sort Date Newest First tetap berlaku: baris pertama adalah entri seeding batch 3
12. Verifikasi baris Action Delete Group Name `Log4 {runId}-144` tampil (kriteria filter terlepas)

### TC-FA-GRP-480: Clear Search saat Filter dan Sort aktif

13. Klik icon Filter
14. Pilih `Edit` pada dropdown Action
15. Klik [Apply]
16. Klik `✕` pada kotak Search
17. Tekan Enter
18. Verifikasi kotak Search kosong
19. Verifikasi indikator filter aktif tetap tampil pada icon Filter
20. Verifikasi sedikitnya satu baris tampil pada tabel
21. Verifikasi baris Action Delete Group Name `Log4 {runId}-144` tidak tampil (filter Action `Edit` tetap berlaku)
22. Verifikasi sort Date Newest First tetap berlaku: baris pertama adalah entri Action `Edit` seeding batch 3

### TC-FA-GRP-481: Ganti target sort saat Search dan Filter aktif

23. Ketik Search `{runId}-144`, tekan Enter
24. Klik header Date satu kali sampai sort netral
25. Klik header Group Name satu kali (Ascending)
26. Klik header Field
27. Verifikasi sort berpindah ke kolom Field Ascending: baris 1 dan 2 ber-Field `Code`, baris 3 dan 4 ber-Field `Description`, baris 5 sampai 7 ber-Field `Function`
28. Verifikasi sort kolom Group Name kembali netral
29. Verifikasi baris Action Delete Group Name `Log4 {runId}-144` tidak tampil (Search dan filter tetap menyaring)
30. Klik header Field dua kali sampai sort netral

### TC-FA-GRP-482: Pemulihan dari empty state hasil Search + Filter

31. Klik icon Filter
32. Klik [Clear Field]
33. Klik [Apply]
34. Ganti isi kotak search dengan `delete`, tekan Enter
35. Klik icon Filter
36. Pilih `Create` pada dropdown Action
37. Klik [Apply]
38. Verifikasi empty state tampil dengan Illustration, title `No results found`, dan body `Try adjusting your search or filter.`
39. Klik icon Filter
40. Klik [Clear Field]
41. Klik [Apply]
42. Verifikasi baris Action Delete Group Name `Log4 {runId}-144` tampil (tabel pulih)
43. Klik `(←)` pada kotak Search
44. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membentuk state awal Search + Filter + Sort, membersihkan filter dan Search antar TC, dan mengembalikan sort ke netral (S-03, S-09, R-16). Pada TC-FA-GRP-480 filter Action `Edit` dipasang ulang karena TC-FA-GRP-479 melepasnya.
- TC-FA-GRP-481: kolom A = Group Name (Ascending) dan kolom B = Field; TC-FA-GRP-482: Search `delete` dengan filter Action `Create` tidak beririsan. Keduanya ditentukan spec karena TC memakai "K", "A", "B" tanpa nilai.
- Spec 44 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
