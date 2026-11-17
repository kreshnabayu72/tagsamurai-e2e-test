---
id: TC-FA-PREF-E2E-068-kunci-terbuka-kembali-save-fiscal-year-start-dan-kunci-aktif-setelah-muat-ulang
title: "Kunci Terbuka Kembali Setelah Periode Dibuka Kembali; Save Fiscal Year Start Berhasil; Kunci Aktif Setelah Muat Ulang"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-241
  - TC-FA-PREF-242
  - TC-FA-PREF-243
  - TC-FA-PREF-248
sourceRules: ["§Resolved#r10", "FAPREF-LOGIC-02c", "ST-05", "D-01", "F-FAPREF-01.k21b", "T-01", "D-03", "E-FAPREF-37", "SET-01", "FAPREF-LOGIC-10j", "§4.2b#b1", "SET-03"]
smoke: []
dependsOn: []
trace:
  "§Resolved#r10": [2, 3, 15]
  "FAPREF-LOGIC-02c": [2, 3, 15, 18, 25, 26]
  "ST-05": [5, 18, 25, 26]
  "D-01": 9
  "F-FAPREF-01.k21b": 9
  "T-01": [10, 22]
  "D-03": [11, 23]
  "E-FAPREF-37": 12
  "SET-01": 12
  "FAPREF-LOGIC-10j": 22
  "§4.2b#b1": 23
  "SET-03": 24
coverage:
  web: automated
---

# Kunci Terbuka Kembali Setelah Periode Dibuka Kembali; Save Fiscal Year Start Berhasil; Kunci Aktif Setelah Muat Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji). Varian: PB-7d (periode Mar 2026 pernah Soft Closed lalu dibuka kembali ke Open tanpa posting penyusutan) dan PB-7a (posting penyusutan pertama).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Sesi API aktor untuk pemicu perubahan state (fixture BE): kemampuan disediakan tim BE/FE (butir "Sesi API aktor" di `suite.md`).
- Data Dinamis DB-1 (nilai Preferences hasil Save) dipulihkan ke PB-1 lewat seed API sebelum TC berikutnya dan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-241: Kunci terbuka kembali saat periode dibuka kembali tanpa posting penyusutan

1. Seed periode dibuka kembali (PB-7d) lewat API, lalu muat ulang halaman dengan F5
2. Verifikasi Select Fiscal Year Start berstatus Enabled tanpa ikon gembok
3. Verifikasi Select bulan dan Select tahun First Accounting Period berstatus Enabled tanpa ikon gembok
4. Arahkan kursor ke Select Fiscal Year Start
5. Verifikasi tooltip "Fiscal year start is locked because depreciation has been posted or a period has been closed. It cannot be changed from this page." tidak tampil

### TC-FA-PREF-242: Save Fiscal Year Start berhasil setelah periode dibuka kembali tanpa posting penyusutan

6. Ubah Select Fiscal Year Start dari "January" menjadi "July"
7. Klik [Save changes]
8. Klik [Save] pada dialog D-01
9. Verifikasi dialog D-01 tertutup
10. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
11. Verifikasi tidak ada dialog D-03
12. Verifikasi Select Fiscal Year Start menampilkan "July"
13. Pulihkan Preferences dan periode ke PB-7d lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-243: Kunci aktif setelah periode pertama keluar dari Open dan tab dimuat ulang

14. Pulihkan Preferences ke PB-1 lewat seed API, lalu muat ulang halaman dengan F5
15. Verifikasi Select Fiscal Year Start dan Select bulan serta tahun First Accounting Period berstatus Enabled
16. Lewat sesi API (fixture BE), ubah status periode Mar 2026 menjadi Soft Closed hingga status tersimpan
17. Muat ulang halaman dengan F5
18. Verifikasi Select Fiscal Year Start dan Select bulan serta tahun First Accounting Period berstatus Disabled dengan ikon gembok

### TC-FA-PREF-248: Save field lain saat terkunci berhasil dan nilai Fiscal Year Start serta First Accounting Period tidak berubah

19. Seed posting penyusutan pertama (PB-7a) lewat API, lalu muat ulang halaman dengan F5
20. Ubah Select In-service Date Source menjadi "Manual by Accounting"
21. Klik [Save changes]
22. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
23. Verifikasi tidak ada dialog D-01 dan tidak ada dialog D-03
24. Verifikasi Select In-service Date Source menampilkan "Manual by Accounting"
25. Verifikasi Select Fiscal Year Start tetap "January" berstatus Disabled dengan ikon gembok
26. Verifikasi Select bulan dan tahun First Accounting Period tetap "March" "2026" berstatus Disabled dengan ikon gembok
27. Pulihkan kunci dan Preferences ke PB-1 lewat seed API

## Notes

- Langkah penghubung (S-03): seed varian kunci, muat ulang dan pemulihan di akhir tiap TC; hover FYS pada TC-241 melengkapi asersi absence tooltip.
- Urutan Verifikasi TC-248 dan TC-242: toast sukses sebagai anchor positif sebelum asersi absence dialog (bagian 8b butir 2). TC-603 dan TC-604 ada di spec 163.
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - TC-241 Post Condition, TC-243 Post Condition "tidak ada entri log baru untuk penguncian" dan TC-242 Post Condition b (periode dibangun ulang) tidak punya langkah observasi di TC masing-masing; tidak diasersi (TC-244 menguji tidak adanya log penguncian).
