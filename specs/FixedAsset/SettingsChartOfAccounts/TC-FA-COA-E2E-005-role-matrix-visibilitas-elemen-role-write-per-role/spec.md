---
id: TC-FA-COA-E2E-005-role-matrix-visibilitas-elemen-role-write-per-role
title: "Role Matrix: Visibilitas Elemen Role Write per Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-10
  - TC-FA-COA-11
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Role Write per Role

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (bagian 3a; spec ditulis per blok role, urutan blok = urutan tabel):

| Role | Akun | Env password | TC |
|---|---|---|---|
| Manage accounting – Update (akun pertama, login di hook `before`) | `manageAccountingUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_UPDATE_PASSWORD` (terdaftar di `spectra.config.ts` dan `.env.example`) | TC-FA-COA-10 |
| Manage accounting – Delete | `manageAccountingDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_DELETE_PASSWORD` (terdaftar di `spectra.config.ts` dan `.env.example`) | TC-FA-COA-11 |

- Login akun pertama (Manage accounting – Update) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca, tidak diubah): akun P1 `5-6001` (Active) dan P3 `4-7001` (Inactive). Pencarian `001` dipilih spec untuk menampilkan P1 dan P3 sekaligus pada satu halaman (kode Pre-setup lain yang memuat `001` adalah `6-2001` dan `1-2001`); kecukupan hasil pada satu halaman perlu dikonfirmasi tim FE.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` untuk akun aktor yang dipakai, termasuk akun role di tabel (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `Fixture.settingsChartOfAccounts.<kunci>` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-10: Visibilitas elemen untuk Manage accounting – Update

1. Ketik Search `001`, tekan Enter
2. Verifikasi Switch Status baris P1 Show dan Enabled
3. Centang baris P1 dan P3
4. Verifikasi Checkbox dan Bulk Action Bar Show
5. Verifikasi Bulk Activate dan Bulk Deactivate Show
6. Verifikasi Bulk Delete Hidden
7. Klik `Unselect All`
8. Verifikasi ⋯ per baris P1 Show
9. Klik ⋯ pada baris P1
10. Verifikasi row action `Edit` Show
11. Verifikasi row action `Delete` Hidden
12. Tekan Esc
13. Verifikasi `+ Account` Hidden
14. Klik `(←)` pada kotak Search

### TC-FA-COA-11: Visibilitas elemen untuk Manage accounting – Delete

15. Logout dari akun Manage accounting – Update
16. Login sebagai Manage accounting – Delete
17. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
18. Ketik Search `001`, tekan Enter
19. Hover Switch Status pada baris P1
20. Verifikasi Switch Status baris P1 Disabled dengan tooltip `You don't have permission to edit.`
21. Centang baris P1 dan P3
22. Verifikasi Checkbox dan Bulk Action Bar Show
23. Verifikasi Bulk Delete Show
24. Verifikasi Bulk Activate dan Bulk Deactivate Hidden
25. Klik `Unselect All`
26. Verifikasi ⋯ per baris P1 Show
27. Klik ⋯ pada baris P1
28. Verifikasi row action `Delete` Show
29. Verifikasi row action `Edit` Hidden
30. Tekan Esc
31. Verifikasi `+ Account` Hidden
32. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Role Matrix visibilitas (bagian 3a): matriks elemen per role boleh memuat polaritas Show dan Hidden/Disabled dalam satu spec. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`) dan langkah per role berbeda (Bulk Activate dan Deactivate versus Bulk Delete; Edit versus Delete). Satu spec memuat dua role karena daftar elemen yang diperiksa sama (visibilitas role Write); aksi tulis tidak ada.
- Langkah penghubung (S-03): langkah 1 dan 18 (Search untuk menampilkan baris target; R-16, bagian 8b butir 13); langkah 3, 7, 21, dan 25 (menyiapkan seleksi lalu `Unselect All`, S-09); langkah 9, 12, 27, dan 30 (membuka dan menutup menu ⋯); langkah 14 dan 32 (menutup Search dan mereset tabel, S-09); langkah 15 sampai 17 (ganti akun eksplisit, S-07).
- Asersi tambahan di luar Expected TC (S-03): seleksi P1 (Active) dan P3 (Inactive) pada langkah 3 dan 21 diperlukan karena Bulk Activate tampil hanya bila seleksi memuat akun Inactive (komposisi seleksi, lihat TC-FA-COA-363 butir c); absence Hidden pada langkah 6, 11, 13, 24, 29, dan 31 memakai langkah Show di blok yang sama (Bulk Activate dan Deactivate, `Edit`, Bulk Delete, atau `Delete`) sebagai anchor permukaan (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-COA-363 (Manage accounting – Update + Delete) dan TC-FA-COA-364 (Default User) ada di spec 085.
- Temuan untuk QA:
  - TC-FA-COA-10 dan TC-FA-COA-11 tidak menyebut baris untuk Switch Status, ⋯ per baris, dan seleksi Bulk; spec memakai P1 (Active) dan P3 (Inactive) lewat Search `001`.
  - TC-FA-COA-11 butir a menyebut tooltip pada Switch Status Disabled tanpa langkah hover; spec menambah langkah hover (langkah 19) sebagai langkah penghubung.
