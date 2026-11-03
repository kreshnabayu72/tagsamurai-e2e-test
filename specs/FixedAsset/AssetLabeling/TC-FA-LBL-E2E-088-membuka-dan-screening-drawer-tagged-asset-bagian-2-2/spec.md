---
id: TC-FA-LBL-E2E-088-membuka-dan-screening-drawer-tagged-asset-bagian-2-2
title: "Membuka dan Screening Drawer Tagged Asset (bagian 2/2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-334
  - TC-FA-LBL-336
  - TC-FA-LBL-373
  - TC-FA-LBL-374
  - TC-FA-LBL-509
coverage:
  web: automated
---

# Membuka dan Screening Drawer Tagged Asset (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Akun ganti: Total Control Company Extra (Pre-setup #56: salinan label Pre-setup #12 plus seed tambahan), `Fixture.assetLabeling.akun.totalControlExtra`. Nama company, email akun (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), dan nama env password belum ada, disediakan tim FE; tidak diisi di spec. Dipakai pada langkah 21 sampai 23 (ganti akun, S-07). Hook `after` suite mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Data Pre-setup #12 dan #13 (Company Alpha; hanya dibaca, tidak diubah). Label `Finance Department` (`#3B82F6`, Total Asset 5) memiliki lima aset aktif berikut; `Scanner Zebra - 6` (Deleted) terpasang label yang sama dan tidak dihitung:

  | Aset | Asset ID | Status | Brand | Model/Type | Group | Category | Label lain | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | `Laptop Dell - 1` | `AST-0001` | `Available` | `Dell` | `Latitude 5440` | `Head Office > Floor 1` | `IT Equipment > Laptop` | `High Priority` | 14 Sep 2026 09:00 |
  | `Laptop Dell - 2` | `AST-0002` | `Borrowed` | `Dell` | `Latitude 5440` | `Head Office > Floor 2` | `IT Equipment > Laptop` | - | 13 Sep 2026 09:00 |
  | `Printer HP - 3` | `AST-0003` | `Draft` | `HP` | `LaserJet Pro` | `Head Office` | `Printer` | `Audit Ready`, `Maintenance Due` | 12 Sep 2026 09:00 |
  | `Monitor LG - 4` | `AST-0004` | `Waiting for Approval` | `LG` | `UltraWide 34` | `Head Office` | `Monitor` | - | 11 Sep 2026 09:00 |
  | `Projector Epson - 5` | `AST-0005` | `Disposed` | `Epson` | `EB-X49` | `Warehouse` | `Projector` | - | 10 Sep 2026 09:00 |

- Data Pre-setup #32 (hanya dibaca, di Company Extra, Pre-setup #56): label `Empty Cell Label` (`#A855F7`) terpasang pada aset `Bare Asset - 26` (Active) tanpa Brand, Model/Type, dan Group.
- Fixture label: `Fixture.assetLabeling.labelFinanceDepartment` (`Finance Department`, Pre-setup #12), `Fixture.assetLabeling.labelEmptyCell` (`Empty Cell Label`, Pre-setup #32).
- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.
- Kemampuan teknis: `Spectra.intercept()` menahan respons data Tagged Asset pada langkah 15 dan melepasnya pada langkah 19 (hanya untuk mengamati state loading; bukan kegagalan yang dipaksa). Endpoint data Tagged Asset disediakan tim FE.

## Test Steps

### TC-FA-LBL-334: Hover badge Group menampilkan hierarki penuh dan Brand menampilkan nama penuh

1. Klik chip `Finance Department` di kolom Label
2. Hover badge Group `Floor 1` pada `Laptop Dell - 1`
3. Verifikasi tooltip Group menampilkan `Head Office > Floor 1`
4. Hover badge Brand `Dell`
5. Verifikasi tooltip Brand menampilkan `Dell`

### TC-FA-LBL-373: Toolbar Drawer hanya berisi Search dan Filter

6. Verifikasi toolbar berisi `Search` dan `Filter` saja
7. Verifikasi tidak ada Download, Changelog, atau tombol `[+ Label]` di toolbar dan header Drawer

### TC-FA-LBL-374: Tooltip icon Search, Filter, dan header Actions di Drawer

8. Hover icon Search
9. Verifikasi tooltip `Search`
10. Hover icon Filter
11. Verifikasi tooltip `Filter`
12. Hover header kolom Actions (⋯)
13. Verifikasi tooltip `Column Visibility`

### TC-FA-LBL-336: State loading Drawer menampilkan Shimmer

14. Klik icon `[✕]` pada Drawer
15. Tunda respons data Tagged Asset (tahan respons lewat `Spectra.intercept()`)
16. Klik chip `Finance Department` di kolom Label
17. Verifikasi area konten Drawer menampilkan Shimmer
18. Verifikasi header Drawer dan `[✕]` tetap tampil
19. Lepas tahanan respons data Tagged Asset dan tunggu baris Drawer selesai dimuat
20. Klik icon `[✕]` pada Drawer

### TC-FA-LBL-509: Sel kosong Brand, Model/Type, dan Group di Drawer Tagged Asset tampil —

21. Ganti akun: logout dari Total Control Company Alpha
22. Login sebagai Total Control Company Extra (`Fixture.assetLabeling.akun.totalControlExtra`)
23. Buka Fixed Asset > Settings > Asset Master > tab Labels
24. Ketik Search `Empty Cell Label` di kotak Search Labels List, tekan Enter
25. Klik `⋯` pada baris `Empty Cell Label`, lalu klik `Detail`
26. Verifikasi kolom Brand, Model/Type, dan Group pada baris `Bare Asset - 26` menampilkan `—`
27. Verifikasi kolom lain pada baris `Bare Asset - 26` tetap terisi
28. Tutup Drawer dengan `[✕]`, lalu klik `(←)` pada kotak Search Labels List

## Notes

- Mode: FE+BE (backend nyata; penahanan respons hanya untuk mengamati state loading, bagian 3 prinsip 13b). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4c (Drawer Tagged Asset).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec ini: TC-FA-LBL-334, TC-FA-LBL-373, dan TC-FA-LBL-374 memakai satu pembukaan Drawer (tanpa perubahan state); TC-FA-LBL-336 membutuhkan pembukaan baru dengan respons ditahan sehingga ditaruh sesudahnya; TC-FA-LBL-509 memakai label dan Drawer lain di Company Extra (ganti akun pada langkah 21 sampai 23, S-07) sehingga ditaruh terakhir.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup Drawer (langkah 15 didahului penutupan, langkah 19 diikuti penutupan); melepas tahanan respons dan menunggu baris dimuat (langkah 19); Search `Empty Cell Label` untuk menemukan baris target (label tambahan Pre-setup #32 mungkin tidak berada di halaman pertama); membersihkan Search Labels List di langkah terakhir.
- Pembagian TC lintas spec: TC-FA-LBL-327 sampai TC-FA-LBL-331 ada di spec 087; TC-FA-LBL-332 dan TC-FA-LBL-333 ada di spec 169; TC-FA-LBL-335 ada di spec 102.
- Temuan untuk QA:
  - TC-FA-LBL-336 menulis 'Tunda respons data Tagged Asset' tanpa menyebut endpoint atau cara menahan; spec memakai `Spectra.intercept()` pada permintaan data Tagged Asset yang disediakan tim FE (S-13).
  - TC-FA-LBL-509 menulis tanda strip panjang `—` pada judul skenario dan Expected; spec memakai karakter itu persis.
  - Company Extra (Pre-setup #56) memuat salinan label Pre-setup #12 plus seed tambahan; baris `Empty Cell Label` dicari lewat Search dan posisi halamannya ditentukan tim FE.
