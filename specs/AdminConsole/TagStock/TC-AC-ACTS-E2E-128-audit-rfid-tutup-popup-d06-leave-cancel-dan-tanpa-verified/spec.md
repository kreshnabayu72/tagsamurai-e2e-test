---
id: TC-AC-ACTS-E2E-128-audit-rfid-tutup-popup-d06-leave-cancel-dan-tanpa-verified
title: "Audit RFID: Tutup Popup Setelah Stop dengan Baris Verified (D-06 Leave dan Cancel) dan Tutup Popup Tanpa Verified Langsung Tertutup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-332
  - TC-AC-ACTS-333
  - TC-AC-ACTS-334
coverage:
  web: automated
---

# Audit RFID: Tutup Popup Setelah Stop dengan Baris Verified (D-06 Leave dan Cancel) dan Tutup Popup Tanpa Verified Langsung Tertutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.

## Test Steps

### TC-AC-ACTS-332: Menutup popup setelah Stop dengan baris Verified memunculkan D-06: `[Leave]`

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Klik `[Start Scan]`
4. Scan 1 unit
5. Klik `[Stop]`
6. Klik `✕` pada popup
7. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
8. Klik `[Leave]`
9. Verifikasi popup tertutup dan kembali ke Tab Available
10. Klik `[Audit TAG]` di toolbar Tab Available
11. Verifikasi baris Verified yang belum Submit hilang: seluruh baris `Not Scanned`
12. Klik `✕` pada popup untuk menutup popup Idle

### TC-AC-ACTS-333: D-06 `[Cancel]` tetap di popup dengan Verified utuh

13. Klik `[Audit TAG]` di toolbar Tab Available
14. Klik `[Start Scan]`
15. Scan 1 unit
16. Klik `[Stop]`
17. Klik `✕` pada popup
18. Klik `[Cancel]` pada dialog Unsaved Changes
19. Verifikasi dialog tertutup dan Popup Audit tetap terbuka
20. Verifikasi baris Verified utuh
21. Klik `✕` pada popup
22. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
23. Klik `[Leave]`

### TC-AC-ACTS-334: Menutup popup tanpa baris Verified langsung tertutup

24. Klik `[Audit TAG]` di toolbar Tab Available
25. Klik `✕` pada popup tanpa scan
26. Verifikasi popup tertutup tanpa dialog
27. Verifikasi Tab Available tetap tampil

## Notes

- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), `[Stop]` yang membuka kunci popup, dan penutup popup di akhir blok (pemulihan state, S-09).
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-332 butir b ("baris Verified yang belum Submit hilang") tidak memberi langkah observasi; spec membuka Popup Audit lagi untuk mengasersinya.
  - Pembagian TC lintas spec: TC-AC-ACTS-335, 336, 799, dan 800 (sesi scan aktif ditinggalkan) ada di spec 163.
