---
id: TC-FA-PREF-E2E-107-changelog-sort-default-siklus-tiga-state-date-dan-kolom-teks-kolom-actions-tanpa-sort
title: "Changelog Sort: urutan bawaan Date Newest First, siklus tiga state kolom Date dan kolom teks, kolom Actions tanpa sort"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-323
  - TC-FA-PREF-324
  - TC-FA-PREF-325
  - TC-FA-PREF-331
sourceRules: ["§4.1.4#p2", "§4.1.4#r1", "§9.5#r8", "§4.1.4#r2", "§4.1.4#r3", "§4.1.4#r4"]
smoke: []
dependsOn: []
trace:
  "§4.1.4#p2": 2
  "§4.1.4#r1": [3, 7, 9, 33]
  "§9.5#r8": [4, 12, 19, 25, 31]
  "§4.1.4#r2": [15, 17]
  "§4.1.4#r3": [21, 23]
  "§4.1.4#r4": [27, 29]
anchor: [11, 34]
coverage:
  web: automated
---

# Changelog Sort: urutan bawaan Date Newest First, siklus tiga state kolom Date dan kolom teks, kolom Actions tanpa sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4 dan PB-U), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PB-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month; periode Mar 2026 sampai Dec 2026 Open). Changelog Preferences berisi 9 entri contoh (PB-C1) sebagai seluruh isi Changelog; seed disediakan tim FE/BE. Baris disebut "baris N" mengikuti nomor berikut (urutan tampil default Newest First; kolom Modified By tampil `Budi S` dan `Rina A`):
  - Baris 1: Date 27/10/26 16:40, Action Edit, Section Chart of Accounts, Field Default Capitalization Offset, Old Value —, New Value 1-2900 – Biaya Dikapitalisasi, Modified By Budi S
  - Baris 2: Date 26/10/26, Action Edit, Section Disposal, Field Disposal Documents — Sell, Old Value Optional, New Value Required, Modified By Rina A
  - Baris 3: Date 26/10/26, Action Edit, Section Disposal, Field Disposal Documents — Scrap, Old Value Optional, New Value Required, Modified By Rina A
  - Baris 4: Date tidak tertulis di TC, Action Edit, Section Journal Export, Field Journal Grouping, Old Value Group, New Value Group, Category, Modified By Budi S
  - Baris 5: Date tidak tertulis di TC, Action Edit, Section Disposal, Field Default Gain on Disposal, Old Value 4-9100 – Laba Pelepasan Aset, New Value —, Modified By Rina A
  - Baris 6: Date 22/10/26 sampai 23/10/26, Action Edit, Section General, Field Fiscal Year Start, Old Value January, New Value April, Modified By Rina A
  - Baris 7: Date 22/10/26 sampai 23/10/26, Action Edit, Section General, Field First Accounting Period, Old Value Mar 2026, New Value Jan 2026, Modified By Rina A
  - Baris 8: Date 22/10/26 sampai 23/10/26, Action Edit, Section Capitalization, Field Default Capitalization Threshold, Old Value 5.000.000, New Value 10.000.000, Modified By Rina A
  - Baris 9: Date 20/10/26 09:12, Action Create, Section —, Field Preferences, Old Value —, New Value Initial values, Modified By Budi S
  - Urutan tulis seed: baris 3 ditulis sebelum baris 2 dan baris 7 sebelum baris 6 pada Date yang sama (tie-break sort).
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-323: Urutan bawaan modal Changelog Date Newest First

1. Klik ikon View history di header tab Preferences
2. Verifikasi baris tampil dari yang terbaru: baris 1 lalu baris 2 lalu baris 3 lalu baris 4 lalu baris 5 lalu baris 6 lalu baris 7 lalu baris 8 lalu baris 9
3. Verifikasi header kolom Date menampilkan indikator sort Newest First
4. Verifikasi kolom lain tanpa indikator sort aktif

### TC-FA-PREF-324: Siklus sort tiga state pada kolom Date

5. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
6. Klik header kolom Date satu kali
7. Verifikasi urutan ascending (Oldest First): baris 9 lalu baris 8 lalu baris 7 lalu baris 6 lalu baris 5 lalu baris 4 lalu baris 3 lalu baris 2 lalu baris 1
8. Klik header kolom Date kali kedua
9. Verifikasi urutan descending (Newest First): baris 1 lalu baris 2 lalu baris 3 lalu baris 4 lalu baris 5 lalu baris 6 lalu baris 7 lalu baris 8 lalu baris 9
10. Klik header kolom Date kali ketiga
11. Verifikasi indikator sort aktif hilang
12. Verifikasi urutan kembali ke urutan bawaan: baris 1 lalu baris 2 lalu baris 3 lalu baris 4 lalu baris 5 lalu baris 6 lalu baris 7 lalu baris 8 lalu baris 9

### TC-FA-PREF-325: Siklus sort tiga state pada kolom teks Action, Section, dan Field

13. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
14. Klik header kolom Action satu kali
15. Verifikasi Action klik 1 (A-Z): baris 9 lalu baris 1 lalu baris 3 lalu baris 2 lalu baris 4 lalu baris 5 lalu baris 7 lalu baris 6 lalu baris 8
16. Klik header kolom Action kali kedua
17. Verifikasi Action klik 2 (Z-A): baris 1 lalu baris 2 lalu baris 3 lalu baris 4 lalu baris 5 lalu baris 6 lalu baris 7 lalu baris 8 lalu baris 9
18. Klik header kolom Action kali ketiga
19. Verifikasi Action klik 3: urutan bawaan baris 1 lalu baris 2 lalu baris 3 lalu baris 4 lalu baris 5 lalu baris 6 lalu baris 7 lalu baris 8 lalu baris 9
20. Klik header kolom Section satu kali
21. Verifikasi Section klik 1 (A-Z): baris 8 lalu baris 1 lalu baris 3 lalu baris 2 lalu baris 5 lalu baris 7 lalu baris 6 lalu baris 4 lalu baris 9
22. Klik header kolom Section kali kedua
23. Verifikasi Section klik 2 (Z-A): baris 9 lalu baris 4 lalu baris 6 lalu baris 7 lalu baris 2 lalu baris 3 lalu baris 5 lalu baris 1 lalu baris 8
24. Klik header kolom Section kali ketiga
25. Verifikasi Section klik 3: urutan bawaan baris 1 lalu baris 2 lalu baris 3 lalu baris 4 lalu baris 5 lalu baris 6 lalu baris 7 lalu baris 8 lalu baris 9
26. Klik header kolom Field satu kali
27. Verifikasi Field klik 1 (A-Z): baris 1 lalu baris 8 lalu baris 5 lalu baris 3 lalu baris 2 lalu baris 7 lalu baris 6 lalu baris 4 lalu baris 9
28. Klik header kolom Field kali kedua
29. Verifikasi Field klik 2 (Z-A): baris 9 lalu baris 4 lalu baris 6 lalu baris 7 lalu baris 2 lalu baris 3 lalu baris 5 lalu baris 8 lalu baris 1
30. Klik header kolom Field kali ketiga
31. Verifikasi Field klik 3: urutan bawaan baris 1 lalu baris 2 lalu baris 3 lalu baris 4 lalu baris 5 lalu baris 6 lalu baris 7 lalu baris 8 lalu baris 9

### TC-FA-PREF-331: Kolom Actions (⋯) tidak memiliki ikon sort

32. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
33. Verifikasi header kolom Date menampilkan ikon sort
34. Verifikasi header kolom Actions (⋯) tidak menampilkan ikon sort dan tidak dapat diurutkan

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baris seed Changelog disebut "baris N" mengikuti tabel PB-C1 di Prerequisites; Modified By ditulis `Budi S` dan `Rina A` sesuai format kolom (R-14).
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih untuk tiap TC. Setiap siklus sort berakhir pada state netral (klik ketiga), sehingga tidak ada sort aktif yang tersisa (S-09).
- Asersi tambahan (S-03): "Verifikasi header kolom Date menampilkan ikon sort" pada TC-FA-PREF-331 adalah anchor positif untuk asersi absence ikon sort kolom Actions (8b.2); TC tidak memuatnya.
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-323 sampai 325 dan 331; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - Kolom Section baris seed 1 (Chart of Accounts) dan baris 4 (Journal Export) serta Date baris seed 4 dan 5 tidak tertulis eksplisit di TC; Section disimpulkan dari urutan sort TC-FA-PREF-325 dan daftar opsi Section TC-FA-PREF-306.
  - TC-FA-PREF-331 Expected "tidak dapat diurutkan" tidak punya langkah aksi di TC (hanya mengamati header); spec memverifikasinya bersama klausa ikon sort.
