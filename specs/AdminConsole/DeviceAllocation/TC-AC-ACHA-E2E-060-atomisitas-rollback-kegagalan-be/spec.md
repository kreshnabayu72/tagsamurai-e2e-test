---
id: TC-AC-ACHA-E2E-060-atomisitas-rollback-kegagalan-be
title: "Atomisitas Transaksi: Rollback Penuh Saat Kegagalan di Tengah Submit Jalur Langsung dan Approve"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-467
  - TC-AC-ACHA-468
coverage:
  web: automated
---

# Atomisitas Transaksi: Rollback Penuh Saat Kegagalan di Tengah Submit Jalur Langsung dan Approve

## Prerequisites

- Mode: FE+BE.
- Kelas harness b (fault injection sisi server: rollback database). Pemicu bukan respons HTTP yang dapat di-intercept di browser, sehingga spec tetap FE+BE dan kemampuan teknisnya ditulis sebagai kebutuhan.
- Akun: Total Control Distributor `totalControlDistributor_automated_qaTeam1@qwertysystem.net` (Pre-setup #27, Hendra Wibowo), password `Spectra.env.AC_DA_TC_DIST_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan menonaktifkan fault injection.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- Kemampuan teknis (disediakan tim BE; tanpa endpoint karangan): lingkungan BE dengan fault injection pada lapisan database yang (a) menggagalkan penambahan kuota Client sesudah pemotongan saldo berhasil dalam satu transaksi (TC-AC-ACHA-467) dan (b) menggagalkan penambahan kuota Client sesudah Capture berhasil dalam satu transaksi (TC-AC-ACHA-468); fixture baca (disediakan tim FE/BE) untuk jumlah transaksi entitas pengirim, status, Reserved, saldo kantong PT Global Distribusi, dan kuota Client PT Sejahtera Logistik; fault injection dinonaktifkan sesudah tiap TC dan di hook `after`. Bila tim BE tidak menyediakan kemampuan ini, spec ditandai `coverage.web: unsupported` (bukan dihapus).
- Data Pre-setup: #7 Client PT Sejahtera Logistik, #14 harga produk, #16 kantong PT Global Distribusi saldo $20,000.00 (Reserved awal $0.00, dipulihkan fixture di hook `before`).
- Data seeding milik spec (fixture API disediakan tim FE/BE; salinan milik spec dari Pre-setup #49): transaksi Waiting for Approval milik MB_ON (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00) untuk TC-AC-ACHA-468. Allocation ID tiap salinan ditangkap dari respons fixture seeding (Dynamic Reference) dan dipakai sebagai penanda Search, asersi, dan cleanup hook `after`.
- Pemulihan dan efek (R-08, S-06): hook `after` menonaktifkan fault injection, membatalkan transaksi Waiting for Approval salinan TC-AC-ACHA-468 yang tetap Waiting, dan memulihkan saldo serta Reserve kantong PT Global Distribusi lewat fixture yang disediakan tim FE/BE; transaksi tidak dapat dihapus lewat UI. Pre-setup bersama tidak diubah selain saldo dan Reserve kantong itu.
- Baseline (S-12): sebelum tiap TC dicatat lewat fixture baca jumlah transaksi, status, Reserved, saldo, kuota Client, dan jumlah entri Object `Device Allocation` pada Activity Log (Admin Console); asersi memakai selisih terhadap baseline.
- Suite berjalan serial (`parallel: false`): fault injection dan saldo kantong adalah state global.

## Test Steps

### TC-AC-ACHA-467: Atomisitas Submit jalur langsung: eksekusi, kuota, dan saldo satu transaksi

1. Catat jumlah transaksi entitas pengirim, saldo kantong PT Global Distribusi, kuota BLE Client PT Sejahtera Logistik lewat fixture baca, dan jumlah entri Object `Device Allocation` pada Activity Log sebagai baseline
2. Aktifkan fault injection yang menggagalkan penambahan kuota Client setelah pemotongan saldo berhasil dalam satu transaksi
3. Klik `[+ Allocation]`, pilih Category `TAG - BLE`, Client `PT Sejahtera Logistik`, dan isi Quantity `20`
4. Klik `[Submit]` jalur langsung
5. Lepas fault injection
6. Verifikasi toast error "Error, failed to create device allocation."
7. Verifikasi form tetap terbuka
8. Baca jumlah transaksi, saldo kantong, dan kuota BLE Client lewat fixture baca
9. Verifikasi tidak ada transaksi baru dibanding baseline langkah 1
10. Verifikasi saldo kantong tetap $20,000.00 dibanding baseline langkah 1
11. Verifikasi kuota Client tidak berubah dibanding baseline langkah 1
12. Klik `[×]` pada form
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`
15. Buka Activity Log di Admin Console dan hitung jumlah entri Object `Device Allocation`
16. Verifikasi Activity Log tampil dengan entri Object `Device Allocation` milik aksi lain sebagai pembanding
17. Verifikasi tidak ada dokumen audit baru: jumlah entri sama dengan baseline langkah 1

### TC-AC-ACHA-468: Atomisitas Approve: Capture dan kuota dalam satu transaksi

18. Catat status dan Reserved transaksi Waiting for Approval milik MB_ON (salinan blok ini), saldo kantong, dan kuota BLE Client PT Sejahtera Logistik lewat fixture baca sebagai baseline
19. Aktifkan fault injection yang menggagalkan penambahan kuota Client setelah Capture berhasil dalam satu transaksi
20. Buka Approvals > Device Allocation, klik `[Approve]` pada transaksi itu, lalu konfirmasi
21. Lepas fault injection
22. Verifikasi toast error "Error, failed to approve transaction."
23. Baca status, Reserved, saldo kantong, dan kuota Client lewat fixture baca
24. Verifikasi status tetap `Waiting for Approval` sesuai baseline langkah 18
25. Verifikasi Reserved tetap $250.00 sesuai baseline langkah 18
26. Verifikasi tidak ada Capture: saldo kantong tidak berubah dibanding baseline langkah 18
27. Verifikasi kuota Client tidak berubah dibanding baseline langkah 18

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 9d, Atomisitas, berlabel Manual Only/BE di TC). Subjudul `###` memetakan langkah ke id TC granular.
- TC-AC-ACHA-467 dan 468 berlabel Manual Only (c) di kolom Automation karena kegagalan di tengah transaksi database tidak dapat dipicu lewat UI atau API; label itu bukan alasan mengeluarkan TC dari spec (konvensi bagian 2). Kebutuhan fault injection ditulis di Prerequisites sebagai kemampuan yang disediakan tim BE; bila tidak tersedia, `coverage.web` diubah menjadi `unsupported`.
- P-1 (state berat): asersi "tidak ada dokumen audit" pada TC-AC-ACHA-467 (baseline langkah 1 dan pembacaan Activity Log sesudah form ditutup) tetap berada di spec ini karena konteksnya bergantung pada fault injection yang baru dibangun; memakai baseline jumlah entri (S-12) dengan anchor positif entri pembanding Activity Log tepat sebelumnya.
- Langkah penghubung (S-03): langkah baseline (1, 18), langkah mengaktifkan dan melepas fault injection (S-09), langkah baca state lewat fixture baca ("disediakan tim FE/BE", S-11, S-13), langkah menutup form dirty (S-08).
- Baris target (R-16): transaksi salinan blok TC-AC-ACHA-468 pada langkah 20 ditemukan lewat Allocation ID yang ditangkap dari respons fixture seeding; baris Approvals dicocokkan dengan Allocation ID itu (Search bila tersedia) sebagai langkah penghubung tanpa `Verifikasi` dan tanpa nomor sendiri.
- Pengecualian S-12 nama literal (Lampiran A butir A-6): Notes `Batch uji` ditulis persis seperti TC.
- Temuan untuk QA:
  - TC-AC-ACHA-467 dan 468 menyebut "kuota Client tidak berubah" tanpa surface pembacaan; spec memakai fixture baca kuota (disediakan tim FE/BE).
  - TC-AC-ACHA-467 b menyebut "tidak ada dokumen audit" tanpa menyebut surface log; spec membaca Activity Log (Admin Console).
  - TC-AC-ACHA-467 dan 468 mengasumsikan kemampuan fault injection di lapisan database yang tidak didefinisikan di TC, PRD, atau LLD (Catatan TC: tidak dapat dipicu dari sisi klien); mekanisme dicatat sebagai kemampuan tim BE tanpa endpoint karangan.
  - TC-AC-ACHA-467 langkah 3 dan 468 langkah 3 ("Lepas fault injection") adalah langkah observasi yang mendahului pembacaan; spec melepas fault injection segera sesudah pemicu agar state dapat dibaca.
  - Post Condition TC-AC-ACHA-467 dan 468 ("-") tidak ada.
