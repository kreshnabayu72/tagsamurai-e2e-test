---
id: TC-FA-PREF-E2E-055-save-disposal-documents-required-dan-toast-hilang-4-detik
title: "Save Semua Jenis Disposal Documents Required; Toast Sukses Hilang Otomatis 4 Detik"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-177
  - TC-FA-PREF-182
sourceRules: ["T-01", "F-FAPREF-01.k22b", "F-FAPREF-01.k22a", "FAPREF-LOGIC-10j", "DOC-01", "DOC-02", "DOC-03", "DOC-04", "DOC-05", "DOC-06", "§3.1#b6", "ST-01"]
smoke: []
dependsOn: []
trace:
  "T-01": [8, 21]
  "F-FAPREF-01.k22b": [8, 21]
  "F-FAPREF-01.k22a": 9
  "FAPREF-LOGIC-10j": 9
  "DOC-01": 10
  "DOC-02": 11
  "DOC-03": 12
  "DOC-04": 13
  "DOC-05": 14
  "DOC-06": 15
  "§3.1#b6": 16
  "ST-01": 17
anchor: [23]
coverage:
  web: automated
---

# Save Semua Jenis Disposal Documents Required; Toast Sukses Hilang Otomatis 4 Detik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Data Dinamis DB-1 (nilai Preferences hasil Save) dipulihkan ke PB-1 lewat seed API sebelum TC berikutnya dan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-177: Save hanya mengubah Disposal Documents keenam jenis menjadi Required

1. Ubah Select Disposal Documents jenis Sell dari "Optional" menjadi "Required"
2. Ubah Select Disposal Documents jenis Scrap dari "Optional" menjadi "Required"
3. Ubah Select Disposal Documents jenis Lost dari "Optional" menjadi "Required"
4. Ubah Select Disposal Documents jenis Donate dari "Optional" menjadi "Required"
5. Ubah Select Disposal Documents jenis Trade-in dari "Optional" menjadi "Required"
6. Ubah Select Disposal Documents jenis Write-off dari "Optional" menjadi "Required"
7. Klik [Save changes]
8. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
9. Verifikasi tidak ada dialog D-01 yang tampil setelah klik [Save changes]
10. Verifikasi Select Disposal Documents jenis Sell menampilkan "Required"
11. Verifikasi Select Disposal Documents jenis Scrap menampilkan "Required"
12. Verifikasi Select Disposal Documents jenis Lost menampilkan "Required"
13. Verifikasi Select Disposal Documents jenis Donate menampilkan "Required"
14. Verifikasi Select Disposal Documents jenis Trade-in menampilkan "Required"
15. Verifikasi Select Disposal Documents jenis Write-off menampilkan "Required"
16. Verifikasi form tetap terbuka dengan nilai tersimpan
17. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
18. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-182: Toast sukses Save hilang otomatis setelah 4 detik

19. Ubah Select In-service Date Source menjadi "Manual by Accounting"
20. Klik [Save changes]
21. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar (severity success)
22. Amati toast di kanan bawah layar selama 4 detik tanpa menutupnya
23. Verifikasi toast hilang otomatis setelah 4 detik tanpa tindakan pengguna
24. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03): pemulihan Preferences lewat seed API dan muat ulang di akhir tiap TC, tanpa Verifikasi.
- Urutan Verifikasi TC-177: toast sukses lebih dulu sebagai anchor positif sebelum absence dialog D-01 (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - TC-182 Post Condition (In-service Date Source tersimpan) tidak punya langkah observasi di TC ini; tidak diasersi.
