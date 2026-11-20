---
id: TC-FA-DAMAGED-BE-213-storage-penuh-blokir-upload-foto
title: "Server menolak upload Damaged Photo dan After photo baru saat Storage client penuh: laporan banyak aset ditolak seluruhnya, foto wajib tidak dikecualikan, tanpa file baru tidak dicek, client tanpa kuota tidak diblokir, dan tanpa efek turunan pada record yang ditolak"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [DAMAGED-LOGIC-10c, DAMAGED-LOGIC-10d, DAMAGED-LOGIC-10e, V-DMG-20, EC-DMG-38, EC-DMG-39, F-DMG-01.k10, F-DMG-05.k7]
smoke: []
dependsOn: []
owner: BE
trace:
  DAMAGED-LOGIC-10c: [2, 6, 10, 14, 17, 20, 22, 27, 36]
  DAMAGED-LOGIC-10d: [2, 22, 23, 31]
  DAMAGED-LOGIC-10e: [3, 4, 7, 8, 11, 12, 24, 25, 28, 29]
  V-DMG-20: [2, 6, 10, 14, 22, 27]
  EC-DMG-38: [2, 3, 4, 6, 7, 8, 10, 11, 12, 14, 17, 18, 20]
  EC-DMG-39: [22, 23, 24, 25, 27, 28, 29, 31, 34]
  F-DMG-01.k10: [2, 3, 4, 6, 7, 10, 11, 12, 14]
  F-DMG-05.k7: [22, 24, 25, 27, 28, 29]
coverage:
  web: automated
---

# Server menolak upload Damaged Photo dan After photo baru saat Storage client penuh: laporan banyak aset ditolak seluruhnya, foto wajib tidak dikecualikan, tanpa file baru tidak dicek, client tanpa kuota tidak diblokir, dan tanpa efek turunan pada record yang ditolak

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged, pada Client `Client Storage Penuh {runId}`.
  - Pelapor umum `Budi Santoso {runId}`, pemegang aset, tanpa role Damaged, pada Client `Client Storage Penuh {runId}`.
  - Total Control `Citra Lestari {runId}`, Aktor Damaged, pada Client `Client Tanpa Kuota {runId}`.
- Data:
  - DU-213-1: Client `Client Storage Penuh {runId}` dengan kuota Storage `50.0 GB` dan usage ledger `50.0 GB`.
  - DU-213-2: Client `Client Tanpa Kuota {runId}` yang Storage-nya belum pernah dialokasikan (tanpa kuota).
  - DU-213-3: Aset `Laptop Dell Latitude 5420 - 31 {runId}`, Group `Head Office {runId}`, TAG `RFID-L31 {runId}`, status global `Normal`, tanpa record Damage.
  - DU-213-4: Aset `Laptop Dell Latitude 5420 - 32 {runId}`, Group `Head Office {runId}`, status global `Normal`, tanpa record Damage.
  - DU-213-5: Aset `Laptop Dell Latitude 5420 - 33 {runId}`, Group `Head Office {runId}`, status global `Normal`, tanpa record Damage.
  - DU-213-6: Aset `Monitor Dell P2422H - 31 {runId}`, Group `Head Office {runId}`, dipegang `Budi Santoso {runId}`, status global `Assigned`, tanpa record Damage.
  - DU-213-7: Aset `Printer HP LaserJet M404 - 31 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged`.
  - DU-213-8: Aset `Printer HP LaserJet M404 - 32 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged`.
  - DU-213-9: Aset `Printer HP LaserJet M404 - 33 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged`.
  - DU-213-10: Aset `Printer HP LaserJet M404 - 34 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged`.
  - DU-213-11: Aset `Kamera Canon EOS - 31 {runId}`, Group `Head Office` pada Client `Client Tanpa Kuota {runId}`, status global `Normal`, tanpa record Damage.
  - DU-213-12: What happened `Layar retak dan perangkat tidak menyala`.
  - DU-213-13: Damaged Photo baru `kerusakan-be-{runId}.jpeg` (JPEG, di bawah 1 MB).
  - DU-213-14: Berkas `catatan-servis.pdf` sebagai berkas berformat tidak valid.
  - DU-213-15: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-213-16: After photo baru `perbaikan-be-{runId}.jpeg` (JPEG, di bawah 1 MB).
- Kondisi:
  - Storage `Client Storage Penuh {runId}` penuh sesuai DU-213-1 kecuali disebut lain pada langkah.
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
13. Usage ledger `Client Storage Penuh {runId}` diatur `51.2 GB` dengan kuota `50.0 GB`, lalu Total Control `Agus Pratama {runId}` menjalankan Report Damaged atas `Laptop Dell Latitude 5420 - 31 {runId}` dengan What happened `Layar retak dan perangkat tidak menyala` dan Damaged Photo baru `kerusakan-be-{runId}.jpeg`
14. Verifikasi permintaan ditolak karena Storage penuh dan nilai terpakai yang dilaporkan `51.2 GB` dibanding kuota `50.0 GB`
15. Usage ledger dikembalikan ke `50.0 GB`

### Format file ditolak didahulukan atas Storage penuh
16. Total Control `Agus Pratama {runId}` menjalankan Report Damaged atas `Laptop Dell Latitude 5420 - 31 {runId}` dengan What happened `Layar retak dan perangkat tidak menyala` dan berkas `catatan-servis.pdf` sebagai Damaged Photo
17. Verifikasi permintaan ditolak karena format berkas tidak valid, bukan karena Storage penuh
18. Verifikasi tidak ada record Damage baru untuk `Laptop Dell Latitude 5420 - 31 {runId}`

### Client tanpa kuota tidak diblokir
19. Total Control `Citra Lestari {runId}` pada Client `Client Tanpa Kuota {runId}` menjalankan Report Damaged atas `Kamera Canon EOS - 31 {runId}` dengan What happened `Layar retak dan perangkat tidak menyala` dan Damaged Photo baru `kerusakan-be-{runId}.jpeg`
20. Verifikasi permintaan diterima, record `Damaged` tercipta, dan status global aset menjadi `Damaged`

### Mark as Repaired dengan After photo wajib (setting ON) ditolak saat Storage penuh
21. Dengan After photo required `ON`, Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 31 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}` dan After photo baru `perbaikan-be-{runId}.jpeg`
22. Verifikasi permintaan ditolak karena Storage penuh
23. Verifikasi pemblokiran itu berlaku karena After photo wajib tidak dikecualikan dari Storage penuh
24. Verifikasi record `Printer HP LaserJet M404 - 31 {runId}` tetap `Damaged`, status global aset tetap `Damaged`, dan penanda tidak berubah
25. Verifikasi penolakan itu tidak menambah node `Marked as repaired by` di Damage Log, tidak mencatat Mark as Repaired di Transaction log aset, dan tidak memicu event `damaged_resolved`

### Mark as Repaired dengan After photo opsional yang diisi ditolak saat Storage penuh
26. Dengan After photo required `OFF`, Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 32 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}` dan After photo baru `perbaikan-be-{runId}.jpeg`
27. Verifikasi permintaan ditolak karena Storage penuh
28. Verifikasi record `Printer HP LaserJet M404 - 32 {runId}` tetap `Damaged` dan status global aset tetap `Damaged`
29. Verifikasi penolakan itu tidak menambah node Damage Log dan tidak memicu event `damaged_resolved`

### Mark as Repaired tanpa After photo tidak mengunggah file dan tidak dicek
30. Dengan After photo required `OFF`, Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 33 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}` dan tanpa After photo
31. Verifikasi permintaan diterima walau Storage penuh dan record menjadi `Repaired`

### Storage dibebaskan atau kuota ditambah membuat permintaan yang sama diterima
32. Kuota `Client Storage Penuh {runId}` ditambah menjadi `100.0 GB` dengan usage ledger tetap `50.0 GB`
33. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 34 {runId}` dengan Repair note `Komponen rusak sudah diganti {runId}` dan After photo baru `perbaikan-be-{runId}.jpeg`
34. Verifikasi permintaan diterima dan record menjadi `Repaired` dengan After photo tersimpan pada node `Marked as repaired by`
35. Total Control `Agus Pratama {runId}` menjalankan Report Damaged atas `Laptop Dell Latitude 5420 - 31 {runId}` dengan What happened `Layar retak dan perangkat tidak menyala` dan Damaged Photo baru `kerusakan-be-{runId}.jpeg`
36. Verifikasi permintaan diterima, record `Damaged` tercipta, dan status global aset menjadi `Damaged`
37. Kuota `Client Storage Penuh {runId}` dikembalikan ke `50.0 GB`

## Notes
- Spec ini bersumber dari PRD `damaged.md` (DAMAGED-LOGIC-10c sampai 10e, V-DMG-20, EC-DMG-38, EC-DMG-39); belum ada TestCase untuk aturan Storage penuh, sehingga keterlacakan memakai ID aturan PRD.
- Pesan penolakan server, kode status, dan bentuk payload tidak ditetapkan PRD; asersi hanya pada keputusan tolak/terima dan efek ke record, status global aset, node Damage Log, log, dan event.
- Cek Storage dievaluasi setelah format dan ukuran file lolos (DAMAGED-LOGIC-10c); karena itu langkah 16 sampai 17 mengasersi format lebih dulu.
- Report Damaged dari form modul asal (Return, Unassign, Receive, Stock Opname, Mark as Found) memakai aturan blokir yang sama (DAMAGED-LOGIC-10a) tetapi asersinya dimiliki spec modul asal.
- Di atas 35 langkah (37) karena satu keadaan Storage penuh dipakai bersama oleh seluruh titik cek Report Damaged dan Mark as Repaired.
