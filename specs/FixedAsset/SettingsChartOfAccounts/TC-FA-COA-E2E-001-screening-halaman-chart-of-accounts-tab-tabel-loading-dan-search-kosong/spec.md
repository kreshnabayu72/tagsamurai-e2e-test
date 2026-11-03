---
id: TC-FA-COA-E2E-001-screening-halaman-chart-of-accounts-tab-tabel-loading-dan-search-kosong
title: "Screening Halaman Chart of Accounts: Tab, Tabel, Loading, dan Search Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-1
  - TC-FA-COA-3
  - TC-FA-COA-4
  - TC-FA-COA-138
coverage:
  web: automated
---

# Screening Halaman Chart of Accounts: Tab, Tabel, Loading, dan Search Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca, tidak dibuat atau diubah): akun P1 `5-6001 – Depreciation Expense – Admin`, P2 `6-2001 – Repairs & Maintenance Expense`, P3 `4-7001 – Gain on Disposal`, P4 `1-1002 – Equipment – Legacy Code`, P5 `CAP-6100 – Capitalization Clearing – Repairs`. Client uji memuat akun Pre-setup lebih dari 10 sehingga halaman pertama tabel penuh 10 baris.
- Kemampuan teknis: `Spectra.intercept()` menahan respons daftar akun (TC-FA-COA-4). Endpoint daftar akun tidak tertulis di TC; disediakan tim FE (S-13). Intercept dilepas pada langkah 31 dan dilepas lagi di hook `after` bila spec gagal di tengah.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-chart-of-accounts.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-1: Screening halaman Chart of Accounts saat tabel berisi data

1. Verifikasi Breadcrumb `Settings > Accounting > Chart of Accounts` tampil
2. Verifikasi tombol `[?]` tampil tepat di kanan Breadcrumb
3. Hover tombol `[?]`
4. Verifikasi tooltip tombol `[?]` `Show guide`
5. Hover icon Search di toolbar
6. Verifikasi tooltip icon Search `Search`
7. Klik icon Search
8. Verifikasi placeholder kotak Search `Search account...`
9. Klik `(←)` pada kotak Search
10. Hover icon Filter di toolbar
11. Verifikasi tooltip icon Filter `Filter`
12. Hover icon Download di toolbar
13. Verifikasi tooltip icon Download `Download`
14. Hover icon Changelog di toolbar
15. Verifikasi tooltip icon Changelog `Changelog`
16. Verifikasi toolbar rata kanan memuat Search, Filter, Download, Changelog, dan `+ Account`
17. Verifikasi kolom default tampil: Active, Account Code, Account Name, Function, Used By, dan Last Used in Journal
18. Verifikasi kolom Modified By dan Last Updated hidden
19. Verifikasi baris akun P4 `1-1002`, P3 `4-7001`, P1 `5-6001`, P2 `6-2001`, dan P5 `CAP-6100` tampil berurutan Account Code A-Z
20. Verifikasi halaman pertama tabel menampilkan 10 baris per halaman
21. Verifikasi Account Code tampil sebagai teks biasa (bukan link)

### TC-FA-COA-138: Tab Chart of Accounts aktif pada tab bar halaman Accounting

22. Verifikasi tab bar memuat empat tab berurutan dari kiri ke kanan: Preferences, Chart of Accounts, Tax Depreciation Class, Asset Class
23. Verifikasi tab `Chart of Accounts` berstatus aktif
24. Verifikasi Breadcrumb `Settings > Accounting > Chart of Accounts` tampil

### TC-FA-COA-3: Hasil Search/Filter kosong menampilkan empty state pencarian

25. Ketik Search `zzz`, tekan Enter
26. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
27. Klik `(←)` pada kotak Search

### TC-FA-COA-4: Tabel menampilkan loading shimmer saat data diambil

28. Tahan respons daftar akun (network delay)
29. Muat ulang halaman (F5)
30. Verifikasi tabel menampilkan Loading (Shimmer) selama data belum diterima
31. Lepas tahanan respons daftar akun
32. Verifikasi Loading (Shimmer) hilang
33. Verifikasi sedikitnya satu baris akun tampil di tabel

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Layar awal: langkah "Buka Settings > Accounting > Chart of Accounts" TC-FA-COA-1 dan TC-FA-COA-138 dikerjakan hook `beforeEach` suite (konvensi bagian 4); TC-FA-COA-4 membuka ulang layar lewat muat ulang (langkah 29).
- Urutan (S-10): screening TC-FA-COA-1 dan TC-FA-COA-138 (hanya baca) di awal, empty state pencarian TC-FA-COA-3, lalu TC-FA-COA-4 yang menahan respons di akhir.
- Langkah penghubung (S-03): langkah 9 dan 27 (menutup input Search dan mereset tabel, S-09); langkah 29 (muat ulang untuk membuka layar di bawah tahanan respons); langkah 31 (lepas tahanan respons).
- Asersi tambahan di luar Expected TC (S-03): langkah 33 menjadi anchor positif bahwa tabel selesai dimuat setelah Loading (Shimmer) hilang (bagian 8b butir 2); langkah 18 (kolom hidden) memakai langkah 17 sebagai anchor kolom lain tampil.
- Menahan respons daftar akun hanya untuk mengamati state Loading (TC-FA-COA-4), bukan kegagalan atau timeout yang dipaksakan, sehingga bukan kelas b (konvensi bagian 3, prinsip 13b) dan tidak memakai `P-2`.
- Temuan untuk QA:
  - TC-FA-COA-3 butir b ("Chip filter aktif dan `Clear all` tetap tampil bila ada filter") bersyarat, sedangkan Precondition dan Langkah Uji tidak menyiapkan filter aktif; spec mengikuti Langkah Uji TC (hanya Search `zzz`) dan butir b tidak diasersi.
  - TC-FA-COA-1 Post Condition "Tabel tetap dalam keadaan tersimpan" tidak punya langkah observasi sehingga tidak diasersi.
  - TC-FA-COA-1 butir e ("paginasi 10 per halaman") tidak menyebut jumlah akun client; spec mengasumsikan akun Pre-setup client lebih dari 10 (P1 sampai P115).
  - TC-FA-COA-4 tidak menyebut durasi tahanan respons; spec menahan sampai langkah 31.
