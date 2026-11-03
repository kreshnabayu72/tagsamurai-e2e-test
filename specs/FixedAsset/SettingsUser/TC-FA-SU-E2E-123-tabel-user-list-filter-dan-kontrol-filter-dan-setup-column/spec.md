---
id: TC-FA-SU-E2E-123-tabel-user-list-filter-dan-kontrol-filter-dan-setup-column
title: "Tabel User List: Chip Filter, Overlay Column Visibility, dan Screening Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-349
  - TC-FA-SU-350
  - TC-FA-SU-351
coverage:
  web: automated
---

# Tabel User List: Chip Filter, Overlay Column Visibility, dan Screening Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Opsi Status yang dicentang TC-FA-SU-349 tidak disebut TC; spec memakai `Active` dan `Inactive`. Keyword dropdown tanpa hasil: `zzzzqx` (pilihan spec).

## Test Steps

### TC-FA-SU-349: Chip dan checkbox dropdown Filter sinkron dua arah

1. Klik icon Filter, buka dropdown Status
2. Centang `Active` dan `Inactive`, klik `[Apply]`
3. Verifikasi dua chip `Active` dan `Inactive` tampil di dalam field Status
4. Verifikasi hasil adalah gabungan (OR) kedua opsi: tabel memuat baris Active (`Ahmad Dahlan`) dan baris Inactive (`Doni Prasetyo`)
5. Klik ✕ pada chip `Inactive` tanpa membuka dropdown
6. Verifikasi chip `Inactive` hilang dan chip `Active` tetap
7. Buka dropdown Status
8. Verifikasi checkbox opsi `Inactive` ter-uncheck
9. Hapus centang `Active`
10. Verifikasi chip `Active` hilang
11. Ketik `ACT` di kotak cari dropdown
12. Verifikasi opsi dropdown dipersempit secara substring tidak case-sensitive: `Active`, `Inactive`
13. Ganti isi kotak cari dropdown dengan `zzzzqx`
14. Verifikasi `No results found` tampil di dropdown
15. Tutup dropdown, klik `[Clear Field]` lalu `[Apply]`

### TC-FA-SU-350: Overlay Column Visibility

16. Hover header kolom Actions (⋯)
17. Verifikasi tooltip `Column Visibility` tampil pada header
18. Klik header kolom Actions (⋯)
19. Verifikasi overlay Column Visibility tampil
20. Verifikasi daftar kolom berurutan `Active`, `Name`, `Email`, `Role`, `Home Group`, `Position`, `Division`, `Employee ID`, `Modified By`, `Last Updated` dengan checkbox ☑ Hideable terpilih dan enabled serta drag handle
21. Verifikasi item `Setup Column...` di bagian bawah overlay
22. Verifikasi kolom curated `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Shift` tidak tampil sebagai baris tabel (☐ Curated)

### TC-FA-SU-351: Screening Popup Setup Column dan Preview Table

23. Klik `Setup Column...`
24. Verifikasi header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon close ✕
25. Verifikasi body memuat daftar kolom `Active`, `Name`, `Email`, `Role`, `Home Group`, `Position`, `Division`, `Employee ID`, `Modified By`, `Last Updated`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Shift` dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
26. Verifikasi footer `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
27. Klik `[✕]` pada Setup Column

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 15 (membersihkan Filter, S-09) dan 27 (menutup Setup Column).
- Temuan untuk QA (S-15): (1) TC-FA-SU-349 langkah 3 dan 5 tidak menyebut opsi yang dicentang; spec memakai `Active` dan `Inactive`. Expected d memuat pencarian substring dalam dropdown yang tidak punya langkah; spec menambah langkah mengetik `ACT` sebagai pemicu asersi itu. (2) TC-FA-SU-349 Expected a menyebut hasil gabungan OR tanpa nama baris; spec memakai `Ahmad Dahlan` (Active) dan `Doni Prasetyo` (Inactive) dari TC-FA-SU-1057.
