---
id: TC-GS-IMPORT-E2E-094-save-diblokir-all-or-nothing-wajib-panjang-live-karakter-ke-121-urutan
title: "Save diblokir all-or-nothing: wajib, panjang live (karakter ke-121), urutan pesan, tiap Import Type, dan Save ditolak karena baris dihapus admin lain"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-212
  - TC-GS-IMPORT-213
  - TC-GS-IMPORT-214
  - TC-GS-IMPORT-671
  - TC-GS-IMPORT-673
  - TC-GS-IMPORT-674
  - TC-GS-IMPORT-842
coverage:
  web: automated
---

# Save diblokir all-or-nothing: wajib, panjang live (karakter ke-121), urutan pesan, tiap Import Type, dan Save ditolak karena baris dihapus admin lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan spec ini menggeser jam server (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pelaku kedua (hanya memicu Remove langsung, tanpa asersi UI di sesinya, P-2): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC2_PASSWORD`; klien HTTP untuk permintaan langsung disediakan tim FE/BE (endpoint Remove baris tidak tertulis di TC; lihat Temuan untuk QA).
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis (nama literal karena asersi bergantung pada isi dan jumlah baris; pengecualian S-12), dipulihkan oleh skrip pemulihan (Kontrak Fixture R2) sebelum spec: D-01 (Draft Brand 12 baris `pending`: #1 `Acme Corp`, #2 `Lenovo`, ..., #12 `Asus`), D-02 (Measurement 6 baris), D-03 (Position 6 baris), D-04 (Division 6 baris), D-05 (User Login 8 baris, Custom Field Shift Notes aktif). "N karakter `A`" berarti huruf `A` diulang N kali.
- Tabel "Batas panjang live" (TC-671; baris edit pada draft Client A):

  | No | Sub-Tab | Baris | Field | Batas | Pesan sel | Baris Callout |
  |---|---|---|---|---|---|---|
  | 1 | Measurement | #1 | Unit Name | 120 | Max. 120 characters | Unit Name: Max. 120 characters |
  | 2 | Measurement | #1 | Symbol | 10 | Max. 10 characters | Symbol: Max. 10 characters |
  | 3 | Position | #1 | Position Name | 120 | Max. 120 characters | Position Name: Max. 120 characters |
  | 4 | Division | #2 | Division Name | 120 | Max. 120 characters | Division Name: Max. 120 characters |
  | 5 | Division | #2 | Code | 15 | Max. 15 characters | Code: Max. 15 characters |
  | 6 | User Login | #1 | First Name | 120 | Max. 120 characters | First Name: Max. 120 characters |
  | 7 | User Login | #1 | Last Name | 120 | Max. 120 characters | Last Name: Max. 120 characters |
  | 8 | User Login | #1 | Employee ID | 120 | Max. 120 characters | Employee ID: Max. 120 characters |
  | 9 | User Login | #1 | Custom Field Shift Notes (Text Area) | 360 | Max. 360 characters | Shift notes: Max. 360 characters |

- Tabel "Field wajib dikosongkan" (TC-674):

  | No | Sub-Tab | Baris | Field | Pesan sel dan baris Callout |
  |---|---|---|---|---|
  | 1 | Measurement | #1 | Unit Name | Unit name must not be empty |
  | 2 | Measurement | #1 | Symbol | Symbol must not be empty |
  | 3 | Position | #1 | Position Name | Position name must not be empty |
  | 4 | Division | #2 | Division Name | Division name must not be empty |
  | 5 | User Login | #1 | First Name | First name must not be empty |
  | 6 | User Login | #1 | Last Name | Last name must not be empty |
  | 7 | User Login | #1 | Email | Email must not be empty |
  | 8 | User Login | #1 | Division | Division must not be empty |
  | 9 | User Login | #1 | Access | Access must not be empty |
- Kemampuan teknis: pengamatan toast dan dialog; injeksi value langsung ke DOM pada input sel (melewati filter input FE; disediakan tim FE); hook jam server (memajukan jam server 11 menit dan memulihkannya; jam browser tidak diubah karena kedaluwarsa kunci dihitung di server); sesi API Admin kedua dengan token Admin kedua; pembacaan pengenal baris Row # 1 dari respons pembacaan Staging Table; skrip pemulihan draft (semuanya disediakan tim FE/BE).
- State global: jam server dimajukan 11 menit pada langkah 65 dan dipulihkan ke waktu nyata pada langkah 73; hook `after` memulihkan jam server dan draft sebagai cadangan.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan jam server; pulihkan draft Brand, Measurement, Position, Division, dan User Login Client A ke D-01 sampai D-05; lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-212: Save dengan Brand Name kosong

1. Klik `⋯` pada baris #1, pilih `Edit`
2. Kosongkan Brand Name baris #1
3. Klik `[Save]`
4. Verifikasi `[Save]` diblokir tanpa toast sukses
5. Verifikasi sel Brand Name baris #1 berborder `danger` dengan pesan "Brand name must not be empty"
6. Verifikasi Error Summary Callout memuat satu baris pesan "Brand name must not be empty" dengan badge "1 row"
7. Verifikasi footer tetap menampilkan `[Cancel]` dan `[Save]` (sesi tetap terbuka)
8. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-213: Edit this page, satu baris melanggar menggagalkan seluruh simpan

9. Aktifkan Switch `Edit this page`
10. Ubah Brand Name baris #1 menjadi `Acme Corporation`
11. Ubah Brand Name baris #2 menjadi 121 karakter `A`
12. Klik `[Save]`
13. Verifikasi `[Save]` diblokir: sel Brand Name baris #2 berborder `danger` dengan pesan "Max. 120 characters"
14. Verifikasi Error Summary Callout memuat satu baris pesan "Brand Name: Max. 120 characters" dengan badge "1 row"
15. Verifikasi footer tetap `[Cancel]` dan `[Save]`
16. Klik `[Cancel]`
17. Klik `[Discard]` pada dialog Discard Changes
18. Verifikasi baris #1 menampilkan `Acme Corp` (perubahan valid pada baris #1 tidak tersimpan)

### TC-GS-IMPORT-214: Aturan panjang ditandai live di karakter ke-121

19. Klik `⋯` pada baris #1, pilih `Edit`
20. Ganti isi sel Brand Name baris #1 dengan 120 karakter `A`
21. Verifikasi sel Brand Name baris #1 tidak berborder `danger`
22. Verifikasi sel Brand Name baris #1 tanpa pesan
23. Ketik satu karakter `A` sehingga isi sel 121 karakter
24. Verifikasi sel Brand Name baris #1 berborder `danger` dengan pesan "Max. 120 characters"
25. Hapus satu karakter sehingga isi sel kembali 120 karakter
26. Verifikasi border `danger` dan pesan pada sel Brand Name baris #1 hilang
27. Kosongkan seluruh isi sel
28. Klik area kosong di luar tabel (blur)
29. Verifikasi sel Brand Name baris #1 kosong tidak berborder `danger` dan tanpa pesan (tidak ada validasi saat blur)
30. Klik `[Save]`
31. Verifikasi `[Save]` diblokir dan sel Brand Name baris #1 berborder `danger` dengan pesan "Brand name must not be empty"
32. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-673: Dua aturan dilanggar, pesan aturan pertama

33. Klik `⋯` pada baris #1, pilih `Edit`
34. Ganti isi sel Brand Name baris #1 dengan 121 karakter `A` diikuti emoji 😀 lewat injeksi value langsung ke DOM
35. Klik `[Save]`
36. Verifikasi `[Save]` diblokir dan sel Brand Name baris #1 berborder `danger` dengan pesan "Max. 120 characters"
37. Verifikasi Error Summary Callout memuat baris pesan "Brand Name: Max. 120 characters"
38. Verifikasi Error Summary Callout tidak memuat baris pesan "Brand name contains invalid characters"
39. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-671: Batas panjang live pada tiap field

Untuk setiap baris tabel "Batas panjang live" (langkah 40 sampai 52 diulang sembilan kali, urutan No 1 sampai 9):

40. Buka Sub-Tab sesuai kolom Sub-Tab
41. Klik `⋯` pada baris sesuai kolom Baris, pilih `Edit`
42. Isi sel field sesuai kolom Field dengan karakter `A` sebanyak Batas
43. Verifikasi sel field tidak berborder `danger`
44. Verifikasi sel field tanpa pesan
45. Ketik satu karakter `A` tambahan
46. Verifikasi sel field berborder `danger` dengan Pesan sel
47. Klik `[Save]`
48. Verifikasi `[Save]` diblokir: sel field berborder `danger` dengan Pesan sel
49. Verifikasi Error Summary Callout memuat baris pesan sesuai kolom Baris Callout dengan badge "1 row"
50. Verifikasi footer tetap `[Cancel]` dan `[Save]`
51. Klik `[Cancel]`
52. Klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-674: Field wajib dikosongkan pada tiap Import Type

Untuk setiap baris tabel "Field wajib dikosongkan" (langkah 53 sampai 60 diulang sembilan kali, urutan No 1 sampai 9):

53. Buka Sub-Tab sesuai kolom Sub-Tab
54. Klik `⋯` pada baris sesuai kolom Baris, pilih `Edit`
55. Kosongkan sel field sesuai kolom Field
56. Klik `[Save]`
57. Verifikasi `[Save]` diblokir tanpa toast sukses
58. Verifikasi sel field berborder `danger` dengan pesan sesuai kolom Pesan
59. Verifikasi Error Summary Callout memuat baris pesan sesuai kolom Pesan dengan badge "1 row"
60. Verifikasi footer tetap `[Cancel]` dan `[Save]`; klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-842: Save ditolak karena baris dihapus admin lain (dijalankan paling akhir)

61. Pilih Sub-Tab Brand; ambil pengenal baris Row # 1 dari respons pembacaan Staging Table (aksi Admin kedua Client A, tanpa `Verifikasi`)
62. Aktifkan Switch `Edit this page`
63. Ubah Brand Name baris #1 menjadi `Acme Corporation`
64. Ubah Brand Name baris #2 menjadi `Lenovo Baru`
65. Majukan jam server 11 menit (fixture jam server)
66. Admin kedua Client A mengirim permintaan Remove langsung ke server dengan token akun Admin kedua Client A untuk pengenal baris itu
67. Verifikasi server membalas sukses atas permintaan Remove langsung
68. Klik `[Save]`
69. Verifikasi dialog dengan Title "Draft Is Being Edited" dan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." tampil
70. Verifikasi dialog hanya memiliki tombol `[OK]`
71. Klik `[OK]`
72. Verifikasi dialog tertutup
73. Pulihkan jam server ke waktu nyata (aksi tanpa `Verifikasi`)
74. Muat ulang halaman Import > Brand
75. Verifikasi baris #1 menampilkan `Lenovo`
76. Verifikasi tidak ada baris `Lenovo Baru`, `Acme Corp`, maupun `Acme Corporation`
77. Verifikasi kartu Total Rows menampilkan 11
78. Verifikasi Pagination "Showing 1 - 10 of 11 items"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional; permintaan langsung dan jam server pada TC-842 hanyalah pemicu state (P-2), bukan objek uji kelas a atau d.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-673 dan TC-212 sampai 214 mendahului blok Sub-Tab lain; TC-842 dijalankan paling akhir karena menghapus baris dan memajukan jam server (prinsip 5 bagian 3). Jam server dipulihkan pada langkah 73 (sesudah Save ditolak dan sebelum pemuatan ulang) sebagai langkah aksi tanpa `Verifikasi` (S-09); hook `after` hanya cadangan.
- P-2: langkah 61, 65, 66, dan 73 adalah pemicu atau pemulihan (jam server, permintaan Remove langsung, pengenal baris); asersi respons server (langkah 67) hanya status sukses. Perilaku FE atas Save diasersi pada langkah 69 sampai 72.
- Langkah penghubung (tanpa `Verifikasi`): langkah 8, 16 sampai 17, 32, 39, 51 sampai 52, dan 60 (`[Cancel]` lalu `[Discard]`) membuang perubahan karena sesi edit berisi perubahan sehingga dialog Discard Changes pasti tampil.
- Langkah penghubung sebelum muat ulang: langkah 73 (pemulihan jam server) mendahului langkah 74 (muat ulang). `[OK]` pada langkah 71 menutup dialog dan sesi edit serta melepas kunci (PRD baris 568), sehingga tidak ada `[Cancel]` atau `[Discard]` sesudahnya.
- Spec berisi sekitar 246 langkah dengan ekspansi (langkah 40 sampai 52 dikali 9 dan langkah 53 sampai 60 dikali 9 ditambah 57 langkah lain). Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (Save diblokir all-or-nothing), parameter tiap iterasi ada di tabel Prerequisites tanpa langkah bersyarat, tiap blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-672 dan 675 (karakter terlarang dan format) ada di spec 095; TC-GS-IMPORT-871 dan 869 (kunci sesi) ada di spec lain.
- Temuan untuk QA:
  - TC-GS-IMPORT-673 langkah 3 (121 karakter `A` diikuti emoji 😀) belum menyebut injeksi value langsung ke DOM, sedangkan TC-GS-IMPORT-672 memakainya karena filter input FE memblok karakter di luar whitelist; spec menulis langkah 34 dengan injeksi agar kedua aturan sama-sama dilanggar dan presedensi pesan teruji.
  - TC-GS-IMPORT-842 Expected a ("server membalas sukses" atas permintaan Remove langsung) mengasersi kontrak API pada langkah 6 padahal judul dan objek uji adalah penolakan Save; spec memuatnya sebagai langkah 67 dan tidak mengasersi perilaku FE atas permintaan langsung (8b butir 1). TC berada di section 3g (konflik kunci) padahal topiknya Save all-or-nothing.
  - TC-GS-IMPORT-842 tidak menyebut endpoint Remove langsung maupun cara mengambil pengenal baris; spec memakai "permintaan Remove langsung" dan "respons pembacaan Staging Table" tanpa mengarang endpoint; disediakan tim FE/BE (S-13).
  - TC-GS-IMPORT-842 Expected e ("Showing 1 - 10 of 11 items") dan Expected d bergantung pada urutan dan jumlah D-01; tidak ada hook jam browser karena kedaluwarsa kunci dihitung server.
  - TC-GS-IMPORT-213, 214, 673: nilai "121 kali" atau "120 kali" ditandai `PRD?` di dump TC; ini data uji berulang karakter dan tidak memengaruhi hasil.
  - TC-GS-IMPORT-842 Expected b menulis Body "Another admin is currently editing this draft. Please try again in a moment.", yang menyimpang dari PRD baris 568 ("Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved."); spec mengikuti PRD pada langkah 69. Expected c (dialog tertutup, sesi edit tertutup, kunci dilepas) diasersi pada langkah 72 sebatas dialog tertutup; penutupan sesi dan pelepasan kunci tidak punya penanda UI di TC dan dibuktikan tidak langsung lewat muat ulang langkah 74.
  - Post Condition TC-842 ("Draft Brand Client A berisi 11 baris `pending`", "Jam server dikembalikan") dipenuhi oleh Expected e dan langkah 73; tidak diasersi lagi (S-01). Post Condition b TC-842 (sesi edit tertutup dan kunci dilepas setelah `[OK]`) dipenuhi oleh Expected c dan langkah 72; penutupan sesi tidak punya penanda UI selain dialog tertutup.
