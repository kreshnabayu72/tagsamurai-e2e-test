---
id: TC-FA-FAREG-BE-131-delete-draft
title: "Delete dan Bulk Delete draft"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [FAREG-LOGIC-10c, FAREG-LOGIC-10d, FAREG-LOGIC-10e, "§9.4.2#r24", "§9.4.3#b4", "§9.6#r6", "§9.6#r7", EB-ERR-3]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-10c: [2, 3]
  FAREG-LOGIC-10d: [5]
  FAREG-LOGIC-10e: [20, 23, 24, 28, 29, 30, 32]
  "§9.4.2#r24": [10, 17]
  "§9.4.3#b4": [2, 3]
  "§9.6#r6": [7, 8, 10, 12, 13, 15, 20, 21, 36]
  "§9.6#r7": [26, 27, 28, 29, 30, 32, 34, 35, 37]
  EB-ERR-3: [10, 17, 20, 21]
owner: BE
---
# Delete dan Bulk Delete draft

## Prerequisites
- Aktor: Rina (Manage asset & TAG, Group terkelola `Gudang Kediri {runId}`, pembuat dan Owner batch Draft di bawah); Budi (Manage asset & TAG, Group terkelola `Gudang Kediri {runId}`, tampil `Budi S`); Dewi (Manage purchase, cakupan `Gudang Kediri {runId}`).
- Data:
  - DU-131-1: Group `Gudang Kediri {runId}`, Assignable, di entitas aktor.
  - DU-131-2: Group `Gudang Madiun {runId}`, Assignable, di entitas aktor, di luar Group terkelola Rina.
  - DU-131-3: Asset Name `Laptop {runId}`, Category `IT Equipment`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`.
  - DU-131-4: Asset Name `Meja Kerja {runId}`, Category `Furnitur`, Brand `Olympic`, Model `OL-131`, TAG Type `Non-TAG`.
  - DU-131-5: Tag RFID `E280-1310-0001 {runId}`, status `Reserved` oleh batch DU-131-10.
  - DU-131-6: Tag RFID `E280-1310-0002 {runId}`, status `Reserved` oleh batch DU-131-13.
  - DU-131-7: Tag RFID `E280-1310-0003 {runId}`, status `Reserved` oleh batch DU-131-15.
  - DU-131-8: batch Draft milik Rina, Group `Gudang Kediri {runId}`, dua aset `Meja Kerja {runId}`, terakhir diubah `T0 − 400 hari`.
  - DU-131-9: batch milik Rina, Group `Gudang Kediri {runId}`, satu aset `Meja Kerja {runId}`, berstatus Waiting for Approval dengan Registration ID `REG-20261105-01310`.
  - DU-131-10: batch Draft milik Rina, Group `Gudang Kediri {runId}`, satu aset `Laptop {runId}` dengan Tag RFID `E280-1310-0001 {runId}` dan satu berkas Photo.
  - DU-131-11: batch Draft milik Rina, Group `Gudang Kediri {runId}`, satu aset `Meja Kerja {runId}`; Asset Code asetnya sudah dialokasikan dan Origin batch ini (Registration ID pengajuan asal) adalah milik DU-131-11, dibentuk server pada Submit pengajuan asal (kembalian dari pengajuan yang dibatalkan).
  - DU-131-12: batch Draft milik Rina, Group `Gudang Kediri {runId}`, satu aset `Meja Kerja {runId}`.
  - DU-131-13: batch Draft milik Rina, Group `Gudang Kediri {runId}`, satu aset `Laptop {runId}` dengan Tag RFID `E280-1310-0002 {runId}`.
  - DU-131-14: batch Draft milik Rina, Group `Gudang Kediri {runId}`, satu aset `Meja Kerja {runId}`.
  - DU-131-15: batch Draft milik Rina, Group `Gudang Kediri {runId}`, satu aset `Laptop {runId}` dengan Tag RFID `E280-1310-0003 {runId}` dan satu berkas Photo.
  - DU-131-16: batch Draft milik Rina, Group `Gudang Kediri {runId}`, satu aset `Meja Kerja {runId}`.
  - DU-131-17: batch Draft milik Agus Pratama, Group `Gudang Madiun {runId}`, satu aset `Meja Kerja {runId}`.
  - DU-131-18: batch Draft kembalian milik Rina, Group `Gudang Kediri {runId}`, satu aset `Meja Kerja {runId}`; Asset Code asetnya sudah dialokasikan dan Origin batch ini (Registration ID pengajuan asal) adalah milik DU-131-18, dibentuk server pada Submit pengajuan asal.
  - DU-131-19: batch Draft milik Rina, Group `Gudang Kediri {runId}`, satu aset `Meja Kerja {runId}`.
- Kondisi:
  - Tidak ada pekerjaan terjadwal lain yang mengubah batch Draft selama spec berjalan.

## Test Steps

### Draft tidak punya batas umur dan tidak dihapus otomatis
1. Rina memuat daftar batch Draft di Group `Gudang Kediri {runId}`
2. Verifikasi batch DU-131-8 yang terakhir diubah `T0 − 400 hari` masih tampil di daftar Draft dengan Total Asset `2`
3. Verifikasi kedua aset batch DU-131-8 masih berstatus Draft dan tidak dihapus sistem

### Delete hanya untuk Draft
4. Rina mengirim Delete atas batch DU-131-9 yang berstatus Waiting for Approval
5. Verifikasi Delete ditolak server dan batch DU-131-9 tetap berstatus Waiting for Approval dengan satu aset

### Delete satu batch Draft melepas Tag dan ulangannya tidak mengubah apa pun
6. Rina mengirim Delete atas batch DU-131-10
7. Verifikasi Delete berhasil dan batch DU-131-10 tidak lagi tampil di daftar Draft
8. Verifikasi Tag `E280-1310-0001 {runId}` kembali berstatus `Available`
9. Rina mengirim Delete atas batch DU-131-10 yang sama sekali lagi
10. Verifikasi Delete ditolak server dengan pesan `This draft is no longer available.` tanpa mutasi

### Delete batch kembalian meng-Voided Asset Code yang sudah dialokasikan
11. Rina mengirim Delete atas batch DU-131-11
12. Verifikasi Delete berhasil dan batch DU-131-11 tidak lagi tampil di daftar Draft
13. Verifikasi Asset Code aset batch DU-131-11 berstatus `Voided`

### Draft yang sudah dihapus pihak lain
14. Budi mengirim Delete atas batch DU-131-12
15. Verifikasi Delete oleh Budi berhasil dan batch DU-131-12 tidak lagi tampil di daftar Draft
16. Rina mengirim Delete atas batch DU-131-12 yang sudah dihapus Budi
17. Verifikasi Delete ditolak server dengan pesan `This draft is no longer available.` tanpa mutasi

### Delete batch yang kuncinya dipegang user lain
18. Budi membuka batch DU-131-13 dalam mode Edit sehingga memegang kunci sesinya
19. Rina mengirim Delete atas batch DU-131-13
20. Verifikasi Delete ditolak server dengan pesan `Budi S is editing this draft. It can't be deleted right now.`
21. Verifikasi batch DU-131-13 tetap Draft, Tag `E280-1310-0002 {runId}` tetap `Reserved`, dan kunci sesi tetap dipegang Budi

### Delete oleh user tanpa hak
22. Dewi mengirim Delete atas batch DU-131-14
23. Verifikasi Delete ditolak server dengan pesan `You don't have permission to do this.`
24. Verifikasi batch DU-131-14 tetap Draft tanpa perubahan

### Bulk Delete memproses tiap batch dan melewati yang tidak dapat dihapus
25. Rina mengirim Bulk Delete atas lima batch: DU-131-15, DU-131-16, DU-131-12 (sudah dihapus Budi), DU-131-13 (kuncinya dipegang Budi), dan DU-131-17 (di Group `Gudang Madiun {runId}`)
26. Verifikasi batch DU-131-15 dan DU-131-16 terhapus dan tidak lagi tampil di daftar Draft
27. Verifikasi Tag `E280-1310-0003 {runId}` kembali berstatus `Available`
28. Verifikasi batch DU-131-12 dilewati tanpa kesalahan dan tanpa mutasi
29. Verifikasi batch DU-131-13 dilewati dan tetap Draft dengan kunci sesi tetap dipegang Budi
30. Verifikasi batch DU-131-17 dilewati karena Rina tanpa hak atas `Gudang Madiun {runId}` dan batch tetap Draft
31. Rina mengirim Bulk Delete yang sama sekali lagi
32. Verifikasi seluruh lima batch dilewati: batch DU-131-13 dan DU-131-17 tetap Draft dan tidak ada batch lain yang terhapus

### Bulk Delete meng-Voided Asset Code yang sudah dialokasikan
33. Rina mengirim Bulk Delete atas dua batch: DU-131-18 dan DU-131-19
34. Verifikasi batch DU-131-18 dan DU-131-19 terhapus dan tidak lagi tampil di daftar Draft
35. Verifikasi Asset Code aset batch DU-131-18 berstatus `Voided`

### Berkas Photo aset yang dihapus ikut terhapus
36. Verifikasi berkas Photo aset batch DU-131-10 yang dihapus pada langkah 6 tidak lagi tersedia
37. Verifikasi berkas Photo aset batch DU-131-15 yang dihapus pada langkah 25 tidak lagi tersedia
