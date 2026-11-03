---
id: TC-AC-ACTS-E2E-055-add-stock-rfid-reader-tidak-terhubung-putus-saat-sesi-dan-idle
title: "Add Stock RFID: Reader Tidak Terhubung (Toast V-03), Putus di Tengah Sesi, Putus saat Idle, dan Satu dari Dua Reader Putus"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-163
  - TC-AC-ACTS-164
  - TC-AC-ACTS-165
  - TC-AC-ACTS-166
coverage:
  web: automated
---

# Add Stock RFID: Reader Tidak Terhubung (Toast V-03), Putus di Tengah Sesi, Putus saat Idle, dan Satu dari Dua Reader Putus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #12 `RFID-ASSET-CORE-R5` (Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, TAG Type RFID).
- Kemampuan teknis: simulator pemindai RFID (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- TAG uji RFID (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | EPC | UID |
|---|---|---|
| TAG A | `Fixture.tagStock.rfidA.epc` (`E280116060000208A1B2C3`) | `Fixture.tagStock.rfidA.uid` (`A1B2C3D4E5F6`) |
| TAG B | `Fixture.tagStock.rfidB.epc` (`E280116060000208D4E5F6`) | `Fixture.tagStock.rfidB.uid` (`A1B2C3D4E5F7`) |
| TAG C | `Fixture.tagStock.rfidC.epc` | `Fixture.tagStock.rfidC.uid` |

- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Atur simulator: reader RFID tidak terhubung
2. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
3. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-163: Add by Scan tanpa reader terhubung

4. Klik `[Add by Scan]`
5. Verifikasi toast error `Reader not connected. Check Bluetooth connection.`
6. Verifikasi sesi tidak dimulai dan halaman tetap Idle
7. Verifikasi tombol `[Reconnect]` inline tampil

### TC-AC-ACTS-165: Reader putus saat Idle

8. Hubungkan reader RFID melalui simulator
9. Putuskan Bluetooth reader saat belum ada sesi
10. Verifikasi `Reader disconnected.` tampil
11. Verifikasi tombol `[Reconnect]` tampil

### TC-AC-ACTS-164: Reader putus di tengah sesi scan

12. Hubungkan kembali reader RFID melalui simulator
13. Klik `[Add by Scan]`
14. Scan TAG A
15. Scan TAG B
16. Putuskan Bluetooth semua perangkat yang melayani sesi
17. Verifikasi sesi berhenti otomatis seperti `[Stop]` (blur hilang)
18. Verifikasi widget scan hilang
19. Verifikasi dua baris yang sudah ter-scan tetap ada
20. Verifikasi Sync Panel terbuka otomatis
21. Verifikasi tidak ada popup `[Reconnect]` terpisah
22. Tutup Sync Panel

### TC-AC-ACTS-166: Satu dari dua reader putus

23. Hubungkan dua reader RFID melalui simulator
24. Klik `[Add by Scan]`
25. Putuskan satu reader
26. Verifikasi sesi tidak berhenti
27. Verifikasi tidak ada notifikasi
28. Scan TAG C lewat reader yang tersisa
29. Verifikasi baris TAG C bertambah di Scanned TAG List
30. Klik `[Stop]`
31. Klik `[Cancel]`
32. Verifikasi dialog Unsaved Changes: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
33. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 2 dan 3 (membuka halaman Add Stock), penyetelan simulator reader antar TC (menghubungkan dan memutuskan), penutupan Sync Panel, dan penutupan halaman dirty di akhir (S-08).
- Urutan TC dalam spec: 163, 165, 164, 166 (keadaan reader tidak terhubung lebih dulu, lalu terhubung dan diputus).
- Temuan untuk QA: TC-AC-ACTS-163, 164, 165, dan 166 memakai "putuskan Bluetooth" tanpa menjelaskan cara memutus reader di simulator; disediakan tim FE. TC-AC-ACTS-166 Expected (b) "reader yang tersisa terus melayani scan" ditulis sebagai scan satu TAG lewat reader tersisa (TC tidak memberi langkah scan).
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
