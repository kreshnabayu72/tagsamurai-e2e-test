---
id: TC-FA-GRP-E2E-211-tab-assets-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-hide
title: "Tab Assets Search: Interaksi, Last Updated Tidak Match, dan Kolom Asset ID Di-Hide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-677
  - TC-FA-GRP-681
  - TC-FA-GRP-682
coverage:
  web: automated
---

# Tab Assets Search: Interaksi, Last Updated Tidak Match, dan Kolom Asset ID Di-Hide

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: login default, flag Guided Tooltip `seen`, sesi API aktor, klien HTTP, dan fixture BE disediakan tim FE/BE.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9: 24 aset aktif variasi status + 2 Disposed). Nilai variasi (Name, Asset ID, Status, Brand, Model/Type, Category, Last Updated; sedikitnya dua nilai distinct per kolom yang dipakai Search, Filter, dan Sort, S-11) dan nilai fixture acuan `Fixture.settingsGroups.<kunci>` disediakan tim FE/BE; Tabel Data Uji TC tidak memuat nilai konkret (lihat Temuan untuk QA).
- Keyword: `Fixture.settingsGroups.searchKeyword` = potongan nilai kolom pertama Tab Assets (kolom Name) dengan sedikitnya dua karakter, dan `Fixture.settingsGroups.searchChar` = satu karakter pertamanya; `Fixture.settingsGroups.lastUpdatedBarisPertama` = nilai Last Updated baris pertama; `Fixture.settingsGroups.assetIdUnik` = nilai unik kolom Asset ID salah satu aset Warehouse A.
- Kemampuan teknis: menyalin dan menempel nilai sel (clipboard browser).
- Preferensi kolom Setup Column: spec ini tidak menyimpan konfigurasi kolom; tampilan kolom yang diubah lewat Column Visibility bersifat sesi dan dipulihkan di langkah penghubung. Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-GRP-677: Interaksi Search Tab Assets (reveal, Enter, clear, collapse)

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
3. Hover icon Search pada toolbar
4. Verifikasi tooltip Search tampil
5. Klik icon Search
6. Verifikasi input Search melebar
7. Verifikasi input Search auto-focus
8. Verifikasi placeholder input Search sesuai konvensi platform
9. Catat jumlah baris tabel Tab Assets sebelum mengetik Search
10. Ketik 1 karakter keyword `Fixture.settingsGroups.searchChar` di input Search tanpa menekan Enter
11. Verifikasi icon (✕) tampil di dalam input
12. Verifikasi tabel belum tersaring (jumlah baris sama dengan jumlah baris yang dicatat sebelum mengetik)
13. Ganti isi kotak search dengan `Fixture.settingsGroups.searchKeyword`, tekan Enter
14. Verifikasi sedikitnya satu baris tampil
15. Verifikasi setiap baris yang tampil sesuai keyword `Fixture.settingsGroups.searchKeyword`
16. Klik icon (✕) di dalam input
17. Verifikasi input Search kosong
18. Verifikasi input Search tetap terbuka dan fokus
19. Verifikasi tabel tetap menampilkan hasil search terakhir
20. Tekan Enter pada input kosong
21. Verifikasi tabel kembali menampilkan semua data (jumlah baris sama dengan jumlah baris yang dicatat sebelum mengetik Search)
22. Ketik Search `  Fixture.settingsGroups.searchKeyword  ` (dua spasi sebelum dan sesudah keyword), tekan Enter
23. Verifikasi baris yang tampil sama dengan baris pada langkah 15
24. Verifikasi isi input Search di layar tetap `  Fixture.settingsGroups.searchKeyword  ` seperti yang diketik
25. Ganti isi kotak search dengan `Fixture.settingsGroups.searchKeyword`, tekan Enter
26. Klik icon (←)
27. Verifikasi input Search tertutup
28. Verifikasi keyword dikosongkan
29. Verifikasi tabel langsung reset menampilkan semua data

### TC-FA-GRP-681: Search nilai Last Updated tidak menghasilkan match

30. Salin nilai Last Updated yang tampil pada baris pertama (`Fixture.settingsGroups.lastUpdatedBarisPertama`)
31. Klik icon Search, tempel nilai tersebut, tekan Enter
32. Verifikasi empty state "No results found"
33. Klik icon Filter
34. Verifikasi Filter Panel memuat field Last Updated
35. Tutup Filter Panel dan klik icon (←) pada kotak Search (langkah pemulihan)

### TC-FA-GRP-682: Search pada kolom Asset ID yang di-hide

36. Sembunyikan kolom Asset ID lewat Column Visibility
37. Ketik Search `Fixture.settingsGroups.assetIdUnik`, tekan Enter
38. Verifikasi empty state "No results found"
39. Tampilkan kembali kolom Asset ID lewat Column Visibility
40. Ganti isi kotak search dengan `Fixture.settingsGroups.assetIdUnik`, tekan Enter
41. Verifikasi baris yang cocok dengan nilai Asset ID tampil

## Notes

- Langkah penghubung (S-03): langkah 2 membuka Popup Detail Group Tab Assets dari Groups List; langkah 33 membuka Filter Panel hanya untuk menjangkau Expected TC-681 b dan menutupnya. Langkah menutup Filter Panel dan klik (←) serta langkah menampilkan kembali kolom adalah pemulihan state (S-09).
- Spec memuat 3 TC Search Tab Assets satu kelas harness tanpa harness eksternal; tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain. Jumlah langkah (41) di atas smell 35 langkah karena TC-677 sendiri memuat 8 klausa Expected (a sampai g) yang masing-masing menjadi `Verifikasi`.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Pembanding jumlah baris (S-12): jumlah baris tabel Tab Assets dicatat sebelum mengetik Search dan dipakai pada Verifikasi tabel belum tersaring serta tabel kembali menampilkan semua data.
- Temuan untuk QA:
  - TC-677 a: placeholder "sesuai konvensi platform" tidak menyebut teks persis; spec mengasersi mengikuti konvensi tanpa teks literal.
  - TC-677: "keyword 1 karakter lalu lanjutkan tanpa Enter" ambigu (lanjutkan apa); spec mengetik 1 karakter tanpa Enter lalu mengamati ikon (✕) dan tabel belum tersaring.
  - TC-677 dan TC-681/682: Tabel Data Uji TC tidak memuat nilai konkret; nilai keyword memakai fixture yang disediakan tim FE/BE.
  - TC-681 b: "penyaringan Last Updated hanya tersedia lewat Filter Panel" tidak punya langkah observasi di TC; diasersi sebagai keberadaan field Last Updated di Filter Panel.
