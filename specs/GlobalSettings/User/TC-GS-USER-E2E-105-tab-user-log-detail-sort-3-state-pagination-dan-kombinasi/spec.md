---
id: TC-GS-USER-E2E-105-tab-user-log-detail-sort-3-state-pagination-dan-kombinasi
title: "Tab User Log Detail: Sort 3-State, Pagination, dan Kombinasi Search+Filter+Sort+Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-652
  - TC-GS-USER-653
  - TC-GS-USER-654
  - TC-GS-USER-669
  - TC-GS-USER-670
coverage:
  web: automated
---

# Tab User Log Detail: Sort 3-State, Pagination, dan Kombinasi Search+Filter+Sort+Pagination

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD`, `USER_PASSWORD_NEW` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan No. 23, 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). TC memakai `John Doe` (Pre-setup No. 18) sebagai pemilik log, sedangkan isi User Log-nya bergantung pada riwayat login lingkungan dan tidak boleh diubah; spec memakai user seed milik spec (S-06, S-11). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before`. User diberi Division `Finance` dan Access `Fixed Asset` (Pre-setup No. 23 dan 26):
  - U-1: Name `John Doe {runId}-105`, email `johndoe+{runId}-105@qwertysystem.net`, status Activated, password `Spectra.env.USER_PASSWORD`. Pemilik User Log yang diuji (pengganti `John Doe` di TC).
  - Riwayat event U-1 (27 event, dipicu berurutan di hook `before`; Data Uji TC-GS-USER-669 menyebut tabel berisi 25 baris (fixture BE, Pre-setup No. 29) dan 27 baris membuat page size 25 menghasilkan dua halaman sehingga batas maksimal 25 baris teramati; sedikitnya dua nilai distinct pada tiap kolom yang di-sort, S-11):
    - Event 1 (terlama): Activity `Login`, Status `Failed`, Note `Invalid password`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS` (password salah sembarang yang disediakan tim FE/BE).
    - Event 2: Activity `Login`, Status `Success`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 3: Activity `Change Password`, Status `Success`, Note `Password changed`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS` (password diganti dari `Spectra.env.USER_PASSWORD` menjadi `Spectra.env.USER_PASSWORD_NEW`; login berikutnya memakai password baru).
    - Event 4: Activity `Logout`, Status `—`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 5 sampai 26: 11 pasang Login (Status `Success`, Note `—`) lalu Logout (Status `—`, Note `—`), seluruhnya IP Address `10.0.0.11`, Device / Browser `Chrome on Windows`.
    - Event 27 (terbaru): Activity `Login`, Status `Success`, Note `—`, IP Address `172.16.9.3`, Device / Browser `—` (User-Agent tidak dikenal, tidak terparse).
  - Hasil pada tabel (27 baris): Activity memuat `Login` (14 baris), `Logout` (12), dan `Change Password` (1); Status memuat `Success` (14), `Failed` (1), dan `—` (12); Note memuat `Invalid password` (1), `Password changed` (1), dan `—` (25); IP Address memuat `10.0.0.11` (22), `192.168.5.7` (4), dan `172.16.9.3` (1); Device / Browser memuat `Chrome on Windows` (22), `Firefox on macOS` (4), dan `—` (1).
- Baseline audit trail (S-12, bagian 8b butir 10): user `U-1` (`John Doe {runId}-105`) dibuat baru oleh hook `before` dengan nama dan email bersuffix `-105`, sehingga sebelum seeding Tab User Log belum memuat entri apa pun; baseline = 0 dicatat eksplisit di hook `before` tepat sebelum seeding. Jumlah baris total yang diasersi adalah selisih terhadap baseline itu (baseline 0 + 27 entri seed), bukan total absolut tabel. Bila baseline perlu dibaca, kemampuan baca total entri disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut caranya).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1, serta sisa user bersuffix `-105` dari run lama. Entri User Log tidak bisa dihapus.
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak menyebut mekanisme maupun endpoint): (a) seeding user berstatus Activated lewat API dengan password `Spectra.env.USER_PASSWORD`; (b) memicu event Login (Success dan Failed), Logout, dan Change Password (Success) untuk user uji dengan IP Address dan User-Agent tertentu, berurutan sesuai daftar dan bercap waktu hari uji. Hook `before` memicu Event 1 sampai 4, menunggu sampai menit berganti (maksimum 60 detik, konvensi bagian 6), lalu memicu Event 5 sampai 27; dengan begitu Event 1 sampai 4 dan Event 5 sampai 27 berbeda menit. Asersi urutan Date hanya memakai pasangan baris yang berbeda menit (baris Event 27 dan baris Event 1); urutan antar-event dalam menit yang sama tidak diasersi.
- Kemampuan teknis lain: membaca indikator sort pada header kolom; mengubah page size dan mengetik nomor halaman pada Pagination; mengetik di kotak Search; memilih opsi dropdown filter.
- State yang diubah dan dipulihkan: page size diubah ke 100 di langkah 4 (agar seluruh 27 baris teramati pada satu halaman saat Sort) dan dikembalikan ke 10 di langkah 77; Search, Filter, dan Sort dikembalikan ke default di akhir spec (langkah 71 sampai 77); hook `after` sebagai cadangan. Suite berjalan serial (`parallel: false`).
- Precondition TC-GS-USER-652, 653, 654, 669, 670: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### TC-GS-USER-652: Sort 3-state kolom kelas tanggal

1. Klik icon Search di User List, ketik `John Doe {runId}-105`, tekan Enter
2. Klik Name `John Doe {runId}-105`
3. Klik Tab `User Log`
4. Ubah page size ke 100
5. Verifikasi tabel memuat selisih 27 baris terhadap baseline 0 entri (27 event seed)
6. Klik header Date
7. Verifikasi Date klik 1 Oldest First: baris Status `Failed`, Note `Invalid password` berada sebelum baris IP Address `172.16.9.3`
8. Klik header Date
9. Verifikasi Date klik 2 Newest First: baris IP Address `172.16.9.3`, Device / Browser `—` berada sebelum baris Status `Failed`
10. Klik header Date
11. Verifikasi Date klik 3 urutan kembali ke default sort tabel Date Newest First (baris IP Address `172.16.9.3` berada sebelum baris Status `Failed`)

### TC-GS-USER-653: Sort 3-state kolom kelas teks A-Z dengan — di akhir

12. Klik header Activity
13. Verifikasi Activity klik 1 A-Z: baris 1 `Change Password`, baris 2 sampai 15 `Login`, baris 16 sampai 27 `Logout`
14. Klik header Activity
15. Verifikasi Activity klik 2 Z-A: baris 1 sampai 12 `Logout`, baris 13 sampai 26 `Login`, baris 27 `Change Password`
16. Klik header Activity
17. Verifikasi Activity klik 3 urutan kembali ke default sort tabel Date Newest First (baris IP Address `172.16.9.3` berada sebelum baris Status `Failed`)
18. Klik header Status
19. Verifikasi Status klik 1 A-Z: baris 1 `Failed`, baris 2 sampai 15 `Success`
20. Verifikasi Status klik 1: `—` di akhir (baris 16 sampai 27 bernilai `—`)
21. Klik header Status
22. Verifikasi Status klik 2 Z-A: baris 13 sampai 26 `Success`, baris 27 `Failed`
23. Verifikasi Status klik 2: `—` di awal (baris 1 sampai 12 bernilai `—`)
24. Klik header Status
25. Verifikasi Status klik 3 urutan kembali ke default sort tabel Date Newest First (baris IP Address `172.16.9.3` berada sebelum baris Status `Failed`)
26. Klik header Note
27. Verifikasi Note klik 1 A-Z: baris 1 `Invalid password`, baris 2 `Password changed`
28. Verifikasi Note klik 1: `—` di akhir (baris 3 sampai 27 bernilai `—`)
29. Klik header Note
30. Verifikasi Note klik 2 Z-A: baris 26 `Password changed`, baris 27 `Invalid password`
31. Verifikasi Note klik 2: `—` di awal (baris 1 sampai 25 bernilai `—`)
32. Klik header Note
33. Verifikasi Note klik 3 urutan kembali ke default sort tabel Date Newest First (baris IP Address `172.16.9.3` berada sebelum baris Status `Failed`)
34. Klik header Device / Browser
35. Verifikasi Device / Browser klik 1 A-Z: baris 1 sampai 22 `Chrome on Windows`, baris 23 sampai 26 `Firefox on macOS`
36. Verifikasi Device / Browser klik 1: `—` di akhir (baris 27 bernilai `—`)
37. Klik header Device / Browser
38. Verifikasi Device / Browser klik 2 Z-A: baris 1 sampai 4 `Firefox on macOS`, baris 5 sampai 26 `Chrome on Windows`
39. Verifikasi Device / Browser klik 2: `—` tetap di akhir (baris 27 bernilai `—`)
40. Klik header Device / Browser
41. Verifikasi Device / Browser klik 3 urutan kembali ke default sort tabel Date Newest First (baris IP Address `172.16.9.3` berada sebelum baris Status `Failed`)

### TC-GS-USER-654: Sort 3-state kolom kelas string IP

42. Klik header IP Address
43. Verifikasi IP Address klik 1 urut string A-Z: baris 1 sampai 22 `10.0.0.11`, baris 23 `172.16.9.3`, baris 24 sampai 27 `192.168.5.7`
44. Klik header IP Address
45. Verifikasi IP Address klik 2 Z-A: baris 1 sampai 4 `192.168.5.7`, baris 5 `172.16.9.3`, baris 6 sampai 27 `10.0.0.11`
46. Klik header IP Address
47. Verifikasi IP Address klik 3 urutan kembali ke default sort tabel Date Newest First (baris IP Address `172.16.9.3` berada sebelum baris Status `Failed`)

### TC-GS-USER-669: Pagination: ubah page size dan input nomor halaman

48. Ubah page size ke 25
49. Verifikasi halaman 1 memuat tepat 25 baris (maksimal 25 baris)
50. Ubah page size kembali ke 10
51. Ketik `2` pada input nomor halaman, tekan Enter
52. Verifikasi langsung berada di halaman 2: input halaman bernilai `2` dan tabel memuat 10 baris
53. Klik next
54. Verifikasi berpindah ke halaman 3: tabel memuat 7 baris
55. Klik prev
56. Verifikasi berpindah kembali ke halaman 2: input halaman bernilai `2` dan tabel memuat 10 baris

### TC-GS-USER-670: Kombinasi Search, Filter, Sort, dan Pagination bersamaan

57. Klik icon Search, ketik `Success`, tekan Enter
58. Verifikasi halaman 1 memuat 10 baris dan footer menampilkan 2 halaman (14 baris Status `Success`)
59. Klik icon Filter
60. Buka dropdown Activity
61. Pilih opsi `Login`
62. Klik area kosong di Filter Panel untuk menutup dropdown Activity
63. Klik `[Apply]`
64. Verifikasi halaman 1 memuat 10 baris dan footer menampilkan 2 halaman (13 baris dengan Activity `Login` dan Status `Success`)
65. Klik header Device / Browser
66. Verifikasi Device / Browser A-Z: halaman 1 memuat 10 baris `Chrome on Windows`
67. Ubah page size ke 25
68. Verifikasi halaman 1 memuat 13 baris: baris 1 sampai 11 `Chrome on Windows`, baris 12 `Firefox on macOS`, baris 13 `—` (Search, Filter, Sort, dan page size berlaku bersamaan)
69. Verifikasi kotak Search tetap berisi `Success`
70. Verifikasi indikator sort Device / Browser ascending tetap aktif
71. Klik icon `←`
72. Klik icon Filter
73. Klik `[Clear Field]`
74. Klik `[Apply]`
75. Klik header Device / Browser
76. Klik header Device / Browser
77. Ubah page size kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `John Doe` (Pre-setup No. 18). Isi User Log-nya bergantung pada riwayat login lingkungan, sehingga spec memakai user milik spec dengan riwayat event yang diketahui (S-06, S-11).
- Urutan TC dalam spec mengikuti `sourceTc` (652, 653, 654, 669, 670); TC-GS-USER-670 yang mengubah Search, Filter, Sort, dan page size ditaruh terakhir.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 (mencari user di User List agar Name dapat diklik); langkah 4 (page size 100 agar 27 baris teramati pada satu halaman sehingga posisi baris dapat diasersi; TC-GS-USER-652 sampai 654 tidak menyebut page size); langkah 71 sampai 77 (mengembalikan Search, Filter, Sort, dan page size ke default).
- Asersi tambahan (dicatat sesuai S-03): langkah 5 (tabel memuat 27 baris) adalah anchor jumlah seed sebelum Sort. Posisi baris pada Expected Sort (misal "baris 2 sampai 15 `Login`") adalah konkretisasi untuk data seed yang diketahui. Klik 3 pada tiap kolom mengembalikan sort ke default (Date Newest First), diamati lewat pasangan baris event terbaru (Event 27) dan event terlama (Event 1) yang berbeda menit; posisi absolut baris pertama dan terakhir tidak diasersi karena event dalam menit yang sama tidak punya urutan pasti (konvensi bagian 6). Nilai `—` pada Status dan Note diasersi di akhir pada klik 1 dan di awal pada klik 2; nilai `—` pada Device / Browser diasersi di akhir pada klik 1 dan klik 2, sesuai Expected TC-GS-USER-653.
- Spec melewati sekitar 35 langkah (77 langkah) karena lima TC memakai tab dan dataset (U-1) yang sama dalam satu kelas harness (fungsional), dan tiap blok berdiri sendiri karena tiap kolom diklik tiga kali sehingga kembali ke default sort. Sort enam kolom tiga klik dengan masing-masing klik diamati (S-01) merupakan blok identik.
- Pembagian TC lintas spec: Screening dan Search TC-GS-USER-409, 411, 412, 631 sampai 637 diverifikasi di spec 102; Filter Panel TC-GS-USER-638 sampai 646 di spec 103; kombinasi Search dan Filter TC-GS-USER-647 sampai 651 di spec 104; Setup Column TC-GS-USER-655 sampai 663 di spec 106; Download TC-GS-USER-410 dan 664 sampai 668 di spec 107.
- Total entri Tab User Log tidak diasersi sebagai angka absolut (S-12, bagian 8b butir 10): asersi jumlah baris total memakai selisih 27 terhadap baseline 0 yang ditulis eksplisit di Prerequisites (user seed bersuffix `-105` dibuat baru, jadi baseline nol). Hitungan hasil Search atau Filter bersuffix dan isi per halaman tidak berubah.
- Temuan untuk QA: (1) TC-GS-USER-652 sampai 654, 669, dan 670 memakai `John Doe` Pre-setup sebagai pemilik log; spec memakai user seed milik spec. (2) Mekanisme memicu event Login, Logout, dan Change Password dengan IP Address dan User-Agent tertentu tidak disebut di TC, PRD, dan LLD; disediakan tim FE/BE. (3) TC-GS-USER-652 sampai 654: default sort tabel adalah Date Newest First sehingga klik 2 dan klik 3 pada Date menghasilkan urutan yang sama; keduanya dibedakan lewat langkah klik bernomor. (4) TC-GS-USER-653 tidak menyebut cara mengamati "kembali ke default sort tabel" selain urutan baris; spec memakai pasangan baris Event 27 dan Event 1 pada default sort (Date Newest First). (5) TC-GS-USER-669 Data Uji menyebut tabel berisi 25 baris (fixture BE) sedangkan Expected a ("maksimal 25 baris") tidak membedakan 25 dari jumlah baris total; spec men-seed 27 baris sehingga halaman 1 berisi tepat 25 dan terdapat halaman kedua. (6) TC-GS-USER-670 langkah 3 "Search keyword" tidak menyebut kata kunci; spec memakai kata kunci yang disebut di langkah spec, dan langkah 4 TC ("Terapkan filter pada Activity (1 opsi)") diikuti apa adanya dengan filter Activity `Login`. (7) TC-GS-USER-653 menyebut sort A-Z kolom Note dan Device / Browser tanpa nilai; spec memakai dua nilai Note non-kosong dan dua nilai Device / Browser terparse (S-11). (8) Mekanisme menandai Guided Tooltip sebagai sudah dilihat tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
