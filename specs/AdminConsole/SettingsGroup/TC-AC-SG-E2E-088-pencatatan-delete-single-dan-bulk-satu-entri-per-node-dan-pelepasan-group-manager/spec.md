---
id: TC-AC-SG-E2E-088-pencatatan-delete-single-dan-bulk-satu-entri-per-node-dan-pelepasan-group-manager
title: "Pencatatan Delete Single dan Bulk: Satu Entri per Node dan per Group, Pelepasan Group Manager"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-329
  - TC-AC-SG-330
  - TC-AC-SG-333
  - TC-AC-SG-334
coverage:
  web: automated
---

# Pencatatan Delete Single dan Bulk: Satu Entri per Node dan per Group, Pelepasan Group Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Distributor Hapus Utama, `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net` (Pre-setup #21), password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Akses akun aktor ke Activity Log Admin Console, Settings > User (Detail user > Changelog: User, Detail akun aktor > Tab System Log), dan Settings > Role & Permission > Changelog Group Manager tersedia (Pre-setup #40).
- Data milik spec (seed lewat Fixture BE di hook `before` pada entitas Distributor Hapus Utama; setiap nama bersuffix `{runId}-088`; Pre-setup #21 tidak diubah):
  - TC-AC-SG-329: `Hapus Warn B {runId}-088` dengan anak `Hapus Warn B1 {runId}-088` dan `Hapus Warn B2 {runId}-088`, semuanya tanpa entitas dan tanpa penugasan.
  - TC-AC-SG-330: `Hapus Bulk 1 {runId}-088` dan `Hapus Bulk 2 {runId}-088`, tanpa entitas.
  - TC-AC-SG-333: `Hapus GM Satu {runId}-088` dengan anak `Hapus GM Satu Anak {runId}-088`; Group Manager `Lia Marlina` (user Pre-setup #21) ditugaskan pada `Hapus GM Satu Anak {runId}-088`.
  - TC-AC-SG-334: `Hapus GM Dua {runId}-088` dengan anak `Hapus GM Dua Anak {runId}-088`; Group Manager `Lia Marlina` ditugaskan pada `Hapus GM Dua Anak {runId}-088`.
- Changelog, Activity Log, dan System Log adalah audit trail permanen: entri dikenali lewat nama group bersuffix unik (baseline nol, S-12); jumlah entri Changelog total (TC-AC-SG-330) serta Activity Log dan System Log untuk Object `Group Manager (Group Deleted)` (TC-AC-SG-334) dibandingkan terhadap baseline yang dicatat per TC sebelum aksi pemicu TC itu (kemampuan baca jumlah entri disediakan tim FE/BE).
- Kemampuan teknis: Fixture BE (seeding group dan penugasan Group Manager, pemulihan baseline entitas Distributor Hapus Utama; disediakan tim FE/BE). Hook `after` menghapus sisa data milik spec.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-329: Delete single dengan cascade mencatat satu entri per node yang terhapus

1. Ketik Search `{runId}-088`, tekan Enter
2. Klik ikon `⋯` pada baris `Hapus Warn B {runId}-088` lalu `Delete`
3. Konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
4. Tunggu hingga entri log muncul
5. Klik ikon Changelog pada toolbar
6. Verifikasi Modal "Changelog: Group" menambah tepat 3 entri Delete untuk Group Name `Hapus Warn B {runId}-088`, `Hapus Warn B1 {runId}-088`, dan `Hapus Warn B2 {runId}-088`
7. Verifikasi tiap entri itu memiliki Field `Group Name`, Old Value berupa nama group yang dihapus, dan New Value `—`
8. Tutup Modal Changelog dengan `✕`
9. Buka Activity Log Admin Console dan saring Object `Group`
10. Verifikasi Activity Log mencatat 3 entri Delete dengan kolom Name `Hapus Warn B {runId}-088`, `Hapus Warn B1 {runId}-088`, dan `Hapus Warn B2 {runId}-088` (nama leaf)
11. Hover kolom Name entri Delete `Hapus Warn B1 {runId}-088`
12. Verifikasi tooltip menampilkan snapshot full path `Hapus Warn B {runId}-088 > Hapus Warn B1 {runId}-088`
13. Buka Settings > User > Detail akun aktor > Tab System Log
14. Verifikasi System Log aktor mencatat 3 entri Delete dengan kolom Name `Hapus Warn B {runId}-088`, `Hapus Warn B1 {runId}-088`, dan `Hapus Warn B2 {runId}-088` (nama leaf)

### TC-AC-SG-330: Bulk Delete mencatat satu entri per group yang berhasil dihapus

15. Buka Settings > Group lewat sidebar
16. Klik ikon Changelog pada toolbar
17. Catat jumlah total entri Modal "Changelog: Group" sebagai baseline
18. Tutup Modal Changelog dengan `✕`
19. Ketik Search `{runId}-088`, tekan Enter
20. Centang kolom Checkbox pada baris `Hapus Bulk 1 {runId}-088` dan `Hapus Bulk 2 {runId}-088`
21. Pilih `Bulk Action` > `Delete` pada Bulk Actions Bar, lalu konfirmasi dengan `[Delete]` pada dialog
22. Tunggu hingga entri log muncul
23. Klik ikon Changelog pada toolbar
24. Verifikasi jumlah total entri bertambah tepat 2 dari baseline (tidak ada entri gabungan)
25. Verifikasi Modal "Changelog: Group" memuat satu entri Delete untuk `Hapus Bulk 1 {runId}-088` dan satu entri Delete untuk `Hapus Bulk 2 {runId}-088`
26. Tutup Modal Changelog dengan `✕`

### TC-AC-SG-333: Pelepasan Group Manager akibat Delete dicatat di Changelog Group Manager

27. Buka Settings > Group lewat sidebar, lalu ketik Search `{runId}-088`, tekan Enter
28. Klik ikon `⋯` pada baris `Hapus GM Satu {runId}-088` lalu `Delete`
29. Konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
30. Tunggu hingga entri log muncul
31. Buka Settings > Role & Permission > Changelog Group Manager
32. Verifikasi Changelog Group Manager memuat entri baru dengan Action `Remove (Group Deleted)` dan kolom `Lia Marlina — Hapus GM Satu Anak {runId}-088`
33. Verifikasi entri itu memiliki Field `Group Manager`, Old Value `Assigned`, New Value `—`, dan pelaku akun aktor spec ini (admin yang menghapus group)

### TC-AC-SG-334: Pelepasan Group Manager juga dicatat di Changelog: User, System Log, dan Activity Log

34. Buka Activity Log Admin Console dan saring Object `Group Manager (Group Deleted)`
35. Tunggu hingga entri log muncul
36. Catat jumlah entri Action `Remove` untuk Object `Group Manager (Group Deleted)` sebagai baseline Activity Log TC-AC-SG-334
37. Buka Settings > User > Detail akun aktor > Tab System Log
38. Catat jumlah entri Action `Remove` untuk Object `Group Manager (Group Deleted)` sebagai baseline System Log TC-AC-SG-334
39. Buka Settings > Group lewat sidebar, lalu ketik Search `{runId}-088`, tekan Enter
40. Klik ikon `⋯` pada baris `Hapus GM Dua {runId}-088` lalu `Delete`
41. Konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
42. Tunggu hingga entri log muncul
43. Buka Activity Log Admin Console dan saring Object `Group Manager (Group Deleted)`
44. Verifikasi jumlah entri Action `Remove` untuk Object `Group Manager (Group Deleted)` pada Activity Log bertambah 1 dari baseline Activity Log TC-AC-SG-334
45. Buka Settings > User > Detail `Lia Marlina` > Changelog: User
46. Verifikasi Changelog: User `Lia Marlina` memuat entri Action `Remove (Group Deleted)`, Field `Group Manager — Hapus GM Dua Anak {runId}-088`, Old Value `Assigned`, New Value `—`
47. Buka Settings > User > Detail akun aktor > Tab System Log
48. Verifikasi jumlah entri Action `Remove` untuk Object `Group Manager (Group Deleted)` pada System Log aktor bertambah 1 dari baseline System Log TC-AC-SG-334
49. Verifikasi entri terbaru pada System Log aktor bernama `Lia Marlina`

## Notes

- Langkah penghubung (S-03, R-16, tanpa `Verifikasi`): Search `{runId}-088` untuk menemukan baris target, membuka kembali Settings > Group lewat sidebar, mencatat baseline, menutup Modal Changelog dengan `✕`, dan menunggu entri log muncul (pencatatan bersifat eventual).
- Cara baca beberapa entri di menit yang sama (TC-AC-SG-329 dan TC-AC-SG-330): kolom Date berketelitian menit sehingga urutan entri dalam satu menit tidak dijamin; entri dikenali lewat nama group bersuffix unik, bukan posisi baris. Pada tiap blok, `Verifikasi` selisih jumlah entri ditulis sebelum membaca isi entri; di TC-AC-SG-334 asersi Activity Log (langkah 43 dan 44) mendahului isi Changelog: User (langkah 45 dan 46) agar selisih jumlah terbaca lebih dulu.
- Cara baca entri satu menit di audit trail (TC-AC-SG-333 dan TC-AC-SG-334): entri yang tercatat dalam menit yang sama dibaca sebagai himpunan baris teratas urutan bawaan Date terbaru, sebanyak selisih jumlah yang sudah dibuktikan; entri dikenali lewat nama unik, bukan posisi baris. TC-AC-SG-333 dan TC-AC-SG-334 memakai nama yang sama (`Lia Marlina`), sehingga tiap blok dibaca setelah selisih jumlahnya sendiri (langkah 32 dan 33 sesudah entri baru TC-AC-SG-333; langkah 44 dan 48 sesudah selisih +1 TC-AC-SG-334).
- Urutan TC: semua TC adalah Delete; hasilnya tidak dipakai TC lain sehingga TC-AC-SG-333 dan TC-AC-SG-334 yang memakai nama `Lia Marlina` yang sama ditaruh berurutan. Tiap TC mencatat baseline sendiri: baseline Activity Log dan System Log TC-AC-SG-334 dicatat sesudah Delete TC-AC-SG-333 selesai (langkah 34 sampai 38, langkah 35 menunggu entri TC-AC-SG-333 muncul) dan sebelum Delete TC-AC-SG-334 (langkah 40 dan 41), sehingga selisihnya +1 hanya berasal dari TC-AC-SG-334.
- Alasan di atas sekitar 35 langkah: seluruh langkah satu topik (pencatatan Delete) dan satu harness (empat surface audit trail); kegagalan satu blok tidak menghilangkan makna blok lain. Langkah baca-log berpola (buka surface, saring, `Verifikasi` kolom log) terjadi di langkah 5 sampai 14, 16 sampai 18, 23 sampai 26, 31 sampai 33, 34 sampai 38, dan 43 sampai 49 dan tidak dihitung menurut bagian 3 (prinsip 13, Smell); tanpa blok itu langkah inti kurang dari 35.
- Penugasan Group Role dan Group Manager pada group milik spec memakai user Pre-setup `Lia Marlina` (Group Manager); penugasan itu di-seed Fixture BE dan terlepas oleh Delete.
- Group Role `Nina Amelia` pada `Hapus Warn B` (TC-AC-SG-335) dan TC lain tentang pelepasan Group Role ada di spec 091.
- Temuan untuk QA:
  - TC-AC-SG-329 Expected butir b menuntut System Log aktor, tetapi Langkah Uji hanya membuka Activity Log; spec menambah langkah membuka Tab System Log berdasarkan Expected.
  - Nama tampil akun Total Control Distributor Hapus Utama tidak tertulis di Pre-setup #21; pelaku pada TC-AC-SG-333 ditulis sebagai akun aktor spec ini.
  - TC-AC-SG-334 Expected butir b tidak menyebut jumlah entri; spec mengasersi selisih +1 terhadap baseline yang dicatat sesudah Delete TC-AC-SG-333 (satu pelepasan oleh TC-AC-SG-334) karena nama `Lia Marlina` dipakai kedua TC.
  - TC-AC-SG-330 dan TC-AC-SG-333 menulis "hapus lewat Bulk Actions Bar" dan "konfirmasi" tanpa label tombol dialog; spec memakai `Bulk Action` > `Delete` dan `[Delete]` menurut catatan TC (header TC, Bulk Actions Bar PRD §4.2).
