---
id: TC-AC-SG-E2E-091-absence-log-delete-cancel-skip-bulk-dan-diblok-dialog
title: "Absence Log Delete: Cancel, Skip pada Bulk, dan Diblok Dialog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-134
  - TC-AC-SG-331
  - TC-AC-SG-332
coverage:
  web: automated
---

# Absence Log Delete: Cancel, Skip pada Bulk, dan Diblok Dialog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Distributor Hapus Utama, `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net` (Pre-setup #21), password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Akses akun aktor ke Activity Log Admin Console tersedia (Pre-setup #40).
- Data milik spec (seed lewat Fixture BE di hook `before` pada entitas Distributor Hapus Utama; setiap nama bersuffix `{runId}-091`; Pre-setup #21 tidak diubah):
  - `Hapus Warn A {runId}-091` (tanpa entitas; Group Role `Manage partner` pada `Joko Susilo`, user Pre-setup #21; Group Role dipakai sebagai precondition TC, tidak diasersi) untuk TC-AC-SG-134.
  - `Hapus Campur 2 {runId}-091` (tanpa entitas) dan `Hapus Campur M2 {runId}-091` (satu Client Active `Client Campur {runId}-091`) untuk TC-AC-SG-331.
  - `Hapus Member A {runId}-091` (satu Client Active `Client Mawar {runId}-091`) untuk TC-AC-SG-332.
- Baseline audit trail permanen (kemampuan baca jumlah entri disediakan tim FE/BE): jumlah total entri Changelog Group (BC) dan jumlah entri Activity Log dengan saringan Object `Group` (BA) dicatat sebelum aksi pertama (TC-AC-SG-134); baseline kedua (BC2 dan BA2) dicatat ulang sebelum aksi pemicu TC-AC-SG-332. Entri milik spec dikenali lewat nama group bersuffix unik (baseline nol, S-12).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan; disediakan tim FE/BE). Hook `after` menghapus sisa data milik spec.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Baseline sebelum aksi

1. Klik ikon Changelog pada toolbar
2. Catat jumlah total entri Modal "Changelog: Group" sebagai BC
3. Tutup Modal Changelog dengan `✕`
4. Buka Activity Log Admin Console dan saring Object `Group`
5. Catat jumlah entri Activity Log sebagai BA
6. Buka halaman Settings > Group lewat sidebar
7. Ketik Search `{runId}-091`, tekan Enter

### TC-AC-SG-134: Cancel pada dialog warning tidak menghapus apa pun

8. Klik ikon `⋯` pada baris `Hapus Warn A {runId}-091` lalu `Delete`
9. Klik `[Cancel]` pada dialog Delete
10. Verifikasi dialog Delete tertutup
11. Verifikasi tidak ada toast
12. Verifikasi baris `Hapus Warn A {runId}-091` masih ada di tabel
13. Verifikasi node `Hapus Warn A {runId}-091` masih ada di Sidebar Group Tree
14. Klik ikon Changelog pada toolbar
15. Verifikasi jumlah total entri Modal "Changelog: Group" bertambah 0 dari BC
16. Tutup Modal Changelog dengan `✕`
17. Buka Activity Log Admin Console dan saring Object `Group`
18. Verifikasi jumlah entri Activity Log bertambah 0 dari BA

### TC-AC-SG-331: Group yang di-skip pada Bulk Delete campuran tidak menghasilkan entri

19. Buka halaman Settings > Group lewat sidebar
20. Ketik Search `{runId}-091`, tekan Enter
21. Centang kolom Checkbox pada baris `Hapus Campur 2 {runId}-091` dan `Hapus Campur M2 {runId}-091`
22. Pilih `Bulk Action` > `Delete` pada Bulk Actions Bar
23. Klik `[Continue]` pada dialog
24. Tunggu hingga entri log muncul
25. Klik ikon Changelog pada toolbar
26. Verifikasi Modal "Changelog: Group" memuat tepat 1 entri Delete untuk Group Name `Hapus Campur 2 {runId}-091`
27. Verifikasi Modal "Changelog: Group" tidak memuat entri untuk Group Name `Hapus Campur M2 {runId}-091`
28. Tutup Modal Changelog dengan `✕`

### TC-AC-SG-332: Aksi yang diblok dialog tidak menghasilkan entri log

29. Klik ikon Changelog pada toolbar
30. Catat jumlah total entri Modal "Changelog: Group" sebagai BC2
31. Tutup Modal Changelog dengan `✕`
32. Buka Activity Log Admin Console dan saring Object `Group`
33. Tunggu hingga entri Delete `Hapus Campur 2 {runId}-091` muncul pada Activity Log
34. Catat jumlah entri Activity Log sebagai BA2
35. Buka halaman Settings > Group lewat sidebar
36. Ketik Search `{runId}-091`, tekan Enter
37. Klik ikon `⋯` pada baris `Hapus Member A {runId}-091` lalu `Delete`
38. Klik `[OK]` pada dialog blok
39. Verifikasi baris `Hapus Member A {runId}-091` masih ada di tabel
40. Klik ikon Changelog pada toolbar
41. Verifikasi jumlah total entri Changelog bertambah 0 dari BC2 (tidak ada entri baru dari aksi yang diblok)
42. Verifikasi Modal "Changelog: Group" memuat entri Delete untuk Group Name `Hapus Campur 2 {runId}-091`
43. Tutup Modal Changelog dengan `✕`
44. Buka Activity Log Admin Console dan saring Object `Group`
45. Verifikasi jumlah entri Activity Log bertambah 0 dari BA2 (tidak ada entri baru dari aksi yang diblok)
46. Verifikasi Activity Log memuat entri Delete untuk Name `Hapus Campur 2 {runId}-091`

## Notes

- Kelas g (absence). Aksi nyata dan baseline sendiri ada di spec ini. Anchor positif tiap asersi absence: dialog Delete tertutup dan baris/node masih ada (TC-AC-SG-134), entri Delete `Hapus Campur 2 {runId}-091` pada surface yang sama (TC-AC-SG-331 dan TC-AC-SG-332), serta baseline agregat BC dan BA.
- TC-AC-SG-134 memakai `Verifikasi` tidak ada toast tepat setelah dialog tertutup dan sebelum asersi artefak (bagian 8b butir 11); dialog tertutup dan baris tetap ada menjadi anchor.
- TC-AC-SG-134 terbelah antara presence (dialog tertutup, baris tetap ada) dan absence (tanpa toast, tanpa entri log); keduanya ditulis di spec ini dengan aksi nyata (S-05).
- Langkah penghubung (S-03, R-16, tanpa `Verifikasi`): langkah 1 sampai 7 (baseline dan Search `{runId}-091` untuk menemukan baris target), langkah 19 dan 20, langkah 29 sampai 36 (baseline kedua BC2 dan BA2 sebelum aksi pemicu TC-AC-SG-332, S-12; langkah 33 menunggu entri TC-AC-SG-331 muncul di Activity Log agar BA2 sudah memuatnya), penutupan Modal Changelog, dan menunggu entri log muncul pada langkah 24 (pencatatan bersifat eventual).
- Urutan TC: TC-AC-SG-134 (Cancel) lebih dulu, lalu TC-AC-SG-331 (satu Delete sukses yang menjadi anchor bagi TC-AC-SG-332). Perubahan urutan terhadap bagian TC: TC-AC-SG-332 ditaruh sesudah TC-AC-SG-331 agar entri Delete milik TC-AC-SG-331 menjadi anchor positif.
- TC lain tentang pelepasan Group Role dan notifikasi in-app (TC-AC-SG-335, 336, 337) ada di spec 116.
- Temuan untuk QA:
  - TC-AC-SG-134 Expected "tidak ada entri log" tidak menyebut surface log; spec memakai Changelog dan Activity Log.
  - TC-AC-SG-332 Langkah Uji "Tunggu hingga entri log muncul" tidak mungkin dipenuhi untuk aksi yang tidak menulis entri; spec menunggu hingga entri Delete milik TC-AC-SG-331 tampil di surface yang sama sebagai penanda eventual selesai.
  - TC-AC-SG-331 Expected hanya menyebut Changelog; spec memeriksa Activity Log hanya pada TC-AC-SG-332 sesuai Expected TC itu.
- Alasan di atas sekitar 35 langkah: seluruh langkah satu topik (absence log Delete yang dibatalkan, di-skip, atau diblok) dan satu harness: baseline entri log dicatat per TC yang mengasersi selisih (BC dan BA sebelum TC-AC-SG-134, BC2 dan BA2 sebelum TC-AC-SG-332), lalu tiap blok membandingkannya; tiap blok berdiri sendiri pada group milik spec sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
