---
id: TC-AC-SG-E2E-094-sinkron-lintas-modul-setelah-delete-settings-user-tab-role-group-manager-list-dan-akses-history
title: "Sinkron Lintas Modul setelah Delete: Settings > User, Tab Role, Group Manager List, dan Akses History"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-344
  - TC-AC-SG-345
  - TC-AC-SG-346
  - TC-AC-SG-347
coverage:
  web: automated
---

# Sinkron Lintas Modul setelah Delete: Settings > User, Tab Role, Group Manager List, dan Akses History

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control entitas Distributor Hapus Utama, `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net` (Pre-setup #21), password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun di langkah 42): user `Lia Marlina` (Group Manager, Pre-setup #21). Email dan password akun ini tidak tertulis di Pre-setup TC; disediakan tim FE (lihat Temuan untuk QA).
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Akses akun aktor ke Settings > User (Sidebar Group, Detail user > Tab Role) dan Settings > Role & Permission (Tab Group Manager List) tersedia (Pre-setup #40).
- Data milik spec (seed lewat Fixture BE di hook `before` pada entitas Distributor Hapus Utama; setiap nama bersuffix `{runId}-094`; Pre-setup #21 tidak diubah):
  - TC-AC-SG-344: `Hapus Sinkron A {runId}-094` (tanpa entitas dan tanpa penugasan).
  - TC-AC-SG-345: `Hapus Sinkron B {runId}-094` (tanpa entitas; Group Role `Manage partner` pada `Joko Susilo`).
  - TC-AC-SG-346: `Hapus Sinkron C {runId}-094` dengan anak `Hapus Sinkron C Anak {runId}-094` (Group Manager `Lia Marlina` pada anak).
  - TC-AC-SG-347: `Hapus Sinkron D {runId}-094` dengan anak `Hapus Sinkron D Anak {runId}-094` (Group Manager `Lia Marlina` pada anak) beserta riwayat Approvals ber-scope Group Manager untuk `Hapus Sinkron D Anak {runId}-094`; seeding riwayat itu disediakan tim FE/BE.
- Kemampuan teknis: Fixture BE (seeding group, penugasan, riwayat Approvals; pemulihan; disediakan tim FE/BE). Hook `after` menghapus sisa data milik spec dan mengembalikan sesi ke akun aktor pertama.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-344: Group yang dihapus hilang dari Settings > User dan dropdown Select Group

1. Ketik Search `{runId}-094`, tekan Enter
2. Klik ikon `⋯` pada baris `Hapus Sinkron A {runId}-094` lalu `Delete`
3. Konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
4. Tunggu aksi selesai (dialog/popup tertutup)
5. Buka Settings > User lewat sidebar
6. Verifikasi Sidebar Group User List memuat `Default Group`
7. Verifikasi Sidebar Group User List tidak memuat `Hapus Sinkron A {runId}-094`
8. Buka Detail user `Joko Susilo` > Tab Role > Sub-tab Group Role
9. Klik `[Assign Group]` pada baris role `Manage partner`
10. Klik `[+ Assign Group]`
11. Verifikasi popup Select Group memuat `Default Group`
12. Verifikasi popup Select Group tidak memuat `Hapus Sinkron A {runId}-094`
13. Tutup popup Select Group dengan `✕`
14. Tutup popup Assign Group dengan `✕`

### TC-AC-SG-345: Penugasan Group Role user hilang dari Tab Role setelah group dihapus

15. Buka Settings > User > Detail `Joko Susilo` > Tab Role > Sub-tab Group Role
16. Catat daftar penugasan Group Role `Joko Susilo` sebagai baseline GR
17. Buka halaman Settings > Group lewat sidebar
18. Ketik Search `{runId}-094`, tekan Enter
19. Klik ikon `⋯` pada baris `Hapus Sinkron B {runId}-094` lalu `Delete`
20. Konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
21. Tunggu aksi selesai (dialog/popup tertutup)
22. Buka Settings > User > Detail `Joko Susilo` > Tab Role > Sub-tab Group Role
23. Verifikasi baris role `Manage partner` tampil pada Sub-tab Group Role
24. Verifikasi Tab Role `Joko Susilo` tidak memuat penugasan Group Role pada `Hapus Sinkron B {runId}-094`
25. Verifikasi daftar penugasan Group Role `Joko Susilo` sama dengan GR dikurangi penugasan pada `Hapus Sinkron B {runId}-094` (tidak dialihkan ke group lain)

### TC-AC-SG-346: Penugasan Group Manager hilang dari Tab Group Manager List dan banner GM

26. Buka halaman Settings > Group lewat sidebar
27. Ketik Search `{runId}-094`, tekan Enter
28. Klik ikon `⋯` pada baris `Hapus Sinkron C {runId}-094` lalu `Delete`
29. Konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
30. Tunggu aksi selesai (dialog/popup tertutup)
31. Buka Settings > Role & Permission > Tab Group Manager List
32. Verifikasi Tab Group Manager List tampil
33. Verifikasi Tab Group Manager List tidak memuat baris Group Manager `Lia Marlina` untuk `Hapus Sinkron C Anak {runId}-094`
34. Buka Settings > User > Detail `Lia Marlina`
35. Verifikasi Detail user `Lia Marlina` tampil
36. Verifikasi banner GM pada Detail user tidak menampilkan `Hapus Sinkron C Anak {runId}-094`

### TC-AC-SG-347: User yang kehilangan Group Manager kehilangan akses history ber-scope group yang dihapus

37. Buka halaman Settings > Group lewat sidebar
38. Ketik Search `{runId}-094`, tekan Enter
39. Klik ikon `⋯` pada baris `Hapus Sinkron D {runId}-094` lalu `Delete`
40. Konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
41. Tunggu aksi selesai (dialog/popup tertutup)
42. Ganti akun: Logout, lalu login sebagai `Lia Marlina`
43. Buka history Approvals untuk group `Hapus Sinkron D Anak {runId}-094`
44. Verifikasi halaman Approvals tampil
45. Verifikasi history ber-scope Group Manager untuk `Hapus Sinkron D Anak {runId}-094` tidak lagi dapat diakses (akses mengikuti assignment saat ini)

## Notes

- Langkah penghubung (S-03, R-16, tanpa `Verifikasi`): langkah 4, 21, 30, dan 41 (`Tunggu aksi selesai (dialog/popup tertutup)`, bagian 8b butir 8) menunggu dialog Delete tertutup sebelum surface berganti atau akun diganti; Search `{runId}-094` untuk menemukan baris target, membuka kembali Settings > Group lewat sidebar, konfirmasi Delete, serta menutup popup Select Group dan Assign Group dengan `✕` (langkah 13 dan 14; langkah 15 dan 16 membuka Sub-tab Group Role `Joko Susilo` dan mencatat baseline GR sebelum Delete, aksi tanpa `Verifikasi`, S-03 dan S-12; popup hanya dibuka dan tidak diubah sehingga tidak ada dialog `Unsaved Changes`).
- Absence (langkah 7, 12, 24, 25, 33, 36, 45) didahului `Verifikasi` anchor pada surface yang sama: `Default Group` (langkah 6 dan 11), baris role `Manage partner` (langkah 23), Tab Group Manager List dan Detail user tampil (langkah 32 dan 35), halaman Approvals tampil (langkah 44). Langkah 23, 32, 35, dan 44 ditambahkan sebagai anchor (S-03) dan bukan klausa Expected.
- Langkah 25 membandingkan daftar penugasan Group Role `Joko Susilo` dengan baseline GR (langkah 16) dikurangi penugasan pada `Hapus Sinkron B {runId}-094`; asersi tidak mengandaikan daftar absolut.
- Langkah 42 adalah ganti akun eksplisit (S-07); sesi dipulihkan ke akun aktor pertama di hook `after`. TC-AC-SG-347 ditaruh paling akhir karena berpindah akun.
- Spec ini 45 langkah. Alasan di atas sekitar 35 langkah: seluruh blok satu kelas harness (fungsional lintas modul di backend nyata) dan berdiri sendiri; tiap blok memakai group milik spec sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Empat blok membuka surface yang berbeda sehingga langkah navigasi tidak dapat digabung.
- TC-AC-SG-344 sampai 347 menarget node Pre-setup `Hapus Warn A` dan `Hapus Warn B`; spec memakai node milik spec (S-06). TC-AC-SG-347 berstatus Automation `Manual Only` di TC sumber.
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email atau password akun `Lia Marlina` (hanya nama user pada Pre-setup #21); TC-AC-SG-347 langkah 3 menuntut login sebagai `Lia Marlina`.
  - TC-AC-SG-344 menyebut "popup Select Group" tanpa menyebut jalur dan user pembukanya; spec memakai Detail user `Joko Susilo` > Tab Role > Group Role > `[Assign Group]` > `[+ Assign Group]` dan tidak menyimpan.
  - TC-AC-SG-347 Langkah Uji tidak menyebut letak "history Approvals" dan Expected tidak menyebut tampilan saat tidak dapat diakses (pesan, halaman kosong, atau 403); spec mengasersi tidak dapat diakses secara umum.
  - Persyaratan seed riwayat Approvals ber-scope Group Manager untuk group yang dihapus tidak ada di Pre-setup #21.
