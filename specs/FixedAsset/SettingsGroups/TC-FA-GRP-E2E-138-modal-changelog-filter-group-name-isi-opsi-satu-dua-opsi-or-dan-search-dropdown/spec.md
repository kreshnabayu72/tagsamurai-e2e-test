---
id: TC-FA-GRP-E2E-138-modal-changelog-filter-group-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown
title: "Modal Changelog Filter Group Name: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-449
  - TC-FA-GRP-450
  - TC-FA-GRP-451
  - TC-FA-GRP-452
coverage:
  web: automated
---

# Modal Changelog Filter Group Name: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-138`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-138` sampai `Log4 {runId}-138` adalah group level 1; Description awal group `Log2 {runId}-138` dan `Log3 {runId}-138` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-138` | Group Name | `—` | `Log1 {runId}-138` | ModA | 1 |
| 2 | Create | `Log2 {runId}-138` | Group Name | `—` | `Log2 {runId}-138` | ModA | 1 |
| 3 | Create | `Log3 {runId}-138` | Group Name | `—` | `Log3 {runId}-138` | ModB | 1 |
| 4 | Create | `Log4 {runId}-138` | Group Name | `—` | `Log4 {runId}-138` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-138` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-138` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-138` | Code | `LA138` | `LB138` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-138` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-138` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-138` | Code | `LC138` | `LD138` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-138` | Group Name | `Log4 {runId}-138` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-138` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-138` sampai `Log4 {runId}-138` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).

## Test Steps

1. Klik icon Changelog
2. Ketik Search `{runId}-138`, tekan Enter

### TC-FA-GRP-449: Isi opsi dropdown Filter Group Name

3. Klik icon Filter
4. Buka dropdown Group Name
5. Verifikasi opsi `Log1 {runId}-138`, `Log2 {runId}-138`, `Log3 {runId}-138`, dan `Log4 {runId}-138` (full path; `Log4 {runId}-138` sudah dihapus tetapi punya histori) tampil sebagai nilai Group Name distinct pada baris tabel
6. Verifikasi opsi `Default Group` tidak tampil (group tanpa entri log tidak muncul)
7. Verifikasi kotak search internal tampil di dalam dropdown
8. Centang opsi `Log1 {runId}-138` dan opsi `Log3 {runId}-138`
9. Verifikasi opsi `Log1 {runId}-138` dan `Log3 {runId}-138` keduanya tercentang (multi-select)
10. Hilangkan centang opsi `Log1 {runId}-138` dan `Log3 {runId}-138`

### TC-FA-GRP-450: Filter Group Name satu opsi

11. Pilih opsi `Log3 {runId}-138` pada dropdown Group Name
12. Klik [Apply]
13. Verifikasi sedikitnya satu baris tampil pada tabel
14. Verifikasi baris Action Create Group Name `Log3 {runId}-138` tampil
15. Verifikasi baris Action Create Group Name `Log1 {runId}-138` tidak tampil
16. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-451: Filter Group Name dua opsi (OR)

17. Klik icon Filter
18. Klik [Clear Field]
19. Centang opsi `Log1 {runId}-138` dan opsi `Log3 {runId}-138` pada dropdown Group Name
20. Klik [Apply]
21. Verifikasi baris Action Create Group Name `Log1 {runId}-138` dan baris Action Create Group Name `Log3 {runId}-138` tampil (opsi 1 atau opsi 2)
22. Verifikasi baris Action Create Group Name `Log2 {runId}-138` tidak tampil

### TC-FA-GRP-452: Search internal dropdown Filter Group Name

23. Klik icon Filter
24. Klik [Clear Field]
25. Buka dropdown Group Name
26. Ketik `log3` huruf kecil di kotak search dropdown
27. Verifikasi daftar opsi menyempit: opsi `Log3 {runId}-138` tampil
28. Verifikasi opsi `Log1 {runId}-138` tidak tampil
29. Ganti isi kotak search dropdown dengan `zzz-tidak-ada`
30. Verifikasi daftar opsi kosong dengan teks `No results found` (teks saja, tanpa ilustrasi)
31. Klik [Apply]
32. Klik `(←)` pada kotak Search
33. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Modal Changelog, membatasi tabel dengan Search suffix spec, membuka Filter Panel dan dropdown, menghilangkan centang pada TC pertama, serta [Clear Field] + [Apply] dan `(←)` sebagai pemulihan state antar TC (S-03, S-09, R-16).
- Pilihan opsi untuk satu opsi, dua opsi, dan potongan nama pencarian dropdown ditentukan spec dari dataset karena TC menyebut "1 opsi", "2 opsi berbeda", dan "potongan nama opsi" tanpa nilai.
- Opsi `Default Group` tidak tampil karena seed Default Group tidak dicatat di Changelog (NC-01); asersi absence didahului `Verifikasi` opsi `Log1` tampil (bagian 8b butir 2).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
