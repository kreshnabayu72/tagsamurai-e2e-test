---
id: TC-FA-PREF-E2E-106-changelog-mengosongkan-search-tidak-mereset-filter-dan-hasil-kosong-pulih
title: "Changelog: mengosongkan Search tidak mereset Filter dan Sort, hasil kosong dari Search dan Filter pulih saat salah satu dilepas"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-321
  - TC-FA-PREF-322
coverage:
  web: automated
---

# Changelog: mengosongkan Search tidak mereset Filter dan Sort, hasil kosong dari Search dan Filter pulih saat salah satu dilepas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4 dan PB-U), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PB-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month; periode Mar 2026 sampai Dec 2026 Open). Changelog Preferences berisi 9 entri contoh (PB-C1) sebagai seluruh isi Changelog; seed disediakan tim FE/BE. Baris disebut "baris N" mengikuti nomor berikut (urutan tampil default Newest First; kolom Modified By tampil `Budi S` dan `Rina A`):
  - Baris 1: Date 27/10/26 16:40, Action Edit, Section Chart of Accounts, Field Default Capitalization Offset, Old Value —, New Value 1-2900 – Biaya Dikapitalisasi, Modified By Budi S
  - Baris 2: Date 26/10/26, Action Edit, Section Disposal, Field Disposal Documents — Sell, Old Value Optional, New Value Required, Modified By Rina A
  - Baris 3: Date 26/10/26, Action Edit, Section Disposal, Field Disposal Documents — Scrap, Old Value Optional, New Value Required, Modified By Rina A
  - Baris 4: Date tidak tertulis di TC, Action Edit, Section Journal Export, Field Journal Grouping, Old Value Group, New Value Group, Category, Modified By Budi S
  - Baris 5: Date tidak tertulis di TC, Action Edit, Section Disposal, Field Default Gain on Disposal, Old Value 4-9100 – Laba Pelepasan Aset, New Value —, Modified By Rina A
  - Baris 6: Date 22/10/26 sampai 23/10/26, Action Edit, Section General, Field Fiscal Year Start, Old Value January, New Value April, Modified By Rina A
  - Baris 7: Date 22/10/26 sampai 23/10/26, Action Edit, Section General, Field First Accounting Period, Old Value Mar 2026, New Value Jan 2026, Modified By Rina A
  - Baris 8: Date 22/10/26 sampai 23/10/26, Action Edit, Section Capitalization, Field Default Capitalization Threshold, Old Value 5.000.000, New Value 10.000.000, Modified By Rina A
  - Baris 9: Date 20/10/26 09:12, Action Create, Section —, Field Preferences, Old Value —, New Value Initial values, Modified By Budi S
  - Urutan tulis seed: baris 3 ditulis sebelum baris 2 dan baris 7 sebelum baris 6 pada Date yang sama (tie-break sort).
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-321: Mengosongkan Search tidak mereset Filter dan Sort

1. Klik ikon View history di header tab Preferences
2. Klik ikon Filter, pilih opsi Disposal pada dropdown Section, lalu klik `[Apply]`
3. Ketik Search "Rina", tekan Enter
4. Klik `✕` pada Search, tekan Enter
5. Verifikasi filter Section = Disposal tetap aktif
6. Verifikasi tabel menampilkan baris 2, baris 3, dan baris 5
7. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-PREF-322: Hasil kosong dari Search dan Filter pulih saat salah satu dilepas

8. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
9. Ketik Search "Budi", tekan Enter
10. Klik ikon Filter, pilih opsi General pada dropdown Section, lalu klik `[Apply]`
11. Verifikasi empty state berjudul "No results found" dengan deskripsi "Try adjusting your search or filter."
12. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
13. Verifikasi tabel menampilkan baris 1, baris 4, dan baris 9
14. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baris seed Changelog disebut "baris N" mengikuti tabel PB-C1 di Prerequisites; Modified By ditulis `Budi S` dan `Rina A` sesuai format kolom (R-14).
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih; langkah `[Clear Field]` setelah blok TC-FA-PREF-321 dan "Klik `(←)` pada kotak Search" di akhir TC-FA-PREF-322 memulihkan filter dan Search (S-09).
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-321 dan 322; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - TC-FA-PREF-321 Expected a ("filter Section = Disposal tetap aktif") tidak menyebut cara mengamati status filter; spec menulis Verifikasi sesuai teks TC.
