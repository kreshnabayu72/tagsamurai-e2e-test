---
id: TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert
title: "Pencatatan Assign dan Remove Access Level, Permission Individual, Auto-Revert Tier, dan Assign dari Tab Role di Changelog, System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-898
  - TC-GS-USER-899
  - TC-GS-USER-900
  - TC-GS-USER-901
  - TC-GS-USER-902
  - TC-GS-USER-903
  - TC-GS-USER-904
  - TC-GS-USER-905
  - TC-GS-USER-906
  - TC-GS-USER-1052
coverage:
  web: automated
---

# Pencatatan Assign dan Remove Access Level, Permission Individual, Auto-Revert Tier, dan Assign dari Tab Role di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor pertama: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): akun aktor Siti Nurhaliza (No. 2) sebagai pelaku (Modified By `Siti N`) dan pemilik Tab System Log; role sistem `Manage TAG`, `Manage files`, dan `Manage hardware` (definisi role tetap, hanya penugasannya ke user seed yang berubah). User Pre-setup Andi Wijaya, Doni Pratama, dan Ahmad Fauzi (No. 10, 11, 13) tidak dipakai karena aksi tulis memakai user seed milik spec (S-06).
- Data Dinamis milik spec (suffix per run dan nomor spec), semuanya Activated, Division `Finance`, Access `Global Settings`, di-seed lewat API di hook `before` (HK1) dan dihapus di hook `after`:
  - `Andi Wijaya {runId}-144`, Email `andiwijaya+{runId}-144@qwertysystem.net`, tanpa tier akses (Basic): target TC-GS-USER-898 (Assign Total Control) lalu TC-GS-USER-899 (Remove Total Control).
  - `Andi Wijaya B {runId}-144`, Email `andiwijayab+{runId}-144@qwertysystem.net`, tier Total Control: target TC-GS-USER-905 (Auto-Revert).
  - `Doni Pratama {runId}-144`, Email `donipratama+{runId}-144@qwertysystem.net`, tanpa tier akses (Basic): target TC-GS-USER-900 (Assign Read Only) lalu TC-GS-USER-901 (Remove Read Only).
  - `Doni Pratama B {runId}-144`, Email `donipratamab+{runId}-144@qwertysystem.net`, tier Read Only: target TC-GS-USER-906 (Auto-Revert).
  - `Ahmad Fauzi {runId}-144`, Email `ahmadfauzi+{runId}-144@qwertysystem.net`, tanpa tier akses, role `Manage files` sudah Assigned, role `Manage TAG` dan `Manage hardware` belum di-assign: target TC-GS-USER-903, 902, 1052, dan 904.
- Kemampuan teknis, disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut endpoint): seeding user dengan tier Total Control atau Read Only dan penugasan role individual (`Manage files`) lewat API; seeding memakai endpoint aplikasi sehingga entri log seed ditulis sebelum baseline dicatat; kemampuan baca jumlah baris log per user dan Action lewat BE dicatat di butir Baseline log di bawah.
- State global: tidak ada. Tier dan penugasan role hanya pada user seed milik spec. Suite berjalan serial (`suite.md`).
- Baseline log: jumlah entri audit trail permanen (Changelog, System Log, Activity Log) tidak dapat diturunkan dari seeding. Sebelum aksi pemicu tiap TC, spec mencatat baseline `{n0}` = jumlah baris per user target dan Action (dan Field) yang diasersi, pada keempat surface (Modal Changelog User, Tab Changelog user target, Tab System Log Siti Nurhaliza, Activity Log), lewat kemampuan baca BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak menyebut endpoint). Asersi memakai selisih terhadap baseline itu (S-12), dicatat ulang untuk tiap TC; entri seed ditulis sebelum baseline sehingga ikut dalam baseline.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API kelima user seed bersuffix `{runId}-144` (penugasan role dan tier ikut hilang). Hook `before` menghapus sisa user bersuffix `-144` dari run lama. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### TC-GS-USER-898: Assign Total Control mencatat Field Access Level di empat surface

1. Catat baseline `{n0}` pada keempat surface (lewat kemampuan baca BE): jumlah baris Action `Assign` dengan Field `Access Level` untuk `Andi Wijaya {runId}-144`, dan `{n0-semua}` jumlah seluruh baris untuk `Andi Wijaya {runId}-144` di Modal Changelog User
2. Buka Global Settings > Role & Permission, buka Tab Total Control, klik [+ Assign]
3. Isi Search Popup Table User Picker dengan `Andi Wijaya {runId}-144`, tekan Enter, centang barisnya, klik [Assign]
4. Tunggu aksi selesai (Popup tertutup)
5. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
6. Verifikasi Modal Changelog User: jumlah baris dengan Action `Assign` dan Field `Access Level` untuk `Andi Wijaya {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
7. Verifikasi Modal Changelog User: baris teratas dengan Action `Assign`, User Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Siti N`
8. Verifikasi Modal Changelog User: jumlah seluruh baris untuk `Andi Wijaya {runId}-144` bertambah tepat 1 dari baseline `{n0-semua}`, yaitu 1 baris ringkasan `Access Level` tersebut tanpa baris per role
9. Tutup Modal Changelog User
10. Buka Global Settings > User > User List, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter, klik Name `Andi Wijaya {runId}-144`, buka Tab Changelog
11. Verifikasi Tab Changelog `Andi Wijaya {runId}-144`: jumlah baris dengan Action `Assign` dan Field `Access Level` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
12. Verifikasi Tab Changelog `Andi Wijaya {runId}-144`: baris teratas dengan Action `Assign`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Siti N`
13. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
14. Verifikasi Tab System Log `Siti Nurhaliza`: jumlah baris dengan Action `Assign`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
15. Verifikasi Tab System Log `Siti Nurhaliza`: baris teratas dengan Action `Assign`, Object `Total Control`, Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Total Control`
16. Buka Global Settings > Activity Log, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
17. Verifikasi Activity Log: jumlah baris dengan Action `Assign`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
18. Verifikasi Activity Log: baris teratas dengan Action `Assign`, Object `Total Control`, Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Siti N`

### TC-GS-USER-899: Remove Total Control mencatat Field Access Level di empat surface

19. Catat baseline `{n0}` pada keempat surface (lewat kemampuan baca BE): jumlah baris Action `Remove` dengan Field `Access Level` untuk `Andi Wijaya {runId}-144`
20. Buka Global Settings > Role & Permission, buka Tab Total Control, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter, klik `⋯` pada baris `Andi Wijaya {runId}-144` > Remove
21. Klik [Remove] pada dialog Remove Total Control
22. Tunggu aksi selesai (dialog tertutup)
23. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
24. Verifikasi Modal Changelog User: jumlah baris dengan Action `Remove` dan Field `Access Level` untuk `Andi Wijaya {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
25. Verifikasi Modal Changelog User: baris teratas dengan Action `Remove`, User Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`
26. Tutup Modal Changelog User
27. Buka Global Settings > User > User List, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter, klik Name `Andi Wijaya {runId}-144`, buka Tab Changelog
28. Verifikasi Tab Changelog `Andi Wijaya {runId}-144`: jumlah baris dengan Action `Remove` dan Field `Access Level` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
29. Verifikasi Tab Changelog `Andi Wijaya {runId}-144`: baris teratas dengan Action `Remove`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`
30. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
31. Verifikasi Tab System Log `Siti Nurhaliza`: jumlah baris dengan Action `Remove`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
32. Verifikasi Tab System Log `Siti Nurhaliza`: baris teratas dengan Action `Remove`, Object `Total Control`, Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`
33. Buka Global Settings > Activity Log, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
34. Verifikasi Activity Log: jumlah baris dengan Action `Remove`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
35. Verifikasi Activity Log: baris teratas dengan Action `Remove`, Object `Total Control`, Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`

### TC-GS-USER-900: Assign Read Only mencatat Field Access Level di empat surface

36. Catat baseline `{n0}` pada keempat surface (lewat kemampuan baca BE): jumlah baris Action `Assign` dengan Field `Access Level` untuk `Doni Pratama {runId}-144`
37. Buka Global Settings > Role & Permission, buka Tab Read Only, klik [+ Assign]
38. Isi Search Popup Table User Picker dengan `Doni Pratama {runId}-144`, tekan Enter, centang barisnya, klik [Assign]
39. Tunggu aksi selesai (Popup tertutup)
40. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
41. Verifikasi Modal Changelog User: jumlah baris dengan Action `Assign` dan Field `Access Level` untuk `Doni Pratama {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
42. Verifikasi Modal Changelog User: baris teratas dengan Action `Assign`, User Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Read Only`, Modified By `Siti N`
43. Tutup Modal Changelog User
44. Buka Global Settings > User > User List, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter, klik Name `Doni Pratama {runId}-144`, buka Tab Changelog
45. Verifikasi Tab Changelog `Doni Pratama {runId}-144`: jumlah baris dengan Action `Assign` dan Field `Access Level` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
46. Verifikasi Tab Changelog `Doni Pratama {runId}-144`: baris teratas dengan Action `Assign`, Field `Access Level`, Old Value `—`, New Value `Read Only`, Modified By `Siti N`
47. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
48. Verifikasi Tab System Log `Siti Nurhaliza`: jumlah baris dengan Action `Assign`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
49. Verifikasi Tab System Log `Siti Nurhaliza`: baris teratas dengan Action `Assign`, Object `Read Only`, Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Read Only`
50. Buka Global Settings > Activity Log, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
51. Verifikasi Activity Log: jumlah baris dengan Action `Assign`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
52. Verifikasi Activity Log: baris teratas dengan Action `Assign`, Object `Read Only`, Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Read Only`, Modified By `Siti N`

### TC-GS-USER-901: Remove Read Only mencatat Field Access Level di empat surface

53. Catat baseline `{n0}` pada keempat surface (lewat kemampuan baca BE): jumlah baris Action `Remove` dengan Field `Access Level` untuk `Doni Pratama {runId}-144`
54. Buka Global Settings > Role & Permission, buka Tab Read Only, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter, klik `⋯` pada baris `Doni Pratama {runId}-144` > Remove
55. Klik [Remove] pada dialog Remove Read Only
56. Tunggu aksi selesai (dialog tertutup)
57. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
58. Verifikasi Modal Changelog User: jumlah baris dengan Action `Remove` dan Field `Access Level` untuk `Doni Pratama {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
59. Verifikasi Modal Changelog User: baris teratas dengan Action `Remove`, User Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`
60. Tutup Modal Changelog User
61. Buka Global Settings > User > User List, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter, klik Name `Doni Pratama {runId}-144`, buka Tab Changelog
62. Verifikasi Tab Changelog `Doni Pratama {runId}-144`: jumlah baris dengan Action `Remove` dan Field `Access Level` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
63. Verifikasi Tab Changelog `Doni Pratama {runId}-144`: baris teratas dengan Action `Remove`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`
64. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
65. Verifikasi Tab System Log `Siti Nurhaliza`: jumlah baris dengan Action `Remove`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
66. Verifikasi Tab System Log `Siti Nurhaliza`: baris teratas dengan Action `Remove`, Object `Read Only`, Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`
67. Buka Global Settings > Activity Log, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
68. Verifikasi Activity Log: jumlah baris dengan Action `Remove`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
69. Verifikasi Activity Log: baris teratas dengan Action `Remove`, Object `Read Only`, Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`

### TC-GS-USER-903: Assign role Manage TAG dari Role & Permission mencatat Field Manage TAG di empat surface

70. Catat baseline `{n0}` pada keempat surface (lewat kemampuan baca BE): jumlah baris Action `Assign` dengan Field `Manage TAG` untuk `Ahmad Fauzi {runId}-144`
71. Buka Global Settings > Role & Permission, buka Tab System, klik Role Name `Manage TAG`, klik [+ Assign]
72. Isi Search Popup Table User Picker dengan `Ahmad Fauzi {runId}-144`, tekan Enter, centang barisnya, klik [Assign]
73. Tunggu aksi selesai (Popup tertutup)
74. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
75. Verifikasi Modal Changelog User: jumlah baris dengan Action `Assign` dan Field `Manage TAG` untuk `Ahmad Fauzi {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
76. Verifikasi Modal Changelog User: baris teratas dengan Action `Assign`, User Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG`, Old Value `—`, New Value `Assigned`, Modified By `Siti N`
77. Tutup Modal Changelog User
78. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik Name `Ahmad Fauzi {runId}-144`, buka Tab Changelog
79. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: jumlah baris dengan Action `Assign` dan Field `Manage TAG` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
80. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: baris teratas dengan Action `Assign`, Field `Manage TAG`, Old Value `—`, New Value `Assigned`, Modified By `Siti N`
81. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
82. Verifikasi Tab System Log `Siti Nurhaliza`: jumlah baris dengan Action `Assign`, Object `System Role`, dan Field `Manage TAG` untuk `Ahmad Fauzi {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
83. Verifikasi Tab System Log `Siti Nurhaliza`: baris teratas dengan Action `Assign`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG`, Old Value `—`, New Value `Assigned`
84. Buka Global Settings > Activity Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
85. Verifikasi Activity Log: jumlah baris dengan Action `Assign`, Object `System Role`, dan Field `Manage TAG` untuk `Ahmad Fauzi {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
86. Verifikasi Activity Log: baris teratas dengan Action `Assign`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG`, Old Value `—`, New Value `Assigned`, Modified By `Siti N`

### TC-GS-USER-902: Centang Update Manage TAG di Tab Role mencatat Field Manage TAG — Update di empat surface

87. Catat baseline `{n0}` pada keempat surface (lewat kemampuan baca BE): jumlah baris Action `Edit` dengan Field `Manage TAG — Update` untuk `Ahmad Fauzi {runId}-144`
88. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik Name `Ahmad Fauzi {runId}-144`, buka Tab Role
89. Centang Update pada baris `Manage TAG`
90. Tunggu aksi selesai (checkbox tersimpan)
91. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
92. Verifikasi Modal Changelog User: jumlah baris dengan Action `Edit` dan Field `Manage TAG — Update` untuk `Ahmad Fauzi {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
93. Verifikasi Modal Changelog User: baris teratas dengan Action `Edit`, User Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG — Update`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
94. Tutup Modal Changelog User
95. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik Name `Ahmad Fauzi {runId}-144`, buka Tab Changelog
96. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: jumlah baris dengan Action `Edit` dan Field `Manage TAG — Update` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
97. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: baris teratas dengan Action `Edit`, Field `Manage TAG — Update`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
98. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
99. Verifikasi Tab System Log `Siti Nurhaliza`: jumlah baris dengan Action `Edit`, Object `System Role`, dan Field `Manage TAG — Update` untuk `Ahmad Fauzi {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
100. Verifikasi Tab System Log `Siti Nurhaliza`: baris teratas dengan Action `Edit`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG — Update`, Old Value `Inactive`, New Value `Active`
101. Buka Global Settings > Activity Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
102. Verifikasi Activity Log: jumlah baris dengan Action `Edit`, Object `System Role`, dan Field `Manage TAG — Update` untuk `Ahmad Fauzi {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
103. Verifikasi Activity Log: baris teratas dengan Action `Edit`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG — Update`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`

### TC-GS-USER-1052: Centang Read pada role belum di-assign di Tab Role mencatat Assign

104. Catat baseline (lewat kemampuan baca BE): `{n0-role}` jumlah baris hasil Search `Manage hardware` di Modal Changelog User > Role `Ahmad Fauzi {runId}-144` dan `{n0-user}` jumlah baris Action `Assign` dengan Field `Manage hardware` untuk `Ahmad Fauzi {runId}-144` di Modal Changelog User
105. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik Name `Ahmad Fauzi {runId}-144`, buka Tab Role
106. Centang Read pada baris `Manage hardware` (belum di-assign)
107. Tunggu aksi selesai (checkbox tersimpan)
108. Klik icon Changelog di Tab Role (Modal Changelog: User > Role), klik icon Search, ketik `Manage hardware`, tekan Enter
109. Verifikasi Modal Changelog User > Role: jumlah baris hasil Search `Manage hardware` bertambah tepat 1 dari baseline `{n0-role}`, yaitu `Assign` (tidak ada baris `Edit`)
110. Verifikasi Modal Changelog User > Role `Ahmad Fauzi {runId}-144`: baris teratas dengan Action `Assign`, Role `Manage hardware`, Field `Access`, Old Value `—`, New Value `Assigned`, Modified By `Siti N`
111. Tutup Modal Changelog User > Role
112. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Manage hardware`, tekan Enter
113. Verifikasi Modal Changelog User: jumlah baris dengan Action `Assign` dan Field `Manage hardware` untuk `Ahmad Fauzi {runId}-144` bertambah tepat 1 dari baseline `{n0-user}`
114. Verifikasi Modal Changelog User: baris teratas dengan Action `Assign`, User Name `Ahmad Fauzi {runId}-144`, Field `Manage hardware`, Old Value `—`, New Value `Assigned`, Modified By `Siti N`
115. Tutup Modal Changelog User

### TC-GS-USER-904: Remove role Manage files mencatat Field Manage files di empat surface

116. Catat baseline `{n0}` pada keempat surface (lewat kemampuan baca BE): jumlah baris Action `Remove` dengan Field `Manage files` untuk `Ahmad Fauzi {runId}-144`
117. Buka Global Settings > Role & Permission, buka Tab System, klik Role Name `Manage files`
118. Klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik `⋯` pada baris `Ahmad Fauzi {runId}-144` > Remove
119. Klik [Remove] pada dialog Remove Access
120. Tunggu aksi selesai (dialog tertutup)
121. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
122. Verifikasi Modal Changelog User: jumlah baris dengan Action `Remove` dan Field `Manage files` untuk `Ahmad Fauzi {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
123. Verifikasi Modal Changelog User: baris teratas dengan Action `Remove`, User Name `Ahmad Fauzi {runId}-144`, Field `Manage files`, Old Value `Assigned`, New Value `—`, Modified By `Siti N`
124. Tutup Modal Changelog User
125. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik Name `Ahmad Fauzi {runId}-144`, buka Tab Changelog
126. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: jumlah baris dengan Action `Remove` dan Field `Manage files` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
127. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: baris teratas dengan Action `Remove`, Field `Manage files`, Old Value `Assigned`, New Value `—`, Modified By `Siti N`
128. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
129. Verifikasi Tab System Log `Siti Nurhaliza`: jumlah baris dengan Action `Remove`, Object `System Role`, dan Field `Manage files` untuk `Ahmad Fauzi {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
130. Verifikasi Tab System Log `Siti Nurhaliza`: baris teratas dengan Action `Remove`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage files`, Old Value `Assigned`, New Value `—`
131. Buka Global Settings > Activity Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
132. Verifikasi Activity Log: jumlah baris dengan Action `Remove`, Object `System Role`, dan Field `Manage files` untuk `Ahmad Fauzi {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
133. Verifikasi Activity Log: baris teratas dengan Action `Remove`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage files`, Old Value `Assigned`, New Value `—`, Modified By `Siti N`

### TC-GS-USER-905: Auto-Revert tier Total Control mencatat Field Access Level di empat surface

134. Catat baseline (lewat kemampuan baca BE): `{n0}` jumlah baris Action `Auto-Revert` dengan Field `Access Level` untuk `Andi Wijaya B {runId}-144` pada keempat surface, `{n0-edit}` jumlah baris Action `Edit` dengan Role `Manage TAG` dan Field `Update`, dan `{n0-ar}` jumlah baris Action `Auto-Revert`, keduanya di Modal Changelog User > Role `Andi Wijaya B {runId}-144`
135. Buka Global Settings > User > User List, klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter, klik Name `Andi Wijaya B {runId}-144`, buka Tab Role
136. Hapus centang Update pada baris `Manage TAG` sehingga CRUD menyimpang dari pattern Total Control
137. Klik [Remove] pada dialog Remove Access
138. Tunggu aksi selesai (dialog tertutup)
139. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter
140. Verifikasi Modal Changelog User: jumlah baris dengan Action `Auto-Revert` dan Field `Access Level` untuk `Andi Wijaya B {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
141. Verifikasi Modal Changelog User: baris teratas dengan Action `Auto-Revert`, User Name `Andi Wijaya B {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`
142. Verifikasi Modal Changelog User: Modified By baris `Auto-Revert` untuk `Andi Wijaya B {runId}-144` adalah `Siti N`, bukan `System`
143. Tutup Modal Changelog User
144. Buka Global Settings > User > User List, klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter, klik Name `Andi Wijaya B {runId}-144`, buka Tab Changelog
145. Verifikasi Tab Changelog `Andi Wijaya B {runId}-144`: jumlah baris dengan Action `Auto-Revert` dan Field `Access Level` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
146. Verifikasi Tab Changelog `Andi Wijaya B {runId}-144`: baris teratas dengan Action `Auto-Revert`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`
147. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter
148. Verifikasi Tab System Log `Siti Nurhaliza`: jumlah baris dengan Action `Auto-Revert`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya B {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
149. Verifikasi Tab System Log `Siti Nurhaliza`: baris teratas dengan Action `Auto-Revert`, Object `Total Control`, Name `Andi Wijaya B {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`
150. Buka Global Settings > Activity Log, klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter
151. Verifikasi Activity Log: jumlah baris dengan Action `Auto-Revert`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya B {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
152. Verifikasi Activity Log: baris teratas dengan Action `Auto-Revert`, Object `Total Control`, Name `Andi Wijaya B {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`
153. Buka Global Settings > User > User List, klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter, klik Name `Andi Wijaya B {runId}-144`, buka Tab Role, klik icon Changelog di Tab Role (Modal Changelog: User > Role)
154. Verifikasi Modal Changelog User > Role `Andi Wijaya B {runId}-144`: jumlah baris dengan Action `Edit`, Role `Manage TAG`, dan Field `Update` bertambah tepat 1 dari baseline `{n0-edit}`
155. Verifikasi Modal Changelog User > Role `Andi Wijaya B {runId}-144`: baris teratas dengan Action `Edit`, Role `Manage TAG`, Field `Update`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N` (entri Edit CRUD pemicu)
156. Verifikasi Modal Changelog User > Role `Andi Wijaya B {runId}-144`: jumlah baris dengan Action `Auto-Revert` tetap sama dengan baseline `{n0-ar}` (tidak bertambah)
157. Tutup Modal Changelog User > Role

### TC-GS-USER-906: Auto-Revert tier Read Only mencatat Field Access Level di empat surface

158. Catat baseline (lewat kemampuan baca BE): `{n0}` jumlah baris Action `Auto-Revert` dengan Field `Access Level` untuk `Doni Pratama B {runId}-144` pada keempat surface, `{n0-edit}` jumlah baris Action `Edit` dengan Role `Manage TAG` dan Field `Update`, dan `{n0-ar}` jumlah baris Action `Auto-Revert`, keduanya di Modal Changelog User > Role `Doni Pratama B {runId}-144`
159. Buka Global Settings > User > User List, klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter, klik Name `Doni Pratama B {runId}-144`, buka Tab Role
160. Hapus centang Update pada baris `Manage TAG` sehingga CRUD menyimpang dari pattern Read Only
161. Klik [Remove] pada dialog Remove Access
162. Tunggu aksi selesai (dialog tertutup)
163. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter
164. Verifikasi Modal Changelog User: jumlah baris dengan Action `Auto-Revert` dan Field `Access Level` untuk `Doni Pratama B {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
165. Verifikasi Modal Changelog User: baris teratas dengan Action `Auto-Revert`, User Name `Doni Pratama B {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`
166. Verifikasi Modal Changelog User: Modified By baris `Auto-Revert` untuk `Doni Pratama B {runId}-144` adalah `Siti N`, bukan `System`
167. Tutup Modal Changelog User
168. Buka Global Settings > User > User List, klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter, klik Name `Doni Pratama B {runId}-144`, buka Tab Changelog
169. Verifikasi Tab Changelog `Doni Pratama B {runId}-144`: jumlah baris dengan Action `Auto-Revert` dan Field `Access Level` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
170. Verifikasi Tab Changelog `Doni Pratama B {runId}-144`: baris teratas dengan Action `Auto-Revert`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`
171. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter
172. Verifikasi Tab System Log `Siti Nurhaliza`: jumlah baris dengan Action `Auto-Revert`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama B {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
173. Verifikasi Tab System Log `Siti Nurhaliza`: baris teratas dengan Action `Auto-Revert`, Object `Read Only`, Name `Doni Pratama B {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`
174. Buka Global Settings > Activity Log, klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter
175. Verifikasi Activity Log: jumlah baris dengan Action `Auto-Revert`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama B {runId}-144` bertambah tepat 1 dari baseline `{n0}` (tidak duplikat)
176. Verifikasi Activity Log: baris teratas dengan Action `Auto-Revert`, Object `Read Only`, Name `Doni Pratama B {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`
177. Buka Global Settings > User > User List, klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter, klik Name `Doni Pratama B {runId}-144`, buka Tab Role, klik icon Changelog di Tab Role (Modal Changelog: User > Role)
178. Verifikasi Modal Changelog User > Role `Doni Pratama B {runId}-144`: jumlah baris dengan Action `Edit`, Role `Manage TAG`, dan Field `Update` bertambah tepat 1 dari baseline `{n0-edit}`
179. Verifikasi Modal Changelog User > Role `Doni Pratama B {runId}-144`: baris teratas dengan Action `Edit`, Role `Manage TAG`, Field `Update`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N` (entri Edit CRUD pemicu)
180. Verifikasi Modal Changelog User > Role `Doni Pratama B {runId}-144`: jumlah baris dengan Action `Auto-Revert` tetap sama dengan baseline `{n0-ar}` (tidak bertambah)
181. Tutup Modal Changelog User > Role

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Urutan TC di spec: 898, 899, 900, 901, 903, 902, 1052, 904, 905, 906. 899 sesudah 898 dan 901 sesudah 900 mengikuti rantai Assign lalu Remove pada user yang sama. 903 sebelum 902 karena baris `Manage TAG` baru ada di Tab Role Ahmad setelah di-assign (902 mencentang Update pada baris itu). 1052 sebelum 904, dan Auto-Revert (905, 906) paling akhir karena Remove dan Auto-Revert menghilangkan akses pada user seed.
- P-1 (state berat) untuk TC-GS-USER-905 dan 906: klausa "tidak tampil di Modal Changelog User > Role" ditulis sebagai `Verifikasi` berbaseline di spec ini, bukan dipindah ke spec absence, karena kondisinya (user bertier yang CRUD-nya diedit menyimpang) dibangun oleh aksi pemicu TC yang sama; anchor positif pada surface yang sama adalah baris `Edit` pemicu di Modal Changelog User > Role.
- Pembagian TC lintas spec: TC-GS-USER-929 sampai 932 (Assign dan Remove Total Control dan Read Only tidak menulis entry per-role di Modal Changelog User > Role) diverifikasi di spec `TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role`. Modal Changelog User > Role untuk Edit, Assign, dan Remove role individual juga diverifikasi di spec `TC-GS-USER-E2E-145-pencatatan-modal-changelog-user-role-edit-assign-remove`.
- Expected Result f TC-GS-USER-898 ("Satu baris ringkasan, tanpa baris per role") ditulis sebagai asersi selisih: jumlah seluruh baris untuk user itu di Modal Changelog User bertambah tepat 1 dari baseline `{n0-semua}` (bukan absence kelas g).
- Asersi selisih "bertambah tepat 1" dibatasi pada Action dan Field karena Search nama user juga memuat baris dari TC lain milik user yang sama; baseline `{n0}` dihitung dengan kriteria yang sama. Isi entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih terbukti; entri baru dan entri seed dalam menit yang sama tidak diurutkan di antaranya, sehingga yang diasersi adalah himpunan baris teratas sebanyak selisih (1 baris) beserta nilai kolomnya (S-14).
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan baseline jumlah entri di awal tiap TC (S-12), pembukaan Role & Permission dan pemilihan user di Popup Table User Picker, "Tunggu aksi selesai" (8b butir 8), pembukaan tiap surface log beserta Search nama, dan penutupan Modal Changelog User. Search ditulis pada tiap pembukaan karena Modal Changelog User, tab, dan Activity Log dibuka segar. Tab System Log dibuka di Detail Siti Nurhaliza sesuai TC (aktor = pemilik System Log); Tab Changelog dibuka di Detail user target. Search pada Tab Changelog Detail tidak dipakai karena baris tab dikenali lewat Action dan Field.
- Baris Edit pemicu di Modal Changelog User > Role (anchor TC-GS-USER-905 dan 906) memakai Role `Manage TAG`, Field `Update`, Old Value `Active`, New Value `Inactive` sesuai PRD `user.md` §8.2a; nilai itu bukan Expected Result TC dan ditulis sebagai anchor positif (S-03).
- Spec melewati sekitar 35 langkah karena sepuluh TC berada dalam satu kelas (pencatatan log tier, role, dan permission), satu dataset user seed, dan tiap TC berdiri sendiri pada user dan baris log yang dikenali lewat nama bersuffix. Hampir seluruh langkah adalah blok baca-log berpola (buka surface, Search, `Verifikasi` kolom log) yang tidak dihitung ke batas ±35 langkah (bagian 3 konvensi, Smell). Kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-USER-898, 899, 900, 901: Pre-setup Andi Wijaya (No. 10) sudah tier Total Control dan Doni Pratama (No. 11) sudah Read Only, sehingga Assign tier pada user itu tidak mungkin; spec memakai user seed Basic milik spec untuk 898 sampai 901, dan user seed bertier untuk 905 dan 906.
  - TC-GS-USER-905 dan 906: Langkah 1 menulis "Edit CRUD Tab Role Andi Wijaya menyimpang pattern lalu `[Remove]`", sedangkan PRD `user.md` §4.8 menyatakan checkbox CRUD Tab Role Disabled untuk target Total Control/Read Only, dan Auto-Revert oleh edit CRUD dipicu dari Detail role di Role & Permission (`role/PRD/role.md` F-ROLE-06, dialog Remove Access). Spec mengikuti TC (edit di Tab Role Detail user, lalu `[Remove]` pada dialog Remove Access) dan butuh klarifikasi QA tentang lokasi pemicu dan pola CRUD yang menyimpang (spec memilih menghapus centang Update pada `Manage TAG`).
  - TC-GS-USER-902 dan 903: 902 mensyaratkan baris `Manage TAG` sudah ada di Tab Role Ahmad Fauzi (Update Inactive), sedangkan 903 men-assign role yang sama; TC tidak menyebut urutan atau precondition. Spec menjalankan 903 lebih dulu.
  - TC-GS-USER-905 dan 906 Expected Result f: "Modified By = admin pemicu, bukan System" diasersi tersendiri pada Modal Changelog User; surface lain memuat Modified By `Siti N` pada baris yang sama.
  - TC-GS-USER-1052 Langkah 3 ("Klik icon Changelog di Tab Role") dan Langkah 4 ("Buka Modal Changelog User") berurutan tanpa menyebut penutupan modal; spec menutup Modal Changelog User > Role sebelum membuka Modal Changelog User.
  - TC sumber slice ini tidak punya Post Condition.
