---
id: TC-FA-CAT-E2E-150-gerbang-asset-value-viewer-sort-filter-dan-no-access
title: "Gerbang Asset Value untuk Asset Value Viewer: Sel No access, Sort, dan Filter pada Asset Value dan Warranty Expiry"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-669
  - TC-FA-CAT-674
  - TC-FA-CAT-675
coverage:
  web: automated
---

# Gerbang Asset Value untuk Asset Value Viewer: Sel No access, Sort, dan Filter pada Asset Value dan Warranty Expiry

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Asset Value Viewer (Pre-setup #51) `assetValueViewer_automated_{namaCompany}@qwertysystem.net` (Manage Asset Master Data: R; Group Role View asset value hanya pada group `Head Office` beserta descendant; tanpa Manage purchase dan Manage accounting), client CatMain (Pre-setup #20), password `Spectra.env.FA_AV_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun Ganti akun (TC-FA-CAT-674 dan TC-FA-CAT-675): Purchase Group A (Pre-setup #53) `purchaseGroupA_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_PGA_PASSWORD`.
- Env var `FA_AV_PASSWORD` dan `FA_PGA_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 (CatMain, node `Laptop`, seed API): Asset Value (Commercial) `Laptop Dell - 1` 15000000.00, `Laptop Dell - 2` 0, `Laptop HP - 1` 7500000.00, `Laptop HP - 3` 20000000.00 (Group `Region Jawa > Jakarta Selatan Distribution Center`); `Laptop Dell - 3` Group `Head Office` tanpa nilai; Warranty Expiry `Laptop Dell - 1` 2027-03-15, `Laptop HP - 1` 2026-12-01, `Laptop HP - 3` 2027-06-30. Pre-setup #51 dan #53 disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-669: Gerbang Asset Value untuk pemegang View asset value pada group

3. Klik header Actions (⋯) > `Setup Column...`, centang `Asset Value` dan `Warranty Expiry`, lalu klik `[Save]`
4. Verifikasi sel Asset Value `Laptop Dell - 1` (Group `Head Office > Floor 1 > Room 301`) menampilkan nilainya (descendant `Head Office` termasuk)
5. Verifikasi sel Asset Value `Laptop Dell - 3` (Group `Head Office`, nilai belum ada) menampilkan `—` (berhak, nilai belum ada)
6. Klik kontrol halaman berikutnya
7. Verifikasi sel Asset Value `Laptop HP - 3` menampilkan `No access`
8. Hover sel `No access` pada `Laptop HP - 3`
9. Verifikasi hover menampilkan `Requires View asset value access in this group.`
10. Klik kontrol halaman sebelumnya
11. Verifikasi seluruh sel Warranty Expiry menampilkan `No access` (View asset value bukan hak Warranty)
12. Hover salah satu sel Warranty Expiry
13. Verifikasi hover menampilkan `Requires Manage purchase access in this group.`

### TC-FA-CAT-674: Sort Asset Value dan Warranty Expiry, baris No access paling akhir

14. Klik header Asset Value satu kali
15. Klik kontrol halaman berikutnya (halaman terakhir)
16. Verifikasi baris `Laptop HP - 3` (`No access`) berada paling akhir pada Asset Value Ascending
17. Klik header Asset Value satu kali lagi
18. Verifikasi baris `Laptop HP - 3` (`No access`) tetap paling akhir pada halaman terakhir Asset Value Descending
19. Ganti akun: login sebagai Purchase Group A, pilih node `Electronics`, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
20. Klik header Actions (⋯) > `Setup Column...`, centang `Warranty Expiry`, lalu klik `[Save]`
21. Klik header Warranty Expiry satu kali
22. Klik kontrol halaman berikutnya (halaman terakhir)
23. Verifikasi baris `Laptop HP - 3` (`No access`) paling akhir pada Warranty Expiry Ascending
24. Klik header Warranty Expiry satu kali lagi
25. Verifikasi baris `Laptop HP - 3` (`No access`) tetap paling akhir pada halaman terakhir Warranty Expiry Descending

### TC-FA-CAT-675: Filter Asset Value dan Warranty Expiry, baris No access tidak cocok

26. Klik header Warranty Expiry satu kali lagi hingga urutan Netral
27. Klik icon Filter, pilih rentang Warranty Expiry 2026-01-01 sampai 2027-12-31, lalu klik `[Apply]`
28. Verifikasi hasil Warranty Expiry memuat `Laptop HP - 1` dan `Laptop Dell - 1`
29. Verifikasi hasil Warranty Expiry tidak memuat `Laptop HP - 3` (`No access`)
30. Ganti akun: login sebagai Asset Value Viewer, pilih node `Electronics`, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
31. Klik icon Filter, isi Asset Value Min `0` dan Max `99999999`, lalu klik `[Apply]`
32. Verifikasi hasil Asset Value memuat baris Head Office yang bernilai (`Laptop Dell - 1`, `Laptop Dell - 2`, `Laptop HP - 1`)
33. Verifikasi hasil Asset Value tidak memuat `Laptop HP - 3` (`No access`) walau rentang mencakup seluruh nilai

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03, S-07, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah pindah ke halaman terakhir (langkah 6, 15, 22) sebelum asersi "paling akhir" dan kembali ke halaman 1 (langkah 10) (S-14; 12 aset dengan page size bawaan 10, mengganti sort tidak mengubah halaman), dan langkah Ganti akun; langkah mengembalikan Sort ke Netral sebelum Filter.
- Urutan TC-FA-CAT-675: asersi Warranty Expiry (Purchase Group A) didahulukan sebelum kembali ke Asset Value Viewer untuk menghemat satu pergantian akun; isi tiap Expected tidak diubah.
- Temuan untuk QA:
  - TC-FA-CAT-674 dan TC-FA-CAT-675 menyebut kolom `Asset Value` dan `Warranty Expiry` tetapi TC-FA-CAT-698 menetapkan dua kolom Asset Value; spec memakai `Asset Value` seperti tertulis di TC dengan menganggap kolom Commercial.
  - Setup Column kolom `Asset Value` pada TC-FA-CAT-675 diasumsikan masih tersimpan dari TC-FA-CAT-669 karena TC tidak menyebut centang ulang.
