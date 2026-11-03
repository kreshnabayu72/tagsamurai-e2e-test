---
id: TC-FA-CF-E2E-017-role-positif-toggle-pemegang-update
title: "Role Positif: Pemegang Update Toggle Status dan Bulk Deactivate"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-44
  - TC-FA-CF-45
coverage:
  web: automated
---

# Role Positif: Pemegang Update Toggle Status dan Bulk Deactivate

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji:

| Role | Akun (Pre-setup) | Env password |
|---|---|---|
| Master-Update (Update dan Read) | #6 `masterUpdate_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha | `Spectra.env.FA_MU_PASSWORD` |

- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru (`FA_MU_PASSWORD`) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Dinamis: field `Asset Serial Tag {runId}-017` dan `Legacy Tag {runId}-017` (Text, Active, padanan bersuffix milik spec) di-seed lewat API di hook `before` (kemampuan seeding disediakan tim FE/BE; seeding tidak memakai akun aktor). Cleanup hook `after`: hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-017`.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah selain data field milik spec (dibersihkan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-44: Menonaktifkan field lewat switch dan dialog konfirmasi

1. Ketik Search `{runId}-017`, tekan Enter
2. Geser switch Active baris `Asset Serial Tag {runId}-017` ke OFF
3. Verifikasi dialog `Deactivate Custom Field` tampil
4. Klik `[Deactivate]` pada dialog
5. Verifikasi toast sukses `Success, custom field has been deactivated.` tampil
6. Verifikasi switch Active baris `Asset Serial Tag {runId}-017` pada posisi OFF
7. Geser switch Active baris `Asset Serial Tag {runId}-017` ke ON dan konfirmasi dialog agar baris kembali Active sebelum TC-FA-CF-45

### TC-FA-CF-45: Bulk Deactivate sampai sukses

8. Centang baris `Asset Serial Tag {runId}-017` dan `Legacy Tag {runId}-017`
9. Klik `[Deactivate]` pada Bulk Action Bar
10. Verifikasi dialog `Deactivate Custom Fields` memuat bullet `Asset Serial Tag {runId}-017` dan `Legacy Tag {runId}-017`
11. Tunggu toast lama hilang otomatis
12. Klik `[Deactivate]` pada dialog
13. Verifikasi toast sukses `Success, custom field has been deactivated.` tampil
14. Verifikasi switch Active baris `Asset Serial Tag {runId}-017` dan `Legacy Tag {runId}-017` pada posisi OFF
15. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Spec positif untuk aksi Toggle Active dan Bulk Deactivate (bagian 3a); pemegang Update saja. Subjudul `###` memetakan langkah ke id TC granular.
- Target aksi memakai field milik spec `Asset Serial Tag {runId}-017` dan `Legacy Tag {runId}-017`, padanan bersuffix baris Pre-setup yang disebut TC-FA-CF-44 dan 45 (S-06, R-06).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search `{runId}-017` menemukan baris target (langkah 1, R-16) dan `(←)` mereset Search (langkah 15); langkah 7 mengaktifkan kembali `Asset Serial Tag {runId}-017` lewat switch dan dialog konfirmasi supaya TC-FA-CF-45, yang mengasumsikan kedua baris Active, berjalan dari keadaan awalnya (S-09); dialog dan toast aktivasi itu tidak diasersi karena tidak ada di Expected TC.
- Langkah penghubung toast (S-03, R-22): langkah 11 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-45 Dependensi `-` tetapi memakai baris `Asset Serial Tag` yang sudah dinonaktifkan TC-FA-CF-44 bila dijalankan berurutan; spec memulihkan baseline di antaranya.
  - TC-FA-CF-44 dan TC-FA-CF-45 menyebut baris Pre-setup `Asset Serial Tag` dan `Legacy Tag` yang juga dipakai TC lain; spec memakai padanan bersuffix milik spec.
