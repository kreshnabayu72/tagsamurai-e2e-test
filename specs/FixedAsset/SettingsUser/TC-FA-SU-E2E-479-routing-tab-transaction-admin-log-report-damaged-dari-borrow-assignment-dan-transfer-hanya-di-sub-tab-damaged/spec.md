---
id: TC-FA-SU-E2E-479-routing-tab-transaction-admin-log-report-damaged-dari-borrow-assignment-dan-transfer-hanya-di-sub-tab-damaged
title: "Routing Tab Transaction Admin Log: Report Damaged dari Borrow, Assignment, dan Transfer Hanya di Sub-tab Damaged dengan Source Asal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1192
coverage:
  web: automated
---

# Routing Tab Transaction Admin Log: Report Damaged dari Borrow, Assignment, dan Transfer Hanya di Sub-tab Damaged dengan Source Asal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Pelaku kedua Budi Santoso (Pelapor admin) bertindak lewat sesi API; aktor Lina Marlina mengamati Tab Transaction Admin Log. Sesi pelaku kedua hanya memicu state tanpa asersi di dalamnya. Akun pelaku kedua disediakan tim FE: Budi Santoso `Spectra.env.FA_BUDI_PASSWORD` (nama usulan).
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Damaged berisi 4 baris sesuai Pre-setup #29 TC (Damaged: `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`). Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed aset khusus spec ini (disediakan tim FE lewat seed API di hook `before`, dihapus di hook `after`, tidak memengaruhi Pre-setup #29): `Projector Epson - 3` (Borrow berjalan), `Monitor LG 24 - 9` (Assignment berjalan), dan `Printer HP LaserJet - 5` (Transfer siap Receive), masing-masing tanpa Damage record.
- Kemampuan transaksi lintas modul (disediakan tim FE/BE, tanpa endpoint karangan): Report Damaged dari halaman Borrow, dari halaman Assignment, dan saat Receive dari halaman Transfer; dijalankan lewat sesi API, ditulis "... hingga ... tersimpan" (R-20). Entri log yang tercipta pada Tab Transaction Admin Log bersifat permanen dan tidak dibersihkan; hitungan memakai baseline relatif (S-12).
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Catat jumlah baris sub-tab Borrow sebagai baseline
3. Klik Sub-tab Assignment
4. Catat jumlah baris sub-tab Assignment sebagai baseline
5. Klik Sub-tab Transfer
6. Catat jumlah baris sub-tab Transfer sebagai baseline
7. Klik Sub-tab Damaged
8. Catat jumlah baris sub-tab Damaged sebagai baseline
9. Lakukan Report Damaged atas `Projector Epson - 3` yang sedang dipinjam sebagai Budi Santoso (Pelapor admin) dari halaman Borrow lewat sesi API hingga laporan tersimpan
10. Lakukan Report Damaged atas `Monitor LG 24 - 9` yang sedang ditugaskan sebagai Budi Santoso dari halaman Assignment lewat sesi API hingga laporan tersimpan
11. Lakukan Report Damaged saat Receive atas `Printer HP LaserJet - 5` sebagai Budi Santoso dari halaman Transfer lewat sesi API hingga laporan tersimpan
12. Tunggu aksi selesai, lalu tekan F5 pada halaman Detail
13. Klik Sub-tab Damaged
14. Verifikasi baris `Projector Epson - 3` tampil dengan Activity `Reported damaged` dan Source `Borrowed asset`
15. Verifikasi baris `Monitor LG 24 - 9` tampil dengan Activity `Reported damaged` dan Source `Assigned asset`
16. Verifikasi baris `Printer HP LaserJet - 5` tampil dengan Activity `Reported damaged` dan Source `Transfer receive`
17. Verifikasi Group ketiga baris itu adalah grup aset saat tindakan
18. Verifikasi Date ketiga baris itu adalah tanggal hari aksi
19. Verifikasi jumlah baris sub-tab Damaged bertambah tepat tiga dari baseline
20. Verifikasi keempat baris Pre-setup #29 sub-tab Damaged tidak berubah: `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`
21. Klik Sub-tab Borrow
22. Verifikasi jumlah baris sub-tab Borrow sama dengan baseline
23. Klik icon Filter lalu buka dropdown `Activity`
24. Verifikasi opsi dropdown `Activity` tidak memuat `Reported damaged`
25. Klik icon Filter untuk menutup panel
26. Klik Sub-tab Assignment
27. Verifikasi jumlah baris sub-tab Assignment sama dengan baseline
28. Klik icon Filter lalu buka dropdown `Activity`
29. Verifikasi opsi dropdown `Activity` tidak memuat `Reported damaged`
30. Klik icon Filter untuk menutup panel
31. Klik Sub-tab Transfer
32. Verifikasi jumlah baris sub-tab Transfer sama dengan baseline
33. Klik icon Filter lalu buka dropdown `Activity`
34. Verifikasi opsi dropdown `Activity` tidak memuat `Reported damaged`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pencatatan baseline jumlah baris (S-12), pemicuan state lewat sesi API (R-20), pemuatan ulang halaman Detail, pembukaan panel Filter dan dropdown, serta perpindahan sub-tab dan halaman.
- Pembagian TC lintas spec: Report Missing dari halaman Borrow, Assignment, Transfer, dan Task Detail Audit (TC-FA-SU-1193) ada di spec 480; pelapor non-admin dan Cancel Report (TC-FA-SU-1194 sampai 1196) ada di spec 481 dan 482.
- Klausa absence ("tidak menambah baris" dan opsi Filter tanpa `Reported damaged`) ditulis sebagai asersi jumlah terhadap baseline yang dicatat sebelum pemicu (S-12); anchor positif adalah tiga baris `Reported damaged` di sub-tab Damaged yang diverifikasi sebelumnya (8b.2).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1192 menyebut aksi "Sebagai Budi Santoso ... lakukan Report Damaged" lewat UI modul lain tanpa menyatakan akun atau jalur aksi; spec memicunya lewat sesi API (R-20) karena objek asersi adalah baris di Tab Transaction Admin Log aktor. (2) Nama aset seed memakai literal TC (`Projector Epson - 3`, `Monitor LG 24 - 9`, `Printer HP LaserJet - 5`); increment dibangkitkan sistem sehingga seed harus menjamin nama itu. (3) Nilai Source `Borrowed asset`, `Assigned asset`, dan `Transfer receive` bersumber dari Expected a TC-FA-SU-1192 dan Pre-setup #29. (4) Seed khusus TC dinyatakan tidak memengaruhi Pre-setup #29, tetapi aksinya menulis tiga baris baru ke log Budi Santoso yang juga dibaca spec 468 sampai 475; asersi jumlah memakai baseline relatif.
