---
id: TC-FA-LBL-E2E-087-membuka-dan-screening-drawer-tagged-asset-bagian-1-2
title: "Membuka dan Screening Drawer Tagged Asset (bagian 1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-327
  - TC-FA-LBL-328
  - TC-FA-LBL-329
  - TC-FA-LBL-330
  - TC-FA-LBL-331
coverage:
  web: automated
---

# Membuka dan Screening Drawer Tagged Asset (bagian 1/2)

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

- Pre-setup #12 (katalog Company Alpha): label `Finance Department` (`#3B82F6`, Total Asset 5) dipakai sebagai label uji; label lain hanya dibaca. Company Alpha memiliki dua buku Asset Value tetap `Commercial` dan `Fiscal` (precondition TC-FA-LBL-330).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.
- Kemampuan teknis: Drawer ditutup dengan `Esc` (langkah 33); tidak ada form dirty sehingga tidak ada dialog `Unsaved Changes`.

## Test Steps

### TC-FA-LBL-327: Membuka Drawer Tagged Asset lewat klik chip di kolom Label

1. Klik chip `Finance Department` di kolom Label
2. Verifikasi Drawer berjudul `Tagged Assets` terbuka
3. Verifikasi Drawer menampilkan lima aset label `Finance Department`
4. Klik icon `[✕]` pada Drawer

### TC-FA-LBL-328: Membuka Drawer Tagged Asset lewat klik angka di kolom Total Asset

5. Klik angka `5` di kolom Total Asset baris `Finance Department`
6. Verifikasi Drawer yang sama (berjudul `Tagged Assets`) terbuka
7. Verifikasi Drawer menampilkan lima aset label `Finance Department`
8. Klik icon `[✕]` pada Drawer

### TC-FA-LBL-329: Membuka Drawer Tagged Asset lewat row action Detail

9. Klik `⋯` pada baris `Finance Department`, lalu klik `Detail`
10. Verifikasi Drawer yang sama (berjudul `Tagged Assets`) terbuka
11. Verifikasi Drawer menampilkan lima aset label `Finance Department`
12. Klik icon `[✕]` pada Drawer

### TC-FA-LBL-330: Screening Drawer Tagged Asset (3 zona)

13. Klik chip `Finance Department` di kolom Label
14. Verifikasi Zona Header: Title `Tagged Assets` (flat, tanpa nama label)
15. Verifikasi Zona Header: tombol Close `[✕]` tampil
16. Verifikasi Zona Header: blok identitas berbentuk grid label:value berisi `Label` (chip `Finance Department`), `Color Hex` (`#3B82F6`), `Total Asset` (`5`)
17. Verifikasi Zona Header: toolbar `Search` dan `Filter` tampil
18. Verifikasi Zona Body: kolom `Name (sortable)`, `Asset ID (sortable)`, `TAG (sortable)`, `Brand (sortable)`, `Model/Type (sortable)`, `Group (sortable)`, `Status (sortable)`, `Last Updated (sortable)`, `Column Visibility (⋯)` (unsortable: header klik membuka overlay Column Visibility dengan CTA `[Setup Column]` di dalamnya)
19. Verifikasi Zona Body: lima baris tampil dengan default sort Name A-Z: `Laptop Dell - 1`, `Laptop Dell - 2`, `Monitor LG - 4`, `Printer HP - 3`, `Projector Epson - 5`
20. Verifikasi Zona Body: kolom Measurement, Category, Label, Transactional Policy, Last Scanned, Asset Value (Commercial), Asset Value (Fiscal), dan Warranty Expiry tersembunyi secara default
21. Verifikasi Zona Footer: pagination default 10
22. Verifikasi Zona Footer: tidak ada tombol aksi, tidak ada Download, tidak ada Changelog, dan tidak ada breadcrumb
23. Klik icon Search di toolbar Drawer
24. Verifikasi Zona Header: kotak Search berplaceholder `Search name, asset ID, brand...`
25. Klik icon `[✕]` pada Drawer

### TC-FA-LBL-331: Drawer ditutup hanya lewat ✕ atau Esc

26. Klik chip `Finance Department` di kolom Label
27. Klik area gelap di luar Drawer
28. Verifikasi Drawer tetap terbuka (klik backdrop tidak menutup Drawer)
29. Verifikasi tidak ada tombol teks `Close` di Drawer
30. Klik icon `[✕]` pada Drawer
31. Verifikasi Drawer tertutup
32. Klik chip `Finance Department` di kolom Label
33. Tekan Esc
34. Verifikasi Drawer tertutup

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup Drawer dengan `[✕]` sesudah tiap TC agar TC berikutnya membuka Drawer dari Labels List; membuka kotak Search toolbar sebelum `Verifikasi` placeholder (S-14: placeholder dicek saat input terbuka dan kosong).
- Urutan penyimpangan dari Expected TC-FA-LBL-330 (bagian 8b butir 5): `Verifikasi` placeholder Search diletakkan sesudah zona Footer karena membuka kotak Search mengubah toolbar; sesudahnya Drawer ditutup sehingga state Search tidak terbawa.
- Pembagian TC lintas spec: TC-FA-LBL-332 dan TC-FA-LBL-333 ada di spec 169; TC-FA-LBL-334 dan TC-FA-LBL-336 ada di spec 088; TC-FA-LBL-335 ada di spec 102.
- Temuan untuk QA:
  - TC-FA-LBL-330 Expected b menulis daftar kolom Body dalam satu sel dengan pemisah pipa dan keterangan `unsortable — header klik = buka overlay Column Visibility dengan CTA [Setup Column] di dalamnya`; spec mengasersi daftar kolom persis dan keterangan header Actions sebagai satu klausa, urutan kolom menurut TC.
  - TC-FA-LBL-330 menyebut toolbar `Search` (placeholder `Search name, asset ID, brand...`) tanpa menyatakan bahwa placeholder baru terlihat sesudah Search dibuka (TC-FA-LBL-493); spec membuka Search lebih dulu.
  - Pre-setup #12 menyebut katalog Company Alpha tepat 9 label, sedangkan Pre-setup #18, #22, #27 sampai #30, #32, dan #35 menambah label pada Company Alpha; spec mengklik chip label dasar langsung sesuai TC, posisi halaman label itu pada Labels List ditentukan tim FE.
