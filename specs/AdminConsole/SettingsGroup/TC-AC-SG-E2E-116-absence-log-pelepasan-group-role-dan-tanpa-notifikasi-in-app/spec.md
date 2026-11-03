---
id: TC-AC-SG-E2E-116-absence-log-pelepasan-group-role-dan-tanpa-notifikasi-in-app
title: "Absence Log Pelepasan Group Role akibat Delete dan Tanpa Notifikasi In-App"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-335
  - TC-AC-SG-336
  - TC-AC-SG-337
coverage:
  web: automated
---

# Absence Log Pelepasan Group Role akibat Delete dan Tanpa Notifikasi In-App

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control entitas Distributor Hapus Utama, `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net` (Pre-setup #21), password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua dan ketiga (ganti akun pada TC-AC-SG-337): user `Nina Amelia` dan user `Lia Marlina` (Pre-setup #21). Email dan password kedua akun tidak tertulis di Pre-setup TC; disediakan tim FE (lihat Temuan untuk QA).
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Akses akun aktor ke Activity Log Admin Console dan ke Settings > User (Detail user > Tab Role dan Changelog: User, Detail akun aktor > Tab System Log) tersedia (Pre-setup #40).
- Data milik spec (seed lewat Fixture BE di hook `before` pada entitas Distributor Hapus Utama; setiap nama bersuffix `{runId}-116`; Pre-setup #21 tidak diubah):
  - `Hapus Warn B {runId}-116` (tanpa entitas; Group Role `Manage partner` pada `Nina Amelia`) untuk TC-AC-SG-335.
  - `Hapus Warn A {runId}-116` (tanpa entitas; Group Role `Manage partner` pada `Joko Susilo`) untuk TC-AC-SG-336.
  - `Hapus Notif {runId}-116` (tanpa entitas; Group Role `Manage partner` pada `Nina Amelia`) dengan anak `Hapus Notif Anak {runId}-116` (Group Manager `Lia Marlina`) untuk TC-AC-SG-337.
- Baseline audit trail permanen (kemampuan baca jumlah entri disediakan tim FE/BE): sebelum tiap Delete, spec mencatat jumlah entri surface yang diperiksa pada TC itu (Changelog: User `Nina Amelia`; Activity Log tanpa saringan Object; System Log aktor).
- Jendela tunggu 5 detik pada langkah 7 adalah pilihan spec: pencatatan bersifat eventual dan TC tidak menyatakan durasinya.
- Kemampuan teknis: Fixture BE (seeding group dan penugasan, pemulihan; disediakan tim FE/BE). Hook `after` menghapus sisa data milik spec dan mengembalikan sesi ke akun aktor pertama.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-335: Pelepasan Group Role tidak dicatat di Changelog: User

1. Buka Settings > User > Detail `Nina Amelia` > Changelog: User
2. Catat jumlah total entri Changelog: User `Nina Amelia` sebagai baseline TN
3. Buka halaman Settings > Group lewat sidebar
4. Ketik Search `{runId}-116`, tekan Enter
5. Klik ikon `⋯` pada baris `Hapus Warn B {runId}-116` lalu `Delete`
6. Konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
7. Tunggu 5 detik
8. Buka Settings > User > Detail `Nina Amelia` > Tab Role > Sub-tab Group Role
9. Verifikasi Tab Role dan Sub-tab Group Role `Nina Amelia` tampil
10. Verifikasi Tab Role `Nina Amelia` tidak memuat penugasan Group Role pada `Hapus Warn B {runId}-116`
11. Buka Changelog: User `Nina Amelia`
12. Verifikasi jumlah total entri Changelog: User `Nina Amelia` sama dengan TN (tidak ada entri `Remove (Group Deleted)` untuk Group Role)

### TC-AC-SG-336: Pelepasan Group Role tidak dicatat di System Log maupun Activity Log

13. Buka Activity Log Admin Console tanpa saringan Object
14. Catat jumlah total entri Activity Log sebagai baseline BA
15. Buka Settings > User > Detail akun aktor > Tab System Log
16. Catat jumlah total entri System Log aktor sebagai baseline BS
17. Buka halaman Settings > Group lewat sidebar
18. Ketik Search `{runId}-116`, tekan Enter
19. Klik ikon `⋯` pada baris `Hapus Warn A {runId}-116` lalu `Delete`
20. Konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
21. Tunggu hingga entri log muncul
22. Buka Activity Log Admin Console tanpa saringan Object
23. Verifikasi jumlah total entri Activity Log sama dengan BA ditambah 1 (tidak ada entri Object `Group Role (Group Deleted)`)
24. Verifikasi Activity Log memuat entri Action `Delete`, Object `Group`, Name `Hapus Warn A {runId}-116`
25. Buka Settings > User > Detail akun aktor > Tab System Log
26. Verifikasi jumlah total entri System Log aktor sama dengan BS ditambah 1 (tidak ada entri Object `Group Role (Group Deleted)`)
27. Verifikasi System Log aktor memuat entri Action `Delete`, Object `Group`, Name `Hapus Warn A {runId}-116`

### TC-AC-SG-337: Tidak ada notifikasi in-app ke user yang terdampak Delete

28. Buka halaman Settings > Group lewat sidebar
29. Ketik Search `{runId}-116`, tekan Enter
30. Klik ikon `⋯` pada baris `Hapus Notif {runId}-116` lalu `Delete`
31. Konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
32. Tunggu hingga Sidebar Group Tree tidak lagi memuat `Hapus Notif {runId}-116`
33. Ganti akun: Logout, lalu login sebagai `Nina Amelia`
34. Buka notifikasi in-app
35. Verifikasi panel notifikasi in-app tampil
36. Verifikasi notifikasi in-app `Nina Amelia` tidak memuat notifikasi yang menyebut `Hapus Notif {runId}-116`
37. Ganti akun: Logout, lalu login sebagai `Lia Marlina`
38. Buka notifikasi in-app
39. Verifikasi panel notifikasi in-app tampil
40. Verifikasi notifikasi in-app `Lia Marlina` tidak memuat notifikasi yang menyebut `Hapus Notif {runId}-116`

## Notes

- Kelas g (absence). Aksi nyata (Delete group yang memiliki Group Role) dan baseline ada di spec ini. Anchor positif tiap asersi absence: Tab Role dan Sub-tab Group Role tampil (langkah 9, anchor yang ditambahkan spec, S-03) dan baseline agregat TN (TC-AC-SG-335); entri Delete Group pada surface yang sama dan baseline agregat BA dan BS (TC-AC-SG-336); panel notifikasi in-app tampil (TC-AC-SG-337, anchor yang ditambahkan spec, S-03, karena Expected TC hanya menyebut ketiadaan notifikasi).
- Langkah penghubung (S-03, R-16, tanpa `Verifikasi`): langkah 1 sampai 8, 11, 13 sampai 22, 25, dan 28 sampai 34 (membuka surface, baseline, Search `{runId}-116` untuk menemukan baris target, konfirmasi Delete, dan menunggu), serta langkah 7 (menunggu pencatatan yang bersifat eventual; durasi tercatat di Prerequisites).
- Langkah 33 dan 37 adalah ganti akun eksplisit (S-07); sesi dipulihkan ke akun aktor pertama di hook `after`.
- Pembagian TC: TC-AC-SG-134, 331, dan 332 (absence log Delete lainnya) ada di spec 091.
- Spec ini 40 langkah. Alasan di atas sekitar 35 langkah: seluruh langkah satu topik (absence atas pelepasan Group Role akibat Delete) dan satu kelas (absence log); langkah membaca surface (buka surface, catat atau `Verifikasi` jumlah entri) pada langkah 1 sampai 2, 8 sampai 16, dan 22 sampai 27 (17 langkah) tidak dihitung menurut bagian 3 (prinsip 13, Smell); tanpa langkah itu langkah inti 23.
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email, password, atau akun login untuk `Nina Amelia` dan `Lia Marlina` (hanya nama user pada Pre-setup #21); TC-AC-SG-337 langkah 3 menuntut login sebagai keduanya. Spec menulis akun itu sebagai disediakan tim FE.
  - TC-AC-SG-335 dan TC-AC-SG-336 tidak menyebut nama Group Role yang ditugaskan pada `Nina Amelia` dan `Hapus Warn A`; spec memakai `Manage partner` (sama dengan TC-AC-SG-345 untuk `Joko Susilo`).
  - TC-AC-SG-337 Expected tidak menyebut teks atau jenis notifikasi; spec memeriksa ketiadaan notifikasi yang menyebut nama group bersuffix unik.
  - TC-AC-SG-336 menyebut Object `Group Role (Group Deleted)` tetapi tidak menyatakan apakah Object itu ada sebagai pilihan saringan Activity Log; spec membandingkan jumlah total entri tanpa saringan Object terhadap baseline.
