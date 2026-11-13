---
id: TC-FA-PREF-E2E-177-tooltip-opsi-dan-tanpa-shortcut-select-default-disposal-proceeds-account
title: "Select Default Disposal Proceeds Account (SET-13): tooltip, opsi akun Disposal Proceeds, dan tanpa shortcut Create account"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-622
  - TC-FA-PREF-623
  - TC-FA-PREF-624
coverage:
  web: automated
---

# Select Default Disposal Proceeds Account (SET-13): tooltip, opsi akun Disposal Proceeds, dan tanpa shortcut Create account

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PC (TC-FA-PREF-362-631), company `PT Contoh Konstruksi` plan Growth (PC-1): Default Disposal Proceeds Account tersimpan kosong, setting lain bernilai awal. Chart of Accounts PC-22 (PC-5 ditambah akun function Disposal Proceeds): Active `1-3100 – Kliring Hasil Pelepasan` dan `1-3110 – Kliring Hasil Pelepasan Cabang`, Inactive `1-3190 – Kliring Hasil Lama`; akun function lain dari PC-5 yang dipakai asersi: `4-9100 – Laba Pelepasan Aset` (Gain on Disposal) dan `1-2900 – Biaya Dikapitalisasi` (Capitalization Offset).
- State yang diubah spec: tidak ada (spec hanya membaca). Hook `after` memulihkan Preferences dan Chart of Accounts ke nilai awal lewat seed API.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-622: Tooltip Default Disposal Proceeds Account (SET-13)

1. Seed company ke seri PC (Preferences PC-1 dan Chart of Accounts PC-22) lewat API hingga tersimpan
2. Buka ulang Fixed Asset > Settings > Accounting > Preferences
3. Hover ikon ⓘ di sebelah label "Default Disposal Proceeds Account"
4. Verifikasi tooltip tampil dengan teks persis: "Clearing account for the proceeds of assets that are sold, scrapped, or traded in. Settle the cash or receivable in your accounting system. If empty, the disposal journal is held at export."

### TC-FA-PREF-623: Opsi Select Default Disposal Proceeds Account hanya memuat akun Active ber-function Disposal Proceeds urut kode A-Z

5. Gulir ke SectionCard Disposal
6. Verifikasi Select Default Disposal Proceeds Account menampilkan placeholder "Select account"
7. Klik Select Default Disposal Proceeds Account
8. Verifikasi opsi Select Default Disposal Proceeds Account berurutan kode A-Z: `1-3100 – Kliring Hasil Pelepasan | 1-3110 – Kliring Hasil Pelepasan Cabang`
9. Verifikasi daftar opsi tidak memuat akun Inactive "1-3190 – Kliring Hasil Lama"
10. Verifikasi daftar opsi tidak memuat akun ber-function lain "4-9100 – Laba Pelepasan Aset" dan "1-2900 – Biaya Dikapitalisasi"
11. Tutup daftar opsi Select Default Disposal Proceeds Account

### TC-FA-PREF-624: Select Default Disposal Proceeds Account tidak memiliki shortcut Create account

12. Klik Select Default Gain on Disposal
13. Verifikasi shortcut `+ Create account` tampil pada Select Default Gain on Disposal
14. Tutup daftar opsi Select Default Gain on Disposal
15. Klik Select Default Disposal Proceeds Account
16. Verifikasi daftar opsi Select Default Disposal Proceeds Account memuat "1-3100 – Kliring Hasil Pelepasan"
17. Verifikasi Select Default Disposal Proceeds Account tidak memiliki shortcut `+ Create account`
18. Tutup daftar opsi Select Default Disposal Proceeds Account

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah 1 TC ("Buka Tab Preferences") dijalankan hook `beforeEach` suite; layar dibuka ulang pada langkah 2 sesudah seed seri PC.
- Langkah penghubung (S-03): langkah 1 dan 2 (seed seri PC dan membuka ulang halaman), langkah 5 (menggulir ke SectionCard Disposal, tempat Select berada menurut TC-FA-PREF-623 langkah 2), langkah 11, 14, dan 18 (menutup daftar opsi).
- Asersi absence akun (langkah 9 dan 10) didahului `Verifikasi` daftar opsi berurutan yang memuat akun pembanding pada daftar yang sama (langkah 8; 8b.2); daftar opsi diasersi saat terbuka (8b.5). Asersi absence shortcut (langkah 17) memakai anchor positif langkah 12 sampai 13 (shortcut tampil pada Select Default Gain on Disposal) dan langkah 16 (daftar opsi Select Default Disposal Proceeds Account sudah termuat), mengikuti pola spec 162.
- Temuan untuk QA:
  - TC-FA-PREF-624 "Periksa Select" tidak menjelaskan letak shortcut `+ Create account` (di dalam daftar opsi atau di samping Select) dan tidak menyebut pembanding positif; spec memakai Select Default Gain on Disposal sebagai pembanding berdasarkan TC-FA-PREF-168.
  - TC-FA-PREF-623 Expected a menulis placeholder tampil saat nilai kosong dengan langkah "Periksa Select" tanpa menyebut aksi gulir; spec menambah langkah gulir sebagai penghubung.
  - TC-FA-PREF-6 dan TC-FA-PREF-21 (isi dan urutan SectionCard Disposal) tidak menyebut Default Disposal Proceeds Account; urutan Select di SectionCard Disposal tidak diasersi di spec ini.
  - Post Condition kosong pada TC-FA-PREF-622 sampai 624; tidak ada yang diasersi lebih lanjut.
