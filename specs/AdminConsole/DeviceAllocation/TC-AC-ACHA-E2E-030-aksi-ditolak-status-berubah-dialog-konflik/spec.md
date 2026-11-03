---
id: TC-AC-ACHA-E2E-030-aksi-ditolak-status-berubah-dialog-konflik
title: "Cancel dan Edit Ditolak Server karena Status Transaksi Sudah Berubah: Dialog Konflik Allocation Changed"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-230
  - TC-AC-ACHA-231
  - TC-AC-ACHA-232
  - TC-AC-ACHA-451
  - TC-AC-ACHA-452
  - TC-AC-ACHA-453
  - TC-AC-ACHA-454
coverage:
  web: automated
---

# Cancel dan Edit Ditolak Server karena Status Transaksi Sudah Berubah: Dialog Konflik Allocation Changed

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Group Member Distributor toggle ON (MB_ON, Pre-setup #32) `memberOnDistributor_automated_qaTeam1@qwertysystem.net`, nama pengguna Budi Santoso (PIC pada Allocation Log = Budi Santoso), password `Spectra.env.AC_DA_MB_ON_PASSWORD`. Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Satu sesi UI saja sepanjang spec.
- Pelaku kedua (sesi API, bukan sesi UI): Approver Total Control Distributor (TC_DIST, Pre-setup #27) `totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_DIST_PASSWORD`, untuk Approve dan Reject (aksi di Approvals > Device Allocation dilakukan lewat sesi API); sesi API MB_ON untuk Cancel oleh creator (TC-AC-ACHA-453).
- Hook suite: sesi API aktor, flag Guided Tooltip, pemulihan preferensi Setup Column, seed 30 baris idempotent (Lampiran A butir A-11), dan fixture API Pre-setup #20 dinyatakan di `suite.md`. Hook `after` memulihkan jam server dan seed lewat fixture Pre-setup #20.
- Data milik spec (dibuat lewat fixture seeding "disediakan tim FE/BE" di awal tiap blok, dibersihkan di hook `after`; Allocation ID dan waktu terbit T1 dibaca saat seeding sebagai Dynamic Reference): satu transaksi Waiting for Approval baru dibuat MB_ON per blok yang mereplikasi Pre-setup #49 (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00 pada kantong PT Global Distribusi saldo $20,000.00). Notes `Batch uji` literal karena replika Pre-setup dan Rejection Reason `Stok belum siap` literal karena diasersi TC (pengecualian S-12, Lampiran A butir A-11).
- Konfigurasi: Approval Timeout platform-wide 3 day(s) (Pre-setup #63) untuk blok TC-AC-ACHA-232 dan 454.
- Kemampuan teknis: (1) sesi API Approve, Reject (Rejection Reason `Stok belum siap`), dan Cancel oleh creator, masing-masing "disediakan tim FE/BE" (kontrak endpoint tidak tertulis di TC, PRD, atau LLD; tidak ada toast pada sesi API); (2) fixture Pre-setup #20 untuk menggeser jam server absolut ke T1 + 3 hari + 1 menit (T1 dibaca dari waktu terbit transaksi saat seeding, margin kurang dari 5 menit sehingga dihitung dari T1), menunggu satu siklus job Timeout Auto-Cancel lewat polling fixture status job tiap 5 detik (batas 2 menit; kelas timing eventual), dan memulihkan jam server; hanya jam server yang diatur karena Timeout dihitung murni di server dan tidak diamati lewat countdown UI; (3) kemampuan membaca Status, Quantity, Capture, Reserved, saldo kantong, dan jumlah entri Allocation Log transaksi (disediakan tim FE/BE, tanpa endpoint karangan, S-13); (4) sesi UI dan sesi API tetap valid selama jam server digeser pada langkah 75 sampai 79 dan 90 sampai 95 (dinyatakan di `suite.md`).
- State global: jam server (digeser pada blok TC-AC-ACHA-232 dan 454, dipulihkan segera sesudah job selesai dan di hook `after`); suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_DA_MB_ON_PASSWORD`, `AC_DA_TC_DIST_PASSWORD` (satu nama satu arti).

## Test Steps

### TC-AC-ACHA-230: Cancel pada transaksi yang sudah berstatus Completed ditolak dengan dialog konflik

1. Siapkan transaksi T-230 lewat fixture seeding hingga tersimpan, muat ulang halaman (F5), lalu ketik Search Allocation ID transaksi itu, tekan Enter
2. Buka menu row action `⋯` transaksi itu, klik `Cancel Allocation`
3. Lewat sesi API TC_DIST (Approver), setujui transaksi T-230 hingga status `Completed` tersimpan
4. Catat jumlah entri Allocation Log transaksi T-230 sebagai baseline
5. Kembali ke dialog Cancel Allocation yang masih terbuka, klik `[Cancel Allocation]`
6. Verifikasi dialog konflik berjudul "Allocation Changed" dengan body "This allocation was changed by someone else. Please review." dan footer satu tombol `[OK]`
7. Verifikasi tidak ada toast sukses
8. Klik `[OK]` pada dialog konflik
9. Verifikasi dialog konflik tertutup
10. Verifikasi dialog Cancel Allocation di belakangnya tertutup
11. Verifikasi List dimuat ulang tanpa data basi: baris transaksi menampilkan Status `Completed`
12. Verifikasi Status transaksi T-230 tetap `Completed` (data server tidak diubah oleh Cancel)
13. Verifikasi jumlah entri Allocation Log transaksi T-230 sama dengan baseline pada langkah 4 (tidak ada entri log baru)

### TC-AC-ACHA-231: Cancel pada transaksi yang sudah berstatus Rejected ditolak dengan dialog konflik

14. Siapkan transaksi T-231 lewat fixture seeding hingga tersimpan, muat ulang halaman (F5), lalu ganti isi kotak search dengan Allocation ID transaksi itu, tekan Enter
15. Buka menu row action `⋯` transaksi itu, klik `Cancel Allocation`
16. Lewat sesi API TC_DIST (Approver), tolak transaksi T-231 dengan Rejection Reason `Stok belum siap` hingga status `Rejected` tersimpan
17. Catat jumlah entri Allocation Log transaksi T-231 sebagai baseline
18. Kembali ke dialog Cancel Allocation yang masih terbuka, klik `[Cancel Allocation]`
19. Verifikasi dialog konflik berjudul "Allocation Changed" dengan body "This allocation was changed by someone else. Please review." dan footer satu tombol `[OK]`
20. Verifikasi tidak ada toast sukses
21. Klik `[OK]` pada dialog konflik
22. Verifikasi dialog konflik tertutup
23. Verifikasi dialog Cancel Allocation di belakangnya tertutup
24. Verifikasi List dimuat ulang tanpa data basi: baris transaksi menampilkan Status `Rejected`
25. Verifikasi Status transaksi T-231 tetap `Rejected` (data server tidak diubah oleh Cancel)
26. Verifikasi jumlah entri Allocation Log transaksi T-231 sama dengan baseline pada langkah 17 (tidak ada entri log baru)

### TC-AC-ACHA-451: Edit setelah Approve ditolak sebagai konflik status

27. Siapkan transaksi T-451 lewat fixture seeding hingga tersimpan, muat ulang halaman (F5), lalu ganti isi kotak search dengan Allocation ID transaksi itu, tekan Enter
28. Buka menu row action `⋯` transaksi itu, klik `Edit`
29. Lewat sesi API TC_DIST (Approver), setujui transaksi T-451 hingga status `Completed` tersimpan
30. Catat jumlah entri Allocation Log transaksi T-451 serta Quantity dan Capture transaksi sebagai baseline
31. Ubah Quantity menjadi `120`
32. Klik `[Save]`
33. Verifikasi dialog konflik berjudul "Allocation Changed" dengan body "This allocation was changed by someone else. Please review." dan footer satu tombol `[OK]`
34. Klik `[OK]` pada dialog konflik
35. Verifikasi dialog konflik tertutup
36. Verifikasi form Edit Allocation di belakangnya tertutup
37. Verifikasi dialog `Unsaved Changes` tidak muncul
38. Verifikasi List dimuat ulang tanpa data basi: baris transaksi menampilkan Status `Completed`
39. Verifikasi Status transaksi T-451 tetap `Completed`
40. Verifikasi Quantity transaksi sama dengan baseline pada langkah 30 (`100`)
41. Verifikasi Capture transaksi sama dengan baseline pada langkah 30 ($250.00)
42. Verifikasi jumlah entri Allocation Log transaksi T-451 sama dengan baseline pada langkah 30 (tidak ada entri log Edit)

### TC-AC-ACHA-452: Edit setelah Reject ditolak sebagai konflik status

43. Siapkan transaksi T-452 lewat fixture seeding hingga tersimpan, muat ulang halaman (F5), lalu ganti isi kotak search dengan Allocation ID transaksi itu, tekan Enter
44. Buka menu row action `⋯` transaksi itu, klik `Edit`
45. Lewat sesi API TC_DIST (Approver), tolak transaksi T-452 dengan Rejection Reason `Stok belum siap` hingga status `Rejected` tersimpan
46. Catat jumlah entri Allocation Log transaksi T-452 sebagai baseline
47. Ubah Quantity menjadi `120`
48. Klik `[Save]`
49. Verifikasi dialog konflik berjudul "Allocation Changed" dengan body "This allocation was changed by someone else. Please review." dan footer satu tombol `[OK]`
50. Klik `[OK]` pada dialog konflik
51. Verifikasi dialog konflik tertutup
52. Verifikasi form Edit Allocation di belakangnya tertutup
53. Verifikasi dialog `Unsaved Changes` tidak muncul
54. Verifikasi List dimuat ulang tanpa data basi: baris transaksi menampilkan Status `Rejected`
55. Verifikasi Status transaksi T-452 tetap `Rejected` dan Quantity tetap `100`
56. Verifikasi Wallet kantong PT Global Distribusi: Reserved $0.00 dan saldo $20,000.00
57. Verifikasi jumlah entri Allocation Log transaksi T-452 sama dengan baseline pada langkah 46 (tidak ada entri log Edit)

### TC-AC-ACHA-453: Edit setelah Cancel oleh creator sendiri ditolak sebagai konflik status

58. Siapkan transaksi T-453 lewat fixture seeding hingga tersimpan, muat ulang halaman (F5), lalu ganti isi kotak search dengan Allocation ID transaksi itu, tekan Enter
59. Buka menu row action `⋯` transaksi itu, klik `Edit`
60. Lewat sesi API MB_ON (creator), batalkan transaksi T-453 hingga status `Canceled` tersimpan
61. Catat jumlah entri Allocation Log transaksi T-453 sebagai baseline
62. Ubah Quantity menjadi `120`
63. Klik `[Save]`
64. Verifikasi dialog konflik berjudul "Allocation Changed" dengan body "This allocation was changed by someone else. Please review." dan footer satu tombol `[OK]`
65. Klik `[OK]` pada dialog konflik
66. Verifikasi dialog konflik tertutup
67. Verifikasi form Edit Allocation di belakangnya tertutup
68. Verifikasi dialog `Unsaved Changes` tidak muncul
69. Verifikasi List dimuat ulang tanpa data basi: baris transaksi menampilkan Status `Canceled`
70. Verifikasi Status transaksi T-453 tetap `Canceled` dan Quantity tetap `100`
71. Verifikasi Wallet kantong PT Global Distribusi: Reserved $0.00 dan saldo $20,000.00
72. Verifikasi jumlah entri Allocation Log transaksi T-453 sama dengan baseline pada langkah 61 (tidak ada entri log Edit)

### TC-AC-ACHA-232: Cancel pada transaksi yang sudah berstatus Canceled ditolak dengan dialog konflik

73. Siapkan transaksi T-232 lewat fixture seeding hingga tersimpan (catat waktu terbit T1), muat ulang halaman (F5), lalu ganti isi kotak search dengan Allocation ID transaksi itu, tekan Enter
74. Buka menu row action `⋯` transaksi itu, klik `Cancel Allocation`
75. Geser jam server ke T1 + 3 hari + 1 menit lewat fixture Pre-setup #20
76. Tunggu hingga fixture status job melaporkan transaksi T-232 berstatus `Canceled` oleh Timeout Auto-Cancel (polling tiap 5 detik, batas 2 menit)
77. Pulihkan jam server lewat fixture hingga tersimpan
78. Catat jumlah entri Allocation Log transaksi T-232 sebagai baseline
79. Kembali ke dialog Cancel Allocation yang masih terbuka, klik `[Cancel Allocation]`
80. Verifikasi dialog konflik berjudul "Allocation Changed" dengan body "This allocation was changed by someone else. Please review." dan footer satu tombol `[OK]`
81. Verifikasi tidak ada toast sukses
82. Klik `[OK]` pada dialog konflik
83. Verifikasi dialog konflik tertutup
84. Verifikasi dialog Cancel Allocation di belakangnya tertutup
85. Verifikasi List dimuat ulang tanpa data basi: baris transaksi menampilkan Status `Canceled`
86. Verifikasi Status transaksi T-232 tetap `Canceled`
87. Verifikasi jumlah entri Allocation Log transaksi T-232 sama dengan baseline pada langkah 78 (tidak ada entri log baru)

### TC-AC-ACHA-454: Edit setelah Timeout Auto-Cancel ditolak sebagai konflik status

88. Siapkan transaksi T-454 lewat fixture seeding hingga tersimpan (catat waktu terbit T1), muat ulang halaman (F5), lalu ganti isi kotak search dengan Allocation ID transaksi itu, tekan Enter
89. Buka menu row action `⋯` transaksi itu, klik `Edit`
90. Geser jam server ke T1 + 3 hari + 1 menit lewat fixture Pre-setup #20
91. Tunggu hingga fixture status job melaporkan transaksi T-454 berstatus `Canceled` oleh Timeout Auto-Cancel (polling tiap 5 detik, batas 2 menit)
92. Pulihkan jam server lewat fixture hingga tersimpan
93. Catat jumlah entri Allocation Log transaksi T-454 sebagai baseline
94. Ubah Quantity menjadi `120`
95. Klik `[Save]`
96. Verifikasi dialog konflik berjudul "Allocation Changed" dengan body "This allocation was changed by someone else. Please review." dan footer satu tombol `[OK]`
97. Klik `[OK]` pada dialog konflik
98. Verifikasi dialog konflik tertutup
99. Verifikasi form Edit Allocation di belakangnya tertutup
100. Verifikasi dialog `Unsaved Changes` tidak muncul
101. Verifikasi List dimuat ulang tanpa data basi: baris transaksi menampilkan Status `Canceled`
102. Verifikasi Status transaksi T-454 tetap `Canceled` dan Quantity tetap `100`
103. Verifikasi Wallet kantong PT Global Distribusi: Reserved $0.00 dan saldo $20,000.00
104. Verifikasi jumlah entri Allocation Log transaksi T-454 sama dengan baseline pada langkah 93 (tidak ada entri log Edit)

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan TC (S-05, S-10): blok yang tidak mengatur jam server (TC-AC-ACHA-230, 231, 451, 452, 453) berjalan lebih dulu; dua blok yang menggeser jam server (TC-AC-ACHA-232, 454) di akhir supaya jam dipulihkan dalam rangkaian terakhir (S-09). Tiap blok memakai transaksi sendiri.
- Pelaku kedua memakai sesi API (pengecualian aturan pelaku kedua): bukan konteks kedua kelas c, tidak memakai `P-2` untuk konteks kedua, dan tidak ada sesi UI kedua; hasil yang diasersi hanya di sesi UI. Karena sesi API tidak menampilkan toast, "sampai toast sukses" pada langkah TC dipenuhi dengan "hingga status ... tersimpan".
- P-2 (pemicu bukan objek uji): proses job latar Timeout Auto-Cancel pada TC-AC-ACHA-232 dan 454 (langkah 75 sampai 77 dan 90 sampai 92) hanya memicu kondisi status `Canceled` yang diuji; objek uji tetap penolakan Cancel atau Edit oleh server dan dialog konflik. Jam server dipulihkan segera sesudah job selesai.
- P-1 (state berat): asersi "tidak ada entri log baru" pada langkah 13, 26, 42, 57, 72, 87, 104 memakai baseline yang dicatat sesudah aksi pelaku kedua (karena Approve, Reject, Cancel oleh creator, dan Timeout Auto-Cancel sendiri mencatat entri) di spec ini, karena state-nya dibangun langkah sebelumnya pada transaksi yang sama; tidak ada spec absence yang memuat aksi nyata untuk TC ini.
- Langkah penghubung (S-03, R-16): langkah 1 (juga 14, 27, 43, 58, 73, 88): membuat transaksi baru, muat ulang, dan Search Allocation ID untuk menemukan baris target; langkah 4, 17, 30, 46, 61, 78, 93 (baseline jumlah entri Allocation Log setelah aksi pelaku kedua, S-12); langkah 75 sampai 77 dan 90 sampai 92 (mengatur dan memulihkan jam server, polling status job).
- Spec ini melewati sekitar 35 langkah. Alasan: seluruhnya satu topik (penolakan server atas Cancel atau Edit karena status berubah) dengan satu pola dialog konflik; tiap blok memakai transaksi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan `Verifikasi` dipecah per klausa (S-01).
- Temuan untuk QA:
  - Judul dialog konflik "Allocation Changed" adalah inferensi dari pola sibling `Device Changed` (Catatan TC) dan belum dikonfirmasi user; spec memakai teks persis TC.
  - TC-AC-ACHA-451 Expected b memakai istilah "Capture tetap $250.00" yang tidak didefinisikan di TC (Wallet Balance memakai Reserved dan saldo); spec membacanya sebagai nilai Capture yang dibaca lewat kemampuan baca fixture.
  - TC-AC-ACHA-230 dan 231 dan 232 Expected a menyatakan "List dimuat ulang tanpa data basi" tanpa cara observasi; spec mengasersinya lewat Status baris List yang sudah berubah.
  - Langkah TC "Di sesi lain, Approver ... sampai toast sukses" (TC-AC-ACHA-230, 231, 451, 452) dan "creator membatalkan ... sampai toast sukses" (TC-AC-ACHA-453) mengasumsikan sesi UI kedua; spec memakai sesi API hingga status tersimpan. Kontrak sesi API Approve, Reject, dan Cancel serta fixture status job tidak tertulis di TC, PRD, atau LLD; ditulis "disediakan tim FE/BE" (R-19, S-13).
  - TC-AC-ACHA-232 dan 454 tidak menyatakan interval pengecekan job (PRD tidak menulisnya); spec memakai polling 5 detik dengan batas 2 menit sebagai pilihan spec.
  - Post Condition TC-AC-ACHA-230, 231, 232, 451, 452, 453, 454 bernilai `-`: tidak ada yang diasersi tambahan.
