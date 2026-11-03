---
id: TC-FA-LBL-E2E-069-setup-column-labels-list-overlay-popup-dan-ceklis
title: "Setup Column Labels List: Overlay, Popup, dan Ceklis Kolom Hideable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-255
  - TC-FA-LBL-256
  - TC-FA-LBL-257
coverage:
  web: automated
---

# Setup Column Labels List: Overlay, Popup, dan Ceklis Kolom Hideable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Color Hex | Total Asset | Modified By |
  |---|---|---|---|
  | `High Priority` | `#EF4444` | 3 | `Sarah J` |
  | `Finance Department` | `#3B82F6` | 5 | `David K` |
  | `Audit Ready` | `#10B981` | 2 | `Sarah J` |
  | `Executive Asset` | `#8B5CF6` | 1 | `Michael W` |
  | `Maintenance Due` | `#F59E0B` | 4 | `David K` |
  | `Seasonal Event` | `#EC4899` | 0 | `Michael W` |
  | `Night Shift` | `#1E3A8A` | 0 | `Sarah J` |
  | `Warehouse Priority` | `#0EA5E9` | 0 | `Sarah J` |
  | `Field Kit` | `#84CC16` | 2 | `David K` |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global yang diubah: konfigurasi kolom Setup Column Labels List (diubah dan dipulihkan oleh langkah spec); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4).
- Kolom Hideable (TC-FA-LBL-257, urutan iterasi sesuai tabel):

  | Kolom |
  |---|
  | `Label` |
  | `Color Hex` |
  | `Total Asset` |
  | `Modified By` |


## Test Steps

### TC-FA-LBL-255: Screening overlay Column Visibility Labels List

1. Klik header kolom Actions (⋯)
2. Verifikasi overlay memuat daftar kolom `Label`, `Color Hex`, `Total Asset`, `Modified By`, `Last Updated`
3. Verifikasi tiap kolom pada overlay memiliki checkbox tercentang dan enabled (Hideable)
4. Verifikasi tiap kolom pada overlay memiliki drag handle
5. Verifikasi di bagian bawah overlay ada item `Setup Column...`

### TC-FA-LBL-256: Screening Popup Setup Column dan Preview Table (3 zona)

6. Klik `Setup Column...`
7. Verifikasi Zona Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan tombol Close `[✕]`
8. Verifikasi Zona Body: lima kolom `Label`, `Color Hex`, `Total Asset`, `Modified By`, `Last Updated` tercentang dengan drag handle dan icon Pin
9. Verifikasi Zona Body: Live Preview menampilkan urutan header dan isi sel
10. Verifikasi Zona Footer: `[Reset to Default]` (Text, Primary) dan `[Save]` (Filled, Success)
11. Verifikasi tidak ada `[Cancel]` pada Zona Footer

### TC-FA-LBL-257: Setup Column: ceklis dan unceklis kelas kolom Hideable

12. Untuk setiap baris tabel Kolom Hideable (langkah 12 sampai 13): hapus centang kolom pada baris itu di daftar Setup Column
13. Verifikasi kolom pada baris itu langsung hilang dari Live Preview
14. Verifikasi hanya `Last Updated` yang tersisa di Live Preview
15. Untuk setiap baris tabel Kolom Hideable (langkah 15 sampai 16): centang kembali kolom pada baris itu di daftar Setup Column
16. Verifikasi kolom pada baris itu muncul kembali di Live Preview pada posisi semula
17. Hapus centang `Last Updated`
18. Verifikasi `Last Updated` hilang dari Live Preview
19. Klik `[Save]`
20. Verifikasi tabel memuat `Label`, `Color Hex`, `Total Asset`, `Modified By` tanpa `Last Updated`
21. Tekan F5
22. Verifikasi tabel tetap memuat `Label`, `Color Hex`, `Total Asset`, `Modified By` tanpa `Last Updated` setelah F5
23. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
24. Centang `Last Updated`
25. Klik `[Save]`
26. Verifikasi `Last Updated` tampil kembali di tabel

## Notes

- Mode: FE+BE (backend nyata; konfigurasi kolom tersimpan di browser). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Spec ini 26 langkah nominal dan 38 langkah setelah ekspansi (di atas smell 35 langkah; langkah 12 sampai 13 dan 15 sampai 16 diulang untuk empat baris tabel Kolom Hideable, bagian 8b butir 7). Alasan: seluruh blok adalah screening dan ceklis Setup Column Labels List pada popup dan dataset yang sama; ekspansi berasal dari iterasi per kolom yang prosedurnya identik, bukan dari alur yang berbeda.
- Overlay Column Visibility dibiarkan terbuka dari TC-FA-LBL-255 ke langkah `Klik Setup Column...` TC-FA-LBL-256, dan popup Setup Column dari TC-FA-LBL-256 dipakai TC-FA-LBL-257, sehingga langkah pembuka `Klik header kolom Actions (⋯) lalu klik Setup Column...` TC-FA-LBL-257 terpenuhi oleh langkah 1 dan 6.
- Langkah 23 sampai 25 (centang kembali `Last Updated` lalu simpan) adalah butir terakhir TC-FA-LBL-257 sendiri, bukan langkah penghubung.
- Temuan untuk QA:
  - TC-FA-LBL-257 Expected b menyebut kolom muncul "pada posisi semula" tanpa memerinci posisi; spec mengasersi posisi sama dengan urutan awal lima kolom.
