---
id: TC-FA-FAAM-E2E-199-total-assets-asset-value-commercial-fiscal-dua-kolom-tetap
title: "Tab Total Assets: Asset Value Dua Kolom Tetap Commercial dan Fiscal serta Not Depreciated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-823
  - TC-FA-FAAM-824
  - TC-FA-FAAM-825
coverage:
  web: automated
---

# Tab Total Assets: Asset Value Dua Kolom Tetap Commercial dan Fiscal serta Not Depreciated

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Full Value Access (Pre-setup #32e) `fullValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_FVA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Client `AutoDepreciation` (Pre-setup #37): salinan `Column Matrix Item` (Pre-setup #33, #33b) dengan `Asset Value (Commercial)` seperti Pre-setup #33b (`AST-2001` 15000000, `AST-2002` 0, `AST-2004` 5000000, `AST-2005` 20000000, `AST-2003` dan `AST-2006` tanpa harga perolehan) dan `Asset Value (Fiscal)`: `AST-2001` 9000000, `AST-2002` 0, `AST-2004` 4000000, `AST-2005` 25000000 (Asset Class `Not Depreciated` pada buku fiskal sehingga menampilkan harga perolehan), `AST-2003` dan `AST-2006` tanpa harga perolehan; Commercial `AST-2001` bermetode `Straight Line` masa manfaat 60 months. Login di hook `before` memakai akun Full Value Access pada client ini (disediakan tim FE; lihat Temuan untuk QA).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-824: Daftar kolom Asset Value tetap dua dan kedua kolom tetap tersembunyi hingga dicentang

1. Klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
2. Klik header Actions (⋯), pilih `Setup Column...`, amati baris Asset Value
3. Verifikasi Setup Column memuat tepat dua baris Asset Value: `Asset Value (Commercial)` lalu `Asset Value (Fiscal)`, keduanya `☐ Curated` (unchecked, enabled)
4. Verifikasi sebelum dicentang tidak ada kolom Asset Value di tabel
5. Centang hanya `Asset Value (Fiscal)`, klik `[Save]`
6. Verifikasi hanya `Asset Value (Fiscal)` tampil di tabel
7. Tutup popup Detail, klik nama `Column Matrix Item`, klik tab `Total Assets (6)`
8. Klik header Actions (⋯), pilih `Setup Column...`
9. Verifikasi daftar tetap dua baris Asset Value yang sama (tidak ada kolom tambahan)
10. Hapus centang `Asset Value (Fiscal)`, klik `[Save]`

### TC-FA-FAAM-823: Kolom Asset Value selalu dua kolom tetap berurutan Commercial lalu Fiscal, default tersembunyi

11. Amati header kolom tabel
12. Verifikasi pada kondisi default tidak ada kolom Asset Value di tabel
13. Klik header Actions (⋯), pilih `Setup Column...`, amati baris Asset Value
14. Verifikasi Setup Column memuat tepat dua baris `Asset Value (Commercial)` lalu `Asset Value (Fiscal)` (urutan tetap) di posisi antara `Last Scanned` dan `Warranty Expiry`, keduanya `☐ Curated` (unchecked, enabled)
15. Verifikasi tidak ada baris Asset Value lain
16. Centang kedua kolom Asset Value, klik `[Save]`
17. Verifikasi kedua kolom tampil di Live Preview dan tabel dengan header `Asset Value (Commercial)` lalu `Asset Value (Fiscal)` berurutan
18. Verifikasi `Commercial`: `AST-2001` 15000000, `AST-2004` 5000000
19. Verifikasi `Fiscal`: `AST-2001` 9000000, `AST-2004` 4000000
20. Hover sel `AST-2001` pada kolom `Asset Value (Commercial)`
21. Verifikasi tooltip sel menampilkan metode dan masa manfaat `Straight Line · 60 months`

### TC-FA-FAAM-825: Aset Not Depreciated menampilkan harga perolehan pada kolom buku itu, bukan strip

22. Amati kedua kolom pada keenam baris
23. Verifikasi `Asset Value (Fiscal)`: `AST-2001` 9000000, `AST-2002` currency nol, `AST-2004` 4000000, `AST-2005` 25000000 (harga perolehan karena Asset Class `Not Depreciated` pada buku fiskal, bukan `—`)
24. Verifikasi `AST-2003` dan `AST-2006` (tanpa harga perolehan) menampilkan `—` pada `Asset Value (Fiscal)`
25. Verifikasi `Asset Value (Commercial)`: `AST-2001` 15000000, `AST-2002` currency nol, `AST-2004` 5000000, `AST-2005` 20000000
26. Verifikasi `AST-2003` dan `AST-2006` menampilkan `—` pada `Asset Value (Commercial)`
27. Verifikasi tidak ada sel `No access` karena aktor berhak atas seluruh baris

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 824, 823, 825 (824 mengasersi daftar default dan mencentang Fiscal saja lalu mengembalikannya; 823 dan 825 melanjutkan dengan kedua kolom tercentang. Blok TC-FA-FAAM-825 memakai konfigurasi kolom yang disimpan blok TC-FA-FAAM-823, sehingga langkah mencentang kedua kolom (LK 3 TC-825) dihapus agar tidak membatalkan centang).
- Langkah penghubung: menghapus centang kolom di akhir blok TC-FA-FAAM-824, mengamati header, dan menutup popup Detail untuk membuka kembali tab.
- Temuan untuk QA:
  - Pre-setup #37 menyebut Client `AutoDepreciation` tetapi tidak memberi email akun Full Value Access/Asset Value HO pada client itu; spec memakai akun Full Value Access pada client tersebut yang disediakan tim FE.
  - TC-FA-FAAM-825 mengasersi `Not Depreciated` pada buku fiskal; TC tidak menyebut cara membaca Asset Class di UI selain nilai sel.
