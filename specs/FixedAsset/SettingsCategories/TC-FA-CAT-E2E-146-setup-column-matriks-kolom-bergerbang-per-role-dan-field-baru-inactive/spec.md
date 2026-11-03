---
id: TC-FA-CAT-E2E-146-setup-column-matriks-kolom-bergerbang-per-role-dan-field-baru-inactive
title: "Setup Column Tabel Assets: Matriks Kolom Bergerbang per Role serta Custom Field Baru dan Inactive"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-673
  - TC-FA-CAT-678
coverage:
  web: automated
---

# Setup Column Tabel Assets: Matriks Kolom Bergerbang per Role serta Custom Field Baru dan Inactive

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Full Sensitive (Pre-setup #50) `fullSensitive_automated_{namaCompany}@qwertysystem.net` (Manage Asset Master Data: R; Group Role View asset value dan Manage purchase pada group `Head Office` dan `Region Jawa`; Global Role Manage accounting; lisensi FA-7 aktif), client CatMain (Pre-setup #20), password `Spectra.env.FA_FS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_FS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun role lain (client CatMain, Pre-setup #20), dipakai lewat langkah Ganti akun (S-07): Asset Value Viewer (Pre-setup #51) `assetValueViewer_automated_{namaCompany}@qwertysystem.net`, env `Spectra.env.FA_AV_PASSWORD`; Accounting Global (Pre-setup #52) `accountingGlobal_automated_{namaCompany}@qwertysystem.net`, env `Spectra.env.FA_ACCGL_PASSWORD`; Purchase Group A (Pre-setup #53) `purchaseGroupA_automated_{namaCompany}@qwertysystem.net`, env `Spectra.env.FA_PGA_PASSWORD`; Tanpa Hak Nilai Sensitif (Pre-setup #54) `noSensitive_automated_{namaCompany}@qwertysystem.net`, env `Spectra.env.FA_NOSENS_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Role yang diuji (parameter langkah 8 sampai 13):

| Role | Asset Value dan Warranty Expiry | Custom Field Purchasing (`Nilai Kontrak`, `Nomor Kontrak Dell`, `Nomor PO`) | Custom Field Accounting (`Kode Anggaran`) |
|---|---|---|---|
| Full Sensitive | tersedia | tersedia | tersedia |
| Asset Value Viewer | tersedia | tidak tersedia | tidak tersedia |
| Accounting Global | tersedia | tidak tersedia | tersedia |
| Purchase Group A | tersedia | tersedia | tidak tersedia |
| Tanpa Hak Nilai Sensitif | tersedia | tidak tersedia | tidak tersedia |

- Env var `FA_AV_PASSWORD`, `FA_ACCGL_PASSWORD`, `FA_PGA_PASSWORD`, dan `FA_NOSENS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #56 (Custom Field, lisensi FA-7 aktif): Purchasing `Nilai Kontrak`, `Nomor Kontrak Dell`, `Nomor PO`; Accounting `Kode Anggaran`; Inactive `Catatan Lama`. Disediakan tim FE.
- Kemampuan teknis (TC-FA-CAT-678): Principal Automation (Pre-setup #11) membuat dan mengubah status Custom Field lewat sesi API aktor (butir hook suite "Sesi API aktor", disediakan tim BE/FE). Custom Field milik spec: `Field Baru {runId}-146` (General); dihapus atau dinonaktifkan di hook `after`.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-673: Matriks ketersediaan kolom bergerbang di Setup Column per role

3. Klik header Actions (⋯) > `Setup Column...` pada role Full Sensitive
4. Verifikasi Asset Value dan Warranty Expiry tersedia di daftar Setup Column
5. Verifikasi kolom Custom Field Purchasing tersedia
6. Verifikasi kolom Custom Field Accounting tersedia
7. Klik icon close (✕) pada Popup Detail
8. Ganti akun: login sebagai role berikutnya pada tabel "Role yang diuji", pilih node `Electronics`, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
9. Klik header Actions (⋯) > `Setup Column...` dan catat daftar kolom bergerbang
10. Verifikasi Asset Value dan Warranty Expiry tersedia di daftar Setup Column
11. Verifikasi kolom Custom Field Purchasing sesuai kolom tabel (tersedia atau tidak tersedia)
12. Verifikasi kolom Custom Field Accounting sesuai kolom tabel (tersedia atau tidak tersedia)
13. Klik icon close (✕) pada Popup Detail

### TC-FA-CAT-678: Custom Field baru tampil sebagai kolom Hidden dan field yang menjadi Inactive hilang

14. Ganti akun: login sebagai Full Sensitive, pilih node `Electronics`, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
15. Klik header Actions (⋯) > `Setup Column...` dan catat daftar kolom Custom Field
16. Verifikasi daftar Setup Column tidak memuat `Field Baru {runId}-146`
17. Principal Automation membuat Custom Field General `Field Baru {runId}-146` (Active) lewat sesi API hingga tersimpan
18. Muat ulang Popup Detail `Laptop` dan buka Setup Column
19. Verifikasi `Field Baru {runId}-146` ada di daftar dengan checkbox ☐ (Hidden)
20. Verifikasi `Field Baru {runId}-146` tidak tampil di tabel
21. Principal Automation mengubah `Field Baru {runId}-146` menjadi Inactive lewat sesi API hingga tersimpan
22. Muat ulang Popup Detail `Laptop` dan buka Setup Column
23. Verifikasi `Field Baru {runId}-146` hilang dari daftar Setup Column
24. Verifikasi field Inactive `Catatan Lama` tetap tidak menjadi kolom

## Notes

- Mode: FE+BE. Langkah 8 sampai 13 diulang untuk empat role terakhir pada tabel (bagian 8b butir 7); role pertama (Full Sensitive) memakai langkah eksplisit karena login di hook `before`.
- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah menutup Popup Detail, dan langkah Ganti akun (termasuk kembali ke Full Sensitive sebelum TC-FA-CAT-678).
- Spec melewati sekitar 35 langkah dengan ekspansi (nominal 24). Alasan: satu TC sumber mengulang urutan identik per role dengan parameter pada tabel Prerequisites.
- Temuan untuk QA:
  - TC-FA-CAT-673 Expected d tidak punya langkah observasi terpisah dari Expected b dan c; spec mengasersi lewat kolom tabel role.
  - TC-FA-CAT-678 memakai nama `Field Baru` literal; spec memakai nama bersuffix per run (S-12).
  - Nama env var role (`FA_FS_PASSWORD`, `FA_AV_PASSWORD`, `FA_ACCGL_PASSWORD`, `FA_PGA_PASSWORD`, `FA_NOSENS_PASSWORD`) adalah usulan; TC tidak menyebut nama env var.
  - Plan menyebut pembagian TC-FA-CAT-673 dan TC-FA-CAT-678 ke spec ini; kolom ACC TC hanya memuat #20 dan #50 padahal TC-FA-CAT-673 memakai #51 sampai #54 dan TC-FA-CAT-678 memakai #11 (Precondition TC diikuti).
