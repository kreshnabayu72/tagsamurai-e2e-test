---
id: TC-AC-ACTS-E2E-122-audit-rfid-screening-popup-start-scan-dan-verified-di-tempat
title: "Audit RFID: Screening Popup Idle, Start Scan Mengunci Popup, TAG Cocok Menjadi Verified, dan TAG Tidak di Tabel Diabaikan Tanpa Toast"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-309
  - TC-AC-ACTS-310
  - TC-AC-ACTS-311
  - TC-AC-ACTS-312
coverage:
  web: automated
---

# Audit RFID: Screening Popup Idle, Start Scan Mengunci Popup, TAG Cocok Menjadi Verified, dan TAG Tidak di Tabel Diabaikan Tanpa Toast

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Pengamat request jaringan browser (menghitung request selama sesi scan) disediakan tim FE.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Unit dari SKU lain: satu unit terdaftar milik SKU `NFC-CARD-BETA-N2` (Pre-setup #13) dipakai sebagai TAG di luar tabel pada TC-AC-ACTS-312.

## Test Steps

### TC-AC-ACTS-309: Screening Popup Audit TAG RFID saat Idle

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Verifikasi judul popup `Audit TAG` tanpa kode SKU dengan icon (X) dan tanpa breadcrumb
4. Verifikasi SKU info card baris 1 `RFID Asset Tag (RFID-ASSET-CORE-R5)` setelah foto
5. Verifikasi SKU info card: `TAG Type:` icon RFID, `Brand:` badge `Core`, `Model/Type:` badge `R5`
6. Verifikasi body memuat tombol `[Start Scan]`
7. Verifikasi satu tabel dengan kolom `TAG Code` | `Identifier` | `Status` | `Audit Status`
8. Verifikasi semua baris berbadge Audit Status `Not Scanned` severity warning
9. Verifikasi urutan TAG Code A-Z tanpa pagination (scroll vertikal)
10. Verifikasi footer memuat `[Submit]` (Success) aktif
11. Verifikasi tidak ada icon `[Event Log]` di header popup
12. Verifikasi tidak ada indikator `Status: ● Connected` di halaman
13. Klik `✕` pada popup untuk menutup popup Idle

### TC-AC-ACTS-310: `[Start Scan]` mengunci popup dan halaman di belakangnya serta menampilkan widget

14. Klik `[Audit TAG]` di toolbar Tab Available
15. Klik `[Start Scan]`
16. Verifikasi popup dan halaman di belakangnya blur dan non-interaktif
17. Verifikasi Floating Widget `Scanning…` dengan counter `[N] TAGs verified` dan `[Stop]`
18. Verifikasi tidak ada request per TAG selama sesi
19. Klik `[Stop]` di Floating Widget
20. Klik `✕` pada popup untuk menutup popup

### TC-AC-ACTS-311: TAG yang cocok baris menjadi Verified di tempat

21. Klik `[Audit TAG]` di toolbar Tab Available
22. Klik `[Start Scan]`
23. Scan unit A (eligible)
24. Klik `[Stop]`
25. Verifikasi Audit Status baris unit A berubah dari `Not Scanned` menjadi `✓ Verified` di tempat dan baris tidak berpindah
26. Verifikasi belum ada write ke database: status unit A di backend tidak berubah (dibaca lewat fixture BE)
27. Klik `✕` pada popup
28. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
29. Klik `[Leave]`

### TC-AC-ACTS-312: TAG yang tidak ada di tabel diabaikan tanpa toast

30. Klik `[Audit TAG]` di toolbar Tab Available
31. Klik `[Start Scan]`
32. Verifikasi Floating Widget `Scanning…` tampil
33. Scan TAG terdaftar milik SKU `NFC-CARD-BETA-N2` (di luar tabel Audit)
34. Verifikasi tidak ada toast
35. Verifikasi counter `[N] TAGs verified` tidak bertambah (`0 TAGs verified`)
36. Klik `[Stop]`
37. Verifikasi tidak ada baris baru di tabel Audit (empat baris awal tetap `Not Scanned`)
38. Klik `✕` pada popup untuk menutup popup

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU, karena `beforeEach` suite membuka Stock List), langkah 13 dan penutup popup di akhir TC-AC-ACTS-310 dan TC-AC-ACTS-312 (pemulihan state, S-09), serta `[Stop]` yang membuka kunci popup sebelum menutup.
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Langkah Uji TC-AC-ACTS-312 nomor 3 menyebut "TAG SKU lain atau yang belum terdaftar" tanpa toast, sedangkan TC-AC-ACTS-948 menyatakan kode yang belum terdaftar menampilkan toast T-38. Spec memakai TAG terdaftar milik SKU lain (sejalan dengan TC-AC-ACTS-949); varian belum terdaftar diuji di spec 130.
  - TC-AC-ACTS-310 butir b ("tidak ada request per TAG") tidak menyebut cara mengamati request; spec memakai pengamat request jaringan browser yang disediakan tim FE.
  - TC-AC-ACTS-311 butir b ("belum ada write ke database") diamati lewat pembacaan state BE oleh fixture BE; TC tidak memberi cara cek.
