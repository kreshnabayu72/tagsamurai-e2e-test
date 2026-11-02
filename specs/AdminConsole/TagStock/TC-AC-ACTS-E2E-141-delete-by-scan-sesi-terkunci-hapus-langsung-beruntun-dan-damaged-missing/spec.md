---
id: TC-AC-ACTS-E2E-141-delete-by-scan-sesi-terkunci-hapus-langsung-beruntun-dan-damaged-missing
title: "Delete by Scan: Sesi Terkunci dengan Widget Deleting TAGs, Scan Eligible Langsung Terhapus, Scan Beruntun, dan Unit Damaged/Missing"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-820
  - TC-AC-ACTS-821
  - TC-AC-ACTS-822
  - TC-AC-ACTS-823
coverage:
  web: automated
---

# Delete by Scan: Sesi Terkunci dengan Widget Deleting TAGs, Scan Eligible Langsung Terhapus, Scan Beruntun, dan Unit Damaged/Missing

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Pembacaan Stock List (Total Registered), Device Allocation > Stock Balance Summary Panel, dan Activity Log dipakai untuk TC-AC-ACTS-821; asersi memakai baseline sebelum aksi (S-12).

## Test Steps

### TC-AC-ACTS-820: Sesi Delete by Scan, halaman terkunci dengan Floating Status Widget `Deleting TAGs...` dan counter

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Delete by Scan]`
3. Scan U1
4. Verifikasi halaman blur dan non-interactive
5. Verifikasi widget pojok kanan-bawah berstatus `Deleting TAGs...` dengan `[Stop]` sebagai satu-satunya kontrol
6. Verifikasi counter widget `1 TAG deleted`
7. Scan U2
8. Verifikasi counter widget `2 TAGs deleted`
9. Klik `[Stop]`
10. Verifikasi blur dan widget hilang dan halaman interaktif
11. Verifikasi U1 dan U2 tidak ada di tabel

### TC-AC-ACTS-821: Scan unit eligible langsung menghapus unit tanpa dialog, mengurangi Total Registered dan Stock Ledger

12. Reset dataset: U1 sampai U4 lewat fixture BE
13. Buka Stock List dan catat Total Registered SKU `RFID-ASSET-CORE-R5` (N)
14. Buka Device Allocation > Stock Balance Summary Panel dan catat saldo entitas registrant (S)
15. Buka Activity Log (filter Object `TAG Stock`) dan catat baseline jumlah entri `Delete by Scan` untuk `RFID-ASSET-CORE-R5 (RFID)` dan jumlah entri `Delete Stock` untuk `TAG-4F7K2XQ9`
16. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
17. Klik `[Delete by Scan]` dan scan U1 (`TAG-4F7K2XQ9`)
18. Verifikasi toast `Success, TAG-4F7K2XQ9 has been deleted.`
19. Verifikasi tidak ada dialog konfirmasi
20. Klik `[Stop]`
21. Verifikasi U1 tidak ada di Tab Available
22. Buka Stock List dan baca Total Registered SKU `RFID-ASSET-CORE-R5`
23. Verifikasi Total Registered sama dengan N dikurangi 1
24. Buka Device Allocation > Stock Balance Summary Panel dan baca saldo entitas registrant
25. Verifikasi saldo Stock Ledger entitas registrant sama dengan S dikurangi 1
26. Buka Activity Log (filter Object `TAG Stock`)
27. Verifikasi jumlah entri Activity Log `Delete by Scan` bertambah 1 dari baseline langkah 15, dengan entri baru ber-Name `RFID-ASSET-CORE-R5 (RFID)`, Field `Quantity`, Old Value `1 TAG`, New Value `—`
28. Verifikasi jumlah entri Activity Log `Delete Stock` untuk `TAG-4F7K2XQ9` sama dengan baseline langkah 15 (tanpa entri per unit)
29. Tunggu toast lama hilang

### TC-AC-ACTS-822: Scan beruntun tiga unit eligible, satu toast per unit, tanpa jeda dan tanpa dialog

30. Reset dataset: U1 sampai U4 lewat fixture BE
31. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
32. Klik `[Delete by Scan]`
33. Scan U1, U2, dan U3 berturut-turut tanpa menunggu
34. Verifikasi tiga toast `Success, [TAG Code] has been deleted.` dengan TAG Code tiap unit yang di-scan
35. Verifikasi tidak ada dialog dan scan berikutnya tidak tertahan; sesi tetap aktif sampai `[Stop]`
36. Verifikasi counter widget `3 TAGs deleted`
37. Klik `[Stop]`
38. Verifikasi U1, U2, dan U3 tidak ada di tabel

### TC-AC-ACTS-823: Scan unit Damaged/Missing eligible menghapusnya langsung

39. Reset dataset: U1 sampai U4 lewat fixture BE
40. Klik `[Delete by Scan]` dan scan U4
41. Verifikasi toast `Success, [TAG Code] has been deleted.` dengan TAG Code U4
42. Klik `[Stop]`
43. Verifikasi U4 tidak ada di tabel

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset", pencatatan baseline dan navigasi ke Stock List, Device Allocation, dan Activity Log, serta "Tunggu toast lama hilang" (pemulihan state, S-09).
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Identifier dan hitungan tetap (Data Uji Dinamis) dipakai ulang lintas TC dan tidak dapat bersuffix per run; kebenaran hitungan hanya terjamin bila fixture BE mereset dataset sebelum spec.
  - TC-AC-ACTS-821 Precondition "Total Registered SKU = 10" dan saldo dicatat; Expected `9`; spec mengasersi relatif terhadap baseline (S-12).
