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
- Akun kedua (TC-GS-HHR-370, langkah 67): Total Control Client D (Suspended; memiliki reader dan Event Log sebelumnya), email `totalControl_automated_qaTeam9@qwertysystem.net`, password `Spectra.env.GS_CLIENTD_TC_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` oleh owner suite). Hook `after` mengembalikan sesi ke akun default suite (Client A).
- Data Pre-setup: Client A plan Growth, Seed Reader A (`Fixture.hardwareHandheldReader.seedReaderA`, fixture baru; 10 reader DD-01 s.d. DD-10, pagination `Showing 1 - 10 of 10 readers`), format tanggal `dd/MM/yy` 24-hour. Reader yang dipakai: DD-01 (`Zebra RFID Reader - 1`, `SN-HHR-00101`; Tab Usage memuat event UE-01 s.d. UE-06 `Audit Scan`, `Transfer Departure Verify`, `Borrow Verify`, `Audit TAG`, `Pair TAG`, `Combine TAG`), DD-02 (`Gudang Reader - 1`, `SN-HHR-00102`, Alias Name `Reader Gudang 02`), DD-04 (`Gudang Reader - 2`, `SN-HHR-00104`, Missing), dan DD-06 (`Zebra RFID Reader - 1`, `SN-HHR-00107`, pembanding TC-GS-HHR-188). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya.
- Seed Changelog Client A (CL-01 s.d. CL-09; `Fixture.hardwareHandheldReader.seedChangelogClientA`) dan Seed Event Log Client A (EL-01 s.d. EL-05; `Fixture.hardwareHandheldReader.seedEventLogClientA`) dibuat fixture backend dengan `Date` Juni 2026 (kemampuan disediakan tim FE/BE). Audit trail permanen tidak dipulihkan ke seed: Changelog, System Log, Activity Log, dan Event Log dibaca relatif terhadap baseline yang dicatat sebelum aksi pemicu (S-12), bukan terhadap jumlah seed.
- Baseline log (S-12): jumlah entri total Changelog Handheld Reader, System Log aktor (Global Settings > User > Detail akun aktor > tab System Log), dan Activity Log (Global Settings > Activity Log > tab User Action) dicatat sebelum aksi pemicu tiap TC; Event Log Activate dicatat sebelum TC-GS-HHR-369 dan 370. Total entri tidak diasersi sebagai angka absolut. Untuk TC-GS-HHR-187 baseline Activity Log adalah jumlah baris hasil Search `Gudang Reader - 2` (nol bila empty state `No results found`).
- Kemampuan teknis: (1) simulator reader USB dan driver lokal, termasuk keadaan "driver lokal belum terpasang" (TC-GS-HHR-369), dan reader tersambung pada Client D (TC-GS-HHR-370); (2) sesi pemindaian produk memakai reader DD-04 yang menulis Usage Event (TC-GS-HHR-187); semuanya disediakan tim FE, mekanismenya tidak didefinisikan di TC, PRD, atau LLD; TC-GS-HHR-187, 369, dan 370 berlabel Manual Only (b) di TC sumber; (3) pemulihan Seed Reader A lewat fixture backend dan pembuatan seed audit trail bertanggal Juni 2026; (4) pembacaan jumlah dan isi entri pada tiga surface log dan Event Log.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor (termasuk akun Client D) dan hook `after` memulihkannya; lihat `suite.md`.
- State global: tidak ada yang diubah selain Seed Reader A (DD-01 dihapus lalu dipulihkan oleh hook `after`) dan flag Guided Tooltip.

## Test Steps

### TC-GS-HHR-354: Usage Event tidak masuk Changelog

1. Klik ikon Changelog
2. Verifikasi tabel Changelog menampilkan sedikitnya satu baris entri
3. Verifikasi Changelog Handheld Reader tidak memuat baris `Audit Scan`, `Borrow Verify`, `Transfer Departure Verify`, `Audit TAG`, `Pair TAG`, atau `Combine TAG`
4. Tutup Modal Changelog dengan `✕`
5. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
6. Verifikasi Tab Usage DD-01 memuat enam event `Audit Scan`, `Transfer Departure Verify`, `Borrow Verify`, `Audit TAG`, `Pair TAG`, dan `Combine TAG`
7. Tutup Popup `Handheld Reader Detail` dengan `✕`

### TC-GS-HHR-355: Edit No-Op tidak menulis entri pada tiga surface

8. Buka ikon Changelog, catat jumlah entri total sebagai baseline Changelog, tutup modal dengan `✕`
9. Buka Global Settings > User > Detail akun aktor > tab System Log, catat jumlah entri total sebagai baseline System Log
10. Buka Global Settings > Activity Log > tab User Action, catat jumlah entri total sebagai baseline Activity Log
11. Buka Global Settings > Hardware > Handheld Reader
12. Klik `⋯` pada baris DD-02 (Serial Number `SN-HHR-00102`), pilih `Edit Alias Name`
13. Klik `[Save]` tanpa mengubah `Alias Name`
14. Tunggu aksi selesai (dialog tertutup)
15. Buka ikon Changelog
16. Verifikasi tabel Changelog menampilkan sedikitnya satu baris entri
17. Verifikasi jumlah entri Changelog sama dengan baseline Changelog
18. Tutup Modal Changelog dengan `✕`
19. Buka Global Settings > User > Detail akun aktor > tab System Log
20. Verifikasi tabel System Log aktor menampilkan sedikitnya satu baris entri
21. Verifikasi jumlah entri System Log aktor sama dengan baseline System Log
22. Buka Global Settings > Activity Log > tab User Action
23. Verifikasi tabel Activity Log menampilkan sedikitnya satu baris entri
24. Verifikasi jumlah entri Activity Log sama dengan baseline Activity Log
25. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-187: Perubahan Last Scanned tidak menghasilkan entri Changelog atau Activity Log

26. Buka ikon Changelog, catat jumlah entri total sebagai baseline Changelog TC-GS-HHR-187, tutup modal dengan `✕`
27. Buka Global Settings > Activity Log > tab User Action
28. Ketik Search `Gudang Reader - 2`, tekan Enter
29. Catat jumlah baris hasil sebagai baseline Activity Log reader DD-04
30. Buka Global Settings > Hardware > Handheld Reader
31. Selesaikan satu sesi pemindaian produk memakai reader DD-04 (`Gudang Reader - 2`)
32. Buka ikon Changelog
33. Verifikasi tabel Changelog menampilkan sedikitnya satu baris entri
34. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline Changelog TC-GS-HHR-187
35. Tutup Modal Changelog dengan `✕`
36. Buka Global Settings > Activity Log > tab User Action
37. Verifikasi tabel Activity Log menampilkan sedikitnya satu baris entri
38. Ketik Search `Gudang Reader - 2`, tekan Enter
39. Verifikasi jumlah baris hasil sama dengan baseline Activity Log reader DD-04 (tidak ada entri baru untuk reader DD-04)
40. Buka Global Settings > Hardware > Handheld Reader

### TC-GS-HHR-369: Kegagalan driver sebelum Sync tidak dicatat di Event Log

41. Klik ikon Event Log
42. Verifikasi Popup Event Log Activate menampilkan sedikitnya satu baris
43. Catat jumlah baris Event Log sebagai baseline N0 Event Log
44. Tutup Popup Event Log Activate dengan `✕`
45. Pastikan driver lokal reader belum terpasang pada simulator
46. Klik `[+ Activate Reader]`
47. Klik `Long Range` pada Overlay `Select Range Type`
48. Klik `[Sync]`
49. Tutup Popup `Activate Handheld Reader` dengan `✕`
50. Klik ikon Event Log
51. Verifikasi jumlah baris Event Log sama dengan baseline N0 Event Log; tidak ada baris dari kegagalan driver
52. Tutup Popup Event Log Activate dengan `✕`

### TC-GS-HHR-188: Usage Event reader yang sudah dihapus tidak memiliki surface untuk dilihat

53. Buka Overlay row action baris DD-01 (Serial Number `SN-HHR-00101`)
54. Klik `Delete`
55. Klik `[Delete]` pada dialog
56. Tunggu aksi selesai (dialog tertutup)
57. Ketik Search `Zebra RFID Reader - 1`, tekan Enter
58. Verifikasi baris DD-06 (Serial Number `SN-HHR-00107`, `Zebra RFID Reader - 1`) tampil
59. Verifikasi baris DD-01 (Serial Number `SN-HHR-00101`) hilang dari tabel sehingga tidak ada `Device Name` yang dapat diklik untuk membuka Popup Detail dan Tab Usage reader itu
60. Klik `(←)` pada kotak Search
61. Klik ikon Changelog
62. Ketik Search `Zebra RFID Reader - 1 (SKU-HHR-01)` di modal, tekan Enter
63. Verifikasi modal memuat entri Action `Delete` untuk Device Name `Zebra RFID Reader - 1 (SKU-HHR-01)` sebagai snapshot
64. Verifikasi modal tidak memuat entri Usage Event (`Audit Scan`, `Borrow Verify`, `Transfer Departure Verify`, `Audit TAG`, `Pair TAG`, `Combine TAG`)
65. Tutup Modal Changelog dengan `✕`

### TC-GS-HHR-370: Penolakan Suspended tidak dicatat di Event Log (Client D)

66. Logout dari akun Total Control Client A
67. Login sebagai Total Control Client D (`Spectra.env.GS_CLIENTD_TC_PASSWORD`)
68. Buka Global Settings > Hardware > Handheld Reader
69. Klik ikon Event Log
70. Verifikasi Popup Event Log Activate Client D menampilkan baris sebelumnya (sedikitnya satu baris)
71. Catat jumlah baris Event Log sebagai baseline Event Log Client D
72. Tutup Popup Event Log Activate dengan `✕`
73. Klik `[+ Activate Reader]`
74. Klik `Long Range` pada Overlay `Select Range Type`
75. Klik `[Sync]`
76. Klik `[Submit]`
77. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
78. Tutup Popup `Activate Handheld Reader` dengan `✕`
79. Verifikasi dialog `Cancel Activation` tampil dengan body `Are you sure you want to cancel this activation? The Sync progress you've made will be lost.` dan tombol `[Go Back]` `[Cancel Activation]`
80. Klik `[Cancel Activation]`
81. Klik ikon Event Log
82. Verifikasi jumlah baris Event Log sama dengan baseline Event Log Client D (tidak bertambah)
83. Tutup Popup Event Log Activate dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 3j, 5a, 5b). Kelas harness: absence log (g) dengan pemicu kelas lain (P-5).
- P-5 (a): spec absence ini memuat pemicu kelas d (sesi pemindaian produk TC-GS-HHR-187; kegagalan driver TC-GS-HHR-369; Sync dan Submit pada TC-GS-HHR-370) dan kelas h (Client D Suspended pada TC-GS-HHR-370) hanya untuk membentuk kondisi yang diasersi tidak tercatat; pemicu bukan objek uji. Tiap TC punya baseline sendiri.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 354, 355, 187, 369, 188, 370. Menyimpang dari urutan nomor TC sumber: TC-GS-HHR-188 (menghapus DD-01 dan tidak bisa dipulihkan dalam spec) dipindah ke akhir bagian Client A sesudah TC-GS-HHR-354 yang membaca Tab Usage DD-01; TC-GS-HHR-370 paling akhir karena ganti akun ke Client D (langkah 66 dan 67); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Anchor positif (8b butir 2): TC-GS-HHR-354 didahului `Verifikasi` Changelog menampilkan sedikitnya satu baris entri; TC-GS-HHR-355 dan 187 memakai baris entri tiap surface dan jumlah baseline sebagai pembanding agregat (pemicu Save tanpa perubahan dan sesi pemindaian produk tidak menyentuh entri anchor); TC-GS-HHR-369 dan 370 memakai sedikitnya satu baris Event Log yang tampil dan jumlah baseline N0; TC-GS-HHR-188 memakai baris DD-06 (`Zebra RFID Reader - 1` lain) dan entri `Delete` pada surface yang sama sebelum asersi absence Usage Event.
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan baseline dan kembali ke layar Handheld Reader; "Tunggu aksi selesai" sebelum berpindah surface (8b butir 8); membuka dan menutup surface log, popup, dan modal; klik `[Cancel Activation]` (langkah 80); Search untuk menemukan baris target atau entri DD-04 dan `(←)` untuk mengosongkannya; Logout dan Login.
- Spec memuat 83 langkah, di atas sekitar 35 langkah. Alasan: seluruh blok satu kelas (asersi absence, kelas g) dengan baseline dan anchor positif sendiri per TC; tiap blok dimulai dari layar Handheld Reader dan tidak bergantung pada hasil blok sebelumnya (kecuali data DD-01 yang sengaja dihapus di blok TC-GS-HHR-188 pada akhir bagian Client A), sehingga kegagalan satu blok tidak menghilangkan makna blok lain; 23 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01) dan blok baca-log berpola (buka surface, bandingkan jumlah) tidak dihitung ke batas ukuran.
- Penutupan Popup `Activate Handheld Reader` pada TC-GS-HHR-370 (langkah 78 sampai 80): `[Submit]` yang ditolak T-12 meninggalkan hasil Sync pada popup, sehingga `✕` memunculkan dialog `Cancel Activation` (PRD §3.1 langkah 9 dan §4.2c, D-03; teks dialog dari TC-GS-HHR-89). Spec memverifikasi dialog itu, lalu klik `[Cancel Activation]` menurut A-1 (S-08); `Verifikasi` dialog bukan butir Expected TC-GS-HHR-370 dan dicatat di sini (S-03). Pada TC-GS-HHR-369 Sync gagal sebelum ada hasil Sync, sehingga popup (langkah 49) langsung tertutup tanpa dialog (PRD §3.1 langkah 9).
- Pembagian TC lintas spec: Edit No-Op dengan toast `No changes to save.` (TC-GS-HHR-106 dan 107) di spec 030; kegagalan 5xx tanpa entri tiga surface (TC-GS-HHR-352) di spec 027; Last Scanned dari Usage Event produk lain (TC-GS-HHR-185 dan 186) di spec 038; Event Log untuk aktivasi yang berhasil atau ditolak (TC-GS-HHR-364 sampai 367) di spec 067; pencatatan log per aksi (TC-GS-HHR-345 sampai 353) di spec 063.
- Temuan untuk QA:
  - TC-GS-HHR-187 dan 370 tidak menjelaskan cara menyelesaikan sesi pemindaian produk atau menyambungkan reader pada Client D; TC-GS-HHR-369 tidak menjelaskan cara membuat keadaan "driver lokal belum terpasang". Mekanisme simulasi tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE.
  - TC-GS-HHR-187 Expected b ("tidak mendapat entri baru untuk reader DD-04") tidak menyebut cara membaca Activity Log; spec membandingkan jumlah baris Search `Gudang Reader - 2` sebelum dan sesudah. TC tidak menyebut System Log aktor meski judulnya menyebutnya; spec tidak mengasersinya.
  - TC-GS-HHR-188 Search `Zebra RFID Reader - 1` tetap mencocokkan baris DD-06 yang bernama sama; spec mengidentifikasi DD-01 lewat Serial Number `SN-HHR-00101`. Expected c ("Tidak ada layar lain yang menampilkan Usage Event reader terhapus") tidak punya langkah observasi di TC; spec tidak mengasersinya terpisah (tercakup oleh Expected a dan b).
  - TC-GS-HHR-355 meminta klik `[Save]` tanpa perubahan; bila `[Save]` pada kasus ini dinonaktifkan atau menampilkan toast netral, TC tidak menyatakannya (spec 030 mengasersi toast netral `No changes to save.`); spec mengikuti langkah TC dan tidak mengasersi toast.
  - TC-GS-HHR-369 menyebut "tutup popup" tanpa menyatakan ada atau tidaknya dialog konfirmasi; spec menutup dengan `✕` saja karena belum ada hasil Sync (PRD §3.1 langkah 9) dan tidak menulis langkah bersyarat.
  - TC-GS-HHR-370 tidak menyebut Serial Number reader yang tersambung; spec menuliskan reader tersambung pada Client D sebagai kemampuan yang disediakan tim FE. Nama env password Client D `GS_CLIENTD_TC_PASSWORD` belum terdaftar di `spectra.config.ts` dan `.env.example` (didaftarkan owner suite).
