---
id: TC-AC-ACTS-E2E-135-audit-tag-tidak-tersedia-untuk-ble-gps-dan-qr
title: "Audit TAG Tidak Tersedia: Hidden untuk SKU BLE dan GPS, Request Langsung Ditolak, QR Tanpa Audit, Unit BLE Pra-Aktivasi Tanpa Jalur Damaged/Missing, dan Status BLE di Tab In Use"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-240
  - TC-AC-ACTS-271
  - TC-AC-ACTS-355
  - TC-AC-ACTS-356
  - TC-AC-ACTS-357
  - TC-AC-ACTS-358
  - TC-AC-ACTS-359
coverage:
  web: automated
---

# Audit TAG Tidak Tersedia: Hidden untuk SKU BLE dan GPS, Request Langsung Ditolak, QR Tanpa Audit, Unit BLE Pra-Aktivasi Tanpa Jalur Damaged/Missing, dan Status BLE di Tab In Use

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Data Pre-setup: SKU BLE `BLE-BEACON-ALPHA-B1` (Pre-setup #14), SKU GPS `GPS-TRACK-CORE-G3` (Pre-setup #15), dan SKU RFID `RFID-ASSET-CORE-R5` (Pre-setup #12). Unit uji milik spec di-seed di hook `before` (idempoten): unit Available pada SKU BLE dan SKU GPS, unit BLE In Use (TC-AC-ACTS-358); dipulihkan fixture BE di hook `after`.
- Kemampuan teknis: Klien HTTP untuk request langsung ke server (TC-AC-ACTS-359) dan pengirim event Condition (Damaged/Missing dari FAMS atau Supply) yang disediakan tim FE/BE; endpoint dan mekanismenya tidak disebut di TC, PRD, atau LLD sehingga tidak ditulis di spec.
- Idiom polling: pada TC-AC-ACTS-358 halaman dimuat ulang tiap 5 detik sampai event Condition diproses (batas tunggu 2 menit).

## Test Steps

### TC-AC-ACTS-240: `[Audit TAG]` Hidden untuk SKU BLE

1. Klik row action `Detail` pada SKU `BLE-BEACON-ALPHA-B1` di Stock List, lalu buka Tab Available
2. Verifikasi toolbar memuat Search, Filter, Download, `[Event Log]`, `[Delete by Scan]`, `[Add Stock]`
3. Verifikasi `[Audit TAG]` tidak ada di toolbar

### TC-AC-ACTS-271: `[Audit TAG]` Hidden untuk SKU GPS

4. Kembali ke Stock List, lalu klik row action `Detail` pada SKU `GPS-TRACK-CORE-G3` dan buka Tab Available
5. Verifikasi toolbar Tab Available tanpa `[Audit TAG]`

### TC-AC-ACTS-355: GPS tidak punya mekanisme re-scan Audit

6. Verifikasi `[Audit TAG]` tidak ada di toolbar Tab Available SKU GPS
7. Klik (⋯) pada satu unit GPS
8. Verifikasi satu-satunya aksi unit GPS pra-aktivasi yang hilang atau rusak adalah `[Delete]`
9. Tutup menu aksi unit

### TC-AC-ACTS-356: QR tidak punya Audit di Admin Console

10. Buka Stock List
11. Verifikasi Stock List tidak memuat Audit, Generate, atau Print QR
12. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, lalu buka Tab Available
13. Verifikasi toolbar Tab Available memuat Search, Filter, Download, dan `[Event Log]` (halaman termuat)
14. Verifikasi Tab Available tidak memuat Generate QR atau Print QR (satu-satunya Audit adalah `[Audit TAG]` TAG RFID dan NFC)
15. Buka Tab In Use
16. Verifikasi Tab In Use tidak memuat Audit, Generate, atau Print QR
17. Klik `[Add Stock]`
18. Verifikasi halaman Add Stock tidak memuat Audit, Generate, atau Print QR
19. Kembali ke Stock List

### TC-AC-ACTS-357: Unit BLE pra-aktivasi tidak punya jalur Damaged/Missing selain Delete

20. Klik row action `Detail` pada SKU `BLE-BEACON-ALPHA-B1`, lalu buka Tab Available
21. Verifikasi `[Audit TAG]` tidak ada di toolbar
22. Klik (⋯) pada unit Available
23. Verifikasi aksi unit adalah `TAG Log` dan `Delete`
24. Tutup menu aksi unit

### TC-AC-ACTS-358: Damaged/Missing unit BLE hanya muncul sebagai Status di Tab In Use lewat sinkron

25. Kirim event Condition Damaged/Missing untuk unit BLE In Use (disediakan tim FE/BE)
26. Muat ulang halaman tiap 5 detik sampai event Condition diproses (batas tunggu 2 menit)
27. Buka Tab In Use
28. Verifikasi kolom Status unit menampilkan Damaged/Missing
29. Verifikasi unit tetap di Tab In Use

### TC-AC-ACTS-359: Audit TAG untuk SKU BLE atau GPS tidak tersedia, request langsung ditolak

30. Buka Tab Available SKU `BLE-BEACON-ALPHA-B1`
31. Verifikasi `[Audit TAG]` Hidden
32. Kirim request daftar unit Audit untuk SKU BLE secara langsung lewat klien HTTP sebagai Total Control
33. Verifikasi server menolak request (status respons penolakan)
34. Verifikasi tidak ada data tersimpan: state unit SKU BLE tidak berubah (dibaca lewat fixture BE)

## Notes

- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), navigasi antar SKU dan Stock List, "Klik (⋯)" dan "Tutup menu aksi unit" (pembuka dan penutup observasi row action), serta "Muat ulang halaman tiap 5 detik" (idiom polling).
- K-1: TC-AC-ACTS-359 berkelas a (request langsung) dengan Expected respons API; tetap FE+BE dan hanya mengasersi status respons dan state data (8b butir 1). TC itu satu-satunya objek uji ringan kelas a di spec ini (P-5 butir b).
- Pembagian TC lintas spec: TC-AC-ACTS-240 dan 271 (Hidden untuk BLE dan GPS) dikumpulkan di spec ini bersama TC-AC-ACTS-355 sampai 359.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - TC-AC-ACTS-355 butir "satu-satunya aksi unit GPS ... adalah `[Delete]`" tidak punya langkah observasi di TC; spec menambah langkah membuka menu aksi unit GPS untuk mengasersinya.
  - TC-AC-ACTS-356 langkah "Telusuri semua halaman TAG > Stock" tidak menyebut halaman; spec menelusuri Stock List, Tab Available, Tab In Use, dan halaman Add Stock.
  - TC-AC-ACTS-358 menyebut Client melaporkan Damaged/Missing lewat FAMS atau Supply tanpa langkah pemicu; spec memakai pengirim event Condition yang disediakan tim FE/BE.
  - TC-AC-ACTS-359 tidak menyebut endpoint dan format respons penolakan; spec hanya mengasersi bahwa respons menolak dan state data tidak berubah (8b butir 1).
