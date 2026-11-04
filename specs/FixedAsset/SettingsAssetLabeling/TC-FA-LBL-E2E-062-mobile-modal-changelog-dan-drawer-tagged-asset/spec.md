---
id: TC-FA-LBL-E2E-062-mobile-modal-changelog-dan-drawer-tagged-asset
title: "Mobile: Modal Changelog: Labels dan Drawer Tagged Asset sebagai full-screen sheet"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:mobile-layout/modal-changelog-labels
  - FALB:mobile-layout/tagged-asset-drawer
coverage:
  mobile: automated
---

# Mobile: Modal Changelog: Labels dan Drawer Tagged Asset sebagai full-screen sheet

## Prerequisites

- Mode: FE+BE (backend nyata). Platform: aplikasi native Android (PRD §4.8 Mobile Layout); Modal Changelog dan Drawer Tagged Asset tampil sebagai sheet dengan card.
- Perangkat atau emulator Android dengan aplikasi TAG Samurai terpasang (`DU-66`), serta kemampuan mengetuk elemen UI, menggulir layar, dan membaca isi card; disediakan tim FE. Spec ini hanya berjalan di aplikasi mobile (`coverage.mobile: automated`). `parallel: false` untuk perangkat bersama.
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di aplikasi pada hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Tidak ada ganti akun. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji, dibuat lewat sesi API di hook `before` dan dihapus di hook `after` (aset lalu label): `DU-62` (Dataset Changelog: Labels) bersuffix `{runId}-062`, label `Log-{runId}-062-nn` dengan entri Create, Edit Label Name, Edit Color, dan Delete oleh `DU-01` dan `DU-31` (env `FA_TC2_EMAIL` dan `FA_TC2_PASSWORD`); dan `DU-59` (Dataset Drawer Tagged Asset) dengan label `Tagged-{runId}-062` dan 12 aset Active bersuffix.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, aset, dan entri Changelog, disediakan tim FE/BE.
- State global: tidak ada yang diubah; spec hanya membaca. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB:mobile-layout/modal-changelog-labels: Modal Changelog: Labels sebagai full-screen sheet dengan card per baris log

1. Ketuk ikon Changelog di header halaman
2. Verifikasi Modal Changelog: Labels tampil sebagai full-screen sheet
3. Buka bottom sheet toolbar pada Modal Changelog
4. Verifikasi bottom sheet toolbar memuat Filter dan Search
5. Ketik Search `DU-62`, tekan Enter
6. Tutup bottom sheet toolbar
7. Verifikasi tiap baris log milik `DU-62` tampil sebagai card, bukan baris tabel
8. Verifikasi card entri Edit Color menampilkan Date, Action, Label Name, Field, Old Value `#3B82F6` → New Value `#EF4444`, dan Modified By
9. Tutup Modal Changelog lewat `[✕]`

### FALB:mobile-layout/tagged-asset-drawer: Drawer Tagged Asset sebagai full-screen bottom sheet dengan card list per aset

10. Ketik Search `DU-59`, tekan Enter
11. Ketuk chip badge label milik `DU-59`
12. Verifikasi Drawer Tagged Asset tampil sebagai full-screen bottom sheet
13. Verifikasi daftar aset tampil sebagai card list per aset, bukan tabel
14. Verifikasi card aset menampilkan Name, Asset ID, TAG, Brand, Model/Type, Group, Status, dan Last Updated
15. Buka bottom sheet toolbar pada Drawer Tagged Asset
16. Verifikasi bottom sheet toolbar memuat Search dan Filter Panel
17. Tutup bottom sheet toolbar
18. Tutup Drawer Tagged Asset lewat `[✕]`

## Notes

- Langkah penghubung (S-03): langkah 1, 3, 11, dan 15 membuka elemen; langkah 5 dan 10 mempersempit daftar ke data `DU-62` dan `DU-59` (R-16); langkah 6, 9, 17, dan 18 menutup sheet.
- Anchor positif (bagian 8b butir 2): langkah 7 membuktikan card milik `DU-62` sudah termuat sebelum asersi isi card di langkah 8; langkah 13 membuktikan card aset termuat sebelum asersi isi di langkah 14.
- Kolom Visible Tabel 2 (Name, Asset ID, TAG, Brand, Model/Type, Group, Status, Last Updated) mengikuti PRD §4.8; kolom Curated (Hidden) tidak diasersi.
- Temuan PRD: PRD §4.8 menyatakan "Filter dan Search di bottom sheet toolbar" untuk Modal Changelog tanpa menyatakan elemen pemicu bottom sheet itu (ikon atau tombol); langkah 3 dan 15 membuka bottom sheet lewat pemicu yang tersedia di aplikasi dan tidak mengasersi bentuk pemicunya.
