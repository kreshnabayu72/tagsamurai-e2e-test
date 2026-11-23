---
id: TC-FA-SU-E2E-257-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-1
title: "Tab Transaction Admin Log: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-776
  - TC-FA-SU-777
  - TC-FA-SU-778
coverage:
  web: automated
---

# Tab Transaction Admin Log: Filter dan Kontrol Filter (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso. Sub-tab Borrow berisi 5 baris sesuai Pre-setup #29 TC: `18/07/26` `Returned · Self-processed` `BRW-2026-0315` `Laptop Dell Latitude - 3` `Rina Wijaya` `General Affairs`; `16/07/26` `Rejected` `BRW-2026-0314` `Projector Epson - 1` `Andi Pratama` `Branch Surabaya`; `15/07/26` `Handed over` `BRW-2026-0313` `Camera Sony A7 - 2` `Budi Santoso` `Logistics Warehouse`; `13/07/26` `Requested` `BRW-2026-0312` `Laptop Dell Latitude - 5` `Dewi Lestari` `Finance & Accounting`; `12/07/26` `Draft created` `—` `Tablet Samsung Tab - 4` `—` `IT Infrastructure`. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Kemampuan teknis: dropdown multi-select, date range picker pada Filter Panel.
- State: yang berubah hanya Filter di sisi klien; filter dibersihkan dengan `[Clear Field]` dan `[Apply]` di antara TC dan di akhir spec. Tidak ada state global dan tidak ada data yang dibuat spec.

## Test Steps

### TC-FA-SU-776: Filter kelas fk, Group

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Klik icon Filter
3. Buka dropdown Group
4. Verifikasi opsi dropdown Group sama dengan nilai DISTINCT data tabel: `Branch Surabaya`, `Finance & Accounting`, `General Affairs`, `IT Infrastructure`, `Logistics Warehouse`
5. Centang `Branch Surabaya`
6. Verifikasi chip `Branch Surabaya` tampil di dalam field Group
7. Klik `[Apply]`
8. Verifikasi tabel menyisakan `BRW-2026-0314` (1 baris)
9. Verifikasi panel Filter tetap terbuka setelah `[Apply]`
10. Klik icon Filter
11. Verifikasi panel Filter tertutup
12. Klik icon Filter
13. Klik `[Clear Field]`
14. Klik `[Apply]`

### TC-FA-SU-777: Filter kelas enum, Activity

15. Buka dropdown Activity
16. Verifikasi opsi dropdown Activity sama dengan nilai DISTINCT kolom Activity pada tabel, mencakup `Draft created`, `Handed over`, `Rejected`, dan `Requested`
17. Centang `Rejected`
18. Verifikasi chip `Rejected` tampil di dalam field Activity
19. Klik `[Apply]`
20. Verifikasi tabel menyisakan `BRW-2026-0314` (1 baris)
21. Verifikasi panel Filter tetap terbuka setelah `[Apply]`
22. Klik icon Filter
23. Verifikasi panel Filter tertutup
24. Klik icon Filter
25. Klik `[Clear Field]`
26. Klik `[Apply]`

### TC-FA-SU-778: Filter kelas date, Date

27. Pilih rentang 12/07/26 sampai 13/07/26 pada Date
28. Klik `[Apply]`
29. Verifikasi rentang inklusif 12/07/26 sampai 13/07/26 menyisakan `BRW-2026-0312` dan `Draft created` (2 baris)
30. Klik `[Clear Field]`
31. Klik `[Apply]`
32. Klik icon Filter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna di User List lalu membuka sub-tab; R-16) serta pembersihan filter dan pembukaan atau penutupan panel di antara TC (langkah 12 sampai 14, 24 sampai 26, 30 sampai 32; S-09). Filter Panel tetap terbuka sesudah `[Apply]` (8b.9), sehingga TC-FA-SU-777 dan TC-FA-SU-778 mengubah filter tanpa membuka panel lagi; langkah 12 dan 24 membuka kembali panel yang ditutup oleh langkah 10 dan 22 (butir Expected b TC-FA-SU-776 dan 777).
- Opsi dropdown pada langkah 4 dan 16 diasersi saat dropdown masih terbuka (8b.5) dan sebelum memilih opsi.
- Temuan untuk QA (S-15): (1) Kolom ACC TC-FA-SU-776 sampai 778 berisi `#20`, yang di Pre-setup adalah Client `FaUserMain`, bukan akun; aktor diambil dari hook suite (Lina Marlina, Pre-setup #1). (2) TC-FA-SU-777 butir a menyebut opsi Activity "mencakup" `Draft created`, `Handed over`, `Rejected`, `Requested`, sedangkan baris `BRW-2026-0315` bernilai Activity `Returned · Self-processed`; TC tidak menyebut apakah opsi untuk baris itu `Returned`, `Returned · Self-processed`, atau tidak ada. Spec mengasersi hanya empat opsi yang disebut TC. (3) TC-FA-SU-778 langkah 3 tidak menyebut cara memilih rentang pada date range picker; spec menulis satu langkah "Pilih rentang". (4) Post Condition tidak ada pada ketiga TC.
