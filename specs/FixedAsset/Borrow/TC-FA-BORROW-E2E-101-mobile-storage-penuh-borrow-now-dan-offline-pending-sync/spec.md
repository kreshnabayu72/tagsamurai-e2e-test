---
id: TC-FA-BORROW-E2E-101-mobile-storage-penuh-borrow-now-dan-offline-pending-sync
title: "Mobile: Borrow Now ditolak saat Storage penuh dan langkah offline yang ditolak Storage penuh tetap Pending sync"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceRules: ["BORROW-LOGIC-23d", "BORROW-LOGIC-23b", "BORROW-LOGIC-23e", "V-BRW-47", "T-BRW-33", "EC-BRW-181", "BORROW-LOGIC-23g", "BORROW-LOGIC-23h", "BORROW-LOGIC-23l", "EC-BRW-184"]
smoke: []
dependsOn: []
trace:
  "BORROW-LOGIC-23d": 6
  "BORROW-LOGIC-23b": 7
  "BORROW-LOGIC-23e": 8
  "V-BRW-47": 8
  "T-BRW-33": [8, 21, 34]
  "EC-BRW-181": [8, 9, 12]
  "BORROW-LOGIC-23g": [9, 23, 36]
  "BORROW-LOGIC-23h": [10, 11, 12]
  "BORROW-LOGIC-23l": [19, 20, 21, 22, 23, 24, 25, 26, 32, 33, 34, 35, 36, 37, 38]
  "EC-BRW-184": [19, 21, 22, 23, 26, 32, 34, 35, 36, 38]
anchor: []
coverage:
  android: manual
---

# Mobile: Borrow Now ditolak saat Storage penuh dan langkah offline yang ditolak Storage penuh tetap Pending sync

## Prerequisites
- Mode: FE+BE (backend nyata; perangkat Android native Fixed Asset; cek Storage dijalankan server saat langkah dikirim atau disinkron; keadaan Storage diatur lewat fixture BE).
- Aktor: Borrower `Hendra Kusuma {runId}-101` (DU-101-1) untuk Borrow Now, lalu Asset Admin `Agus Pratama {runId}` (DU-101-2) dengan Group penugasan `Head Office` untuk Handover dan Return offline.
- Layar awal: layar utama aplikasi native Android Fixed Asset.
- Data:
  - DU-101-1: karyawan `Hendra Kusuma {runId}-101` dengan akun login, Home Group `Head Office`, Status `Active`, Eligibility `Can borrow`.
  - DU-101-2: Asset Admin `Agus Pratama {runId}` aktif, memakai aplikasi native Android.
  - DU-101-3: aset `Mesin Label Brother {runId}-101`, Group `Head Office`, TAG `QR`, Self service `ON`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`, Custody `Available`, Max Duration `7 days`, Photo at start ON.
  - DU-101-4: isian Borrow Now aset DU-101-3: Duration `2` hari, Purpose `Pelabelan arsip gudang`.
  - DU-101-5: BRW `Waiting for Handover` Group `Head Office`, Borrower `Hendra Kusuma {runId}-101`, Photo at start ON, berisi baris aset `Laptop Dell Latitude 5420 {runId}-101` (TAG `RFID`).
  - DU-101-6: BRW `Borrowed` Group `Head Office`, Borrower `Hendra Kusuma {runId}-101`, Photo at end ON, berisi baris aset `Kamera Sony A7 {runId}-101` (TAG `NFC`).
  - DU-101-7: Client dengan kuota Storage `50.0 GB` dan usage ledger `50.0 GB` (usage di atau di atas kuota) pada awal spec; fixture BE menaikkan kuota di atas usage pada langkah yang menyebutnya.
- Kondisi: perangkat Android terhubung online kecuali pada langkah yang menyatakan koneksi dimatikan atau dinyalakan.

## Test Steps
### Borrow Now berfoto ditolak saat Storage penuh
1. Masuk sebagai Borrower `Hendra Kusuma {runId}-101`
2. Klik menu Profile pada navbar, klik `My Asset`, lalu klik tab `Borrowed`
3. Klik `[Borrow an Asset]`
4. Pindai TAG aset DU-101-3 lewat komponen scan
5. Isi Duration baris `Mesin Label Brother {runId}-101` dengan `2` dan Purpose dengan `Pelabelan arsip gudang`
6. Ambil foto aset `Mesin Label Brother {runId}-101` dengan kamera perangkat
7. Klik `[Borrow Now]`
8. Verifikasi toast Error `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
9. Verifikasi panel hasil `Success, 1 asset is now borrowed. Return by [Date].` tidak tampil dan aset `Mesin Label Brother {runId}-101` belum berstatus `Borrowed`
10. Kuota Storage Client dinaikkan menjadi lebih besar dari usage ledger lewat fixture BE
11. Ambil ulang foto aset `Mesin Label Brother {runId}-101` lalu klik `[Borrow Now]`
12. Verifikasi panel hasil `Success, 1 asset is now borrowed. Return by [Date].` tampil

### Handover offline yang ditolak Storage penuh tetap Pending sync dengan alasan Storage is full
13. Usage ledger Client dikembalikan ke atau di atas kuota lewat fixture BE
14. Masuk sebagai Asset Admin `Agus Pratama {runId}`
15. Ketuk `[Hand Over]` pada kartu aset `Laptop Dell Latitude 5420 {runId}-101`
16. Matikan koneksi data perangkat
17. Pindai TAG aset `Laptop Dell Latitude 5420 {runId}-101`
18. Ambil foto aset `Laptop Dell Latitude 5420 {runId}-101`
19. Verifikasi pemindaian TAG dan foto berhasil dilakukan saat perangkat offline dengan status `Pending sync` di perangkat
20. Nyalakan koneksi data perangkat sehingga langkah disinkron ke server
21. Verifikasi toast Error `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil pada pemberitahuan sinkron
22. Verifikasi langkah Handover aset `Laptop Dell Latitude 5420 {runId}-101` tetap `Pending sync` di perangkat dengan alasan `Storage is full` dan tidak ada transaksi yang hilang
23. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}-101` di server tetap `Waiting for Handover`
24. Kuota Storage Client dinaikkan menjadi lebih besar dari usage ledger lewat fixture BE
25. Kirim ulang langkah Handover yang tertunda dari perangkat
26. Verifikasi status `Pending sync` hilang setelah tersinkron dan kartu aset `Laptop Dell Latitude 5420 {runId}-101` tampil di daftar BRW

### Return offline yang ditolak Storage penuh tetap Pending sync dengan alasan Storage is full
27. Usage ledger Client dikembalikan ke atau di atas kuota lewat fixture BE
28. Ketuk `[Return]` pada kartu aset `Kamera Sony A7 {runId}-101`
29. Matikan koneksi data perangkat
30. Pindai TAG aset `Kamera Sony A7 {runId}-101`
31. Ambil foto Return aset `Kamera Sony A7 {runId}-101`
32. Verifikasi scan dan foto Return disimpan lokal dengan status `Pending sync`
33. Nyalakan koneksi data perangkat sehingga langkah disinkron ke server
34. Verifikasi toast Error `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil pada pemberitahuan sinkron
35. Verifikasi langkah Return aset `Kamera Sony A7 {runId}-101` tetap `Pending sync` di perangkat dengan alasan `Storage is full`
36. Verifikasi baris aset `Kamera Sony A7 {runId}-101` di server tetap `Borrowed`
37. Kuota Storage Client dinaikkan menjadi lebih besar dari usage ledger lewat fixture BE, lalu kirim ulang langkah Return yang tertunda dari perangkat
38. Verifikasi baris aset `Kamera Sony A7 {runId}-101` menjadi `Returned` dan status `Pending sync` hilang

## Notes
- Mode: FE+BE. Sumber: PRD `fixed-asset/borrow/PRD/borrow.md` (`BORROW-LOGIC-23`, `V-BRW-47`, `T-BRW-33`, `EC-BRW-180` sampai `EC-BRW-186`) dan `fixed-asset/file-manager/PRD/file-manager.md`. Belum ada TestCase untuk aturan ini; spec dikutip langsung dari ID aturan PRD.
- Cakupan platform: aplikasi native Android saja; `coverage.android: manual` seperti spec mobile Borrow lain karena perangkat dan pemutusan koneksi dikendalikan manual.
- Langkah penghubung (bukan klausa aturan): langkah 1 sampai 5 (masuk, navigasi, scan, dan isian Borrow Now), langkah 13 sampai 17 dan 27 sampai 30 (memulihkan keadaan Storage, masuk sebagai Asset Admin, memutus koneksi, dan memindai).
- Nilai `50.0 GB` pada Client dan toast adalah nilai data uji (format Size T-FAFM-01; contoh PRD `50.0 GB of 50.0 GB`); keadaan Storage dan kenaikan kuota diatur lewat fixture BE.
- Temuan untuk PM: PRD (`BORROW-LOGIC-23l`) menetapkan bahwa langkah yang ditolak dapat dikirim ulang dari perangkat tetapi tidak menetapkan kontrol UI untuk mengirim ulang; langkah `Kirim ulang langkah ... yang tertunda dari perangkat` memakai kata generik, kontrol sebenarnya ditetapkan di tahap script.
- Temuan untuk PM: tampilan alasan `Storage is full` pada status `Pending sync` ditetapkan PRD sebagai tanda alasan tanpa letak UI; spec mengasersi alasan tampil bersama status.
- Di atas smell 35 langkah: spec ini 38 langkah karena tiga alur mobile berurutan berbagi satu Client Storage penuh dan satu perangkat; alasan P-1 (state berat) untuk satu Client Storage penuh dan perangkat.
