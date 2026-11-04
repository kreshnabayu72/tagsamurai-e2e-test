---
id: TC-FA-COA-E2E-051-setup-column-tabel-quick-panel-popup-dan-kolom-default-hidden
title: "Setup Column Tabel: Quick Panel, Popup, dan Kolom Default Hidden"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-187
  - TC-FA-COA-188
  - TC-FA-COA-189
  - TC-FA-COA-193
coverage:
  web: automated
---

# Setup Column Tabel: Quick Panel, Popup, dan Kolom Default Hidden

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data: tabel Chart of Accounts client default berisi akun Pre-setup P1 sampai P5 dan akun lain hasil seed (lihat Seed dan pemulihan di `suite.md`); spec tidak membaca atau menulis nilai akun tertentu, hanya kolom tabel.
- Kolom default Visible untuk langkah berulang (langkah 20 sampai 23):

  | Kolom |
  |---|
  | `Active` |
  | `Account Code` |
  | `Account Name` |
  | `Function` |
  | `Used By` |
  | `Last Used in Journal` |

- Kolom default Hidden: `Modified By` dan `Last Updated`.
- State yang diubah spec: tidak ada konfigurasi kolom yang disimpan; semua perubahan di popup dibuang dengan ikon ✕ tanpa `[Save]` (langkah 26 dan 35). Hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-187: Screening Quick Panel Column Visibility

1. Arahkan kursor ke ikon ⋯ pada header kolom Actions
2. Verifikasi tooltip ikon ⋯ header kolom Actions `Column Visibility`
3. Klik header kolom Actions ⋯
4. Verifikasi panel dropdown tampil dengan daftar kolom data; Active, Account Code, Account Name, Function, Used By, dan Last Used in Journal tercentang
5. Verifikasi Modified By dan Last Updated tidak tercentang
6. Verifikasi setiap baris kolom memiliki checkbox dan kontrol drag untuk reorder
7. Verifikasi kolom checkbox dan kolom Actions tidak muncul sebagai baris pada panel
8. Verifikasi item `Setup Column...` tampil di bagian bawah panel
9. Tekan `Esc` untuk menutup panel

### TC-FA-COA-188: Screening popup modal Setup Column

10. Klik header kolom Actions ⋯
11. Klik `Setup Column...`
12. Verifikasi header modal berjudul `Setup Column` dengan deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
13. Verifikasi ikon close ✕ tampil di kanan atas header modal
14. Verifikasi daftar kolom data berurutan Active, Account Code, Account Name, Function, Used By, Last Used in Journal, Modified By, Last Updated
15. Verifikasi tiap baris kolom memiliki checkbox, kontrol drag, dan kontrol pin
16. Verifikasi kolom checkbox dan kolom Actions tidak muncul sebagai baris
17. Verifikasi footer berisi `Reset to Default` (teks) dan `Save` (filled)
18. Verifikasi tidak ada tombol `Cancel` pada footer

### TC-FA-COA-189: Ceklis dan unceklis kolom default Visible

19. Verifikasi sedikitnya satu kolom data tampil pada tabel di balik modal
20. Hapus centang kolom `Active` pada daftar modal
21. Verifikasi kolom `Active` hilang dari tabel di balik modal
22. Centang kembali kolom `Active`
23. Verifikasi kolom `Active` muncul kembali di tabel di balik modal
24. Ulangi langkah 20 sampai 23 untuk setiap kolom lain pada tabel Prerequisites (`Account Code`, `Account Name`, `Function`, `Used By`, `Last Used in Journal`)
25. Verifikasi perubahan centang pada langkah 20 dan 22 terlihat pada tabel di balik modal tanpa klik `[Save]` (pratinjau langsung)
26. Tutup modal dengan ikon ✕

### TC-FA-COA-193: Guard satu kolom tersisa

27. Klik header kolom Actions ⋯
28. Klik `Setup Column...`
29. Hapus centang kolom Account Code, Account Name, Function, Used By, dan Last Used in Journal sehingga hanya Active yang tampil
30. Arahkan kursor ke checkbox Active, lalu klik checkbox itu
31. Verifikasi checkbox Active Disabled dengan tooltip "At least one column must remain visible."
32. Verifikasi checkbox Active tetap tercentang
33. Centang kembali Account Code
34. Verifikasi checkbox Active Enabled kembali
35. Tutup modal dengan ikon ✕

## Notes

- Alasan spec di atas sekitar 35 langkah (35 langkah nominal, sekitar 55 dengan ekspansi langkah 24): semua blok memakai satu tabel, satu popup Setup Column, dan satu kelas harness (fungsional Setup Column); langkah 20 sampai 23 diulang untuk enam kolom pada tabel Prerequisites (idiom 8b.7, `Verifikasi` tetap satu per klausa) dan tiap blok berdiri sendiri, sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Langkah 24 mengulang langkah 20 sampai 23 untuk lima kolom lain.
- Langkah penghubung (S-03): langkah 1 (hover ikon agar tooltip TC-187 butir e teramati sebelum panel dibuka, 8b.5), langkah 9 (menutup panel), langkah 19 (anchor positif asersi hilangnya kolom, 8b.2), langkah 26 dan 35 (menutup popup tanpa `[Save]`), langkah 27 dan 28 (membuka ulang popup untuk TC-193), langkah 29 (menyiapkan precondition TC-193).
- TC-189 langkah 1 (buka popup) dipenuhi oleh popup yang masih terbuka dari langkah 11.
- Pemulihan Setup Column (R-24, 8b.14): spec tidak menyimpan konfigurasi kolom; semua perubahan dibuang dengan ✕ tanpa `[Save]` (langkah 26 dan 35).
- TC-193 butir a ditulis dua `Verifikasi` (Disabled dengan tooltip pada langkah 31, tetap tercentang pada langkah 32).
- Temuan untuk QA:
  - TC-189 butir g ("pratinjau langsung sebelum Save") tidak menyebut cara membedakan pratinjau dari tabel tersimpan; spec mengasersi bahwa tabel berubah tanpa klik `[Save]` (langkah 25).
  - TC-187 tidak memuat langkah hover untuk butir e (tooltip ikon ⋯); spec menambah langkah 1 sebagai langkah penghubung.
