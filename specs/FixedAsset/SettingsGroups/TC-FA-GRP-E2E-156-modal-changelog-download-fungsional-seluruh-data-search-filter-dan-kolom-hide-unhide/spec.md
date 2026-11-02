---
id: TC-FA-GRP-E2E-156-modal-changelog-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide
title: "Modal Changelog Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, dan Kolom Hide/Unhide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-510
  - TC-FA-GRP-511
  - TC-FA-GRP-512
  - TC-FA-GRP-513
coverage:
  web: automated
---

# Modal Changelog Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, dan Kolom Hide/Unhide

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-156`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-156` sampai `Log4 {runId}-156` adalah group level 1; Description awal group `Log2 {runId}-156` dan `Log3 {runId}-156` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-156` | Group Name | `—` | `Log1 {runId}-156` | ModA | 1 |
| 2 | Create | `Log2 {runId}-156` | Group Name | `—` | `Log2 {runId}-156` | ModA | 1 |
| 3 | Create | `Log3 {runId}-156` | Group Name | `—` | `Log3 {runId}-156` | ModB | 1 |
| 4 | Create | `Log4 {runId}-156` | Group Name | `—` | `Log4 {runId}-156` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-156` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-156` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-156` | Code | `LA156` | `LB156` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-156` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-156` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-156` | Code | `LC156` | `LD156` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-156` | Group Name | `Log4 {runId}-156` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-156` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-156` sampai `Log4 {runId}-156` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): penangkapan berkas unduhan browser dan pembacaan isi berkas CSV/XLSX (nama berkas, baris header, jumlah baris data).

## Test Steps

1. Klik icon Changelog

### TC-FA-GRP-510: Download tanpa Search/filter, seluruh data

2. Klik icon Download
3. Klik `Download as CSV`
4. Verifikasi tidak ada toast sukses tampil
5. Verifikasi berkas `Changelog-Group.csv` terunduh
6. Verifikasi berkas `Changelog-Group.csv` memuat seluruh 12 baris entri seeding (baris dengan Group Name memuat `{runId}-156`), lebih banyak dari 10 baris pada halaman aktif

### TC-FA-GRP-511: Download dengan Search dan filter aktif

7. Ketik Search `{runId}-156`, tekan Enter
8. Klik icon Filter
9. Pilih `Edit` pada dropdown Action
10. Klik [Apply]
11. Klik icon Download
12. Klik `Download as XLSX`
13. Verifikasi tidak ada toast sukses tampil
14. Verifikasi berkas `Changelog-Group.xlsx` terunduh
15. Verifikasi berkas `Changelog-Group.xlsx` berisi tepat 7 baris data entri Action `Edit` milik seeding
16. Verifikasi berkas `Changelog-Group.xlsx` tidak memuat baris Action `Create` dan `Delete` milik seeding

### TC-FA-GRP-512: Kolom yang di-hide tidak ikut ter-export

17. Klik icon Filter
18. Klik [Clear Field]
19. Klik [Apply]
20. Hide kolom Action lewat Column Visibility (icon `⋯` di header kolom terakhir)
21. Verifikasi kolom Action tidak tampil pada header tabel modal
22. Klik icon Download
23. Klik `Download as CSV`
24. Verifikasi berkas `Changelog-Group.csv` terunduh
25. Verifikasi header berkas tidak memuat kolom Action dan berurutan Date, Group Name, Field, Old Value, New Value, Modified By
26. Verifikasi tidak ada toast atau peringatan tambahan tampil

### TC-FA-GRP-513: Kolom yang di-unhide kembali ikut ter-export

27. Tampilkan kembali kolom Action lewat Column Visibility
28. Verifikasi kolom Action tampil pada header tabel modal
29. Klik icon Download
30. Klik `Download as CSV`
31. Verifikasi berkas `Changelog-Group.csv` terunduh
32. Verifikasi header berkas memuat kolom Action
33. Klik `(←)` pada kotak Search
34. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Isi sel berkas diasersi pada spec kelas f terpisah (spec 157); spec ini hanya mengasersi nama berkas, header, dan jumlah baris (bagian 3 prinsip 13 kelas f).
- Bagian 8b butir 11: asersi "tidak ada toast sukses" ditulis segera setelah memilih format dan sebelum `Verifikasi` berkas terunduh; pemilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas.
- TC-FA-GRP-510 "seluruh baris" diasersi atas entri seeding (12 baris) karena total entri Changelog tidak dapat diasersi sebagai angka absolut (S-12).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
