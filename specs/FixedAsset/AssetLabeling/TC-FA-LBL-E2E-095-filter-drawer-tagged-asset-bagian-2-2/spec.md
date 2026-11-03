---
id: TC-FA-LBL-E2E-095-filter-drawer-tagged-asset-bagian-2-2
title: "Filter Drawer Tagged Asset (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-351
  - TC-FA-LBL-352
  - TC-FA-LBL-353
  - TC-FA-LBL-354
  - TC-FA-LBL-575
coverage:
  web: automated
---

# Filter Drawer Tagged Asset (bagian 2/2)

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

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-LBL-351: Filter Last Updated Drawer: rentang inklusif

1. Klik chip `Finance Department` di kolom Label
2. Verifikasi lima baris tampil di Drawer (pembanding asersi hasil Filter)
3. Klik icon Filter di toolbar Drawer
4. Pilih rentang `11 Sep 2026` sampai `12 Sep 2026` pada field `Last Updated`, lalu klik `[Apply]`
5. Verifikasi dua baris `Monitor LG - 4` (11 Sep) dan `Printer HP - 3` (12 Sep) tampil
6. Pulihkan: klik `[Clear Field]`, klik `[Apply]`, lalu klik area di luar panel

### TC-FA-LBL-352: Kombinasi filter Brand dan Status berlogika AND di Drawer

7. Klik icon Filter di toolbar Drawer
8. Pilih `Brand` = `Dell` dan `Status` = `Borrowed`, lalu klik `[Apply]`
9. Verifikasi hanya `Laptop Dell - 2` tampil
10. Pulihkan: klik `[Clear Field]`, klik `[Apply]`, lalu klik area di luar panel

### TC-FA-LBL-353: Search dan Filter Drawer menghasilkan irisan

11. Ketik Search `Dell`, tekan Enter
12. Klik icon Filter di toolbar Drawer
13. Pilih `Status` = `Borrowed`, lalu klik `[Apply]`
14. Verifikasi hanya `Laptop Dell - 2` tampil
15. Pulihkan: klik `[Clear Field]`, klik `[Apply]`, lalu klik area di luar panel, lalu klik `(←)` pada kotak Search

### TC-FA-LBL-354: Membuka ulang Drawer tidak membawa filter ter-Apply sebelumnya

16. Klik icon Filter di toolbar Drawer
17. Pilih `Brand` = `Dell`, lalu klik `[Apply]`
18. Tutup Drawer dengan `[✕]`
19. Klik chip `Finance Department` di kolom Label
20. Verifikasi Drawer menampilkan lima baris
21. Verifikasi tidak ada filter ter-Apply (icon Filter tanpa badge titik)
22. Verifikasi sort default Name A-Z

### TC-FA-LBL-575: Filter Drawer kolom Asset ID: tidak Filterable (Asset ID unik), pencarian lewat Search

23. Klik icon Filter di toolbar Drawer
24. Verifikasi Filter Panel memuat field `Asset Name`
25. Verifikasi Filter Panel tidak memuat field `Asset ID`
26. Tutup Filter Panel (klik area di luar panel)
27. Ketik Search `AST-0003`, tekan Enter
28. Verifikasi hanya `Printer HP - 3` tampil
29. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): pemulihan filter, panel, dan Search sesudah tiap TC (S-09); menutup Filter Panel sebelum mengetik Search pada TC-FA-LBL-575 (TC menulis 'Tutup Filter Panel lalu ketik').
- Asersi tambahan (S-03): `Verifikasi` lima baris tampil di Drawer sebelum Filter pertama menjadi pembanding asersi universal (bagian 8b butir 2); `Verifikasi` icon Filter tanpa badge titik mengamati 'tanpa filter ter-Apply' memakai indikator titik pada icon Filter yang ditetapkan TC-FA-LBL-236 (spec 165); `Verifikasi` field `Asset Name` tampil pada langkah 24 menjadi anchor positif untuk absence field `Asset ID` (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-LBL-346 sampai TC-FA-LBL-349 ada di spec 094; TC-FA-LBL-350 ada di spec 096.
- Temuan untuk QA:
  - Expected TC-FA-LBL-532 (spec 102) menyebut field `Asset ID` di Filter Panel, bertentangan dengan TC-FA-LBL-346 dan TC-FA-LBL-575 yang menyatakan `Asset ID` tidak Filterable; spec ini mengikuti TC-FA-LBL-575.
  - TC-FA-LBL-354 tidak menyatakan cara mengamati 'tanpa filter ter-Apply'; spec memakai indikator titik pada icon Filter.
  - TC-FA-LBL-351 hingga TC-FA-LBL-353 tidak menyatakan apakah `[Apply]` menutup Filter Panel; spec berasumsi panel tetap terbuka sesudah `[Apply]` dan menutupnya dengan klik area di luar panel pada langkah pemulihan.
