---
id: TC-FA-COA-E2E-095-absence-log-permintaan-langsung-ditolak-role-create-update-dan-delete
title: "Absence Log: Permintaan Langsung Ditolak Role Create, Update, dan Delete Tidak Menulis Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-269
  - TC-FA-COA-270
  - TC-FA-COA-271
coverage:
  web: automated
---

# Absence Log: Permintaan Langsung Ditolak Role Create, Update, dan Delete Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Kelas harness g (asersi absence log). Pemicu adalah permintaan langsung ke server yang ditolak (kelas a) dan hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji (P-5). Suite berjalan serial (`parallel: false`).
- Akun login hook `before` spec ini: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun UI: semua permintaan langsung memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- Aktor permintaan langsung (sesi API aktor; email mengikuti tabel Pre-setup TC):

  | TC | Aktor | Email | Password |
  |---|---|---|---|
  | TC-FA-COA-269 | Manage accounting - Create | `manageAccountingCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_CREATE_PASSWORD` |
  | TC-FA-COA-270 | Manage accounting - Update | `manageAccountingUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_UPDATE_PASSWORD` |
  | TC-FA-COA-271 | Manage accounting - Delete | `manageAccountingDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_DELETE_PASSWORD` |

- Env var `FA_TC_PASSWORD`, `FA_MACC_CREATE_PASSWORD`, `FA_MACC_UPDATE_PASSWORD`, dan `FA_MACC_DELETE_PASSWORD` terdaftar di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed disediakan tim FE/BE), pada client yang sama dengan akun aktor:
  - Akun target aktif: Code `DID095A`, Account Name `Akun Target Aktif {runId}-095`, Function Depreciation Expense, Active, Used By 0, belum pernah diekspor (padanan P1 pada TC-FA-COA-269, 270, 271).
  - Akun target nonaktif: Code `DID095B`, Account Name `Akun Target Nonaktif {runId}-095`, Function Gain on Disposal, Inactive, Used By 0, belum pernah diekspor (padanan P3 pada TC-FA-COA-269, 270, 271).
  - Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `DID095A` dan `DID095B` memuat nomor spec supaya unik per spec, sedangkan `CAP-8300` dan `CAP-8304` adalah nilai TC untuk permintaan Create yang selalu ditolak 403 dan tidak pernah tersimpan, sehingga tidak masuk daftar pembersihan; spec 070 juga mengetik kedua Code itu pada permintaan Create yang sama-sama selalu ditolak (pengecualian A-18). `DID095A` dan `DID095B` dibersihkan di hook `before` dan `after` (R-13).
  - Name bersuffix `{runId}-095` dipakai pada payload Edit `Akun Edit Bypass {runId}-095` dan Create `Akun Create {runId}-095`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): klien HTTP untuk permintaan langsung (Create, Edit, Delete, Activate, Deactivate) dengan sesi API aktor; kemampuan membaca dari server jumlah entri Changelog (per Account Code), System Log milik user aktor permintaan (Detail User > Tab System Log, kolom Name), dan Activity Log FAMS (kolom Name) untuk objek Chart of Accounts per Account Code. Jumlah entri dibaca sebagai baseline sebelum aksi pemicu tiap TC dan dibandingkan sesudahnya (S-12).
- Seed dan pemulihan mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.

## Test Steps

### TC-FA-COA-269: Manage accounting - Create

1. Catat baseline jumlah entri Account Code `DID095A` dan `DID095B` pada Changelog, System Log aktor Manage accounting - Create, dan Activity Log dari server
2. Kirim permintaan Edit Account Name `DID095A` menjadi `Akun Edit Bypass {runId}-095` langsung ke server menggunakan sesi API aktor Manage accounting - Create hingga respons diterima
3. Kirim permintaan Activate `DID095B` langsung ke server menggunakan sesi API aktor Manage accounting - Create hingga respons diterima
4. Kirim permintaan Deactivate `DID095A` langsung ke server menggunakan sesi API aktor Manage accounting - Create hingga respons diterima
5. Kirim permintaan Delete `DID095A` langsung ke server menggunakan sesi API aktor Manage accounting - Create hingga respons diterima
6. Verifikasi setiap permintaan pada langkah 2 sampai 5 ditolak server dengan 403
7. Verifikasi jumlah entri `DID095A` dan `DID095B` pada Changelog sama dengan baseline langkah 1
8. Verifikasi jumlah entri `DID095A` dan `DID095B` pada System Log aktor sama dengan baseline langkah 1
9. Verifikasi jumlah entri `DID095A` dan `DID095B` pada Activity Log sama dengan baseline langkah 1

### TC-FA-COA-270: Manage accounting - Update

10. Catat baseline jumlah entri Account Code `DID095A`, `DID095B`, dan `CAP-8300` pada Changelog, System Log aktor Manage accounting - Update, dan Activity Log dari server
11. Kirim permintaan Create akun Code `CAP-8300`, Account Name `Akun Create {runId}-095`, Function Depreciation Expense langsung ke server menggunakan sesi API aktor Manage accounting - Update hingga respons diterima
12. Kirim permintaan Delete `DID095A` langsung ke server menggunakan sesi API aktor Manage accounting - Update hingga respons diterima
13. Verifikasi setiap permintaan pada langkah 11 dan 12 ditolak server dengan 403
14. Verifikasi jumlah entri `DID095A`, `DID095B`, dan `CAP-8300` pada Changelog sama dengan baseline langkah 10
15. Verifikasi jumlah entri `DID095A`, `DID095B`, dan `CAP-8300` pada System Log aktor sama dengan baseline langkah 10
16. Verifikasi jumlah entri `DID095A`, `DID095B`, dan `CAP-8300` pada Activity Log sama dengan baseline langkah 10

### TC-FA-COA-271: Manage accounting - Delete

17. Catat baseline jumlah entri Account Code `DID095A`, `DID095B`, dan `CAP-8304` pada Changelog, System Log aktor Manage accounting - Delete, dan Activity Log dari server
18. Kirim permintaan Create akun Code `CAP-8304`, Account Name `Akun Create {runId}-095`, Function Depreciation Expense langsung ke server menggunakan sesi API aktor Manage accounting - Delete hingga respons diterima
19. Kirim permintaan Edit Account Name `DID095A` menjadi `Akun Edit Bypass {runId}-095` langsung ke server menggunakan sesi API aktor Manage accounting - Delete hingga respons diterima
20. Kirim permintaan Activate `DID095B` langsung ke server menggunakan sesi API aktor Manage accounting - Delete hingga respons diterima
21. Kirim permintaan Deactivate `DID095A` langsung ke server menggunakan sesi API aktor Manage accounting - Delete hingga respons diterima
22. Verifikasi setiap permintaan pada langkah 18 sampai 21 ditolak server dengan 403
23. Verifikasi jumlah entri `DID095A`, `DID095B`, dan `CAP-8304` pada Changelog sama dengan baseline langkah 17
24. Verifikasi jumlah entri `DID095A`, `DID095B`, dan `CAP-8304` pada System Log aktor sama dengan baseline langkah 17
25. Verifikasi jumlah entri `DID095A`, `DID095B`, dan `CAP-8304` pada Activity Log sama dengan baseline langkah 17

## Notes

- `P-5`: spec absence (kelas g) memuat pemicu kelas a (permintaan langsung ke server yang ditolak 403) yang hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC punya baseline sendiri (langkah 1, 10, 17).
- Spec memuat tiga aktor (Manage accounting - Create, Update, dan Delete); tiap langkah permintaan langsung menyebut sesi API aktornya secara eksplisit (bagian 3, Tidak boleh butir c), sehingga tidak ada pergantian sesi UI.
- Pembagian TC lintas spec (S-05): TC-FA-COA-269, TC-FA-COA-270, dan TC-FA-COA-271 ada di spec 070 (respons 403 dan state data, kelas a) dan di spec ini (asersi "tidak ada log"). Spec ini memuat permintaan langsung yang sama dengan baseline sendiri per TC (S-12); spec 070 tidak mengasersi log.
- Tanpa langkah UI: semua aksi adalah permintaan langsung (bagian 8b butir 1). Langkah 6, 13, dan 22 (respons 403 atas permintaan yang sama) menjadi anchor positif sebelum asersi absence pada tiap surface log (bagian 8b butir 2); tiga surface disebut satu per satu.
- Langkah 1, 10, dan 17 mencatat baseline sebelum aksi pemicu pertama tiap TC (S-12) dan bukan asersi. Baseline Create (`CAP-8300`, `CAP-8304`) mencatat entri Account Code yang tidak pernah dibuat.
- `A-18`: Account Code literal tanpa suffix menjadi objek asersi: `DID095A` dan `DID095B` (TC-FA-COA-269, 270, 271: jumlah entri log sama dengan baseline; langkah 7 sampai 9, 14 sampai 16, 23 sampai 25), `CAP-8300` (TC-FA-COA-270; langkah 14 sampai 16), dan `CAP-8304` (TC-FA-COA-271; langkah 23 sampai 25). `DID095A` dan `DID095B` dibersihkan di hook `before` dan `after`; `CAP-8300` dan `CAP-8304` hanya diketik pada Create yang selalu ditolak 403 dan tidak pernah tersimpan.
- Temuan untuk QA:
  - TC-FA-COA-269, 270, 271 Post Condition "Data akun P1 dan P3 tidak berubah" tidak punya Expected padanan; state data dicek di spec 070, bukan di spec ini. Klausa "tidak ada log" diasersi di sini dengan akun milik spec `DID095A` dan `DID095B` sebagai padanan P1 dan P3 (S-06).
  - TC tidak menyebut surface log; spec mengasersi Changelog, System Log aktor, dan Activity Log (PRD §8).
  - TC-FA-COA-269, 270, 271 tidak menyebut payload Edit dan Create; spec memakai `Akun Edit Bypass {runId}-095` dan `Akun Create {runId}-095` dengan Function Depreciation Expense.
