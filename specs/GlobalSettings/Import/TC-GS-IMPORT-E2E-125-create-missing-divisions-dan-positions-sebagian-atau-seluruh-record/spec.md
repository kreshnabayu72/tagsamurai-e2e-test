---
id: TC-GS-IMPORT-E2E-125-create-missing-divisions-dan-positions-sebagian-atau-seluruh-record
title: "Create Missing Divisions dan Positions: sebagian atau seluruh record gagal, kategori Callout baru, dan urutan pesan Callout"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-330
  - TC-GS-IMPORT-331
  - TC-GS-IMPORT-333
  - TC-GS-IMPORT-334
  - TC-GS-IMPORT-854
  - TC-GS-IMPORT-865
coverage:
  web: automated
---

# Create Missing Divisions dan Positions: sebagian atau seluruh record gagal, kategori Callout baru, dan urutan pesan Callout

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Spec ini tidak memakai akun lain (Admin kedua Client C tidak dibutuhkan langkah).
- Layar awal: hook `beforeEach` suite membuka Import > User Login (Client C); `## Test Steps` membuka Global Settings > User > Division atau Position hanya untuk verifikasi master data, lalu kembali ke Import > User Login.
- Data Pre-setup Client C (tidak diubah spec ini): Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang` (5 baris); Position `Store Manager`, `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor` (5 baris). Client C tanpa draft Tab User Login pada awal spec (Kontrak Fixture R1).
- Data Dinamis (berkas CSV User Login standar D-45 dengan isi dari Data Uji TC pemakai; fixture baru `Fixture.import.berkas`, disediakan tim QA): `user-login-division-partial.csv` (3 baris: Division `Logistik`, `Pengadaan`, dan 121 karakter), `user-login-division-emoji.csv` (1 baris: Division `Logistik 😀`), `user-login-position-emoji.csv` (1 baris: Division `Engineering`, Position `Store Supervisor 😀`), `user-login-position-partial.csv` (3 baris: Position `Store Supervisor`, `Shift Lead`, dan 121 karakter), `user-login-division-partial-3.csv` (3 baris: `Logistik`, `Pengadaan`, 121 karakter huruf `D`), `user-login-order-2.csv` (2 baris: baris 1 Division 121 karakter huruf `D`; baris 2 Division `Engineering` dan Position `Store Supervisor`).
- Nama master data baru yang dibuat spec lewat Create Missing (`Logistik`, `Pengadaan`, `Store Supervisor`, `Shift Lead`) literal tanpa suffix karena isi berkas CSV menentukan pesan "not found"; hook `before` menghapus sisa nama itu lewat API (kemampuan disediakan tim FE/BE) dan langkah penghubung menghapusnya di antara TC; hook `after` menghapusnya lagi dan melakukan Discard Draft Tab User Login Client C.
- Layanan AI mock mode normal (Data Dinamis D-40, tabel D-41 dan D-42): hook `before` menyetel mode normal; hook `after` mengembalikan ke normal.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis disediakan tim FE/BE: reset draft Tab User Login Client C ke tanpa draft (Kontrak Fixture R1) dan hapus Division atau Position lewat API (Kontrak Fixture R2).
- State global: master data Client C dan mock AI; suite berjalan serial (`parallel: false`).
- Env var: `GS_CLIENTC_TC_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-330: Bulk Create Missing, 2 nama valid dan 1 nama tidak valid

1. Klik [Upload File] di Dropzone
2. Pilih berkas `user-login-division-partial.csv` di file picker
3. Biarkan seluruh dropdown File Column pada nilai auto-match
4. Klik [Confirm Mapping]
5. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
6. Verifikasi toast sukses "Success, division has been created. Some items were skipped."
7. Verifikasi Error Summary Callout memuat "Division: Max. 120 characters" dengan badge "1 row"
8. Muat ulang halaman Import > User Login
9. Verifikasi baris #1 dan baris #2 berstatus `pending`
10. Verifikasi baris #3 tetap berstatus `error`
11. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 2, Errors 1
12. Verifikasi Error Summary Callout tetap memuat "Division: Max. 120 characters" dengan badge "1 row" setelah muat ulang halaman
13. Buka Global Settings > User > Division
14. Verifikasi daftar Division memuat `Logistik` dan `Pengadaan` (7 baris pada tabel)
15. Verifikasi daftar Division tidak memuat nama 121 karakter

### TC-GS-IMPORT-331: Seluruh record Division gagal

16. Hapus Division `Logistik` dan `Pengadaan` lewat API, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
17. Klik [Upload File] di Dropzone dan pilih berkas `user-login-division-emoji.csv`
18. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
19. Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
20. Verifikasi toast error "Error, failed to create division."
21. Verifikasi baris #1 tetap berstatus `error`
22. Verifikasi Error Summary Callout memuat "Division name contains invalid characters" dengan badge "1 row"
23. Buka Global Settings > User > Division
24. Verifikasi daftar Division tetap berisi 5 baris

### TC-GS-IMPORT-333: Seluruh record Position gagal

25. Reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
26. Klik [Upload File] di Dropzone dan pilih berkas `user-login-position-emoji.csv`
27. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
28. Klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
29. Verifikasi toast error "Error, failed to create position."
30. Verifikasi baris #1 tetap berstatus `error`
31. Verifikasi Error Summary Callout memuat "Position name contains invalid characters" dengan badge "1 row"
32. Buka Global Settings > User > Position
33. Verifikasi daftar Position tetap berisi 5 baris

### TC-GS-IMPORT-334: Bulk Create Missing Positions, sebagian record dilewati

34. Reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
35. Klik [Upload File] di Dropzone dan pilih berkas `user-login-position-partial.csv`
36. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
37. Klik `[Create Missing Positions]` pada baris pesan "Position not found" di Error Summary Callout
38. Verifikasi toast sukses "Success, position has been created. Some items were skipped."
39. Verifikasi Error Summary Callout memuat "Position: Max. 120 characters" dengan badge "1 row"
40. Muat ulang halaman Import > User Login
41. Verifikasi baris #1 dan baris #2 berstatus `pending`
42. Verifikasi baris #3 tetap berstatus `error`
43. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 2, Errors 1
44. Buka Global Settings > User > Position
45. Verifikasi daftar Position memuat `Store Supervisor` dan `Shift Lead` (7 baris pada tabel)
46. Verifikasi daftar Position tidak memuat nama 121 karakter

### TC-GS-IMPORT-854: Kategori Callout baru untuk baris gagal dan percobaan ulang lewat Actions per-baris

47. Hapus Position `Store Supervisor` dan `Shift Lead` lewat API, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
48. Klik [Upload File] dan pilih berkas `user-login-division-partial-3.csv`
49. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
50. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "3 rows"
51. Pada Error Summary Callout kategori "Division not found" klik [Create Missing Divisions]
52. Verifikasi toast sukses "Success, division has been created. Some items were skipped."
53. Verifikasi baris #3 tetap berstatus `error`
54. Verifikasi Error Summary Callout memuat "Division: Max. 120 characters" dengan badge "1 row"
55. Verifikasi Error Summary Callout memuat [View Data] dan [Delete All Rows] tanpa tombol [Create Missing Divisions]
56. Verifikasi kategori "Division not found" tidak tampil di Error Summary Callout
57. Klik `⋯` pada baris #3 lalu pilih `[Create Missing Divisions]`
58. Verifikasi toast error "Error, failed to create division."
59. Verifikasi baris #3 tetap berstatus `error`
60. Buka Global Settings > User > Division
61. Verifikasi daftar Division memuat `Logistik` dan `Pengadaan` yang dibuat pada langkah 51
62. Verifikasi tidak ada Division baru selain `Logistik` dan `Pengadaan` (7 baris pada tabel)

### TC-GS-IMPORT-865: Urutan kategori Callout

63. Hapus Division `Logistik` dan `Pengadaan` lewat API, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
64. Klik [Upload File] dan pilih berkas `user-login-order-2.csv`
65. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
66. Verifikasi Error Summary Callout memuat "Division not found" (1 row) lalu "Position not found" (1 row) menurut urutan itu
67. Klik [Create Missing Divisions] pada kategori "Division not found" di Error Summary Callout
68. Verifikasi urutan baris pesan Error Summary Callout: "Division: Max. 120 characters" (1 row), lalu "Position not found" (1 row)
69. Verifikasi "Division not found" tidak tampil di Error Summary Callout

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-330, 331, 333, 334, 854, 865).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber 330, 331, 333, 334, 854, 865 dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16, 25, 34, 47, dan 63 (hapus master data yang dibuat TC sebelumnya, reset draft, dan buka kembali Import > User Login supaya precondition TC berikutnya terpenuhi, Kontrak Fixture R1 dan R2); langkah 13, 23, 32, 44, dan 60 berpindah ke daftar Division atau Position untuk verifikasi.
- Spec berisi 69 langkah, di atas sekitar 35 langkah. Alasan: enam blok TC berbentuk sama (unggah, Confirm Mapping, Create Missing, verifikasi hasil), tiap blok berdiri sendiri dengan draft dan master data yang di-reset di langkah pembuka, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Ukuran memuat blok baca-hasil per klausa Expected (S-01).
- Pembagian TC lintas spec: seluruh TC spec ini fungsional kelas none; tidak ada TC yang dibelah. Pola konflik kunci (338, 725 sampai 727, 919) ada di spec 126; duplicate dari pihak lain dan no-op halaman basi di spec 127.
- Pengecualian S-12 nama literal: nama `Logistik`, `Pengadaan`, `Store Supervisor`, dan `Shift Lead` literal tanpa suffix karena ditentukan isi berkas CSV dari TC; pembersihan sisa di hook `before` dan `after` serta suite serial menjamin isolasi.
- Temuan untuk QA:
  - TC-GS-IMPORT-854 menyebut Admin kedua Client C pada Precondition a, tetapi Langkah Uji tidak memuat langkah Admin kedua; spec tidak memakai akun itu.
  - TC-GS-IMPORT-854 Langkah 5 memakai menu `⋯` baris #3 untuk `[Create Missing Divisions]` padahal Expected c menyatakan Callout tidak lagi memuat tombol itu untuk kategori baru; ketersediaan item menu pada baris `error` bernama 121 karakter tidak dinyatakan TC, spec mengikuti TC.
  - Nama berkas CSV (misalnya `user-login-division-partial.csv`) hanya didefinisikan di kolom Data Uji TC, tidak ada di Tabel Data Uji Dinamis; spec memakai isi dari Data Uji TC.
  - Cara menghapus Division atau Position hasil Create Missing (Kontrak Fixture R2) dan mereset draft tidak didefinisikan sebagai endpoint di TC; dicatat sebagai kemampuan disediakan tim FE/BE.
  - Post Condition "tersimpan permanen" pada TC-GS-IMPORT-330, 334, dan 854 diamati lewat daftar Division atau Position, bukan lewat pembacaan data BE.
