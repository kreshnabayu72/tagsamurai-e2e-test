---
id: TC-FA-CF-E2E-178-form-dan-detail-aset-ganti-data-type-scope-dan-value-type
title: "Detail Aset: Ganti Data Type, Keluarkan Asset Name dari Scope, dan Ubah Value Type"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-535
  - TC-FA-CF-536
  - TC-FA-CF-537
coverage:
  web: automated
---

# Detail Aset: Ganti Data Type, Keluarkan Asset Name dari Scope, dan Ubah Value Type

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Nilai (Pre-setup #1 dan #18). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Nilai (Pre-setup #18; dasar Company Alpha #11 dan baseline #12) dengan aset A1 (Pump, Active), A2 (Generator, Active), dan A3 (Pump, deleted), dirujuk lewat fixture `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE). Field yang diubah: `Rated Power` (Numeric, 1 Decimal Place, Scope {Generator, Pump}, Specific, `12.5` pada A1); `Brand Tier` (A1 = `Gold`) dipakai sebagai anchor.
- Data Dinamis: tidak ada; perubahan konfigurasi pada `Rated Power` dipulihkan seed reset Company.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset). Langkah 5 dan 10 memulihkan `Rated Power` di antara TC.
- State global: tidak ada yang diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-535: Penggantian Data Type yang dikonfirmasi mengosongkan nilai aset

1. Klik row action `⋯` > `Edit` pada baris `Rated Power`, ganti Data Type menjadi `Text`, klik `[Save]`, lalu klik `[Change Data Type]` pada dialog
2. Buka Detail aset `A1`
3. Verifikasi Detail aset `A1` menampilkan field `Brand Tier` dengan nilai `Gold`
4. Verifikasi nilai `Rated Power` pada `A1` kosong

### TC-FA-CF-536: Mengeluarkan Asset Name dari Scope membuang nilai aset di luar cakupan baru

5. Pulihkan baseline Company lewat seed reset Company (`Rated Power` kembali Numeric, Scope {Generator, Pump}, `12.5` pada A1) lalu buka Fixed Asset > Settings > Custom Fields
6. Klik row action `⋯` > `Edit` pada baris `Rated Power`, hapus chip `Pump` dari Scope, klik `[Save]`, lalu klik `[Change Scope]` pada dialog
7. Buka Detail aset `A1` (Asset Name `Pump`)
8. Verifikasi Detail aset `A1` menampilkan field `Brand Tier` dengan nilai `Gold`
9. Verifikasi field `Rated Power` tidak lagi tampil di Detail aset `A1` dan nilai `12.5` pada `A1` dibuang

### TC-FA-CF-537: Perubahan Value Type Specific ke Global membuang nilai aset dan menampilkan nilai Global read-only

10. Pulihkan baseline Company lewat seed reset Company (`Rated Power` kembali Specific dengan `12.5` pada A1) lalu buka Fixed Asset > Settings > Custom Fields
11. Klik row action `⋯` > `Edit` pada baris `Rated Power`, ubah Value Type menjadi `Global`, isi Value `Generator` = `10` dan `Pump` = `20`, klik `[Save]`, lalu konfirmasi dialog perubahan Value Type
12. Buka Detail aset `A1`
13. Verifikasi Detail aset `A1` menampilkan nilai Global `20` untuk `Rated Power` secara read-only
14. Verifikasi nilai individual `12.5` untuk `Rated Power` pada `A1` tidak ada

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec memuat TC lintas modul (NC-01): tata letak Detail aset tidak didefinisikan PRD modul ini; spec hanya mengasersi sejauh teks Expected TC.
- Urutan TC di spec: 535, 536, 537. Ketiganya mengubah `Rated Power` dari baseline yang sama, sehingga langkah 5 dan 10 memulihkannya (S-09). TC-FA-CF-531 sampai 534 ada di spec 137.
- Absence nilai dan field pada Detail didahului `Verifikasi` field lain pada surface yang sama (anchor, 8b butir 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5, 10, dan pembukaan Detail aset.
- Temuan untuk QA:
  - TC-FA-CF-536 Expected "field tidak lagi tampil dan nilai pada A1 dibuang" memuat dua klausa yang tidak teramati terpisah (nilai dibuang hanya terlihat dari field yang tak tampil); spec menulis satu `Verifikasi` (S-03).
  - TC-FA-CF-537 tidak menyebut label tombol dialog konfirmasi perubahan Value Type; spec menulis "konfirmasi dialog perubahan Value Type".
  - Email akun Total Control Company Nilai tidak tertulis di Pre-setup TC; env var `FA_TC_NILAI_PASSWORD` disediakan tim FE.
