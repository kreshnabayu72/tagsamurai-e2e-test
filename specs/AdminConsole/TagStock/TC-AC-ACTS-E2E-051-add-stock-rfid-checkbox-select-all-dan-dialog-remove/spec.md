---
id: TC-AC-ACTS-E2E-051-add-stock-rfid-checkbox-select-all-dan-dialog-remove
title: "Add Stock RFID: Kolom Checkbox, Select All dan Unselect All, Bulk Action Bar Remove, serta Dialog Remove TAG dan TAGs"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-868
  - TC-AC-ACTS-869
  - TC-AC-ACTS-870
  - TC-AC-ACTS-871
coverage:
  web: automated
---

# Add Stock RFID: Kolom Checkbox, Select All dan Unselect All, Bulk Action Bar Remove, serta Dialog Remove TAG dan TAGs

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`. Jalur approval normal (tanpa bypass E2a).
- Login di hook `before` spec ini sebagai Distributor Toggle ON; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #12 `RFID-ASSET-CORE-R5` (Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, TAG Type RFID).
- Kemampuan teknis: simulator pemindai RFID (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji RFID (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | EPC | UID |
|---|---|---|
| TAG A | `Fixture.tagStock.rfidA.epc` (`E280116060000208A1B2C3`) | `Fixture.tagStock.rfidA.uid` (`A1B2C3D4E5F6`) |
| TAG B | `Fixture.tagStock.rfidB.epc` (`E280116060000208D4E5F6`) | `Fixture.tagStock.rfidB.uid` (`A1B2C3D4E5F7`) |
| TAG C | `Fixture.tagStock.rfidC.epc` | `Fixture.tagStock.rfidC.uid` |

- Unit existing (status Available, Data Uji Dinamis #7) di-seed fixture BE milik spec dan dipulihkan di hook `after`: satu unit pada SKU `RFID-ASSET-CORE-R5` memegang EPC TAG B (UID TAG B baru) sehingga TAG B berstatus Waiting for Approval pada Scanned TAG List.
- TAG tambahan (TC-AC-ACTS-871): 9 TAG unik tambahan dari `Fixture.tagStock.bulk9` agar Scanned TAG List mencapai 12 baris.
- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
2. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`
3. Klik `[Add by Scan]`
4. Scan TAG A
5. Scan TAG B
6. Scan TAG C
7. Klik `[Stop]`

### TC-AC-ACTS-868: Kolom Checkbox, Select All, Unselect All, dan Bulk Action Bar

8. Verifikasi kolom Checkbox ada di paling kiri (pinned) sebelum kolom `#`
9. Centang TAG A
10. Verifikasi bar tampil dengan `1 TAG selected`
11. Verifikasi tombol `Bulk Action` berisi satu aksi `Remove`
12. Verifikasi tombol `Select All (3 records)` tampil
13. Klik `Select All (3 records)`
14. Verifikasi bar menampilkan `3 TAGs selected`
15. Verifikasi tombol berubah menjadi `Unselect All`
16. Klik `Unselect All`
17. Verifikasi seleksi dibatalkan
18. Verifikasi bar hilang

### TC-AC-ACTS-869: Semua baris punya checkbox

19. Verifikasi baris TAG B berstatus Waiting for Approval
20. Verifikasi baris TAG A, TAG B, dan TAG C memiliki checkbox
21. Klik checkbox header
22. Verifikasi checkbox header memilih ketiga baris
23. Verifikasi bar menampilkan `3 TAGs selected`
24. Klik `Unselect All`

### TC-AC-ACTS-870: Dialog Remove TAG dan Cancel

25. Centang TAG A
26. Pilih Bulk Action > `Remove`
27. Verifikasi dialog `Remove TAG`: `• <EPC TAG A>`, `For more accurate results, use Remove by Scan.`, `Are you sure you want to remove it?`, tombol `[Cancel]` dan `[Remove]`
28. Klik `[Cancel]`
29. Verifikasi list tetap 3 baris
30. Verifikasi bar tetap `1 TAG selected`
31. Klik `Unselect All`

### TC-AC-ACTS-871: Dialog Remove TAGs dengan 12 baris

32. Klik `[Add by Scan]`, scan 9 TAG tambahan dari fixture "TAG tambahan", lalu klik `[Stop]`
33. Klik `Select All (12 records)`
34. Pilih Bulk Action > `Remove`
35. Verifikasi dialog `Remove TAGs` memuat 12 bullet identifier lengkap dalam container scrollable tanpa ringkasan jumlah
36. Gulir daftar bullet sampai bullet terakhir
37. Verifikasi dialog `Remove TAGs`: `For more accurate results, use Remove by Scan.`, `Are you sure you want to remove them?`, tombol `[Cancel]` dan `[Remove]`
38. Klik `[Cancel]`
39. Klik `Unselect All`
40. Klik `[Cancel]`
41. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
42. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (membuka halaman Add Stock), pembentukan list precondition TC (scan TAG A, B, C lalu `[Stop]`), `Unselect All` dan `[Cancel]` antar TC (S-09), dan penutupan halaman dirty di akhir (S-08).
- Temuan untuk QA:
  - TC-AC-ACTS-871 mencantumkan precondition "list 3 baris" dan "list 12 baris" bersamaan; spec memperluas list menjadi 12 baris dengan 9 TAG tambahan.
  - TC-AC-ACTS-868 kolom `#` dan 871 kolom pinned tidak punya Expected tooltip; tidak ada yang diasersi di luar teks TC.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator RFID) dan satu dataset (Scanned TAG List berisi TAG A, B, C); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
