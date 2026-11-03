---
id: TC-AC-ACTS-E2E-134-audit-nfc-start-scan-tanpa-reader-d06-leave-cancel-dan-scan-uid-belum-terdaftar
title: "Audit NFC: Start Scan Tanpa Reader (V-03), Tutup Popup Setelah Stop (D-06 Leave dan Cancel), dan Scan UID Belum Terdaftar (T-38)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-717
  - TC-AC-ACTS-718
  - TC-AC-ACTS-719
  - TC-AC-ACTS-951
coverage:
  web: automated
---

# Audit NFC: Start Scan Tanpa Reader (V-03), Tutup Popup Setelah Stop (D-06 Leave dan Cancel), dan Scan UID Belum Terdaftar (T-38)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `NFC-CARD-BETA-N2` (Pre-setup #13; Device Name `NFC Access Card`, Brand `Beta`, Model `N2`). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai NFC (scan UID satu per satu, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data kode scan TC-AC-ACTS-951: UID `04A1B2C3D4E5F6` tidak terdaftar di TAG Stock (nilai literal tetap, S-12).
- TC-AC-ACTS-717 memerlukan kondisi tanpa reader NFC terhubung (simulator); diletakkan di akhir spec.

## Test Steps

### TC-AC-ACTS-718: Menutup popup setelah Stop dengan baris Verified memunculkan D-06: `[Leave]`

1. Klik row action `Detail` pada SKU `NFC-CARD-BETA-N2` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Klik `[Start Scan]`
4. Scan 1 unit
5. Klik `[Stop]`
6. Klik `✕` pada popup
7. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
8. Klik `[Leave]`
9. Verifikasi popup tertutup dan kembali ke Tab Available
10. Klik `[Audit TAG]` di toolbar Tab Available
11. Verifikasi baris Verified yang belum Submit hilang: seluruh baris `Not Scanned`
12. Klik `✕` pada popup untuk menutup popup Idle

### TC-AC-ACTS-719: D-06 `[Cancel]` tetap di popup dengan Verified utuh

13. Klik `[Audit TAG]` di toolbar Tab Available
14. Klik `[Start Scan]`
15. Scan 1 unit
16. Klik `[Stop]`
17. Klik `✕` pada popup
18. Klik `[Cancel]` pada dialog Unsaved Changes
19. Verifikasi dialog tertutup dan Popup Audit tetap terbuka
20. Verifikasi baris Verified utuh
21. Klik `✕` pada popup
22. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
23. Klik `[Leave]`

### TC-AC-ACTS-951: Scan UID yang belum terdaftar di TAG Stock menampilkan toast T-38

24. Klik `[Audit TAG]` di toolbar Tab Available
25. Klik `[Start Scan]`
26. Scan UID `04A1B2C3D4E5F6`
27. Verifikasi toast error `Error, this TAG hasn't been registered yet.`
28. Verifikasi tidak ada baris yang berubah atau bertambah (seluruh baris tetap `Not Scanned`)
29. Verifikasi sesi scan tetap aktif (Floating Widget `Scanning…` tampil)
30. Klik `[Stop]`
31. Klik `✕` pada popup untuk menutup popup Idle

### TC-AC-ACTS-717: `[Start Scan]` tanpa reader NFC terhubung menampilkan toast V-03

32. Putuskan semua reader NFC (simulator)
33. Klik `[Audit TAG]` di toolbar Tab Available
34. Klik `[Start Scan]`
35. Verifikasi toast error `Reader not connected. Check Bluetooth connection.`
36. Verifikasi sesi tidak dimulai: popup tetap Idle dengan `[Start Scan]` tampil
37. Verifikasi tombol `[Reconnect]` inline tampil
38. Klik `✕` pada popup untuk menutup popup Idle

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), `[Stop]` yang membuka kunci popup, penutup popup, dan "Putuskan semua reader NFC" sebagai pembentuk kondisi TC-AC-ACTS-717 (pemulihan state, S-09). Urutan TC: 718, 719, 951, 717 karena 717 membutuhkan kondisi tanpa reader.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-718 butir b ("baris Verified yang belum Submit hilang") tidak memberi langkah observasi; spec membuka Popup Audit lagi untuk mengasersinya.
  - TC-AC-ACTS-951 menyebut "sesi scan tetap aktif sampai `[Stop]`"; spec mengasersi widget `Scanning…` sebelum `[Stop]`.
