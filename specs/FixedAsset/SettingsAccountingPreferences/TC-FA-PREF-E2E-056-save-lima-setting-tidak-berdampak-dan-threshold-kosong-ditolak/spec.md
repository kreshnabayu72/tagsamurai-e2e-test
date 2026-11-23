---
id: TC-FA-PREF-E2E-056-save-lima-setting-tidak-berdampak-dan-threshold-kosong-ditolak
title: "Save Threshold Kosong Ditolak Tanpa Dialog; Save Lima Setting Tidak Berdampak Sekaligus"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-181
  - TC-FA-PREF-213
  - TC-FA-PREF-584
sourceRules: ["V-01", "F-FAPREF-01.k2b", "ST-04", "F-FAPREF-01.k2c", "FAPREF-LOGIC-10a", "T-01", "FAPREF-LOGIC-10j", "ST-01", "F-FAPREF-01.k13", "F-FAPREF-01.k14", "FAPREF-LOGIC-09c", "F-FAPREF-01.k22a"]
smoke: []
dependsOn: []
trace:
  "V-01": 3
  "F-FAPREF-01.k2b": 3
  "ST-04": 5
  "F-FAPREF-01.k2c": 5
  "FAPREF-LOGIC-10a": 6
  "T-01": [15, 30]
  "FAPREF-LOGIC-10j": 16
  "ST-01": 18
  "F-FAPREF-01.k13": 19
  "F-FAPREF-01.k14": 20
  "FAPREF-LOGIC-09c": 22
  "F-FAPREF-01.k22a": 31
anchor: [4, 7, 17, 21]
coverage:
  web: automated
---

# Save Threshold Kosong Ditolak Tanpa Dialog; Save Lima Setting Tidak Berdampak Sekaligus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji).
- Blok TC-584 memakai seri PC: PC-1 (Preferences nilai awal setara PB-1) dan PC-5 (akun Chart of Accounts, memuat `4-1500 – Pendapatan Lain-lain` yang tidak ada di PB-2); seri PC dibentuk lewat seed API pada langkah penghubung.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Data Dinamis DB-1 (nilai Preferences hasil Save) dipulihkan ke PB-1 lewat seed API sebelum TC berikutnya dan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-213: Save dengan Default Capitalization Threshold dikosongkan ditolak tanpa dialog

1. Kosongkan CurrencyInput Default Capitalization Threshold
2. Klik [Save changes]
3. Verifikasi caption "Default capitalization threshold must not be empty" tampil pada field Default Capitalization Threshold
4. Verifikasi field Default Capitalization Threshold berstatus Invalid (severity danger)
5. Verifikasi SectionCard Capitalization menampilkan titik peringatan (Badge Standalone Dot severity danger) pada judulnya
6. Verifikasi tidak ada dialog yang tampil
7. Verifikasi tidak ada toast yang tampil
8. Ketik 5000000 pada CurrencyInput Default Capitalization Threshold (mengembalikan nilai tersimpan)

### TC-FA-PREF-181: Save mengubah seluruh lima setting tidak berdampak sekaligus dalam satu Save

9. Ubah Select In-service Date Source menjadi "Manual by Accounting"
10. Ubah Select Disposal Documents jenis Sell menjadi "Required"
11. Pilih "1-2900 – Biaya Dikapitalisasi" pada Select Default Capitalization Offset
12. Pilih "1-1001 – Kas Utama" pada Select Found Asset Credit Account
13. Centang opsi "Category" pada MultiSelect Journal Grouping
14. Klik [Save changes]
15. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
16. Verifikasi tidak ada dialog D-01 yang tampil
17. Verifikasi form tetap terbuka dengan nilai tersimpan
18. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
19. Verifikasi Section Capitalization menampilkan In-service Date Source "Manual by Accounting"
20. Verifikasi Section Disposal menampilkan Disposal Documents Sell "Required"
21. Verifikasi Section Chart of Accounts menampilkan "1-2900 – Biaya Dikapitalisasi" pada Default Capitalization Offset dan "1-1001 – Kas Utama" pada Found Asset Credit Account
22. Verifikasi Section Journal Export menampilkan chip "Group" dan "Category"
23. Seed ulang Preferences ke PC-1 dan akun PC-5 lewat API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-584: Save yang hanya mengubah setting tidak berdampak langsung tersimpan tanpa dialog

24. Pilih "Manual by Accounting" pada Select In-service Date Source
25. Pilih "Required" pada Select Disposal Documents jenis Sell
26. Pilih "1-2900 – Biaya Dikapitalisasi" pada Select Default Capitalization Offset
27. Pilih "4-1500 – Pendapatan Lain-lain" pada Select Found Asset Credit Account
28. Tambahkan opsi "Category" pada Journal Grouping
29. Klik [Save changes]
30. Verifikasi toast "Success, accounting preferences have been saved." tampil
31. Verifikasi dialog Save Changes tidak tampil
32. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

## Notes

- Urutan: validasi diblokir (TC-213) lebih dulu, lalu aksi Save sukses (S-10); TC-213 ditulis sebelum TC-181 walau nomor TC lebih besar.
- Langkah penghubung (S-03): mengembalikan threshold ke 5000000 setelah TC-213, seed ulang ke seri PC sebelum TC-584, dan pemulihan Preferences di akhir.
- Urutan Verifikasi TC-181 dan TC-584: toast sukses lebih dulu sebagai anchor positif sebelum absence dialog (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).
  - TC-584 tidak menyatakan ketersediaan akun Chart of Accounts di Precondition; langkahnya memilih `1-2900 – Biaya Dikapitalisasi` dan `4-1500 – Pendapatan Lain-lain`, yang hanya ada di PC-5 (4-1500 tidak ada di PB-2). Spec memakai PC-5 untuk blok itu.
