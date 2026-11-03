---
id: TC-FA-LIC-E2E-081-active-sessions-filter-date-range-kolom-curated-temporary
title: "Active Sessions: Filter Date Range, Kolom Curated, Temporary Until, dan Badge Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-278
  - TC-FA-LIC-279
  - TC-FA-LIC-280
  - TC-FA-LIC-281
coverage:
  web: automated
---

# Active Sessions: Filter Date Range, Kolom Curated, Temporary Until, dan Badge Filter

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #26 (identitas dan nilai dirujuk lewat `Fixture.fixedAssetLicense.*`, berkas fixture belum ada, disiapkan tim FE; nilai pada langkah dan tabel di bawah adalah nilai fixture itu):
  - Hook `before` menyiapkan fixture ini: tepat lima sesi cuplikan Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso pada client Paid Pre-setup #1; Online Users 5/25; seluruh Login Time dan Last Activity bertanggal 29/09/26; Andi Pratama Pending Activation dengan Position `—`; Dewi Lestari Temporary User Yes sampai 31/12/26 (Temporary Until); lainnya Temporary User No. Format tanggal General Settings `dd/MM/yy`. Kolom Curated (`Activation Status`, `Temporary User`, `Temporary Until`, `TAG`) tetap Hidden secara default dan tidak ditampilkan spec ini.
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel.
- Tabel "Filter date range" (parameter langkah 3 sampai 9):

  | Field | Rentang | Baris yang tampil |
  |---|---|---|
  | Login Time | 29/09/26 sampai 29/09/26 | Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso |
  | Last Activity | 29/09/26 sampai 29/09/26 | Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso |

- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #26. Spec ini tidak menyimpan Setup Column.

## Test Steps

### TC-FA-LIC-278: Filter per kelas date range picker (inklusif)

1. Klik tab Concurrent User
2. Klik ikon Filter pada toolbar
3. Untuk setiap baris tabel "Filter date range" (langkah 3 sampai 9): lihat field pada baris itu
4. Verifikasi placeholder field `Select date`
5. Pilih rentang tanggal pada baris itu, lalu lihat teks tanggal terpilih
6. Verifikasi teks tanggal terpilih mengikuti Date Format General Settings (`dd/MM/yy`)
7. Klik `[Apply]`
8. Verifikasi tabel menampilkan tepat baris pada kolom "Baris yang tampil"
9. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LIC-279: Pilih satu hari saja (Start = End) bersifat inklusif

10. Pada `Login Time` pilih tanggal 29/09/26 sebagai awal dan akhir, klik `[Apply]`
11. Verifikasi baris dengan Login Time tepat 29/09/26 tampil: Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso
12. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LIC-280: Filter Panel memuat kolom Curated walau kolom tidak dicentang

13. Verifikasi Filter Panel memuat field `Activation Status` dengan placeholder `All statuses`
14. Verifikasi Filter Panel memuat field `Temporary User` dengan placeholder `All options`
15. Verifikasi Filter Panel memuat field `Temporary Until` dengan placeholder `Select date`
16. Pilih `Activation Status` = `Pending Activation`, klik `[Apply]`
17. Verifikasi tabel menampilkan: Andi Pratama
18. Klik `[Clear Field]`, lalu klik `[Apply]`
19. Pilih `Temporary User` = `Yes`, klik `[Apply]`
20. Verifikasi tabel menampilkan: Dewi Lestari
21. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LIC-281: Kolom Temporary Until dan nilai kosong disaring keluar saat filter dipakai

22. Pilih `Position` = `Staff Gudang`, klik `[Apply]`
23. Verifikasi tabel menampilkan hanya: Rudi Hartono
24. Verifikasi Andi Pratama (Position `—`) tersaring keluar dan tidak tampil
25. Buka dropdown `Position`
26. Verifikasi dropdown `Position` memuat opsi `Admin Aset`, `Staff Gudang`, `Staff Keuangan`, `Supervisor Gudang`
27. Verifikasi dropdown `Position` tidak memiliki opsi untuk nilai kosong
28. Verifikasi badge titik tampil pada ikon Filter selama filter ter-Apply
29. Klik `[Clear Field]`, lalu klik `[Apply]`
30. Verifikasi badge titik pada ikon Filter hilang
31. Pilih `Temporary Until` rentang 01/01/26 sampai 31/12/26, klik `[Apply]`
32. Verifikasi tabel menampilkan: Dewi Lestari
33. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: `[Clear Field]` lalu `[Apply]` di akhir tiap blok (S-09).
- Asersi pembanding di luar Expected TC (S-03): langkah 26 memverifikasi opsi `Admin Aset`, `Staff Gudang`, `Staff Keuangan`, `Supervisor Gudang` pada dropdown `Position` sebagai data pembanding sebelum asersi absence opsi nilai kosong pada langkah 27; opsi diturunkan dari TC-FA-LIC-274 butir a (Pre-setup #26).
- Blok ulang: langkah 3 sampai 9 dijalankan 2 kali; setelah ekspansi spec ini mendekati sekitar 40 langkah. Alasan: seluruh blok adalah Filter satu tabel dengan satu dataset Pre-setup #26 dan satu kelas harness, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC-FA-LIC-280 langkah 4 menerapkan Temporary User `Yes` tanpa menyebut pembersihan filter Activation Status sebelumnya, padahal Expected c hanya menyebut Dewi Lestari; spec membersihkan filter sebelum Temporary User `Yes`. TC-FA-LIC-279 mengulang cakupan TC-FA-LIC-278 pada field Login Time (rentang satu hari yang sama); keduanya tetap diasersi sesuai TC. Pada TC-FA-LIC-278 seluruh lima baris tampil pada filter 29/09/26 sehingga rentang tidak membuktikan penyaringan di luar rentang; TC tidak menyediakan baris pembanding di luar tanggal itu. TC-FA-LIC-281 butir c menyebut dropdown `Position` tidak memiliki opsi untuk nilai kosong tanpa menyebut opsi pembanding; spec memakai opsi dari TC-FA-LIC-274 butir a.
