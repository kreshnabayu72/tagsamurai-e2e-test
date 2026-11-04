---
id: TC-GS-USER-E2E-093-tab-changelog-detail-sort-3-state-pagination-dan-kombinasi
title: "Tab Changelog Detail: Sort 3-State, Pagination, dan Kombinasi Search, Filter, Sort, dan Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-572
  - TC-GS-USER-573
  - TC-GS-USER-574
  - TC-GS-USER-589
  - TC-GS-USER-590
coverage:
  web: automated
---

# Tab Changelog Detail: Sort 3-State, Pagination, dan Kombinasi Search, Filter, Sort, dan Pagination

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, tampil `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` spec ini; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role Full CRUD (Fajar Nugroho, tampil `Fajar N`) `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4; kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`). Dipakai hanya untuk membuat entri Changelog dengan Modified By kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`.
- Data Pre-setup yang dipakai (hanya dibaca, tidak diubah; S-06): Position `Staff`, `Supervisor`, `Finance Manager`, `Internal Auditor`, dan `HR Business Partner` (Tabel Data Uji Pre-setup No. 22) dan Client PT Maju Bersama dengan subscription Fixed Asset + Supply Asset (No. 26). John Doe (No. 18) yang disebut TC tidak dipakai: riwayat Changelog-nya tidak dijamin memuat sedikitnya dua nilai distinct pada kolom yang diuji (S-11) dan data Pre-setup tidak diubah (S-06), sehingga spec memakai user uji milik spec.
- Data Dinamis (user uji milik spec, seeding lewat API di hook `before`; kemampuan seeding user lewat API disediakan tim FE/BE, endpoint tidak disebut di TC dan PRD):
  - User uji: Name `Log User {runId}-093`, Email `loguser+{runId}-093@qwertysystem.net`, Position `Staff`, Employee ID `{empId1}`, Access `Fixed Asset`, Active. `{empId1}`, `{empId2}`, `{empId3}` adalah tiga Employee ID numerik, naik berurutan (`{empId1}` < `{empId2}` < `{empId3}`), unik per run, diturunkan dari `{runId}` (hanya digit timestamp) dan memuat nomor spec (S-12): `{empId1}` = `{runId}0931`, `{empId2}` = `{runId}0932`, `{empId3}` = `{runId}0933`.
  - Entri Changelog base (12 entri, urutan seeding = urutan waktu, dari terlama ke terbaru; Modified By tampil `[First Name] [Last Initial]`):
    - a. `Create` | `Name` | `—` | `Log User {runId}-093` | `Siti N`
    - b. `Edit` | `Position` | `Staff` | `Supervisor` | `Siti N`
    - c. `Edit` | `Employee ID` | `{empId1}` | `{empId2}` | `Siti N`
    - d. `Deactivate` | `Status (Global)` | `Active` | `Inactive` | `Siti N`
    - e. `Activate` | `Status (Global)` | `Inactive` | `Active` | `Siti N`
    - f. `Add Access` | `App Access` | `—` | `Supply Asset` | `Siti N`
    - g. `Remove Access` | `App Access` | `Supply Asset` | `—` | `Siti N`
    - h. `Edit` | `Position` | `Supervisor` | `Finance Manager` | `Fajar N`
    - i. `Edit` | `Position` | `Finance Manager` | `Staff` | `Fajar N`
    - j. `Edit` | `Employee ID` | `{empId2}` | `{empId3}` | `Fajar N`
    - k. `Edit` | `Position` | `Staff` | `Internal Auditor` | `Fajar N`
    - l. `Edit` | `Position` | `Internal Auditor` | `Supervisor` | `Fajar N`
  - Entri Changelog tambahan untuk spec ini (10 entri, dibuat sesudah entri l; total 22 entri, lebih dari 21):
    - m. `Edit` | `Position` | `Supervisor` | `Staff` | `Fajar N`
    - n. `Edit` | `Position` | `Staff` | `Supervisor` | `Siti N`
    - o. `Edit` | `Position` | `Supervisor` | `Staff` | `Fajar N`
    - p. `Edit` | `Position` | `Staff` | `Supervisor` | `Siti N`
    - q. `Edit` | `Position` | `Supervisor` | `Staff` | `Fajar N`
    - r. `Edit` | `Position` | `Staff` | `Supervisor` | `Siti N`
    - s. `Edit` | `Position` | `Supervisor` | `Staff` | `Fajar N`
    - t. `Edit` | `Position` | `Staff` | `Supervisor` | `Siti N`
    - u. `Edit` | `Position` | `Supervisor` | `Staff` | `Fajar N`
    - v. `Edit` | `Position` | `Staff` | `HR Business Partner` | `Siti N`
  - Pelaku entri: `Siti N` lewat sesi API Total Control, `Fajar N` lewat sesi API Fajar Nugroho. Dengan demikian kolom Modified By memuat dua nilai distinct (`Siti N`, `Fajar N`); kolom Action, Field, Old Value, dan New Value memuat sedikitnya dua nilai distinct (S-11).
- Kemampuan teknis yang disediakan tim FE/BE (TC, PRD, dan LLD tidak memberi cara): memberi cap waktu pada entri seed sehingga setiap entri berjarak sedikitnya 1 menit dari entri sebelumnya mengikuti urutan huruf di atas, dan entri a (`Create`) bercap tanggal hari uji dikurangi 2 hari (H-2) sedangkan entri lain bercap hari uji. Cap waktu ini membuat urutan Date deterministik (entri terbaru di atas) dan memberi dua nilai distinct pada kolom Date.
- Kemampuan teknis: klik header kolom dan icon di toolbar tabel; mengetik di kotak Search dan dropdown Filter; menyalin teks sel.
- Konfigurasi kolom Tab Changelog akun Total Control dalam keadaan default (6 kolom tampil, tanpa pin) saat spec dimulai; hook `before` mengosongkan konfigurasi kolom Tab Changelog bila perlu (mekanisme disediakan tim FE).
- Baseline audit trail (S-12, bagian 8b butir 10): user uji `Log User {runId}-093` dibuat baru oleh hook `before` dengan nama dan email bersuffix `-093`, sehingga sebelum seeding Tab Changelog belum memuat entri apa pun; baseline = 0 dicatat eksplisit di hook `before` tepat sebelum seeding. Jumlah baris total yang diasersi adalah selisih terhadap baseline itu (baseline 0 + 22 entri seed), bukan total absolut tabel. Bila baseline perlu dibaca, kemampuan baca total entri disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut caranya).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user uji `Log User {runId}-093` lewat API. Entri Changelog tidak bisa dihapus.
- Precondition TC-GS-USER-572, 573, 574, 589, 590: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tersedia; user uji punya riwayat Changelog.
- Suite serial (`parallel: false`) karena spec membaca dan mengubah konfigurasi kolom Tab Changelog di browser yang sama dengan spec lain.
- State global yang diubah dan dipulihkan: tidak ada yang bertahan; visibilitas kolom yang diubah di dalam spec dikembalikan lewat langkah, dan hook `after` memulihkan konfigurasi kolom Tab Changelog ke nilai awal sebagai cadangan.

## Test Steps

### TC-GS-USER-572: Sort 3-state kolom kelas tanggal

1. Klik icon Search di User List, ketik `Log User {runId}-093`, tekan Enter
2. Klik Name `Log User {runId}-093` di User List
3. Klik Tab `Changelog`
4. Verifikasi tabel memuat sedikitnya dua baris data uji
5. Klik header Date
6. Verifikasi klik 1: Date Oldest First (baris pertama Action `Create`, Field `Name`)
7. Klik header Date
8. Verifikasi klik 2: Date Newest First (baris pertama New Value `HR Business Partner`)
9. Klik header Date
10. Verifikasi urutan kembali ke default sort tabel: baris pertama adalah entri terbaru (New Value `HR Business Partner`, Modified By `Siti N`) dan baris kedua Modified By `Fajar N`

### TC-GS-USER-573: Sort 3-state kolom kelas teks A-Z

11. Klik header Action
12. Verifikasi klik 1: Action A-Z (baris pertama Action `Activate`)
13. Klik header Action
14. Verifikasi klik 2: Action Z-A (baris pertama Action `Remove Access`)
15. Klik header Action
16. Verifikasi urutan kembali ke default sort tabel: baris pertama adalah entri terbaru (New Value `HR Business Partner`, Modified By `Siti N`) dan baris kedua Modified By `Fajar N`
17. Klik header Field
18. Verifikasi klik 1: Field A-Z (baris pertama Field `App Access`)
19. Klik header Field
20. Verifikasi klik 2: Field Z-A (baris pertama Field `Status (Global)`)
21. Klik header Field
22. Verifikasi urutan kembali ke default sort tabel: baris pertama adalah entri terbaru (New Value `HR Business Partner`, Modified By `Siti N`) dan baris kedua Modified By `Fajar N`
23. Klik header Modified By
24. Verifikasi klik 1: Modified By A-Z (baris pertama Modified By `Fajar N`)
25. Klik header Modified By
26. Verifikasi klik 2: Modified By Z-A (baris pertama Modified By `Siti N`)
27. Klik header Modified By
28. Verifikasi urutan kembali ke default sort tabel: baris pertama adalah entri terbaru (New Value `HR Business Partner`, Modified By `Siti N`) dan baris kedua Modified By `Fajar N`

### TC-GS-USER-574: Sort 3-state kolom kelas nilai campuran

29. Klik header Old Value
30. Verifikasi klik 1: Old Value numerik dulu (baris pertama `{empId1}`, baris kedua `{empId2}`)
31. Verifikasi klik 1: Old Value teks sesudah numerik (baris ketiga `Active`)
32. Pindah ke halaman terakhir (halaman 3) pada Pagination
33. Verifikasi klik 1: Old Value kosong di akhir (baris terakhir halaman 3 bernilai `—`)
34. Pindah ke halaman 1 pada Pagination
35. Klik header Old Value
36. Verifikasi klik 2: Old Value kosong di awal (baris pertama bernilai `—`)
37. Verifikasi klik 2: Old Value teks Z-A sesudah kosong (baris ketiga `Supply Asset`)
38. Pindah ke halaman terakhir (halaman 3) pada Pagination
39. Verifikasi klik 2: Old Value numerik terbesar ke terkecil di akhir (baris terakhir halaman 3 `{empId1}`)
40. Pindah ke halaman 1 pada Pagination
41. Klik header Old Value
42. Verifikasi urutan kembali ke default sort tabel: baris pertama adalah entri terbaru (New Value `HR Business Partner`, Modified By `Siti N`) dan baris kedua Modified By `Fajar N`
43. Klik header New Value
44. Verifikasi klik 1: New Value numerik dulu (baris pertama `{empId2}`, baris kedua `{empId3}`)
45. Verifikasi klik 1: New Value teks sesudah numerik (baris ketiga `Active`)
46. Pindah ke halaman terakhir (halaman 3) pada Pagination
47. Verifikasi klik 1: New Value kosong di akhir (baris terakhir halaman 3 bernilai `—`)
48. Pindah ke halaman 1 pada Pagination
49. Klik header New Value
50. Verifikasi klik 2: New Value kosong di awal (baris pertama bernilai `—`)
51. Verifikasi klik 2: New Value teks Z-A sesudah kosong (baris kedua `Supply Asset`)
52. Pindah ke halaman terakhir (halaman 3) pada Pagination
53. Verifikasi klik 2: New Value numerik terbesar ke terkecil di akhir (baris terakhir halaman 3 `{empId2}`)
54. Pindah ke halaman 1 pada Pagination
55. Klik header New Value
56. Verifikasi urutan kembali ke default sort tabel: baris pertama adalah entri terbaru (New Value `HR Business Partner`, Modified By `Siti N`) dan baris kedua Modified By `Fajar N`

### TC-GS-USER-589: Pagination ubah page size dan input nomor halaman

57. Ubah page size ke 25
58. Verifikasi page size 25: halaman 1 memuat selisih 22 baris terhadap baseline 0 entri (22 entri seed, tidak lebih dari 25)
59. Ubah page size kembali ke 10
60. Ketik nomor halaman `2` pada input halaman, tekan Enter
61. Verifikasi input 2 + Enter: langsung ke halaman 2 (baris pertama Old Value `Internal Auditor`, New Value `Supervisor`)
62. Klik next
63. Verifikasi next: halaman 3 tampil (2 baris sisa dari 22 entri seed terhadap baseline 0: Action `Edit`, Field `Position`, Old Value `Staff`, New Value `Supervisor` dan Action `Create`)
64. Klik prev
65. Verifikasi prev: halaman 2 tampil (baris pertama Old Value `Internal Auditor`, New Value `Supervisor`)
66. Pindah ke halaman 1 pada Pagination

### TC-GS-USER-590: Kombinasi Search + Filter + Sort + Pagination berjalan bersamaan

67. Klik icon Search, ketik `Siti`, tekan Enter
68. Ubah page size ke 25
69. Verifikasi Search saja menyaring: tabel memuat 21 baris (semua entri seed kecuali entri j), termasuk baris Action `Create`, `Deactivate`, `Activate`, `Add Access`, dan `Remove Access`
70. Klik icon Filter, pilih opsi `Edit` pada Action, lalu klik `[Apply]`
71. Klik header Modified By sekali (A-Z)
72. Verifikasi Search tetap berlaku (input Search berisi `Siti`)
73. Verifikasi Filter tetap berlaku bersama Search (tabel memuat 16 baris, semuanya Action `Edit`; baris Action `Create`, `Deactivate`, `Activate`, `Add Access`, dan `Remove Access` tidak tampil)
74. Verifikasi Sort tetap berlaku (Modified By A-Z: baris pertama `Fajar N`, baris terakhir `Siti N`)
75. Verifikasi Pagination tetap berlaku (halaman 1 memuat 16 baris pada page size 25)
76. Ubah page size kembali ke 10
77. Verifikasi Search, Filter, dan Sort tetap berlaku sesudah page size diubah (input Search berisi `Siti`; pagination menampilkan 2 halaman dari 16 baris Action `Edit` pada page size 10, bukan 3 halaman dari 21 baris tanpa Filter; halaman 1 memuat 10 baris, semuanya Action `Edit`, baris pertama `Fajar N` dan baris terakhir `Siti N`)
78. Pindah ke halaman 2 pada Pagination
79. Verifikasi halaman 2 memuat 6 baris, semuanya Action `Edit` dan Modified By `Siti N`
80. Pindah ke halaman 1 pada Pagination
81. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
82. Klik icon ×, lalu tekan Enter pada input kosong
83. Klik header Modified By dua kali sampai sort kembali ke default

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber dengan TC-GS-USER-589 dan 590 di akhir (572, 573, 574, 589, 590). TC-GS-USER-572, 573, dan 574 mengembalikan sort ke default pada klik ketiga sehingga TC berikutnya mulai dari default. Detail user dan Tab `Changelog` dibuka sekali di langkah 1 sampai 3.
- Langkah 1 sampai 3 (mencari user uji lewat Search User List, lalu klik Name dan Tab `Changelog`) adalah langkah penghubung tanpa `Verifikasi`; TC menulis "Klik Name `John Doe`" tanpa cara menemukan baris, dan user uji milik spec menggantikan John Doe (lihat Prerequisites).
- Dataset spec ini 22 entri Changelog (12 entri base dan 10 entri tambahan, lihat Prerequisites); halaman 1 memuat entri terbaru sampai ke-10 (v sampai m), halaman 2 memuat l sampai c, halaman 3 memuat b dan a (`Create`).
- Langkah 4 (`Verifikasi tabel memuat sedikitnya dua baris data uji`) adalah asersi tambahan (S-03) yang mendahului asersi sort pertama (langkah 6, baris pertama Date Oldest First), karena urutan hanya bermakna bila tabel memuat sedikitnya dua baris; dataset spec ini 22 entri (Prerequisites).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03, S-09, dan S-14): pindah ke halaman terakhir dan kembali ke halaman 1 pada TC-GS-USER-574 (nilai kosong di akhir ascending dan numerik di akhir descending diamati di halaman terakhir, sedangkan klik header berikutnya dimulai dari halaman 1); "Pindah ke halaman 1" di akhir TC-GS-USER-589; dan tiga langkah terakhir TC-GS-USER-590 (membersihkan filter, Search, dan sort; langkah 81 sampai 83), serta pindah halaman di TC-GS-USER-590 (langkah 78 ke halaman 2 sebelum asersi halaman 2 dan langkah 80 kembali ke halaman 1 sebelum membersihkan filter). Langkah 68 (Ubah page size ke 25) di TC-GS-USER-590 juga aksi tanpa `Verifikasi` sendiri; dilakukan sebelum Filter supaya jumlah baris hasil Search saja (langkah 69) teramati penuh dalam satu halaman. Karena itu perubahan page size sebagai aksi terakhir TC-GS-USER-590 dilakukan lagi di langkah 76 (kembali ke 10) dan langkah 77 dan 79 memverifikasi bahwa Search, Filter, dan Sort tidak ikut tereset (halaman 2 berisi 6 baris Action `Edit` membuktikan Filter masih berlaku, karena tanpa Filter ada 21 baris dan 3 halaman).
- Langkah 69 adalah asersi pembanding tambahan (S-03, bagian 8b butir 2): jumlah baris hasil Search saja (21) harus lebih besar dari hasil Search + Filter (16, langkah 73), sehingga Filter Action `Edit` terbukti mempersempit hasil dan tidak lolos bila Filter hilang atau tereset. Kata kunci `Siti` cocok dengan kolom Modified By (`Siti N`) dan dengan Field `Position` (substring tidak peka huruf besar-kecil, lihat spec 090 langkah 50); satu-satunya entri seed yang tidak cocok adalah entri j (Field `Employee ID`, Modified By `Fajar N`).
- Asersi sort memakai nilai baris pertama atau terakhir karena entri seed bercap waktu berurutan (Prerequisites). Verifikasi default ("kembali ke default sort tabel", Date Newest First) memakai dua baris teratas karena baris pertama saja tidak membedakan default dari Modified By Z-A (kedua baris pertama bernilai `Siti N`).
- Sort Old Value dan New Value mengikuti prd-conventions.md §9.7: ascending numerik dulu lalu teks A-Z, kosong di akhir; descending kebalikan penuh (kosong di awal, teks Z-A, lalu numerik dari terbesar). Entri seed menyediakan nilai numerik (Employee ID), teks, dan kosong pada kedua kolom.
- Pembagian TC Tab Changelog di User Detail: Sort dan Pagination di spec 093; TC-GS-USER-590 (kombinasi Search, Filter, Sort, Pagination) di spec 093; kombinasi Search dan Filter tanpa Sort di spec 092.
- Spec melewati sekitar 35 langkah (83 langkah) karena TC-GS-USER-573 dan 574 menguji lima kolom dengan tiga klik dan `Verifikasi` per klik (S-01); semua blok satu kelas harness (Sort dan Pagination Tab Changelog), satu akun, satu dataset, dan tiap blok berdiri sendiri karena sort dikembalikan ke default pada klik ketiga.
- Total entri Tab Changelog tidak diasersi sebagai angka absolut (S-12, bagian 8b butir 10): asersi jumlah baris total memakai selisih 22 terhadap baseline 0 yang ditulis eksplisit di Prerequisites (user seed bersuffix `-093` dibuat baru, jadi baseline nol). Hitungan hasil Search atau Filter bersuffix dan isi per halaman tidak berubah.
- Temuan untuk QA: (1) Cap waktu entri Changelog (entri `Create` H-2, jarak sedikitnya 1 menit antar entri) tidak punya cara di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE (S-13). (2) Label Field Changelog untuk perubahan Employee ID tidak disebut eksplisit (PRD user.md §8.3 hanya menulis `[Field]`); spec memakai `Employee ID`. (3) TC-GS-USER-572 sampai 574 tidak menyebut "default sort tabel" secara eksplisit; spec membacanya sebagai Date Newest First (PRD user.md §4.1.5). (4) TC-GS-USER-574 Expected "kebalikannya" tidak menyebut posisi nilai kosong pada descending; spec mengikuti prd-conventions.md §9.7 (kosong di awal). (5) Kolom New Value kosong (Delete) tidak dapat muncul pada user yang masih ada; spec memakai baris `Remove Access` (New Value `—`) sebagai nilai kosong New Value. (6) TC-GS-USER-589 Data Uji "21 baris atau lebih" tidak menyebut jumlah pasti; spec menyediakan 22 entri. (7) TC-GS-USER-590 "Search keyword" tidak menyebut kata kunci; spec memakai `Siti` (cocok dengan Modified By `Siti N` dan Field `Position`) dan Filter Action satu opsi `Edit` (sesuai TC), sehingga Search dan Filter menyaring himpunan berbeda dan gabungannya lebih kecil dari Search saja (Search saja 21 baris; Search + Filter 16 baris; lima baris Action `Create`, `Deactivate`, `Activate`, `Add Access`, dan `Remove Access` tersaring oleh Filter, dan satu baris Field `Employee ID` Modified By `Fajar N` tersaring oleh Search). (8) TC-GS-USER-590 Expected "tanpa saling mereset" tidak menyebut nilai yang diamati; spec mengasersi keyword, filter, sort, dan jumlah baris pada page size 25.

