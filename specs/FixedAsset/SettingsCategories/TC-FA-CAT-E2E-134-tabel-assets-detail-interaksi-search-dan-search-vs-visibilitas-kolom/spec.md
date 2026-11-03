---
id: TC-FA-CAT-E2E-134-tabel-assets-detail-interaksi-search-dan-search-vs-visibilitas-kolom
title: "Tabel Assets Popup Detail: Interaksi Search serta Search Terikat Visibilitas Kolom dan Filter Independen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-589
  - TC-FA-CAT-590
coverage:
  web: automated
---

# Tabel Assets Popup Detail: Interaksi Search serta Search Terikat Visibilitas Kolom dan Filter Independen

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-589: Interaksi Search: reveal, Enter, (✕), dan panah tutup

3. Hover icon Search di toolbar tabel Assets
4. Verifikasi tooltip icon `Search` tampil
5. Klik icon Search
6. Verifikasi input Search melebar (reveal)
7. Verifikasi kursor langsung fokus di input
8. Verifikasi placeholder `Search asset name, asset ID, brand...`
9. Ketik `Laptop Dell` tanpa menekan `Enter`
10. Verifikasi icon (✕) muncul pada input
11. Verifikasi tabel belum tersaring (tidak live-as-you-type) dan masih menampilkan 10 baris pada halaman 1
12. Tekan `Enter`
13. Verifikasi tabel hanya memuat 8 aset `Laptop Dell - 1` sampai `Laptop Dell - 8`
14. Klik icon (✕) pada input
15. Verifikasi input kosong
16. Verifikasi tabel masih memuat 8 aset `Laptop Dell - 1` sampai `Laptop Dell - 8` (hasil terakhir dipertahankan)
17. Tekan `Enter` pada input kosong
18. Verifikasi tabel kembali memuat seluruh 12 aset
19. Ketik Search `Laptop HP`, tekan Enter
20. Klik icon panah (←) di kiri toolbar
21. Verifikasi kotak pencarian menutup menjadi icon Search biasa
22. Verifikasi keyword kosong
23. Verifikasi tabel langsung memuat seluruh 12 aset tanpa menekan `Enter`

### TC-FA-CAT-590: Search terikat visibilitas kolom, Filter independen dari visibilitas kolom

24. Buka Setup Column lewat header kolom Actions (⋯), hilangkan centang kolom `Brand`, lalu klik `[Save]`
25. Ketik Search `Hewlett`, tekan Enter
26. Verifikasi empty state `No results found` dengan `Try adjusting your search or filter.` tampil karena keyword `Hewlett` tidak mencocokkan baris saat `Brand` di-hide
27. Buka Setup Column, centang kembali kolom `Brand`, lalu klik `[Save]`
28. Ganti isi kotak search dengan `Hewlett`, tekan Enter
29. Verifikasi keyword `Hewlett` mencocokkan satu aset ber-Brand `Hewlett Packard Enterprise Indonesia`
30. Klik `(←)` pada kotak Search
31. Buka Setup Column, hilangkan centang kolom `Group`, lalu klik `[Save]`
32. Klik icon Filter, pilih Group `Head Office > Floor 1 > Room 301`, lalu klik `[Apply]`
33. Klik icon Filter untuk membuka kembali Filter Panel
34. Verifikasi field Filter `Group` tetap ada di Filter Panel
35. Verifikasi nilai Group `Head Office > Floor 1 > Room 301` tetap ter-Apply
36. Verifikasi tabel hanya menampilkan aset ber-Group `Head Office > Floor 1 > Room 301` walau kolom `Group` disembunyikan

## Notes

- Mode: FE+BE. Spec melewati sekitar 35 langkah (nominal 36). Alasan: dua TC pada satu tabel Assets Popup Detail yang dibuka sekali; TC-FA-CAT-589 sendiri memuat lima butir Expected bermajemuk yang masing-masing dipecah menjadi `Verifikasi` per klausa (S-01).
- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah 20 dan langkah Search `(←)` sesudah `Hewlett` (menutup kotak Search), serta langkah yang membuka Setup Column untuk menampilkan kembali kolom `Brand`. Kolom `Group` yang disembunyikan dipulihkan hook `after`.
- Temuan untuk QA:
  - TC-FA-CAT-589 Expected e menyebut "tabel langsung memuat seluruh 12 aset" tanpa menyebut halaman; spec mengasersi 12 aset sebagai total (10 baris pada halaman 1).
  - TC-FA-CAT-590 langkah 6 menyebut "buka kembali Filter Panel" tanpa menjelaskan keadaan Filter Panel sesudah `[Apply]`; spec membuka ulang lewat icon Filter.
