---
id: TC-FA-BORROW-BE-097-storage-penuh-blokir-foto-transaksi-aturan-server
title: "Storage penuh memblokir foto wajib Handover, Borrow Now, dan Return di server tanpa efek turunan"
layer: be-e2e
priority: High
caseType: Negative
status: draft
sourceRules: ["BORROW-LOGIC-23a", "BORROW-LOGIC-23b", "BORROW-LOGIC-23c", "BORROW-LOGIC-23e", "V-BRW-47", "T-BRW-33", "EC-BRW-180", "BORROW-LOGIC-23f", "BORROW-LOGIC-23g", "BORROW-LOGIC-23h", "V-BRW-31", "EC-BRW-185", "EC-BRW-183", "EC-BRW-181", "BORROW-LOGIC-23d", "EC-BRW-182"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-23a": 2
  "BORROW-LOGIC-23b": [2, 12, 13, 22, 29]
  "BORROW-LOGIC-23c": [2, 15, 20]
  "BORROW-LOGIC-23e": [3, 17, 18, 22, 30]
  "V-BRW-47": [3, 22, 30]
  "T-BRW-33": [3, 22, 30]
  "EC-BRW-180": [3, 5, 6, 10, 13]
  "BORROW-LOGIC-23f": [4, 30]
  "BORROW-LOGIC-23g": [5, 6, 7, 23, 31, 32]
  "BORROW-LOGIC-23h": [8, 9, 10, 27, 35, 36, 37]
  "V-BRW-31": [17, 25]
  "EC-BRW-185": [17, 18]
  "EC-BRW-183": 20
  "EC-BRW-181": [22, 23, 25, 27]
  "BORROW-LOGIC-23d": [25, 29, 34]
  "EC-BRW-182": [30, 31, 32, 34, 37]
anchor: []
coverage:
  web: automated
---

# Storage penuh memblokir foto wajib Handover, Borrow Now, dan Return di server tanpa efek turunan

## Prerequisites
- Mode: FE+BE (backend nyata; cek Storage dijalankan server berdasarkan usage ledger Client saat langkah yang mengirim foto disubmit; keadaan Storage diatur lewat fixture BE).
- Aktor: Asset Admin `Agus Pratama {runId}` dengan Group penugasan `Head Office {runId}` (DU-097-1); Borrower `Rina Wijaya {runId}` (DU-097-2); Borrower self-service `Sari Dewi {runId}` (DU-097-3); Asset Admin `Bagus Santoso {runId}` pada Client tanpa kuota Storage (DU-097-4).
- Data:
  - DU-097-1 sampai DU-097-3: pengguna aktif pada Client PT Storage Penuh {runId} (DU-097-5), seperti di Aktor.
  - DU-097-4: pengguna aktif pada Client PT Tanpa Kuota {runId} (DU-097-6), seperti di Aktor.
  - DU-097-5: Client PT Storage Penuh {runId} dengan kuota Storage `50.0 GB` dan usage ledger `50.0 GB` (usage di atau di atas kuota); fixture BE dapat menaikkan kuota dan mengembalikan usage ke atau di atas kuota.
  - DU-097-6: Client PT Tanpa Kuota {runId} yang Storage-nya belum pernah dialokasikan.
  - DU-097-7: BRW A `Waiting for Handover` Group `Head Office {runId}`, Borrower `Rina Wijaya {runId}`, Photo at start `ON`, aset ber-tag `Laptop Dell Latitude {runId}` dan `Proyektor Epson {runId}`.
  - DU-097-8: BRW B `Waiting for Handover` Group `Head Office {runId}`, Photo at start `OFF`, aset ber-tag `Kursi Lipat Rapat {runId}`.
  - DU-097-9: BRW D `Waiting for Handover` Group `Head Office {runId}`, Photo at start `ON`, aset ber-tag `Printer HP {runId}`.
  - DU-097-10: BRW E `Waiting for Handover` pada Client PT Tanpa Kuota {runId}, Photo at start `ON`, aset ber-tag `Monitor LG {runId}`.
  - DU-097-11: aset self-service `Gimbal DJI RS 3 {runId}`, Group `Head Office {runId}`, TAG `QR`, Custody `Available`, Self service `ON`, Photo at start `ON`.
  - DU-097-12: BRW C berisi baris `Borrowed` aset ber-tag `Kamera Mirrorless {runId}` (Photo at end `ON`), baris `Overdue` aset ber-tag `Tablet Samsung {runId}` (Photo at end `ON`), dan baris `Borrowed` aset ber-tag `Pompa Air Portable {runId}` yang tagnya tidak dapat dipindai (Photo at end `OFF`); Borrower `Rina Wijaya {runId}`, Group `Head Office {runId}`.
  - DU-097-13: file lain milik Client PT Storage Penuh {runId} di File Manager yang dapat di-Delete untuk membebaskan Storage.
- Kondisi: Photo at end `OFF` pada `Pompa Air Portable {runId}` sehingga Return Photo barisnya wajib hanya karena `I Can't Scan the TAG`.

## Test Steps
### Handover berfoto ditolak Storage penuh sebelum sesi konfirmasi dibuat
1. Asset Admin `Agus Pratama {runId}` mencatat jumlah entri Borrow Log BRW A (N0) dan jumlah notifikasi konfirmasi Handover yang diterima Borrower `Rina Wijaya {runId}` (K0)
2. Asset Admin memverifikasi scan `Laptop Dell Latitude {runId}` dan `Proyektor Epson {runId}` pada Handover BRW A dengan 1 foto per aset, lalu mengirim Request Confirmation saat Client PT Storage Penuh {runId} penuh
3. Verifikasi server menolak pengiriman dengan toast Error persisten `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).`, bukan galat server dan bukan inline error
4. Verifikasi cek Storage dijalankan sekali atas seluruh pengiriman sebelum baris mana pun diproses, sehingga tidak ada baris BRW A yang selesai sebagian
5. Verifikasi baris `Laptop Dell Latitude {runId}` dan `Proyektor Epson {runId}` tetap `Waiting for Handover`
6. Verifikasi jumlah entri Borrow Log BRW A sama dengan N0 dan jumlah notifikasi konfirmasi Borrower sama dengan K0, karena tidak ada sesi konfirmasi, entri log, atau notifikasi dari pengiriman yang ditolak
7. Verifikasi Custody dan Due date kedua aset sama dengan sebelum pengiriman

### Penolakan tidak mengunci BRW dan pengiriman ulang berhasil setelah kuota ditambah
8. Kuota Storage Client PT Storage Penuh {runId} dinaikkan menjadi lebih besar dari usage ledger lewat fixture BE
9. Asset Admin mengirim ulang Request Confirmation BRW A dengan foto yang diambil ulang untuk kedua aset
10. Verifikasi sesi konfirmasi dibuat dan Borrower menerima tepat 1 notifikasi konfirmasi baru (K0 + 1)
11. Usage ledger Client PT Storage Penuh {runId} dikembalikan ke atau di atas kuota lewat fixture BE
12. Borrower `Rina Wijaya {runId}` menerima konfirmasi lewat Accept
13. Verifikasi baris `Laptop Dell Latitude {runId}` dan `Proyektor Epson {runId}` menjadi `Borrowed` walau Storage penuh, karena konfirmasi Borrower tidak menyimpan file baru dan tidak mengecek Storage

### Cek Storage hanya berlaku bila langkah mengirim foto
14. Asset Admin mengirim Request Confirmation BRW B dengan `Kursi Lipat Rapat {runId}` terverifikasi tanpa foto saat Storage penuh
15. Verifikasi sesi konfirmasi dibuat karena langkah tidak mengirim foto sehingga tidak ada cek Storage

### Kewajiban foto didahulukan sebelum cek Storage
16. Asset Admin mengirim Request Confirmation BRW D dengan `Printer HP {runId}` terverifikasi tanpa foto saat Storage penuh
17. Verifikasi server menolak dengan pesan `1 asset needs a handover photo.`
18. Verifikasi penolakan itu berasal dari kewajiban foto dan bukan dari cek Storage penuh

### Client tanpa kuota Storage tidak diblokir
19. Asset Admin `Bagus Santoso {runId}` memverifikasi scan `Monitor LG {runId}` pada Handover BRW E dengan 1 foto lalu mengirim Request Confirmation
20. Verifikasi pengiriman tidak diblokir dan sesi konfirmasi dibuat

### Borrow Now self-service ditolak sebelum transaksi dan tanpa jalur tanpa foto
21. Borrower `Sari Dewi {runId}` mengirim Borrow Now atas `Gimbal DJI RS 3 {runId}` dengan scan TAG, Duration `2` Days, Purpose `Liputan acara`, dan 1 foto saat Storage penuh
22. Verifikasi server menolak dengan toast Error `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` sebelum transaksi dimulai
23. Verifikasi tidak ada BRW dan baris yang dibuat atas `Gimbal DJI RS 3 {runId}` dan Custody aset tetap `Available`
24. Borrower `Sari Dewi {runId}` mengirim Borrow Now atas `Gimbal DJI RS 3 {runId}` yang sama tanpa foto saat Storage masih penuh
25. Verifikasi server menolak dengan pesan `1 asset needs a handover photo.` sehingga tidak ada jalur menyelesaikan Borrow Now tanpa foto
26. Kuota Storage dinaikkan menjadi lebih besar dari usage ledger lewat fixture BE, lalu Borrower `Sari Dewi {runId}` mengirim ulang Borrow Now dengan 1 foto
27. Verifikasi BRW dan baris `Borrowed` dibuat atas `Gimbal DJI RS 3 {runId}`

### Return berfoto ditolak seluruhnya, termasuk Return Photo wajib karena I Can't Scan the TAG
28. Usage ledger Client PT Storage Penuh {runId} dikembalikan ke atau di atas kuota lewat fixture BE; Asset Admin `Agus Pratama {runId}` mencatat jumlah notifikasi `borrow_returned` Borrower `Rina Wijaya {runId}` (R0)
29. Asset Admin memverifikasi scan `Kamera Mirrorless {runId}` dan `Tablet Samsung {runId}` dengan Return Photo, memilih `I Can't Scan the TAG` untuk `Pompa Air Portable {runId}` dengan Return Photo, lalu mengirim Return atas ketiganya
30. Verifikasi server menolak seluruh Return dengan toast Error `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).`
31. Verifikasi baris `Kamera Mirrorless {runId}` dan `Pompa Air Portable {runId}` tetap `Borrowed` dan baris `Tablet Samsung {runId}` tetap `Overdue`
32. Verifikasi ketiga aset tidak menjadi `Available`, tidak ada Damage Report, dan jumlah notifikasi `borrow_returned` Borrower sama dengan R0
33. Asset Admin mengirim Return atas `Pompa Air Portable {runId}` saja dengan Return Photo yang wajib karena `I Can't Scan the TAG` walau Photo at end `OFF`
34. Verifikasi server menolak Return itu dengan toast Error yang sama karena blokir Storage penuh tidak punya pengecualian untuk foto wajib
35. Administrator Client men-Delete file lain DU-097-13 di File Manager sehingga usage ledger turun di bawah kuota
36. Asset Admin mengirim ulang Return atas ketiga aset dengan foto yang diambil ulang
37. Verifikasi ketiga baris menjadi `Returned` dan aset menjadi `Available`

## Notes
- Mode: FE+BE. Sumber: PRD `fixed-asset/borrow/PRD/borrow.md` (`BORROW-LOGIC-23`, `V-BRW-47`, `T-BRW-33`, `EC-BRW-180` sampai `EC-BRW-186`) dan `fixed-asset/file-manager/PRD/file-manager.md` (`FAFM-LOGIC-01`, `FAFM-LOGIC-02`, `FAFM-LOGIC-07`). Belum ada TestCase untuk aturan ini; spec dikutip langsung dari ID aturan PRD.
- Di atas smell 35 langkah: satu alur server lintas tiga langkah transaksi (Handover, Borrow Now, Return) memakai Client Storage penuh yang sama; memecahnya menggandakan seeding Client dan fixture BE. Alasan P-1 (state berat) untuk satu Client Storage penuh.
- Klausa absence EC-BRW-180 (tidak ada sesi, entri log, dan notifikasi dari pengiriman ditolak) diasersi sebagai jumlah sama dengan baseline (N0, K0, R0) dan sebagai tepat satu notifikasi baru sesudah pengiriman ulang, bukan asersi ketiadaan murni.
- Nilai `50.0 GB` pada toast dan Client adalah nilai data uji (format Size T-FAFM-01; contoh PRD `50.0 GB of 50.0 GB`); disediakan fixture BE.
- Perilaku mobile offline (`BORROW-LOGIC-23l`, `EC-BRW-184`) ada di spec mobile terpisah; foto dihapus di File Manager (`BORROW-LOGIC-23j`, `EC-BRW-186`) ada di spec web terpisah.
