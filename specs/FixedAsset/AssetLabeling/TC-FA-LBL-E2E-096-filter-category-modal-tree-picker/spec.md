---
id: TC-FA-LBL-E2E-096-filter-category-modal-tree-picker
title: "Filter Category: Modal Tree Picker"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-350
  - TC-FA-LBL-527
  - TC-FA-LBL-528
  - TC-FA-LBL-529
coverage:
  web: automated
---

# Filter Category: Modal Tree Picker

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

- Tree Category client Company Alpha (Pre-setup #13 dan #30): `IT Equipment` (induk) dengan turunan `Laptop` dan `Enterprise Computing Hardware Devices`; `Printer`, `Monitor`, dan `Projector` adalah node tingkat atas (bukan turunan `IT Equipment`).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-LBL-527: Screening Modal Tree Picker filter Category di Drawer

1. Klik chip `Finance Department` di kolom Label
2. Klik icon Filter di toolbar Drawer
3. Klik field `Category`
4. Verifikasi Modal Tree Picker multi-select terbuka
5. Verifikasi tree Category penuh client tampil, termasuk `IT Equipment` dengan turunan `Laptop` dan `Enterprise Computing Hardware Devices` serta `Printer`, `Monitor`, dan `Projector` sebagai node tingkat atas
6. Verifikasi tiap node punya checkbox
7. Verifikasi kotak Search untuk memfilter node tampil
8. Verifikasi footer berisi tombol `[Cancel]` dan `[Select]`

### TC-FA-LBL-528: Modal Tree Picker Category: centang induk men-cascade turunan dan Search memfilter node

9. Centang node `IT Equipment`
10. Verifikasi turunan `Laptop` dan `Enterprise Computing Hardware Devices` ikut tercentang (cascade induk ke turunan)
11. Ketik `Lapt` di kotak Search tree
12. Verifikasi node `Laptop` (dengan induk `IT Equipment`) tampil
13. Verifikasi node yang tidak cocok tidak tampil
14. Klik `[Cancel]` (membuang pilihan pending)

### TC-FA-LBL-529: Modal Tree Picker Category: Cancel membuang pilihan pending, Select menerapkannya sebagai chip

15. Klik field `Category`
16. Centang node `Printer`
17. Klik `[Cancel]`
18. Verifikasi modal tertutup
19. Verifikasi field `Category` tetap kosong tanpa chip (pilihan pending dibuang)
20. Klik field `Category` lagi
21. Centang `Printer`
22. Klik `[Select]`
23. Verifikasi modal tertutup
24. Verifikasi chip `Printer` tampil di field `Category`
25. Klik `(✕)` pada chip `Printer` di field `Category`
26. Verifikasi chip `Printer` hilang dari field

### TC-FA-LBL-350: Filter Category memakai Modal Tree Picker multi-select

27. Klik field `Category`
28. Centang node induk `IT Equipment` di tree picker
29. Klik `[Select]`
30. Klik `[Apply]`
31. Verifikasi dua baris `Laptop Dell - 1` dan `Laptop Dell - 2` tampil karena Category `Laptop` adalah turunan `IT Equipment`
32. Verifikasi `Printer HP - 3`, `Monitor LG - 4`, dan `Projector Epson - 5` tidak tampil karena Category-nya node tingkat atas lain
33. Pulihkan: klik `[Clear Field]`, klik `[Apply]`, lalu klik area di luar panel

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC: screening Modal Tree Picker (TC-FA-LBL-527) lebih dulu, lalu cascade dan Search tree (TC-FA-LBL-528), Cancel dan Select (TC-FA-LBL-529), dan terakhir aksi sukses `[Apply]` (TC-FA-LBL-350) sesuai urutan bagian 3 (screening di awal, aksi sukses di akhir). Modal dari TC-FA-LBL-527 tetap terbuka untuk TC-FA-LBL-528; TC-FA-LBL-528 ditutup dengan `[Cancel]` agar TC-FA-LBL-529 mulai dari pilihan kosong.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): `[Cancel]` penutup TC-FA-LBL-528; pemulihan filter dan panel di langkah terakhir (S-09). Absence 'tidak tampil' pada TC-FA-LBL-350 memakai dua baris `Laptop Dell` yang diasersi sebelumnya sebagai anchor (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-LBL-346 sampai TC-FA-LBL-349 ada di spec 094; TC-FA-LBL-351 sampai TC-FA-LBL-354 dan TC-FA-LBL-575 ada di spec 095.
- Temuan untuk QA:
  - TC-FA-LBL-527 menyebut tree 'penuh client' termasuk `Enterprise Computing Hardware Devices` (Pre-setup #30); Pre-setup #13 tidak memuat node itu sehingga tree di Company Alpha bergantung pada Pre-setup #30 tersedia.
  - TC-FA-LBL-350 tidak menyatakan apakah `[Apply]` menutup Filter Panel; spec berasumsi panel tetap terbuka sesudah `[Apply]` dan menutupnya dengan klik area di luar panel pada langkah pemulihan.
