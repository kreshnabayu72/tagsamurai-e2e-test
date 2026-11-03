---
id: TC-FA-CAT-E2E-144-warranty-expiry-dan-custom-field-full-sensitive
title: "Kolom Warranty Expiry dan Custom Field Tabel Assets untuk Full Sensitive: Sort, Filter, Urutan Grup, Sel per Data Type, dan Strip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-663
  - TC-FA-CAT-664
  - TC-FA-CAT-665
  - TC-FA-CAT-666
coverage:
  web: automated
---

# Kolom Warranty Expiry dan Custom Field Tabel Assets untuk Full Sensitive: Sort, Filter, Urutan Grup, Sel per Data Type, dan Strip

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Full Sensitive (Pre-setup #50) `fullSensitive_automated_{namaCompany}@qwertysystem.net` (Manage Asset Master Data: R; Group Role View asset value dan Manage purchase pada group `Head Office` dan `Region Jawa`; Global Role Manage accounting; lisensi FA-7 aktif), client CatMain (Pre-setup #20), password `Spectra.env.FA_FS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_FS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 (CatMain, node `Laptop`, seed API): Warranty Expiry `Laptop Dell - 1` 2027-03-15, `Laptop HP - 1` 2026-12-01, `Laptop HP - 3` 2027-06-30, aset lain tanpa nilai.
- Data Pre-setup #56 (Custom Field, lisensi FA-7 aktif): Field Active General `Kondisi Fisik`, `Rasio Pemakaian`, `Skor Aset`, `Tanggal Inspeksi` (`Laptop Dell - 1` 2026-08-20), `Warna Casing` (Text, Scope Specific Asset Name `Laptop Dell`; `Laptop Dell - 1` `Silver`, `Laptop Dell - 2` tanpa nilai); Purchasing `Nilai Kontrak` (Number; `Laptop Dell - 1` 5000, `Laptop Dell - 2` 0, `Laptop HP - 1` 250), `Nomor Kontrak Dell`, `Nomor PO` (Text; `Laptop Dell - 1` `PO-0001`, `Laptop Dell - 3` tanpa nilai); Accounting `Kode Anggaran` (Text; `Laptop Dell - 1` `ANG-01`); Inactive `Catatan Lama`. Disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-663: Sort, Filter date range, dan guard Search kolom Warranty Expiry

3. Buka Setup Column lewat header kolom Actions (⋯), centang `Warranty Expiry`, lalu klik `[Save]`
4. Klik header Warranty Expiry satu kali
5. Verifikasi Ascending Oldest First: `Laptop HP - 1` 2026-12-01, `Laptop Dell - 1` 2027-03-15, `Laptop HP - 3` 2027-06-30, lalu baris `—` di akhir
6. Klik header Warranty Expiry satu kali lagi
7. Verifikasi Descending Newest First
8. Klik header Warranty Expiry satu kali lagi
9. Verifikasi urutan kembali Netral ke default Name A-Z
10. Klik icon Filter
11. Verifikasi field `Warranty Expiry` berupa date range picker dengan placeholder `Select date`
12. Pilih rentang Warranty Expiry 2027-01-01 sampai 2027-04-30, lalu klik `[Apply]`
13. Verifikasi hasil hanya `Laptop Dell - 1`
14. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
15. Ketik Search `2027`, tekan Enter
16. Verifikasi tidak ada hasil karena kolom tanggal tidak dicari lewat Search
17. Klik `(←)` pada kotak Search

### TC-FA-CAT-664: Kolom Custom Field satu kolom per field Active

18. Buka Setup Column lewat header kolom Actions (⋯)
19. Verifikasi daftar kolom di antara `Warranty Expiry` dan `Last Updated` berurutan grup General (`Kondisi Fisik`, `Rasio Pemakaian`, `Skor Aset`, `Tanggal Inspeksi`, `Warna Casing`), Purchasing (`Nilai Kontrak`, `Nomor Kontrak Dell`, `Nomor PO`), Accounting (`Kode Anggaran`) dengan Field Name A-Z dalam grup
20. Verifikasi seluruh checkbox kolom Custom Field ☐ unchecked tetapi enabled
21. Verifikasi kolom Custom Field tidak tampil di tabel
22. Verifikasi field Inactive `Catatan Lama` tidak ada di daftar Setup Column
23. Centang `Warna Casing`, lalu klik `[Save]`
24. Verifikasi kolom `Warna Casing` tampil di tabel

### TC-FA-CAT-665: Sel Custom Field mengikuti Data Type

25. Buka Setup Column, centang `Tanggal Inspeksi`, `Nilai Kontrak`, `Nomor PO`, dan `Kode Anggaran` (kolom `Warna Casing` sudah tercentang), lalu klik `[Save]`
26. Verifikasi sel `Warna Casing` `Laptop Dell - 1` menampilkan `Silver`
27. Verifikasi sel `Nomor PO` `Laptop Dell - 1` menampilkan `PO-0001`
28. Verifikasi sel `Kode Anggaran` `Laptop Dell - 1` menampilkan `ANG-01`
29. Verifikasi sel `Tanggal Inspeksi` `Laptop Dell - 1` menampilkan tanggal mengikuti Date Format General Settings
30. Verifikasi sel `Nilai Kontrak` `Laptop Dell - 1` menampilkan angka sesuai format Data Type Number (`settings-custom-fields` §6.1)
31. Verifikasi sel `Nilai Kontrak` `Laptop Dell - 2` menampilkan nilai nol (bukan `—`)

### TC-FA-CAT-666: Custom Field di luar Scope dan nilai belum diisi menampilkan strip

32. Verifikasi sel `Warna Casing` `Laptop HP - 1` menampilkan `—` karena Asset Name `Laptop HP` di luar Scope field (bukan `No access`)
33. Verifikasi sel `Warna Casing` `Laptop Dell - 2` menampilkan `—` karena nilai belum diisi
34. Verifikasi sel `Nomor PO` `Laptop Dell - 3` menampilkan `—` (berhak, nilai belum ada)

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah `[Clear Field]` + `[Apply]` yang melepas Filter, dan langkah `(←)` pada Search.
- Urutan blok: Setup Column pada TC-FA-CAT-665 dan TC-FA-CAT-666 tidak diulang untuk `Warna Casing` dan `Nomor PO` karena sudah tercentang dan tersimpan; `Nomor PO` dicentang pada TC-FA-CAT-665 dan dipakai langsung TC-FA-CAT-666.
- Temuan untuk QA:
  - TC-FA-CAT-663 Expected a: urutan Descending Newest First tidak diperinci; spec mengasersi kebalikan Ascending.
  - TC-FA-CAT-665 langkah 3 menyuruh memperhatikan sel kelima kolom pada `Laptop Dell - 1`; TC tidak memberi nilai Tanggal Inspeksi dalam format tampilan sehingga hanya format yang diasersi.
  - TC-FA-CAT-666 Expected a mengasersi `—` pada `Laptop HP - 1`; anchor positif untuk strip dihasilkan oleh sel yang bernilai pada TC-FA-CAT-665 (spec yang sama).
  - Nama env var `FA_FS_PASSWORD` untuk akun Full Sensitive adalah usulan (TC tidak menyebut nama env var); perlu konfirmasi tim.
