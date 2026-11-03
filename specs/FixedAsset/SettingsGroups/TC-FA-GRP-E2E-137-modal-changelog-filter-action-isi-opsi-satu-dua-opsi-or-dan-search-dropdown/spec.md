---
id: TC-FA-GRP-E2E-137-modal-changelog-filter-action-isi-opsi-satu-dua-opsi-or-dan-search-dropdown
title: "Modal Changelog Filter Action: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-443
  - TC-FA-GRP-444
  - TC-FA-GRP-445
  - TC-FA-GRP-446
coverage:
  web: automated
---

# Modal Changelog Filter Action: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-137`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-137` sampai `Log4 {runId}-137` adalah group level 1; Description awal group `Log2 {runId}-137` dan `Log3 {runId}-137` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-137` | Group Name | `—` | `Log1 {runId}-137` | ModA | 1 |
| 2 | Create | `Log2 {runId}-137` | Group Name | `—` | `Log2 {runId}-137` | ModA | 1 |
| 3 | Create | `Log3 {runId}-137` | Group Name | `—` | `Log3 {runId}-137` | ModB | 1 |
| 4 | Create | `Log4 {runId}-137` | Group Name | `—` | `Log4 {runId}-137` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-137` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-137` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-137` | Code | `LA137` | `LB137` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-137` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-137` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-137` | Code | `LC137` | `LD137` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-137` | Group Name | `Log4 {runId}-137` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-137` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-137` sampai `Log4 {runId}-137` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).

## Test Steps

1. Klik icon Changelog
2. Ketik Search `{runId}-137`, tekan Enter

### TC-FA-GRP-443: Isi opsi dropdown Filter Action

3. Klik icon Filter
4. Buka dropdown Action
5. Verifikasi opsi `Create`, `Edit`, dan `Delete` tampil sebagai nilai Action distinct pada baris tabel
6. Verifikasi kotak search internal tampil di dalam dropdown
7. Centang opsi `Create` dan opsi `Delete`
8. Verifikasi opsi `Create` dan `Delete` keduanya tercentang (multi-select)
9. Hilangkan centang opsi `Create` dan `Delete`

### TC-FA-GRP-444: Filter Action satu opsi

10. Pilih opsi `Delete` pada dropdown Action
11. Klik [Apply]
12. Verifikasi sedikitnya satu baris tampil pada tabel
13. Verifikasi baris Action Delete Group Name `Log4 {runId}-137` tampil
14. Verifikasi baris Action Create Group Name `Log1 {runId}-137` tidak tampil
15. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-445: Filter Action dua opsi (OR)

16. Klik icon Filter
17. Klik [Clear Field]
18. Centang opsi `Create` dan opsi `Delete` pada dropdown Action
19. Klik [Apply]
20. Verifikasi baris Action Create Group Name `Log1 {runId}-137` dan baris Action Delete Group Name `Log4 {runId}-137` tampil (opsi 1 atau opsi 2)
21. Verifikasi baris Action Edit Group Name `Log1 {runId}-137` Field Function tidak tampil

### TC-FA-GRP-446: Search internal dropdown Filter Action

22. Klik icon Filter
23. Klik [Clear Field]
24. Buka dropdown Action
25. Ketik `ele` huruf kecil di kotak search dropdown
26. Verifikasi daftar opsi menyempit: opsi `Delete` tampil
27. Verifikasi opsi `Create` tidak tampil
28. Ganti isi kotak search dropdown dengan `zzz-tidak-ada`
29. Verifikasi daftar opsi kosong dengan teks `No results found` (teks saja, tanpa ilustrasi)
30. Klik [Apply]
31. Klik `(←)` pada kotak Search
32. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Modal Changelog, membatasi tabel dengan Search suffix spec, membuka Filter Panel dan dropdown, menghilangkan centang pada TC pertama, serta [Clear Field] + [Apply] dan `(←)` sebagai pemulihan state antar TC (S-03, S-09, R-16).
- Pilihan opsi untuk satu opsi, dua opsi, dan potongan nama pencarian dropdown ditentukan spec dari dataset karena TC menyebut "1 opsi", "2 opsi berbeda", dan "potongan nama opsi" tanpa nilai.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
