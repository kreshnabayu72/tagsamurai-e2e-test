---
id: TC-FA-COA-E2E-098-absence-log-create-gagal-5xx-atau-timeout
title: "Absence Log: Create Account Gagal 5xx atau Timeout Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-32
  - TC-FA-COA-302
coverage:
  web: automated
---

# Absence Log: Create Account Gagal 5xx atau Timeout Tidak Menulis Log

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons Create dipaksa lewat `Spectra.intercept()`, jumlah entri log dibaca dari backend nyata).
- Kelas harness g (asersi absence log). Pemicu adalah kegagalan 5xx atau timeout yang dipaksa (kelas b) dan hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji (P-5). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Data Dinamis (tidak ada yang tersimpan; dipakai sebagai input form): Account Code `5-6600` dengan Account Name `Depreciation Expense – Failure Test {runId}-098` (TC-FA-COA-32) dan Account Code `5-6910` dengan Account Name `Depreciation Expense – Timeout {runId}-098` (TC-FA-COA-302). Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal adalah nilai TC untuk Create yang selalu gagal (tidak pernah tersimpan) dan dibersihkan di hook `before` dan `after` (R-13).
- Kebutuhan intercept (kelas b; `Spectra.intercept()`, tanpa endpoint karangan): TC-FA-COA-32 respons Create dipaksa 5xx; TC-FA-COA-302 respons Create tidak diberikan (timeout). Intercept dilepas segera setelah pemicu diasersi dan dipulihkan di hook `after` bila spec gagal di tengah.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): kemampuan membaca dari server jumlah entri Changelog (per Account Code), System Log milik user aktor (Detail User > Tab System Log, kolom Name), dan Activity Log FAMS (kolom Name) untuk objek Chart of Accounts per Account Code, dibaca sebagai baseline sebelum aksi pemicu tiap TC (S-12); pembersihan akun lewat API.
- Seed dan pemulihan mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.

## Test Steps

### TC-FA-COA-32: Submit Create gagal 5xx

1. Catat baseline jumlah entri Account Code `5-6600` pada Changelog, System Log aktor, dan Activity Log dari server
2. Klik `+ Account` di toolbar
3. Isi Account Code `5-6600`, Account Name `Depreciation Expense – Failure Test {runId}-098`, dan pilih Account Function Depreciation Expense
4. Paksa respons Create menjadi 5xx lewat intercept jaringan
5. Klik `[Submit]`
6. Verifikasi toast `Error, failed to create account.` tampil
7. Lepas intercept respons Create
8. Klik ikon ✕ pada modal Add Account
9. Verifikasi dialog `Unsaved Changes` tampil
10. Klik `[Leave]`
11. Verifikasi jumlah entri `5-6600` pada Changelog sama dengan baseline langkah 1
12. Verifikasi jumlah entri `5-6600` pada System Log aktor sama dengan baseline langkah 1
13. Verifikasi jumlah entri `5-6600` pada Activity Log sama dengan baseline langkah 1

### TC-FA-COA-302: Timeout saat Create

14. Catat baseline jumlah entri Account Code `5-6910` pada Changelog, System Log aktor, dan Activity Log dari server
15. Klik `+ Account` di toolbar
16. Isi Account Code `5-6910`, Account Name `Depreciation Expense – Timeout {runId}-098`, dan pilih Account Function Depreciation Expense
17. Putus respons Create lewat intercept jaringan (tidak ada respons)
18. Klik `[Submit]`
19. Verifikasi toast `Connection problem. Please try again.` tampil
20. Lepas intercept respons Create
21. Klik ikon ✕ pada modal Add Account
22. Verifikasi dialog `Unsaved Changes` tampil
23. Klik `[Leave]`
24. Verifikasi jumlah entri `5-6910` pada Changelog sama dengan baseline langkah 14
25. Verifikasi jumlah entri `5-6910` pada System Log aktor sama dengan baseline langkah 14
26. Verifikasi jumlah entri `5-6910` pada Activity Log sama dengan baseline langkah 14

## Notes

- Pembagian TC lintas spec (S-05): TC-FA-COA-32 dan TC-FA-COA-302 ada di spec 066 (toast, modal, input, dan tidak ada akun dibuat) dan di spec ini (asersi "tidak ada log"). Spec ini memuat pemicu Create yang sama dengan baseline sendiri per TC (S-12); spec 066 tidak mengasersi log.
- Langkah 6 dan 19 (toast kegagalan hasil server) menjadi anchor positif bahwa respons sudah diproses sebelum asersi absence pada tiap surface log (bagian 8b butir 2 dan 11); tiga surface disebut satu per satu. Asersi absence ditulis sesudah intercept dilepas dan modal ditutup.
- Langkah penghubung (S-03, S-08, S-09): langkah 7 dan 20 (melepas intercept); langkah 8 sampai 10 dan 21 sampai 23 (menutup form dirty secara deterministik); langkah 1 dan 14 mencatat baseline sebelum aksi pemicu tiap TC dan bukan asersi.
- Temuan untuk QA:
  - TC-FA-COA-32 dan 302 menyebut "tidak ada log" tanpa surface; spec mengasersi Changelog, System Log aktor, dan Activity Log (PRD §8).
  - TC-FA-COA-32 dan 302 tidak menyebut cara menutup modal setelah kegagalan; spec memakai ✕, `Unsaved Changes`, `[Leave]` sebagai langkah penghubung.
