---
id: TC-AC-ACHA-E2E-026-edit-sukses-reserve-disesuaikan
title: "Edit Allocation Berhasil: Quantity, Notes, Pay From, Snapshot Harga, Principal, dan Reserve Disesuaikan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-196
  - TC-AC-ACHA-197
  - TC-AC-ACHA-198
  - TC-AC-ACHA-199
  - TC-AC-ACHA-200
  - TC-AC-ACHA-201
  - TC-AC-ACHA-208
coverage:
  web: automated
---

# Edit Allocation Berhasil: Quantity, Notes, Pay From, Snapshot Harga, Principal, dan Reserve Disesuaikan

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Member Distributor toggle ON (MB_ON, Pre-setup #32) `memberOnDistributor_automated_qaTeam1@qwertysystem.net`, nama pengguna Budi Santoso (PIC pada Allocation Log = Budi Santoso), password `Spectra.env.AC_DA_MB_ON_PASSWORD`. Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun di tengah spec: Group Member Partner CV Karya Mandiri toggle ON (MB_P2, Pre-setup #47) `memberOnPartner2_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_P2_PASSWORD`; Group Member Principal toggle ON (MB_PRIN, Pre-setup #24) `memberOnPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_PRIN_PASSWORD`.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, fixture API Pre-setup #20, dan pemulihan preferensi Setup Column di hook `after`.
- Data milik spec (dibuat di hook `before` lewat fixture seeding "disediakan tim FE/BE", dibersihkan di hook `after`): (1) transaksi Waiting for Approval dibuat MB_ON yang mereplikasi Pre-setup #49 (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00 pada kantong PT Global Distribusi saldo $20,000.00), dipulihkan ke keadaan awal itu lewat fixture sebelum tiap blok MB_ON; (2) transaksi Waiting for Approval dibuat MB_P2 yang mereplikasi Pre-setup #50 (NFC, Quantity 40, Client PT Cipta Kreasi, Pay From `PT Global Distribusi (Distributor)`, Total Cost $60.00, Reserve $60.00 pada kantong A saldo $1,000.00; kantong B saldo $3,000.00, Pre-setup #18 dan #19); (3) transaksi Waiting for Approval dibuat MB_PRIN yang mereplikasi Pre-setup #51 (Handheld Reader Long Range, Quantity 10, Client PT Manufaktur Unggul, Payment Free). Allocation ID dibaca saat seeding (Dynamic Reference) dan dipakai sebagai kata kunci Search; Notes `Batch uji` literal karena diasersi TC (pengecualian S-12, Lampiran A butir A-6).
- Kemampuan teknis: (1) fixture API Pre-setup #20 untuk memulihkan transaksi, mengubah harga produk, dan memulihkannya; (2) kemampuan membaca Reserved dan saldo kantong serta jumlah entri Allocation Log transaksi (disediakan tim FE/BE, tanpa endpoint karangan, S-13); (3) jam server dan jam browser sinkron untuk asersi Last Updated (toleransi satu menit).
- State global: harga RFID Object TAG di PT ABC (diubah menjadi $3.00 pada blok TC-AC-ACHA-208, dipulihkan ke $2.50 di akhir blok dan di hook `after`); preferensi kolom Setup Column akun MB_ON, MB_P2, dan MB_PRIN (dipulihkan hook `after`); suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_DA_MB_ON_PASSWORD`, `AC_DA_MB_P2_PASSWORD`, `AC_DA_MB_PRIN_PASSWORD` (satu nama satu arti).

## Test Steps

1. Buka Setup Column, aktifkan kolom Notes, Cost, dan Paid From, klik `[Save]`

### TC-AC-ACHA-196: Edit menaikkan Quantity: Reserve disesuaikan dengan snapshot harga

2. Ketik Search Allocation ID transaksi milik spec, tekan Enter
3. Catat jumlah entri Allocation Log transaksi itu sebagai baseline
4. Buka menu row action `⋯` transaksi itu, klik `Edit`
5. Ubah Quantity menjadi `150`
6. Verifikasi Preview `Estimated Cost` `$375.00 (150 × $2.50/unit)`
7. Klik `[Save]`
8. Verifikasi toast sukses: "Success, device allocation has been updated."
9. Verifikasi form Edit tertutup
10. Catat waktu sesudah Save
11. Verifikasi baris List: Quantity `150`
12. Verifikasi baris List: Cost `$375.00`
13. Verifikasi baris List: Status tetap `Waiting for Approval`
14. Verifikasi baris List: Last Updated berubah ke waktu Save (toleransi satu menit terhadap waktu pada langkah 10)
15. Verifikasi Wallet kantong PT Global Distribusi: Reserved menjadi $375.00 (disesuaikan dari $250.00)
16. Verifikasi Wallet kantong PT Global Distribusi: saldo $20,000.00 tidak berubah
17. Buka menu row action `⋯` transaksi itu, klik `Allocation Log`
18. Verifikasi jumlah entri bertambah satu dari baseline pada langkah 3 dan entri baru `Allocation edited by [PIC]` memuat `Quantity: 150` dan `Cost: $375.00`
19. Tutup modal Allocation Log

### TC-AC-ACHA-197: Edit menurunkan Quantity: Reserve turun

20. Pulihkan transaksi milik spec ke keadaan awal lewat fixture hingga tersimpan, muat ulang halaman (F5), lalu ketik Search Allocation ID transaksi itu, tekan Enter
21. Buka menu row action `⋯` transaksi itu, klik `Edit`
22. Ubah Quantity menjadi `60`
23. Klik `[Save]`
24. Verifikasi toast sukses: "Success, device allocation has been updated."
25. Verifikasi baris List: Quantity `60`
26. Verifikasi baris List: Cost `$150.00`
27. Verifikasi Wallet kantong PT Global Distribusi: Reserved menjadi $150.00 (turun dari $250.00)

### TC-AC-ACHA-198: Edit hanya Notes tidak mengubah biaya dan Reserve

28. Pulihkan transaksi milik spec ke keadaan awal lewat fixture hingga tersimpan, muat ulang halaman (F5), lalu ketik Search Allocation ID transaksi itu, tekan Enter
29. Catat jumlah entri Allocation Log transaksi itu sebagai baseline
30. Buka menu row action `⋯` transaksi itu, klik `Edit`
31. Ubah Notes dari `Batch uji` menjadi `Batch revisi`
32. Klik `[Save]`
33. Verifikasi toast sukses: "Success, device allocation has been updated."
34. Verifikasi kolom Notes menjadi `Batch revisi`
35. Verifikasi Quantity `100` dan Cost `$250.00` tidak berubah
36. Verifikasi Wallet kantong PT Global Distribusi: Reserved $250.00 tidak berubah
37. Buka menu row action `⋯` transaksi itu, klik `Allocation Log`
38. Verifikasi jumlah entri bertambah satu dari baseline pada langkah 29 dan entri baru `Allocation edited by [PIC]` memuat `Notes: Batch revisi`
39. Tutup modal Allocation Log

### TC-AC-ACHA-200: Edit beberapa field sekaligus

40. Pulihkan transaksi milik spec ke keadaan awal lewat fixture hingga tersimpan, muat ulang halaman (F5), lalu ketik Search Allocation ID transaksi itu, tekan Enter
41. Catat jumlah entri Allocation Log transaksi itu sebagai baseline
42. Buka menu row action `⋯` transaksi itu, klik `Edit`
43. Ubah Quantity menjadi `120` dan Notes menjadi `Revisi ganda`
44. Klik `[Save]`
45. Verifikasi toast sukses: "Success, device allocation has been updated."
46. Verifikasi baris List: Quantity `120`
47. Verifikasi baris List: Cost `$300.00`
48. Verifikasi baris List: Notes `Revisi ganda`
49. Buka menu row action `⋯` transaksi itu, klik `Allocation Log`
50. Verifikasi jumlah entri bertambah tepat satu dari baseline pada langkah 41 dan entri baru `Allocation edited by [PIC]` memuat `Quantity: 120`, `Notes: Revisi ganda`, dan `Cost: $300.00`
51. Tutup modal Allocation Log

### TC-AC-ACHA-208: Edit memakai snapshot harga transaksi pertama

52. Pulihkan transaksi milik spec ke keadaan awal lewat fixture hingga tersimpan, muat ulang halaman (F5), lalu ketik Search Allocation ID transaksi itu, tekan Enter
53. Ubah harga RFID Object TAG di PT ABC dari $2.50 menjadi $3.00 lewat fixture hingga tersimpan
54. Buka menu row action `⋯` transaksi itu, klik `Edit`
55. Verifikasi `Unit Price (Snapshot)` pada Preview tetap `$2.50/unit`
56. Ubah Quantity menjadi `120`
57. Klik `[Save]`
58. Tunggu form Edit tertutup
59. Verifikasi baris List: Cost `$300.00` (120 × $2.50 snapshot), bukan $360.00
60. Verifikasi Wallet kantong PT Global Distribusi: Reserved $300.00
61. Pulihkan harga RFID Object TAG di PT ABC menjadi $2.50 lewat fixture hingga tersimpan

### TC-AC-ACHA-199: Edit ganti Pay From: Release kantong lama dan Reserve kantong baru atomik

62. Ganti akun: Logout, login sebagai MB_P2 (Pre-setup #47), buka Allocation > Device Allocation
63. Buka Setup Column, aktifkan kolom Paid From dan Cost, klik `[Save]`
64. Ketik Search Allocation ID transaksi milik spec (replika Pre-setup #50), tekan Enter
65. Buka menu row action `⋯` transaksi itu, klik `Edit`
66. Ganti Pay From menjadi `PT ABC (Principal)`
67. Verifikasi Preview: `Unit Price (Snapshot)` `$1.20/unit`, `Estimated Cost` `$48.00 (40 × $1.20/unit)`, dan `Your Pocket Balance` `$3,000.00`
68. Klik `[Save]`
69. Verifikasi toast sukses: "Success, device allocation has been updated."
70. Verifikasi baris List: Paid From `PT ABC (Principal)`
71. Verifikasi baris List: Cost `$48.00`
72. Verifikasi Wallet kantong A (sumber `PT Global Distribusi (Distributor)`): Reserved menjadi $0.00 (Release)
73. Verifikasi Wallet kantong B (sumber `PT ABC (Principal)`): Reserved menjadi $48.00 (Reserve baru)

### TC-AC-ACHA-201: Edit Principal tanpa wallet

74. Ganti akun: Logout, login sebagai MB_PRIN (Pre-setup #24), buka Allocation > Device Allocation
75. Buka Setup Column, aktifkan kolom Notes dan Cost, klik `[Save]`
76. Ketik Search Allocation ID transaksi milik spec (replika Pre-setup #51), tekan Enter
77. Buka menu row action `⋯` transaksi itu, klik `Edit`
78. Ubah Quantity menjadi `15` dan Notes menjadi `Revisi Principal`
79. Klik `[Save]`
80. Verifikasi toast sukses: "Success, device allocation has been updated."
81. Verifikasi baris List: Quantity `15`
82. Verifikasi baris List: Notes `Revisi Principal`
83. Verifikasi baris List: Cost `—`

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan TC (S-05, S-10): blok MB_ON (TC-AC-ACHA-196, 197, 198, 200, 208) berjalan lebih dulu sebelum blok ganti akun TC-AC-ACHA-199 (MB_P2) dan TC-AC-ACHA-201 (MB_PRIN), supaya tiap ganti akun hanya satu kali. Semua blok adalah aksi sukses yang tiap kali memakai keadaan awal yang sama; tidak ada blok yang memakai hasil blok sebelumnya (langkah 20, 28, 40, 52 memulihkan transaksi).
- Langkah penghubung (S-03, R-16): langkah 1, 63, 75 (Setup Column; precondition TC "kolom ditampilkan lewat Setup Column"); langkah 2, 20, 28, 40, 52, 64, 76 (Search Allocation ID untuk menemukan baris target; pemulihan transaksi dan muat ulang di langkah 20, 28, 40, 52); langkah 3, 29, 41 (baseline jumlah entri Allocation Log, S-12); langkah 10 (waktu pembanding Last Updated); langkah 19, 39, 51 (menutup modal Allocation Log); langkah 53 dan 61 (mengubah dan memulihkan harga produk); langkah 58 (menunggu form tertutup); langkah 62 dan 74 (ganti akun).
- Spec ini melewati sekitar 35 langkah. Alasan: seluruhnya satu topik (aksi Edit sukses), tiap blok memakai transaksi yang dipulihkan sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan `Verifikasi` dipecah per klausa (S-01).
- Pengecualian S-12: Notes `Batch uji`, nama entitas Pre-setup, dan nilai Pre-setup bernilai literal karena diasersi TC (Lampiran A butir A-6).
- Temuan untuk QA:
  - Kontrak fixture seeding transaksi milik spec, pemulihan transaksi, baca Reserved atau saldo kantong, baca jumlah entri Allocation Log, dan pengubah harga produk (Pre-setup #20) tidak tertulis di TC, PRD, atau LLD; ditulis "disediakan tim FE/BE" (R-19, S-13). TC menulis "Buka Wallet Balance kantong PT Global Distribusi"; spec membacanya lewat kemampuan baca Reserved dan saldo agar nilai Reserved terbaca pasti.
  - TC-AC-ACHA-196 Post Condition ("Status tetap Waiting for Approval dan batas waktu persetujuan tidak di-reset"): status diasersi lewat Expected butir c; "batas waktu persetujuan tidak di-reset" tidak punya langkah observasi sehingga tidak diasersi.
  - TC-AC-ACHA-197, 199, 200, 201, 208 Post Condition ("Wallet Balance dan Wallet Transaction List (Reserve disesuaikan), Approvals Active Tab (data subject terbaru)") tanpa langkah observasi di TC: tidak diasersi.
  - TC-AC-ACHA-199 butir d menyebut Release dan Reserve terjadi "dalam satu perubahan atomik"; atomisitas tidak teramati dari UI, spec hanya mengasersi kedua nilai Reserved akhir (atomisitas diuji TC-AC-ACHA-467 dan 468).
  - TC-AC-ACHA-201 butir b ("tanpa Reserve atau potongan wallet") tidak punya cara observasi pada Principal tanpa wallet; spec hanya mengasersi Quantity, Notes, dan Cost `—`.
  - TC-AC-ACHA-208 tidak memuat toast di Expected; spec hanya menunggu form tertutup (langkah 58) sebelum membaca Cost.
