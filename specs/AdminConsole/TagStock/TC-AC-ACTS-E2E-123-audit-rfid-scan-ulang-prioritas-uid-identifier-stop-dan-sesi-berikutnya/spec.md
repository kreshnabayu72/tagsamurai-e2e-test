---
id: TC-AC-ACTS-E2E-123-audit-rfid-scan-ulang-prioritas-uid-identifier-stop-dan-sesi-berikutnya
title: "Audit RFID: Scan Ulang Tidak Menambah Counter, UID Menang, Kolom Identifier EPC/UID, Stop Membuka Kunci, dan Sesi Berikutnya Mempertahankan Verified"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-313
  - TC-AC-ACTS-314
  - TC-AC-ACTS-315
  - TC-AC-ACTS-316
  - TC-AC-ACTS-317
coverage:
  web: automated
---

# Audit RFID: Scan Ulang Tidak Menambah Counter, UID Menang, Kolom Identifier EPC/UID, Stop Membuka Kunci, dan Sesi Berikutnya Mempertahankan Verified

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

### TC-AC-ACTS-313: Scan ulang TAG yang sudah Verified tidak menambah counter

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Klik `[Start Scan]`
4. Scan unit A dua kali
5. Verifikasi counter menghitung baris Verified unik: `1 TAG verified`
6. Verifikasi tabel tidak berubah: hanya baris unit A `✓ Verified`, baris lain tetap `Not Scanned`
7. Verifikasi tidak ada toast
8. Klik `[Stop]`
9. Klik `✕` pada popup
10. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
11. Klik `[Leave]`

### TC-AC-ACTS-314: UID menang bila EPC dan UID cocok ke baris berbeda

12. Klik `[Audit TAG]` di toolbar Tab Available
13. Klik `[Start Scan]`
14. Scan TAG dengan EPC milik baris A dan UID milik baris B
15. Klik `[Stop]`
16. Verifikasi baris B (UID cocok) menjadi `✓ Verified`
17. Verifikasi baris A tetap `Not Scanned`
18. Klik `✕` pada popup
19. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
20. Klik `[Leave]`

### TC-AC-ACTS-315: Kolom Identifier menampilkan `EPC / UID` per baris

21. Klik `[Audit TAG]` di toolbar Tab Available
22. Verifikasi setiap baris RFID pada kolom Identifier menampilkan `[EPC Code] / [UID Code]`
23. Klik `✕` pada popup untuk menutup popup Idle

### TC-AC-ACTS-316: `[Stop]` membuka kunci dan `[Submit]` aktif

24. Klik `[Audit TAG]` di toolbar Tab Available
25. Klik `[Start Scan]`
26. Scan satu unit
27. Klik `[Stop]`
28. Verifikasi popup interaktif kembali
29. Verifikasi `[Start Scan]` tampil dan aktif di samping `[Submit]`
30. Verifikasi `[Submit]` aktif
31. Klik `✕` pada popup
32. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
33. Klik `[Leave]`

### TC-AC-ACTS-317: Sesi scan berikutnya mempertahankan baris Verified

34. Klik `[Audit TAG]` di toolbar Tab Available
35. Klik `[Start Scan]`
36. Scan unit A
37. Klik `[Stop]`
38. Klik `[Start Scan]` lagi
39. Verifikasi counter widget sesi kedua dimulai dari `1 TAG verified` (kumulatif lintas sesi)
40. Scan unit B
41. Verifikasi counter widget menjadi `2 TAGs verified`
42. Klik `[Stop]`
43. Verifikasi baris A tetap `✓ Verified` dan baris B menjadi `✓ Verified`, tanpa reset ke `Not Scanned`
44. Klik `✕` pada popup
45. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
46. Klik `[Leave]`

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), penutup popup di akhir tiap blok TC (pemulihan state, S-09).
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Langkah Uji TC-AC-ACTS-317 nomor 3 menyebut "amati counter widget" saat sesi kedua dimulai; spec mengasersi `1 TAG verified` sesudah `[Start Scan]` lagi, mengikuti Expected butir b.
