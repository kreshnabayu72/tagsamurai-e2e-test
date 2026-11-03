---
id: TC-FA-CAT-E2E-138-kolom-tag-ikon-per-tipe-tag-dan-toggle-geser-pin-persist
title: "Kolom TAG Tabel Assets: Ikon per Tipe Tag Aktif serta Toggle, Geser, Pin, dan Persist Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-651
  - TC-FA-CAT-652
coverage:
  web: automated
---

# Kolom TAG Tabel Assets: Ikon per Tipe Tag Aktif serta Toggle, Geser, Pin, dan Persist Setup Column

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 (CatMain, node `Laptop`, seed API): tag aktif `Laptop Dell - 1` RFID `RFID-0001` dan QR `QR-0001`, `Laptop Dell - 2` NFC `NFC-0002`, `Laptop Dell - 3` tanpa tag, `Laptop Dell - 4` pairing BARCODE berstatus nonaktif. Disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-652: Sel TAG satu ikon per tipe tag aktif

3. Verifikasi sel TAG `Laptop Dell - 1` menampilkan dua ikon penuh (tipe RFID dan QR) tanpa `+N more`
4. Verifikasi sel TAG `Laptop Dell - 2` menampilkan satu ikon tipe NFC
5. Verifikasi sel TAG `Laptop Dell - 3` dan `Laptop Dell - 4` menampilkan `—` (pairing nonaktif tidak menjadi ikon)
6. Hover ikon tipe RFID pada `Laptop Dell - 1`
7. Verifikasi hover menampilkan label tipe `RFID`
8. Hover ikon tipe QR pada `Laptop Dell - 1`
9. Verifikasi hover menampilkan label tipe `QR`
10. Verifikasi Tag Code (`RFID-0001`, `QR-0001`, `NFC-0002`) tidak tampil sebagai teks sel maupun isi hover

### TC-FA-CAT-651: Kolom TAG default Visible, toggle Setup Column, geser, pin, dan persist

11. Verifikasi kolom `TAG` tampil sebagai kolom Visible tepat setelah Asset ID pada header tabel
12. Klik header Actions (⋯) > `Setup Column...`
13. Verifikasi checkbox `TAG` ☑ Hideable (checked, enabled)
14. Hilangkan centang kolom `TAG`
15. Verifikasi Live Preview menyembunyikan kolom `TAG`
16. Centang kembali kolom `TAG`
17. Verifikasi Live Preview menampilkan kembali kolom `TAG`
18. Geser `TAG` ke posisi pertama pada daftar Setup Column, lalu klik `[Save]`
19. Tekan F5
20. Pilih node `Electronics`, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
21. Verifikasi `TAG` menjadi kolom data pertama dan urutan bertahan setelah F5
22. Buka Setup Column, klik icon Pin pada `TAG`, lalu klik `[Save]`
23. Scroll tabel Assets secara horizontal
24. Verifikasi kolom `TAG` tetap di kiri saat scroll horizontal
25. Tekan F5
26. Pilih node `Electronics`, lalu klik elipsis (⋯) pada baris `Laptop` > `Detail`
27. Scroll tabel Assets secara horizontal
28. Verifikasi kolom `TAG` tetap di kiri sehingga Pin bertahan setelah F5

## Notes

- Mode: FE+BE.
- Urutan blok: TC-FA-CAT-652 didahulukan sebelum TC-FA-CAT-651 karena TC-FA-CAT-651 mengubah urutan dan Pin kolom tersimpan; TC-FA-CAT-652 membaca sel pada tata letak bawaan.
- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail) serta langkah 20 dan 26 (membuka kembali Popup Detail sesudah F5). Pemulihan konfigurasi kolom dilakukan hook `after`.
- Sort dan Filter kolom TAG (TC-FA-CAT-653) berada di spec lain pada suite ini.
- Temuan untuk QA:
  - TC-FA-CAT-651 langkah 5 dan 6 menyuruh F5 lalu langsung membuka Setup Column tanpa menyebut membuka kembali Popup Detail yang tertutup oleh muat ulang; spec menambah langkah membuka kembali.
  - TC-FA-CAT-652 Expected d menyebut hover pada ikon `RFID` dan `QR`; hover ikon `NFC` pada `Laptop Dell - 2` tidak diminta sehingga tidak diasersi.
