---
id: TC-AC-ACTS-E2E-219-modal-event-log-angka-success-per-tag-hardware-dan-unit-bypass
title: "Modal Event Log: Angka Success Add Stock RFID Satu dan Dua TAG, Hardware Kosong untuk Import GPS, serta Unit Bypass E2a Tidak Dihitung"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-766
  - TC-AC-ACTS-775
  - TC-AC-ACTS-944
coverage:
  web: automated
---

# Modal Event Log: Angka Success Add Stock RFID Satu dan Dua TAG, Hardware Kosong untuk Import GPS, serta Unit Bypass E2a Tidak Dihitung

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `epcBypass` = EPC unit yang sudah terdaftar pada entitas Principal (memicu bypass E2a); `epcNew1` = `E280116060000208A1B2C3` (EPC baru, Data Uji Dinamis #1); `epcNew2` = EPC RFID baru kedua (identifier belum terdaftar, dipastikan fixture BE); `epcNew3` = EPC RFID baru ketiga (identifier belum terdaftar, dipastikan fixture BE); `epcNew4` = EPC RFID baru keempat (identifier belum terdaftar, dipastikan fixture BE; khusus TC-AC-ACTS-944); `epcNew5` = EPC RFID baru kelima (identifier belum terdaftar, dipastikan fixture BE; khusus TC-AC-ACTS-944); `imeiManual` = `356938035643817` (IMEI valid baru, Data Uji Dinamis #2); `skuGps` = `GPS-TRACK-CORE-G3` (SKU GPS, Pre-setup #15); `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed: SKU `Fixture.tagStock.skuGps` untuk TC-AC-ACTS-775 (IMEI `Fixture.tagStock.imeiManual` belum terdaftar) dan SKU `Fixture.tagStock.skuRfid` untuk TC-AC-ACTS-766 dan 944. Identifier RFID baru (`Fixture.tagStock.epcNew1` sampai `Fixture.tagStock.epcNew5`) belum terdaftar sebelum spec ini; tiap identifier dipakai pada satu sesi saja; `Fixture.tagStock.epcBypass` terdaftar pada entitas Principal (memicu bypass E2a). Seeding idempotent dan pemulihan lewat fixture BE (S-12).
- Spec berjalan serial karena memakai simulator pemindai bersama dan identifier tetap.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Simulator pemindai RFID `Zebra RFD40 (SN-2201)` (scan satu per satu dan beruntun, kode tidak dikenali) disediakan tim FE; mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Pembacaan lewat fixture BE atas jumlah total entri sesi Event Log SKU per tab sebagai baseline (selain teks footer pagination); TC tidak menyebut cara membaca baseline (lihat Temuan untuk QA).
- Kemampuan teknis: Pembacaan Activity Log lewat UI (Search atau Filter entri); jalur menu Activity Log tidak disebut TC (lihat Temuan untuk QA).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps


### TC-AC-ACTS-775: Event Log Tab Add Stock: sesi Add Stock Import GPS satu IMEI tanpa reader menampilkan Hardware `—`

1. Ketik Search `Fixture.tagStock.skuGps`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuGps`
3. Catat jumlah total entri sesi Tab Add Stock SKU `Fixture.tagStock.skuGps` sebagai baseline (kemampuan baca fixture BE)
4. Lakukan Add Stock GPS dengan satu IMEI valid baru `Fixture.tagStock.imeiManual` lewat Manual Entry, klik `[Submit]`
5. Tunggu aksi selesai (tombol aksi aktif kembali)
6. Klik icon `[Event Log]` di toolbar Tab Available
7. Verifikasi jumlah total entri sesi Tab Add Stock bertambah tepat satu dari baseline
8. Verifikasi baris sesi terbaru: Activity `Add Stock`, Success `1`, Waiting for Approval `0`, Failed `—`
9. Verifikasi Hardware baris sesi terbaru adalah `—` (Import atau Manual GPS tanpa Handheld Reader)
10. Tutup modal Event Log dengan klik (X)
11. Buka TAG > Stock lewat sidebar
12. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
13. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`

### TC-AC-ACTS-766: Event Log Tab Add Stock: sesi Add Stock RFID satu TAG dan dua TAG menghasilkan angka Success masing-masing

14. Catat jumlah total entri sesi Tab Add Stock SKU `Fixture.tagStock.skuRfid` sebagai baseline (kemampuan baca fixture BE)
15. Lakukan Add Stock RFID dengan satu TAG baru (`Fixture.tagStock.epcNew1`) lewat sesi scan reader RFID `Zebra RFD40 (SN-2201)`, klik `[Submit]`
16. Lakukan Add Stock RFID dengan dua TAG baru (`Fixture.tagStock.epcNew2` dan `Fixture.tagStock.epcNew3`) lewat sesi scan reader RFID `Zebra RFD40 (SN-2201)`, klik `[Submit]`
17. Tunggu aksi selesai (tombol aksi aktif kembali)
18. Klik icon `[Event Log]` di toolbar Tab Available
19. Verifikasi jumlah total entri sesi Tab Add Stock bertambah tepat dua dari baseline
20. Verifikasi baris sesi pertama: Success `1`, Waiting for Approval `0`, Failed `—`
21. Verifikasi baris sesi kedua: Success `2`, Waiting for Approval `0`, Failed `—`
22. Verifikasi kedua baris memiliki Activity `Add Stock` dan sel berisi angka (tanpa teks bentuk tunggal atau jamak)

### TC-AC-ACTS-944: Unit bypass E2a tidak dihitung di kolom Success maupun Popup Detail Event Log

23. Tutup modal Event Log dengan klik (X)
24. Catat jumlah total entri sesi Tab Add Stock SKU `Fixture.tagStock.skuRfid` sebagai baseline (kemampuan baca fixture BE)
25. Lakukan Add Stock RFID dengan 3 TAG (2 baru dan 1 match unit terdaftar yang memicu bypass E2a) (`Fixture.tagStock.epcNew4`, `Fixture.tagStock.epcNew5`, `Fixture.tagStock.epcBypass`) lewat sesi scan reader RFID `Zebra RFD40 (SN-2201)`, klik `[Submit]`
26. Tunggu aksi selesai (tombol aksi aktif kembali)
27. Klik icon `[Event Log]` di toolbar Tab Available
28. Verifikasi jumlah total entri sesi Tab Add Stock bertambah tepat satu dari baseline
29. Verifikasi baris sesi terbaru memiliki Success `2` dan Waiting for Approval `0`
30. Klik (⋯) pada baris sesi terbaru, klik `Detail`
31. Verifikasi section `Added` pada Popup Detail hanya memuat 2 unit
32. Verifikasi unit bypass tidak tampil di Popup Detail
33. Tutup Popup Detail dan modal Event Log
34. Buka Activity Log dan cari entri `Duplicate Approved` dengan identifier `Fixture.tagStock.epcBypass` (Search atau Filter, tidak bergantung posisi teratas)
35. Verifikasi entri `Duplicate Approved` untuk unit bypass tampil di Activity Log sebagai satu-satunya jejak unit bypass

## Notes

- Langkah penghubung (S-03): Search SKU di Stock List yang mendahului row action `Detail` mencari baris target (R-16); tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay (termasuk menutup modal Event Log sebelum pindah halaman atau memulai Add Stock berikutnya); mencatat baseline; menunggu aksi Submit selesai.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Blok TC-AC-ACTS-775 (Manual Entry GPS, tanpa simulator) diletakkan lebih dulu; blok yang memakai simulator pemindai (TC-AC-ACTS-766 dan 944) menyusul.
- TC-AC-ACTS-944 Expected c: unit bypass tercatat sebagai entri `Duplicate Approved` di Activity Log; asersinya hanya keberadaan entri tersebut, sedangkan ketiadaan unit bypass di Event Log diasersi pada Expected a dan b.
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-766, 775, dan 944 tidak menyebut cara membaca jumlah baris sebelum aksi (baseline); spec memakai kemampuan baca fixture BE dan mencatatnya per blok sebelum aksi.
  - TC-AC-ACTS-766 dan 944 tidak merinci langkah UI Add Stock (tombol, dialog) selain `[Submit]`; spec mengikuti rumusan TC.
  - TC-AC-ACTS-944 Expected c tidak punya langkah membaca Activity Log dan tidak menyebut jalur menunya; spec memakai pencarian entri sebagai langkah penghubung.
  - TC-AC-ACTS-766 Expected c ("tidak ada teks bentuk tunggal/jamak") dirumuskan sebagai sel berisi angka; spec mengasersi sel berisi angka.
  - Cara simulasi reader RFID tidak didefinisikan di TC, PRD, atau LLD; ditulis "disediakan tim FE".
