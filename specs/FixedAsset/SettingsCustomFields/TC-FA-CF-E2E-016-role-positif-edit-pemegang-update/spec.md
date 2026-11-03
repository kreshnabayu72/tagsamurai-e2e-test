---
id: TC-FA-CF-E2E-016-role-positif-edit-pemegang-update
title: "Role Positif: Pemegang Update Menyelesaikan Edit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-43
coverage:
  web: automated
---

# Role Positif: Pemegang Update Menyelesaikan Edit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji:

| Role | Akun (Pre-setup) | Env password |
|---|---|---|
| Master-Update (Update dan Read) | #6 `masterUpdate_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha | `Spectra.env.FA_MU_PASSWORD` |

- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru (`FA_MU_PASSWORD`) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Dinamis: field `Storage Capacity {runId}-016` (Numeric 0 Decimal Places, Scope `Generator` dan `Pump`, padanan bersuffix `Storage Capacity` milik spec) di-seed lewat API di hook `before` (kemampuan seeding disediakan tim FE/BE; seeding tidak memakai akun aktor yang hanya pemegang Update dan Read); target Edit adalah field ini. Nama baru `Storage Capacity Updated {runId}-016`. Cleanup hook `after`: hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-016`.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah selain data field milik spec (dibersihkan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `{runId}-016`, tekan Enter
2. Buka menu row action baris `Storage Capacity {runId}-016`
3. Klik row action `Edit`
4. Ubah Field Name menjadi `Storage Capacity Updated {runId}-016`
5. Klik `[Save]`
6. Verifikasi toast sukses `Success, custom field has been updated.` tampil
7. Verifikasi modal Edit tertutup
8. Verifikasi baris menampilkan Field Name `Storage Capacity Updated {runId}-016`
9. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md` (TC-FA-CF-43). Spec positif untuk aksi Edit (bagian 3a); pemegang Update saja.
- Toast (langkah 6) diasersi sebelum modal tertutup (langkah 7) mengikuti 8b butir 5, meski Expected a TC menyebut modal lebih dahulu.
- Target Edit memakai field milik spec `Storage Capacity {runId}-016`, padanan bersuffix baris Pre-setup `Storage Capacity` yang disebut TC-FA-CF-43 (S-06); Field Name pada TC (`Storage Capacity`, `Storage Capacity Updated`) ditulis dengan suffix (R-06).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search `{runId}-016` untuk menemukan baris target (langkah 1, R-16; kata kunci memuat nama sebelum dan sesudah rename) dan `(←)` untuk mereset Search (langkah 9).
- Nama field hasil rename bersuffix `{runId}-016` (S-12).
- Temuan untuk QA:
  - TC-FA-CF-43 menyebut baris Pre-setup `Storage Capacity` sebagai target Edit, yang juga dipakai TC lain; spec memakai padanan bersuffix milik spec.
