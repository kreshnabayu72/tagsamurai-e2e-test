---
id: TC-FA-PREF-E2E-108-changelog-sort-old-value-new-value-modified-by-dan-pindah-kolom-sort-tidak-mereset-search-filter
title: "Changelog Sort: Old Value, New Value, Modified By, dan berpindah kolom sort tidak mereset Search dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-327
  - TC-FA-PREF-328
  - TC-FA-PREF-329
  - TC-FA-PREF-330
coverage:
  web: automated
---

# Changelog Sort: Old Value, New Value, Modified By, dan berpindah kolom sort tidak mereset Search dan Filter

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

### TC-FA-PREF-327: Sort kolom Old Value campuran tipe data dengan nilai kosong di akhir saat ascending

1. Klik ikon View history di header tab Preferences
2. Klik header kolom Old Value satu kali
3. Verifikasi ascending: baris 8 lalu baris 5 lalu baris 4 lalu baris 6 lalu baris 7 lalu baris 3 lalu baris 2, dengan dua baris Old Value "—" (baris 1 dan baris 9) di akhir
4. Klik header kolom Old Value kali kedua
5. Verifikasi descending: dua baris Old Value "—" (baris 1 lalu baris 9) di awal, lalu baris 2 lalu baris 3 lalu baris 7 lalu baris 6 lalu baris 4 lalu baris 5 lalu baris 8
6. Klik header kolom Old Value kali ketiga
7. Verifikasi urutan kembali ke urutan bawaan: baris 1 lalu baris 2 lalu baris 3 lalu baris 4 lalu baris 5 lalu baris 6 lalu baris 7 lalu baris 8 lalu baris 9

### TC-FA-PREF-328: Sort kolom New Value campuran tipe data dengan nilai kosong di akhir saat ascending

8. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
9. Klik header kolom New Value satu kali
10. Verifikasi ascending: baris 8 lalu baris 1 lalu baris 6 lalu baris 4 lalu baris 9 lalu baris 7 lalu baris 3 lalu baris 2, dengan baris 5 (New Value "—") di akhir
11. Klik header kolom New Value kali kedua
12. Verifikasi descending: baris 5 (New Value "—") di awal, lalu baris 2 lalu baris 3 lalu baris 7 lalu baris 9 lalu baris 4 lalu baris 6 lalu baris 1 lalu baris 8
13. Klik header kolom New Value kali ketiga hingga indikator sort hilang

### TC-FA-PREF-329: Sort kolom Modified By berdasarkan nama lengkap

14. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
15. Klik header kolom Modified By satu kali
16. Verifikasi A-Z: baris 1 lalu baris 4 lalu baris 9 (Budi S) lalu baris 3 lalu baris 2 lalu baris 5 lalu baris 7 lalu baris 6 lalu baris 8 (Rina A)
17. Klik header kolom Modified By kali kedua
18. Verifikasi Z-A: baris 2 lalu baris 3 lalu baris 5 lalu baris 6 lalu baris 7 lalu baris 8 (Rina A) lalu baris 1 lalu baris 4 lalu baris 9 (Budi S)
19. Klik header kolom Modified By kali ketiga hingga indikator sort hilang

### TC-FA-PREF-330: Berpindah kolom sort tidak mereset Search dan Filter

20. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
21. Ketik Search "Rina", tekan Enter
22. Klik header kolom Date satu kali
23. Klik header kolom Action satu kali
24. Verifikasi indikator sort pada Date hilang
25. Verifikasi indikator ascending pada Action aktif
26. Verifikasi kata kunci Search tetap "Rina"
27. Verifikasi tabel menampilkan baris Modified By Rina A
28. Verifikasi tabel tidak menampilkan baris Modified By Budi S
29. Klik `(←)` pada kotak Search
30. Klik header kolom Action dua kali hingga indikator sort hilang

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baris seed Changelog disebut "baris N" mengikuti tabel PB-C1 di Prerequisites; Modified By ditulis `Budi S` dan `Rina A` sesuai format kolom (R-14).
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih; klik ketiga pada TC-FA-PREF-328 dan TC-FA-PREF-329, serta "Klik `(←)` pada kotak Search" dan klik Action dua kali di akhir TC-FA-PREF-330, mengembalikan sort dan Search ke keadaan awal (S-09).
- Klausa "hanya baris Modified By Rina A" TC-FA-PREF-330 Expected b ditulis dua Verifikasi (baris Rina A tampil, baris Budi S tidak tampil), dengan baris Rina A sebagai anchor positif (8b.2).
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-327 sampai 330; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - Kolom Section baris seed 1 (Chart of Accounts) dan baris 4 (Journal Export) serta Date baris seed 4 dan 5 tidak tertulis eksplisit di TC; Section disimpulkan dari urutan sort TC-FA-PREF-325 dan daftar opsi Section TC-FA-PREF-306.
  - TC-FA-PREF-329 judul menyebut sort berdasarkan nama lengkap, sedangkan kolom tampil `Budi S` dan `Rina A`; spec mengasersi urutan baris sesuai Expected TC.
