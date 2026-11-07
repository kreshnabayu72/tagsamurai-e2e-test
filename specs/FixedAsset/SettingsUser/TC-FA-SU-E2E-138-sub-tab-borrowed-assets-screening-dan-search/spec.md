---
id: TC-FA-SU-E2E-138-sub-tab-borrowed-assets-screening-dan-search
title: "Sub-tab Borrowed Assets: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-410
  - TC-FA-SU-411
  - TC-FA-SU-412
  - TC-FA-SU-413
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Responsibilities (#24). Pengguna target: Budi Santoso dengan 5 baris Borrowed Assets: `Laptop - 1`, `Laptop - 2` (Transaction ID `BRW-20260610`, PIC `Ahmad D`), `Kamera DSLR` (Brand `Canon`), `Proyektor Portable` (Asset ID `AST-01011`), dan `Kendaraan Operasional` (Model / Type `Vario 125`); nilai kolom lain tiap baris mengikuti Pre-setup #24. Kelima baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-410: Screening Sub-tab Borrowed Assets: Table Tools, kolom, dan default sort

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
3. Verifikasi Table Tools `Search | Filter | Download` tampil rata kanan
4. Hover tiap icon Table Tools
5. Verifikasi tooltip hover masing-masing icon sesuai nama icon
6. Klik icon Search
7. Verifikasi placeholder Search `Search name, asset ID, or transaction ID...`
8. Klik `(←)` pada kotak Search
9. Verifikasi kolom tabel berurutan `Photo | Name | Asset ID | Transaction ID | Brand | Model / Type | Due Return Date | PIC | Column Visibility (⋯)`
10. Verifikasi kolom Photo unsortable
11. Verifikasi kolom Name, Asset ID, Transaction ID, Brand, Model / Type, Due Return Date, dan PIC sortable
12. Klik header kolom Column Visibility (⋯)
13. Verifikasi overlay Column Visibility terbuka
14. Tutup overlay Column Visibility dengan Esc
15. Verifikasi body tiap baris kosong pada kolom Column Visibility (⋯) tanpa row action
16. Verifikasi pengurutan default Due Return Date ascending
17. Verifikasi baris default berurutan `Laptop - 1`, `Laptop - 2`, `Kamera DSLR`, `Proyektor Portable`, `Kendaraan Operasional`
18. Verifikasi footer pagination 10 data per halaman
19. Buka dropdown page size
20. Verifikasi pilihan page size 10, 25, 50, 100
21. Tutup dropdown page size dengan Esc

### TC-FA-SU-411: Search Sub-tab Borrowed Assets kelas teks: kolom Name, Asset ID, Transaction ID

22. Ketik Search `Kamera` (kolom Name), tekan Enter
23. Verifikasi kolom Name: keyword `Kamera` menyisakan `Kamera DSLR` (1 baris)
24. Kosongkan isi kotak search, tekan Enter
25. Ketik Search `AST-01011` (kolom Asset ID), tekan Enter
26. Verifikasi kolom Asset ID: keyword `AST-01011` menyisakan `Proyektor Portable` (1 baris)
27. Kosongkan isi kotak search, tekan Enter
28. Ketik Search `BRW-20260610` (kolom Transaction ID), tekan Enter
29. Verifikasi kolom Transaction ID: keyword `BRW-20260610` menyisakan `Laptop - 1` dan `Laptop - 2` (2 baris)
30. Klik `(←)` pada kotak Search

### TC-FA-SU-412: Search Sub-tab Borrowed Assets kelas badge: kolom Brand, Model / Type

31. Ketik Search `Canon` (kolom Brand), tekan Enter
32. Verifikasi kolom Brand: keyword `Canon` menyisakan `Kamera DSLR` (1 baris)
33. Kosongkan isi kotak search, tekan Enter
34. Ketik Search `Vario` (kolom Model / Type), tekan Enter
35. Verifikasi kolom Model / Type: keyword `Vario` menyisakan `Kendaraan Operasional` (1 baris)
36. Klik `(←)` pada kotak Search

### TC-FA-SU-413: Search Sub-tab Borrowed Assets kelas user: kolom PIC

37. Ketik Search `Lestari` (kolom PIC), tekan Enter
38. Verifikasi kolom PIC: keyword `Lestari` menyisakan `Kamera DSLR` dan `Proyektor Portable` (2 baris)
39. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung (S-03, R-16): sebelum Detail pengguna dibuka, kotak Search User List diisi nama persis `Budi Santoso` (nama Pre-setup) karena User List memuat 25 pengguna pada 3 halaman dan posisi baris tidak diandalkan (R-23, 8b.13); langkah itu hanya menyaring baris target dan tidak diverifikasi.
- Alasan melewati sekitar 35 langkah (39 langkah tertulis, 39 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-413: keyword `Lestari` mencocokkan baris `Kamera DSLR` dan `Proyektor Portable`, sedangkan kolom PIC dan opsi Filter PIC menampilkan bentuk singkat seperti `Ahmad D`; TC tidak menyatakan bahwa Search PIC mencocokkan nama lengkap (R-14).
