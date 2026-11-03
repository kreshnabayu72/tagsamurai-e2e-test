---
id: TC-FA-GRP-E2E-145-modal-changelog-sort-kolom-date-action-group-name-dan-field
title: "Modal Changelog Sort Kolom Date, Action, Group Name, dan Field (Asc, Desc, Netral)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-471
  - TC-FA-GRP-472
  - TC-FA-GRP-473
  - TC-FA-GRP-474
coverage:
  web: automated
---

# Modal Changelog Sort Kolom Date, Action, Group Name, dan Field (Asc, Desc, Netral)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-145`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-145` sampai `Log4 {runId}-145` adalah group level 1; Description awal group `Log2 {runId}-145` dan `Log3 {runId}-145` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-145` | Group Name | `—` | `Log1 {runId}-145` | ModA | 1 |
| 2 | Create | `Log2 {runId}-145` | Group Name | `—` | `Log2 {runId}-145` | ModA | 1 |
| 3 | Create | `Log3 {runId}-145` | Group Name | `—` | `Log3 {runId}-145` | ModB | 1 |
| 4 | Create | `Log4 {runId}-145` | Group Name | `—` | `Log4 {runId}-145` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-145` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-145` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-145` | Code | `LA145` | `LB145` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-145` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-145` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-145` | Code | `LC145` | `LD145` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-145` | Group Name | `Log4 {runId}-145` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-145` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-145` sampai `Log4 {runId}-145` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- Parameter iterasi TC-FA-GRP-471, 472, 473, 474, urutan baris = urutan iterasi. Tabel dibatasi Search suffix spec (12 entri; 10 baris di halaman 1). Urutan default (netral) = Date Newest First: baris 1 adalah entri seeding batch 3. `ModMin`/`ModMax` = nama lengkap Modified By yang paling awal/akhir secara alfabet di antara `ModA`, `ModB`, `ModC` (dibaca sebelum uji).

| Kolom | Setelah klik #1 (Ascending) | Setelah klik #2 (Descending) |
|---|---|---|
| Date | baris 1 adalah entri seeding batch 1 (Oldest First) | baris 1 adalah entri seeding batch 3 (Newest First) |
| Action | baris 1 sampai 4 ber-Action `Create`, baris 5 `Delete`, baris 6 `Edit` | baris 1 sampai 7 ber-Action `Edit`, baris 8 `Delete`, baris 9 `Create` |
| Group Name | baris 1 sampai 2 = `Log1 {runId}-145`, baris 3 sampai 6 = `Log2 {runId}-145`, baris 7 sampai 10 = `Log3 {runId}-145` | baris 1 sampai 2 = `Log4 {runId}-145`, baris 3 sampai 6 = `Log3 {runId}-145`, baris 7 sampai 10 = `Log2 {runId}-145` |
| Field | baris 1 sampai 2 ber-Field `Code`, baris 3 sampai 4 `Description`, baris 5 sampai 7 `Function`, baris 8 sampai 10 `Group Name` | baris 1 sampai 5 ber-Field `Group Name`, baris 6 sampai 8 `Function`, baris 9 sampai 10 `Description` |

## Test Steps

1. Klik icon Changelog
2. Ketik Search `{runId}-145`, tekan Enter

### TC-FA-GRP-471 sampai 474: Sort kolom Date, Action, Group Name, dan Field (iterasi per kolom)

3. Untuk setiap baris tabel parameter iterasi (langkah 4 sampai 10): jalankan langkah berikut dengan kolom pada baris itu
4. Verifikasi header kolom pada baris tabel tampil di tabel
5. Klik header kolom pada baris tabel satu kali
6. Verifikasi urutan tabel sesuai sel "Setelah klik #1 (Ascending)" baris tabel
7. Klik header kolom yang sama satu kali lagi
8. Verifikasi urutan tabel sesuai sel "Setelah klik #2 (Descending)" baris tabel
9. Klik header kolom yang sama satu kali lagi
10. Verifikasi urutan tabel kembali ke default (Date Newest First): baris pertama adalah entri seeding batch 3
11. Klik `(←)` pada kotak Search
12. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 4 sampai 10 diulang untuk tiap baris tabel parameter iterasi: 4 iterasi x 7 langkah.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka/menutup Modal Changelog dan membatasi tabel dengan Search suffix spec (S-03, R-16).
- Kolom Field tidak pernah kosong (TC-FA-GRP-474 Expected a); diamati dari seluruh baris halaman 1.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
