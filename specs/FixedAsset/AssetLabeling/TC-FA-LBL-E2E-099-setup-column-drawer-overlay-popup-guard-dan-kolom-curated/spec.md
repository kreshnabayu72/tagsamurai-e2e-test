---
id: TC-FA-LBL-E2E-099-setup-column-drawer-overlay-popup-guard-dan-kolom-curated
title: "Setup Column Drawer: Overlay, Popup, Guard, dan Kolom Curated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-362
  - TC-FA-LBL-363
  - TC-FA-LBL-365
  - TC-FA-LBL-369
coverage:
  web: automated
---

# Setup Column Drawer: Overlay, Popup, Guard, dan Kolom Curated

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

- Company Alpha tidak memiliki Custom Field Active dan memiliki dua buku Asset Value tetap `Commercial` dan `Fiscal` (precondition TC-FA-LBL-362 dan TC-FA-LBL-363).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (kolom `Category` dan `Label` ditampilkan pada langkah 23 dan dipulihkan pada langkah 29); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]`.

## Test Steps

### TC-FA-LBL-362: Screening overlay Column Visibility Drawer

1. Klik chip `Finance Department` di kolom Label
2. Klik header kolom Actions (⋯) di Drawer
3. Verifikasi overlay memuat delapan kolom Hideable tercentang (`Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`)
4. Verifikasi overlay memuat delapan kolom Curated tidak tercentang (`Measurement`, `Category`, `Label`, `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, `Warranty Expiry`)
5. Verifikasi urutan daftar: `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Measurement`, `Category`, `Group`, `Label`, `Status`, `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, `Warranty Expiry`, `Last Updated`
6. Verifikasi tidak ada kolom yang dikecualikan (`Group` dan `Category` sama-sama tersedia)
7. Verifikasi overlay memuat drag handle dan item `Setup Column...`

### TC-FA-LBL-363: Screening Popup Setup Column Drawer (3 zona)

8. Klik `Setup Column...`
9. Verifikasi Zona Header: Title `Setup Column`
10. Verifikasi Zona Header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi Zona Header: `[✕]` tampil
12. Verifikasi Zona Body: enam belas kolom dengan checkbox, drag handle, icon Pin
13. Verifikasi Zona Body: delapan kolom default tercentang dan delapan kolom Curated (`Measurement`, `Category`, `Label`, `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, `Warranty Expiry`) tidak tercentang
14. Verifikasi Zona Body: Live Preview tampil
15. Verifikasi Zona Footer: `[Reset to Default]` dan `[Save]` tampil
16. Verifikasi Zona Footer: tidak ada `[Cancel]`

### TC-FA-LBL-369: Setup Column Drawer: guard satu kolom tersisa

17. Hapus centang tujuh kolom Hideable lain (`Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`) sehingga hanya `Name` tersisa
18. Hover checkbox `Name`
19. Verifikasi checkbox `Name` disabled dengan tooltip `At least one column must remain visible.`
20. Klik `[✕]` pada popup Setup Column (menutup tanpa menyimpan)

### TC-FA-LBL-365: Setup Column Drawer: ceklis kelas Curated menampilkan Category dan Label

21. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
22. Centang `Category` dan `Label`
23. Klik `[Save]`
24. Verifikasi kolom `Category` (badge Primary) tampil di tabel
25. Hover badge `Category`
26. Verifikasi hover badge `Category` menampilkan hierarki `IT Equipment > Laptop`
27. Verifikasi kolom `Label` (BadgeGroup berwarna hex label) tampil di tabel
28. Verifikasi kolom Label memuat seluruh label aset, termasuk `Finance Department` yang sedang dibuka
29. Pulihkan konfigurasi kolom: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC: TC-FA-LBL-362, TC-FA-LBL-363, dan TC-FA-LBL-369 dilakukan pada overlay dan popup yang sama tanpa menyimpan perubahan (overlay dari TC-FA-LBL-362 dilanjutkan ke popup TC-FA-LBL-363; popup tetap terbuka untuk TC-FA-LBL-369 yang ditutup dengan `[✕]` tanpa menyimpan); TC-FA-LBL-365 yang menyimpan konfigurasi (`[Save]`) ditaruh terakhir (aksi yang mengubah state di akhir, bagian 3).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): pemulihan konfigurasi kolom di langkah 29 (S-09). `[Save]` Setup Column adalah aksi sisi klien (bagian 8b butir 8).
- Pembagian TC lintas spec: TC-FA-LBL-364 ada di spec 170; TC-FA-LBL-366 ada di spec 101; TC-FA-LBL-367 dan TC-FA-LBL-368 ada di spec 100.
- Temuan untuk QA:
  - TC-FA-LBL-362 Expected menulis 'drag handle, dan item `Setup Column...`' tanpa kata kerja di depan 'drag handle'; spec membaca keduanya sebagai elemen yang tampil di overlay.
  - TC-FA-LBL-362 menyebut delapan kolom Curated 'tidak tercentang' sekaligus 'tidak ada kolom yang dikecualikan'; spec mengasersi keduanya sebagai dua klausa terpisah.
  - TC-FA-LBL-365 menulis 'hover hierarki `IT Equipment > Laptop`' tanpa menyatakan target hover; spec menghover badge `Category`.
