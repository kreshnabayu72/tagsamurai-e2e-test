---
id: TC-FA-FATR-BE-130-kegagalan-sistem-dep-lintas
title: "Kegagalan di dalam sistem: Save Changes gagal dan job Transaction timeout gagal"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§9.6#r5", "§9.4.4#r15", "§9.2#b60", "§9.6#r16"]
smoke: []
dependsOn:
  - "Borrow: pengajuan, Extension, dan Return"
  - "Assign: pengajuan, handover, Reassign, dan Unassign"
  - "Transfer: pengajuan, Send, dan Receive"
  - "Disposal: pengajuan, approval, dan Execute"
trace:
  "§9.6#r5": [9, 11, 13, 15, 18, 19, 20, 21, 23]
  "§9.4.4#r15": [3, 4, 7]
  "§9.2#b60": [3, 6]
  "§9.6#r16": 3
anchor: []
---

# Kegagalan di dalam sistem: Save Changes gagal dan job Transaction timeout gagal

## Prerequisites
- Aktor: Admin `Teguh Wibowo {runId}` (DU-130-2), Total Control entitas khusus, yang menyimpan setting dan mengajukan Borrow, Assign, Transfer, dan Disposal. Job Transaction timeout berjalan tanpa aktor.
- Data:
  - DU-130-1: Entitas, entitas khusus spec ini, tidak dipakai spec lain: Name `Entitas Kegagalan Sistem {runId}`; Transaction timeout `1`; Require approval Borrow, Assign, Transfer, dan Disposal `OFF`.
  - DU-130-2: User, Admin Total Control: Name `Teguh Wibowo {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-130-3: User, Employee Borrower: Name `Dewi Anggraini {runId}`; Peran `Employee aktif`; Group `Gudang Gagal {runId}`.
  - DU-130-4: User, Employee Assignee: Name `Bagus Setiawan {runId}`; Peran `Employee aktif`; Akun login `Ada`; Group `Gudang Gagal {runId}`.
  - DU-130-5: Group, Group asal aset: Name `Gudang Gagal {runId}`.
  - DU-130-6: Group, Group tujuan Transfer: Name `Gudang Tujuan Gagal {runId}`.
  - DU-130-7: Category, Category leaf target Save Changes: Name `Perkakas Gagal {runId}`; Max duration nilai sendiri `7`.
  - DU-130-8: Asset, aset pengajuan Borrow: Name `Bor Listrik Gagal {runId}`; Category `Perkakas Gagal {runId}`; Group `Gudang Gagal {runId}`; Status `Active`.
  - DU-130-9: Asset, aset pengajuan Assign: Name `Laptop Kantor Gagal {runId}`; Category `Perkakas Gagal {runId}`; Group `Gudang Gagal {runId}`; Status `Active`.
  - DU-130-10: Asset, aset pengajuan Transfer: Name `Meja Rapat Gagal {runId}`; Category `Perkakas Gagal {runId}`; Group `Gudang Gagal {runId}`; Status `Active`; Tag `Ber-tag, dapat di-scan`.
  - DU-130-11: Asset, aset pengajuan Disposal: Name `Mesin Fotokopi Gagal {runId}`; Category `Perkakas Gagal {runId}`; Group `Gudang Gagal {runId}`; Status `Active`; Tag `Ber-tag, dapat di-scan`.
  - DU-130-12 sampai DU-130-16 adalah nilai input dan record yang dibuat di langkah masing-masing, bukan record yang sudah ada: Max duration `9` pada Save Changes; pengajuan Borrow, Assign, Transfer, dan Disposal.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Kegagalan Sistem {runId}` (DU-130-1) yang tidak dipakai spec lain, karena Transaction timeout diatur `1` hari; semua data di atas berada di entitas itu.
  - Plan entitas menyediakan level Feature Suite Borrowing, Assignment, Transfer, dan Disposal `Full`.
  - Transaction timeout bernilai `1` (days) dan Require approval bernilai `OFF` di Company default untuk Borrow, Assign, Transfer, dan Disposal, tanpa override.
  - Save Changes pertama atas Category `Perkakas Gagal {runId}` gagal karena error server (5xx atau timeout); Save Changes sesudahnya berhasil.
  - Pemrosesan pertama job Transaction timeout atas baris Borrow, Assign, Transfer, dan Disposal gagal di dalam sistem; pemrosesan berikutnya berhasil.
  - Akun Admin `Teguh Wibowo {runId}` aktif dan kredensialnya disediakan fase 2.
  - Jumlah entri Changelog dan Activity Log dibaca sebagai selisih terhadap jumlah yang dicatat sebelum aksi.

## Test Steps

### Save Changes yang gagal tidak menyimpan perubahan dan tidak mencatat log
1. Catat jumlah entri Changelog dan Activity Log untuk Category `Perkakas Gagal {runId}`
2. Admin `Teguh Wibowo {runId}` menyimpan Category `Perkakas Gagal {runId}` dengan Max duration nilai sendiri `9` lewat Save Changes
3. Verifikasi Max duration Category `Perkakas Gagal {runId}` tetap `7` sebagai nilai tersimpan, karena Save Changes yang gagal tidak menyimpan perubahan
4. Verifikasi Changelog dan Activity Log untuk Category `Perkakas Gagal {runId}` tidak bertambah entri dari jumlah yang dicatat, karena Save Changes yang gagal tidak mencatat log
5. Admin mengulang Save Changes Category `Perkakas Gagal {runId}` dengan Max duration nilai sendiri `9`
6. Verifikasi Save Changes yang diulang diterima dan Max duration Category `Perkakas Gagal {runId}` menjadi `9`
7. Verifikasi Changelog dan Activity Log masing-masing bertambah satu entri dari jumlah yang dicatat, yaitu untuk perubahan Max duration pada Save Changes yang diulang

### Job Transaction timeout yang gagal tidak mengubah status transaksi
8. Admin mengajukan Borrow aset `Bor Listrik Gagal {runId}` untuk Borrower `Dewi Anggraini {runId}` dengan Duration `3 hari`
9. Verifikasi baris Borrow aset `Bor Listrik Gagal {runId}` berstatus `Waiting for Handover`, karena nilai efektif Require approval `OFF`
10. Admin mengajukan Assign aset `Laptop Kantor Gagal {runId}` kepada Assignee `Bagus Setiawan {runId}`
11. Verifikasi baris Assign aset `Laptop Kantor Gagal {runId}` berstatus `Waiting for Handover`, karena nilai efektif Require approval `OFF`
12. Admin mengajukan Transfer aset `Meja Rapat Gagal {runId}` ke Group `Gudang Tujuan Gagal {runId}`
13. Verifikasi baris Transfer aset `Meja Rapat Gagal {runId}` berstatus `Waiting for Send`, karena nilai efektif Require approval `OFF`
14. Admin mengajukan Disposal jenis `Scrap` atas aset `Mesin Fotokopi Gagal {runId}` dengan scan tag aset dan Reason `Aset rusak berat`
15. Verifikasi baris Disposal aset `Mesin Fotokopi Gagal {runId}` berstatus `Waiting for Execution`, karena nilai efektif Require approval `OFF`
16. Waktu berlalu sampai 25 jam sejak keempat baris masuk status menunggunya, sehingga batas Transaction timeout `1` hari terlampaui
17. Job Transaction timeout berjalan
18. Verifikasi baris Borrow aset `Bor Listrik Gagal {runId}` tetap berstatus `Waiting for Handover`, karena job yang gagal tidak mengubah status transaksi
19. Verifikasi baris Assign aset `Laptop Kantor Gagal {runId}` tetap berstatus `Waiting for Handover`, karena job yang gagal tidak mengubah status transaksi
20. Verifikasi baris Transfer aset `Meja Rapat Gagal {runId}` tetap berstatus `Waiting for Send`, karena job yang gagal tidak mengubah status transaksi
21. Verifikasi baris Disposal aset `Mesin Fotokopi Gagal {runId}` tetap berstatus `Waiting for Execution`, karena job yang gagal tidak mengubah status transaksi
22. Job Transaction timeout berjalan lagi
23. Verifikasi baris Borrow, Assign, Transfer, dan Disposal pada langkah 8 sampai 15 kini berstatus `Canceled`, sehingga status yang tidak berubah sebelumnya disebabkan job yang gagal, bukan batas yang belum terlampaui
