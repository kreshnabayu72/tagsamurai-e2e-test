---
id: TC-AC-ACTS-E2E-138-delete-by-scan-screening-toolbar-visibilitas-sku-gps-dan-tanpa-reader
title: "Delete by Scan: Toolbar Tab Available RFID, Tab In Use Tanpa Delete by Scan, SKU GPS Hanya Bulk Delete, dan Klik Tanpa Reader (V-03 atau V-04)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-815
  - TC-AC-ACTS-817
  - TC-AC-ACTS-818
  - TC-AC-ACTS-819
coverage:
  web: automated
---

# Delete by Scan: Toolbar Tab Available RFID, Tab In Use Tanpa Delete by Scan, SKU GPS Hanya Bulk Delete, dan Klik Tanpa Reader (V-03 atau V-04)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data Pre-setup: SKU RFID `RFID-ASSET-CORE-R5` (#12), SKU BLE `BLE-BEACON-ALPHA-B1` (#14), SKU GPS `GPS-TRACK-CORE-G3` (#15). Unit uji milik spec di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: SKU GPS: Available U1 dan U2; SKU RFID: unit Available dan unit In Use (Tab In Use); SKU BLE: unit Available.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Simulator pemindai BLE (kondisi reader tidak terhubung) disediakan tim FE.

## Test Steps

### TC-AC-ACTS-815: Toolbar Tab Available RFID, `[Delete by Scan]` tampil, Enabled, dengan tooltip

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Amati toolbar Tab Available dari kiri ke kanan
3. Verifikasi toolbar memuat Search, Filter, Download, `[Event Log]`, `[Delete by Scan]`, `[Audit TAG]`, `[Add Stock]` berurutan
4. Verifikasi `[Delete by Scan]` berikon scan dan Enabled (bukan Disabled)
5. Arahkan kursor ke tombol `[Delete by Scan]`
6. Verifikasi tooltip `This will remove the TAG from stock. Scanned TAGs are deleted immediately.`
7. Verifikasi label tombol bukan `Remove by Scan`

### TC-AC-ACTS-818: Tab In Use tidak memiliki `[Delete by Scan]`, kolom Checkbox, maupun Bulk Action Bar

8. Buka Tab In Use
9. Verifikasi toolbar Tab In Use hanya Search, Filter, Download
10. Verifikasi `[Delete by Scan]` tidak ada di toolbar Tab In Use
11. Verifikasi tidak ada kolom Checkbox di paling kiri tabel dan tidak ada Bulk Action Bar

### TC-AC-ACTS-817: SKU GPS, `[Delete by Scan]` Hidden, Bulk Delete tersedia, dialog tanpa baris petunjuk

12. Kembali ke Stock List, lalu klik row action `Detail` pada SKU `GPS-TRACK-CORE-G3` dan buka Tab Available
13. Verifikasi toolbar Tab Available memuat Search, Filter, Download, `[Event Log]`, dan `[Add Stock]`
14. Verifikasi `[Delete by Scan]` tidak ada di toolbar
15. Klik (⋯) pada unit U1, lalu klik `Delete`
16. Verifikasi dialog `Delete Unit` memuat `• [TAG Code]` dan `This action cannot be undone. Are you sure you want to delete it?` tanpa baris `For more accurate results, use Delete by Scan.`
17. Klik `[Cancel]`
18. Centang U1 dan U2, pilih Bulk Action > `Delete`
19. Verifikasi dialog `Delete Units` memuat bullet U1 dan U2 dan `This action cannot be undone. Are you sure you want to delete them?` tanpa baris `For more accurate results, use Delete by Scan.`
20. Klik `[Cancel]`
21. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

### TC-AC-ACTS-819: Klik `[Delete by Scan]` tanpa reader terhubung menampilkan toast V-03 (RFID) atau V-04 (BLE)

22. Putuskan semua reader (simulator)
23. Kembali ke Stock List, lalu klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` dan buka Tab Available
24. Klik `[Delete by Scan]`
25. Verifikasi toast error RFID `Reader not connected. Check Bluetooth connection.`
26. Verifikasi sesi tidak dimulai dan tidak ada unit terhapus (jumlah unit Tab Available sama dengan sebelum klik)
27. Tunggu toast lama hilang
28. Kembali ke Stock List, lalu klik row action `Detail` pada SKU `BLE-BEACON-ALPHA-B1` dan buka Tab Available
29. Klik `[Delete by Scan]`
30. Verifikasi toast error BLE `Scanner not connected. Check Bluetooth connection.`
31. Verifikasi sesi tidak dimulai dan tidak ada unit terhapus (jumlah unit Tab Available sama dengan sebelum klik)

## Notes

- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), navigasi antar SKU dan Stock List, `[Cancel]` dialog, pembatalan seleksi, "Putuskan semua reader", dan "Tunggu toast lama hilang". Urutan TC: 815, 818, 817, 819; TC-AC-ACTS-819 terakhir karena membutuhkan kondisi tanpa reader.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-817 dan 819 tidak mendaftar unit GPS dan unit BLE di Data Uji Dinamis #5 (hanya SKU RFID); spec memakai unit hasil seeding pada SKU tersebut.
  - TC-AC-ACTS-819 menulis "ulangi untuk BLE-BEACON-ALPHA-B1" dan membuka dua SKU dalam satu TC; spec menuliskannya sebagai dua blok langkah (RFID lalu BLE) dan mengasersi teks toast V-03 dan V-04 persis seperti TC.
