---
id: TC-AC-ACTS-E2E-261-modal-event-log-penulisan-sesi-delete-by-scan-unit-dilewati-audit-dan-kolom-hardware
title: "Modal Event Log: Penulisan Sesi Delete by Scan, Unit Dilewati pada Sesi Audit TAG, dan Kolom Hardware Tab Audit TAG"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-476
  - TC-AC-ACTS-931
  - TC-AC-ACTS-932
coverage:
  web: automated
---

# Modal Event Log: Penulisan Sesi Delete by Scan, Unit Dilewati pada Sesi Audit TAG, dan Kolom Hardware Tab Audit TAG

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `scanUnitA` = TAG Code unit Available pertama untuk Delete by Scan (milik spec, di-seed fixture BE); `scanUnitB` = TAG Code unit Available kedua untuk Delete by Scan; `scanUnitC` = TAG Code unit Available ketiga untuk Delete by Scan; `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12); `unknownCode` = kode TAG yang tidak dikenali sistem.
- Data seed: SKU `Fixture.tagStock.skuRfid` dengan tiga unit Available milik spec untuk Delete by Scan (`Fixture.tagStock.scanUnitA`, `Fixture.tagStock.scanUnitB`, `Fixture.tagStock.scanUnitC`) dan satu kode tidak dikenali (`Fixture.tagStock.unknownCode`) untuk TC-AC-ACTS-476; 6 unit eligible Audit dengan satu unit yang akan diaktivasi Client untuk TC-AC-ACTS-931; unit eligible Audit untuk TC-AC-ACTS-932. Di-seed ulang fixture BE sebelum tiap TC (langkah penghubung) dan dipulihkan di hook `after`.
- Spec berjalan serial karena memakai simulator pemindai dan Handheld Reader USB bersama.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pembacaan lewat fixture BE atas jumlah total entri sesi Event Log SKU per tab sebagai baseline (selain teks footer pagination); TC tidak menyebut cara membaca baseline (lihat Temuan untuk QA).
- Kemampuan teknis: Simulator pemindai RFID `Zebra RFD40 (SN-2201)` (scan satu per satu dan beruntun, kode tidak dikenali) disediakan tim FE; mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Simulator Handheld Reader USB `HR-RFID-01` di Sync Panel (terdeteksi dan diputus) disediakan tim FE; mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Pelaku kedua (Client di Global Settings) lewat sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-476: Event Log Tab Add Stock: sesi Delete by Scan menulis satu baris dengan Failed 0

4. Catat jumlah total entri sesi Tab Add Stock SKU `Fixture.tagStock.skuRfid` sebagai baseline (kemampuan baca fixture BE)
5. Tutup modal Event Log dengan klik (X)
6. Klik `[Delete by Scan]`
7. Pindai unit `Fixture.tagStock.scanUnitA`, `Fixture.tagStock.scanUnitB`, dan `Fixture.tagStock.scanUnitC` lewat reader RFID `Zebra RFD40 (SN-2201)`
8. Pindai kode tidak dikenali `Fixture.tagStock.unknownCode`
9. Klik `[Stop]`
10. Klik icon `[Event Log]` di toolbar Tab Available
11. Verifikasi satu baris sesi terbaru: Activity `Delete Stock`, Success `3`, Waiting for Approval `—`, Failed `0`, Hardware `Zebra RFD40 (SN-2201)`
12. Verifikasi scan yang ditolak tidak menambah baris (jumlah total entri bertambah tepat satu dari baseline)
13. Verifikasi scan yang ditolak tidak menaikkan Failed (Failed tetap `0`)

### TC-AC-ACTS-931: Unit yang dilewati karena status berubah di tengah sesi Audit tidak dihitung di Found, Not Found, maupun Popup Detail

14. Tutup modal Event Log dengan klik (X)
15. Klik `[Audit TAG]` di toolbar Tab Available, klik `[Start Scan]`
16. Pindai 4 unit eligible termasuk unit yang akan diaktivasi lewat reader RFID `Zebra RFD40 (SN-2201)`, klik `[Stop]`
17. Aktivasi unit yang ikut terpindai oleh Client di Global Settings lewat sesi API hingga status unit tersimpan
18. Tunggu aksi selesai (tombol aksi aktif kembali)
19. Klik `[Submit]`, biarkan checkbox `D-03` dicentang, klik `[Confirm]`
20. Verifikasi toast memuat klausa `T-08` untuk 1 unit yang dilewati
21. Klik icon `[Event Log]` di toolbar Tab Available, klik tab `Audit TAG`
22. Verifikasi baris sesi terbaru: Found tidak menghitung unit yang dilewati
23. Verifikasi baris sesi terbaru: Not Found hanya menghitung unit Not Scanned yang lolos re-cek
24. Klik (⋯) pada baris sesi terbaru, klik `Detail`
25. Verifikasi unit yang dilewati tidak muncul di Popup Detail
26. Tutup Popup Detail dengan klik (X)

### TC-AC-ACTS-932: Kolom Hardware Tab Audit TAG: nama reader bila reader terdeteksi dan `—` bila tidak

27. Tutup modal Event Log dengan klik (X)
28. Pastikan Handheld Reader `HR-RFID-01` terdeteksi di Sync Panel (simulator reader USB)
29. Klik `[Audit TAG]` di toolbar Tab Available, klik `[Start Scan]`, pindai unit eligible, klik `[Stop]`, klik `[Submit]`
30. Tunggu aksi selesai (tombol aksi aktif kembali)
31. Putuskan Handheld Reader `HR-RFID-01` dari Sync Panel (simulator reader USB)
32. Klik `[Audit TAG]` di toolbar Tab Available, klik `[Start Scan]`, pindai unit eligible, klik `[Stop]`, klik `[Submit]`
33. Tunggu aksi selesai (tombol aksi aktif kembali)
34. Klik icon `[Event Log]` di toolbar Tab Available, klik tab `Audit TAG`
35. Verifikasi sesi dengan reader terdeteksi menampilkan Hardware `Zebra RFD40 (SN-2201)`
36. Verifikasi sesi tanpa reader terdeteksi menampilkan Hardware `—`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; menutup kotak Search lewat `(←)`; mengosongkan Filter lewat `[Clear Field]` dan `[Apply]`; mencatat baseline; dan memulihkan state antar TC supaya TC berikutnya tidak mengandalkan state sebelumnya.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Alasan di atas sekitar 35 langkah: spec ini 36 langkah dihitung dengan ekspansi; ketiga blok memakai simulator pemindai yang sama dan menulis sesi Event Log pada SKU yang sama, dan tiap blok berdiri sendiri; jumlah langkah berasal dari pemindaian, pencatatan baseline, dan Verifikasi per klausa Expected (S-01).
- P-8: TC-AC-ACTS-932 membutuhkan Sync Panel (simulator Handheld Reader USB `HR-RFID-01`) hanya untuk membentuk precondition (reader terdeteksi atau tidak); objek ujinya kolom Hardware Tab Audit TAG, bukan reader USB. Blok USB diletakkan paling akhir sehingga kegagalan keras simulator tidak menutupi blok TC-AC-ACTS-476 dan 931; state antar blok dipulihkan lewat langkah penghubung (Tutup modal dan Popup).
- Penulisan sesi Add Stock dan Audit lain ada di spec 218 dan 220.
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-931 Expected b tidak memberi angka Found dan Not Found; spec mengasersi secara kualitatif (unit dilewati tidak dihitung).
  - TC-AC-ACTS-932 menyebut Hardware `Zebra RFD40 (SN-2201)` untuk sesi dengan "Handheld Reader terdeteksi di Sync Panel", sedangkan Pre-setup #25 menamai reader di Sync Panel `HR-RFID-01`; hubungan keduanya tidak jelas, spec mengikuti rumusan TC.
  - TC-AC-ACTS-476 menyebut "pindai tiga unit lalu satu kode tidak dikenali" tanpa menyebut toast penolakan; spec tidak mengasersi toast.
  - TC-AC-ACTS-931 tidak menyebut cara mengaktivasi unit oleh Client; spec memakai sesi API Client (disediakan tim FE/BE).
  - Cara simulasi reader RFID dan USB tidak didefinisikan di TC, PRD, atau LLD; ditulis "disediakan tim FE".
