---
id: TC-FA-LBL-E2E-092-search-drawer-tagged-asset-bagian-1-2
title: "Search Drawer Tagged Asset (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-338
  - TC-FA-LBL-339
  - TC-FA-LBL-340
  - TC-FA-LBL-341
  - TC-FA-LBL-342
  - TC-FA-LBL-343
coverage:
  web: automated
---

# Search Drawer Tagged Asset (bagian 1/2)

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
- Search pada spec ini adalah Search toolbar Drawer Tagged Asset (menyaring saat Enter, bagian 8b butir 9).

## Test Steps

### TC-FA-LBL-338: Search Drawer kolom Asset ID

1. Klik chip `Finance Department` di kolom Label
2. Verifikasi sedikitnya satu baris tampil di Drawer (pembanding asersi hasil Search)
3. Ketik Search `AST-0003`, tekan Enter
4. Verifikasi hanya `Printer HP - 3` tampil
5. Klik `(←)` pada kotak Search

### TC-FA-LBL-339: Search Drawer mencocokkan teks lengkap Name dengan Increment

6. Klik icon Search di toolbar Drawer
7. Verifikasi kotak Search yang kosong berplaceholder `Search name, asset ID, brand...`
8. Ketik `Laptop Dell - 2` di kotak Search, tekan Enter
9. Verifikasi hanya `Laptop Dell - 2` tampil
10. Klik `(←)` pada kotak Search

### TC-FA-LBL-340: Search Drawer kelas Model/Type dan Group

11. Ketik Search `UltraWide`, tekan Enter
12. Verifikasi `UltraWide`: hanya `Monitor LG - 4` tampil
13. Ganti isi kotak search dengan `Warehouse`, tekan Enter
14. Verifikasi `Warehouse`: hanya `Projector Epson - 5` tampil
15. Klik `(←)` pada kotak Search

### TC-FA-LBL-341: Search Drawer kolom Status

16. Ketik Search `draft`, tekan Enter
17. Verifikasi `draft`: hanya `Printer HP - 3` tampil
18. Ganti isi kotak search dengan `Disposed`, tekan Enter
19. Verifikasi `Disposed`: hanya `Projector Epson - 5` tampil
20. Klik `(←)` pada kotak Search

### TC-FA-LBL-342: Search Drawer kolom Brand

21. Ketik Search `Dell`, tekan Enter
22. Verifikasi dua baris `Laptop Dell - 1` dan `Laptop Dell - 2` (Brand `Dell`) tampil
23. Klik `(←)` pada kotak Search

### TC-FA-LBL-343: Search Drawer tanpa hasil

24. Ketik Search `zzzz`, tekan Enter
25. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.` tampil
26. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Seluruh TC memakai satu pembukaan Drawer `Finance Department` (TC tanpa perubahan state data); setiap TC diakhiri `(←)` pada kotak Search agar tabel kembali ke lima baris (S-09).
- Asersi tambahan (S-03): `Verifikasi` sedikitnya satu baris tampil di Drawer sebelum Search pertama menjadi pembanding asersi universal 'hanya ...' (bagian 8b butir 2); tidak ada di TC sumber. Membuka kotak Search sebelum `Verifikasi` placeholder pada TC-FA-LBL-339 adalah langkah penghubung (S-14).
- Pembagian TC lintas spec: TC-FA-LBL-344, TC-FA-LBL-345, dan TC-FA-LBL-493 ada di spec 093; TC-FA-LBL-575 (Asset ID bukan field Filter) ada di spec 095.
- Temuan untuk QA:
  - TC-FA-LBL-341 mengetik `draft` huruf kecil dan mengharapkan `Printer HP - 3` (Status `Draft`); spec mengikuti TC sehingga ketidakpekaan huruf besar-kecil pada Search Status ikut teruji.
