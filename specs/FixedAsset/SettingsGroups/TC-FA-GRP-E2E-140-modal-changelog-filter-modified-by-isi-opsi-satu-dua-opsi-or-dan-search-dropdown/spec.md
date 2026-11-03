---
id: TC-FA-GRP-E2E-140-modal-changelog-filter-modified-by-isi-opsi-satu-dua-opsi-or-dan-search-dropdown
title: "Modal Changelog Filter Modified By: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-461
  - TC-FA-GRP-462
  - TC-FA-GRP-463
  - TC-FA-GRP-464
coverage:
  web: automated
---

# Modal Changelog Filter Modified By: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-140`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-140` sampai `Log4 {runId}-140` adalah group level 1; Description awal group `Log2 {runId}-140` dan `Log3 {runId}-140` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-140` | Group Name | `—` | `Log1 {runId}-140` | ModA | 1 |
| 2 | Create | `Log2 {runId}-140` | Group Name | `—` | `Log2 {runId}-140` | ModA | 1 |
| 3 | Create | `Log3 {runId}-140` | Group Name | `—` | `Log3 {runId}-140` | ModB | 1 |
| 4 | Create | `Log4 {runId}-140` | Group Name | `—` | `Log4 {runId}-140` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-140` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-140` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-140` | Code | `LA140` | `LB140` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-140` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-140` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-140` | Code | `LC140` | `LD140` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-140` | Group Name | `Log4 {runId}-140` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-140` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-140` sampai `Log4 {runId}-140` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).

## Test Steps

1. Klik icon Changelog
2. Ketik Search `{runId}-140`, tekan Enter

### TC-FA-GRP-461: Isi opsi dropdown Filter Modified By

3. Klik icon Filter
4. Buka dropdown Modified By
5. Verifikasi opsi `ModA`, `ModB`, dan `ModC` tampil sebagai nilai Modified By distinct pada baris tabel
6. Verifikasi kotak search internal tampil di dalam dropdown
7. Centang opsi `ModA` dan opsi `ModB`
8. Verifikasi opsi `ModA` dan `ModB` keduanya tercentang (multi-select)
9. Hilangkan centang opsi `ModA` dan `ModB`

### TC-FA-GRP-462: Filter Modified By satu opsi

10. Pilih opsi `ModB` pada dropdown Modified By
11. Klik [Apply]
12. Verifikasi sedikitnya satu baris tampil pada tabel
13. Verifikasi baris Action Create Group Name `Log3 {runId}-140` tampil
14. Verifikasi baris Action Create Group Name `Log1 {runId}-140` tidak tampil
15. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-463: Filter Modified By dua opsi (OR)

16. Klik icon Filter
17. Klik [Clear Field]
18. Centang opsi `ModA` dan opsi `ModB` pada dropdown Modified By
19. Klik [Apply]
20. Ganti isi kotak Search dengan `Log1 {runId}-140`, tekan Enter
21. Verifikasi baris Action Create Group Name `Log1 {runId}-140` tampil (opsi 1)
22. Ganti isi kotak Search dengan `Log3 {runId}-140`, tekan Enter
23. Verifikasi baris Action Create Group Name `Log3 {runId}-140` tampil (opsi 2)
24. Ganti isi kotak Search dengan `Log1 {runId}-140`, tekan Enter
25. Verifikasi baris Action Edit Group Name `Log1 {runId}-140` Field Function (Modified By `ModC`) tidak tampil

### TC-FA-GRP-464: Search internal dropdown Filter Modified By

26. Klik icon Filter
27. Klik [Clear Field]
28. Buka dropdown Modified By
29. Ketik potongan nama `ModC` huruf kecil di kotak search dropdown
30. Verifikasi daftar opsi menyempit: opsi `ModC` tampil
31. Verifikasi opsi `ModA` tidak tampil
32. Ganti isi kotak search dropdown dengan `zzz-tidak-ada`
33. Verifikasi daftar opsi kosong dengan teks `No results found` (teks saja, tanpa ilustrasi)
34. Klik [Apply]
35. Klik `(←)` pada kotak Search
36. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Modal Changelog, membatasi tabel dengan Search suffix spec, membuka Filter Panel dan dropdown, menghilangkan centang pada TC pertama, serta [Clear Field] + [Apply] dan `(←)` sebagai pemulihan state antar TC (S-03, S-09, R-16).
- Pilihan opsi untuk satu opsi, dua opsi, dan potongan nama pencarian dropdown ditentukan spec dari dataset karena TC menyebut "1 opsi", "2 opsi berbeda", dan "potongan nama opsi" tanpa nilai.
- Filter ModA atau ModB meloloskan 11 entri dengan page size 10, sehingga baris bernama dicari lewat Search nama bersuffix sebelum asersi (S-03, R-16).
- Spec 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
