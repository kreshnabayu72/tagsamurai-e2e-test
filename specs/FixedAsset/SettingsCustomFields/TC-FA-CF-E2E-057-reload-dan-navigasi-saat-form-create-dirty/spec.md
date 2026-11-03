---
id: TC-FA-CF-E2E-057-reload-dan-navigasi-saat-form-create-dirty
title: "Reload dan Navigasi Internal Saat Form Create Dirty"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-182
  - TC-FA-CF-183
coverage:
  web: automated
---

# Reload dan Navigasi Internal Saat Form Create Dirty

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-057`): Field Name yang diketik tetapi tidak pernah tersimpan: `Dirty Reload {runId}-057` dan `Dirty Nav {runId}-057`.
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-057`.
- Kemampuan teknis: penanganan dialog `beforeunload` bawaan browser (mengamati kemunculannya dan membatalkannya) saat muat ulang halaman (S-08); klik menu sidebar lain di Fixed Asset (TC tidak menyebut nama menu).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-182: Reload halaman saat form Create dirty memicu konfirmasi bawaan browser dan tidak saat bersih

1. Klik [+ Custom Field]
2. Isi Field Name `Dirty Reload {runId}-057`
3. Muat ulang halaman (F5)
4. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
5. Batalkan konfirmasi browser
6. Kosongkan Field Name
7. Muat ulang halaman (F5)
8. Verifikasi tombol `[+ Custom Field]` tampil
9. Verifikasi konfirmasi bawaan browser (beforeunload) tidak muncul

### TC-FA-CF-183: Navigasi internal saat form Create dirty mencegat perubahan route dengan dialog Unsaved Changes

10. Klik [+ Custom Field]
11. Isi Field Name `Dirty Nav {runId}-057`
12. Klik menu sidebar lain
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Cancel]`
15. Verifikasi navigasi dibatalkan: pengguna tetap di form Create
16. Klik menu sidebar lain lagi
17. Klik `[Leave]`
18. Verifikasi navigasi dilanjutkan: halaman menu tujuan tampil
19. Buka kembali Fixed Asset > Settings > Custom Fields
20. Verifikasi modal Create tidak terbuka
21. Ketik Search `{runId}-057`, tekan Enter
22. Verifikasi empty state "No results found" tampil (field `Dirty Nav {runId}-057` tidak tersimpan)
23. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sama dengan sumber (182, 183). Kemampuan `beforeunload` ditulis di Prerequisites (S-08): dialog diamati lalu dibatalkan pada langkah 4 dan 5; sesi edit dirty dikosongkan (langkah 6) sebelum muat ulang berikutnya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 3, 5, 6, 7, 10, 12, 16, 17, 19, 21, 23, serta pengisian form sebagai bagian langkah TC. Langkah 8 adalah anchor positif bagi asersi absence pada langkah 9 (R-21). Langkah 19 sampai 22 membuktikan bahwa `[Leave]` menutup modal tanpa menyimpan field: Expected b TC-FA-CF-183 ("modal ditutup tanpa menyimpan") diamati sesudah kembali ke halaman asal.
- Temuan untuk QA:
  - TC-FA-CF-183: TC menyebut "menu sidebar lain" tanpa nama menu; spec mengikuti teks TC dan tim FE menentukan menu tujuan yang tersedia bagi akun Total Control Company Alpha.
  - TC-FA-CF-183: Expected a menyebut "`[Cancel]` membatalkan navigasi dan tetap di form"; spec mengasersinya sebagai pengguna tetap di form Create (langkah 15) karena TC tidak menyebut elemen penanda halaman.
  - Nama field memakai suffix `{runId}-057` (S-12) sehingga tidak sama dengan `Dirty Reload` dan `Dirty Nav` pada Data Uji TC.
