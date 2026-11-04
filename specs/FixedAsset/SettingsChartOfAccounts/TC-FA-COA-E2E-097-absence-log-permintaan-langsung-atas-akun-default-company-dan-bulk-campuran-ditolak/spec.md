---
id: TC-FA-COA-E2E-097-absence-log-permintaan-langsung-atas-akun-default-company-dan-bulk-campuran-ditolak
title: "Absence Log: Permintaan Langsung Delete Akun Terpakai, Akun Default Company, dan Bulk Deactivate Campuran Tidak Menulis Log untuk Akun Terblokir"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-273
  - TC-FA-COA-274
  - TC-FA-COA-275
coverage:
  web: automated
---

# Absence Log: Permintaan Langsung Delete Akun Terpakai, Akun Default Company, dan Bulk Deactivate Campuran Tidak Menulis Log untuk Akun Terblokir

## Prerequisites

- Mode: FE+BE.
- Kelas harness g (asersi absence log). Pemicu adalah permintaan langsung ke server yang ditolak (kelas a) dan hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji (P-5). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Semua permintaan langsung memakai sesi API aktor Total Control (butir "Sesi API aktor" di `suite.md`); tidak ada ganti akun UI.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed disediakan tim FE/BE):
  - Akun dipakai Asset Class: Code `DID097A`, Account Name `Akun Dipakai {runId}-097`, Function Depreciation Expense, Active, Used By 1 oleh Asset Class `Asset Class Pemakai {runId}-097` yang dibuat hook `before` dan dihapus hook `after`; belum pernah diekspor; padanan P6 pada TC-FA-COA-273 dan 275.
  - Akun default company: Code `DID097B`, Account Name `Akun Default Gain {runId}-097`, Function Gain on Disposal, Active, Used By 0; menjadi Default Gain on Disposal (`SET-05`) di Settings > Accounting > Preferences; padanan P28 pada TC-FA-COA-274.
  - Akun eligible: Code `DID097C`, Account Name `Akun Eligible {runId}-097`, Function Capitalization Offset, Active, Used By 0, belum pernah diekspor; padanan P86 pada TC-FA-COA-275. Langkah 14 menjadikannya Inactive.
  - Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `DID097A`, `DID097B`, dan `DID097C` memuat nomor spec supaya unik per spec dan dibersihkan di hook `before` dan `after` (R-13).
- State global: spec mengubah nilai Default Gain on Disposal di Settings > Accounting > Preferences menjadi `DID097B`. Hook `before` menyimpan nilai awal dan menyetel `DID097B` sebagai default, hook `after` memulihkan nilai awal sebelum menghapus `DID097B` (R-08). Kemampuan menyetel dan memulihkan nilai default company disediakan tim FE/BE; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): klien HTTP untuk permintaan langsung (Delete, Bulk Deactivate) dengan sesi API aktor; pembacaan akun dari server beserta status; kemampuan membaca dari server jumlah entri Changelog (per Account Code), System Log milik user aktor (Detail User > Tab System Log, kolom Name), dan Activity Log FAMS (kolom Name) untuk objek Chart of Accounts per Account Code. Jumlah entri dibaca sebagai baseline sebelum aksi pemicu tiap TC dan dibandingkan sesudahnya (S-12).
- Seed dan pemulihan mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.

## Test Steps

### TC-FA-COA-273: Delete akun yang dipakai Asset Class

1. Catat baseline jumlah entri Account Code `DID097A` pada Changelog, System Log aktor, dan Activity Log dari server
2. Kirim permintaan Delete `DID097A` langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
3. Verifikasi permintaan ditolak server dengan penolakan Guard 2 (`FACO-LOGIC-03`)
4. Verifikasi jumlah entri `DID097A` pada Changelog sama dengan baseline langkah 1
5. Verifikasi jumlah entri `DID097A` pada System Log aktor sama dengan baseline langkah 1
6. Verifikasi jumlah entri `DID097A` pada Activity Log sama dengan baseline langkah 1

### TC-FA-COA-274: Delete akun nilai default company

7. Catat baseline jumlah entri Account Code `DID097B` pada Changelog, System Log aktor, dan Activity Log dari server
8. Kirim permintaan Delete `DID097B` langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
9. Verifikasi permintaan ditolak server
10. Verifikasi jumlah entri `DID097B` pada Changelog sama dengan baseline langkah 7
11. Verifikasi jumlah entri `DID097B` pada System Log aktor sama dengan baseline langkah 7
12. Verifikasi jumlah entri `DID097B` pada Activity Log sama dengan baseline langkah 7

### TC-FA-COA-275: Bulk Deactivate campuran akun terpakai dan akun eligible

13. Catat baseline jumlah entri Account Code `DID097A` pada Changelog, System Log aktor, dan Activity Log dari server
14. Kirim permintaan Bulk Deactivate untuk `DID097A` dan `DID097C` langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
15. Verifikasi akun `DID097C` menjadi Inactive pada data dari server
16. Verifikasi jumlah entri `DID097A` pada Changelog sama dengan baseline langkah 13
17. Verifikasi jumlah entri `DID097A` pada System Log aktor sama dengan baseline langkah 13
18. Verifikasi jumlah entri `DID097A` pada Activity Log sama dengan baseline langkah 13

## Notes

- Pembagian TC lintas spec (S-05): TC-FA-COA-273, TC-FA-COA-274, dan TC-FA-COA-275 ada di spec 072 (penolakan server, status akun, dan keberadaan akun, kelas a) dan di spec ini (asersi "tidak ada entri log" dan "tidak ada log untuk P6"). Spec ini memuat permintaan langsung yang sama dengan baseline sendiri per TC (S-12); spec 072 tidak mengasersi log.
- Tanpa langkah UI: semua aksi adalah permintaan langsung (bagian 8b butir 1). Langkah 3 dan 9 (penolakan server) dan langkah 15 (akun eligible menjadi Inactive, bukti respons Bulk Deactivate diproses) menjadi anchor positif sebelum asersi absence pada tiap surface log (bagian 8b butir 2); tiga surface disebut satu per satu.
- Langkah 1, 7, dan 13 mencatat baseline sebelum aksi pemicu tiap TC (S-12) dan bukan asersi. Baseline TC-FA-COA-275 hanya untuk `DID097A` karena Expected a menyebut tidak ada log untuk akun terblokir.
- Temuan untuk QA:
  - TC-FA-COA-273, 274, 275 menyebut "tidak ada entri log" tanpa surface; spec mengasersi Changelog, System Log aktor, dan Activity Log (PRD §8).
  - TC-FA-COA-275 Post Condition "Log L-03 hanya untuk P86" tidak punya langkah observasi di TC sehingga tidak diasersi (S-01); spec hanya mengasersi tidak adanya entri untuk akun terblokir.
  - TC-FA-COA-273, 274, 275 memakai P6, P28, dan P86 sebagai target; spec memakai akun milik spec `DID097A`, `DID097B`, dan `DID097C` (S-06). Menyetel akun milik spec sebagai nilai default company mengubah state global Preferences sehingga dipulihkan hook `after`; perlu dikonfirmasi tim FE/BE bahwa nilai default company dapat disetel lewat seed.
