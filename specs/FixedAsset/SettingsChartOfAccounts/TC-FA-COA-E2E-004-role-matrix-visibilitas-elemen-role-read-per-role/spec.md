---
id: TC-FA-COA-E2E-004-role-matrix-visibilitas-elemen-role-read-per-role
title: "Role Matrix: Visibilitas Elemen Role Read per Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-6
  - TC-FA-COA-7
  - TC-FA-COA-8
  - TC-FA-COA-9
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Role Read per Role

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (bagian 3a; spec ditulis per blok role, urutan blok = urutan tabel):

| Role | Akun | Env password | TC |
|---|---|---|---|
| Total Control (akun pertama, login di hook `before`) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` (terdaftar) | TC-FA-COA-6 |
| Read Only | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` (terdaftar) | TC-FA-COA-7 |
| Manage accounting – Read | `manageAccountingRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_READ_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; perlu didaftarkan tim FE) | TC-FA-COA-8 |
| Manage accounting – Create | `manageAccountingCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_CREATE_PASSWORD` (belum terdaftar; perlu didaftarkan tim FE) | TC-FA-COA-9 |

- Login akun pertama (Total Control) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca, tidak diubah): akun P1 `5-6001` (Active), P3 `4-7001` (Inactive), dan P7 `4-7002 – Gain and Loss on Disposal` (Used By 2). Pencarian `001` dipilih spec untuk menampilkan P1 dan P3 sekaligus pada satu halaman (kode Pre-setup lain yang memuat `001` adalah `6-2001` dan `1-2001`); kecukupan hasil pada satu halaman perlu dikonfirmasi tim FE.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` untuk akun aktor yang dipakai, termasuk akun role di tabel (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-chart-of-accounts.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-6: Visibilitas elemen untuk Total Control

1. Verifikasi menu `Accounting` pada sidebar Show dan Enabled
2. Verifikasi Search, Filter, Download, Changelog, dan `+ Account` di toolbar Show dan Enabled
3. Ketik Search `001`, tekan Enter
4. Verifikasi Switch Status baris P1 Show dan Enabled
5. Verifikasi Checkbox baris P1 Show dan Enabled
6. Verifikasi ⋯ per baris P1 Show dan Enabled
7. Klik ⋯ pada baris P1
8. Verifikasi row action `Edit` dan `Delete` Show dan Enabled
9. Tekan Esc
10. Centang baris P1 dan P3
11. Verifikasi Bulk Action Bar tampil
12. Verifikasi Bulk Activate, Bulk Deactivate, dan Bulk Delete Show dan Enabled
13. Klik `Unselect All`
14. Klik `(←)` pada kotak Search

### TC-FA-COA-7: Visibilitas elemen untuk Read Only

15. Logout dari akun Total Control
16. Login sebagai Read Only
17. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
18. Verifikasi Search, Filter, Download, Changelog, dan ⋯ header Column Visibility Show
19. Verifikasi `+ Account` Hidden
20. Hover Switch Status pada baris pertama
21. Verifikasi Switch Status baris pertama tampil dan Disabled dengan tooltip `You don't have permission to edit.`
22. Verifikasi kolom checkbox, Bulk Action Bar, dan ⋯ per baris Hidden

### TC-FA-COA-8: Visibilitas elemen untuk Manage accounting – Read

23. Logout dari akun Read Only
24. Login sebagai Manage accounting – Read
25. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
26. Verifikasi Search, Filter, Download, Changelog, dan Column Visibility Show
27. Ketik Search `4-7002`, tekan Enter
28. Verifikasi link Used By pada baris P7 Show
29. Verifikasi `+ Account`, checkbox, Bulk Action Bar, ⋯ per baris, dan row action `Edit` serta `Delete` Hidden
30. Hover Switch Status pada baris P7
31. Verifikasi Switch Status baris P7 Disabled dengan tooltip `You don't have permission to edit.`
32. Klik `(←)` pada kotak Search

### TC-FA-COA-9: Visibilitas elemen untuk Manage accounting – Create

33. Logout dari akun Manage accounting – Read
34. Login sebagai Manage accounting – Create
35. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
36. Verifikasi `+ Account` Show
37. Hover Switch Status pada baris pertama
38. Verifikasi Switch Status baris pertama Disabled dengan tooltip `You don't have permission to edit.`
39. Verifikasi checkbox, Bulk Action Bar, dan ⋯ per baris Hidden

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Role Matrix visibilitas (bagian 3a): matriks elemen per role boleh memuat polaritas Show dan Hidden/Disabled dalam satu spec. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`) dan langkah per role berbeda. Satu spec memuat empat role karena daftar elemen yang diperiksa sama (visibilitas role Read); aksi tulis tidak ada.
- Langkah penghubung (S-03): langkah 3, 27 (Search untuk menampilkan baris target sebelum aksi atau asersi pada baris itu; R-16, bagian 8b butir 12); langkah 7 dan 9 (membuka dan menutup menu ⋯); langkah 10, 13, dan 14 (menyiapkan seleksi lalu `Unselect All` dan mereset Search, S-09); langkah 15 sampai 17, 23 sampai 25, dan 33 sampai 35 (ganti akun eksplisit, S-07).
- Asersi tambahan di luar Expected TC (S-03): langkah 11 dan 12 untuk Bulk Activate memerlukan seleksi yang memuat akun Inactive (P3), karena Bulk Activate tampil hanya bila seleksi memuat akun Inactive (komposisi seleksi, lihat TC-FA-COA-363 butir c); absence Hidden pada langkah 19, 22, 29, dan 39 memakai langkah Show di blok yang sama (toolbar, Switch Status, atau link Used By) sebagai anchor permukaan (bagian 8b butir 2).
- Ukuran spec 39 langkah, melewati sekitar 35 langkah karena empat blok role berdiri sendiri, Expected dipecah per klausa (S-01), dan sembilan langkah ganti akun eksplisit. Seluruh blok satu kelas (Role Matrix visibilitas) dan satu layar tanpa aksi tulis; kegagalan satu blok role tidak membuat blok role lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-COA-6 butir a menyebut "Menu" tanpa definisi; spec memakai menu `Accounting` pada sidebar (entri yang juga disebut TC-FA-COA-12).
  - TC-FA-COA-6 tidak menyebut seleksi yang membuat Bulk Activate, Bulk Deactivate, dan Bulk Delete tampil bersamaan; spec memilih P1 (Active) dan P3 (Inactive) lewat Search `001`.
  - TC-FA-COA-8 butir a menyebut "link Used By Show" tanpa menyebut baris; spec memakai P7 (Used By 2) karena Used By 0 belum tentu berupa link.
  - TC-FA-COA-7, 8, dan 9 menyebut Switch Status tanpa menyebut baris; spec memakai baris pertama (TC-FA-COA-7 dan 9) atau P7 (TC-FA-COA-8).
