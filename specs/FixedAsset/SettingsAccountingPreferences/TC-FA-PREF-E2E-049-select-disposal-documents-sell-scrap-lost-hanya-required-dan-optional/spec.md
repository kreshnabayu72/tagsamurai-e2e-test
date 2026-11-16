---
id: TC-FA-PREF-E2E-049-select-disposal-documents-sell-scrap-lost-hanya-required-dan-optional
title: "Select Disposal Documents jenis Sell, Scrap, dan Lost hanya berisi Required dan Optional dan tidak dapat dikosongkan"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-158
  - TC-FA-PREF-159
  - TC-FA-PREF-160
sourceRules: ["DOC-01", "FAPREF-LOGIC-07h", "SET-07", "V-07", "DOC-02", "DOC-03"]
smoke: []
dependsOn: []
trace:
  "DOC-01": 3
  "FAPREF-LOGIC-07h": [4, 5, 14, 15, 24, 25]
  "SET-07": [7, 9, 17, 19, 27, 29]
  "V-07": [10, 20, 30]
  "DOC-02": 13
  "DOC-03": 23
coverage:
  web: automated
---

# Select Disposal Documents jenis Sell, Scrap, dan Lost hanya berisi Required dan Optional dan tidak dapat dikosongkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PA (TC-FA-PREF-1-175), company `PT Contoh Konstruksi` plan Growth (PA-1) dengan Preferences nilai awal PA-2 (tidak terkunci, semua setting wajib terisi; Disposal Documents keenam jenis "Optional"; periode Mar 2026 sampai Dec 2026 Open).
- State yang diubah spec: nilai Select Disposal Documents jenis Sell, Scrap, Lost diubah ke "Required" lalu dikembalikan ke "Optional" pada form tanpa Save. Hook `after` memulihkan Preferences ke PA-2 lewat seed API bila ada yang tersimpan.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-158: Select Disposal Documents jenis Sell hanya berisi Required dan Optional dan tidak dapat dikosongkan

1. Scroll ke SectionCard Disposal
2. Klik Select Disposal Documents jenis Sell
3. Verifikasi daftar opsi Select Sell tepat dua berurutan: `Required | Optional`
4. Verifikasi daftar opsi Select Sell tidak memuat opsi kosong
5. Verifikasi tidak tersedia kontrol untuk mengosongkan Select Sell
6. Pilih "Required" pada daftar opsi Select Sell
7. Verifikasi nilai Select Sell "Required"
8. Pilih kembali "Optional" pada Select Sell
9. Verifikasi nilai Select Sell "Optional"
10. Verifikasi tidak ada caption pada Select Sell

### TC-FA-PREF-159: Select Disposal Documents jenis Scrap hanya berisi Required dan Optional dan tidak dapat dikosongkan

11. Scroll ke SectionCard Disposal
12. Klik Select Disposal Documents jenis Scrap
13. Verifikasi daftar opsi Select Scrap tepat dua berurutan: `Required | Optional`
14. Verifikasi daftar opsi Select Scrap tidak memuat opsi kosong
15. Verifikasi tidak tersedia kontrol untuk mengosongkan Select Scrap
16. Pilih "Required" pada daftar opsi Select Scrap
17. Verifikasi nilai Select Scrap "Required"
18. Pilih kembali "Optional" pada Select Scrap
19. Verifikasi nilai Select Scrap "Optional"
20. Verifikasi tidak ada caption pada Select Scrap

### TC-FA-PREF-160: Select Disposal Documents jenis Lost hanya berisi Required dan Optional dan tidak dapat dikosongkan

21. Scroll ke SectionCard Disposal
22. Klik Select Disposal Documents jenis Lost
23. Verifikasi daftar opsi Select Lost tepat dua berurutan: `Required | Optional`
24. Verifikasi daftar opsi Select Lost tidak memuat opsi kosong
25. Verifikasi tidak tersedia kontrol untuk mengosongkan Select Lost
26. Pilih "Required" pada daftar opsi Select Lost
27. Verifikasi nilai Select Lost "Required"
28. Pilih kembali "Optional" pada Select Lost
29. Verifikasi nilai Select Lost "Optional"
30. Verifikasi tidak ada caption pada Select Lost

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah 1 TC ("Buka Tab Preferences") dijalankan hook `beforeEach` suite; langkah 1, 11, 21 (scroll ke SectionCard Disposal) disalin dari TC.
- Langkah 3, 13, 23 (daftar opsi tepat dua berurutan) menjadi anchor positif asersi absence opsi kosong dan kontrol pengosong (8b.2). Daftar opsi diasersi saat terbuka (8b.5).
- Setiap blok berakhir dengan Select kembali ke "Optional" (nilai tersimpan) sehingga form tidak dirty dan tidak perlu `[Cancel]`; tidak ada Save pada spec ini.
- Temuan untuk QA:
  - TC-FA-PREF-158 sampai 160 tidak menjelaskan bentuk "kontrol untuk mengosongkan" (mis. ikon clear atau opsi kosong); spec mengasersi tidak ada kontrol pengosong di Select tanpa menyebut bentuknya.
  - Expected b menyebut nilai "selalu berupa Required atau Optional"; TC tidak punya langkah observasi nilai, spec menambah Verifikasi nilai setelah tiap pemilihan.
  - Langkah 4 TC ("Pilih Required lalu pilih kembali Optional") tidak menyebut apakah daftar opsi dibuka ulang antar pilihan; spec memilih dari daftar opsi yang terbuka lalu membukanya lagi untuk pilihan kedua.
  - Data kolom Data TC-FA-PREF-158 sampai 160 kosong dan Post Condition kosong; tidak ada yang diasersi lebih lanjut.
