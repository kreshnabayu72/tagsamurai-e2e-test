---
id: TC-AC-SG-E2E-102-konkurensi-dua-admin-target-sudah-dihapus-admin-lain-add-subgroup-edit-delete-dan-bulk
title: "Konkurensi Dua Admin: Target Sudah Dihapus Admin Lain pada Add Subgroup, Edit, Delete, dan Bulk Delete"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-385
  - TC-AC-SG-386
  - TC-AC-SG-387
  - TC-AC-SG-388
  - TC-AC-SG-389
coverage:
  web: automated
---

# Konkurensi Dua Admin: Target Sudah Dihapus Admin Lain pada Add Subgroup, Edit, Delete, dan Bulk Delete

## Prerequisites

- Mode: FE+BE.
- Sesi A (akun aktor pertama, sesi UI): Total Control entitas Distributor Race, `totalControlRaceA_automated_{namaCompany}@qwertysystem.net` (Pre-setup #32), password `Spectra.env.AC_SG_RACEA_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Sesi B (sesi API aktor, hanya memicu penghapusan; Pre-setup #39): Total Control entitas Distributor Race, `totalControlRaceB_automated_{namaCompany}@qwertysystem.net` (Pre-setup #32), password `Spectra.env.AC_SG_RACEB_PASSWORD`. Login API (password) memakai token yang tidak dihitung sebagai sesi web sehingga sesi UI Sesi A tidak terusir (suite.md).
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE di hook `before` pada entitas Distributor Race, dihapus atau dipulihkan hook `after`; setiap nama bersuffix `{runId}-102`; Pre-setup #32 tidak diubah). Tiap TC memakai node sendiri sehingga tidak ada pemulihan antar blok:
  - TC-AC-SG-385: `Race Lain Satu {runId}-102` (level 1, tanpa entitas).
  - TC-AC-SG-386: `Race Lain Dua {runId}-102` (level 1, tanpa entitas).
  - TC-AC-SG-387: `Race Lain Tiga {runId}-102` (level 1, tanpa entitas).
  - TC-AC-SG-388: `Race Induk Empat {runId}-102` dan `Race Lain Empat {runId}-102` (level 1, tanpa entitas).
  - TC-AC-SG-389: `Race Induk Lima {runId}-102` dengan anak `Race Induk Anak Lima {runId}-102`, dan `Race Lain Lima {runId}-102` (level 1, tanpa entitas).
- Baseline audit trail permanen: entri Changelog dikenali lewat nama group bersuffix unik (baseline nol, S-12); kemampuan baca disediakan tim FE/BE.
- Kemampuan teknis: Fixture BE dan sesi API aktor untuk memicu penghapusan oleh Sesi B (disediakan tim FE/BE tanpa endpoint karangan di spec).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-385: Add Subgroup pada parent yang sudah dihapus admin lain

1. Pada Sesi A, klik ikon `⋯` pada node `Race Lain Satu {runId}-102` di sidebar lalu `+ Add Subgroup`
2. Pada Sesi A, ketik `Anak Satu {runId}-102` pada popup Add Subgroup
3. Pada Sesi B (API), hapus `Race Lain Satu {runId}-102` hingga terhapus
4. Pada Sesi A, klik `[Submit]`
5. Verifikasi popup Add Subgroup ditutup
6. Verifikasi toast netral: "This group is no longer available."
7. Verifikasi Sidebar Group Tree Sesi A di-refresh dan tidak memuat `Race Lain Satu {runId}-102`

### TC-AC-SG-386: Edit node yang sudah dihapus admin lain

8. Pada Sesi A, klik ikon `⋯` pada node `Race Lain Dua {runId}-102` di sidebar lalu `Edit`
9. Pada Sesi A, ubah nama menjadi `Race Lain Dua Ubah {runId}-102`
10. Pada Sesi B (API), hapus `Race Lain Dua {runId}-102` hingga terhapus
11. Pada Sesi A, klik `[Save]`
12. Verifikasi popup Edit Group ditutup
13. Verifikasi toast netral: "This group is no longer available."
14. Verifikasi Sidebar Group Tree Sesi A di-refresh dan tidak memuat `Race Lain Dua {runId}-102`

### TC-AC-SG-387: Delete node yang sudah dihapus admin lain

15. Pada Sesi A, klik node `Race Lain Tiga {runId}-102` di Sidebar Group Tree
16. Pada Sesi A, ketik Search `x`, tekan Enter
17. Pada Sesi A, klik ikon `⋯` pada node `Race Lain Tiga {runId}-102` di sidebar lalu `Delete`
18. Pada Sesi B (API), hapus `Race Lain Tiga {runId}-102` hingga terhapus
19. Pada Sesi A, klik `[Delete]` pada dialog
20. Verifikasi dialog Delete ditutup
21. Verifikasi toast netral: "This group is no longer available."
22. Verifikasi tidak ada toast sukses
23. Verifikasi Sidebar Group Tree Sesi A di-refresh dan tidak memuat `Race Lain Tiga {runId}-102`
24. Verifikasi seleksi sidebar kembali ke `All Groups`
25. Verifikasi Search, Filter, Sort, dan halaman Sesi A kembali ke default

### TC-AC-SG-388: Sebagian item bulk sudah dihapus admin lain: dilewati tanpa pesan terpisah, toast campuran

26. Pada Sesi A, tunggu toast lama hilang otomatis
27. Pada Sesi A, ketik Search `{runId}-102`, tekan Enter
28. Pada Sesi A, centang kolom Checkbox pada baris `Race Induk Empat {runId}-102` dan `Race Lain Empat {runId}-102`
29. Pada Sesi A, pilih `Bulk Action` > `Delete` pada Bulk Actions Bar sehingga dialog Delete Groups terbuka
30. Pada Sesi B (API), hapus `Race Lain Empat {runId}-102` hingga terhapus
31. Pada Sesi A, klik `[Delete]` pada dialog
32. Verifikasi toast campuran: "Success, group has been deleted. Some items were skipped."
33. Verifikasi `Race Induk Empat {runId}-102` terhapus (tidak ada di Sidebar Group Tree dan tabel)
34. Verifikasi `Race Lain Empat {runId}-102` dilewati tanpa pesan terpisah (hanya satu toast, yaitu toast campuran)
35. Pada Sesi A, klik ikon Changelog pada toolbar
36. Verifikasi Modal "Changelog: Group" memuat tepat 1 entri Delete untuk Group Name `Race Lain Empat {runId}-102` (milik penghapusan Sesi B; batch Sesi A tidak menambah entri)
37. Pada Sesi A, tutup Modal Changelog dengan `✕`

### TC-AC-SG-389: Seluruh item bulk sudah dihapus admin lain

38. Pada Sesi A, tunggu toast lama hilang otomatis
39. Pada Sesi A, ganti isi kotak search dengan `{runId}-102`, tekan Enter
40. Pada Sesi A, centang kolom Checkbox pada baris `Race Induk Anak Lima {runId}-102` dan `Race Lain Lima {runId}-102`
41. Pada Sesi A, pilih `Bulk Action` > `Delete` pada Bulk Actions Bar sehingga dialog Delete Groups terbuka
42. Pada Sesi B (API), hapus `Race Induk Anak Lima {runId}-102` dan `Race Lain Lima {runId}-102` hingga terhapus
43. Pada Sesi A, klik `[Delete]` pada dialog
44. Verifikasi toast netral: "This group is no longer available."
45. Verifikasi Sidebar Group Tree Sesi A di-refresh dan tidak memuat `Race Induk Anak Lima {runId}-102` dan `Race Lain Lima {runId}-102`

## Notes

- Kelas c (multi-konteks, dua admin). Sesi B hanya memicu penghapusan lewat sesi API dan seluruh hasil diasersi di Sesi A, sehingga konteks kedua UI tidak dipakai dan butir P-2 tidak diperlukan (bagian 3 prinsip 13, P-2 `[KEPUTUSAN 2026-10-30]`).
- Langkah penghubung (S-03, R-16, tanpa `Verifikasi`): langkah 16, 26, 27, 38, dan 39 (Search untuk menemukan baris target atau menyiapkan seleksi, termasuk menunggu toast lama hilang agar toast berulang diasersi sebagai toast baru, R-12).
- Absence (langkah 7, 14, 22, 23, 33, 34, 36, dan 45) didahului `Verifikasi` toast netral atau toast campuran pada surface yang sama sebagai anchor positif (respons server sudah diproses, bagian 8b butir 2); pada TC-AC-SG-385 dan TC-AC-SG-386 toast netral (langkah 6 dan 13) ditaruh sebelum asersi tree.
- P-1: klausa "tanpa entri log" pada TC-AC-SG-388 (langkah 36) bergantung pada state kontensi yang dibangun Sesi B pada langkah 30 dan tidak dapat diulang di spec absence; ditulis sebagai `Verifikasi` berbaseline nama bersuffix unik (S-05).
- Alasan di atas sekitar 35 langkah: seluruh blok satu kelas harness (kelas c, dua admin pada satu entitas), berdiri sendiri, dan memakai node sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pemisahan akan mengulang login dan seeding yang sama.
- Hook `after` memulihkan pohon Distributor Race lewat Fixture BE.
- Temuan untuk QA:
  - TC-AC-SG-385 dan TC-AC-SG-386 tidak menyebut nama yang diketik pada popup Add Subgroup dan Edit; spec mengetik nama baru karena `[Submit]` dan `[Save]` tanpa perubahan akan memicu respons lain (nama wajib; "No changes to save.").
  - TC-AC-SG-387 Langkah Uji mengetik "x" pada Search tabel sebelum membuka dialog Delete; Search tidak diberi Enter secara eksplisit di TC, spec menambah Enter menurut aturan Search.
  - TC-AC-SG-388 Expected "tanpa entri log" untuk `Race Lain` tidak menyatakan bahwa penghapusan Sesi B tetap menulis satu entri Delete; spec mengasersi tepat 1 entri Delete untuk nama itu.
