---
id: TC-GS-ROLE-E2E-027-popup-assign-sort-pagination-dan-column-visibility
title: "Popup Assign: Column Visibility, Sort Kolom, dan Pagination dengan Retensi Seleksi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-75
  - TC-GS-ROLE-76
  - TC-GS-ROLE-293
  - TC-GS-ROLE-317
coverage:
  web: automated
---

# Popup Assign: Column Visibility, Sort Kolom, dan Pagination dengan Retensi Seleksi

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data; seleksi checkbox hanya state popup dan popup tidak pernah di-submit.
- Akun: Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD` (Pre-setup #1). Login dan navigasi dilakukan sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): kandidat picker Pre-setup #11 (termasuk Maya Anggraini, Inactive, Staff, IT; Ahmad Fauzan `ahmad.fz@client.com` dan `ahmad.fauzan@client.com`) dan Pre-setup #18. Pool picker lebih dari 10 user (N total dari seeding, 11 atau lebih) sehingga halaman 2 ada dan halaman 1 berisi 10 baris. Pool memuat sedikitnya dua nilai distinct pada kolom Name, Email, Position, Division, dan Status (Status Active dan Inactive).
- Data uji kolom Curated untuk TC-GS-ROLE-317 (disediakan tim FE, sedikitnya dua nilai distinct per kolom yang di-sort): Activation Status `Activated` dan `Pending Activation` (Rudi Hartono, Pre-setup #11); Temporary User `Yes` dan `No`; Temporary Until dua tanggal berbeda serta baris kosong (`—`); TAG dua kode berbeda (salah satunya `TG-00877`) serta baris kosong (`—`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: membuka Global Settings > Role & Permission > Tab Total Control.
- Suite berjalan serial (`parallel: false`).
- State yang diubah dan dipulihkan: konfigurasi kolom Popup Assign diubah di TC-GS-ROLE-76 dan TC-GS-ROLE-317, dikembalikan ke default lewat `[Reset to Default]` lalu `[Save]` (langkah 12 sampai 14 dan langkah 56 sampai 58), hook `after` sebagai cadangan.
- Kemampuan teknis: membaca urutan nilai tiap kolom pada halaman aktif; membaca counter seleksi dan jumlah baris halaman; Popup Setup Column picker. Locator trigger Column Visibility (⋯) di header kolom Actions tabel picker belum dipetakan (FE follow-up, lihat Notes).

Sort kolom Popup Assign (tiga klik berturut-turut per header; langkah 24 sampai 29):

| Kolom | Klik 1 | Klik 2 | Klik 3 |
|---|---|---|---|
| Name | A-Z | Z-A | default (Name A-Z) |
| Email | A-Z | Z-A | default (Name A-Z) |
| Position | A-Z | Z-A | default (Name A-Z) |
| Division | A-Z | Z-A | default (Name A-Z) |
| Status | A-Z (Active di atas) | Z-A (Inactive, Maya Anggraini di atas) | default (Name A-Z) |

Sort kolom Curated Popup Assign setelah diaktifkan (tiga klik berturut-turut per header; langkah 40 sampai 53):

| Kolom | Klik 1 | Klik 2 | Klik 3 | Nilai kosong (`—`) |
|---|---|---|---|---|
| Activation Status | A-Z | Z-A | default (Name A-Z) | tidak ada |
| Temporary User | A-Z | Z-A | default (Name A-Z) | tidak ada |
| Temporary Until | Oldest First | Newest First | default (Name A-Z) | di akhir pada klik 1 (ascending), di awal pada klik 2 (descending) |
| TAG | A-Z | Z-A | default (Name A-Z) | di akhir pada klik 1 (ascending), di awal pada klik 2 (descending) |

## Test Steps

1. Klik `[+ Assign]`

### TC-GS-ROLE-76: Column Visibility / Setup Column pada Popup Assign

2. Verifikasi header tabel picker memiliki kolom Actions dengan trigger Column Visibility (⋯)
3. Buka Popup Setup Column lewat trigger Column Visibility (⋯) di header kolom Actions tabel picker lalu `Setup Column...`
4. Verifikasi popup Setup Column mendaftar `Name`, `Email`, `Position`, `Division`, dan `Status` dalam keadaan tercentang
5. Verifikasi popup Setup Column mendaftar `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan `Region` dalam keadaan tidak tercentang
6. Verifikasi popup Setup Column tidak mencantumkan kolom `Checkbox` dan `Actions`
7. Centang kolom Activation Status
8. Centang kolom TAG
9. Klik `[Save]`
10. Verifikasi kolom Activation Status tampil di tabel picker
11. Verifikasi kolom TAG tampil di tabel picker
12. Buka Popup Setup Column lewat trigger Column Visibility (⋯) di header kolom Actions tabel picker lalu `Setup Column...`
13. Klik `[Reset to Default]`
14. Klik `[Save]`
15. Verifikasi kolom tabel picker berurutan `Checkbox`, `Name`, `Email`, `Position`, `Division`, `Status`
16. Klik Filter
17. Verifikasi field Filter Activation Status tersedia di Filter Panel
18. Verifikasi field Filter Temporary User tersedia di Filter Panel
19. Verifikasi field Filter Temporary Until tersedia di Filter Panel
20. Verifikasi field Filter Region tersedia di Filter Panel
21. Tutup Filter Panel dengan Esc

### TC-GS-ROLE-293: Sort kolom Popup Assign

22. Centang baris Ahmad Fauzan (`ahmad.fz@client.com`)
23. Verifikasi counter `1 user selected`
24. Untuk setiap kolom pada tabel Prerequisites "Sort kolom Popup Assign" (langkah 24 sampai 29), klik header kolom
25. Verifikasi susunan baris sesuai kolom "Klik 1" pada tabel
26. Klik header kolom yang sama
27. Verifikasi susunan baris sesuai kolom "Klik 2" pada tabel
28. Klik header kolom yang sama
29. Verifikasi susunan baris sesuai kolom "Klik 3" pada tabel
30. Verifikasi counter `1 user selected` (seleksi checkbox tidak berubah oleh sort)
31. Hapus centang baris Ahmad Fauzan (`ahmad.fz@client.com`)

### TC-GS-ROLE-317: Sort kolom Curated Popup Assign setelah diaktifkan lewat Setup Column

32. Buka Popup Setup Column lewat trigger Column Visibility (⋯) di header kolom Actions tabel picker lalu `Setup Column...`
33. Centang kolom Activation Status
34. Centang kolom Temporary User
35. Centang kolom Temporary Until
36. Centang kolom TAG
37. Klik `[Save]`
38. Centang baris Ahmad Fauzan (`ahmad.fz@client.com`)
39. Verifikasi counter `1 user selected`
40. Untuk setiap kolom `Activation Status` lalu `Temporary User` (langkah 40 sampai 45, parameter di tabel Prerequisites "Sort kolom Curated"), klik header kolom
41. Verifikasi susunan baris sesuai kolom "Klik 1" pada tabel
42. Klik header kolom yang sama
43. Verifikasi susunan baris sesuai kolom "Klik 2" pada tabel
44. Klik header kolom yang sama
45. Verifikasi susunan baris sesuai kolom "Klik 3" pada tabel
46. Untuk setiap kolom `Temporary Until` lalu `TAG` (langkah 46 sampai 53, parameter di tabel Prerequisites "Sort kolom Curated"), klik header kolom
47. Verifikasi susunan baris sesuai kolom "Klik 1" pada tabel
48. Verifikasi baris kosong (`—`) berada di akhir
49. Klik header kolom yang sama
50. Verifikasi susunan baris sesuai kolom "Klik 2" pada tabel
51. Verifikasi baris kosong (`—`) berada di awal
52. Klik header kolom yang sama
53. Verifikasi susunan baris sesuai kolom "Klik 3" pada tabel
54. Verifikasi counter `1 user selected` (seleksi checkbox tidak berubah oleh sort)
55. Hapus centang baris Ahmad Fauzan (`ahmad.fz@client.com`)
56. Buka Popup Setup Column lewat trigger Column Visibility (⋯) di header kolom Actions tabel picker lalu `Setup Column...`
57. Klik `[Reset to Default]`
58. Klik `[Save]`

### TC-GS-ROLE-75: Pagination Popup Assign

59. Verifikasi halaman 1 berisi 10 baris
60. Verifikasi opsi page size `10`, `25`, `50`, dan `100`
61. Ubah page size ke 25
62. Ubah page size ke 10
63. Klik halaman 2
64. Verifikasi halaman 2 aktif dan memuat baris yang berbeda dari halaman 1
65. Centang satu user di halaman 2 (baris pertama halaman 2)
66. Verifikasi counter `1 user selected`
67. Klik halaman 1
68. Verifikasi counter tetap `1 user selected`
69. Klik checkbox Select All di header picker
70. Verifikasi 10 baris halaman 1 checked
71. Verifikasi counter `11 users selected`
72. Klik halaman 2
73. Verifikasi user yang dicentang di langkah 65 tetap checked

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber diubah: TC-GS-ROLE-76 (Setup Column dan Filter, dikembalikan ke default) di awal, TC-GS-ROLE-293 (sort kolom default) sesudahnya, TC-GS-ROLE-317 (sort kolom Curated setelah diaktifkan) sesudahnya, dan TC-GS-ROLE-75 (pagination dengan seleksi) terakhir karena seleksinya meninggalkan 11 centang yang tidak perlu dibersihkan sebelum spec lain (popup tidak pernah di-submit; hook `beforeEach` berikutnya mereset layar). TC-GS-ROLE-317 dijalankan setelah TC-GS-ROLE-293 karena TC-GS-ROLE-293 membutuhkan enam kolom default.
- Langkah 24 sampai 29 diulang per kolom pada tabel Prerequisites (5 iterasi). Langkah 40 sampai 45 (2 iterasi: Activation Status, Temporary User) dan langkah 46 sampai 53 (2 iterasi: Temporary Until, TAG) diulang pada tabel sort kolom Curated; tabel dipisah menjadi dua blok supaya tidak ada langkah bersyarat untuk kolom tanpa nilai kosong. Jumlah langkah dengan ekspansi 111: langkah 1 sampai 23 (23), blok sort 5 x 6 (30), langkah 30 dan 31 (2), langkah 32 sampai 39 (8), blok Curated 2 x 6 (12) dan 2 x 8 (16), langkah 54 sampai 73 (20).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): langkah 21 (menutup Filter Panel), langkah 22 (centang satu baris untuk mengamati Expected f TC-GS-ROLE-293), langkah 31 (hapus centang supaya seleksi TC-GS-ROLE-317 dimulai kosong), langkah 38 dan 55 (centang dan hapus centang baris untuk mengamati Expected e TC-GS-ROLE-317), serta langkah 12 sampai 14 dan 56 sampai 58 (`[Reset to Default]` lalu `[Save]` mengembalikan konfigurasi kolom; TC-GS-ROLE-76 Langkah Uji 5 dan pemulihan setelah TC-GS-ROLE-317). Baris Ahmad Fauzan (`ahmad.fz@client.com`) berada di halaman 1 pada urutan default. Langkah 61 dan 62 (ubah page size ke 25 lalu kembali ke 10) dijalankan sesuai TC tanpa `Verifikasi` karena TC tidak menyebut hasilnya.
- Spec melewati sekitar 35 langkah (111 langkah dengan ekspansi) karena sort lima kolom default dan empat kolom Curated memakai blok identik dengan tiga klik per kolom, ditambah blok Setup Column dan Filter. Semua blok satu kelas harness (fungsional), satu popup dan satu dataset; blok Column Visibility, sort, dan pagination memeriksa permukaan berbeda pada popup yang sama dan tidak bergantung pada hasil blok lain (seleksi blok sort dibersihkan di langkah 31 dan 55, konfigurasi kolom dikembalikan ke default di langkah 12 sampai 14 dan 56 sampai 58, sehingga blok berikutnya dimulai dari seleksi kosong dan enam kolom default), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-ROLE-51, 52, 53, 77 ada di spec 023; TC-GS-ROLE-54 sampai 57 ada di spec 024; TC-GS-ROLE-69 sampai 72 dan 316 ada di spec 025; TC-GS-ROLE-73, 74 ada di spec 026.
- Temuan untuk QA:
  - TC-GS-ROLE-293 Expected f ("seleksi checkbox tidak berubah saat sort") tidak punya langkah yang memilih baris; spec menambah langkah 22 dan 23 sebagai precondition seleksi.
  - TC-GS-ROLE-75 langkah 2 (page size 25) dan langkah 3 (kembali ke 10) tidak punya Expected eksplisit selain "opsi 10/25/50/100"; tidak ada `Verifikasi` untuk jumlah baris pada page size 25.
  - TC-GS-ROLE-75 Expected c ("Centang di halaman 2 tetap") dan d ("centang di halaman 2 tetap") diasersi lewat counter (langkah 68, 71) dan langkah 73 (user halaman 2 tetap checked); langkah 72 dan 73 adalah observasi tambahan untuk klausa d.
  - TC-GS-ROLE-75 precondition "Pool picker berisi >10 user (Pre-setup #11 + #17)" merujuk Pre-setup #17 (volume data) yang ditulis untuk Detail dan Tab Total Control; spec memakai pool Pre-setup #11 dan #18 yang lebih dari 10 user.
  - TC-GS-ROLE-76 Langkah Uji 6 ("screening field") dijalankan sesudah Reset to Default; spec mengasersi empat field yang disebut Expected e (Activation Status, Temporary User, Temporary Until, Region). Expected e ("saat kolomnya tampil maupun tidak") tidak punya langkah uji saat kolom tampil; field Filter diasersi hanya saat kolom tidak tampil.
  - TC-GS-ROLE-317 Langkah Uji 2 mengaktifkan empat kolom (tanpa Region) sedangkan TC-GS-ROLE-76 Expected b mendaftar Region sebagai Custom Field aktif; Region disediakan tim FE sebagai Custom Field aktif.
  - TC-GS-ROLE-317 Expected a sampai d tidak menyebut nilai konkret baris; spec mengasersi arah urutan pada kolom yang diklik dan data uji dua nilai distinct disediakan tim FE (Prerequisites).
  - FE follow-up: locator trigger Column Visibility (⋯) di header kolom Actions tabel picker belum ada di Page Object; langkah 3, 12, 32, dan 56 memakai deskripsi UI sampai tim FE memetakannya.
