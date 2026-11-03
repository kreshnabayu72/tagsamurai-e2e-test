---
id: TC-FA-CAT-E2E-143-kolom-asset-value-commercial-full-sensitive
title: "Kolom Asset Value (Commercial) dan Warranty Expiry Tabel Assets untuk Full Sensitive: Hidden Default, Format, Sort, Filter, dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-660
  - TC-FA-CAT-661
  - TC-FA-CAT-662
coverage:
  web: automated
---

# Kolom Asset Value (Commercial) dan Warranty Expiry Tabel Assets untuk Full Sensitive: Hidden Default, Format, Sort, Filter, dan Search

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Full Sensitive (Pre-setup #50) `fullSensitive_automated_{namaCompany}@qwertysystem.net` (Manage Asset Master Data: R; Group Role View asset value dan Manage purchase pada group `Head Office` dan `Region Jawa`; Global Role Manage accounting; lisensi FA-7 aktif), client CatMain (Pre-setup #20), password `Spectra.env.FA_FS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_FS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 (CatMain, node `Laptop`, seed API): Asset Value (Commercial) nilai buku terkini `Laptop Dell - 1` 15000000.00, `Laptop Dell - 2` 0, `Laptop HP - 1` 7500000.00, `Laptop HP - 3` 20000000.00 (Group `Region Jawa > Jakarta Selatan Distribution Center`, Brand `Hewlett Packard Enterprise Indonesia`), aset lain tanpa nilai; Warranty Expiry `Laptop Dell - 1` 2027-03-15, `Laptop HP - 1` 2026-12-01, `Laptop HP - 3` 2027-06-30, aset lain tanpa nilai. Disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-660: Kolom Asset Value (Commercial) Hidden default, format currency, nilai nol, dan strip

3. Verifikasi kolom `Asset Value (Commercial)` tidak tampil di tabel
4. Buka Setup Column lewat header kolom Actions (⋯)
5. Verifikasi kolom `Asset Value (Commercial)` ada di Setup Column dengan checkbox ☐ unchecked tetapi enabled
6. Centang kolom `Asset Value (Commercial)`, lalu klik `[Save]`
7. Verifikasi sel Asset Value `Laptop Dell - 1` menampilkan currency 2 desimal rata kanan sesuai `prd-conventions.md` §32
8. Verifikasi sel Asset Value `Laptop Dell - 2` menampilkan currency nol sesuai `prd-conventions.md` §32 (mis. `Rp 0,00`), bukan `—` dan bukan `No access`
9. Verifikasi sel Asset Value `Laptop Dell - 3` menampilkan `—` (berhak, nilai belum ada)
10. Klik kontrol halaman berikutnya
11. Verifikasi sel Asset Value `Laptop HP - 3` menampilkan nilainya (aktor berhak pada group `Region Jawa`)
12. Klik kontrol halaman sebelumnya
13. Verifikasi isi sel Asset Value adalah nilai buku terkini pada buku Commercial menurut `asset.md` `AST-LOGIC-12` (`Laptop Dell - 1` 15000000.00)

### TC-FA-CAT-661: Sort numerik, Filter range Min-Max, dan Search nilai tampil kolom Asset Value (Commercial)

14. Klik header Asset Value satu kali
15. Verifikasi Sort numerik (bukan alfabetis) Ascending 0, 7500000, 15000000, 20000000 lalu baris `—` di akhir
16. Klik header Asset Value satu kali lagi
17. Verifikasi Descending kebalikan dengan baris `—` di awal
18. Klik header Asset Value satu kali lagi
19. Verifikasi urutan kembali Netral ke default Name A-Z
20. Klik icon Filter
21. Verifikasi field `Asset Value` berupa range dengan placeholder `Min` dan `Max`
22. Isi Asset Value Min `1000000` dan Max `16000000`, lalu klik `[Apply]`
23. Verifikasi hasil hanya `Laptop HP - 1` (7500000) dan `Laptop Dell - 1` (15000000)
24. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
25. Ketik Search `15.000.000`, tekan Enter
26. Verifikasi Search mencocokkan nilai yang tampil pada sel berhak sehingga `Laptop Dell - 1` ditemukan
27. Klik `(←)` pada kotak Search

### TC-FA-CAT-662: Kolom Warranty Expiry Hidden default, format tanggal, dan strip

28. Verifikasi kolom `Warranty Expiry` tidak tampil di tabel
29. Buka Setup Column lewat header kolom Actions (⋯)
30. Verifikasi kolom `Warranty Expiry` ada di Setup Column dengan checkbox ☐ unchecked tetapi enabled
31. Centang kolom `Warranty Expiry`, lalu klik `[Save]`
32. Verifikasi sel Warranty Expiry `Laptop Dell - 1` menampilkan tanggal mengikuti Date Format General Settings
33. Verifikasi sel Warranty Expiry `Laptop Dell - 2` menampilkan `—` (berhak, nilai belum ada)
34. Klik kontrol halaman berikutnya
35. Verifikasi sel Warranty Expiry `Laptop HP - 3` menampilkan tanggal mengikuti Date Format General Settings

## Notes

- Mode: FE+BE. Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah pindah halaman 2 dan kembali ke halaman 1 untuk membaca `Laptop HP - 3` (S-14), langkah `[Clear Field]` + `[Apply]` yang melepas Filter, dan langkah `(←)` pada Search.
- Kolom `Asset Value (Commercial)` yang dicentang di TC-FA-CAT-660 tetap tampil di TC-FA-CAT-661 dan TC-FA-CAT-662 (Setup Column tersimpan); hook `after` memulihkannya.
- Temuan untuk QA:
  - TC-FA-CAT-660 Expected b/c merujuk `prd-conventions.md` §32 tanpa mengutip format teksnya (hanya contoh `Rp 0,00`); spec mengikuti rujukan itu.
  - TC-FA-CAT-661 Expected b: hasil Filter Min `1000000` Max `16000000` menyisakan `Laptop HP - 1` dan `Laptop Dell - 1`; urutan baris keduanya tidak disebut sehingga tidak diasersi.
  - TC-FA-CAT-660 langkah 4 menyebut `Laptop HP - 3` yang berada di halaman 2 pada default sort Name A-Z tanpa langkah pindah halaman; spec menambah langkah pindah halaman.
  - Nama env var `FA_FS_PASSWORD` untuk akun Full Sensitive adalah usulan (TC tidak menyebut nama env var); perlu konfirmasi tim.
