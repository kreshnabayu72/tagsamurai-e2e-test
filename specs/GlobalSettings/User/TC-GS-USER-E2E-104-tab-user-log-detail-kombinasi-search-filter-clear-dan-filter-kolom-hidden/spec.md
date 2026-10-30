---
id: TC-GS-USER-E2E-104-tab-user-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden
title: "Tab User Log Detail: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-647
  - TC-GS-USER-648
  - TC-GS-USER-649
  - TC-GS-USER-650
  - TC-GS-USER-651
coverage:
  web: automated
---

# Tab User Log Detail: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD`, `USER_PASSWORD_NEW` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan No. 23, 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). TC memakai `John Doe` (Pre-setup No. 18) sebagai pemilik log, sedangkan isi User Log-nya bergantung pada riwayat login lingkungan dan tidak boleh diubah; spec memakai user seed milik spec (S-06, S-11). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before`. User diberi Division `Finance` dan Access `Fixed Asset` (Pre-setup No. 23 dan 26):
  - U-1: Name `John Doe {runId}-104`, email `johndoe+{runId}-104@qwertysystem.net`, status Activated, password `Spectra.env.USER_PASSWORD`. Pemilik User Log yang diuji (pengganti `John Doe` di TC).
  - Riwayat event U-1 (7 event, dipicu berurutan di hook `before`; sedikitnya dua nilai distinct pada kolom yang di-search, difilter, dan di-sort, S-11):
    - Event 1 (terlama): Activity `Login`, Status `Failed`, Note `Invalid password`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS` (password salah sembarang yang disediakan tim FE/BE).
    - Event 2: Activity `Login`, Status `Success`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 3: Activity `Change Password`, Status `Success`, Note `Password changed`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS` (password diganti dari `Spectra.env.USER_PASSWORD` menjadi `Spectra.env.USER_PASSWORD_NEW`; login berikutnya memakai password baru).
    - Event 4: Activity `Logout`, Status `—`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 5: Activity `Login`, Status `Success`, Note `—`, IP Address `10.0.0.11`, Device / Browser `Chrome on Windows`.
    - Event 6: Activity `Logout`, Status `—`, Note `—`, IP Address `10.0.0.11`, Device / Browser `Chrome on Windows`.
    - Event 7 (terbaru): Activity `Login`, Status `Success`, Note `—`, IP Address `172.16.9.3`, Device / Browser `—` (User-Agent tidak dikenal, tidak terparse).
  - Hasil pada tabel: Activity memuat `Login` (4 baris), `Logout` (2), dan `Change Password` (1); Status memuat `Success` (4), `Failed` (1), dan `—` (2); Device / Browser memuat `Firefox on macOS` (4), `Chrome on Windows` (2), dan `—` (1). Tabel memuat 7 baris.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1, serta sisa user bersuffix `-104` dari run lama. Entri User Log tidak bisa dihapus.
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak menyebut mekanisme maupun endpoint): (a) seeding user berstatus Activated lewat API dengan password `Spectra.env.USER_PASSWORD`; (b) memicu event Login (Success dan Failed), Logout, dan Change Password (Success) untuk user uji dengan IP Address dan User-Agent tertentu, berurutan dengan jeda sedikitnya satu detik antar-event supaya cap waktu tiap event berbeda. Event dipicu berurutan sesuai daftar dan bercap waktu hari uji.
- Kemampuan teknis lain: mengetik di kotak Search, memilih opsi dropdown filter, membaca indikator sort pada header kolom, menyetel visibilitas kolom lewat Overlay Column Visibility.
- State yang diubah dan dipulihkan: Search dan Filter dikosongkan di akhir tiap TC; sort Activity dikembalikan ke default (langkah 46 sampai 48); visibilitas kolom `Status` dicentang kembali di langkah 64; hook `after` sebagai cadangan. Suite berjalan serial (`parallel: false`).
- Precondition TC-GS-USER-647 sampai 651: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### TC-GS-USER-647: Search lalu Filter menghasilkan irisan

1. Klik icon Search di User List, ketik `John Doe {runId}-104`, tekan Enter
2. Klik Name `John Doe {runId}-104`
3. Klik Tab `User Log`
4. Klik icon Search, ketik `Firefox`, tekan Enter
5. Verifikasi hasil Search saja: 4 baris dengan Device / Browser `Firefox on macOS`
6. Klik icon Filter
7. Buka dropdown Activity
8. Pilih opsi `Login`
9. Klik area kosong di Filter Panel untuk menutup dropdown Activity
10. Klik `[Apply]`
11. Verifikasi hasil adalah irisan Search dan Filter: 2 baris dengan Activity `Login` dan Device / Browser `Firefox on macOS`
12. Verifikasi kotak Search tetap berisi `Firefox` (keyword tidak ter-reset)
13. Klik icon `←`
14. Klik icon Filter
15. Klik `[Clear Field]`
16. Klik `[Apply]`

### TC-GS-USER-648: Filter lalu Search menghasilkan irisan

17. Klik icon Filter
18. Buka dropdown Activity
19. Pilih opsi `Logout`
20. Klik area kosong di Filter Panel untuk menutup dropdown Activity
21. Klik `[Apply]`
22. Verifikasi hasil Filter saja: 2 baris dengan Activity `Logout`
23. Klik icon Search, ketik `Chrome`, tekan Enter
24. Verifikasi hasil adalah irisan Filter dan Search: 1 baris dengan Activity `Logout` dan Device / Browser `Chrome on Windows`
25. Verifikasi icon Filter tetap gelap (Filter tetap aktif)
26. Klik icon `←`
27. Klik icon Filter
28. Klik `[Clear Field]`
29. Klik `[Apply]`

### TC-GS-USER-649: Clear filter saat Search dan Sort aktif

30. Klik icon Search, ketik `Firefox`, tekan Enter
31. Verifikasi hasil Search saja: 4 baris dengan Device / Browser `Firefox on macOS`
32. Klik header Activity (sort ascending)
33. Verifikasi indikator sort Activity ascending aktif dan 4 baris berurutan A-Z: `Change Password`, `Login`, `Login`, `Logout`
34. Klik icon Filter
35. Buka dropdown Status
36. Pilih opsi `Success`
37. Klik area kosong di Filter Panel untuk menutup dropdown Status
38. Klik `[Apply]`
39. Verifikasi hasil adalah irisan Search dan Filter: 2 baris berurutan Activity `Change Password`, `Login`
40. Klik icon Filter
41. Klik `[Clear Field]`
42. Klik `[Apply]`
43. Verifikasi kotak Search tetap berisi `Firefox`
44. Verifikasi indikator sort Activity ascending tetap aktif dan 4 baris berurutan A-Z: `Change Password`, `Login`, `Login`, `Logout`
45. Verifikasi Filter terlepas: icon Filter tidak gelap
46. Klik icon `←`
47. Klik header Activity (sort descending)
48. Klik header Activity (kembali ke default sort tabel)

### TC-GS-USER-650: Filter tetap tersedia untuk kolom yang di-hide

49. Klik icon Filter
50. Buka dropdown Status
51. Pilih opsi `Failed`
52. Klik area kosong di Filter Panel untuk menutup dropdown Status
53. Klik `[Apply]`
54. Verifikasi hasil Filter saja: 1 baris dengan Note `Invalid password`
55. Klik header Column Visibility (⋯)
56. Hilangkan centang kolom `Status`
57. Verifikasi kolom `Status` tidak tampil di tabel
58. Verifikasi Filter tetap aktif menyaring: tabel tetap 1 baris dengan Note `Invalid password` dan icon Filter tetap gelap
59. Klik icon Filter
60. Verifikasi field `Status` tetap ada di Filter Panel dengan chip `Failed`
61. Klik `[Clear Field]`
62. Klik `[Apply]`
63. Klik header Column Visibility (⋯)
64. Centang kembali kolom `Status`

### TC-GS-USER-651: Kombinasi Search dan Filter menghasilkan 0 baris, pulih saat Filter dilepas

65. Klik icon Search, ketik `Chrome`, tekan Enter
66. Verifikasi hasil Search saja: 2 baris dengan Device / Browser `Chrome on Windows`
67. Klik icon Filter
68. Buka dropdown Status
69. Pilih opsi `Failed`
70. Klik area kosong di Filter Panel untuk menutup dropdown Status
71. Klik `[Apply]`
72. Verifikasi empty filtered state tampil dengan pesan `No results found`
73. Klik icon Filter
74. Klik `[Clear Field]`
75. Klik `[Apply]`
76. Verifikasi 2 baris dengan Device / Browser `Chrome on Windows` kembali tampil
77. Klik icon `←`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `John Doe` (Pre-setup No. 18). Isi User Log-nya bergantung pada riwayat login lingkungan, sehingga spec memakai user milik spec dengan riwayat event yang diketahui (S-06, S-11).
- Urutan TC dalam spec mengikuti `sourceTc` (647 sampai 651). TC-GS-USER-650 (hide kolom) ditaruh sebelum TC-GS-USER-651 dan dipulihkan di langkah 64 supaya TC-GS-USER-651 memakai konfigurasi kolom default.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 (mencari user di User List agar Name dapat diklik); langkah "Klik area kosong di Filter Panel untuk menutup dropdown" (menutup dropdown multi-select); langkah "Klik icon `←`" sesudah tiap TC dan langkah "Klik icon Filter, Klik `[Clear Field]`, Klik `[Apply]`" yang mengikutinya (membersihkan Search dan Filter sebelum TC berikutnya: langkah 13, 26, 46, 77); langkah 46 sampai 48 (mengembalikan sort Activity ke default); langkah 55 sampai 64 (hide dan unhide kolom `Status` bagian TC-GS-USER-650); langkah 61 (membersihkan Filter sebelum kolom dicentang kembali). Filter Panel diasumsikan menutup sesudah `[Apply]` sehingga dibuka lagi lewat icon Filter.
- Asersi tambahan (dicatat sesuai S-03): `Verifikasi` hasil Search saja atau Filter saja sebelum kombinasi adalah anchor positif untuk membuktikan irisan lebih sempit dari masing-masing (8b butir 2), dan khusus TC-GS-USER-651 untuk empty filtered state; jumlah baris pada Expected adalah konkretisasi untuk data seed yang diketahui. Data uji tiap kombinasi dipilih agar irisan tidak sama dengan Search saja maupun Filter saja: TC-GS-USER-647 (Search `Firefox` 4 baris, Filter `Login` 4 baris, irisan 2 baris), TC-GS-USER-648 (Filter `Logout` 2 baris, Search `Chrome` 2 baris, irisan 1 baris), TC-GS-USER-651 (Search `Chrome` dan Filter Status `Failed` tidak beririsan).
- TC-GS-USER-649: keyword dan arah sort diverifikasi sesudah `[Clear Field]` dan `[Apply]` (langkah 40 sampai 42) dan Filter terlepas diamati lewat icon Filter tidak gelap.
- Spec melewati sekitar 35 langkah (77 langkah) karena lima TC memakai tab, Filter Panel, dan dataset (U-1) yang sama dalam satu kelas harness (fungsional), dan tiap blok berdiri sendiri karena Search dan Filter dibersihkan di akhir tiap blok. Langkah membuka dan membersihkan Filter yang berulang termasuk prefix berulang.
- Pembagian TC lintas spec: Screening dan Search TC-GS-USER-409, 411, 412, 631 sampai 637 diverifikasi di spec 102; Filter Panel TC-GS-USER-638 sampai 646 di spec 103; Sort, Pagination, dan kombinasi TC-GS-USER-652 sampai 654, 669, 670 di spec 105; Setup Column TC-GS-USER-655 sampai 663 di spec 106; Download TC-GS-USER-410 dan 664 sampai 668 di spec 107.
- Temuan untuk QA: (1) TC-GS-USER-647 sampai 651 memakai `John Doe` Pre-setup sebagai pemilik log; spec memakai user seed milik spec. (2) Mekanisme memicu event Login, Logout, dan Change Password dengan IP Address dan User-Agent tertentu tidak disebut di TC, PRD, dan LLD; disediakan tim FE/BE. (3) TC-GS-USER-647 sampai 651 menyebut "keyword", "filter", dan "sort salah satu kolom" tanpa nilai; spec memakai nilai yang tercantum di langkah. (4) TC-GS-USER-650 Expected a ("Filter tetap aktif menyaring") tidak menyatakan cara mengamati saat kolom yang difilter tidak tampil; spec memakai jumlah baris dan kolom lain (Note) serta icon Filter gelap. (5) TC-GS-USER-649 dan 647 tidak menyatakan tampilan Search sesudah `[Apply]`; spec mengasersi isi kotak Search. (6) Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan mengosongkan preferensi Setup Column tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
