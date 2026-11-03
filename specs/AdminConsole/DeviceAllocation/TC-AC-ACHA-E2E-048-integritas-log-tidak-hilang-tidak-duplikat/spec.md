---
id: TC-AC-ACHA-E2E-048-integritas-log-tidak-hilang-tidak-duplikat
title: "Integritas Log: Satu Entri per Aksi, Entri Lama Immutable, dan Aksi Gagal Tidak Mengubah Allocation Log"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHA-389
  - TC-AC-ACHA-390
  - TC-AC-ACHA-391
coverage:
  web: automated
---

# Integritas Log: Satu Entri per Aksi, Entri Lama Immutable, dan Aksi Gagal Tidak Mengubah Allocation Log

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata untuk TC-AC-ACHA-391).
- Akun: Group Member Distributor `memberOnDistributor_automated_qaTeam1@qwertysystem.net` (Pre-setup #32, Budi Santoso, MB_ON), password `Spectra.env.AC_DA_MB_ON_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- Data Pre-setup: #14 harga produk (RFID Object TAG PT ABC $2.50), #16 kantong PT Global Distribusi saldo $20,000.00 (Reserved awal $0.00, dipulihkan fixture di hook `before`), #7 Client PT Sejahtera Logistik.
- Data seeding milik spec (fixture API disediakan tim FE/BE; salinan milik spec dari Pre-setup #49): transaksi Waiting for Approval milik MB_ON (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00), tiga salinan: satu transaksi pembanding untuk TC-AC-ACHA-389 (transaksi pertama TC-AC-ACHA-389 dibuat lewat UI, bukan salinan), satu untuk TC-AC-ACHA-390, dan satu untuk TC-AC-ACHA-391.
- Pemulihan dan efek (R-08, S-06): hook `after` membatalkan transaksi Waiting for Approval sisa (pembanding, salinan TC-AC-ACHA-390 dan 391), memulihkan Reserved kantong PT Global Distribusi dan seed ke 30 baris lewat fixture yang disediakan tim FE/BE; transaksi yang dibuat spec tidak dapat dihapus lewat UI dan audit trail (Allocation Log, Activity Log) bertambah permanen, sehingga asersi memakai Allocation ID. Pre-setup bersama tidak diubah selain Reserve kantong PT Global Distribusi. Allocation ID tiap salinan ditangkap dari respons fixture seeding (Dynamic Reference) dan dipakai sebagai penanda Search, asersi, dan cleanup hook `after`.
- Transaksi di blok TC-AC-ACHA-389 dibuat lewat `[+ Allocation]` (jalur persetujuan; Category, Type, Client, Pay From, dan Quantity sama dengan salinan seed) supaya dokumen Create tertulis lewat jalur normal dan jumlah dokumen Activity Log dapat diasersi tepat empat. Baseline baris log nol karena Allocation ID baru (S-12).
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons Cancel 500 (TC-AC-ACHA-391, dilepas segera sesudah pemicu); fixture baca Reserved kantong PT Global Distribusi (disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACHA-389: Tepat satu entri audit per aksi, tidak nyasar ke transaksi lain

1. Klik `[+ Allocation]`, pilih Category `TAG - RFID`, Type `Object TAG`, Client `PT Sejahtera Logistik`, Pay From `PT ABC (Principal)`, isi Quantity `100`, klik `[Submit]`, lalu Catat Allocation ID baru sebagai transaksi pertama (penanda cleanup)
2. Klik `Edit` pada transaksi pertama, ubah Quantity menjadi `120`, lalu klik `[Save]`
3. Klik `Edit` pada transaksi pertama, ubah Notes menjadi `Batch revisi`, lalu klik `[Save]`
4. Klik `Cancel Allocation` pada transaksi pertama, lalu konfirmasi di dialog
5. Buka menu row action `⋯` transaksi pertama dan klik `Allocation Log`
6. Verifikasi modal Allocation Log transaksi pertama memuat tepat empat entri berurutan dari atas: `Allocation canceled`, `Allocation edited`, `Allocation edited`, `Allocation created` (tanpa duplikat dan tanpa entri hilang)
7. Tutup modal Allocation Log dengan `[×]`
8. Buka Activity Log di Admin Console dan cari Allocation ID transaksi pertama
9. Verifikasi Activity Log memuat tepat empat dokumen untuk Allocation ID itu: Create (1 baris), Edit Quantity (1 baris), Edit Notes (1 baris), Cancel (1 baris)
10. Buka menu row action `⋯` transaksi pembanding (transaksi Waiting for Approval kedua milik MB_ON dari fixture) dan klik `Allocation Log`
11. Verifikasi modal Allocation Log transaksi pembanding tetap hanya berisi entri `Allocation created` (tidak ada entri nyasar)
12. Tutup modal Allocation Log dengan `[×]`

### TC-AC-ACHA-390: Entri log lama tidak berubah setelah Edit berikutnya

13. Buka menu row action `⋯` transaksi Waiting for Approval milik MB_ON (salinan untuk blok ini), klik `Allocation Log`, dan catat isi entri `Allocation created`
14. Tutup modal Allocation Log dengan `[×]`
15. Klik `Edit` pada transaksi itu, ubah Quantity menjadi `120`, lalu klik `[Save]`
16. Klik `Edit` pada transaksi itu, ubah Quantity menjadi `150`, lalu klik `[Save]`
17. Buka kembali modal Allocation Log transaksi itu
18. Verifikasi entri `Allocation created` tetap berisi `Quantity: 100` dan `Cost: $250.00`, sama dengan isi yang dicatat pada langkah 13
19. Verifikasi entri `Allocation edited` pertama tetap berisi `Quantity: 120` dan `Cost: $300.00`
20. Verifikasi entri `Allocation edited` kedua berisi `Quantity: 150` dan `Cost: $375.00`
21. Verifikasi urutan entri terbaru di atas
22. Verifikasi isi semua entri tidak berubah dibanding pencatatan sebelumnya
23. Tutup modal Allocation Log dengan `[×]`

### TC-AC-ACHA-391: Aksi gagal tidak meninggalkan entri log

24. Baca Reserved kantong PT Global Distribusi lewat fixture baca (disediakan tim FE/BE) dan catat sebagai R0 (baseline sebelum Cancel)
25. Atur intercept agar respons Cancel dipaksa server error 500
26. Klik `Cancel Allocation` pada transaksi Waiting for Approval milik MB_ON (salinan untuk blok ini), lalu konfirmasi di dialog
27. Lepas intercept respons Cancel
28. Verifikasi toast error "Error, failed to cancel device allocation."
29. Verifikasi status transaksi tetap `Waiting for Approval`
30. Baca Reserved kantong PT Global Distribusi lewat fixture baca (disediakan tim FE/BE)
31. Verifikasi Reserved kantong sama dengan R0 pada langkah 24 (tidak berubah akibat Cancel yang gagal)
32. Buka menu row action `⋯` transaksi itu dan klik `Allocation Log`
33. Verifikasi Allocation Log tetap hanya memuat entri `Allocation created`
34. Tutup modal Allocation Log dengan `[×]`

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 5c). Subjudul `###` memetakan langkah ke id TC granular.
- Pembagian TC lintas spec: TC-AC-ACHA-391 b (klausa "Activity Log dan System Log tidak memuat dokumen Cancel") dijalankan sebagai aksi nyata dengan baseline sendiri di spec 049 (`absence-pencatatan-log-aksi-ditolak`, S-05); spec ini mengasersi bagian lain TC-AC-ACHA-391, yaitu toast, status, Reserved, dan isi Allocation Log (asersi jumlah, bukan absence). TC-AC-ACHA-391 tetap primer di spec ini.
- P-5 (b, objek uji ringan): TC-AC-ACHA-391 adalah satu kegagalan 5xx yang dipaksa (respons Cancel 500) tanpa harness eksternal dan tanpa state berat sendiri, satu-satunya TC kelas b di spec ini; respons 500 pada langkah 25 sampai 27 adalah objek uji (status, Reserved, dan Allocation Log tidak berubah); intercept dilepas pada langkah 27, segera setelah pemicu (S-09).
- Langkah penghubung (S-03): langkah 7, 12, 14, 23, 34 (tutup modal Allocation Log); langkah 13 (catat isi entri sebagai pembanding langkah 18); langkah 17 (buka kembali modal); langkah 30 (baca state Reserved lewat fixture, untuk Expected "Reserved tidak berubah dari baseline"; langkah 24 mencatat R0 sebelum Cancel diintercept); langkah 32 (buka modal).
- Baris target (R-16): transaksi milik spec ditemukan lewat Search Allocation ID yang dicatat saat pembuatan atau fixture sebagai langkah penghubung tanpa `Verifikasi` sebelum aksi baris; langkah ini tidak diberi nomor sendiri, dan Search dikosongkan lewat klik `(←)` pada kotak Search sebelum blok berikutnya.
- Pembuatan transaksi lewat UI pada langkah 1 menggantikan precondition "Pre-setup #49 tersedia" supaya dokumen Create tertulis lewat jalur normal dan Expected "tepat empat dokumen" dapat diasersi tanpa baseline; transaksi pembanding berasal dari fixture. Transaksi dibatalkan di langkah 4 sehingga tidak tersisa Reserve.
- Penanda transaksi (A-11, S-12): transaksi pertama diberi penanda lewat Allocation ID yang dicatat pada langkah 1 (dipakai Search, asersi, dan cleanup hook `after`); Notes bukan data TC pada langkah itu sehingga tidak memakai `{runId}`. `Batch revisi` adalah nilai input non-identitas. R0 pada langkah 24 dicatat di awal blok TC-AC-ACHA-391 karena kantong PT Global Distribusi masih memegang Reserve salinan blok TC-AC-ACHA-389 dan 390 yang tetap Waiting for Approval, sehingga Reserved tidak diasersi sebagai nilai absolut.
- Temuan untuk QA:
  - TC-AC-ACHA-389 precondition d menyebut "Transaksi Waiting for Approval kedua milik akun yang sama untuk pembanding (Pre-setup #49)" padahal Pre-setup #49 satu transaksi; spec memakai satu salinan fixture tambahan.
  - TC-AC-ACHA-389 b mengharapkan tepat empat dokumen termasuk Create, yang hanya benar bila transaksi dibuat lewat jalur normal; spec membuatnya lewat UI (lihat Notes).
  - TC-AC-ACHA-391 Expected a menyebut Reserved $250.00 tanpa surface pembacaan; spec memakai fixture baca (disediakan tim FE/BE).
  - Post Condition TC-AC-ACHA-389, 390, 391 ("-") tidak ada.
