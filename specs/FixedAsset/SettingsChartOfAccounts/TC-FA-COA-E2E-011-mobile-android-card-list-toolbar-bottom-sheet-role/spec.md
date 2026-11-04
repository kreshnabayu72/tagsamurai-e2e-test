---
id: TC-FA-COA-E2E-011-mobile-android-card-list-toolbar-bottom-sheet-role
title: "Mobile Android: Card List, Toolbar, Bottom Sheet, Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-98
  - TC-FA-COA-99
  - TC-FA-COA-100
  - TC-FA-COA-102
  - TC-FA-COA-103
  - TC-FA-COA-104
coverage:
  mobile: automated
---

# Mobile Android: Card List, Toolbar, Bottom Sheet, Role

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi Android native pada emulator atau perangkat yang disediakan tim FE. `parallel: false` karena perangkat fisik bersama.
- Role yang diuji (bagian 3a; spec ditulis per blok role, urutan blok = urutan tabel):

| Role | Akun | Env password | TC |
|---|---|---|---|
| Total Control (akun pertama, login di hook `before`) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` (terdaftar) | TC-FA-COA-98, 104, 99, 100, 103 (blok akhir) |
| Manage accounting – Delete | `manageAccountingDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_DELETE_PASSWORD` (terdaftar di `spectra.config.ts` dan `.env.example`) | TC-FA-COA-102 |
| Read Only | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` (terdaftar) | TC-FA-COA-103 |

- Login akun pertama (Total Control) di hook `before` spec ini. Pengecualian atas hook `beforeEach` suite: layar web tidak berlaku di Android, sehingga spec membuka layar Chart of Accounts sendiri lewat langkah spec. Hook `after` spec mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca, tidak diubah): akun P1 `5-6001 – Depreciation Expense – Admin` sampai P5 `CAP-6100 – Capitalization Clearing – Repairs`.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` untuk akun aktor yang dipakai (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `Fixture.settingsChartOfAccounts.<kunci>` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-98: Tampilan card list: Account Code, Account Name, badge Function, switch Status, dan Used By

1. Buka Settings > Accounting, pilih tab Chart of Accounts
2. Verifikasi setiap akun tampil sebagai card dengan Account Code sebagai judul
3. Verifikasi card memuat Account Name, badge Function, switch Status, dan Used By
4. Verifikasi tidak ada tabel dan kolom header

### TC-FA-COA-104: Guided Tooltip dan tombol `[?]` tidak tampil di aplikasi Android

5. Verifikasi tombol `[?]` tidak tampil di header halaman
6. Verifikasi tur panduan tidak berjalan

### TC-FA-COA-99: Toolbar mobile: Search dan ⋯ berisi Column Visibility, Filter, dan Download; Changelog tetap di header

7. Verifikasi toolbar memuat `[🔍]` dan `[⋯]`
8. Buka `[⋯]`
9. Verifikasi di dalam `[⋯]` tampil Column Visibility, Filter, dan Download
10. Tutup menu `[⋯]`
11. Verifikasi ikon Changelog tetap di header halaman

### TC-FA-COA-100: Add dan Edit Account tampil sebagai bottom sheet

12. Tekan `+ Account`
13. Verifikasi Add Account tampil sebagai bottom sheet, bukan modal
14. Tutup bottom sheet Add Account
15. Ketik Search `5-6001`, tekan Enter
16. Tekan Edit pada card P1
17. Verifikasi Edit Account tampil sebagai bottom sheet
18. Verifikasi bottom sheet Edit Account memuat nilai tersimpan P1
19. Tutup bottom sheet Edit Account
20. Tutup kotak Search

### TC-FA-COA-102: Aksi Edit dan Delete tunggal lewat ikon ⋯ di pojok kanan card

21. Logout dari akun Total Control di Android
22. Login sebagai Manage accounting – Delete di Android
23. Buka Settings > Accounting, pilih tab Chart of Accounts
24. Ketik Search `CAP-6100`, tekan Enter
25. Tekan ⋯ pada card P5
26. Verifikasi menu ⋯ card memuat Delete
27. Verifikasi Edit tidak tampil di menu ⋯ card
28. Tutup menu ⋯ card
29. Tutup kotak Search

### TC-FA-COA-103: Tombol `+ Account` tampil di bawah toolbar dan Hidden untuk role tanpa Create

30. Logout dari akun Manage accounting – Delete di Android
31. Login sebagai Read Only di Android
32. Buka Settings > Accounting, pilih tab Chart of Accounts
33. Verifikasi `+ Account` Hidden di area di atas card list
34. Logout dari akun Read Only di Android
35. Login sebagai Total Control di Android
36. Buka Settings > Accounting, pilih tab Chart of Accounts
37. Verifikasi `+ Account` tampil di area di atas card list

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Role Matrix Android (bagian 3a): blok Total Control (TC-FA-COA-98, 104, 99, 100), Manage accounting – Delete (TC-FA-COA-102), lalu Read Only dan Total Control kembali (TC-FA-COA-103). Spec ditulis per blok role karena ganti akun menuntut Step eksplisit dan langkah per role berbeda.
- Urutan: TC-FA-COA-104 diletakkan tepat sesudah TC-FA-COA-98 agar absence tur diamati segera setelah halaman dibuka (bagian 8b butir 5).
- Langkah penghubung (S-03): langkah 8 dan 10 (membuka dan menutup menu `[⋯]`); langkah 14 dan 19 (menutup bottom sheet; formulir tidak diisi atau tidak diubah sehingga tidak dirty); langkah 15 dan 24 (Search untuk menampilkan card target; R-16, bagian 8b butir 13); langkah 20 dan 29 (menutup Search dan mereset daftar, S-09); langkah 21 sampai 23, 30 sampai 32, dan 34 sampai 36 (ganti akun eksplisit, S-07); langkah 28 (menutup menu ⋯ card).
- Asersi tambahan di luar Expected TC (S-03): absence Hidden dan tidak tampil pada langkah 4, 5, 6, 27, dan 33 memakai langkah tampil di blok yang sama (card list, ikon Changelog, Delete, atau card list) sebagai anchor permukaan (bagian 8b butir 2).
- Ukuran spec 37 langkah, melewati sekitar 35 langkah hanya tipis karena sembilan langkah ganti akun eksplisit dan Expected dipecah per klausa (S-01). Seluruh blok satu kelas (mobile Android) dan satu layar tanpa aksi tulis; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-COA-100 langkah 2 ("Tekan Edit pada card P1") tidak menyebut cara membuka Edit; spec memakai Edit pada card P1 setelah Search `5-6001`. Cara menutup bottom sheet juga tidak disebut; ditulis "Tutup bottom sheet" dan ditetapkan tim FE.
  - TC-FA-COA-98 sampai 104 tidak menyebut cara memuat card P1 sampai P5 di card list; spec memakai Search untuk card yang ditindak.
  - TC-FA-COA-103 butir b menyebut "area yang sama" setelah login ulang; spec mengasersi `+ Account` di area di atas card list.
