---
id: TC-FA-RP-E2E-176-tab-system-search-setup-column-download-dan-state-4
title: "Tab System: Search, Setup Column, Download, dan state (4/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-588
  - TC-FA-RP-589
  - TC-FA-RP-590
  - TC-FA-RP-592
coverage:
  web: automated
---

# Tab System: Search, Setup Column, Download, dan state (4/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #39 (Tab System memuat 9 Global Role dan 7 Group Role; Detail Role Group Role `Manage files` terisi). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): membaca berkas unduhan (nama berkas, jumlah sheet, nama kolom, urutan dan tipe baris).
- State yang diubah: konfigurasi kolom Setup Column Tab System (kolom Users disembunyikan); hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Tab System menampilkan seluruh baris tanpa pagination (TC-FA-RP-589)

1. Klik Tab `System`
2. Verifikasi tidak ada pagination pada bagian bawah tiap section
3. Verifikasi seluruh 9 Global Role dan 7 Group Role tampil

### Download Tab System (TC-FA-RP-590)

4. Klik ikon Download lalu `Download as CSV`
5. Verifikasi tidak ada toast sukses
6. Verifikasi berkas `Role-Permission-System.csv` terunduh
7. Klik ikon Download lalu `Download as XLSX`
8. Verifikasi tidak ada toast sukses
9. Verifikasi berkas `Role-Permission-System.xlsx` terunduh
10. Verifikasi berkas XLSX memuat satu sheet plain tanpa header info atau summary
11. Verifikasi kolom pertama `Role Type` bernilai `Global Role` atau `Group Role` diikuti kolom `Role Name` dan `Users`
12. Verifikasi baris Global Role tampil lebih dulu lalu baris Group Role
13. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, hapus centang kolom `Users`, lalu klik `[Save]`
14. Klik ikon Download lalu `Download as CSV`
15. Verifikasi kolom `Role Type` tetap ada pada berkas walau kolom lain disembunyikan
16. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, centang kembali kolom `Users`, lalu klik `[Save]`

### State Search dipertahankan setelah Back dari Detail Role (TC-FA-RP-592)

17. Ketik Search `manage`, tekan Enter
18. Catat baris yang tampil pada hasil Search
19. Klik Role Name `Manage files`
20. Klik segmen `System` pada Breadcrumb
21. Verifikasi Tab System aktif dengan Search `manage` tetap terpasang
22. Verifikasi hasil yang tampil sama dengan hasil sebelum membuka Detail Role
23. Kosongkan isi kotak search, tekan Enter

### Konfigurasi kolom Tab System tidak memengaruhi tabel lain (TC-FA-RP-588)

24. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, hapus centang kolom `Users`, lalu klik `[Save]`
25. Klik Tab `Total Control`
26. Verifikasi Tab Total Control tetap memakai konfigurasi kolomnya sendiri (kolom bawaan tampil lengkap; cache per tabel)

## Notes

- Urutan TC dalam spec: 589, 590, 592, 588 (bukan urutan nomor). Alasan: TC-FA-RP-588 menyimpan konfigurasi kolom dan berpindah tab sehingga dijalankan terakhir; TC-FA-RP-590 dan TC-FA-RP-592 memakai tampilan kolom default (S-10).
- Asersi "tidak ada toast sukses" (langkah 5 dan 8) diletakkan segera setelah pemicu dan sebelum asersi artefak; klik format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (bagian 8b butir 11).
- Langkah 13 sampai 16 memenuhi klausa Expected d ("`Role Type` tetap ada walau kolom lain disembunyikan") yang tidak punya langkah di Langkah Uji TC-FA-RP-590; langkah 13, 14, dan 16 adalah langkah penghubung yang ditambahkan spec dan langkah 16 memulihkan kolom `Users`.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1, 25); mencatat baris (langkah 18); klik Role Name dan Breadcrumb (langkah 19, 20); mengosongkan Search (langkah 23).
- Langkah 2 dan 3 memetakan Expected TC-FA-RP-589; Tab Total Control pada langkah 25 dipakai sebagai "tabel lain pada modul" (TC-FA-RP-588 menyebut "tab lain atau modal Changelog").
- Temuan untuk QA:
  - TC-FA-RP-590 Expected d menyebut `Role Type` tetap ada walau kolom lain disembunyikan tanpa langkah yang menyembunyikan kolom; spec menambah langkah 13 sampai 16 (lihat di atas).
  - TC-FA-RP-590 Expected b ("satu sheet plain") hanya berlaku untuk XLSX; spec mengasersinya pada berkas XLSX.
  - TC-FA-RP-592 langkah 3 menyebut "segmen `System` pada Breadcrumb" tanpa teks lain Breadcrumb; spec mengikuti teks TC.
