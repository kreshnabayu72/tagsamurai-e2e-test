---
id: TC-FA-GRP-E2E-135-modal-changelog-search-per-kolom-old-value-new-value-dan-modified-by
title: "Modal Changelog Search per Kolom Old Value, New Value, dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-436
  - TC-FA-GRP-437
  - TC-FA-GRP-438
coverage:
  web: automated
---

# Modal Changelog Search per Kolom Old Value, New Value, dan Modified By

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-135`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-135` sampai `Log4 {runId}-135` adalah group level 1; Description awal group `Log2 {runId}-135` dan `Log3 {runId}-135` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-135` | Group Name | `—` | `Log1 {runId}-135` | ModA | 1 |
| 2 | Create | `Log2 {runId}-135` | Group Name | `—` | `Log2 {runId}-135` | ModA | 1 |
| 3 | Create | `Log3 {runId}-135` | Group Name | `—` | `Log3 {runId}-135` | ModB | 1 |
| 4 | Create | `Log4 {runId}-135` | Group Name | `—` | `Log4 {runId}-135` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-135` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-135` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-135` | Code | `LA135` | `LB135` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-135` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-135` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-135` | Code | `LC135` | `LD135` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-135` | Group Name | `Log4 {runId}-135` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-135` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-135` sampai `Log4 {runId}-135` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- Parameter iterasi TC-FA-GRP-436, 437, 438, urutan baris = urutan iterasi; keyword tanpa kecocokan: `zzz-tidak-ada`. Search adalah objek uji sehingga tabel tidak dibatasi suffix; baris yang dicek dipastikan berada di halaman 1 karena entri seeding adalah entri terbaru:

| Kolom | Keyword huruf kecil | Keyword KAPITAL | Baris yang harus tampil | Baris yang tidak boleh tampil |
|---|---|---|---|---|
| Old Value | `edit me` | `EDIT ME` | baris Action Edit Group Name `Log3 {runId}-135` Field Description | baris Action Edit Group Name `Log3 {runId}-135` Field Code |
| New Value | `updated notes` | `UPDATED NOTES` | baris Action Edit Group Name `Log3 {runId}-135` Field Description | baris Action Edit Group Name `Log3 {runId}-135` Field Code |
| Modified By | potongan nama `ModB` huruf kecil | potongan yang sama huruf KAPITAL | baris Action Create Group Name `Log3 {runId}-135` | baris Action Create Group Name `Log1 {runId}-135` |

## Test Steps

1. Klik icon Changelog

### TC-FA-GRP-436, 437, 438: Search per kolom Old Value, New Value, dan Modified By (iterasi per kolom)

2. Untuk setiap baris tabel parameter iterasi (langkah 3 sampai 13): jalankan langkah berikut dengan kolom dan keyword pada baris itu
3. Verifikasi header kolom pada baris tabel tampil di tabel
4. Ketik Search keyword huruf kecil baris tabel, tekan Enter
5. Verifikasi sedikitnya satu baris tampil pada tabel
6. Verifikasi baris yang harus tampil pada baris tabel tampil
7. Verifikasi baris yang tidak boleh tampil pada baris tabel tidak tampil
8. Ganti isi kotak search dengan keyword KAPITAL baris tabel, tekan Enter
9. Verifikasi baris yang harus tampil pada baris tabel tampil (hasil identik dengan keyword huruf kecil)
10. Verifikasi baris yang tidak boleh tampil pada baris tabel tidak tampil
11. Ganti isi kotak search dengan `zzz-tidak-ada`, tekan Enter
12. Verifikasi empty state tampil dengan Illustration, title `No results found`, dan body `Try adjusting your search or filter.`
13. Klik `(←)` pada kotak Search
14. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 3 sampai 13 diulang untuk tiap baris tabel parameter iterasi: 3 iterasi x 11 langkah. Tiap `Verifikasi` tetap satu per klausa.
- Langkah penghubung (tanpa awalan `Verifikasi`): `Klik (←)` pada kotak Search di akhir tiap iterasi dan menutup Modal Changelog (S-09).
- Keyword Modified By dipilih dari nama `ModB` yang bukan bagian nama `ModA`.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
