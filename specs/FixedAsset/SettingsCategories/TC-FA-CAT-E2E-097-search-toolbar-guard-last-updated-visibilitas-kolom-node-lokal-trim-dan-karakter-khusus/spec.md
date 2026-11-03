---
id: TC-FA-CAT-E2E-097-search-toolbar-guard-last-updated-visibilitas-kolom-node-lokal-trim-dan-karakter-khusus
title: "Search Toolbar: Modified By, Guard Last Updated, Visibilitas Kolom, Trim, Karakter Khusus, dan Pencarian Lokal Node"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-326
  - TC-FA-CAT-327
  - TC-FA-CAT-328
  - TC-FA-CAT-330
  - TC-FA-CAT-331
  - TC-FA-CAT-329
coverage:
  web: automated
---

# Search Toolbar: Modified By, Guard Last Updated, Visibilitas Kolom, Trim, Karakter Khusus, dan Pencarian Lokal Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini pada client CatMany (Pre-setup #24); halaman dibuka hook `beforeEach` suite. Langkah 21 berganti akun ke Total Control client CatMain (Pre-setup #20); hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #24 (CatMany): 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30` dengan Code `SC01` sampai `SC30`; `Seed Cat 03` dan `Seed Cat 05` bercode `SC03` dan `SC05`. Sebagian baris Modified By `Alex B` (nama lengkap `Alex Brown`).
- Data Pre-setup #20 (CatMain) untuk TC-FA-CAT-329: node `Electronics` dan `Furniture` sebagai kategori sejajar (`Furniture` bukan direct child `Electronics`); `Electronics` memiliki sedikitnya satu direct child.
- State yang diubah spec: konfigurasi Setup Column (kolom Code disembunyikan lalu ditampilkan kembali pada langkah 8 dan 11). Pemulihan: hook `after` menghapus preferensi kolom di browser (butir hook suite di `suite.md`; kemampuan disediakan tim FE).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-326: Search kolom Modified By dengan nama depan

1. Ketik Search `alex`, tekan Enter
2. Verifikasi tabel memuat sedikitnya satu baris
3. Verifikasi seluruh baris yang Modified By-nya `Alex B` (nama lengkap `Alex Brown`) ditemukan

### TC-FA-CAT-327: Guard, kolom Last Updated tidak dapat dicari lewat Search toolbar

4. Klik icon panah (←) di kiri toolbar
5. Catat nilai Last Updated baris pertama tabel
6. Ketik Search nilai Last Updated baris pertama, tekan Enter
7. Verifikasi empty state `No results found` tampil (penyaringan tanggal hanya lewat Filter Panel)

### TC-FA-CAT-328: Search terikat visibilitas kolom

8. Buka Setup Column, hilangkan centang kolom Code, lalu Save
9. Ganti isi kotak search dengan `sc05`, tekan Enter
10. Verifikasi empty state `No results found` tampil (saat Code di-hide keyword `sc05` tidak mencocokkan baris)
11. Buka Setup Column, munculkan kembali kolom Code, lalu Save
12. Ganti isi kotak search dengan `sc05`, tekan Enter
13. Verifikasi baris `Seed Cat 05` ditemukan (setelah Code di-unhide)

### TC-FA-CAT-330: Query Search di-trim saat Enter tanpa mengubah isi input

14. Ganti isi kotak search dengan dua spasi + `Seed Cat 03` + dua spasi, tekan Enter
15. Verifikasi baris `Seed Cat 03` ditemukan (hasil sama dengan keyword tanpa spasi)
16. Verifikasi isi input di layar tetap dua spasi + `Seed Cat 03` + dua spasi

### TC-FA-CAT-331: Karakter khusus pada Search dicocokkan sebagai teks biasa

17. Ganti isi kotak search dengan `<b>x</b>`, tekan Enter
18. Verifikasi empty state `No results found` tampil
19. Verifikasi tidak ada markup yang dirender atau diinterpretasi (isi input tetap teks `<b>x</b>`)

### TC-FA-CAT-329: Search lokal terhadap node terpilih, tidak mencari di luar direct children

20. Klik icon panah (←) di kiri toolbar
21. Ganti akun: logout, lalu login sebagai Total Control client CatMain (Pre-setup #20) dengan `Spectra.env.FA_TC_PASSWORD`
22. Klik node `Electronics` di sidebar
23. Verifikasi tabel memuat sedikitnya satu baris direct child `Electronics`
24. Ketik Search `Furniture`, tekan Enter
25. Verifikasi Title `No results found` tampil (`Furniture` bukan direct child `Electronics`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Urutan TC: TC-FA-CAT-326, 327, 328, 330, 331 pada client CatMany, lalu TC-FA-CAT-329 pada client CatMain karena berganti client (S-10). Pembukaan halaman dipakai berulang; kotak Search diganti isinya antar-TC (8b.9).
- Spec 096 memuat TC-FA-CAT-321 sampai TC-FA-CAT-325.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 4 dan 20 (menutup Search), 5 (mencatat nilai), 8 dan 11 (Setup Column).
- Asersi `No results found` pada langkah 10 dan 25 adalah anchor positif absence hasil Search (8b.2); langkah 23 menjadi pembanding positif sebelum Search lokal.
- Temuan untuk QA:
  - TC-FA-CAT-327 menyebut "nilai tanggal baris pertama pada kolom Last Updated" tanpa format; spec mengetik nilai sebagaimana tampil di tabel.
  - TC-FA-CAT-331 Expected "tidak ada markup yang dirender" tidak punya locator yang disebut; spec mengasersi isi input tetap teks `<b>x</b>`.
  - TC-FA-CAT-326 tidak menyebut jumlah baris `Alex B`; spec mengasersi baris Modified By `Alex B` dari seed Pre-setup #24 tanpa jumlah.
