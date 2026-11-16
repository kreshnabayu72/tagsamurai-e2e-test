---
id: TC-FA-FACO-BE-158-search-sort-filter
title: "Hasil Search, Sort, dan Filter daftar akun"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [EB-SRC-1, EB-FLT-3, EB-SRT-1, "§5#b1"]
smoke: []
dependsOn: []
trace:
  EB-SRC-1: [2, 4, 6, 8, 10, 12, 14]
  EB-FLT-3: [16, 18, 20, 22, 24, 26]
  EB-SRT-1: [28, 30, 32, 34, 36, 38, 40]
  "§5#b1": [2, 16, 30, 42, 44, 49, 51, 53, 55, 57, 59, 61]
---

# Hasil Search, Sort, dan Filter daftar akun

## Prerequisites
- Aktor: Admin A (DU-158-1), Total Control dengan cakupan seluruh client.
- Data:
  - DU-158-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-158-2: Account Code `SFA-{runId}`, Account Name `anggur Kas Saring {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-158-3: Account Code `SFB-{runId}`, Account Name `Apel Kas Saring {runId}`, Account Function `Depreciation Expense`, Status `Active`.
  - DU-158-4: Account Code `SFC-{runId}`, Account Name `Beban Kas Saring {runId}`, Account Function `Accumulated Depreciation`, Status `Inactive`.
  - DU-158-5: Account Code `SFD-{runId}`, Account Name `cabang Kas Saring {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-158-6: Account Code `SFE-{runId}`, Account Name `Dana Kas Saring {runId}`, Account Function `Gain on Disposal`, Status `Inactive`.
  - DU-158-7: Account Code `SFF-{runId}`, Account Name `Kas Apel Lain Saring {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-158-8: 12 akun dengan Account Code `PG{n}-{runId}` dan Account Name `Kas Halaman {n} Paginasi {runId}` (n dari 1 sampai 12), Account Function `Asset Cost`, Status `Active`.
  - Changelog akun `CLG-{runId}` yang diharapkan sesudah langkah 45 sampai 47 memuat tepat 11 entri, dari DU-158-9 sampai DU-158-19: 1 entri Action `Create` dengan Field `Account Code`, 5 entri Action `Edit` dengan Field `Account Name`, dan 5 entri Action `Edit` dengan Field `Account Function`; entri dari Account Name terakhir `Kas Riwayat Log 5 {runId}` dan Account Function terakhir `Capitalization Offset` adalah entri terbaru.
- Kondisi:
  - Semua akun di atas belum pernah diekspor dan tidak dipakai Asset Class (Used By 0), sehingga spec ini tidak bergantung pada modul lain.
  - Pada permintaan daftar, `Saring {runId}` membatasi hasil ke keenam akun DU-158-2 sampai DU-158-7 dan `Paginasi {runId}` membatasi hasil ke ke-12 akun DU-158-8, sehingga akun lain di client tidak memengaruhi urutan atau isi hasil; langkah yang tidak memakainya menyatakan sendiri akun yang dicek.

## Test Steps

### Search mencocokkan substring tanpa membedakan huruf besar atau kecil
1. Admin A mengirim permintaan daftar dengan Search `pel Kas Saring {runId}`, potongan yang dimulai di tengah kata
2. Verifikasi hasil memuat akun `SFB-{runId}` dan tidak memuat akun SF lain
3. Admin A mengirim permintaan daftar dengan Search `APEL KAS SARING {runId}`, huruf besar semua kecuali runId
4. Verifikasi hasil memuat akun `SFB-{runId}` dan tidak memuat akun SF lain, sama dengan pencarian huruf campuran
5. Admin A mengirim permintaan daftar dengan Search `sfc-{runId}`, huruf kecil atas Account Code
6. Verifikasi hasil memuat akun `SFC-{runId}` dan tidak memuat akun SF lain, karena kolom Account Code ikut dicari
7. Admin A mengirim permintaan daftar dengan Search `Accumulated Depreciation`, label badge kolom Function
8. Verifikasi hasil memuat akun `SFC-{runId}` dan tidak memuat akun `SFA-{runId}`, `SFB-{runId}`, `SFD-{runId}`, `SFE-{runId}`, `SFF-{runId}`, karena kolom Function ikut dicari
9. Admin A mengirim permintaan daftar dengan Search `Apel Lain Saring {runId}`, urutan kata yang sama dengan Account Name
10. Verifikasi hasil memuat akun `SFF-{runId}` dan tidak memuat akun SF lain, karena spasi di tengah query menjadi bagian dari teks yang dicari
11. Admin A mengirim permintaan daftar dengan Search `Lain Apel Saring {runId}`, kata yang sama dengan urutan terbalik
12. Verifikasi hasil kosong, karena query tidak dipecah menjadi kata-kata terpisah
13. Admin A mengirim permintaan daftar dengan Search `Tidak Ada Saring {runId}` yang tidak cocok dengan akun mana pun
14. Verifikasi hasil kosong, yang pada tabel ditampilkan sebagai `No results found`

### Filter: logika OR dalam satu field dan AND antar field
15. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Filter Function berisi `Asset Cost` dan `Gain on Disposal`
16. Verifikasi hasil memuat tepat akun `SFA-{runId}`, `SFD-{runId}`, `SFE-{runId}`, `SFF-{runId}`, gabungan (OR) dari kedua nilai dalam satu field
17. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Filter Function berisi `Asset Cost` serta Filter Active berisi `Active`
18. Verifikasi hasil memuat tepat akun `SFA-{runId}`, `SFD-{runId}`, `SFF-{runId}`, irisan (AND) antar field, dan tidak memuat akun `SFE-{runId}` yang Function-nya `Gain on Disposal` maupun akun `SFB-{runId}` dan `SFC-{runId}`
19. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Filter Active berisi `Active` dan `Inactive`
20. Verifikasi hasil memuat keenam akun `SFA-{runId}`, `SFB-{runId}`, `SFC-{runId}`, `SFD-{runId}`, `SFE-{runId}`, `SFF-{runId}`, gabungan (OR) kedua status
21. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Filter Active berisi `Inactive`
22. Verifikasi hasil memuat tepat akun `SFC-{runId}`, `SFE-{runId}`
23. Admin A mengirim permintaan daftar dengan Search `Apel Kas Saring {runId}` dan Filter Function berisi `Asset Cost`
24. Verifikasi hasil kosong, karena akun yang cocok dengan Search (`SFB-{runId}`) tidak memenuhi Filter Function
25. Admin A mengirim permintaan daftar dengan Search `Apel` dan Filter Function berisi `Depreciation Expense`
26. Verifikasi hasil memuat akun `SFB-{runId}` dan tidak memuat akun `SFF-{runId}`, irisan Search dan Filter

### Sort sesuai tipe data kolom
27. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` tanpa Sort aktif
28. Verifikasi baris berurutan menurut default Account Code A-Z: `SFA-{runId}`, `SFB-{runId}`, `SFC-{runId}`, `SFD-{runId}`, `SFE-{runId}`, `SFF-{runId}`
29. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Account Name menaik
30. Verifikasi baris berurutan tanpa membedakan huruf besar atau kecil, sehingga Account Name `anggur Kas Saring {runId}` mendahului `Apel Kas Saring {runId}`: `SFA-{runId}`, `SFB-{runId}`, `SFC-{runId}`, `SFD-{runId}`, `SFE-{runId}`, `SFF-{runId}`
31. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Account Name menurun
32. Verifikasi baris berurutan `SFF-{runId}`, `SFE-{runId}`, `SFD-{runId}`, `SFC-{runId}`, `SFB-{runId}`, `SFA-{runId}`
33. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Function menaik
34. Verifikasi baris berurutan menurut label badge A-Z, dengan akun berfungsi sama diurutkan menurut default sort: `SFC-{runId}`, `SFA-{runId}`, `SFD-{runId}`, `SFF-{runId}`, `SFB-{runId}`, `SFE-{runId}`
35. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Active menaik (Active First)
36. Verifikasi akun Active di atas akun Inactive, masing-masing kelompok menurut default sort: `SFA-{runId}`, `SFB-{runId}`, `SFD-{runId}`, `SFF-{runId}`, `SFC-{runId}`, `SFE-{runId}`
37. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Active menurun (Inactive First)
38. Verifikasi akun Inactive di atas akun Active, masing-masing kelompok menurut default sort: `SFC-{runId}`, `SFE-{runId}`, `SFA-{runId}`, `SFB-{runId}`, `SFD-{runId}`, `SFF-{runId}`
39. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Account Code menurun
40. Verifikasi baris berurutan `SFF-{runId}`, `SFE-{runId}`, `SFD-{runId}`, `SFC-{runId}`, `SFB-{runId}`, `SFA-{runId}`, dan urutan yang sama muncul pada permintaan ulang

### Paginasi diproses server
41. Admin A mengirim permintaan daftar dengan Search `Paginasi {runId}`, ukuran halaman `10`, halaman 1
42. Verifikasi hasil memuat tepat 10 dari ke-12 akun DU-158-8
43. Admin A mengirim permintaan daftar dengan Search `Paginasi {runId}`, ukuran halaman `10`, halaman 2
44. Verifikasi hasil memuat tepat 2 akun, dan gabungan halaman 1 dan halaman 2 memuat ke-12 akun DU-158-8 tanpa akun ganda dan tanpa akun terlewat
### Changelog: Search, Filter, Sort, dan paginasi diproses server
45. Admin A mengirim Create dengan Account Code `CLG-{runId}`, Account Name `Kas Riwayat Log {runId}`, Account Function `Asset Cost`
46. Admin A mengirim lima Edit berurutan atas akun `CLG-{runId}`, masing-masing satu Save yang mengganti Account Name menjadi `Kas Riwayat Log 1 {runId}`, `Kas Riwayat Log 2 {runId}`, `Kas Riwayat Log 3 {runId}`, `Kas Riwayat Log 4 {runId}`, dan `Kas Riwayat Log 5 {runId}`
47. Admin A mengirim lima Edit berurutan atas akun `CLG-{runId}`, masing-masing satu Save yang mengganti Account Function menjadi `Depreciation Expense`, `Accumulated Depreciation`, `Gain on Disposal`, `Loss on Disposal`, dan `Capitalization Offset`
48. Admin A mengirim permintaan daftar Changelog dengan Search `CLG-{runId}`, ukuran halaman `10`, halaman 1, tanpa Sort aktif
49. Verifikasi hasil memuat tepat 10 baris, seluruhnya Action `Edit`, dengan baris pertama berisi Field `Account Function` dan New Value `Capitalization Offset`, karena urutan bawaan menempatkan entri terbaru di atas
50. Admin A mengirim permintaan daftar Changelog dengan Search `CLG-{runId}`, ukuran halaman `10`, halaman 2, tanpa Sort aktif
51. Verifikasi hasil memuat tepat 1 baris dengan Action `Create`, Field `Account Code`, dan New Value `CLG-{runId}`, sehingga halaman 1 dan halaman 2 memuat ke-11 entri tanpa baris ganda dan tanpa baris terlewat
52. Admin A mengirim permintaan daftar Changelog dengan Search `Kas Riwayat Log 3 {runId}`
53. Verifikasi hasil memuat tepat 2 baris dengan Field `Account Name`: satu dengan New Value `Kas Riwayat Log 3 {runId}` dan satu dengan Old Value `Kas Riwayat Log 3 {runId}`, karena kolom Old Value dan New Value ikut dicari
54. Admin A mengirim permintaan daftar Changelog dengan Search `CLG-{runId}` dan Filter Field berisi `Account Code` dan `Account Function`
55. Verifikasi hasil memuat tepat 6 baris: 1 baris Action `Create` dengan Field `Account Code` dan 5 baris Action `Edit` dengan Field `Account Function`, gabungan (OR) kedua nilai dalam satu field
56. Admin A mengirim permintaan daftar Changelog dengan Search `CLG-{runId}`, Filter Action berisi `Edit`, dan Filter Field berisi `Account Code` dan `Account Function`
57. Verifikasi hasil memuat tepat 5 baris Action `Edit` dengan Field `Account Function`, irisan (AND) antar field, dan tidak memuat baris Action `Create` yang Field-nya `Account Code`
58. Admin A mengirim permintaan daftar Changelog dengan Search `CLG-{runId}` dan Sort Field menaik, ukuran halaman `10`, halaman 1
59. Verifikasi baris berurutan menurut Field A-Z: 1 baris Field `Account Code`, lalu 5 baris Field `Account Function`, lalu 4 baris Field `Account Name`
60. Admin A mengirim permintaan daftar Changelog dengan Search `CLG-{runId}` dan Sort Field menaik, ukuran halaman `10`, halaman 2
61. Verifikasi hasil memuat tepat 1 baris dengan Field `Account Name`, sehingga Sort berlaku pada seluruh entri Changelog lintas halaman dan bukan per halaman
