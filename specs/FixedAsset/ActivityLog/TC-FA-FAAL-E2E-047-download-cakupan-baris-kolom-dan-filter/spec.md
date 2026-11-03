---
id: TC-FA-FAAL-E2E-047-download-cakupan-baris-kolom-dan-filter
title: "Download: Seluruh Baris, Kolom Tersembunyi, Satu Kolom Tersisa, Hasil Kosong, serta Search dan Filter Aktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-166
  - TC-FA-FAAL-167
  - TC-FA-FAAL-168
  - TC-FA-FAAL-169
  - TC-FA-FAAL-184
  - TC-FA-FAAL-189
coverage:
  web: automated
---

# Download: Seluruh Baris, Kolom Tersembunyi, Satu Kolom Tersisa, Hasil Kosong, serta Search dan Filter Aktif

## Prerequisites

- Mode: FE+BE (backend nyata; unduhan nyata tanpa intercept).
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Tab Session terbuka).
- Data Pre-setup: Data Log Tab Session SS-01 sampai SS-11 (#11) dan Tab User Action UA-01 sampai UA-15 (#12), disediakan lewat seed suite. Identitas data dirujuk lewat `fixtures/activity-log.json` (belum ada, disediakan tim FE; nama kunci ditetapkan tim FE). Data Dinamis: tidak ada.
- Data Filter dan Search (dari TC sumber): Tab Session Filter Division `Finance` dan Search `Hendra` (hasil pada data seed: SS-09); Tab User Action Filter Action `Assign` (hasil pada data seed: UA-01 dan UA-07). Kombinasi kosong: Tab Session Position `Manager` dan Division `Operations`; Tab User Action Action `Delete` dan Object `Audit`; keduanya tidak memiliki baris pada data seed.
- Jendela Seed (precondition TC-FA-FAAL-166, 167, 184, 189): Tab Session Filter Date `14/07/26` sampai `16/07/26` (memuat SS-01 sampai SS-11) diterapkan di langkah 1 dan ulang di langkah 39; Tab User Action Filter Date `18/06/26` sampai `18/06/26` (memuat UA-01 sampai UA-15) diterapkan di langkah 6 dan ulang di langkah 47. Pengulangan perlu karena `[Clear Field]` mengosongkan seluruh Filter termasuk Date. Jumlah baris berkas diasersi sesuai TC (11 dan 15 baris; satu dan dua baris pada Search dan Filter TC-FA-FAAL-167) karena dihitung hanya atas baris seed. Rows per page memakai nilai default 10.
- Kemampuan teknis (disediakan tim FE): penangkap unduhan browser dan parser CSV untuk membaca header dan jumlah baris berkas.
- State yang diubah dan pemulihannya: Filter Date dan Filter lain kedua tab (langkah 38 dan 46 mengosongkannya; Filter Date di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya), serta konfigurasi kolom (Column Visibility dan Setup Column) kedua tab. Langkah 20, 22 dan 32 memulihkan konfigurasi kolom; hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API, pemulihan konfigurasi kolom) mengikuti `suite.md`.
- Env var: `FA_TC_PASSWORD`, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps
1. Di Tab Session klik icon Filter, pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date, klik `[Apply]`

### TC-FA-FAAL-166: Download tanpa Search dan Filter memuat seluruh baris

2. Di Tab Session klik icon Download, pilih `Download as CSV`
3. Verifikasi berkas CSV Tab Session memuat header
4. Verifikasi berkas CSV Tab Session memuat 11 baris data (SS-01 sampai SS-11, lebih banyak dari satu halaman)
5. Klik tab User Action
6. Di Tab User Action klik icon Filter, pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date, klik `[Apply]`
7. Klik icon Download, pilih `Download as CSV`
8. Verifikasi berkas CSV Tab User Action memuat header
9. Verifikasi berkas CSV Tab User Action memuat 15 baris data (UA-01 sampai UA-15, lebih banyak dari satu halaman)

### TC-FA-FAAL-168: Kolom yang disembunyikan tidak ikut diekspor

10. Klik tab Session
11. Buka Column Visibility lewat header Actions (⋯), sembunyikan kolom Note
12. Klik icon Download, pilih `Download as CSV`
13. Verifikasi tidak ada toast peringatan kolom parsial
14. Verifikasi header berkas Tab Session `Date, User, Employee ID, Position, Division, Activity, Status, IP Address, Device/Browser` tanpa Note
15. Klik tab User Action
16. Buka Column Visibility lewat header Actions (⋯), sembunyikan kolom Field
17. Klik icon Download, pilih `Download as CSV`
18. Verifikasi tidak ada toast peringatan kolom parsial
19. Verifikasi header berkas Tab User Action `Date, Action, Object, Name, Old Value, New Value, Modified By` tanpa Field

### TC-FA-FAAL-169: Kolom yang ditampilkan kembali ikut diekspor lagi

20. Tampilkan kembali kolom Field lewat Column Visibility di Tab User Action
21. Klik tab Session
22. Tampilkan kembali kolom Note lewat Column Visibility
23. Klik icon Download, pilih `Download as CSV`
24. Verifikasi header berkas Tab Session memuat Note kembali
25. Verifikasi header berkas Tab Session memuat 10 kolom sesuai urutan tabel

### TC-FA-FAAL-189: Download saat hanya satu kolom tersisa

26. Lewat Setup Column di Tab Session sembunyikan sembilan kolom hingga hanya Device/Browser tampil, klik `[Save]`
27. Verifikasi icon Download aktif
28. Klik icon Download, pilih `Download as CSV`
29. Verifikasi tidak ada toast error
30. Verifikasi berkas memuat satu kolom `Device/Browser`
31. Verifikasi berkas memuat 11 baris data
32. Lewat Setup Column tampilkan kembali sembilan kolom yang disembunyikan, klik `[Save]`

### TC-FA-FAAL-184: Download dengan hasil Filter kosong

33. Di Tab Session terapkan Filter Position `Manager` dan Division `Operations`
34. Klik icon Download, pilih `Download as CSV`
35. Verifikasi tidak ada toast error
36. Verifikasi berkas CSV Tab Session memuat baris header kolom yang tampil
37. Verifikasi berkas CSV Tab Session tidak memuat baris data
38. Klik `[Clear Field]`, klik `[Apply]`
39. Di Tab Session klik icon Filter, pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date, klik `[Apply]`
40. Klik tab User Action
41. Terapkan Filter Action `Delete` dan Object `Audit`
42. Klik icon Download, pilih `Download as CSV`
43. Verifikasi tidak ada toast error
44. Verifikasi berkas CSV Tab User Action memuat baris header kolom yang tampil
45. Verifikasi berkas CSV Tab User Action tidak memuat baris data
46. Klik `[Clear Field]`, klik `[Apply]`
47. Di Tab User Action klik icon Filter, pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date, klik `[Apply]`

### TC-FA-FAAL-167: Download mengikuti Search dan Filter aktif per tab

48. Klik tab Session
49. Terapkan Filter Division `Finance`
50. Ketik Search `Hendra`, tekan Enter
51. Klik icon Download, pilih `Download as CSV`
52. Verifikasi berkas CSV Tab Session memuat header
53. Verifikasi berkas CSV Tab Session memuat satu baris data (SS-09) hasil Search dan Filter
54. Klik tab User Action
55. Terapkan Filter Action `Assign`
56. Klik icon Download, pilih `Download as CSV`
57. Verifikasi berkas CSV Tab User Action memuat header
58. Verifikasi berkas CSV Tab User Action memuat dua baris data (UA-01 dan UA-07) hasil Filter

## Notes

- Mode: FE+BE. Asersi spec ini adalah jumlah baris, nama kolom (header), dan ada tidaknya toast; keduanya fungsional menurut bagian 3 prinsip 13f. Isi sel berkas ada di spec 048 dan 049.
- Alasan melewati sekitar 35 langkah (58 langkah): seluruh blok memiliki satu topik (cakupan baris dan kolom berkas Download), satu dataset (#11 dan #12), dan satu harness (penangkap unduhan dan parser CSV); tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan blok berbeda dari urutan nomor TC sumber (S-10): blok kolom (TC-FA-FAAL-168, 169, 189) dijalankan sebelum blok Filter (TC-FA-FAAL-184, 167) agar tidak ada langkah pembersih Filter tambahan di antaranya, dan TC-FA-FAAL-167 berada di akhir karena asersinya bergantung pada Filter yang aktif.
- TC-FA-FAAL-169 langkah 1 menyembunyikan lalu menampilkan kembali kolom Note; kolom Note sudah tersembunyi sejak langkah 11 (TC-FA-FAAL-168), sehingga langkah 22 hanya menampilkannya kembali.
- Urutan asersi pada langkah 13 sampai 14, 18 sampai 19, 29 sampai 31, 35 sampai 36, 43 sampai 44: absence toast ditulis segera setelah pemicu dan sebelum asersi berkas (bagian 8b butir 11). Langkah 27 (icon Download aktif) ditulis sebelum langkah 28 karena asersi state aktif harus sebelum aksi.
- Langkah penghubung (S-03, S-09): langkah 5, 10, 15, 21, 40, 48 dan 54 (pindah tab); langkah 1, 6, 39 dan 47 (menerapkan Filter Date Jendela Seed); langkah 20 (pemulihan kolom Field dari langkah 16); langkah 32 (pemulihan Setup Column); langkah 38 dan 46 (membersihkan Filter).
- Temuan untuk QA:
  - TC-FA-FAAL-166, 167, 184, dan 189 memberi precondition Filter Date Jendela Seed pada kedua tab agar jumlah baris berkas (11, 15, satu, dan dua baris) tidak bergantung pada baris log lain; spec menerapkannya di langkah 1 dan 6, dan menerapkannya ulang di langkah 39 dan 47 sesudah `[Clear Field]`. TC tidak menyatakan bahwa Filter Date hilang bersama `[Clear Field]`; spec mengasumsikan semua Filter terkosongkan.
  - TC-FA-FAAL-189 tidak menyebut cara memulihkan kolom; langkah 32 ditambahkan sebagai pemulihan (S-09).
