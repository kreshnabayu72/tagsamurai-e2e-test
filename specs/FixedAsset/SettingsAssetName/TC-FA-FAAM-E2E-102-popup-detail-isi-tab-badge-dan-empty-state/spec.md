---
id: TC-FA-FAAM-E2E-102-popup-detail-isi-tab-badge-dan-empty-state
title: "Popup Detail: Tab Models per Brand, Linked Custom Fields, Empty State, dan Badge Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-305
  - TC-FA-FAAM-306
  - TC-FA-FAAM-307
  - TC-FA-FAAM-312
  - TC-FA-FAAM-313
coverage:
  web: automated
---

# Popup Detail: Tab Models per Brand, Linked Custom Fields, Empty State, dan Badge Status

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; seed API per TC mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Dinamis (suffix `{runId}-102`, seed di hook `before`, cleanup di hook `after`; hanya dibaca):
  - `No Model Item {runId}-102`: salinan Pre-setup #14k (Brand `Dell` tanpa model ketikan, model `No Model`).
  - `Linked Empty Item {runId}-102`: Asset Name tanpa custom field terkait (Pre-setup #14l).
- Data Pre-setup yang hanya dibaca: Pre-setup #10 `Dell Latitude` dengan 3 Linked Custom Fields Pre-setup #27 (`Cost Center` Dropdown Global `Finance`, `Operating System` Dropdown Specific, `Warranty Notes` Text kosong), fixture `Fixture.faAssetName.dellLatitude`; Pre-setup #12 `MacBook Pro` (Category Locked), fixture `Fixture.faAssetName.macBookPro`; Pre-setup #13 `Warehouse Pallet` (Non-TAG, Total Asset 0), fixture `Fixture.faAssetName.warehousePallet`. Tidak ada data yang diubah.
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-305: Tab Models per Brand menampilkan No Model dan tidak punya empty state

1. Ketik Search `No Model Item {runId}-102`, tekan Enter
2. Klik nama `No Model Item {runId}-102`
3. Verifikasi tab Models per Brand menampilkan baris `Dell` dengan badge `No Model`
4. Verifikasi tidak ada empty state pada tab Models per Brand
5. Klik icon `[✕]`

### TC-FA-FAAM-306: Tab Linked Custom Fields menampilkan tabel dan tautan dengan nilai per-asset

6. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
7. Klik nama `Dell Latitude`
8. Klik tab `Linked Custom Fields (3)`
9. Verifikasi tabel memiliki kolom `Field Name`, `Data Type`, `Global Value`
10. Verifikasi baris `Cost Center` dengan Data Type Dropdown dan Global Value `Finance`
11. Verifikasi baris `Operating System` dengan Data Type Dropdown dan Global Value `(per-asset)`
12. Verifikasi baris `Warranty Notes` dengan Data Type Text dan Global Value `—`
13. Verifikasi tautan `Open in Custom Fields ↗` tampil
14. Klik icon `[✕]`

### TC-FA-FAAM-307: Tab Linked Custom Fields kosong menampilkan empty state

15. Ganti isi kotak search dengan `Linked Empty Item {runId}-102`, tekan Enter
16. Klik nama `Linked Empty Item {runId}-102`
17. Klik tab `Linked Custom Fields (0)`
18. Verifikasi empty state Title `No custom fields linked` dan Description `No custom fields are scoped to this asset name.`
19. Klik icon `[✕]`

### TC-FA-FAAM-312: Popup Detail Asset Name Category Locked menampilkan badge Needs Update

20. Ganti isi kotak search dengan `MacBook Pro`, tekan Enter
21. Arahkan pointer ke badge `Needs Update` pada baris `MacBook Pro` di List dan catat teks tooltip
22. Klik nama `MacBook Pro`
23. Verifikasi Category tampil sebagai badge Primary
24. Verifikasi badge `Needs Update` tampil di samping Category
25. Arahkan pointer ke badge `Needs Update` pada Popup Detail
26. Verifikasi tooltip sama dengan tooltip badge `Needs Update` di List
27. Klik icon `[✕]`

### TC-FA-FAAM-313: Popup Detail Asset Name Non-TAG menampilkan teks Non-TAG dan Default Addon strip

28. Ganti isi kotak search dengan `Warehouse Pallet`, tekan Enter
29. Klik nama `Warehouse Pallet`
30. Verifikasi TAG Type menampilkan teks `Non-TAG` tanpa badge
31. Verifikasi Default Addon menampilkan `—`
32. Klik icon `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 1, 6, 15, 20, 28), `[✕]` menutup popup sebelum TC berikutnya (langkah 5, 14, 19, 27, 32; S-09), dan mencatat teks tooltip List (langkah 21) sebagai pembanding langkah 26.
- Asersi absence pada langkah 4 memakai baris `Dell` pada langkah 3 sebagai anchor.
- Temuan untuk QA:
  - TC-FA-FAAM-305 dan TC-FA-FAAM-307 tidak menyebut nama Asset Name (hanya "Asset Name tersebut" dan Pre-setup #14k, #14l); spec memakai salinan seed bernama `No Model Item {runId}-102` dan `Linked Empty Item {runId}-102`.
  - TC-FA-FAAM-312 Expected menyebut "tooltip yang sama dengan List" tanpa teks tooltip; spec membandingkan tooltip Popup Detail dengan tooltip badge pada baris List.
  - TC-FA-FAAM-306 Expected a menyebut Global Value `(per-asset)` untuk `Operating System`; spec mengasersi teks itu persis seperti TC.
