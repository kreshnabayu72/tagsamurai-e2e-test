---
id: TC-AC-ACTS-E2E-215-modal-event-log-kolom-actions-detail-dan-popup-detail-sesi-add-stock-delete-bulk-dan-scan
title: "Modal Event Log: Kolom Actions Detail per Baris serta Popup Detail Sesi Add Stock, Delete Stock Bulk Parsial, dan Delete by Scan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-905
  - TC-AC-ACTS-933
  - TC-AC-ACTS-934
  - TC-AC-ACTS-935
coverage:
  web: automated
---

# Modal Event Log: Kolom Actions Detail per Baris serta Popup Detail Sesi Add Stock, Delete Stock Bulk Parsial, dan Delete by Scan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed (kemampuan fixture BE): sesi Add Stock dengan Success `3` dan Waiting for Approval `1` (3 unit OK, 1 unit Waiting); sesi Delete Stock hasil Bulk Delete parsial dengan Success `2` dan Failed `2` (U1 dan U2 terhapus; C1 dan P1 dilewati); sesi Delete Stock hasil Delete by Scan dengan Success `3` dan Failed `0`. Sesi dikenali dari kombinasi nilai kolom itu, dan kombinasinya unik pada SKU. Dipakai sebagai precondition TC; aksi Delete tidak dijalankan di spec ini.
- Sesi seed Tab Add Stock dan Tab Audit TAG tersedia (sedikitnya satu baris per tab untuk TC-AC-ACTS-905).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-905: Kolom Actions memuat `[Detail]` per baris dan tidak dapat disortir (kedua tab)

4. Klik (⋯) pada satu baris Tab Add Stock
5. Verifikasi menu baris hanya berisi `Detail` (icon `FileInfoLine`)
6. Verifikasi tidak ada row action lain (tanpa Delete, Edit, atau Review)
7. Tutup menu baris dengan Esc
8. Klik header kolom Actions
9. Verifikasi header kolom Actions tidak memiliki ikon sort
10. Verifikasi klik header kolom Actions membuka Overlay Column Visibility
11. Tutup Overlay Column Visibility dengan Esc
12. Klik tab `Audit TAG`
13. Klik (⋯) pada satu baris Tab Audit TAG
14. Verifikasi menu baris hanya berisi `Detail` (icon `FileInfoLine`)
15. Verifikasi tidak ada row action lain (tanpa Delete, Edit, atau Review)
16. Tutup menu baris dengan Esc
17. Klik header kolom Actions
18. Verifikasi header kolom Actions tidak memiliki ikon sort
19. Verifikasi klik header kolom Actions membuka Overlay Column Visibility
20. Tutup Overlay Column Visibility dengan Esc

### TC-AC-ACTS-933: Popup Detail sesi Add Stock: section `Added` dan `Waiting for Approval`

21. Klik tab `Add Stock`
22. Klik (⋯) pada baris sesi Add Stock dengan Success `3` dan Waiting for Approval `1`
23. Klik `Detail`
24. Verifikasi Popup Detail terbuka read-only dengan section `Added` lalu section `Waiting for Approval`
25. Verifikasi section `Added` memuat kolom `TAG Code` dan `Identifier` (RFID: `EPC / UID`)
26. Verifikasi TAG Code pada section `Added` terisi dan terurut TAG Code A–Z
27. Verifikasi section `Waiting for Approval` memuat TAG Code `—` (belum terbit) dan Identifier unit itu
28. Tutup Popup Detail dengan klik (X)

### TC-AC-ACTS-934: Popup Detail sesi Delete Stock (Bulk parsial): section `Deleted` dan `Failed`

29. Klik (⋯) pada baris sesi Delete Stock hasil Bulk Delete parsial (Success `2`, Failed `2`)
30. Klik `Detail`
31. Verifikasi section `Deleted` memuat kolom `TAG Code`, `Identifier`, `Status Sebelum Dihapus` (`Available` atau `Damaged/Missing`) untuk U1 dan U2
32. Verifikasi section `Failed` memuat kolom `TAG Code`, `Identifier`, `Status Sebelum Dihapus` untuk C1 dan P1
33. Verifikasi section `Failed` tidak memiliki kolom `Reason`
34. Verifikasi urutan section adalah `Deleted` lalu `Failed`
35. Tutup Popup Detail dengan klik (X)

### TC-AC-ACTS-935: Popup Detail sesi Delete by Scan: hanya section `Deleted`

36. Klik (⋯) pada baris sesi Delete Stock hasil Delete by Scan (Success `3`, Failed `0`)
37. Klik `Detail`
38. Verifikasi Popup Detail hanya memuat section `Deleted` dengan 3 unit
39. Verifikasi section `Failed` beserta judulnya tidak tampil (penolakan scan hanya berupa toast)
40. Tutup Popup Detail dengan klik (X)

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Alasan di atas sekitar 35 langkah: spec ini 40 langkah dihitung dengan ekspansi; semua blok membaca Popup Detail dari sesi seed pada modal Event Log yang sama dan berdiri sendiri; jumlah langkah berasal dari `Verifikasi` per klausa Expected (S-01) dan langkah membuka atau menutup popup antar TC (S-09).
- Penulisan sesi Delete Stock dan Add Stock (aksinya) diuji di spec 218 dan 261; spec ini hanya membaca isi Popup Detail dari sesi seed.
- Temuan untuk QA (S-15):
  - TC-AC-ACTS-905 berjudul "kedua tab" tetapi langkah 6 (klik header kolom Actions) hanya satu kali; spec memeriksa header Actions pada kedua tab mengikuti judul.
  - TC-AC-ACTS-933 sampai 935 tidak menyebut penanda baris sesi yang dimaksud; spec mengenalinya dari kombinasi nilai kolom seed.
