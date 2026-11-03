---
id: TC-AC-ACTS-E2E-153-pencatatan-log-add-stock-via-scan-import-gps-waiting-dan-batch-waiting
title: "Pencatatan Log: Add Stock via Scan, Import GPS, dan Waiting for Approval di System Log, Activity Log, dan Event Log; Entri Level SKU; Batch Seluruhnya Waiting"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-521
  - TC-AC-ACTS-655
  - TC-AC-ACTS-656
  - TC-AC-ACTS-657
  - TC-AC-ACTS-669
coverage:
  web: automated
---

# Pencatatan Log: Add Stock via Scan, Import GPS, dan Waiting for Approval di System Log, Activity Log, dan Event Log; Entri Level SKU; Batch Seluruhnya Waiting

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor kedua (Ganti akun): Manage TAG stock Read+Create (Pre-setup #5) `manageTagStockCreate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TS_CREATE_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Data tambahan: SKU GPS `GPS-TRACK-CORE-G3` (Pre-setup #15) dengan 3 IMEI baru untuk Import GPS (TC-AC-ACTS-656); TAG baru untuk Add Stock scan 2 TAG (TC-AC-ACTS-655); identifier yang cocok existing (milik unit terdaftar) untuk Waiting for Approval (TC-AC-ACTS-657) dan batch seluruh barisnya cocok existing (TC-AC-ACTS-669). Entri log dibaca dengan baseline jumlah entri sebelum aksi (S-12).
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.

## Test Steps

### TC-AC-ACTS-655: Log Add Stock via Scan di System Log, Activity Log, dan Event Log

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Catat baseline jumlah entri Activity Log dan System Log (User Detail) serta jumlah baris Event Log SKU (Tab Add Stock)
3. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5`, scan 2 TAG baru, klik `[Stop]`, lalu klik `[Submit]`
4. Tunggu aksi selesai
5. Buka User Detail > System Log dan Activity Log
6. Verifikasi entri Activity Log baru: Action `Add Stock`, Object `TAG Stock`, Name `RFID-ASSET-CORE-R5 (RFID)`, Field `Quantity`, Old Value `—`, New Value `2 TAGs`
7. Verifikasi Modified By entri Activity Log berformat `[First Name] [Last Initial]`
8. Verifikasi entri System Log baru dengan kolom yang sama tanpa Modified By
9. Buka modal Event Log SKU (Tab Add Stock)
10. Verifikasi satu baris baru Activity `Add Stock` dengan Success `2`
11. Tutup modal Event Log

### TC-AC-ACTS-521: Entri Activity Log aksi level-SKU memakai Name SKU tanpa TAG Code

12. Buka Activity Log (filter Object `TAG Stock`)
13. Cari baris Action `Add Stock` (batch yang sudah di-submit pada TC-AC-ACTS-655)
14. Verifikasi Name `RFID-ASSET-CORE-R5 (RFID)`, Field `Quantity`, Old Value `—`, New Value `2 TAGs`
15. Verifikasi tidak ada kolom TAG Code pada entri itu

### TC-AC-ACTS-656: Log Add Stock via Import GPS di System Log, Activity Log, dan Event Log

16. Buka User Detail > System Log dan Activity Log dan catat baseline jumlah entri `Add Stock`; buka modal Event Log SKU GPS (Tab Add Stock), catat baseline jumlah baris, lalu tutup modal Event Log
17. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` dan Import 3 IMEI baru, lalu klik `[Submit]`
18. Tunggu aksi selesai
19. Buka User Detail > System Log dan Activity Log
20. Verifikasi jumlah entri System Log dan Activity Log `Add Stock` bertambah 1 dari baseline langkah 16, dengan entri baru: Action `Add Stock`, New Value `3 TAGs`
21. Buka modal Event Log SKU GPS (Tab Add Stock)
22. Verifikasi jumlah baris Event Log bertambah 1 dari baseline langkah 16, dengan baris baru Activity `Add Stock`, Success `3`, dan Hardware `—`
23. Tutup modal Event Log

### TC-AC-ACTS-657 dan TC-AC-ACTS-669: pemicu sebagai Manage TAG stock Read+Create

24. Ganti akun: Logout, lalu login sebagai Manage TAG stock Read+Create (`Spectra.env.AC_TS_CREATE_PASSWORD`)
25. Catat baseline jumlah entri Activity Log `Add Stock` dan `Waiting for Approval` serta jumlah baris Event Log SKU (Tab Add Stock)
26. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5`, scan TAG yang cocok existing (TC-AC-ACTS-657), klik `[Stop]`, lalu klik `[Submit]`
27. Tunggu aksi selesai
28. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5`, submit batch yang semua barisnya cocok existing (TC-AC-ACTS-669), lalu klik `[Submit]`
29. Tunggu aksi selesai
30. Ganti akun: Logout, lalu login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)

### TC-AC-ACTS-657: Log Waiting for Approval di System Log dan Activity Log

31. Buka User Detail > System Log dan Activity Log
32. Verifikasi entri Activity Log dan System Log baru: Action `Waiting for Approval`, Field `Status`, Old Value `—`, New Value `Waiting for Approval`
33. Verifikasi Name entri System Log adalah identifier

### TC-AC-ACTS-669: Batch Add Stock yang seluruhnya Waiting tidak menulis entri Activity Log Add Stock tetapi menulis baris Event Log

34. Buka Activity Log (filter Object `TAG Stock`)
35. Verifikasi Activity Log memuat entri `Waiting for Approval` per unit batch
36. Verifikasi jumlah entri `Add Stock` sama dengan baseline (tidak ada entri `Add Stock` baru dari batch itu)
37. Buka modal Event Log SKU (Tab Add Stock)
38. Verifikasi satu baris baru Activity `Add Stock` dengan Success `0` dan Waiting for Approval sejumlah unit batch

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu topik (pembacaan log setelah aksi) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Blok baca-log berpola (buka surface, cari entri, Verifikasi kolom) berulang.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), pencatatan baseline, "Tunggu aksi selesai" sesudah Submit dan sebelum Ganti akun, dan pemicu TC-AC-ACTS-657 dan 669 dikumpulkan sebelum satu kali Ganti akun ke Total Control (pembacaan log keduanya sesudahnya). Urutan TC: 655, 521, 656, 657 dan 669 (pemicu), 657, 669. Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- P-1: asersi "tanpa entri `Add Stock`" TC-AC-ACTS-669 diasersi sebagai jumlah entri sama dengan baseline di spec ini (anchor: entri `Waiting for Approval` per unit) karena bergantung pada batch seluruhnya Waiting yang baru dibangun langkah sebelumnya; tidak ada spec absence untuk TC itu.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-656 menulis Precondition SKU `RFID-ASSET-CORE-R5` untuk Import GPS yang berlaku pada SKU GPS; spec memakai SKU GPS `GPS-TRACK-CORE-G3` dan Hardware `—` pada Event Log mengikuti TC.
  - TC-AC-ACTS-657 dan 669 tidak menyebut TAG yang cocok existing; spec memakai identifier unit terdaftar milik seeding. Pre-setup #5 tertulis `Manage TAG stock Read+Create` dan dipakai sebagai pemicu.
  - TC-AC-ACTS-655 butir a menulis Modified By `[first] [inisial]`; spec mengasersi format `[First Name] [Last Initial]` (R-14).
