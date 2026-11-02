---
id: TC-FA-CAT-E2E-149-asset-value-fiscal-not-depreciated-reset-default-dan-perubahan-real-time
title: "Kolom Asset Value Fiscal: Not Depreciated, Hidden Default setelah Reset to Default, dan Perubahan Policy serta Custom Field Real-Time"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-699
  - TC-FA-CAT-700
  - TC-FA-CAT-680
coverage:
  web: automated
---

# Kolom Asset Value Fiscal: Not Depreciated, Hidden Default setelah Reset to Default, dan Perubahan Policy serta Custom Field Real-Time

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Full Sensitive (Pre-setup #50) `fullSensitive_automated_{namaCompany}@qwertysystem.net` (Manage Asset Master Data: R; Group Role View asset value dan Manage purchase pada group `Head Office` dan `Region Jawa`; Global Role Manage accounting; lisensi FA-7 aktif), client CatMain (Pre-setup #20), password `Spectra.env.FA_FS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_FS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 dan #59 (CatMain, node `Laptop`, seed API): `Laptop HP - 3` Asset Class `Not Depreciated` pada buku Fiscal, harga perolehan 20000000.00, Asset Value (Commercial) 20000000.00; `Laptop Dell - 1` Asset Value (Commercial) 15000000.00.
- Data TC-FA-CAT-680 (sesi A Total Control, sesi B Principal Automation Pre-setup #11): Policy Transaksi `Laptop Dell` Borrow On dan Assign On (Transfer Off), Custom Field `Warna Casing` (Text, Scope `Laptop Dell`, Active), Pre-setup #55 dan #56. Perubahan sesi B: Transfer On pada policy Asset Name `Laptop Dell` dan `Warna Casing` Inactive.
- Akun sesi A pada TC-FA-CAT-680: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, env `Spectra.env.FA_TC_PASSWORD`, dipakai lewat langkah Ganti akun (S-07).
- Kemampuan teknis: Principal Automation mengubah policy transaksi dan status Custom Field lewat sesi API aktor (butir hook suite "Sesi API aktor"); pemulihan policy Transfer Off dan `Warna Casing` Active dilakukan di hook `after`; disediakan tim BE/FE.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-700: Kedua kolom Asset Value Hidden default dan urutan tetap setelah Reset to Default

3. Klik header Actions (⋯) > `Setup Column...`
4. Verifikasi kedua kolom `Asset Value (Commercial)` dan `Asset Value (Fiscal)` ada dengan checkbox ☐ (Hidden) dan tidak tampil di tabel, urutan `Commercial` lalu `Fiscal`
5. Centang `Asset Value (Fiscal)` saja, lalu klik `[Save]`
6. Verifikasi hanya kolom `Asset Value (Fiscal)` tampil di tabel
7. Buka Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`
8. Buka kembali Setup Column
9. Verifikasi kedua kolom kembali ☐ Hidden dengan urutan tetap `Commercial` lalu `Fiscal`

### TC-FA-CAT-699: Aset Not Depreciated menampilkan harga perolehan

10. Centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
11. Klik kontrol halaman berikutnya
12. Verifikasi `Laptop HP - 3` menampilkan 20000000.00 pada kolom `Asset Value (Commercial)`
13. Verifikasi `Laptop HP - 3` menampilkan harga perolehan 20000000.00 pada kolom `Asset Value (Fiscal)`, bukan `—` dan bukan `No access`
14. Klik kontrol halaman sebelumnya

### TC-FA-CAT-680: Perubahan policy transaksi dan status Custom Field diperbarui real-time

15. Klik icon close (✕) pada Popup Detail
16. Ganti akun: login sebagai Total Control (sesi A), pilih node `Electronics`, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
17. Klik header Actions (⋯) > `Setup Column...`, centang `Transactional Policy` dan `Warna Casing`, lalu klik `[Save]`
18. Sesi B (Principal Automation) mengaktifkan Transfer pada policy Asset Name `Laptop Dell` lewat sesi API hingga tersimpan
19. Verifikasi sel Transactional Policy seluruh aset `Laptop Dell` menampilkan ikon Transfer tambahan setelah Borrow dan Assign tanpa muat ulang
20. Sesi B menonaktifkan Custom Field `Warna Casing` lewat sesi API hingga tersimpan
21. Verifikasi kolom `Warna Casing` hilang dari tabel tanpa muat ulang
22. Buka Setup Column
23. Verifikasi kolom `Warna Casing` hilang dari Setup Column

## Notes

- Mode: FE+BE. Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), dan langkah menutup Popup Detail serta Ganti akun ke Total Control. TC-FA-CAT-700 menguji `[Reset to Default]` sebagai aksi TC (bukan pemulihan).
- TC-FA-CAT-700 diurutkan sebelum TC-FA-CAT-699 supaya keadaan awal kolom Asset Value Hidden terbaca sebelum dicentang.
- Temuan untuk QA:
  - TC-FA-CAT-680 berlabel Manual Only (dua sesi paralel) tetapi sesi B hanya memicu perubahan state sehingga memakai sesi API (P-2); asersi real-time tanpa muat ulang bergantung pada mekanisme pembaruan yang tidak dijelaskan TC.
  - TC-FA-CAT-680 Expected a/b disusun tanpa langkah observasi Setup Column untuk `Warna Casing`; spec menambah `Verifikasi` Setup Column sesuai klausa "hilang dari tabel dan Setup Column".
  - Kolom ACC TC-FA-CAT-680 memuat #20 dan #11 sedangkan Precondition menyebut #50 dan #56; Precondition TC diikuti.
