---
id: TC-AC-ACHA-E2E-027-edit-ditolak-saldo-dan-harga
title: "Edit Allocation Ditolak karena Saldo Kantong dan Harga Produk, serta Opsi Pay From Mengikuti Ketersediaan Kantong"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-202
  - TC-AC-ACHA-203
  - TC-AC-ACHA-204
  - TC-AC-ACHA-205
  - TC-AC-ACHA-206
  - TC-AC-ACHA-207
  - TC-AC-ACHA-485
coverage:
  web: automated
---

# Edit Allocation Ditolak karena Saldo Kantong dan Harga Produk, serta Opsi Pay From Mengikuti Ketersediaan Kantong

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Member Distributor toggle ON (MB_ON, Pre-setup #32) `memberOnDistributor_automated_qaTeam1@qwertysystem.net`, nama pengguna Budi Santoso (PIC pada Allocation Log = Budi Santoso), password `Spectra.env.AC_DA_MB_ON_PASSWORD`. Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun di tengah spec: Group Member Partner CV Karya Mandiri toggle ON (MB_P2, Pre-setup #47) `memberOnPartner2_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_P2_PASSWORD`.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, fixture API Pre-setup #20, dan pemulihan preferensi Setup Column di hook `after`.
- Data milik spec (dibuat di hook `before` lewat fixture seeding "disediakan tim FE/BE", dibersihkan di hook `after`; Allocation ID dibaca saat seeding sebagai Dynamic Reference dan dipakai sebagai kata kunci Search):
  - T-A (MB_ON, blok TC-AC-ACHA-202, 485, 203): transaksi Waiting for Approval yang mereplikasi Pre-setup #49 (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00 pada kantong PT Global Distribusi).
  - T-204 (MB_P2, blok TC-AC-ACHA-204): replika Pre-setup #50 (NFC, Quantity 40, Client PT Cipta Kreasi, Pay From `PT Global Distribusi (Distributor)`, Total Cost $60.00, Reserve $60.00 pada kantong A saldo $1,000.00; kantong B `PT ABC (Principal)` saldo $3,000.00, Pre-setup #18 dan #19).
  - T-205 (MB_P2, blok TC-AC-ACHA-205): transaksi serupa T-204 yang dibuat saat hanya kantong A yang tersedia (toggle loncat ke Principal CV Karya Mandiri belum aktif) sehingga snapshot harga tidak memuat harga kantong B.
  - T-206 (MB_P2, blok TC-AC-ACHA-206): transaksi serupa T-204 yang dibuat saat harga NFC di PT ABC belum dikonfigurasi.
  - T-207 (MB_P2, blok TC-AC-ACHA-207): replika Pre-setup #50 dengan toggle loncat ke Principal aktif saat dibuat.
- Kemampuan teknis (fixture API Pre-setup #20, "disediakan tim FE/BE"): (1) menyetel saldo dan Reserved kantong PT Global Distribusi dan kantong B CV Karya Mandiri, serta memulihkannya; (2) menahan Reserve $40.00 pada kantong PT Global Distribusi dari sesi lain (blok TC-AC-ACHA-485), dilepas kembali di akhir blok; (3) mengaktifkan dan mematikan toggle loncat ke Principal CV Karya Mandiri (blok TC-AC-ACHA-205 dan 207); (4) mengonfigurasi harga NFC `$1.20` di PT ABC (blok TC-AC-ACHA-206); (5) membaca Reserved dan saldo kantong serta jumlah entri Allocation Log transaksi (tanpa endpoint karangan, S-13).
- State global: saldo dan Reserved kantong PT Global Distribusi dan kantong B CV Karya Mandiri, toggle loncat ke Principal CV Karya Mandiri, harga NFC di PT ABC, preferensi kolom Setup Column akun MB_ON dan MB_P2; semuanya dipulihkan ke Pre-setup (#3, #5, #14, #16, #18, #19) pada akhir blok masing-masing dan di hook `after`; suite berjalan serial (`parallel: false`).
- Urutan state harga NFC di PT ABC (fixture Pre-setup #20, disediakan tim FE/BE): (1) hook `before` membuat T-206 saat harga NFC PT ABC belum dikonfigurasi, lalu mengonfigurasi harga NFC `$1.20` (nilai Pre-setup #14) sebelum blok TC-204 dimulai, karena langkah 47 menghitung biaya baru $48.00 (40 × $1.20); (2) harga tetap `$1.20` sampai langkah 72, yang memastikan harga NFC `$1.20` terkonfigurasi sebelum Edit T-206 (T-206 sudah dibuat sehingga snapshot harganya tidak memuatnya); (3) harga tetap `$1.20` pada blok TC-207 dan langkah 97 memulihkannya; hook `after` memulihkan state akhir.
- Env var yang dipakai: `AC_DA_MB_ON_PASSWORD`, `AC_DA_MB_P2_PASSWORD` (satu nama satu arti).

## Test Steps

### TC-AC-ACHA-202: Edit dengan saldo kurang untuk biaya baru ditolak, data lama utuh

1. Buka Setup Column, aktifkan kolom Cost, klik `[Save]`
2. Setel saldo kantong PT Global Distribusi menjadi $400.00 dengan Reserved $250.00 lewat fixture hingga tersimpan
3. Ketik Search Allocation ID transaksi T-A, tekan Enter
4. Buka menu row action `⋯` transaksi itu, klik `Edit`
5. Ubah Quantity menjadi `200` (biaya baru $500.00)
6. Verifikasi pesan danger real-time: "Insufficient balance in your pocket. Available: $400.00. Required: $500.00."
7. Verifikasi `[Save]` disabled
8. Arahkan kursor ke `[Save]` yang disabled
9. Verifikasi tidak ada tooltip pada `[Save]` yang disabled
10. Klik `[×]`
11. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
12. Klik `[Leave]`
13. Verifikasi baris transaksi di List: Quantity `100` dan Cost `$250.00` tidak berubah
14. Verifikasi Wallet kantong PT Global Distribusi: Reserved $250.00 tidak berubah

### TC-AC-ACHA-485: Save Edit ditolak server karena saldo kantong berkurang antara cek FE dan commit

15. Buka menu row action `⋯` transaksi T-A, klik `Edit`
16. Ubah Quantity menjadi `160` (biaya baru $400.00)
17. Verifikasi tidak ada pesan saldo kurang
18. Catat jumlah entri Allocation Log transaksi T-A sebagai baseline
19. Dari sesi lain, tahan Reserve $40.00 pada kantong PT Global Distribusi lewat fixture hingga tersimpan
20. Klik `[Save]`
21. Verifikasi pesan inline "Insufficient balance in your pocket. Available: $360.00. Required: $400.00." tampil dengan Available terbaru
22. Verifikasi form Edit tetap terbuka dengan input dipertahankan (Quantity `160`)
23. Verifikasi `[Save]` disabled
24. Verifikasi tidak ada toast dan tidak ada dialog
25. Klik `[×]`
26. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
27. Klik `[Leave]`
28. Verifikasi baris transaksi di List: Quantity `100` dan Cost `$250.00` tidak berubah
29. Verifikasi Wallet kantong PT Global Distribusi: Reserve transaksi tetap $250.00 dan Reserved kantong $290.00 (termasuk $40.00 dari sesi lain)
30. Verifikasi jumlah entri Allocation Log transaksi T-A sama dengan baseline pada langkah 18 (tidak ada entri `Allocation edited by [PIC]` baru)
31. Lepas Reserve $40.00 dari sesi lain lewat fixture hingga tersimpan

### TC-AC-ACHA-203: Edit dengan biaya baru tepat sama dengan saldo tersedia berhasil

32. Buka menu row action `⋯` transaksi T-A, klik `Edit`
33. Ubah Quantity menjadi `160` (biaya baru $400.00)
34. Verifikasi tidak ada pesan saldo kurang
35. Verifikasi `[Save]` enabled
36. Klik `[Save]`
37. Verifikasi toast sukses: "Success, device allocation has been updated."
38. Verifikasi Wallet kantong PT Global Distribusi: Reserved menjadi $400.00
39. Verifikasi Wallet kantong PT Global Distribusi: saldo tersedia $0.00
40. Pulihkan saldo kantong PT Global Distribusi menjadi $20,000.00 dengan Reserved $250.00 lewat fixture hingga tersimpan

### TC-AC-ACHA-204: Ganti Pay From ke kantong dengan saldo kurang ditolak

41. Ganti akun: Logout, login sebagai MB_P2 (Pre-setup #47), buka Allocation > Device Allocation
42. Buka Setup Column, aktifkan kolom Paid From, klik `[Save]`
43. Setel saldo kantong B (`PT ABC (Principal)`) menjadi $10.00 lewat fixture hingga tersimpan
44. Ketik Search Allocation ID transaksi T-204, tekan Enter
45. Buka menu row action `⋯` transaksi itu, klik `Edit`
46. Ganti Pay From menjadi `PT ABC (Principal)` (biaya baru $48.00)
47. Verifikasi pesan danger: "Insufficient balance in your pocket. Available: $10.00. Required: $48.00."
48. Verifikasi `[Save]` disabled
49. Verifikasi Wallet: Reserved kantong A tetap $60.00 dan kantong B tetap $0.00
50. Klik `[×]`
51. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
52. Klik `[Leave]`
53. Pulihkan saldo kantong B menjadi $3,000.00 lewat fixture hingga tersimpan

### TC-AC-ACHA-205: Edit ganti Pay From ke kantong yang baru tersedia tanpa harga pada snapshot ditolak

54. Aktifkan toggle loncat ke Principal untuk CV Karya Mandiri lewat fixture hingga tersimpan (kantong B `PT ABC (Principal)` tersedia, snapshot harga T-205 tidak memuat harganya)
55. Ketik Search Allocation ID transaksi T-205, tekan Enter
56. Catat jumlah entri Allocation Log transaksi T-205 sebagai baseline
57. Buka menu row action `⋯` transaksi itu, klik `Edit`
58. Buka dropdown Pay From
59. Verifikasi dropdown Pay From memuat kantong yang tersedia saat Edit dibuka: `PT Global Distribusi (Distributor)` dan `PT ABC (Principal)`
60. Pilih `PT ABC (Principal)`
61. Klik `[Save]`
62. Verifikasi pesan "Price not set for this item. Please configure product pricing first." tampil inline di bawah field Pay From
63. Verifikasi tidak ada toast dan tidak ada dialog
64. Verifikasi form tetap terbuka dengan input dipertahankan (Pay From `PT ABC (Principal)` tetap terpilih dan Quantity `40`)
65. Verifikasi `[Save]` disabled
66. Klik `[×]`
67. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
68. Klik `[Leave]`
69. Verifikasi baris List: kolom Paid From tetap `PT Global Distribusi (Distributor)`
70. Verifikasi Wallet: Reserve lama utuh, kantong A Reserved $60.00 dan kantong B Reserved $0.00
71. Verifikasi jumlah entri Allocation Log transaksi T-205 sama dengan baseline pada langkah 56 (tidak ada entri log baru)

### TC-AC-ACHA-206: Edit ganti Pay From ke kantong dengan harga yang dikonfigurasi setelah Submit ditolak

72. Konfigurasikan harga NFC di PT ABC `$1.20` lewat fixture hingga tersimpan (setelah T-206 dibuat sehingga snapshot harganya tidak memuatnya)
73. Ketik Search Allocation ID transaksi T-206, tekan Enter
74. Catat jumlah entri Allocation Log transaksi T-206 sebagai baseline
75. Buka menu row action `⋯` transaksi itu, klik `Edit`
76. Buka dropdown Pay From
77. Verifikasi dropdown Pay From memuat kantong yang tersedia saat Edit dibuka: `PT Global Distribusi (Distributor)` dan `PT ABC (Principal)`
78. Pilih `PT ABC (Principal)`
79. Klik `[Save]`
80. Verifikasi pesan "Price not set for this item. Please configure product pricing first." tampil inline di bawah field Pay From
81. Verifikasi tidak ada toast dan tidak ada dialog
82. Verifikasi form tetap terbuka dengan input dipertahankan (Pay From `PT ABC (Principal)` tetap terpilih dan Quantity `40`)
83. Verifikasi `[Save]` disabled
84. Klik `[×]`
85. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
86. Klik `[Leave]`
87. Verifikasi baris List: kolom Paid From tetap `PT Global Distribusi (Distributor)`
88. Verifikasi Wallet: Reserve lama utuh, kantong A Reserved $60.00 dan kantong B Reserved $0.00
89. Verifikasi jumlah entri Allocation Log transaksi T-206 sama dengan baseline pada langkah 74 (tidak ada entri log baru)

### TC-AC-ACHA-207: Opsi Pay From pada Edit mengikuti ketersediaan kantong saat form dibuka

90. Matikan toggle loncat ke Principal untuk CV Karya Mandiri lewat fixture hingga tersimpan (setelah T-207 dibuat)
91. Ketik Search Allocation ID transaksi T-207, tekan Enter
92. Buka menu row action `⋯` transaksi itu, klik `Edit`
93. Buka dropdown Pay From
94. Verifikasi dropdown Pay From memuat opsi `PT Global Distribusi (Distributor)`
95. Verifikasi `PT ABC (Principal)` tidak muncul sebagai opsi
96. Klik `[×]` (form belum diubah sehingga langsung tertutup)
97. Pulihkan toggle loncat ke Principal CV Karya Mandiri menjadi aktif dan harga NFC di PT ABC menjadi `$1.20` lewat fixture hingga tersimpan

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan TC (S-05, S-10): blok TC-AC-ACHA-485 dijalankan sebelum TC-AC-ACHA-203 karena 485 adalah penolakan (diblokir) dan 203 adalah satu-satunya aksi sukses blok MB_ON, yang diletakkan paling akhir sebelum ganti akun. Blok MB_P2 (TC-AC-ACHA-204 s.d. 207) seluruhnya aksi ditolak atau baca saja.
- Langkah penghubung (S-03, R-16): langkah 1 dan 42 (Setup Column; Cost dan Paid From diperlukan untuk asersi baris); langkah 2, 31, 40, 43, 53, 54, 72, 90, 97 (pengaturan dan pemulihan state fixture); langkah 3, 44, 55, 73, 91 (Search Allocation ID untuk menemukan baris target); langkah 18, 56, 74 (baseline jumlah entri Allocation Log, S-12); langkah 10, 12, 25, 27, 50, 52, 66, 68, 84, 86 (menutup form dirty lewat `[×]`, `[Leave]`; `Verifikasi` dialog di langkah 11, 26, 51, 67, 85 diwajibkan S-08); langkah 41 (ganti akun).
- Spec ini melewati sekitar 35 langkah. Alasan: seluruhnya satu topik (Edit ditolak karena saldo atau harga, kondisi data kantong) dan tiap blok memakai transaksi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; ekspansi disebabkan `Verifikasi` dipecah per klausa (S-01) dan penutupan form dirty yang deterministik (S-08).
- P-1 (state berat): asersi "tidak ada entri log baru" pada langkah 30, 71, 89 memakai baseline (S-12) di spec ini karena state-nya dibangun langkah sebelumnya (Edit yang baru saja ditolak server); tidak ada spec absence yang memuat aksi nyata untuk TC-AC-ACHA-485, 205, dan 206.
- Pengecualian S-12: Notes `Batch uji`, nama entitas Pre-setup, dan nilai Pre-setup bernilai literal karena diasersi TC (Lampiran A butir A-6).
- Temuan untuk QA:
  - TC-AC-ACHA-205 dan TC-AC-ACHA-206 memiliki Expected identik; judul membedakan "tanpa harga pada snapshot" versus "harga dikonfigurasi setelah Submit", dan perbedaan itu hanya tertulis di Precondition. Spec mengikuti TC dengan dua blok terpisah.
  - TC-AC-ACHA-205 butir e ("`[Save]` disabled sampai Pay From diganti") tidak menyatakan kondisi saat Pay From diganti kembali ke nilai tersimpan (kantong A); spec hanya mengasersi `[Save]` disabled sesudah penolakan.
  - TC-AC-ACHA-205 dan TC-AC-ACHA-206 menyatakan pesan "Price not set for this item. Please configure product pricing first." untuk kantong B padahal Pre-setup #14 memuat harga PT ABC; spec mengikuti precondition TC (harga tidak ada pada snapshot).
  - TC-AC-ACHA-206 menulis harga NFC dikonfigurasi "setelah Submit", sedangkan TC-AC-ACHA-204 pada spec yang sama membutuhkan harga NFC `$1.20` terkonfigurasi (langkah 47); kedua kondisi hanya konsisten bila T-206 dibuat saat harga belum dikonfigurasi (hook `before`) dan harga dikonfigurasi sebelum blok TC-204, sehingga langkah 72 menjadi penegasan. Urutan ini adalah pilihan spec dan bergantung pada kemampuan fixture membuat transaksi pada state harga tertentu.
  - Kontrak fixture (pengaturan saldo dan Reserved kantong, penahan Reserve sesi lain, toggle loncat ke Principal, harga NFC, pembuatan transaksi dengan state pembuatan khusus, baca Reserved dan jumlah entri Allocation Log) tidak tertulis di TC, PRD, atau LLD; ditulis "disediakan tim FE/BE" (R-19, S-13).
  - TC-AC-ACHA-202 butir c menyatakan penyebab `[Save]` disabled "dijelaskan oleh pesan inline"; klausa ini identik dengan butir a sehingga hanya "tidak ada tooltip" yang punya langkah `Verifikasi` tersendiri (langkah 9).
  - Post Condition TC-AC-ACHA-203 ("Wallet Balance dan Wallet Transaction List (Reserve disesuaikan), Approvals Active Tab (data subject terbaru)") tanpa langkah observasi di TC: tidak diasersi.
