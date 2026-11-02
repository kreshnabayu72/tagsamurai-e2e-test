---
id: TC-FA-CAT-E2E-136-tabel-assets-detail-download-cakupan-dan-transformasi-data
title: "Tabel Assets Popup Detail: Download Cakupan Baris dan Kolom serta Transformasi Data pada Berkas Export"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-593
  - TC-FA-CAT-613
coverage:
  web: automated
---

# Tabel Assets Popup Detail: Download Cakupan Baris dan Kolom serta Transformasi Data pada Berkas Export

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #40 (CatMain, node `Laptop`): label aset dibuat di Settings > Asset Master > Labels: `Laptop Dell - 1` label `Fragile`; `Laptop Dell - 2` label `Fragile` dan `Priority`; `Laptop Dell - 3` label `Fragile`, `Priority`, `Insured`, dan `Outdoor`; `Laptop HP - 1` label `Bulky`; aset lain tanpa label. Disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- Kemampuan teknis: membaca isi berkas unduhan CSV dan XLSX (nama berkas, kolom, jumlah dan isi baris, nilai sel); disediakan tim FE.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-593: Cakupan baris, kolom mengikuti Column Visibility, hasil nol baris, dan urutan Sort

3. Klik Download > `Download as CSV` tanpa Search dan Filter (pagination 10)
4. Verifikasi berkas `Category-Assets.csv` terunduh
5. Buka berkas `Category-Assets.csv`
6. Verifikasi berkas memuat seluruh 12 aset (bukan hanya 10 baris halaman aktif)
7. Ketik Search `Laptop HP`, tekan Enter
8. Klik Download > `Download as CSV`
9. Buka berkas yang terunduh
10. Verifikasi berkas hanya memuat 4 aset `Laptop HP - 1` sampai `Laptop HP - 4`
11. Klik `(←)` pada kotak Search
12. Buka Setup Column lewat header kolom Actions (⋯), hilangkan centang kolom `Brand`, lalu klik `[Save]`
13. Klik Download > `Download as CSV`
14. Verifikasi tidak ada toast atau peringatan
15. Buka berkas yang terunduh
16. Verifikasi berkas tidak memuat kolom `Brand`
17. Buka Setup Column, munculkan kembali kolom `Brand`, lalu klik `[Save]`
18. Klik Download > `Download as CSV`
19. Buka berkas yang terunduh
20. Verifikasi kolom `Brand` kembali ikut ter-export
21. Ketik Search `tidak-ada-xyz`, tekan Enter
22. Verifikasi tombol Download tetap aktif
23. Klik Download > `Download as CSV`
24. Verifikasi tidak ada toast
25. Buka berkas yang terunduh
26. Verifikasi berkas hanya berisi baris header kolom yang visible tanpa baris data
27. Klik `(←)` pada kotak Search
28. Klik header kolom Name hingga urutan Descending
29. Klik Download > `Download as XLSX`
30. Buka berkas `Category-Assets.xlsx`
31. Verifikasi baris berkas berurut Name menurun mengikuti Sort aktif

### TC-FA-CAT-613: Transformasi data badge, Brand/Model/Group, kosong, dan kolom +N more di berkas export

32. Klik header kolom Name hingga urutan kembali netral ke default Name A-Z
33. Buka Setup Column, centang kolom `Label`, lalu klik `[Save]`
34. Klik Download > `Download as XLSX`
35. Buka berkas `Category-Assets.xlsx`
36. Verifikasi sel Status multi-badge `Borrowed` + `Damaged` ditulis label teks apa adanya dipisah koma+spasi `Borrowed, Damaged` tanpa informasi warna
37. Verifikasi Brand dan Model/Type ditulis nama penuh tanpa pemotongan (`Hewlett Packard Enterprise Indonesia`, `Elite Dragonfly G3 Notebook PC`)
38. Verifikasi Group ditulis hierarki penuh dari root (`Head Office > Floor 1 > Room 301`, `Region Jawa > Jakarta Selatan Distribution Center`)
39. Verifikasi sel kosong `Laptop HP - 4` pada Brand, Model/Type, dan Group ditulis `-` (bukan blank, `—`, atau `null`)
40. Verifikasi sel Label `Laptop Dell - 3` menulis keempat label (`Fragile`, `Priority`, `Insured`, `Outdoor`) penuh dipisah koma+spasi, bukan `+N more`
41. Verifikasi Last Updated mengikuti Date Format dan Time Format General Settings

## Notes

- Mode: FE+BE. Spec melewati sekitar 35 langkah (nominal 41). Alasan: dua TC yang sama-sama membaca isi berkas export dari tabel Assets Popup Detail yang dibuka sekali; pecahan per TC memaksa membuka Popup Detail dan menyiapkan kolom ulang tanpa memperbaiki isolasi.
- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah `(←)` pada Search (menutup Search dua kali), langkah membuka dan menyimpan Setup Column untuk kolom `Brand` dan `Label`, serta langkah mengembalikan Sort ke netral sebelum TC-FA-CAT-613.
- Tanpa toast pada unduhan (langkah 14 dan 24) diasersi segera setelah klik Download dan sebelum `Verifikasi` isi berkas; klik format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas (langkah 16 dan 26; pada hasil nol baris berupa header berkas) (bagian 8b butir 11 dan butir 5).
- Temuan untuk QA:
  - TC-FA-CAT-593 langkah 4 menggabungkan dua unduhan (kolom `Brand` dihilangkan lalu dimunculkan kembali) dalam satu langkah; spec memisahkannya menjadi dua unduhan.
  - TC-FA-CAT-613 Expected f ("Last Updated mengikuti Date Format dan Time Format General Settings") tidak menyebut sel atau baris yang diperiksa; spec memeriksa kolom Last Updated pada berkas.
  - TC-FA-CAT-593 dan TC-FA-CAT-613 berlabel HINT `f` (binary buffer) dan berada di spec fungsional yang sama dengan TC lain.
