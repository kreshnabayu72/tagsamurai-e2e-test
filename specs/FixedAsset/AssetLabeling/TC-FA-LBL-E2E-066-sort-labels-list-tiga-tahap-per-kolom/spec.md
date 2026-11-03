---
id: TC-FA-LBL-E2E-066-sort-labels-list-tiga-tahap-per-kolom
title: "Sort Labels List: Tiga Tahap per Kolom dan Perpindahan Kolom Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-241
  - TC-FA-LBL-242
  - TC-FA-LBL-243
  - TC-FA-LBL-244
  - TC-FA-LBL-245
  - TC-FA-LBL-246
coverage:
  web: automated
---

# Sort Labels List: Tiga Tahap per Kolom dan Perpindahan Kolom Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Color Hex | Total Asset | Modified By | Last Updated |
  |---|---|---|---|---|
  | `High Priority` | `#EF4444` | 3 | `Sarah J` | 15 Sep 2026 |
  | `Finance Department` | `#3B82F6` | 5 | `David K` | 14 Sep 2026 |
  | `Audit Ready` | `#10B981` | 2 | `Sarah J` | 12 Sep 2026 |
  | `Executive Asset` | `#8B5CF6` | 1 | `Michael W` | 10 Sep 2026 |
  | `Maintenance Due` | `#F59E0B` | 4 | `David K` | 08 Sep 2026 |
  | `Seasonal Event` | `#EC4899` | 0 | `Michael W` | 05 Sep 2026 |
  | `Night Shift` | `#1E3A8A` | 0 | `Sarah J` | 13 Sep 2026 |
  | `Warehouse Priority` | `#0EA5E9` | 0 | `Sarah J` | 09 Sep 2026 |
  | `Field Kit` | `#84CC16` | 2 | `David K` | 11 Sep 2026 |

- Data uji sort (tiap kolom punya sedikitnya dua nilai distinct pada Pre-setup #12, S-11):

  | TC | Kolom | Klik 1 (Ascending) | Klik 2 (Descending) |
  |---|---|---|---|
  | TC-FA-LBL-241 | `Label` | `Audit Ready`, `Executive Asset`, `Field Kit`, `Finance Department`, `High Priority`, `Maintenance Due`, `Night Shift`, `Seasonal Event`, `Warehouse Priority` | urutan terbalik penuh dari `Warehouse Priority` sampai `Audit Ready` |
  | TC-FA-LBL-242 | `Color Hex` | `#0EA5E9`, `#10B981`, `#1E3A8A`, `#3B82F6`, `#84CC16`, `#8B5CF6`, `#EC4899`, `#EF4444`, `#F59E0B` | urutan terbalik penuh dari `#F59E0B` sampai `#0EA5E9` |
  | TC-FA-LBL-243 | `Total Asset` | nilai `0` (`Night Shift`, `Seasonal Event`, `Warehouse Priority`), `1` (`Executive Asset`), `2` (`Audit Ready`, `Field Kit`), `3` (`High Priority`), `4` (`Maintenance Due`), `5` (`Finance Department`); baris dengan nilai sama urut Label A-Z | nilai `5`, `4`, `3`, `2` (`Audit Ready`, `Field Kit`), `1`, lalu `0` (`Night Shift`, `Seasonal Event`, `Warehouse Priority`); baris dengan nilai sama tetap urut Label A-Z |
  | TC-FA-LBL-244 | `Modified By` | kelompok `David K` (`Field Kit`, `Finance Department`, `Maintenance Due`), `Michael W` (`Executive Asset`, `Seasonal Event`), `Sarah J` (`Audit Ready`, `High Priority`, `Night Shift`, `Warehouse Priority`); dalam kelompok urut Label A-Z | kelompok `Sarah J`, `Michael W`, lalu `David K`; dalam kelompok tetap urut Label A-Z |
  | TC-FA-LBL-245 | `Last Updated` | Oldest First: `Seasonal Event` (05 Sep), `Maintenance Due` (08 Sep), `Warehouse Priority` (09 Sep), `Executive Asset` (10 Sep), `Field Kit` (11 Sep), `Audit Ready` (12 Sep), `Night Shift` (13 Sep), `Finance Department` (14 Sep), `High Priority` (15 Sep) | Newest First: urutan terbalik dari `High Priority` sampai `Seasonal Event` |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-LBL-241, TC-FA-LBL-242, TC-FA-LBL-243, TC-FA-LBL-244, TC-FA-LBL-245: Sort 3 tahap per kolom

1. Untuk setiap baris tabel Data uji sort (langkah 1 sampai 7): klik header kolom pada baris itu satu kali
2. Verifikasi urutan baris sesuai kolom "Klik 1 (Ascending)" pada baris tabel
3. Klik header kolom yang sama kali kedua
4. Verifikasi urutan baris sesuai kolom "Klik 2 (Descending)" pada baris tabel
5. Klik header kolom yang sama kali ketiga
6. Verifikasi urutan kembali ke default `Label` A-Z
7. Verifikasi indikator sort hilang

### TC-FA-LBL-246: Berpindah kolom sort mereset kolom sebelumnya dan memulai Ascending

8. Klik header `Total Asset` sekali
9. Klik header `Modified By` sekali
10. Verifikasi indikator sort `Total Asset` kembali netral
11. Verifikasi indikator sort `Modified By` Ascending
12. Verifikasi hanya satu kolom yang memiliki sort aktif

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Spec ini 12 langkah nominal dan 40 langkah setelah ekspansi (di atas smell 35 langkah; langkah 1 sampai 7 diulang untuk lima baris tabel Data uji sort, bagian 8b butir 7). Alasan: seluruh blok adalah Sort Labels List pada dataset Pre-setup #12 yang sama dengan prosedur tiga klik yang identik per kolom dan hanya data tabel yang berbeda; kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Baris tabel Data uji sort memetakan satu TC per baris: TC-FA-LBL-241 (Label), TC-FA-LBL-242 (Color Hex), TC-FA-LBL-243 (Total Asset), TC-FA-LBL-244 (Modified By), TC-FA-LBL-245 (Last Updated).
