---
id: TC-GS-HHR-E2E-065-absence-log-last-scanned-usage-event-no-op-dan-event-log
title: "Absence Log: Last Scanned, Usage Event, Edit No-Op, Kegagalan Driver, dan Penolakan Client Suspended Tidak Menghasilkan Entri"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-187
  - TC-GS-HHR-188
  - TC-GS-HHR-354
  - TC-GS-HHR-355
  - TC-GS-HHR-369
  - TC-GS-HHR-370
coverage:
  web: automated
---

# Absence Log: Last Scanned, Usage Event, Edit No-Op, Kegagalan Driver, dan Penolakan Client Suspended Tidak Menghasilkan Entri

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memakai simulator USB dan sesi pemindaian produk bersama, menghapus reader DD-01 Seed Reader A (aksi hapus di akhir bagian Client A), dan berganti ke Client D (Suspended).
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` membuka layar itu lagi hanya sebagai kembali dari surface log atau sesudah ganti akun.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Akun kedua (TC-GS-HHR-370, langkah 79): Total Control Client D (Suspended; memiliki reader dan Event Log sebelumnya), email `totalControl_automated_qaTeam9@qwertysystem.net`, password `Spectra.env.GS_CLIENTD_TC_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` oleh owner suite). Hook `after` mengembalikan sesi ke akun default suite (Client A).
- Data Pre-setup: Client A plan Growth, Seed Reader A (`Fixture.hardwareHandheldReader.seedReaderA`, fixture baru; 10 reader DD-01 s.d. DD-10, pagination `Showing 1 - 10 of 10 readers`), format tanggal `dd/MM/yy` 24-hour. Reader yang dipakai: DD-01 (`Zebra RFID Reader - 1`, `SN-HHR-00101`; Tab Usage memuat event UE-01 s.d. UE-06 `Audit Scan`, `Transfer Departure Verify`, `Borrow Verify`, `Audit TAG`, `Pair TAG`, `Combine TAG`), DD-02 (`Gudang Reader - 1`, `SN-HHR-00102`, Alias Name `Reader Gudang 02`), DD-04 (`Gudang Reader - 2`, `SN-HHR-00104`, Missing), dan DD-06 (`Zebra RFID Reader - 1`, `SN-HHR-00107`, pembanding TC-GS-HHR-188). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya.
- Seed Changelog Client A (CL-01 s.d. CL-09; `Fixture.hardwareHandheldReader.seedChangelogClientA`) dan Seed Event Log Client A (EL-01 s.d. EL-05; `Fixture.hardwareHandheldReader.seedEventLogClientA`) dibuat fixture backend dengan `Date` Juni 2026 (kemampuan disediakan tim FE/BE). Audit trail permanen tidak dipulihkan ke seed: Changelog, System Log, Activity Log, dan Event Log dibaca relatif terhadap baseline yang dicatat sebelum aksi pemicu (S-12), bukan terhadap jumlah seed.
- Baseline log (S-12): jumlah entri total Changelog Handheld Reader, System Log aktor (Global Settings > User > Detail akun aktor > tab System Log), dan Activity Log (Global Settings > Activity Log > tab User Action) dicatat sebelum aksi pemicu tiap TC; Event Log Activate dicatat sebelum TC-GS-HHR-369 dan 370. Total entri tidak diasersi sebagai angka absolut. Untuk TC-GS-HHR-187 baseline Activity Log adalah jumlah baris hasil Search `Gudang Reader - 2` (nol bila empty state `No results found`).
- Kemampuan teknis: (1) simulator reader USB dan driver lokal, termasuk keadaan "driver lokal belum terpasang" (TC-GS-HHR-369), dan reader tersambung pada Client D (TC-GS-HHR-370); (2) sesi pemindaian produk memakai reader DD-04 yang menulis Usage Event (TC-GS-HHR-187); semuanya disediakan tim FE, mekanismenya tidak didefinisikan di TC, PRD, atau LLD; TC-GS-HHR-187, 369, dan 370 berlabel Manual Only (b) di TC sumber; (3) pemulihan Seed Reader A lewat fixture backend dan pembuatan seed audit trail bertanggal Juni 2026; (4) pembacaan jumlah dan isi entri pada tiga surface log dan Event Log; (5) pengisian rentang tanggal pada Filter `Date` Tab Usage lewat date picker (nilai `Date` pada langkah ditulis dalam format tampil `dd/MM/yy`; input date picker memakai format `MM/dd/yyyy`; Filter `Date` diproses server-side dan inklusif kedua ujung, tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE/BE).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor (termasuk akun Client D) dan hook `after` memulihkannya; lihat `suite.md`.
- State global: tidak ada yang diubah selain Seed Reader A (DD-01 dihapus lalu dipulihkan oleh hook `after`) dan flag Guided Tooltip.

## Test Steps

### TC-GS-HHR-354: Usage Event tidak masuk Changelog, System Log, maupun Activity Log

1. Klik ikon Changelog
2. Verifikasi tabel Changelog menampilkan sedikitnya satu baris entri
3. Verifikasi Changelog Handheld Reader tidak memuat baris `Audit Scan`, `Borrow Verify`, `Transfer Departure Verify`, `Audit TAG`, `Pair TAG`, atau `Combine TAG`
4. Tutup Modal Changelog dengan `✕`
5. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
6. Klik ikon Filter di tab, isi `Date` rentang `16/06/26` sampai `21/06/26`, klik `[Apply]` (pembatas seed UE-01 sampai UE-06)
7. Verifikasi Tab Usage DD-01 memuat enam event `Audit Scan`, `Transfer Departure Verify`, `Borrow Verify`, `Audit TAG`, `Pair TAG`, dan `Combine TAG`
8. Klik `[Clear Field]`, klik `[Apply]`, lalu klik ikon Filter di tab untuk menutup Filter Panel
9. Tutup Popup `Handheld Reader Detail` dengan `✕`
10. Buka Global Settings > User > Detail akun aktor > tab System Log
11. Verifikasi tabel System Log aktor menampilkan sedikitnya satu baris entri
12. Verifikasi System Log aktor tidak memuat baris `Audit Scan`, `Borrow Verify`, `Transfer Departure Verify`, `Audit TAG`, `Pair TAG`, atau `Combine TAG`
13. Buka Global Settings > Activity Log > tab User Action
14. Verifikasi tabel Activity Log menampilkan sedikitnya satu baris entri
15. Verifikasi Activity Log tidak memuat baris `Audit Scan`, `Borrow Verify`, `Transfer Departure Verify`, `Audit TAG`, `Pair TAG`, atau `Combine TAG`
16. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-355: Edit No-Op tidak menulis entri pada tiga surface

17. Buka ikon Changelog, catat jumlah entri total sebagai baseline Changelog, tutup modal dengan `✕`
18. Buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri total sebagai baseline System Log
19. Buka Global Settings > Activity Log > tab User Action, catat jumlah entri total sebagai baseline Activity Log
20. Buka Global Settings > Hardware > Handheld Reader
21. Klik `⋯` pada baris DD-02 (Serial Number `SN-HHR-00102`), pilih `Edit Alias Name`
22. Klik `[Save]` tanpa mengubah `Alias Name`
23. Tunggu aksi selesai (dialog tertutup)
24. Buka ikon Changelog
25. Verifikasi tabel Changelog menampilkan sedikitnya satu baris entri
26. Verifikasi jumlah entri Changelog sama dengan baseline Changelog
27. Tutup Modal Changelog dengan `✕`
28. Buka Global Settings > User > Detail akun aktor > tab System Log
29. Verifikasi tabel System Log aktor menampilkan sedikitnya satu baris entri
30. Verifikasi jumlah entri System Log aktor sama dengan baseline System Log
31. Buka Global Settings > Activity Log > tab User Action
32. Verifikasi tabel Activity Log menampilkan sedikitnya satu baris entri
33. Verifikasi jumlah entri Activity Log sama dengan baseline Activity Log
34. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-187: Perubahan Last Scanned tidak menghasilkan entri Changelog atau Activity Log

35. Buka ikon Changelog, catat jumlah entri total sebagai baseline Changelog TC-GS-HHR-187, tutup modal dengan `✕`
36. Buka Global Settings > Activity Log > tab User Action
37. Ketik Search `Gudang Reader - 2`, tekan Enter
38. Catat jumlah baris hasil sebagai baseline Activity Log reader DD-04
39. Buka Global Settings > Hardware > Handheld Reader
40. Selesaikan satu sesi pemindaian produk memakai reader DD-04 (`Gudang Reader - 2`)
41. Tunggu aksi selesai
42. Buka ikon Changelog
43. Verifikasi tabel Changelog menampilkan sedikitnya satu baris entri
44. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline Changelog TC-GS-HHR-187
45. Tutup Modal Changelog dengan `✕`
46. Buka Global Settings > Activity Log > tab User Action
47. Verifikasi tabel Activity Log menampilkan sedikitnya satu baris entri
48. Ketik Search `Gudang Reader - 2`, tekan Enter
49. Verifikasi jumlah baris hasil sama dengan baseline Activity Log reader DD-04 (tidak ada entri baru untuk reader DD-04)
50. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-369: Kegagalan driver sebelum Sync tidak dicatat di Event Log

51. Klik ikon Event Log
52. Verifikasi Popup Event Log Activate menampilkan sedikitnya satu baris
53. Catat jumlah baris Event Log sebagai baseline N0 Event Log
54. Tutup Popup Event Log Activate dengan `✕`
55. Pastikan driver lokal reader belum terpasang pada simulator
56. Klik `[+ Activate Reader]`
57. Klik `Long Range` pada Overlay `Select Range Type`
58. Klik `[Sync]`
59. Tutup Popup `Activate Handheld Reader` dengan `✕`
60. Klik ikon Event Log
61. Verifikasi jumlah baris Event Log sama dengan baseline N0 Event Log; tidak ada baris dari kegagalan driver
62. Tutup Popup Event Log Activate dengan `✕`
63. Klik ikon Changelog, catat jumlah entri total sebagai baseline Changelog TC-GS-HHR-188, tutup Modal Changelog dengan `✕`

### TC-GS-HHR-188: Usage Event reader yang sudah dihapus tidak memiliki surface untuk dilihat

64. Buka Overlay row action baris DD-01 (Serial Number `SN-HHR-00101`)
65. Klik `Delete`
66. Klik `[Delete]` pada dialog
67. Tunggu aksi selesai (dialog tertutup)
68. Ketik Search `Zebra RFID Reader - 1`, tekan Enter
69. Verifikasi baris DD-06 (Serial Number `SN-HHR-00107`, `Zebra RFID Reader - 1`) tampil
70. Verifikasi baris DD-01 (Serial Number `SN-HHR-00101`) hilang dari tabel sehingga tidak ada `Device Name` yang dapat diklik untuk membuka Popup Detail dan Tab Usage reader itu
71. Klik `(←)` pada kotak Search
72. Klik ikon Changelog
73. Verifikasi jumlah entri Changelog Handheld Reader bertambah satu dari baseline Changelog TC-GS-HHR-188
74. Ketik Search `Zebra RFID Reader - 1 (SKU-HHR-01)` di modal, tekan Enter
75. Verifikasi entri teratas hasil Search modal adalah entri Action `Delete` untuk Device Name `Zebra RFID Reader - 1 (SKU-HHR-01)` sebagai snapshot
76. Verifikasi modal tidak memuat entri Usage Event (`Audit Scan`, `Borrow Verify`, `Transfer Departure Verify`, `Audit TAG`, `Pair TAG`, `Combine TAG`)
77. Tutup Modal Changelog dengan `✕`

### TC-GS-HHR-370: Penolakan Suspended tidak dicatat di Event Log (Client D)

78. Logout dari akun Total Control Client A
79. Login sebagai Total Control Client D (`Spectra.env.GS_CLIENTD_TC_PASSWORD`)
80. Buka Global Settings > Hardware > Handheld Reader
81. Klik ikon Event Log
82. Verifikasi Popup Event Log Activate Client D menampilkan baris sebelumnya (sedikitnya satu baris)
83. Catat jumlah baris Event Log sebagai baseline Event Log Client D
84. Tutup Popup Event Log Activate dengan `✕`
85. Klik `[+ Activate Reader]`
86. Klik `Long Range` pada Overlay `Select Range Type`
87. Klik `[Sync]`
88. Klik `[Submit]`
89. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
90. Tutup Popup `Activate Handheld Reader` dengan `✕`
91. Verifikasi dialog `Cancel Activation` tampil dengan body `Are you sure you want to cancel this activation? The Sync progress you've made will be lost.` dan tombol `[Go Back]` `[Cancel Activation]`
92. Klik `[Cancel Activation]`
93. Klik ikon Event Log
94. Verifikasi jumlah baris Event Log sama dengan baseline Event Log Client D (tidak bertambah)
95. Tutup Popup Event Log Activate dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3j, 5a, 5b). Kelas harness: absence log (g) dengan pemicu kelas lain (P-5).
- P-5 (a): spec absence ini memuat pemicu kelas d (sesi pemindaian produk TC-GS-HHR-187; kegagalan driver TC-GS-HHR-369; Sync dan Submit pada TC-GS-HHR-370) dan kelas h (Client D Suspended pada TC-GS-HHR-370) hanya untuk membentuk kondisi yang diasersi tidak tercatat; pemicu bukan objek uji. Tiap TC punya baseline sendiri.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Cara baca entri baru (S-12, S-14): pada TC-GS-HHR-188 entri `Delete` DD-01 dibaca pada baris teratas hasil Search modal Changelog (urutan default `Date` terbaru) sesudah `Verifikasi` selisih satu dari baseline Changelog TC-GS-HHR-188 (baseline langkah 63, selisih langkah 73); satu Delete menghasilkan satu entri sehingga tidak ada himpunan baris dalam menit yang sama.
- Urutan TC dalam spec: 354, 355, 187, 369, 188, 370. Menyimpang dari urutan nomor TC sumber: TC-GS-HHR-188 (menghapus DD-01 dan tidak bisa dipulihkan dalam spec) dipindah ke akhir bagian Client A sesudah TC-GS-HHR-354 yang membaca Tab Usage DD-01; TC-GS-HHR-370 paling akhir karena ganti akun ke Client D (langkah 78 dan 79); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Anchor positif (8b butir 2): TC-GS-HHR-354 didahului `Verifikasi` tiap surface (Changelog, System Log aktor, Activity Log) menampilkan sedikitnya satu baris entri; TC-GS-HHR-355 dan 187 memakai baris entri tiap surface dan jumlah baseline sebagai pembanding agregat (pemicu Save tanpa perubahan dan sesi pemindaian produk tidak menyentuh entri anchor); TC-GS-HHR-369 dan 370 memakai sedikitnya satu baris Event Log yang tampil dan jumlah baseline N0; TC-GS-HHR-188 memakai baris DD-06 (`Zebra RFID Reader - 1` lain) dan entri `Delete` pada surface yang sama sebelum asersi absence Usage Event.
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan baseline dan kembali ke layar Handheld Reader; "Tunggu aksi selesai" sebelum berpindah surface (8b butir 8; juga langkah 41 sesudah sesi pemindaian produk); Filter `Date` seed Tab Usage DD-01 sebagai pembatas baca beserta pelepasannya (langkah 6 dan 8); membuka dan menutup surface log, popup, dan modal; klik `[Cancel Activation]` (langkah 92); Search untuk menemukan baris target atau entri DD-04 dan `(←)` untuk mengosongkannya; Logout dan Login.
- Spec memuat 95 langkah, di atas sekitar 35 langkah. Alasan: seluruh blok satu kelas (asersi absence, kelas g) dengan baseline dan anchor positif sendiri per TC; tiap blok dimulai dari layar Handheld Reader dan tidak bergantung pada hasil blok sebelumnya (kecuali data DD-01 yang sengaja dihapus di blok TC-GS-HHR-188 pada akhir bagian Client A), sehingga kegagalan satu blok tidak menghilangkan makna blok lain; 28 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01) dan blok baca-log berpola (buka surface, bandingkan jumlah) tidak dihitung ke batas ukuran.
- Penutupan Popup `Activate Handheld Reader` pada TC-GS-HHR-370 (langkah 90 sampai 92): `[Submit]` yang ditolak T-12 meninggalkan hasil Sync pada popup, sehingga `✕` memunculkan dialog `Cancel Activation` (PRD §3.1 langkah 9 dan §4.2c, D-03; teks dialog dari TC-GS-HHR-89). Spec memverifikasi dialog itu, lalu klik `[Cancel Activation]` menurut A-1 (S-08); `Verifikasi` dialog bukan butir Expected TC-GS-HHR-370 dan dicatat di sini (S-03). Pada TC-GS-HHR-369 Sync gagal sebelum ada hasil Sync, sehingga popup (langkah 59) langsung tertutup tanpa dialog (PRD §3.1 langkah 9).
- Pembagian TC lintas spec: Edit No-Op dengan toast `No changes to save.` (TC-GS-HHR-106 dan 107) di spec 030; kegagalan 5xx tanpa entri tiga surface (TC-GS-HHR-352) di spec 027; Last Scanned dari Usage Event produk lain (TC-GS-HHR-185 dan 186) di spec 038; Event Log untuk aktivasi yang berhasil atau ditolak (TC-GS-HHR-364 sampai 367) di spec 067; pencatatan log per aksi (TC-GS-HHR-345 sampai 353) di spec 063.
- Temuan untuk QA:
  - TC-GS-HHR-187 dan 370 tidak menjelaskan cara menyelesaikan sesi pemindaian produk atau menyambungkan reader pada Client D; TC-GS-HHR-369 tidak menjelaskan cara membuat keadaan "driver lokal belum terpasang". Mekanisme simulasi tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE.
  - TC-GS-HHR-187 Expected b ("tidak mendapat entri baru untuk reader DD-04") tidak menyebut cara membaca Activity Log; spec membandingkan jumlah baris Search `Gudang Reader - 2` sebelum dan sesudah. TC tidak menyebut System Log aktor meski judulnya menyebutnya; spec tidak mengasersinya.
  - TC-GS-HHR-188 Search `Zebra RFID Reader - 1` tetap mencocokkan baris DD-06 yang bernama sama; spec mengidentifikasi DD-01 lewat Serial Number `SN-HHR-00101`. Expected c ("Tidak ada layar lain yang menampilkan Usage Event reader terhapus") tidak punya langkah observasi di TC; spec tidak mengasersinya terpisah (tercakup oleh Expected a dan b).
  - TC-GS-HHR-355 meminta klik `[Save]` tanpa perubahan; bila `[Save]` pada kasus ini dinonaktifkan atau menampilkan toast netral, TC tidak menyatakannya (spec 030 mengasersi toast netral `No changes to save.`); spec mengikuti langkah TC dan tidak mengasersi toast.
  - TC-GS-HHR-369 menyebut "tutup popup" tanpa menyatakan ada atau tidaknya dialog konfirmasi; spec menutup dengan `✕` saja karena belum ada hasil Sync (PRD §3.1 langkah 9) dan tidak menulis langkah bersyarat.
  - TC-GS-HHR-370 tidak menyebut Serial Number reader yang tersambung; spec menuliskan reader tersambung pada Client D sebagai kemampuan yang disediakan tim FE. Nama env password Client D `GS_CLIENTD_TC_PASSWORD` belum terdaftar di `spectra.config.ts` dan `.env.example` (didaftarkan owner suite).
  - Pembatas Filter `Date` `16/06/26` sampai `21/06/26` pada Tab Usage DD-01 (langkah 6; pelepasan di langkah 8) ditambahkan spec di luar langkah TC-GS-HHR-354 agar enam baris seed UE-01 sampai UE-06 berada pada satu halaman meski Tab Usage dapat bertambah entri (S-14); Expected TC tetap terpenuhi karena filter tidak mengubah identitas baris seed. Tolong konfirmasi bahwa penambahan itu tidak mengubah maksud TC. Panel Filter tetap terbuka sesudah `[Apply]`, jadi ditutup dengan ikon Filter.
