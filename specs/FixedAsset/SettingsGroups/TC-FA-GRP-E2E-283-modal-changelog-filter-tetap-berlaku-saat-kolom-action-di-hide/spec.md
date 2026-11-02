---
id: TC-FA-GRP-E2E-283-modal-changelog-filter-tetap-berlaku-saat-kolom-action-di-hide
title: "Modal Changelog Filter: Tetap Tersedia dan Tetap Berlaku Saat Kolom Action Di-Hide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1119
coverage:
  web: automated
---

# Modal Changelog Filter: Tetap Tersedia dan Tetap Berlaku Saat Kolom Action Di-Hide

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-283`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-283` sampai `Log4 {runId}-283` adalah group level 1; Description awal group `Log2 {runId}-283` dan `Log3 {runId}-283` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-283` | Group Name | `—` | `Log1 {runId}-283` | ModA | 1 |
| 2 | Create | `Log2 {runId}-283` | Group Name | `—` | `Log2 {runId}-283` | ModA | 1 |
| 3 | Create | `Log3 {runId}-283` | Group Name | `—` | `Log3 {runId}-283` | ModB | 1 |
| 4 | Create | `Log4 {runId}-283` | Group Name | `—` | `Log4 {runId}-283` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-283` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-283` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-283` | Code | `LA283` | `LB283` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-283` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-283` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-283` | Code | `LC283` | `LD283` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-283` | Group Name | `Log4 {runId}-283` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-283` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-283` sampai `Log4 {runId}-283` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).

## Test Steps

1. Klik icon Changelog

### TC-FA-GRP-1119: Filter tetap tersedia dan berlaku saat kolom Action di-hide

2. Ketik Search `{runId}-283`, tekan Enter
3. Klik icon Filter
4. Pilih `Delete` pada dropdown Action
5. Klik [Apply]
6. Verifikasi sedikitnya satu baris tampil dan seluruh baris yang tampil ber-Action `Delete`
7. Verifikasi baris Action Delete Group Name `Log4 {runId}-283` tampil
8. Catat nama baris yang tampil pada tabel modal
9. Hide kolom Action lewat Column Visibility (icon `⋯` di header kolom terakhir)
10. Verifikasi kolom Action tidak tampil pada header tabel modal
11. Verifikasi filter yang sudah di-Apply tetap berlaku: nama baris yang tampil sama dengan yang dicatat
12. Klik icon Filter
13. Verifikasi Filter Panel tetap memuat field Action walau kolomnya tersembunyi
14. Klik icon Filter untuk menutup panel
15. Tampilkan kembali kolom Action lewat Column Visibility
16. Verifikasi kolom Action tampil pada header tabel modal
17. Verifikasi nama baris yang tampil tidak berubah dari yang dicatat
18. Klik icon Filter
19. Verifikasi nilai filter Action tetap `Delete`
20. Klik [Clear Field]
21. Klik [Apply]
22. Klik `(←)` pada kotak Search
23. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka dan menutup Modal Changelog, membatasi tabel dengan Search suffix spec, mencatat nama baris, men-hide dan meng-unhide kolom Action lewat Column Visibility, serta [Clear Field] + [Apply] (S-03, S-09, R-16).
- TC-FA-GRP-507, 508, dan 509 berada di spec 148.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
