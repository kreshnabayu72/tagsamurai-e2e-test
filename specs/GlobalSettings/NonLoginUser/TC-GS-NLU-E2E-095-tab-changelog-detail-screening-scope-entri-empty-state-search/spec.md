---
id: TC-GS-NLU-E2E-095-tab-changelog-detail-screening-scope-entri-empty-state-search
title: "Tab Changelog Detail: Screening, Scope Entri, Empty State, dan Search"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-333
  - TC-GS-NLU-334
  - TC-GS-NLU-335
  - TC-GS-NLU-336
  - TC-GS-NLU-337
coverage:
  web: automated
---

# Tab Changelog Detail: Screening, Scope Entri, Empty State, dan Search

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Data milik spec (hook `before`, sesi API aktor Total Control, kemampuan disediakan tim FE/BE; dihapus di hook `after`):
  - `Budi Kurniawan {runId}-095` (Division Operations): riwayat 12 entri oleh `Siti N` dalam urutan Create (Field `Name`), 10 kali Edit Division bergantian `Logistics` dan `Operations` (Field `Division`), lalu Deactivate (Field `Status`, Old Value `Active`, New Value `Inactive`) sebagai entri terakhir. Riwayat lebih dari 10 entri agar footer pagination tampil.
  - `Pembanding {runId}-095`: Non-Login User lain dengan riwayat sendiri (entri Create), dipakai sebagai pembanding scope entri TC-GS-NLU-334.
  - `Tanpa Riwayat {runId}-095`: Non-Login User yang di-seed tanpa menulis entri Changelog (kemampuan seeding tanpa audit trail disediakan tim FE/BE; Pre-setup No. 11 tidak menyebut record tanpa riwayat, lihat Temuan untuk QA).
- Tabel `Data uji Search TC-GS-NLU-336` (dipakai langkah 17 sampai 18):

  | Kolom | Kata kunci |
  |---|---|
  | `Action` | `deactiv` |
  | `Field` | `status` |
  | `Old Value` | `activ` |
  | `New Value` | `inactiv` |
  | `Modified By` | `siti` |
- Format tanggal General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Tabel Data Uji Pre-setup No. 16); spec tidak mengubahnya. Jam server dan jam browser sinkron.
- Kemampuan teknis: membaca baris dan kolom tabel Tab Changelog.
- Suite berjalan serial (`parallel: false`). Hook `after` menghapus data `{runId}` milik spec ini dan memulihkan state yang diubahnya.

## Test Steps

### TC-GS-NLU-333: Screening Tab Changelog Detail Non-Login User

1. Ketik Search `Budi Kurniawan {runId}-095`, tekan Enter
2. Buka Detail Non-Login User dengan Name tepat `Budi Kurniawan {runId}-095`
3. Klik tab `Changelog`
4. Verifikasi Breadcrumb `User > Detail`
5. Verifikasi Tab `Responsibilities | Changelog (aktif)`
6. Verifikasi toolbar tab: `Search | Filter | Download`
7. Verifikasi placeholder Search `"Search action, field, modified by, or value..."`
8. Verifikasi kolom: `Date (sortable) | Action (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable)`
9. Verifikasi tidak ada kolom Name pada tabel
10. Verifikasi default sort Date terbaru di atas: baris pertama adalah entri Deactivate (aksi terakhir seeding)
11. Verifikasi footer tab: pagination default 10

### TC-GS-NLU-334: Tab Changelog hanya memuat entri milik Non-Login User yang dibuka

12. Verifikasi sedikitnya satu baris entri tampil di Tab Changelog (pembanding generik)
13. Ketik Search `Pembanding {runId}-095`, tekan Enter
14. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (tidak ada entri Non-Login User lain, termasuk `Pembanding {runId}-095`)
15. Klik `(←)` pada kotak Search

### TC-GS-NLU-336: Search substring dan case-insensitive pada kolom Action, Field, Old Value, New Value, Modified By di Tab Changelog Detail

16. Klik icon Search
17. Untuk setiap baris tabel `Data uji Search TC-GS-NLU-336` di `## Prerequisites` (langkah 17 sampai 18): ketik Search kata kunci pada baris tabel, tekan Enter
18. Verifikasi sedikitnya satu baris tampil dan baris yang memuat kata kunci pada kolom pada baris tabel ditemukan (substring, tidak membedakan huruf besar kecil)

### TC-GS-NLU-337: Empty state saat Search tidak ditemukan di Tab Changelog Detail

19. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
20. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
21. Klik `(←)` pada kotak Search

### TC-GS-NLU-335: Empty state Tab Changelog saat belum ada riwayat

22. Kembali ke daftar Non-Login User (Global Settings > User > User List > sub-tab Non-Login User)
23. Ketik Search `Tanpa Riwayat {runId}-095`, tekan Enter
24. Buka Detail Non-Login User dengan Name tepat `Tanpa Riwayat {runId}-095`
25. Klik tab `Changelog`
26. Verifikasi empty state Tab Changelog: ilustrasi dengan judul `"No changelog yet"` dan deskripsi `"Activities and changes will appear here."`

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber diubah: TC-GS-NLU-335 (empty state) ditaruh paling akhir karena membuka Detail record lain (langkah 22 sampai 25), sedangkan TC-GS-NLU-333, 334, 336, 337 memakai Detail record yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3 (Search `Budi Kurniawan {runId}-095`, membuka Detail, dan tab `Changelog`; R-16); langkah 13 (Search pembanding, aksi TC-GS-NLU-334 untuk membuktikan tidak ada entri milik record lain); langkah 15, 21 (mengosongkan Search); langkah 16 (membuka input Search); langkah 22, 23, 24, 25 (kembali ke daftar dan membuka Detail record tanpa riwayat).
- Langkah yang diulang: langkah 17 sampai 18 diulang untuk lima baris tabel `Data uji Search TC-GS-NLU-336` di Prerequisites.
- Asersi tambahan (konkretisasi Expected): langkah 10 ("default sort Date terbaru di atas" ditulis sebagai baris pertama adalah entri Deactivate seeding, S-14); langkah 14 (TC-GS-NLU-334 a "tidak ada entri Non-Login User lain" dibuktikan lewat Search nama record pembanding yang menghasilkan `No results found`, dengan pembanding positif pada langkah 12; scope exclusion dengan data milik spec bukan kelas g, bagian 3 prinsip 13g).
- Pembagian TC lintas spec: Filter, Sort, Pagination, Download Tab Changelog ada di spec 096 dan 136; Setup Column ada di spec 097 dan 098.
- Temuan untuk QA:
  - TC-GS-NLU-335: precondition menunjuk Pre-setup No. 11 tanpa menyebut record mana yang tanpa riwayat, padahal audit trail permanen; spec memakai record milik spec yang di-seed tanpa menulis log (mekanisme disediakan tim FE/BE, R-19).
  - TC-GS-NLU-333: footer "pagination default 10" tidak tampil bila baris tidak lebih dari 10; spec menyeding riwayat 12 entri. Cara membuka Detail Non-Login User dari daftar tidak dijelaskan TC (hanya "User > Detail"); spec menulis "Buka Detail Non-Login User" tanpa mekanisme klik tertentu.
  - TC-GS-NLU-336: TC tidak menyebut data yang memuat kata kunci `activ` (Old Value) dan `inactiv` (New Value); spec menyeding Deactivate dengan Old Value `Active` dan New Value `Inactive`.
