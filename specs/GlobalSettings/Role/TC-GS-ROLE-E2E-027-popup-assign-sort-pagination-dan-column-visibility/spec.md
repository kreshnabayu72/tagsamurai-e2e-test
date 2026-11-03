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
- State yang diubah dan dipulihkan: konfigurasi kolom Popup Assign diubah di TC-GS-ROLE-76 dan TC-GS-ROLE-317, dikembalikan ke default lewat `[Reset to Default]` lalu `[Save]` (langkah 18 sampai 20 dan langkah 64 sampai 66), hook `after` sebagai cadangan; pemulihan lewat langkah UI diterima untuk spec draft.
- Kemampuan teknis: membaca urutan nilai tiap kolom pada halaman aktif; membaca counter seleksi dan jumlah baris halaman; Popup Setup Column picker; membaca dan menghapus preferensi kolom Popup Assign di penyimpanan browser (pemulihan konfigurasi kolom). Locator trigger Column Visibility (⋯) di header kolom Actions tabel picker belum dipetakan (FE follow-up, lihat Notes).

Sort kolom Popup Assign (tiga klik berturut-turut per header; langkah 30 sampai 35):

| Kolom | Klik 1 | Klik 2 | Klik 3 |
|---|---|---|---|
| Name | A-Z | Z-A | default (Name A-Z) |
| Email | A-Z | Z-A | default (Name A-Z) |
| Position | A-Z | Z-A | default (Name A-Z) |
| Division | A-Z | Z-A | default (Name A-Z) |
| Status | A-Z (Active di atas) | Z-A (Inactive, Maya Anggraini di atas) | default (Name A-Z) |

Sort kolom Curated Popup Assign setelah diaktifkan (tiga klik berturut-turut per header; langkah 46 sampai 61):

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
12. Klik Filter
13. Verifikasi field Filter Activation Status tersedia di Filter Panel (kolom tampil)
14. Verifikasi field Filter Temporary User tersedia di Filter Panel
15. Verifikasi field Filter Temporary Until tersedia di Filter Panel
16. Verifikasi field Filter Region tersedia di Filter Panel
17. Tutup Filter Panel dengan Esc
18. Buka Popup Setup Column lewat trigger Column Visibility (⋯) di header kolom Actions tabel picker lalu `Setup Column...`
19. Klik `[Reset to Default]`
20. Klik `[Save]`
21. Verifikasi kolom tabel picker berurutan `Checkbox`, `Name`, `Email`, `Position`, `Division`, `Status`
22. Klik Filter
23. Verifikasi field Filter Activation Status tersedia di Filter Panel
24. Verifikasi field Filter Temporary User tersedia di Filter Panel
25. Verifikasi field Filter Temporary Until tersedia di Filter Panel
26. Verifikasi field Filter Region tersedia di Filter Panel
27. Tutup Filter Panel dengan Esc

### TC-GS-ROLE-293: Sort kolom Popup Assign

28. Centang baris Ahmad Fauzan (`ahmad.fz@client.com`)
29. Verifikasi counter `1 user selected`
30. Untuk setiap kolom pada tabel Prerequisites "Sort kolom Popup Assign" (langkah 30 sampai 35), klik header kolom
31. Verifikasi susunan baris sesuai kolom "Klik 1" pada tabel
32. Klik header kolom yang sama
33. Verifikasi susunan baris sesuai kolom "Klik 2" pada tabel
34. Klik header kolom yang sama
35. Verifikasi susunan baris sesuai kolom "Klik 3" pada tabel
36. Verifikasi counter `1 user selected` (seleksi checkbox tidak berubah oleh sort)
37. Hapus centang baris Ahmad Fauzan (`ahmad.fz@client.com`)

### TC-GS-ROLE-317: Sort kolom Curated Popup Assign setelah diaktifkan lewat Setup Column

38. Buka Popup Setup Column lewat trigger Column Visibility (⋯) di header kolom Actions tabel picker lalu `Setup Column...`
39. Centang kolom Activation Status
40. Centang kolom Temporary User
41. Centang kolom Temporary Until
42. Centang kolom TAG
43. Klik `[Save]`
44. Centang baris Ahmad Fauzan (`ahmad.fz@client.com`)
45. Verifikasi counter `1 user selected`
46. Untuk setiap kolom `Activation Status` lalu `Temporary User` (langkah 46 sampai 51, parameter di tabel Prerequisites "Sort kolom Curated"), klik header kolom
47. Verifikasi susunan baris sesuai kolom "Klik 1" pada tabel
48. Klik header kolom yang sama
49. Verifikasi susunan baris sesuai kolom "Klik 2" pada tabel
50. Klik header kolom yang sama
51. Verifikasi susunan baris sesuai kolom "Klik 3" pada tabel
52. Untuk setiap kolom `Temporary Until` lalu `TAG` (langkah 52 sampai 61, parameter di tabel Prerequisites "Sort kolom Curated"), klik header kolom
53. Verifikasi susunan baris sesuai kolom "Klik 1" pada tabel
54. Pindah ke halaman terakhir picker
55. Verifikasi baris kosong (`—`) berada di akhir
56. Pindah ke halaman pertama picker
57. Klik header kolom yang sama
58. Verifikasi susunan baris sesuai kolom "Klik 2" pada tabel
59. Verifikasi baris kosong (`—`) berada di awal
60. Klik header kolom yang sama
61. Verifikasi susunan baris sesuai kolom "Klik 3" pada tabel
62. Verifikasi counter `1 user selected` (seleksi checkbox tidak berubah oleh sort)
63. Hapus centang baris Ahmad Fauzan (`ahmad.fz@client.com`)
64. Buka Popup Setup Column lewat trigger Column Visibility (⋯) di header kolom Actions tabel picker lalu `Setup Column...`
65. Klik `[Reset to Default]`
66. Klik `[Save]`

### TC-GS-ROLE-75: Pagination Popup Assign

67. Verifikasi halaman 1 berisi 10 baris
68. Verifikasi opsi page size `10`, `25`, `50`, dan `100`
69. Ubah page size ke 25
70. Ubah page size ke 10
71. Klik halaman 2
72. Verifikasi halaman 2 aktif dan memuat baris yang berbeda dari halaman 1
73. Centang satu user di halaman 2 (baris pertama halaman 2)
74. Verifikasi counter `1 user selected`
75. Klik halaman 1
76. Verifikasi counter tetap `1 user selected`
77. Klik checkbox Select All di header picker
78. Verifikasi 10 baris halaman 1 checked
79. Verifikasi counter `11 users selected`
80. Klik halaman 2
81. Verifikasi user yang dicentang di langkah 73 tetap checked
82. Tekan Esc untuk menutup Popup Assign

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber diubah: TC-GS-ROLE-76 (Setup Column dan Filter, dikembalikan ke default) di awal, TC-GS-ROLE-293 (sort kolom default) sesudahnya, TC-GS-ROLE-317 (sort kolom Curated setelah diaktifkan) sesudahnya, dan TC-GS-ROLE-75 (pagination dengan seleksi) terakhir karena seleksinya meninggalkan 11 centang yang tidak perlu dibersihkan sebelum spec lain (popup tidak pernah di-submit; hook `beforeEach` berikutnya mereset layar). TC-GS-ROLE-317 dijalankan setelah TC-GS-ROLE-293 karena TC-GS-ROLE-293 membutuhkan enam kolom default.
- Langkah 30 sampai 35 diulang per kolom pada tabel Prerequisites (5 iterasi). Langkah 46 sampai 51 (2 iterasi: Activation Status, Temporary User) dan langkah 52 sampai 61 (2 iterasi: Temporary Until, TAG) diulang pada tabel sort kolom Curated; tabel dipisah menjadi dua blok supaya tidak ada langkah bersyarat untuk kolom tanpa nilai kosong. Jumlah langkah dengan ekspansi 122: langkah 1 sampai 29 (29), blok sort 5 x 6 (30), langkah 36 dan 37 (2), langkah 38 sampai 45 (8), blok Curated 2 x 6 (12) dan 2 x 10 (20), langkah 62 sampai 82 (21).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): langkah 12 dan 17 (membuka dan menutup Filter Panel untuk mengamati Expected e TC-GS-ROLE-76 saat kolom tampil), langkah 27 (menutup Filter Panel), langkah 28 (centang satu baris untuk mengamati Expected f TC-GS-ROLE-293), langkah 37 (hapus centang supaya seleksi TC-GS-ROLE-317 dimulai kosong), langkah 44 dan 63 (centang dan hapus centang baris untuk mengamati Expected e TC-GS-ROLE-317), langkah 18 sampai 20 dan 64 sampai 66 (`[Reset to Default]` lalu `[Save]` mengembalikan konfigurasi kolom; TC-GS-ROLE-76 Langkah Uji 5 dan pemulihan setelah TC-GS-ROLE-317). Baris Ahmad Fauzan (`ahmad.fz@client.com`) berada di halaman 1 pada urutan default. Langkah 69 dan 70 (ubah page size ke 25 lalu kembali ke 10) dijalankan sesuai TC tanpa `Verifikasi` karena TC tidak menyebut hasilnya. Langkah 82 (Esc menutup Popup Assign, tanpa Verifikasi) menutup popup di akhir spec; seleksi 11 user tidak di-submit.
- Spec melewati sekitar 35 langkah (122 langkah dengan ekspansi) karena sort lima kolom default dan empat kolom Curated memakai blok identik dengan tiga klik per kolom, ditambah blok Setup Column dan Filter. Semua blok satu kelas harness (fungsional), satu popup dan satu dataset; blok Column Visibility, sort, dan pagination memeriksa permukaan berbeda pada popup yang sama dan tidak bergantung pada hasil blok lain (seleksi blok sort dibersihkan di langkah 37 dan 63, konfigurasi kolom dikembalikan ke default di langkah 18 sampai 20 dan 64 sampai 66, sehingga blok berikutnya dimulai dari seleksi kosong dan enam kolom default), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Alasan pemisahan spec 025, 026, dan 027: ekspansi gabungan ±226 langkah (53, 51, dan 122) jauh melewati sekitar 35 langkah, sehingga tiap permukaan Popup Assign menjadi spec sendiri (Search di 025, Filter Panel di 026, Column Visibility, sort, dan pagination di 027); ketiganya satu kelas harness dan tidak bergantung pada hasil spec lain.
- Pembagian TC lintas spec: TC-GS-ROLE-51, 52, 53, 77 ada di spec 023; TC-GS-ROLE-54 sampai 57 ada di spec 024; TC-GS-ROLE-69 sampai 72 dan 316 ada di spec 025; TC-GS-ROLE-73, 74 ada di spec 026.
- Langkah penghubung (S-14, bukan dari TC sumber): pada iterasi kolom `Temporary Until` dan `TAG`, langkah 54 memindahkan picker ke halaman terakhir sebelum `Verifikasi` baris kosong (`—`) berada di akhir, dan langkah 56 memindahkannya kembali ke halaman pertama sebelum klik header berikutnya sehingga `Verifikasi` baris kosong berada di awal dibaca pada halaman pertama.
- Temuan untuk QA:
  - TC-GS-ROLE-293 Expected f ("seleksi checkbox tidak berubah saat sort") tidak punya langkah yang memilih baris; spec menambah langkah 28 dan 29 sebagai precondition seleksi.
  - TC-GS-ROLE-75 langkah 2 (page size 25) dan langkah 3 (kembali ke 10) tidak punya Expected eksplisit selain "opsi 10/25/50/100"; tidak ada `Verifikasi` untuk jumlah baris pada page size 25.
  - TC-GS-ROLE-75 Expected c ("Centang di halaman 2 tetap") dan d ("centang di halaman 2 tetap") diasersi lewat counter (langkah 76, 79) dan langkah 81 (user halaman 2 tetap checked); langkah 80 dan 81 adalah observasi tambahan untuk klausa d.
  - TC-GS-ROLE-75 precondition "Pool picker berisi >10 user (Pre-setup #11 + #17)" merujuk Pre-setup #17 (volume data) yang ditulis untuk Detail dan Tab Total Control; spec memakai pool Pre-setup #11 dan #18 yang lebih dari 10 user.
  - TC-GS-ROLE-76 Langkah Uji 6 ("screening field") dijalankan sesudah Reset to Default; spec mengasersi empat field yang disebut Expected e (Activation Status, Temporary User, Temporary Until, Region). Expected e ("saat kolomnya tampil maupun tidak") tidak punya langkah uji saat kolom tampil; spec menambah langkah 12 sampai 17 (field Filter diasersi setelah Activation Status dan TAG ditampilkan) di samping langkah 22 sampai 27 (setelah Reset to Default). Pada langkah 13 sampai 16 hanya kolom Activation Status yang tampil dari empat field Filter; kolom Temporary User, Temporary Until, dan Region tetap tidak tampil karena Langkah Uji TC hanya mencentang Activation Status dan TAG.
  - TC-GS-ROLE-317 Langkah Uji 2 mengaktifkan empat kolom (tanpa Region) sedangkan TC-GS-ROLE-76 Expected b mendaftar Region sebagai Custom Field aktif; Region disediakan tim FE sebagai Custom Field aktif.
  - TC-GS-ROLE-317 Expected a sampai d tidak menyebut nilai konkret baris; spec mengasersi arah urutan pada kolom yang diklik dan data uji dua nilai distinct disediakan tim FE (Prerequisites).
  - FE follow-up: locator trigger Column Visibility (⋯) di header kolom Actions tabel picker belum ada di Page Object; langkah 3, 18, 38, dan 64 memakai deskripsi UI sampai tim FE memetakannya.
