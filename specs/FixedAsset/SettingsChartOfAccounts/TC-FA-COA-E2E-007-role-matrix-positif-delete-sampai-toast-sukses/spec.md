---
id: TC-FA-COA-E2E-007-role-matrix-positif-delete-sampai-toast-sukses
title: "Role Matrix Positif: Delete sampai Toast Sukses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-267
  - TC-FA-COA-268
coverage:
  web: automated
---

# Role Matrix Positif: Delete sampai Toast Sukses

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (bagian 3a):

| Role | Akun | Env password | TC |
|---|---|---|---|
| Manage accounting – Delete (login di hook `before`) | `manageAccountingDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MACC_DELETE_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; perlu didaftarkan tim FE) | TC-FA-COA-267, 268 |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (target hapus sekali pakai; seed idempotent mengembalikannya sebelum run berikutnya): P78 `CAP-8208 – Capitalization Clearing – Delete Only Single`, P79 `CAP-8209 – Capitalization Clearing – Delete Only Bulk A`, dan P80 `CAP-8210 – Capitalization Clearing – Delete Only Bulk B`; seluruhnya Function Capitalization Offset, Active, Used By 0, Last Used in Journal kosong, belum pernah diekspor, dan bukan nilai default company.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` untuk akun aktor yang dipakai, termasuk akun role di tabel (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-chart-of-accounts.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-267: Manage accounting – Delete dapat menghapus akun single sampai toast sukses

1. Ketik Search `CAP-8208`, tekan Enter
2. Klik row action `Delete` pada akun P78
3. Klik `[Delete]` pada dialog D-07
4. Verifikasi toast `Success, account has been deleted.`
5. Verifikasi akun P78 hilang dari tabel

### TC-FA-COA-268: Manage accounting – Delete dapat menjalankan Bulk Delete sampai toast sukses

6. Ganti isi kotak search dengan `Delete Only Bulk`, tekan Enter
7. Centang P79 dan P80
8. Klik Bulk `Delete`
9. Klik `[Delete]` pada dialog D-08
10. Verifikasi toast `Success, account has been deleted.`
11. Verifikasi kedua akun P79 dan P80 hilang dari tabel
12. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Role Matrix positif (bagian 3a, `[KEPUTUSAN 2026-11-02]`): satu spec memuat dua aksi (Delete single dan Bulk Delete) dengan polaritas seragam dan satu role (Manage accounting – Delete); aksi hapus di akhir spec (S-10), Delete single lebih dulu lalu Bulk Delete.
- Langkah penghubung (S-03): langkah 1 dan 6 (Search untuk menampilkan akun target sebelum aksi pada baris itu; R-16, bagian 8b butir 9 dan 12); langkah 12 (menutup Search dan mereset tabel, S-09). Pembukaan menu ⋯ untuk row action `Delete` ditulis dalam langkah 2.
- Asersi absence "hilang dari tabel" (langkah 5 dan 11) memakai toast sukses hapus (langkah 4 dan 10) sebagai anchor (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-COA-267 dan 268 Post Condition ("dihapus permanen; log L-04 tercatat") tidak punya langkah observasi untuk log; hanya toast dan hilangnya baris yang diasersi.
