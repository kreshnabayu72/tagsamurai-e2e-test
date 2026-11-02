---
id: TC-FA-CAT-E2E-140-kolom-transactional-policy-ikon-sort-filter-dan-search-nama-transaksi
title: "Kolom Transactional Policy Tabel Assets: Ikon Transaksi On, Sort 3-State, Filter, dan Search Nama Transaksi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-656
  - TC-FA-CAT-657
  - TC-FA-CAT-683
coverage:
  web: automated
---

# Kolom Transactional Policy Tabel Assets: Ikon Transaksi On, Sort 3-State, Filter, dan Search Nama Transaksi

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 (CatMain, seed API): Policy Transaksi Asset Name `Laptop Dell` Borrow On dan Assign On (Self Service Borrow dan Transfer Off), `Laptop HP` hanya Transfer On, `Office Chair` (node `Furniture`) semua Off. Disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-656: Kolom Transactional Policy curated Hidden default dan ikon hanya transaksi On

3. Verifikasi kolom `Transactional Policy` tidak ada di header tabel
4. Buka Setup Column lewat header kolom Actions (⋯)
5. Verifikasi checkbox kolom `Transactional Policy` ☐ unchecked tetapi enabled
6. Centang kolom `Transactional Policy`, lalu klik `[Save]`
7. Verifikasi sel Transactional Policy `Laptop Dell - 1` menampilkan ikon Borrow lalu ikon Assign (urutan tetap Borrow, Self Service Borrow, Assign, Transfer; hanya yang On)
8. Verifikasi sel Transactional Policy `Laptop HP - 1` menampilkan satu ikon Transfer
9. Hover ikon Borrow pada `Laptop Dell - 1`
10. Verifikasi hover menampilkan nama transaksi `Borrow`
11. Hover ikon Assign pada `Laptop Dell - 1`
12. Verifikasi hover menampilkan nama transaksi `Assign`
13. Klik icon close (✕) pada Popup Detail
14. Pilih node `All Categories` di Sidebar Category Tree
15. Klik elipsis (⋯) pada baris `Furniture` > `Detail`
16. Verifikasi sel Transactional Policy aset ber-Asset Name `Office Chair` (semua policy Off) menampilkan `—`

### TC-FA-CAT-657: Sort 3-state dan Filter kolom Transactional Policy

17. Klik icon close (✕) pada Popup Detail
18. Pilih node `Electronics` di Sidebar Category Tree
19. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
20. Klik header Transactional Policy satu kali
21. Verifikasi Ascending alfabetis atas label ikon: 8 aset `Laptop Dell` (`Assign, Borrow`) sebelum 4 aset `Laptop HP` (`Transfer`)
22. Klik header Transactional Policy satu kali lagi
23. Verifikasi Descending kebalikan penuh
24. Klik header Transactional Policy satu kali lagi
25. Verifikasi urutan kembali Netral ke default Name A-Z
26. Klik icon Filter
27. Verifikasi field `Transactional Policy` dengan placeholder `All transactions` tampil di Filter Panel
28. Buka dropdown field `Transactional Policy`
29. Verifikasi field berupa multi-select searchable
30. Verifikasi opsi tetap empat transaksi (`Borrow`, `Self Service Borrow`, `Assign`, `Transfer`) walau tidak semuanya On pada data tabel
31. Pilih `Transfer`, lalu klik `[Apply]`
32. Verifikasi tabel menyisakan 4 aset `Laptop HP`
33. Klik icon Filter, ganti pilihan menjadi `Borrow` saja, lalu klik `[Apply]`
34. Verifikasi tabel menyisakan 8 aset `Laptop Dell`
35. Klik icon Filter, pilih `Transfer` dan `Borrow`, lalu klik `[Apply]`
36. Verifikasi tabel menyisakan seluruh 12 aset (OR)
37. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-CAT-683: Search kolom Transactional Policy mencocokkan nama transaksi pada ikon On

38. Ketik Search `borrow`, tekan Enter
39. Verifikasi tabel menemukan 8 aset `Laptop Dell - 1` sampai `Laptop Dell - 8`
40. Klik `(←)` pada kotak Search
41. Ketik Search `transfer`, tekan Enter
42. Verifikasi tabel menemukan 4 aset `Laptop HP - 1` sampai `Laptop HP - 4`
43. Klik `(←)` pada kotak Search
44. Ketik Search `self service`, tekan Enter
45. Verifikasi tidak ada hasil karena Self Service Borrow Off dan ikonnya tidak tampil

## Notes

- Mode: FE+BE. Spec melewati sekitar 35 langkah (nominal 45). Alasan: tiga TC memakai kolom `Transactional Policy` yang disiapkan sekali pada TC-FA-CAT-656 dan Popup Detail `Laptop` yang sama; langkah di atas 35 berasal dari butir Expected bermajemuk (S-01), bukan pembukaan berulang.
- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah menutup Popup Detail, memilih node, dan membuka Popup Detail `Laptop` (termasuk langkah 17), langkah `[Clear Field]` sebelum TC-FA-CAT-683, dan langkah `(←)` pada Search.
- Bentuk ikon final tidak diasersi (TC-FA-CAT-656 Expected f; Open Item `asset.md` #5, NC-23).
- Temuan untuk QA:
  - TC-FA-CAT-657 Expected a menyebut sel `—` mengikuti `prd-conventions.md` §9.7, tetapi seluruh 12 aset `Laptop` memiliki ikon sehingga tidak ada baris `—` pada data ini; klausa itu tidak diasersi.
  - TC-FA-CAT-657 langkah 5 sampai 7 mengganti pilihan tanpa menyebut membersihkan pilihan sebelumnya; spec mengganti pilihan eksplisit.
  - TC-FA-CAT-656 langkah 5 membuka `Furniture` lewat Popup Detail tanpa menyebut node yang dipilih; spec memilih `All Categories`.
