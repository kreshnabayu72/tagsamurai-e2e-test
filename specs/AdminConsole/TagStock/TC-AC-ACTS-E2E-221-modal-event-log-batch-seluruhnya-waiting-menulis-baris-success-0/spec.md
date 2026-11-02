---
id: TC-AC-ACTS-E2E-221-modal-event-log-batch-seluruhnya-waiting-menulis-baris-success-0
title: "Modal Event Log: Batch Add Stock Seluruhnya Waiting Menulis Baris dengan Success 0"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-945
coverage:
  web: automated
---

# Modal Event Log: Batch Add Stock Seluruhnya Waiting Menulis Baris dengan Success 0

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `epcMatchA` = EPC pertama yang cocok dengan unit terdaftar; `epcMatchB` = EPC kedua yang cocok dengan unit terdaftar; `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed: SKU `Fixture.tagStock.skuRfid` dengan dua EPC yang cocok unit terdaftar (`Fixture.tagStock.epcMatchA`, `Fixture.tagStock.epcMatchB`). Seeding idempotent dan pemulihan lewat fixture BE (S-12).
- Spec berjalan serial karena memakai simulator pemindai bersama.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Simulator pemindai RFID `Zebra RFD40 (SN-2201)` (scan satu per satu dan beruntun, kode tidak dikenali) disediakan tim FE; mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Pembacaan lewat fixture BE atas jumlah total entri sesi Event Log SKU per tab sebagai baseline (selain teks footer pagination); TC tidak menyebut cara membaca baseline (lihat Temuan untuk QA).
- Kemampuan teknis: Pembacaan Activity Log lewat UI (Search atau Filter entri); jalur menu Activity Log tidak disebut TC (lihat Temuan untuk QA).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Activity Log (filter Object `TAG Stock`) dan catat baseline jumlah entri Activity `Add Stock` untuk SKU `Fixture.tagStock.skuRfid`
2. Buka TAG > Stock lewat sidebar
3. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
4. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`

### TC-AC-ACTS-945: Batch Add Stock yang seluruhnya Waiting for Approval menulis baris Event Log dengan Success 0

5. Catat jumlah total entri sesi Tab Add Stock SKU `Fixture.tagStock.skuRfid` sebagai baseline (kemampuan baca fixture BE)
6. Lakukan Add Stock RFID dengan 2 TAG yang match unit terdaftar (`Fixture.tagStock.epcMatchA` dan `Fixture.tagStock.epcMatchB`) lewat sesi scan reader RFID `Zebra RFD40 (SN-2201)`, klik `[Submit]`
7. Tunggu aksi selesai (tombol aksi aktif kembali)
8. Klik icon `[Event Log]` di toolbar Tab Available
9. Verifikasi jumlah total entri sesi Tab Add Stock bertambah tepat satu dari baseline
10. Verifikasi baris sesi terbaru: Activity `Add Stock`, Success `0`, Waiting for Approval `2`, Failed `—`
11. Klik (⋯) pada baris sesi terbaru, klik `Detail`
12. Verifikasi Popup Detail hanya memuat section `Waiting for Approval` dengan 2 identifier (TAG Code `—`)
13. Tutup Popup Detail dan modal Event Log
14. Buka Activity Log (filter Object `TAG Stock`)
15. Verifikasi tabel Activity Log memuat sedikitnya satu baris data
16. Verifikasi jumlah entri Activity `Add Stock` untuk SKU `Fixture.tagStock.skuRfid` sama dengan baseline langkah 1 (tidak ada entri `Add Stock` Quantity 0 untuk batch ini)

## Notes

- Langkah penghubung (S-03): langkah 3 (Search SKU di Stock List untuk menemukan baris target, R-16) dan langkah 4 (row action `Detail`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; mencatat baseline; menunggu aksi Submit selesai.
- P-1: asersi absence TC-AC-ACTS-945 butir c tetap di spec ini karena bergantung pada sesi Add Stock seluruhnya Waiting yang baru dibangun lewat simulator pemindai pada langkah 6 (state berat).
- Penulisan sesi Add Stock dengan Success lebih dari 0 diuji di spec 219.
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-945 Expected c (tidak ada entri log aktivitas `Add Stock` untuk Quantity 0) tidak punya langkah membaca Activity Log dan tidak menyebut jalur menunya; spec membuka Activity Log dengan filter Object `TAG Stock` (idiom suite) untuk mencatat baseline (langkah 1) dan membandingkan jumlah entri (langkah 16), dengan anchor positif tabel Activity Log berisi baris (langkah 15) dan baris Event Log yang tampil lebih dulu (langkah 10).
  - TC-AC-ACTS-945 tidak menyebut cara membaca jumlah baris Event Log sebelum aksi (baseline); spec memakai kemampuan baca fixture BE dan mencatatnya sebelum Submit.
  - TC-AC-ACTS-945 tidak merinci langkah UI Add Stock selain `[Submit]`; spec mengikuti rumusan TC.
  - Cara simulasi reader RFID tidak didefinisikan di TC, PRD, atau LLD; ditulis "disediakan tim FE".
