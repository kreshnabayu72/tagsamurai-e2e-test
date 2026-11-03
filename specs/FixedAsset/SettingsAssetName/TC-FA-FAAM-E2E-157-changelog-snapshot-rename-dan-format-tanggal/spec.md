---
id: TC-FA-FAAM-E2E-157-changelog-snapshot-rename-dan-format-tanggal
title: "Modal Changelog: Entri Lama Tidak Berubah Setelah Rename dan Format Tanggal General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-469
  - TC-FA-FAAM-500
coverage:
  web: automated
---

# Modal Changelog: Entri Lama Tidak Berubah Setelah Rename dan Format Tanggal General Settings

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup dan Dinamis: Asset Name `Snap One {runId}-157` (salinan Pre-setup #13f, Total Asset 0, disediakan seed API di hook `before`, dirujuk lewat fixture baru `Fixture.faAssetName.snapOne`). Spec me-rename menjadi `Snap Two {runId}-157` lalu `Snap Three {runId}-157`; hook `after` menghapus Asset Name itu lewat sesi API. Entri Changelog milik spec dicari lewat keyword `{runId}-157` sehingga baseline entri nol (S-12). Changelog contoh PRD §4.1 (Pre-setup #28) berisi sedikitnya satu entri bertanggal sehingga kolom Date tampil.
- Data General Settings: nilai Date Format dan Time Format alternatif ada di `Fixture.faAssetName.generalSettingsAlt` dan nilai bawaan client di `Fixture.faAssetName.generalSettingsDefault` (fixture baru belum ada; TC tidak menyebut nilai konkret, lihat Temuan untuk QA).
- Kemampuan teknis: mengubah Date Format dan Time Format di General Settings oleh akun aktor, dan pemulihan nilainya.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: Date Format dan Time Format General Settings client diubah langkah 13. Pemulihan: langkah 19 mengembalikan nilai bawaan, dan hook `after` memulihkannya sebagai cadangan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-469: Entri lama tidak berubah setelah Asset Name di-rename dua kali

1. Ketik Search `Snap One {runId}-157`, tekan Enter
2. Klik `⋯` baris `Snap One {runId}-157` lalu `Edit`
3. Ubah Asset Name menjadi `Snap Two {runId}-157`, lalu klik `[Save]`
4. Ganti isi kotak search dengan `Snap Two {runId}-157`, tekan Enter
5. Klik `⋯` baris `Snap Two {runId}-157` lalu `Edit`
6. Ubah Asset Name menjadi `Snap Three {runId}-157`, lalu klik `[Save]`
7. Klik icon Changelog
8. Ketik Search `{runId}-157`, tekan Enter
9. Verifikasi entri Edit pertama tetap Old Value `Snap One {runId}-157` dan New Value `Snap Two {runId}-157`
10. Verifikasi entri Edit kedua Old Value `Snap Two {runId}-157` dan New Value `Snap Three {runId}-157`
11. Verifikasi kolom Asset Name entri pertama `Snap Two {runId}-157` dan entri kedua `Snap Three {runId}-157`
12. Tekan Esc

### TC-FA-FAAM-500: Kolom Date Changelog dan input Date Filter mengikuti General Settings

13. Buka General Settings, ubah Date Format dan Time Format ke nilai `Fixture.faAssetName.generalSettingsAlt`, lalu klik `[Save]`
14. Buka Fixed Asset > Settings > Asset Master > Asset Name
15. Klik icon Changelog
16. Verifikasi kolom Date pada tabel Changelog mengikuti Date Format dan Time Format baru
17. Klik icon Filter, lalu pilih tanggal pada input Date
18. Verifikasi teks tanggal terpilih pada input Date Filter mengikuti Date Format baru
19. Pulihkan Date Format dan Time Format General Settings ke nilai `Fixture.faAssetName.generalSettingsDefault`, lalu klik `[Save]`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): mencari baris target lewat Search (langkah 1 dan 4), mengganti nama dua kali sesuai TC (langkah 2 sampai 6), menyaring Changelog ke entri milik spec lewat keyword `{runId}-157` (langkah 8, baseline entri nol), menutup modal (langkah 12), membuka kembali halaman Asset Name (langkah 14), dan memulihkan General Settings (langkah 19, R-08).
- Entri Create hasil seed ikut tampil pada keyword `{runId}-157`; asersi langkah 9 sampai 11 hanya menyebut dua entri Edit.
- Verifikasi format pada langkah 16 dan 18 beranchor baris Changelog yang tampil (langkah 9 sampai 11) dan kolom Date yang tampil di tabel.
- Temuan untuk QA:
  - TC-FA-FAAM-500 tidak menyebut nilai Date Format dan Time Format, jalur menu General Settings, maupun nilai bawaan client; spec memakai fixture alternatif dan bawaan yang disediakan tim FE.
  - TC-FA-FAAM-469 Precondition menyebut `Snap One` sebagai Pre-setup #13f, sedangkan Data Uji Dinamis tidak mendaftarkan nama bersuffix; spec memakai `Snap One {runId}-157` (S-12) dan menghapusnya di `after`.
