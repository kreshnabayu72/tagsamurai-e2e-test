---
id: TC-FA-SU-E2E-187-tab-non-login-user-filter-dan-kontrol-filter-dan-setup-column
title: "Tab Non-Login User: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-558
  - TC-FA-SU-559
  - TC-FA-SU-560
  - TC-FA-SU-1035
coverage:
  web: automated
---

# Tab Non-Login User: Filter dan Kontrol Filter dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Custom Field Shift (Pre-setup #31, `FaUserMain`): Gudang Cabang Bekasi `Morning`, Kendaraan Operasional B 1234 XY `Night`, Mesin Fotokopi Lt.3 `Morning`, Printer Lantai 5 `Night`, Ruang Meeting Anggrek `Morning`; kolom curated Shift muncul setelah ditampilkan lewat Setup Column.
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-558: Chip dan checkbox dropdown Filter sinkron dua arah, logika OR dalam field

2. Klik icon Filter
3. Buka dropdown Division
4. Centang `Facility` dan `Logistics Warehouse`
5. Klik `[Apply]`
6. Verifikasi dua chip `Facility` dan `Logistics Warehouse` tampil di dalam field Division
7. Verifikasi hasil adalah gabungan (OR) kedua opsi: `Gudang Cabang Bekasi`, `Ruang Meeting Anggrek`
8. Klik ✕ pada chip `Facility` tanpa membuka dropdown
9. Verifikasi chip `Facility` hilang
10. Buka dropdown Division
11. Verifikasi checkbox opsi `Facility` ter-uncheck
12. Verifikasi chip `Logistics Warehouse` tetap tampil
13. Hilangkan centang opsi `Logistics Warehouse`
14. Verifikasi chip `Logistics Warehouse` hilang
15. Ketik `facil` di kotak cari dropdown Division
16. Verifikasi opsi dropdown menyempit menjadi `Facility` (substring, tidak case-sensitive)
17. Ganti isi kotak cari dropdown dengan `zzz`
18. Verifikasi `No results found` tampil di dalam dropdown
19. Klik icon Filter

### TC-FA-SU-559: Screening Overlay Column Visibility

20. Hover header kolom Actions (⋯)
21. Verifikasi tooltip `Column Visibility`
22. Klik header kolom Actions (⋯)
23. Verifikasi overlay Column Visibility tampil
24. Verifikasi daftar kolom berurutan `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update`
25. Verifikasi checkbox ☑ Hideable terpilih dan enabled pada tiap kolom
26. Verifikasi drag handle tampil pada tiap kolom
27. Verifikasi kolom curated Temporary User, Temporary Until, dan Shift tidak tampil sebagai baris overlay (☐ Curated)
28. Verifikasi item `Setup Column...` di bagian bawah overlay
29. Tekan Esc

### TC-FA-SU-560: Screening Popup Setup Column dan Preview Table

30. Klik header kolom Actions (⋯), klik `Setup Column...`
31. Verifikasi header popup: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, icon close ✕
32. Verifikasi daftar kolom `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update`, `Temporary User`, `Temporary Until`, `Shift`
33. Verifikasi checkbox tampil pada tiap kolom
34. Verifikasi drag handle tampil pada tiap kolom
35. Verifikasi icon Pin tampil pada tiap kolom
36. Verifikasi Live Preview tabel tampil
37. Verifikasi footer `[Reset to Default]` dan `[Save]` rata kanan
38. Verifikasi tanpa `[Cancel]` di footer
39. Klik ✕ pada popup Setup Column

### TC-FA-SU-1035: Filter kelas cf (Shift)

40. Klik icon Filter
41. Buka dropdown Shift
42. Verifikasi opsi dropdown = DISTINCT data tabel (`Morning`, `Night`)
43. Centang `Morning`
44. Klik `[Apply]`
45. Verifikasi `Morning` menyisakan `Gudang Cabang Bekasi`, `Mesin Fotokopi Lt.3`, `Ruang Meeting Anggrek` (3 baris)
46. Verifikasi chip `Morning` tampil di dalam field Shift

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): Search nama `Budi Santoso` (Enter) lalu membuka Detail Budi Santoso, karena User List memuat lebih dari satu halaman (R-16, 8b butir 13); `Klik icon Filter` menutup panel sebelum TC-FA-SU-559; `Tekan Esc` menutup overlay Column Visibility; `✕` menutup popup Setup Column (S-09).
- Langkah `Ketik facil` dan `Verifikasi opsi dropdown menyempit` pada TC-FA-SU-558 ditambahkan karena Expected d menyebut penyempitan opsi (substring, tidak case-sensitive) sementara langkah TC hanya mengetik keyword tanpa hasil (S-03).
- Jumlah langkah: 46 tertulis, 46 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (46 langkah). Seluruh blok berada pada satu surface (satu tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-SU-558 menyebut dropdown Position, tetapi Position tidak memiliki opsi (seluruh nilai kosong, TC-FA-SU-552) sehingga dua opsi tidak dapat dicentang; spec memakai dropdown Division (opsi `Facility` dan `Logistics Warehouse`). Pemetaan Division ke baris diturunkan dari urutan sort Division pada TC-FA-SU-545 (`Facility` = Ruang Meeting Anggrek; `Logistics Warehouse` = Gudang Cabang Bekasi).
  - TC-FA-SU-558 langkah 5 meng-uncheck "opsi yang tersisa" sehingga Expected c ("chip lain tetap") tidak punya chip pembanding; spec mengasersi chip yang di-uncheck hilang.
