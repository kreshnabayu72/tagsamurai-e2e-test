---
id: TC-FA-FATR-BE-112-aturan-activity-log-dep-activity-log
title: "Entri Activity Log dari Settings dan override"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
owner: BE
sourceRules: ["§8.1#r6", "§8.2#p1", "§8.2#p2", "§9.2#b247", "§9.2#b372", "§9.2#b377", "§9.4.4#r26", "§9.4.4#r30", "§9.4.4#r45", "§9.6#r1", "§9.6#r2", "§9.6#r3", "§9.6#r4", "§9.6#r21", "§9.7#r3", "§9.7#r10", "§9.7#r19", "§9.8#r15", "§9.8#r16", "§9.8#r18", "§11#r11"]
smoke: []
dependsOn: ["Activity Log: daftar entri"]
trace:
  "§8.2#p1": [3, 4, 5, 7, 10, 16, 24, 26]
  "§9.7#r10": 3
  "§11#r11": 3
  "§9.8#r15": [12, 13]
  "§9.6#r1": [12, 13]
  "§8.1#r6": [16, 30]
  "§9.6#r2": [16, 18]
  "§9.7#r3": 16
  "§9.4.4#r30": [16, 20]
  "§9.6#r21": 18
  "§9.2#b377": [21, 26, 30, 31]
  "§9.4.4#r45": [21, 31]
  "§9.8#r16": [21, 26, 31]
  "§9.7#r19": [26, 30]
  "§9.6#r3": [26, 28]
  "§9.4.4#r26": 30
  "§9.6#r4": [33, 35, 37]
  "§9.8#r18": [33, 35]
  "§9.2#b372": [33, 35, 37]
  "§9.2#b247": 39
  "§8.2#p2": [40, 42]
---

# Entri Activity Log dari Settings dan override

## Prerequisites
- Aktor: Total Control, `Dewi Lestari {runId}`, berwenang atas seluruh entitas. Pengaju peminjaman: `Bagus Prasetyo {runId}`.
- Data:
  - DU-112-1: user `Dewi Lestari {runId}`, role Total Control, cakupan seluruh entitas.
  - DU-112-2: Category `Peralatan Lab {runId} > Mikroskop {runId}`, Max duration Inherit, Max assets per borrower Inherit.
  - DU-112-3: Group `Divisi Riset {runId}`, tanpa Role Transaksi `Approver` yang ditugaskan.
  - DU-112-4: Group `Divisi Produksi {runId}`.
  - DU-112-5: Group `Divisi Mutu {runId}`.
  - DU-112-6: aset `Autoklaf Mini {runId}`, peminjaman berstatus Waiting for Handover sejak `T0 − 30 hari`; batas Transaction timeout `7` (days) sudah terlewati dan belum diproses job.
  - DU-112-7: aset `Sentrifus Meja {runId}`, di Category `Peralatan Lab {runId} > Mikroskop {runId}` dan Group `Divisi Riset {runId}`, tersedia untuk dipinjam.
  - DU-112-8: Max duration bernilai `7`.
  - DU-112-9: Max assets per borrower bernilai `3`.
  - DU-112-10: override Max duration bernilai `5`.
  - DU-112-11: Group `Divisi Gudang {runId}`.
  - DU-112-12: override dua field untuk target `Divisi Gudang {runId}`: Max duration bernilai `4` dan Max assets per borrower bernilai `2`.
  - DU-112-13: user `Bagus Prasetyo {runId}`, pengaju peminjaman, bukan Total Control dan bukan Group Manager yang menaungi Group `Divisi Riset {runId}`.
- Kondisi:
  - Approval Workflow tersedia pada paket entitas.
  - Require approval bernilai `ON` untuk transaksi pinjam di Company default, dan Inherit pada Category `Peralatan Lab {runId} > Mikroskop {runId}`.
  - Level Feature Suite Borrowing bernilai `Full`.
  - Transaction timeout bernilai `7` (days).

## Test Steps

### Save Changes menulis satu entri Activity Log per field yang berubah
1. Catat jumlah entri Activity Log dan Changelog untuk Category `Peralatan Lab {runId} > Mikroskop {runId}`
2. Total Control menyimpan Max duration bernilai `7` dan Max assets per borrower bernilai `3` pada tab Borrow Category `Peralatan Lab {runId} > Mikroskop {runId}`, keduanya sebelumnya Inherit
3. Verifikasi Activity Log bertambah dua entri berformat `[Name] changed [Field] of [Transaction] for [Category] from [Old] to [New]`, satu per field yang berubah, dengan [Name] `Dewi Lestari {runId}`
4. Verifikasi entri untuk field `Max duration` ditulis `from Inherit` dengan nilai baru `7`
5. Verifikasi Changelog bertambah dua entri, sejajar dengan Activity Log
6. Total Control menyimpan Max duration kembali ke Inherit pada tab Borrow Category `Peralatan Lab {runId} > Mikroskop {runId}`
7. Verifikasi entri baru untuk field `Max duration` ditulis `to Inherit`
8. Total Control mengklik Reset to Default pada tab Borrow Category `Peralatan Lab {runId} > Mikroskop {runId}`
9. Total Control menyimpan hasil Reset to Default
10. Verifikasi Reset to Default yang disimpan dicatat sebagai satu entri perubahan field biasa untuk field `Max assets per borrower`
11. Total Control menyimpan tab Borrow Category `Peralatan Lab {runId} > Mikroskop {runId}` tanpa mengubah nilai apa pun
12. Verifikasi Save tanpa selisih tidak menambah entri Activity Log
13. Verifikasi Save tanpa selisih tidak menambah entri Changelog

### Add override menulis satu entri Activity Log per override
14. Catat jumlah entri Activity Log dan Changelog untuk Category `Peralatan Lab {runId} > Mikroskop {runId}`
15. Total Control menambah override pada transaksi pinjam Category `Peralatan Lab {runId} > Mikroskop {runId}` dengan target `Divisi Riset {runId}` dan `Divisi Produksi {runId}`, field `Max duration` bernilai `5`, dalam satu Submit
16. Verifikasi Activity Log bertambah dua entri berformat `[Name] added an override on [Transaction] for [Target] in [Category]`, satu per target, masing-masing memuat field `Max duration` dan nilai `5`
17. Total Control menambah override pada transaksi pinjam Category `Peralatan Lab {runId} > Mikroskop {runId}` dengan target `Divisi Mutu {runId}`, field `Max duration` bernilai `5`, dalam Submit kedua
18. Verifikasi Submit kedua menambah satu entri Activity Log lagi untuk target `Divisi Mutu {runId}`
19. Total Control menambah override duplikat pada transaksi pinjam Category `Peralatan Lab {runId} > Mikroskop {runId}` dengan target `Divisi Riset {runId}`, field `Max duration` bernilai `5`
20. Verifikasi Submit duplikat ditolak dan tidak menambah entri Activity Log
21. Verifikasi Add override tidak menambah entri Changelog

### Add override dengan lebih dari satu field menulis satu entri yang memuat semua pasangan field
22. Catat jumlah entri Activity Log untuk Category `Peralatan Lab {runId} > Mikroskop {runId}`
23. Total Control menambah override pada transaksi pinjam Category `Peralatan Lab {runId} > Mikroskop {runId}` dengan target `Divisi Gudang {runId}`, field `Max duration` bernilai `4` dan field `Max assets per borrower` bernilai `2`, dalam satu Submit
24. Verifikasi Activity Log bertambah satu entri berformat `[Name] added an override on [Transaction] for [Target] in [Category]: [field] ([value]), ...` untuk target `Divisi Gudang {runId}` yang memuat pasangan `Max duration` (`4`) dan `Max assets per borrower` (`2`)

### Delete override menulis satu entri Activity Log per override yang terhapus
25. Total Control menghapus override target `Divisi Riset {runId}` pada transaksi pinjam Category `Peralatan Lab {runId} > Mikroskop {runId}`
26. Verifikasi Activity Log bertambah satu entri berformat `[Name] deleted an override on [Transaction] for [Target] in [Category]` untuk target `Divisi Riset {runId}`
27. Total Control mengirim ulang Delete untuk override target `Divisi Riset {runId}` yang sudah terhapus
28. Verifikasi pengulangan Delete pada override yang sudah terhapus tidak menambah entri Activity Log
29. Total Control menjalankan Bulk Delete untuk override target `Divisi Produksi {runId}` dan `Divisi Mutu {runId}` pada transaksi pinjam Category `Peralatan Lab {runId} > Mikroskop {runId}`
30. Verifikasi Bulk Delete menambah dua entri Activity Log, satu per override (per target)
31. Verifikasi Delete override tidak menambah entri Changelog

### Export rules menulis satu entri Activity Log per export
32. Total Control mengekspor rules untuk Category `Peralatan Lab {runId} > Mikroskop {runId}`
33. Verifikasi Activity Log bertambah satu entri berformat `[Name] exported transaction rules for [Category]` dengan [Category] berisi full path `Peralatan Lab {runId} > Mikroskop {runId}`
34. Total Control mengekspor rules untuk All categories
35. Verifikasi Activity Log bertambah satu entri berformat `[Name] exported transaction rules for [Category]` dengan [Category] `All categories`
36. Total Control mengekspor rules untuk All categories sekali lagi
37. Verifikasi export kedua untuk All categories menambah satu entri lagi, sehingga tiap export menambah satu entri

### Aksi sistem dicatat dengan Modified By System tanpa System Log
38. Job Transaction timeout berjalan atas peminjaman aset `Autoklaf Mini {runId}`
39. Verifikasi log aset `Autoklaf Mini {runId}` memuat node `Returned to Draft` yang dicatat oleh `System`
40. Verifikasi transaksi yang ditutup timeout itu dicatat dengan Modified By `System` dan tanpa entri System Log
41. `Bagus Prasetyo {runId}` mengajukan peminjaman aset `Sentrifus Meja {runId}` di Category `Peralatan Lab {runId} > Mikroskop {runId}` dan Group `Divisi Riset {runId}` yang tidak punya Approver, sehingga rute approval jatuh ke Group Manager atau Total Control
42. Verifikasi rute approval yang jatuh ke Group Manager atau Total Control dicatat dengan Modified By `System` dan tanpa entri System Log
