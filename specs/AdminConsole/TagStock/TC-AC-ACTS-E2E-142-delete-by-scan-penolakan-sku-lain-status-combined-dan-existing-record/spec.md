---
id: TC-AC-ACTS-E2E-142-delete-by-scan-penolakan-sku-lain-status-combined-dan-existing-record
title: "Delete by Scan: Penolakan Unit SKU Lain (T-26), Waiting, In Use, Tidak di Stok, Combined (T-27), dan Existing Record Pending (T-28)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-824
  - TC-AC-ACTS-825
  - TC-AC-ACTS-826
  - TC-AC-ACTS-827
coverage:
  web: automated
---

# Delete by Scan: Penolakan Unit SKU Lain (T-26), Waiting, In Use, Tidak di Stok, Combined (T-27), dan Existing Record Pending (T-28)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Satu kode TAG yang belum pernah diregistrasi (Z1) dipakai pada TC-AC-ACTS-825 (nilai literal tetap, S-12).

## Test Steps

### TC-AC-ACTS-824: Scan unit milik SKU lain ditolak dengan toast T-26

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Delete by Scan]` dan scan X1 (unit Available SKU `NFC-CARD-BETA-N2`)
3. Verifikasi toast error `Error, this TAG belongs to another SKU and can't be deleted here.`
4. Verifikasi tidak ada dialog dan sesi tetap aktif (Floating Widget `Deleting TAGs...` tampil)
5. Klik `[Stop]`
6. Tunggu aksi selesai (sesi Delete by Scan tertutup)
7. Buka Detail SKU `NFC-CARD-BETA-N2` > Tab Available
8. Verifikasi X1 masih ada di Tab Available SKU NFC
9. Tunggu toast lama hilang

### TC-AC-ACTS-825: Scan unit Waiting for Approval, In Use, atau yang tidak ada di stok ditolak dengan toast Error per status

10. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
11. Klik `[Delete by Scan]`
12. Scan W1
13. Verifikasi toast error W1 `Error, this TAG is waiting for approval and can't be deleted.`
14. Scan I1
15. Verifikasi toast error I1 `Error, this TAG is currently in use and can't be deleted.`
16. Scan Z1
17. Verifikasi toast error Z1 `Error, TAG not found in stock.`
18. Verifikasi tidak ada dialog
19. Klik `[Stop]`
20. Tunggu aksi selesai (sesi Delete by Scan tertutup)
21. Buka Approvals > TAG Stock > Tab Active
22. Verifikasi Subject unit W1 tetap ada di Tab Active (W1 tetap Waiting for Approval)
23. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab In Use
24. Verifikasi I1 tetap di Tab In Use
25. Tunggu toast lama hilang

### TC-AC-ACTS-826: Scan unit komponen Combined set aktif ditolak dengan toast T-27

26. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
27. Klik `[Delete by Scan]` dan scan C1
28. Verifikasi toast error `Error, this TAG is part of a Combined TAG and can't be deleted. Separate it first.`
29. Verifikasi tidak ada dialog `Cannot Delete Unit` dan sesi tetap aktif
30. Klik `[Stop]`
31. Verifikasi C1 masih ada di Tab Available
32. Tunggu toast lama hilang

### TC-AC-ACTS-827: Scan unit Existing Record Subject Register Duplicate pending ditolak dengan toast T-28

33. Klik `[Delete by Scan]` dan scan P1
34. Verifikasi toast error `Error, this TAG is referenced by a pending approval and can't be deleted.`
35. Verifikasi tidak ada dialog `Cannot Delete Unit` dan sesi tetap aktif
36. Klik `[Stop]`
37. Verifikasi P1 masih ada di Tab Available

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), `[Stop]`, navigasi ke Approvals dan antar SKU dan tab, serta "Tunggu toast lama hilang" (pemulihan state, S-09).
- Langkah penghubung (S-03, 8b butir 8): "Tunggu aksi selesai (sesi Delete by Scan tertutup)" sesudah `[Stop]` menunggu sesi Delete by Scan tertutup sebelum log atau surface lain dibuka; tidak ada `Verifikasi` karena hanya pemulihan state (S-09).
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Identifier dan hitungan tetap (Data Uji Dinamis) dipakai ulang lintas TC dan tidak dapat bersuffix per run; kebenaran hitungan hanya terjamin bila fixture BE mereset dataset sebelum spec.
  - TC-AC-ACTS-825 Expected butir b mengamati Approvals > Tab Active dan Tab In Use pada Langkah Uji nomor 3; Tab In Use berada di Detail SKU, sehingga spec membukanya dari Detail SKU `RFID-ASSET-CORE-R5`.
  - Judul TC-AC-ACTS-825 menyebut toast T-31, T-32, dan T-33 tanpa menyebut pemetaan status ke kode; spec mengasersi teks toast persis per status.
