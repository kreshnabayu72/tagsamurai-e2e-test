---
id: TC-FA-CAID-E2E-099-pencatatan-log-absence-request-validasi-ditolak
title: "Pencatatan Log Absence: Request Save dengan Payload Tidak Valid Ditolak Tanpa Entri Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-306
  - TC-FA-CAID-307
  - TC-FA-CAID-308
  - TC-FA-CAID-309
  - TC-FA-CAID-337
  - TC-FA-CAID-338
coverage:
  web: automated
---

# Pencatatan Log Absence: Request Save dengan Payload Tidak Valid Ditolak Tanpa Entri Log

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 dan aset A1 sampai A5 (Pre-setup No 11) di `beforeEach` dan `after` lewat sesi API aktor. Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company). Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): penyunting request dan respons pada sesi otomasi (Pre-setup No 26) untuk mengubah payload request Save yang dikirim dari browser (langkah 3, 18, 33, 48, 63, dan 78) dan mengamati respons server; konfirmasi otomatis dialog `beforeunload` bawaan browser oleh harness untuk muat ulang pada form yang belum disimpan (langkah 6, 21, 36, 51, 66, dan 81); kemampuan membaca jumlah entri Object `Custom Asset ID` di Modal Changelog: Custom Asset ID, System Log (Detail User), dan Activity Log (tab User Action) sebelum dan sesudah request (audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12).
- State: tidak ada perubahan tersimpan yang diharapkan; semua request ditolak server. Entri log yang sudah ada tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-306: Request Save dengan daftar segmen kosong tidak menulis entri log

1. Catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID, System Log (Detail pengguna Sarah Johnson), dan Activity Log (tab User Action)
2. Pilih Separator `- (Dash)`
3. Ubah payload request Save lewat penyunting sehingga daftar segmen kosong
4. Klik `[Save]`
5. Verifikasi alert inline severity danger tampil tepat di atas `[Save]` berbunyi `Select at least one segment`
6. Muat ulang halaman
7. Buka Modal Changelog: Custom Asset ID
8. Verifikasi tabel Changelog termuat dengan header kolom tampil
9. Verifikasi jumlah entri Changelog tidak bertambah dibanding baseline
10. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
11. Verifikasi tabel System Log termuat dengan header kolom tampil
12. Verifikasi jumlah entri System Log tidak bertambah dibanding baseline
13. Buka Fixed Asset > Activity Log > tab User Action
14. Verifikasi tabel Activity Log termuat dengan header kolom tampil
15. Verifikasi jumlah entri Activity Log tidak bertambah dibanding baseline

### TC-FA-CAID-307: Request Save tanpa segmen Asset Increment tidak menulis entri log

16. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog, System Log, dan Activity Log
17. Pilih Separator `- (Dash)`
18. Ubah payload request Save lewat penyunting sehingga daftar segmen hanya memuat `Group Code` dan `Category Code` tanpa `Asset Increment`
19. Klik `[Save]`
20. Verifikasi alert inline di atas `[Save]` berbunyi `Select at least one segment`
21. Muat ulang halaman
22. Buka Modal Changelog: Custom Asset ID
23. Verifikasi tabel Changelog termuat dengan header kolom tampil
24. Verifikasi jumlah entri Changelog tidak bertambah dibanding baseline
25. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
26. Verifikasi tabel System Log termuat dengan header kolom tampil
27. Verifikasi jumlah entri System Log tidak bertambah dibanding baseline
28. Buka Fixed Asset > Activity Log > tab User Action
29. Verifikasi tabel Activity Log termuat dengan header kolom tampil
30. Verifikasi jumlah entri Activity Log tidak bertambah dibanding baseline

### TC-FA-CAID-308: Request Save tanpa Separator tidak menulis entri log

31. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog, System Log, dan Activity Log
32. Centang `Initial Company` dan ketik `ABC` pada input Initial Company
33. Ubah payload request Save lewat penyunting sehingga Separator kosong
34. Klik `[Save]`
35. Verifikasi server menolak request dengan pesan `Separator must not be empty`
36. Muat ulang halaman
37. Buka Modal Changelog: Custom Asset ID
38. Verifikasi tabel Changelog termuat dengan header kolom tampil
39. Verifikasi jumlah entri Changelog tidak bertambah dibanding baseline
40. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
41. Verifikasi tabel System Log termuat dengan header kolom tampil
42. Verifikasi jumlah entri System Log tidak bertambah dibanding baseline
43. Buka Fixed Asset > Activity Log > tab User Action
44. Verifikasi tabel Activity Log termuat dengan header kolom tampil
45. Verifikasi jumlah entri Activity Log tidak bertambah dibanding baseline

### TC-FA-CAID-309: Request Save dengan Initial Company dicentang tanpa nilai tidak menulis entri log

46. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog, System Log, dan Activity Log
47. Pilih Separator `- (Dash)`
48. Ubah payload request Save lewat penyunting sehingga entry Initial Company dicentang dengan nilai kosong
49. Klik `[Save]`
50. Verifikasi server menolak request dengan pesan `Initial company must not be empty`
51. Muat ulang halaman
52. Buka Modal Changelog: Custom Asset ID
53. Verifikasi tabel Changelog termuat dengan header kolom tampil
54. Verifikasi jumlah entri Changelog tidak bertambah dibanding baseline
55. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
56. Verifikasi tabel System Log termuat dengan header kolom tampil
57. Verifikasi jumlah entri System Log tidak bertambah dibanding baseline
58. Buka Fixed Asset > Activity Log > tab User Action
59. Verifikasi tabel Activity Log termuat dengan header kolom tampil
60. Verifikasi jumlah entri Activity Log tidak bertambah dibanding baseline

### TC-FA-CAID-337: Request Save dengan Initial Company berkarakter di luar A-Z dan 0-9 tidak menulis entri log

61. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog, System Log, dan Activity Log
62. Pilih Separator `- (Dash)`
63. Ubah payload request Save lewat penyunting sehingga entry Initial Company dicentang dengan nilai `AB-1!`
64. Klik `[Save]`
65. Tunggu aksi selesai
66. Muat ulang tab Custom Asset ID
67. Buka Modal Changelog: Custom Asset ID
68. Verifikasi tabel Changelog termuat dengan header kolom tampil
69. Verifikasi jumlah entri Changelog tidak bertambah dibanding baseline
70. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
71. Verifikasi tabel System Log termuat dengan header kolom tampil
72. Verifikasi jumlah entri System Log tidak bertambah dibanding baseline
73. Buka Fixed Asset > Activity Log > tab User Action
74. Verifikasi tabel Activity Log termuat dengan header kolom tampil
75. Verifikasi jumlah entri Activity Log tidak bertambah dibanding baseline

### TC-FA-CAID-338: Request Save dengan Initial Company lebih dari 5 karakter tidak menulis entri log

76. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog, System Log, dan Activity Log
77. Pilih Separator `- (Dash)`
78. Ubah payload request Save lewat penyunting sehingga entry Initial Company dicentang dengan nilai `ABCDEF`
79. Klik `[Save]`
80. Tunggu aksi selesai
81. Muat ulang tab Custom Asset ID
82. Buka Modal Changelog: Custom Asset ID
83. Verifikasi tabel Changelog termuat dengan header kolom tampil
84. Verifikasi jumlah entri Changelog tidak bertambah dibanding baseline
85. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
86. Verifikasi tabel System Log termuat dengan header kolom tampil
87. Verifikasi jumlah entri System Log tidak bertambah dibanding baseline
88. Buka Fixed Asset > Activity Log > tab User Action
89. Verifikasi tabel Activity Log termuat dengan header kolom tampil
90. Verifikasi jumlah entri Activity Log tidak bertambah dibanding baseline

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 90 langkah, di atas smell 35 langkah. Alasan: seluruhnya satu kelas harness (kelas g, asersi absence log atas request Save yang ditolak server) dengan harness penyunting request yang sama, dan tiap TC berdiri sendiri dengan baseline sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna; blok baca-log berpola (buka surface, `Verifikasi` tabel termuat, `Verifikasi` jumlah) tidak dihitung menurut bagian 3 prinsip 13 (enam blok sembilan langkah: langkah 7 sampai 15, 22 sampai 30, 37 sampai 45, 52 sampai 60, 67 sampai 75, dan 82 sampai 90), sehingga langkah di luar blok itu 36 (6 per TC).
- Bagian 8b butir 1 dan `P-5` butir (a): pemicu (penyunting payload lalu `[Save]`) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; asersi spec ini hanya penolakan (anchor) dan jumlah entri log terhadap baseline. Status respons dan state data (konfigurasi tersimpan dan Asset ID) TC-FA-CAID-306 sampai 309, 337, dan 338 diasersi di spec 027 dan 028.
- Anchor positif asersi absence (bagian 8b butir 2): alert inline D-03 pada langkah 5 dan 20 serta pesan penolakan server pada langkah 35 dan 50 (ditambahkan sebagai anchor penolakan dari Expected a TC, S-03), jumlah awal yang dicatat pada langkah 1, 16, 31, 46, 61, dan 76, dan `Verifikasi` tabel log termuat dengan header kolom pada tiap surface sebelum jumlah diasersi. TC-FA-CAID-337 dan 338 tidak memberi pesan penolakan (G-13) sehingga anchornya baseline dan tabel termuat.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 16, 31, 46, 61, dan 76 (membuka halaman dan mencatat baseline, S-12), langkah 2, 17, 32, 47, 62, dan 77 (menyiapkan form agar `[Save]` aktif, sesuai Langkah Uji TC), langkah 65 dan 80 (Tunggu aksi selesai sebelum muat ulang karena hasil `[Save]` tidak diasersi, bagian 8b butir 8), serta seluruh langkah membuka surface log. Muat ulang (langkah 6, 21, 36, 51, 66, dan 81) terjadi pada form yang masih dirty; konfirmasi `beforeunload` ditangani harness sesuai Prerequisites, sehingga form berakhir pristine pada nilai tersimpan.
- Pembagian TC lintas spec: TC-FA-CAID-306 sampai 309 juga ada di spec 027 dan TC-FA-CAID-337 dan 338 di spec 028 (hanya status respons dan state data); TC-FA-CAID-303 sampai 305 ada di spec 098; TC-FA-CAID-312 dan 313 ada di spec 100.
- Temuan untuk QA:
  - TC-FA-CAID-306 sampai 309 menyebut "tidak ada mass update" tanpa langkah observasi; hal itu tidak diasersi.
  - TC-FA-CAID-308 a dan TC-FA-CAID-309 a menyebut "Server menolak request dengan pesan ..." tanpa menyebut tempat pesan tampil di UI; spec mengasersi isi respons server yang diamati lewat penyunting respons (kemampuan disediakan tim FE).
  - TC-FA-CAID-306 b menyebut "Asset ID aset ... tidak berubah" dan TC-FA-CAID-337 dan 338 membuka Modal Changelog, System Log, dan Activity Log hanya untuk asersi absence; asersi state data ada di spec 027 dan 028.
  - Pemicu TC-FA-CAID-308 ("Ubah Initial Company menjadi tercentang bernilai `ABC` agar `[Save]` aktif") ditulis sebagai langkah 32 mengikuti Langkah Uji.
  - Post Condition TC-FA-CAID-306 sampai 309, 337, dan 338 tidak diasersi karena TC tidak memberi langkah observasinya.
