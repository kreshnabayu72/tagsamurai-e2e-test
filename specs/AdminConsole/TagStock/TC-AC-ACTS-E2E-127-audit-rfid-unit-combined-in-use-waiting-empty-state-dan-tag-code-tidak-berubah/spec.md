---
id: TC-AC-ACTS-E2E-127-audit-rfid-unit-combined-in-use-waiting-empty-state-dan-tag-code-tidak-berubah
title: "Audit RFID: Unit Combined Tetap Eligible, In Use dan Waiting Tidak Ditawarkan, Tanpa Unit Eligible (Empty State), Gagal Memuat Daftar, dan TAG Code Tidak Berubah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-328
  - TC-AC-ACTS-329
  - TC-AC-ACTS-330
  - TC-AC-ACTS-331
  - TC-AC-ACTS-733
coverage:
  web: automated
---

# Audit RFID: Unit Combined Tetap Eligible, In Use dan Waiting Tidak Ditawarkan, Tanpa Unit Eligible (Empty State), Gagal Memuat Daftar, dan TAG Code Tidak Berubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data Pre-setup SKU tambahan: `RFID-SEAL-DELTA-R1` (Pre-setup #16, SKU tanpa unit) dipakai sebagai SKU RFID tanpa unit eligible pada TC-AC-ACTS-330 (TC tidak menyebut SKU-nya; lihat Temuan untuk QA).
- Data per blok TC (di-reset fixture BE): TC-AC-ACTS-328 menambah satu unit RFID Combined dengan NFC (E) ke dataset; TC-AC-ACTS-329 menambah satu unit In Use dan satu unit Waiting for Approval; TC-AC-ACTS-733 memakai tepat 2 unit Available (A dan B) tanpa unit Damaged/Missing.
- Kemampuan teknis: Intercept respons `5xx` atas request daftar unit eligible Audit (`Spectra.intercept()` di atas backend nyata), dilepas segera setelah blok TC-AC-ACTS-331.
- Kemampuan teknis: Pengamat request jaringan browser (menghitung request keluar sesudah klik `[Submit]`) untuk Verifikasi "tidak ada request" pada TC-AC-ACTS-330, disediakan tim FE.

## Test Steps

### TC-AC-ACTS-328: Unit Combined tetap eligible dan combined set tidak pecah

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Verifikasi unit Combined E ditawarkan di tabel
4. Klik `[Start Scan]`
5. Scan unit lain saja (A), unit Combined E tidak ter-scan
6. Klik `[Stop]`
7. Klik `[Submit]`
8. Biarkan checkbox dicentang, klik `[Confirm]`
9. Verifikasi unit Combined E ditandai Damaged/Missing tanpa Separate
10. Verifikasi combined set tidak pecah otomatis (relasi Combined unit E dengan NFC tetap, dibaca lewat fixture BE)

### TC-AC-ACTS-329: Unit In Use dan Waiting for Approval tidak ditawarkan

11. Reset dataset: tambahkan satu unit In Use dan satu unit Waiting for Approval lewat fixture BE
12. Klik `[Audit TAG]` di toolbar Tab Available
13. Verifikasi tabel memuat sedikitnya satu baris unit eligible (Available atau Damaged/Missing)
14. Verifikasi tabel hanya memuat unit Available dan Damaged/Missing; unit In Use dan Waiting for Approval tidak ada
15. Klik `✕` pada popup untuk menutup popup Idle

### TC-AC-ACTS-330: Tanpa unit eligible: empty state, `[Start Scan]` disabled, `[Submit]` error inline

16. Klik row action `Detail` pada SKU `RFID-SEAL-DELTA-R1` di Stock List, lalu buka Tab Available
17. Klik `[Audit TAG]` di toolbar Tab Available
18. Verifikasi empty state: Illustration, Title `No TAGs to audit`, dan Description `This SKU has no registered TAGs to verify.`
19. Verifikasi `[Start Scan]` disabled dan `[Submit]` aktif
20. Klik `[Submit]`
21. Verifikasi error inline `No TAGs to audit.` tampil di atas tombol
22. Verifikasi tidak ada dialog dan tidak ada request
23. Klik `✕` pada popup untuk menutup popup

### TC-AC-ACTS-331: Gagal memuat daftar unit menampilkan error

24. Kembali ke Stock List, lalu klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` dan buka Tab Available
25. Intercept request daftar unit eligible Audit dengan respons `5xx`
26. Klik `[Audit TAG]` di toolbar Tab Available
27. Verifikasi area tabel menampilkan `Unable to load this data.` dengan `[Try Again]`
28. Verifikasi `[Start Scan]` disabled dan `[Submit]` tetap aktif
29. Klik `[Submit]`
30. Verifikasi error inline `No TAGs to audit.` tampil di atas tombol
31. Lepas intercept
32. Klik `✕` pada popup untuk menutup popup

### TC-AC-ACTS-733: TAG Code unit tidak berubah setelah Mark Damaged/Missing dan recovery

33. Reset dataset: tepat 2 unit Available (A dan B) lewat fixture BE
34. Catat TAG Code unit A di Tab Available
35. Klik `[Audit TAG]` di toolbar Tab Available
36. Klik `[Start Scan]`
37. Scan unit B saja
38. Klik `[Stop]`
39. Klik `[Submit]`
40. Biarkan checkbox tercentang (default), klik `[Confirm]`
41. Verifikasi unit A berstatus Damaged/Missing dengan TAG Code sama seperti yang dicatat pada langkah 34
42. Klik `[Audit TAG]` lagi
43. Klik `[Start Scan]`
44. Scan unit A dan unit B
45. Klik `[Stop]`
46. Klik `[Submit]`
47. Verifikasi unit A pulih menjadi Available dengan TAG Code tetap sama seperti yang dicatat pada langkah 34

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset" lewat fixture BE, `[Stop]` yang membuka kunci popup, penutup popup, dan "Lepas intercept" (pemulihan state, S-09).
- P-5 butir b: TC-AC-ACTS-331 (satu kegagalan 5xx pada daftar Audit, objek uji ringan tanpa harness eksternal) berada di spec fungsional Audit dengan harness dominan yang sama; hanya satu TC kelas b di spec ini.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-330 menyebut "SKU RFID tanpa unit eligible" tanpa menyebut SKU; spec memakai `RFID-SEAL-DELTA-R1` (Pre-setup #16, SKU tanpa unit) dan reader tidak dibutuhkan.
  - TC-AC-ACTS-328 Data Uji "Unit Combined tidak ter-scan" tanpa menyebut kode unit; spec memakai unit E hasil seeding.
  - TC-AC-ACTS-330 butir c menyatakan "tidak ada request" tanpa cara mengamatinya; spec memakai pengamat request jaringan browser yang disediakan tim FE.
