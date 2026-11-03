---
id: TC-FA-CAT-E2E-141-kolom-last-scanned-asset-id-tidak-filterable-dan-kolom-category-tidak-ada
title: "Kolom Last Scanned Tabel Assets serta Asset ID Tidak Filterable dan Kolom Category Tidak Ada"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-658
  - TC-FA-CAT-659
  - TC-FA-CAT-688
  - TC-FA-CAT-679
coverage:
  web: automated
---

# Kolom Last Scanned Tabel Assets serta Asset ID Tidak Filterable dan Kolom Category Tidak Ada

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 (CatMain, node `Laptop`, seed API): Last Scanned (Audit) `Laptop Dell - 1` 2026-10-10 14:30 dan `Laptop Dell - 2` 2026-09-01 09:00, aset lain belum pernah dipindai; `Laptop Dell - 3` pernah ditemukan lewat Search by Scan yang tidak dihitung sebagai Last Scanned. Asset ID `Laptop Dell - 1` dibaca dari seed (nilainya tidak tertulis di TC; disediakan tim FE). Disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-658: Kolom Last Scanned curated Hidden default dan format tanggal

3. Verifikasi kolom `Last Scanned` tidak ada di header tabel
4. Buka Setup Column lewat header kolom Actions (⋯)
5. Verifikasi checkbox kolom `Last Scanned` ☐ unchecked tetapi enabled
6. Centang kolom `Last Scanned`, lalu klik `[Save]`
7. Verifikasi sel Last Scanned `Laptop Dell - 1` menampilkan waktu pindai terbaru mengikuti Date Format dan Time Format General Settings
8. Verifikasi sel Last Scanned `Laptop Dell - 2` menampilkan waktu pindai terbaru mengikuti Date Format dan Time Format General Settings
9. Verifikasi sel Last Scanned `Laptop Dell - 3` menampilkan `—` (Search by Scan tidak dihitung sebagai Last Scanned)
10. Tekan F5
11. Pilih node `Electronics`, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
12. Verifikasi kolom `Last Scanned` tetap tampil

### TC-FA-CAT-659: Sort 3-state, Filter date range, dan guard Search kolom Last Scanned

13. Klik header Last Scanned satu kali
14. Verifikasi Ascending Oldest First (`Laptop Dell - 2` sebelum `Laptop Dell - 1`, baris `—` di akhir)
15. Klik header Last Scanned satu kali lagi
16. Verifikasi Descending Newest First (baris `—` di awal)
17. Klik header Last Scanned satu kali lagi
18. Verifikasi urutan kembali Netral ke default Name A-Z
19. Klik icon Filter
20. Verifikasi field `Last Scanned` berupa date range picker dengan placeholder `Select date`
21. Pilih rentang Last Scanned 2026-10-01 sampai 2026-10-31, lalu klik `[Apply]`
22. Verifikasi hasil hanya `Laptop Dell - 1`
23. Verifikasi baris `—` tidak tampil
24. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
25. Ketik Search `2026-10-10`, tekan Enter
26. Verifikasi tidak ada hasil karena kolom tanggal tidak dicari lewat Search
27. Klik `(←)` pada kotak Search

### TC-FA-CAT-688: Kolom Asset ID tidak Filterable

28. Klik icon Filter
29. Verifikasi Filter Panel memuat field `Name`
30. Verifikasi Filter Panel tidak memuat field `Asset ID`
31. Tutup Filter Panel
32. Ketik Asset ID milik `Laptop Dell - 1` di Search, tekan Enter
33. Verifikasi Search menampilkan hanya baris `Laptop Dell - 1`
34. Klik `(←)` pada kotak Search

### TC-FA-CAT-679: Kolom Category tidak ada

35. Verifikasi header tabel Assets memuat kolom `Name` dan tidak memuat kolom `Category`
36. Buka Setup Column lewat header kolom Actions (⋯)
37. Verifikasi daftar Setup Column memuat kolom curated lain (mis. `Last Scanned`)
38. Verifikasi daftar Setup Column tidak memuat `Category`
39. Tutup popup Setup Column
40. Klik icon Filter
41. Verifikasi Filter Panel tidak memuat field `Category`
42. Verifikasi default sort tetap Name A-Z

## Notes

- Mode: FE+BE. Spec melewati sekitar 35 langkah (nominal 42). Alasan: empat TC memakai Popup Detail `Laptop` yang sama; kolom `Last Scanned` yang disiapkan TC-FA-CAT-658 dipakai TC-FA-CAT-659 dan TC-FA-CAT-679 tanpa menyiapkan ulang.
- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah 11 (membuka kembali Popup Detail sesudah F5), langkah `[Clear Field]` + `[Apply]` yang melepas Filter, langkah `(←)` pada Search, dan langkah menutup Filter Panel dan popup Setup Column.
- TC-FA-CAT-659 langkah 2 (centang `Last Scanned` lalu `[Save]`) tidak diulang karena kolom sudah tercentang dan tersimpan dari TC-FA-CAT-658 pada spec yang sama (kolom tetap tampil sesudah F5).
- Search untuk menemukan `Laptop Dell - 1` lewat Asset ID adalah bagian Expected TC-FA-CAT-688, bukan langkah penghubung.
- Temuan untuk QA:
  - TC-FA-CAT-688 menyebut "Asset ID milik `Laptop Dell - 1`" tanpa nilai Asset ID di Pre-setup #22 atau #55; spec membaca Asset ID dari seed (kemampuan tim FE).
  - TC-FA-CAT-679 Expected b ("kolom curated lain tetap ada") tidak menyebut kolom pembanding; spec memakai `Last Scanned` yang sudah tampil di Setup Column pada spec ini.
