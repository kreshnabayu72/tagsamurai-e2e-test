---
id: TC-GS-USER-E2E-103-tab-user-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and
title: "Tab User Log Detail: Filter Panel (Opsi, Multi-Select, OR, Dropdown Search, Chip, Rentang Tanggal, dan AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-638
  - TC-GS-USER-639
  - TC-GS-USER-640
  - TC-GS-USER-641
  - TC-GS-USER-642
  - TC-GS-USER-643
  - TC-GS-USER-644
  - TC-GS-USER-645
  - TC-GS-USER-646
coverage:
  web: automated
---

# Tab User Log Detail: Filter Panel (Opsi, Multi-Select, OR, Dropdown Search, Chip, Rentang Tanggal, dan AND)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD`, `USER_PASSWORD_NEW` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan No. 23, 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). TC memakai `John Doe` (Pre-setup No. 18) sebagai pemilik log, sedangkan isi User Log-nya bergantung pada riwayat login lingkungan dan tidak boleh diubah; spec memakai user seed milik spec (S-06, S-11). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before`. User diberi Division `Finance` dan Access `Fixed Asset` (Pre-setup No. 23 dan 26):
  - U-1: Name `John Doe {runId}-103`, email `johndoe+{runId}-103@qwertysystem.net`, status Activated, password `Spectra.env.USER_PASSWORD`. Pemilik User Log yang diuji (pengganti `John Doe` di TC).
  - Riwayat event U-1 (7 event, dipicu berurutan di hook `before`; sedikitnya dua nilai distinct pada tiap kolom yang difilter, S-11):
    - Event 1 (terlama): Activity `Login`, Status `Failed`, Note `Invalid password`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS` (password salah sembarang yang disediakan tim FE/BE).
    - Event 2: Activity `Login`, Status `Success`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 3: Activity `Change Password`, Status `Success`, Note `Password changed`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS` (password diganti dari `Spectra.env.USER_PASSWORD` menjadi `Spectra.env.USER_PASSWORD_NEW`; login berikutnya memakai password baru).
    - Event 4: Activity `Logout`, Status `—`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 5: Activity `Login`, Status `Success`, Note `—`, IP Address `10.0.0.11`, Device / Browser `Chrome on Windows`.
    - Event 6: Activity `Logout`, Status `—`, Note `—`, IP Address `10.0.0.11`, Device / Browser `Chrome on Windows`.
    - Event 7 (terbaru): Activity `Login`, Status `Success`, Note `—`, IP Address `172.16.9.3`, Device / Browser `—` (User-Agent tidak dikenal, tidak terparse).
  - Hasil pada tabel: Activity memuat `Login` (4 baris), `Logout` (2), dan `Change Password` (1); Status memuat `Success` (4), `Failed` (1), dan `—` (2). Tabel memuat 7 baris. Seluruh event bercap waktu hari uji.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1, serta sisa user bersuffix `-103` dari run lama. Entri User Log tidak bisa dihapus.
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak menyebut mekanisme maupun endpoint): (a) seeding user berstatus Activated lewat API dengan password `Spectra.env.USER_PASSWORD`; (b) memicu event Login (Success dan Failed), Logout, dan Change Password (Success) untuk user uji dengan IP Address dan User-Agent tertentu, berurutan dengan jeda sedikitnya satu detik antar-event supaya cap waktu tiap event berbeda. Event dipicu berurutan sesuai daftar dan bercap waktu hari uji.
- Kemampuan teknis lain: memilih opsi pada dropdown multi-select, mengetik di kotak search dropdown, dan memilih rentang tanggal pada date range picker.
- Date Format General Settings `DD/MM/YY` (default environment); spec ini tidak mengubahnya. Spec lain mengubah dan memulihkan nilai ini di hook `after`-nya, sehingga suite berjalan serial (`parallel: false`).
- State yang diubah dan dipulihkan: Filter dikosongkan di akhir spec (langkah 91 sampai 93); hook `after` sebagai cadangan.
- Precondition TC-GS-USER-638 sampai 646: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### TC-GS-USER-638: Screening Filter Panel Tab User Log

1. Klik icon Search di User List, ketik `John Doe {runId}-103`, tekan Enter
2. Klik Name `John Doe {runId}-103`
3. Klik Tab `User Log`
4. Klik icon Filter
5. Verifikasi field `Activity` berupa multi-select searchable dengan placeholder `All activities`
6. Verifikasi field `Status` berupa multi-select searchable dengan placeholder `All statuses`
7. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
8. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-USER-639: Opsi dropdown filter diambil dari nilai yang ada di tabel

9. Buka dropdown Activity
10. Verifikasi dropdown Activity memuat opsi `Change Password`, `Login`, dan `Logout`
11. Verifikasi opsi `Reset Password` dan `Session` tidak ada di dropdown Activity
12. Buka dropdown Status
13. Verifikasi dropdown Status memuat opsi `Failed` dan `Success`

### TC-GS-USER-640: Filter multi-select per field menyaring baris

14. Buka dropdown Activity
15. Pilih opsi `Logout`
16. Klik area kosong di Filter Panel untuk menutup dropdown Activity
17. Klik `[Apply]`
18. Verifikasi tabel menampilkan 2 baris, seluruhnya Activity `Logout`
19. Verifikasi icon Filter berubah gelap
20. Klik icon Filter
21. Klik `[Clear Field]`
22. Klik `[Apply]`
23. Klik icon Filter
24. Buka dropdown Status
25. Pilih opsi `Failed`
26. Klik area kosong di Filter Panel untuk menutup dropdown Status
27. Klik `[Apply]`
28. Verifikasi tabel menampilkan 1 baris dengan Status `Failed` (Activity `Login`, Note `Invalid password`)
29. Verifikasi icon Filter berubah gelap
30. Klik icon Filter
31. Klik `[Clear Field]`
32. Klik `[Apply]`

### TC-GS-USER-641: Dua opsi dalam satu field filter digabung OR

33. Klik icon Filter
34. Buka dropdown Activity
35. Pilih opsi `Login`
36. Pilih opsi `Logout`
37. Klik area kosong di Filter Panel untuk menutup dropdown Activity
38. Klik `[Apply]`
39. Verifikasi tabel menampilkan 6 baris dengan Activity `Login` (4 baris) atau `Logout` (2 baris)
40. Klik icon Filter
41. Klik `[Clear Field]`
42. Klik `[Apply]`

### TC-GS-USER-642: Search di dalam dropdown filter mempersempit opsi

43. Klik icon Filter
44. Buka dropdown Activity
45. Ketik `LOG` pada kotak search dropdown Activity
46. Verifikasi opsi `Login` dan `Logout` tampil dan opsi `Change Password` tidak tampil (substring tanpa membedakan huruf besar kecil)
47. Ganti isi kotak search dropdown dengan `zzz`
48. Verifikasi tidak ada opsi yang cocok di dropdown Activity

### TC-GS-USER-643: Hapus chip filter lewat (X) meng-uncheck opsi

49. Kosongkan isi kotak search dropdown Activity
50. Pilih opsi `Login`
51. Pilih opsi `Logout`
52. Klik area kosong di Filter Panel untuk menutup dropdown Activity
53. Verifikasi chip `Login` dan `Logout` tampil di field Activity
54. Klik (X) pada chip pertama `Login`
55. Verifikasi chip `Login` hilang
56. Verifikasi chip `Logout` tetap tampil
57. Buka dropdown Activity
58. Verifikasi checkbox opsi `Login` ter-uncheck

### TC-GS-USER-644: Uncheck opsi di dropdown menghapus chip

59. Klik area kosong di Filter Panel untuk menutup dropdown Activity
60. Klik `[Clear Field]`
61. Buka dropdown Activity
62. Pilih opsi `Login`
63. Pilih opsi `Logout`
64. Klik area kosong di Filter Panel untuk menutup dropdown Activity
65. Buka dropdown Activity
66. Hilangkan centang opsi `Logout` (opsi kedua)
67. Verifikasi chip `Logout` hilang
68. Verifikasi chip `Login` tetap tampil

### TC-GS-USER-645: Filter date range per field

69. Klik area kosong di Filter Panel untuk menutup dropdown Activity
70. Klik `[Clear Field]`
71. Pilih rentang tanggal hari ini sampai hari ini pada field Date
72. Verifikasi input Date menampilkan rentang dengan format Date Format General Settings (`DD/MM/YY`)
73. Klik `[Apply]`
74. Verifikasi tabel menampilkan 7 baris (seluruh event bercap waktu hari ini)
75. Klik icon Filter
76. Pilih rentang tanggal kemarin sampai kemarin pada field Date
77. Klik `[Apply]`
78. Verifikasi tabel menampilkan pesan `No results found` (tidak ada baris dalam rentang kemarin)
79. Klik icon Filter
80. Klik `[Clear Field]`
81. Klik `[Apply]`

### TC-GS-USER-646: Kombinasi dua field filter digabung AND

82. Klik icon Filter
83. Buka dropdown Activity
84. Pilih opsi `Login`
85. Klik area kosong di Filter Panel untuk menutup dropdown Activity
86. Buka dropdown Status
87. Pilih opsi `Success`
88. Klik area kosong di Filter Panel untuk menutup dropdown Status
89. Klik `[Apply]`
90. Verifikasi tabel menampilkan 3 baris dengan Activity `Login` dan Status `Success` (baris `Login` berstatus `Failed` tidak tampil)
91. Klik icon Filter
92. Klik `[Clear Field]`
93. Klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `John Doe` (Pre-setup No. 18). Isi User Log-nya bergantung pada riwayat login lingkungan, sehingga spec memakai user milik spec dengan riwayat event yang diketahui (S-06, S-11).
- Urutan TC dalam spec mengikuti `sourceTc` (638 sampai 646); screening (TC-GS-USER-638) di awal dan TC-GS-USER-639 sebelum Filter diterapkan supaya opsi dropdown diamati dari tabel penuh.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 (mencari user di User List agar Name dapat diklik); langkah "Klik area kosong di Filter Panel untuk menutup dropdown" (menutup dropdown multi-select supaya pemilihan berikutnya deterministik); langkah "Klik icon Filter, Klik `[Clear Field]`, Klik `[Apply]`" setelah tiap kasus yang menerapkan Filter (membersihkan Filter sebelum kasus berikutnya); langkah "Kosongkan isi kotak search dropdown Activity" dan "Klik `[Clear Field]`" (membersihkan state panel antar TC-GS-USER-642, 643, 644, dan 645). Filter Panel diasumsikan menutup sesudah `[Apply]` sehingga dibuka lagi lewat icon Filter.
- Asersi tambahan (dicatat sesuai S-03): jumlah baris pada Expected TC-GS-USER-640, 641, 645, dan 646 adalah konkretisasi "hanya baris dengan nilai terpilih tampil" untuk data seed yang diketahui; `Verifikasi` chip `Login` dan `Logout` tampil pada TC-GS-USER-643 adalah anchor positif sebelum chip dihapus (8b butir 2); `Verifikasi` opsi `Reset Password` dan `Session` tidak ada (TC-GS-USER-639) didahului `Verifikasi` tiga opsi yang tampil di dropdown yang sama (8b butir 2). TC-GS-USER-645: rentang hari ini menampilkan 7 baris dan rentang kemarin menampilkan `No results found`; seed tidak punya event bertanggal lampau, sehingga filter rentang diuji pada kedua sisi batas hari tanpa baris di luar rentang pada hari yang sama.
- Spec melewati sekitar 35 langkah (93 langkah) karena sembilan TC memakai Filter Panel yang sama, satu akun, satu dataset (U-1), satu kelas harness (fungsional), dan tiap blok berdiri sendiri karena Filter dibersihkan di akhir tiap blok. Langkah membuka dan membersihkan Filter yang berulang termasuk prefix berulang.
- Pembagian TC lintas spec: Screening dan Search TC-GS-USER-409, 411, 412, 631 sampai 637 diverifikasi di spec 102; kombinasi Search dan Filter TC-GS-USER-647 sampai 651 di spec 104; Sort, Pagination, dan kombinasi TC-GS-USER-652 sampai 654, 669, 670 di spec 105; Setup Column TC-GS-USER-655 sampai 663 di spec 106; Download TC-GS-USER-410 dan 664 sampai 668 di spec 107.
- Temuan untuk QA: (1) TC-GS-USER-638 sampai 646 memakai `John Doe` Pre-setup sebagai pemilik log; spec memakai user seed milik spec. (2) Mekanisme memicu event Login, Logout, dan Change Password dengan IP Address dan User-Agent tertentu tidak disebut di TC, PRD, dan LLD; disediakan tim FE/BE. (3) TC-GS-USER-639 tidak menyebut apakah nilai `—` pada Status muncul sebagai opsi dropdown Status (PRD §4.1.7 hanya menyebut `Success`/`Failed`); spec mengasersi opsi `Failed` dan `Success` saja. (4) TC-GS-USER-640, 641, 643, 644, dan 646 menyebut "opsi sesuai data" tanpa nilai; spec memakai opsi yang tercantum di langkah. (5) TC-GS-USER-645 Data Uji "Rentang tanggal sesuai data" tanpa data bertanggal lampau; seed hanya menghasilkan event bercap waktu hari uji (cap waktu event tidak dapat diatur tanpa kemampuan khusus); selain itu hari "hari ini" bergantung pada zona waktu client General Settings. (6) TC-GS-USER-642 tidak menyebut teks pada dropdown tanpa opsi cocok; spec hanya mengasersi tidak ada opsi. (7) TC-GS-USER-643 dan 644 tidak menyebut urutan chip; spec memilih `Login` lalu `Logout` sehingga urutan pilihan dan urutan abjad sama. (8) Mekanisme menandai Guided Tooltip sebagai sudah dilihat tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
