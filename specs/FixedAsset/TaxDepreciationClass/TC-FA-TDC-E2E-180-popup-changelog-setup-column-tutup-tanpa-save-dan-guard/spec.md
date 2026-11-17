---
id: TC-FA-TDC-E2E-180-popup-changelog-setup-column-tutup-tanpa-save-dan-guard
title: "Popup Changelog Setup Column: Reset to Default, Tutup Tanpa Save, dan Guard Satu Kolom Tersisa"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-645
  - TC-FA-TDC-646
  - TC-FA-TDC-647
sourceRules: ["§4.1.1#r25", "§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r29", "§4.1.1#r30", "§4.1.1#r31", "§5#b9", "§4.5#b1", "§4.1.1#b4"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r25": [10, 14]
  "§4.1.1#r26": [10, 14]
  "§4.1.1#r27": [10, 14]
  "§4.1.1#r28": [10, 14]
  "§4.1.1#r29": [10, 14]
  "§4.1.1#r30": [10, 14]
  "§4.1.1#r31": [10, 14]
  "§5#b9": [14, 20, 26]
  "§4.5#b1": 25
  "§4.1.1#b4": [31, 36]
anchor: [19]
coverage:
  web: automated
---

# Popup Changelog Setup Column: Reset to Default, Tutup Tanpa Save, dan Guard Satu Kolom Tersisa

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL); `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` berisi 16 entri Popup Changelog sesuai Example Data Modal Changelog PRD. Konfigurasi kolom Popup Changelog dalam keadaan default (urutan `Date | Action | Class Code | Field | Old Value | New Value | Modified By`, tujuh kolom tampil). Data Dinamis: tidak ada.
- Kemampuan teknis: riwayat Changelog diatur ke 16 entri Example Data lewat Fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD); Popup Setup Column dengan Live Preview dan Overlay Column Visibility pada Popup Changelog; mengarahkan kursor (hover) untuk tooltip; konfigurasi kolom Popup Changelog tersimpan di browser dan dibaca ulang setelah muat ulang halaman; pemulihan lewat langkah eksplisit (8b.14, R-24).
- State global yang diubah: konfigurasi kolom Popup Changelog. Blok TC-FA-TDC-645 menyimpan perubahan lalu `[Reset to Default]` dan `[Save]` (langkah 9 sampai 11) mengembalikan susunan default; blok TC-FA-TDC-647 mengembalikan kolom yang di-uncheck pada Overlay (langkah 37). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

1. Klik icon Changelog

### TC-FA-TDC-645: Reset to Default di Popup Setup Column Popup Changelog

2. Klik icon `⋯` pada header kolom Actions
3. Klik `Setup Column...`
4. Hapus centang kolom Date
5. Seret kolom Modified By ke posisi paling atas daftar
6. Klik `[Save]`
7. Klik icon `⋯` pada header kolom Actions
8. Klik `Setup Column...`
9. Klik `[Reset to Default]`
10. Verifikasi Live Preview kembali ke susunan default (urutan dan visibilitas awal)
11. Klik `[Save]`
12. Muat ulang halaman (F5)
13. Klik icon Changelog untuk membuka kembali Popup Changelog
14. Verifikasi susunan kolom tabel sama dengan default awal

### TC-FA-TDC-646: Menutup Popup Setup Column tanpa Save membuang perubahan

15. Klik icon `⋯` pada header kolom Actions
16. Klik `Setup Column...`
17. Hapus centang kolom Date
18. Klik `(X)` pada Popup Setup Column
19. Verifikasi Popup Setup Column tertutup
20. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir dengan kolom Date tampil
21. Klik icon `⋯` pada header kolom Actions
22. Klik `Setup Column...`
23. Hapus centang kolom Date
24. Tekan Esc
25. Verifikasi Popup Setup Column tertutup
26. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir dengan kolom Date tampil

### TC-FA-TDC-647: Guard satu kolom tersisa pada Popup Changelog

27. Klik icon `⋯` pada header kolom Actions
28. Klik `Setup Column...`
29. Hapus centang kolom Date, Action, Class Code, Field, Old Value, dan New Value
30. Arahkan kursor ke checkbox Modified By pada Popup Setup Column
31. Verifikasi checkbox Modified By pada Popup Setup Column Disabled (tetap tampil) dengan tooltip `At least one column must remain visible.`
32. Tutup Popup Setup Column tanpa `[Save]` lewat `(X)`
33. Klik icon `⋯` pada header kolom Actions untuk membuka Overlay Column Visibility
34. Hapus centang kolom Date, Action, Class Code, Field, Old Value, dan New Value pada Overlay
35. Arahkan kursor ke checkbox Modified By pada Overlay
36. Verifikasi checkbox Modified By pada Overlay Disabled (tetap tampil) dengan tooltip `At least one column must remain visible.`
37. Centang kembali kolom Date, Action, Class Code, Field, Old Value, dan New Value pada Overlay
38. Tutup Overlay Column Visibility
39. Tutup Popup Changelog lewat ikon Close `(X)`

## Notes

- Alasan lebih dari sekitar 35 langkah: tiga TC Setup Column Popup Changelog dengan data Pre-setup yang sama dan satu kelas harness; tiap blok TC berdiri sendiri (kegagalan satu blok tidak menghapus makna blok lain) dan tiap blok mengembalikan konfigurasi kolom ke default sebelum blok berikutnya.
- Langkah 1 TC-FA-TDC-646 dan TC-FA-TDC-647 ("Klik icon Changelog") tidak diulang karena Popup Changelog tetap terbuka sejak langkah 1; langkah 13 membuka kembali Popup sesudah muat ulang halaman pada langkah 12.
- Langkah penghubung (S-03): langkah 12 dan 13 (muat ulang dan membuka kembali Popup), langkah 32 (menutup Popup Setup Column tanpa `[Save]` sesuai langkah 4 TC-FA-TDC-647), langkah 37 (mengembalikan kolom pada Overlay), langkah 38 dan 39 (menutup Overlay dan Popup Changelog).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-645 menyebut "Klik `[Save]` dan refresh" tanpa menyebut keadaan tabel yang diasersi sebelum Reset; spec hanya mengasersi susunan sesudah Reset dan sesudah F5.
  - TC-FA-TDC-646 tidak menyebut apakah penutupan Popup Setup Column dengan perubahan belum disimpan memicu dialog `Unsaved Changes`; spec mengikuti TC (Popup tertutup tanpa dialog).
  - TC-FA-TDC-647 langkah 2 dan 4 menyebut "uncheck semua kolom kecuali Modified By" tanpa menyatakan keadaan Overlay sesudah Popup ditutup tanpa Save, dan tidak menyatakan pemulihan kolom; spec mengembalikan kolom pada langkah 37.
  - TC-FA-TDC-645 sampai TC-FA-TDC-647 menyebut header kolom `Actions`, sedangkan TC-FA-TDC-613 menyebut `Column Visibility (⋯)`.
