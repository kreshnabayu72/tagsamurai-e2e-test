---
id: TC-FA-CAT-E2E-151-gerbang-asset-value-download-no-access-kedua-kolom-dan-respons-server
title: "Gerbang Asset Value: Download Sel No access, Gerbang pada Kedua Kolom Asset Value, dan Respons Server Tanpa Nilai"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-677
  - TC-FA-CAT-701
  - TC-FA-CAT-681
coverage:
  web: automated
---

# Gerbang Asset Value: Download Sel No access, Gerbang pada Kedua Kolom Asset Value, dan Respons Server Tanpa Nilai

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Asset Value Viewer (Pre-setup #51) `assetValueViewer_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_AV_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun Ganti akun (TC-FA-CAT-681): Purchase Group A (Pre-setup #53) `purchaseGroupA_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_PGA_PASSWORD`.
- Env var `FA_AV_PASSWORD` dan `FA_PGA_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55, #56, #59 (CatMain, node `Laptop`, seed API): Asset Value `Laptop Dell - 1` 15000000.00 (Fiscal 12000000.00), `Laptop Dell - 3` belum ada nilai, `Laptop HP - 3` 20000000.00 (Group `Region Jawa > Jakarta Selatan Distribution Center`), Warranty Expiry `Laptop HP - 3` 2027-06-30, Custom Field `Nomor PO` `Laptop HP - 3` `PO-0099`. Disediakan tim FE.
- Kemampuan teknis: membaca isi berkas unduhan XLSX; Spectra.intercept untuk membaca (tanpa mengubah) respons data tabel Assets; disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-677: Download sel No access

3. Klik header Actions (⋯) > `Setup Column...`, centang `Asset Value` dan `Warranty Expiry`, lalu klik `[Save]`
4. Klik Download > `Download as XLSX`
5. Verifikasi berkas `Category-Assets.xlsx` terunduh
6. Buka berkas `Category-Assets.xlsx`
7. Verifikasi Asset Value `Laptop Dell - 1` ditulis nilai numerik asli (`15000000`)
8. Verifikasi Asset Value `Laptop HP - 3` ditulis teks `No access`
9. Verifikasi Asset Value `Laptop Dell - 3` ditulis `-` (bukan `No access`)
10. Verifikasi seluruh sel Warranty Expiry ditulis teks `No access`

### TC-FA-CAT-701: Gerbang No access pada kedua kolom Asset Value

11. Buka Setup Column, centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
12. Verifikasi `Laptop Dell - 1` menampilkan nilai pada kedua kolom
13. Verifikasi `Laptop Dell - 3` menampilkan `—` pada kedua kolom (berhak, tidak ada nilai)
14. Klik kontrol halaman berikutnya
15. Verifikasi `Laptop HP - 3` menampilkan `No access` pada kedua kolom, bukan `—` atau harga perolehan pada kolom `Fiscal`
16. Hover sel `No access` pada kolom `Asset Value (Commercial)`
17. Verifikasi hover menampilkan `Requires View asset value access in this group.`
18. Hover sel `No access` pada kolom `Asset Value (Fiscal)`
19. Verifikasi hover menampilkan `Requires View asset value access in this group.`
20. Klik kontrol halaman sebelumnya

### TC-FA-CAT-681: Respons server tidak memuat nilai sel No access

21. Pasang intercept pada respons data tabel Assets
22. Muat ulang Popup Detail `Laptop` dengan kolom `Asset Value` dan `Warranty Expiry` tampil
23. Verifikasi UI menampilkan `No access` pada `Laptop HP - 3`
24. Verifikasi respons untuk `Laptop HP - 3` tidak memuat nilai Asset Value `20000000` dan tidak memuat nilai Warranty Expiry `2027-06-30`
25. Ganti akun: login sebagai Purchase Group A, pilih node `Electronics`, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
26. Klik header Actions (⋯) > `Setup Column...`, centang `Nomor PO` dan `Warranty Expiry`, lalu klik `[Save]`
27. Pasang intercept pada respons data tabel Assets dan muat ulang Popup Detail `Laptop`
28. Verifikasi UI menampilkan `No access` pada `Laptop HP - 3`
29. Verifikasi respons untuk `Laptop HP - 3` tidak memuat nilai `PO-0099` dan tidak memuat `2027-06-30`

## Notes

- Mode: FE+BE. Pengecualian K-1: TC-FA-CAT-681 dan TC-FA-CAT-701 (defense-in-depth) mengasersi respons API di samping tampilan UI; respons dibaca lewat intercept pengamat.
- Langkah penghubung (S-03, S-07, S-09): langkah 1 dan 2 (membuka Popup Detail), pindah halaman 2 dan kembali (S-14), memuat ulang Popup Detail, dan Ganti akun ke Purchase Group A.
- Temuan untuk QA:
  - TC-FA-CAT-677 menyebut kolom `Asset Value` tetapi TC-FA-CAT-698 menetapkan dua kolom Asset Value; spec TC-FA-CAT-677 memakai `Asset Value` seperti di TC.
  - TC-FA-CAT-681 langkah 3 menyebut "periksa objek baris" tanpa menyebut nama endpoint; spec mengintercept respons data tabel Assets tanpa menyebut endpoint (S-13).
  - TC-FA-CAT-681 Expected a/b mengasersi UI `No access` yang ditambahkan spec sebagai anchor positif pada respons; asersi nilai Warranty Expiry `2027-06-30` mengikuti Data TC.
