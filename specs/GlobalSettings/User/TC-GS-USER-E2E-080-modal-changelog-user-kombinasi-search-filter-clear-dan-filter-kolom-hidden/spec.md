---
id: TC-GS-USER-E2E-080-modal-changelog-user-kombinasi-search-filter-clear-dan-filter-kolom-hidden
title: "Modal Changelog User: Kombinasi Search dan Filter, Clear Filter saat Search dan Sort Aktif, Filter Kolom Hidden, dan Nol Baris"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-486
  - TC-GS-USER-487
  - TC-GS-USER-488
  - TC-GS-USER-489
  - TC-GS-USER-490
coverage:
  web: automated
---

# Modal Changelog User: Kombinasi Search dan Filter, Clear Filter saat Search dan Sort Aktif, Filter Kolom Hidden, dan Nol Baris

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2); kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite: login di hook `before`, hook `after` mengembalikan sesi ke akun ini. Nama singkat di kolom Modified By: `Siti N` (tooltip `Siti Nurhaliza`). Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role, Full CRUD (Fajar Nugroho), `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4); kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`. Dipakai hanya untuk memicu entri Changelog dengan Modified By kedua `Fajar N` (nama singkat dibentuk seperti `Siti N`; TC tidak menyebutnya), sehingga kolom Modified By punya sedikitnya dua nilai distinct (S-11). Tidak ada sesi UI kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Seeding minimal (S-11; lewat API di hook `before`, berurutan; kemampuan seeding user dan perubahan user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD. Tiap user seed diberi Position `Staff` (Tabel Data Uji Pre-setup No. 22), Division `Finance` (No. 23), dan Access `Fixed Asset` (No. 26), email `<nama>+{runId}-080@qwertysystem.net`. Kuota user plan cukup untuk user seed milik spec ini (disediakan tim FE). Hanya data yang dipakai `Verifikasi` yang di-seed; Modified By dan Action punya sedikitnya dua nilai distinct):
  - U-1: Create `Alfa {runId}-080` oleh Siti Nurhaliza (Action Create, Modified By `Siti N`), lalu Edit Position `Staff` menjadi `Supervisor` oleh Siti Nurhaliza (Action Edit).
  - U-2: Create `Beta {runId}-080` oleh Fajar Nugroho (Action Create, Modified By `Fajar N`), lalu Deactivate oleh Siti Nurhaliza (Action Deactivate).
  - Search `{runId}-080` mencocokkan kolom User Name dan hanya mengembalikan empat entri seed di atas (Create `Alfa`, Edit `Alfa`, Create `Beta`, Deactivate `Beta`), sehingga irisan dengan Filter dapat diasersi tepat.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1 dan U-2 bila masih ada; kembalikan sesi ke akun default suite; hapus konfigurasi kolom Modal Changelog User di `localStorage` bila tersisa. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: kontrol date range picker (rentang 1 Jan 2020 sampai 31 Jan 2020); klik header kolom sort.
- Precondition TC-GS-USER-486 sampai 490: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); riwayat Changelog terisi.
- Suite serial (`parallel: false`). Changelog bersifat append-only dan dipakai bersama spec lain: asersi memakai pola baris (nilai bersuffix `{runId}-080`), bukan jumlah baris total, kecuali dinyatakan lain. Spec ini tidak mengubah atau menghapus data Pre-setup (S-06).
- State global yang diubah: konfigurasi kolom Modal Changelog User (TC-GS-USER-489 menyembunyikan `Modified By`, dipulihkan di langkah 46).

## Test Steps

### TC-GS-USER-486: Search lalu Filter menghasilkan irisan
1. Klik icon Changelog di Table Tools
2. Klik icon Search, ketik `{runId}-080`, tekan Enter
3. Verifikasi baris Create `Beta {runId}-080` (Modified By `Fajar N`) tampil sebelum Filter diterapkan
4. Klik icon Filter, pilih opsi `Siti N` pada Modified By, klik `[Apply]`
5. Verifikasi hasil = Search ∩ Filter: tabel memuat tepat tiga baris, yaitu Create `Alfa {runId}-080`, Edit `Alfa {runId}-080`, dan Deactivate `Beta {runId}-080`, semuanya Modified By `Siti N`
6. Verifikasi baris Create `Beta {runId}-080` (Modified By `Fajar N`) tidak tampil
7. Verifikasi keyword Search tidak ter-reset (input Search berisi `{runId}-080`)
### TC-GS-USER-487: Filter lalu Search menghasilkan irisan
8. Klik `[✕]` untuk menutup Modal Changelog
9. Klik icon Changelog di Table Tools
10. Klik icon Filter, pilih opsi `Fajar N` pada Modified By, klik `[Apply]`
11. Klik icon Search, ketik `{runId}-080`, tekan Enter
12. Verifikasi hasil = Filter ∩ Search: tabel memuat tepat satu baris, yaitu Create `Beta {runId}-080`
### TC-GS-USER-488: Clear filter saat Search dan Sort aktif
13. Klik `[✕]` untuk menutup Modal Changelog
14. Klik icon Changelog di Table Tools
15. Klik icon Search, ketik `{runId}-080`, tekan Enter
16. Klik header Action
17. Klik icon Filter, pilih opsi `Fajar N` pada Modified By, klik `[Apply]`
18. Verifikasi tabel memuat tepat satu baris, yaitu Create `Beta {runId}-080` (filter berlaku)
19. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
20. Verifikasi keyword Search tetap aktif (input Search berisi `{runId}-080`)
21. Verifikasi sort Action ascending tetap aktif (urutan Action dari atas: `Create`, `Create`, `Deactivate`, `Edit`)
22. Verifikasi filter terlepas (tabel memuat empat baris, termasuk Create `Beta {runId}-080` dengan Modified By `Fajar N`)
### TC-GS-USER-490: Kombinasi Search dan Filter menghasilkan 0 baris lalu pulih saat filter dilepas
23. Klik `[✕]` untuk menutup Modal Changelog
24. Klik icon Changelog di Table Tools
25. Klik icon Search, ketik `{runId}-080`, tekan Enter
26. Verifikasi tabel memuat empat baris hasil Search (Create dan Edit `Alfa {runId}-080`, Create dan Deactivate `Beta {runId}-080`)
27. Klik icon Filter, pilih rentang tanggal 1 Jan 2020 sampai 31 Jan 2020 pada Date, klik `[Apply]`
28. Verifikasi Ilustrasi empty filtered state tampil
29. Verifikasi Title `No results found`
30. Verifikasi Description `Try adjusting your search or filter.`
31. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
32. Verifikasi baris hasil Search tampil kembali (tabel memuat empat baris, Create dan Edit `Alfa {runId}-080`, Create dan Deactivate `Beta {runId}-080`)
### TC-GS-USER-489: Filter tetap tersedia untuk kolom yang di-hide
33. Klik `[✕]` untuk menutup Modal Changelog
34. Klik icon Changelog di Table Tools
35. Verifikasi baris Create `Alfa {runId}-080` (Modified By `Siti N`) dan Create `Beta {runId}-080` (Modified By `Fajar N`) tampil sebelum Filter diterapkan
36. Klik icon Filter, pilih opsi `Fajar N` pada Modified By, klik `[Apply]`
37. Klik header Column Visibility (⋯), hilangkan centang `Modified By` pada overlay
38. Tutup overlay Column Visibility
39. Verifikasi kolom `Modified By` tidak tampil di tabel
40. Verifikasi filter tetap aktif menyaring: baris Create `Beta {runId}-080` tampil
41. Verifikasi filter tetap aktif menyaring: baris Create `Alfa {runId}-080` tidak tampil
42. Klik icon Filter
43. Verifikasi field `Modified By` tetap ada di Filter Panel
44. Tutup Filter Panel
45. Klik header Column Visibility (⋯), centang kembali `Modified By` pada overlay
46. Tutup overlay Column Visibility

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-USER-486, 487, 488, 490, 489. Alasan: TC-GS-USER-489 menyembunyikan kolom (mengubah konfigurasi kolom) sehingga di akhir (bagian 3 konvensi); empat TC lain tidak mengubah konfigurasi kolom. Tiap TC membuka Modal Changelog sendiri supaya Search, Filter, dan Sort TC sebelumnya tidak terbawa (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): `Klik [✕] untuk menutup Modal Changelog` lalu `Klik icon Changelog` di awal TC-GS-USER-487, 488, 490, dan 489; menutup overlay Column Visibility dan Filter Panel; mengembalikan `Modified By` ke tampil pada akhir TC-GS-USER-489. Langkah `[Clear Field]` + `[Apply]` pada TC-GS-USER-488 dan 490 adalah langkah TC.
- Langkah tambahan atas TC (S-03): `Search {runId}-080` pada TC-GS-USER-486 sampai 490 membatasi baris yang diamati ke entri seed spec ini sehingga irisan dapat diasersi tepat; `Verifikasi` baris sebelum Filter diterapkan adalah pembanding untuk ketiadaan baris dan penyaringan.
- Pembagian TC Modal Changelog User: screening dan Search ada di spec 078, Filter Panel ada di spec 079, Sort dan Pagination ada di spec 081, Setup Column ada di spec 082, Download ada di spec 083.
- Spec melewati sekitar 35 langkah (46 langkah) karena lima TC masing-masing memasang Search, Filter, dan Sort sendiri pada modal baru dan tiap klausa Expected menjadi satu `Verifikasi` (S-01); semua blok satu layar (Modal Changelog User), satu akun aktor, dan satu dataset seed, serta tiap blok berdiri sendiri karena modal ditutup dan dibuka ulang di antara blok.
- Temuan untuk QA: (1) TC-GS-USER-486, 487, 488, dan 489 menyebut "filter" atau "salah satu kolom" tanpa field dan nilainya; spec memakai Modified By `Siti N` (486) dan `Fajar N` (487, 488, 489). (2) TC-GS-USER-488 tidak menyebut kolom yang di-sort; spec memakai Action. (3) TC-GS-USER-490 "filter yang tidak beririsan" tidak menyebut filternya; spec memakai rentang Date 1 Jan 2020 sampai 31 Jan 2020. (4) TC-GS-USER-489 "hide kolom tersebut" dilakukan lewat overlay Column Visibility; TC tidak menyebut apakah lewat overlay atau Setup Column. (5) TC-GS-USER-488 tidak menyebut tiga kontrol aktif di langkah mana Search diketik; spec mengikuti urutan Search, Sort, Filter.
