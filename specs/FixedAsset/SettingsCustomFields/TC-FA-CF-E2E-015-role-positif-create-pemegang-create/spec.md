---
id: TC-FA-CF-E2E-015-role-positif-create-pemegang-create
title: "Role Positif: Pemegang Create Menyelesaikan Create"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-42
coverage:
  web: automated
---

# Role Positif: Pemegang Create Menyelesaikan Create

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji:

| Role | Akun (Pre-setup) | Env password |
|---|---|---|
| Master-Create (Create dan Read) | #5 `masterCreate_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha | `Spectra.env.FA_MC_PASSWORD` |

- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru (`FA_MC_PASSWORD`) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12), dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis: field `Create Only Field {runId}-015` (Text) dibuat spec pada langkah 1 sampai 4 dan dihapus hook `after` (seed reset Company).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah selain data field Company Alpha (dipulihkan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik `[+ Custom Field]`
2. Isi Field Name `Create Only Field {runId}-015`
3. Pilih Data Type `Text`
4. Klik `[Submit]`
5. Verifikasi toast sukses `Success, custom field has been created.` tampil
6. Verifikasi modal Create tertutup
7. Verifikasi baris `Create Only Field {runId}-015` tampil di tabel tab General
8. Verifikasi switch Active baris `Create Only Field {runId}-015` pada posisi ON

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md` (TC-FA-CF-42). Spec positif untuk aksi Create (bagian 3a); pemegang Create saja tanpa role lain.
- Toast (langkah 5) diasersi sebelum modal tertutup (langkah 6) mengikuti 8b butir 5 (state sementara tepat waktu), meski Expected a TC menyebut modal lebih dahulu.
- Nama field Dinamis bersuffix `{runId}-015` (S-12); Expected TC menyebut `Create Only Field` tanpa suffix.
- Temuan untuk QA:
  - TC-FA-CF-42 tidak menyebut field wajib lain pada form Create selain Field Name dan Data Type; spec hanya mengisi yang disebut TC.
