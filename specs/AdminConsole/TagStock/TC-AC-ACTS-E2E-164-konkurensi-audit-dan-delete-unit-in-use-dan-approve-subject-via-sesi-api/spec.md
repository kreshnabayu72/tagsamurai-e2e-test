---
id: TC-AC-ACTS-E2E-164-konkurensi-audit-dan-delete-unit-in-use-dan-approve-subject-via-sesi-api
title: "Konkurensi Audit dan Delete: Unit Menjadi In Use di Tengah Audit dan Delete Bersamaan dengan Approve Subject"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-712
  - TC-AC-ACTS-713
coverage:
  web: automated
---

# Konkurensi Audit dan Delete: Unit Menjadi In Use di Tengah Audit dan Delete Bersamaan dengan Approve Subject

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Sesi API aktor (login API password, token tidak dihitung sebagai sesi web) untuk pelaku kedua yang hanya memicu perubahan state, disediakan tim BE/FE (lihat `suite.md`).
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Pelaku kedua: sesi lain yang mengaktivasi unit (status In Use) dan Admin 2 yang meng-approve Subject memakai sesi API aktor dengan kemampuan aktivasi unit dan approve Subject yang disediakan tim FE/BE (aktor tidak disebut di TC; S-13).
- Data per blok TC (di-reset fixture BE): TC-AC-ACTS-712 memakai unit eligible hanya unit A (Available) dan unit B (Damaged/Missing); TC-AC-ACTS-713 memakai unit Existing Record sebuah Subject Register Duplicate pending (P1).

## Test Steps

### TC-AC-ACTS-712: Unit menjadi In Use di tengah sesi Audit, di-skip saat Submit

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Catat baseline jumlah entri Activity Log `TAG Stock` untuk unit A (Search TAG Code)
3. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
4. Klik `[Audit TAG]`, klik `[Start Scan]`, scan unit A dan unit B, klik `[Stop]`
5. Sesi API mengaktivasi unit A hingga status In Use tersimpan
6. Klik `[Submit]` (semua baris Verified, tanpa dialog)
7. Verifikasi unit A di-skip: status tetap In Use
8. Verifikasi unit B pulih menjadi Available
9. Verifikasi satu toast gabungan `Success, TAG has been verified. 1 TAG recovered to Available. 1 TAG was skipped because its status had changed.`
10. Buka Activity Log (filter Object `TAG Stock`)
11. Verifikasi jumlah entri Activity Log untuk unit A sama dengan baseline langkah 2

### TC-AC-ACTS-713: Delete unit bersamaan dengan Approve Subject yang merujuk unit itu

12. Reset dataset: unit P1 sebagai Existing Record Subject pending lewat fixture BE
13. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
14. Klik (⋯) pada unit P1, lalu klik `Delete`
15. Verifikasi dialog blok `D-08` tampil: `This unit is referenced by a pending approval and cannot be deleted.`
16. Klik `[OK]`
17. Sesi API (Admin 2) meng-approve Subject hingga status resolved tersimpan
18. Muat ulang halaman
19. Klik (⋯) pada unit P1, lalu klik `Delete`, klik `[Delete]`
20. Verifikasi Delete berhasil: unit P1 tidak ada di Tab Available

## Notes

- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), pencatatan baseline, navigasi ke Activity Log dan kembali ke Detail SKU, "Reset dataset", `[OK]` dialog, dan "Muat ulang halaman" (pemulihan state, S-09).
- Pembagian TC lintas spec: TC-AC-ACTS-710, 711, dan 714 (dua sesi UI) ada di spec 146.
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Aktor dan mekanisme "sesi lain mengaktivasi unit" dan "Admin 2 Approve" tidak didefinisikan di TC, PRD, atau LLD; spec memakai sesi API aktor dengan kemampuan yang disediakan tim FE/BE.
  - TC-AC-ACTS-712 butir a ("tanpa log" untuk unit A) tidak punya langkah observasi di TC; spec mengasersi jumlah entri Activity Log unit A sama dengan baseline.
  - Langkah Uji TC-AC-ACTS-713 nomor 1 menyebut Admin 1 Delete "ditolak dialog blok D-08" lalu Admin 2 Approve; Expected butir akhir ("setelah Subject resolved Delete berhasil") diasersi dengan unit hilang dari Tab Available.
