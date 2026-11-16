---
id: TC-FA-PREF-E2E-050-select-disposal-documents-donate-trade-in-write-off-hanya-required-dan-optional
title: "Select Disposal Documents jenis Donate, Trade-in, dan Write-off hanya berisi Required dan Optional dan tidak dapat dikosongkan"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-161
  - TC-FA-PREF-162
  - TC-FA-PREF-163
sourceRules: ["DOC-04", "FAPREF-LOGIC-07h", "DOC-05", "DOC-06"]
smoke: []
dependsOn: []
trace:
  "DOC-04": [3, 7, 9]
  "FAPREF-LOGIC-07h": [4, 5, 10, 14, 15, 20, 24, 25, 30]
  "DOC-05": [13, 17, 19]
  "DOC-06": [23, 27, 29]
coverage:
  web: automated
---

# Select Disposal Documents jenis Donate, Trade-in, dan Write-off hanya berisi Required dan Optional dan tidak dapat dikosongkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PA (TC-FA-PREF-1-175), company `PT Contoh Konstruksi` plan Growth (PA-1) dengan Preferences nilai awal PA-2 (tidak terkunci, semua setting wajib terisi; Disposal Documents keenam jenis "Optional"; periode Mar 2026 sampai Dec 2026 Open).
- State yang diubah spec: nilai Select Disposal Documents jenis Donate, Trade-in, Write-off diubah ke "Required" lalu dikembalikan ke "Optional" pada form tanpa Save. Hook `after` memulihkan Preferences ke PA-2 lewat seed API bila ada yang tersimpan.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-161: Select Disposal Documents jenis Donate hanya berisi Required dan Optional dan tidak dapat dikosongkan

1. Scroll ke SectionCard Disposal
2. Klik Select Disposal Documents jenis Donate
3. Verifikasi daftar opsi Select Donate tepat dua berurutan: `Required | Optional`
4. Verifikasi daftar opsi Select Donate tidak memuat opsi kosong
5. Verifikasi tidak tersedia kontrol untuk mengosongkan Select Donate
6. Pilih "Required" pada daftar opsi Select Donate
7. Verifikasi nilai Select Donate "Required"
8. Pilih kembali "Optional" pada Select Donate
9. Verifikasi nilai Select Donate "Optional"
10. Verifikasi tidak ada caption pada Select Donate

### TC-FA-PREF-162: Select Disposal Documents jenis Trade-in hanya berisi Required dan Optional dan tidak dapat dikosongkan

11. Scroll ke SectionCard Disposal
12. Klik Select Disposal Documents jenis Trade-in
13. Verifikasi daftar opsi Select Trade-in tepat dua berurutan: `Required | Optional`
14. Verifikasi daftar opsi Select Trade-in tidak memuat opsi kosong
15. Verifikasi tidak tersedia kontrol untuk mengosongkan Select Trade-in
16. Pilih "Required" pada daftar opsi Select Trade-in
17. Verifikasi nilai Select Trade-in "Required"
18. Pilih kembali "Optional" pada Select Trade-in
19. Verifikasi nilai Select Trade-in "Optional"
20. Verifikasi tidak ada caption pada Select Trade-in

### TC-FA-PREF-163: Select Disposal Documents jenis Write-off hanya berisi Required dan Optional dan tidak dapat dikosongkan

21. Scroll ke SectionCard Disposal
22. Klik Select Disposal Documents jenis Write-off
23. Verifikasi daftar opsi Select Write-off tepat dua berurutan: `Required | Optional`
24. Verifikasi daftar opsi Select Write-off tidak memuat opsi kosong
25. Verifikasi tidak tersedia kontrol untuk mengosongkan Select Write-off
26. Pilih "Required" pada daftar opsi Select Write-off
27. Verifikasi nilai Select Write-off "Required"
28. Pilih kembali "Optional" pada Select Write-off
29. Verifikasi nilai Select Write-off "Optional"
30. Verifikasi tidak ada caption pada Select Write-off

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah 1 TC ("Buka Tab Preferences") dijalankan hook `beforeEach` suite; langkah 1, 11, 21 (scroll ke SectionCard Disposal) disalin dari TC.
- Langkah 3, 13, 23 (daftar opsi tepat dua berurutan) menjadi anchor positif asersi absence opsi kosong dan kontrol pengosong (8b.2). Daftar opsi diasersi saat terbuka (8b.5).
- Setiap blok berakhir dengan Select kembali ke "Optional" (nilai tersimpan) sehingga form tidak dirty dan tidak perlu `[Cancel]`; tidak ada Save pada spec ini.
- Temuan untuk QA:
  - TC-FA-PREF-161 sampai 163 tidak menjelaskan bentuk "kontrol untuk mengosongkan" (mis. ikon clear atau opsi kosong); spec mengasersi tidak ada kontrol pengosong di Select tanpa menyebut bentuknya.
  - Expected b menyebut nilai "selalu berupa Required atau Optional"; TC tidak punya langkah observasi nilai, spec menambah Verifikasi nilai setelah tiap pemilihan.
  - Langkah 4 TC ("Pilih Required lalu pilih kembali Optional") tidak menyebut apakah daftar opsi dibuka ulang antar pilihan; spec memilih dari daftar opsi yang terbuka lalu membukanya lagi untuk pilihan kedua.
  - Data kolom Data TC-FA-PREF-161 sampai 163 kosong dan Post Condition kosong; tidak ada yang diasersi lebih lanjut.
