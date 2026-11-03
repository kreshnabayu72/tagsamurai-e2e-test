---
id: TC-FA-LBL-E2E-062-filter-labels-list-panel-total-asset-dan-dropdown-modified-by
title: "Filter Labels List: Panel, Total Asset, dan Dropdown Modified By"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-220
  - TC-FA-LBL-221
  - TC-FA-LBL-222
  - TC-FA-LBL-223
  - TC-FA-LBL-224
  - TC-FA-LBL-225
coverage:
  web: automated
---

# Filter Labels List: Panel, Total Asset, dan Dropdown Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Total Asset | Modified By |
  |---|---|---|
  | `High Priority` | 3 | `Sarah J` |
  | `Finance Department` | 5 | `David K` |
  | `Audit Ready` | 2 | `Sarah J` |
  | `Executive Asset` | 1 | `Michael W` |
  | `Maintenance Due` | 4 | `David K` |
  | `Seasonal Event` | 0 | `Michael W` |
  | `Night Shift` | 0 | `Sarah J` |
  | `Warehouse Priority` | 0 | `Sarah J` |
  | `Field Kit` | 2 | `David K` |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-LBL-220: Screening Filter Panel Labels List

1. Klik icon Filter di Table Tools
2. Verifikasi panel muncul di bawah toolbar
3. Verifikasi icon Filter berubah gelap
4. Verifikasi field berurutan `Total Asset` (Range Min–Max, placeholder `Min` dan `Max`), `Modified By` (multi-select searchable, placeholder `All users`), `Last Updated` (date range picker, placeholder `Select date`)
5. Verifikasi maksimal 4 field per baris
6. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan)
7. Verifikasi tidak ada filter ter-Apply (icon Filter tanpa badge titik)
8. Verifikasi seluruh 9 label tampil
9. Verifikasi field `Label` dan `Color Hex` tidak ada di panel

### TC-FA-LBL-221: Filter Total Asset: hanya batas minimum

10. Isi `Min` dengan 3 dan biarkan `Max` kosong
11. Klik `[Apply]`
12. Verifikasi tabel memuat baris dengan Total Asset 3 atau lebih (inklusif): `Finance Department` (5), `High Priority` (3), `Maintenance Due` (4)
13. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LBL-222: Filter Total Asset: hanya batas maksimum

14. Isi `Max` dengan 1 dan biarkan `Min` kosong
15. Klik `[Apply]`
16. Verifikasi tabel memuat baris dengan Total Asset 1 atau kurang (inklusif): `Executive Asset` (1), `Night Shift` (0), `Seasonal Event` (0), `Warehouse Priority` (0)
17. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LBL-223: Filter Total Asset: rentang Min dan Max inklusif di kedua ujung

18. Isi `Min` dengan 2 dan `Max` dengan 3
19. Klik `[Apply]`
20. Verifikasi tabel hanya memuat baris `Audit Ready` (2), `Field Kit` (2), dan `High Priority` (3)
21. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LBL-224: Screening isi opsi dropdown Modified By: nilai DISTINCT dari data tabel

22. Buka dropdown `Modified By`
23. Verifikasi opsi berisi tepat tiga pengguna yang tercatat sebagai Modified By pada tabel: `David K`, `Michael W`, `Sarah J`
24. Verifikasi tidak ada opsi untuk pengguna yang belum pernah memodifikasi label
25. Verifikasi dropdown memiliki kotak search di dalamnya

### TC-FA-LBL-225: Search di dalam dropdown Modified By dan empty state opsi

26. Ketik `Mich` di kotak search internal dropdown `Modified By`
27. Verifikasi hanya opsi `Michael W` yang tampil
28. Ganti keyword di kotak search internal menjadi `Zulkifli`
29. Verifikasi teks `No results found` tampil
30. Verifikasi tidak ada ilustrasi pada teks `No results found`
31. Klik area di luar panel (menutup panel tanpa `[Apply]`)

## Notes

- Mode: FE+BE (backend nyata; opsi Modified By dan hasil filter berasal dari data server). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Panel Filter dibiarkan terbuka antar blok TC-FA-LBL-221 sampai TC-FA-LBL-225 karena `[Apply]` tidak menutup panel; langkah pembuka `Klik icon Filter` TC-FA-LBL-221 sampai TC-FA-LBL-225 terpenuhi oleh langkah 1.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 13, 17, dan 21 mengosongkan kriteria dan menerapkannya agar blok berikutnya mulai dari 9 label (S-09); langkah 31 menutup panel.
- Temuan untuk QA:
  - TC tidak menyatakan apakah `[Apply]` menutup Filter Panel; spec mengikuti urutan TC-FA-LBL-235 dan TC-FA-LBL-236 yang menyiratkan panel tetap terbuka sesudah Apply (opsi tambahan dipilih langsung sesudah Apply; panel ditutup lalu dibuka lagi) dan menutup panel lewat klik area di luar panel.
