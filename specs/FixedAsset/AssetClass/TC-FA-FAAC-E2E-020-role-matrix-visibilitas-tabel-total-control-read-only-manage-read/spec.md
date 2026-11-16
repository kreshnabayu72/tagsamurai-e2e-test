---
id: TC-FA-FAAC-E2E-020-role-matrix-visibilitas-tabel-total-control-read-only-manage-read
title: "Role Matrix: Visibilitas Elemen Tabel Asset Class untuk Total Control, Read Only, dan Manage Accounting (Read)"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-56
  - TC-FA-FAAC-57
  - TC-FA-FAAC-58
sourceRules: ["§4.8#r1", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r11", "§4.8#r14", "§4.8#r15", "§4.8#b3", "§4.8#r16", "§4.8#r17", "§4.8#r18", "§4.8#r20", "§4.8#r19", "ST-32"]
smoke: []
dependsOn: []
trace:
  "§4.8#r1": [1, 15, 25]
  "§4.8#r3": [1, 15, 25]
  "§4.8#r4": [1, 15, 25]
  "§4.8#r5": [1, 15, 25]
  "§4.8#r11": [2, 16, 26]
  "§4.8#r14": [5, 18, 28]
  "§4.8#r15": [5, 18, 28]
  "§4.8#b3": 6
  "§4.8#r16": [8, 19, 29]
  "§4.8#r17": 9
  "§4.8#r18": 9
  "§4.8#r20": 9
  "§4.8#r19": [12, 22, 32]
  "ST-32": [21, 31]
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Tabel Asset Class untuk Total Control, Read Only, dan Manage Accounting (Read)

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Total Control) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun lain memakai langkah ganti akun eksplisit di Test Steps. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | TC-FA-FAAC-56 |
| Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_RO_PASSWORD` | TC-FA-FAAC-57 |
| Manage accounting (Read) | `manageAccountingRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_R_PASSWORD` | TC-FA-FAAC-58 |

- Env var: `FA_TC_PASSWORD`, `FA_AC_RO_PASSWORD`, `FA_AC_MA_R_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: sembilan Asset Class contoh (Tabel Data Uji Pre-setup; nilai mengikuti Example Data PRD §4.1.1): HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); langkah memakai nama seed literal sesuai TC. Dibaca, tidak diubah.
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Kemampuan teknis: ganti akun (logout lalu login), hover pada elemen dan membaca tooltip, centang baris tabel.

## Test Steps

### TC-FA-FAAC-56

1. Verifikasi halaman Accounting, tab bar, tab Asset Class, Search, Filter, Download, Changelog, header Actions ⋯ (Column Visibility), link Class Code, dan link Asset Names: Show
2. Verifikasi Button [+ Asset Class]: Show
3. Ketik Search `HEAVY-EQ`, tekan Enter
4. Centang baris HEAVY-EQ
5. Verifikasi kolom Checkbox dan Bulk Action Bar (Bulk Activate / Deactivate): Show
6. Verifikasi Bulk Action Bar menampilkan aksi Activate / Deactivate sesuai komposisi seleksi
7. Klik tombol ⋯ pada baris HEAVY-EQ
8. Verifikasi tombol ⋯ per baris: Show
9. Verifikasi menu ⋯ hanya memuat Edit, Duplicate, Delete
10. Tutup menu ⋯ dan hapus centang baris HEAVY-EQ
11. Arahkan kursor ke toggle Active baris HEAVY-EQ
12. Verifikasi toggle kolom Active: Show dan Enabled (dapat diklik)

### TC-FA-FAAC-57

13. Ganti akun: logout, lalu login sebagai Read Only
14. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
15. Verifikasi halaman Accounting, tab bar, tab Asset Class, Search, Filter, Download, Changelog, header Actions ⋯ (Column Visibility), link Class Code, dan link Asset Names: Show
16. Verifikasi Button [+ Asset Class]: Hidden
17. Ketik Search `HEAVY-EQ`, tekan Enter
18. Verifikasi kolom Checkbox dan Bulk Action Bar (Bulk Activate / Deactivate): Hidden (tidak ada kolom checkbox di header maupun baris)
19. Verifikasi tombol ⋯ per baris: Hidden
20. Arahkan kursor ke toggle Active baris HEAVY-EQ
21. Verifikasi tooltip "You don't have permission to edit." tampil
22. Verifikasi toggle kolom Active tetap tampil (visible) namun berstatus Disabled (tidak dapat diklik)

### TC-FA-FAAC-58

23. Ganti akun: logout, lalu login sebagai Manage accounting (Read)
24. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
25. Verifikasi halaman Accounting, tab bar, tab Asset Class, Search, Filter, Download, Changelog, header Actions ⋯ (Column Visibility), link Class Code, dan link Asset Names: Show
26. Verifikasi Button [+ Asset Class]: Hidden
27. Ketik Search `HEAVY-EQ`, tekan Enter
28. Verifikasi kolom Checkbox dan Bulk Action Bar (Bulk Activate / Deactivate): Hidden (tidak ada kolom checkbox di header maupun baris)
29. Verifikasi tombol ⋯ per baris: Hidden
30. Arahkan kursor ke toggle Active baris HEAVY-EQ
31. Verifikasi tooltip "You don't have permission to edit." tampil
32. Verifikasi toggle kolom Active tetap tampil (visible) namun berstatus Disabled (tidak dapat diklik)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi). Tiap role punya blok sendiri karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 (tutup menu ⋯ dan hapus centang agar blok berikutnya tidak mewarisi state, S-09), langkah 13 dan 23 (ganti akun), langkah 14 dan 24 (membuka tab Asset Class sesudah login ulang, S-07).
- Search `HEAVY-EQ` (langkah 3, 17, dan 27) mendahului aksi pada baris HEAVY-EQ karena baris itu tidak dijamin berada di halaman 1 (R-16).
- Asersi Hidden memakai asersi Show elemen halaman (Search, Filter, Download, Changelog, dan lainnya) pada langkah pertama tiap blok sebagai anchor positif permukaan (bagian 8b butir 2).
- Langkah TC "Centang satu baris bila kolom checkbox tampil" dan "Klik tombol ⋯ bila tampil" ditulis deterministik tanpa langkah bersyarat: bila role memilikinya, langkah diklik dan diasersi Show; bila tidak, kolom checkbox dan tombol ⋯ diasersi Hidden.
- Temuan untuk QA:
  - TC-FA-FAAC-56 sampai 58 menaruh Search pada langkah 3 sesudah centang baris pada langkah 2; spec memindahkan Search sebelum centang agar baris yang dicentang adalah HEAVY-EQ.
  - TC-FA-FAAC-56 sampai 58 tidak menyebut baris yang dicentang pada langkah 2; spec memakai baris HEAVY-EQ (baris yang sama dipakai langkah 3 dan 4 TC).
  - Bulk Action Bar pada TC-FA-FAAC-56 baru tampil setelah ada seleksi; spec menambah langkah centang baris HEAVY-EQ sebelum asersi dan langkah penghubung yang menghapus centang.
