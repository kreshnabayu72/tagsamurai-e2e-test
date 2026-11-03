---
id: TC-FA-LBL-E2E-169-jumlah-baris-format-sel-dan-truncation-badge-di-drawer-tagged-asset
title: "Jumlah Baris, Format Sel, dan Truncation Badge di Drawer Tagged Asset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-332
  - TC-FA-LBL-333
  - TC-FA-LBL-490
  - TC-FA-LBL-491
coverage:
  web: automated
---

# Jumlah Baris, Format Sel, dan Truncation Badge di Drawer Tagged Asset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. TC-FA-LBL-490 dan TC-FA-LBL-491 memakai Total Control `Company Extra` (Pre-setup #56), `Fixture.assetLabeling.akun.totalControlExtra`: akun, `{namaCompany}`, dan password belum ada, disediakan tim FE (pola Pre-setup #56 `totalControl_automated_{namaCompany}@qwertysystem.net`); ganti akun pada langkah 16.
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

- Data Pre-setup #30 (Company Extra, Pre-setup #56; hanya dibaca): label `Truncate Label` (warna tidak diasersi) terpasang pada aset `Truncate Asset - 24` dengan nilai panjang berikut:

  | Kolom | Nilai | Panjang |
  |---|---|---|
  | Brand | `International Business Machines` | 31 karakter |
  | Model/Type | `ThinkPad X1 Carbon Gen 11 Extended` | 34 karakter |
  | Group | `Head Office > Regional Distribution Center Jakarta Selatan` (badge memakai segmen terakhir `Regional Distribution Center Jakarta Selatan`) | 44 karakter |
  | Category | `IT Equipment > Enterprise Computing Hardware Devices` (badge memakai segmen terakhir `Enterprise Computing Hardware Devices`) | 37 karakter |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Drawer Tagged Asset (kolom `Category` ditampilkan lalu dipulihkan pada langkah 33 dengan menghapus centang `Category` lalu `[Save]`); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-LBL-332: Jumlah baris Drawer sama dengan Total Asset dan aset Deleted tidak tampil

1. Klik chip `Finance Department` di kolom Label
2. Verifikasi Drawer menampilkan 5 baris, sama dengan Total Asset `5` di Labels List
3. Verifikasi aset `Scanner Zebra - 6` (berstatus Deleted) tidak tampil
4. Verifikasi aset berstatus Draft (`Printer HP - 3`) tampil
5. Verifikasi aset berstatus Waiting for Approval (`Monitor LG - 4`) tampil
6. Verifikasi aset berstatus Disposed (`Projector Epson - 5`) tampil

### TC-FA-LBL-333: Format sel Drawer: Name, Brand, Group, Status, Last Updated, dan Name sebagai teks biasa

7. Verifikasi kolom Name `Laptop Dell - 1` (format `[Asset Name] - [Increment]`) berupa teks biasa
8. Verifikasi Brand `Dell` pada `Laptop Dell - 1` berupa badge Dark
9. Verifikasi Model/Type `Latitude 5440` pada `Laptop Dell - 1` berupa badge Dark
10. Verifikasi Group `Floor 1` pada `Laptop Dell - 1` berupa badge Primary
11. Verifikasi Status `Available` (`Laptop Dell - 1`) dan `Borrowed` (`Laptop Dell - 2`) sebagai badge
12. Verifikasi Last Updated mengikuti format General Settings
13. Klik teks Name `Laptop Dell - 1`
14. Verifikasi klik tidak membuka halaman lain (halaman Labels tetap aktif dan Drawer tetap terbuka)
15. Klik icon `[✕]` pada Drawer

### TC-FA-LBL-490: Badge Brand dan Model/Type lebih dari 25 karakter dipotong dan hover menampilkan nama penuh

16. Ganti akun: Logout, login sebagai Total Control Company Extra `Fixture.assetLabeling.akun.totalControlExtra` (password disediakan tim FE, lihat Prerequisites), buka Fixed Asset > Settings > Asset Master > tab `Labels`
17. Ketik Search `Truncate Label` di kotak Search Labels List, tekan Enter
18. Klik chip `Truncate Label` di kolom Label
19. Verifikasi badge Brand (Dark) pada `Truncate Asset - 24` menampilkan `Internationa..ess Machines`
20. Verifikasi badge Model/Type (Dark) pada `Truncate Asset - 24` menampilkan `ThinkPad X1 .. 11 Extended`
21. Hover badge Brand
22. Verifikasi tooltip menampilkan nama penuh `International Business Machines` tanpa hierarki
23. Hover badge Model/Type
24. Verifikasi tooltip menampilkan nama penuh `ThinkPad X1 Carbon Gen 11 Extended` tanpa hierarki

### TC-FA-LBL-491: Badge Group dan Category lebih dari 25 karakter dipotong dan hover menampilkan hierarki lengkap

25. Klik header kolom Actions (⋯) Drawer, lalu klik `Setup Column...`
26. Centang `Category`, lalu klik `[Save]`
27. Verifikasi badge Group (Primary) pada `Truncate Asset - 24` menampilkan `Regional Dis..arta Selatan`
28. Verifikasi badge Category (Primary) pada `Truncate Asset - 24` menampilkan `Enterprise C..ware Devices`
29. Hover badge Group
30. Verifikasi tooltip Group menampilkan `Head Office > Regional Distribution Center Jakarta Selatan`
31. Hover badge Category
32. Verifikasi tooltip Category menampilkan `IT Equipment > Enterprise Computing Hardware Devices`
33. Pulihkan konfigurasi kolom: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hilangkan centang `Category`, lalu klik `[Save]`
34. Tutup Drawer dengan `[✕]`, lalu klik `(←)` pada kotak Search Labels List

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup Drawer sebelum mencari label berikutnya; Search `Truncate Label` pada Labels List untuk menemukan baris target (label tambahan Pre-setup #30 mungkin tidak berada di halaman pertama); ganti akun ke Company Extra (langkah 16); pemulihan konfigurasi kolom (langkah 33); membersihkan Search Labels List di langkah terakhir. `[Save]` Setup Column adalah aksi sisi klien (bagian 8b butir 8).
- Langkah 7 sampai 14 (TC-FA-LBL-333) dilanjutkan pada Drawer yang sama dengan TC-FA-LBL-332 (satu pembukaan untuk TC tanpa perubahan state, bagian 3 prinsip 13 'halaman yang sama dipakai berulang').
- Pembagian TC lintas spec: TC-FA-LBL-327 sampai TC-FA-LBL-331 ada di spec 087; TC-FA-LBL-334, TC-FA-LBL-336, dan TC-FA-LBL-509 ada di spec 088.
- Temuan untuk QA:
  - TC-FA-LBL-490 dan TC-FA-LBL-491 hanya menyebut `Truncate Label` terpasang pada `Truncate Asset - 24`; Pre-setup #30 tidak menyebut warna label sehingga warna tidak diasersi.
  - Pre-setup #12 menyebut katalog Company Alpha tepat 9 label, sedangkan label `Truncate Label` (Pre-setup #30) berada di Company Extra (Pre-setup #56); baris label dicari lewat Search dan posisi halamannya ditentukan tim FE.
  - Pre-setup #56 belum memberi `{namaCompany}` dan password akun Total Control Company Extra (menunggu konfirmasi tim FE); spec memakai akun ini mulai langkah 16.
  - Rumus potong badge (12 huruf pertama, `..`, 12 huruf terakhir) mengacu ke TC-FA-LBL-490 dan TC-FA-LBL-491; contoh `Internationa..ess Machines` memuat spasi pada potongan akhir sesuai TC.
