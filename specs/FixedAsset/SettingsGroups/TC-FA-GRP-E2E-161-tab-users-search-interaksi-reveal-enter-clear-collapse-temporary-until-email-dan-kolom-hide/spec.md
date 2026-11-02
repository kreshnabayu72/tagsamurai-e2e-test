---
id: TC-FA-GRP-E2E-161-tab-users-search-interaksi-reveal-enter-clear-collapse-temporary-until-email-dan-kolom-hide
title: "Tab Users Search: Interaksi, Temporary Until Tidak Match, Email Searchable (Tidak di Filter Panel), dan Kolom Email Di-Hide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-572
  - TC-FA-GRP-583
  - TC-FA-GRP-584
  - TC-FA-GRP-675
coverage:
  web: automated
---

# Tab Users Search: Interaksi, Temporary Until Tidak Match, Email Searchable (Tidak di Filter Panel), dan Kolom Email Di-Hide

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Fixture (berkas baru `groupsTabUsers`, ditetapkan tim FE): `Fixture.groupsTabUsers.keywordKolomPertama` (potongan nilai kolom pertama tabel yang mencocokkan sedikitnya satu baris dan tidak semua baris), `Fixture.groupsTabUsers.emailUnik` (nilai unik kolom Email satu user).
- Kemampuan teknis (disediakan tim FE): menyalin nilai sel tabel ke langkah berikutnya (nilai Temporary Until baris pertama); menghapus preferensi kolom Setup Column di browser (pemulihan kolom di hook `after`).
- State yang diubah spec: kolom Email di-hide dan kolom Temporary Until ditampilkan lewat Column Visibility; dipulihkan lewat langkah penghubung di akhir spec dan hook `after` (hapus preferensi kolom).

## Test Steps

### TC-572: Interaksi Search

1. Klik angka Total User Warehouse A
2. Hover icon Search pada toolbar
3. Verifikasi tooltip Search tampil
4. Klik icon Search
5. Verifikasi input Search melebar
6. Verifikasi input Search auto-focus
7. Verifikasi placeholder input Search sesuai konvensi platform
8. Ketik keyword `Fixture.groupsTabUsers.keywordKolomPertama` terpotong menjadi 1 karakter pertama, tanpa tekan Enter
9. Verifikasi icon (✕) tampil di dalam input
10. Verifikasi tabel belum tersaring
11. Tekan Enter
12. Verifikasi sedikitnya satu baris tampil
13. Verifikasi tabel tersaring sesuai keyword
14. Klik icon (✕) di dalam input
15. Verifikasi input Search kosong
16. Verifikasi input Search tetap terbuka dan fokus
17. Verifikasi tabel tetap menampilkan hasil search terakhir
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali ke semua data
20. Ketik keyword `Fixture.groupsTabUsers.keywordKolomPertama` dengan dua spasi sebelum dan sesudah keyword, tekan Enter
21. Verifikasi sedikitnya satu baris tampil
22. Verifikasi baris yang tampil sama dengan hasil keyword tanpa spasi tepi (query di-trim saat Enter)
23. Verifikasi isi input di layar tetap seperti yang diketik
24. Ganti isi kotak search dengan `Fixture.groupsTabUsers.keywordKolomPertama`, tekan Enter
25. Klik icon (←) pada kotak Search
26. Verifikasi input Search tertutup
27. Verifikasi keyword dikosongkan
28. Verifikasi tabel langsung reset

### TC-583: Temporary Until tidak menghasilkan match

29. Tampilkan kolom Temporary Until via Column Visibility
30. Salin nilai Temporary Until yang tampil pada baris pertama
31. Ketik Search nilai Temporary Until yang disalin, tekan Enter
32. Verifikasi empty state dengan ilustrasi, title "No results found", dan body "Try adjusting your search or filter."
33. Verifikasi kolom Temporary Until tidak dapat disaring lewat Search (tidak ada baris yang cocok)
34. Klik `(←)` pada kotak Search

### TC-584: Search pada kolom Email yang di-hide

35. Hide kolom Email via Column Visibility
36. Ketik Search `Fixture.groupsTabUsers.emailUnik`, tekan Enter
37. Verifikasi empty state dengan ilustrasi, title "No results found", dan body "Try adjusting your search or filter." (baris tidak ditemukan lewat nilai Email karena kolom yang di-hide dikecualikan dari cakupan search)
38. Unhide kolom Email via Column Visibility
39. Ganti isi kotak search dengan `Fixture.groupsTabUsers.emailUnik`, tekan Enter
40. Verifikasi baris yang cocok dengan nilai Email ditemukan
41. Klik `(←)` pada kotak Search

### TC-675: Email tidak ada di Filter Panel

42. Klik icon Filter
43. Verifikasi Filter Panel tidak memuat field Email
44. Tutup Filter Panel

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menampilkan kolom Temporary Until pada TC-583 (TC tidak menulis langkah ini; kolom curated tidak tampil default, lihat Temuan untuk QA), `(←)` pada kotak Search di akhir TC-583 dan TC-584 (menutup Search dan mereset tabel), menutup Filter Panel di akhir spec, dan ganti isi kotak search sebelum klik `(←)` pada TC-572.
- Verifikasi "sedikitnya satu baris tampil" (langkah 12 dan 21) ditambahkan sebagai anchor positif sebelum asersi universal hasil Search (8b butir 2; S-03).
- Spec memiliki 44 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Search Tab Users pada dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan TC-572 sendiri memuat 25 langkah karena satu TC menguji siklus input Search (buka, ketik, Enter, hapus, trim, tutup).
- Kolom Email dalam keadaan tampil di akhir spec (langkah unhide TC-584); kolom Temporary Until yang ditampilkan dipulihkan lewat hook `after` (hapus preferensi kolom).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-572 menulis "placeholder sesuai konvensi platform" tanpa teks; spec memverifikasi placeholder tanpa teks eksplisit sampai TC menyebutnya. Langkah 5 TC-572 "keyword 1 karakter lalu lanjutkan tanpa Enter" dibaca sebagai mengetik 1 karakter dan tidak menekan Enter.
  - TC-583 langkah 3 menyalin nilai Temporary Until yang "tampil" tanpa precondition kolom Temporary Until ditampilkan; spec menambah langkah penghubung menampilkan kolom itu.
  - TC-584 tidak menyebut apakah Hide/Unhide lewat Column Visibility perlu [Save]; spec mengikuti teks TC.
  - TC-675 tidak punya Expected untuk "Email searchable"; judul TC itu dicakup TC-574 (spec 162) dan TC-584.
