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
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role. Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Syarat data Temporary Until (TC-583): baris pertama tabel Warehouse A bernilai tanggal pada kolom Temporary Until (bukan `—`); jaminan data ini disediakan tim FE (lihat Temuan untuk QA).
- Fixture (berkas baru `groupsTabUsers`, ditetapkan tim FE): `Fixture.groupsTabUsers.keywordKolomPertama` (potongan nilai kolom pertama tabel yang mencocokkan sedikitnya satu baris dan tidak semua baris), `Fixture.groupsTabUsers.emailUnik` (nilai unik kolom Email satu user).
- Kemampuan teknis (disediakan tim FE): menyalin nilai sel tabel ke langkah berikutnya (nilai Temporary Until baris pertama); menghapus preferensi kolom Setup Column di browser (pemulihan kolom di hook `after`).
- State yang diubah spec: kolom Email di-hide dan kolom Temporary Until ditampilkan lewat Column Visibility; dipulihkan lewat langkah penghubung di akhir spec dan hook `after` (hapus preferensi kolom).

## Test Steps

### TC-572: Interaksi Search

1. Ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
2. Catat nama baris halaman 1 tabel (semua data, belum tersaring)
3. Hover icon Search pada toolbar
4. Verifikasi tooltip Search tampil
5. Klik icon Search
6. Verifikasi input Search melebar
7. Verifikasi input Search auto-focus
8. Verifikasi placeholder input Search sesuai konvensi platform
9. Ketik keyword `Fixture.groupsTabUsers.keywordKolomPertama` terpotong menjadi 1 karakter pertama, tanpa tekan Enter
10. Verifikasi icon (✕) tampil di dalam input
11. Verifikasi nama baris halaman 1 tabel sama dengan catatan langkah 2 (tabel belum tersaring)
12. Tekan Enter
13. Verifikasi sedikitnya satu baris tampil
14. Verifikasi tabel tersaring sesuai keyword
15. Catat nama baris halaman 1 tabel (hasil search terakhir)
16. Klik icon (✕) di dalam input
17. Verifikasi input Search kosong
18. Verifikasi input Search tetap terbuka dan fokus
19. Verifikasi nama baris halaman 1 tabel sama dengan catatan langkah 15 (tabel tetap menampilkan hasil search terakhir)
20. Tekan Enter pada input kosong
21. Verifikasi nama baris halaman 1 tabel sama dengan catatan langkah 2 (tabel kembali ke semua data)
22. Ketik keyword `Fixture.groupsTabUsers.keywordKolomPertama` dengan dua spasi sebelum dan sesudah keyword, tekan Enter
23. Verifikasi sedikitnya satu baris tampil
24. Catat nama baris halaman 1 tabel (hasil keyword dengan spasi tepi)
25. Verifikasi isi input di layar tetap seperti yang diketik
26. Ganti isi kotak search dengan `Fixture.groupsTabUsers.keywordKolomPertama`, tekan Enter
27. Verifikasi nama baris halaman 1 tabel sama dengan catatan langkah 24 (query di-trim saat Enter, hasil sama dengan keyword tanpa spasi tepi)
28. Klik icon (←) pada kotak Search
29. Verifikasi input Search tertutup
30. Verifikasi keyword dikosongkan
31. Verifikasi nama baris halaman 1 tabel sama dengan catatan langkah 2 (tabel langsung reset)

### TC-583: Temporary Until tidak menghasilkan match

32. Tampilkan kolom Temporary Until via Column Visibility
33. Salin nilai Temporary Until yang tampil pada baris pertama
34. Ketik Search nilai Temporary Until yang disalin, tekan Enter
35. Verifikasi empty state dengan ilustrasi, title "No results found", dan body "Try adjusting your search or filter."
36. Verifikasi kolom Temporary Until tidak dapat disaring lewat Search (tidak ada baris yang cocok)
37. Klik `(←)` pada kotak Search

### TC-584: Search pada kolom Email yang di-hide

38. Hide kolom Email via Column Visibility
39. Ketik Search `Fixture.groupsTabUsers.emailUnik`, tekan Enter
40. Verifikasi empty state dengan ilustrasi, title "No results found", dan body "Try adjusting your search or filter." (baris tidak ditemukan lewat nilai Email karena kolom yang di-hide dikecualikan dari cakupan search)
41. Unhide kolom Email via Column Visibility
42. Ganti isi kotak search dengan `Fixture.groupsTabUsers.emailUnik`, tekan Enter
43. Verifikasi baris yang cocok dengan nilai Email ditemukan
44. Klik `(←)` pada kotak Search

### TC-675: Email tidak ada di Filter Panel

45. Klik icon Filter
46. Verifikasi Filter Panel tidak memuat field Email
47. Tutup Filter Panel

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menampilkan kolom Temporary Until pada TC-583 (TC tidak menulis langkah ini; kolom curated tidak tampil default, lihat Temuan untuk QA), `(←)` pada kotak Search di akhir TC-583 dan TC-584 (menutup Search dan mereset tabel), menutup Filter Panel di akhir spec, dan ganti isi kotak search sebelum klik `(←)` pada TC-572.
- Asersi pembanding tabel (langkah 11, 19, 21, 27, 31) memakai langkah `Catat nama baris halaman 1 tabel` (langkah 2, 15, 24) sebagai baseline (S-12). Langkah 25 (isi input tetap seperti diketik) dan langkah 26-27 (hasil tanpa spasi tepi sama dengan hasil dengan spasi tepi) berurutan sehingga baseline hasil dengan spasi tepi dicatat lebih dulu; urutan Expected TC-572 sedikit berbeda dari TC.
- Verifikasi "sedikitnya satu baris tampil" (langkah 13 dan 23) ditambahkan sebagai anchor positif sebelum asersi universal hasil Search (8b butir 2; S-03).
- Spec memiliki 47 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Search Tab Users pada dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan TC-572 sendiri memuat 31 langkah karena satu TC menguji siklus input Search (buka, ketik, Enter, hapus, trim, tutup).
- Kolom Email dalam keadaan tampil di akhir spec (langkah unhide TC-584); kolom Temporary Until yang ditampilkan dipulihkan lewat hook `after` (hapus preferensi kolom).
- Baris `Warehouse A` dicari lewat Search sebelum klik angka Total User (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; Refresh F5 membuang Search sehingga Search diketik ulang). Langkah Search digabung ke langkah klik angka dan dihitung langkah penghubung (S-03, S-14, R-16).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-572 menulis "placeholder sesuai konvensi platform" tanpa teks; spec memverifikasi placeholder tanpa teks eksplisit sampai TC menyebutnya. Langkah 5 TC-572 "keyword 1 karakter lalu lanjutkan tanpa Enter" dibaca sebagai mengetik 1 karakter dan tidak menekan Enter.
  - TC-583 tidak menjamin baris pertama Warehouse A punya nilai Temporary Until; bila selnya `—`, asersi tidak bermakna. Spec menuliskan syarat nilai di Prerequisites sebagai jaminan data yang disediakan tim FE.
  - TC-583 langkah 3 menyalin nilai Temporary Until yang "tampil" tanpa precondition kolom Temporary Until ditampilkan; spec menambah langkah penghubung menampilkan kolom itu.
  - TC-584 tidak menyebut apakah Hide/Unhide lewat Column Visibility perlu [Save]; spec mengikuti teks TC.
  - TC-675 tidak punya Expected untuk "Email searchable"; judul TC itu dicakup TC-574 (spec 162) dan TC-584.
