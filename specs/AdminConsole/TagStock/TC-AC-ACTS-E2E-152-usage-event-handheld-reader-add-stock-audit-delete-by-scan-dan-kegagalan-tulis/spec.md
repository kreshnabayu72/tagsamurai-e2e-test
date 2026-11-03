---
id: TC-AC-ACTS-E2E-152-usage-event-handheld-reader-add-stock-audit-delete-by-scan-dan-kegagalan-tulis
title: "Usage Event Handheld Reader: Satu Event per Sesi Add Stock, Audit, dan Delete by Scan serta Kegagalan Menulis Usage Event pada Submit Add Stock dan Delete by Scan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-860
  - TC-AC-ACTS-861
  - TC-AC-ACTS-862
  - TC-AC-ACTS-866
  - TC-AC-ACTS-867
coverage:
  web: automated
---

# Usage Event Handheld Reader: Satu Event per Sesi Add Stock, Audit, dan Delete by Scan serta Kegagalan Menulis Usage Event pada Submit Add Stock dan Delete by Scan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Data Pre-setup: Handheld Reader `HR-RFID-01` (Pre-setup #25), terdaftar dan terdeteksi di Sync Panel lewat simulator reader USB; Tab Usage dibaca sebagai baseline jumlah baris sebelum aksi (S-12). Reader USB bukan objek uji spec ini, melainkan pembentuk kondisi.
- Kemampuan teknis: Simulator Handheld Reader USB `HR-RFID-01` di Sync Panel (terdeteksi atau tidak terdaftar) dan simulator pemindai RFID disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Injeksi kegagalan penulisan Usage Event di sisi server (TC-AC-ACTS-866 dan 867; pemicu: penulisan Usage Event diset gagal lewat fixture BE), disediakan tim BE; mekanismenya tidak ditulis di spec. Hook `after` spec ini memulihkan penulisan Usage Event ke normal lewat fixture BE bila langkah pemulihan di akhir blok tidak tercapai. Waktu baris Usage Event dibandingkan dengan waktu sesi ditutup (toleransi satu menit; jam server dan jam browser sinkron).
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data per blok TC (di-reset fixture BE): TC-AC-ACTS-860 memakai SKU `RFID-ASSET-CORE-R5` dengan 3 TAG baru yang belum terdaftar; TC-AC-ACTS-861 memakai 2 Available dan 2 Damaged/Missing; TC-AC-ACTS-862, 867 memakai unit uji hapus (Data Dinamis #5); TC-AC-ACTS-866 memakai 2 TAG baru di Scanned TAG List.

## Test Steps

### TC-AC-ACTS-860: Usage Event `Add Stock`, satu event per Submit sesi Add Stock RFID

1. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage, lalu catat baseline jumlah baris
2. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5`
3. Klik `[Add by Scan]`, scan 3 TAG baru, klik `[Stop]`
4. Klik `[Submit]`
5. Tunggu aksi selesai
6. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage
7. Verifikasi Tab Usage memuat tepat satu baris baru untuk sesi ini (bukan tiga baris per TAG)
8. Verifikasi baris itu: Product `Admin Console`, Event Type `Add Stock`, PIC nama pengguna pelaksana, Transaction ID `—`, waktu sesuai waktu sesi ditutup (`[Submit]`)

### TC-AC-ACTS-861: Usage Event `Audit Stock`, satu event per Submit atau Confirm Audit RFID

9. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage, lalu catat baseline jumlah baris
10. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
11. Klik `[Audit TAG]` dan `[Start Scan]`, scan 2 unit, klik `[Stop]`
12. Klik `[Submit]`, lalu pada dialog `Confirm Audit` klik `[Confirm]`
13. Tunggu aksi selesai
14. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage
15. Verifikasi Tab Usage memuat satu baris baru dari baseline
16. Verifikasi baris itu: Product `Admin Console`, Event Type `Audit Stock`, PIC nama pengguna pelaksana, Transaction ID `—`

### TC-AC-ACTS-862: Usage Event `Delete Stock`, satu event per sesi Delete by Scan, ditulis saat sesi ditutup

17. Reset dataset: U1 sampai U4 lewat fixture BE
18. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage, lalu catat baseline jumlah baris
19. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, klik `[Delete by Scan]`, scan U1, U2, dan U3
20. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage sebelum sesi ditutup
21. Verifikasi belum ada baris `Delete Stock` baru di Tab Usage (jumlah baris sama dengan baseline)
22. Kembali ke sesi Delete by Scan dan klik `[Stop]`
23. Tunggu aksi selesai
24. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage
25. Verifikasi Tab Usage memuat tepat satu baris baru
26. Verifikasi baris itu: Product `Admin Console`, Event Type `Delete Stock`, PIC nama pengguna pelaksana, Transaction ID `—`, waktu sesuai waktu sesi ditutup

### TC-AC-ACTS-866: Kegagalan menulis Usage Event membatalkan Submit Add Stock

27. Reset dataset dan atur penulisan Usage Event gagal di sisi server lewat fixture BE
28. Catat baseline jumlah entri Activity Log `Add Stock`, jumlah unit SKU `RFID-ASSET-CORE-R5`, dan saldo Stock Ledger
29. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5`, scan 2 TAG baru, klik `[Stop]`
30. Klik `[Submit]`
31. Verifikasi toast error `Error, failed to register TAGs.`
32. Buka Activity Log dan Tab Available
33. Verifikasi tidak ada unit, receipt, saldo Stock Ledger, atau entri Activity Log yang tersimpan: jumlah unit, saldo, dan jumlah entri sama dengan baseline (rollback penuh)

### TC-AC-ACTS-867: Kegagalan menulis Usage Event saat sesi Delete by Scan ditutup, unit terhapus tetap terhapus

34. Reset dataset: U1 sampai U4 lewat fixture BE, dan atur penulisan Usage Event gagal di sisi server
35. Catat baseline jumlah entri Activity Log `Delete by Scan`, jumlah baris Event Log SKU (Tab Add Stock), dan jumlah baris Tab Usage `HR-RFID-01`
36. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, klik `[Delete by Scan]`, scan U1 dan U2
37. Klik `[Stop]`
38. Verifikasi toast error `Error, failed to delete unit.` saat sesi ditutup
39. Verifikasi U1 dan U2 tetap terhapus (tanpa entri log per unit)
40. Buka Activity Log
41. Verifikasi jumlah entri level-sesi `Delete by Scan` sama dengan baseline
42. Buka modal Event Log SKU (Tab Add Stock)
43. Verifikasi jumlah baris Event Log sama dengan baseline
44. Tutup modal Event Log
45. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage
46. Verifikasi jumlah baris Tab Usage sama dengan baseline
47. Pulihkan penulisan Usage Event ke normal lewat fixture BE

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (pencatatan baseline Tab Usage), "Reset dataset", navigasi ke Tab Usage, Activity Log, dan Detail SKU, "Tunggu aksi selesai", serta pemulihan penulisan Usage Event ke normal. Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- P-8: seluruh TC di spec ini membutuhkan Handheld Reader USB `HR-RFID-01` terdeteksi di Sync Panel (simulator USB) hanya untuk membentuk precondition; objek uji adalah penulisan Usage Event, bukan reader USB. Blok TC kegagalan penulisan (TC-AC-ACTS-866 dan 867) diletakkan paling akhir sehingga kegagalan simulator tidak menutupi blok sebelumnya.
- P-1: bagian "tidak ada unit, receipt, saldo, atau entri Activity Log tersimpan" (TC-AC-ACTS-866) dan "tidak ada entri level-sesi, baris Event Log, dan baris Tab Usage" (TC-AC-ACTS-867) diasersi sebagai jumlah sama dengan baseline di spec ini karena bergantung pada state kegagalan penulisan yang dibangun fixture BE sebelum aksi TC yang sama.
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Identifier dan hitungan tetap (Data Uji Dinamis) dipakai ulang lintas TC dan tidak dapat bersuffix per run; kebenaran hitungan hanya terjamin bila fixture BE mereset dataset sebelum spec.
  - Langkah Uji TC-AC-ACTS-860 nomor 1 menyebut `[Add by Scan]` dan TC-AC-ACTS-861 menyebut Tab Usage tanpa menyebut cara menutup dialog; spec mengikuti TC dan tidak menambah langkah.
  - TC-AC-ACTS-862 butir a mengasersi Tab Usage sebelum sesi ditutup; spec membuka Tab Usage di tengah sesi (halaman lain dalam tab browser yang sama menutup sesi) sehingga urutan keluar dan kembali ke sesi mengikuti langkah TC; QA perlu memastikan sesi tidak berhenti saat berpindah halaman.
  - Waktu baris Usage Event (waktu sesi ditutup) diasersi dengan toleransi satu menit; TC tidak menyebut toleransi.
