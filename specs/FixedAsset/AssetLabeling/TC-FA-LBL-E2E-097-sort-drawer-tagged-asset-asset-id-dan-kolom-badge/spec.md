---
id: TC-FA-LBL-E2E-097-sort-drawer-tagged-asset-asset-id-dan-kolom-badge
title: "Sort Drawer Tagged Asset: Asset ID dan Kolom Badge"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-356
  - TC-FA-LBL-357
coverage:
  web: automated
---

# Sort Drawer Tagged Asset: Asset ID dan Kolom Badge

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

- Tabel "Data uji sort kolom badge" (parameter langkah berulang 10 sampai 15; TC-FA-LBL-357):

  | Kolom | Ascending | Descending |
  |---|---|---|
  | `Brand` | `Dell` (`Laptop Dell - 1`, `Laptop Dell - 2`), `Epson`, `HP`, `LG` | `LG`, `HP`, `Epson`, `Dell` |
  | `Model/Type` | `EB-X49`, `LaserJet Pro`, `Latitude 5440` (dua baris), `UltraWide 34` | urutan terbalik: `UltraWide 34`, `Latitude 5440` (dua baris), `LaserJet Pro`, `EB-X49` |
  | `Group` | `Floor 1`, `Floor 2`, `Head Office` (`Monitor LG - 4` lalu `Printer HP - 3`), `Warehouse` | urutan terbalik: `Warehouse`, `Head Office`, `Floor 2`, `Floor 1` |
  | `Category` | `Laptop` (dua baris), `Monitor`, `Printer`, `Projector` | urutan terbalik: `Projector`, `Printer`, `Monitor`, `Laptop` (dua baris) |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (kolom `Category` ditampilkan pada langkah 9 dan dipulihkan pada langkah 16); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]`.

## Test Steps

### TC-FA-LBL-356: Sort Drawer kolom Asset ID

1. Klik chip `Finance Department` di kolom Label
2. Klik header kolom `Asset ID` satu kali
3. Verifikasi Ascending: `AST-0001` sampai `AST-0005` berurutan (`Laptop Dell - 1`, `Laptop Dell - 2`, `Printer HP - 3`, `Monitor LG - 4`, `Projector Epson - 5`)
4. Klik header kolom `Asset ID` sekali lagi (klik kedua)
5. Verifikasi Descending: `AST-0005` sampai `AST-0001`
6. Klik header kolom `Asset ID` sekali lagi (klik ketiga)
7. Verifikasi Netral: kembali ke default Name A-Z

### TC-FA-LBL-357: Sort Drawer kelas badge Brand, Model/Type, Group, dan Category: alfabetis 3 tahap

8. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
9. Tampilkan kolom `Category`: centang `Category`, lalu klik `[Save]`
10. Untuk setiap baris tabel "Data uji sort kolom badge" (langkah 10 sampai 15): klik header kolom pada baris itu satu kali
11. Verifikasi Ascending sesuai kolom "Ascending" pada baris tabel
12. Klik header kolom pada baris itu sekali lagi (klik kedua)
13. Verifikasi Descending sesuai kolom "Descending" pada baris tabel
14. Klik header kolom pada baris itu sekali lagi (klik ketiga)
15. Verifikasi klik ketiga mengembalikan default Name A-Z
16. Pulihkan konfigurasi kolom: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah berulang (bagian 8b butir 7): empat kolom TC-FA-LBL-357 memakai tabel "Data uji sort kolom badge" pada Prerequisites, tanpa langkah bersyarat; langkah yang diulang adalah langkah 10 sampai 15. Ambang langkah dihitung dengan ekspansi (empat kali enam langkah): spec berisi 34 langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menampilkan kolom `Category` lewat Setup Column (langkah TC); pemulihan konfigurasi kolom di langkah 16 (S-09). `[Save]` Setup Column adalah aksi sisi klien (bagian 8b butir 8).
- Pembagian TC lintas spec: TC-FA-LBL-355 (sort Name pada 500 aset) ada di spec 103; TC-FA-LBL-358 sampai TC-FA-LBL-361 ada di spec 098.
- Temuan untuk QA:
  - TC-FA-LBL-357 menulis Descending sebagai 'urutan terbalik' tanpa merinci urutan baris bernilai sama (dua baris `Latitude 5440`, dua baris `Head Office`, dua baris `Laptop`); spec hanya mengasersi urutan nilai badge, bukan urutan baris sama-nilai pada Descending. Tie-breaker baris sama-nilai ditetapkan TC-FA-LBL-361 (spec 098).
