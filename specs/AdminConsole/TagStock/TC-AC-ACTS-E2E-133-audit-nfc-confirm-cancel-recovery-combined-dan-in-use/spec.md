---
id: TC-AC-ACTS-E2E-133-audit-nfc-confirm-cancel-recovery-combined-dan-in-use
title: "Audit NFC: Confirm dengan dan Tanpa Centang, Cancel Dialog, Recovery Damaged/Missing, Unit Combined Eligible, dan Unit In Use Tidak Ditawarkan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-348
  - TC-AC-ACTS-349
  - TC-AC-ACTS-350
  - TC-AC-ACTS-351
  - TC-AC-ACTS-352
  - TC-AC-ACTS-353
coverage:
  web: automated
---

# Audit NFC: Confirm dengan dan Tanpa Centang, Cancel Dialog, Recovery Damaged/Missing, Unit Combined Eligible, dan Unit In Use Tidak Ditawarkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `NFC-CARD-BETA-N2` (Pre-setup #13; Device Name `NFC Access Card`, Brand `Beta`, Model `N2`). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai NFC (scan UID satu per satu, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data per blok TC (di-reset fixture BE): TC-AC-ACTS-348 memakai 4 unit Available; TC-AC-ACTS-349 dan 350 memakai 2 Available dan 2 Damaged/Missing; TC-AC-ACTS-351 memakai satu unit NFC Damaged/Missing saja; TC-AC-ACTS-352 memakai satu unit NFC Combined dengan RFID; TC-AC-ACTS-353 menambah satu unit In Use.

## Test Steps

### TC-AC-ACTS-348: Confirm dengan checkbox dicentang menandai semua Not Scanned Damaged/Missing

1. Reset dataset: 4 unit Available lewat fixture BE
2. Klik row action `Detail` pada SKU `NFC-CARD-BETA-N2` di Stock List, lalu buka Tab Available
3. Klik `[Audit TAG]` di toolbar Tab Available
4. Klik `[Start Scan]`
5. Scan 2 unit Available
6. Klik `[Stop]`
7. Klik `[Submit]`
8. Biarkan checkbox dicentang, klik `[Confirm]`
9. Verifikasi dua baris Not Scanned berstatus Damaged/Missing
10. Verifikasi toast `Success, TAG has been marked as Damaged/Missing.`
11. Verifikasi popup tertutup dan Tab Available di-refresh
12. Verifikasi badge Damaged/Missing tampil di Tab Available
13. Tunggu toast lama hilang

### TC-AC-ACTS-349: Confirm tanpa centang tidak mengubah baris Not Scanned

14. Reset dataset: 2 Available dan 2 Damaged/Missing lewat fixture BE
15. Klik `[Audit TAG]` di toolbar Tab Available
16. Klik `[Start Scan]`
17. Scan 1 unit Available (A) dan 1 unit Damaged/Missing (C)
18. Klik `[Stop]`
19. Klik `[Submit]`
20. Hilangkan centang checkbox, klik `[Confirm]`
21. Verifikasi baris Not Scanned tidak berubah: unit B tetap Available dan unit D tetap Damaged/Missing
22. Verifikasi unit C (Damaged/Missing yang discan) pulih ke Available
23. Verifikasi toast `Success, TAG has been verified. 1 TAG recovered to Available.`
24. Verifikasi popup tertutup dan Tab Available di-refresh
25. Tunggu toast lama hilang

### TC-AC-ACTS-350: `[Cancel]` pada dialog Konfirmasi tidak commit

26. Reset dataset: 2 Available dan 2 Damaged/Missing lewat fixture BE
27. Klik `[Audit TAG]` di toolbar Tab Available
28. Klik `[Start Scan]`
29. Scan 2 unit
30. Klik `[Stop]`
31. Klik `[Submit]`
32. Klik `[Cancel]` pada dialog
33. Verifikasi dialog tertutup dan kembali ke tabel tanpa perubahan data (status unit di backend tetap, dibaca lewat fixture BE)
34. Verifikasi keadaan setelah `[Stop]`: `[Start Scan]` dan `[Submit]` aktif
35. Verifikasi baris Verified dipertahankan
36. Klik `✕` pada popup
37. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
38. Klik `[Leave]`

### TC-AC-ACTS-351: Recovery Damaged/Missing ke Available lewat Submit

39. Reset dataset: satu unit NFC Damaged/Missing saja lewat fixture BE
40. Klik `[Audit TAG]` di toolbar Tab Available
41. Klik `[Start Scan]`
42. Scan unit Damaged/Missing
43. Klik `[Stop]`
44. Klik `[Submit]`
45. Verifikasi unit menjadi Available
46. Verifikasi toast memuat klausa recovery `1 TAG recovered to Available`

### TC-AC-ACTS-352: Unit Combined (sisi NFC) tetap eligible

47. Reset dataset: satu unit NFC Combined dengan RFID lewat fixture BE
48. Klik `[Audit TAG]` di toolbar Tab Available
49. Verifikasi unit NFC Combined ditawarkan di tabel
50. Klik `✕` pada popup untuk menutup popup Idle

### TC-AC-ACTS-353: Unit In Use tidak ditawarkan

51. Reset dataset: tambahkan satu unit In Use dan pertahankan unit eligible lewat fixture BE
52. Klik `[Audit TAG]` di toolbar Tab Available
53. Verifikasi tabel memuat sedikitnya satu baris unit eligible
54. Verifikasi unit In Use tidak ada di tabel
55. Klik `✕` pada popup untuk menutup popup Idle

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 2 (membuka Detail SKU), "Reset dataset" lewat fixture BE, `[Stop]` yang membuka kunci popup, penutup popup, dan "Tunggu toast lama hilang" (pemulihan state, S-09).
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-351, 352, dan 353 tidak menyebut jumlah dan kode unit pada Data Uji; spec memakai unit hasil seeding sesuai Precondition.
  - TC-AC-ACTS-351 mengharapkan "toast memuat klausa recovery" tanpa menyebut teks persis; spec mengasersi klausa `1 TAG recovered to Available` yang konsisten dengan TC-AC-ACTS-349.
