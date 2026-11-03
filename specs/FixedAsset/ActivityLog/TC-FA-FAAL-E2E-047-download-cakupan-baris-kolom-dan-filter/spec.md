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
- Jendela Seed (precondition TC-FA-FAAL-166, 167, 184, 189): Tab Session Filter Date `14/07/26` sampai `16/07/26` (memuat SS-01 sampai SS-11) diterapkan di langkah 1 dan ulang di langkah 36; Tab User Action Filter Date `18/06/26` sampai `18/06/26` (memuat UA-01 sampai UA-15) diterapkan di langkah 5 dan ulang di langkah 43. Pengulangan perlu karena `[Clear Field]` mengosongkan seluruh Filter termasuk Date. Jumlah baris berkas diasersi sesuai TC (11 dan 15 baris; satu dan dua baris pada Search dan Filter TC-FA-FAAL-167) karena dihitung hanya atas baris seed. Rows per page memakai nilai default 10.
- Kemampuan teknis (disediakan tim FE): penangkap unduhan browser dan parser CSV untuk membaca header dan jumlah baris berkas.
- State yang diubah dan pemulihannya: Filter Date dan Filter lain kedua tab (langkah 35 dan 42 mengosongkannya; Filter Date di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya), serta konfigurasi kolom (Column Visibility dan Setup Column) kedua tab. Langkah 18, 20 dan 30 memulihkan konfigurasi kolom; hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API, pemulihan konfigurasi kolom) mengikuti `suite.md`.
- Env var: `FA_TC_PASSWORD`, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps
1. Di Tab Session klik icon Filter, pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date, klik `[Apply]`

### TC-FA-FAAL-166: Download tanpa Search dan Filter memuat seluruh baris

2. Di Tab Session klik icon Download, pilih `Download as CSV`
3. Verifikasi berkas CSV Tab Session memuat header dan 11 baris data (SS-01 sampai SS-11, lebih banyak dari satu halaman)
4. Klik tab User Action
5. Di Tab User Action klik icon Filter, pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date, klik `[Apply]`
6. Klik icon Download, pilih `Download as CSV`
7. Verifikasi berkas CSV Tab User Action memuat header dan 15 baris data (UA-01 sampai UA-15, lebih banyak dari satu halaman)

### TC-FA-FAAL-168: Kolom yang disembunyikan tidak ikut diekspor

8. Klik tab Session
9. Buka Column Visibility lewat header Actions (⋯), sembunyikan kolom Note
10. Klik icon Download, pilih `Download as CSV`
11. Verifikasi tidak ada toast peringatan kolom parsial
12. Verifikasi header berkas Tab Session `Date, User, Employee ID, Position, Division, Activity, Status, IP Address, Device/Browser` tanpa Note
13. Klik tab User Action
14. Buka Column Visibility lewat header Actions (⋯), sembunyikan kolom Field
15. Klik icon Download, pilih `Download as CSV`
16. Verifikasi tidak ada toast peringatan kolom parsial
17. Verifikasi header berkas Tab User Action `Date, Action, Object, Name, Old Value, New Value, Modified By` tanpa Field

### TC-FA-FAAL-169: Kolom yang ditampilkan kembali ikut diekspor lagi

18. Tampilkan kembali kolom Field lewat Column Visibility di Tab User Action
19. Klik tab Session
20. Tampilkan kembali kolom Note lewat Column Visibility
21. Klik icon Download, pilih `Download as CSV`
22. Verifikasi header berkas Tab Session memuat Note kembali
23. Verifikasi header berkas Tab Session memuat 10 kolom sesuai urutan tabel

### TC-FA-FAAL-189: Download saat hanya satu kolom tersisa

24. Lewat Setup Column di Tab Session sembunyikan sembilan kolom hingga hanya Device/Browser tampil, klik `[Save]`
25. Verifikasi icon Download aktif
26. Klik icon Download, pilih `Download as CSV`
27. Verifikasi tidak ada toast error
28. Verifikasi berkas memuat satu kolom `Device/Browser`
29. Verifikasi berkas memuat 11 baris data
30. Lewat Setup Column tampilkan kembali sembilan kolom yang disembunyikan, klik `[Save]`

### TC-FA-FAAL-184: Download dengan hasil Filter kosong

31. Di Tab Session terapkan Filter Position `Manager` dan Division `Operations`
32. Klik icon Download, pilih `Download as CSV`
33. Verifikasi tidak ada toast error
34. Verifikasi berkas CSV Tab Session hanya memuat baris header kolom yang tampil dan tidak ada baris data
35. Klik `[Clear Field]`, klik `[Apply]`
36. Di Tab Session klik icon Filter, pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date, klik `[Apply]`
37. Klik tab User Action
38. Terapkan Filter Action `Delete` dan Object `Audit`
39. Klik icon Download, pilih `Download as CSV`
40. Verifikasi tidak ada toast error
41. Verifikasi berkas CSV Tab User Action hanya memuat baris header kolom yang tampil dan tidak ada baris data
42. Klik `[Clear Field]`, klik `[Apply]`
43. Di Tab User Action klik icon Filter, pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date, klik `[Apply]`

### TC-FA-FAAL-167: Download mengikuti Search dan Filter aktif per tab

44. Klik tab Session
45. Terapkan Filter Division `Finance`
46. Ketik Search `Hendra`, tekan Enter
47. Klik icon Download, pilih `Download as CSV`
48. Verifikasi berkas CSV Tab Session memuat header dan satu baris data (SS-09) hasil Search dan Filter
49. Klik tab User Action
50. Terapkan Filter Action `Assign`
51. Klik icon Download, pilih `Download as CSV`
52. Verifikasi berkas CSV Tab User Action memuat header dan dua baris data (UA-01 dan UA-07) hasil Filter

## Notes

- Mode: FE+BE. Asersi spec ini adalah jumlah baris, nama kolom (header), dan ada tidaknya toast; keduanya fungsional menurut bagian 3 prinsip 13f. Isi sel berkas ada di spec 048 dan 049.
- Alasan melewati sekitar 35 langkah (52 langkah): seluruh blok memiliki satu topik (cakupan baris dan kolom berkas Download), satu dataset (#11 dan #12), dan satu harness (penangkap unduhan dan parser CSV); tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan blok berbeda dari urutan nomor TC sumber (S-10): blok kolom (TC-FA-FAAL-168, 169, 189) dijalankan sebelum blok Filter (TC-FA-FAAL-184, 167) agar tidak ada langkah pembersih Filter tambahan di antaranya, dan TC-FA-FAAL-167 berada di akhir karena asersinya bergantung pada Filter yang aktif.
- TC-FA-FAAL-169 langkah 1 menyembunyikan lalu menampilkan kembali kolom Note; kolom Note sudah tersembunyi sejak langkah 9 (TC-FA-FAAL-168), sehingga langkah 20 hanya menampilkannya kembali.
- Urutan asersi pada langkah 11 sampai 12, 16 sampai 17, 27 sampai 29, 33 sampai 34, 40 sampai 41: absence toast ditulis segera setelah pemicu dan sebelum asersi berkas (bagian 8b butir 11). Langkah 25 (icon Download aktif) ditulis sebelum langkah 26 karena asersi state aktif harus sebelum aksi.
- Langkah penghubung (S-03, S-09): langkah 4, 8, 13, 19, 37, 44 dan 49 (pindah tab); langkah 1, 5, 36 dan 43 (menerapkan Filter Date Jendela Seed); langkah 18 (pemulihan kolom Field dari langkah 14); langkah 30 (pemulihan Setup Column); langkah 35 dan 42 (membersihkan Filter).
- Temuan untuk QA:
  - TC-FA-FAAL-166, 167, 184, dan 189 memberi precondition Filter Date Jendela Seed pada kedua tab agar jumlah baris berkas (11, 15, satu, dan dua baris) tidak bergantung pada baris log lain; spec menerapkannya di langkah 1 dan 5, dan menerapkannya ulang di langkah 36 dan 43 sesudah `[Clear Field]`. TC tidak menyatakan bahwa Filter Date hilang bersama `[Clear Field]`; spec mengasumsikan semua Filter terkosongkan.
  - TC-FA-FAAL-189 tidak menyebut cara memulihkan kolom; langkah 30 ditambahkan sebagai pemulihan (S-09).
