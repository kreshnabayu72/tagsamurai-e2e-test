---
id: TC-GS-IMPORT-E2E-150-multi-konteks-client-e-commit-bersamaan-dua-sesi-banner-hasil-commit
title: "Multi-konteks Client E: commit bersamaan dua sesi, Banner Hasil Commit sekali per administrator, halaman terbuka basi, commit berhenti"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-571
  - TC-GS-IMPORT-580
  - TC-GS-IMPORT-585
  - TC-GS-IMPORT-741
  - TC-GS-IMPORT-845
  - TC-GS-IMPORT-846
coverage:
  web: automated
---

# Multi-konteks Client E: commit bersamaan dua sesi, Banner Hasil Commit sekali per administrator, halaman terbuka basi, commit berhenti

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec melakukan commit nyata di Client E, mengubah state global (kontrol worker commit, jam atau penanda kemajuan job, hasil commit terakhir) dan Client E dipakai bersama spec commit lain; lihat `suite.md`.
- Dua konteks browser dalam satu spec, ditandai `[Sesi A]` dan `[Sesi B]` (keduanya mengasersi hasil di UI):
  - Sesi A (aktor utama): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > Import dibuka hook `beforeEach`.
  - Sesi B (administrator lain): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC2_PASSWORD`. Login di hook `before` pada konteks browser terpisah.
  - Akun pembaca: Import data (Read Only) Client E (Indra Gunawan) `importRead_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_IMPORTRO_PASSWORD`; dipakai lewat ganti akun eksplisit pada Sesi A di blok TC-585. Admin kedua Client E juga dipakai sebagai pemicu lewat sesi API (permintaan Import fixture) pada TC-585 dan TC-741.
  - Password tidak ditulis di spec atau fixture.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk ketiga akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - Dua konteks browser paralel; `Spectra.intercept` untuk menahan lalu melepas dua permintaan Import bersamaan (barrier) pada TC-571.
  - Kontrol worker commit D-47: mode 1 (dijeda sebelum job mulai) untuk TC-846, mode 3 (dijeda setelah batch pertama selesai, 100 baris terkomit, tidak dijalankan lagi selama TC) untuk TC-845; hook membaca jumlah percobaan pelanjutan job; fixture timestamp kemajuan job (memundurkan penanda kemajuan 16 menit).
  - Hook umur draft D-76 varian 1 (>=24 jam; `created_at` dimundurkan 25 jam) untuk TC-741, 845, 846.
  - Sesi API Admin kedua Client E untuk permintaan Import fixture (TC-585, TC-741) dan kueri fixture status job.
  - Skrip fixture reset Client E (D-47): hapus draft, lanjutkan worker, hapus Brand hasil commit (`Brand Impor nnn`, `Acme Corp`, `Lenovo`, `Dell`, `Autodel nn`, dan lainnya dari berkas commit), reset hasil commit terakhir dan penanda Banner Hasil Commit semua administrator.
  - Jeda nyata: polling "muat ulang setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)" menunggu job commit latar belakang selesai; satu jeda nyata 30 detik pada TC-741 (di batas ±30 detik) mengamati halaman terbuka yang tidak menerima push.
- Data Dinamis (milik spec ini; draft Client E dibuang dan hasil commit dihapus oleh reset):
  - D-50 `brand-12.csv`: 12 baris `Acme Corp`, `Lenovo`, `Zebra Technologies`, `Honeywell`, `Dell`, `HP Inc`, `Canon`, `Epson`, `Brother`, `Logitech`, `Cisco`, `Asus`.
  - D-56 `brand-250-impor.csv`: `Brand Impor 001` sampai `Brand Impor 250` (TC-571 dan TC-845).
  - D-64 `brand-13-autodel.csv`: baris #1 sampai #12 `Autodel 01` sampai `Autodel 12` (`pending`), baris #13 Brand Name 121 karakter huruf `A` (`error`) (TC-846).
- Pemulihan (hook `after`, tetap jalan walau spec gagal): lanjutkan worker commit, kembalikan penanda kemajuan job, hapus draft Client E, hapus Brand hasil commit, reset hasil commit terakhir dan penanda Banner Hasil Commit (D-47), tutup konteks Sesi B, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-571: Dua permintaan commit bersamaan dari dua sesi

1. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
2. [Sesi A] Muat ulang halaman Import > Brand
3. [Sesi B] Buka Global Settings > Import, pilih Sub-Tab Brand
4. [Sesi A] Pasang intercept yang menahan permintaan Import
5. [Sesi B] Pasang intercept yang menahan permintaan Import
6. [Sesi A] Klik `[Import (250)]`
7. [Sesi B] Klik `[Import (250)]`
8. Lepaskan kedua permintaan bersamaan
9. Verifikasi tepat satu dari kedua sesi tidak menampilkan dialog
10. Verifikasi sesi lainnya menampilkan Dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
11. Pada sesi yang menampilkan dialog, klik `[OK]`
12. [Sesi A] Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
13. [Sesi A] Verifikasi Dropzone tampil
14. [Sesi A] Buka halaman Master Reference > Brand
15. [Sesi A] Ketik Search `Brand Impor`, tekan Enter
16. [Sesi A] Verifikasi Pagination tabel Brand Client E menampilkan "Showing 1 - 10 of 250 items"

### TC-GS-IMPORT-580: Banner Hasil Commit ditampilkan sekali per administrator

17. Reset Client E (D-47) dan seed draft Brand D-50 (12 baris `pending`) lewat skrip fixture
18. [Sesi A] Buka Global Settings > Import, pilih Sub-Tab Brand
19. [Sesi A] Klik `[Import (12)]`
20. [Sesi A] Tunggu aksi selesai (permintaan mendapat respons)
21. [Sesi A] Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
22. [Sesi A] Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
23. [Sesi A] Klik `[×]` pada banner
24. [Sesi A] Muat ulang halaman Import > Brand
25. [Sesi A] Verifikasi Dropzone tampil
26. [Sesi A] Verifikasi Banner Hasil Commit tidak tampil
27. [Sesi B] Muat ulang halaman Import > Brand (pembukaan pertama sesudah commit selesai)
28. [Sesi B] Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
29. [Sesi B] Muat ulang halaman Import > Brand
30. [Sesi B] Verifikasi Dropzone tampil
31. [Sesi B] Verifikasi Banner Hasil Commit tidak tampil

### TC-GS-IMPORT-585: Banner Hasil Commit untuk pembaca Import data (Read Only)

32. Reset Client E (D-47) dan seed draft Brand D-50 (12 baris `pending`) lewat skrip fixture; pastikan Sesi A dan Sesi B tidak membuka Import > Brand sejak reset
33. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API) tanpa membuka halaman Import, lalu tunggu job terhapus (kueri fixture status job)
34. [Sesi A] Ganti akun: logout, lalu login sebagai Import data (Read Only) Client E (Indra Gunawan)
35. [Sesi A] Buka Global Settings > Import, pilih Sub-Tab Brand
36. [Sesi A] Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
37. [Sesi A] Muat ulang halaman Import > Brand
38. [Sesi A] Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil pada pembacaan kedua
39. [Sesi A] Ganti akun: logout, lalu login sebagai Total Control Client E (Yoga Permana)
40. [Sesi A] Buka Global Settings > Import, pilih Sub-Tab Brand
41. [Sesi A] Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
42. [Sesi A] Muat ulang halaman Import > Brand
43. [Sesi A] Verifikasi Dropzone tampil
44. [Sesi A] Verifikasi Banner Hasil Commit tidak tampil

### TC-GS-IMPORT-741: Halaman yang sudah terbuka tidak berubah saat commit selesai

45. Reset Client E (D-47) dan seed draft Brand D-50 (12 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
46. [Sesi A] Muat ulang halaman Import > Brand
47. [Sesi A] Verifikasi footer `[Import (12)]` Enabled
48. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
49. Tunggu job terhapus (kueri fixture status job)
50. [Sesi A] Amati halaman langkah 46 tanpa muat ulang selama 30 detik (jeda nyata)
51. [Sesi A] Verifikasi Staging Table tetap tampil dengan Pagination "Showing 1 - 10 of 12 items"
52. [Sesi A] Verifikasi `[Import (12)]` tetap Enabled
53. [Sesi A] Verifikasi Unsaved Banner tetap tampil
54. [Sesi A] Verifikasi Dropzone tidak tampil
55. [Sesi A] Verifikasi Banner Hasil Commit tidak tampil
56. [Sesi A] Muat ulang halaman Import > Brand
57. [Sesi A] Verifikasi Dropzone tampil
58. [Sesi A] Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil

### TC-GS-IMPORT-845: Commit kedua yang berhenti tidak menimpa Banner Hasil Commit commit tuntas pertama

59. Reset Client E (D-47) dan seed draft Brand D-50 (12 baris `pending`) lewat skrip fixture
60. [Sesi A] Muat ulang halaman Import > Brand
61. [Sesi A] Klik `[Import (12)]`
62. [Sesi A] Tunggu aksi selesai (permintaan mendapat respons)
63. [Sesi A] Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
64. [Sesi A] Verifikasi Dropzone tampil
65. [Sesi A] Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
66. [Sesi A] Klik `[Upload File]`
67. [Sesi A] Pilih berkas `brand-250-impor.csv` di file picker
68. [Sesi A] Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
69. [Sesi A] Tunggu aksi selesai (Modal Column Mapping tertutup)
70. Mundurkan umur draft 25 jam lewat hook umur draft D-76
71. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai, 100 baris terkomit) dan jangan jalankan lagi selama blok ini
72. [Sesi A] Klik `[Import (250)]`
73. [Sesi A] Tunggu aksi selesai (permintaan mendapat respons)
74. [Sesi A] Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
75. [Sesi A] Verifikasi kartu Total Rows menampilkan 150
76. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
77. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
78. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
79. Mundurkan lagi penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
80. [Sesi A] Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
81. [Sesi A] Verifikasi `[Discard]` Enabled (job kembali `draft`)
82. [Sesi A] Verifikasi Unsaved Banner tampil
83. [Sesi A] Verifikasi Banner Hasil Commit tidak tampil
84. [Sesi B] Muat ulang halaman Import > Brand
85. [Sesi B] Verifikasi Unsaved Banner tampil
86. [Sesi B] Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." (hasil commit tuntas pertama) tampil

### TC-GS-IMPORT-846: Banner commit sebelumnya tetap tampil selama commit berikutnya committing

87. Reset Client E (D-47) dan seed draft Brand D-50 (12 baris `pending`) lewat skrip fixture
88. [Sesi A] Muat ulang halaman Import > Brand
89. [Sesi A] Klik `[Import (12)]`
90. [Sesi A] Tunggu aksi selesai (permintaan mendapat respons)
91. [Sesi A] Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
92. [Sesi A] Verifikasi Dropzone tampil
93. [Sesi A] Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
94. [Sesi A] Klik `[Upload File]`
95. [Sesi A] Pilih berkas `brand-13-autodel.csv` di file picker
96. [Sesi A] Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
97. [Sesi A] Tunggu aksi selesai (Modal Column Mapping tertutup)
98. Mundurkan umur draft 25 jam lewat hook umur draft D-76
99. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai; job yang dimulai tetap `committing`)
100. [Sesi A] Klik `[Import (12)]`
101. [Sesi A] Tunggu aksi selesai (permintaan mendapat respons)
102. [Sesi B] Muat ulang halaman Import > Brand
103. [Sesi B] Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." (hasil commit pertama) tampil
104. [Sesi B] Verifikasi `[Discard]` Disabled
105. Lepaskan jeda worker commit lewat kontrol worker
106. [Sesi B] Muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil (batas tunggu 2 menit)
107. [Sesi B] Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
108. [Sesi B] Verifikasi hanya satu Banner Hasil Commit tampil
109. [Sesi B] Verifikasi Unsaved Banner tampil
110. [Sesi B] Verifikasi `[Discard]` Enabled

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (c); kontrol worker commit, jam atau penanda kemajuan, dan permintaan Import fixture Admin kedua hanya pemicu state (P-2), bukan objek uji. TC-GS-IMPORT-571 dan TC-GS-IMPORT-580 berstatus Manual di sumber (race dua sesi); keduanya tetap spec sesuai konvensi bagian 2 dan kebutuhan teknisnya tercatat di Prerequisites.
- Alasan melewati sekitar 35 langkah (110 langkah nominal): enam blok homogen (satu kelas multi-konteks, satu harness Client E), tiap blok berdiri sendiri dengan reset Client E (D-47) di awal sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Urutan blok mengikuti kenaikan kompleksitas harness: commit bersamaan, Banner Hasil Commit, halaman basi, lalu commit yang berhenti (kontrol worker dan penanda kemajuan).
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 17, 32, 45, 59, 87), pembukaan halaman dan Sub-Tab, pemasangan dan pelepasan intercept (langkah 4, 5, 8), polling "muat ulang setiap 5 detik" (langkah 12, 21, 63, 74, 77, 80, 91, 106) yang menunggu job latar belakang dan bukan menunggu jam, langkah ganti akun (langkah 34 dan 39), langkah 11 menutup dialog Import In Progress pada sesi yang kalah (S-03), serta langkah 23 menutup banner, dan langkah 101 (menunggu permintaan commit mendapat respons sebelum Sesi B membuka halaman). Langkah 20, 62, 73, dan 90 (Tunggu aksi selesai: permintaan mendapat respons) memisahkan klik `[Import (N)]` dari polling pada Sesi A. Langkah 69, 97 (Tunggu aksi selesai: menunggu aksi tanpa `Verifikasi` selesai sebelum hook umur draft memundurkan umur draft; penanda Modal Column Mapping tertutup).
- Login Sesi B pada hook `before` menggantikan langkah "Login sebagai Admin kedua Client E" pada TC-GS-IMPORT-580 langkah 5; langkah 27 memuat bahwa Sesi B memuat ulang Import > Brand untuk pertama kali sesudah commit selesai (reset D-47 menghapus penanda Banner Hasil Commit semua administrator di awal tiap blok).
- Muat ulang sesudah reset fixture: langkah 27, 46, 60, 84, 88, dan 102 memakai "Muat ulang halaman Import > Brand" karena reset D-47 membuang atau mengganti draft sementara halaman Import dari blok sebelumnya masih terbuka pada sesi itu (`suite.md`). Pada TC-GS-IMPORT-741 halaman Sesi A dimuat segar pada langkah 46 sebelum pemicu langkah 48 dan tidak dimuat ulang sampai langkah 56.
- Langkah 47 adalah `Verifikasi` tambahan di luar Expected TC-GS-IMPORT-741 yang membuktikan prasyarat (halaman terbuka dengan `[Import (12)]` Enabled) sebelum commit dimulai oleh Admin kedua. Langkah 13, 25, 30, 43, 57, 64, dan 92 (Dropzone tampil) menjadi anchor positif bagi asersi absence Banner Hasil Commit sesudah muat ulang (butir 2 bagian 8b).
- Langkah 9 dan 10 tidak menyebut sesi mana yang menang karena Expected TC-GS-IMPORT-571 menyatakan "tepat satu sesi" tanpa menentukan pemenang; langkah 11 menutup dialog Import In Progress pada sesi mana pun yang menampilkannya (S-03), sehingga langkah berikutnya tidak berjalan di balik dialog terbuka ketika Sesi B yang kalah.
- Temuan untuk QA:
  - TC-GS-IMPORT-571 berstatus Manual Only (race) tetapi Expected-nya deterministik secara agregat (tepat satu sesi tanpa dialog); alasan Manual tidak menggugurkan spec. Pemenang race tidak ditentukan TC, sehingga barrier dua sesi dan pelepasan serentak disediakan tim FE.
  - TC-GS-IMPORT-580 berstatus Manual Only padahal langkahnya sekuensial dan deterministik (dua sesi berurutan); mekanisme dua sesi dipertahankan sebagai UI kedua karena hasil di Sesi B diasersi.
  - TC-GS-IMPORT-585 langkah 1 menyebut permintaan Import fixture atas nama Admin kedua tanpa menyebut mekanismenya; spec memakai sesi API Admin kedua (pemicu, P-2) yang disediakan tim FE/BE.
  - TC-GS-IMPORT-845 dan 846 merujuk umur draft kedua "dimundurkan 25 jam pada langkah 5" tetapi memakai hook D-76 yang menyebut `created_at` atau jam server; spec memakai `created_at`. TC-GS-IMPORT-845 tidak menyebut apakah "mundurkan penanda kemajuan job 16 menit" dua kali (langkah 74 dan 77) dilakukan pada penanda yang sama atau pada job pelanjutan baru; spec mengikuti Langkah TC.
  - TC-GS-IMPORT-845 Expected c dan TC-GS-IMPORT-846 mengasersi hitungan yang hanya bisa dibaca lewat hook (jumlah percobaan pelanjutan); hook baca itu tidak disebut D-47 per nomor mode (D-47 hanya menyebut "hook membaca jumlah percobaan pelanjutan job").
  - Post Condition TC-GS-IMPORT-571, 580, 585, 741 ("draft dihapus", "N record Brand baru tersimpan", "banner ditandai ditampilkan") dan TC-GS-IMPORT-845, 846 (draft 150 baris atau 1 baris `error`, 112 atau 24 record Brand) tidak punya langkah observasi tersendiri selain yang tercakup Expected dan tidak diasersi tambahan (S-01). Pengecualian: TC-GS-IMPORT-571 Post Condition b dikonfirmasi oleh Expected c.
  - TC-GS-IMPORT-846 Expected b menyebut `[Discard]` Disabled selama commit berikutnya `committing`; tidak ada rujukan PRD di TC untuk alasan Disabled (selain §4.3 Committing).
  - Kebutuhan kontrol worker, hook penanda kemajuan, dan hook umur draft tidak didefinisikan di TC selain D-47 dan D-76; disediakan tim FE/BE.
  - Penanda selesai untuk langkah 101 (klik `[Import (12)]` Sesi A sebelum Sesi B membuka halaman) tidak disebut di TC, PRD, atau spec ini; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di surface Sesi A.
