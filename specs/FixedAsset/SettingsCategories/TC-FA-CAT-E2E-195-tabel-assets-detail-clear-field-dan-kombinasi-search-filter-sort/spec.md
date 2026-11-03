---
id: TC-FA-CAT-E2E-195-tabel-assets-detail-clear-field-dan-kombinasi-search-filter-sort
title: "Tabel Assets Popup Detail: Clear Field Filter serta Kombinasi Search, Filter, dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-592
coverage:
  web: automated
---

# Tabel Assets Popup Detail: Clear Field Filter serta Kombinasi Search, Filter, dan Sort

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Ketik Search `Laptop Dell`, tekan Enter
4. Klik icon Filter, pilih Brand `Dell`, lalu klik `[Apply]`
5. Klik header kolom Name hingga urutan Descending
6. Verifikasi hasil adalah irisan Search `Laptop Dell` dan Filter Brand `Dell` terurut Name menurun
7. Verifikasi titik indikator tampil pada icon Filter
8. Klik icon Filter untuk membuka Filter Panel, klik `[Clear Field]`
9. Verifikasi seluruh field Filter kosong
10. Klik `[Apply]`
11. Verifikasi Filter lepas dari tabel
12. Verifikasi titik indikator pada icon Filter hilang
13. Verifikasi Search `Laptop Dell` dipertahankan
14. Verifikasi Sort Name Descending dipertahankan
15. Klik icon Filter, pilih Brand `Dell`, lalu klik `[Apply]`
16. Klik `✕` pada kotak Search, tekan Enter
17. Verifikasi Filter Brand `Dell` dipertahankan
18. Verifikasi Sort Name Descending dipertahankan
19. Klik header kolom Name hingga urutan kembali netral ke default Name A-Z
20. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
21. Klik icon Filter, pilih Brand `Dell`, lalu klik `[Apply]`
22. Ketik Search `Laptop Dell`, tekan Enter
23. Verifikasi dataset sama dengan hasil Search lalu Filter pada langkah 6 (himpunan aset yang sama, terlepas dari urutan Sort)
24. Verifikasi keyword `Laptop Dell` tetap tampil pada kotak Search dan tidak tertimpa saat Filter diterapkan
25. Ganti isi kotak search dengan `zzzz`, tekan Enter
26. Verifikasi empty state `No results found` dengan `Try adjusting your search or filter.` tampil
27. Klik `✕` pada Search, tekan Enter
28. Verifikasi tabel pulih otomatis menampilkan hasil Filter Brand `Dell`

## Notes

- Mode: FE+BE. Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah yang mengembalikan Sort ke netral dan langkah yang membersihkan Filter sebelum menerapkan ulang Filter Brand `Dell` (Reset semua kontrol pada langkah 5 TC-FA-CAT-592).
- Temuan untuk QA:
  - TC-FA-CAT-592 Expected d menyatakan "dataset identik" antara urutan Filter lalu Search dan Search lalu Filter, tetapi hanya langkah 2 yang memakai Sort Name Descending; spec membandingkan himpunan aset, bukan urutan.
  - TC-FA-CAT-592 Expected c ("Mengosongkan Search mempertahankan Filter dan Sort") disusun sesudah Filter diterapkan ulang pada langkah 4 TC; spec mengikuti urutan itu.
