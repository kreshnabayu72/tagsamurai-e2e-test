---
id: TC-AC-ACTS-E2E-132-audit-nfc-screening-start-scan-verified-stop-dan-submit-dialog
title: "Audit NFC: Screening Popup Idle, Start Scan Mengunci Popup, Verified di Tempat, Stop, dan Submit dengan Not Scanned Membuka Dialog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-343
  - TC-AC-ACTS-344
  - TC-AC-ACTS-345
  - TC-AC-ACTS-346
  - TC-AC-ACTS-347
coverage:
  web: automated
---

# Audit NFC: Screening Popup Idle, Start Scan Mengunci Popup, Verified di Tempat, Stop, dan Submit dengan Not Scanned Membuka Dialog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `NFC-CARD-BETA-N2` (Pre-setup #13; Device Name `NFC Access Card`, Brand `Beta`, Model `N2`). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai NFC (scan UID satu per satu, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Pengamat request jaringan browser (menghitung request selama sesi scan) disediakan tim FE.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.

## Test Steps

### TC-AC-ACTS-343: Screening Popup Audit TAG NFC saat Idle

1. Klik row action `Detail` pada SKU `NFC-CARD-BETA-N2` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Verifikasi judul popup `Audit TAG` tanpa kode SKU dengan icon (X) dan tanpa breadcrumb
4. Verifikasi SKU info card baris 1 `NFC Access Card (NFC-CARD-BETA-N2)` setelah foto
5. Verifikasi SKU info card: `TAG Type:` icon NFC, `Brand:` badge `Beta`, `Model/Type:` badge `N2`
6. Verifikasi body memuat tombol `[Start Scan]`
7. Verifikasi satu tabel dengan kolom `TAG Code` | `Identifier` | `Status` | `Audit Status`
8. Verifikasi semua baris berbadge Audit Status `Not Scanned` severity warning
9. Verifikasi urutan TAG Code A-Z tanpa pagination (scroll vertikal)
10. Verifikasi footer memuat `[Submit]` (Success) aktif
11. Verifikasi tidak ada icon `[Event Log]` di header popup
12. Verifikasi tidak ada indikator `Status: ● Connected` di halaman
13. Klik `✕` pada popup untuk menutup popup Idle

### TC-AC-ACTS-344: `[Start Scan]` mengunci popup dan halaman di belakangnya serta menampilkan widget

14. Klik `[Audit TAG]` di toolbar Tab Available
15. Klik `[Start Scan]`
16. Verifikasi popup dan halaman di belakangnya blur dan non-interaktif
17. Verifikasi Floating Widget `Scanning…` dengan counter `[N] TAGs verified` dan `[Stop]`
18. Verifikasi tidak ada request per TAG selama sesi
19. Klik `[Stop]` di Floating Widget
20. Klik `✕` pada popup untuk menutup popup

### TC-AC-ACTS-345: TAG yang cocok baris menjadi Verified di tempat

21. Klik `[Audit TAG]` di toolbar Tab Available
22. Klik `[Start Scan]`
23. Scan satu unit eligible
24. Klik `[Stop]`
25. Verifikasi Audit Status baris berubah dari `Not Scanned` menjadi `✓ Verified` di tempat dan baris tidak berpindah
26. Verifikasi belum ada write ke database: status unit di backend tidak berubah (dibaca lewat fixture BE)
27. Klik `✕` pada popup
28. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
29. Klik `[Leave]`

### TC-AC-ACTS-346: `[Stop]` membuka kunci dan `[Submit]` aktif

30. Klik `[Audit TAG]` di toolbar Tab Available
31. Klik `[Start Scan]`
32. Scan satu unit
33. Klik `[Stop]`
34. Verifikasi popup interaktif kembali
35. Verifikasi `[Start Scan]` tampil dan aktif di samping `[Submit]`
36. Verifikasi `[Submit]` aktif
37. Klik `✕` pada popup
38. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
39. Klik `[Leave]`

### TC-AC-ACTS-347: `[Submit]` dengan baris Not Scanned membuka dialog Konfirmasi

40. Klik `[Audit TAG]` di toolbar Tab Available
41. Klik `[Start Scan]`
42. Scan 2 dari 4 unit
43. Klik `[Stop]`
44. Klik `[Submit]`
45. Verifikasi dialog `Confirm Audit` dengan teks `2 TAGs were not found during this audit.`, satu checkbox `Mark all as Damaged/Missing — uncheck to keep their current status instead.` (default dicentang), tombol `[Cancel]` dan `[Confirm]`, tanpa daftar identifier
46. Verifikasi belum ada commit: status unit di backend tidak berubah (dibaca lewat fixture BE)
47. Klik `[Cancel]` pada dialog
48. Klik `✕` pada popup
49. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
50. Klik `[Leave]`

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), `[Stop]` yang membuka kunci popup, `[Cancel]` dialog, dan penutup popup (pemulihan state, S-09).
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-343 dan 344 tidak menyebut cara mengamati request dan blur; spec memakai pengamat request jaringan browser yang disediakan tim FE.
  - TC-AC-ACTS-345 butir b ("belum ada write ke database") diamati lewat pembacaan state BE oleh fixture BE; TC tidak memberi cara cek.
