---
id: TC-GS-USER-E2E-140-pencatatan-status-global-per-produk-dan-temporary-user
title: "Pencatatan Activate dan Deactivate (Status Global dan Fixed Asset), Set dan Remove Temporary User, serta Reactivate Temporary Extend dan Make Permanent di Changelog, System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-878
  - TC-GS-USER-879
  - TC-GS-USER-880
  - TC-GS-USER-881
  - TC-GS-USER-892
  - TC-GS-USER-893
  - TC-GS-USER-912
  - TC-GS-USER-913
coverage:
  web: automated
---

# Pencatatan Activate dan Deactivate (Status Global dan Fixed Asset), Set dan Remove Temporary User, serta Reactivate Temporary Extend dan Make Permanent di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Siti Nurhaliza (No. 2) sebagai pelaku dan pemilik Tab System Log; Division `Finance` (No. 23); Client subscribe Fixed Asset dan Supply Asset (No. 26). Data target Pre-setup No. 10 sampai 21 tidak dipakai sebagai target aksi dan tidak diubah (S-06).
- Data Dinamis (suffix `{runId}-140`; di-seed lewat API di hook `before`; Division `Finance`; menggantikan Jane Smith No. 17, Dewi Lestari No. 12, Joko Susilo No. 19, Ahmad Fauzi No. 13, dan Budi Hartono No. 16):
  - `Jane Smith {runId}-140` (Email `janesmith+{runId}-140@qwertysystem.net`): Activated, Inactive (dinonaktifkan manual), Access `Supply Asset` (TC-GS-USER-878).
  - `Dewi Lestari {runId}-140` (Email `dewilestari+{runId}-140@qwertysystem.net`): Activated, Active, Access `Fixed Asset` dan `Global Settings` (TC-GS-USER-879).
  - `Joko Susilo {runId}-140` (Email `jokosusilo+{runId}-140@qwertysystem.net`): Activated, Active secara global, Access `Fixed Asset` dan `Supply Asset`, toggle per-produk Fixed Asset OFF (TC-GS-USER-880 lalu 881), tanpa borrowed asset dan tanpa approval.
  - `Ahmad Fauzi {runId}-140` (Email `ahmadfauzi+{runId}-140@qwertysystem.net`): Activated, Active, Access `Fixed Asset`, belum menjadi Temporary User (Old Value `—`) (TC-GS-USER-892). `{tgl14}` = hari uji + 14 hari.
  - `Dewi Lestari Temp {runId}-140` (Email `dewilestaritemp+{runId}-140@qwertysystem.net`): Activated, Active, Access `Fixed Asset`, Temporary User aktif dengan Temporary Until hari seeding + 30 hari (TC-GS-USER-893). `{tglLama}` = nilai Temporary Until awal yang dibaca di Popup Edit.
  - `Budi Hartono {runId}-140` (Email `budihartono+{runId}-140@qwertysystem.net`) dan `Budi Hartono Permanen {runId}-140` (Email `budihartonopermanen+{runId}-140@qwertysystem.net`): Activated, Temporary-expired (Temporary User, Temporary Until sudah terlewati), Inactive, Access `Fixed Asset` (TC-GS-USER-912 dan 913). `{tglLamaBudi}` dan `{tglLamaPermanen}` = nilai Temporary Until awal masing-masing seed; `{tgl7}` = hari uji + 7 hari. Semua tanggal dalam Date Format General Settings client.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, dan LLD): seeding user dengan status, toggle per-produk, Temporary User aktif, dan Temporary User yang sudah terlewati (Temporary Until masa lalu) lewat API; membuka Fixed Asset > Settings > User dengan akun Total Control; mengisi date picker (Temporary Until dan Extend period).
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketujuh user seed di atas. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)

### TC-GS-USER-878: Log Activate field Status (Global)

2. Klik icon Search, ketik `Jane Smith {runId}-140`, tekan Enter
3. Klik switch Active baris `Jane Smith {runId}-140` (OFF)
4. Klik `[Activate]`
5. Tunggu aksi selesai (switch Active baris `Jane Smith {runId}-140` berubah ON)
6. Buka Modal Changelog User, klik icon Search, ketik `Jane Smith {runId}-140`, tekan Enter
7. Verifikasi Modal Changelog User: baris dengan Action `Activate`, Name `Jane Smith {runId}-140`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
8. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Jane Smith {runId}-140` (tidak duplikat)
9. Buka Detail `Jane Smith {runId}-140` > Tab `Changelog`
10. Verifikasi Tab Changelog Detail `Jane Smith {runId}-140`: baris dengan Action `Activate`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
11. Verifikasi Tab Changelog Detail `Jane Smith {runId}-140`: tepat 1 baris dengan Action `Activate` (tidak duplikat)
12. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Jane Smith {runId}-140`, tekan Enter
13. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Activate`, Object `User`, Name `Jane Smith {runId}-140`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`
14. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Jane Smith {runId}-140` (tidak duplikat)
15. Buka Global Settings > Activity Log, klik icon Search, ketik `Jane Smith {runId}-140`, tekan Enter
16. Verifikasi Activity Log: baris dengan Action `Activate`, Object `User`, Name `Jane Smith {runId}-140`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
17. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Jane Smith {runId}-140` (tidak duplikat)

### TC-GS-USER-879: Log Deactivate field Status (Global)

18. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari {runId}-140`, tekan Enter
19. Klik switch Active baris `Dewi Lestari {runId}-140` (ON)
20. Klik `[Deactivate]`
21. Tunggu aksi selesai (switch Active baris `Dewi Lestari {runId}-140` berubah OFF)
22. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari {runId}-140`, tekan Enter
23. Verifikasi Modal Changelog User: baris dengan Action `Deactivate`, Name `Dewi Lestari {runId}-140`, Field `Status (Global)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`
24. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Dewi Lestari {runId}-140` (tidak duplikat)
25. Buka Detail `Dewi Lestari {runId}-140` > Tab `Changelog`
26. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-140`: baris dengan Action `Deactivate`, Field `Status (Global)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`
27. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-140`: tepat 1 baris dengan Action `Deactivate` (tidak duplikat)
28. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari {runId}-140`, tekan Enter
29. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Deactivate`, Object `User`, Name `Dewi Lestari {runId}-140`, Field `Status (Global)`, Old Value `Active`, New Value `Inactive`
30. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Dewi Lestari {runId}-140` (tidak duplikat)
31. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari {runId}-140`, tekan Enter
32. Verifikasi Activity Log: baris dengan Action `Deactivate`, Object `User`, Name `Dewi Lestari {runId}-140`, Field `Status (Global)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`
33. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Dewi Lestari {runId}-140` (tidak duplikat)

### TC-GS-USER-880: Log Activate field Status (Fixed Asset)

34. Buka Fixed Asset > Settings > User
35. Cari baris `Joko Susilo {runId}-140`
36. Aktifkan toggle per-produk Fixed Asset baris `Joko Susilo {runId}-140`
37. Tunggu aksi selesai (toggle Fixed Asset baris `Joko Susilo {runId}-140` berubah ON)
38. Buka Modal Changelog User, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
39. Verifikasi Modal Changelog User: baris dengan Action `Activate`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
40. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Joko Susilo {runId}-140` (tidak duplikat)
41. Buka Detail `Joko Susilo {runId}-140` > Tab `Changelog`
42. Verifikasi Tab Changelog Detail `Joko Susilo {runId}-140`: baris dengan Action `Activate`, Field `Status (Fixed Asset)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
43. Verifikasi Tab Changelog Detail `Joko Susilo {runId}-140`: tepat 1 baris dengan Action `Activate` (tidak duplikat)
44. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
45. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Activate`, Object `User`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Inactive`, New Value `Active`
46. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Joko Susilo {runId}-140` (tidak duplikat)
47. Buka Global Settings > Activity Log, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
48. Verifikasi Activity Log: baris dengan Action `Activate`, Object `User`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
49. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Joko Susilo {runId}-140` (tidak duplikat)
50. Verifikasi Activity Log: baris `Activate` Status (Fixed Asset) untuk `Joko Susilo {runId}-140` berasal dari aksi di modul produk Fixed Asset (Fixed Asset > Settings > User) dan tercatat di surface Global Settings

### TC-GS-USER-881: Log Deactivate field Status (Fixed Asset)

51. Buka Fixed Asset > Settings > User
52. Cari baris `Joko Susilo {runId}-140`
53. Nonaktifkan toggle per-produk Fixed Asset baris `Joko Susilo {runId}-140`
54. Tunggu aksi selesai (toggle Fixed Asset baris `Joko Susilo {runId}-140` berubah OFF)
55. Buka Modal Changelog User, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
56. Verifikasi Modal Changelog User: baris dengan Action `Deactivate`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`
57. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Joko Susilo {runId}-140` (tidak duplikat)
58. Buka Detail `Joko Susilo {runId}-140` > Tab `Changelog`
59. Verifikasi Tab Changelog Detail `Joko Susilo {runId}-140`: baris dengan Action `Deactivate`, Field `Status (Fixed Asset)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`
60. Verifikasi Tab Changelog Detail `Joko Susilo {runId}-140`: tepat 1 baris dengan Action `Deactivate` (tidak duplikat)
61. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
62. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Deactivate`, Object `User`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Active`, New Value `Inactive`
63. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Joko Susilo {runId}-140` (tidak duplikat)
64. Buka Global Settings > Activity Log, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
65. Verifikasi Activity Log: baris dengan Action `Deactivate`, Object `User`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`
66. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Joko Susilo {runId}-140` (tidak duplikat)

### TC-GS-USER-892: Log Set Temporary User field Temporary Until

67. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Ahmad Fauzi {runId}-140`, tekan Enter
68. Klik (⋯) baris `Ahmad Fauzi {runId}-140` → `Edit`
69. Centang `Set as Temporary User`
70. Pilih Temporary Until hari ini + 14 hari (`{tgl14}`)
71. Klik `[Save]`
72. Tunggu aksi selesai (Popup Edit tertutup)
73. Buka Modal Changelog User, klik icon Search, ketik `Ahmad Fauzi {runId}-140`, tekan Enter
74. Verifikasi Modal Changelog User: baris dengan Action `Set Temporary User`, Name `Ahmad Fauzi {runId}-140`, Field `Temporary Until`, Old Value `—`, New Value `{tgl14}`, Modified By `Siti N`
75. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Set Temporary User` untuk `Ahmad Fauzi {runId}-140` (tidak duplikat)
76. Buka Detail `Ahmad Fauzi {runId}-140` > Tab `Changelog`
77. Verifikasi Tab Changelog Detail `Ahmad Fauzi {runId}-140`: baris dengan Action `Set Temporary User`, Field `Temporary Until`, Old Value `—`, New Value `{tgl14}`, Modified By `Siti N`
78. Verifikasi Tab Changelog Detail `Ahmad Fauzi {runId}-140`: tepat 1 baris dengan Action `Set Temporary User` (tidak duplikat)
79. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Ahmad Fauzi {runId}-140`, tekan Enter
80. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Set Temporary User`, Object `User`, Name `Ahmad Fauzi {runId}-140`, Field `Temporary Until`, Old Value `—`, New Value `{tgl14}`
81. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Set Temporary User` untuk `Ahmad Fauzi {runId}-140` (tidak duplikat)
82. Buka Global Settings > Activity Log, klik icon Search, ketik `Ahmad Fauzi {runId}-140`, tekan Enter
83. Verifikasi Activity Log: baris dengan Action `Set Temporary User`, Object `User`, Name `Ahmad Fauzi {runId}-140`, Field `Temporary Until`, Old Value `—`, New Value `{tgl14}`, Modified By `Siti N`
84. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Set Temporary User` untuk `Ahmad Fauzi {runId}-140` (tidak duplikat)

### TC-GS-USER-893: Log Remove Temporary User field Temporary Until

85. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari Temp {runId}-140`, tekan Enter
86. Klik (⋯) baris `Dewi Lestari Temp {runId}-140` → `Edit`
87. Catat Temporary Until awal (+30 hari) sebagai `{tglLama}`
88. Uncheck `Set as Temporary User`
89. Klik `[Save]`
90. Tunggu aksi selesai (Popup Edit tertutup)
91. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari Temp {runId}-140`, tekan Enter
92. Verifikasi Modal Changelog User: baris dengan Action `Remove Temporary User`, Name `Dewi Lestari Temp {runId}-140`, Field `Temporary Until`, Old Value `{tglLama}`, New Value `—`, Modified By `Siti N`
93. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Remove Temporary User` untuk `Dewi Lestari Temp {runId}-140` (tidak duplikat)
94. Buka Detail `Dewi Lestari Temp {runId}-140` > Tab `Changelog`
95. Verifikasi Tab Changelog Detail `Dewi Lestari Temp {runId}-140`: baris dengan Action `Remove Temporary User`, Field `Temporary Until`, Old Value `{tglLama}`, New Value `—`, Modified By `Siti N`
96. Verifikasi Tab Changelog Detail `Dewi Lestari Temp {runId}-140`: tepat 1 baris dengan Action `Remove Temporary User` (tidak duplikat)
97. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari Temp {runId}-140`, tekan Enter
98. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Remove Temporary User`, Object `User`, Name `Dewi Lestari Temp {runId}-140`, Field `Temporary Until`, Old Value `{tglLama}`, New Value `—`
99. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Remove Temporary User` untuk `Dewi Lestari Temp {runId}-140` (tidak duplikat)
100. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari Temp {runId}-140`, tekan Enter
101. Verifikasi Activity Log: baris dengan Action `Remove Temporary User`, Object `User`, Name `Dewi Lestari Temp {runId}-140`, Field `Temporary Until`, Old Value `{tglLama}`, New Value `—`, Modified By `Siti N`
102. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Remove Temporary User` untuk `Dewi Lestari Temp {runId}-140` (tidak duplikat)

### TC-GS-USER-912: Reactivate Temporary Extend menulis Set Temporary User lalu Activate

103. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Budi Hartono {runId}-140`, tekan Enter
104. Klik switch Active baris `Budi Hartono {runId}-140` (OFF, Temporary-expired)
105. Pilih `Extend period`, isi date picker dengan hari ini + 7 hari (`{tgl7}`)
106. Klik `[Reactivate]`
107. Tunggu aksi selesai (switch Active baris `Budi Hartono {runId}-140` berubah ON)
108. Buka Detail `Budi Hartono {runId}-140` > Tab `Changelog`
109. Verifikasi Tab Changelog Detail `Budi Hartono {runId}-140`: baris dengan Action `Set Temporary User`, Field `Temporary Until`, Old Value `{tglLamaBudi}`, New Value `{tgl7}`
110. Verifikasi Tab Changelog Detail `Budi Hartono {runId}-140`: baris dengan Action `Activate`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`
111. Verifikasi Tab Changelog Detail `Budi Hartono {runId}-140`: Date baris `Activate` sama atau lebih baru dari Date baris `Set Temporary User` (baris Activate mengikuti baris Set Temporary User)

### TC-GS-USER-913: Reactivate Temporary Make permanent menulis Remove Temporary User lalu Activate

112. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Budi Hartono Permanen {runId}-140`, tekan Enter
113. Klik switch Active baris `Budi Hartono Permanen {runId}-140` (OFF, Temporary-expired)
114. Pilih `Make permanent`
115. Klik `[Reactivate]`
116. Tunggu aksi selesai (switch Active baris `Budi Hartono Permanen {runId}-140` berubah ON)
117. Buka Detail `Budi Hartono Permanen {runId}-140` > Tab `Changelog`
118. Verifikasi Tab Changelog Detail `Budi Hartono Permanen {runId}-140`: baris dengan Action `Remove Temporary User`, Field `Temporary Until`, Old Value `{tglLamaPermanen}`, New Value `—`
119. Verifikasi Tab Changelog Detail `Budi Hartono Permanen {runId}-140`: baris dengan Action `Activate`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`
120. Verifikasi Tab Changelog Detail `Budi Hartono Permanen {runId}-140`: Date baris `Activate` sama atau lebih baru dari Date baris `Remove Temporary User` (baris Activate mengikuti baris Remove Temporary User)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Baris log dikenali lewat nama bersuffix `{runId}-140` yang unik per run, Action, dan Field, bukan posisi teratas dan bukan penanda waktu (S-12). Tiap TC memakai user seed sendiri, kecuali TC-GS-USER-880 dan 881 yang berurutan pada `Joko Susilo {runId}-140` (baris dibedakan lewat Action dan Old Value atau New Value).
- Surface disebut satu per satu pada TC-GS-USER-878, 879, 880, 881, 892, dan 893: Modal Changelog User, Tab Changelog Detail, Tab System Log Detail Siti Nurhaliza, dan Activity Log. TC-GS-USER-912 dan 913 hanya memuat Tab Changelog Detail sesuai Langkah Uji TC. Expected "Tepat 1 baris per surface (tidak duplikat)" diasersi sebagai jumlah baris dengan Action dan nama yang sama sesudah `Verifikasi` isi baris pada surface yang sama.
- Urutan TC di spec mengikuti urutan sourceTc. TC-GS-USER-881 mengikuti TC-GS-USER-880 pada user seed yang sama (toggle OFF lalu ON lalu OFF); tidak ada TC yang menghapus data.
- Pembagian TC lintas spec: seluruh TC di spec ini memverifikasi pencatatan yang berhasil; asersi absence kelas g untuk aksi tanpa perubahan ada di spec `TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role`.
- Spec melewati sekitar 35 langkah (120 langkah). Alasan: seluruh blok satu kelas (pencatatan log) dengan user seed sendiri per TC (kecuali pasangan 880 dan 881) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) mendominasi jumlah langkah dan tidak dihitung ke batas ukuran (bagian 3 konvensi).
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 sampai 6, 9, 12, 15, 18 sampai 22, 25, 28, 31, 34 sampai 38, 41, 44, 47, 51 sampai 55, 58, 61, 64, 67 sampai 73, 76, 79, 82, 85 sampai 91, 94, 97, 100, 103 sampai 108, 112 sampai 117. Frasa "Buka ..." pada langkah baca-log mencakup navigasi dari halaman sebelumnya (klik menu User di sidebar Global Settings atau menu Activity Log), menutup Modal Changelog User dengan `✕`, dan, untuk Detail, Search nama pada User List lalu klik Name. Pembukaan Detail `Siti Nurhaliza` mengikuti pola yang sama.
- Temuan untuk QA:
  - TC-GS-USER-878 dan 879: Langkah Uji menyebut "via toggle" tanpa menyebut dialog Activate atau Deactivate; spec menambahkan klik `[Activate]` dan `[Deactivate]` sesuai dialog pada TC Toggle Active.
  - TC-GS-USER-880 dan 881: aksi toggle per-produk di Fixed Asset > Settings > User tidak menyebut dialog atau konfirmasi; spec tidak menulis langkah konfirmasi. Keadaan awal toggle per-produk (OFF untuk 880, ON untuk 881) tidak disebut precondition; seeding toggle per-produk disediakan tim FE/BE. Expected f ("Baris dari modul produk tercatat di surface GS") diasersi sebagai kesimpulan pada Activity Log.
  - TC-GS-USER-892, 893, 912, dan 913: Expected memakai placeholder `[tanggal]` dan `[tanggal lama]` tanpa format; spec memakai Date Format General Settings client. Cara membuat Temporary Until yang sudah terlewati untuk 912 dan 913 lewat seeding tidak disebut TC.
  - TC-GS-USER-912 dan 913: Expected "Diikuti baris Activate" tidak mendefinisikan urutan; spec mengasersi Date baris `Activate` sama atau lebih baru dari baris Set atau Remove Temporary User. Modified By tidak disebut Expected dan tidak diasersi. TC-GS-USER-913 Precondition tidak menyebut Budi Hartono Temporary-expired dan Inactive; spec memakai keadaan yang sama dengan TC-GS-USER-912 pada user seed terpisah.
  - TC-GS-USER-892, 893, 912, 913 memakai nama Pre-setup (Ahmad Fauzi, Dewi Lestari, Budi Hartono) sebagai target tulis; spec memakai padanan seed bersuffix (S-06).
  - Asumsi seeding: seeding user dan data pendukung lewat API hanya menghasilkan entri log aksi `Create`; spec tidak mengandalkan entri Update atau Delete dari seeding (diterima 2026-11-03).
