---
id: TC-AC-ACTS-E2E-137-delete-unit-konfirmasi-damaged-missing-klik-ganda-distributor-dan-unit-terakhir-sku
title: "Delete Unit: Konfirmasi Delete Mengurangi Total Registered dan Ledger, Delete Damaged/Missing, Klik Ganda, Distributor Hanya Unit Miliknya, dan Hapus Unit Terakhir SKU"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-361
  - TC-AC-ACTS-362
  - TC-AC-ACTS-371
  - TC-AC-ACTS-372
  - TC-AC-ACTS-373
coverage:
  web: automated
---

# Delete Unit: Konfirmasi Delete Mengurangi Total Registered dan Ledger, Delete Damaged/Missing, Klik Ganda, Distributor Hanya Unit Miliknya, dan Hapus Unit Terakhir SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor kedua (Ganti akun): Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Data tambahan: SKU `RFID-SEAL-DELTA-R1` (Pre-setup #16, SKU tanpa unit) diberi satu unit Available oleh fixture BE untuk TC-AC-ACTS-373; unit Distributor D1 (Local Registration) dan unit Principal pada SKU `RFID-ASSET-CORE-R5` untuk TC-AC-ACTS-372. Total Registered SKU dan saldo Stock Ledger dibaca sebagai baseline sebelum aksi (bukan nilai absolut, S-12).
- Kemampuan teknis: Klien HTTP untuk request langsung ke server (TC-AC-ACTS-372; endpoint tidak disebut di TC, PRD, atau LLD sehingga tidak ditulis di spec), disediakan tim FE/BE.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-361: Konfirmasi Delete menghapus unit, mengurangi Total Registered dan Stock Ledger

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Buka Stock List dan catat Total Registered SKU `RFID-ASSET-CORE-R5` (N); buka Device Allocation > Stock Balance Summary Panel dan catat saldo entitas registrant (S)
3. Buka Activity Log (filter Object `TAG Stock`) dan catat baseline jumlah entri `Delete Stock` untuk unit U1 (`TAG-4F7K2XQ9`) (Search TAG Code)
4. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
5. Klik (⋯) pada unit Available U1 (`TAG-4F7K2XQ9`), lalu klik `Delete`
6. Klik `[Delete]`
7. Verifikasi toast sukses `Success, unit has been deleted.`
8. Verifikasi baris U1 hilang dari Tab Available
9. Buka Stock List dan baca Total Registered SKU `RFID-ASSET-CORE-R5`
10. Verifikasi Total Registered sama dengan N dikurangi 1
11. Buka Device Allocation > Stock Balance Summary Panel dan baca saldo entitas registrant
12. Verifikasi saldo Stock Ledger entitas registrant sama dengan S dikurangi 1
13. Buka Activity Log (filter Object `TAG Stock`)
14. Verifikasi jumlah entri Activity Log `Delete Stock` untuk unit U1 bertambah 1 dari baseline langkah 3, dengan entri baru ber-Field `TAG Code`, Old Value `TAG-4F7K2XQ9`, New Value `—`
15. Tunggu toast lama hilang

### TC-AC-ACTS-362: Delete unit Damaged/Missing diperbolehkan

16. Kembali ke Stock List dan catat Total Registered SKU `RFID-ASSET-CORE-R5` (N2)
17. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, lalu buka Tab Available
18. Klik (⋯) pada unit Damaged/Missing U4, lalu klik `Delete`
19. Klik `[Delete]`
20. Verifikasi toast sukses `Success, unit has been deleted.`
21. Buka Stock List dan baca Total Registered SKU `RFID-ASSET-CORE-R5`
22. Verifikasi Total Registered sama dengan N2 dikurangi 1
23. Tunggu toast lama hilang

### TC-AC-ACTS-371: Klik ganda `[Delete]` diproses sekali

24. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, lalu buka Tab Available
25. Catat baseline jumlah entri Activity Log `Delete Stock` untuk unit U2 (Search TAG Code)
26. Klik (⋯) pada unit Available U2, lalu klik `Delete`
27. Klik `[Delete]` dua kali cepat
28. Verifikasi satu unit terhapus (U2 tidak ada di Tab Available)
29. Buka Activity Log (filter Object `TAG Stock`)
30. Verifikasi satu entri Activity Log `Delete Stock` untuk unit U2 bertambah dari baseline langkah 25
31. Tunggu toast lama hilang

### TC-AC-ACTS-373: Menghapus unit terakhir SKU, baris SKU tetap tampil dengan metrik 0

32. Buka Stock List, lalu klik row action `Detail` pada SKU `RFID-SEAL-DELTA-R1` dan buka Tab Available
33. Klik (⋯) pada satu-satunya unit Available, lalu klik `Delete`, klik `[Delete]`
34. Tunggu aksi selesai
35. Buka Stock List
36. Verifikasi baris SKU `RFID-SEAL-DELTA-R1` tetap tampil dengan Total Registered `0`

### TC-AC-ACTS-372: Distributor hanya dapat menghapus unit Local Registration miliknya

37. Ganti akun: Logout, lalu login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)
38. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, lalu buka Tab Available
39. Verifikasi Tab Available memuat unit Distributor sendiri D1 dan unit Principal tidak terlihat
40. Klik (⋯) pada unit milik sendiri D1, lalu klik `Delete`, klik `[Delete]`
41. Verifikasi Delete unit sendiri berhasil: D1 tidak ada di Tab Available
42. Kirim Delete langsung ke server untuk unit milik Principal lewat klien HTTP
43. Verifikasi Delete unit bukan miliknya ditolak server (status respons penolakan)
44. Verifikasi unit milik Principal tetap ada (dibaca lewat fixture BE)

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), pencatatan baseline Total Registered dan saldo, navigasi ke Stock List, Device Allocation, dan Activity Log, serta "Tunggu toast lama hilang" dan "Tunggu aksi selesai". Aksi Delete memakai unit milik spec; TC-AC-ACTS-373 memakai SKU Pre-setup tanpa unit yang diberi satu unit seeding sehingga Last Updated SKU itu berubah, dipulihkan fixture BE (S-06). Urutan TC: 361, 362, 371, 373, 372; TC-AC-ACTS-372 diletakkan terakhir karena membutuhkan Ganti akun ke Distributor.
- P-5 butir b: TC-AC-ACTS-372 (request langsung ke server sebagai bagian Security, objek uji ringan kelas a tanpa harness eksternal) berada di spec fungsional Delete dengan permukaan yang sama; satu-satunya TC kelas a di spec ini. Asersi request langsung hanya status respons dan state data (8b butir 1).
- Temuan untuk QA:
  - Identifier dan hitungan tetap (Data Uji Dinamis) dipakai ulang lintas TC dan tidak dapat bersuffix per run; kebenaran hitungan hanya terjamin bila fixture BE mereset dataset sebelum spec.
  - TC-AC-ACTS-361 Precondition menyebut "Total Registered SKU = 10" dan Expected `9`; spec mengasersi relatif terhadap baseline (S-12). Post Condition ("Receipt batch registrasi tidak dihapus") tanpa langkah observasi tidak diasersi.
  - TC-AC-ACTS-361 Expected butir d menulis entri Activity Log `Delete Stock` per unit untuk Delete lewat row action; pencatatan Delete by Scan dan Bulk Delete (satu entri level-sesi) ada di spec 141, 144, dan 145.
  - TC-AC-ACTS-372 tidak menyebut endpoint request langsung dan akun Distributor penghapus; spec memakai klien HTTP yang disediakan tim FE/BE.
