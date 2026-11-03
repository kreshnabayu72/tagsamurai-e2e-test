---
id: TC-AC-ACTS-E2E-145-bulk-delete-sukses-sebagian-dilewati-collapse-satu-baris-dan-distributor
title: "Bulk Delete: Seleksi Satu Baris Collapse ke Dialog Single, Sukses (T-15), Sebagian Dilewati (Delete Result), dan Distributor Menghapus Unit Sendiri"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-844
  - TC-AC-ACTS-846
  - TC-AC-ACTS-847
  - TC-AC-ACTS-852
coverage:
  web: automated
---

# Bulk Delete: Seleksi Satu Baris Collapse ke Dialog Single, Sukses (T-15), Sebagian Dilewati (Delete Result), dan Distributor Menghapus Unit Sendiri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor kedua (Ganti akun): Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Data tambahan TC-AC-ACTS-852: dua unit Available milik Distributor ini D1 dan D2 pada SKU `RFID-ASSET-CORE-R5`, di-seed fixture BE.
- Pembacaan Total Registered, saldo Stock Ledger, Activity Log, dan modal Event Log SKU memakai baseline sebelum aksi (S-12).
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.

## Test Steps

### TC-AC-ACTS-844: Bulk Delete dengan seleksi 1 baris collapse ke dialog Delete Unit single

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Centang hanya U1
3. Klik `Bulk Action` > `Delete`
4. Verifikasi dialog `Delete Unit` dengan bullet `• TAG-4F7K2XQ9`, `For more accurate results, use Delete by Scan.`, `This action cannot be undone. Are you sure you want to delete it?`, tombol `[Cancel]` dan `[Delete]`
5. Verifikasi dialog bukan `Delete Units`
6. Klik `[Cancel]`, lalu klik icon `×` pada Bulk Action Bar

### TC-AC-ACTS-847: Bulk Delete sebagian dilewati, dialog Delete Result

7. Centang U1, U2, C1, dan P1, pilih Bulk Action > `Delete`
8. Klik `[Delete]`
9. Verifikasi dialog `Delete Result` dengan `2 units have been deleted.`, `The following units were skipped:`, bullet `• [TAG Code C1] — Part of a Combined TAG` dan `• [TAG Code P1] — Referenced by a pending approval`, dan satu-satunya tombol `[Close]`
10. Klik `[Close]`
11. Verifikasi Bulk Action Bar hilang dan seleksi 0
12. Verifikasi U1 dan U2 tidak ada di tabel
13. Verifikasi C1 dan P1 tetap ada di tabel

### TC-AC-ACTS-846: Bulk Delete sukses, toast T-15, bar hilang, Total Registered dan Stock Ledger berkurang

14. Reset dataset: U1 sampai U4 lewat fixture BE
15. Buka Stock List dan catat Total Registered SKU `RFID-ASSET-CORE-R5` (N); buka Device Allocation > Stock Balance Summary Panel dan catat saldo entitas registrant (S)
16. Buka Activity Log (filter Object `TAG Stock`) dan modal Event Log SKU (Tab Add Stock), lalu catat baseline jumlah entri `Delete Stock` dan `Delete by Scan` serta jumlah baris Event Log, lalu tutup modal Event Log
17. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
18. Centang U1, U2, dan U3, pilih Bulk Action > `Delete`
19. Klik `[Delete]` pada dialog `Delete Units`
20. Verifikasi toast `Success, unit has been deleted.`
21. Verifikasi tidak ada dialog hasil
22. Verifikasi Bulk Action Bar hilang dan seleksi 0
23. Verifikasi ketiga baris tidak ada di Tab Available
24. Buka Stock List dan baca Total Registered SKU `RFID-ASSET-CORE-R5`
25. Verifikasi Total Registered sama dengan N dikurangi 3
26. Buka Device Allocation > Stock Balance Summary Panel dan baca saldo entitas registrant
27. Verifikasi saldo Stock Ledger sama dengan S dikurangi 3
28. Buka Activity Log (filter Object `TAG Stock`)
29. Verifikasi satu entri `Delete Stock` baru (Name `RFID-ASSET-CORE-R5 (RFID)`, Field `Quantity`, Old Value `3 TAGs`, New Value `—`)
30. Verifikasi jumlah entri `Delete by Scan` sama dengan baseline
31. Buka modal Event Log SKU (Tab Add Stock)
32. Verifikasi satu baris baru Activity `Delete Stock` dengan Success `3`
33. Tutup modal Event Log

### TC-AC-ACTS-852: Distributor, Bulk Delete atas unit stok sendiri berhasil

34. Ganti akun: Logout, lalu login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)
35. Buka Stock List dan catat Total Registered SKU `RFID-ASSET-CORE-R5` milik Distributor (ND)
36. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, lalu buka Tab Available
37. Centang D1 dan D2, pilih Bulk Action > `Delete`
38. Klik `[Delete]`
39. Verifikasi toast `Success, unit has been deleted.`
40. Verifikasi D1 dan D2 tidak ada di tabel
41. Buka Stock List dan baca Total Registered SKU `RFID-ASSET-CORE-R5`
42. Verifikasi Total Registered Distributor sama dengan ND dikurangi 2

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), pembatalan seleksi, "Reset dataset", pencatatan baseline dan navigasi ke Stock List, Device Allocation, Activity Log, dan modal Event Log. Urutan TC: 844, 847, 846, 852; blok yang menghapus data (847, 846, 852) di akhir, dan TC-AC-ACTS-852 terakhir karena Ganti akun. Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Identifier dan hitungan tetap (Data Uji Dinamis) dipakai ulang lintas TC dan tidak dapat bersuffix per run; kebenaran hitungan hanya terjamin bila fixture BE mereset dataset sebelum spec.
  - TC-AC-ACTS-846 Precondition "Total Registered = 10" dan Expected `7`; spec mengasersi relatif terhadap baseline (S-12).
  - TC-AC-ACTS-852 Expected "Total Registered Distributor berkurang 2" tidak menyebut permukaan baca; spec membacanya di Stock List sebagai Distributor.
  - TC-AC-ACTS-847 menyebut U1, U2 lolos tanpa U3; spec memakai U1 dan U2 sesuai TC.
