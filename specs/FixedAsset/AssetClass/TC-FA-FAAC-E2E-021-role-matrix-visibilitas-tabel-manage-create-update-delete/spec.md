---
id: TC-FA-FAAC-E2E-021-role-matrix-visibilitas-tabel-manage-create-update-delete
title: "Role Matrix: Visibilitas Elemen Tabel Asset Class untuk Manage Accounting (Read, Create), (Read, Update), dan (Read, Delete)"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-59
  - TC-FA-FAAC-60
  - TC-FA-FAAC-61
sourceRules: ["§4.8#r1", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r11", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17", "§4.8#r18", "§4.8#r20", "ST-32", "§4.8#r19", "§4.8#b3"]
smoke: []
dependsOn: []
trace:
  "§4.8#r1": [1, 14, 28]
  "§4.8#r3": [1, 14, 28]
  "§4.8#r4": [1, 14, 28]
  "§4.8#r5": [1, 14, 28]
  "§4.8#r11": [2, 15, 29]
  "§4.8#r14": [4, 18, 31]
  "§4.8#r15": [4, 18, 31]
  "§4.8#r16": [6, 21, 33]
  "§4.8#r17": [7, 22, 34]
  "§4.8#r18": [7, 22, 34]
  "§4.8#r20": [7, 22, 34]
  "ST-32": [10, 37]
  "§4.8#r19": [11, 25, 38]
  "§4.8#b3": 19
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Tabel Asset Class untuk Manage Accounting (Read, Create), (Read, Update), dan (Read, Delete)

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Manage accounting (Read, Create)) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun lain memakai langkah ganti akun eksplisit di Test Steps. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Manage accounting (Read, Create) | `manageAccountingReadCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RC_PASSWORD` | TC-FA-FAAC-59 |
| Manage accounting (Read, Update) | `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RU_PASSWORD` | TC-FA-FAAC-60 |
| Manage accounting (Read, Delete) | `manageAccountingReadDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RD_PASSWORD` | TC-FA-FAAC-61 |

- Env var: `FA_AC_MA_RC_PASSWORD`, `FA_AC_MA_RU_PASSWORD`, `FA_AC_MA_RD_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: sembilan Asset Class contoh (Tabel Data Uji Pre-setup; nilai mengikuti Example Data PRD §4.1.1): HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); langkah memakai nama seed literal sesuai TC. Dibaca, tidak diubah.
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Kemampuan teknis: ganti akun (logout lalu login), hover pada elemen dan membaca tooltip, centang baris tabel.

## Test Steps

### TC-FA-FAAC-59

1. Verifikasi halaman Accounting, tab bar, tab Asset Class, Search, Filter, Download, Changelog, header Actions ⋯ (Column Visibility), link Class Code, dan link Asset Names: Show
2. Verifikasi Button [+ Asset Class]: Show
3. Ketik Search `HEAVY-EQ`, tekan Enter
4. Verifikasi kolom Checkbox dan Bulk Action Bar (Bulk Activate / Deactivate): Hidden (tidak ada kolom checkbox di header maupun baris)
5. Klik tombol ⋯ pada baris HEAVY-EQ
6. Verifikasi tombol ⋯ per baris: Show
7. Verifikasi menu ⋯ hanya memuat Duplicate dan tidak memuat Edit, Delete
8. Tutup menu ⋯
9. Arahkan kursor ke toggle Active baris HEAVY-EQ
10. Verifikasi tooltip "You don't have permission to edit." tampil
11. Verifikasi toggle kolom Active tetap tampil (visible) namun berstatus Disabled (tidak dapat diklik)

### TC-FA-FAAC-60

12. Ganti akun: logout, lalu login sebagai Manage accounting (Read, Update)
13. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
14. Verifikasi halaman Accounting, tab bar, tab Asset Class, Search, Filter, Download, Changelog, header Actions ⋯ (Column Visibility), link Class Code, dan link Asset Names: Show
15. Verifikasi Button [+ Asset Class]: Hidden
16. Ketik Search `HEAVY-EQ`, tekan Enter
17. Centang baris HEAVY-EQ
18. Verifikasi kolom Checkbox dan Bulk Action Bar (Bulk Activate / Deactivate): Show
19. Verifikasi Bulk Action Bar menampilkan aksi Activate / Deactivate sesuai komposisi seleksi
20. Klik tombol ⋯ pada baris HEAVY-EQ
21. Verifikasi tombol ⋯ per baris: Show
22. Verifikasi menu ⋯ hanya memuat Edit dan tidak memuat Duplicate, Delete
23. Tutup menu ⋯ dan hapus centang baris HEAVY-EQ
24. Arahkan kursor ke toggle Active baris HEAVY-EQ
25. Verifikasi toggle kolom Active: Show dan Enabled (dapat diklik)

### TC-FA-FAAC-61

26. Ganti akun: logout, lalu login sebagai Manage accounting (Read, Delete)
27. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
28. Verifikasi halaman Accounting, tab bar, tab Asset Class, Search, Filter, Download, Changelog, header Actions ⋯ (Column Visibility), link Class Code, dan link Asset Names: Show
29. Verifikasi Button [+ Asset Class]: Hidden
30. Ketik Search `HEAVY-EQ`, tekan Enter
31. Verifikasi kolom Checkbox dan Bulk Action Bar (Bulk Activate / Deactivate): Hidden (tidak ada kolom checkbox di header maupun baris)
32. Klik tombol ⋯ pada baris HEAVY-EQ
33. Verifikasi tombol ⋯ per baris: Show
34. Verifikasi menu ⋯ hanya memuat Delete dan tidak memuat Edit, Duplicate
35. Tutup menu ⋯
36. Arahkan kursor ke toggle Active baris HEAVY-EQ
37. Verifikasi tooltip "You don't have permission to edit." tampil
38. Verifikasi toggle kolom Active tetap tampil (visible) namun berstatus Disabled (tidak dapat diklik)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi). Tiap role punya blok sendiri karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8, 23, dan 35 (tutup menu ⋯ dan, bila ada, hapus centang baris, S-09), langkah 12 dan 26 (ganti akun), langkah 13 dan 27 (membuka tab Asset Class sesudah login ulang, S-07).
- Search `HEAVY-EQ` (langkah 3, 16, dan 30) mendahului aksi pada baris HEAVY-EQ karena baris itu tidak dijamin berada di halaman 1 (R-16).
- Spec ini melewati sekitar 35 langkah (38 langkah). Alasan: ketiga blok satu kelas (Role Matrix) dan satu topik (visibilitas elemen tabel per role), tiap blok role berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected tiap TC memuat lima klausa yang masing-masing wajib punya `Verifikasi` sendiri (S-01).
- Asersi Hidden memakai asersi Show elemen halaman (Search, Filter, Download, Changelog, dan lainnya) pada langkah pertama tiap blok sebagai anchor positif permukaan (bagian 8b butir 2).
- Langkah TC "Centang satu baris bila kolom checkbox tampil" dan "Klik tombol ⋯ bila tampil" ditulis deterministik tanpa langkah bersyarat: bila role memilikinya, langkah diklik dan diasersi Show; bila tidak, kolom checkbox dan tombol ⋯ diasersi Hidden.
- Temuan untuk QA:
  - TC-FA-FAAC-59 sampai 61 menaruh Search pada langkah 3 sesudah langkah centang baris pada langkah 2; spec memindahkan Search sebelum aksi baris agar baris yang dipakai adalah HEAVY-EQ.
  - TC-FA-FAAC-59 sampai 61 tidak menyebut baris yang dicentang dan dipakai untuk menu ⋯; spec memakai baris HEAVY-EQ.
  - Bulk Action Bar pada TC-FA-FAAC-60 baru tampil setelah seleksi; spec menambah langkah centang baris HEAVY-EQ sebelum asersi.
