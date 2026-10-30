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
- Data Dinamis (suffix `{runId}-140`; di-seed lewat API di hook `before` sebelum penanda waktu T140; Division `Finance`; menggantikan Jane Smith No. 17, Dewi Lestari No. 12, Joko Susilo No. 19, Ahmad Fauzi No. 13, dan Budi Hartono No. 16):
  - `Jane Smith {runId}-140` (Email `janesmith+{runId}-140@qwertysystem.net`): Activated, Inactive (dinonaktifkan manual), Access `Supply Asset` (TC-GS-USER-878).
  - `Dewi Lestari {runId}-140` (Email `dewilestari+{runId}-140@qwertysystem.net`): Activated, Active, Access `Fixed Asset` dan `Global Settings` (TC-GS-USER-879).
  - `Joko Susilo {runId}-140` (Email `jokosusilo+{runId}-140@qwertysystem.net`): Activated, Active secara global, Access `Fixed Asset` dan `Supply Asset`, toggle per-produk Fixed Asset OFF (TC-GS-USER-880 lalu 881), tanpa borrowed asset dan tanpa approval.
  - `Ahmad Fauzi {runId}-140` (Email `ahmadfauzi+{runId}-140@qwertysystem.net`): Activated, Active, Access `Fixed Asset`, belum menjadi Temporary User (Old Value `—`) (TC-GS-USER-892). `{tgl14}` = hari uji + 14 hari.
  - `Dewi Lestari Temp {runId}-140` (Email `dewilestaritemp+{runId}-140@qwertysystem.net`): Activated, Active, Access `Fixed Asset`, Temporary User aktif dengan Temporary Until hari seeding + 30 hari (TC-GS-USER-893). `{tglLama}` = nilai Temporary Until awal yang dibaca di Popup Edit.
  - `Budi Hartono {runId}-140` (Email `budihartono+{runId}-140@qwertysystem.net`) dan `Budi Hartono Permanen {runId}-140` (Email `budihartonopermanen+{runId}-140@qwertysystem.net`): Activated, Temporary-expired (Temporary User, Temporary Until sudah terlewati), Inactive, Access `Fixed Asset` (TC-GS-USER-912 dan 913). `{tglLamaBudi}` dan `{tglLamaPermanen}` = nilai Temporary Until awal masing-masing seed; `{tgl7}` = hari uji + 7 hari. Semua tanggal dalam Date Format General Settings client.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, dan LLD): seeding user dengan status, toggle per-produk, Temporary User aktif, dan Temporary User yang sudah terlewati (Temporary Until masa lalu) lewat API; membuka Fixed Asset > Settings > User dengan akun Total Control; mengisi date picker (Temporary Until dan Extend period); membaca waktu server untuk penanda waktu T140.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketujuh user seed di atas. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar dan penanda waktu

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Catat penanda waktu T140 (waktu server) sebelum aksi pemicu pertama (klik `[Activate]` pada TC-GS-USER-878)

### TC-GS-USER-878: Log Activate field Status (Global)

3. Klik icon Search, ketik `Jane Smith {runId}-140`, tekan Enter
4. Klik switch Active baris `Jane Smith {runId}-140` (OFF)
5. Klik `[Activate]`
6. Tunggu aksi selesai (switch Active baris `Jane Smith {runId}-140` berubah ON)
7. Buka Modal Changelog User, klik icon Search, ketik `Jane Smith {runId}-140`, tekan Enter
8. Verifikasi Modal Changelog User: baris dengan Action `Activate`, Name `Jane Smith {runId}-140`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`, bertanggal pada atau sesudah T140
9. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Jane Smith {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
10. Buka Detail `Jane Smith {runId}-140` > Tab `Changelog`
11. Verifikasi Tab Changelog Detail `Jane Smith {runId}-140`: baris dengan Action `Activate`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`, bertanggal pada atau sesudah T140
12. Verifikasi Tab Changelog Detail `Jane Smith {runId}-140`: tepat 1 baris dengan Action `Activate` bertanggal pada atau sesudah T140 (tidak duplikat)
13. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Jane Smith {runId}-140`, tekan Enter
14. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Activate`, Object `User`, Name `Jane Smith {runId}-140`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`, bertanggal pada atau sesudah T140
15. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Jane Smith {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
16. Buka Global Settings > Activity Log, klik icon Search, ketik `Jane Smith {runId}-140`, tekan Enter
17. Verifikasi Activity Log: baris dengan Action `Activate`, Object `User`, Name `Jane Smith {runId}-140`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`, bertanggal pada atau sesudah T140
18. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Jane Smith {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)

### TC-GS-USER-879: Log Deactivate field Status (Global)

19. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari {runId}-140`, tekan Enter
20. Klik switch Active baris `Dewi Lestari {runId}-140` (ON)
21. Klik `[Deactivate]`
22. Tunggu aksi selesai (switch Active baris `Dewi Lestari {runId}-140` berubah OFF)
23. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari {runId}-140`, tekan Enter
24. Verifikasi Modal Changelog User: baris dengan Action `Deactivate`, Name `Dewi Lestari {runId}-140`, Field `Status (Global)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`, bertanggal pada atau sesudah T140
25. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Dewi Lestari {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
26. Buka Detail `Dewi Lestari {runId}-140` > Tab `Changelog`
27. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-140`: baris dengan Action `Deactivate`, Field `Status (Global)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`, bertanggal pada atau sesudah T140
28. Verifikasi Tab Changelog Detail `Dewi Lestari {runId}-140`: tepat 1 baris dengan Action `Deactivate` bertanggal pada atau sesudah T140 (tidak duplikat)
29. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari {runId}-140`, tekan Enter
30. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Deactivate`, Object `User`, Name `Dewi Lestari {runId}-140`, Field `Status (Global)`, Old Value `Active`, New Value `Inactive`, bertanggal pada atau sesudah T140
31. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Dewi Lestari {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
32. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari {runId}-140`, tekan Enter
33. Verifikasi Activity Log: baris dengan Action `Deactivate`, Object `User`, Name `Dewi Lestari {runId}-140`, Field `Status (Global)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`, bertanggal pada atau sesudah T140
34. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Dewi Lestari {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)

### TC-GS-USER-880: Log Activate field Status (Fixed Asset)

35. Buka Fixed Asset > Settings > User
36. Cari baris `Joko Susilo {runId}-140`
37. Aktifkan toggle per-produk Fixed Asset baris `Joko Susilo {runId}-140`
38. Tunggu aksi selesai (toggle Fixed Asset baris `Joko Susilo {runId}-140` berubah ON)
39. Buka Modal Changelog User, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
40. Verifikasi Modal Changelog User: baris dengan Action `Activate`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`, bertanggal pada atau sesudah T140
41. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Joko Susilo {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
42. Buka Detail `Joko Susilo {runId}-140` > Tab `Changelog`
43. Verifikasi Tab Changelog Detail `Joko Susilo {runId}-140`: baris dengan Action `Activate`, Field `Status (Fixed Asset)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`, bertanggal pada atau sesudah T140
44. Verifikasi Tab Changelog Detail `Joko Susilo {runId}-140`: tepat 1 baris dengan Action `Activate` bertanggal pada atau sesudah T140 (tidak duplikat)
45. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
46. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Activate`, Object `User`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Inactive`, New Value `Active`, bertanggal pada atau sesudah T140
47. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Joko Susilo {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
48. Buka Global Settings > Activity Log, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
49. Verifikasi Activity Log: baris dengan Action `Activate`, Object `User`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`, bertanggal pada atau sesudah T140
50. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Activate` untuk `Joko Susilo {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
51. Verifikasi Activity Log: baris `Activate` Status (Fixed Asset) untuk `Joko Susilo {runId}-140` berasal dari aksi di modul produk Fixed Asset (Fixed Asset > Settings > User) dan tercatat di surface Global Settings

### TC-GS-USER-881: Log Deactivate field Status (Fixed Asset)

52. Buka Fixed Asset > Settings > User
53. Cari baris `Joko Susilo {runId}-140`
54. Nonaktifkan toggle per-produk Fixed Asset baris `Joko Susilo {runId}-140`
55. Tunggu aksi selesai (toggle Fixed Asset baris `Joko Susilo {runId}-140` berubah OFF)
56. Buka Modal Changelog User, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
57. Verifikasi Modal Changelog User: baris dengan Action `Deactivate`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`, bertanggal pada atau sesudah T140
58. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Joko Susilo {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
59. Buka Detail `Joko Susilo {runId}-140` > Tab `Changelog`
60. Verifikasi Tab Changelog Detail `Joko Susilo {runId}-140`: baris dengan Action `Deactivate`, Field `Status (Fixed Asset)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`, bertanggal pada atau sesudah T140
61. Verifikasi Tab Changelog Detail `Joko Susilo {runId}-140`: tepat 1 baris dengan Action `Deactivate` bertanggal pada atau sesudah T140 (tidak duplikat)
62. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
63. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Deactivate`, Object `User`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Active`, New Value `Inactive`, bertanggal pada atau sesudah T140
64. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Joko Susilo {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
65. Buka Global Settings > Activity Log, klik icon Search, ketik `Joko Susilo {runId}-140`, tekan Enter
66. Verifikasi Activity Log: baris dengan Action `Deactivate`, Object `User`, Name `Joko Susilo {runId}-140`, Field `Status (Fixed Asset)`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N`, bertanggal pada atau sesudah T140
67. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Deactivate` untuk `Joko Susilo {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)

### TC-GS-USER-892: Log Set Temporary User field Temporary Until

68. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Ahmad Fauzi {runId}-140`, tekan Enter
69. Klik (⋯) baris `Ahmad Fauzi {runId}-140` → `Edit`
70. Centang `Set as Temporary User`
71. Pilih Temporary Until hari ini + 14 hari (`{tgl14}`)
72. Klik `[Save]`
73. Tunggu aksi selesai (Popup Edit tertutup)
74. Buka Modal Changelog User, klik icon Search, ketik `Ahmad Fauzi {runId}-140`, tekan Enter
75. Verifikasi Modal Changelog User: baris dengan Action `Set Temporary User`, Name `Ahmad Fauzi {runId}-140`, Field `Temporary Until`, Old Value `—`, New Value `{tgl14}`, Modified By `Siti N`, bertanggal pada atau sesudah T140
76. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Set Temporary User` untuk `Ahmad Fauzi {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
77. Buka Detail `Ahmad Fauzi {runId}-140` > Tab `Changelog`
78. Verifikasi Tab Changelog Detail `Ahmad Fauzi {runId}-140`: baris dengan Action `Set Temporary User`, Field `Temporary Until`, Old Value `—`, New Value `{tgl14}`, Modified By `Siti N`, bertanggal pada atau sesudah T140
79. Verifikasi Tab Changelog Detail `Ahmad Fauzi {runId}-140`: tepat 1 baris dengan Action `Set Temporary User` bertanggal pada atau sesudah T140 (tidak duplikat)
80. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Ahmad Fauzi {runId}-140`, tekan Enter
81. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Set Temporary User`, Object `User`, Name `Ahmad Fauzi {runId}-140`, Field `Temporary Until`, Old Value `—`, New Value `{tgl14}`, bertanggal pada atau sesudah T140
82. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Set Temporary User` untuk `Ahmad Fauzi {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
83. Buka Global Settings > Activity Log, klik icon Search, ketik `Ahmad Fauzi {runId}-140`, tekan Enter
84. Verifikasi Activity Log: baris dengan Action `Set Temporary User`, Object `User`, Name `Ahmad Fauzi {runId}-140`, Field `Temporary Until`, Old Value `—`, New Value `{tgl14}`, Modified By `Siti N`, bertanggal pada atau sesudah T140
85. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Set Temporary User` untuk `Ahmad Fauzi {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)

### TC-GS-USER-893: Log Remove Temporary User field Temporary Until

86. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Dewi Lestari Temp {runId}-140`, tekan Enter
87. Klik (⋯) baris `Dewi Lestari Temp {runId}-140` → `Edit`
88. Catat Temporary Until awal (+30 hari) sebagai `{tglLama}`
89. Uncheck `Set as Temporary User`
90. Klik `[Save]`
91. Tunggu aksi selesai (Popup Edit tertutup)
92. Buka Modal Changelog User, klik icon Search, ketik `Dewi Lestari Temp {runId}-140`, tekan Enter
93. Verifikasi Modal Changelog User: baris dengan Action `Remove Temporary User`, Name `Dewi Lestari Temp {runId}-140`, Field `Temporary Until`, Old Value `{tglLama}`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T140
94. Verifikasi Modal Changelog User: hasil Search memuat tepat 1 baris dengan Action `Remove Temporary User` untuk `Dewi Lestari Temp {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
95. Buka Detail `Dewi Lestari Temp {runId}-140` > Tab `Changelog`
96. Verifikasi Tab Changelog Detail `Dewi Lestari Temp {runId}-140`: baris dengan Action `Remove Temporary User`, Field `Temporary Until`, Old Value `{tglLama}`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T140
97. Verifikasi Tab Changelog Detail `Dewi Lestari Temp {runId}-140`: tepat 1 baris dengan Action `Remove Temporary User` bertanggal pada atau sesudah T140 (tidak duplikat)
98. Buka Detail `Siti Nurhaliza` > Tab `System Log`, klik icon Search, ketik `Dewi Lestari Temp {runId}-140`, tekan Enter
99. Verifikasi Tab System Log Detail Siti Nurhaliza: baris dengan Action `Remove Temporary User`, Object `User`, Name `Dewi Lestari Temp {runId}-140`, Field `Temporary Until`, Old Value `{tglLama}`, New Value `—`, bertanggal pada atau sesudah T140
100. Verifikasi Tab System Log Detail Siti Nurhaliza: hasil Search memuat tepat 1 baris dengan Action `Remove Temporary User` untuk `Dewi Lestari Temp {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)
101. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari Temp {runId}-140`, tekan Enter
102. Verifikasi Activity Log: baris dengan Action `Remove Temporary User`, Object `User`, Name `Dewi Lestari Temp {runId}-140`, Field `Temporary Until`, Old Value `{tglLama}`, New Value `—`, Modified By `Siti N`, bertanggal pada atau sesudah T140
103. Verifikasi Activity Log: hasil Search memuat tepat 1 baris dengan Action `Remove Temporary User` untuk `Dewi Lestari Temp {runId}-140` bertanggal pada atau sesudah T140 (tidak duplikat)

### TC-GS-USER-912: Reactivate Temporary Extend menulis Set Temporary User lalu Activate

104. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Budi Hartono {runId}-140`, tekan Enter
105. Klik switch Active baris `Budi Hartono {runId}-140` (OFF, Temporary-expired)
106. Pilih `Extend period`, isi date picker dengan hari ini + 7 hari (`{tgl7}`)
107. Klik `[Reactivate]`
108. Tunggu aksi selesai (switch Active baris `Budi Hartono {runId}-140` berubah ON)
109. Buka Detail `Budi Hartono {runId}-140` > Tab `Changelog`
110. Verifikasi Tab Changelog Detail `Budi Hartono {runId}-140`: baris dengan Action `Set Temporary User`, Field `Temporary Until`, Old Value `{tglLamaBudi}`, New Value `{tgl7}`, bertanggal pada atau sesudah T140
111. Verifikasi Tab Changelog Detail `Budi Hartono {runId}-140`: baris dengan Action `Activate`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`, bertanggal pada atau sesudah T140
112. Verifikasi Tab Changelog Detail `Budi Hartono {runId}-140`: Date baris `Activate` sama atau lebih baru dari Date baris `Set Temporary User` (baris Activate mengikuti baris Set Temporary User)

### TC-GS-USER-913: Reactivate Temporary Make permanent menulis Remove Temporary User lalu Activate

113. Klik menu User di sidebar Global Settings, klik icon Search, ketik `Budi Hartono Permanen {runId}-140`, tekan Enter
114. Klik switch Active baris `Budi Hartono Permanen {runId}-140` (OFF, Temporary-expired)
115. Pilih `Make permanent`
116. Klik `[Reactivate]`
117. Tunggu aksi selesai (switch Active baris `Budi Hartono Permanen {runId}-140` berubah ON)
118. Buka Detail `Budi Hartono Permanen {runId}-140` > Tab `Changelog`
119. Verifikasi Tab Changelog Detail `Budi Hartono Permanen {runId}-140`: baris dengan Action `Remove Temporary User`, Field `Temporary Until`, Old Value `{tglLamaPermanen}`, New Value `—`, bertanggal pada atau sesudah T140
120. Verifikasi Tab Changelog Detail `Budi Hartono Permanen {runId}-140`: baris dengan Action `Activate`, Field `Status (Global)`, Old Value `Inactive`, New Value `Active`, bertanggal pada atau sesudah T140
121. Verifikasi Tab Changelog Detail `Budi Hartono Permanen {runId}-140`: Date baris `Activate` sama atau lebih baru dari Date baris `Remove Temporary User` (baris Activate mengikuti baris Remove Temporary User)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penanda waktu T140 dicatat di langkah 2, sebelum aksi pemicu pertama yang diasersi (S-12). Tiap TC memakai user seed sendiri, kecuali TC-GS-USER-880 dan 881 yang berurutan pada `Joko Susilo {runId}-140` (baris dibedakan lewat Action dan Old Value atau New Value). Baris log dikenali lewat nama bersuffix, Action, dan tanggal pada atau sesudah T140, bukan posisi teratas.
- Surface disebut satu per satu pada TC-GS-USER-878, 879, 880, 881, 892, dan 893: Modal Changelog User, Tab Changelog Detail, Tab System Log Detail Siti Nurhaliza, dan Activity Log. TC-GS-USER-912 dan 913 hanya memuat Tab Changelog Detail sesuai Langkah Uji TC. Expected "Tepat 1 baris per surface (tidak duplikat)" diasersi sebagai jumlah baris dengan Action dan nama yang sama sesudah `Verifikasi` isi baris pada surface yang sama.
- Urutan TC di spec mengikuti urutan sourceTc. TC-GS-USER-881 mengikuti TC-GS-USER-880 pada user seed yang sama (toggle OFF lalu ON lalu OFF); tidak ada TC yang menghapus data.
- Pembagian TC lintas spec: seluruh TC di spec ini memverifikasi pencatatan yang berhasil; asersi absence kelas g untuk aksi tanpa perubahan ada di spec `TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role`.
- Spec melewati sekitar 35 langkah (121 langkah). Alasan: seluruh blok satu kelas (pencatatan log) dengan user seed sendiri per TC (kecuali pasangan 880 dan 881) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) mendominasi jumlah langkah dan tidak dihitung ke batas ukuran (bagian 3 konvensi).
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 sampai 7, 10, 13, 16, 19 sampai 23, 26, 29, 32, 35 sampai 39, 42, 45, 48, 52 sampai 56, 59, 62, 65, 68 sampai 74, 77, 80, 83, 86 sampai 92, 95, 98, 101, 104 sampai 109, 113 sampai 118. Frasa "Buka ..." pada langkah baca-log mencakup navigasi dari halaman sebelumnya (klik menu User di sidebar Global Settings atau menu Activity Log), menutup Modal Changelog User dengan `✕`, dan, untuk Detail, Search nama pada User List lalu klik Name. Pembukaan Detail `Siti Nurhaliza` mengikuti pola yang sama.
- Temuan untuk QA:
  - TC-GS-USER-878 dan 879: Langkah Uji menyebut "via toggle" tanpa menyebut dialog Activate atau Deactivate; spec menambahkan klik `[Activate]` dan `[Deactivate]` sesuai dialog pada TC Toggle Active.
  - TC-GS-USER-880 dan 881: aksi toggle per-produk di Fixed Asset > Settings > User tidak menyebut dialog atau konfirmasi; spec tidak menulis langkah konfirmasi. Keadaan awal toggle per-produk (OFF untuk 880, ON untuk 881) tidak disebut precondition; seeding toggle per-produk disediakan tim FE/BE. Expected f ("Baris dari modul produk tercatat di surface GS") diasersi sebagai kesimpulan pada Activity Log.
  - TC-GS-USER-892, 893, 912, dan 913: Expected memakai placeholder `[tanggal]` dan `[tanggal lama]` tanpa format; spec memakai Date Format General Settings client. Cara membuat Temporary Until yang sudah terlewati untuk 912 dan 913 lewat seeding tidak disebut TC.
  - TC-GS-USER-912 dan 913: Expected "Diikuti baris Activate" tidak mendefinisikan urutan; spec mengasersi Date baris `Activate` sama atau lebih baru dari baris Set atau Remove Temporary User. Modified By tidak disebut Expected dan tidak diasersi. TC-GS-USER-913 Precondition tidak menyebut Budi Hartono Temporary-expired dan Inactive; spec memakai keadaan yang sama dengan TC-GS-USER-912 pada user seed terpisah.
  - TC-GS-USER-892, 893, 912, 913 memakai nama Pre-setup (Ahmad Fauzi, Dewi Lestari, Budi Hartono) sebagai target tulis; spec memakai padanan seed bersuffix (S-06).
