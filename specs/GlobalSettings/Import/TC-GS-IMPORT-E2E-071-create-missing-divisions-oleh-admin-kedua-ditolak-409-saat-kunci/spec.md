---
id: TC-GS-IMPORT-E2E-071-create-missing-divisions-oleh-admin-kedua-ditolak-409-saat-kunci
title: "Create Missing Divisions oleh Admin Kedua Ditolak 409 saat Kunci Dipegang (Client C)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-247
coverage:
  web: automated
---

# Create Missing Divisions oleh Admin Kedua Ditolak 409 saat Kunci Dipegang (Client C)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Dua sesi browser (kelas multi-konteks), konteks terpisah dengan sesi login sendiri, keduanya login di hook `before` dan berada di Import > User Login Client C:
  - Sesi TC: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
  - Sesi Admin kedua: Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC2_PASSWORD`.
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup konteks Sesi Admin kedua dan mengembalikan sesi ke akun default suite.
- Data Dinamis (Client C, dibuat ulang lewat skrip fixture sebelum TC): D-30 draft User Login 7 baris dari `user-login-fk.csv` (Access `Global Settings` pada semua baris; baris #2 Citra Lestari dengan Division `Gudng` tidak ditemukan sehingga `error`). Division `Engineering` dan `Gudang` serta Position `Senior Developer` ada di Client C.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > User Login untuk kedua sesi. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: sesi edit Sesi TC ditutup dengan `[Cancel]`; draft D-30 direset (R2).

## Test Steps

1. [Sesi TC] Klik `⋯` pada baris #1
2. [Sesi TC] Pilih Edit
3. [Sesi Admin kedua] Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
4. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
5. [Sesi Admin kedua] Klik `[Cancel]` pada dialog
6. [Sesi Admin kedua] Muat ulang halaman Import > User Login
7. [Sesi Admin kedua] Verifikasi baris #2 tetap berstatus `error` dengan Division `Gudng` tidak ditemukan
8. [Sesi Admin kedua] Verifikasi `[Create Missing Divisions]` tetap tampil di Error Summary Callout
9. [Sesi TC] Verifikasi baris #1 tetap input aktif
10. [Sesi TC] Verifikasi footer tetap `[Cancel]` dan `[Save]`
11. [Sesi TC] Klik `[Cancel]` pada footer

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (kelas c, prinsip 13c); client berbeda dari spec 068 sampai 070 (Client C).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (muat ulang Sesi Admin kedua), langkah 11 (menutup sesi edit Sesi TC).
- Pembagian TC lintas spec: aksi tulis lain Admin kedua saat kunci dipegang pada Client A ada di spec 068 sampai 070.
- Temuan untuk QA:
  - TC-GS-IMPORT-247 tidak mereferensikan TC dependensi (kolom Dependensi "-"); Precondition TC (D-30) dipakai sebagai sumber.
  - TC-GS-IMPORT-247 tidak menyebut cara menutup sesi edit Total Control; spec menambahkan `[Cancel]` sebagai langkah penghubung.
