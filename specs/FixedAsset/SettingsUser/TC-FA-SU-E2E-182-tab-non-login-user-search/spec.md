---
id: TC-FA-SU-E2E-182-tab-non-login-user-search
title: "Tab Non-Login User: Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-542
  - TC-FA-SU-543
  - TC-FA-SU-544
  - TC-FA-SU-1058
coverage:
  web: automated
---

# Tab Non-Login User: Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Data Dinamis: tidak ada.
- Nilai kolom Last Update `02/07/26` (TC-FA-SU-543) adalah nilai salah satu dari lima baris Pre-setup #26; baris pemiliknya tidak tertulis di TC (lihat Temuan untuk QA).
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.
- Varian TC-FA-SU-1058 (Pre-setup #47, `FaUserNL`): Budi Santoso dengan Non-Login User Printer Lantai 5 ber-Temporary User `Yes` dan Temporary Until `31/12/26`; empat Non-Login User lain Temporary User `No`. Varian ini disiapkan lewat seed API di hook `before` dan dipulihkan ke Pre-setup #26 di hook `after`; Client dan akun aktor varian tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).

## Test Steps

1. Ketik Search `Budi Santoso` pada User List, tekan Enter, lalu buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-542: Siklus interaksi Search

2. Hover icon Search
3. Verifikasi tooltip `Search`
4. Klik icon Search
5. Verifikasi input Search melebar
6. Verifikasi kursor fokus di input Search
7. Verifikasi placeholder `Search name, email, or employee ID...`
8. Ketik karakter pertama `P` pada kotak Search tanpa menekan Enter
9. Verifikasi icon ✕ tampil di kanan input
10. Verifikasi tabel belum tersaring (kelima baris tampil)
11. Ketik sisa `rinter` pada kotak Search, tekan Enter
12. Verifikasi tabel tersaring menjadi `Printer Lantai 5`
13. Klik ✕ pada kotak Search
14. Verifikasi input kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi kursor fokus di input Search
17. Verifikasi tabel tetap menampilkan hasil search terakhir (`Printer Lantai 5`)
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali ke semua baris (kelima baris)
20. Ketik Search `Printer`, tekan Enter
21. Klik `←` pada kotak Search
22. Verifikasi search bar menutup
23. Verifikasi keyword dikosongkan
24. Verifikasi tabel langsung kembali ke semua baris (kelima baris)
25. Ketik Search `  Printer  ` (spasi awal dan akhir), tekan Enter
26. Verifikasi hasil sama dengan `Printer` tanpa spasi (`Printer Lantai 5`)
27. Verifikasi isi input tidak berubah (spasi awal dan akhir tetap ada)

### TC-FA-SU-543: Guard kolom non-searchable (Last Update)

28. Klik `←` pada kotak Search
29. Verifikasi kolom Last Update menampilkan nilai `02/07/26` pada salah satu baris tabel
30. Ketik Search `02/07/26` (nilai kolom Last Update), tekan Enter
31. Verifikasi `02/07/26` tidak mencocokkan baris melalui Search; empty state `No results found` tampil

### TC-FA-SU-544: Search terikat visibilitas kolom Name

32. Klik `←` pada kotak Search
33. Ketik Search `Printer`, tekan Enter
34. Verifikasi sebelum hide: keyword `Printer` menyisakan `Printer Lantai 5`
35. Klik header kolom Actions (⋯), lalu hilangkan centang Name
36. Ganti isi kotak search dengan `Printer`, tekan Enter
37. Verifikasi setelah kolom Name di-hide: keyword yang sama menyisakan `Printer Lantai 5` (kolom tersembunyi tidak dicari; kolom lain yang tampil tetap dicari)
38. Klik header kolom Actions (⋯), lalu centang kembali Name
39. Ganti isi kotak search dengan `Printer`, tekan Enter
40. Verifikasi setelah kolom Name di-unhide: hasil kembali `Printer Lantai 5`

### TC-FA-SU-1058: Guard kolom non-searchable (Temporary Until)

41. Klik `←` pada kotak Search
42. Klik header kolom Actions (⋯), lalu centang kolom curated Temporary Until
43. Verifikasi kolom Temporary Until tampil dengan nilai `31/12/26` pada baris `Printer Lantai 5`
44. Ketik Search `31/12/26` (nilai kolom Temporary Until), tekan Enter
45. Verifikasi `31/12/26` tidak mencocokkan baris melalui Search; empty state `No results found` tampil

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso; `←` pada kotak Search sebelum tiap TC (S-09). TC-FA-SU-1058 ditaruh terakhir karena memakai varian data Pre-setup #47.
- Langkah penghubung Search (R-16, bagian 8b butir 9 dan 13): langkah 1 mengetik Search `Budi Santoso` pada User List sebelum membuka Detail, karena User List memuat 3 halaman sehingga spec tidak mengandalkan posisi baris di halaman.
- Jumlah langkah: 45 tertulis, 45 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (45 langkah). Seluruh blok berada pada satu surface (satu tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Search nilai kolom Date non-searchable (langkah 30 dan 44) didahului Verifikasi nilai Date tampil sebagai anchor positif (langkah 29 untuk `02/07/26`, langkah 43 untuk `31/12/26`; S-03, bagian 8b butir 15 b); kedua nilai tercatat di Prerequisites.
- Temuan untuk QA:
  - TC-FA-SU-543 tidak menyebut baris pemilik nilai Last Update `02/07/26`; spec memverifikasi nilai itu tampil pada salah satu baris sebelum Search (anchor positif sebelum absence, 8b butir 2) tanpa menyebut baris (S-15).
  - TC-FA-SU-1058 langkah 1 menyuruh mencentang kolom curated Temporary Until lewat Column Visibility, tetapi TC-FA-SU-559 menyatakan kolom curated tidak tampil sebagai baris overlay Column Visibility (hanya lewat Setup Column); spec mengikuti TC-FA-SU-1058 dan perlu dikoreksi pemilik TC bila yang benar lewat Setup Column.
  - TC-FA-SU-1058 memakai varian Pre-setup #47 (`FaUserNL`) yang bertentangan dengan Pre-setup #26 (Temporary User `No` untuk Printer Lantai 5); Client dan akun login untuk varian itu tidak tertulis, sehingga spec menyiapkannya lewat seed API dan memulihkannya.
  - TC-FA-SU-544 Expected b memberi hasil `Printer Lantai 5` setelah kolom Name disembunyikan; hasil ini bergantung pada kolom Email Printer Lantai 5 yang memuat kata `printer`, yang tidak tertulis di Pre-setup #26.
