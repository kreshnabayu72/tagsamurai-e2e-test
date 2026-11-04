---
id: TC-FA-NOTIF-E2E-006-state-loading-dropdown-panel-dan-notification-center
title: "State Loading Dropdown Panel dan Notification Center serta Tooltip Icon Toolbar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-17
  - TC-FA-NOTIF-26
  - TC-FA-NOTIF-58
coverage:
  web: automated
---

# State Loading Dropdown Panel dan Notification Center serta Tooltip Icon Toolbar

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard, Dropdown Panel, dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed notifikasi N-01 sampai N-07 (Pre-setup #17) milik akun aktor. Spec hanya membaca data; fixture BE pemulih seed dijalankan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Kemampuan teknis: intercept respons jaringan di atas backend nyata (`Spectra.intercept()`, disebut di `suite.md`) untuk menahan respons snapshot notifikasi (Dropdown Panel) dan respons list notifikasi (Notification Center) selama 3 detik. Penahanan hanya untuk mengamati state Loading, bukan kegagalan yang dipaksakan. Pola URL respons ditentukan tim FE (TC tidak menyebut endpoint) dan intercept dilepas segera setelah state Loading teramati.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true) dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-17: Dropdown Panel: state Loading saat mengambil snapshot awal

1. Tahan respons snapshot notifikasi selama 3 detik lewat intercept
2. Klik Bell icon
3. Verifikasi Loading component tampil pada Dropdown Panel
4. Verifikasi belum ada item dan belum ada empty state pada Dropdown Panel
5. Lepas tahanan respons snapshot (intercept dilepas)

### TC-FA-NOTIF-26: Notification Center: state Loading saat mengambil snapshot awal

6. Muat ulang halaman, lalu tahan respons list notifikasi selama 3 detik lewat intercept
7. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
8. Verifikasi Loading component tampil pada list Notification Center
9. Verifikasi belum ada item dan belum ada empty state pada list
10. Lepas tahanan respons list (intercept dilepas)

### TC-FA-NOTIF-58: Tooltip icon toolbar Search dan Filter

11. Verifikasi list Notification Center memuat item N-01
12. Arahkan kursor ke icon Search
13. Verifikasi tooltip icon Search `Search`
14. Arahkan kursor ke icon Filter
15. Verifikasi tooltip icon Filter `Filter`

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Menahan respons hanya untuk mengamati Loading bukan kegagalan yang dipaksakan (kelas b tidak berlaku; bagian 3 prinsip 13b), sehingga TC-17 dan TC-26 berada di spec fungsional ini.
- Langkah penghubung (S-03): langkah 5 dan 10 (lepas tahanan respons), langkah 6 (muat ulang halaman sebelum menahan respons berikutnya), langkah 7 (buka Notification Center), langkah 11 (anchor bahwa list Notification Center sudah termuat setelah tahanan dilepas; asersi tambahan di luar Expected TC).
- Temuan untuk QA:
  - TC-17 dan TC-26 menulis "perlambat respons (delay response jaringan)" tanpa menyebut endpoint atau pola URL yang ditahan; spec menyerahkan pola URL ke tim FE (S-13).
