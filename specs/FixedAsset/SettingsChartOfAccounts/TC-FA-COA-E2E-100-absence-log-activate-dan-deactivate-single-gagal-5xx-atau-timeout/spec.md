---
id: TC-FA-COA-E2E-100-absence-log-activate-dan-deactivate-single-gagal-5xx-atau-timeout
title: "Absence Log: Activate dan Deactivate Single Timeout Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-304
  - TC-FA-COA-361
coverage:
  web: automated
---

# Absence Log: Activate dan Deactivate Single Timeout Tidak Menulis Log

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons Deactivate dan Activate dipaksa lewat `Spectra.intercept()`, jumlah entri log dibaca dari backend nyata).
- Kelas harness g (asersi absence log). Pemicu adalah timeout yang dipaksa (kelas b) dan hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji (P-5). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed disediakan tim FE/BE):
  - Akun A: Code `DID100A`, Account Name `Akun Status A {runId}-100`, Function Depreciation Expense, Active, Used By 0 (padanan P1 pada TC-FA-COA-304).
  - Akun B: Code `DID100B`, Account Name `Akun Status B {runId}-100`, Function Gain on Disposal, Inactive, Used By 0 (padanan P3 pada TC-FA-COA-361).
  - Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `DID100A` dan `DID100B` memuat nomor spec supaya unik per spec dan dibersihkan di hook `before` dan `after` (R-13).
- Kebutuhan intercept (kelas b; `Spectra.intercept()`, tanpa endpoint karangan): TC-FA-COA-304 respons Deactivate tidak diberikan (timeout); TC-FA-COA-361 respons Activate tidak diberikan (timeout). Intercept dilepas segera setelah pemicu diasersi dan dipulihkan di hook `after` bila spec gagal di tengah.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): kemampuan membaca dari server jumlah entri Changelog (per Account Code), System Log milik user aktor (Detail User > Tab System Log, kolom Name), dan Activity Log FAMS (kolom Name) untuk objek Chart of Accounts per Account Code, dibaca sebagai baseline sebelum aksi pemicu tiap TC (S-12).
- Seed dan pemulihan mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.

## Test Steps

### TC-FA-COA-304: Timeout saat Deactivate

1. Catat baseline jumlah entri Account Code `DID100A` pada Changelog, System Log aktor, dan Activity Log dari server
2. Ketik Search `{runId}-100`, tekan Enter
3. Klik switch Status pada baris akun `DID100A` sehingga dialog Deactivate (D-01) terbuka
4. Putus respons Deactivate lewat intercept jaringan (tidak ada respons)
5. Klik `[Deactivate]` pada dialog D-01
6. Verifikasi toast `Connection problem. Please try again.` tampil
7. Lepas intercept respons Deactivate
8. Klik `[Cancel]` pada dialog D-01
9. Verifikasi jumlah entri `DID100A` pada Changelog sama dengan baseline langkah 1
10. Verifikasi jumlah entri `DID100A` pada System Log aktor sama dengan baseline langkah 1
11. Verifikasi jumlah entri `DID100A` pada Activity Log sama dengan baseline langkah 1

### TC-FA-COA-361: Timeout saat Activate

12. Catat baseline jumlah entri Account Code `DID100B` pada Changelog, System Log aktor, dan Activity Log dari server
13. Klik switch Status pada baris akun `DID100B` sehingga dialog konfirmasi Activate (D-14) terbuka
14. Putus respons Activate lewat intercept jaringan (tidak ada respons)
15. Klik `[Activate]` pada dialog D-14
16. Verifikasi toast `Connection problem. Please try again.` tampil
17. Lepas intercept respons Activate
18. Klik `[Cancel]` pada dialog D-14
19. Verifikasi jumlah entri `DID100B` pada Changelog sama dengan baseline langkah 12
20. Verifikasi jumlah entri `DID100B` pada System Log aktor sama dengan baseline langkah 12
21. Verifikasi jumlah entri `DID100B` pada Activity Log sama dengan baseline langkah 12
22. Klik `(←)` pada kotak Search

## Notes

- Pembagian TC lintas spec (S-05): TC-FA-COA-304 dan TC-FA-COA-361 ada di spec 067 (toast, dialog, dan switch kembali) dan di spec ini (asersi "tidak ada log"). Spec ini memuat pemicu timeout yang sama dengan baseline sendiri per TC (S-12); spec 067 tidak mengasersi log.
- Langkah 6 dan 16 (toast koneksi hasil intercept) menjadi anchor positif bahwa respons sudah diproses sebelum asersi absence pada tiap surface log (bagian 8b butir 2 dan 11); tiga surface disebut satu per satu. Asersi absence ditulis sesudah intercept dilepas dan dialog ditutup.
- Langkah penghubung (S-03, S-09, R-16, R-23): langkah 2 (Search sufiks `{runId}-100` sebagai penemu baris target) dan langkah 22 (mengosongkan Search); langkah 3 dan 13 (membuka dialog konfirmasi lewat switch Status, precondition TC); langkah 7 dan 17 (melepas intercept); langkah 8 dan 18 (menutup dialog dengan `[Cancel]`); langkah 1 dan 12 mencatat baseline sebelum aksi pemicu tiap TC dan bukan asersi.
- Temuan untuk QA:
  - TC-FA-COA-304 dan 361 menyebut "tidak ada log" tanpa surface; spec mengasersi Changelog, System Log aktor, dan Activity Log (PRD §8).
  - TC-FA-COA-304 dan 361 tidak menyebut cara menutup dialog setelah kegagalan; `[Cancel]` dipakai sebagai langkah penghubung.
