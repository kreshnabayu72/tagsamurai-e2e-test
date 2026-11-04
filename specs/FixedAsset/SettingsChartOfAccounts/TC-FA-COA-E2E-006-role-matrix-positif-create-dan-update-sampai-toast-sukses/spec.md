---
id: TC-FA-COA-E2E-006-role-matrix-positif-create-dan-update-sampai-toast-sukses
title: "Role Matrix Positif: Create dan Update sampai Toast Sukses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-261
  - TC-FA-COA-262
  - TC-FA-COA-263
  - TC-FA-COA-264
  - TC-FA-COA-265
  - TC-FA-COA-266
coverage:
  web: automated
---

# Role Matrix Positif: Create dan Update sampai Toast Sukses

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (bagian 3a; spec ditulis per blok role, urutan blok = urutan tabel):

| Role | Akun | Env password | TC |
|---|---|---|---|
| Manage accounting – Create (akun pertama, login di hook `before`) | `manageAccountingCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_CREATE_PASSWORD` (terdaftar di `spectra.config.ts` dan `.env.example`) | TC-FA-COA-261 |
| Manage accounting – Update | `manageAccountingUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_UPDATE_PASSWORD` (terdaftar di `spectra.config.ts` dan `.env.example`) | TC-FA-COA-262, 263, 264, 265, 266 |

- Login akun pertama (Manage accounting – Create) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Data Dinamis (dibuat spec lewat UI): akun D5 Account Code `CAP-8200`, Account Name `Capitalization Clearing – Create Only {runId}-006`, Account Function `Capitalization Offset` (TC-FA-COA-261). Account Code `CAP-8200` literal tanpa suffix karena batas 15 karakter (A-18, lihat Temuan untuk QA); hook `before` menghapus akun `CAP-8200` bila sudah ada (idempotent) dan hook `after` menghapusnya lewat API; nama akun berbeda dari spec lain.
- Data Pre-setup (target tulis sekali pakai; identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE): P71 `CAP-8201 – Capitalization Clearing – Update Only Edit` (Active), P72 `CAP-8202 – Capitalization Clearing – Update Only Activate` (Inactive), P73 `CAP-8203 – Capitalization Clearing – Update Only Deactivate` (Active), P74 `CAP-8204 – Capitalization Clearing – Update Only Bulk Activate A` (Inactive), P75 `CAP-8205 – Capitalization Clearing – Update Only Bulk Activate B` (Inactive), P76 `CAP-8206 – Capitalization Clearing – Update Only Bulk Deactivate A` (Active), P77 `CAP-8207 – Capitalization Clearing – Update Only Bulk Deactivate B` (Active); seluruhnya Function Capitalization Offset, Used By 0, Last Used in Journal kosong. Account Name baru P71: `Capitalization Clearing – Update Only Edit Renamed {runId}-006`.
- Pengecualian A-18 (butir "Data bersama" di `suite.md`): P71 sampai P77 dan Account Code literal `CAP-8200` dipakai spec ini saja. Seed idempotent dan pemulihan P71 sampai P77 ke kondisi awal (termasuk Account Name P71 dan Last Updated) serta penghapusan `CAP-8200` dijalankan fixture backend (disediakan tim FE/BE) di hook `before` dan `after` spec ini; suite berjalan serial.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` untuk akun aktor yang dipakai, termasuk akun role di tabel (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan akun Pre-setup serta penghapusan akun D5 lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-261: Manage accounting – Create dapat membuat akun sampai toast sukses

1. Klik `+ Account` di toolbar
2. Isi Account Code `CAP-8200`
3. Isi Account Name `Capitalization Clearing – Create Only {runId}-006`
4. Pilih Account Function `Capitalization Offset`
5. Klik `[Submit]`
6. Verifikasi toast `Success, account has been created.`
7. Verifikasi modal Add Account tertutup
8. Ketik Search `CAP-8200`, tekan Enter
9. Verifikasi akun `CAP-8200` tampil di tabel dengan Status Active

### TC-FA-COA-262: Manage accounting – Update dapat menyimpan Edit akun sampai toast sukses

10. Logout dari akun Manage accounting – Create
11. Login sebagai Manage accounting – Update
12. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
13. Ketik Search `CAP-8201`, tekan Enter
14. Klik row action `Edit` pada akun P71
15. Ubah Account Name menjadi `Capitalization Clearing – Update Only Edit Renamed {runId}-006`
16. Klik `[Save]`
17. Verifikasi toast `Success, account has been updated.`
18. Verifikasi modal Edit Account tertutup
19. Verifikasi tabel menampilkan Account Name `Capitalization Clearing – Update Only Edit Renamed {runId}-006` pada baris P71

### TC-FA-COA-263: Manage accounting – Update dapat mengaktifkan akun single sampai toast sukses

20. Ganti isi kotak search dengan `CAP-8202`, tekan Enter
21. Klik switch Status P72
22. Klik `[Activate]` pada dialog D-14
23. Verifikasi toast `Success, account has been activated.`
24. Verifikasi switch Status P72 menjadi Active

### TC-FA-COA-264: Manage accounting – Update dapat menonaktifkan akun single sampai toast sukses

25. Ganti isi kotak search dengan `CAP-8203`, tekan Enter
26. Klik switch Status P73
27. Klik `[Deactivate]` pada dialog D-01
28. Verifikasi toast `Success, account has been deactivated.`
29. Verifikasi switch Status P73 menjadi Inactive

### TC-FA-COA-265: Manage accounting – Update dapat menjalankan Bulk Activate sampai toast sukses

30. Ganti isi kotak search dengan `Update Only Bulk Activate`, tekan Enter
31. Centang P74 dan P75
32. Klik Bulk `Activate`
33. Klik `[Activate]` pada dialog D-15
34. Verifikasi toast `Success, account has been activated.`
35. Verifikasi kedua akun P74 dan P75 menjadi Active

### TC-FA-COA-266: Manage accounting – Update dapat menjalankan Bulk Deactivate sampai toast sukses

36. Ganti isi kotak search dengan `Update Only Bulk Deactivate`, tekan Enter
37. Centang P76 dan P77
38. Klik Bulk `Deactivate`
39. Klik `[Deactivate]` pada dialog D-02
40. Verifikasi toast `Success, account has been deactivated.`
41. Verifikasi kedua akun P76 dan P77 menjadi Inactive
42. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Role Matrix positif (bagian 3a, `[KEPUTUSAN 2026-11-02]`): satu spec memuat dua aksi (Create dan Update) dengan polaritas seragam (positif sampai toast sukses). Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`) dan langkah per role berbeda. Aksi Update memiliki lima TC (Edit, Activate, Deactivate, Bulk Activate, Bulk Deactivate) yang semuanya memakai akun Manage accounting – Update.
- Langkah penghubung (S-03): langkah 8, 13, 20, 25, 30, dan 36 (Search untuk menampilkan baris atau akun target sebelum aksi atau asersi pada baris itu; R-16, bagian 8b butir 9 dan 13; bila Search sudah terisi ditulis "ganti isi kotak search dengan"); langkah 10 sampai 12 (ganti akun eksplisit, S-07); langkah 42 (menutup Search dan mereset tabel, S-09). Pembukaan menu ⋯ untuk row action `Edit` ditulis dalam langkah 14.
- Asersi tambahan di luar Expected TC (S-03): tidak ada.
- `A-18`: P71 sampai P77 menjadi target tulis sekali pakai (TC-FA-COA-262 sampai 266) dan Account Code `CAP-8200` literal (TC-FA-COA-261); syarat A-18 (seed idempotent, pemulihan di hook `before` dan `after`, suite serial, satu akun dan satu Code satu spec) dinyatakan di `## Prerequisites`.
- Ukuran spec 42 langkah, melewati sekitar 35 langkah karena Expected dipecah per klausa (S-01) dan enam TC masing-masing berdiri sendiri lewat data sekali pakai; langkah ganti akun 3. Seluruh blok satu kelas (Role Matrix positif sampai toast sukses), satu layar, dan tiap TC memakai akun Pre-setup sendiri (P71 sampai P77) sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - Account Code dibatasi 15 karakter dengan whitelist huruf, angka, `-`, `_`, `.`, sehingga suffix Data Dinamis `{runId}-<NNN>` tidak muat pada Account Code D5 `CAP-8200` (8 karakter ditambah suffix timestamp melebihi 15). Spec memakai Account Code literal `CAP-8200` sesuai A-18 dengan pembersihan idempotent di hook `before` dan `after`, suite serial, dan nama berbeda per spec; suffix dipasang pada Account Name.
  - TC-FA-COA-262 menetapkan Account Name baru literal `Capitalization Clearing – Update Only Edit Renamed`; spec menambah suffix `{runId}-006` agar nama unik per run (S-12).
  - TC-FA-COA-261, 262, 263, 264, 265, dan 266 Post Condition (record tersimpan, log L-01 sampai L-03, status baru) tidak punya langkah observasi untuk log; hanya toast dan state tabel yang diasersi.
  - TC-FA-COA-262 sampai 266 tidak menyebut baris pada hasil tabel tanpa Search; spec mencari target lewat Search sebelum aksi (R-16).
