---
id: TC-GS-USER-E2E-049-temporary-auto-inactive-jam-server-dan-job-terjadwal
title: "Temporary Auto-Inactive: Aktif sampai 23.59, Job 00.00, Zona Waktu Client, Non-Login User, Modified By System, dan Pencatatan Log Auto-Deactivate"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-259
  - TC-GS-USER-260
  - TC-GS-USER-1012
  - TC-GS-USER-1013
  - TC-GS-USER-1014
  - TC-GS-USER-1088
  - TC-GS-USER-907
coverage:
  web: automated
---

# Temporary Auto-Inactive: Aktif sampai 23.59, Job 00.00, Zona Waktu Client, Non-Login User, Modified By System, dan Pencatatan Log Auto-Deactivate

## Prerequisites

- Mode: FE+BE. Kelas harness: harness eksternal (jam server dan jam browser, job terjadwal auto-deactivate).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup) dibaca saja: Siti Nurhaliza (No. 2) dan Hendra Gunawan (Default User, No. 1) dipakai hanya untuk membuka Tab System Log; tidak diubah.
- Tanggal D: tanggal hari ini pada zona waktu client General Settings, dibaca di hook `before` (spec tidak dijalankan menjelang tengah malam zona itu). Zona waktu client General Settings awal `Asia/Jakarta` (UTC+7); nilai awal tidak disebut TC dan disediakan tim FE.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD):
  - F-1: Login User, Name `Fikri Ramadhan {runId}-049` (First Name `Fikri`, Last Name `Ramadhan {runId}-049`), email `fikriramadhan+{runId}-049@qwertysystem.net`, Activated, Active, Division `Finance`, Access `Fixed Asset`, Temporary User dengan Temporary Until = D.
  - N-1: Non-Login User, Name `Rudi Setiawan {runId}-049`, Temporary User dengan Temporary Until = D, Active.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak memberi cara):
  - Mengatur jam server dan jam browser bersama ke waktu absolut dalam zona waktu client (bukan geseran relatif) dan memulihkannya ke waktu nyata; keduanya diatur bersama karena asersi memakai tampilan UI.
  - Memicu job terjadwal auto-deactivate Temporary (job 00.00) secara eksplisit dan mengetahui job selesai.
  - Mengubah dan memulihkan General Settings Timezone entitas.
- State global yang diubah: jam server dan jam browser, General Settings Timezone entitas (`Asia/Jakarta` ke `Asia/Jayapura` dan kembali), status F-1 dan N-1 oleh job. Pemulihan jam dan Timezone ditulis sebagai langkah aksi (langkah 17 dan 25) sebelum akun aktor membuka Activity Log atau User Log; hook `after` memulihkan jam, Timezone, dan menghapus F-1 dan N-1 sebagai cadangan (tetap jalan walau spec gagal). Suite berjalan serial (`parallel: false`).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus F-1 dan N-1 lewat API, pulihkan jam dan Timezone.
- Admin pembanding untuk Tab System Log (TC-GS-USER-907 butir c "beberapa admin"): Siti Nurhaliza dan Hendra Gunawan (Default User). Entri System Log milik kedua admin yang menjadi pembanding disediakan tim FE (TC tidak menyebutnya).

## Test Steps

### Persiapan

1. Klik icon Search, ketik `{runId}-049`, tekan Enter
2. Klik icon Changelog pada Table Tools
3. Klik icon Search pada Modal Changelog, ketik `Fikri Ramadhan {runId}-049`, tekan Enter
4. Catat jumlah entri hasil Search sebagai baseline J0 dan waktu nyata sebagai T0
5. Tutup Modal Changelog lewat `✕`

### TC-GS-USER-1014: Validasi Temporary Until 'besok' memakai zona waktu client General Settings

6. Atur General Settings Timezone entitas menjadi `Asia/Jayapura` (UTC+9)
7. Atur jam server dan jam browser bersama ke tanggal D pukul 23.30 UTC+7
8. Klik `[+ User]` di Table Tools
9. Isi First Name `Papua`, Last Name `Uji {runId}-049`, Division `Finance`, Email `papuauji+{runId}-049@qwertysystem.net`, centang Access `Fixed Asset`
10. Centang `Set as Temporary User`
11. Pilih Temporary Until = tanggal kalender browser D + 1
12. Klik `[Submit]`
13. Verifikasi error `Please select a future date.`
14. Klik `✕` pada header form
15. Verifikasi dialog `Unsaved Changes`
16. Klik `[Leave]`
17. Pulihkan General Settings Timezone entitas menjadi `Asia/Jakarta`

### TC-GS-USER-1012: Temporary Until hari ini, user masih Active sampai akhir hari

18. Atur jam server dan jam browser bersama ke tanggal D pukul 23.59 UTC+7
19. Muat ulang halaman User List
20. Klik icon Search, ketik `{runId}-049`, tekan Enter
21. Verifikasi switch Active baris `Fikri Ramadhan {runId}-049` ON

### Job terjadwal 00.00 hari berikutnya

22. Atur jam server dan jam browser bersama ke tanggal D + 1 pukul 00.00 UTC+7
23. Picu job terjadwal auto-inactive Temporary
24. Tunggu job terjadwal selesai
25. Pulihkan jam server dan jam browser ke waktu nyata

### TC-GS-USER-260: Temporary auto-inactive berlaku juga untuk Non-Login User

26. Muat ulang halaman User List
27. Klik sub-tab `Non-Login User`
28. Klik icon Search, ketik `{runId}-049`, tekan Enter
29. Verifikasi status `Rudi Setiawan {runId}-049` Inactive

### TC-GS-USER-259, TC-GS-USER-1013, dan TC-GS-USER-1088: Auto-inactive setelah Temporary Until terlewati, Modified By dan Last Update

30. Muat ulang halaman User List
31. Klik icon Search, ketik `{runId}-049`, tekan Enter
32. Verifikasi switch Active baris `Fikri Ramadhan {runId}-049` OFF
33. Verifikasi Modified By baris `Fikri Ramadhan {runId}-049` `System`
34. Verifikasi Last Update baris `Fikri Ramadhan {runId}-049` sama dengan waktu job (tanggal D + 1 pukul 00.00 zona waktu client)
35. Catat nilai Last Update baris `Fikri Ramadhan {runId}-049` sebagai L1
36. Klik icon Changelog pada Table Tools
37. Klik icon Search pada Modal Changelog, ketik `Fikri Ramadhan {runId}-049`, tekan Enter
38. Verifikasi jumlah entri hasil Search bertambah 1 dibanding baseline J0
39. Verifikasi baris `Auto-Deactivate | Fikri Ramadhan {runId}-049 | Status (Global) | Active | Inactive | System`
40. Tutup Modal Changelog lewat `✕`
41. Buka Detail `Fikri Ramadhan {runId}-049` dengan klik Name
42. Klik Tab `Changelog`
43. Verifikasi Modified By baris `Auto-Deactivate` terbaru `System`
44. Verifikasi Date baris `Auto-Deactivate` terbaru sama dengan L1

### TC-GS-USER-907: Log Auto-Deactivate tercatat dengan System dan tidak tampil di System Log

45. Buka Global Settings > Activity Log
46. Klik icon Search, ketik `Fikri Ramadhan {runId}-049`, tekan Enter
47. Verifikasi Activity Log memuat baris `Auto-Deactivate` untuk `Fikri Ramadhan {runId}-049` dengan Status (Global) `Active` ke `Inactive` dan Modified By `System`
48. Klik menu User di sidebar Global Settings
49. Klik icon Search, ketik `Siti Nurhaliza`, tekan Enter
50. Buka Detail `Siti Nurhaliza` dengan klik Name
51. Klik Tab `System Log`
52. Verifikasi Tab System Log memuat sedikitnya satu baris (pembanding)
53. Klik icon Search, ketik `Auto-Deactivate`, tekan Enter
54. Verifikasi Tab System Log Siti Nurhaliza tidak memuat baris `Auto-Deactivate`
55. Klik menu User di sidebar Global Settings
56. Klik icon Search, ketik `Hendra Gunawan`, tekan Enter
57. Buka Detail `Hendra Gunawan` dengan klik Name
58. Klik Tab `System Log`
59. Verifikasi Tab System Log memuat sedikitnya satu baris (pembanding)
60. Klik icon Search, ketik `Auto-Deactivate`, tekan Enter
61. Verifikasi Tab System Log Hendra Gunawan tidak memuat baris `Auto-Deactivate`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas harness d (bagian 3 prinsip 13d): TC-GS-USER-259, 260, 1012, 1013, 1014, 1088, dan 907 mengamati job terjadwal dan jam server/browser.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (61 langkah) karena semua TC berada di satu kelas harness (jam server dan browser serta job auto-deactivate) dan memakai seed F-1 yang sama: TC-GS-USER-259, 1013, 1088, dan 907 mengamati hasil satu eksekusi job pada F-1 (precondition identik: Temporary Until terlewati, job dijalankan), sehingga memecahnya mengulang seeding, penggeseran jam, dan pemicu job. Tiap blok berdiri sendiri pada surface sendiri (User List, Non-Login User, Modal Changelog, Tab Changelog, Activity Log, Tab System Log). Langkah 48 sampai 61 adalah pembacaan Tab System Log dua admin (blok baca-log berpola).
- Urutan TC sumber diubah: TC-GS-USER-1014 (validasi yang diblokir) dan TC-GS-USER-1012 (kondisi sebelum job) mendahului pemicu job; TC-GS-USER-259, 1013, dan 1088 digabung pada pengamatan pascajob yang sama (Expected 259 a sama dengan Expected 1013 a; Expected 259 b sama dengan Expected 1013 b dan 907 a); TC-GS-USER-1088 membaca Last Update dan Tab Changelog sesudah TC-GS-USER-259; TC-GS-USER-260 ditaruh sebelum pembacaan Login User karena memakai sub-tab lain dan dibuka lewat muat ulang; TC-GS-USER-907 paling akhir karena membuka Activity Log dan Tab System Log (bagian 3 prinsip 3). Ketergantungan TC-GS-USER-1088 pada TC-GS-USER-1012 dipenuhi oleh F-1 yang sama yang diamati Active pada langkah 21 sebelum job.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 sampai 5 (Search dan baseline J0 dan T0 sebelum jam digeser), 6, 7, 17, 18, 22, 25 (mengatur dan memulihkan Timezone serta jam), 14 dan 16 (menutup form dirty lewat `✕` dan `[Leave]`, S-08), 19, 20, 26 sampai 28, 30, 31 (muat ulang dan Search), 23 dan 24 (pemicu dan penantian job), 35 (mencatat nilai), 36 sampai 37, 40 sampai 42, 45, 46, 48 sampai 51, 53, 55 sampai 58, 60 (membuka surface dan mencari).
- Asersi tambahan: langkah 15 (dialog `Unsaved Changes`) adalah bagian penutupan form dirty menurut S-08 dan tidak ada di Expected TC-GS-USER-1014; langkah 38 adalah perbandingan jumlah entri terhadap baseline J0 (S-12) untuk "baris baru"; langkah 52 dan 59 adalah pembanding sebelum asersi absence (bagian 8b butir 2).
- P-1: TC-GS-USER-907 butir c ("tidak ada baris Auto-Deactivate di System Log admin mana pun") diasersi di spec ini (langkah 52 sampai 61) karena konteksnya bergantung pada state berat yang baru dibangun langkah sebelumnya (jam digeser dan job dijalankan) dan tidak ada spec absence yang memuat aksi nyata untuk TC itu (S-05). Baseline: penanda waktu nyata T0 dan jumlah entri J0 dicatat di langkah 4 sebelum jam digeser; karena log Auto-Deactivate bercap waktu job (D + 1 00.00), asersi mencari baris berdasarkan Note `Auto-Deactivate` dan Name, bukan posisi teratas (S-12).
- Jam server dan jam browser diatur bersama dan dipulihkan lewat langkah 25 sebelum akun aktor membuka Activity Log, User Log, atau Tab System Log (S-09). Langkah 7 mengatur keduanya bersama ke tanggal D pukul 23.30 UTC+7 sehingga tanggal Asia/Jayapura (UTC+9) sudah D + 1.
- Pembagian TC: pencatatan Changelog, Activity Log, dan System Log untuk aksi lain (Create, Edit, Deactivate manual, dan seterusnya) diverifikasi di spec pencatatan log; hanya log Auto-Deactivate yang diverifikasi di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-259 Post Condition a (sesi aktif Fikri diakhiri) dan b (terdampak user list produk dan approver pool) tanpa langkah observasi; tidak diasersi.
  - TC-GS-USER-259, 1013, 1088, dan 907 memakai precondition yang sama (Temporary Until terlewati, job dijalankan) tanpa menyebut cara memicu job atau menggeser waktu sistem; disediakan tim FE/BE.
  - TC-GS-USER-1012 tidak menyatakan apakah halaman dimuat ulang pada 23.59; spec memuat ulang User List pada pukul itu supaya status dibaca dari server.
  - TC-GS-USER-1014 mensyaratkan General Settings Timezone `Asia/Jayapura` dan waktu browser UTC+7 pukul 23.30 tanpa menyebut cara mengubah Timezone dan nilai awalnya, serta tanpa menyebut jam server; spec mengatur jam server dan jam browser bersama dan Timezone dengan kemampuan yang disediakan tim FE.
  - TC-GS-USER-1014 tidak menyebut cara menutup form dirty sesudah error; spec memakai `✕`, dialog `Unsaved Changes`, `[Leave]` (S-08).
  - TC-GS-USER-260 butir ("Status Rudi Setiawan Inactive") tidak menyebut kolom atau kontrol yang diamati di sub-tab Non-Login User; spec mengasersi status Inactive pada baris.
  - TC-GS-USER-907 butir b tidak menyebut kolom baris Activity Log; spec mengasersi Auto-Deactivate, nama user, Status (Global) Active ke Inactive, dan Modified By `System`. Butir c tidak menyebut admin yang dimaksud ("beberapa admin"); spec memakai Siti Nurhaliza dan Hendra Gunawan.
  - TC-GS-USER-907 butir c mensyaratkan surface System Log admin yang memuat sedikitnya satu baris pembanding; TC tidak menyebut baris itu. Disediakan tim FE.
  - TC-GS-USER-1088 butir b ("Last Update = waktu job 00.00 hari ini") tidak menyebut format atau toleransi detik; spec mengasersi tanggal D + 1 pukul 00.00 zona waktu client.
