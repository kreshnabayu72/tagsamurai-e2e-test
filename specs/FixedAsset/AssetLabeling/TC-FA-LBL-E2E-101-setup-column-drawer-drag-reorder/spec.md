---
id: TC-FA-LBL-E2E-101-setup-column-drawer-drag-reorder
title: "Setup Column Drawer: Drag Reorder"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-366
coverage:
  web: automated
---

# Setup Column Drawer: Drag Reorder

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
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (urutan dan tampilan kolom disimpan lewat `[Save]`, dipulihkan pada langkah 11); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]`.
- Kemampuan teknis: muat ulang halaman dengan F5 (`beforeunload` tidak dipicu karena tidak ada form dirty).
- Tabel "Data uji drag" (parameter langkah berulang 4 sampai 5; sepuluh seretan berurutan, tiap baris menyeret kolom ke posisi paling atas; urutan sesudahnya ditulis dari kolom pertama):

  | Kolom yang diseret | Urutan Live Preview sesudahnya |
  |---|---|
  | `Asset ID` | `Asset ID` pertama |
  | `Brand` | `Brand`, `Asset ID` |
  | `Model/Type` | `Model/Type`, `Brand`, `Asset ID` |
  | `Group` | `Group`, `Model/Type`, `Brand`, `Asset ID` |
  | `Status` | `Status`, `Group`, `Model/Type`, `Brand`, `Asset ID` |
  | `Last Updated` | `Last Updated`, `Status`, `Group`, `Model/Type`, `Brand`, `Asset ID` |
  | `Category` | `Category`, `Last Updated`, `Status`, `Group`, `Model/Type`, `Brand`, `Asset ID` |
  | `Label` | `Label`, `Category`, `Last Updated`, `Status`, `Group`, `Model/Type`, `Brand`, `Asset ID` |
  | `Name` | `Name`, `Label`, `Category`, `Last Updated`, `Status`, `Group`, `Model/Type`, `Brand`, `Asset ID`, lalu `TAG` |
  | `TAG` | `TAG`, `Name`, `Label`, `Category`, `Last Updated`, `Status`, `Group`, `Model/Type`, `Brand`, `Asset ID` |


## Test Steps

### TC-FA-LBL-366: Setup Column Drawer: drag reorder

1. Klik chip `Finance Department` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
3. Centang `Category` dan `Label`
4. Untuk setiap baris tabel "Data uji drag" (langkah 4 sampai 5): seret kolom pada baris itu ke posisi paling atas daftar Setup Column
5. Verifikasi urutan Live Preview sesuai kolom "Urutan Live Preview sesudahnya" pada baris tabel
6. Klik `[Save]`
7. Verifikasi urutan header tabel Drawer sama dengan urutan Live Preview pada baris terakhir tabel (`TAG`, `Name`, `Label`, `Category`, `Last Updated`, `Status`, `Group`, `Model/Type`, `Brand`, `Asset ID`)
8. Tekan F5
9. Klik chip `Finance Department` di kolom Label (membuka Drawer kembali)
10. Verifikasi urutan header tabel Drawer bertahan setelah reload (sama dengan urutan sebelum F5)
11. Pulihkan konfigurasi kolom: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Mode: FE+BE (backend nyata; konfigurasi kolom tersimpan di browser). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah berulang (bagian 8b butir 7): sepuluh seretan TC-FA-LBL-366 memakai tabel "Data uji drag" pada Prerequisites, tanpa langkah bersyarat; langkah yang diulang adalah langkah 4 sampai 5. Ambang langkah dihitung dengan ekspansi (sepuluh kali dua langkah): spec berisi 29 langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): membuka Drawer kembali sesudah F5; pemulihan konfigurasi kolom di langkah 11 (S-09). `[Save]` Setup Column adalah aksi sisi klien (bagian 8b butir 8).
- Pembagian TC lintas spec: TC-FA-LBL-362, TC-FA-LBL-363, TC-FA-LBL-365, dan TC-FA-LBL-369 ada di spec 099; TC-FA-LBL-364 ada di spec 170; TC-FA-LBL-367 dan TC-FA-LBL-368 ada di spec 100.
- Temuan untuk QA:
  - Expected TC-FA-LBL-366 butir a sampai h hanya menyebut kolom yang sudah diseret (kolom pertama diikuti kolom yang diseret sebelumnya); spec mengasersi awalan urutan itu, bukan seluruh urutan Live Preview, kecuali butir i, j, dan k yang menyebut urutan lengkap.
  - TC-FA-LBL-366 butir i menulis kolom `TAG` di urutan terakhir sesudah `Asset ID`; spec mengikuti penulisan TC.
