---
id: TC-FA-TDC-E2E-178-popup-changelog-setup-column-screening-overlay-popup-dan-kolom-default
title: "Popup Changelog Setup Column: Screening Overlay, Popup, dan Kolom Default"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-640
  - TC-FA-TDC-641
sourceRules: ["§4.4#r11", "§4.1.1#r25", "§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r29", "§4.1.1#r30", "§4.1.1#r31", "§4.1.1#p8"]
smoke: []
dependsOn: []
trace:
  "§4.4#r11": [3, 8]
  "§4.1.1#r25": [5, 6, 13, 14]
  "§4.1.1#r26": [5, 6, 13, 14]
  "§4.1.1#r27": [5, 6, 13, 14]
  "§4.1.1#r28": [5, 6, 13, 14]
  "§4.1.1#r29": [5, 6, 13, 14]
  "§4.1.1#r30": [5, 6, 13, 14]
  "§4.1.1#r31": [5, 6, 13, 14]
  "§4.1.1#p8": 10
anchor: [4, 7, 11, 12, 15, 16, 17]
coverage:
  web: automated
---

# Popup Changelog Setup Column: Screening Overlay, Popup, dan Kolom Default

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL); `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` berisi 16 entri Popup Changelog sesuai Example Data Modal Changelog PRD. Konfigurasi kolom Popup Changelog dalam keadaan default (tujuh kolom tampil). Format tanggal General Settings `dd/MM/yy HH:mm`. Data Dinamis: tidak ada.
- Kemampuan teknis: riwayat Changelog diatur ke 16 entri Example Data lewat Fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD); Overlay Column Visibility dan Popup Setup Column pada Popup Changelog beserta Live Preview.
- State global yang diubah: tidak ada (spec ini tidak menyimpan konfigurasi kolom).

## Test Steps

### TC-FA-TDC-640: Screening Overlay Column Visibility Popup Changelog

1. Klik icon Changelog
2. Klik icon `⋯` pada header kolom Actions
3. Verifikasi Overlay Column Visibility tampil menempel pada pemicu
4. Verifikasi Overlay tampil tanpa backdrop
5. Verifikasi Overlay memuat daftar kolom berurutan `Date | Action | Class Code | Field | Old Value | New Value | Modified By`
6. Verifikasi status checkbox default: Date, Action, Class Code, Field, Old Value, New Value, dan Modified By checked dan enabled
7. Verifikasi setiap baris kolom memiliki drag handle
8. Verifikasi item `Setup Column...` ada di bagian bawah panel

### TC-FA-TDC-641: Screening Popup Setup Column Popup Changelog

9. Klik `Setup Column...`
10. Verifikasi Title `Setup Column`
11. Verifikasi Deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
12. Verifikasi tombol Close `(X)` di kanan atas
13. Verifikasi daftar kolom berurutan `Date | Action | Class Code | Field | Old Value | New Value | Modified By` dengan checkbox, drag handle, dan icon Pin per baris
14. Verifikasi status checkbox default: Date, Action, Class Code, Field, Old Value, New Value, dan Modified By checked
15. Verifikasi Live Preview tabel menampilkan urutan header dan data sel yang sama dengan tabel asli
16. Verifikasi footer memuat tombol `[Reset to Default]` dan `[Save]` rata kanan
17. Verifikasi tidak ada tombol `[Cancel]`
18. Tutup Popup Setup Column lewat ikon Close `(X)`
19. Tutup Popup Changelog lewat ikon Close `(X)`

## Notes

- Langkah 1 TC-FA-TDC-641 ("Klik icon Changelog") dan langkah 2 ("Klik icon `⋯`") tidak diulang karena Popup Changelog dan pemicu Overlay sudah dipakai di langkah 1 dan 2; langkah 9 mengklik `Setup Column...` dari Overlay yang sama.
- Langkah penghubung (S-03): langkah 18 dan 19 (menutup Popup Setup Column dan Popup Changelog tanpa `[Save]`; tidak ada perubahan yang tersimpan).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-640 dan TC-FA-TDC-641 menyebut header kolom `Actions`, sedangkan TC-FA-TDC-613 menyebut `Column Visibility (⋯)`.
  - TC-FA-TDC-641 tidak menyebut data sel yang diasersi pada Live Preview selain "sama dengan tabel asli"; spec mengasersi urutan header dan data sel sama dengan tabel asli.
  - Isi Popup Changelog memakai 16 entri Example Data pada audit trail permanen; Lampiran A konvensi tidak memuat pengecualian untuk modul ini. Spec membutuhkan kemampuan Fixture BE yang menimpa riwayat Changelog (tidak disebut TC, PRD, atau LLD).
