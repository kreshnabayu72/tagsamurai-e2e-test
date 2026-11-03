---
id: TC-FA-LBL-E2E-063-filter-labels-list-modified-by-multi-pilih-chip-dan-last-updated
title: "Filter Labels List: Modified By Multi-Pilih, Chip, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-226
  - TC-FA-LBL-227
  - TC-FA-LBL-228
  - TC-FA-LBL-229
  - TC-FA-LBL-230
  - TC-FA-LBL-231
coverage:
  web: automated
---

# Filter Labels List: Modified By Multi-Pilih, Chip, dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Modified By | Last Updated |
  |---|---|---|
  | `High Priority` | `Sarah J` | 15 Sep 2026 |
  | `Finance Department` | `David K` | 14 Sep 2026 |
  | `Audit Ready` | `Sarah J` | 12 Sep 2026 |
  | `Executive Asset` | `Michael W` | 10 Sep 2026 |
  | `Maintenance Due` | `David K` | 08 Sep 2026 |
  | `Seasonal Event` | `Michael W` | 05 Sep 2026 |
  | `Night Shift` | `Sarah J` | 13 Sep 2026 |
  | `Warehouse Priority` | `Sarah J` | 09 Sep 2026 |
  | `Field Kit` | `David K` | 11 Sep 2026 |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: lebar viewport dipersempit di blok TC-FA-LBL-229 dan dipulihkan oleh langkah 25; hook `after` suite memulihkan viewport sebagai cadangan.
- Kemampuan teknis: mengubah lebar viewport browser.

## Test Steps

### TC-FA-LBL-226: Dropdown Modified By memilih dua opsi menghasilkan gabungan OR

1. Klik icon Filter di Table Tools
2. Centang `David K` dan `Michael W` di dropdown `Modified By`
3. Klik `[Apply]`
4. Verifikasi tabel memuat lima baris: `Executive Asset`, `Field Kit`, `Finance Department`, `Maintenance Due`, `Seasonal Event`
5. Verifikasi tidak ada baris dengan Modified By `Sarah J`
6. Verifikasi dua chip `David K` dan `Michael W` tampil di dalam field

### TC-FA-LBL-227: Menghapus chip dengan ikon (✕) meng-uncheck opsi di dropdown

7. Klik `[Clear Field]`, lalu klik `[Apply]`
8. Centang `David K` dan `Michael W` di dropdown `Modified By`
9. Klik `(✕)` pada chip `David K` tanpa membuka dropdown
10. Verifikasi chip `David K` hilang
11. Verifikasi chip `Michael W` tetap ada
12. Buka dropdown `Modified By`
13. Verifikasi checkbox `David K` tidak tercentang
14. Verifikasi checkbox `Michael W` tercentang

### TC-FA-LBL-228: Meng-uncheck opsi di dalam dropdown yang terbuka menghapus chip-nya

15. Klik `[Clear Field]`
16. Centang `David K` dan `Michael W` di dropdown `Modified By`
17. Buka dropdown `Modified By`, lalu hapus centang `David K`
18. Verifikasi chip `David K` hilang dari field
19. Verifikasi chip `Michael W` tetap ada

### TC-FA-LBL-229: Chip Modified By yang melebihi lebar field diringkas menjadi +N more

20. Klik `[Clear Field]`
21. Persempit lebar viewport sampai field `Modified By` sempit
22. Centang `David K`, `Michael W`, dan `Sarah J` di dropdown `Modified By`
23. Verifikasi chip ditampilkan sebanyak yang muat dan sisanya diringkas dalam satu chip `+N more`
24. Verifikasi field tidak melebar keluar panel
25. Pulihkan lebar viewport ke ukuran semula

### TC-FA-LBL-230: Filter Last Updated: rentang beberapa hari inklusif

26. Klik `[Clear Field]`
27. Pilih rentang `09 Sep 2026` sampai `11 Sep 2026` di `Last Updated`
28. Klik `[Apply]`
29. Verifikasi tabel memuat tiga baris: `Warehouse Priority` (09 Sep 2026), `Executive Asset` (10 Sep 2026), `Field Kit` (11 Sep 2026)

### TC-FA-LBL-231: Filter Last Updated: satu hari dengan Start sama dengan End

30. Klik `[Clear Field]`, lalu klik `[Apply]`
31. Pilih rentang `15 Sep 2026` sampai `15 Sep 2026` di `Last Updated`
32. Klik `[Apply]`
33. Verifikasi tabel memuat satu baris `High Priority` (15 Sep 2026)

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7, 15, 20, 26, dan 30 mengosongkan kriteria draft atau yang ter-Apply agar tiap blok mulai dari 9 label tanpa pilihan sebelumnya (S-09); langkah 25 memulihkan viewport sebelum blok berikutnya (S-03).
- Panel Filter dibiarkan terbuka antar blok; langkah pembuka `Klik icon Filter` TC-FA-LBL-227 sampai TC-FA-LBL-231 terpenuhi oleh langkah 1 spec ini.
- Temuan untuk QA:
  - TC tidak menyatakan apakah `[Apply]` menutup Filter Panel; spec mengikuti urutan TC-FA-LBL-235 dan TC-FA-LBL-236 yang menyiratkan panel tetap terbuka sesudah Apply (opsi tambahan dipilih langsung sesudah Apply; panel ditutup lalu dibuka lagi) dan menutup panel lewat klik area di luar panel.
  - TC-FA-LBL-227 dan TC-FA-LBL-228 tidak menyatakan apakah dropdown `Modified By` masih terbuka sesudah opsi dicentang; spec mengikuti penulisan TC ("tanpa membuka dropdown" dan "Buka dropdown" ditulis apa adanya).
  - TC-FA-LBL-229 tidak menyebut lebar viewport "sempit" secara numerik; lebar yang membuat chip tiga opsi tidak muat ditetapkan tim FE saat script.
