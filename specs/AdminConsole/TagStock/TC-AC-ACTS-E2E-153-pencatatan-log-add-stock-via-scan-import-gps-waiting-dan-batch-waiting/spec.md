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
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
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
2. Catat baseline jumlah entri `Add Stock` Activity Log (filter Object `TAG Stock`) dan System Log (User Detail) serta jumlah baris Event Log SKU (Tab Add Stock)
3. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5`, scan 2 TAG baru, klik `[Stop]`, lalu klik `[Submit]`
4. Tunggu aksi selesai
5. Buka User Detail > System Log dan Activity Log
6. Verifikasi jumlah entri `Add Stock` Activity Log dan System Log naik tepat 1 dari baseline langkah 2
7. Verifikasi entri Activity Log `Add Stock` teratas (urutan default `Date` terbaru): Action `Add Stock`, Object `TAG Stock`, Name `RFID-ASSET-CORE-R5 (RFID)`, Field `Quantity`, Old Value `—`, New Value `2 TAGs`
8. Verifikasi Modified By entri Activity Log berformat `[First Name] [Last Initial]`
9. Verifikasi entri System Log `Add Stock` teratas (urutan default `Date` terbaru) dengan kolom yang sama tanpa Modified By
10. Buka modal Event Log SKU (Tab Add Stock)
11. Verifikasi jumlah baris Event Log naik tepat 1 dari baseline langkah 2
12. Verifikasi baris Event Log teratas (urutan default terbaru): Activity `Add Stock` dengan Success `2`
13. Tutup modal Event Log

### TC-AC-ACTS-521: Entri Activity Log aksi level-SKU memakai Name SKU tanpa TAG Code

14. Buka Activity Log (filter Object `TAG Stock`)
15. Baca entri `Add Stock` teratas (urutan default `Date` terbaru; batch yang sudah di-submit pada TC-AC-ACTS-655, selisih satu entri sudah diverifikasi pada langkah 6)
16. Verifikasi Name `RFID-ASSET-CORE-R5 (RFID)`, Field `Quantity`, Old Value `—`, New Value `2 TAGs`
17. Verifikasi tidak ada kolom TAG Code pada entri itu

### TC-AC-ACTS-656: Log Add Stock via Import GPS di System Log, Activity Log, dan Event Log

18. Buka User Detail > System Log dan Activity Log dan catat baseline jumlah entri `Add Stock`; buka modal Event Log SKU GPS (Tab Add Stock), catat baseline jumlah baris, lalu tutup modal Event Log
19. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` dan Import 3 IMEI baru, lalu klik `[Submit]`
20. Tunggu aksi selesai
21. Buka User Detail > System Log dan Activity Log
22. Verifikasi jumlah entri System Log dan Activity Log `Add Stock` bertambah 1 dari baseline langkah 18, dengan entri teratas (urutan default `Date` terbaru) baru: Action `Add Stock`, New Value `3 TAGs`
23. Buka modal Event Log SKU GPS (Tab Add Stock)
24. Verifikasi jumlah baris Event Log bertambah 1 dari baseline langkah 18, dengan baris teratas baru: Activity `Add Stock`, Success `3`, dan Hardware `—`
25. Tutup modal Event Log

### TC-AC-ACTS-657 dan TC-AC-ACTS-669: pemicu sebagai Manage TAG stock Read+Create

26. Ganti akun: Logout, lalu login sebagai Manage TAG stock Read+Create (`Spectra.env.AC_TS_CREATE_PASSWORD`)
27. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri `Waiting for Approval` dan `Add Stock` pada keduanya
28. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5`, scan TAG yang cocok existing (TC-AC-ACTS-657), klik `[Stop]`, lalu klik `[Submit]`
29. Tunggu aksi selesai
30. Buka modal Event Log SKU (Tab Add Stock), catat baseline jumlah baris, lalu tutup modal Event Log
31. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5`, submit batch yang semua barisnya cocok existing (TC-AC-ACTS-669), lalu klik `[Submit]`
32. Tunggu aksi selesai
33. Ganti akun: Logout, lalu login sebagai Total Control (`Spectra.env.AC_TC_PASSWORD`)

### TC-AC-ACTS-657: Log Waiting for Approval di System Log dan Activity Log

34. Buka User Detail > System Log dan Activity Log
35. Verifikasi jumlah entri `Waiting for Approval` Activity Log dan System Log naik tepat 1 + K dari baseline langkah 27 (1 untuk TC-AC-ACTS-657, K = jumlah unit batch TC-AC-ACTS-669 pada langkah 31)
36. Verifikasi himpunan 1 + K entri teratas (urutan default `Date` terbaru; tanpa mengandalkan urutan di antaranya) memuat entri Activity Log dan System Log: Action `Waiting for Approval`, Field `Status`, Old Value `—`, New Value `Waiting for Approval`
37. Verifikasi Name entri System Log adalah identifier

### TC-AC-ACTS-669: Batch Add Stock yang seluruhnya Waiting tidak menulis entri Activity Log Add Stock tetapi menulis baris Event Log

38. Buka Activity Log (filter Object `TAG Stock`)
39. Verifikasi himpunan 1 + K entri teratas yang selisihnya diverifikasi pada langkah 35 memuat entri `Waiting for Approval` per unit batch
40. Verifikasi jumlah entri `Add Stock` sama dengan baseline langkah 27 (tidak ada entri `Add Stock` baru dari batch itu)
41. Buka modal Event Log SKU (Tab Add Stock)
42. Verifikasi jumlah baris Event Log naik tepat 1 dari baseline langkah 30
43. Verifikasi baris Event Log teratas (urutan default terbaru): Activity `Add Stock` dengan Success `0` dan Waiting for Approval sejumlah unit batch

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu topik (pembacaan log setelah aksi) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Blok baca-log berpola (buka surface, cari entri, Verifikasi kolom) berulang.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), pencatatan baseline, "Tunggu aksi selesai" sesudah Submit dan sebelum Ganti akun, dan pemicu TC-AC-ACTS-657 dan 669 dikumpulkan sebelum satu kali Ganti akun ke Total Control (pembacaan log keduanya sesudahnya). Urutan TC: 655, 521, 656, 657 dan 669 (pemicu), 657, 669. Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- P-1: asersi "tanpa entri `Add Stock`" TC-AC-ACTS-669 diasersi sebagai jumlah entri sama dengan baseline di spec ini (anchor: entri `Waiting for Approval` per unit) karena bergantung pada batch seluruhnya Waiting yang baru dibangun langkah sebelumnya; tidak ada spec absence untuk TC itu.
- Cara baca entri audit trail baru (S-12, S-14): jumlah entri dicatat sebelum aksi pemicu, selisihnya diverifikasi, lalu baris teratas urutan default `Date` terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya. Pada TC-AC-ACTS-657 dan 669 yang dibaca adalah himpunan 1 + K entri teratas (satu entri TC-AC-ACTS-657 ditambah K unit batch TC-AC-ACTS-669; K dari seeding batch) karena kedua pemicu berjalan sebelum satu kali Ganti akun; baseline baris Event Log TC-AC-ACTS-669 dicatat tepat sebelum Submit batch itu.
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-656 menulis Precondition SKU `RFID-ASSET-CORE-R5` untuk Import GPS yang berlaku pada SKU GPS; spec memakai SKU GPS `GPS-TRACK-CORE-G3` dan Hardware `—` pada Event Log mengikuti TC.
  - TC-AC-ACTS-657 dan 669 tidak menyebut TAG yang cocok existing; spec memakai identifier unit terdaftar milik seeding. Pre-setup #5 tertulis `Manage TAG stock Read+Create` dan dipakai sebagai pemicu.
  - TC-AC-ACTS-655 butir a menulis Modified By `[first] [inisial]`; spec mengasersi format `[First Name] [Last Initial]` (R-14).
