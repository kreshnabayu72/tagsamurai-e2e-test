---
id: TC-FA-COA-E2E-096-absence-log-permintaan-langsung-atas-akun-terkunci-dan-akun-dipakai-asset-class-ditolak
title: "Absence Log: Permintaan Langsung atas Akun Terekspor dan Akun Dipakai Asset Class Ditolak Tidak Menulis Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-36
  - TC-FA-COA-124
  - TC-FA-COA-272
coverage:
  web: automated
---

# Absence Log: Permintaan Langsung atas Akun Terekspor dan Akun Dipakai Asset Class Ditolak Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Kelas harness g (asersi absence log). Pemicu adalah permintaan langsung ke server yang ditolak (kelas a) dan hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji (P-5). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Semua permintaan langsung memakai sesi API aktor Total Control (butir "Sesi API aktor" di `suite.md`); tidak ada ganti akun UI.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed disediakan tim FE/BE):
  - Akun terekspor: Code `DID096A`, Account Name `Akun Terekspor {runId}-096`, Function Capitalization Offset, Active, Used By 0, Last Used in Journal terisi (diekspor hook `before` lewat jalur Journal J-06 yang disediakan tim FE/BE); padanan P2 pada TC-FA-COA-36.
  - Akun dipakai Asset Class: Code `DID096B`, Account Name `Akun Dipakai {runId}-096`, Function Depreciation Expense, Active, Used By 1 oleh Asset Class `Asset Class Pemakai {runId}-096` yang dibuat hook `before` dan dihapus hook `after`; belum pernah diekspor; padanan P6 pada TC-FA-COA-124 dan TC-FA-COA-272.
  - Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `DID096A`, `DID096B`, dan `DID096X` memuat nomor spec supaya unik per spec dan dibersihkan di hook `before` dan `after` (R-13). `DID096X` adalah Code tujuan perubahan yang selalu ditolak (tidak pernah tersimpan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): klien HTTP untuk permintaan langsung (ubah Account Code, ubah Account Function, Deactivate) dengan sesi API aktor; kemampuan membaca dari server jumlah entri Changelog (per Account Code), System Log milik user aktor (Detail User > Tab System Log, kolom Name), dan Activity Log FAMS (kolom Name) untuk objek Chart of Accounts per Account Code. Jumlah entri dibaca sebagai baseline sebelum aksi pemicu tiap TC dan dibandingkan sesudahnya (S-12).
- Seed dan pemulihan mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.

## Test Steps

### TC-FA-COA-36: Ubah Account Code akun pernah diekspor

1. Catat baseline jumlah entri Account Code `DID096A` dan `DID096X` pada Changelog, System Log aktor, dan Activity Log dari server
2. Kirim permintaan ubah Account Code `DID096A` menjadi `DID096X` langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
3. Verifikasi permintaan ditolak server
4. Verifikasi jumlah entri `DID096A` dan `DID096X` pada Changelog sama dengan baseline langkah 1
5. Verifikasi jumlah entri `DID096A` dan `DID096X` pada System Log aktor sama dengan baseline langkah 1
6. Verifikasi jumlah entri `DID096A` dan `DID096X` pada Activity Log sama dengan baseline langkah 1

### TC-FA-COA-124: Ubah Account Function akun yang dipakai Asset Class

7. Catat baseline jumlah entri Account Code `DID096B` pada Changelog, System Log aktor, dan Activity Log dari server
8. Kirim permintaan ubah Account Function `DID096B` menjadi Asset Cost langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
9. Verifikasi permintaan ditolak server
10. Verifikasi jumlah entri `DID096B` pada Changelog sama dengan baseline langkah 7
11. Verifikasi jumlah entri `DID096B` pada System Log aktor sama dengan baseline langkah 7
12. Verifikasi jumlah entri `DID096B` pada Activity Log sama dengan baseline langkah 7

### TC-FA-COA-272: Deactivate akun yang dipakai Asset Class

13. Catat baseline jumlah entri Account Code `DID096B` pada Changelog, System Log aktor, dan Activity Log dari server
14. Kirim permintaan Deactivate `DID096B` langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
15. Verifikasi permintaan ditolak server dengan penolakan guard Deactivate (`FACO-LOGIC-02c`)
16. Verifikasi jumlah entri `DID096B` pada Changelog sama dengan baseline langkah 13
17. Verifikasi jumlah entri `DID096B` pada System Log aktor sama dengan baseline langkah 13
18. Verifikasi jumlah entri `DID096B` pada Activity Log sama dengan baseline langkah 13

## Notes

- Pembagian TC lintas spec (S-05): TC-FA-COA-36 dan TC-FA-COA-124 ada di spec 071 (penolakan server dan state data, kelas a) dan di spec ini (asersi "tidak ada log"); TC-FA-COA-272 ada di spec 072 (penolakan dengan guard dan status akun, kelas a) dan di spec ini (asersi "tidak ada entri log"). Spec ini memuat permintaan langsung yang sama dengan baseline sendiri per TC (S-12); spec 071 dan 072 tidak mengasersi log.
- Tanpa langkah UI: semua aksi adalah permintaan langsung (bagian 8b butir 1). Langkah 3, 9, dan 15 (penolakan server atas permintaan yang sama) menjadi anchor positif sebelum asersi absence pada tiap surface log (bagian 8b butir 2); tiga surface disebut satu per satu.
- Langkah 1, 7, dan 13 mencatat baseline sebelum aksi pemicu tiap TC (S-12) dan bukan asersi.
- Temuan untuk QA:
  - TC-FA-COA-36 dan 124 menyebut "tidak ada log" tanpa surface; spec mengasersi Changelog, System Log aktor, dan Activity Log (PRD §8).
  - TC-FA-COA-36 dan 124 memakai P2 dan P6 sebagai target; spec memakai akun milik spec `DID096A` dan `DID096B` dengan state yang sama (S-06). Keadaan "pernah diekspor" `DID096A` dibuat hook `before` lewat jalur J-06 yang disediakan tim FE/BE.
  - TC-FA-COA-36 menyebut Code tujuan `6-2002`; spec memakai `DID096X` karena akun asal adalah akun milik spec.
