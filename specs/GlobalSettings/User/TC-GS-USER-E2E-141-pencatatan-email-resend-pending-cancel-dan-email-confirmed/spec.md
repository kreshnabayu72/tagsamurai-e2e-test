---
id: TC-GS-USER-E2E-141-pencatatan-email-resend-pending-cancel-dan-email-confirmed
title: "Pencatatan Resend Activation Email, Resend Confirmation Email, Pending Email Change, Cancel Email Change, Email Updated, dan Email Confirmed di Changelog, System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-882
  - TC-GS-USER-883
  - TC-GS-USER-894
  - TC-GS-USER-895
  - TC-GS-USER-896
  - TC-GS-USER-908
coverage:
  web: automated
---

# Pencatatan Resend Activation Email, Resend Confirmation Email, Pending Email Change, Cancel Email Change, Email Updated, dan Email Confirmed di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE (kelas harness d: mail-catcher dan manipulasi jam server dan jam browser).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Siti Nurhaliza (No. 2) sebagai pelaku dan pemilik Tab System Log; Division `Finance` (No. 23). Data target Pre-setup No. 10 sampai 21 tidak dipakai sebagai target aksi dan tidak diubah (S-06).
- Data Dinamis (suffix `{runId}-141`; di-seed lewat API di hook `before`; Division `Finance`, Access `Fixed Asset`; menggantikan Mike Tan No. 14, Rina Putri No. 15, dan Dewi Lestari No. 12; semua Activation Email dan Confirmation Email seed memulai cooldown Resend 60 detik pada waktu terbit):
  - `Mike Tan {runId}-141` (Email `miketan+{runId}-141@qwertysystem.net`): Pending Activation (TC-GS-USER-882).
  - `Rina Putri {runId}-141` (Email `rinaputri+{runId}-141@qwertysystem.net`): Activated dengan email pending `rinaputri.new+{runId}-141@qwertysystem.net` (TC-GS-USER-883).
  - `Dewi Lestari {runId}-141` (Email `dewilestari+{runId}-141@qwertysystem.net`): Activated, tanpa email pending; email baru uji `dewilestari.new+{runId}-141@qwertysystem.net` (TC-GS-USER-894).
  - `Rina Putri Cancel {runId}-141` (Email `rinaputricancel+{runId}-141@qwertysystem.net`): Activated dengan email pending `rinaputricancel.new+{runId}-141@qwertysystem.net` (TC-GS-USER-895).
  - `Mike Tan Email {runId}-141` (Email `miketanemail+{runId}-141@qwertysystem.net`): Pending Activation; email baru uji `miketanemail.new+{runId}-141@qwertysystem.net` (TC-GS-USER-896).
  - `Rina Putri Confirm {runId}-141` (First Name `Rina`, Last Name `Putri Confirm {runId}-141`, Email `rinaputriconfirm+{runId}-141@qwertysystem.net`): Activated dengan email pending `rinaputriconfirm.new+{runId}-141@qwertysystem.net` dan Confirmation Email terkirim ke alamat itu (TC-GS-USER-908). Modified By user itu sendiri tampil sebagai `Rina P`.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, dan LLD):
  - Mail-catcher: membaca daftar email per alamat tujuan (waktu terbit dan tautan di badan email) dan membuka tautan konfirmasi di tab baru. Tidak ada asersi jumlah email di spec ini sehingga baseline jumlah email tidak dicatat.
  - Manipulasi jam: jam server dan jam browser diatur bersama ke nilai absolut dan dipulihkan ke waktu nyata (cooldown Resend dihitung di server dan countdown UI di jam browser).
  - Seeding user Pending Activation, user Activated dengan email pending (beserta Confirmation Email pertama), dan user Activated tanpa email pending lewat API; membaca jumlah baris log per user dan Action sebagai baseline.
- Rumus jam (batas eksak 60 detik): `T_M` = waktu terbit Activation Email awal `Mike Tan {runId}-141` dan `T_R` = waktu terbit Confirmation Email awal `Rina Putri {runId}-141`, keduanya dibaca dari mail-catcher; jam diatur absolut ke `max(T_M, T_R)` + 60 detik (bukan digeser relatif).
- State global yang diubah: jam server dan jam browser (diatur sebelum aksi Resend dan dipulihkan lewat langkah eksplisit sebelum Modal Changelog User dibuka, S-09; hook `after` memulihkan jam sebagai cadangan). Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan jam, lalu hapus lewat API keenam user seed di atas. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar dan jam untuk Resend

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Baca waktu terbit Activation Email awal `Mike Tan {runId}-141` (`T_M`) dan Confirmation Email awal `Rina Putri {runId}-141` (`T_R`) dari mail-catcher
3. Atur jam server dan jam browser bersama ke waktu absolut `max(T_M, T_R)` + 60 detik, sehingga cooldown Resend kedua user berakhir

### TC-GS-USER-882: Aksi Resend Activation Email

4. Klik icon Search, ketik `Mike Tan {runId}-141`, tekan Enter
5. Klik (⋯) baris `Mike Tan {runId}-141` → `Resend Activation Email`
6. Tunggu aksi selesai (menu row action tertutup)

### TC-GS-USER-883: Aksi Resend Confirmation Email

7. Ganti isi kotak search dengan `Rina Putri {runId}-141`, tekan Enter
8. Klik (⋯) baris `Rina Putri {runId}-141` → `Resend Confirmation Email`
9. Tunggu aksi selesai (menu row action tertutup)
10. Pulihkan jam server dan jam browser ke waktu nyata

### TC-GS-USER-882: Pencatatan Resend Activation Email

11. Buka Modal Changelog User, klik icon Search, ketik `Mike Tan {runId}-141`, tekan Enter
12. Verifikasi Modal Changelog User: baris dengan Action `Resend Activation Email`, Name `Mike Tan {runId}-141`, Field `Activation Email`, Old Value `—`, New Value `miketan+{runId}-141@qwertysystem.net`, Modified By `Siti N`
13. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Resend Activation Email` untuk `Mike Tan {runId}-141` (tidak duplikat)
14. Buka Detail `Mike Tan {runId}-141` > Tab `Changelog`
15. Verifikasi Tab Changelog Detail `Mike Tan {runId}-141`: baris dengan Action `Resend Activation Email`, Field `Activation Email`, Old Value `—`, New Value `miketan+{runId}-141@qwertysystem.net`, Modified By `Siti N`
16. Verifikasi Tab Changelog Detail `Mike Tan {runId}-141`: tepat 1 baris dengan Action `Resend Activation Email` (tidak duplikat)
17. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Mike Tan {runId}-141`, tekan Enter
18. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Resend Activation Email`, Object `User`, Name `Mike Tan {runId}-141`, Field `Activation Email`, Old Value `—`, New Value `miketan+{runId}-141@qwertysystem.net`
19. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Resend Activation Email` untuk `Mike Tan {runId}-141` (tidak duplikat)
20. Buka Global Settings > Activity Log, klik icon Search, ketik `Mike Tan {runId}-141`, tekan Enter
21. Verifikasi Activity Log: baris dengan Action `Resend Activation Email`, Object `User`, Name `Mike Tan {runId}-141`, Field `Activation Email`, Old Value `—`, New Value `miketan+{runId}-141@qwertysystem.net`, Modified By `Siti N`
22. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Resend Activation Email` untuk `Mike Tan {runId}-141` (tidak duplikat)

### TC-GS-USER-883: Pencatatan Resend Confirmation Email

23. Buka Modal Changelog User, klik icon Search, ketik `Rina Putri {runId}-141`, tekan Enter
24. Verifikasi Modal Changelog User: baris dengan Action `Resend Confirmation Email`, Name `Rina Putri {runId}-141`, Field `Confirmation Email`, Old Value `—`, New Value `rinaputri.new+{runId}-141@qwertysystem.net`, Modified By `Siti N`
25. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Resend Confirmation Email` untuk `Rina Putri {runId}-141` (tidak duplikat)
26. Buka Detail `Rina Putri {runId}-141` > Tab `Changelog`
27. Verifikasi Tab Changelog Detail `Rina Putri {runId}-141`: baris dengan Action `Resend Confirmation Email`, Field `Confirmation Email`, Old Value `—`, New Value `rinaputri.new+{runId}-141@qwertysystem.net`, Modified By `Siti N`
28. Verifikasi Tab Changelog Detail `Rina Putri {runId}-141`: tepat 1 baris dengan Action `Resend Confirmation Email` (tidak duplikat)
29. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Rina Putri {runId}-141`, tekan Enter
30. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Resend Confirmation Email`, Object `User`, Name `Rina Putri {runId}-141`, Field `Confirmation Email`, Old Value `—`, New Value `rinaputri.new+{runId}-141@qwertysystem.net`
31. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Resend Confirmation Email` untuk `Rina Putri {runId}-141` (tidak duplikat)
32. Buka Global Settings > Activity Log, klik icon Search, ketik `Rina Putri {runId}-141`, tekan Enter
33. Verifikasi Activity Log: baris dengan Action `Resend Confirmation Email`, Object `User`, Name `Rina Putri {runId}-141`, Field `Confirmation Email`, Old Value `—`, New Value `rinaputri.new+{runId}-141@qwertysystem.net`, Modified By `Siti N`
34. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Resend Confirmation Email` untuk `Rina Putri {runId}-141` (tidak duplikat)

### TC-GS-USER-894: Pencatatan Pending Email Change

35. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari {runId}-141`, tekan Enter
36. Klik (⋯) baris `Dewi Lestari {runId}-141` → `Edit`
37. Ubah Email ke `dewilestari.new+{runId}-141@qwertysystem.net`
38. Klik `[Save]`
39. Tunggu aksi selesai (Popup Edit tertutup)
40. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari {runId}-141`, tekan Enter
41. Verifikasi Modal Changelog User: baris dengan Action `Pending Email Change`, Name `Dewi Lestari {runId}-141`, Field `Email`, Old Value `dewilestari+{runId}-141@qwertysystem.net`, New Value `dewilestari.new+{runId}-141@qwertysystem.net (pending)`, Modified By `Siti N`
42. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Pending Email Change` untuk `Dewi Lestari {runId}-141` (tidak duplikat)
43. Buka Detail `Dewi Lestari {runId}-141` > Tab `Changelog`
44. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-141`: baris dengan Action `Pending Email Change`, Field `Email`, Old Value `dewilestari+{runId}-141@qwertysystem.net`, New Value `dewilestari.new+{runId}-141@qwertysystem.net (pending)`, Modified By `Siti N`
45. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-141`: tepat 1 baris dengan Action `Pending Email Change` (tidak duplikat)
46. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari {runId}-141`, tekan Enter
47. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Pending Email Change`, Object `User`, Name `Dewi Lestari {runId}-141`, Field `Email`, Old Value `dewilestari+{runId}-141@qwertysystem.net`, New Value `dewilestari.new+{runId}-141@qwertysystem.net (pending)`
48. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Pending Email Change` untuk `Dewi Lestari {runId}-141` (tidak duplikat)
49. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari {runId}-141`, tekan Enter
50. Verifikasi Activity Log: baris dengan Action `Pending Email Change`, Object `User`, Name `Dewi Lestari {runId}-141`, Field `Email`, Old Value `dewilestari+{runId}-141@qwertysystem.net`, New Value `dewilestari.new+{runId}-141@qwertysystem.net (pending)`, Modified By `Siti N`
51. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Pending Email Change` untuk `Dewi Lestari {runId}-141` (tidak duplikat)

### TC-GS-USER-895: Pencatatan Cancel Email Change

52. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Rina Putri Cancel {runId}-141`, tekan Enter
53. Klik (⋯) baris `Rina Putri Cancel {runId}-141` → `Edit`
54. Klik Button Cancel di samping label pending
55. Klik `[Cancel Change]` pada dialog `Cancel Pending Email Change`
56. Tunggu aksi selesai (label pending hilang)
57. Klik `✕` pada header Popup Edit
58. Buka Modal Changelog User, klik icon Search, ketik `Rina Putri Cancel {runId}-141`, tekan Enter
59. Verifikasi Modal Changelog User: baris dengan Action `Cancel Email Change`, Name `Rina Putri Cancel {runId}-141`, Field `Email`, Old Value `rinaputricancel.new+{runId}-141@qwertysystem.net (pending)`, New Value `rinaputricancel+{runId}-141@qwertysystem.net`, Modified By `Siti N`
60. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Cancel Email Change` untuk `Rina Putri Cancel {runId}-141` (tidak duplikat)
61. Verifikasi Modal Changelog User: Modified By baris `Cancel Email Change` untuk `Rina Putri Cancel {runId}-141` adalah admin yang membatalkan, `Siti N`
62. Buka Detail `Rina Putri Cancel {runId}-141` > Tab `Changelog`
63. Verifikasi Tab Changelog Detail `Rina Putri Cancel {runId}-141`: baris dengan Action `Cancel Email Change`, Field `Email`, Old Value `rinaputricancel.new+{runId}-141@qwertysystem.net (pending)`, New Value `rinaputricancel+{runId}-141@qwertysystem.net`, Modified By `Siti N`
64. Verifikasi Tab Changelog Detail `Rina Putri Cancel {runId}-141`: tepat 1 baris dengan Action `Cancel Email Change` (tidak duplikat)
65. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Rina Putri Cancel {runId}-141`, tekan Enter
66. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Cancel Email Change`, Object `User`, Name `Rina Putri Cancel {runId}-141`, Field `Email`, Old Value `rinaputricancel.new+{runId}-141@qwertysystem.net (pending)`, New Value `rinaputricancel+{runId}-141@qwertysystem.net`
67. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Cancel Email Change` untuk `Rina Putri Cancel {runId}-141` (tidak duplikat)
68. Buka Global Settings > Activity Log, klik icon Search, ketik `Rina Putri Cancel {runId}-141`, tekan Enter
69. Verifikasi Activity Log: baris dengan Action `Cancel Email Change`, Object `User`, Name `Rina Putri Cancel {runId}-141`, Field `Email`, Old Value `rinaputricancel.new+{runId}-141@qwertysystem.net (pending)`, New Value `rinaputricancel+{runId}-141@qwertysystem.net`, Modified By `Siti N`
70. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Cancel Email Change` untuk `Rina Putri Cancel {runId}-141` (tidak duplikat)

### TC-GS-USER-896: Pencatatan Email Updated

71. Catat baseline `{n0}` (lewat kemampuan baca BE) sebelum aksi pemicu: jumlah baris Action `Resend Activation Email` untuk `Mike Tan Email {runId}-141`
72. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Mike Tan Email {runId}-141`, tekan Enter
73. Klik (⋯) baris `Mike Tan Email {runId}-141` → `Edit`
74. Ubah Email ke `miketanemail.new+{runId}-141@qwertysystem.net`
75. Klik `[Save]`
76. Tunggu aksi selesai (Popup Edit tertutup)
77. Buka Modal Changelog User, klik icon Search, ketik `Mike Tan Email {runId}-141`, tekan Enter
78. Verifikasi Modal Changelog User: baris dengan Action `Email Updated`, Name `Mike Tan Email {runId}-141`, Field `Email`, Old Value `miketanemail+{runId}-141@qwertysystem.net`, New Value `miketanemail.new+{runId}-141@qwertysystem.net`, Modified By `Siti N`
79. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Email Updated` untuk `Mike Tan Email {runId}-141` (tidak duplikat)
80. Verifikasi Modal Changelog User: baris Action `Email Updated` untuk `Mike Tan Email {runId}-141` berjumlah tepat 1 dan jumlah baris Action `Resend Activation Email` untuk `Mike Tan Email {runId}-141` tetap sama dengan baseline `{n0}` (tidak ada baris `Resend Activation Email` tambahan dari kirim otomatis)
81. Buka Detail `Mike Tan Email {runId}-141` > Tab `Changelog`
82. Verifikasi Tab Changelog Detail `Mike Tan Email {runId}-141`: baris dengan Action `Email Updated`, Field `Email`, Old Value `miketanemail+{runId}-141@qwertysystem.net`, New Value `miketanemail.new+{runId}-141@qwertysystem.net`, Modified By `Siti N`
83. Verifikasi Tab Changelog Detail `Mike Tan Email {runId}-141`: tepat 1 baris dengan Action `Email Updated` (tidak duplikat)
84. Verifikasi Tab Changelog Detail `Mike Tan Email {runId}-141`: baris Action `Email Updated` berjumlah tepat 1 dan jumlah baris Action `Resend Activation Email` tetap sama dengan baseline `{n0}` (tidak ada baris `Resend Activation Email` tambahan dari kirim otomatis)
85. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Mike Tan Email {runId}-141`, tekan Enter
86. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Email Updated`, Object `User`, Name `Mike Tan Email {runId}-141`, Field `Email`, Old Value `miketanemail+{runId}-141@qwertysystem.net`, New Value `miketanemail.new+{runId}-141@qwertysystem.net`
87. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Email Updated` untuk `Mike Tan Email {runId}-141` (tidak duplikat)
88. Buka Global Settings > Activity Log, klik icon Search, ketik `Mike Tan Email {runId}-141`, tekan Enter
89. Verifikasi Activity Log: baris dengan Action `Email Updated`, Object `User`, Name `Mike Tan Email {runId}-141`, Field `Email`, Old Value `miketanemail+{runId}-141@qwertysystem.net`, New Value `miketanemail.new+{runId}-141@qwertysystem.net`, Modified By `Siti N`
90. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Email Updated` untuk `Mike Tan Email {runId}-141` (tidak duplikat)

### TC-GS-USER-908: Pencatatan Email Confirmed oleh user itu sendiri

91. Buka tab baru, buka tautan konfirmasi pada Confirmation Email terbaru ke `rinaputriconfirm.new+{runId}-141@qwertysystem.net` dari mail-catcher
92. Tunggu halaman tautan konfirmasi selesai dimuat
93. Tutup tab tautan konfirmasi
94. Buka Modal Changelog User, klik icon Search, ketik `Rina Putri Confirm {runId}-141`, tekan Enter
95. Verifikasi Modal Changelog User: baris dengan Action `Email Confirmed`, Name `Rina Putri Confirm {runId}-141`, Field `Email`, Old Value `rinaputriconfirm+{runId}-141@qwertysystem.net`, New Value `rinaputriconfirm.new+{runId}-141@qwertysystem.net`, Modified By `Rina P`
96. Buka Detail `Rina Putri Confirm {runId}-141` > Tab `System Log`, klik icon Search, ketik `Rina Putri Confirm {runId}-141`, tekan Enter
97. Verifikasi Tab System Log Detail `Rina Putri Confirm {runId}-141`: baris dengan Action `Email Confirmed` dan Name `Rina Putri Confirm {runId}-141`

## Notes

- Mode: FE+BE (kelas harness d). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-GS-USER-882 dan 883 memiliki dua subjudul (aksi, lalu pencatatan) karena jam diatur sekali sebelum kedua aksi Resend dan dipulihkan sebelum log dibuka.
- Baris log dikenali lewat nama bersuffix `{runId}-141` yang unik per run, Action, dan Field, bukan posisi teratas dan bukan penanda waktu (S-12). Log yang dibuat saat jam digeser bercap waktu masa depan, sehingga asersi memakai nama dan Action, bukan posisi teratas. Tiap TC memakai user seed sendiri; TC-GS-USER-896 mencatat baseline jumlah baris `Resend Activation Email` sebelum aksi pemicu.
- Surface disebut satu per satu pada TC-GS-USER-882, 883, 894, 895, dan 896: Modal Changelog User, Tab Changelog Detail, Tab System Log Detail Siti Nurhaliza, dan Activity Log. TC-GS-USER-908 mengikuti Langkah Uji: Modal Changelog User dan Tab System Log Detail `Rina Putri Confirm {runId}-141`. Expected "Tepat 1 baris per surface (tidak duplikat)" diasersi sebagai jumlah baris dengan Action dan nama yang sama sesudah `Verifikasi` isi baris pada surface yang sama.
- Klausa Expected f TC-GS-USER-896 ("Tidak ada baris Resend Activation Email tambahan dari kirim otomatis") diasersi sebagai jumlah baris `Email Updated` (tepat 1) dan jumlah baris `Resend Activation Email` yang tetap sama dengan baseline `{n0}` untuk `Mike Tan Email {runId}-141`, bukan asersi absence kelas g (aksi berhasil dan baris yang diharapkan terasersi pada hasil yang sama). Asersi absence kelas g untuk log lintas user dan Edit No-Op ada di spec `TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role`.
- Urutan TC di spec: 882 dan 883 (aksi dalam satu pengaturan jam) lebih dulu, lalu pencatatan 882 dan 883, kemudian 894, 895, 896, 908 sesuai urutan sourceTc. Tidak ada TC yang menghapus data. TC-GS-USER-882 dan 883 membutuhkan cooldown Resend yang sudah berakhir (opsi `Resend` disabled selama cooldown), sehingga jam diatur sebelum aksi.
- Mail-catcher dipakai untuk membaca waktu terbit email (cooldown) dan untuk membuka tautan konfirmasi pada TC-GS-USER-908; spec ini tidak mengasersi isi atau jumlah email karena Expected TC hanya menyebut baris log.
- Spec melewati sekitar 35 langkah (97 langkah). Alasan: seluruh blok satu kelas harness (pencatatan log dengan mail-catcher dan jam) dengan user seed sendiri per TC sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) mendominasi jumlah langkah dan tidak dihitung ke batas ukuran (bagian 3 konvensi).
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 sampai 11, 14, 17, 20, 23, 26, 29, 32, 35 sampai 40, 43, 46, 49, 52 sampai 58, 62, 65, 68, 71 sampai 77, 81, 85, 88, 91 sampai 94, 96. Frasa "Buka ..." pada langkah baca-log mencakup navigasi dari halaman sebelumnya (klik menu User di sidebar Global Settings atau menu Activity Log), menutup Modal Changelog User dengan `✕`, dan, untuk Detail, Search nama pada User List lalu klik Name. Pembukaan Detail `Siti Nurhaliza` mengikuti pola yang sama.
- Temuan untuk QA:
  - TC-GS-USER-908 berstatus `Manual Only` di TC; spec memasukkannya (bagian 2 konvensi) dengan tautan konfirmasi dibuka dari mail-catcher. Expected tidak menyebut tampilan halaman tautan konfirmasi sehingga hanya log yang diasersi. Modified By `Rina P` diturunkan dari pola nama pelaku (`Siti N` untuk Siti Nurhaliza); kolom System Log selain Name tidak disebut Expected b dan tidak diasersi.
  - TC-GS-USER-882 dan 883: Precondition tidak menyebut cooldown Resend 60 detik dari email seed; spec mengatur jam server dan jam browser sehingga spec membutuhkan manipulasi jam (HK5) selain mail-catcher (HK4). Waktu terbit email seed dan manipulasi jam tidak punya sumber di TC, PRD, dan LLD; disediakan tim FE/BE.
  - TC-GS-USER-882 dan 883 tidak menyebut toast hasil Resend; spec tidak mengasersinya.
  - TC-GS-USER-894, 895, dan 896: `[email lama]` dan `[email baru]` tidak bernilai di TC; spec memakai email seed bersuffix. TC-GS-USER-895 Langkah Uji 1 tidak menyebut dialog `Cancel Pending Email Change`; spec menambah klik `[Cancel Change]` pada dialog itu.
  - TC-GS-USER-882 sampai 896 memakai nama Pre-setup (Mike Tan, Rina Putri, Dewi Lestari) sebagai target tulis; spec memakai padanan seed bersuffix (S-06).
