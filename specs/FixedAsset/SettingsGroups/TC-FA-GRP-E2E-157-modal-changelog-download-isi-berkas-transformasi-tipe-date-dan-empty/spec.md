---
id: TC-FA-GRP-E2E-157-modal-changelog-download-isi-berkas-transformasi-tipe-date-dan-empty
title: "Modal Changelog Download Isi Berkas: Transformasi Tipe Date dan Empty"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-515
  - TC-FA-GRP-516
coverage:
  web: automated
---

# Modal Changelog Download Isi Berkas: Transformasi Tipe Date dan Empty

## Prerequisites

- Mode: FE+BE.
- Kelas harness: f (binary buffer) untuk isi berkas XLSX.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-157`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-157` sampai `Log4 {runId}-157` adalah group level 1; Description awal group `Log2 {runId}-157` dan `Log3 {runId}-157` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-157` | Group Name | `—` | `Log1 {runId}-157` | ModA | 1 |
| 2 | Create | `Log2 {runId}-157` | Group Name | `—` | `Log2 {runId}-157` | ModA | 1 |
| 3 | Create | `Log3 {runId}-157` | Group Name | `—` | `Log3 {runId}-157` | ModB | 1 |
| 4 | Create | `Log4 {runId}-157` | Group Name | `—` | `Log4 {runId}-157` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-157` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-157` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-157` | Code | `LA157` | `LB157` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-157` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-157` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-157` | Code | `LC157` | `LD157` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-157` | Group Name | `Log4 {runId}-157` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-157` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-157` sampai `Log4 {runId}-157` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): penangkapan berkas unduhan browser dan pembacaan isi berkas CSV/XLSX (nama berkas, baris header, jumlah baris data).

## Test Steps

1. Klik icon Changelog
2. Ketik Search `{runId}-157`, tekan Enter

### TC-FA-GRP-515 dan 516: Transformasi tipe Date dan Empty pada berkas XLSX

3. Klik icon Download
4. Klik `Download as XLSX`
5. Verifikasi berkas `Changelog-Group.xlsx` terunduh
6. Buka berkas `Changelog-Group.xlsx`
7. Verifikasi kolom Date pada berkas mengikuti format tanggal General Settings
8. Verifikasi Old Value baris Action Create Group Name `Log1 {runId}-157` (kosong `—` di tabel) ditulis hyphen tunggal `-` pada berkas
9. Verifikasi New Value baris Action Delete Group Name `Log4 {runId}-157` (kosong `—` di tabel) ditulis hyphen tunggal `-` pada berkas
10. Klik `(←)` pada kotak Search
11. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Spec kelas f (isi berkas XLSX, bagian 3 prinsip 13). Nama berkas dan jumlah baris diasersi pada spec 156.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
