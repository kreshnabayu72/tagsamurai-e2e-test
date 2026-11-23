---
id: TC-FA-PREF-E2E-068-kunci-terbuka-kembali-save-fiscal-year-start-dan-kunci-aktif-setelah-muat-ulang
title: "Kunci Aktif Setelah Posting Penyusutan Pertama dan Muat Ulang; Save Field Lain Saat Terkunci"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-243
  - TC-FA-PREF-248
sourceRules: ["§Resolved#r10", "FAPREF-LOGIC-02c", "ST-05", "T-01", "D-03", "FAPREF-LOGIC-10j", "§4.2b#b1", "SET-03"]
smoke: []
dependsOn: []
trace:
  "§Resolved#r10": 1
  "FAPREF-LOGIC-02c": [1, 4, 11, 12]
  "ST-05": [4, 11, 12]
  "T-01": 8
  "D-03": 9
  "FAPREF-LOGIC-10j": 8
  "§4.2b#b1": 9
  "SET-03": 10
coverage:
  web: automated
---

# Kunci Aktif Setelah Posting Penyusutan Pertama dan Muat Ulang; Save Field Lain Saat Terkunci

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; belum ada Run Posted) dan PB-2 (akun Chart of Accounts uji). Varian: PB-7a (posting penyusutan pertama, Depreciation Run berstatus Posted).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Sesi API aktor untuk pemicu perubahan state (fixture BE): kemampuan disediakan tim BE/FE (butir "Sesi API aktor" di `suite.md`).
- Data Dinamis DB-1 (nilai Preferences hasil Save) dipulihkan ke PB-1 lewat seed API sebelum TC berikutnya dan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-243: Kunci aktif setelah posting penyusutan pertama dan tab dimuat ulang

1. Verifikasi Select Fiscal Year Start dan Select bulan serta tahun First Accounting Period berstatus Enabled
2. Lewat sesi API (fixture BE), lakukan posting penyusutan pertama (Depreciation Run berstatus Posted) hingga status tersimpan
3. Muat ulang halaman dengan F5
4. Verifikasi Select Fiscal Year Start dan Select bulan serta tahun First Accounting Period berstatus Disabled dengan ikon gembok

### TC-FA-PREF-248: Save field lain saat terkunci berhasil dan nilai Fiscal Year Start serta First Accounting Period tidak berubah

5. Seed posting penyusutan pertama (PB-7a) lewat API, lalu muat ulang halaman dengan F5
6. Ubah Select In-service Date Source menjadi "Manual by Accounting"
7. Klik [Save changes]
8. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
9. Verifikasi tidak ada dialog D-01 dan tidak ada dialog D-03
10. Verifikasi Select In-service Date Source menampilkan "Manual by Accounting"
11. Verifikasi Select Fiscal Year Start tetap "January" berstatus Disabled dengan ikon gembok
12. Verifikasi Select bulan dan tahun First Accounting Period tetap "March" "2026" berstatus Disabled dengan ikon gembok
13. Pulihkan kunci dan Preferences ke PB-1 lewat seed API

## Notes

- Langkah penghubung (S-03): seed varian kunci, muat ulang dan pemulihan di akhir TC.
- Urutan Verifikasi TC-248: toast sukses sebagai anchor positif sebelum asersi absence dialog (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - TC-243 Post Condition "tidak ada entri log baru untuk penguncian" tidak punya langkah observasi di TC ini; tidak diasersi (TC-244 menguji tidak adanya log penguncian).
