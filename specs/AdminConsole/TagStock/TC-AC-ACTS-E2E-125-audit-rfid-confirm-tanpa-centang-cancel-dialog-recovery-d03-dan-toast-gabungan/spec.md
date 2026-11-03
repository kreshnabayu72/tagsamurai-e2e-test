---
id: TC-AC-ACTS-E2E-125-audit-rfid-confirm-tanpa-centang-cancel-dialog-recovery-d03-dan-toast-gabungan
title: "Audit RFID: Confirm Tanpa Centang, Cancel Dialog, Baris Damaged/Missing Tak Ter-Scan Masuk Hitungan D-03, dan Toast Gabungan dengan Klausa Recovery"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-323
  - TC-AC-ACTS-324
  - TC-AC-ACTS-325
  - TC-AC-ACTS-326
coverage:
  web: automated
---

# Audit RFID: Confirm Tanpa Centang, Cancel Dialog, Baris Damaged/Missing Tak Ter-Scan Masuk Hitungan D-03, dan Toast Gabungan dengan Klausa Recovery

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Pembacaan Activity Log (filter Object `TAG Stock`, Search TAG Code) dipakai untuk TC-AC-ACTS-325; asersi jumlah entri memakai baseline sebelum aksi (S-12).

## Test Steps

### TC-AC-ACTS-323: Confirm tanpa centang tidak mengubah baris Not Scanned

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Klik `[Start Scan]`
4. Scan 1 unit Available (A) dan 1 unit Damaged/Missing (C)
5. Klik `[Stop]`
6. Klik `[Submit]`
7. Hilangkan centang checkbox pada dialog `Confirm Audit`, klik `[Confirm]`
8. Verifikasi baris Not Scanned tidak berubah: unit B tetap Available dan unit D tetap Damaged/Missing
9. Verifikasi unit C (Damaged/Missing yang discan) pulih ke Available
10. Verifikasi toast `Success, TAG has been verified. 1 TAG recovered to Available.`
11. Verifikasi popup tertutup dan Tab Available di-refresh
12. Tunggu toast lama hilang

### TC-AC-ACTS-324: `[Cancel]` pada dialog Konfirmasi tidak commit

13. Reset dataset: 2 Available dan 2 Damaged/Missing lewat fixture BE
14. Klik `[Audit TAG]` di toolbar Tab Available
15. Klik `[Start Scan]`
16. Scan 2 unit (A dan B)
17. Klik `[Stop]`
18. Klik `[Submit]`
19. Klik `[Cancel]` pada dialog
20. Verifikasi dialog tertutup dan kembali ke tabel tanpa perubahan data (status unit di backend tetap, dibaca lewat fixture BE)
21. Verifikasi keadaan setelah `[Stop]`: `[Start Scan]` dan `[Submit]` aktif
22. Verifikasi baris Verified dipertahankan (unit A dan B tetap `✓ Verified`)
23. Klik `✕` pada popup
24. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
25. Klik `[Leave]`

### TC-AC-ACTS-325: Baris Damaged/Missing yang tidak ter-scan masuk hitungan D-03

26. Buka Activity Log (filter Object `TAG Stock`)
27. Catat baseline jumlah entri Activity Log `TAG Stock` untuk unit C dan unit D (Search TAG Code)
28. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
29. Klik `[Audit TAG]` di toolbar Tab Available
30. Klik `[Start Scan]`
31. Scan hanya 2 unit Available (A dan B)
32. Klik `[Stop]`
33. Klik `[Submit]`
34. Verifikasi copy hitungan pada dialog `Confirm Audit` menghitung semua baris Not Scanned termasuk yang sudah Damaged/Missing: `2 TAGs were not found during this audit.`
35. Biarkan checkbox dicentang, klik `[Confirm]`
36. Verifikasi unit C dan D (sudah Damaged/Missing) dilewati: status keduanya tetap Damaged/Missing
37. Buka Activity Log (filter Object `TAG Stock`)
38. Verifikasi jumlah entri Activity Log untuk unit C dan unit D (Search TAG Code) sama dengan baseline langkah 27

### TC-AC-ACTS-326: Toast gabungan memuat klausa recovery bila ada

39. Reset dataset: 2 Available dan 2 Damaged/Missing lewat fixture BE
40. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
41. Klik `[Audit TAG]` di toolbar Tab Available
42. Klik `[Start Scan]`
43. Scan 1 unit Damaged/Missing (C) dan 1 unit Available (A)
44. Klik `[Stop]`
45. Klik `[Submit]`
46. Biarkan checkbox dicentang, klik `[Confirm]`
47. Verifikasi satu toast gabungan `Success, TAG has been marked as Damaged/Missing. 1 TAG recovered to Available.`
48. Verifikasi klausa dengan count 0 tidak ditulis pada toast

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset" lewat fixture BE, penutup popup, `[Stop]` yang membuka kunci popup, navigasi ke Activity Log dan kembali ke Detail SKU, serta "Tunggu toast lama hilang" (pemulihan state, S-09). Urutan TC mengikuti nomor TC; TC-AC-ACTS-320 ada di spec 126.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-323 Post Condition ("Satu unit Damaged/Missing kini Available") ekuivalen dengan Expected butir b dan diasersi di langkah itu.
  - TC-AC-ACTS-325 Expected butir b ("tanpa entri Activity Log baru") diasersi sebagai jumlah entri sama dengan baseline (S-12); TC tidak menyebut filter Activity Log yang dipakai.
  - TC-AC-ACTS-326 Data Uji menyebut "Not Scanned Available ditandai" tanpa menyebut unit mana; spec memakai unit B (Available tak ter-scan) sebagai yang ditandai dan unit D sebagai no-op.
