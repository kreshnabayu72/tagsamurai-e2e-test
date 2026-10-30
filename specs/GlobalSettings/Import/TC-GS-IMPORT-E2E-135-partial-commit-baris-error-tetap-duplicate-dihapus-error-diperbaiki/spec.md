---
id: TC-GS-IMPORT-E2E-135-partial-commit-baris-error-tetap-duplicate-dihapus-error-diperbaiki
title: "Partial Commit: baris error tetap, duplicate dihapus, error diperbaiki lalu commit ulang, dan penomoran ulang padat Row #"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-358
  - TC-GS-IMPORT-359
  - TC-GS-IMPORT-833
  - TC-GS-IMPORT-834
coverage:
  web: automated
---

# Partial Commit: baris error tetap, duplicate dihapus, error diperbaiki lalu commit ulang, dan penomoran ulang padat Row #

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import (Client E), Tab Brand; spec ini tidak menguji navigasi sehingga tidak membuka ulang Tab Brand kecuali setelah berpindah ke halaman lain.
- Client E khusus commit: Date Format `dd MMM yy`, Time Format `HH:mm`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`. Master data Pre-setup Client E seperti Client A (Brand `Samsung` sebagai duplikat terhadap sistem).
- Data Dinamis (fixture baru; berkas dan nama literal dari TC karena Client E dedicated commit dan direset sesuai D-47):
  - `Fixture.import.brandPartial15` (brand-partial-15.csv, D-58): draft Brand 15 baris: #1 sampai #9 `Nikon`, `Pentax`, `Olympus`, `Fujifilm`, `Leica`, `Sigma`, `Tamron`, `Hasselblad`, `Ricoh` (`pending`); #10 dan #11 `Brand Kembar` (`duplicate` antar-baris); #12 `Brand Kembar` (`pending`); #13 `Samsung` (`duplicate` terhadap sistem); #14 Brand Name 121 karakter huruf `A` dan #15 Brand Name 121 karakter huruf `B` (`error`). Dipakai di TC-GS-IMPORT-358 (dengan umur draft 25 jam) dan TC-GS-IMPORT-834 (tanpa umur).
  - `Fixture.import.brandErr14` (D-17): draft Brand 14 baris di Client E: 12 baris `pending` (seperti brand-12.csv) dan baris #13 dan #14 `error` (Brand Name nilai sumber Brand pertama D-41 sebanyak 121 karakter, dan nilai sumber Brand kedua D-41 sebanyak 125 karakter) dengan badge saran AI; layanan AI mock mode normal (D-40, D-41, D-42) dipakai sebagai precondition TC-GS-IMPORT-833, tidak diasersi.
  - Nilai pengganti TC-GS-IMPORT-359: `Kamera Baru` dan `Printer Baru` (belum ada di sistem).
- Kemampuan teknis yang disediakan tim FE/BE: penyiapan draft Client E lewat fixture sebelum tiap blok (R1, R3); hook umur draft D-76 varian 1 (`created_at` dimundurkan 25 jam, diterapkan sebelum halaman dimuat); mock layanan AI mode normal (D-40) dan pengembaliannya di hook `after`; reset Client E sesuai D-47 (hapus Brand hasil commit, hapus draft, reset hasil commit terakhir dan penanda Banner Hasil Commit); worker commit normal (tunggu commit selesai dengan batas 2 menit, muat ulang tiap 5 detik).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset Client E sesuai D-47, kembalikan mock AI ke mode normal, pulihkan sesi ke akun default suite. Hook `afterEach` suite juga mereset Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- State global: Client E berubah permanen oleh commit dan dipulihkan oleh reset D-47; suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `GS_CLIENTE_TC_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-358: Partial Commit

1. Siapkan draft Brand 15 baris (brand-partial-15.csv, D-58) di Client E lewat fixture, mundurkan umur draft 25 jam (D-76 varian 1), lalu muat ulang halaman Import > Brand
2. Catat baseline: buka Changelog Import (icon [Changelog] di header halaman), baca total pada teks Pagination (0 bila empty state), lalu tutup modal
3. Klik [Import (10)]
4. Muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
5. Verifikasi Staging Metric Card Total Rows 2
6. Verifikasi Staging Metric Card Ready to Import 0 (Disabled)
7. Verifikasi Staging Metric Card Errors 2
8. Verifikasi Staging Metric Card Duplicates 0 (Disabled)
9. Verifikasi Staging Table menampilkan 2 baris berstatus `error` (Brand Name 121 karakter)
10. Verifikasi tidak ada baris `duplicate` yang tampil
11. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 2 errors remain." tampil
12. Verifikasi Unsaved Banner dengan tombol `[Discard]` tampil
13. Buka halaman Master Reference > Brand
14. Atur Rows per page 100
15. Verifikasi halaman Master Reference > Brand Client E memuat 10 Brand baru: Nikon, Pentax, Olympus, Fujifilm, Leica, Sigma, Tamron, Hasselblad, Ricoh, dan `Brand Kembar` satu kali
16. Verifikasi `Samsung` tetap satu
17. Verifikasi tidak ada Brand dari kedua baris `error`
18. Buka halaman Import > Brand
19. Buka Changelog Import (icon [Changelog] di header halaman)
20. Verifikasi total pada teks Pagination Changelog Import bertambah tepat satu dibanding baseline
21. Verifikasi entri teratas (sort default Date descending): Action `Import Brand`, Data `10 records imported, 3 duplicates ignored, 2 errors remaining`, Modified By `Yoga P`
22. Tutup modal Changelog Import

### TC-GS-IMPORT-359: Perbaiki baris error lalu commit ulang (melanjutkan keadaan akhir TC-GS-IMPORT-358)

23. Buka Changelog Import (icon [Changelog] di header halaman)
24. Klik icon Filter
25. Pilih Action `Import Brand` pada dropdown Action
26. Klik `[Apply]`
27. Catat angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state)
28. Tutup modal Changelog Import
29. Buka row action Edit pada baris `error` pertama dari atas
30. Ubah Brand Name menjadi `Kamera Baru`
31. Klik [Save]
32. Buka row action Edit pada baris `error` yang tersisa
33. Ubah Brand Name menjadi `Printer Baru`
34. Klik [Save]
35. Verifikasi Staging Metric Card Ready to Import 2
36. Verifikasi Staging Metric Card Errors 0 (Disabled)
37. Verifikasi footer menampilkan `[Import (2)]`
38. Klik [Import (2)]
39. Muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
40. Verifikasi Dropzone tampil menggantikan Staging Table
41. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
42. Buka halaman Master Reference > Brand
43. Atur Rows per page 100
44. Verifikasi halaman Master Reference > Brand Client E memuat Brand `Kamera Baru` dan `Printer Baru`
45. Buka halaman Import > Brand
46. Buka Changelog Import (icon [Changelog] di header halaman)
47. Klik icon Filter
48. Pilih Action `Import Brand` pada dropdown Action
49. Klik `[Apply]`
50. Baca angka total pada teks Pagination
51. Verifikasi total pada Pagination Changelog Import dengan Filter Action `Import Brand` bertambah tepat satu dibanding langkah 27
52. Verifikasi baris pertama tabel (sort default Date descending): Data `2 records imported, 0 duplicates ignored, 0 errors remaining`
53. Tutup modal Changelog Import dan reset Client E sesuai D-47 lewat fixture

### TC-GS-IMPORT-833: Penomoran ulang padat setelah commit (draft 12 pending dan 2 error)

54. Siapkan draft Brand 14 baris (D-17) di Client E lewat fixture dengan mock AI mode normal, lalu muat ulang halaman Import > Brand
55. Atur Rows per page 100
56. Verifikasi dua baris `error` bernomor 13 dan 14
57. Klik [Import (12)]
58. Muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
59. Verifikasi Staging Table menampilkan 2 baris `error`: baris dengan Brand Name 121 karakter bernomor 1 dan baris dengan Brand Name 125 karakter bernomor 2
60. Verifikasi Staging Metric Card Total Rows 2 (Active)
61. Verifikasi Staging Metric Card Ready to Import 0 (Disabled)
62. Verifikasi Staging Metric Card Errors 2
63. Verifikasi Staging Metric Card Duplicates 0 (Disabled)
64. Verifikasi Pagination "Showing 1 - 2 of 2 items"
65. Reset Client E sesuai D-47 lewat fixture

### TC-GS-IMPORT-834: Penomoran ulang padat setelah commit (draft 10 pending, 2 error, 3 duplicate)

66. Siapkan draft Brand 15 baris (brand-partial-15.csv, D-58) di Client E lewat fixture, lalu muat ulang halaman Import > Brand
67. Atur Rows per page 100
68. Verifikasi dua baris `error` bernomor 14 dan 15
69. Klik [Import (10)]
70. Muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
71. Verifikasi Staging Table menampilkan 2 baris `error`: baris Brand Name 121 huruf `A` bernomor 1 dan baris Brand Name 121 huruf `B` bernomor 2
72. Verifikasi tidak ada baris `duplicate` yang tampil
73. Verifikasi Staging Metric Card Total Rows 2 (Active)
74. Verifikasi Staging Metric Card Ready to Import 0 (Disabled)
75. Verifikasi Staging Metric Card Errors 2
76. Verifikasi Staging Metric Card Duplicates 0 (Disabled)
77. Verifikasi Pagination "Showing 1 - 2 of 2 items"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-358, 359, 833, 834).
- Subjudul `###` memetakan langkah ke id TC granular. TC-GS-IMPORT-359 diletakkan tepat sesudah TC-GS-IMPORT-358 dalam spec yang sama karena melanjutkan keadaan akhirnya (draft Brand 2 baris `error`, Dependensi 1 pada TC sumber); TC-GS-IMPORT-359 tidak punya D-ref sendiri. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 54, 66 (penyiapan draft sebagai precondition TC lewat fixture); langkah 2 (baseline jumlah entri Changelog Import sebelum aksi pemicu pertama yang diasersi, S-12); langkah 22, 28 (menutup modal); langkah 23 sampai 27 (membaca baseline total Pagination dengan Filter Action `Import Brand`, sesuai TC langkah 1 sampai 5); langkah 53, 65 (reset Client E sesuai D-47 sebelum TC berikutnya, Kontrak Fixture R1); langkah 14, 43, 55, 67 (Rows per page 100).
- Baseline Changelog: pada TC-GS-IMPORT-358 total Changelog tanpa filter dibandingkan sebelum dan sesudah; pada TC-GS-IMPORT-359 total dengan Filter Action `Import Brand` dibandingkan dengan nilai langkah 27 (S-12). Total tidak diasersi sebagai angka absolut.
- Absence: "tidak ada baris `duplicate`" (langkah 10, 72) didahului `Verifikasi` dua baris `error` tampil pada tabel yang sama; "tidak ada Brand dari kedua baris `error`" (langkah 17) didahului `Verifikasi` 10 Brand baru tampil di daftar yang sama.
- Spec ini di atas sekitar 35 langkah (77 langkah). Alasan: empat blok yang berdiri sendiri dengan draft Client E dan reset D-47 sendiri (TC-GS-IMPORT-358 dan 359 berurutan karena 359 melanjutkan 358; TC-GS-IMPORT-833 dan 834 homogen: periksa penomoran ulang padat setelah commit); kegagalan 833 atau 834 tidak membuat blok sebelumnya kehilangan makna.
- Pembagian TC lintas spec: commit sukses tanpa baris error ada di spec 133 dan 134; Banner Hasil Commit dapat ditutup dan batas umur banner di spec 136; Commit hanya menambah record di spec 137.
- Temuan untuk QA:
  - TC-GS-IMPORT-359 tidak punya D-ref dan Precondition-nya bergantung pada keadaan akhir TC-GS-IMPORT-358 (2 baris `error` tersisa); tidak berdiri sendiri. Spec meletakkannya sesudah TC-GS-IMPORT-358.
  - TC-GS-IMPORT-359 langkah 5 menyebut "0 bila yang tampil adalah empty state" sebagai baseline tetapi tidak menyatakan nilai awal yang dijamin; spec mencatat baseline dari pembacaan langkah 27.
  - Post Condition TC-GS-IMPORT-833 (a, b, c) dan TC-GS-IMPORT-834 (a, b, c) tidak punya langkah observasi tambahan di luar Expected; hanya yang ada di Expected yang diasersi. Khusus 833 dan 834 Post Condition b (record Brand baru tersimpan di Master Reference > Brand) tidak diasersi.
  - TC-GS-IMPORT-833 Precondition d (mock AI mode normal) dan D-17 (badge saran AI pada kedua baris `error`) tidak diasersi pada Expected; spec memakai keduanya sebagai precondition tanpa `Verifikasi`.
  - TC-GS-IMPORT-358 Precondition d (umur draft 25 jam, D-76) hanya relevan untuk Unsaved Banner (Expected d); spec menerapkan hook umur draft hanya pada TC-GS-IMPORT-358 dan tidak pada 834 yang memakai D-58 yang sama tanpa Precondition umur.
  - TC-GS-IMPORT-358, 359, 833, dan 834 bertanda FE Test `Need API` tanpa menyebut endpoint; spec tidak menyebut endpoint (S-13).
  - Baseline Changelog pada TC-GS-IMPORT-358 tidak ada di TC; spec menambah langkah baseline (S-12) sebagai langkah penghubung.
