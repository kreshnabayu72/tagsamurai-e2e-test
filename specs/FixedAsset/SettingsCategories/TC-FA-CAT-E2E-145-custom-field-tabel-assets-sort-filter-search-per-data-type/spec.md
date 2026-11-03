---
id: TC-FA-CAT-E2E-145-custom-field-tabel-assets-sort-filter-search-per-data-type
title: "Custom Field Tabel Assets: Sort, Search, dan Filter per Data Type, serta Filter Numeric/Percentage"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-667
  - TC-FA-CAT-691
coverage:
  web: automated
---

# Custom Field Tabel Assets: Sort, Search, dan Filter per Data Type, serta Filter Numeric/Percentage

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Full Sensitive (Pre-setup #50) `fullSensitive_automated_{namaCompany}@qwertysystem.net` (Manage Asset Master Data: R; Group Role View asset value dan Manage purchase pada group `Head Office` dan `Region Jawa`; Global Role Manage accounting; lisensi FA-7 aktif), client CatMain (Pre-setup #20), password `Spectra.env.FA_FS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_FS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #56 (Custom Field, lisensi FA-7 aktif): General `Warna Casing` (Text, Scope Specific Asset Name `Laptop Dell`; `Laptop Dell - 1` `Silver`), `Rasio Pemakaian` (Percentage; `Laptop Dell - 1` 80, `Laptop HP - 1` 20); Purchasing `Nilai Kontrak` (Number; `Laptop Dell - 1` 5000, `Laptop Dell - 2` 0, `Laptop HP - 1` 250); Accounting `Kode Anggaran` (Text; `Laptop Dell - 1` `ANG-01`, `Laptop HP - 1` `ANG-02`). Disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-667: Sort per Data Type, Search nilai, dan Filter hanya untuk Data Type yang berfilter

3. Buka Setup Column lewat header kolom Actions (⋯), centang `Warna Casing`, `Nilai Kontrak`, dan `Kode Anggaran`, lalu klik `[Save]`
4. Klik header Nilai Kontrak satu kali
5. Verifikasi Sort numerik Ascending 0 (`Laptop Dell - 2`), 250 (`Laptop HP - 1`), 5000 (`Laptop Dell - 1`), lalu baris `—` di akhir
6. Klik header Nilai Kontrak satu kali lagi
7. Verifikasi Descending kebalikan penuh
8. Klik header Nilai Kontrak satu kali lagi
9. Verifikasi urutan kembali Netral ke default Name A-Z
10. Klik header Warna Casing satu kali
11. Verifikasi Sort `Warna Casing` alfabetis A-Z
12. Klik header Warna Casing hingga urutan kembali Netral ke default Name A-Z
13. Ketik Search `Silver`, tekan Enter
14. Verifikasi `Silver` menemukan `Laptop Dell - 1`
15. Ganti isi kotak search dengan `ANG-02`, tekan Enter
16. Verifikasi `ANG-02` menemukan `Laptop HP - 1`
17. Klik `(←)` pada kotak Search
18. Klik icon Filter
19. Verifikasi Filter Panel memuat field `Nilai Kontrak` berupa range Min-Max
20. Verifikasi Filter Panel tidak memuat field `Warna Casing` dan `Kode Anggaran` (Text tanpa Filter)

### TC-FA-CAT-691: Custom Field Numeric dan Percentage: Filter range, Sort numerik, dan Search nilai

21. Tutup Filter Panel
22. Buka Setup Column, centang `Rasio Pemakaian` (kolom `Nilai Kontrak` sudah tercentang), lalu klik `[Save]`
23. Klik icon Filter, isi `Nilai Kontrak` Min `100` dan Max `6000`, lalu klik `[Apply]`
24. Verifikasi field Filter `Nilai Kontrak` berupa range Min-Max
25. Verifikasi hasil `Laptop Dell - 1` (5000) dan `Laptop HP - 1` (250)
26. Klik icon Filter, klik `[Clear Field]`, isi `Rasio Pemakaian` Min `50` dan Max `100`, lalu klik `[Apply]`
27. Verifikasi field Filter `Rasio Pemakaian` berupa range Min-Max
28. Verifikasi hasil hanya `Laptop Dell - 1` (80)
29. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
30. Ketik Search `5000`, tekan Enter
31. Verifikasi `5000` menemukan `Laptop Dell - 1`
32. Klik `(←)` pada kotak Search
33. Klik header Rasio Pemakaian satu kali
34. Verifikasi Sort numerik Ascending 20 sebelum 80
35. Klik header Rasio Pemakaian satu kali lagi
36. Verifikasi Descending kebalikan penuh
37. Klik header Rasio Pemakaian satu kali lagi
38. Verifikasi urutan kembali Netral ke default Name A-Z

## Notes

- Mode: FE+BE. Spec melewati sekitar 35 langkah (nominal 38). Alasan: dua TC memakai Popup Detail `Laptop` yang sama dan kolom Custom Field yang dicentang di TC-FA-CAT-667 dipakai langsung oleh TC-FA-CAT-691 tanpa menyiapkan ulang; ekspansi berasal dari butir Expected bermajemuk yang dipecah per klausa (S-01).
- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah `[Clear Field]` + `[Apply]` yang melepas Filter, langkah `(←)` pada Search, dan langkah menutup Filter Panel.
- Kelompok tipe Currency diwakili Numeric dan Percentage pada fixture (TC-FA-CAT-691 Expected e); ketentuan fixture, tidak diasersi.
- Isi berkas unduhan XLSX Tabel Assets (TC-FA-CAT-668) ada di spec TC-FA-CAT-E2E-204.
- Temuan untuk QA:
  - TC-FA-CAT-667 Expected a menyebut "Sort `Nilai Kontrak` numerik" dengan baris `—` di akhir; asersi pada halaman 1 saja karena 12 aset terbagi dua halaman dan nilai berada pada tiga baris pertama.
  - Nama env var `FA_FS_PASSWORD` untuk akun Full Sensitive adalah usulan (TC tidak menyebut nama env var); perlu konfirmasi tim.
