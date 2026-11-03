---
id: TC-AC-ACTS-E2E-144-delete-by-scan-reader-putus-pindah-halaman-log-sesi-dan-distributor
title: "Delete by Scan: Reader Terputus, Meninggalkan Halaman (Modal RFID Scan Stopped), Log Sesi Level-Sesi, dan Distributor Hanya Menghapus Stok Sendiri"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-833
  - TC-AC-ACTS-834
  - TC-AC-ACTS-835
  - TC-AC-ACTS-836
coverage:
  web: automated
---

# Delete by Scan: Reader Terputus, Meninggalkan Halaman (Modal RFID Scan Stopped), Log Sesi Level-Sesi, dan Distributor Hanya Menghapus Stok Sendiri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor kedua (Ganti akun): Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Data tambahan TC-AC-ACTS-836: unit Available milik Distributor ini D1 dan unit Available milik Principal P2 pada SKU yang sama, di-seed fixture BE.
- Pembacaan Activity Log, System Log user aktor, dan modal Event Log SKU (Tab Add Stock) dipakai untuk TC-AC-ACTS-835; asersi memakai baseline sebelum aksi (S-12).
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.

## Test Steps

### TC-AC-ACTS-833: Reader terputus di tengah sesi Delete by Scan

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Delete by Scan]` dan scan U1
3. Putuskan Bluetooth semua reader
4. Verifikasi sesi berhenti otomatis seperti `[Stop]`: blur dan widget hilang
5. Verifikasi Sync Panel terbuka
6. Tutup Sync Panel
7. Verifikasi U1 tetap terhapus dan tidak ada di tabel
8. Hubungkan kembali reader RFID (simulator)

### TC-AC-ACTS-834: Meninggalkan halaman saat sesi Delete by Scan aktif memunculkan modal `RFID Scan Stopped`

9. Reset dataset: U1 sampai U4 lewat fixture BE, lalu muat ulang Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
10. Klik `[Delete by Scan]` dan scan U1
11. Klik tombol Back browser
12. Verifikasi modal `RFID Scan Stopped` dengan body `The scan process was interrupted because you left this window.` dan tombol `Leave Page` dan `Continue Scan`
13. Klik `Continue Scan`
14. Verifikasi `Continue Scan` mengembalikan ke sesi aktif
15. Klik tombol Back browser lagi, lalu klik `Leave Page`
16. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
17. Verifikasi U1 tetap terhapus

### TC-AC-ACTS-835: Log sesi Delete by Scan, satu entri level-sesi tanpa entri `Delete Stock` per unit

18. Reset dataset: U1 sampai U4 lewat fixture BE
19. Buka Activity Log (filter Object `TAG Stock`), System Log user aktor, dan modal Event Log SKU (Tab Add Stock), lalu catat baseline jumlah entri `Delete by Scan` dan `Delete Stock` di Activity Log, jumlah entri `Delete by Scan` di System Log, serta jumlah baris Event Log, lalu tutup modal Event Log
20. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
21. Klik `[Delete by Scan]`, scan U1 dan U2, scan satu kode tidak dikenal
22. Klik `[Stop]`
23. Buka Activity Log (filter Object `TAG Stock`), urutkan Newest First
24. Verifikasi satu entri `Delete by Scan` baru (Name `RFID-ASSET-CORE-R5 (RFID)`, Field `Quantity`, Old Value `2 TAGs`, New Value `—`)
25. Verifikasi jumlah entri `Delete Stock` per unit sama dengan baseline
26. Verifikasi scan yang ditolak tidak dihitung pada `Quantity`
27. Buka System Log user aktor
28. Verifikasi jumlah entri `Delete by Scan` di System Log bertambah 1 dari baseline langkah 19 dan entri baru yang sama tampil dengan Quantity `2`
29. Buka modal Event Log SKU (Tab Add Stock)
30. Verifikasi satu baris baru Activity `Delete Stock` dengan Success `2` dan Failed `0`
31. Tutup modal Event Log

### TC-AC-ACTS-836: Distributor hanya menghapus unit stok sendiri; unit entitas lain ditolak sebagai tidak ada di stok

32. Ganti akun: Logout, lalu login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)
33. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
34. Klik `[Delete by Scan]`
35. Scan P2 (milik Principal)
36. Verifikasi toast error `Error, TAG not found in stock.`
37. Scan D1 (milik sendiri)
38. Verifikasi toast `Success, [TAG Code] has been deleted.` dengan TAG Code D1
39. Klik `[Stop]`
40. Verifikasi P2 tidak terhapus (dibaca lewat fixture BE)
41. Verifikasi D1 tidak ada di tabel

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset", "Tutup Sync Panel", "Hubungkan kembali reader RFID", pencatatan baseline dan navigasi ke Activity Log, System Log, dan modal Event Log. Urutan TC mengikuti nomor TC; TC-AC-ACTS-836 terakhir karena Ganti akun ke Distributor. Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Identifier dan hitungan tetap (Data Uji Dinamis) dipakai ulang lintas TC dan tidak dapat bersuffix per run; kebenaran hitungan hanya terjamin bila fixture BE mereset dataset sebelum spec.
  - TC-AC-ACTS-833 Expected butir a ("sesi berhenti otomatis seperti `[Stop]`") dan TC-AC-ACTS-834 butir c ("U1 tetap terhapus") tidak punya langkah observasi sesudah keluar halaman; spec membuka kembali Detail SKU.
  - TC-AC-ACTS-835 butir a (tidak ada entri `Delete Stock` per unit) diasersi sebagai jumlah entri sama dengan baseline (S-12).
  - TC-AC-ACTS-836 tidak menyebut kode unit D1 dan P2; spec memakai unit hasil seeding.
