---
id: TC-AC-ACTS-E2E-129-audit-rfid-klik-ganda-tanpa-stock-ledger-event-log-dan-start-scan-tanpa-reader
title: "Audit RFID: Klik Ganda Submit Diproses Sekali, Audit Tidak Menulis Stock Ledger, Pencatatan Perubahan di Event Log, dan Start Scan Tanpa Reader (V-03)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-340
  - TC-AC-ACTS-341
  - TC-AC-ACTS-342
  - TC-AC-ACTS-716
coverage:
  web: automated
---

# Audit RFID: Klik Ganda Submit Diproses Sekali, Audit Tidak Menulis Stock Ledger, Pencatatan Perubahan di Event Log, dan Start Scan Tanpa Reader (V-03)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Kemampuan teknis: Pembacaan saldo Stock Ledger entitas registrant lewat Device Allocation > Stock Balance Summary Panel dan pembacaan Activity Log (Search TAG Code); asersi jumlah entri memakai baseline sebelum aksi (S-12).
- Data per blok TC (di-reset fixture BE): tiap blok memakai 2 Available (A, B) dan 2 Damaged/Missing (C, D); blok TC-AC-ACTS-716 memerlukan kondisi tanpa reader RFID terhubung (simulator). Pemutusan reader di TC-AC-ACTS-716 adalah langkah uji; koneksi dipulihkan oleh hook `beforeEach` suite (lihat `suite.md`).

## Test Steps

### TC-AC-ACTS-340: Klik ganda `[Submit]` diproses sekali

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Buka Activity Log (filter Object `TAG Stock`) dan catat baseline jumlah entri untuk unit C dan unit D (Search TAG Code)
3. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
4. Klik `[Audit TAG]` di toolbar Tab Available
5. Klik `[Start Scan]`
6. Scan semua unit (A, B, C, D)
7. Klik `[Stop]`
8. Klik `[Submit]` dua kali cepat
9. Verifikasi tombol `[Submit]` disabled setelah klik pertama
10. Tunggu aksi selesai (Popup Audit TAG tertutup)
11. Buka Activity Log (filter Object `TAG Stock`, Search TAG Code unit C dan D)
12. Verifikasi satu commit: jumlah entri Activity Log untuk unit C dan D masing-masing bertambah satu dari baseline langkah 2

### TC-AC-ACTS-341: Audit tidak menulis Stock Ledger

13. Reset dataset: 2 Available dan 2 Damaged/Missing lewat fixture BE
14. Buka Device Allocation > Stock Balance Summary Panel dan catat saldo Stock Ledger entitas registrant
15. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
16. Klik `[Audit TAG]` di toolbar Tab Available
17. Klik `[Start Scan]`
18. Scan 1 unit Damaged/Missing (C) dan 1 unit Available (A)
19. Klik `[Stop]`
20. Klik `[Submit]`
21. Biarkan checkbox dicentang, klik `[Confirm]` (unit B ditandai Damaged/Missing dan unit C dipulihkan)
22. Tunggu aksi selesai (Popup Audit TAG tertutup)
23. Buka Device Allocation > Stock Balance Summary Panel dan baca saldo entitas registrant
24. Verifikasi saldo Stock Ledger tidak berubah oleh Mark maupun Recovery

### TC-AC-ACTS-342: Pencatatan perubahan kondisi di Event Log dan audit trail

25. Reset dataset: 2 Available dan 2 Damaged/Missing lewat fixture BE
26. Buka Activity Log (filter Object `TAG Stock`)
27. Catat baseline jumlah entri Activity Log `Mark as Damaged/Missing` dan `Mark as Available` untuk unit A, B, C
28. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
29. Klik `[Audit TAG]` di toolbar Tab Available
30. Klik `[Start Scan]`
31. Scan 1 unit Damaged/Missing (C) dan 1 unit Available (A)
32. Klik `[Stop]`
33. Klik `[Submit]`
34. Biarkan checkbox dicentang, klik `[Confirm]` (satu Mark pada unit B dan satu Recovery pada unit C)
35. Tunggu aksi selesai (Popup Audit TAG tertutup)
36. Buka Activity Log (filter Object `TAG Stock`)
37. Verifikasi entri `Mark as Damaged/Missing` untuk unit B bertambah satu dari baseline langkah 27
38. Verifikasi entri `Mark as Available` untuk unit C bertambah satu dari baseline langkah 27

### TC-AC-ACTS-716: `[Start Scan]` tanpa reader RFID terhubung menampilkan toast V-03

39. Reset dataset: 2 Available dan 2 Damaged/Missing lewat fixture BE, lalu putuskan semua reader RFID (simulator)
40. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
41. Klik `[Audit TAG]` di toolbar Tab Available
42. Klik `[Start Scan]`
43. Verifikasi toast error `Reader not connected. Check Bluetooth connection.`
44. Verifikasi sesi tidak dimulai: popup tetap Idle dengan `[Start Scan]` tampil
45. Verifikasi tombol `[Reconnect]` inline tampil
46. Klik `✕` pada popup untuk menutup popup Idle

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset", navigasi ke Device Allocation, Activity Log, dan kembali ke Detail SKU, serta penutup popup (pemulihan state, S-09). TC-AC-ACTS-716 diletakkan di akhir karena membutuhkan kondisi tanpa reader. Langkah "Tunggu aksi selesai" ditambahkan sebelum pindah surface atau ganti akun sesudah aksi yang hasilnya tidak diasersi langsung (bagian 8b butir 8).
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-340 Expected ("satu commit") tidak menyebut cara mengamati satu commit; spec memakai jumlah entri Activity Log per unit terhadap baseline.
  - TC-AC-ACTS-342 menyebut "Event Log dan audit trail" pada skenario tetapi Expected dan langkah hanya Activity Log; spec mengasersi Activity Log saja (S-02) karena TC tidak menyebut Event Log di Expected.
  - TC-AC-ACTS-341 dan 342 tidak menyebut unit yang dipakai; spec memakai unit A sampai D hasil seeding.
