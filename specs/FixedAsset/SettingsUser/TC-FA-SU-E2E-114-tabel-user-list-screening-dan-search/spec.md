---
id: TC-FA-SU-E2E-114-tabel-user-list-screening-dan-search
title: "Tabel User List: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-320
  - TC-FA-SU-321
  - TC-FA-SU-322
  - TC-FA-SU-323
coverage:
  web: automated
---

# Tabel User List: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna) dan penugasan peran (#23). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Kolom `TAG` tersedia pada plan Enterprise; kolom ditampilkan lewat Setup Column pada langkah 18.
- Tabel `Ikon Table Tools`:

| Ikon | Tooltip |
|---|---|
| Search | `Search` |
| Filter | `Filter` |
| Download | `Download` |
| Changelog | `Changelog` |

- Tabel `Keyword Search Teks`:

| Kolom | Keyword | Hasil |
|---|---|---|
| Name | `Budi` | `Budi Santoso`, `Doni Prasetyo`, `Fajar Nugroho`, `Indra Wijaya`, `Kartika Sari`, `Lukman Hakim` (8 baris; kolom Name dan kolom Modified By `Budi Santoso`, Pre-setup #43) |
| Email | `lestari` | `Citra Lestari` (1 baris) |
| Position | `Manager` | `Ahmad Dahlan`, `Budi Santoso` (2 baris) |
| Division | `Logistics` | `Doni Prasetyo`, `Fajar Nugroho`, `Rina Susanti`, `Rudi Hartono` (4 baris) |
| Employee ID | `EMP-10131` | `Lina Marlina` (1 baris) |
| TAG | `TAG-0001` | `Budi Santoso` (1 baris) |

- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-SU-320: Screening User List

1. Verifikasi Table Tools `Search`, `Filter`, `Download`, `Changelog` tampil rata kanan
2. Untuk setiap baris tabel `Ikon Table Tools` di Prerequisites (langkah 3 sampai 4):
3. Hover ikon `<Ikon>`
4. Verifikasi tooltip `<Tooltip>` tampil
5. Klik icon Search
6. Verifikasi placeholder Search `Search by name, position, division...`
7. Klik `(←)` pada kotak Search
8. Verifikasi kolom tabel: `Active (sortable)`, `Name (sortable)`, `Email (sortable)`, `Role (sortable)`, `Home Group (sortable)`, `Position (sortable)`, `Division (sortable)`, `Employee ID (sortable)`, `Modified By (sortable)`, `Last Updated (sortable)`, dan `Column Visibility (⋯)` dengan body kolom Actions kosong tanpa row action
9. Klik header kolom Actions (⋯)
10. Verifikasi overlay Column Visibility terbuka
11. Tekan Esc
12. Verifikasi default sort Name ascending: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`
13. Verifikasi footer pagination 10 data per halaman dengan page size 10, 25, 50, 100

### TC-FA-SU-321: Search kelas exact

14. Ketik Search `active` (kolom Active), tekan Enter
15. Verifikasi tabel menyisakan `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Eka Wulandari`, `Gita Permata`, `Hana Kusuma` (21 baris)
16. Klik `(←)` pada kotak Search

### TC-FA-SU-322: Search kelas teks

17. Klik header kolom Actions (⋯), klik `Setup Column...`
18. Centang `TAG`, klik `[Save]`
19. Klik icon Search
20. Untuk setiap baris tabel `Keyword Search Teks` di Prerequisites (langkah 21 sampai 22):
21. Ganti isi kotak search dengan `<Keyword>` (kolom `<Kolom>`), tekan Enter
22. Verifikasi tabel menyisakan <Hasil>
23. Klik `(←)` pada kotak Search

### TC-FA-SU-323: Search kelas role

24. Ketik Search `Approver` (kolom Role), tekan Enter
25. Verifikasi tabel menyisakan `Eka Wulandari`, `Lukman Hakim`, `Mira Anggraini`, `Oscar Pranata`, `Qori Akbar`, `Yuda Pratama` (6 baris; Oscar Pranata dan Qori Akbar lewat baris pola Approver Group Manager yang dihitung sebagai penugasan aktif biasa)
26. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 7, 16, 23, 26 (menutup Search), 9 dan 11 (membuka dan menutup overlay Column Visibility), 17 dan 18 (menampilkan kolom `TAG` lewat Setup Column).
- Langkah yang diulang: langkah 3 sampai 4 (empat ikon) dan langkah 21 sampai 22 (enam keyword), dengan parameter pada tabel Prerequisites.
- Temuan untuk QA (S-15): (1) Daftar nama pada Expected TC berupa baris teratas hasil (kurang dari jumlah baris yang disebut atau dari ukuran halaman); spec mengasersi daftar nama itu dan jumlah baris sebagaimana tertulis. (2) Expected a TC-FA-SU-322 (Name `Budi`) menyebut 8 baris tetapi hanya enam nama; TC-FA-SU-328 dan 330 memuat enam nama yang sama tanpa jumlah baris. (3) Expected TC-FA-SU-323 menghitung Oscar Pranata dan Qori Akbar lewat baris pola Approver Group Manager; perilaku Search atas baris pola belum diputuskan PM (Open Item 3 PRD settings-user) dan spec mengasersi sesuai TC.
- Alasan di atas sekitar 35 langkah (ekspansi perulangan dihitung): seluruh blok berkelas fungsional yang sama pada halaman, akun, dan dataset Pre-setup #20 yang sama tanpa mengubah data; langkah berulang per kolom atau field berpola identik (langkah 3 sampai 4, langkah 21 sampai 22) dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna; bagian 3 konvensi menetapkan Setup Column, Bulk Action Bar, dan Search, Filter, Sort tetap satu spec selama dataset dan harness sama, sedangkan pemecahan hanya menambah login, hook, dan pembukaan halaman.
