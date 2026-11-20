---
id: TC-FA-BORROW-E2E-098-handover-storage-penuh-request-confirmation
title: "Request Confirmation pada Handover berfoto ditolak saat Storage penuh dan berhasil setelah kuota ditambah"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceRules: ["BORROW-LOGIC-23e", "V-BRW-31", "EC-BRW-185", "BORROW-LOGIC-23d", "BORROW-LOGIC-23b", "BORROW-LOGIC-23c", "V-BRW-47", "T-BRW-33", "EC-BRW-180", "BORROW-LOGIC-23g", "BORROW-LOGIC-23h"]
smoke: []
dependsOn: []
trace:
  "BORROW-LOGIC-23e": [8, 12, 14]
  "V-BRW-31": 8
  "EC-BRW-185": 8
  "BORROW-LOGIC-23d": [9, 10]
  "BORROW-LOGIC-23b": 11
  "BORROW-LOGIC-23c": 11
  "V-BRW-47": 12
  "T-BRW-33": [12, 14]
  "EC-BRW-180": [12, 15, 20, 28]
  "BORROW-LOGIC-23g": [15, 20]
  "BORROW-LOGIC-23h": [21, 22, 25, 26, 27, 28, 29]
anchor: []
coverage:
  web: automated
---

# Request Confirmation pada Handover berfoto ditolak saat Storage penuh dan berhasil setelah kuota ditambah

## Prerequisites
- Mode: FE+BE (backend nyata; cek Storage dijalankan server saat `[Request Confirmation]`; keadaan Storage diatur lewat fixture BE).
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office`; ia bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-098-1: BRW `Waiting for Handover` Group `Head Office`, Borrower `Hendra Kusuma {runId}-098`, Requested By `Agus Pratama {runId}`, Photo at start ON pada semua barisnya, berisi aset DU-098-2 dan DU-098-3.
  - DU-098-2: aset `Laptop Asus Zenbook {runId}-098`, TAG `RFID`, Category `Laptop`, status baris `Waiting for Handover`.
  - DU-098-3: aset `Proyektor BenQ {runId}-098`, TAG `QR`, Category `Proyektor`, status baris `Waiting for Handover`.
  - DU-098-4: Client Aktor dengan kuota Storage `50.0 GB` dan usage ledger `50.0 GB` (usage di atau di atas kuota) pada awal spec; fixture BE menaikkan kuota di atas usage pada langkah yang menyebutnya.
  - Asset ID aset DU-098-2 dan DU-098-3 dibentuk sistem dan menjadi milik entri aset masing-masing.
- Jeda: langkah 13 menunggu 10 detik tanpa menutup toast agar kepersistenan toast teramati; jeda melampaui durasi tampil toast biasa dan jauh di bawah 30 detik.

## Test Steps
### Kewajiban foto didahulukan sebelum cek Storage
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Ketik Search `Hendra Kusuma {runId}-098`, tekan Enter
4. Klik menu ⋯ pada baris BRW milik DU-098-1, lalu klik `Hand Over`
5. Scan TAG aset DU-098-2 lewat `[Verify Asset]`
6. Scan TAG aset DU-098-3 lewat `[Verify Asset]`
7. Klik `[Request Confirmation]`
8. Verifikasi pesan `2 assets need a handover photo.` tampil di atas tombol `[Request Confirmation]`

### Request Confirmation berfoto ditolak karena Storage penuh
9. Ambil foto pada kolom Handover Photo baris DU-098-2
10. Ambil foto pada kolom Handover Photo baris DU-098-3
11. Klik `[Request Confirmation]`
12. Verifikasi toast Error `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
13. Tunggu 10 detik tanpa menutup toast
14. Verifikasi toast Error Storage penuh masih tampil (persisten, tidak hilang otomatis)
15. Verifikasi popup `Waiting for Confirmation` tidak terbuka karena penolakan terjadi sebelum sesi konfirmasi dibuat
16. Tutup toast Error secara manual

### Baris tetap Waiting for Handover dan pengiriman ulang berhasil setelah kuota ditambah
17. Klik `Transactions` pada sidebar
18. Klik `Borrow`
19. Ketik Search `Hendra Kusuma {runId}-098`, tekan Enter
20. Verifikasi badge status header BRW milik DU-098-1 tetap `Waiting for Handover`
21. Kuota Storage Client dinaikkan menjadi lebih besar dari usage ledger lewat fixture BE
22. Klik menu ⋯ pada baris BRW milik DU-098-1, lalu klik `Hand Over`
23. Scan TAG aset DU-098-2 lewat `[Verify Asset]`
24. Scan TAG aset DU-098-3 lewat `[Verify Asset]`
25. Ambil ulang foto pada kolom Handover Photo baris DU-098-2
26. Ambil ulang foto pada kolom Handover Photo baris DU-098-3
27. Klik `[Request Confirmation]`
28. Verifikasi popup `Waiting for Confirmation` tampil
29. Verifikasi daftar aset sesi konfirmasi memuat aset DU-098-2 dan DU-098-3
30. Klik `[Cancel Request]`

## Notes
- Mode: FE+BE. Sumber: PRD `fixed-asset/borrow/PRD/borrow.md` (`BORROW-LOGIC-23`, `V-BRW-47`, `T-BRW-33`, `EC-BRW-180` sampai `EC-BRW-186`) dan `fixed-asset/file-manager/PRD/file-manager.md`. Belum ada TestCase untuk aturan ini; spec dikutip langsung dari ID aturan PRD.
- Langkah penghubung (bukan klausa aturan): langkah 1 sampai 6 (navigasi dan scan), langkah 13 (jeda 10 detik agar kepersistenan toast teramati), langkah 16 (menutup toast persisten sebelum langkah berikut), dan langkah 30 (membersihkan sesi konfirmasi).
- Nilai `50.0 GB` pada Client dan toast adalah nilai data uji (format Size T-FAFM-01; contoh PRD `50.0 GB of 50.0 GB`); keadaan Storage dan kenaikan kuota diatur lewat fixture BE.
- Klausa absence EC-BRW-180 (tidak ada notifikasi konfirmasi dan entri log dari pengiriman yang ditolak) tidak diasersi di spec UI ini; diasersi dengan baseline jumlah di `TC-FA-BORROW-BE-097-storage-penuh-blokir-foto-transaksi-aturan-server`.
- Temuan untuk PM: PRD tidak menetapkan apakah meninggalkan halaman Handover lewat sidebar sesudah penolakan memunculkan dialog perubahan belum tersimpan; spec berpindah halaman lewat sidebar tanpa asersi dialog.
