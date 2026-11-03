---
id: TC-AC-ACTS-E2E-130-audit-rfid-scan-kode-belum-terdaftar-bukan-eligible-dan-format-tidak-valid
title: "Audit RFID: Scan Kode Belum Terdaftar (Toast T-38), Kode Terdaftar Bukan Unit Eligible Diabaikan, dan Teks Berformat Tidak Valid Diabaikan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-948
  - TC-AC-ACTS-949
  - TC-AC-ACTS-950
coverage:
  web: automated
---

# Audit RFID: Scan Kode Belum Terdaftar (Toast T-38), Kode Terdaftar Bukan Unit Eligible Diabaikan, dan Teks Berformat Tidak Valid Diabaikan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data kode scan: kode `E280999999999999` tidak terdaftar di TAG Stock (TC-AC-ACTS-948); unit terdaftar non-eligible milik spec: Available SKU lain (U-lain), In Use (U-pakai), dan Waiting for Approval (W1) (TC-AC-ACTS-949); teks `ZZZ-123` bukan EPC atau UID valid (TC-AC-ACTS-950). Kode literal bersifat tetap (S-12); seeding idempoten dan pemulihan lewat fixture BE.
- Kemampuan teknis: Pengamat request jaringan browser (menghitung request selama sesi scan) disediakan tim FE.

## Test Steps

### TC-AC-ACTS-948: Scan kode yang belum terdaftar di TAG Stock menampilkan toast T-38

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Klik `[Start Scan]`
4. Scan kode `E280999999999999`
5. Verifikasi toast error `Error, this TAG hasn't been registered yet.`
6. Verifikasi tidak ada baris yang berubah atau bertambah (seluruh baris tetap `Not Scanned`) dan sesi scan tetap aktif (Floating Widget `Scanning…` tampil)
7. Scan satu unit eligible
8. Verifikasi unit eligible yang di-scan berubah menjadi `✓ Verified`
9. Verifikasi counter widget `1 TAG verified`
10. Klik `[Stop]`
11. Klik `✕` pada popup
12. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
13. Klik `[Leave]`

### TC-AC-ACTS-949: Scan kode terdaftar tetapi bukan unit eligible diabaikan tanpa toast

14. Klik `[Audit TAG]` di toolbar Tab Available
15. Klik `[Start Scan]`
16. Verifikasi Floating Widget `Scanning…` tampil
17. Scan U-lain, U-pakai, dan W1
18. Verifikasi tidak ada toast untuk ketiga scan
19. Verifikasi tabel Audit tidak berubah: semua baris tetap `Not Scanned`
20. Verifikasi counter widget `0 TAGs verified`
21. Klik `[Stop]`
22. Klik `✕` pada popup untuk menutup popup Idle

### TC-AC-ACTS-950: Scan teks berformat tidak valid diabaikan tanpa toast dan tanpa perubahan baris

23. Klik `[Audit TAG]` di toolbar Tab Available
24. Klik `[Start Scan]`
25. Verifikasi Floating Widget `Scanning…` tampil
26. Scan teks `ZZZ-123`
27. Verifikasi tidak ada toast
28. Verifikasi tabel Audit tidak berubah
29. Verifikasi counter widget `0 TAGs verified`
30. Klik `[Stop]`
31. Klik `✕` pada popup untuk menutup popup Idle

## Notes

- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), `[Stop]`, dan penutup popup (pemulihan state, S-09).
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-948 menulis teks toast T-38 literal di Expected; spec mengasersi teks itu persis.
  - Ketiga TC mengasersi "tidak ada toast" tanpa menyebut jangka waktu pengamatan; spec mengasersi segera setelah scan sebelum `[Stop]`, dengan widget aktif sebagai anchor.
  - Pre-setup TC tidak mendaftar unit SKU lain, unit In Use, dan unit Waiting for Approval untuk TC-AC-ACTS-949; spec memakai unit hasil seeding.
