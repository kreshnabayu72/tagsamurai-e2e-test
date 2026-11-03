---
id: TC-AC-ACTS-E2E-124-audit-rfid-submit-dialog-konfirmasi-dan-confirm-dengan-checkbox
title: "Audit RFID: Submit Sebelum Scan, Tanpa Not Scanned Commit Langsung (T-05), Dialog Konfirmasi, dan Confirm dengan Checkbox Menandai Not Scanned"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-318
  - TC-AC-ACTS-319
  - TC-AC-ACTS-321
  - TC-AC-ACTS-322
coverage:
  web: automated
---

# Audit RFID: Submit Sebelum Scan, Tanpa Not Scanned Commit Langsung (T-05), Dialog Konfirmasi, dan Confirm dengan Checkbox Menandai Not Scanned

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data TC-AC-ACTS-322: SKU yang sama dengan 4 unit Available (di-reset fixture BE sebelum blok TC itu); saldo dan Last Updated SKU dipulihkan fixture BE di hook `after`.

## Test Steps

### TC-AC-ACTS-318: `[Submit]` aktif sebelum sesi scan pertama dan membuka dialog konfirmasi

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Verifikasi `[Submit]` aktif pada keadaan Idle
4. Klik `[Submit]`
5. Verifikasi dialog Konfirmasi `D-03` tampil dengan copy `4 TAGs were not found during this audit.` dan checkbox dicentang
6. Klik `[Cancel]` pada dialog
7. Verifikasi dialog tertutup tanpa perubahan data (status keempat unit di backend tetap, dibaca lewat fixture BE)
8. Klik `✕` pada popup untuk menutup popup Idle

### TC-AC-ACTS-319: Submit tanpa baris Not Scanned commit langsung (T-05)

9. Klik `[Audit TAG]` di toolbar Tab Available
10. Klik `[Start Scan]`
11. Scan semua 4 unit (A, B, C, D)
12. Klik `[Stop]`
13. Klik `[Submit]`
14. Verifikasi tanpa dialog dan recovery Damaged/Missing: unit C dan D menjadi Available
15. Verifikasi toast `Success, TAG has been verified. 2 TAGs recovered to Available.`
16. Verifikasi popup tertutup dan Tab Available di-refresh
17. Verifikasi dua unit Damaged/Missing kini Available (badge Damaged/Missing tidak ada pada unit C dan D)
18. Tunggu toast lama hilang

### TC-AC-ACTS-321: `[Submit]` dengan baris Not Scanned membuka dialog Konfirmasi

19. Reset dataset: kembalikan unit C dan D ke Damaged/Missing lewat fixture BE
20. Klik `[Audit TAG]` di toolbar Tab Available
21. Klik `[Start Scan]`
22. Scan 2 dari 4 unit (A dan B)
23. Klik `[Stop]`
24. Klik `[Submit]`
25. Verifikasi dialog `Confirm Audit` dengan teks `2 TAGs were not found during this audit.`, satu checkbox `Mark all as Damaged/Missing — uncheck to keep their current status instead.` (default dicentang), tombol `[Cancel]` dan `[Confirm]`, tanpa daftar identifier
26. Verifikasi belum ada commit: status unit di backend tetap (dibaca lewat fixture BE)
27. Klik `[Cancel]` pada dialog
28. Klik `✕` pada popup
29. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
30. Klik `[Leave]`

### TC-AC-ACTS-322: Confirm dengan checkbox dicentang menandai semua Not Scanned Damaged/Missing

31. Reset dataset: 4 unit Available lewat fixture BE
32. Klik `[Audit TAG]` di toolbar Tab Available
33. Klik `[Start Scan]`
34. Scan 2 unit Available
35. Klik `[Stop]`
36. Klik `[Submit]`
37. Biarkan checkbox dicentang, klik `[Confirm]`
38. Verifikasi dua baris Not Scanned berstatus Damaged/Missing
39. Verifikasi toast `Success, TAG has been marked as Damaged/Missing.`
40. Verifikasi popup tertutup dan Tab Available di-refresh
41. Verifikasi badge Damaged/Missing tampil di Tab Available

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), `[Cancel]` dialog dan penutup popup antar blok, "Tunggu toast lama hilang" sesudah toast TC-AC-ACTS-319, serta langkah "Reset dataset" lewat fixture BE sebelum TC-AC-ACTS-321 dan TC-AC-ACTS-322 (pemulihan state, S-09). Urutan TC mengikuti nomor TC; TC-AC-ACTS-320 ada di spec 126.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-318 menyebut copy `4 TAGs were not found` pada keadaan Idle dengan 4 unit eligible; Pre-setup TC tidak menyebut kode unit, sehingga spec memakai unit A sampai D hasil seeding.
  - Post Condition TC-AC-ACTS-322 ("Badge Damaged/Missing tampil di Tab Available") diasersi karena TC memberi padanan pada Expected butir a.
