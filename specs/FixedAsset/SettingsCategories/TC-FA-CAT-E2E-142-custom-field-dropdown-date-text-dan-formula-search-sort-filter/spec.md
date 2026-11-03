---
id: TC-FA-CAT-E2E-142-custom-field-dropdown-date-text-dan-formula-search-sort-filter
title: "Kolom Custom Field Tabel Assets: Dropdown, Date, serta Text dan Formula untuk Search, Sort, dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-689
  - TC-FA-CAT-690
  - TC-FA-CAT-692
coverage:
  web: automated
---

# Kolom Custom Field Tabel Assets: Dropdown, Date, serta Text dan Formula untuk Search, Sort, dan Filter

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 (CatMain, node `Laptop`, seed API) dan #56 (Custom Field, lisensi FA-7 aktif): General `Kondisi Fisik` (Dropdown, opsi `Baik` dan `Rusak Ringan`, Scope General; `Laptop Dell - 1` `Baik`, `Laptop Dell - 2` `Rusak Ringan`, `Laptop HP - 1` `Baik`), `Tanggal Inspeksi` (Date, Scope General; `Laptop Dell - 1` 2026-08-20), `Warna Casing` (Text, Scope Specific Asset Name `Laptop Dell`; `Laptop Dell - 1` `Silver`, `Laptop Dell - 2` tanpa nilai), dan `Skor Aset` (Formula, Scope General; dihitung saat dibaca). Disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-689: Custom Field Dropdown

3. Buka Setup Column lewat header kolom Actions (⋯), centang `Kondisi Fisik`, lalu klik `[Save]`
4. Ketik Search `rusak`, tekan Enter
5. Verifikasi `rusak` menemukan `Laptop Dell - 2`
6. Klik `(←)` pada kotak Search
7. Klik header Kondisi Fisik satu kali
8. Verifikasi Ascending A-Z (`Baik` sebelum `Rusak Ringan`)
9. Klik header Kondisi Fisik satu kali lagi
10. Verifikasi Descending kebalikan penuh
11. Klik header Kondisi Fisik satu kali lagi
12. Verifikasi urutan kembali Netral ke default Name A-Z
13. Klik icon Filter
14. Buka dropdown field Filter `Kondisi Fisik`
15. Verifikasi field `Kondisi Fisik` berupa multi-select searchable
16. Verifikasi opsi dropdown memuat nilai field `Baik` dan `Rusak Ringan`
17. Pilih `Baik`, lalu klik `[Apply]`
18. Verifikasi tabel menyisakan `Laptop Dell - 1` dan `Laptop HP - 1`
19. Klik icon Filter, tambahkan `Rusak Ringan` sehingga `Baik` dan `Rusak Ringan` terpilih, lalu klik `[Apply]`
20. Verifikasi tabel menyisakan `Laptop Dell - 1`, `Laptop Dell - 2`, dan `Laptop HP - 1` (OR)
21. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-CAT-690: Custom Field Date

22. Buka Setup Column, centang `Tanggal Inspeksi`, lalu klik `[Save]`
23. Klik header Tanggal Inspeksi satu kali
24. Verifikasi Ascending Oldest First dengan baris `—` mengikuti `prd-conventions.md` §9.7
25. Klik header Tanggal Inspeksi satu kali lagi
26. Verifikasi Descending Newest First dengan baris `—` mengikuti `prd-conventions.md` §9.7
27. Klik header Tanggal Inspeksi satu kali lagi
28. Verifikasi urutan kembali Netral ke default Name A-Z
29. Klik icon Filter
30. Verifikasi field Filter `Tanggal Inspeksi` berupa date range picker
31. Pilih rentang `Tanggal Inspeksi` 2026-08-01 sampai 2026-08-31, lalu klik `[Apply]`
32. Verifikasi hasil hanya `Laptop Dell - 1`
33. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
34. Ketik Search `2026-08-20`, tekan Enter
35. Verifikasi tidak ada hasil karena Data Type Date tidak dicari lewat Search
36. Klik `(←)` pada kotak Search

### TC-FA-CAT-692: Custom Field Text dan Formula

37. Buka Setup Column, centang `Warna Casing` dan `Skor Aset`, lalu klik `[Save]`
38. Ketik Search `Silver`, tekan Enter
39. Verifikasi `Silver` menemukan `Laptop Dell - 1` (Text dapat dicari)
40. Klik `(←)` pada kotak Search
41. Klik header Skor Aset
42. Verifikasi header `Skor Aset` tidak dapat diurutkan (tidak ada Sort dan urutan tabel tetap)
43. Ketik Search nilai yang tampil pada sel `Skor Aset` `Laptop Dell - 1`, tekan Enter
44. Verifikasi tidak ada hasil (Formula tidak dicari)
45. Klik `(←)` pada kotak Search
46. Klik icon Filter
47. Verifikasi Filter Panel memuat field `Tanggal Inspeksi`
48. Verifikasi Filter Panel tidak memuat field `Warna Casing` maupun `Skor Aset`

## Notes

- Mode: FE+BE. Spec melewati sekitar 35 langkah (nominal 48). Alasan: tiga TC memakai Popup Detail `Laptop` yang sama dan kolom Custom Field yang disiapkan di Setup Column terus dipakai; setiap TC mengulang tiga keadaan Sort dan satu Filter yang masing-masing punya `Verifikasi` (S-01).
- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah `(←)` pada Search, dan langkah `[Clear Field]` + `[Apply]` yang melepas Filter sebelum TC berikutnya.
- Kelompok tipe Multi-Dropdown, DateTime, serta Text Area/Phone/Email/URL/Document diwakili Dropdown, Date, dan Text pada fixture (TC-FA-CAT-689 Expected e, TC-FA-CAT-690 Expected d, TC-FA-CAT-692 Expected e); keterwakilan ini ketentuan fixture dan tidak diasersi.
- Temuan untuk QA:
  - TC-FA-CAT-692 langkah 5 menyebut "nilai yang tampil pada sel `Skor Aset`" tanpa nilai konkret karena Formula dihitung saat dibaca; spec membaca nilai sel saat dijalankan.
  - TC-FA-CAT-692 Expected d menyebut Filter Panel tidak memuat `Warna Casing` maupun `Skor Aset`; anchor positif (`Tanggal Inspeksi` memiliki Filter) ditambahkan spec tanpa disebut TC (butir 2 bagian 8b).
  - TC-FA-CAT-690 Expected a menyebut urutan Ascending/Descending tanpa memuat nilai pembanding; spec hanya mengasersi arah Oldest First dan Newest First sesuai TC.
