---
id: TC-FA-COA-E2E-102-absence-log-bulk-activate-dan-deactivate-gagal-5xx
title: "Absence Log: Bulk Activate dan Bulk Deactivate Gagal 5xx Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-300
  - TC-FA-COA-301
coverage:
  web: automated
---

# Absence Log: Bulk Activate dan Bulk Deactivate Gagal 5xx Tidak Menulis Log

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons Bulk Activate dan Bulk Deactivate dipaksa lewat `Spectra.intercept()`, jumlah entri log dibaca dari backend nyata).
- Kelas harness g (asersi absence log). Pemicu adalah kegagalan 5xx yang dipaksa (kelas b) dan hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji (P-5). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed disediakan tim FE/BE):
  - Akun `DID102A` (Account Name `Akun Bulk A {runId}-102`) dan `DID102B` (Account Name `Akun Bulk B {runId}-102`): Function Gain on Disposal, Inactive, Used By 0; padanan P3 dan P4 pada TC-FA-COA-300.
  - Akun `DID102C` (Account Name `Akun Bulk C {runId}-102`) dan `DID102D` (Account Name `Akun Bulk D {runId}-102`): Function Depreciation Expense, Active, Used By 0; padanan P1 dan P5 pada TC-FA-COA-301.
  - Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `DID102A` sampai `DID102D` memuat nomor spec supaya unik per spec dan dibersihkan di hook `before` dan `after` (R-13).
- Kebutuhan intercept (kelas b; `Spectra.intercept()`, tanpa endpoint karangan): TC-FA-COA-300 respons Bulk Activate dipaksa 5xx; TC-FA-COA-301 respons Bulk Deactivate dipaksa 5xx. Intercept dilepas segera setelah pemicu diasersi dan dipulihkan di hook `after` bila spec gagal di tengah.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): kemampuan membaca dari server jumlah entri Changelog (per Account Code), System Log milik user aktor (Detail User > Tab System Log, kolom Name), dan Activity Log FAMS (kolom Name) untuk objek Chart of Accounts per Account Code, dibaca sebagai baseline sebelum aksi pemicu tiap TC (S-12).
- Seed dan pemulihan mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.

## Test Steps

### TC-FA-COA-300: Bulk Activate gagal 5xx

1. Catat baseline jumlah entri Account Code `DID102A` dan `DID102B` pada Changelog, System Log aktor, dan Activity Log dari server
2. Ketik Search `{runId}-102`, tekan Enter
3. Centang baris akun `DID102A`
4. Centang baris akun `DID102B`
5. Klik `Activate` pada Bulk Action Bar sehingga dialog D-15 terbuka
6. Paksa respons Bulk Activate menjadi 5xx lewat intercept jaringan
7. Klik `[Activate]` pada dialog D-15
8. Verifikasi toast `Error, failed to activate account.` tampil
9. Lepas intercept respons Bulk Activate
10. Klik `[Cancel]` pada dialog D-15
11. Lepas seleksi akun terpilih
12. Verifikasi jumlah entri `DID102A` dan `DID102B` pada Changelog sama dengan baseline langkah 1
13. Verifikasi jumlah entri `DID102A` dan `DID102B` pada System Log aktor sama dengan baseline langkah 1
14. Verifikasi jumlah entri `DID102A` dan `DID102B` pada Activity Log sama dengan baseline langkah 1

### TC-FA-COA-301: Bulk Deactivate gagal 5xx

15. Catat baseline jumlah entri Account Code `DID102C` dan `DID102D` pada Changelog, System Log aktor, dan Activity Log dari server
16. Centang baris akun `DID102C`
17. Centang baris akun `DID102D`
18. Klik `Deactivate` pada Bulk Action Bar sehingga dialog D-02 terbuka
19. Paksa respons Bulk Deactivate menjadi 5xx lewat intercept jaringan
20. Klik `[Deactivate]` pada dialog D-02
21. Verifikasi toast `Error, failed to deactivate account.` tampil
22. Lepas intercept respons Bulk Deactivate
23. Klik `[Cancel]` pada dialog D-02
24. Lepas seleksi akun terpilih
25. Verifikasi jumlah entri `DID102C` dan `DID102D` pada Changelog sama dengan baseline langkah 15
26. Verifikasi jumlah entri `DID102C` dan `DID102D` pada System Log aktor sama dengan baseline langkah 15
27. Verifikasi jumlah entri `DID102C` dan `DID102D` pada Activity Log sama dengan baseline langkah 15
28. Klik `(←)` pada kotak Search

## Notes

- Pembagian TC lintas spec (S-05): TC-FA-COA-300 dan TC-FA-COA-301 ada di spec 069 (dialog, seleksi, Bulk Action Bar, dan tabel disegarkan) dan di spec ini (asersi "tidak ada log untuk akun yang tidak berubah"). Spec ini memuat pemicu bulk yang sama dengan baseline sendiri per TC (S-12); spec 069 tidak mengasersi log.
- Langkah 8 dan 21 (toast kegagalan hasil server) menjadi anchor positif bahwa respons sudah diproses sebelum asersi absence pada tiap surface log (bagian 8b butir 2 dan 11); tiga surface disebut satu per satu. Asersi absence ditulis sesudah intercept dilepas dan dialog ditutup.
- Langkah penghubung (S-03, S-09, R-16, R-23): langkah 2 (Search sufiks `{runId}-102` menampilkan keempat akun milik spec sebagai penemu baris target; langkah 28 mengosongkannya); langkah 9 dan 22 (melepas intercept); langkah 10 dan 23 (menutup dialog dengan `[Cancel]`); langkah 11 dan 24 (melepas seleksi); langkah 1 dan 15 mencatat baseline sebelum aksi pemicu tiap TC dan bukan asersi. Pemilihan akun pada langkah 3, 4, 16, dan 17 adalah precondition TC.
- Temuan untuk QA:
  - TC-FA-COA-300 dan 301 menyebut "tidak ada log untuk akun yang tidak berubah" tanpa surface; spec mengasersi Changelog, System Log aktor, dan Activity Log (PRD §8).
  - TC-FA-COA-300 dan 301 memakai P1, P3, P4, dan P5 sebagai target; spec memakai akun milik spec `DID102A` sampai `DID102D` (S-06).
  - Label tombol `[Cancel]` pada dialog D-02 dan D-15 diambil dari rumpun TC yang sama (bukan dari baris sumber spec ini).
