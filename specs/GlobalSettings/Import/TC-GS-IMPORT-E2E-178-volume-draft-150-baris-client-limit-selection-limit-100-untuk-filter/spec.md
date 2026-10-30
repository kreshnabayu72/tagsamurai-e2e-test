---
id: TC-GS-IMPORT-E2E-178-volume-draft-150-baris-client-limit-selection-limit-100-untuk-filter
title: "Volume: draft 150 baris Client Limit (Selection Limit 100) untuk filter kartu halaman 2, retensi Sub-Tab, pagination 10/25/50/100, lompat halaman, reset halaman"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-464
  - TC-GS-IMPORT-472
  - TC-GS-IMPORT-478
  - TC-GS-IMPORT-479
  - TC-GS-IMPORT-480
  - TC-GS-IMPORT-576
  - TC-GS-IMPORT-586
  - TC-GS-IMPORT-763
coverage:
  web: automated
---

# Volume: draft 150 baris Client Limit (Selection Limit 100) untuk filter kartu halaman 2, retensi Sub-Tab, pagination 10/25/50/100, lompat halaman, reset halaman

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): draft Brand Client Limit dibagikan ke seluruh admin dan berbagi Sub-Tab Brand dengan draft D-32 (Selection Limit) pada spec lain; lihat `suite.md`. Spec ini hanya membaca draft (tidak menghapus atau mengubah baris).
- Akun aktor (login sekali di hook `before`): Total Control Client Limit (Bima Saputra) `totalControl_automated_qaTeam7@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTLIMIT_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client Limit dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): skrip seed draft Brand 150 baris lewat skrip fixture (volume >= 100 baris); Selection Limit Client Limit 100 (nilai minimum, R7); skrip reset Client Limit ke tanpa draft Tab Division.
- Data Dinamis (milik spec ini; draft dibuang oleh reset sehingga nama baris berkas literal): D-61 `brand-150-mixed.csv`: draft Brand 150 baris di Client Limit, 120 `pending`, 25 `error` `Max. 120 characters`, 5 `error` `contains invalid characters`; dibuat ulang sebelum spec ini karena berbagi Sub-Tab Brand Client Limit dengan D-32. Tab Division Client Limit tanpa draft.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus draft Client Limit dan kembalikan sesi ke akun default suite.

## Test Steps

### Pagination, lompat halaman, dan Rows per page (TC-GS-IMPORT-478, TC-GS-IMPORT-479, TC-GS-IMPORT-480)

1. Reset Client Limit lewat skrip fixture: seed draft Brand D-61 (150 baris) dan tanpa draft Tab Division
2. Buka Global Settings > Import, pilih Sub-Tab Brand
3. Verifikasi pagination menampilkan "Showing 1 - 10 of 150 items" (default 10 baris per halaman)
4. Buka dropdown Rows per page
5. Verifikasi dropdown Rows per page memuat opsi 10, 25, 50, dan 100
6. Verifikasi dropdown Rows per page tidak memuat opsi "All"
7. Tutup dropdown Rows per page dengan menekan Esc
8. Ketik `5` pada input nomor halaman, tekan Enter
9. Verifikasi tabel melompat ke halaman 5 dan pagination menampilkan "Showing 41 - 50 of 150 items"
10. Pindah ke halaman 1
11. Pilih Rows per page 25
12. Verifikasi pagination menampilkan "Showing 1 - 25 of 150 items"
13. Pilih Rows per page 50
14. Verifikasi pagination menampilkan "Showing 1 - 50 of 150 items"
15. Pilih Rows per page 100
16. Verifikasi pagination menampilkan "Showing 1 - 100 of 150 items"
17. Pilih Rows per page 10

### Filter kartu dan halaman (TC-GS-IMPORT-464, TC-GS-IMPORT-576)

18. Klik kartu Errors
19. Verifikasi kartu Errors Active
20. Verifikasi pagination menampilkan "Showing 1 - 10 of 30 items"
21. Pindah ke halaman 2 tabel
22. Verifikasi pagination menampilkan "Showing 11 - 20 of 30 items"
23. Klik kartu Errors yang sudah Active
24. Verifikasi kartu Errors tetap Active
25. Verifikasi pagination tetap "Showing 11 - 20 of 30 items" (halaman 2)
26. Verifikasi total item tetap 30 sehingga tabel tidak kembali ke semua baris (150)
27. Klik kartu Total Rows (kembali ke semua baris)
28. Pindah ke halaman 3
29. Klik kartu Errors
30. Verifikasi tabel kembali ke halaman 1 ("Showing 1 - 10 of 30 items")
31. Pindah ke halaman 2 pada kartu Errors
32. Klik `[View Data]` pada baris pesan `Brand Name: Max. 120 characters`
33. Verifikasi tabel kembali ke halaman 1 ("Showing 1 - 10 of 25 items")
34. Verifikasi filter kategori aktif (chip "Showing rows with: Brand Name: Max. 120 characters" tampil)

### Klik kartu Errors Active saat chip aktif (TC-GS-IMPORT-586)

35. Klik kartu Total Rows (kembali ke semua baris)
36. Klik `[View Data]` pada baris pesan `Brand Name: Max. 120 characters`
37. Verifikasi chip "Showing rows with: Brand Name: Max. 120 characters" dengan `[×]` tampil
38. Verifikasi kartu Errors Active
39. Verifikasi pagination menampilkan "Showing 1 - 10 of 25 items"
40. Pindah ke halaman 2 tabel
41. Verifikasi pagination menampilkan "Showing 11 - 20 of 25 items"
42. Klik kartu Errors yang sudah Active
43. Verifikasi kartu Errors tetap Active
44. Verifikasi chip terlepas
45. Verifikasi tabel menampilkan semua baris Error ("Showing 1 - 10 of 30 items") dan paginasi kembali ke halaman 1

### Klik [×] pada chip di halaman 2 (TC-GS-IMPORT-763)

46. Klik kartu Total Rows (kembali ke semua baris)
47. Klik `[View Data]` pada baris pesan `Brand Name: Max. 120 characters`
48. Pindah ke halaman 2 tabel
49. Verifikasi pagination menampilkan "Showing 11 - 20 of 25 items"
50. Klik `[×]` pada chip
51. Verifikasi kartu Errors tetap Active
52. Verifikasi chip hilang
53. Verifikasi pagination menampilkan "Showing 1 - 10 of 30 items" (halaman 1)

### Retensi filter dan halaman Sub-Tab Brand (TC-GS-IMPORT-472)

54. Klik kartu Total Rows (kembali ke semua baris)
55. Klik `[View Data]` pada baris pesan `Brand Name: Max. 120 characters`
56. Verifikasi chip "Showing rows with: Brand Name: Max. 120 characters" tampil
57. Verifikasi kartu Errors Active
58. Pindah ke halaman 2 tabel
59. Verifikasi pagination menampilkan "Showing 11 - 20 of 25 items"
60. Klik Sub-Tab Division
61. Verifikasi Tab Division menampilkan Dropzone
62. Verifikasi kartu Total Rows Active pada Tab Division
63. Verifikasi Tab Division tanpa chip
64. Klik Sub-Tab Brand
65. Verifikasi Tab Brand menampilkan kartu Errors Active
66. Verifikasi Tab Brand menampilkan chip "Showing rows with: Brand Name: Max. 120 characters"
67. Verifikasi pagination Tab Brand "Showing 11 - 20 of 25 items"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data (e); draft 150 baris (di atas ambang 100 baris) menjadi dataset bersama dan volume adalah syarat asersi pagination ("of 150 items", halaman 5, halaman 3). Spec hanya membaca draft sehingga delapan TC berbagi satu seeding.
- Alasan melewati sekitar 35 langkah (67 langkah nominal): lima kelompok homogen (pagination dan filter kartu pada satu dataset) yang membaca draft yang sama tanpa mengubah data, semua satu kelas volume. Seeding draft 150 baris satu kali di awal (langkah 1) dan penjagaan state antar-TC dengan klik kartu Total Rows memenuhi S-09.
- Urutan kelompok mengikuti kebutuhan state halaman: pagination default (TC-478, 479, 480) lebih dulu agar Rows per page dikembalikan ke 10, lalu filter kartu (TC-464, 576, 586, 763), dan retensi Sub-Tab terakhir (TC-472).
- Langkah penghubung (tanpa `Verifikasi`): seeding (langkah 1), pembukaan halaman dan Sub-Tab, pemulihan state antar-TC (langkah 10, 17, 27, 35, 46, 54: kembali ke halaman 1, Rows per page 10, atau klik kartu Total Rows), tutup dropdown (langkah 7), serta perpindahan halaman.
- Asersi absence chip (langkah 44, 52) didahului Verifikasi kartu Errors tetap Active (langkah 43, 51) sebagai anchor positif pada surface yang sama.
- Temuan untuk QA:
  - TC-GS-IMPORT-464, 472, 576, 586, 763 memakai draft D-61 yang dibuat ulang sebelum tiap TC; spec memakai satu draft untuk delapan TC karena semuanya hanya membaca. Penjagaan state antar-TC memakai klik kartu Total Rows (kartu Total Rows Active tanpa chip menurut Expected TC-GS-IMPORT-472 c).
  - TC-GS-IMPORT-478 Expected b menyebut Rows per page memuat opsi 10, 25, 50, 100 tanpa opsi "All"; TC tidak menyebut tampilan dropdown (daftar tertutup atau terbuka) sebelum klik.
  - TC-GS-IMPORT-479 dan TC-GS-IMPORT-480 tidak menyebut apakah Rows per page 10 dipulihkan sebelum TC berikutnya; spec memulihkannya (langkah 17).
  - Selection Limit 100 pada Client Limit tidak diasersi di spec ini; draft 150 baris dipakai sebagai volume. Asersi Selection Limit ada di spec lain (S3).
  - Post Condition semua TC di spec ini "-" dan tidak ada keadaan lain yang perlu dipulihkan selain yang dikerjakan hook `after`.
