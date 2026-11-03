---
id: TC-AC-ACTS-E2E-148-resilience-delete-dan-audit-gagal-5xx-dan-timeout
title: "Resilience Delete dan Audit: Audit Submit Gagal (T-09), Delete Gagal 5xx (T-16), Delete by Scan Gagal dan Timeout (T-16, T-24), dan Bulk Delete Tanpa Respons (T-24)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-339
  - TC-AC-ACTS-370
  - TC-AC-ACTS-832
  - TC-AC-ACTS-849
coverage:
  web: automated
---

# Resilience Delete dan Audit: Audit Submit Gagal (T-09), Delete Gagal 5xx (T-16), Delete by Scan Gagal dan Timeout (T-16, T-24), dan Bulk Delete Tanpa Respons (T-24)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk respons `5xx` pada request Submit Audit, Delete, dan hapus Delete by Scan serta penahanan respons sampai klien mencapai timeout (TC-AC-ACTS-832 dan 849); intercept dilepas segera setelah pemicu selesai (S-09). Kegagalan dan timeout adalah objek uji kelas b.
- Data per blok TC: TC-AC-ACTS-339 memakai 2 Available dan 2 Damaged/Missing (Data Audit di atas); TC-AC-ACTS-370, 832, dan 849 memakai unit uji hapus U1 sampai U4 (Data Dinamis #5), di-reset fixture BE.

## Test Steps

### TC-AC-ACTS-339: Audit Submit gagal menampilkan T-09 dan state dipertahankan

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Klik `[Start Scan]`
4. Scan 2 unit
5. Klik `[Stop]`
6. Intercept request Submit Audit dengan respons `5xx`
7. Klik `[Submit]`
8. Pada dialog `Confirm Audit` biarkan checkbox dicentang, klik `[Confirm]` (respons `5xx` terjadi pada langkah ini)
9. Verifikasi toast error `Error, failed to update TAG status.`
10. Verifikasi tidak ada perubahan status (rollback): status unit di backend tetap (dibaca lewat fixture BE)
11. Verifikasi baris Verified dan tombol tetap
12. Lepas intercept
13. Klik `✕` pada popup
14. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
15. Klik `[Leave]`
16. Tunggu toast lama hilang

### TC-AC-ACTS-370: Delete gagal 5xx menampilkan T-16 dan unit tetap ada

17. Reset dataset: U1 sampai U4 lewat fixture BE
18. Intercept request Delete dengan respons `5xx`
19. Klik (⋯) pada unit U1, lalu klik `Delete`, klik `[Delete]`
20. Verifikasi toast error `Error, failed to delete unit.`
21. Verifikasi rollback penuh: unit U1 tetap ada di Tab Available dan di backend
22. Lepas intercept
23. Tunggu toast lama hilang

### TC-AC-ACTS-832: Delete by Scan gagal di server menampilkan toast T-16; timeout menampilkan toast T-24

24. Klik `[Delete by Scan]`
25. Intercept request hapus dengan respons `5xx`, lalu scan U1
26. Verifikasi toast `Error, failed to delete unit.`
27. Verifikasi U1 tidak terhapus
28. Lepas intercept, lalu tahan respons request hapus sampai klien mencapai timeout dan scan U2
29. Verifikasi toast `Connection problem. Please try again.`
30. Verifikasi sesi tetap aktif (Floating Widget `Deleting TAGs...` tampil) setelah kedua toast
31. Lepas tahanan respons
32. Klik `[Stop]`
33. Tunggu toast lama hilang

### TC-AC-ACTS-849: Bulk Delete tanpa respons (timeout jaringan) menampilkan toast T-24

34. Reset dataset: U1 sampai U4 lewat fixture BE
35. Centang U1 dan U2, pilih Bulk Action > `Delete`
36. Tahan respons request hapus sampai klien mencapai timeout
37. Klik `[Delete]`
38. Verifikasi toast `Connection problem. Please try again.`
39. Verifikasi toast bukan `Error, failed to delete units.`
40. Lepas tahanan respons
41. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (c) dan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah "Reset dataset" dan pembukaan Detail SKU diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset", "Lepas intercept" dan "Lepas tahanan respons", `[Stop]`, penutup popup, pembatalan seleksi, dan "Tunggu toast lama hilang" (pemulihan state, S-09).
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-832 dan 849 menyatakan "tahan respons sampai timeout" tanpa menyebut durasi timeout klien; spec memakai penahanan respons yang melepas setelah klien mencapai timeout (kemampuan intercept disediakan tim FE, tanpa menunggu waktu nyata di atas jeda pendek).
  - TC-AC-ACTS-832 mengasersi toast T-16 untuk scan pertama dan T-24 untuk scan kedua dalam satu sesi; urutan pelepasan intercept ditambahkan sebagai langkah penghubung.
  - Kode pesan T-09, T-16, dan T-24 pada judul disertai teks toast di Expected sehingga spec mengasersi teks persis.
