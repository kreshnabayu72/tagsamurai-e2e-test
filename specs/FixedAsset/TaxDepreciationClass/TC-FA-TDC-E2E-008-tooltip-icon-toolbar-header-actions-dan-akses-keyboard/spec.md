---
id: TC-FA-TDC-E2E-008-tooltip-icon-toolbar-header-actions-dan-akses-keyboard
title: "Tooltip Icon Toolbar, Header Actions, dan Akses Keyboard"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-15
  - TC-FA-TDC-35
sourceRules: ["§4.7#r5", "§4.7#r6", "§4.5#b5"]
smoke: []
dependsOn: []
trace:
  "§4.7#r5": [4, 14]
  "§4.7#r6": [8, 18]
  "§4.5#b5": [12, 14, 16, 18]
anchor: [2, 6, 10]
coverage:
  web: automated
---

# Tooltip Icon Toolbar, Header Actions, dan Akses Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND belum diubah. Data Dinamis: tidak ada.
- Kemampuan teknis: mengarahkan kursor (hover) dan menekan `Tab` untuk memindahkan fokus keyboard; membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-15: Tooltip icon toolbar dan header kolom Actions

1. Arahkan kursor ke icon Search
2. Verifikasi tooltip Search `Search`
3. Arahkan kursor ke icon Filter
4. Verifikasi tooltip Filter `Filter`
5. Arahkan kursor ke icon Download
6. Verifikasi tooltip Download `Download`
7. Arahkan kursor ke icon Changelog
8. Verifikasi tooltip Changelog `Changelog`
9. Arahkan kursor ke icon `⋯` pada header kolom Actions
10. Verifikasi tooltip header Actions `Column Visibility`

### TC-FA-TDC-35: Tooltip toolbar dapat diakses lewat keyboard focus

11. Tekan Tab hingga fokus berada pada icon Search
12. Verifikasi fokus pada icon Search menampilkan tooltip `Search`
13. Tekan Tab hingga fokus berada pada icon Filter
14. Verifikasi fokus pada icon Filter menampilkan tooltip `Filter`
15. Tekan Tab hingga fokus berada pada icon Download
16. Verifikasi fokus pada icon Download menampilkan tooltip `Download`
17. Tekan Tab hingga fokus berada pada icon Changelog
18. Verifikasi fokus pada icon Changelog menampilkan tooltip `Changelog`

## Notes

- Tiap `Verifikasi` tooltip ditulis tepat sesudah hover atau fokus yang memicunya karena tooltip adalah state sementara (8b.5).
- Langkah penghubung (S-03): tidak ada.
- Temuan untuk QA:
  - TC-FA-TDC-35 langkah 1 menyebut urutan fokus "Search, lalu Filter, Download, dan Changelog satu per satu" tanpa menyebut elemen yang menerima fokus sebelum Search; spec menekan Tab hingga fokus tiba di tiap icon.
  - Email akun Total Control tidak tertulis di TC.
