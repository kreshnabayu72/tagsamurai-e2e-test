---
id: TC-AC-ACTS-E2E-126-audit-rfid-toast-netral-t20-bentuk-tunggal-counter-dan-badge-severity
title: "Audit RFID: Submit Tanpa Perubahan Status (Toast Netral T-20), Dialog Konfirmasi Bentuk Tunggal, Counter Widget Tunggal dan Jamak, dan Badge Audit Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-320
  - TC-AC-ACTS-756
  - TC-AC-ACTS-765
  - TC-AC-ACTS-774
coverage:
  web: automated
---

# Audit RFID: Submit Tanpa Perubahan Status (Toast Netral T-20), Dialog Konfirmasi Bentuk Tunggal, Counter Widget Tunggal dan Jamak, dan Badge Audit Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data per blok TC (di-reset fixture BE sebelum tiap blok): TC-AC-ACTS-774 dan 765 memakai 2 Available dan 2 Damaged/Missing; TC-AC-ACTS-756 memakai 3 unit eligible; TC-AC-ACTS-320 memakai seluruh unit eligible berstatus Available (2 unit).
- Pembacaan Activity Log dan Last Updated SKU di Stock List dipakai untuk TC-AC-ACTS-320; asersi memakai baseline sebelum aksi (S-12).

## Test Steps

### TC-AC-ACTS-774: Badge Audit Status severity warning untuk Not Scanned dan success untuk Verified

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Verifikasi semua baris awal berbadge `Not Scanned` severity warning
4. Klik `[Start Scan]`
5. Scan satu unit eligible
6. Klik `[Stop]`
7. Verifikasi baris yang discan berbadge `✓ Verified` severity success
8. Klik `✕` pada popup
9. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
10. Klik `[Leave]`

### TC-AC-ACTS-765: Counter widget bentuk tunggal untuk satu TAG dan jamak untuk lebih dari satu

11. Klik `[Audit TAG]` di toolbar Tab Available
12. Klik `[Start Scan]`
13. Scan satu unit eligible
14. Verifikasi counter `1 TAG verified`
15. Scan unit eligible kedua
16. Verifikasi counter `2 TAGs verified`
17. Klik `[Stop]`
18. Klik `✕` pada popup
19. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
20. Klik `[Leave]`

### TC-AC-ACTS-756: Dialog Konfirmasi bentuk tunggal untuk satu baris Not Scanned

21. Reset dataset: 3 unit eligible lewat fixture BE
22. Klik `[Audit TAG]` di toolbar Tab Available
23. Klik `[Start Scan]`
24. Scan 2 dari 3 unit
25. Klik `[Stop]`
26. Klik `[Submit]`
27. Verifikasi dialog `Confirm Audit` dengan teks `1 TAG was not found during this audit.` dan satu checkbox `Mark all as Damaged/Missing — uncheck to keep their current status instead.`
28. Verifikasi tombol `[Cancel]` dan `[Confirm]`
29. Klik `[Cancel]` pada dialog
30. Klik `✕` pada popup
31. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
32. Klik `[Leave]`

### TC-AC-ACTS-320: Submit tanpa perubahan status memakai toast netral T-20

33. Reset dataset: seluruh unit eligible berstatus Available lewat fixture BE
34. Kembali ke Stock List dan catat Last Updated SKU `RFID-ASSET-CORE-R5`
35. Buka Activity Log (filter Object `TAG Stock`)
36. Catat baseline jumlah entri Activity Log `TAG Stock`
37. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
38. Klik `[Audit TAG]` di toolbar Tab Available
39. Klik `[Start Scan]`
40. Scan semua unit eligible
41. Klik `[Stop]`
42. Klik `[Submit]`
43. Verifikasi toast netral `No changes to save.`
44. Verifikasi tidak ada perubahan status: seluruh unit tetap Available (dibaca lewat fixture BE)
45. Buka Activity Log (filter Object `TAG Stock`)
46. Verifikasi jumlah entri Activity Log sama dengan baseline langkah 36
47. Buka Stock List dan baca Last Updated SKU `RFID-ASSET-CORE-R5`
48. Verifikasi Last Updated SKU tidak berubah dari nilai yang dicatat

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset" lewat fixture BE, penutup popup, `[Stop]` yang membuka kunci popup, `[Cancel]` dialog, dan navigasi antar Stock List, Activity Log, dan Detail SKU (pemulihan state, S-09).
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-320 Expected butir b ("tidak ada entri Activity Log baru, Last Updated tidak berubah") diasersi sebagai jumlah entri sama dengan baseline; TC memberi langkah observasi pada Langkah Uji nomor 4 tetapi tidak menyebut baseline.
  - Langkah Uji TC-AC-ACTS-320 nomor 4 "baca Last Updated" dilakukan sebelum dan sesudah aksi agar perubahan dapat dibandingkan; TC hanya menyebut membaca setelah Submit.
