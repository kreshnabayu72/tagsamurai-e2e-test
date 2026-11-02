---
id: TC-FA-CAT-E2E-188-popup-detail-full-path-penutupan-dan-tanpa-tab-changelog
title: "Popup Detail Category: Category Name Full Path, Penutupan Hanya lewat Close atau Esc, dan Tanpa Tab Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-278
  - TC-FA-CAT-279
  - TC-FA-CAT-280
coverage:
  web: automated
---

# Popup Detail Category: Category Name Full Path, Penutupan Hanya lewat Close atau Esc, dan Tanpa Tab Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Spare Part` > `Bolt` > `Bolt M8`, `Furniture` (level 1), `Electronics` > `Laptop`; Pre-setup #21 dan #22.
- Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-278: Category Name pada header Detail menampilkan full path untuk node bersarang dan nama saja untuk level 1

1. Perluas node `Spare Part` di Sidebar Category Tree, lalu klik node `Bolt`
2. Klik elipsis (⋯) pada baris `Bolt M8` > `Detail`
3. Verifikasi Category Name `Spare Part › Bolt › Bolt M8`
4. Klik icon Close (✕)
5. Klik node `All Categories` di Sidebar Category Tree
6. Klik elipsis (⋯) pada baris `Furniture` > `Detail`
7. Verifikasi Category Name `Furniture`
8. Klik icon Close (✕)

### TC-FA-CAT-279: Popup Detail ditutup hanya lewat icon Close atau Esc dan klik backdrop diabaikan

9. Klik node `Electronics` di Sidebar Category Tree
10. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
11. Klik area backdrop di luar popup
12. Verifikasi popup tetap terbuka
13. Tekan `Esc`
14. Verifikasi popup tertutup
15. Verifikasi tidak ada dialog yang tampil

### TC-FA-CAT-280: Popup Detail tidak memiliki tab Changelog dan riwayat dilihat lewat Modal Changelog

16. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
17. Cari tab atau tombol Changelog di dalam popup
18. Verifikasi popup tidak memiliki tab maupun Changelog
19. Klik icon Close (✕)
20. Klik icon Changelog pada toolbar
21. Verifikasi Modal `Changelog: Category` terbuka
22. Verifikasi Modal Changelog dapat difilter dengan Category Name `Electronics › Laptop`
23. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-FA-CAT-272 sampai TC-FA-CAT-275 ada di spec 081.
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): memperluas dan memilih node sidebar, icon Close (✕), menutup Modal Changelog.
- Temuan untuk QA:
  - TC-FA-CAT-280 Expected b ("dapat difilter dengan Category Name `Electronics › Laptop`") tidak punya langkah aksi filter di TC; cara memfilter tidak dijelaskan.
  - TC-FA-CAT-279 tidak menyebut apakah `Esc` ditekan saat fokus berada di popup; spec mengikuti TC.
