---
id: TC-FA-GRP-E2E-150-modal-changelog-setup-column-uncheck-kolom-old-value-new-value-dan-modified-by
title: "Modal Changelog Setup Column: Uncheck Kolom Old Value, New Value, dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-489
  - TC-FA-GRP-490
  - TC-FA-GRP-491
coverage:
  web: automated
---

# Modal Changelog Setup Column: Uncheck Kolom Old Value, New Value, dan Modified By

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-150`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-150` sampai `Log4 {runId}-150` adalah group level 1; Description awal group `Log2 {runId}-150` dan `Log3 {runId}-150` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-150` | Group Name | `—` | `Log1 {runId}-150` | ModA | 1 |
| 2 | Create | `Log2 {runId}-150` | Group Name | `—` | `Log2 {runId}-150` | ModA | 1 |
| 3 | Create | `Log3 {runId}-150` | Group Name | `—` | `Log3 {runId}-150` | ModB | 1 |
| 4 | Create | `Log4 {runId}-150` | Group Name | `—` | `Log4 {runId}-150` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-150` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-150` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-150` | Code | `LA150` | `LB150` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-150` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-150` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-150` | Code | `LC150` | `LD150` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-150` | Group Name | `Log4 {runId}-150` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-150` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-150` sampai `Log4 {runId}-150` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): viewport browser disesuaikan sehingga tabel Modal Changelog dapat di-scroll horizontal, dan penghapusan preferensi kolom Setup Column di browser (hook `after`, bagian 4).
- Parameter iterasi TC-FA-GRP-489, 490, 491, urutan baris = urutan iterasi:

| Kolom |
|---|
| Old Value |
| New Value |
| Modified By |

## Test Steps

1. Klik icon Changelog

### TC-FA-GRP-489 sampai 491: Uncheck kolom Old Value, New Value, dan Modified By (iterasi per kolom)

2. Untuk setiap baris tabel parameter iterasi (langkah 3 sampai 14): jalankan langkah berikut dengan kolom pada baris itu
3. Buka Popup Setup Column pada Modal Changelog: klik icon `⋯` di header kolom terakhir tabel modal, lalu klik `Setup Column...`
4. Hilangkan centang kolom pada baris tabel pada daftar Popup Setup Column
5. Verifikasi Live Preview langsung menyembunyikan kolom pada baris tabel
6. Klik [Save]
7. Verifikasi kolom pada baris tabel hilang dari tabel modal
8. Muat ulang halaman (F5)
9. Klik icon Changelog
10. Verifikasi kolom selain kolom pada baris tabel tampil di tabel modal
11. Verifikasi kolom pada baris tabel masih hilang dari tabel modal (konfigurasi bertahan setelah F5)
12. Buka Popup Setup Column pada Modal Changelog: klik icon `⋯` di header kolom terakhir tabel modal, lalu klik `Setup Column...`
13. Klik [Reset to Default]
14. Klik [Save]
15. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 3 sampai 14 diulang untuk tiap baris tabel parameter iterasi (Old Value/New Value/Modified By): 12 langkah per iterasi.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Modal Changelog dan Popup Setup Column (icon `⋯` > `Setup Column...`), [Reset to Default] + [Save] untuk memulihkan susunan default antar iterasi, dan membuka kembali Modal Changelog setelah F5 karena F5 menutup modal (S-03, S-09). Verifikasi kolom lain pada tabel tampil (langkah 10) ditambahkan sebagai anchor positif sebelum asersi kolom hilang sesudah F5 (8b butir 2, R-21; S-03). Pemulihan akhir preferensi kolom: hook `after` menghapus preferensi kolom di browser (bagian 4).
- Spec 15 langkah (ekspansi iterasi ± 39 langkah), di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah per kolom/field memakai tabel di Prerequisites (bagian 8b butir 7).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
  - TC Setup Column tidak menyebut lebar viewport; asersi pin (sticky saat scroll horizontal) mensyaratkan tabel modal dapat di-scroll horizontal, sehingga viewport disesuaikan (Prerequisites).
