---
id: TC-AC-ACTS-E2E-212-detail-sku-tab-available-registered-at-hasil-approve
title: "Detail SKU Tab Available: Registered At Unit Hasil Approve Register Duplicate Tetap Waktu Scan, Berpasangan dengan Registered By"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-805
coverage:
  web: automated
---

# Detail SKU Tab Available: Registered At Unit Hasil Approve Register Duplicate Tetap Waktu Scan, Berpasangan dengan Registered By

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit Available `TAG-4F7K2XQ9` (Data Dinamis #5, U1), unit ber-Identifier EPC `E280...` dan UID `A1B2...` (Data Dinamis #1), dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab Available, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Data milik spec (disediakan fixture BE, dipulihkan di hook `after`): Subject Register Duplicate pending dari Distributor Toggle ON; staf `Sari Dewi` (Data Dinamis #3) men-Submit Add Stock pada waktu T1; unit berstatus Waiting for Approval. T1 dibaca lewat API seeding (bagian 8b butir 3); `Sari Dewi` hanya mendaftarkan unit seed spec ini.
- Jam server dan jam browser: keduanya dimajukan bersama sehingga T2 (waktu Approve) lebih dari satu menit sesudah T1, lalu dipulihkan di hook `after`. Suite berjalan serial karena spec ini mengubah jam bersama.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif
2. Ketik Search `sari`, tekan Enter
3. Verifikasi empty state `No results found` (unit hasil Register Duplicate belum tampil di Tab Available)
4. Klik `(←)` pada kotak Search
5. Majukan jam server dan jam browser sampai T2 lebih dari satu menit sesudah T1
6. Klik menu sidebar Approvals > TAG Stock, klik Tab `Active`
7. Klik `Review` pada Subject Register Duplicate seed
8. Pilih Approve, klik `[Submit]`
9. Tunggu aksi selesai
10. Klik menu sidebar TAG > Stock, klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif
11. Ketik Search `sari`, tekan Enter
12. Verifikasi unit berstatus Available dengan TAG Code baru tampil
13. Verifikasi Registered At unit itu sama dengan T1 (waktu scan atau Submit Add Stock), bukan T2
14. Verifikasi Registered By unit itu `Sari D`
15. Klik `(←)` pada kotak Search
16. Pulihkan jam server dan jam browser

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03): reset Search, memajukan dan memulihkan jam, serta Approve Subject oleh Total Control (langkah aksi TC-AC-ACTS-805 butir 2) tanpa `Verifikasi`; Search `sari` adalah langkah penghubung untuk menemukan baris target (R-16) karena Registered By `Sari D` hanya dimiliki unit seed spec ini.
- Registered At berketelitian menit; T1 dan T2 dibuat berbeda lebih dari satu menit oleh langkah memajukan jam.
- Temuan untuk QA: TC-AC-ACTS-805 tidak menyebut identifier unit; spec menemukannya lewat Registered By. Cara membaca T1 tidak disebut TC; dibaca lewat API seeding (disediakan tim FE/BE).
