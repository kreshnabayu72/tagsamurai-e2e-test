---
id: TC-GS-UCF-E2E-064-changelog-sort-dan-pagination
title: "Modal Changelog Custom Field: Pagination, Sort Semua Kolom, dan Entri Hasil Bulk Tanpa Duplikat Antar Halaman"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-267
  - TC-GS-UCF-523
  - TC-GS-UCF-524
  - TC-GS-UCF-268
  - TC-GS-UCF-525
coverage:
  web: automated
---

# Modal Changelog Custom Field: Pagination, Sort Semua Kolom, dan Entri Hasil Bulk Tanpa Duplikat Antar Halaman

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; `## Test Steps` tidak mengulang langkah buka kecuali sesudah aksi yang menutup modal.
- Data Pre-setup (baca-saja, tidak diubah spec ini): 6 Custom Field Pre-setup Client A dan Changelog Pre-setup 8 entri bertanggal 8 sampai 11 Sep 2026 (fixture backend): Edit `Cost Center — Value Setting` (Budi S, 11 Sep), Create `Cost Center` (Budi S, 11 Sep), Activate `Employee Grade — Status` (Siti R, 10 Sep), Deactivate `Joining Date — Status` (Budi S, 9 Sep), Delete `Legacy Field` (Siti R, 8 Sep), Create `Job Description` (Siti R, 10 Sep), Create `Bonus` (Budi S, 9 Sep), Create `Office Phone` (Budi S, 9 Sep).
- Data Population (precondition TC): 8 Custom Field Population dibuat lewat API oleh Sari Dewi di hook `before` bila belum ada (seeding idempotent; 8 entri Create, Modified By `Sari D`). Total entri Changelog Client A untuk TC-GS-UCF-268 tidak dipatok mutlak (Changelog kumulatif): jumlah N dicatat dari Pagination pada langkah 2.
- Data Dinamis TC-GS-UCF-525 (di-seed lewat API oleh Sari Dewi pada langkah 55, bukan di hook `before`, agar entri Create seeding tidak menambah total Changelog sebelum TC-GS-UCF-268; fixture baru `Fixture.customFieldUser.tieLog064`): 12 Custom Field Text Active bebas nilai User `Tie Log 01 {runId}-064` sampai `Tie Log 12 {runId}-064`. Search memakai `{runId}-064` sebagai pengganti `Tie Log` supaya entri run sebelumnya (audit trail permanen) tidak ikut terhitung. Hook `after` menghapus lewat API ke-12 field bila masih ada. Entri Changelog tidak dihapus.
- Setup Column Modal Changelog: konfigurasi default; hook `beforeEach` membersihkan cache browser.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan jumlah total entri dari label Pagination (belum terbukti label menampilkan total; lihat Temuan untuk QA; langkah 2, 4, 6); Select All lintas hasil Search pada tabel utama; Bulk Action Deactivate; pencatatan urutan baris untuk perbandingan.
- State global: tidak ada yang diubah selain flag Guided Tooltip. Spec ini tidak mengubah 14 Custom Field Pre-setup dan Population; TC-GS-UCF-525 menambah 12 entri Deactivate permanen di Changelog Client A, sehingga dijalankan paling akhir; 12 entri Create seeding langkah 55 juga ditambahkan sesudah TC-GS-UCF-268.

## Test Steps

### TC-GS-UCF-268: Pagination Modal Changelog

1. Klik icon Changelog
2. Catat jumlah total entri N dari Pagination (10 < N ≤ 20)
3. Klik Next
4. Verifikasi halaman 2 memuat N − 10 entri sisa
5. Ubah page size ke 25
6. Verifikasi seluruh N entri dalam satu halaman

### TC-GS-UCF-267: Sort Changelog: Date, Action, dan kolom Old Value dan New Value campuran

7. Ubah page size kembali ke 10 (default), klik Filter, pilih Date 8 Sep 2026 sampai 11 Sep 2026, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
8. Verifikasi urutan default Date terbaru di atas
9. Klik header Date
10. Verifikasi Oldest First: entri Delete `Legacy Field` (8 Sep) di atas
11. Klik header Action
12. Verifikasi Action ascending A-Z: `Activate`, `Create`, `Deactivate`, `Delete`, `Edit`
13. Klik header Old Value
14. Verifikasi Old Value ascending: nilai dahulu, `-` (Create) di akhir
15. Klik header New Value
16. Verifikasi New Value ascending: nilai dahulu, `-` (Delete) di akhir

### TC-GS-UCF-523: Sort kolom Field dan Modified By: A-Z, Z-A, lalu default pada klik ketiga

17. Klik Filter, klik `[Clear Field]`, pilih Date 8 Sep 2026 sampai 11 Sep 2026, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
18. Klik header Field sekali
19. Verifikasi Field ascending: `Bonus`, `Cost Center`, `Cost Center — Value Setting`, `Employee Grade — Status`, `Job Description`, `Joining Date — Status`, `Legacy Field`, `Office Phone`
20. Klik header Field lagi
21. Verifikasi Field descending: `Office Phone`, `Legacy Field`, `Joining Date — Status`, `Job Description`, `Employee Grade — Status`, `Cost Center — Value Setting`, `Cost Center`, `Bonus`
22. Klik header Field lagi
23. Verifikasi indikator sort Field nonaktif
24. Verifikasi urutan kembali default Date terbaru di atas (Edit `Cost Center — Value Setting` pertama)
25. Klik header Modified By sekali
26. Verifikasi Modified By ascending berdasarkan nama lengkap: lima entri `Budi S` (Budi Santoso) di atas, lalu tiga entri `Siti R` (Siti Rahmawati)
27. Klik header Modified By lagi
28. Verifikasi Modified By descending: tiga entri `Siti R` di atas, lalu lima entri `Budi S`
29. Klik header Modified By lagi
30. Verifikasi indikator sort Modified By nonaktif
31. Verifikasi urutan kembali default Date terbaru di atas

### TC-GS-UCF-524: Sort kolom Date, Old Value, dan New Value: siklus tiga klik

32. Klik header Date sekali
33. Verifikasi Date Oldest First: Delete `Legacy Field` (8 Sep 2026) di atas
34. Verifikasi Date Oldest First: Edit `Cost Center — Value Setting` (11 Sep 2026) di bawah
35. Klik header Date lagi
36. Verifikasi Date Newest First: Edit `Cost Center — Value Setting` di atas
37. Klik header Date lagi
38. Verifikasi indikator sort Date nonaktif
39. Verifikasi urutan default Date terbaru di atas
40. Klik header Old Value sekali
41. Verifikasi Old Value ascending: `Active`, `Finance, Operations`, `Inactive`, `Legacy Field`, lalu empat entri `-` (Create) di akhir
42. Klik header Old Value lagi
43. Verifikasi Old Value descending: empat entri `-` (Create) di atas, lalu `Legacy Field`, `Inactive`, `Finance, Operations`, `Active`
44. Klik header Old Value lagi
45. Verifikasi indikator sort Old Value nonaktif
46. Verifikasi urutan default Date terbaru di atas
47. Klik header New Value sekali
48. Verifikasi New Value ascending: `Active`, `Bonus`, `Cost Center`, `Finance, Operations, Marketing`, `Inactive`, `Job Description`, `Office Phone`, lalu `-` (Delete) di akhir
49. Klik header New Value lagi
50. Verifikasi New Value descending: `-` (Delete) di atas, lalu `Office Phone`, `Job Description`, `Inactive`, `Finance, Operations, Marketing`, `Cost Center`, `Bonus`, `Active`
51. Klik header New Value lagi
52. Verifikasi indikator sort New Value nonaktif
53. Verifikasi urutan default Date terbaru di atas
54. Klik `[✕]`

### TC-GS-UCF-525: Entri hasil bulk tanpa duplikat dan tanpa terlewat antar halaman

55. Buat lewat API 12 field Text Active bebas nilai User `Tie Log 01 {runId}-064` sampai `Tie Log 12 {runId}-064` (fixture baru `Fixture.customFieldUser.tieLog064`) hingga tersimpan, lalu muat ulang halaman (F5)
56. Ketik Search `{runId}-064` di tab Custom Field, tekan Enter
57. Klik `Select All (12 records)`
58. Klik `Bulk Action` > `Deactivate`, klik `[Deactivate]`
59. Verifikasi toast sukses: "Success, custom field has been deactivated."
60. Klik icon Changelog
61. Klik Filter, pilih Action `Deactivate`, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
62. Ketik Search `{runId}-064`, tekan Enter
63. Verifikasi Changelog memuat 12 entri Deactivate
64. Verifikasi halaman 1 memuat 10 entri
65. Catat entri halaman 1 (P1)
66. Klik Next
67. Verifikasi halaman 2 memuat 2 entri
68. Catat entri halaman 2 (P2)
69. Verifikasi `Tie Log 01 {runId}-064` sampai `Tie Log 12 {runId}-064` masing-masing tampil tepat satu kali pada gabungan P1 dan P2
70. Klik `[✕]`
71. Klik icon Changelog
72. Klik Filter, pilih Action `Deactivate`, klik `[Apply]`, lalu klik icon Filter untuk menutup panel
73. Ketik Search `{runId}-064`, tekan Enter
74. Catat entri halaman 1 (P1')
75. Klik Next
76. Catat entri halaman 2 (P2')
77. Verifikasi susunan baris halaman 1 sama dengan P1
78. Verifikasi susunan baris halaman 2 sama dengan P2
79. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 268, 267, 523, 524, 525. Urutan menyimpang dari urutan TC sumber: Pagination (268) dikerjakan sebelum TC-GS-UCF-525 yang menambah 12 entri Create (seeding langkah 55) dan 12 entri Deactivate permanen, agar N yang dicatat pada langkah 2 tidak ikut bertambah; TC-GS-UCF-525 menjalankan aksi Bulk yang mengubah data sehingga ditaruh paling akhir (bagian 3 prinsip 5). Modal dibuka tiga kali (langkah 1, 60, 71; kasus 267, 523, dan 524 memakai pembukaan langkah 1) dan ditutup tiga kali (langkah 54, 70, 79).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 60, dan 71 (membuka modal), langkah 2 (mencatat N dari Pagination sebagai pembanding asersi langkah 4 dan 6), langkah 7, 17, 61, dan 72 (memasang atau memulihkan filter Date atau Action; langkah 7 sekaligus memulihkan page size 10 yang dibutuhkan precondition d TC-GS-UCF-525), langkah 54, 70, dan 79 (menutup modal lewat `[✕]`; tanpa dialog), langkah 55 (seeding 12 field `Tie Log` lewat API), langkah 56 (Search pada tabel utama untuk mempersempit ke 12 field milik spec), langkah 62 dan 73 (Search Changelog), langkah 65, 68, 74, dan 76 (pencatatan urutan untuk perbandingan). Langkah 7, 17, 61, dan 72 juga menutup Filter Panel (lihat butir Model Filter Panel).
- Model Filter Panel (keputusan K-10 A, 2026-10-29): panel tetap terbuka sesudah `[Apply]` (konsisten dengan TC-GS-UCF-211 dan 213). Karena itu `[Apply]` yang diikuti aksi di luar panel (klik header, Search) ditutup lewat klik icon Filter (langkah 7, 17, 61, 72), dan langkah 17 membuka panel lagi dengan Klik Filter. Pola ini sama dengan spec 052, 053, dan 063.
- TC-GS-UCF-525 menyalin Search `Tie Log` dari TC menjadi `{runId}-064` karena nama Data Dinamis bersuffix per run (S-12); entri Changelog run sebelumnya tidak dihapus sehingga Search `Tie Log` akan memuat entri run lama dan membuat hitungan 12 tidak berlaku.
- Pada TC-GS-UCF-267, 523, dan 524 Filter Date 8 sampai 11 Sep 2026 membatasi entri pada Pre-setup sehingga urutan tidak dipengaruhi entri Population dan entri spec lain.
- Spec melewati sekitar 35 langkah (79 langkah). Seluruhnya satu kelas (Sort dan Pagination Modal Changelog, satu dataset Pre-setup; TC-GS-UCF-525 memakai data milik spec sendiri). Blok sort 267, 523, dan 524 berdiri sendiri di dataset Pre-setup baca-saja; TC-GS-UCF-525 berdiri sendiri dengan 12 field bersuffix dan di akhir, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Topik satu dataset Changelog dipertahankan sebagai spec terpisah (lihat Notes spec 061).
- Temuan untuk QA:
  - TC-GS-UCF-523 dan 525 menulis "Klik Filter" sesudah Filter sebelumnya diterapkan, yang dapat berarti membuka ulang panel; spec mengikuti K-10 A dengan menutup panel sesudah `[Apply]` lebih dulu: perlu konfirmasi QA/PRD.
  - TC-GS-UCF-268 (setelah perbaikan 2026-10-29, K-11 A) mencatat N dari Pagination dan mengasersi N − 10 serta N; bound 10 < N ≤ 20 tidak dapat dijamin pada Changelog kumulatif, dan label Pagination yang menampilkan total belum terbukti: perlu konfirmasi QA. Seeding 12 field `Tie Log` dipindah dari hook `before` ke langkah 55 supaya tidak menambah entri sebelum langkah 2.
  - TC-GS-UCF-523 Expected d dan e mengurutkan Modified By "berdasarkan nama lengkap" (`Budi Santoso` sebelum `Siti Rahmawati`); data Pre-setup tambahan `Budi Setiawan` (inisial tampil `Budi S`, D-231) tidak dikecualikan secara eksplisit dan dapat mengubah hitungan lima entri `Budi S` bila ikut dalam rentang Date (8 sampai 11 Sep 2026).
  - TC-GS-UCF-524 Expected d dan g membandingkan nilai `-` dan teks; urutan `-` di akhir saat ascending dan di awal saat descending mengikuti NC-25 (nilai kosong), diasersi sesuai TC.
  - TC-GS-UCF-525 langkah 8 ("ulangi langkah 5 sampai 7") ditulis ulang sebagai langkah eksplisit 72 sampai 78.
  - Nilai Old Value pada TC-GS-UCF-267 memakai `-`, sedangkan Changelog di TC lain memakai `—` (lihat Temuan spec 061).
