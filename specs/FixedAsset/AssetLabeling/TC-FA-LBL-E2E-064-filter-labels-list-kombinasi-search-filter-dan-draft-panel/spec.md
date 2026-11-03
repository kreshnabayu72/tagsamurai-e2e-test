---
id: TC-FA-LBL-E2E-064-filter-labels-list-kombinasi-search-filter-dan-draft-panel
title: "Filter Labels List: Kombinasi Field, Search dan Filter, serta Draft Panel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-232
  - TC-FA-LBL-233
  - TC-FA-LBL-234
  - TC-FA-LBL-235
coverage:
  web: automated
---

# Filter Labels List: Kombinasi Field, Search dan Filter, serta Draft Panel

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

### TC-FA-LBL-232: Kombinasi dua field filter berlogika AND

1. Klik icon Filter di Table Tools
2. Isi `Total Asset` Min dengan 2
3. Pilih `Modified By` = `Sarah J`
4. Klik `[Apply]`
5. Verifikasi tabel memuat dua baris: `Audit Ready` (2) dan `High Priority` (3)
6. Verifikasi baris `Finance Department` (5, David K) tidak muncul
7. Bersihkan saringan: klik `[Clear Field]`, klik `[Apply]`, lalu klik area di luar panel

### TC-FA-LBL-233: Search lalu Filter menghasilkan irisan

8. Ketik Search `ent`, tekan Enter
9. Verifikasi tabel memuat `Finance Department` dan `Seasonal Event`
10. Klik icon Filter di Table Tools
11. Pilih `Modified By` = `David K`
12. Klik `[Apply]`
13. Verifikasi tabel hanya memuat `Finance Department`
14. Verifikasi keyword `ent` tidak tereset (kotak search tetap berisi `ent`)
15. Pulihkan: klik `[Clear Field]`, klik `[Apply]`, klik area di luar panel, lalu klik `(←)` pada kotak Search

### TC-FA-LBL-234: Filter lalu Search menghasilkan irisan yang sama

16. Klik icon Filter di Table Tools
17. Pilih `Modified By` = `David K`
18. Klik `[Apply]`
19. Ketik Search `ent`, tekan Enter
20. Verifikasi tabel hanya memuat `Finance Department`
21. Verifikasi hasil identik dengan hasil Search lalu Filter pada langkah 13
22. Verifikasi filter `Modified By` = `David K` tetap aktif (icon Filter berbadge titik)
23. Pulihkan: klik `[Clear Field]`, klik `[Apply]`, klik area di luar panel, lalu klik `(←)` pada kotak Search

### TC-FA-LBL-235: Menutup panel tanpa Apply membuang perubahan draft

24. Klik icon Filter di Table Tools
25. Pilih `Modified By` = `Sarah J`
26. Klik `[Apply]`
27. Pilih juga `David K` di dropdown `Modified By` tanpa `[Apply]`
28. Klik area di luar panel
29. Verifikasi tabel tetap hanya memuat baris `Sarah J`: `Audit Ready`, `High Priority`, `Night Shift`, `Warehouse Priority`
30. Klik icon Filter di Table Tools
31. Verifikasi panel hanya berisi `Sarah J` (nilai ter-Apply terakhir)
32. Verifikasi `David K` tidak tercentang

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7, 15, dan 23 membersihkan Filter, Search, dan panel agar blok berikutnya mulai dari 9 label (S-09).
- Indikator "filter tetap aktif" pada TC-FA-LBL-234 diamati lewat badge titik pada icon Filter, indikator yang ditetapkan TC-FA-LBL-236 (spec 165).
- Pembagian TC lintas spec: TC-FA-LBL-236 ada di spec 165.
- Temuan untuk QA:
  - TC tidak menyatakan apakah `[Apply]` menutup Filter Panel; spec mengikuti urutan TC-FA-LBL-235 dan TC-FA-LBL-236 yang menyiratkan panel tetap terbuka sesudah Apply (opsi tambahan dipilih langsung sesudah Apply; panel ditutup lalu dibuka lagi) dan menutup panel lewat klik area di luar panel.
