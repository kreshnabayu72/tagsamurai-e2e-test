---
id: TC-FA-CF-E2E-018-role-positif-delete-pemegang-delete
title: "Role Positif: Pemegang Delete Delete dan Bulk Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-46
  - TC-FA-CF-47
coverage:
  web: automated
---

# Role Positif: Pemegang Delete Delete dan Bulk Delete

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji:

| Role | Akun (Pre-setup) | Env password |
|---|---|---|
| Master-Delete (Delete dan Read) | #7 `masterDelete_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha | `Spectra.env.FA_MD_PASSWORD` |

- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru (`FA_MD_PASSWORD`) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Dinamis: field `Legacy Tag {runId}-018` (target TC-FA-CF-46), serta `Legacy Tag B {runId}-018` dan `Compliance File {runId}-018` (target TC-FA-CF-47), semuanya Text dan padanan bersuffix milik spec, di-seed lewat API di hook `before` (kemampuan seeding disediakan tim FE/BE; seeding tidak memakai akun aktor). Cleanup hook `after`: hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-018`.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah selain data field milik spec (dibersihkan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-46: Menghapus satu custom field sampai sukses

1. Ketik Search `{runId}-018`, tekan Enter
2. Buka menu row action baris `Legacy Tag {runId}-018`
3. Klik row action `Delete`
4. Verifikasi dialog `Delete Custom Field` tampil
5. Klik `[Delete]` pada dialog
6. Verifikasi toast sukses `Success, custom field has been deleted.` tampil
7. Verifikasi baris `Legacy Tag {runId}-018` hilang dari tabel

### TC-FA-CF-47: Bulk Delete sampai sukses

8. Centang baris `Legacy Tag B {runId}-018` dan `Compliance File {runId}-018`
9. Klik `[Delete]` pada Bulk Action Bar
10. Verifikasi dialog `Delete Custom Fields` memuat dua bullet
11. Tunggu toast lama hilang otomatis
12. Klik `[Delete]` pada dialog
13. Verifikasi toast sukses `Success, custom field has been deleted.` tampil
14. Verifikasi baris `Legacy Tag B {runId}-018` dan `Compliance File {runId}-018` hilang dari tabel
15. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Spec positif untuk aksi Delete dan Bulk Delete (bagian 3a); pemegang Delete saja. Aksi hapus berada di akhir spec (S-10). Subjudul `###` memetakan langkah ke id TC granular.
- Target aksi memakai field milik spec bersuffix `{runId}-018`, padanan baris Pre-setup `Legacy Tag` dan `Compliance File` yang disebut TC-FA-CF-46 dan 47 (S-06, R-06). TC-FA-CF-47 memakai `Legacy Tag B {runId}-018` sebagai padanan `Legacy Tag` karena field target TC-FA-CF-46 sudah terhapus (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search `{runId}-018` menemukan baris target (langkah 1, R-16) dan `(←)` mereset Search (langkah 15).
- Absence baris hilang (langkah 7 dan 14) beranchor toast sukses yang diasersi sebelumnya (langkah 6 dan 13; 8b butir 2).
- Langkah penghubung toast (S-03, R-22): langkah 11 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-47 Dependensi `-` tetapi memakai baris `Legacy Tag` yang sudah dihapus TC-FA-CF-46 bila dijalankan berurutan; spec memakai padanan kedua `Legacy Tag B {runId}-018`.
  - Kedua TC menghapus baris Pre-setup yang dipakai TC lain; spec memakai padanan bersuffix milik spec.
