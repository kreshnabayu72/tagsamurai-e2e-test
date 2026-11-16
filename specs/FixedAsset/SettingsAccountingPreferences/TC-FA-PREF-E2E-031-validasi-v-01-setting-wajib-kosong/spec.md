---
id: TC-FA-PREF-E2E-031-validasi-v-01-setting-wajib-kosong
title: "Validasi V-01 Setting Wajib Kosong: Save Menampilkan Caption dan Titik Peringatan"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-125
  - TC-FA-PREF-126
  - TC-FA-PREF-127
  - TC-FA-PREF-550
sourceRules: ["V-01", "ST-01", "FAPREF-LOGIC-10f", "§3.1#b3", "F-FAPREF-01.k2b", "E-FAPREF-02", "ST-04", "F-FAPREF-01.k2c", "F-FAPREF-01.k2a"]
smoke: []
dependsOn: []
trace:
  "V-01": [3, 5, 11, 19, 28, 29, 30, 31, 32]
  "ST-01": 6
  "FAPREF-LOGIC-10f": 6
  "§3.1#b3": [10, 18, 27]
  "F-FAPREF-01.k2b": [11, 19, 28, 29, 30, 31, 32]
  "E-FAPREF-02": [11, 19]
  "ST-04": [13, 14, 21, 34]
  "F-FAPREF-01.k2c": [13, 21]
  "F-FAPREF-01.k2a": 22
anchor: [4, 12, 20, 33]
coverage:
  web: automated
---

# Validasi V-01 Setting Wajib Kosong: Save Menampilkan Caption dan Titik Peringatan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth). Preferences nilai awal PA-2 untuk TC-FA-PREF-126 dan 127; PC-1 untuk TC-FA-PREF-550 (Default Capitalization Threshold tersimpan 5.000.000; Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri, PC-6); PA-5 untuk TC-FA-PREF-125 (Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, dan Depreciation in Disposal Month kosong; setting lain bernilai awal), dibentuk lewat seed pada langkah 24 karena Save UI menolak nilai kosong. Nilai awal PA-2 dan PC-1 setara.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences PA-5 dan pemulihan lewat sesi API aktor (butir "Seed dan pemulihan lewat API" dan "Sesi API aktor" di `suite.md`); pembacaan nilai Default Capitalization Threshold tersimpan di server untuk Expected c TC-FA-PREF-550 (langkah 22).
- State yang diubah spec: Preferences company (hanya seed PA-5). Tidak ada Save yang berhasil. Hook `after` memulihkan Preferences ke PA-2.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-126: Mengosongkan Default Capitalization Threshold tidak menampilkan caption V-01 sebelum Save

1. Hapus seluruh isi CurrencyInput Default Capitalization Threshold
2. Pindahkan fokus ke field lain tanpa klik `[Save changes]`
3. Verifikasi CurrencyInput Default Capitalization Threshold kosong
4. Verifikasi CurrencyInput Default Capitalization Threshold menampilkan placeholder "Enter capitalization threshold"
5. Verifikasi caption "Default capitalization threshold must not be empty" belum tampil
6. Verifikasi `[Save changes]` Enabled

### TC-FA-PREF-127: Save dengan Default Capitalization Threshold dikosongkan menampilkan caption V-01 dan titik peringatan

7. Ketik "5000000" pada CurrencyInput Default Capitalization Threshold
8. Hapus seluruh isi CurrencyInput Default Capitalization Threshold
9. Klik `[Save changes]`
10. Verifikasi tidak ada dialog "Save Changes" dan tidak ada toast
11. Verifikasi caption di bawah Default Capitalization Threshold: "Default capitalization threshold must not be empty"
12. Verifikasi Default Capitalization Threshold berstatus Invalid (severity danger)
13. Verifikasi judul SectionCard Capitalization memiliki titik peringatan
14. Verifikasi judul SectionCard lain tidak memiliki titik peringatan
15. Ketik "5000000" pada CurrencyInput Default Capitalization Threshold

### TC-FA-PREF-550: Save dengan Default Capitalization Threshold kosong menampilkan caption V-01 dan titik peringatan section

16. Kosongkan CurrencyInput Default Capitalization Threshold
17. Klik `[Save changes]`
18. Verifikasi tidak ada dialog "Save Changes"
19. Verifikasi caption "Default capitalization threshold must not be empty" tampil pada field
20. Verifikasi Default Capitalization Threshold berstatus Invalid (severity danger)
21. Verifikasi judul SectionCard Capitalization diberi titik peringatan (Badge Standalone Dot severity danger)
22. Verifikasi nilai Default Capitalization Threshold tersimpan di server tetap 5.000.000
23. Klik `[Cancel]`

### TC-FA-PREF-125: Save dengan lima setting wajib kosong menampilkan caption V-01 pada tiap field dan titik peringatan

24. Bentuk Preferences PA-5 (kelima setting wajib kosong) lewat seed hingga tersimpan, lalu muat ulang halaman Preferences
25. Tambahkan opsi "Category" pada MultiSelect Journal Grouping
26. Klik `[Save changes]`
27. Verifikasi tidak ada dialog dan tidak ada toast
28. Verifikasi caption di bawah Fiscal Year Start: "Fiscal year start must not be empty"
29. Verifikasi caption di bawah First Accounting Period: "First accounting period must not be empty"
30. Verifikasi caption di bawah Default Capitalization Threshold: "Default capitalization threshold must not be empty"
31. Verifikasi caption di bawah In-service Date Source: "In-service date source must not be empty"
32. Verifikasi caption di bawah Depreciation in Disposal Month: "Depreciation in disposal month must not be empty"
33. Verifikasi kelima field berstatus Invalid (severity danger)
34. Verifikasi judul SectionCard General, Capitalization, dan Depreciation memiliki titik peringatan
35. Klik `[Cancel]`

## Notes

- Urutan: TC-FA-PREF-126 dan 127 (PA-2), TC-FA-PREF-550 (PC-1), lalu TC-FA-PREF-125 (PA-5) di akhir karena membutuhkan seed company dengan setting wajib kosong; nilai awal PA-2 dan PC-1 setara sehingga satu company dipakai. Perubahan urutan terhadap nomor TC dilakukan agar state dasar tidak diganti di tengah dan form tidak diseed ulang berulang.
- Langkah penghubung (S-03): langkah 7 (mengembalikan nilai tersimpan agar caption TC-FA-PREF-126 hilang sebelum TC-FA-PREF-127; R-12), 15, 23, 35 (`[Cancel]` atau pemulihan nilai form agar tidak berakhir dirty; S-09), dan 24 (seed PA-5). Setelah `[Cancel]` langkah 23 form kembali ke nilai tersimpan.
- Anchor asersi absence dialog dan toast (langkah 10, 18, 27) adalah asersi caption dan titik peringatan yang menyusul (8b.11).
- Temuan untuk QA:
  - Post Condition TC-FA-PREF-125, 127 ("Tidak ada perubahan data Preferences tersimpan"; "Tidak ada entri log baru") tidak punya langkah observasi sendiri sehingga tidak diasersi (S-01). TC-FA-PREF-550 punya Expected c yang mencakup nilai tersimpan tidak berubah sehingga diasersi lewat pembacaan BE (langkah 22).
  - TC-FA-PREF-127 dan TC-FA-PREF-550 menguji skenario yang sama (threshold dikosongkan lalu Save) pada seri fixture PA dan PC; hanya langkah 14 (judul SectionCard lain tanpa titik peringatan) yang membedakan.
