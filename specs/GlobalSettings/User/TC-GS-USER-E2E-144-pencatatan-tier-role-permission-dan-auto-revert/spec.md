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
- Kemampuan teknis, disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut endpoint): seeding user dengan tier Total Control atau Read Only dan penugasan role individual (`Manage files`) lewat API; seeding memakai endpoint aplikasi sehingga entri log seed ditulis sebelum penanda baseline.
- State global: tidak ada. Tier dan penugasan role hanya pada user seed milik spec. Suite berjalan serial (`suite.md`).
- Baseline log: penanda waktu dicatat pada langkah 2, sesudah hook `before` selesai dan sebelum aksi pemicu pertama (TC-GS-USER-898). Baris log dikenali lewat nama bersuffix `-144` dan Action; baris yang diasersi adalah baris di atas penanda.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API kelima user seed bersuffix `{runId}-144` (penugasan role dan tier ikut hilang). Hook `before` menghapus sisa user bersuffix `-144` dari run lama. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar dan baseline

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Catat penanda waktu baseline (waktu saat ini) untuk Modal Changelog User, Tab Changelog, Tab System Log, dan Activity Log; baris yang diasersi adalah baris di atas penanda ini

### TC-GS-USER-898: Assign Total Control mencatat Field Access Level di empat surface

3. Buka Global Settings > Role & Permission, buka Tab Total Control, klik [+ Assign]
4. Isi Search Popup Table User Picker dengan `Andi Wijaya {runId}-144`, tekan Enter, centang barisnya, klik [Assign]
5. Tunggu aksi selesai (Popup tertutup)
6. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
7. Verifikasi Modal Changelog User: baris di atas penanda baseline dengan Action `Assign`, User Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Siti N`
8. Verifikasi Modal Changelog User: tepat 1 baris di atas penanda baseline dengan Action `Assign` dan Field `Access Level` untuk `Andi Wijaya {runId}-144` (tidak duplikat)
9. Verifikasi Modal Changelog User: seluruh baris di atas penanda baseline untuk `Andi Wijaya {runId}-144` hanya 1 baris ringkasan `Access Level` tersebut, tanpa baris per role
10. Tutup Modal Changelog User
11. Buka Global Settings > User > User List, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter, klik Name `Andi Wijaya {runId}-144`, buka Tab Changelog
12. Verifikasi Tab Changelog `Andi Wijaya {runId}-144`: baris di atas penanda baseline dengan Action `Assign`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Siti N`
13. Verifikasi Tab Changelog `Andi Wijaya {runId}-144`: tepat 1 baris di atas penanda baseline dengan Action `Assign` dan Field `Access Level` (tidak duplikat)
14. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
15. Verifikasi Tab System Log `Siti Nurhaliza`: baris di atas penanda baseline dengan Action `Assign`, Object `Total Control`, Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Total Control`
16. Verifikasi Tab System Log `Siti Nurhaliza`: tepat 1 baris di atas penanda baseline dengan Action `Assign`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya {runId}-144` (tidak duplikat)
17. Buka Global Settings > Activity Log, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
18. Verifikasi Activity Log: baris di atas penanda baseline dengan Action `Assign`, Object `Total Control`, Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Siti N`
19. Verifikasi Activity Log: tepat 1 baris di atas penanda baseline dengan Action `Assign`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya {runId}-144` (tidak duplikat)

### TC-GS-USER-899: Remove Total Control mencatat Field Access Level di empat surface

20. Buka Global Settings > Role & Permission, buka Tab Total Control, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter, klik `⋯` pada baris `Andi Wijaya {runId}-144` > Remove
21. Klik [Remove] pada dialog Remove Total Control
22. Tunggu aksi selesai (dialog tertutup)
23. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
24. Verifikasi Modal Changelog User: baris di atas penanda baseline dengan Action `Remove`, User Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`
25. Verifikasi Modal Changelog User: tepat 1 baris di atas penanda baseline dengan Action `Remove` dan Field `Access Level` untuk `Andi Wijaya {runId}-144` (tidak duplikat)
26. Tutup Modal Changelog User
27. Buka Global Settings > User > User List, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter, klik Name `Andi Wijaya {runId}-144`, buka Tab Changelog
28. Verifikasi Tab Changelog `Andi Wijaya {runId}-144`: baris di atas penanda baseline dengan Action `Remove`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`
29. Verifikasi Tab Changelog `Andi Wijaya {runId}-144`: tepat 1 baris di atas penanda baseline dengan Action `Remove` dan Field `Access Level` (tidak duplikat)
30. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
31. Verifikasi Tab System Log `Siti Nurhaliza`: baris di atas penanda baseline dengan Action `Remove`, Object `Total Control`, Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`
32. Verifikasi Tab System Log `Siti Nurhaliza`: tepat 1 baris di atas penanda baseline dengan Action `Remove`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya {runId}-144` (tidak duplikat)
33. Buka Global Settings > Activity Log, klik icon Search, ketik `Andi Wijaya {runId}-144`, tekan Enter
34. Verifikasi Activity Log: baris di atas penanda baseline dengan Action `Remove`, Object `Total Control`, Name `Andi Wijaya {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`
35. Verifikasi Activity Log: tepat 1 baris di atas penanda baseline dengan Action `Remove`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya {runId}-144` (tidak duplikat)

### TC-GS-USER-900: Assign Read Only mencatat Field Access Level di empat surface

36. Buka Global Settings > Role & Permission, buka Tab Read Only, klik [+ Assign]
37. Isi Search Popup Table User Picker dengan `Doni Pratama {runId}-144`, tekan Enter, centang barisnya, klik [Assign]
38. Tunggu aksi selesai (Popup tertutup)
39. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
40. Verifikasi Modal Changelog User: baris di atas penanda baseline dengan Action `Assign`, User Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Read Only`, Modified By `Siti N`
41. Verifikasi Modal Changelog User: tepat 1 baris di atas penanda baseline dengan Action `Assign` dan Field `Access Level` untuk `Doni Pratama {runId}-144` (tidak duplikat)
42. Tutup Modal Changelog User
43. Buka Global Settings > User > User List, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter, klik Name `Doni Pratama {runId}-144`, buka Tab Changelog
44. Verifikasi Tab Changelog `Doni Pratama {runId}-144`: baris di atas penanda baseline dengan Action `Assign`, Field `Access Level`, Old Value `—`, New Value `Read Only`, Modified By `Siti N`
45. Verifikasi Tab Changelog `Doni Pratama {runId}-144`: tepat 1 baris di atas penanda baseline dengan Action `Assign` dan Field `Access Level` (tidak duplikat)
46. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
47. Verifikasi Tab System Log `Siti Nurhaliza`: baris di atas penanda baseline dengan Action `Assign`, Object `Read Only`, Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Read Only`
48. Verifikasi Tab System Log `Siti Nurhaliza`: tepat 1 baris di atas penanda baseline dengan Action `Assign`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama {runId}-144` (tidak duplikat)
49. Buka Global Settings > Activity Log, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
50. Verifikasi Activity Log: baris di atas penanda baseline dengan Action `Assign`, Object `Read Only`, Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `—`, New Value `Read Only`, Modified By `Siti N`
51. Verifikasi Activity Log: tepat 1 baris di atas penanda baseline dengan Action `Assign`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama {runId}-144` (tidak duplikat)

### TC-GS-USER-901: Remove Read Only mencatat Field Access Level di empat surface

52. Buka Global Settings > Role & Permission, buka Tab Read Only, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter, klik `⋯` pada baris `Doni Pratama {runId}-144` > Remove
53. Klik [Remove] pada dialog Remove Read Only
54. Tunggu aksi selesai (dialog tertutup)
55. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
56. Verifikasi Modal Changelog User: baris di atas penanda baseline dengan Action `Remove`, User Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`
57. Verifikasi Modal Changelog User: tepat 1 baris di atas penanda baseline dengan Action `Remove` dan Field `Access Level` untuk `Doni Pratama {runId}-144` (tidak duplikat)
58. Tutup Modal Changelog User
59. Buka Global Settings > User > User List, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter, klik Name `Doni Pratama {runId}-144`, buka Tab Changelog
60. Verifikasi Tab Changelog `Doni Pratama {runId}-144`: baris di atas penanda baseline dengan Action `Remove`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`
61. Verifikasi Tab Changelog `Doni Pratama {runId}-144`: tepat 1 baris di atas penanda baseline dengan Action `Remove` dan Field `Access Level` (tidak duplikat)
62. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
63. Verifikasi Tab System Log `Siti Nurhaliza`: baris di atas penanda baseline dengan Action `Remove`, Object `Read Only`, Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`
64. Verifikasi Tab System Log `Siti Nurhaliza`: tepat 1 baris di atas penanda baseline dengan Action `Remove`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama {runId}-144` (tidak duplikat)
65. Buka Global Settings > Activity Log, klik icon Search, ketik `Doni Pratama {runId}-144`, tekan Enter
66. Verifikasi Activity Log: baris di atas penanda baseline dengan Action `Remove`, Object `Read Only`, Name `Doni Pratama {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`
67. Verifikasi Activity Log: tepat 1 baris di atas penanda baseline dengan Action `Remove`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama {runId}-144` (tidak duplikat)

### TC-GS-USER-903: Assign role Manage TAG dari Role & Permission mencatat Field Manage TAG di empat surface

68. Buka Global Settings > Role & Permission, buka Tab System, klik Role Name `Manage TAG`, klik [+ Assign]
69. Isi Search Popup Table User Picker dengan `Ahmad Fauzi {runId}-144`, tekan Enter, centang barisnya, klik [Assign]
70. Tunggu aksi selesai (Popup tertutup)
71. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
72. Verifikasi Modal Changelog User: baris di atas penanda baseline dengan Action `Assign`, User Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG`, Old Value `—`, New Value `Assigned`, Modified By `Siti N`
73. Verifikasi Modal Changelog User: tepat 1 baris di atas penanda baseline dengan Action `Assign` dan Field `Manage TAG` untuk `Ahmad Fauzi {runId}-144` (tidak duplikat)
74. Tutup Modal Changelog User
75. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik Name `Ahmad Fauzi {runId}-144`, buka Tab Changelog
76. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: baris di atas penanda baseline dengan Action `Assign`, Field `Manage TAG`, Old Value `—`, New Value `Assigned`, Modified By `Siti N`
77. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: tepat 1 baris di atas penanda baseline dengan Action `Assign` dan Field `Manage TAG` (tidak duplikat)
78. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
79. Verifikasi Tab System Log `Siti Nurhaliza`: baris di atas penanda baseline dengan Action `Assign`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG`, Old Value `—`, New Value `Assigned`
80. Verifikasi Tab System Log `Siti Nurhaliza`: tepat 1 baris di atas penanda baseline dengan Action `Assign`, Object `System Role`, dan Field `Manage TAG` untuk `Ahmad Fauzi {runId}-144` (tidak duplikat)
81. Buka Global Settings > Activity Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
82. Verifikasi Activity Log: baris di atas penanda baseline dengan Action `Assign`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG`, Old Value `—`, New Value `Assigned`, Modified By `Siti N`
83. Verifikasi Activity Log: tepat 1 baris di atas penanda baseline dengan Action `Assign`, Object `System Role`, dan Field `Manage TAG` untuk `Ahmad Fauzi {runId}-144` (tidak duplikat)

### TC-GS-USER-902: Centang Update Manage TAG di Tab Role mencatat Field Manage TAG — Update di empat surface

84. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik Name `Ahmad Fauzi {runId}-144`, buka Tab Role
85. Centang Update pada baris `Manage TAG`
86. Tunggu aksi selesai (checkbox tersimpan)
87. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
88. Verifikasi Modal Changelog User: baris di atas penanda baseline dengan Action `Edit`, User Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG — Update`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
89. Verifikasi Modal Changelog User: tepat 1 baris di atas penanda baseline dengan Action `Edit` dan Field `Manage TAG — Update` untuk `Ahmad Fauzi {runId}-144` (tidak duplikat)
90. Tutup Modal Changelog User
91. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik Name `Ahmad Fauzi {runId}-144`, buka Tab Changelog
92. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: baris di atas penanda baseline dengan Action `Edit`, Field `Manage TAG — Update`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
93. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: tepat 1 baris di atas penanda baseline dengan Action `Edit` dan Field `Manage TAG — Update` (tidak duplikat)
94. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
95. Verifikasi Tab System Log `Siti Nurhaliza`: baris di atas penanda baseline dengan Action `Edit`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG — Update`, Old Value `Inactive`, New Value `Active`
96. Verifikasi Tab System Log `Siti Nurhaliza`: tepat 1 baris di atas penanda baseline dengan Action `Edit`, Object `System Role`, dan Field `Manage TAG — Update` untuk `Ahmad Fauzi {runId}-144` (tidak duplikat)
97. Buka Global Settings > Activity Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
98. Verifikasi Activity Log: baris di atas penanda baseline dengan Action `Edit`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage TAG — Update`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
99. Verifikasi Activity Log: tepat 1 baris di atas penanda baseline dengan Action `Edit`, Object `System Role`, dan Field `Manage TAG — Update` untuk `Ahmad Fauzi {runId}-144` (tidak duplikat)

### TC-GS-USER-1052: Centang Read pada role belum di-assign di Tab Role mencatat Assign

100. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik Name `Ahmad Fauzi {runId}-144`, buka Tab Role
101. Centang Read pada baris `Manage hardware` (belum di-assign)
102. Tunggu aksi selesai (checkbox tersimpan)
103. Klik icon Changelog di Tab Role (Modal Changelog: User > Role), klik icon Search, ketik `Manage hardware`, tekan Enter
104. Verifikasi Modal Changelog User > Role `Ahmad Fauzi {runId}-144`: baris di atas penanda baseline dengan Action `Assign`, Role `Manage hardware`, Field `Access`, Old Value `—`, New Value `Assigned`, Modified By `Siti N`
105. Verifikasi Modal Changelog User > Role: hasil Search `Manage hardware` hanya memuat 1 baris di atas penanda baseline, yaitu `Assign` (tidak ada baris `Edit`)
106. Tutup Modal Changelog User > Role
107. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Manage hardware`, tekan Enter
108. Verifikasi Modal Changelog User: baris di atas penanda baseline dengan Action `Assign`, User Name `Ahmad Fauzi {runId}-144`, Field `Manage hardware`, Old Value `—`, New Value `Assigned`, Modified By `Siti N`
109. Tutup Modal Changelog User

### TC-GS-USER-904: Remove role Manage files mencatat Field Manage files di empat surface

110. Buka Global Settings > Role & Permission, buka Tab System, klik Role Name `Manage files`
111. Klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik `⋯` pada baris `Ahmad Fauzi {runId}-144` > Remove
112. Klik [Remove] pada dialog Remove Access
113. Tunggu aksi selesai (dialog tertutup)
114. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
115. Verifikasi Modal Changelog User: baris di atas penanda baseline dengan Action `Remove`, User Name `Ahmad Fauzi {runId}-144`, Field `Manage files`, Old Value `Assigned`, New Value `—`, Modified By `Siti N`
116. Verifikasi Modal Changelog User: tepat 1 baris di atas penanda baseline dengan Action `Remove` dan Field `Manage files` untuk `Ahmad Fauzi {runId}-144` (tidak duplikat)
117. Tutup Modal Changelog User
118. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter, klik Name `Ahmad Fauzi {runId}-144`, buka Tab Changelog
119. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: baris di atas penanda baseline dengan Action `Remove`, Field `Manage files`, Old Value `Assigned`, New Value `—`, Modified By `Siti N`
120. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-144`: tepat 1 baris di atas penanda baseline dengan Action `Remove` dan Field `Manage files` (tidak duplikat)
121. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
122. Verifikasi Tab System Log `Siti Nurhaliza`: baris di atas penanda baseline dengan Action `Remove`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage files`, Old Value `Assigned`, New Value `—`
123. Verifikasi Tab System Log `Siti Nurhaliza`: tepat 1 baris di atas penanda baseline dengan Action `Remove`, Object `System Role`, dan Field `Manage files` untuk `Ahmad Fauzi {runId}-144` (tidak duplikat)
124. Buka Global Settings > Activity Log, klik icon Search, ketik `Ahmad Fauzi {runId}-144`, tekan Enter
125. Verifikasi Activity Log: baris di atas penanda baseline dengan Action `Remove`, Object `System Role`, Name `Ahmad Fauzi {runId}-144`, Field `Manage files`, Old Value `Assigned`, New Value `—`, Modified By `Siti N`
126. Verifikasi Activity Log: tepat 1 baris di atas penanda baseline dengan Action `Remove`, Object `System Role`, dan Field `Manage files` untuk `Ahmad Fauzi {runId}-144` (tidak duplikat)

### TC-GS-USER-905: Auto-Revert tier Total Control mencatat Field Access Level di empat surface

127. Buka Global Settings > User > User List, klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter, klik Name `Andi Wijaya B {runId}-144`, buka Tab Role
128. Hapus centang Update pada baris `Manage TAG` sehingga CRUD menyimpang dari pattern Total Control
129. Klik [Remove] pada dialog Remove Access
130. Tunggu aksi selesai (dialog tertutup)
131. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter
132. Verifikasi Modal Changelog User: baris di atas penanda baseline dengan Action `Auto-Revert`, User Name `Andi Wijaya B {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`
133. Verifikasi Modal Changelog User: tepat 1 baris di atas penanda baseline dengan Action `Auto-Revert` dan Field `Access Level` untuk `Andi Wijaya B {runId}-144` (tidak duplikat)
134. Verifikasi Modal Changelog User: Modified By baris `Auto-Revert` untuk `Andi Wijaya B {runId}-144` adalah `Siti N`, bukan `System`
135. Tutup Modal Changelog User
136. Buka Global Settings > User > User List, klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter, klik Name `Andi Wijaya B {runId}-144`, buka Tab Changelog
137. Verifikasi Tab Changelog `Andi Wijaya B {runId}-144`: baris di atas penanda baseline dengan Action `Auto-Revert`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`
138. Verifikasi Tab Changelog `Andi Wijaya B {runId}-144`: tepat 1 baris di atas penanda baseline dengan Action `Auto-Revert` dan Field `Access Level` (tidak duplikat)
139. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter
140. Verifikasi Tab System Log `Siti Nurhaliza`: baris di atas penanda baseline dengan Action `Auto-Revert`, Object `Total Control`, Name `Andi Wijaya B {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`
141. Verifikasi Tab System Log `Siti Nurhaliza`: tepat 1 baris di atas penanda baseline dengan Action `Auto-Revert`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya B {runId}-144` (tidak duplikat)
142. Buka Global Settings > Activity Log, klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter
143. Verifikasi Activity Log: baris di atas penanda baseline dengan Action `Auto-Revert`, Object `Total Control`, Name `Andi Wijaya B {runId}-144`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Siti N`
144. Verifikasi Activity Log: tepat 1 baris di atas penanda baseline dengan Action `Auto-Revert`, Object `Total Control`, dan Field `Access Level` untuk `Andi Wijaya B {runId}-144` (tidak duplikat)
145. Buka Global Settings > User > User List, klik icon Search, ketik `Andi Wijaya B {runId}-144`, tekan Enter, klik Name `Andi Wijaya B {runId}-144`, buka Tab Role, klik icon Changelog di Tab Role (Modal Changelog: User > Role)
146. Verifikasi Modal Changelog User > Role `Andi Wijaya B {runId}-144`: baris di atas penanda baseline dengan Action `Edit`, Role `Manage TAG`, Field `Update`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N` (entri Edit CRUD pemicu)
147. Verifikasi Modal Changelog User > Role `Andi Wijaya B {runId}-144` tidak memuat baris dengan Action `Auto-Revert` di atas penanda baseline
148. Tutup Modal Changelog User > Role

### TC-GS-USER-906: Auto-Revert tier Read Only mencatat Field Access Level di empat surface

149. Buka Global Settings > User > User List, klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter, klik Name `Doni Pratama B {runId}-144`, buka Tab Role
150. Hapus centang Update pada baris `Manage TAG` sehingga CRUD menyimpang dari pattern Read Only
151. Klik [Remove] pada dialog Remove Access
152. Tunggu aksi selesai (dialog tertutup)
153. Buka Global Settings > User > User List, klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter
154. Verifikasi Modal Changelog User: baris di atas penanda baseline dengan Action `Auto-Revert`, User Name `Doni Pratama B {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`
155. Verifikasi Modal Changelog User: tepat 1 baris di atas penanda baseline dengan Action `Auto-Revert` dan Field `Access Level` untuk `Doni Pratama B {runId}-144` (tidak duplikat)
156. Verifikasi Modal Changelog User: Modified By baris `Auto-Revert` untuk `Doni Pratama B {runId}-144` adalah `Siti N`, bukan `System`
157. Tutup Modal Changelog User
158. Buka Global Settings > User > User List, klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter, klik Name `Doni Pratama B {runId}-144`, buka Tab Changelog
159. Verifikasi Tab Changelog `Doni Pratama B {runId}-144`: baris di atas penanda baseline dengan Action `Auto-Revert`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`
160. Verifikasi Tab Changelog `Doni Pratama B {runId}-144`: tepat 1 baris di atas penanda baseline dengan Action `Auto-Revert` dan Field `Access Level` (tidak duplikat)
161. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter
162. Verifikasi Tab System Log `Siti Nurhaliza`: baris di atas penanda baseline dengan Action `Auto-Revert`, Object `Read Only`, Name `Doni Pratama B {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`
163. Verifikasi Tab System Log `Siti Nurhaliza`: tepat 1 baris di atas penanda baseline dengan Action `Auto-Revert`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama B {runId}-144` (tidak duplikat)
164. Buka Global Settings > Activity Log, klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter
165. Verifikasi Activity Log: baris di atas penanda baseline dengan Action `Auto-Revert`, Object `Read Only`, Name `Doni Pratama B {runId}-144`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Siti N`
166. Verifikasi Activity Log: tepat 1 baris di atas penanda baseline dengan Action `Auto-Revert`, Object `Read Only`, dan Field `Access Level` untuk `Doni Pratama B {runId}-144` (tidak duplikat)
167. Buka Global Settings > User > User List, klik icon Search, ketik `Doni Pratama B {runId}-144`, tekan Enter, klik Name `Doni Pratama B {runId}-144`, buka Tab Role, klik icon Changelog di Tab Role (Modal Changelog: User > Role)
168. Verifikasi Modal Changelog User > Role `Doni Pratama B {runId}-144`: baris di atas penanda baseline dengan Action `Edit`, Role `Manage TAG`, Field `Update`, Old Value `Active`, New Value `Inactive`, Modified By `Siti N` (entri Edit CRUD pemicu)
169. Verifikasi Modal Changelog User > Role `Doni Pratama B {runId}-144` tidak memuat baris dengan Action `Auto-Revert` di atas penanda baseline
170. Tutup Modal Changelog User > Role

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Urutan TC di spec: 898, 899, 900, 901, 903, 902, 1052, 904, 905, 906. 899 sesudah 898 dan 901 sesudah 900 mengikuti rantai Assign lalu Remove pada user yang sama. 903 sebelum 902 karena baris `Manage TAG` baru ada di Tab Role Ahmad setelah di-assign (902 mencentang Update pada baris itu). 1052 sebelum 904, dan Auto-Revert (905, 906) paling akhir karena Remove dan Auto-Revert menghilangkan akses pada user seed.
- P-1 (state berat) untuk TC-GS-USER-905 dan 906: klausa "tidak tampil di Modal Changelog User > Role" ditulis sebagai `Verifikasi` berbaseline di spec ini, bukan dipindah ke spec absence, karena kondisinya (user bertier yang CRUD-nya diedit menyimpang) dibangun oleh aksi pemicu TC yang sama; anchor positif pada surface yang sama adalah baris `Edit` pemicu di Modal Changelog User > Role.
- Pembagian TC lintas spec: TC-GS-USER-929 sampai 932 (Assign dan Remove Total Control dan Read Only tidak menulis entry per-role di Modal Changelog User > Role) diverifikasi di spec `TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role`. Modal Changelog User > Role untuk Edit, Assign, dan Remove role individual juga diverifikasi di spec `TC-GS-USER-E2E-145-pencatatan-modal-changelog-user-role-edit-assign-remove`.
- Expected Result f TC-GS-USER-898 ("Satu baris ringkasan, tanpa baris per role") ditulis sebagai asersi jumlah: seluruh baris baru untuk user itu di Modal Changelog User hanya 1 baris (bukan absence kelas g).
- Asersi "tepat 1 baris" dibatasi pada Action dan Field karena Search nama user juga memuat baris dari TC lain milik user yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan penanda baseline (langkah 2), pembukaan Role & Permission dan pemilihan user di Popup Table User Picker, "Tunggu aksi selesai" (8b butir 8), pembukaan tiap surface log beserta Search nama, dan penutupan Modal Changelog User. Search ditulis pada tiap pembukaan karena Modal Changelog User, tab, dan Activity Log dibuka segar. Tab System Log dibuka di Detail Siti Nurhaliza sesuai TC (aktor = pemilik System Log); Tab Changelog dibuka di Detail user target. Search pada Tab Changelog Detail tidak dipakai karena baris tab dikenali lewat Action dan Field.
- Baris Edit pemicu di Modal Changelog User > Role (anchor TC-GS-USER-905 dan 906) memakai Role `Manage TAG`, Field `Update`, Old Value `Active`, New Value `Inactive` sesuai PRD `user.md` §8.2a; nilai itu bukan Expected Result TC dan ditulis sebagai anchor positif (S-03).
- Spec melewati sekitar 35 langkah karena sepuluh TC berada dalam satu kelas (pencatatan log tier, role, dan permission), satu dataset user seed, dan tiap TC berdiri sendiri pada user dan baris log yang dikenali lewat nama bersuffix. Hampir seluruh langkah adalah blok baca-log berpola (buka surface, Search, `Verifikasi` kolom log) yang tidak dihitung ke batas ±35 langkah (bagian 3 konvensi, Smell). Kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-USER-898, 899, 900, 901: Pre-setup Andi Wijaya (No. 10) sudah tier Total Control dan Doni Pratama (No. 11) sudah Read Only, sehingga Assign tier pada user itu tidak mungkin; spec memakai user seed Basic milik spec untuk 898 sampai 901, dan user seed bertier untuk 905 dan 906.
  - TC-GS-USER-905 dan 906: Langkah 1 menulis "Edit CRUD Tab Role Andi Wijaya menyimpang pattern lalu `[Remove]`", sedangkan PRD `user.md` §4.8 menyatakan checkbox CRUD Tab Role Disabled untuk target Total Control/Read Only, dan Auto-Revert oleh edit CRUD dipicu dari Detail role di Role & Permission (`role/PRD/role.md` F-ROLE-06, dialog Remove Access). Spec mengikuti TC (edit di Tab Role Detail user, lalu `[Remove]` pada dialog Remove Access) dan butuh klarifikasi QA tentang lokasi pemicu dan pola CRUD yang menyimpang (spec memilih menghapus centang Update pada `Manage TAG`).
  - TC-GS-USER-902 dan 903: 902 mensyaratkan baris `Manage TAG` sudah ada di Tab Role Ahmad Fauzi (Update Inactive), sedangkan 903 men-assign role yang sama; TC tidak menyebut urutan atau precondition. Spec menjalankan 903 lebih dulu.
  - TC-GS-USER-905 dan 906 Expected Result f: "Modified By = admin pemicu, bukan System" diasersi tersendiri pada Modal Changelog User; surface lain memuat Modified By `Siti N` pada baris yang sama.
  - TC-GS-USER-1052 Langkah 3 ("Klik icon Changelog di Tab Role") dan Langkah 4 ("Buka Modal Changelog User") berurutan tanpa menyebut penutupan modal; spec menutup Modal Changelog User > Role sebelum membuka Modal Changelog User.
  - TC sumber slice ini tidak punya Post Condition.
