---
id: TC-FA-COA-E2E-101-absence-log-edit-gagal-5xx-atau-timeout
title: "Absence Log: Save Edit Gagal 5xx atau Timeout Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-41
  - TC-FA-COA-303
coverage:
  web: automated
---

# Absence Log: Save Edit Gagal 5xx atau Timeout Tidak Menulis Log

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons Save Edit dipaksa lewat `Spectra.intercept()`, jumlah entri log dibaca dari backend nyata).
- Kelas harness g (asersi absence log). Pemicu adalah kegagalan 5xx atau timeout yang dipaksa (kelas b) dan hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji (P-5). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed disediakan tim FE/BE): akun Code `DID101A`, Account Name `Depreciation Expense – Admin {runId}-101`, Function Depreciation Expense, Active, Used By 0, belum pernah diekspor (padanan P1 pada TC-FA-COA-41 dan 303). Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `DID101A` memuat nomor spec supaya unik per spec dan dibersihkan di hook `before` dan `after` (R-13).
- Data Dinamis (tidak ada yang tersimpan; dipakai sebagai input form): Account Name `Depreciation Expense – Admin Failure {runId}-101` (TC-FA-COA-41) dan `Depreciation Expense – Admin Timeout {runId}-101` (TC-FA-COA-303).
- Kebutuhan intercept (kelas b; `Spectra.intercept()`, tanpa endpoint karangan): TC-FA-COA-41 respons Save Edit dipaksa 5xx; TC-FA-COA-303 respons Save Edit tidak diberikan (timeout). Intercept dilepas segera setelah pemicu diasersi dan dipulihkan di hook `after` bila spec gagal di tengah.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): kemampuan membaca dari server jumlah entri Changelog (per Account Code), System Log milik user aktor (Detail User > Tab System Log, kolom Name), dan Activity Log FAMS (kolom Name) untuk objek Chart of Accounts per Account Code, dibaca sebagai baseline sebelum aksi pemicu tiap TC (S-12).
- Seed dan pemulihan mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.

## Test Steps

### TC-FA-COA-41: Save Edit gagal 5xx

1. Catat baseline jumlah entri Account Code `DID101A` pada Changelog, System Log aktor, dan Activity Log dari server
2. Ketik Search `{runId}-101`, tekan Enter
3. Klik row action `Edit` pada baris akun `DID101A`
4. Ubah Account Name menjadi `Depreciation Expense – Admin Failure {runId}-101`
5. Paksa respons Save Edit menjadi 5xx lewat intercept jaringan
6. Klik `[Save]`
7. Verifikasi toast `Error, failed to update account.` tampil
8. Lepas intercept respons Save Edit
9. Klik ikon ✕ pada modal Edit Account
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik `[Leave]`
12. Verifikasi jumlah entri `DID101A` pada Changelog sama dengan baseline langkah 1
13. Verifikasi jumlah entri `DID101A` pada System Log aktor sama dengan baseline langkah 1
14. Verifikasi jumlah entri `DID101A` pada Activity Log sama dengan baseline langkah 1

### TC-FA-COA-303: Timeout saat Save Edit

15. Catat baseline jumlah entri Account Code `DID101A` pada Changelog, System Log aktor, dan Activity Log dari server
16. Klik row action `Edit` pada baris akun `DID101A`
17. Ubah Account Name menjadi `Depreciation Expense – Admin Timeout {runId}-101`
18. Putus respons Save Edit lewat intercept jaringan (tidak ada respons)
19. Klik `[Save]`
20. Verifikasi toast `Connection problem. Please try again.` tampil
21. Lepas intercept respons Save Edit
22. Klik ikon ✕ pada modal Edit Account
23. Verifikasi dialog `Unsaved Changes` tampil
24. Klik `[Leave]`
25. Verifikasi jumlah entri `DID101A` pada Changelog sama dengan baseline langkah 15
26. Verifikasi jumlah entri `DID101A` pada System Log aktor sama dengan baseline langkah 15
27. Verifikasi jumlah entri `DID101A` pada Activity Log sama dengan baseline langkah 15
28. Klik `(←)` pada kotak Search

## Notes

- Pembagian TC lintas spec (S-05): TC-FA-COA-41 dan TC-FA-COA-303 ada di spec 066 (toast, modal, input, dan tidak ada perubahan tersimpan) dan di spec ini (asersi "tidak ada log"). Spec ini memuat pemicu Save Edit yang sama dengan baseline sendiri per TC (S-12); spec 066 tidak mengasersi log.
- Langkah 7 dan 20 (toast kegagalan hasil server) menjadi anchor positif bahwa respons sudah diproses sebelum asersi absence pada tiap surface log (bagian 8b butir 2 dan 11); tiga surface disebut satu per satu. Asersi absence ditulis sesudah intercept dilepas dan modal ditutup.
- Langkah penghubung (S-03, S-08, S-09, R-16, R-23): langkah 2 (Search sufiks `{runId}-101` sebagai penemu baris target) dan langkah 28 (mengosongkan Search); langkah 8 dan 21 (melepas intercept); langkah 9 sampai 11 dan 22 sampai 24 (menutup form dirty secara deterministik); langkah 1 dan 15 mencatat baseline sebelum aksi pemicu tiap TC dan bukan asersi.
- Temuan untuk QA:
  - TC-FA-COA-41 dan 303 menyebut "tidak ada log" tanpa surface; spec mengasersi Changelog, System Log aktor, dan Activity Log (PRD §8).
  - TC-FA-COA-41 dan 303 tidak menyebut cara menutup modal setelah kegagalan; spec memakai ✕, `Unsaved Changes`, `[Leave]` sebagai langkah penghubung.
  - TC-FA-COA-41 dan 303 memakai P1 sebagai target; spec memakai akun milik spec `DID101A` (S-06).
