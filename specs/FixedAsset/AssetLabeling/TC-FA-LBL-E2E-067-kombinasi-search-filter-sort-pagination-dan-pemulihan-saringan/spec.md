---
id: TC-FA-LBL-E2E-067-kombinasi-search-filter-sort-pagination-dan-pemulihan-saringan
title: "Kombinasi Search, Filter, Sort, dan Pagination Labels List serta Pemulihan Saringan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-247
  - TC-FA-LBL-249
  - TC-FA-LBL-250
  - TC-FA-LBL-251
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Pagination Labels List serta Pemulihan Saringan

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
- State global: page size tabel diubah ke 25 pada TC-FA-LBL-249 dan dipulihkan ke 10 oleh langkah 18; hook `after` suite memulihkan sebagai cadangan.

## Test Steps

### TC-FA-LBL-247: Mengubah sort tidak mereset Search dan Filter

1. Ketik Search `Sara`, tekan Enter
2. Klik icon Filter di Table Tools
3. Isi `Total Asset` Min dengan 2
4. Klik `[Apply]`
5. Klik header `Total Asset` dua kali
6. Verifikasi Search tetap `Sara`
7. Verifikasi filter Min 2 tetap aktif
8. Verifikasi hasil berurutan `High Priority` (3) lalu `Audit Ready` (2) pada Descending
9. Pulihkan: klik `(←)` pada kotak Search, klik icon Filter, klik `[Clear Field]`, klik `[Apply]`, klik area di luar panel, lalu klik header `Total Asset` sekali sampai indikator sort netral

### TC-FA-LBL-249: Kombinasi Search, Filter, Sort, dan Pagination bersamaan

10. Ketik Search `Sarah`, tekan Enter
11. Klik icon Filter di Table Tools
12. Isi `Total Asset` Min dengan 1
13. Klik `[Apply]`
14. Klik header `Total Asset` dua kali
15. Ganti page size menjadi 25
16. Verifikasi hasil berurutan `High Priority` (3) lalu `Audit Ready` (2)
17. Verifikasi seluruh kondisi berlaku bersamaan tanpa saling menimpa: Search `Sarah`, filter Min 1, sort `Total Asset` Descending, dan page size 25
18. Pulihkan: klik `(←)` pada kotak Search, klik icon Filter, klik `[Clear Field]`, klik `[Apply]`, klik area di luar panel, klik header `Total Asset` sekali sampai indikator sort netral, lalu ganti page size menjadi 10

### TC-FA-LBL-250: Clear Filter saat Search dan Sort aktif mempertahankan Search dan Sort

19. Ketik Search `Sarah`, tekan Enter
20. Klik icon Filter di Table Tools
21. Isi `Total Asset` Min dengan 1
22. Klik `[Apply]`
23. Klik header `Total Asset` sekali
24. Klik icon Filter di Table Tools
25. Klik `[Clear Field]`
26. Klik `[Apply]`
27. Verifikasi hasil kembali ke empat baris `Sarah J`: `Audit Ready`, `High Priority`, `Night Shift`, `Warehouse Priority`
28. Verifikasi keyword `Sarah` tetap aktif
29. Verifikasi sort `Total Asset` Ascending tetap aktif
30. Pulihkan: klik `(←)` pada kotak Search, klik area di luar panel, lalu klik header `Total Asset` dua kali sampai indikator sort netral

### TC-FA-LBL-251: Clear Search saat Filter dan Sort aktif mempertahankan Filter dan Sort

31. Ketik Search `Sarah`, tekan Enter
32. Klik icon Filter di Table Tools
33. Isi `Total Asset` Min dengan 1
34. Klik `[Apply]`
35. Klik header `Total Asset` sekali
36. Klik `(✕)` pada kotak Search, lalu tekan Enter pada input yang kosong
37. Verifikasi filter Min 1 tetap aktif
38. Verifikasi sort `Total Asset` Ascending tetap aktif
39. Verifikasi baris dengan Total Asset 1 atau lebih dari semua pengguna tampil berurutan Ascending: `Executive Asset` (1), `Audit Ready` (2), `Field Kit` (2), `High Priority` (3), `Maintenance Due` (4), `Finance Department` (5)

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Spec ini 39 langkah (di atas smell 35 langkah). Alasan: seluruh blok adalah kombinasi Search, Filter, dan Sort Labels List pada dataset Pre-setup #12 yang sama dan satu kelas fungsional; tiap blok dipulihkan ke keadaan awal (langkah 9, 18, 30) sebelum blok berikutnya sehingga berdiri sendiri, dan pemecahan hanya menambah login serta hook tanpa mengubah dataset.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 9, 18, dan 30 memulihkan Search, Filter, Sort, dan page size (S-09).
- Sort netral dicapai dengan klik header lanjutan sampai indikator hilang (siklus tiga tahap, TC-FA-LBL-243).
- Temuan untuk QA:
  - TC-FA-LBL-249 Expected "semua kondisi berlaku bersamaan tanpa saling menimpa" tidak merinci kondisinya; spec menurunkannya dari langkah TC (Search, Filter, Sort, page size).
  - TC-FA-LBL-251 Expected "baris dengan Total Asset 1 atau lebih dari semua pengguna tampil" tidak menyebut baris; spec menurunkan enam baris dari Pre-setup #12.
