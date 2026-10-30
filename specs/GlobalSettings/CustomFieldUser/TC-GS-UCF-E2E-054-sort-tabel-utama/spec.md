---
id: TC-GS-UCF-E2E-054-sort-tabel-utama
title: "Sort Tabel Utama Custom Field: Siklus Tiga Klik per Kolom, Value Setting Teks Lengkap, Modified By Nama Lengkap, dan Kolom Tanpa Ikon Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-222
  - TC-GS-UCF-223
  - TC-GS-UCF-224
  - TC-GS-UCF-225
  - TC-GS-UCF-501
  - TC-GS-UCF-226
  - TC-GS-UCF-502
  - TC-GS-UCF-227
  - TC-GS-UCF-228
  - TC-GS-UCF-229
coverage:
  web: automated
---

# Sort Tabel Utama Custom Field: Siklus Tiga Klik per Kolom, Value Setting Teks Lengkap, Modified By Nama Lengkap, dan Kolom Tanpa Ikon Sort

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak diubah spec ini, tanpa suffix; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.preset14`):
  - `Cost Center`: Dropdown `Finance`, `Operations`, `Marketing`; Placeholder `Select cost center`; Required Yes; Active; Modified By `Budi S` (Budi Santoso); Last Updated 11 Sep 2026 10:35.
  - `Employee Grade`: Text; Placeholder kosong (efektif `Enter employee grade`); Required No; Active; `Siti R`; 10 Sep 2026 14:15.
  - `Job Description`: Text Area; Placeholder `Describe the job`; Required No; Active; `Siti R`; 10 Sep 2026 11:00.
  - `Bonus`: Numeric Decimal Places 2; Placeholder `Enter bonus`; Required No; Active; `Budi S`; 9 Sep 2026 15:20.
  - `Office Phone`: Phone; Placeholder `Enter phone number`; Required Yes; Active; `Budi S`; 9 Sep 2026 10:10.
  - `Joining Date`: Date; Placeholder `Select date`; Required No; Inactive; `Budi S`; 9 Sep 2026 09:00.
- Data Dinamis Population D-01 (8 field; fixture baru (belum ada; lihat coverage) `Fixture.customFieldUser.population`): `Blood Type` (Dropdown `A`, `B`, `AB`, `O`), `Shirt Size` (Dropdown `S`, `M`, `L`, `XL`; Placeholder `Choose shirt size`), `Emergency Phone` (Phone), `Birth Date` (Date), `Tax ID` (Text; Placeholder `Enter tax ID number`; Required Yes), `Work Notes` (Text Area), `Annual Target` (Numeric Decimal Places 1), `badge number` (Text); Required No kecuali `Tax ID`; Active; Placeholder lain kosong (efektif default); Modified By `Sari D`; Last Updated hari seeding (lebih baru dari seluruh Last Updated Pre-setup, sehingga kolom Last Updated memuat sedikitnya dua nilai distinct). Di-seed lewat API oleh akun Total Control Client A di hook `before` (mekanisme disediakan tim FE/BE, endpoint tidak ditulis di spec). Nama literal tanpa suffix karena asersi urutan A-Z dan jumlah 14 baris bergantung pada nama (pengecualian Population, S-12); seeding idempotent (dilewati bila sudah ada); cleanup hanya menghapus yang dibuat hook spec ini. Total Custom Field Client A tepat 14 saat TC-GS-UCF-222 sampai 229 berjalan.
- Data Dinamis milik spec (di-seed lewat API pada langkah yang menyebutnya, sesudah TC-GS-UCF-229, agar total 14 baris tidak berubah untuk TC sebelumnya; nama bersuffix per run; fixture baru `Fixture.customFieldUser.sortSeed054`): `Sort Key A {runId}-054` (D-229: Dropdown `Pa`, `Pb`, `Zz`; bebas nilai User), `Sort Key B {runId}-054` (D-230: Dropdown `Pa`, `Pb`, `Cc`, `Dd`; bebas nilai User) dibuat oleh akun Total Control Client A, dan `Aaa Setiawan Probe {runId}-054` (D-231: Text) yang dibuat dan satu-satunya diubah oleh Budi Setiawan (akun Total Control Client A, tidak dipakai login; Modified By `Budi S`, nama lengkap Budi Setiawan; pelaku seeding disediakan tim FE/BE).
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`.
- Setup Column tabel utama dalam konfigurasi default (8 kolom terlihat, urutan default, tanpa pin; cache browser dibersihkan atau `[Reset to Default]` dijalankan di hook `before` sebelum spec).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Sort Key A {runId}-054`, `Sort Key B {runId}-054`, `Aaa Setiawan Probe {runId}-054`, dan field Population yang dibuat hook `before`; pulihkan ukuran halaman ke 10 dan sort ke netral.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` halaman Custom Field true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: pembacaan indikator sort pada header (arah dan label seperti `Active First`), urutan baris, isi sel Value Setting (badge dan chip `+N more`), dan tooltip hover sel Modified By.
- State global: ukuran halaman diubah ke 25 (langkah 1) dan dikembalikan ke 10 (langkah 98); sort tiap kolom dikembalikan ke netral dengan siklus tiga klik atau klik tambahan.

## Test Steps

### Persiapan

1. Ubah ukuran halaman tabel ke 25

### TC-GS-UCF-222: Sort 3-state kolom Field Name dan Data Type

2. Klik header Field Name
3. Verifikasi indikator ascending pada header Field Name
4. Verifikasi urutan A-Z tanpa membedakan huruf besar kecil: `Annual Target` berada di atas
5. Klik header Field Name
6. Verifikasi indikator descending pada header Field Name
7. Verifikasi urutan Z-A: `Work Notes` berada di atas
8. Klik header Field Name
9. Verifikasi indikator sort pada header Field Name nonaktif
10. Verifikasi urutan kembali default: `Annual Target` berada di atas
11. Klik header Data Type
12. Verifikasi indikator ascending pada header Data Type
13. Verifikasi dua baris teratas berurutan `Birth Date` lalu `Joining Date` (Data Type `Date` sebelum `Dropdown`; Data Type sama berurut Field Name A-Z)
14. Klik header Data Type
15. Verifikasi indikator descending pada header Data Type
16. Verifikasi dua baris teratas berurutan `Job Description` lalu `Work Notes` (Data Type `Text Area`)
17. Klik header Data Type
18. Verifikasi indikator sort pada header Data Type nonaktif
19. Verifikasi urutan kembali default: `Annual Target` berada di atas

### TC-GS-UCF-223: Sort 3-state kolom Active

20. Klik header Active
21. Verifikasi indikator sort `Active First` pada header Active
22. Verifikasi 13 field Active tampil lebih dahulu dan `Joining Date` berada di baris terakhir
23. Klik header Active
24. Verifikasi indikator sort `Inactive First` pada header Active
25. Verifikasi `Joining Date` berada di baris teratas
26. Klik header Active
27. Verifikasi indikator sort pada header Active nonaktif
28. Verifikasi urutan kembali default: `Annual Target` berada di atas

### TC-GS-UCF-224: Sort 3-state kolom Required

29. Klik header Required
30. Verifikasi indikator sort `Yes First` pada header Required
31. Verifikasi tiga baris teratas berurutan `Cost Center`, `Office Phone`, dan `Tax ID`
32. Klik header Required
33. Verifikasi indikator sort `No First` pada header Required
34. Verifikasi field Required `No` berada di atas dan `Annual Target` berada di baris pertama
35. Klik header Required
36. Verifikasi indikator sort pada header Required nonaktif
37. Verifikasi urutan kembali default: `Annual Target` berada di atas

### TC-GS-UCF-225: Sort Value Setting, baris tanpa Value Setting di akhir saat ascending dan di awal saat descending

38. Klik header Value Setting
39. Verifikasi lima baris teratas berurutan `Annual Target` (`1 Decimal Place`), `Bonus` (`2 Decimal Places`), `Blood Type`, `Cost Center`, lalu `Shirt Size` (urutan teks)
40. Verifikasi sembilan baris terakhir adalah baris tanpa Value Setting (`—`)
41. Klik header Value Setting
42. Verifikasi sembilan baris teratas adalah baris tanpa Value Setting (`—`) berurut Field Name A-Z
43. Verifikasi sesudah sembilan baris itu berurutan `Shirt Size`, `Cost Center`, `Blood Type`, `Bonus`, lalu `Annual Target`
44. Verifikasi sel Value Setting baris `Cost Center` menampilkan badge `Finance`, badge `Operations`, lalu chip `+1 more` (urutan penambahan)
45. Klik header Value Setting
46. Verifikasi indikator sort pada header Value Setting nonaktif
47. Verifikasi urutan kembali default: `Annual Target` berada di atas

### TC-GS-UCF-226: Sort Modified By berdasarkan nama lengkap

48. Klik header Modified By
49. Verifikasi urutan ascending berdasarkan nama lengkap: baris `Budi S` (`Bonus`, `Cost Center`, `Joining Date`, `Office Phone`) lebih dahulu, lalu baris `Sari D`, lalu baris `Siti R`
50. Klik header Modified By
51. Verifikasi urutan descending: baris `Siti R` berada di atas
52. Klik header Modified By
53. Verifikasi indikator sort pada header Modified By nonaktif
54. Verifikasi urutan kembali default: `Annual Target` berada di atas

### TC-GS-UCF-227: Sort Last Updated Oldest First dan Newest First

55. Klik header Last Updated
56. Verifikasi indikator sort `Oldest First` pada header Last Updated
57. Verifikasi enam baris teratas berurutan `Joining Date`, `Office Phone`, `Bonus`, `Job Description`, `Employee Grade`, dan `Cost Center`
58. Klik header Last Updated
59. Verifikasi indikator sort `Newest First` pada header Last Updated
60. Verifikasi field Population (Last Updated hari uji) berada di atas dan `Cost Center` berada di bawah seluruh field Population
61. Klik header Last Updated
62. Verifikasi indikator sort pada header Last Updated nonaktif
63. Verifikasi urutan kembali default: `Annual Target` berada di atas

### TC-GS-UCF-228: Sort Placeholder berdasarkan nilai efektif

64. Klik header Placeholder
65. Verifikasi sepuluh baris teratas ascending berdasarkan nilai efektif berurutan `Shirt Size` (`Choose shirt size`), `Job Description` (`Describe the job`), `Annual Target`, `badge number`, `Bonus`, `Employee Grade`, `Emergency Phone` dan `Office Phone` (nilai sama, urut Field Name A-Z), `Tax ID`, lalu `Work Notes`
66. Klik header Placeholder
67. Verifikasi lima baris teratas descending berurutan `Birth Date` dan `Joining Date` (`Select date`), `Cost Center`, `Blood Type`, lalu `Work Notes`
68. Klik header Placeholder
69. Verifikasi indikator sort pada header Placeholder nonaktif
70. Verifikasi urutan kembali default: `Annual Target` berada di atas

### TC-GS-UCF-229: Kolom Checkbox dan Actions tidak memiliki ikon sort

71. Verifikasi kolom Checkbox tidak memiliki ikon sort
72. Verifikasi header kolom Actions `⋯` tidak memiliki ikon sort

### TC-GS-UCF-501: Sort Value Setting memakai teks Value Setting lengkap

73. Buat lewat API field `Sort Key A {runId}-054` (Dropdown `Pa`, `Pb`, `Zz`) dan `Sort Key B {runId}-054` (Dropdown `Pa`, `Pb`, `Cc`, `Dd`) hingga tersimpan, lalu muat ulang halaman (F5)
74. Ketik Search `Sort Key`, tekan Enter
75. Verifikasi tabel menampilkan tepat dua baris: `Sort Key A {runId}-054` dan `Sort Key B {runId}-054`
76. Verifikasi sel Value Setting `Sort Key A {runId}-054` menampilkan badge `Pa`, badge `Pb`, dan chip `+1 more`
77. Verifikasi sel Value Setting `Sort Key B {runId}-054` menampilkan badge `Pa`, badge `Pb`, dan chip `+2 more`
78. Klik header Value Setting
79. Verifikasi `Sort Key B {runId}-054` berada di atas `Sort Key A {runId}-054` (teks lengkap `Pa, Pb, Cc, Dd` mendahului `Pa, Pb, Zz`)
80. Klik header Value Setting
81. Verifikasi `Sort Key A {runId}-054` berada di atas `Sort Key B {runId}-054`
82. Klik header Value Setting sekali lagi (sort kembali netral)
83. Klik `(←)`

### TC-GS-UCF-502: Sort Modified By memakai nama lengkap untuk dua pelaku berinisial sama

84. Buat lewat API field `Aaa Setiawan Probe {runId}-054` (Text) oleh Budi Setiawan hingga tersimpan, lalu muat ulang halaman (F5)
85. Ketik Search `Budi S`, tekan Enter
86. Verifikasi tabel menampilkan tepat lima baris dengan Modified By `Budi S`: `Aaa Setiawan Probe {runId}-054`, `Bonus`, `Cost Center`, `Joining Date`, dan `Office Phone`
87. Hover `Budi S` pada baris `Aaa Setiawan Probe {runId}-054`
88. Verifikasi tooltip "Budi Setiawan"
89. Hover `Budi S` pada baris `Bonus`
90. Verifikasi tooltip "Budi Santoso"
91. Klik header Modified By
92. Verifikasi `Bonus`, `Cost Center`, `Joining Date`, dan `Office Phone` (Budi Santoso) berada di atas `Aaa Setiawan Probe {runId}-054` (Budi Setiawan)
93. Klik header Modified By
94. Verifikasi `Aaa Setiawan Probe {runId}-054` berada di atas `Bonus`, `Cost Center`, `Joining Date`, dan `Office Phone`
95. Klik header Modified By sekali lagi (sort kembali netral)
96. Klik `(←)`
97. Verifikasi tabel kembali menampilkan seluruh baris (17 baris)
98. Ubah ukuran halaman tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 98 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu topik dan satu dataset (Sort tabel utama), satu akun; tiap blok TC memulai dari sort netral dan tetap bermakna bila blok lain gagal. Siklus tiga klik per kolom menambah langkah `Verifikasi` indikator, arah, dan urutan yang dipecah satu per klausa.
- Urutan TC tidak mengikuti urutan nomor TC sumber: TC-GS-UCF-229 mendahului TC-GS-UCF-501 dan TC-GS-UCF-502, dan TC-GS-UCF-501 dan 502 ditaruh paling akhir karena field `Sort Key A`, `Sort Key B`, dan `Aaa Setiawan Probe` baru dibuat pada langkah 73 dan 84; dengan begitu total tetap 14 baris untuk asersi "13 field Active", "sembilan baris tanpa Value Setting", dan urutan Placeholder pada TC-GS-UCF-223 sampai 228.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 98 (ukuran halaman 25 agar 14 baris tampil pada satu halaman sehingga "di akhir" dan "di awal" dapat diasersi, lalu dikembalikan ke 10); langkah 73 dan 84 (seeding field milik spec lewat API di tengah spec, alasan di butir urutan di atas); langkah 82 dan 95 (klik header ketiga hingga sort kembali netral); langkah 83 dan 96 (`(←)` menutup input Search).
- Verifikasi tambahan di luar Expected TC (S-03): langkah 97 (seluruh baris kembali setelah Search ditutup, 14 baris Client A ditambah tiga field seed) sebagai baseline sebelum ukuran halaman dikembalikan; langkah 3 sampai 10 dan langkah sejenis memecah Expected "klik 1 A-Z" menjadi indikator dan urutan (S-01).
- Asersi sort memakai kolom dengan sedikitnya dua nilai distinct (S-11): Active (13 Active dan 1 Inactive), Required (Yes dan No), Modified By (`Budi S`, `Sari D`, `Siti R`), Last Updated (Pre-setup Sep 2026 dan Population hari uji).
- Pembagian TC lintas spec: Search tabel utama ada di spec 051; Filter Panel di spec 052; kombinasi Search, Filter, Sort, dan Pagination di spec 053; Pagination di spec 055; Setup Column di spec 056.
- Temuan untuk QA:
  - Keputusan NC yang berbeda dari API/LLD: TC-GS-UCF-228 (NC-08, sort Placeholder nilai efektif; LLD `sortBy` tidak memuat `placeholder` sehingga dapat menolak 422), TC-GS-UCF-225 (NC-25 posisi baris tanpa Value Setting di awal saat descending; LLD menaruhnya di akhir pada kedua arah), dan TC-GS-UCF-225 baris `1 Decimal Place` serta `2 Decimal Places` (NC-10 pluralisasi; LLD `<N> decimal place(s)`). Asersi mengikuti TC dan PRD; dapat gagal pada backend nyata sampai API/LLD diselaraskan.
  - TC-GS-UCF-227 Expected b ("field Population terbaru di atas") tidak menyebut urutan antar field Population yang dibuat pada menit yang sama; spec hanya mengasersi bahwa field Population berada di atas `Cost Center`.
  - TC-GS-UCF-228 Expected a menyebut urutan sepuluh baris pertama saja dan Expected b lima baris teratas; empat baris sisanya (`Blood Type`, `Cost Center`, `Birth Date`, `Joining Date` pada ascending) tidak diasersi. Placeholder efektif default `Annual Target`, `badge number`, `Work Notes`, dan `Blood Type` tidak tertulis di TC; spec hanya mengasersi urutan.
  - TC-GS-UCF-222 sampai 228 tidak menyebut ukuran halaman; spec memakai 25 agar seluruh 14 baris terlihat.
  - Akun pelaku seeding Budi Setiawan (D-231) tidak dipakai login dan tidak ada passwordnya; pembuatan field oleh pelaku itu disediakan tim FE/BE tanpa mengarang endpoint.
  - Post Condition TC kosong ("-") pada seluruh TC spec ini; tidak ada yang diasersi.
