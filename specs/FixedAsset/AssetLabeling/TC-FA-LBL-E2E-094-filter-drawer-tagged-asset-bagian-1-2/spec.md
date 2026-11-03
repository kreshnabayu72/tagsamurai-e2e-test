---
id: TC-FA-LBL-E2E-094-filter-drawer-tagged-asset-bagian-1-2
title: "Filter Drawer Tagged Asset (bagian 1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-346
  - TC-FA-LBL-347
  - TC-FA-LBL-348
  - TC-FA-LBL-349
coverage:
  web: automated
---

# Filter Drawer Tagged Asset (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 dan #13 (Company Alpha; hanya dibaca, tidak diubah). Label `Finance Department` (`#3B82F6`, Total Asset 5) memiliki lima aset aktif berikut; `Scanner Zebra - 6` (Deleted) terpasang label yang sama dan tidak dihitung:

  | Aset | Asset ID | Status | Brand | Model/Type | Group | Category | Label lain | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | `Laptop Dell - 1` | `AST-0001` | `Available` | `Dell` | `Latitude 5440` | `Head Office > Floor 1` | `IT Equipment > Laptop` | `High Priority` | 14 Sep 2026 09:00 |
  | `Laptop Dell - 2` | `AST-0002` | `Borrowed` | `Dell` | `Latitude 5440` | `Head Office > Floor 2` | `IT Equipment > Laptop` | - | 13 Sep 2026 09:00 |
  | `Printer HP - 3` | `AST-0003` | `Draft` | `HP` | `LaserJet Pro` | `Head Office` | `Printer` | `Audit Ready`, `Maintenance Due` | 12 Sep 2026 09:00 |
  | `Monitor LG - 4` | `AST-0004` | `Waiting for Approval` | `LG` | `UltraWide 34` | `Head Office` | `Monitor` | - | 11 Sep 2026 09:00 |
  | `Projector Epson - 5` | `AST-0005` | `Disposed` | `Epson` | `EB-X49` | `Warehouse` | `Projector` | - | 10 Sep 2026 09:00 |

- Company Alpha memiliki dua buku Asset Value tetap `Commercial` dan `Fiscal` (precondition TC-FA-LBL-346).
- Tabel "Data uji filter multi-select" (parameter langkah berulang 19 sampai 21; TC-FA-LBL-349):

  | Field dan nilai | Baris hasil |
  |---|---|
  | `Brand` = `HP` dan `LG` | `Printer HP - 3` dan `Monitor LG - 4` (OR dalam field) |
  | `Status` = `Disposed` | `Projector Epson - 5` |
  | `Group` = `Warehouse` | `Projector Epson - 5` |
  | `Model/Type` = `Latitude 5440` | `Laptop Dell - 1` dan `Laptop Dell - 2` |
  | `Label` = `Audit Ready` | `Printer HP - 3` |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-LBL-346: Screening Filter Panel Drawer

1. Klik chip `Finance Department` di kolom Label
2. Verifikasi lima baris tampil di Drawer (pembanding asersi hasil Filter)
3. Klik icon Filter di toolbar Drawer
4. Verifikasi field dan placeholder: `Asset Name` (`All asset names`), `TAG` (`All tags`), `Brand` (`All brands`), `Model/Type` (`All models`), `Measurement` (`All units`), `Category` (tree picker multi-select, `All categories`), `Group` (`All groups`), `Label` (`All labels`), `Status` (`All statuses`), `Transactional Policy` (`All transactions`), `Last Scanned` (`Select date`), `Asset Value (Commercial)` dan `Asset Value (Fiscal)` (`Min` / `Max`), `Warranty Expiry` (`Select date`), `Last Updated` (`Select date`)
5. Verifikasi maksimal 4 field per baris
6. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan)
7. Verifikasi belum ada filter ter-Apply (icon Filter tanpa badge titik)

### TC-FA-LBL-347: Isi opsi dropdown filter Drawer bersumber dari data tabel

8. Buka dropdown `Asset Name`
9. Verifikasi opsi `Asset Name`: `Laptop Dell`, `Monitor LG`, `Printer HP`, `Projector Epson` (nama aset tanpa Increment)
10. Tutup dropdown lalu buka dropdown `Brand`
11. Verifikasi opsi `Brand`: `Dell`, `Epson`, `HP`, `LG`
12. Tutup dropdown lalu buka dropdown `Status`
13. Verifikasi opsi `Status`: `Available`, `Borrowed`, `Disposed`, `Draft`, `Waiting for Approval`
14. Tutup dropdown lalu buka dropdown `Label`
15. Verifikasi opsi `Label`: `Audit Ready`, `Finance Department`, `High Priority`, `Maintenance Due` (seluruh label aset di tabel termasuk label yang sedang dibuka)

### TC-FA-LBL-348: Filter Asset Name menyaring semua unit bernama sama

16. Tutup dropdown `Label`
17. Pilih `Asset Name` = `Laptop Dell`, lalu klik `[Apply]`
18. Verifikasi dua baris `Laptop Dell - 1` dan `Laptop Dell - 2` tampil

### TC-FA-LBL-349: Filter multi-select Drawer kelas Brand, Model/Type, Group, Status, Label

19. Untuk setiap baris tabel "Data uji filter multi-select" (langkah 19 sampai 21): klik `[Clear Field]`
20. Pilih field dan nilai pada baris tabel, lalu klik `[Apply]`
21. Verifikasi baris hasil sesuai kolom "Baris hasil" pada baris tabel
22. Pulihkan: klik `[Clear Field]`, klik `[Apply]`, lalu klik area di luar panel

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah berulang (bagian 8b butir 7): lima variasi filter TC-FA-LBL-349 memakai tabel "Data uji filter multi-select" pada Prerequisites, tanpa langkah bersyarat; langkah yang diulang adalah langkah 19 sampai 21. Ambang langkah dihitung dengan ekspansi (lima kali tiga langkah): spec berisi 34 langkah.
- Seluruh TC memakai satu pembukaan Drawer `Finance Department` (TC tanpa perubahan state data). Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup dropdown; `[Clear Field]` pada awal tiap putaran TC-FA-LBL-349 (TC menulis 'Bersihkan'); pemulihan filter dan panel di langkah 22 (S-09).
- Asersi tambahan (S-03): `Verifikasi` lima baris tampil di Drawer sebelum Filter pertama menjadi pembanding asersi universal (bagian 8b butir 2); `Verifikasi` icon Filter tanpa badge titik mengamati 'belum ada filter ter-Apply' memakai indikator titik pada icon Filter yang ditetapkan TC-FA-LBL-236 (spec 165).
- Pembagian TC lintas spec: TC-FA-LBL-350 ada di spec 096; TC-FA-LBL-351 sampai TC-FA-LBL-354 dan TC-FA-LBL-575 ada di spec 095.
- Temuan untuk QA:
  - TC-FA-LBL-349 menulis 'Bersihkan' tanpa menyatakan apakah `[Clear Field]` sendiri menerapkan filter kosong atau memerlukan `[Apply]`; spec menekan `[Clear Field]` lalu langsung memilih nilai berikutnya dan `[Apply]`.
  - TC-FA-LBL-346 dan TC-FA-LBL-347 tidak menyatakan apakah `[Apply]` menutup Filter Panel; spec berasumsi panel tetap terbuka sesudah `[Apply]` sesuai urutan langkah TC-FA-LBL-349 dan menutup panel dengan klik area di luar panel pada langkah pemulihan.
  - Daftar field Filter Panel pada TC-FA-LBL-346 tidak memuat `Asset ID` (selaras dengan TC-FA-LBL-575), sedangkan Expected TC-FA-LBL-532 (spec 102) menyebut `Asset ID` di Filter Panel.
