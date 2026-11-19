---
id: TC-FA-ASTL-E2E-046-operasi-tag-dep-tag
title: "Operasi TAG tercermin di daftar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-16c", "ASTL-LOGIC-17x", "§9.4.3#p2", "§9.7#r5"]
smoke: []
dependsOn: ["TAG: operasi TAG"]
trace:
  "ASTL-LOGIC-16c": [4, 19]
  "ASTL-LOGIC-17x": 25
  "§9.4.3#p2": 16
  "§9.7#r5": [8, 10, 12]
anchor: [3, 7, 14]
coverage:
  web: automated
---

# Operasi TAG tercermin di daftar

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-046-1: aset `Mobil Operasional {runId} - 1`, Group `Cabang Surabaya {runId}`, Unmanaged, Custody `Available`, TAG `QR` berstatus Paired.
  - DU-046-2: aset `Genset 20kVA {runId} - 1`, Group `Cabang Medan {runId}`, Unmanaged, Custody `Available`, TAG `RFID` berstatus Paired, tanpa penyusutan atau jurnal Posted dan tanpa Disposal.
  - DU-046-3: aset `Server Rack {runId} - 1`, Group `IT {runId}`, managed, belum dipasangi TAG sehingga Status `Not Paired Yet`.
  - DU-046-5: aset `Laptop Pro 16 {runId} - 1`, Group `IT {runId}`, managed, hanya punya satu TAG `RFID` yang merupakan TAG Type wajib.

## Test Steps

### TAG Paired pada aset Unmanaged tetap terpasang
1. Ketik Search `Mobil Operasional {runId}`, tekan Enter
2. Buka menu `⋯` baris `Mobil Operasional {runId} - 1`
3. Verifikasi menu aksi baris `Mobil Operasional {runId} - 1` memuat `Detail`
4. Verifikasi menu aksi baris tidak menawarkan `Replace TAG` maupun `Report TAG`, dan kolom TAG baris tersebut tetap menampilkan ikon `QR`
5. Tutup menu aksi baris

### Operasi TAG tercermin di kolom TAG, Status, dan kartu Issues
6. Ketik Search `Server Rack {runId}`, tekan Enter
7. Verifikasi baris `Server Rack {runId} - 1` menampilkan `Not Paired Yet` dan kolom TAG bernilai `—`
8. Verifikasi angka kartu `Issues` menjadi `1` untuk `Server Rack {runId} - 1` karena Search hanya memuat aset itu
9. Pada modul TAG, Hendra Saputra memasangkan TAG `QR` pada aset `Server Rack {runId} - 1`, tanpa memuat ulang halaman Fixed Asset > Assets
10. Verifikasi kolom TAG baris `Server Rack {runId} - 1` menampilkan ikon `QR`, `Not Paired Yet` tidak lagi tampil, dan angka kartu `Issues` menjadi `0`
11. Pada modul TAG, Hendra Saputra melaporkan TAG aset `Server Rack {runId} - 1`, tanpa memuat ulang halaman Fixed Asset > Assets
12. Verifikasi badge Status baris `Server Rack {runId} - 1` berubah menjadi `TAG Reported` dan angka kartu `Issues` menjadi `1`

### TAG tunggal bertipe wajib tidak bisa dilepas
13. Ketik Search `Laptop Pro 16 {runId}`, tekan Enter
14. Verifikasi baris `Laptop Pro 16 {runId} - 1` menampilkan `Available` dan ikon TAG `RFID`
15. Pada modul TAG, Hendra Saputra mencoba melepas satu-satunya TAG `RFID` dari aset `Laptop Pro 16 {runId} - 1`, tanpa memuat ulang halaman Fixed Asset > Assets
16. Verifikasi kolom TAG baris `Laptop Pro 16 {runId} - 1` tetap menampilkan ikon `RFID` dan `Not Paired Yet` tidak tampil

### Delete Asset Data mengembalikan TAG lewat To Be Returned
17. Kosongkan kolom Search
18. Ketik Search `Genset 20kVA {runId}`, tekan Enter
19. Verifikasi kolom TAG baris `Genset 20kVA {runId} - 1` (Unmanaged) tetap menampilkan ikon `RFID` karena TAG yang Paired tetap terpasang sampai aset dihapus
20. Buka menu `⋯` baris `Genset 20kVA {runId} - 1`
21. Klik `Delete Asset Data`
22. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
23. Klik `[Delete]`
24. Buka tab `To Be Returned` pada modul TAG
25. Verifikasi tab `To Be Returned` memuat TAG `RFID` milik DU-046-2 dengan alasan `Deleted`
