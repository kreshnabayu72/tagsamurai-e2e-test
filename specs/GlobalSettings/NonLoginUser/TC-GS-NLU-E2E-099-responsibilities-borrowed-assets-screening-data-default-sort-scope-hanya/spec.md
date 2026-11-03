---
id: TC-GS-NLU-E2E-099-responsibilities-borrowed-assets-screening-data-default-sort-scope-hanya
title: "Responsibilities Borrowed Assets: Screening, Data, Default Sort, Scope, dan Hanya-Baca"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-353
  - TC-GS-NLU-354
  - TC-GS-NLU-355
  - TC-GS-NLU-356
  - TC-GS-NLU-375
coverage:
  web: automated
---

# Responsibilities Borrowed Assets: Screening, Data, Default Sort, Scope, dan Hanya-Baca

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Non-Login User `Budi Kurniawan` (Tabel Data Uji Pre-setup No. 11) dan data FAMS (No. 14) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data.
- Data FAMS (Tabel Data Uji Pre-setup No. 14, hanya dibaca; diakses lewat rute modul aset FAMS, LLD §4): Budi Kurniawan memiliki Borrowed `BRW-20260610-0001` (Laptop - 1, Asset ID `AST-00123`, Dell Latitude 5420, due `20/08/26`) dan `BRW-20260702-0003` (Proyektor, Epson EB-X06, due `05/08/26`), Assigned `ASG-20260505-0001` (Company Vehicle B1234XY, Asset ID `AST-00456`, Honda Vario 125) dan `ASG-20260610-0002` (Mesin Bor, Asset ID `AST-00789`, Bosch GSB 13), semuanya dengan PIC `Siti Rahma`.
- Data pembanding TC-GS-NLU-356: transaksi `BRW-20260801-0009` (Kamera Uji, milik Login User hasil Convert `Konversi Aset`, Pre-setup No. 14).
- Format tanggal General Settings: Date Format `dd/MM/yy` berlaku (Tabel Data Uji Pre-setup No. 16); spec tidak mengubahnya.
- Kemampuan teknis: membaca teks sel tabel, thumbnail Photo, dan ikon sort pada header.
- Suite berjalan serial (`parallel: false`). Hook `after` memulihkan sesi ke akun default suite.

## Test Steps

### TC-GS-NLU-353: Screening Tab Responsibilities dan sub-tab Borrowed Assets

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Buka Detail Non-Login User dengan Name tepat `Budi Kurniawan`
3. Klik tab `Responsibilities`, sub-tab `Borrowed Assets`
4. Verifikasi Breadcrumb `User > Detail`
5. Verifikasi Tab `Responsibilities (aktif) | Changelog`
6. Verifikasi Sub-tab `Borrowed Assets (aktif) | Assigned Assets`
7. Verifikasi sub-tab tidak memuat Pending Approvals dan Pending Tasks
8. Verifikasi toolbar: `Search | Filter | Download`
9. Verifikasi toolbar tanpa Changelog dan tanpa tombol tambah
10. Verifikasi kolom: `Photo | Transaction ID (sortable) | Name (sortable) | Asset ID (sortable) | Brand (sortable) | Model / Type (sortable) | Due Return Date (sortable) | PIC (sortable) | Column Visibility (⋯) (unsortable)`
11. Verifikasi kolom Photo tidak sortable
12. Verifikasi baris tabel berurutan Proyektor lalu Laptop - 1 (Due Return Date naik)
13. Verifikasi footer tanpa kontrol pagination (baris tidak lebih dari 10)

### TC-GS-NLU-354: Data Borrowed Assets Budi Kurniawan: nilai sel dan format tanggal

14. Verifikasi baris Laptop - 1: Transaction ID `BRW-20260610-0001`, Name `Laptop - 1` (dengan urutan karena ada aset senama), Asset ID `AST-00123`, Brand `Dell`, Model / Type `Latitude 5420`, PIC `Siti Rahma`
15. Verifikasi baris Laptop - 1: Due Return Date `20/08/26` (Date Format `dd/MM/yy`)
16. Verifikasi baris Laptop - 1: Photo thumbnail aset tampil

### TC-GS-NLU-355: Default sort Borrowed Assets Due Return Date ascending

17. Verifikasi baris terurut Due Return Date naik: Proyektor (`05/08/26`) sebelum Laptop - 1 (`20/08/26`)

### TC-GS-NLU-356: Borrowed Assets hanya memuat transaksi milik Non-Login User yang dibuka

18. Verifikasi tabel memuat baris Proyektor dan Laptop - 1 (pembanding positif)
19. Verifikasi tabel tidak memuat transaksi milik user lain (mis. `BRW-20260801-0009` milik Konversi Aset)

### TC-GS-NLU-375: Tab Responsibilities hanya-baca tanpa aksi tulis dan tanpa sub-tab Pending

20. Klik `⋯` pada header kolom Actions
21. Verifikasi kolom Actions hanya memicu Column Visibility
22. Verifikasi baris tabel tidak memuat row action tulis
23. Verifikasi tidak ada sub-tab Pending Approvals dan Pending Tasks
24. Verifikasi tidak ada tab Role, System Log, dan User Log
25. Tutup overlay Column Visibility dengan menekan `Esc`

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (353, 354, 355, 356, 375) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3 (Search `Budi Kurniawan`, membuka Detail, dan tab `Responsibilities` sub-tab `Borrowed Assets`; R-16); langkah 25 (menutup overlay Column Visibility di akhir spec). TC-GS-NLU-354, 355, 356 tidak mengulang langkah klik tab karena dijalankan pada state yang sama dengan TC-GS-NLU-353 (tab dan sub-tab sudah aktif).
- Asersi tambahan (konkretisasi Expected): "Tidak ada transaksi milik Non-Login User atau Login User lain" (TC-GS-NLU-356) ditulis memakai transaksi `BRW-20260801-0009` (Pre-setup No. 14) sebagai pembanding user lain, dengan pembanding positif baris Proyektor dan Laptop - 1.
- Pembagian TC lintas spec: Search dan Filter ada di spec 100; Sort, Photo, Pagination, Download ada di spec 101; Setup Column ada di spec 102 dan 103; sub-tab Assigned Assets ada di spec 104 sampai 107; TC-GS-NLU-376 (error load) ada di spec resilience.
- Temuan untuk QA:
  - TC-GS-NLU-354, 355: precondition TC menyebut Date Format `dd/MM/yy` "berlaku" tanpa menyebut siapa yang menetapkannya; spec menganggapnya state environment (Pre-setup No. 16).
  - TC-GS-NLU-375: TC tidak menyebut cara memeriksa "tidak ada row action tulis"; spec mengasersi baris tabel tidak memuat tombol aksi selain kolom Actions yang memicu Column Visibility. Cara membuka Detail Non-Login User dari daftar tidak dijelaskan TC (hanya "User > Detail"); spec menulis "Buka Detail Non-Login User" tanpa mekanisme klik tertentu.
