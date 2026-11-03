---
id: TC-FA-LBL-E2E-100-setup-column-drawer-reset-to-default-discard-dan-pin
title: "Setup Column Drawer: Reset to Default, Discard, dan Pin"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-367
  - TC-FA-LBL-368
coverage:
  web: automated
---

# Setup Column Drawer: Reset to Default, Discard, dan Pin

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

- Company Alpha memiliki dua buku Asset Value tetap `Commercial` dan `Fiscal` (precondition TC-FA-LBL-368).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (kolom dan pin diubah dan dipulihkan pada langkah 35); lebar viewport dipersempit pada langkah 12 dan dipulihkan pada langkah 35; hook `after` suite menghapus preferensi kolom di browser dan memulihkan viewport sebagai cadangan, bukan `[Reset to Default]`.
- Kemampuan teknis: mempersempit lebar viewport sampai tabel Drawer dapat di-scroll horizontal dan mengamati kolom membeku (sticky) saat scroll; lebar dan mekanisme observasi ditetapkan tim FE saat script.

## Test Steps

### TC-FA-LBL-368: Setup Column Drawer: Reset to Default dan discard

1. Klik chip `Finance Department` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
3. Centang `Category` dan hapus centang `Brand`
4. Klik `[Reset to Default]`
5. Klik `[Save]`
6. Verifikasi setelah Reset dan Save: delapan kolom default tampil
7. Verifikasi setelah Reset dan Save: kedelapan kolom Curated (`Measurement`, `Category`, `Label`, `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, `Warranty Expiry`) tersembunyi
8. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
9. Hapus centang `Group`
10. Klik `[✕]` pada popup Setup Column
11. Verifikasi perubahan `Group` dibuang (kolom `Group` tetap tampil di tabel)

### TC-FA-LBL-367: Setup Column Drawer: pin dan batas pin ketiga

12. Persempit lebar viewport sampai tabel Drawer dapat di-scroll horizontal
13. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
14. Centang `Category` dan `Label`
15. Klik icon Pin `Name`, `Asset ID`, dan `Brand` satu per satu
16. Hover icon Pin `Model/Type`
17. Verifikasi icon Pin `Model/Type` disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
18. Klik `[Save]`
19. Scroll tabel horizontal
20. Verifikasi `Name`, `Asset ID`, dan `Brand` membeku di kiri saat scroll
21. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
22. Lepas pin `Name`, `Asset ID`, dan `Brand`
23. Klik icon Pin `Model/Type`, `Group`, dan `Status`
24. Klik `[Save]`
25. Scroll tabel horizontal
26. Verifikasi `Model/Type`, `Group`, dan `Status` membeku di kiri saat scroll
27. Verifikasi `Name`, `Asset ID`, dan `Brand` ikut bergeser saat scroll
28. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
29. Lepas pin `Model/Type`, `Group`, dan `Status`
30. Klik icon Pin `Last Updated`, `Category`, dan `Label`
31. Klik `[Save]`
32. Scroll tabel horizontal
33. Verifikasi `Last Updated`, `Category`, dan `Label` membeku di kiri saat scroll
34. Verifikasi `Model/Type`, `Group`, dan `Status` ikut bergeser saat scroll
35. Pulihkan konfigurasi dan viewport: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`, lalu pulihkan lebar viewport ke ukuran semula

## Notes

- Mode: FE+BE (backend nyata; konfigurasi kolom tersimpan di browser). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC: TC-FA-LBL-368 (Reset to Default dan discard) lebih dulu karena berakhir pada konfigurasi default, yang menjadi titik awal TC-FA-LBL-367 (pin bertahap yang tiap tahapnya bergantung pada tahap sebelumnya).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): mempersempit lebar viewport agar tabel dapat di-scroll horizontal (langkah 12); pemulihan konfigurasi kolom dan viewport di langkah 35 (S-09). `[Save]` Setup Column adalah aksi sisi klien (bagian 8b butir 8).
- Pembagian TC lintas spec: TC-FA-LBL-362, TC-FA-LBL-363, TC-FA-LBL-365, dan TC-FA-LBL-369 ada di spec 099; TC-FA-LBL-364 ada di spec 170; TC-FA-LBL-366 ada di spec 101.
- Temuan untuk QA:
  - TC-FA-LBL-367 tidak menyebut lebar viewport 'sempit' secara numerik dan cara mengamati kolom membeku saat scroll; lebar dan mekanisme observasi (posisi sticky) ditetapkan tim FE saat script.
  - TC-FA-LBL-368 menulis 'sembunyikan `Brand`' sebelum `[Reset to Default]` tanpa asersi di antaranya; spec mengikuti TC dan hanya mengasersi hasil sesudah Reset dan Save.
