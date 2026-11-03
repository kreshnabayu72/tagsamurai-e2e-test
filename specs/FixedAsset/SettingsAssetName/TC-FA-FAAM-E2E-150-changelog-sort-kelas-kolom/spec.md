---
id: TC-FA-FAAM-E2E-150-changelog-sort-kelas-kolom
title: "Modal Changelog: Sort Kelas Date, Old-New Value, dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-480
  - TC-FA-FAAM-482
  - TC-FA-FAAM-483
coverage:
  web: automated
---

# Modal Changelog: Sort Kelas Date, Old-New Value, dan Modified By

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.changelogSeed`): Changelog contoh PRD §4.1 (Pre-setup #28), entri Create, Edit, dan Delete oleh Sarah Johnson, David Kurniawan, dan Michael Wijaya, bertanggal berbeda-beda dalam `changelogSeed.dateRange`. Seed memuat nilai kosong `—`, nilai numerik, dan nilai teks pada kolom Old Value dan New Value, serta sedikitnya dua nilai distinct pada Date dan Modified By (S-11). Halaman teramati dibatasi Filter Date rentang seed (S-14), sehingga entri baru dari spec lain tidak memengaruhi urutan.
- Tabel "Kolom campuran" (dipakai langkah 9 sampai 16):

  | Kolom |
  |---|
  | Old Value |
  | New Value |

- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: tidak ada yang diubah. Spec ini tidak menyimpan konfigurasi kolom. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Changelog
2. Batasi tabel pada entri seed: klik icon Filter, pilih rentang tanggal `Fixture.faAssetName.changelogSeed.dateRange`, klik `[Apply]`

### TC-FA-FAAM-480: Sort Changelog kelas Date

3. Klik header Date
4. Verifikasi Klik 1: `Oldest First`, baris urut Date dari terlama ke terbaru
5. Klik header Date
6. Verifikasi Klik 2: `Newest First`, baris urut Date dari terbaru ke terlama
7. Klik header Date
8. Verifikasi Klik 3: kembali netral (default Date Newest First)

### TC-FA-FAAM-482: Sort Changelog kelas Old Value, New Value (kolom campuran)

9. Untuk setiap kolom pada tabel "Kolom campuran" (langkah 10 sampai 16):
10. Klik header kolom
11. Verifikasi Klik 1: nilai kosong `—` di akhir
12. Verifikasi Klik 1: nilai numerik sebelum teks
13. Klik header kolom
14. Verifikasi Klik 2: nilai kosong `—` di awal
15. Klik header kolom
16. Verifikasi Klik 3: kembali netral (default Date Newest First)

### TC-FA-FAAM-483: Sort Changelog kelas Modified By

17. Klik header Modified By
18. Verifikasi Klik 1: A-Z menurut nama lengkap
19. Klik header Modified By
20. Verifikasi Klik 2: Z-A menurut nama lengkap
21. Klik header Modified By
22. Verifikasi Klik 3: kembali netral (default Date Newest First)

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): Filter Date rentang seed supaya halaman teramati memuat entri seed dengan nilai distinct (langkah 2, S-14).
- Langkah 10 sampai 16 diulang untuk Old Value lalu New Value (bagian 8b butir 7); jumlah langkah dengan ekspansi 29. Tiap iterasi dimulai dari sort netral (hasil langkah 16 atau langkah 8).
- TC-FA-FAAM-481 (sort kelas Action, Asset Name, Field) ada di spec 164.
- Temuan untuk QA:
  - TC-FA-FAAM-482 mensyaratkan nilai numerik dan nilai kosong `—` pada Old Value dan New Value; Pre-setup #28 tidak merinci nilai kolom tersebut, sehingga spec mengandalkan seed dari tim BE.
  - TC-FA-FAAM-483 Expected menyebut urutan "menurut nama lengkap", sedangkan kolom hanya menampilkan `[First Name] [Last Initial]`; urutan diamati pada nama yang tampil, yang untuk seed (Sarah, David, Michael) searah dengan nama lengkap.
