---
id: TC-AC-ACHA-E2E-049-absence-pencatatan-log-aksi-ditolak
title: "Absence Pencatatan Log: Permintaan Langsung Ditolak, Aksi Gagal, dan Edit No-Op Tidak Menulis Entri Log"
priority: High
caseType: Negative
status: draft
sourceTc: []
coverage:
  web: automated
---

# Absence Pencatatan Log: Permintaan Langsung Ditolak, Aksi Gagal, dan Edit No-Op Tidak Menulis Entri Log

## Prerequisites

- Mode: FE+BE (permintaan langsung lewat sesi API aktor; intercept parsial di atas backend nyata untuk TC-AC-ACHA-391).
- Akun (Pre-setup, email lengkap `<alias>_automated_qaTeam1@qwertysystem.net`; password lewat env var, bukan di spec atau fixture):

| Alias | Pre-setup | Nama pengguna | Peran di spec | Env var password |
|---|---|---|---|---|
| `totalControlDistributor` | #27 | Hendra Wibowo | Aktor hook `before`; pengirim permintaan blok A; pembaca Activity Log dan System Log | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| `memberOnDistributor` | #32 | Budi Santoso (MB_ON) | Pengirim permintaan TC-AC-ACHA-436 dan 439; aktor UI TC-AC-ACHA-391 dan 428 | `Spectra.env.AC_DA_MB_ON_PASSWORD` |
| `readOnlyDistributor` | #34 | Read Only Distributor | Pengirim permintaan TC-AC-ACHA-431 | `Spectra.env.AC_DA_RO_DIST_PASSWORD` |
| `defaultUserDistributor` | #28 | Default User Distributor | Pengirim permintaan TC-AC-ACHA-440 | `Spectra.env.AC_DA_DU_PASSWORD` |
| `memberOffDistributor` | #33 | Citra Anggraini | Pengirim permintaan TC-AC-ACHA-489 | `Spectra.env.AC_DA_MB_OFF_PASSWORD` |

- Login akun pertama (Hendra Wibowo) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite dan memulihkan saldo kantong, harga produk, dan role Citra Anggraini.
- Hook suite (dinyatakan di `suite.md`): flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, sesi API aktor, fixture API disediakan tim FE/BE, pemulihan preferensi Setup Column.
- Data Pre-setup: #7 Client PT Sejahtera Logistik, #10 Client PT Manufaktur Unggul (di luar scope WRITE PT Global Distribusi), #12 Client PT Agro Lestari (Suspended), #13 Client Toko Lama Abadi (Archived), #14 harga produk, #16 kantong PT Global Distribusi saldo $20,000.00, #66 Subcategory `RFID Premium` di bawah node RFID, #71 transaksi milik Citra Anggraini.
- Data seeding milik spec (fixture API disediakan tim FE/BE; salinan milik spec dari Pre-setup #49, #52, #54, #55, #71, dibuat di hook `before` sebelum baseline dicatat): transaksi Waiting for Approval milik MB_ON (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Notes `Batch uji`, Reserve $250.00) dengan peran `target blok A` (TC-AC-ACHA-429, 431, 439, 440), `target TC-391`, dan `target TC-428`; transaksi Canceled milik MB_ON (`target resubmit`); satu transaksi Completed, satu Rejected, dan satu Canceled milik MB_ON (`target status akhir`); satu transaksi Waiting for Approval (BLE Gateway, Quantity 10, Reserve $20.00) dan satu transaksi Canceled (NFC, Quantity 10) milik Citra Anggraini sebelum role Group Jakarta dicabut (`target Citra`).
- Kemampuan teknis: klien HTTP lewat sesi API aktor untuk permintaan langsung ke server (Create, Edit, Cancel, Resubmit, Approve, Reject); `Spectra.intercept()` untuk memaksa respons Cancel 500 (TC-AC-ACHA-391, dilepas segera sesudah pemicu); fixture (disediakan tim FE/BE) untuk menyetel saldo kantong, menghapus dan memulihkan harga produk BLE Gateway, dan mencabut serta memulihkan role Manage allocation Citra Anggraini di Group Jakarta; pengaktifan paksa tombol `[Save]` pada form Edit lewat DOM (hapus atribut disabled) untuk TC-AC-ACHA-428 (langkah 93, 96, dan 101), disediakan tim FE.
- Baseline log (S-12): sebelum aksi pemicu pertama dicatat jumlah entri Object `Device Allocation` pada Activity Log (Admin Console, entitas PT Global Distribusi) dan pada System Log tiap aktor, jumlah baris per Allocation ID untuk TC-AC-ACHA-391 dan 428, dan jumlah entri Allocation Log transaksi `target TC-428` dan `target Citra`. Tiap blok TC memakai pembanding yang sama karena blok sebelumnya sudah diverifikasi tidak menambah entri. Log tidak bisa dihapus, sehingga asersi memakai selisih nol terhadap baseline, bukan nilai absolut.
- Suite berjalan serial (`parallel: false`): saldo kantong, harga produk, dan hak role adalah state global yang dipulihkan di hook `after`. Efek pada Pre-setup bersama (S-06): Last Updated kantong PT Global Distribusi, harga produk BLE Gateway, dan role Citra Anggraini ikut berubah dan audit trail perubahan itu bertambah permanen; nilai dipulihkan lewat fixture yang disediakan tim FE/BE.
- Nilai literal Notes `Batch uji`, `BATCH UJI`, dan `  Batch uji  ` (dua spasi di awal dan akhir) sesuai TC.

## Test Steps

### Baseline

1. Buka Activity Log di Admin Console, filter Object `Device Allocation`, dan catat jumlah entri sebagai baseline Activity Log
2. Buka System Log pada Detail User `Hendra Wibowo` dan catat jumlah entri Object `Device Allocation` sebagai baseline System Log `Hendra Wibowo`
3. Buka System Log pada Detail User `Budi Santoso`, `Citra Anggraini`, Read Only Distributor, dan Default User Distributor, dan catat jumlah entri Object `Device Allocation` pada masing-masing sebagai baseline System Log masing-masing aktor
4. Buka Activity Log dan System Log `Budi Santoso`, cari Allocation ID `target TC-391` dan Allocation ID `target TC-428`, dan catat jumlah baris per Allocation ID pada masing-masing surface sebagai baseline per Allocation ID
5. Buka modal Allocation Log `target TC-428` dan `target Citra`, dan catat jumlah entri masing-masing sebagai baseline Allocation Log

### TC-AC-ACHA-422: Type wajib untuk RFID dan Handheld Reader pada permintaan langsung

6. Kirim permintaan Create langsung (sesi API `Hendra Wibowo`) dengan Category `RFID` tanpa Type
7. Kirim permintaan Create langsung dengan Category `Handheld Reader` tanpa Type
8. Verifikasi kedua permintaan ditolak server dengan pesan "Type must not be empty"
9. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Hendra Wibowo`
10. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan jumlah entri System Log `Hendra Wibowo` sama dengan baseline langkah 2

### TC-AC-ACHA-423: Quantity tidak valid pada permintaan langsung ditolak server

11. Kirim permintaan Create langsung dengan Category `BLE`, Client `PT Sejahtera Logistik`, dan Quantity `-5`
12. Kirim permintaan Create langsung dengan Quantity `2.5`
13. Kirim permintaan Create langsung dengan Quantity `0`
14. Kirim permintaan Create langsung dengan Quantity `1000001`
15. Verifikasi tiga permintaan pertama ditolak server dengan pesan "Quantity must be a positive whole number"
16. Verifikasi permintaan Quantity `1000001` ditolak dengan pesan "Quantity must not exceed 1,000,000"
17. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Hendra Wibowo`
18. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Hendra Wibowo` sama dengan baseline langkah 2

### TC-AC-ACHA-424: Client Suspended pada permintaan langsung ditolak

19. Kirim permintaan Create langsung dengan Client `PT Agro Lestari` (Category `BLE`, Quantity `5`)
20. Verifikasi server menolak dengan HTTP 403 Forbidden
21. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Hendra Wibowo`
22. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Hendra Wibowo` sama dengan baseline langkah 2

### TC-AC-ACHA-425: Client Archived pada permintaan langsung ditolak

23. Kirim permintaan Create langsung dengan Client `Toko Lama Abadi` (Category `BLE`, Quantity `5`)
24. Verifikasi server menolak dengan HTTP 403 Forbidden
25. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Hendra Wibowo`
26. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Hendra Wibowo` sama dengan baseline langkah 2

### TC-AC-ACHA-426: Client di luar scope WRITE pada permintaan langsung ditolak

27. Kirim permintaan Create langsung dengan Client `PT Manufaktur Unggul` (Category `BLE`, Quantity `5`)
28. Verifikasi server menolak permintaan karena Client bukan binaan langsung pengirim
29. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Hendra Wibowo`
30. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Hendra Wibowo` sama dengan baseline langkah 2

### TC-AC-ACHA-427: Category yang bukan node first-level pada permintaan langsung ditolak

31. Kirim permintaan Create langsung dengan Category `TAG` (root grup)
32. Kirim permintaan Create langsung dengan Category `Hardware` (root grup)
33. Kirim permintaan Create langsung dengan Category `RFID Premium` (subcategory level 2 buatan user)
34. Verifikasi ketiga permintaan ditolak server karena Category bukan salah satu dari tujuh node first-level
35. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Hendra Wibowo`
36. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Hendra Wibowo` sama dengan baseline langkah 2

### TC-AC-ACHA-429: Edit dan Cancel oleh non-creator via permintaan langsung ditolak

37. Kirim permintaan Edit langsung (Quantity `120`) untuk transaksi `target blok A` milik MB_ON
38. Kirim permintaan Cancel langsung untuk transaksi `target blok A`
39. Verifikasi kedua permintaan ditolak HTTP 403
40. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Hendra Wibowo`
41. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Hendra Wibowo` sama dengan baseline langkah 2

### TC-AC-ACHA-430: Resubmit oleh non-creator via permintaan langsung ditolak

42. Kirim permintaan Resubmit langsung untuk transaksi `target resubmit` milik MB_ON
43. Verifikasi permintaan ditolak HTTP 403
44. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Hendra Wibowo`
45. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Hendra Wibowo` sama dengan baseline langkah 2

### TC-AC-ACHA-437: Saldo kantong tidak cukup pada permintaan langsung ditolak server

46. Setel kantong PT Global Distribusi ke saldo $99.99 dan harga BLE Gateway ke $2.00 lewat fixture (disediakan tim FE/BE)
47. Kirim permintaan Create langsung dengan Category `BLE Gateway`, Client `PT Sejahtera Logistik`, dan Quantity `50` (Total Cost $100.00, kurang $0.01 dari saldo)
48. Verifikasi server menolak permintaan karena saldo kantong tidak mencukupi
49. Pulihkan saldo kantong PT Global Distribusi ke $20,000.00 dan harga BLE Gateway ke nilai Pre-setup #14 lewat fixture (disediakan tim FE/BE)
50. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Hendra Wibowo`
51. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Hendra Wibowo` sama dengan baseline langkah 2

### TC-AC-ACHA-438: Harga produk belum dikonfigurasi pada permintaan langsung ditolak

52. Hapus harga BLE Gateway pada Wallet > Product Price PT ABC lewat fixture (disediakan tim FE/BE)
53. Kirim permintaan Create langsung dengan Category `BLE Gateway`, Client `PT Sejahtera Logistik`, dan Quantity `5`
54. Verifikasi server menolak permintaan dengan pesan "Price not set for this item. Please configure product pricing first."
55. Pulihkan harga BLE Gateway ke nilai Pre-setup #14 lewat fixture (disediakan tim FE/BE)
56. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Hendra Wibowo`
57. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Hendra Wibowo` sama dengan baseline langkah 2

### TC-AC-ACHA-436: Edit dan Cancel pada status akhir via permintaan langsung ditolak

58. Kirim permintaan Edit langsung (Quantity `120`, sesi API `Budi Santoso`) untuk masing-masing dari ketiga transaksi `target status akhir` (Completed, Rejected, Canceled)
59. Kirim permintaan Cancel langsung untuk transaksi Completed dan transaksi Rejected
60. Verifikasi seluruh permintaan ditolak karena status transaksi sudah berubah (konflik status)
61. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Budi Santoso`
62. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Budi Santoso` sama dengan baseline langkah 3

### TC-AC-ACHA-439: Resubmit pada status selain Canceled via permintaan langsung ditolak

63. Kirim permintaan Resubmit langsung (sesi API `Budi Santoso`) untuk masing-masing transaksi Waiting for Approval (`target blok A`), Completed, dan Rejected (`target status akhir`)
64. Verifikasi ketiga permintaan ditolak karena Resubmit hanya berlaku untuk status `Canceled`
65. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Budi Santoso`
66. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Budi Santoso` sama dengan baseline langkah 3

### TC-AC-ACHA-431: Read Only tidak dapat menulis via permintaan langsung

67. Kirim permintaan Create langsung (sesi API Read Only Distributor) dengan Category `BLE`, Client `PT Sejahtera Logistik`, dan Quantity `5`
68. Kirim permintaan Edit langsung untuk transaksi `target blok A`
69. Kirim permintaan Cancel langsung untuk transaksi `target blok A`
70. Verifikasi ketiga permintaan ditolak HTTP 403 oleh middleware
71. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log Read Only Distributor
72. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log Read Only Distributor sama dengan baseline langkah 3

### TC-AC-ACHA-440: Approve dan Reject oleh non-approver via permintaan langsung ditolak

73. Kirim permintaan Approve langsung (sesi API Default User Distributor) untuk transaksi `target blok A`
74. Kirim permintaan Reject langsung dengan Rejection Reason `Uji` untuk transaksi `target blok A`
75. Verifikasi kedua permintaan ditolak HTTP 403 pada tahap pertama evaluasi izin (aktor bukan anggota approver pool)
76. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log Default User Distributor
77. Verifikasi tidak ada entri log baru: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log Default User Distributor sama dengan baseline langkah 3

### TC-AC-ACHA-489: Aktor yang hanya memiliki Manage allocation di group lain ditolak untuk Create, Edit, Cancel, dan Resubmit

78. Cabut role Manage allocation Citra Anggraini di Group Jakarta lewat fixture hak role (disediakan tim FE/BE) sehingga hanya tersisa role Manage allocation (Create, Read, Update) di Group Surabaya
79. Kirim permintaan Create langsung (sesi API `Citra Anggraini`) dengan Category `BLE Gateway`, Client `PT Sejahtera Logistik`, dan Quantity `5`
80. Kirim permintaan Edit langsung (Quantity `20`) untuk transaksi Waiting for Approval `target Citra`
81. Kirim permintaan Cancel langsung untuk transaksi `target Citra`
82. Kirim permintaan Resubmit langsung untuk transaksi Canceled `target Citra`
83. Verifikasi keempat permintaan ditolak HTTP 403 oleh middleware karena Manage allocation akun ini tidak ada pada group target (Group Jakarta)
84. Hitung ulang jumlah entri Object `Device Allocation` pada Activity Log dan pada System Log `Citra Anggraini`, dan jumlah entri Allocation Log `target Citra`
85. Verifikasi tidak ada entri log baru di Activity Log dan System Log: jumlah entri Activity Log sama dengan baseline langkah 1 dan System Log `Citra Anggraini` sama dengan baseline langkah 3
86. Verifikasi tidak ada entri log baru di Allocation Log `target Citra`: jumlah entri sama dengan baseline langkah 5
87. Pulihkan role Manage allocation Citra Anggraini di Group Jakarta lewat fixture hak role (disediakan tim FE/BE)

### Ganti akun ke Budi Santoso (MB_ON)

88. Logout lalu login sebagai Group Member Distributor `memberOnDistributor` (Pre-setup #32), lalu buka Allocation > Device Allocation

### TC-AC-ACHA-391: Aksi gagal tidak meninggalkan entri log

89. Atur intercept agar respons Cancel dipaksa server error 500
90. Klik `Cancel Allocation` pada transaksi `target TC-391`, lalu konfirmasi di dialog
91. Lepas intercept respons Cancel
92. Verifikasi toast error "Error, failed to cancel device allocation."

### TC-AC-ACHA-428: Save Edit tanpa perubahan adalah No-Op tanpa log

93. Klik `Edit` pada transaksi `target TC-428`, tanpa mengubah nilai aktifkan paksa tombol `[Save]` lewat DOM (hapus atribut disabled), lalu klik `[Save]`
94. Verifikasi toast netral (severity Info) "No changes to save." tampil, bukan toast sukses
95. Tutup form Edit dengan `[×]`
96. Klik `Edit` pada transaksi `target TC-428`, ubah Notes dari `Batch uji` menjadi `BATCH UJI`, aktifkan paksa tombol `[Save]` lewat DOM, lalu klik `[Save]`
97. Verifikasi toast netral "No changes to save."
98. Klik `[×]` pada form Edit
99. Verifikasi dialog `Unsaved Changes` tampil
100. Klik `[Leave]`
101. Klik `Edit` pada transaksi `target TC-428`, ubah Notes menjadi `  Batch uji  ` (dua spasi di awal dan akhir), aktifkan paksa tombol `[Save]` lewat DOM, lalu klik `[Save]`
102. Verifikasi toast netral "No changes to save."
103. Klik `[×]` pada form Edit
104. Verifikasi dialog `Unsaved Changes` tampil
105. Klik `[Leave]`

### Ganti akun ke Hendra Wibowo dan pembacaan log

106. Logout lalu login sebagai Total Control Distributor `totalControlDistributor` (Pre-setup #27)
107. Buka Activity Log dan System Log `Budi Santoso`, cari Allocation ID `target TC-391`, dan hitung jumlah barisnya pada masing-masing surface
108. Verifikasi tidak ada dokumen Cancel baru untuk `target TC-391`: jumlah baris Activity Log dan System Log sama dengan baseline langkah 4
109. Buka Activity Log dan System Log `Budi Santoso`, cari Allocation ID `target TC-428`, dan hitung jumlah barisnya pada masing-masing surface
110. Verifikasi Activity Log dan System Log tidak menambah dokumen untuk `target TC-428`: jumlah baris sama dengan baseline langkah 4
111. Buka modal Allocation Log `target TC-428` dan hitung jumlah entrinya
112. Verifikasi Allocation Log `target TC-428` tidak menambah entri: jumlah entri sama dengan baseline langkah 5

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (Section 8 untuk permintaan langsung, Section 5c untuk TC-AC-ACHA-391, Section 3b untuk TC-AC-ACHA-428). Subjudul `###` memetakan langkah ke id TC granular.
- Kelas harness g (asersi absence). Spec ini adalah rumah asersi "tidak ada entri log" modul Device Allocation. Tidak ada TC primer: tiap TC di bawah tetap primer di spec asalnya dan tidak ditulis ulang di `sourceTc` spec ini (S-05). Pembagian TC lintas spec:
  - TC-AC-ACHA-422 sampai 427, 429, 430, 431, 436, 437, 438, 439, 440, 489: spec asal 054 (`defense-in-depth-permintaan-langsung-payload`) atau 055 (`defense-in-depth-permintaan-langsung-otorisasi`) mengasersi status respons dan state data (saldo, Reserve, status, Quantity); klausa "tidak ada entri log baru" dijalankan di sini dengan permintaan nyata, aktor, dan baseline sendiri.
  - TC-AC-ACHA-391 (spec asal 048): klausa Activity Log dan System Log tidak memuat dokumen Cancel.
  - TC-AC-ACHA-428 (spec asal 028): klausa Allocation Log, Activity Log, dan System Log tidak menambah entri; asersi toast, nilai field, dan Reserved ada di spec 028.
- P-5 (a): permintaan langsung ditolak (kelas a), respons 500 yang dipaksa (kelas b), dan edit paksa lewat DOM hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap blok TC memakai aktor dan pembanding sendiri. Intercept dilepas segera setelah pemicu (langkah 89 sampai 91; S-09).
- Anchor positif absence (bagian 8b butir 2): `Verifikasi` penolakan atau toast tepat sebelum pembacaan ulang log pada tiap blok (permintaan ditolak, toast error langkah 92, toast netral "No changes to save."), ditambah baseline jumlah entri yang dicatat sebelum aksi pemicu pertama (langkah 1 sampai 5); surface log disebut satu per satu pada tiap `Verifikasi`.
- Baseline dicatat sekali di awal dan dipakai semua blok: tiap blok sebelumnya sudah diverifikasi menambah nol entri sehingga pembanding berikutnya tetap sama. Blok TC-AC-ACHA-391 dan 428 memakai baseline per Allocation ID karena aksinya lewat UI dan pembacaan dilakukan sesudah ganti akun ke Hendra Wibowo (langkah 88 adalah ganti akun ke Budi Santoso, S-07).
- Langkah penghubung (S-03): langkah baseline 1 sampai 5; langkah hitung ulang jumlah entri; langkah pemulihan saldo, harga, dan role (S-09); langkah ganti akun (S-07); langkah menutup form Edit dengan `[×]` (bersih) dan `[×]` beserta `Verifikasi` dialog `Unsaved Changes` lalu `[Leave]` pada form dirty (S-08, tidak perlu dicatat lagi).
- Baris target (R-16): transaksi `target TC-391` dan `target TC-428` pada List (langkah 90 sampai 101) ditemukan lewat Search Allocation ID yang dicatat saat seeding sebagai langkah penghubung tanpa `Verifikasi`; langkah ini tidak diberi nomor sendiri.
- Ukuran spec: 112 langkah (melewati sekitar 35 langkah). Alasan: seluruh blok satu kelas harness (g), tiap blok TC berdiri sendiri dengan aktor, pemicu, dan pembanding sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah baca ulang log berpola (hitung ulang entri, `Verifikasi` selisih nol) dan ganti akun tidak dihitung menurut bagian 3 konvensi (Smell).
- Pengecualian S-12 nama literal (Lampiran A butir A-6): Notes `Batch uji` dan Rejection Reason `Uji` ditulis persis seperti TC.
- Temuan untuk QA:
  - TC-AC-ACHA-422 sampai 427, 429, 430, 431, 436 sampai 440, 489 menyebut "tidak ada entri log baru" tanpa menyebut surface log mana yang dibaca dan siapa pembacanya; spec membaca Activity Log (Hendra Wibowo) dan System Log aktor pengirim, dan Allocation Log untuk TC-AC-ACHA-489 (Expected d menyebut ketiganya).
  - TC-AC-ACHA-426 dan TC-AC-ACHA-436 tidak menyebut pesan atau kode penolakan; spec hanya mengasersi "ditolak" sebagai anchor.
  - TC-AC-ACHA-428 tidak menyebut apakah form Edit tetap terbuka sesudah toast netral; spec menutup form sesudah tiap varian (varian dirty melewati dialog `Unsaved Changes` menurut S-08).
  - TC-AC-ACHA-432, 433, 434, 435 tidak memuat klausa "tidak ada entri log baru" sehingga tidak dirujuk spec ini.
  - Post Condition TC-AC-ACHA-391 dan 428 ("-") tidak ada.
