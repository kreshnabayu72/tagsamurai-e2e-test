---
id: TC-GS-USER-E2E-098-tab-system-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden
title: "Tab System Log Detail: Kombinasi Search dan Filter (Irisan, Clear Filter, Filter Kolom Hidden, dan Nol Baris)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-607
  - TC-GS-USER-608
  - TC-GS-USER-609
  - TC-GS-USER-610
  - TC-GS-USER-611
coverage:
  web: automated
---

# Tab System Log Detail: Kombinasi Search dan Filter (Irisan, Clear Filter, Filter Kolom Hidden, dan Nol Baris)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor UI: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 23 dan 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). System Log memuat aksi yang dilakukan user sebagai aktor (PRD user.md §8.3). Tiap user diberi Division `Finance` dan Access `Fixed Asset`:
  - Pemilik log `Aktor Log {runId}-098`, email `aktorlog+{runId}-098@qwertysystem.net`, tier Total Control, status Activated, password `Spectra.env.USER_PASSWORD`. Aktivasi akun seed dan sesi API Aktor Log disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut mekanismenya). Seluruh aksi seed di bawah dijalankan lewat sesi API Aktor Log.
  - Target aksi `Target Alfa {runId}-098` (email `targetalfa+{runId}-098@qwertysystem.net`, Position `Staff`) dan `Target Beta {runId}-098` (email `targetbeta+{runId}-098@qwertysystem.net`).
  - Aksi seed oleh Aktor Log, berurutan (hanya data yang dipakai `Verifikasi`, S-11): (1) Create `Target Alfa` (Field `Name`, Old Value `—`); (2) Create `Target Beta`; (3) Edit Position `Target Alfa` dari `Staff` menjadi `Supervisor`; (4) Deactivate `Target Alfa` (Field `Status (Global)`, `Active` menjadi `Inactive`); (5) Activate `Target Alfa` (`Inactive` menjadi `Active`); (6) Delete `Target Beta` (Field `Name`, New Value `—`); (7) Assign Total Control ke `Target Alfa` (Object `Total Control`, Field `Access Level`, New Value `Total Control`). Hasil: kolom Action memuat `Activate`, `Assign`, `Create`, `Deactivate`, `Delete`, `Edit`; kolom Name memuat `Target Alfa` dan `Target Beta`; kolom Field memuat `Access Level`, `Name`, `Position`, `Status (Global)` (sedikitnya dua nilai distinct per kolom, S-11). Kata kunci Search `alfa` mencocokkan lima entri `Target Alfa` dan tidak mencocokkan entri `Target Beta`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Target Alfa` (cabut tier Total Control lebih dulu bila diperlukan), `Target Beta` bila masih ada, dan `Aktor Log`; hapus sisa user bersuffix `-098` dari run lama. Entri log tidak bisa dihapus.
- Kemampuan teknis: mengetik di kotak Search; mengamati state icon Filter aktif (berubah gelap); klik header kolom sort.
- State global yang diubah dan dipulihkan: visibilitas kolom `Field` pada tabel System Log (di-hide pada langkah 24 lalu dicentang kembali pada langkah 32); hook `before` mengosongkan preferensi Setup Column tab ini (tempat penyimpanan preferensi tidak disebut TC User; disediakan tim FE) dan hook `after` memulihkannya sebagai cadangan. Suite berjalan serial (`parallel: false`).
- Precondition TC-GS-USER-607 sampai 611: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### TC-GS-USER-607: Search lalu Filter menghasilkan irisan

1. Klik icon Search di User List, ketik `Aktor Log {runId}-098`, tekan Enter
2. Klik Name `Aktor Log {runId}-098`
3. Klik Tab `System Log`
4. Klik icon Search, ketik `alfa`, tekan Enter
5. Klik icon Filter
6. Pilih Action `Create`, klik `[Apply]`
7. Verifikasi baris Action `Create` Name `Target Alfa {runId}-098` tampil
8. Verifikasi baris Action `Create` Name `Target Beta {runId}-098` tidak tampil (disaring Search)
9. Verifikasi baris Action `Edit` Name `Target Alfa {runId}-098` tidak tampil (disaring Filter)
10. Verifikasi keyword tidak ter-reset (input Search berisi `alfa`)
11. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
12. Klik icon `×`
13. Tekan Enter pada input kosong

### TC-GS-USER-608: Filter lalu Search menghasilkan irisan

14. Klik icon Filter, pilih Action `Create`, klik `[Apply]`
15. Isi Search dengan `alfa`, tekan Enter
16. Verifikasi baris Action `Create` Name `Target Alfa {runId}-098` tampil
17. Verifikasi baris Action `Create` Name `Target Beta {runId}-098` tidak tampil (disaring Search)
18. Verifikasi baris Action `Edit` Name `Target Alfa {runId}-098` tidak tampil (disaring Filter)
19. Verifikasi Filter tetap aktif (icon Filter gelap)
20. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
21. Klik icon `×`
22. Tekan Enter pada input kosong

### TC-GS-USER-610: Filter tetap tersedia untuk kolom yang di-hide

23. Klik icon Filter, pilih Field `Position`, klik `[Apply]`
24. Klik header Column Visibility (⋯), hilangkan centang kolom `Field`
25. Verifikasi kolom `Field` tidak tampil di tabel
26. Verifikasi Filter tetap aktif menyaring: baris Action `Edit` Name `Target Alfa {runId}-098` (Old Value `Staff`, New Value `Supervisor`) tampil
27. Verifikasi baris Action `Create` tidak tampil
28. Klik icon Filter
29. Verifikasi field filter `Field` tetap ada di Filter Panel
30. Klik `[Clear Field]`
31. Klik `[Apply]`
32. Klik header Column Visibility (⋯), centang kembali kolom `Field`

### TC-GS-USER-611: Kombinasi Search dan Filter menghasilkan 0 baris lalu pulih saat filter dilepas

33. Isi Search dengan `alfa`, tekan Enter
34. Verifikasi baris Action `Create` Name `Target Alfa {runId}-098` tampil
35. Klik icon Filter, pilih Name `Target Beta {runId}-098`, klik `[Apply]`
36. Verifikasi ilustrasi empty filtered state tampil
37. Verifikasi teks `No results found`
38. Verifikasi teks `Try adjusting your search or filter.`
39. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
40. Verifikasi baris Action `Create` Name `Target Alfa {runId}-098` tampil kembali
41. Verifikasi baris Action `Create` Name `Target Beta {runId}-098` tidak tampil (hasil search `alfa`)

### TC-GS-USER-609: Clear filter saat Search dan Sort aktif

42. Klik icon `×`
43. Tekan Enter pada input kosong
44. Isi Search dengan `alfa`, tekan Enter
45. Klik header Action
46. Klik icon Filter, pilih Action `Create`, klik `[Apply]`
47. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
48. Verifikasi keyword tetap aktif (input Search berisi `alfa`)
49. Verifikasi sort Action A-Z tetap aktif (baris pertama Action `Activate`)
50. Verifikasi filter terlepas (icon Filter tidak gelap)
51. Verifikasi baris Action `Edit` Name `Target Alfa {runId}-098` tampil (filter `Create` tidak lagi berlaku)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `Siti Nurhaliza` sebagai pemilik System Log; isi log user itu bergantung pada aksi spec lain. Spec memakai user milik spec (`Aktor Log`) dengan aksi seed yang diketahui (S-06, S-11).
- Urutan TC dalam spec: TC-GS-USER-607, 608, 610, 611, 609. Alasan: TC-GS-USER-609 berakhir dengan sort Action A-Z aktif sehingga ditaruh terakhir; TC-GS-USER-610 mengubah visibilitas kolom dan dipulihkan di langkah 32 sebelum kasus berikutnya. Tab System Log dibuka sekali di langkah 3 untuk kelima TC.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 sampai 3 (membuka User Detail; Name dicari di User List), langkah 11 sampai 13, 20 sampai 22, dan 30 sampai 32 (melepas filter, mengosongkan Search, dan memulihkan kolom `Field` sebelum kasus berikutnya), serta langkah 42 sampai 43 (mengosongkan Search sebelum TC-GS-USER-609). Langkah 39 dan 47 adalah langkah TC (Clear filter).
- Langkah 7 dan 16 adalah anchor positif untuk asersi ketiadaan baris pada langkah 8, 9, 17, 18 (bagian 8b butir 2); langkah 34 adalah anchor untuk empty filtered state pada langkah 36 sampai 38; langkah 26 adalah anchor untuk langkah 27.
- Pembagian TC lintas spec: Search saja TC-GS-USER-591 sampai 597 di spec 096; Filter saja TC-GS-USER-598 sampai 606 di spec 097; Sort, Pagination, dan kombinasi empat kontrol TC-GS-USER-612 sampai 614, 629, 630 di spec 099.
- Asersi memakai pola baris (bukan jumlah baris), sehingga entri log dari run atau spec lain tidak memengaruhi hasil.
- Spec melewati sekitar 35 langkah (51 langkah) karena lima TC memakai kombinasi kontrol yang sama pada satu tab dan tiap klausa Expected menjadi satu `Verifikasi` (S-01). Semua blok satu kelas (kombinasi Search dan Filter Tab System Log), satu akun, satu dataset, dan tiap blok berdiri sendiri karena Search dan Filter dilepas di akhir tiap blok.
- Temuan untuk QA: (1) TC-GS-USER-607, 608, 611 menyebut "keyword" dan "filter" tanpa nilai; spec memakai Search `alfa` dengan Filter Action `Create` (607, 608), Filter Name `Target Beta` yang tidak beririsan dengan `alfa` (611). (2) TC-GS-USER-609 "Sort salah satu kolom" tidak menyebut kolom; spec memakai Action A-Z. (3) TC-GS-USER-610 "filter salah satu kolom" tidak menyebut kolom; spec memakai Field `Position` lalu menyembunyikan kolom `Field`. (4) TC-GS-USER-608 dan 610 Expected "Filter tetap aktif" tidak menyebut cara mengamati; spec memakai state icon Filter dan isi tabel. (5) TC-GS-USER-611 Expected a tidak menyebut teks empty filtered state; spec memakai teks TC-GS-USER-597.
