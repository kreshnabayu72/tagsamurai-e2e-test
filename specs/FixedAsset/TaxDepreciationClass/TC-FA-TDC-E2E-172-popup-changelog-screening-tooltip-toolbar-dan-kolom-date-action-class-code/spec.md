---
id: TC-FA-TDC-E2E-172-popup-changelog-screening-tooltip-toolbar-dan-kolom-date-action-class-code
title: "Popup Changelog: Screening, Tooltip Toolbar, serta Kolom Date, Action, dan Class Code"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-613
  - TC-FA-TDC-614
  - TC-FA-TDC-619
  - TC-FA-TDC-620
sourceRules: ["§5#b8", "§8#r1", "§4.1.1#p8", "§4.1.1#r25", "§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r29", "§4.1.1#r30", "§4.1.1#r31", "§5#b1", "§9.5#r3", "§4.1.1#r32", "§5#b5", "§4.1.1#r35", "L-09", "§4.1.1#r37", "L-11", "§4.1.1#r38", "§4.1.1#r39", "§4.1.1#r40", "§4.1.1#r41"]
smoke: []
dependsOn: []
trace:
  "§5#b8": [2, 4]
  "§8#r1": 2
  "§4.1.1#p8": [4, 8]
  "§4.1.1#r25": [5, 8, 16, 17]
  "§4.1.1#r26": [5, 18, 19]
  "§4.1.1#r27": [5, 20, 21, 22]
  "§4.1.1#r28": 5
  "§4.1.1#r29": 5
  "§4.1.1#r30": 5
  "§4.1.1#r31": 5
  "§5#b1": 6
  "§9.5#r3": [7, 9]
  "§4.1.1#r32": [8, 16, 18, 20]
  "§5#b5": 9
  "§4.1.1#r35": [17, 19]
  "L-09": 21
  "§4.1.1#r37": 21
  "L-11": 22
  "§4.1.1#r38": 22
  "§4.1.1#r39": 22
  "§4.1.1#r40": 22
  "§4.1.1#r41": 22
anchor: [3, 11, 13, 15]
coverage:
  web: automated
---

# Popup Changelog: Screening, Tooltip Toolbar, serta Kolom Date, Action, dan Class Code

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` berisi 16 entri Popup Changelog sesuai Example Data Modal Changelog PRD. Entri yang diasersi spec ini: 28/10/26 09:15 Delete NB-3, 22/10/26 14:20 Edit (baris 4), 15/10/26 Cancel Scheduled Version NB-2 (Jan 2027), dan empat baris Create versi Scheduled BLD-NP (Jan 2027) bertanggal 10/09/26. Format tanggal General Settings `dd/MM/yy HH:mm`. Data Dinamis: tidak ada.
- Kemampuan teknis: riwayat Changelog diatur ke 16 entri Example Data lewat Fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD); mengarahkan kursor (hover) untuk tooltip toolbar Popup.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-613: Screening Popup Changelog

1. Klik icon Changelog
2. Verifikasi Title Popup `Changelog: Tax Depreciation Class`
3. Verifikasi ikon Close `(X)` tampil di header Popup
4. Verifikasi toolbar Popup memuat `Search | Filter | Download`
5. Verifikasi kolom Popup berurutan `Date (sortable) | Action (sortable) | Class Code (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable)`
6. Verifikasi kolom `Column Visibility (⋯)` unsortable
7. Verifikasi Popup menampilkan 10 baris pertama
8. Verifikasi baris diurutkan Date Newest First dengan `28/10/26 09:15` di baris teratas
9. Verifikasi footer Popup memuat Pagination dengan page size default 10

### TC-FA-TDC-614: Tooltip toolbar Popup Changelog

10. Arahkan kursor ke icon Search pada toolbar Popup
11. Verifikasi tooltip `Search`
12. Arahkan kursor ke icon Filter pada toolbar Popup
13. Verifikasi tooltip `Filter`
14. Arahkan kursor ke icon Download pada toolbar Popup
15. Verifikasi tooltip `Download`

### TC-FA-TDC-619: Kolom Date dan Action di Popup Changelog

16. Verifikasi Date baris 1 `28/10/26 09:15`
17. Verifikasi Date baris 4 `22/10/26 14:20`
18. Verifikasi Action baris 1 `Delete` sebagai teks polos tanpa badge
19. Verifikasi Action baris 4 `Edit` sebagai teks polos tanpa badge

### TC-FA-TDC-620: Kolom Class Code di Popup Changelog

20. Verifikasi Class Code baris Delete NB-3 (28/10/26) `NB-3`
21. Verifikasi Class Code baris Cancel Scheduled Version (15/10/26) `NB-2 (Jan 2027)`
22. Verifikasi Class Code empat baris Create versi Scheduled (10/09/26) `BLD-NP (Jan 2027)`
23. Tutup Popup Changelog lewat ikon Close `(X)`

## Notes

- Langkah 1 TC-FA-TDC-614, TC-FA-TDC-619, dan TC-FA-TDC-620 ("Klik icon Changelog") tidak diulang karena Popup Changelog tetap terbuka sejak langkah 1; kasus yang hanya mengamati memakai satu pembukaan (prinsip 13, halaman yang sama dipakai berulang).
- Tiap `Verifikasi` tooltip ditulis tepat sesudah hover yang memicunya (8b.5).
- Langkah penghubung (S-03): langkah 23 (menutup Popup Changelog).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - Isi Popup Changelog memakai jumlah entri absolut (16 entri; 10 baris pada halaman pertama) pada audit trail permanen; Lampiran A konvensi tidak memuat pengecualian untuk modul ini. Spec mengikuti TC dan membutuhkan kemampuan Fixture BE yang menimpa riwayat Changelog dengan 16 entri Example Data (tidak disebut TC, PRD, atau LLD).
  - TC-FA-TDC-613 menyebut header kolom terakhir `Column Visibility (⋯)`, sedangkan TC-FA-TDC-640 menyebut header kolom `Actions`.
  - TC-FA-TDC-620 menyebut "baris Cancel Scheduled Version" sebagai baris Action, padahal opsi Action pada TC-FA-TDC-630 hanya `Create`, `Delete`, dan `Edit`; nilai Action baris itu tidak disebut.
  - TC-FA-TDC-619 tidak menyebut entri yang menempati baris 1 dan baris 4 selain tanggal dan Action.
