---
id: TC-GS-UOM-E2E-050-changelog-sort-pagination-dan-kombinasi
title: "Changelog Measurement: Sort, Nilai Kosong Old/New Value, Pagination, dan Kombinasi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-183
  - TC-GS-UOM-184
  - TC-GS-UOM-185
  - TC-GS-UOM-190
coverage:
  web: automated
---

# Changelog Measurement: Sort, Nilai Kosong Old/New Value, Pagination, dan Kombinasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` suite (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Layar awal Global Settings > Master Reference > Measurement dibuka di hook `beforeEach` suite.
- Akun seeding tambahan (hanya untuk seeding API di hook `before`, bukan login UI): Create+Read, Rina Marlina (`Rina M`), `createOnly_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_CREATE_PASSWORD`.
- Environment variable: `GS_TC_PASSWORD`, `GS_CREATE_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel true oleh hook suite (lihat bagian "Hook suite" di `suite.md`).
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.
- Seeding (lewat API di hook `before`, urutan sebagai berikut):
  - Population D-01 oleh Sari Dewi (setara TC-GS-UOM-36), idempotent (nama yang sudah ada dilewati): `Centimeter`, `Foot`, `Gallon`, `Inch`, `Milliliter`, `Millimeter`, `Ounce`, `Pound`, `Roll`, `Set`, `Sheet`, `Ton`. Menjamin lebih dari 10 entri Changelog (halaman 2 pada TC-GS-UOM-185).
  - `Rina Sort {runId}-050` dibuat oleh Rina Marlina (entri Create oleh `Rina M`; menjamin kolom Modified By punya sedikitnya dua nilai distinct untuk TC-GS-UOM-183).
  - `Gallon {runId}-050` (Symbol `gl`) dibuat oleh Sari Dewi; Symbol diubah menjadi `oz` (Edit pertama); hook menunggu sampai menit berganti (maksimum 60 detik, karena kolom Date berketelitian menit dan asersi sort Date butuh dua nilai Date berbeda); Symbol diubah menjadi `oz.` (Edit kedua). Menghasilkan entri Create dan dua entri Edit (New Value `oz`, lalu `oz.`) dengan Date berbeda.
  - `Hapus {runId}-050` dibuat lalu dihapus oleh Sari Dewi (entri Create dan Delete, setara TC-GS-UOM-96); dilakukan paling akhir sehingga entri Delete menjadi entri terbaru di Changelog (default Date terbaru di atas) dan menyediakan baris New Value `—` untuk TC-GS-UOM-184.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Rina Sort {runId}-050`, `Gallon {runId}-050`, dan unit Population yang dibuat spec ini (yang sudah ada sebelum spec dilewati). Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: pindah ke halaman terakhir lewat Pagination; membaca indikator sort pada header kolom.
- Search `{runId}-050` (langkah 9) membatasi halaman Changelog selama TC-GS-UOM-183 (langkah 9 sampai 23) ke enam entri milik spec: Create `Rina Sort {runId}-050`, Create dan dua Edit `Gallon {runId}-050`, serta Create dan Delete `Hapus {runId}-050`. Halaman yang diamati memuat sedikitnya dua nilai distinct pada Action (`Create`, `Edit`, `Delete`), Field (`Symbol`, `Unit Name`), Modified By (`Rina M`, `Sari D`), dan Unit Name (S-11, S-14). Search dikosongkan di langkah 24. TC-GS-UOM-184 memakai Search yang sama pada kolom Old Value (langkah 25 sampai 29; enam entri milik spec: tiga baris dengan Old Value terisi, yaitu dua Edit dan satu Delete, dan tiga baris Create dengan Old Value `—`, S-14) dan dikosongkan di langkah 29; kolom New Value (langkah 30 sampai 34) memakai Pagination atas seluruh Changelog.
- Tabel "Kolom sort" untuk TC-GS-UOM-183 (klik 1 = ascending, klik 2 = descending, klik 3 = netral):

  | Kolom | Hasil klik 1 | Hasil klik 2 |
  |---|---|---|
  | Action | A-Z, baris pertama Action `Create` | Z-A, baris pertama Action `Edit` |
  | Unit Name | A-Z, baris pertama Unit Name `Gallon {runId}-050` dan baris terakhir `Rina Sort {runId}-050` | Z-A, baris pertama Unit Name `Rina Sort {runId}-050` dan baris terakhir `Gallon {runId}-050` |
  | Field | A-Z, baris pertama Field `Symbol` | Z-A, baris pertama Field `Unit Name` |
  | Modified By | A-Z, baris pertama Modified By `Rina M` dan baris terakhir `Sari D` | Z-A, baris pertama Modified By `Sari D` dan baris terakhir `Rina M` |

- Precondition TC-GS-UOM-183, 184, 185, 190: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement. TC-GS-UOM-184 bergantung pada Delete (TC-GS-UOM-96) dan TC-GS-UOM-190 pada Edit (TC-GS-UOM-70); keduanya dipenuhi seeding di atas. TC-GS-UOM-183 dan 185 bergantung pada Population (TC-GS-UOM-36).

## Test Steps

### TC-GS-UOM-185: Pagination Changelog default 10 dengan pilihan 10/25/50/100

1. Klik icon Changelog di halaman Global Settings > Master Reference > Measurement
2. Verifikasi ukuran halaman default 10
3. Verifikasi halaman 1 menampilkan 10 baris
4. Klik Next pada Pagination Modal Changelog
5. Verifikasi halaman 2 tampil dengan baris data
6. Buka pilihan page size
7. Verifikasi pilihan page size `10`, `25`, `50`, `100`
8. Pilih ukuran halaman `10`, lalu pindah ke halaman 1

### TC-GS-UOM-183: Sort Changelog kolom teks dan Date

9. Ketik Search `{runId}-050`, tekan Enter

Untuk setiap baris tabel "Kolom sort" di Prerequisites (langkah 10 sampai 16):

10. Klik header kolom
11. Verifikasi hasil klik 1 sesuai tabel "Kolom sort"
12. Klik header kolom yang sama
13. Verifikasi hasil klik 2 sesuai tabel "Kolom sort"
14. Klik header kolom yang sama
15. Verifikasi kolom tidak menampilkan panah sort aktif (netral)
16. Verifikasi urutan kembali ke default Date terbaru di atas: baris pertama Action `Delete`, Unit Name `Hapus {runId}-050`

Kolom Date:

17. Klik header Date
18. Verifikasi Oldest First: baris terurut dari tanggal terlama ke terbaru
19. Klik header Date
20. Verifikasi Newest First: baris pertama Action `Delete`, Unit Name `Hapus {runId}-050`
21. Klik header Date
22. Verifikasi kolom Date tidak menampilkan panah sort aktif (netral)
23. Verifikasi urutan kembali ke default Date terbaru di atas: baris pertama Action `Delete`, Unit Name `Hapus {runId}-050`
24. Klik `(←)` pada kotak Search

### TC-GS-UOM-184: Sort Old Value dan New Value menempatkan nilai kosong di akhir saat ascending

25. Ketik Search `{runId}-050`, tekan Enter
26. Klik header Old Value (ascending)
27. Verifikasi tiga baris pertama bernilai (Old Value bukan `—`)
28. Verifikasi tiga baris terakhir adalah baris Create (Old Value `—`)
29. Klik `(←)` pada kotak Search
30. Klik header New Value (ascending)
31. Verifikasi baris pertama pada halaman 1 bernilai (New Value bukan `—`)
32. Pindah ke halaman terakhir pada Pagination
33. Verifikasi baris Delete (New Value `—`) berada di akhir pada halaman terakhir
34. Pindah ke halaman 1 pada Pagination, lalu klik header New Value dua kali hingga netral

### TC-GS-UOM-190: Kombinasi Search, Filter, Sort, Pagination Changelog lalu dipulihkan

35. Ketik Search `gallon {runId}-050`, tekan Enter
36. Verifikasi hasil memuat baris Action `Create`, Unit Name `Gallon {runId}-050`
37. Klik Filter
38. Pilih Action `Edit`
39. Klik [Apply]
40. Verifikasi hasil memuat baris Action `Edit`, Unit Name `Gallon {runId}-050`
41. Verifikasi setiap baris yang tampil memiliki Action `Edit` dan Unit Name `Gallon {runId}-050` (irisan Search dan Filter)
42. Klik header Date (Oldest First)
43. Verifikasi baris pertama New Value `oz` dan baris kedua New Value `oz.` (irisan Search, Filter, dan Sort Date oldest)
44. Kosongkan field Action
45. Klik [Apply]
46. Verifikasi kotak Search tetap berisi `gallon {runId}-050`
47. Verifikasi header Date tetap menampilkan sort Oldest First
48. Verifikasi hasil memuat baris Action `Create`, Unit Name `Gallon {runId}-050` (filter Action `Edit` tidak lagi aktif)
49. Klik `(←)` pada kotak Search
50. Verifikasi header Date tetap menampilkan sort Oldest First

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-UOM-185, 183, 184, 190. Alasan: TC-GS-UOM-185 mengamati state awal Pagination sebelum sort mengubah tabel (screening dahulu, S-14); TC-GS-UOM-190 terakhir karena memakai Search dan Filter.
- Langkah 10 sampai 16 diulang untuk setiap baris tabel "Kolom sort" (4 kolom); parameter tiap iterasi ada di Prerequisites. Ekspansi: 4 x 7 = 28 langkah, ditambah kolom Date (langkah 17 sampai 23).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 (mengembalikan ukuran halaman 10 dan halaman 1), 9 (Search `{runId}-050` membatasi halaman Changelog ke baris milik spec), 24 dan 29 (mengosongkan Search lewat `(←)`; S-09), 25 (Search `{runId}-050` membatasi halaman ke enam entri milik spec untuk kolom Old Value; TC-GS-UOM-184 memakai Pagination atas seluruh Changelog pada kolom New Value), 34 (kembali ke halaman 1 karena halaman terakhir tidak punya Next dan membuat state netral untuk TC berikutnya), dan 44 (mengosongkan filter Action).
- Langkah 36 adalah pembanding positif bagi langkah 41 (asersi universal). Keyword Search TC-GS-UOM-190 `gallon` diperluas menjadi `gallon {runId}-050` supaya irisan tidak memuat baris dari unit `Gallon` Population dan unit Gallon spec lain; Expected TC tidak menghitung baris.
- Langkah 27 dan 31 mewujudkan "baris bernilai lebih dulu" (pada Old Value: tiga baris pertama dari enam entri milik spec; pada New Value: halaman 1) dan langkah 28 dan 33 mewujudkan "`—` di akhir" (pada Old Value: tiga baris terakhir; pada New Value: halaman terakhir, nilai kosong di akhir seluruh urutan ascending).
- Spec ini melewati sekitar 35 langkah (50 langkah nominal, sekitar 71 dengan ekspansi). Alasan: keempat TC adalah perilaku tabel pada satu Modal Changelog dengan satu dataset seeding dan satu kelas harness (fungsional); pemisahan hanya menambah seeding (termasuk tunggu pergantian menit) dan pembukaan modal berulang. Kegagalan keras membuka modal (langkah 1) membuat seluruh blok kehilangan makna.
- Temuan untuk QA:
  - TC-GS-UOM-183 tidak menyebut nilai yang diharapkan untuk Unit Name dan Modified By; spec mengasersi urutan A-Z dan Z-A atas enam entri milik spec yang dibatasi Search `{runId}-050` (nilai konkret ada di tabel "Kolom sort").
  - TC-GS-UOM-184 tidak menyebut apakah mengklik header lain mereset sort kolom sebelumnya; spec membuat kolom netral eksplisit di langkah 34.
  - TC-GS-UOM-190 menulis "Clear Filter" dan "Clear Search" tanpa kontrol yang disebut; spec mengosongkan field Action lalu [Apply] dan memakai `(←)` pada kotak Search.
  - Panel Filter sesudah `[Apply]`: langkah 44 tidak membuka ulang panel karena spec mengasumsikan panel tetap terbuka sesudah `[Apply]` pada langkah 39, juga sesudah klik header Date pada langkah 42. Asumsi kerja ini belum diamati di aplikasi: prd-conventions §9.8 hanya menyebut penutupan panel lewat klik luar panel atau klik ulang icon Filter dan tidak menyatakan keadaan panel sesudah `[Apply]`. Spec 037, 038, 039, dan 045 memakai asumsi yang sama. Selain itu §9.8 menyebut klik luar panel menutup panel tanpa Apply, sehingga klik header Date dapat menutupnya. Bila aplikasi menutup panel (sesudah `[Apply]` atau sesudah klik header Date), langkah 44 perlu diawali `Klik Filter`.
  - TC-GS-UOM-184 Expected a ("Create (Old `—`) di akhir") juga benar pada urutan default (Date terbaru di atas), sehingga tidak membedakan sort Old Value dari tanpa sort. Spec membatasi halaman dengan Search `{runId}-050` dan mengasersi tiga baris pertama terisi dan tiga baris terakhir Create (langkah 25 sampai 29); Expected TC perlu syarat yang tidak benar pada urutan default.
