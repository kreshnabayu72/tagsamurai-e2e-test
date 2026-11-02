---
id: TC-GS-IMPORT-E2E-147-fault-injection-accept-dismiss-saran-gagal-atau-tanpa-respons-gagal
title: "Fault injection: Accept/Dismiss saran gagal atau tanpa respons, gagal memulai commit, timeout Import, koneksi putus, gagal unduh template"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-303
  - TC-GS-IMPORT-304
  - TC-GS-IMPORT-321
  - TC-GS-IMPORT-366
  - TC-GS-IMPORT-372
  - TC-GS-IMPORT-453
  - TC-GS-IMPORT-701
  - TC-GS-IMPORT-702
  - TC-GS-IMPORT-712
  - TC-GS-IMPORT-740
coverage:
  web: automated
---

# Fault injection: Accept/Dismiss saran gagal atau tanpa respons, gagal memulai commit, timeout Import, koneksi putus, gagal unduh template

## Prerequisites

- Mode: FE+BE (backend nyata) dengan `Spectra.intercept` parsial di atas backend nyata; asersi memakai state draft dan data di backend, jadi bukan `Mode: mock`.
- Suite serial (`parallel: false`): spec mengubah state global (mode mock AI, Client E commit) dan memakai draft Client C dan Client E yang dibagikan ke seluruh admin; lihat `suite.md`.
- Akun (login aktor pertama di hook `before`; ganti akun eksplisit di tengah spec, hook `after` mengembalikan sesi ke akun default suite):
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTC_TC_PASSWORD`: aktor pertama, dipakai TC-303, 304, 321, 701, 702, 712.
  - Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC_PASSWORD`: TC-366, 372, 740.
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC_PASSWORD`: TC-453.
  - Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach` untuk akun aktor pertama.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk setiap akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE):
  - `Spectra.intercept` di browser: membalas status 500, menahan respons tanpa jawaban sampai timeout FE, dan emulasi offline browser. Intercept dilepas segera setelah pemicu (S-09).
  - Mock layanan AI mode normal D-40 (tabel D-41 dan D-42); kontrol worker commit tetap normal (tidak dijeda) untuk TC-372.
  - Hook umur draft D-76 varian 1 (>=24 jam) untuk TC-366; skrip fixture seeding draft D-50 (12 baris) dan D-56 (250 baris) di Client E; skrip reset Client C dan Client E.
  - Kueri fixture status job commit Client E (selesai atau belum) untuk TC-372, dipakai saat browser offline.
  - Jeda nyata: TC-372 menunggu job commit latar belakang 250 baris selesai (sekitar 2 menit menurut TC) lewat kueri fixture status job, bukan lewat polling notifikasi lonceng atau muat ulang karena browser offline, dan bukan menunggu jam.
- Data Dinamis (milik spec ini; draft Client C dibuang oleh reset sehingga nama baris berkas literal sesuai Data Uji TC):
  - D-44 `ai-brand-long.csv`: kolom `Brand Name`; 1 baris Brand Name nilai sumber Brand D-41 (121 karakter).
  - `user-login-div-gudng.csv` (D-45): 1 baris Siti Rahmawati, `siti.rahmawati@example.com`, Division `Gudng`, Position kosong; mock D-42 untuk `Gudng`: `Gudang` 0,91.
  - D-50 `brand-12.csv` (Client E): 12 baris `Acme Corp`, `Lenovo`, `Zebra Technologies`, `Honeywell`, `Dell`, `HP Inc`, `Canon`, `Epson`, `Brother`, `Logitech`, `Cisco`, `Asus`.
  - D-56 `brand-250-impor.csv` (Client E): `Brand Impor 001` sampai `Brand Impor 250`. TC-372 menghasilkan 250 record Brand di Client E.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lepas semua intercept dan pulihkan koneksi browser; hapus draft Client C dan Client E; kembalikan mock AI ke normal; hapus Brand hasil commit TC-372 (`Brand Impor 001` sampai `Brand Impor 250`) dan reset hasil commit terakhir serta penanda Banner Hasil Commit Client E (D-47); kembalikan sesi ke akun default suite.

## Test Steps

### Client C: Accept dan Dismiss saran AI gagal

#### TC-GS-IMPORT-303: Accept gagal server pada AI Field Shortening

1. Reset Client C ke tanpa draft pada Sub-Tab Brand dan User Login (aksi fixture); pastikan mock AI mode normal
2. Muat ulang halaman Import > Brand
3. Klik `[Upload File]` di toolbar dan pilih berkas `ai-brand-long.csv`
4. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
5. Pasang intercept jaringan yang membalas permintaan Accept dengan status 500
6. Klik `[Accept]` pada badge saran sel Brand Name baris #1
7. Lepas intercept permintaan Accept
8. Verifikasi toast error: "Error, failed to update row."
9. Verifikasi sel Brand Name baris #1 tetap bernilai 121 karakter semula
10. Verifikasi badge saran pada sel Brand Name baris #1 tetap tampil
11. Verifikasi baris #1 tetap `error`
12. Tutup toast error

#### TC-GS-IMPORT-701: Accept tanpa respons pada AI Field Shortening

13. Klik `[Accept]` setelah memasang intercept yang menahan permintaan Accept tanpa jawaban sampai batas waktu (draft Brand TC-303 dipakai ulang; badge saran masih tampil)
14. Lepas intercept permintaan Accept
15. Verifikasi toast error persisten tanpa tombol aksi: "Connection problem. Please try again."
16. Verifikasi sel Brand Name baris #1 tetap bernilai 121 karakter semula
17. Verifikasi badge saran pada sel Brand Name baris #1 tetap tampil
18. Verifikasi baris #1 tetap `error`
19. Tutup toast error

#### TC-GS-IMPORT-304: Dismiss gagal server pada AI Field Shortening

20. Pasang intercept jaringan yang membalas permintaan Dismiss dengan status 500
21. Klik `[Dismiss]` pada badge saran sel Brand Name baris #1
22. Lepas intercept permintaan Dismiss
23. Verifikasi toast error: "Error, failed to dismiss suggestion."
24. Verifikasi badge saran tetap tampil pada sel Brand Name baris #1
25. Verifikasi baris #1 tetap `error`
26. Tutup toast error

#### TC-GS-IMPORT-702: Dismiss tanpa respons pada AI Field Shortening

27. Pasang intercept yang menahan permintaan Dismiss tanpa jawaban sampai batas waktu
28. Klik `[Dismiss]` pada badge saran sel Brand Name baris #1
29. Lepas intercept permintaan Dismiss
30. Verifikasi toast error persisten tanpa tombol aksi: "Connection problem. Please try again."
31. Verifikasi badge saran tetap tampil pada sel Brand Name baris #1
32. Verifikasi baris #1 tetap `error`
33. Tutup toast error

#### TC-GS-IMPORT-321: Accept gagal server pada AI Reference Suggestion

34. Reset Client C ke tanpa draft pada Sub-Tab Brand dan User Login (aksi fixture)
35. Muat ulang halaman Import > User Login
36. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-div-gudng.csv`
37. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
38. Pasang intercept jaringan yang membalas permintaan Accept dengan status 500
39. Klik `[Accept]` pada badge `Did you mean 'Gudang'?` di sel Division baris #1
40. Lepas intercept permintaan Accept
41. Verifikasi toast error: "Error, failed to update row."
42. Verifikasi sel Division baris #1 tetap `Gudng`
43. Verifikasi badge "Did you mean 'Gudang'?" tetap tampil
44. Verifikasi baris #1 tetap `error`
45. Tutup toast error

#### TC-GS-IMPORT-712: Accept saran Reference tanpa respons

46. Pasang intercept yang menahan permintaan Accept tanpa jawaban sampai batas waktu
47. Klik `[Accept]` pada badge `Did you mean 'Gudang'?` di sel Division baris #1
48. Lepas intercept permintaan Accept
49. Verifikasi toast error persisten tanpa tombol aksi: "Connection problem. Please try again."
50. Verifikasi sel Division baris #1 tetap `Gudng`
51. Verifikasi badge "Did you mean 'Gudang'?" tetap tampil
52. Verifikasi baris #1 tetap `error`
53. Tutup toast error

### Client E: gagal memulai commit, timeout Import, koneksi putus

54. Ganti akun: logout, lalu login sebagai Total Control Client E (Yoga Permana)

#### TC-GS-IMPORT-366: Gagal memulai commit

55. Reset Client E ke tanpa draft (aksi fixture), seed draft Brand D-50 (12 baris `pending`) dengan hook umur draft D-76 varian 1
56. Buka Global Settings > Import, pilih Sub-Tab Brand
57. Verifikasi Unsaved Banner tampil
58. Pasang intercept yang membalas permintaan Import dengan status 500
59. Klik `[Import (12)]`
60. Lepas intercept permintaan Import
61. Verifikasi toast error persisten: "Error, failed to import record."
62. Verifikasi `[Import (12)]` kembali Enabled
63. Verifikasi `[Discard]` Enabled
64. Verifikasi Pagination Staging Table menampilkan "Showing 1 - 10 of 12 items"
65. Verifikasi kartu Total Rows 12
66. Verifikasi kartu Ready to Import 12
67. Tutup toast error

#### TC-GS-IMPORT-740: Timeout saat Import

68. Pasang intercept yang menahan permintaan Import tanpa respons sampai timeout
69. Klik `[Import (12)]`
70. Lepas intercept permintaan Import
71. Verifikasi toast error persisten tanpa tombol aksi: "Connection problem. Please try again."
72. Verifikasi `[Import (12)]` kembali Enabled
73. Verifikasi Pagination Staging Table menampilkan "Showing 1 - 10 of 12 items"
74. Verifikasi kartu Total Rows 12
75. Verifikasi kartu Ready to Import 12
76. Tutup toast error

#### TC-GS-IMPORT-372: Koneksi terputus saat commit berjalan

77. Reset Client E ke tanpa draft (aksi fixture), seed draft Brand D-56 (250 baris `pending`), muat ulang halaman Import > Brand
78. Klik `[Import (250)]`
79. Setelah permintaan Import menerima respons, putuskan koneksi jaringan browser (emulasi offline)
80. Tunggu hingga job commit selesai: kueri fixture status job commit Client E sampai berstatus selesai (browser tetap offline)
81. Pulihkan koneksi jaringan browser
82. Muat ulang halaman Import > Brand
83. Verifikasi Dropzone tampil menggantikan Staging Table
84. Buka halaman Master Reference > Brand
85. Ketik Search `Brand Impor`, tekan Enter
86. Verifikasi Pagination tabel Brand Client E menampilkan "Showing 1 - 10 of 250 items"
87. Buka notifikasi lonceng
88. Verifikasi notifikasi lonceng memuat judul "Import Brand completed"
89. Verifikasi notifikasi lonceng memuat isi "250 records imported."
90. Verifikasi notifikasi lonceng memuat tombol `[Detail]`

### Client A: gagal unduh template

91. Ganti akun: logout, lalu login sebagai Total Control Client A (Sari Dewi)

#### TC-GS-IMPORT-453: Download Template gagal server

92. Buka Global Settings > Import, pilih Sub-Tab Brand
93. Pasang intercept yang membalas permintaan Download Template dengan status 500
94. Klik `[Download Template]`
95. Lepas intercept permintaan Download Template
96. Verifikasi toast error: "Error, failed to download Template-Import-Brand."
97. Verifikasi tidak ada berkas yang terunduh

## Notes

- Mode: FE+BE dengan intercept parsial. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fault injection (b). Pemicu berupa seeding draft, hook umur draft D-76, dan mock AI normal adalah pemicu state (P-2), bukan objek uji.
- Alasan melewati sekitar 35 langkah (97 langkah nominal): semua blok satu kelas (fault injection) dan berdiri sendiri; urutan blok dikelompokkan per akun (Client C, Client E, Client A) dengan langkah ganti akun eksplisit (langkah 54 dan 91), sehingga bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Bagian Client C memakai ulang draft yang sama untuk empat TC berurutan (TC-303, 701, 304, 702): Accept dan Dismiss gagal tidak mengubah draft, sehingga badge saran masih tampil untuk TC berikutnya; hal yang sama berlaku untuk TC-321 dan TC-712.
- TC-701 dan TC-702 diletakkan sesudah TC-303 dan sebelum TC-304 atau sesudah TC-304 mengikuti kebutuhan state: TC-701 (Accept) menyusul TC-303 (Accept) dan TC-702 (Dismiss) menyusul TC-304 (Dismiss). Urutan nomor TC dalam `sourceTc` tidak sama dengan urutan langkah.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 34, 55, 77), pembukaan Sub-Tab dan halaman, melepas intercept (langkah 7, 14, 22, 29, 40, 48, 60, 70, 95; S-09), menutup toast error sebelum asersi toast berikutnya (S-09), dan langkah 13 yang memasang intercept bersama klik. Langkah 80 menunggu job latar belakang selesai lewat kueri fixture status job (browser masih offline), bukan menunggu jam.
- Langkah 57 adalah `Verifikasi` tambahan di luar Expected TC-366 yang menjadi pembuktian prasyarat TC (Unsaved Banner tampil pada draft berumur >=24 jam).
- Langkah 97 (tidak ada berkas terunduh) didahului langkah 96 (toast tampil) sebagai anchor positif yang terhubung ke pemicu.
- Temuan untuk QA:
  - TC-GS-IMPORT-372 memicu koneksi terputus tanpa menyebut mekanisme pemutusan (emulasi offline atau intercept abort); spec memakai emulasi offline browser. Langkah "Tunggu 2 menit" pada TC diganti menunggu job commit selesai lewat kueri fixture status job (browser offline sehingga polling lonceng tidak mungkin) karena menunggu waktu nyata di atas ±30 detik tidak diizinkan konvensi; batas waktu yang diharapkan TC tidak berubah.
  - TC-GS-IMPORT-372 membuat 250 record Brand nyata di Client E; Pre-setup dan D-47 hanya menyebut `Brand Impor nnn` dihapus sesudah TC worker. Hook `after` menghapusnya; mekanisme penghapusan disediakan tim FE/BE.
  - TC-GS-IMPORT-303, 304, 321, 701, 702, 712 tidak menyebut apakah Accept atau Dismiss yang gagal meninggalkan badge saran pada baris yang sama untuk dipakai TC berikutnya; spec mengikuti Expected tiap TC dan memakai ulang draft secara berurutan (lihat Notes). Bila QA menghendaki draft baru per TC, urutan ini perlu direvisi.
  - TC-GS-IMPORT-366 dan TC-GS-IMPORT-740 tidak menyebut urutan antara kedua TC pada draft yang sama; spec memakai draft D-50 yang sama berurutan karena Import yang gagal tidak mengubah draft.
  - TC-GS-IMPORT-366 menyebut kartu Total Rows dan Ready to Import 12 pada Expected c tanpa menyebut kartu lain; spec hanya mengasersi dua kartu itu.
  - Post Condition TC-GS-IMPORT-303, 304, 321, 701, 702, 712 ("draft berisi 1 baris `error`") dan TC-GS-IMPORT-366, 740 ("tidak ada record Brand baru") tidak punya langkah observasi tersendiri dan tidak diasersi (S-01). Post Condition TC-GS-IMPORT-372 b dikonfirmasi oleh Expected b (Search 250 item); Post Condition a oleh Expected a.
  - Intercept pada `Spectra.intercept` untuk endpoint Accept, Dismiss, Import, Download Template tidak didefinisikan di TC selain kata "permintaan Accept/Dismiss/Import/Download Template"; nama endpoint diambil dari kontrak API modul (`import-staging`, `import-draft`) oleh tim FE.
