---
id: TC-AC-ACTS-E2E-218-modal-event-log-penulisan-sesi-add-stock-delete-satuan-bulk-delete-parsial-dan-tanpa-keputusan-duplicate-approval
title: "Modal Event Log: Penulisan Sesi Add Stock (Success dan Waiting), Delete Satuan, Bulk Delete Parsial, dan Tanpa Keputusan Duplicate Approval"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-473
  - TC-AC-ACTS-474
  - TC-AC-ACTS-475
  - TC-AC-ACTS-477
coverage:
  web: automated
---

# Modal Event Log: Penulisan Sesi Add Stock (Success dan Waiting), Delete Satuan, Bulk Delete Parsial, dan Tanpa Keputusan Duplicate Approval

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12); `unitC1` = unit Combined C1 milik fixture BE (Data Uji Dinamis #5); `unitU1` = `TAG-4F7K2XQ9` (unit Available U1, Data Uji Dinamis #5); `unitU2` = unit Available U2 milik fixture BE (Data Uji Dinamis #5); `unitU3` = unit Available U3 milik fixture BE (Data Uji Dinamis #5).
- Data seed (kemampuan fixture BE, dipakai sebagai precondition, tidak diasersi): untuk TC-AC-ACTS-473, dua sesi Add Stock terbaru: hasil registrasi scan RFID 45 TAG valid dan 2 TAG match (Waiting for Approval) memakai reader `Zebra RFD40 (SN-2201)`, serta hasil import GPS 100 IMEI tanpa reader. Untuk TC-AC-ACTS-474 sampai 475, unit milik spec: U1 (`Fixture.tagStock.unitU1`), U2 (`Fixture.tagStock.unitU2`), U3 (`Fixture.tagStock.unitU3`), dan unit Combined C1 (`Fixture.tagStock.unitC1`), semua pada SKU `Fixture.tagStock.skuRfid`. Untuk TC-AC-ACTS-477, dua Subject Register Duplicate untuk SKU itu, satu di-Approve dan satu di-Reject.
- Identifier tetap unit Data Uji Dinamis #5 tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE (S-12).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pembacaan lewat fixture BE atas jumlah total entri sesi Event Log SKU per tab sebagai baseline (selain teks footer pagination); TC tidak menyebut cara membaca baseline (lihat Temuan untuk QA).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`

### TC-AC-ACTS-473: Event Log Tab Add Stock: sesi Add Stock memuat angka Success dan Waiting for Approval

3. Klik icon `[Event Log]` di toolbar Tab Available
4. Verifikasi baris sesi scan: Activity `Add Stock`, Success `45`, Waiting for Approval `2`, Failed `—`, Hardware `Zebra RFD40 (SN-2201)`
5. Verifikasi baris sesi import: Activity `Add Stock`, Success `100`, Waiting for Approval `0`, Failed `—`, Hardware `—`
6. Verifikasi rincian per TAG tidak tampil di baris sesi (hanya lewat `[Detail]`)

### TC-AC-ACTS-474: Event Log Tab Add Stock: Delete satuan menulis sesi Activity Delete Stock

7. Catat jumlah total entri sesi Tab Add Stock SKU `Fixture.tagStock.skuRfid` sebagai baseline (kemampuan baca fixture BE)
8. Tutup modal Event Log dengan klik (X)
9. Ketik Search `Fixture.tagStock.unitU1`, tekan Enter
10. Klik row action `Delete` pada baris unit `Fixture.tagStock.unitU1`
11. Klik `[Delete]` pada dialog konfirmasi
12. Tunggu aksi selesai (tombol aksi aktif kembali)
13. Klik `(←)` pada kotak Search
14. Klik icon `[Event Log]` di toolbar Tab Available
15. Verifikasi baris sesi terbaru: Activity `Delete Stock`, Success `1`, Waiting for Approval `—`, Failed `0`, Hardware `—`, Modified By pelaku (format `[First Name] [Last Initial]`)
16. Verifikasi jumlah total entri bertambah tepat satu dari baseline sehingga hanya satu baris ditambahkan untuk operasi ini

### TC-AC-ACTS-475: Event Log Tab Add Stock: Bulk Delete parsial menulis satu sesi dengan Success dan Failed

17. Catat jumlah total entri sesi Tab Add Stock SKU `Fixture.tagStock.skuRfid` sebagai baseline (kemampuan baca fixture BE)
18. Tutup modal Event Log dengan klik (X)
19. Telusuri halaman Pagination Tab Available dari halaman pertama sampai halaman terakhir dan centang baris unit `Fixture.tagStock.unitU2`, `Fixture.tagStock.unitU3`, dan `Fixture.tagStock.unitC1` pada halaman tempat tiap unit tampil (seleksi bertahan saat pindah halaman, TC-AC-ACTS-842)
20. Pilih Bulk Action `Delete`, klik `[Delete]`
21. Klik `[Close]` pada dialog hasil `D-10`
22. Klik icon `[Event Log]` di toolbar Tab Available
23. Verifikasi satu baris sesi terbaru: Activity `Delete Stock`, Success `2`, Waiting for Approval `—`, Failed `1`
24. Verifikasi tidak ada baris per unit (jumlah total entri bertambah tepat satu dari baseline)

### TC-AC-ACTS-477: Event Log tidak memuat keputusan Duplicate Identifier Approval

25. Verifikasi sedikitnya satu baris sesi Add Stock atau Delete Stock tampil pada Tab Add Stock
26. Ketik Search `duplicate`, tekan Enter
27. Verifikasi empty state `No results found` tampil sehingga tidak ada baris Activity `Duplicate Approved`, `Duplicate Rejected`, maupun `Duplicate Canceled` di Tab Add Stock
28. Klik `(←)` pada kotak Search
29. Klik tab `Audit TAG`
30. Verifikasi sedikitnya satu baris sesi Audit tampil pada Tab Audit TAG
31. Ketik Search `duplicate`, tekan Enter
32. Verifikasi empty state `No results found` tampil sehingga Tab Audit TAG tidak memuat baris keputusan Duplicate Identifier Approval
33. Klik `(←)` pada kotak Search
34. Tutup modal Event Log dengan klik (X)
35. Buka Approvals > TAG Stock lewat sidebar
36. Klik Tab `History`
37. Verifikasi Subject Register Duplicate yang di-Approve tampil di Approvals > TAG Stock > Tab History
38. Verifikasi Subject Register Duplicate yang di-Reject tampil di Approvals > TAG Stock > Tab History

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16) dan langkah 2 (row action `Detail`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; menutup kotak Search lewat `(←)`; mencatat baseline.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Alasan di atas sekitar 35 langkah: spec ini 38 langkah dihitung dengan ekspansi; tiap blok menulis satu sesi berbeda pada SKU dan modal Event Log yang sama dengan unit milik spec, dan berdiri sendiri; jumlah langkah berasal dari pencatatan baseline, aksi Delete, dan `Verifikasi` per klausa Expected (S-01).
- TC-AC-ACTS-477 dibaca lewat Search `duplicate` pada kolom Activity (Tab Add Stock) dan kolom aksi (Tab Audit TAG) sebagai cara mengamati tidak adanya baris keputusan; baris sesi Add Stock, Delete Stock, dan Audit yang tampil menjadi anchor positif.
- Cara menemukan unit (langkah 19): tiap unit milik spec berada pada tepat satu baris Tab Available SKU `Fixture.tagStock.skuRfid`; barisnya ditemukan dengan menelusuri halaman Pagination dari halaman pertama sampai terakhir, bukan Search, sehingga seleksi ketiga unit bertahan lintas halaman (TC-AC-ACTS-842) dan tidak bergantung pada halaman tempat unit berada.
- TC-AC-ACTS-476 (sesi Delete by Scan) ada di spec 261.
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-473 menyebut registrasi scan dan import GPS sebagai precondition tanpa langkah; spec memakai sesi seed fixture BE.
  - TC-AC-ACTS-474 dan 475 menyebut Modified By "pelaku" tanpa nama; spec mengasersi format `[First Name] [Last Initial]` milik akun aktor.
  - TC-AC-ACTS-477 Expected c ("Event Log adalah record sesi tersendiri, bukan tampilan Activity Log") bersifat konseptual dan tidak punya langkah observasi sendiri; dicakup oleh Expected a dan b.
  - TC-AC-ACTS-474 dan 475 tidak menyebut cara membaca jumlah baris sebelum aksi (baseline); spec memakai kemampuan baca fixture BE dan teks footer pagination.
  - Data Uji Dinamis #5 hanya mendefinisikan U1 sampai U3 dan C1, sedangkan TC-AC-ACTS-474 dan 475 membutuhkan unit terpisah per TC; spec memakai unit milik fixture.
