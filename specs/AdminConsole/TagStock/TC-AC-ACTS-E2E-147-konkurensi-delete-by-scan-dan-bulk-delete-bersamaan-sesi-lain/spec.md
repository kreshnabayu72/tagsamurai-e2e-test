---
id: TC-AC-ACTS-E2E-147-konkurensi-delete-by-scan-dan-bulk-delete-bersamaan-sesi-lain
title: "Konkurensi Delete: Unit Berubah Status oleh Sesi Lain (T-17, D-05, T-32), Bulk Delete Tidak Eligible (T-30), dan Bulk Delete Bersamaan dengan Sesi Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-365
  - TC-AC-ACTS-759
  - TC-AC-ACTS-831
  - TC-AC-ACTS-848
  - TC-AC-ACTS-850
coverage:
  web: automated
---

# Konkurensi Delete: Unit Berubah Status oleh Sesi Lain (T-17, D-05, T-32), Bulk Delete Tidak Eligible (T-30), dan Bulk Delete Bersamaan dengan Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Sesi API aktor (login API password, token tidak dihitung sebagai sesi web) untuk pelaku kedua yang hanya memicu perubahan state, disediakan tim BE/FE (lihat `suite.md`).
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Pelaku kedua: sesi lain yang mengaktivasi unit (In Use), meng-Combine U1 dengan unit NFC, dan Admin 2 yang menghapus U2 memakai sesi API aktor dengan kemampuan yang disediakan tim FE/BE (aktor tidak disebut di TC; S-13).
- Pembacaan saldo Stock Ledger, Activity Log, dan modal Event Log SKU (Tab Add Stock) memakai baseline sebelum aksi (S-12).

## Test Steps

### TC-AC-ACTS-365: Unit sudah bukan Available atau Damaged/Missing saat konfirmasi (T-17)

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik (⋯) pada unit U2, lalu klik `Delete` sehingga dialog terbuka
3. Sesi API mengaktivasi unit U2 hingga status In Use tersimpan
4. Klik `[Delete]`
5. Verifikasi toast netral `This unit is no longer available.`
6. Verifikasi tabel di-refresh dan unit U2 tidak ada di Tab Available
7. Buka Tab In Use
8. Verifikasi unit U2 tetap ada di Tab In Use (tidak terhapus)
9. Tunggu toast lama hilang

### TC-AC-ACTS-759: Unit menjadi Combined setelah dialog D-05 dibuka, memunculkan dialog blok tanpa toast

10. Reset dataset: U1 sampai U4 lewat fixture BE
11. Buka Device Allocation > Stock Balance Summary Panel dan catat saldo entitas registrant (S)
12. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
13. Klik (⋯) pada U1, lalu klik `Delete` sehingga dialog `D-05` terbuka
14. Sesi API meng-Combine U1 dengan unit NFC hingga status Combined tersimpan
15. Klik `[Delete]` pada `D-05`
16. Verifikasi dialog blok `Cannot Delete Unit` (`This unit is part of a Combined TAG. Separate it first before deleting.`) tampil dengan `[OK]`
17. Verifikasi tidak ada toast tambahan
18. Klik `[OK]`
19. Verifikasi U1 tidak terhapus
20. Buka Device Allocation > Stock Balance Summary Panel dan baca saldo entitas registrant
21. Verifikasi saldo Stock Ledger tidak berubah dari S

### TC-AC-ACTS-831: Unit menjadi In Use oleh sesi lain sebelum scan, ditolak dengan toast T-32

22. Reset dataset: U1 sampai U4 lewat fixture BE
23. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
24. Klik `[Delete by Scan]`
25. Sesi API mengaktivasi U2 hingga status In Use tersimpan
26. Scan U2
27. Verifikasi toast error `Error, this TAG is currently in use and can't be deleted.`
28. Klik `[Stop]`
29. Buka Tab In Use
30. Verifikasi U2 tidak terhapus dan tetap ada di Tab In Use
31. Tunggu toast lama hilang

### TC-AC-ACTS-848: Bulk Delete, semua unit terpilih tidak lagi eligible saat commit (T-30)

32. Reset dataset: U1 sampai U4 lewat fixture BE
33. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
34. Centang U1 dan U2, pilih Bulk Action > `Delete` sehingga dialog `Delete Units` terbuka
35. Sesi API mengaktivasi U1 dan U2 hingga status In Use tersimpan
36. Klik `[Delete]`
37. Verifikasi toast error `Error, failed to delete units.`
38. Verifikasi tidak ada dialog `Delete Result`
39. Verifikasi Bulk Action Bar hilang dan seleksi di-reset
40. Buka Tab In Use
41. Verifikasi U1 dan U2 tetap ada di Tab In Use (tidak terhapus)
42. Tunggu toast lama hilang

### TC-AC-ACTS-850: Bulk Delete bersamaan dengan sesi lain yang menghapus salah satu unit

43. Reset dataset: U1 sampai U4 lewat fixture BE
44. Buka Activity Log dan modal Event Log SKU (Tab Add Stock), lalu catat baseline jumlah entri `Delete Stock` dan jumlah baris Event Log, lalu tutup modal Event Log
45. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
46. Centang U1, U2, dan U3, pilih Bulk Action > `Delete` sehingga dialog `Delete Units` terbuka
47. Sesi API (Admin 2) menghapus U2 hingga penghapusan tersimpan
48. Klik `[Delete]`
49. Verifikasi dialog `Delete Result`: `2 units have been deleted.` dan bullet `• [TAG Code U2] — No longer available`
50. Klik `[Close]`
51. Buka Activity Log (filter Object `TAG Stock`)
52. Verifikasi tepat satu entri `Delete Stock` baru untuk operasi Bulk (Field `Quantity`, Old Value `2 TAGs`, New Value `—`)
53. Buka modal Event Log SKU (Tab Add Stock)
54. Verifikasi satu baris baru Activity `Delete Stock` dengan Success `2` dan Failed `1`
55. Klik `[Detail]` pada baris `Delete Stock` terbaru
56. Verifikasi Popup Detail section `Deleted` memuat U1 dan U3
57. Verifikasi Popup Detail section `Failed` memuat U2 dengan `Status Sebelum Dihapus` `—` dan tanpa kolom `Reason`

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset", pencatatan baseline, navigasi ke Device Allocation, Activity Log, dan modal Event Log, `[OK]` dan `[Close]`, serta "Tunggu toast lama hilang" (pemulihan state, S-09). Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Identifier dan hitungan tetap (Data Uji Dinamis) dipakai ulang lintas TC dan tidak dapat bersuffix per run; kebenaran hitungan hanya terjamin bila fixture BE mereset dataset sebelum spec.
  - Aktor dan mekanisme "sesi lain mengaktivasi unit", "meng-Combine", dan "Admin 2 menghapus lewat row action" tidak didefinisikan di TC, PRD, atau LLD; spec memakai sesi API aktor dengan kemampuan yang disediakan tim FE/BE.
  - TC-AC-ACTS-365 judul menyebut T-17 dan Expected butir b menyebut "unit tidak terhapus" tanpa menyebut Tab; spec membaca Tab In Use.
  - TC-AC-ACTS-850 butir c menyebut `Status Sebelum Dihapus` `—` bagi unit yang sudah dihapus sesi lain; label kolom diasersi persis seperti TC (PRD sumber label tidak dibuka di spec).
