---
id: TC-FA-FAAC-E2E-124-setup-column-reset-tutup-satu-kolom-dan-persistensi
title: "Setup Column Tabel Asset Class: Reset to Default, Tutup Modal dengan X, Satu Kolom Tersisa, dan Persistensi Konfigurasi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-403
  - TC-FA-FAAC-404
  - TC-FA-FAAC-405
  - TC-FA-FAAC-406
sourceRules: ["§4.1.1#r1", "§4.1.1#r2", "§4.1.1#r3", "§4.1.1#r4", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r7", "§4.1.1#r8", "§4.1.1#r9", "§4.1.1#r10", "§4.1.1#r11", "§4.1.1#b2", "§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r29", "§4.1.1#r30", "§4.1.1#r31", "§4.1.1#r32"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r1": [4, 7]
  "§4.1.1#r2": [4, 7, 26, 31]
  "§4.1.1#r3": [4, 7]
  "§4.1.1#r4": [4, 7]
  "§4.1.1#r5": [4, 7]
  "§4.1.1#r6": [4, 7]
  "§4.1.1#r7": [4, 7]
  "§4.1.1#r8": [4, 7]
  "§4.1.1#r9": [4, 7]
  "§4.1.1#r10": [4, 8]
  "§4.1.1#r11": [4, 8]
  "§4.1.1#b2": [17, 18, 19, 21]
  "§4.1.1#r26": 34
  "§4.1.1#r27": 34
  "§4.1.1#r28": 34
  "§4.1.1#r29": 34
  "§4.1.1#r30": 34
  "§4.1.1#r31": 34
  "§4.1.1#r32": 34
anchor: [12, 13, 27, 32]
coverage:
  web: automated
---

# Setup Column Tabel Asset Class: Reset to Default, Tutup Modal dengan X, Satu Kolom Tersisa, dan Persistensi Konfigurasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Seed disediakan tim FE/BE (lihat `suite.md`).
- Kondisi awal konfigurasi kolom: bawaan (sembilan kolom tampil, Modified By dan Last Updated tersembunyi); preferensi kolom browser bersih sebelum spec dimulai.
- Kemampuan teknis: login ulang di browser yang sama (logout lalu login akun yang sama) untuk TC-FA-FAAC-406; password `Spectra.env.FA_TC_PASSWORD`.
- State yang diubah spec: konfigurasi kolom tabel disimpan di browser (Column Visibility, localStorage; kolom Assets disembunyikan oleh langkah 24). Dipulihkan oleh langkah 36 dan oleh hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-403: Reset to Default pada modal Setup Column

1. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`)
2. Hilangkan centang Class Name, centang Modified By, dan seret Assets ke posisi pertama
3. Klik `[Reset to Default]`
4. Verifikasi tabel di balik modal kembali ke susunan awal (state sementara sebelum Save)
5. Klik `[Save]`
6. Refresh halaman
7. Verifikasi tabel menampilkan sembilan kolom bawaan dengan urutan awal Active | Class Code | Class Name | Commercial | Fiscal | Capitalization Threshold | Accounts | Asset Names | Assets
8. Verifikasi tabel tanpa kolom Modified By dan Last Updated

### TC-FA-FAAC-404: Tutup modal Setup Column dengan X membuang perubahan

9. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`)
10. Hilangkan centang Class Name
11. Klik Close (X)
12. Verifikasi modal tertutup
13. Verifikasi kolom Class Name tetap tampil pada tabel karena perubahan dibuang

### TC-FA-FAAC-405: Satu kolom tersisa tidak dapat disembunyikan

14. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`)
15. Hilangkan centang semua kolom satu per satu hingga tersisa satu kolom
16. Arahkan kursor ke checkbox kolom yang tersisa
17. Verifikasi checkbox kolom terakhir Disabled
18. Verifikasi checkbox kolom terakhir tetap tampil
19. Verifikasi tooltip berbunyi `At least one column must remain visible.`
20. Coba hilangkan centang kolom yang tersisa
21. Verifikasi kolom terakhir tidak dapat di-uncheck
22. Klik Close (X)

### TC-FA-FAAC-406: Konfigurasi kolom bertahan setelah muat ulang dan logout-login di browser yang sama, dan tidak memengaruhi tabel lain

23. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`)
24. Hilangkan centang Assets, klik `[Save]`
25. Muat ulang halaman (F5)
26. Verifikasi kolom Class Code tampil
27. Verifikasi kolom Assets tetap tersembunyi setelah muat ulang
28. Logout
29. Login kembali sebagai Total Control di browser yang sama
30. Buka Settings > Accounting dan klik tab Asset Class
31. Verifikasi kolom Class Code tampil
32. Verifikasi kolom Assets tetap tersembunyi setelah logout-login di browser yang sama
33. Klik icon Changelog
34. Verifikasi tabel modal Changelog tetap menampilkan ketujuh kolom: Date, Action, Class Code, Field, Old Value, New Value, Modified By
35. Tutup modal Changelog

### Pemulihan

36. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`), centang Assets, klik `[Save]`

## Notes

- Langkah penghubung (S-03): langkah 22 (menutup modal tanpa menyimpan satu kolom tersisa, S-09), langkah 30 (membuka layar tab Asset Class sesudah login ulang; halaman landing tidak diandaikan, S-07), langkah 35 (menutup modal Changelog), langkah 36 (mengembalikan kolom Assets yang disembunyikan; TC mencatat Post Condition ini).
- Langkah 28 dan 29 adalah ganti sesi eksplisit pada akun yang sama (S-07); TC-FA-FAAC-406 menyebutnya "logout lalu login kembali sebagai Total Control di browser yang sama".
- Langkah 26 dan 31 (`Verifikasi kolom Class Code tampil`) adalah anchor kolom lain sebelum asersi absence kolom Assets sesudah F5 dan sesudah login ulang (8b butir 2).
- Kolom yang tersisa pada langkah 15 tidak disebut TC; pilihan kolom ditetapkan tahap script (Temuan untuk QA).
- Alasan melebihi sekitar 35 langkah (36 langkah): semua blok satu topik (Setup Column tabel Asset Class) pada satu konfigurasi kolom browser, dan tiap blok berdiri sendiri; dua anchor kolom ditambahkan untuk asersi absence (8b butir 2).
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena data hanya dibaca (S-06, S-12).
- Temuan untuk QA: TC-FA-FAAC-405 tidak menyebut kolom mana yang tersisa; TC-FA-FAAC-406 menjadikan hanya kolom Assets sebagai bahan uji persistensi.
