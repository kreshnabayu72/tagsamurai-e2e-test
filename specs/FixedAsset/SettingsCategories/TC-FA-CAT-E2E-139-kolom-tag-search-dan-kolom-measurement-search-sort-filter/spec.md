---
id: TC-FA-CAT-E2E-139-kolom-tag-search-dan-kolom-measurement-search-sort-filter
title: "Kolom TAG Search Label Tipe Tag serta Kolom Measurement: Toggle, Sel Symbol UoM, Search, Sort, dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-682
  - TC-FA-CAT-654
  - TC-FA-CAT-655
coverage:
  web: automated
---

# Kolom TAG Search Label Tipe Tag serta Kolom Measurement: Toggle, Sel Symbol UoM, Search, Sort, dan Filter

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 (CatMain, node `Laptop`, seed API): tag aktif `Laptop Dell - 1` RFID `RFID-0001` dan QR `QR-0001`, `Laptop Dell - 2` NFC `NFC-0002`; UoM Asset Name `Laptop Dell` Symbol `pcs` (Unit Name `Pieces`) dan `Laptop HP` Symbol `set` (Unit Name `Set`). Disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-682: Search kolom TAG mencocokkan label tipe tag, bukan Tag Code

3. Verifikasi kolom `TAG` tampil pada tabel
4. Ketik Search `rfid`, tekan Enter
5. Verifikasi `rfid` (case-insensitive) menemukan `Laptop Dell - 1`
6. Klik `(←)` pada kotak Search
7. Ketik Search `nfc`, tekan Enter
8. Verifikasi `nfc` menemukan `Laptop Dell - 2`
9. Klik `(←)` pada kotak Search
10. Ketik Search `RFID-0001`, tekan Enter
11. Verifikasi `No results found` dengan `Try adjusting your search or filter.` tampil karena Tag Code tidak ditampilkan dan tidak dicari
12. Klik `(←)` pada kotak Search
13. Buka Setup Column lewat header kolom Actions (⋯), hilangkan centang kolom `TAG`, lalu klik `[Save]`
14. Ketik Search `rfid`, tekan Enter
15. Verifikasi keyword `rfid` tidak mencocokkan baris saat kolom `TAG` disembunyikan (Search terikat visibilitas kolom)
16. Klik `(←)` pada kotak Search
17. Pulihkan konfigurasi kolom tabel Assets dengan menghapus preferensi kolom di browser

### TC-FA-CAT-654: Kolom Measurement curated Hidden default, toggle, dan sel Symbol UoM

18. Verifikasi kolom `Measurement` tidak ada di header tabel
19. Buka Setup Column lewat header kolom Actions (⋯)
20. Verifikasi checkbox kolom `Measurement` ☐ unchecked tetapi enabled
21. Centang kolom `Measurement`
22. Verifikasi Live Preview menambahkan kolom `Measurement`
23. Klik `[Save]`
24. Verifikasi tabel memuat kolom `Measurement`
25. Verifikasi sel Measurement `Laptop Dell - 1` menampilkan `pcs`
26. Verifikasi sel Measurement `Laptop HP - 1` menampilkan `set`
27. Verifikasi Unit Name (`Pieces`) tidak tampil pada sel
28. Verifikasi sel Measurement tidak pernah `—`
29. Tekan F5
30. Pilih node `Electronics`, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
31. Verifikasi kolom `Measurement` tetap tampil

### TC-FA-CAT-655: Search, Sort 3-state, dan Filter kolom Measurement

32. Ketik Search `pcs`, tekan Enter
33. Verifikasi tabel menyisakan 8 aset `Laptop Dell - 1` sampai `Laptop Dell - 8`
34. Klik `(←)` pada kotak Search
35. Klik header Measurement satu kali
36. Verifikasi Ascending alfabet A-Z (`pcs` sebelum `set`)
37. Klik header Measurement satu kali lagi
38. Verifikasi Descending kebalikan penuh
39. Klik header Measurement satu kali lagi
40. Verifikasi urutan kembali Netral ke default Name A-Z
41. Klik icon Filter
42. Verifikasi field `Measurement` dengan placeholder `All units` tampil di Filter Panel
43. Buka dropdown field `Measurement`
44. Verifikasi field `Measurement` berupa multi-select searchable
45. Verifikasi opsi dropdown hanya Symbol distinct dari baris tabel: `pcs`, `set`
46. Pilih `set`, lalu klik `[Apply]`
47. Verifikasi tabel menyisakan 4 aset `Laptop HP - 1` sampai `Laptop HP - 4`

## Notes

- Mode: FE+BE. Spec melewati sekitar 35 langkah (nominal 47). Alasan: tiga TC memakai Popup Detail `Laptop` yang sama; kolom `Measurement` yang disiapkan TC-FA-CAT-654 dipakai langsung oleh TC-FA-CAT-655 tanpa menyiapkan ulang.
- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah `(←)` pada Search, langkah 17 (memulihkan konfigurasi kolom sesudah TC-FA-CAT-682 menyembunyikan `TAG` supaya kolom `Measurement` kembali Hidden default), dan langkah 30 (membuka kembali Popup Detail sesudah F5).
- TC-FA-CAT-655 langkah 2 (centang `Measurement` lalu `[Save]`) tidak diulang karena kolom sudah tercentang dan tersimpan dari TC-FA-CAT-654 pada spec yang sama (kolom tetap tampil sesudah F5, langkah 30).
- Temuan untuk QA:
  - TC-FA-CAT-654 Expected c: "sel tidak pernah `—`" tidak punya aset contoh tanpa Asset Name berUoM; spec mengasersi pada `Laptop Dell - 1` dan `Laptop HP - 1`.
  - TC-FA-CAT-655 Expected b mensyaratkan Descending "kebalikan penuh" tanpa menyebut urutan baris dalam kelompok Symbol yang sama; spec mengasersi kebalikan urutan Ascending.
