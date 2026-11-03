---
id: TC-AC-CS-E2E-089-list-filter-date-range-grace-end-or-dan-and
title: "List Filter: Date Range, Grace End, OR dan AND"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-336
  - TC-AC-CS-337
  - TC-AC-CS-338
  - TC-AC-CS-339
coverage:
  web: automated
---

# List Filter: Date Range, Grace End, OR dan AND

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Cache Setup Column browser dikosongkan di hook `before` dan dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bagian 4).
- Tabel parameter filter tanggal: Start Date `01/01/26` sampai `01/01/26` (batas inklusif); End Date `31/12/26` sampai `31/12/26`; Grace End `17/09/26` sampai `17/09/26`.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-336: Filter date range Start Date dan End Date inklusif

1. Klik ikon Filter, pilih Start Date dari `01/01/26` sampai `01/01/26`, klik `[Apply]`
2. Verifikasi baris dengan Start Date `01/01/26` tampil (batas inklusif)
3. Verifikasi baris tanpa tanggal "—" tidak ikut ketika filter tanggal dipakai
4. Klik `[Clear Field]`, pilih End Date dari `31/12/26` sampai `31/12/26`, klik `[Apply]`
5. Verifikasi baris dengan End Date `31/12/26` tampil

### TC-AC-CS-337: Filter Grace End tetap tersedia walau kolom disembunyikan

6. Klik `[Clear Field]`, pilih Grace End `17/09/26` sampai `17/09/26`, klik `[Apply]` dengan kolom Grace End masih tersembunyi
7. Verifikasi baris `SUBS-20250819-00002` tampil
8. Verifikasi field filter Grace End ada walau kolom Grace End tidak tampil
9. Verifikasi filter ter-Apply tetap bertahan walau kolom Grace End tersembunyi

### TC-AC-CS-338: Beberapa opsi dalam satu field filter bersifat OR

10. Klik `[Clear Field]`, pilih Status `Active` dan `Expired`, klik `[Apply]`
11. Verifikasi baris berstatus Active dan baris berstatus Expired sama-sama tampil
12. Verifikasi baris berstatus lain tidak tampil

### TC-AC-CS-339: Beberapa field filter berbeda bersifat AND

13. Klik `[Clear Field]`, pilih Product `FAMS` dan Status `Active`, klik `[Apply]`
14. Verifikasi hanya baris Product `FAMS` yang sekaligus berstatus Active tampil
15. Verifikasi baris Product FAMS berstatus lain dan baris Active Product lain tidak tampil
16. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah penghubung: `[Clear Field]` dan `[Apply]` antar variasi filter pada panel yang sama.
- Temuan untuk QA: (1) TC-AC-CS-337 butir c ("Filter yang sudah di-Apply tetap bertahan saat kolom disembunyikan setelahnya") menyebut kolom disembunyikan setelah Apply tetapi kolom Grace End sudah Hidden secara default (Curated); spec tidak mengubah visibilitas kolom dan mengasersi filter tetap bertahan dengan kolom tersembunyi. (2) TC-AC-CS-336 memakai rentang satu hari pada kolom Start Date dan End Date tanpa menyebut baris yang dijamin ada; asersi memakai dataset #82.
