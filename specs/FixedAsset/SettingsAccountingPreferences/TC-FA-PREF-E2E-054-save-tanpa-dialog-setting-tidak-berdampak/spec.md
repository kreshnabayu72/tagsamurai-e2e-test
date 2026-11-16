---
id: TC-FA-PREF-E2E-054-save-tanpa-dialog-setting-tidak-berdampak
title: "Save Tanpa Dialog: In-service Date Source, Default Capitalization Offset, Found Asset Credit Account, Journal Grouping"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-176
  - TC-FA-PREF-178
  - TC-FA-PREF-179
  - TC-FA-PREF-180
sourceRules: ["T-01", "F-FAPREF-01.k22b", "F-FAPREF-01.k22a", "FAPREF-LOGIC-10j", "SET-03", "FAPREF-LOGIC-10d", "§3.1#b6", "ST-01", "SET-08", "SET-09", "FAPREF-LOGIC-09c"]
smoke: []
dependsOn: []
trace:
  "T-01": [4, 15, 23, 31]
  "F-FAPREF-01.k22b": [4, 15, 23, 31]
  "F-FAPREF-01.k22a": [5, 16, 24, 32]
  "FAPREF-LOGIC-10j": [5, 16, 24, 32]
  "SET-03": 6
  "FAPREF-LOGIC-10d": 7
  "§3.1#b6": [10, 18, 26, 34]
  "ST-01": [11, 19, 27, 35]
  "SET-08": 17
  "SET-09": 25
  "FAPREF-LOGIC-09c": 33
anchor: [9]
coverage:
  web: automated
---

# Save Tanpa Dialog: In-service Date Source, Default Capitalization Offset, Found Asset Credit Account, Journal Grouping

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Jumlah notifikasi in-app milik Rina Anggraini (Total Control, aktor) dibaca lewat kemampuan baca BE sebelum Save dan sesudahnya (disediakan tim FE/BE); baseline dan hasil dibaca dari sumber yang sama (8b butir 10).
- Jendela amat notifikasi in-app: Tunggu 5 detik tanpa memuat ulang halaman sebelum membaca jumlah notifikasi sesudah Save (pilihan spec, bukan nilai TC/PRD); toast sukses menjadi anchor.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Data Dinamis DB-1 (nilai Preferences hasil Save) dipulihkan ke PB-1 lewat seed API sebelum TC berikutnya dan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-176: Save hanya mengubah In-service Date Source menjadi Manual by Accounting

1. Catat jumlah notifikasi in-app milik Rina Anggraini (Total Control) lewat kemampuan baca BE
2. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
3. Klik [Save changes]
4. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
5. Verifikasi tidak ada dialog D-01 yang tampil setelah klik [Save changes]
6. Verifikasi nilai langsung berlaku: Select In-service Date Source menampilkan "Manual by Accounting"
7. Verifikasi tidak ada langkah approval
8. Tunggu 5 detik tanpa memuat ulang halaman
9. Verifikasi jumlah notifikasi in-app milik Rina Anggraini (kemampuan baca BE) sama dengan jumlah awal
10. Verifikasi form tetap terbuka dengan nilai tersimpan
11. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
12. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-178: Save hanya mengubah Default Capitalization Offset ke akun 1-2900

13. Buka Select Default Capitalization Offset lalu pilih "1-2900 – Biaya Dikapitalisasi"
14. Klik [Save changes]
15. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
16. Verifikasi tidak ada dialog D-01 yang tampil setelah klik [Save changes]
17. Verifikasi Select Default Capitalization Offset menampilkan "1-2900 – Biaya Dikapitalisasi"
18. Verifikasi form tetap terbuka dengan nilai tersimpan
19. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
20. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-179: Save hanya mengubah Found Asset Credit Account ke akun 1-1001

21. Buka Select Found Asset Credit Account lalu pilih "1-1001 – Kas Utama"
22. Klik [Save changes]
23. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
24. Verifikasi tidak ada dialog D-01 yang tampil setelah klik [Save changes]
25. Verifikasi Select Found Asset Credit Account menampilkan "1-1001 – Kas Utama"
26. Verifikasi form tetap terbuka dengan nilai tersimpan
27. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
28. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-180: Save hanya mengubah Journal Grouping dengan menambah dimensi Category

29. Buka MultiSelect Journal Grouping lalu centang opsi "Category" sehingga terpilih "Group" dan "Category"
30. Klik [Save changes]
31. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
32. Verifikasi tidak ada dialog D-01 yang tampil setelah klik [Save changes]
33. Verifikasi MultiSelect Journal Grouping menampilkan chip "Group" dan chip "Category"
34. Verifikasi form tetap terbuka dengan nilai tersimpan
35. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
36. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03): langkah 1 (catat jumlah notifikasi awal lewat kemampuan baca BE, pola spec 057); langkah 8 (Tunggu 5 detik tanpa memuat ulang halaman, jendela amat notifikasi in-app, tanpa Verifikasi); pemulihan Preferences lewat seed API dan muat ulang di akhir tiap TC, tanpa Verifikasi (S-09).
- Klausa Expected d TC-176 dipecah tiga Verifikasi: nilai langsung berlaku (langkah 6), tidak ada langkah approval (langkah 7), jumlah notifikasi sama dengan baseline (langkah 9, sesudah jendela amat langkah 8). Spec ini melewati sekitar 35 langkah (36 langkah) dengan alasan: keempat blok satu kelas harness (Save tanpa dialog), berdiri sendiri, dan tiap blok hanya mengulang pola Ubah, Save, Verifikasi, pemulihan.
- Urutan Verifikasi: toast sukses diasersi lebih dulu sebagai anchor positif sebelum asersi absence dialog D-01 (bagian 8b butir 2); urutan ini menyimpang dari urutan penulisan Expected TC.
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - TC-176 Expected d "tidak ada langkah approval dan tidak ada notifikasi" tidak memberi baseline atau cara cek notifikasi; spec mengasersi tidak ada langkah approval pada layar (langkah 7) dan jumlah notifikasi aktor sama dengan baseline lewat kemampuan baca BE (langkah 1 dan 9).
  - TC-176 Expected d tidak menyebut penerima notifikasi maupun baseline; spec memakai jumlah notifikasi aktor (Rina Anggraini) sebelum dan sesudah Save sebagai pembanding.
