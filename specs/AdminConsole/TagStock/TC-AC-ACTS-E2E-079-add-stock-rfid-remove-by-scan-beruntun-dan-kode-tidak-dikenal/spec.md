---
id: TC-AC-ACTS-E2E-079-add-stock-rfid-remove-by-scan-beruntun-dan-kode-tidak-dikenal
title: "Add Stock RFID: Remove by Scan Beruntun Tanpa Jeda, TAG Tidak di List, dan Kode Tidak Dikenal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-875
  - TC-AC-ACTS-876
coverage:
  web: automated
---

# Add Stock RFID: Remove by Scan Beruntun Tanpa Jeda, TAG Tidak di List, dan Kode Tidak Dikenal

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
| TAG D | `Fixture.tagStock.rfidD.epc` | `Fixture.tagStock.rfidD.uid` |

- Unit existing (status Available, Data Uji Dinamis #7) di-seed fixture BE milik spec dan dipulihkan di hook `after`: satu unit pada SKU `RFID-ASSET-CORE-R5` memegang EPC TAG B (UID TAG B baru) sehingga TAG B berstatus Waiting for Approval pada Scanned TAG List.
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

### TC-AC-ACTS-875: Remove by Scan beruntun tanpa jeda

8. Hover tombol `[Remove by Scan]`
9. Verifikasi tooltip `Scanned TAGs are removed from the list immediately.`
10. Klik `[Remove by Scan]`
11. Scan TAG A lalu TAG C berturut-turut tanpa menunggu
12. Verifikasi toast `Success, <EPC TAG A> has been removed.`
13. Verifikasi toast `Success, <EPC TAG C> has been removed.`
14. Verifikasi tidak ada dialog
15. Verifikasi scan TAG C diproses tanpa tertahan oleh scan TAG A
16. Verifikasi live counter widget `1 TAG scanned`
17. Klik `[Stop]`
18. Verifikasi list hanya menyisakan TAG B
19. Tutup toast

### TC-AC-ACTS-876: Unit tidak ada di list dan kode tidak dikenal

20. Klik `[Add by Scan]`
21. Scan TAG A
22. Scan TAG C
23. Klik `[Stop]`
24. Klik `[Remove by Scan]`
25. Scan TAG D yang tidak ada di list
26. Verifikasi toast error `Error, TAG not found in list.`
27. Tutup toast
28. Scan kode yang bukan identifier TAG
29. Verifikasi toast error `Error, can't recognize TAG.`
30. Verifikasi tidak ada dialog
31. Verifikasi sesi tetap aktif (widget `Removing TAGs...` masih tampil)
32. Tutup toast
33. Scan TAG C
34. Verifikasi toast `Success, <EPC TAG C> has been removed.`
35. Klik `[Stop]`
36. Verifikasi list menyisakan TAG A dan TAG B
37. Klik `[Cancel]`
38. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
39. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (membuka halaman Add Stock), pembentukan list precondition (scan TAG A, B, C lalu `[Stop]`; TAG A dan C dipindai ulang untuk TC-AC-ACTS-876 karena sudah dihapus pada TC-AC-ACTS-875), penutupan toast agar toast berulang tidak tertukar (R-12), dan penutupan halaman dirty di akhir (S-08, S-09).
- Counter widget pada scan beruntun hanya diasersi pada nilai akhir `1 TAG scanned`.
- Temuan untuk QA:
  - TC-AC-ACTS-875 Expected (c) menulis counter `2 TAGs scanned` lalu `1 TAG scanned`; nilai antara tidak teramati pada scan beruntun tanpa jeda, sehingga hanya nilai akhir yang diasersi.
  - TC-AC-ACTS-876 memakai kata "kode yang bukan identifier TAG" tanpa nilai; disediakan simulator reader tim FE.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator RFID) dan satu dataset (Scanned TAG List berisi TAG A, B, C); tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
