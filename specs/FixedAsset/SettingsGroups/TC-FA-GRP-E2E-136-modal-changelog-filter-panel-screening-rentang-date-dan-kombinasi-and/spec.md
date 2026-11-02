---
id: TC-FA-GRP-E2E-136-modal-changelog-filter-panel-screening-rentang-date-dan-kombinasi-and
title: "Modal Changelog Filter: Screening Panel, Rentang Date, Kombinasi Date + Action (AND), dan [Clear Field]"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-441
  - TC-FA-GRP-442
  - TC-FA-GRP-467
  - TC-FA-GRP-468
coverage:
  web: automated
---

# Modal Changelog Filter: Screening Panel, Rentang Date, Kombinasi Date + Action (AND), dan [Clear Field]

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-136`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-136` sampai `Log4 {runId}-136` adalah group level 1; Description awal group `Log2 {runId}-136` dan `Log3 {runId}-136` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-136` | Group Name | `—` | `Log1 {runId}-136` | ModA | 1 |
| 2 | Create | `Log2 {runId}-136` | Group Name | `—` | `Log2 {runId}-136` | ModA | 1 |
| 3 | Create | `Log3 {runId}-136` | Group Name | `—` | `Log3 {runId}-136` | ModB | 1 |
| 4 | Create | `Log4 {runId}-136` | Group Name | `—` | `Log4 {runId}-136` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-136` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-136` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-136` | Code | `LA136` | `LB136` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-136` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-136` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-136` | Code | `LC136` | `LD136` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-136` | Group Name | `Log4 {runId}-136` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-136` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-136` sampai `Log4 {runId}-136` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- Format tanggal input Date mengikuti Date Format General Settings akun aktor (dibaca sebelum uji; spec tidak mengubahnya).

## Test Steps

1. Klik icon Changelog
2. Ketik Search `{runId}-136`, tekan Enter

### TC-FA-GRP-441: Screening Filter Panel Modal Changelog

3. Klik icon Filter
4. Verifikasi Filter Panel terbuka berisi field berurutan: Date (date range picker, placeholder `Select date`), Action (dropdown multi-select searchable, placeholder `All actions`), Group Name (dropdown multi-select searchable, placeholder `All groups`), Field (dropdown multi-select searchable, placeholder `All fields`), dan Modified By (dropdown multi-select searchable, placeholder `All users`)
5. Verifikasi tombol footer [Clear Field] dan [Apply] tampil
6. Verifikasi tidak ada field filter lain di luar daftar field tersebut

### TC-FA-GRP-442: Filter Date rentang tanggal

7. Buka date range picker Date, pilih tanggal awal = hari ini - 1 dan tanggal akhir = hari ini
8. Klik [Apply]
9. Verifikasi sedikitnya satu baris tampil pada tabel
10. Verifikasi baris Action Create Group Name `Log1 {runId}-136` tampil (Date hari ini, batas akhir inklusif)
11. Klik icon Filter
12. Ubah rentang Date: tanggal awal = tanggal akhir = hari ini
13. Verifikasi teks tanggal pada input Date mengikuti Date Format General Settings
14. Klik [Apply]
15. Verifikasi baris Action Create Group Name `Log1 {runId}-136` tampil (hari itu saja)

### TC-FA-GRP-467: Kombinasi Date + Action (AND)

16. Klik icon Filter
17. Isi Date tanggal hari ini sampai tanggal hari ini dan pilih `Delete` pada dropdown Action
18. Klik [Apply]
19. Verifikasi baris Action Delete Group Name `Log4 {runId}-136` tampil (memenuhi kedua kriteria)
20. Verifikasi baris Action Create Group Name `Log1 {runId}-136` tidak tampil (Action `Create`)

### TC-FA-GRP-468: [Clear Field] mengosongkan seluruh field

21. Klik icon Filter
22. Klik [Clear Field]
23. Verifikasi field Date kosong dengan placeholder `Select date`
24. Verifikasi field Action kosong dengan placeholder `All actions`
25. Verifikasi field Group Name kosong dengan placeholder `All groups`
26. Verifikasi field Field kosong dengan placeholder `All fields`
27. Verifikasi field Modified By kosong dengan placeholder `All users`
28. Klik [Apply]
29. Verifikasi tabel kembali menampilkan seluruh data: baris Action Create Group Name `Log1 {runId}-136` tampil dan baris Action Delete Group Name `Log4 {runId}-136` tampil
30. Klik `(←)` pada kotak Search
31. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Modal Changelog, membatasi tabel dengan Search suffix spec, dan membuka/menutup Filter Panel (S-03, R-16). Rentang tanggal TC-FA-GRP-442 memakai tanggal relatif hari uji; TC tidak menyebut tanggal. Nilai kombinasi Date + Action TC-FA-GRP-467 (Date hari ini, Action `Delete`) ditentukan spec.
- Tabel dibatasi Search suffix spec sepanjang spec; [Clear Field] pada TC-FA-GRP-468 hanya mengosongkan field Filter Panel, bukan Search.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
