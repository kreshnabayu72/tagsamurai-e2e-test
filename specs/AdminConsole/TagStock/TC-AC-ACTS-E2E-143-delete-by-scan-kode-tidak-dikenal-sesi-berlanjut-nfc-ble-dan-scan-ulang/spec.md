---
id: TC-AC-ACTS-E2E-143-delete-by-scan-kode-tidak-dikenal-sesi-berlanjut-nfc-ble-dan-scan-ulang
title: "Delete by Scan: Kode Bukan Identifier (T-29), Penolakan Tidak Menghentikan Sesi, SKU NFC dan BLE, dan Scan Ulang Kode yang Sudah Terhapus (T-31)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-828
  - TC-AC-ACTS-829
  - TC-AC-ACTS-830
  - TC-AC-ACTS-858
coverage:
  web: automated
---

# Delete by Scan: Kode Bukan Identifier (T-29), Penolakan Tidak Menghentikan Sesi, SKU NFC dan BLE, dan Scan Ulang Kode yang Sudah Terhapus (T-31)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Simulator pemindai NFC dan BLE (scan UID dan MAC) disediakan tim FE (lihat `suite.md`). Unit Available N1 (SKU `NFC-CARD-BETA-N2`) dan unit Available B1 (SKU `BLE-BEACON-ALPHA-B1`, Pre-setup #14) milik spec di-seed oleh fixture BE.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.

## Test Steps

### TC-AC-ACTS-828: Scan kode yang bukan identifier TAG dikenali ditolak dengan toast T-29

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Delete by Scan]`
3. Scan kode barcode yang bukan identifier TAG Samurai
4. Verifikasi toast error `Error, can't recognize TAG.`
5. Verifikasi tidak ada dialog dan sesi tetap aktif (Floating Widget `Deleting TAGs...` tampil)
6. Klik `[Stop]`
7. Verifikasi tidak ada unit terhapus (jumlah baris Tab Available sama dengan sebelum scan)
8. Tunggu toast lama hilang

### TC-AC-ACTS-829: Penolakan scan tidak menghentikan sesi; scan berikutnya yang eligible tetap terhapus

9. Klik `[Delete by Scan]`
10. Scan X1 (unit SKU lain)
11. Verifikasi toast error penolakan unit SKU lain tampil dan sesi tidak berhenti
12. Scan kode tidak dikenal
13. Verifikasi toast error `Error, can't recognize TAG.` tampil dan sesi tidak berhenti
14. Scan U2
15. Verifikasi toast `Success, [TAG Code] has been deleted.` dengan TAG Code U2
16. Verifikasi counter widget `1 TAG deleted`
17. Klik `[Stop]`
18. Verifikasi X1 tetap ada dan U2 tidak ada di tabel
19. Tunggu toast lama hilang

### TC-AC-ACTS-830: Delete by Scan pada SKU NFC dan BLE menghapus unit hasil scan UID dan MAC

20. Klik row action `Detail` pada SKU `NFC-CARD-BETA-N2` di Stock List, lalu buka Tab Available
21. Klik `[Delete by Scan]`
22. Verifikasi widget berstatus `Deleting TAGs...`
23. Scan UID unit N1
24. Verifikasi toast `Success, [TAG Code] has been deleted.` dengan TAG Code N1
25. Klik `[Stop]`
26. Verifikasi N1 tidak ada di tabel
27. Tunggu toast lama hilang
28. Kembali ke Stock List, lalu klik row action `Detail` pada SKU `BLE-BEACON-ALPHA-B1` dan buka Tab Available
29. Klik `[Delete by Scan]`
30. Verifikasi widget berstatus `Deleting TAGs...`
31. Scan MAC unit B1
32. Verifikasi toast `Success, [TAG Code] has been deleted.` dengan TAG Code B1
33. Klik `[Stop]`
34. Verifikasi B1 tidak ada di tabel
35. Tunggu toast lama hilang

### TC-AC-ACTS-858: Scan ulang kode yang sudah terhapus ditolak dengan toast T-31

36. Reset dataset: U1 sampai U4 lewat fixture BE
37. Kembali ke Stock List, buka Activity Log (filter Object `TAG Stock`), dan catat baseline jumlah entri `Delete by Scan` dan `Delete Stock`
38. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
39. Klik `[Delete by Scan]` dan scan U1
40. Verifikasi toast `Success, TAG-4F7K2XQ9 has been deleted.`
41. Scan U1 sekali lagi
42. Verifikasi toast error `Error, TAG not found in stock.`
43. Verifikasi tidak ada dialog dan sesi tetap aktif
44. Verifikasi counter widget `1 TAG deleted`
45. Klik `[Stop]`
46. Buka Activity Log (filter Object `TAG Stock`)
47. Verifikasi satu entri `Delete by Scan` baru (Old Value `1 TAG`) dari baseline
48. Verifikasi jumlah entri `Delete Stock` per unit sama dengan baseline

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), `[Stop]`, "Reset dataset", navigasi antar SKU, Stock List, dan Activity Log, serta "Tunggu toast lama hilang" (pemulihan state, S-09).
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Identifier dan hitungan tetap (Data Uji Dinamis) dipakai ulang lintas TC dan tidak dapat bersuffix per run; kebenaran hitungan hanya terjamin bila fixture BE mereset dataset sebelum spec.
  - TC-AC-ACTS-829 menyebut penolakan unit SKU lain tanpa teks toast pada Expected butir a; spec mengasersi bahwa toast error penolakan tampil dan memakai teks T-26 (`Error, this TAG belongs to another SKU and can't be deleted here.`) dari TC-AC-ACTS-824.
  - TC-AC-ACTS-830 menulis langkah NFC dan BLE dalam satu TC ("ulangi untuk BLE") dan Data Uji `N1` (BLE: B1) tanpa kode unit; spec menulis dua blok langkah.
