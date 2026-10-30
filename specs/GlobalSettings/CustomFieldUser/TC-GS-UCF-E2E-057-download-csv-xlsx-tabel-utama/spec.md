---
id: TC-GS-UCF-E2E-057-download-csv-xlsx-tabel-utama
title: "Download CSV dan XLSX Tabel Custom Field: Overlay, Isi Berkas, Mengikuti Search dan Filter, Kolom Tersembunyi, Urutan Sort, Hasil Kosong, dan Encoding BOM"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-244
  - TC-GS-UCF-245
  - TC-GS-UCF-246
  - TC-GS-UCF-247
  - TC-GS-UCF-248
  - TC-GS-UCF-249
  - TC-GS-UCF-250
  - TC-GS-UCF-252
coverage:
  web: automated
---

# Download CSV dan XLSX Tabel Custom Field: Overlay, Isi Berkas, Mengikuti Search dan Filter, Kolom Tersembunyi, Urutan Sort, Hasil Kosong, dan Encoding BOM

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak diubah spec ini, tanpa suffix; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.preset14`):
  - `Cost Center`: Dropdown `Finance`, `Operations`, `Marketing`; Placeholder `Select cost center`; Required Yes; Active; Modified By `Budi S` (nama lengkap Budi Santoso).
  - `Employee Grade`: Text; Placeholder kosong (efektif `Enter employee grade`); Required No; Active; `Siti R` (Siti Rahmawati).
  - `Job Description`: Text Area; Placeholder `Describe the job`; Required No; Active; `Siti R`.
  - `Bonus`: Numeric Decimal Places 2; Placeholder `Enter bonus`; Required No; Active; `Budi S`.
  - `Office Phone`: Phone; Placeholder `Enter phone number`; Required Yes; Active; `Budi S`.
  - `Joining Date`: Date; Placeholder `Select date`; Required No; Inactive; `Budi S`.
- Data Dinamis Population D-01 (8 field; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.population`): `Blood Type` (Dropdown), `Shirt Size` (Dropdown; Placeholder `Choose shirt size`), `Emergency Phone` (Phone), `Birth Date` (Date), `Tax ID` (Text; Placeholder `Enter tax ID number`; Required Yes), `Work Notes` (Text Area), `Annual Target` (Numeric Decimal Places 1), `badge number` (Text); Required No kecuali `Tax ID`; Active; Modified By `Sari D` (Sari Dewi). Di-seed lewat API oleh akun Total Control Client A di hook `before` (mekanisme disediakan tim FE/BE, endpoint tidak ditulis di spec). Nama literal tanpa suffix karena asersi jumlah 14 baris, nama baris pertama dan terakhir berkas, dan kata kunci Search `phone` bergantung pada nama (pengecualian Population, S-12); seeding idempotent (dilewati bila sudah ada); cleanup hanya menghapus yang dibuat hook spec ini. Total Custom Field Client A tepat 14 saat spec berjalan (lebih dari satu halaman pada ukuran halaman 10).
- General Settings Client A: Date Format `DDD, MMM dd, yyyy` dan Time Format `hh:mm a` (precondition TC-GS-UCF-248). Hook `before` memastikan format itu berlaku dan hook `after` memulihkan nilai awal; pengubah General Settings disediakan tim FE/BE. Time Zone tidak diubah.
- Setup Column tabel utama dalam konfigurasi default (8 kolom terlihat, urutan default, tanpa pin; cache browser dibersihkan atau `[Reset to Default]` dijalankan di hook `before` sebelum spec).
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API field Population yang dibuat hook `before`; hapus berkas hasil unduhan (`Custom-Field-User-List.csv`, `Custom-Field-User-List.xlsx`) dari direktori unduhan uji; pulihkan preferensi kolom tabel utama ke default, Search, Filter, dan Sort ke netral, serta format General Settings ke nilai awal.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` halaman Custom Field true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: menangkap berkas hasil unduhan browser (nama berkas) dan membaca isinya (CSV sebagai teks mentah termasuk tanda kutip dan tiga byte pertama; XLSX: sheet, baris, header, nilai sel); pembacaan keberadaan toast; pembacaan indikator sort dan urutan baris.
- State global: preferensi kolom tersimpan di browser per pengguna; spec memulihkannya di langkah 31 (TC-GS-UCF-247) dan hook `after` sebagai cadangan. Sort Field Name descending diatur pada langkah 53 dan dikembalikan netral pada langkah 58. Format General Settings: lihat butir General Settings di atas.

## Test Steps

### TC-GS-UCF-244: Menu Download menampilkan dua pilihan format

1. Klik icon Download
2. Verifikasi Overlay memuat `Download as CSV`
3. Verifikasi Overlay memuat `Download as XLSX`
4. Tutup Overlay Download

### TC-GS-UCF-245: Download as CSV tanpa filter mengunduh seluruh baris

5. Klik Download > `Download as CSV`
6. Verifikasi tidak ada toast sukses
7. Verifikasi berkas `Custom-Field-User-List.csv` terunduh
8. Buka berkas `Custom-Field-User-List.csv` hasil unduhan
9. Verifikasi berkas memuat 14 baris data (seluruh field, bukan hanya 10 baris halaman 1)
10. Verifikasi urutan baris berkas mengikuti sort aktif (default Field Name A-Z: baris pertama `Annual Target`)

### TC-GS-UCF-246: Download as XLSX dengan Search dan Filter aktif hanya memuat baris tersaring

11. Ketik Search `phone`, tekan Enter
12. Klik Filter, pilih Required `Yes`, klik [Apply], lalu klik icon Filter untuk menutup panel
13. Klik Download > `Download as XLSX`
14. Verifikasi berkas `Custom-Field-User-List.xlsx` terunduh
15. Buka berkas `Custom-Field-User-List.xlsx` hasil unduhan
16. Verifikasi berkas berisi baris `Office Phone`
17. Verifikasi baris `Emergency Phone` tidak ada di berkas (Required No)
18. Verifikasi berkas memuat satu sheet bernama `Sheet1`
19. Verifikasi header kolom di sheet sama dengan kolom yang tampil di tabel
20. Klik `(←)`
21. Klik Filter, klik [Clear Field], klik [Apply], lalu klik icon Filter untuk menutup panel

### TC-GS-UCF-247: Kolom tersembunyi tidak ikut terunduh dan kembali setelah di-unhide

22. Klik header Column Visibility (`⋯`), uncheck `Placeholder`, tutup Overlay Column Visibility
23. Klik Download > `Download as CSV`
24. Buka berkas `Custom-Field-User-List.csv` hasil unduhan
25. Verifikasi berkas memuat kolom `Field Name`
26. Verifikasi berkas tidak memuat kolom `Placeholder`
27. Klik header Column Visibility (`⋯`), centang `Placeholder`, tutup Overlay Column Visibility
28. Klik Download > `Download as CSV`
29. Buka berkas `Custom-Field-User-List.csv` hasil unduhan
30. Verifikasi berkas memuat kolom `Placeholder`
31. Pulihkan konfigurasi: buka Modal Setup Column lewat `⋯` > `Setup Column...`, klik [Reset to Default], klik [Save]

### TC-GS-UCF-248: Isi sel berkas export mengikuti aturan per kolom

32. Klik Download > `Download as CSV`
33. Buka berkas `Custom-Field-User-List.csv` hasil unduhan sebagai teks mentah dan perhatikan baris `Cost Center`, `Joining Date`, `Bonus`, `Annual Target`, dan `Employee Grade`
34. Verifikasi kolom Active baris `Cost Center` bernilai `Active`
35. Verifikasi kolom Active baris `Joining Date` bernilai `Inactive`
36. Verifikasi kolom Data Type baris `Cost Center` bernilai `Dropdown`
37. Verifikasi kolom Data Type baris `Joining Date` bernilai `Date`
38. Verifikasi kolom Data Type baris `Bonus` bernilai `Numeric`
39. Verifikasi kolom Data Type baris `Employee Grade` bernilai `Text`
40. Verifikasi kolom Value Setting baris `Cost Center` bernilai `Finance, Operations, Marketing` (seluruh value dipisah koma, tidak diringkas `+N more`)
41. Verifikasi kolom Value Setting baris `Bonus` bernilai `2 Decimal Places`
42. Verifikasi kolom Value Setting baris `Annual Target` bernilai `1 Decimal Place`
43. Verifikasi kolom Value Setting baris `Employee Grade` bernilai `-`
44. Verifikasi kolom Placeholder baris `Cost Center` bernilai `Select cost center`
45. Verifikasi kolom Placeholder baris `Employee Grade` bernilai `Enter employee grade` (nilai efektif seperti List)
46. Verifikasi kolom Required baris `Cost Center` bernilai `Yes`
47. Verifikasi kolom Required baris `Employee Grade` bernilai `No`
48. Verifikasi kolom Modified By baris `Cost Center` bernilai `Budi Santoso` (nama lengkap)
49. Verifikasi kolom Modified By baris `Employee Grade` bernilai `Siti Rahmawati` (nama lengkap)
50. Verifikasi kolom Modified By baris `Annual Target` bernilai `Sari Dewi` (nama lengkap)
51. Verifikasi kolom Last Updated berpola `DDD, MMM dd, yyyy hh:mm a` (sama dengan List)
52. Verifikasi nilai Value Setting `Cost Center` pada berkas CSV dibungkus tanda kutip ganda (`"Finance, Operations, Marketing"`) sehingga tidak terpecah ke kolom lain

### TC-GS-UCF-249: Urutan baris berkas export mengikuti sort aktif

53. Klik header Field Name dua kali (descending)
54. Klik Download > `Download as CSV`
55. Buka berkas `Custom-Field-User-List.csv` hasil unduhan
56. Verifikasi baris pertama berkas adalah `Work Notes`
57. Verifikasi baris terakhir berkas adalah `Annual Target`
58. Klik header Field Name sekali lagi (sort kembali netral)

### TC-GS-UCF-250: Download saat hasil kosong tetap menghasilkan berkas berisi header

59. Ketik Search `zzqx`, tekan Enter
60. Verifikasi empty state "No results found" tampil
61. Verifikasi tombol Download tetap aktif
62. Klik Download > `Download as CSV`
63. Verifikasi tidak ada toast
64. Buka berkas `Custom-Field-User-List.csv` hasil unduhan
65. Verifikasi berkas memuat baris header kolom yang tampil
66. Verifikasi berkas tidak memuat baris data
67. Klik `(←)`

### TC-GS-UCF-252: Encoding berkas CSV memakai UTF-8 BOM

68. Klik Download > `Download as CSV`
69. Periksa tiga byte pertama berkas `Custom-Field-User-List.csv` hasil unduhan
70. Verifikasi berkas diawali byte `EF BB BF` (UTF-8 BOM)

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 70 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu kelas (binary buffer: isi berkas unduhan tabel utama), satu akun, tanpa mengubah data Custom Field; langkah membuka berkas unduhan dan `Verifikasi` per sel berkas (TC-GS-UCF-248) mendominasi jumlah langkah. Tiap blok TC dimulai dari tabel tanpa Search, Filter, dan Sort sehingga tetap bermakna bila blok lain gagal.
- Urutan TC mengikuti urutan TC sumber (TC-GS-UCF-244 screening Overlay paling awal).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah menutup Overlay Download dan Overlay Column Visibility, langkah membuka berkas hasil unduhan agar isinya dapat diasersi, langkah `(←)` yang mengosongkan Search, langkah menutup Filter Panel dan mengosongkan Filter dengan `[Clear Field]` lalu `[Apply]`, langkah 31 (pemulihan konfigurasi Setup Column yang dituliskan TC-GS-UCF-247 langkah 5; `[Save]` Setup Column aksi sisi klien tanpa langkah "Tunggu aksi selesai"), dan langkah 58 (sort kembali netral).
- Asersi tidak adanya toast ditaruh tepat sesudah pemicu download dan sebelum asersi berkas (langkah 6 pada TC-GS-UCF-245 dan langkah 63 pada TC-GS-UCF-250) supaya toast yang bersifat sementara tidak terlewat; urutan ini berbeda dari urutan Expected TC (berkas lalu toast) dan mengikuti bagian 8b butir 5 dan 11 konvensi.
- Langkah Verifikasi "baris `Office Phone` ada" mendahului "baris `Emergency Phone` tidak ada" pada TC-GS-UCF-246, dan "berkas memuat baris header" mendahului "tidak memuat baris data" pada TC-GS-UCF-250 (anchor positif, bagian 8b butir 2); "berkas memuat kolom `Field Name`" mendahului "tidak memuat kolom `Placeholder`" pada TC-GS-UCF-247. Ketiganya anchor tambahan di luar Expected TC (S-03).
- Pembagian TC lintas spec: Search tabel utama ada di spec 051; Filter Panel di spec 052; Sort di spec 054; Setup Column di spec 056; kegagalan Download (TC-GS-UCF-251 dan 552) dan Download Changelog yang gagal (TC-GS-UCF-273 dan 553) di spec 060; Download di atas 5.000 baris (TC-GS-UCF-365) di spec 058; Download Modal Changelog (TC-GS-UCF-272, 530 sampai 532) di spec 066.
- Temuan untuk QA:
  - Keputusan NC yang berbeda dari API/LLD: TC-GS-UCF-248 mengikuti NC-09 (kolom Placeholder ada di berkas; LLD `/export` tujuh kolom tanpa Placeholder), NC-10 (`1 Decimal Place`, `2 Decimal Places`; LLD `<N> decimal place(s)`), dan NC-11 (sel kosong `-` dan Modified By nama lengkap; LLD dan PRD memakai `—` pada sel kosong), serta TC-GS-UCF-252 mengikuti NC-12 (CSV dengan UTF-8 BOM; LLD tanpa BOM). Asersi ditulis sesuai TC dan dapat gagal pada backend nyata sampai API/LLD diselaraskan.
  - TC-GS-UCF-245 Expected b ("dengan urutan sort aktif") tidak menyebut sort aktif; spec mengasersi urutan default Field Name A-Z.
  - TC-GS-UCF-246 dan TC-GS-UCF-247 tidak menyebut cara membuka berkas XLSX dan header yang diharapkan; spec mengasersi header sama dengan kolom yang tampil (TC-GS-UCF-246) dan keberadaan kolom `Placeholder` (TC-GS-UCF-247).
  - TC-GS-UCF-248 tidak menyebut nilai Last Updated persis dan mengasersi pola saja; pola mengikuti Date Format dan Time Format General Settings yang diatur precondition.
  - TC-GS-UCF-248 mengasumsikan General Settings Client A `DDD, MMM dd, yyyy` dan `hh:mm a`; mekanisme pengubah General Settings disediakan tim FE/BE.
  - TC-GS-UCF-250 Expected a ("Tombol Download tetap aktif") dan b ("tidak ada toast") dituliskan sesuai TC; TC tidak menyebut nama berkas, spec memakai `Custom-Field-User-List.csv` seperti TC-GS-UCF-245.
  - TC-GS-UCF-245 dan TC-GS-UCF-250 Post Condition kosong; tidak ada yang diasersi.
