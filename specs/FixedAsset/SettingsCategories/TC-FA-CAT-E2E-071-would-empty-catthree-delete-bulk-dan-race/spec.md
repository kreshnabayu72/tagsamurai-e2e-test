---
id: TC-FA-CAT-E2E-071-would-empty-catthree-delete-bulk-dan-race
title: "Would-Empty CatThree: Bulk Delete Seluruh Kategori Diblok D-10, Race Bulk Delete dan Delete Tunggal Ditolak 409"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-254
  - TC-FA-CAT-235
  - TC-FA-CAT-264
coverage:
  web: automated
---

# Would-Empty CatThree: Bulk Delete Seluruh Kategori Diblok D-10, Race Bulk Delete dan Delete Tunggal Ditolak 409

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatThree (Pre-setup #48), password dari `Spectra.env.FA_TC_PASSWORD`. Email akun client CatThree tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #48 (CatThree): tiga kategori L1 `Limit A`, `Limit B`, `Limit C`. Spec ini menghapus `Limit C` dan `Limit B` (kategori client khusus yang tidak dapat dimiliki spec karena Would-Empty bergantung pada seluruh isi client). Pemulihan ke tiga kategori awal lewat fixture backend yang disediakan tim FE/BE, dijalankan di hook `before` dan `after`; efeknya (entri Changelog Delete dan Last Updated) dicatat sebagai efek spec ini. Suite berjalan serial (`parallel: false`).
- Pelaku kedua: sesi API Total Control (Pre-setup #1) yang hanya memicu penghapusan; mengikuti butir "Sesi API aktor" di `suite.md`.
- Kemampuan teknis: membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline); disediakan tim FE/BE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-254: Would-Empty gabungan, seleksi menyisakan 0 kategori diblok D-10

1. Centang checkbox baris `Limit A`, `Limit B`, dan `Limit C`
2. Klik `[Delete]` pada Bulk Action Bar
3. Verifikasi dialog `Cannot Delete Categories` dengan body `You've selected all remaining categories. At least one category must always exist — deselect at least one category and try again.` dan tombol `[OK]` tampil
4. Verifikasi tidak ada toast yang tampil
5. Verifikasi tabel masih memuat baris `Limit A`, `Limit B`, dan `Limit C` (tidak ada eksekusi)
6. Klik `[OK]`
7. Klik icon (×) pada Bulk Action Bar untuk membatalkan seleksi

### TC-FA-CAT-264: Would-Empty baru terpenuhi saat Confirm Bulk Delete, 409 sebelum baris pertama

8. Centang checkbox baris `Limit A` dan `Limit B`
9. Klik `[Delete]` pada Bulk Action Bar sampai dialog D-11 tampil
10. Sesi API Total Control menghapus `Limit C` hingga penghapusan tersimpan
11. Catat baseline jumlah entri Changelog kategori (N1)
12. Klik `[Delete]` pada dialog D-11
13. Verifikasi dialog D-10 `Cannot Delete Categories` dengan body `You've selected all remaining categories. At least one category must always exist — deselect at least one category and try again.` tampil
14. Verifikasi tabel masih memuat baris `Limit A` dan `Limit B` (tidak ada baris yang terhapus)
15. Klik `[OK]`
16. Verifikasi seleksi dan Bulk Action Bar dipertahankan dengan counter `2 categories selected`
17. Verifikasi jumlah entri Changelog kategori masih N1 (tidak ada log baru)
18. Klik icon (×) pada Bulk Action Bar untuk membatalkan seleksi

### TC-FA-CAT-235: Would-Empty baru terpenuhi saat Confirm Delete tunggal, 409 dan dialog berubah menjadi D-06

19. Klik elipsis (⋯) pada baris `Limit A` > `Delete` sampai dialog D-09 tampil
20. Sesi API Total Control menghapus `Limit B` hingga penghapusan tersimpan
21. Klik `[Delete]` pada dialog D-09
22. Verifikasi dialog kontekstual D-06 dengan teks yang diawali `This is your only category...` tampil (penolakan server 409)
23. Tutup dialog D-06
24. Verifikasi tabel masih memuat baris `Limit A` (tidak terhapus)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Urutan TC: TC-FA-CAT-254, TC-FA-CAT-264, lalu TC-FA-CAT-235 (S-10). Urutan ini mengikuti state: tiga kategori awal, lalu `Limit C` dihapus sesi lain, lalu `Limit B` dihapus sesi lain; TC-FA-CAT-235 mensyaratkan hanya dua kategori sehingga harus sesudah TC-FA-CAT-264.
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): klik `[OK]` dan icon (×) untuk menutup dialog dan membatalkan seleksi, tutup dialog D-06, pencatatan baseline Changelog.
- P-1: asersi "tidak ada log" pada TC-FA-CAT-264 diletakkan di spec ini dengan baseline (S-12) karena konteksnya (dialog D-11 terbuka dan perubahan oleh sesi lain) dibangun langkah sebelumnya dan tidak dapat dibentuk ulang di spec absence tanpa membangun seluruh state.
- Temuan untuk QA:
  - Email akun Total Control client CatThree tidak tertulis di Pre-setup TC (#48 hanya menyebut client).
  - TC-FA-CAT-264 Expected a hanya menulis teks D-10 dengan elipsis (`You've selected all remaining categories...`); spec memakai teks lengkap D-10 dari TC-FA-CAT-254.
  - TC-FA-CAT-264 menyebut "tidak ada log" tanpa menyebut surface; spec hanya memeriksa Changelog.
  - TC-FA-CAT-235 tidak menulis teks lengkap dan tombol dialog D-06; spec hanya meng-assert awalan teks dan menutup dialog tanpa menyebut tombol. Status 409 tidak teramati langsung di UI; diamati lewat dialog D-06.
  - TC-FA-CAT-235 dan TC-FA-CAT-264 berlabel Manual Only (dua sesi paralel), tetapi pelaku kedua hanya memicu perubahan state sehingga memakai sesi API.
