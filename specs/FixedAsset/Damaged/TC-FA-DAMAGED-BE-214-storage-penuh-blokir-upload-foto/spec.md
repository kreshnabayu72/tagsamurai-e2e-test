---
id: TC-FA-DAMAGED-BE-214-storage-penuh-blokir-upload-foto
title: "Saat Storage client penuh server menolak Report Damaged dengan Damaged Photo baru dan Mark as Repaired dengan After photo baru sebelum transaksi, tanpa record, node, atau perubahan status; laporan banyak aset ditolak seluruhnya, client tanpa kuota tidak diblokir, dan Mark as Repaired tanpa After photo tidak dicek Storage, dan ditolak saat After photo required ON (V-DMG-15)"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r93", "§Aturan Logika Modul#r94", "§Aturan Logika Modul#r95", V-DMG-20, EC-DMG-38, EC-DMG-39, "§4.2.3#b1", "§4.2.4#p3", "§9.2#b9", "§9.2#b18", "§9.4.4#r10", "§9.4.4#r27", "§9.6#r5", "§9.10#p1", "§9.4.1#r2", "§9.6#r1", "§9.9#p4", FLD-DMG-04]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r93": [2, 6, 10, 15, 18, 21, 23, 28, 37, 40, 46]
  "§Aturan Logika Modul#r94": [2, 23, 24, 32]
  "§Aturan Logika Modul#r95": [3, 4, 7, 8, 11, 12, 25, 26, 29, 30, 41, 47]
  V-DMG-20: [2, 6, 10, 15, 23, 28, 40, 46]
  EC-DMG-38: [2, 3, 4, 6, 7, 8, 10, 11, 12, 15, 18, 19, 21, 40, 41, 46, 47]
  EC-DMG-39: [23, 24, 25, 26, 28, 29, 30, 32, 35]
  "§4.2.3#b1": [3, 7]
  "§4.2.4#p3": [25, 29]
  "§9.2#b9": [2, 18, 43]
  "§9.2#b18": [23, 25, 26, 28, 29, 30]
  "§9.4.4#r10": [2, 3, 4, 6, 7, 10, 11, 12, 15, 41]
  "§9.4.4#r27": [23, 25, 26, 28, 29, 30]
  "§9.10#p1": [2, 23, 28]
  "§9.4.1#r2": [2, 3, 23, 25, 28, 29]
  "§9.6#r1": [2, 6, 7, 10, 40]
  "§9.6#r5": [23, 25, 28, 29]
  "§9.9#p4": [18, 43]
  FLD-DMG-04: [50, 51]
---

# Saat Storage client penuh server menolak Report Damaged dengan Damaged Photo baru dan Mark as Repaired dengan After photo baru sebelum transaksi, tanpa record, node, atau perubahan status; laporan banyak aset ditolak seluruhnya, client tanpa kuota tidak diblokir, dan Mark as Repaired tanpa After photo tidak dicek Storage, dan ditolak saat After photo required ON (V-DMG-15)

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged, pada Client `Client Storage Penuh {runId}`.
  - Pelapor umum `Budi Santoso {runId}`, pemegang aset, tanpa role Damaged, pada Client `Client Storage Penuh {runId}`.
  - Total Control `Citra Lestari {runId}`, Aktor Damaged, pada Client `Client Tanpa Kuota {runId}`.
  - Aktor peminjaman `Yoga Tanuwijaya {runId}`, pada Client `Client Storage Penuh {runId}`.
- Data:
  - DU-214-1: Client `Client Storage Penuh {runId}` dengan kuota Storage `50.0 GB` dan usage ledger `50.0 GB`.
  - DU-214-2: Client `Client Tanpa Kuota {runId}` tanpa baris ledger Storage (dianggap berkuota 0).
  - DU-214-3: Aset `Laptop Dell Latitude 5420 - 31 {runId}`, Group `Head Office {runId}`, TAG `RFID-L31 {runId}`, status global `Normal`, tanpa record Damage.
  - DU-214-4: Aset `Laptop Dell Latitude 5420 - 32 {runId}`, Group `Head Office {runId}`, status global `Normal`, tanpa record Damage.
  - DU-214-5: Aset `Laptop Dell Latitude 5420 - 33 {runId}`, Group `Head Office {runId}`, status global `Normal`, tanpa record Damage.
  - DU-214-6: Aset `Monitor Dell P2422H - 31 {runId}`, Group `Head Office {runId}`, dipegang `Budi Santoso {runId}`, status global `Assigned`, tanpa record Damage.
  - DU-214-7: Aset `Printer HP LaserJet M404 - 31 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged`.
  - DU-214-8: Aset `Printer HP LaserJet M404 - 32 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged`.
  - DU-214-9: Aset `Printer HP LaserJet M404 - 33 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged`.
  - DU-214-10: Aset `Printer HP LaserJet M404 - 34 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged`.
  - DU-214-11: Aset `Kamera Canon EOS - 31 {runId}`, Group `Head Office` pada Client `Client Tanpa Kuota {runId}`, status global `Normal`, tanpa record Damage.
  - DU-214-12: What happened `Layar retak dan perangkat tidak menyala`.
  - DU-214-13: Damaged Photo baru `kerusakan-be-{runId}.jpeg` (JPEG, di bawah 1 MB).
  - DU-214-14: Berkas `catatan-servis.pdf` sebagai berkas berformat tidak valid.
  - DU-214-15: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-214-16: After photo baru `perbaikan-be-{runId}.jpeg` (JPEG, di bawah 1 MB).
  - DU-214-17: Aset `Laptop Dell Latitude 5420 - 34 {runId}`, Group `Head Office {runId}`, status global `Normal`, tanpa record Damage.
  - DU-214-18: Aset `Laptop Dell Latitude 5420 - 35 {runId}`, Group `Head Office {runId}`, status global `Normal`, tanpa record Damage.
  - DU-214-19: Aset `Tablet Samsung Tab A8 - 31 {runId}`, Group `Head Office {runId}`, status global `Borrowed` oleh `Budi Santoso {runId}`, tanpa record Damage.
  - DU-214-20: User `Yoga Tanuwijaya {runId}`, Aktor Borrow, cakupan Group `Head Office {runId}`, pada Client `Client Storage Penuh {runId}`.
  - DU-214-21: Description `Engsel longgar saat dikembalikan {runId}`, foto Return baru `foto-return-be-{runId}.jpeg` (JPEG, di bawah 1 MB).
  - DU-214-22: Usage ledger `Client Storage Penuh {runId}` `51.2 GB` dengan kuota `50.0 GB`, melebihi batas.
  - DU-214-23: Kuota `Client Storage Penuh {runId}` ditambah menjadi `100.0 GB` dengan usage ledger `50.0 GB`, di bawah batas.
  - DU-214-25: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang, pada Client `Client Storage Penuh {runId}`.
  - DU-214-24: Kuota `Client Storage Penuh {runId}` diturunkan menjadi `40.0 GB` dengan usage ledger `50.0 GB`.
  - DU-214-26: Aset `Printer HP LaserJet M404 - 35 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged`.
- Kondisi:
  - Memakai entitas khusus yang tidak dipakai spec lain: Client `Client Storage Penuh {runId}` dan Client `Client Tanpa Kuota {runId}`.
  - Storage `Client Storage Penuh {runId}` penuh sesuai DU-214-1 kecuali disebut lain pada langkah.
  - After photo required diatur sesuai yang disebut pada subjudul tiap blok.

## Test Steps

### Report Damaged satu aset dengan Damaged Photo baru ditolak saat Storage penuh
1. Total Control `Agus Pratama {runId}` menjalankan Report Damaged atas `Laptop Dell Latitude 5420 - 31 {runId}` dengan What happened `Layar retak dan perangkat tidak menyala` dan Damaged Photo baru `kerusakan-be-{runId}.jpeg`
2. Verifikasi permintaan ditolak karena Storage penuh, walau Damaged Photo wajib untuk laporan itu
3. Verifikasi tidak ada record Damage baru untuk `Laptop Dell Latitude 5420 - 31 {runId}` dan status global aset tetap `Normal`
4. Verifikasi tidak ada node Damage Log, tidak ada entri Transaction log aset, dan tidak ada event `damaged_reported` yang tercipta

### Laporan dua aset atau lebih ditolak seluruhnya, bukan per aset
5. Total Control `Agus Pratama {runId}` menjalankan Report Damaged atas `Laptop Dell Latitude 5420 - 32 {runId}` dan `Laptop Dell Latitude 5420 - 33 {runId}` dengan What happened `Layar retak dan perangkat tidak menyala` dan Damaged Photo baru `kerusakan-be-{runId}.jpeg` untuk masing-masing aset
6. Verifikasi seluruh permintaan ditolak karena Storage penuh
7. Verifikasi tidak ada aset yang dilaporkan sebagian: `Laptop Dell Latitude 5420 - 32 {runId}` dan `Laptop Dell Latitude 5420 - 33 {runId}` sama-sama tanpa record Damage dan berstatus global `Normal`
8. Verifikasi penolakan itu berbeda dari aset tidak layak yang dilewati: tidak ada aset yang diproses dan tidak ada keterangan aset dilewati

### Laporan pelapor umum ditolak saat Storage penuh
9. Pelapor umum `Budi Santoso {runId}` menjalankan Report Damaged atas `Monitor Dell P2422H - 31 {runId}` yang ia pegang dengan What happened `Layar retak dan perangkat tidak menyala` dan Damaged Photo baru `kerusakan-be-{runId}.jpeg`
10. Verifikasi permintaan ditolak karena Storage penuh
11. Verifikasi tidak ada record Damage `Waiting for Confirmation` untuk `Monitor Dell P2422H - 31 {runId}` dan status global aset tetap `Assigned` tanpa penanda `Damage reported`
12. Verifikasi tidak ada event `damaged_review_requested` yang tercipta

### Usage melebihi kuota juga ditolak
13. Usage ledger `Client Storage Penuh {runId}` diatur `51.2 GB` dengan kuota `50.0 GB`
14. Total Control `Agus Pratama {runId}` menjalankan Report Damaged atas `Laptop Dell Latitude 5420 - 31 {runId}` dengan What happened `Layar retak dan perangkat tidak menyala` dan Damaged Photo baru `kerusakan-be-{runId}.jpeg`
15. Verifikasi permintaan ditolak karena Storage penuh dan nilai terpakai yang dilaporkan `51.2 GB` dibanding kuota `50.0 GB`
16. Usage ledger dikembalikan ke `50.0 GB`

### Format file ditolak didahulukan atas Storage penuh
17. Total Control `Agus Pratama {runId}` menjalankan Report Damaged atas `Laptop Dell Latitude 5420 - 31 {runId}` dengan What happened `Layar retak dan perangkat tidak menyala` dan berkas `catatan-servis.pdf` sebagai Damaged Photo
18. Verifikasi permintaan ditolak karena format berkas tidak valid, bukan karena Storage penuh
19. Verifikasi tidak ada record Damage baru untuk `Laptop Dell Latitude 5420 - 31 {runId}`

### Client tanpa baris ledger Storage dianggap berkuota 0 dan upload baru ditolak
20. Total Control `Citra Lestari {runId}` pada Client `Client Tanpa Kuota {runId}` menjalankan Report Damaged atas `Kamera Canon EOS - 31 {runId}` dengan What happened `Layar retak dan perangkat tidak menyala` dan Damaged Photo baru `kerusakan-be-{runId}.jpeg`
21. Verifikasi permintaan ditolak karena client tanpa baris ledger Storage dianggap berkuota 0 sehingga diperlakukan sama seperti Storage penuh, tidak ada record `Damaged` untuk `Kamera Canon EOS - 31 {runId}`, dan status global aset tetap `Normal`

### Mark as Repaired dengan After photo wajib (setting ON) ditolak saat Storage penuh
22. Dengan After photo required `ON`, Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 31 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}` dan After photo baru `perbaikan-be-{runId}.jpeg`
23. Verifikasi permintaan ditolak karena Storage penuh
24. Verifikasi pemblokiran itu berlaku karena After photo wajib tidak dikecualikan dari Storage penuh
25. Verifikasi record `Printer HP LaserJet M404 - 31 {runId}` tetap `Damaged`, status global aset tetap `Damaged`, dan penanda tidak berubah
26. Verifikasi penolakan itu tidak menambah node `Marked as repaired by` di Damage Log, tidak mencatat Mark as Repaired di Transaction log aset, dan tidak memicu event `damaged_resolved`

### Mark as Repaired dengan After photo opsional yang diisi ditolak saat Storage penuh
27. Dengan After photo required `OFF`, Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 32 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}` dan After photo baru `perbaikan-be-{runId}.jpeg`
28. Verifikasi permintaan ditolak karena Storage penuh
29. Verifikasi record `Printer HP LaserJet M404 - 32 {runId}` tetap `Damaged` dan status global aset tetap `Damaged`
30. Verifikasi penolakan itu tidak menambah node Damage Log dan tidak memicu event `damaged_resolved`

### Mark as Repaired tanpa After photo tidak mengunggah file dan tidak dicek
31. Dengan After photo required `OFF`, Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 33 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}` dan tanpa After photo
32. Verifikasi permintaan diterima walau Storage penuh dan record menjadi `Repaired`

### Storage dibebaskan atau kuota ditambah membuat permintaan yang sama diterima
33. Kuota `Client Storage Penuh {runId}` ditambah menjadi `100.0 GB` dengan usage ledger tetap `50.0 GB`
34. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 34 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}` dan After photo baru `perbaikan-be-{runId}.jpeg`
35. Verifikasi permintaan diterima dan record menjadi `Repaired` dengan After photo tersimpan pada node `Marked as repaired by`
36. Total Control `Agus Pratama {runId}` menjalankan Report Damaged atas `Laptop Dell Latitude 5420 - 31 {runId}` dengan What happened `Layar retak dan perangkat tidak menyala` dan Damaged Photo baru `kerusakan-be-{runId}.jpeg`
37. Verifikasi permintaan diterima, record `Damaged` tercipta, dan status global aset menjadi `Damaged`
38. Kuota `Client Storage Penuh {runId}` dikembalikan ke `50.0 GB`

### Laporan dari form modul asal ditolak saat Storage penuh dan transaksi modul asal tidak ter-commit
39. Aktor peminjaman `Yoga Tanuwijaya {runId}` pada Client `Client Storage Penuh {runId}` mengirim Report Damaged dari halaman Return Borrow atas `Tablet Samsung Tab A8 - 31 {runId}` dengan Description `Engsel longgar saat dikembalikan {runId}` dan foto Return baru `foto-return-be-{runId}.jpeg`
40. Verifikasi permintaan ditolak karena Storage penuh
41. Verifikasi tidak ada record Damage atau node baru untuk `Tablet Samsung Tab A8 - 31 {runId}`, Return tidak ter-commit sehingga aset tetap `Borrowed` oleh `Budi Santoso {runId}`, dan status global aset tidak berubah

### Storage penuh dievaluasi setelah validasi field lolos
42. Total Control `Agus Pratama {runId}` menjalankan Report Damaged atas `Laptop Dell Latitude 5420 - 34 {runId}` tanpa What happened dan dengan Damaged Photo baru `kerusakan-be-{runId}.jpeg`
43. Verifikasi permintaan ditolak karena What happened wajib diisi, bukan karena Storage penuh, dan tidak ada record Damage untuk `Laptop Dell Latitude 5420 - 34 {runId}`

### Kuota yang diturunkan di bawah usage ledger menolak upload baru
44. Kuota `Client Storage Penuh {runId}` diturunkan menjadi `40.0 GB` dengan usage ledger tetap `50.0 GB`
45. Total Control `Agus Pratama {runId}` menjalankan Report Damaged atas `Laptop Dell Latitude 5420 - 35 {runId}` dengan What happened `Layar retak dan perangkat tidak menyala` dan Damaged Photo baru `kerusakan-be-{runId}.jpeg`
46. Verifikasi permintaan ditolak karena usage ledger melampaui kuota yang diturunkan
47. Verifikasi tidak ada record Damage untuk `Laptop Dell Latitude 5420 - 35 {runId}` dan status global aset tetap `Normal`
48. Kuota `Client Storage Penuh {runId}` dikembalikan ke `50.0 GB`

### Mark as Repaired tanpa After photo ditolak saat After photo required ON
49. Dengan After photo required `ON`, Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 35 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}` dan tanpa After photo
50. Verifikasi permintaan ditolak karena After photo wajib diisi dengan pesan `After photo must not be empty`, bukan karena Storage penuh
51. Verifikasi record `Printer HP LaserJet M404 - 35 {runId}` tetap `Damaged`, status global aset tetap `Damaged`, tidak ada node `Marked as repaired by` di Damage Log, dan tidak ada event `damaged_resolved`
