---
id: TC-FA-SU-E2E-302-creator-auto-assign-home-group-di-null-zero-delta-dan-log-per-pengguna-pada-aksi-bulk
title: "Creator Auto-Assign, Home Group Di-null, Zero-delta, dan Log per Pengguna pada Aksi Bulk"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-931
  - TC-FA-SU-932
  - TC-FA-SU-933
  - TC-FA-SU-934
coverage:
  web: automated
---

# Creator Auto-Assign, Home Group Di-null, Zero-delta, dan Log per Pengguna pada Aksi Bulk

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Wawan Setiawan milik spec (Manage group; akun yang membuat grup baru pada TC-FA-SU-931), email `wawan.setiawan+{runId}-302@qwertysystem.net`; kredensial akun ini disediakan tim FE tanpa nama env (akun ini tidak ada di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Akun aktor kedua untuk TC-FA-SU-932, TC-FA-SU-933, dan TC-FA-SU-934: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`; ganti akun dengan langkah eksplisit 14 dan 15, dan hook `after` mengembalikan sesi ke akun default suite (S-07).
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan penugasan (#23). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Wawan Setiawan {runId}-302`, email `wawan.setiawan+{runId}-302@qwertysystem.net`: Active; Group Role Manage group pada Branch Surabaya, Finance & Accounting, dan Logistics Warehouse sehingga dapat membuat grup; Group Role Manage files pada IT Infrastructure dan Branch Surabaya (target Popup Assign Group Role TC-FA-SU-933).
  - `Eka Wulandari {runId}-302`, email `eka.wulandari+{runId}-302@qwertysystem.net`: Active; Home Group Branch Surabaya.
  - `Fajar Nugroho {runId}-302`, email `fajar.nugroho+{runId}-302@qwertysystem.net`: Active; Home Group Branch Surabaya.
  - `Doni Prasetyo {runId}-302`, email `doni.prasetyo+{runId}-302@qwertysystem.net`: Active; Home Group grup milik spec `Logistics Warehouse {runId}-302`.
  - `Gita Permata {runId}-302`, email `gita.permata+{runId}-302@qwertysystem.net`: Active; tanpa aset aktif.
  - `Budi Santoso {runId}-302`, email `budi.santoso+{runId}-302@qwertysystem.net`: Active; tanpa aset aktif dan bukan approver tertunggu.
  - `Doni Prasetyo {runId}-302-2`, email `doni.prasetyo+{runId}-302-2@qwertysystem.net`: Inactive (dilewati Bulk Deactivate).
  - `Hana Kusuma {runId}-302`, email `hana.kusuma+{runId}-302@qwertysystem.net`: Pending Activation, Home Group General Affairs, cooldown Resend belum berjalan; Resend tunggal diikuti Bulk Resend dalam 60 detik tanpa jam digeser.
  - `Kartika Sari {runId}-302`, email `kartika.sari+{runId}-302@qwertysystem.net`: Pending Activation, Inactive, Home Group Branch Surabaya (TC tidak menyebut Home Group awal; dipilih supaya berubah ke IT Infrastructure).
  - Grup `Regional Audit {runId}-302` dan `Logistics Warehouse {runId}-302` dibuat/dimiliki spec: `Regional Audit {runId}-302` dibuat oleh TC-FA-SU-931 dan dihapus lewat seed API di hook `after`; `Logistics Warehouse {runId}-302` (Home Group Doni Prasetyo {runId}-302) dihapus oleh TC-FA-SU-932.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri per Action dan Field pada Tab Changelog pengguna target, Tab System Log aktor, Activity Log, dan Modal Combined Changelog, dibaca sebelum dan sesudah aksi. Entri log muncul eventual: tiap surface dimuat ulang tiap 5 detik sampai entri tampil (batas tunggu 2 menit, idiom polling bagian 6 konvensi). Audit trail bersifat permanen, sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut. Entri dicari lewat Name atau User Name bersuffix unik.
- Kemampuan baca notifikasi in-app pengguna target (jumlah dan jenis notifikasi), disediakan tim FE/BE: pengguna milik spec selain Wawan Setiawan {runId}-302 tidak punya kredensial login, dan pengguna nonaktif tidak dapat login ke FAMS. Notifikasi Wawan Setiawan {runId}-302 (TC-FA-SU-931) juga dibaca lewat kemampuan ini, baik baseline maupun pembacaan sesudah pemicu, supaya sumber baca sama (8b.10); langkah `Tunggu 5 detik tanpa memuat ulang halaman` (langkah 7) berlaku juga untuk pembacaan lewat kemampuan ini (8b.11).
- Tidak ada intercept, jam server, atau klien HTTP. State global: pohon grup (grup milik spec); suite berjalan serial (`parallel: false`). TC-FA-SU-932 menghapus grup milik spec dan dikerjakan terakhir.

## Test Steps

### TC-FA-SU-931: Creator Auto-Assign tercatat sebagai satu entri Assign Group Role tanpa notifikasi

1. Catat jumlah entri Action `Assign` dan Action `Edit` pada Tab Changelog Wawan Setiawan {runId}-302, Tab System Log aktor, dan Activity Log, serta jumlah notifikasi in-app Wawan Setiawan {runId}-302 (dibaca lewat kemampuan baca notifikasi), sebagai baseline
2. Buat grup baru `Regional Audit {runId}-302` di Settings > Groups
3. Tunggu aksi selesai (grup `Regional Audit {runId}-302` tampil di daftar Settings > Groups)
4. Buka Fixed Asset > Settings > User, ketik Search `Wawan Setiawan {runId}-302`, tekan Enter, klik nama Wawan Setiawan {runId}-302, lalu buka Tab Changelog, muat ulang sampai entri tampil
5. Verifikasi Tab Changelog memuat satu entri `Assign` dengan Field `Manage group — Regional Audit {runId}-302`, Old Value `—`, New Value `Assigned`, dan Modified By `Wawan S` (format `[First Name] [Last Initial]`)
6. Verifikasi jumlah entri Action `Edit` pada Tab Changelog sama dengan baseline (tidak ada entri `Edit` CRUD terpisah)
7. Tunggu 5 detik tanpa memuat ulang halaman
8. Baca jumlah notifikasi in-app Wawan Setiawan {runId}-302 lewat kemampuan baca notifikasi (sumber sama dengan baseline langkah 1)
9. Verifikasi jumlah notifikasi in-app Wawan Setiawan {runId}-302 sama dengan baseline (tidak ada notifikasi in-app)
10. Buka Tab System Log aktor dan cari Name `Wawan Setiawan {runId}-302`, muat ulang sampai entri tampil
11. Verifikasi Tab System Log memuat satu entri `Assign` untuk grup `Regional Audit {runId}-302` pada Group Role Manage group
12. Buka Activity Log dan cari Name `Wawan Setiawan {runId}-302`, muat ulang sampai entri tampil
13. Verifikasi Activity Log memuat satu entri `Assign` untuk grup `Regional Audit {runId}-302` pada Group Role Manage group
14. Ganti akun: klik Logout pada akun saat ini
15. Login sebagai Lina Marlina (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`) lalu buka Fixed Asset > Settings > User

### TC-FA-SU-933: Aksi tanpa perubahan nilai (zero-delta) dilarang menulis entri ke tiga surface log

16. Catat jumlah entri pada Tab Changelog Wawan Setiawan {runId}-302, Tab System Log aktor, Activity Log, dan Modal Combined Changelog sebagai baseline
17. Ketik Search `Wawan Setiawan {runId}-302`, tekan Enter, klik nama Wawan Setiawan {runId}-302, lalu buka Tab Role > Sub-tab Group Role dan buka popup Assign Group Role Manage files
18. Klik `[Save]` tanpa perubahan
19. Verifikasi toast "No changes to save." tampil
20. Tutup popup Assign Group Role dengan `[✕]` lalu kembali ke User List lewat breadcrumb `User`
21. Ganti isi kotak search dengan `{runId}-302`, tekan Enter, lalu centang baris Eka Wulandari {runId}-302 dan Fajar Nugroho {runId}-302 (Home Group Branch Surabaya)
22. Klik Bulk Action > `Edit Home Group`, klik node Branch Surabaya pada popup, lalu klik `[Select]`
23. Verifikasi toast "No changes to save." tampil
24. Klik `Unselect All` dan tunggu aksi selesai
25. Buka Detail Wawan Setiawan {runId}-302 > Tab Changelog, muat ulang sampai halaman termuat
26. Verifikasi jumlah entri pada Tab Changelog Wawan Setiawan {runId}-302 sama dengan baseline
27. Buka Tab System Log aktor
28. Verifikasi jumlah entri pada Tab System Log sama dengan baseline
29. Buka Activity Log
30. Verifikasi jumlah entri pada Activity Log sama dengan baseline
31. Buka Fixed Asset > Settings > User lalu buka Modal Combined Changelog
32. Verifikasi jumlah entri pada Modal Combined Changelog sama dengan baseline
33. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-934: Satu entri log per pengguna yang diproses pada aksi bulk dan baris yang di-skip tidak menghasilkan entri

34. Catat jumlah entri Action `Deactivate` untuk Gita Permata {runId}-302, Budi Santoso {runId}-302, dan Doni Prasetyo {runId}-302-2; Action `Resend Activation Email` untuk Hana Kusuma {runId}-302 dan Kartika Sari {runId}-302; serta Action `Edit Home Group` untuk Hana Kusuma {runId}-302 dan Kartika Sari {runId}-302 pada Modal Combined Changelog sebagai baseline
35. Ketik Search `{runId}-302`, tekan Enter, lalu centang baris Gita Permata {runId}-302, Budi Santoso {runId}-302, dan Doni Prasetyo {runId}-302-2
36. Klik Bulk Action > `Deactivate`, lalu klik `[Deactivate]` pada dialog
37. Tunggu aksi selesai lalu klik `Unselect All`
38. Ganti isi kotak search dengan `Hana Kusuma {runId}-302`, tekan Enter, lalu klik ⋯ pada baris Hana Kusuma {runId}-302 dan klik `Resend Activation Email`
39. Ganti isi kotak search dengan `{runId}-302`, tekan Enter
40. Centang Hana Kusuma {runId}-302 dan Kartika Sari {runId}-302, klik Bulk Action > `Resend Activation Email` dan konfirmasi dialog bulk (Hana Kusuma {runId}-302 berada dalam cooldown)
41. Tunggu aksi selesai lalu klik `Unselect All`
42. Ganti isi kotak search dengan `{runId}-302`, tekan Enter
43. Centang Hana Kusuma {runId}-302 dan Kartika Sari {runId}-302, klik Bulk Action > `Edit Home Group`, klik node IT Infrastructure, lalu klik `[Select]`
44. Tunggu aksi selesai lalu klik `Unselect All`
45. Buka Modal Combined Changelog, muat ulang sampai entri tampil
46. Verifikasi jumlah entri Action `Deactivate` untuk Gita Permata {runId}-302 dan Budi Santoso {runId}-302 masing-masing bertambah satu dari baseline (total dua entri `Deactivate`)
47. Verifikasi jumlah entri Action `Deactivate` untuk Doni Prasetyo {runId}-302-2 sama dengan baseline (baris yang di-skip tidak menghasilkan entri)
48. Verifikasi jumlah entri Action `Resend Activation Email` untuk Kartika Sari {runId}-302 bertambah satu dari baseline
49. Verifikasi jumlah entri Action `Resend Activation Email` untuk Hana Kusuma {runId}-302 bertambah satu dari baseline (hanya dari Resend tunggal; Bulk Resend dalam cooldown tidak menambah entri)
50. Verifikasi jumlah entri Action `Edit Home Group` untuk Hana Kusuma {runId}-302 dan Kartika Sari {runId}-302 masing-masing bertambah satu dari baseline
51. Tutup Modal Combined Changelog dengan `[✕]`

### TC-FA-SU-932: Home Group yang di-null oleh hapus grup tidak menghasilkan entri log

52. Catat jumlah entri Action `Edit Home Group` pada Tab Changelog Doni Prasetyo {runId}-302, Tab System Log aktor, dan Activity Log sebagai baseline
53. Hapus grup `Logistics Warehouse {runId}-302` di Settings > Groups
54. Tunggu aksi selesai (grup hilang dari daftar Settings > Groups)
55. Buka Fixed Asset > Settings > User, ketik Search `Doni Prasetyo {runId}-302`, tekan Enter
56. Verifikasi Home Group baris Doni Prasetyo {runId}-302 tampil `—`
57. Buka Detail Doni Prasetyo {runId}-302 > Tab Changelog, muat ulang sampai halaman termuat
58. Verifikasi jumlah entri Action `Edit Home Group` pada Tab Changelog sama dengan baseline
59. Buka Tab System Log aktor
60. Verifikasi jumlah entri Action `Edit Home Group` pada Tab System Log sama dengan baseline
61. Buka Activity Log
62. Verifikasi jumlah entri Action `Edit Home Group` pada Activity Log sama dengan baseline

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-931 (aktor Wawan Setiawan) dikerjakan pertama, TC-FA-SU-933 dan TC-FA-SU-934 sesudah ganti akun, dan TC-FA-SU-932 (menghapus grup) terakhir (S-10).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 3, 4, 7, 8, 14, 15, 17, 20, 21, 24, 31, 33, 35, 37, 38, 39, 41, 42, 44, 51, 54, 55; langkah baseline jumlah entri (S-12): 1, 16, 34, 52. Langkah 4, 17, 21, 35, 38, 39, 42, 55 juga Search untuk menemukan baris target (R-16; langkah 39 dan 42 mengganti isi kotak search supaya Hana Kusuma dan Kartika Sari sama-sama tampil, 8b.9); langkah 14 dan 15 adalah ganti akun eksplisit.
- Alasan di atas sekitar 35 langkah (langkah baca-log berpola tidak dihitung menurut bagian 3 prinsip 13, Smell: 31 dari 62 langkah, sisa 31 langkah): seluruh TC satu topik (peristiwa yang tidak menulis atau hanya menulis tepat satu entri per pengguna pada surface log), tiap TC berdiri sendiri dengan pengguna dan baseline sendiri, dan kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Klausa "tanpa entri" TC-FA-SU-932 dan TC-FA-SU-933 ditulis sebagai asersi jumlah dengan baseline pada aksi yang benar-benar dijalankan (bagian 3 prinsip 13, "Asersi jumlah atau state"), bukan asersi absence kelas g; anchor positifnya toast "No changes to save." (TC-FA-SU-933) dan Home Group `—` pada baris (TC-FA-SU-932).
- Pengguna dan grup milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-302` (S-06); nama grup `Regional Audit` memakai suffix per run (S-12).
- Temuan untuk QA (S-15):
  - TC-FA-SU-931 beraktor Wawan Setiawan (Manage group) yang tidak ada di Tabel Data Uji Pre-setup (akun #1 sampai #13); spec memakai pengguna milik spec dengan kredensial yang disediakan tim FE.
  - Langkah Uji TC-FA-SU-932 menyebut Tab Changelog dan Activity Log, sedangkan Expected butir a menyebut tiga surface log; spec membuka juga Tab System Log aktor. Expected butir b TC-FA-SU-932 (tidak ada notifikasi in-app) tidak menyebut pengguna yang diamati dan tidak punya langkah observasi, sehingga tidak diasersi.
  - TC-FA-SU-931 butir b menyebut tidak ada notifikasi dan tidak ada entri `Edit` CRUD; keduanya diasersi sebagai selisih jumlah terhadap baseline. Post Condition TC-FA-SU-931 (Wawan memegang Manage group pada grup baru) tidak punya langkah observasi dan tidak diasersi.
  - Expected butir a TC-FA-SU-934 menyebut "tiap surface log", sedangkan Langkah Uji hanya menghitung entri di Modal Combined Changelog; spec mengikuti Langkah Uji. TC tidak menyebut dialog Bulk Deactivate, Bulk Resend, atau hasil Bulk Resend dalam cooldown; spec hanya mengonfirmasi dialog tanpa mengasersi isinya.
  - TC-FA-SU-933 butir c merujuk TC-FA-SU-253 dan TC-FA-SU-99 sebagai TC terpisah dan tidak diasersi di sini.
