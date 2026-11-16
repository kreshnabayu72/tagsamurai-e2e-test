---
id: TC-FA-FATR-UI-071-overrides-tampilan
title: "Tabel Overrides: kolom, format sel, dan empty state"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#r6, §4.1#r41, §4.1#r49, §4.1#r239, §4.1#r241, §4.1#r242, §4.1#r244, §4.1#r240, §4.1#r243, §4.1#r245, §4.1#r247, §4.1#r249, §4.1#r250, §4.1#r251, §4.1#r252, §4.1#r254, §4.1#r255, §4.1#r256, §4.1#r260, §4.1#r261, §4.1#r264, §4.1#r265, §5#r1, §7#r14, S-08, §9.2#b125, §9.2#b152, §9.2#b157, §9.2#b159, §9.4.2#r67, §9.5#r27, §9.5#r28, §9.5#r29, §9.10.1#b5, §9.11#r2, EB-TBL-1@tabel-overrides, EB-TBL-4@created-by-tabel-overrides, EB-TBL-5@tombol-add-override, EB-TBL-5@delete-baris-override, EB-TBL-8@tabel-overrides, EB-TBL-12, EB-XM-1]
smoke: []
dependsOn: []
trace:
  §4.1#r6: [2, 3, 8, 14, 125]
  §4.1#r41: 41
  §4.1#r49: 42
  §4.1#r239: [15, 17, 30, 33, 37, 38, 39]
  §4.1#r241: [18, 20, 30, 33, 40]
  §4.1#r242: [21, 23, 30, 33, 54, 55, 56]
  §4.1#r244: [24, 26, 31, 34, 64, 65]
  §4.1#r240: [28, 30, 33, 45, 47]
  §4.1#r243: [27, 30, 33, 59, 60]
  §4.1#r245: 11
  §4.1#r247: [68, 70]
  §4.1#r249: [72, 75, 78, 120]
  §4.1#r250: 74
  §4.1#r251: [77, 80]
  §4.1#r252: 122
  §4.1#r254: [45, 47, 48, 50]
  §4.1#r255: 43
  §4.1#r256: 44
  §4.1#r260: 35
  §4.1#r261: 83
  §4.1#r264: 90
  §4.1#r265: [84, 85]
  §5#r1: [5, 7, 8, 125]
  §7#r14: [99, 100]
  S-08: [105, 106, 113, 114]
  §9.2#b125: [68, 70]
  §9.2#b152: [72, 74, 75, 78, 120]
  §9.2#b157: [92, 94]
  §9.2#b159: 88
  §9.4.2#r67: [96, 97]
  §9.5#r27: 52
  §9.5#r28: 66
  §9.5#r29: [99, 100]
  §9.10.1#b5: 74
  §9.11#r2: 88
  EB-TBL-1@tabel-overrides: [99, 101, 105, 107, 116, 117, 118]
  EB-TBL-4@created-by-tabel-overrides: [54, 55, 56, 58]
  EB-TBL-5@tombol-add-override: [92, 94]
  EB-TBL-5@delete-baris-override: [88, 90]
  EB-TBL-8@tabel-overrides: 51
  EB-TBL-12: [43, 127, 130, 131, 132, 133]
  EB-XM-1: [59, 60]
anchor: []
coverage:
  web: automated
---

# Tabel Overrides: kolom, format sel, dan empty state

## Prerequisites
- Aktor: Manage asset & TAG (Read + Update) pada Group `Proyek Karawang`. K5 memakai aktor ini. K6 memakai aktor Read Only. K1, K2, K3, K4, K7, K8, dan K9 memakai Total Control.
- Layar awal: Settings > Transaction Settings, bagian `Overrides` pada Category dan transaksi terpilih.
- Komponen: Tabel Overrides
- Data:
  - DU-071-1: override Scope `Group`, Target `Proyek Karawang` (hierarki `Region Jawa > Proyek Karawang`), Overridden `Max duration (30 days), Max extensions (1)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-15 14:05`. Yang diharapkan tampil: Created By `Budi S`, Created At dengan tanggal `15/06/26` dari 2026-06-15 dan jam `14:05` dari 14:05, dengan Date Format `dd/MM/yy` dan Time Format `24h`.
  - DU-071-2: override Scope `Asset Name`, Target `Excavator PC200`, Overridden `Max duration (10 days), Max extensions (No extension)`, Category `Machinery`, Created By `Siti Nurbaya`, Created At `2026-06-12 09:30`. Created By tampil `Siti N`, Created At tampil dengan tanggal `12/06/26` dari 2026-06-12 dan jam `09:30` dari 09:30, dengan Date Format `dd/MM/yy` dan Time Format `24h`.
  - DU-071-3: override Scope `Asset`, Target `EXC-0001 · Excavator PC200 - 1`, Overridden `Allow Borrow (Deny)`, Category `Machinery`, Created By `Alexander Graham Bell`, Created At `2026-06-10 16:45`. Created By tampil `Alexander G`.
  - DU-071-4: override Scope `Group`, Target `Workshop`, Overridden `Due date reminders (D-3; D-1; D-day)` (field Borrow bernilai berderet), Category `All categories`, Created By `Siti Nurbaya`, Created At `2026-06-08 08:15`.
  - DU-071-5: override Scope `Group`, Target `Jakarta Selatan Distribution Center` (hierarki `Region Jawa > Jakarta Selatan Distribution Center`), Overridden `Max duration (14 days)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-05 11:20`. Badge Target yang diharapkan `Jakarta Sela..ution Center`, dari nama Group 35 karakter.
  - DU-071-6: override Scope `Group`, Target `Proyek Bekasi` (di luar cakupan Group aktor), Overridden `Auto-approve (OFF)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-03 10:00`.
  - DU-071-7: override Scope `Group`, Target `Gudang Lama` (Group sudah dihapus), Overridden `Max duration (7 days)`, Category `Machinery`, Created By `Siti Nurbaya`, Created At `2026-06-02 13:10`.
  - DU-071-8: override Scope `Group`, Target `Proyek Surabaya`, Overridden `Require approval (OFF)` (Approval Workflow tidak tersedia di plan), Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-01 15:50`.
  - DU-071-9: override Scope `Group`, Target `Proyek Medan`, Overridden `Self service (ON)` (Borrowing bukan versi penuh di plan), Category `Vehicle > Pool car`, Created By `Siti Nurbaya`, Created At `2026-05-30 09:05`.
  - DU-071-10: override Scope `Group`, Target `Proyek Makassar`, Overridden `Direct handover between holders (Deny)` (Assignment bukan versi penuh di plan), Category `Machinery`, Created By `Alexander Graham Bell`, Created At `2026-05-29 17:25`.
  - DU-071-11: override Scope `Group`, Target `Proyek Palembang`, Overridden `Allow Assign (Allow)` di bawah Category ber-Deny, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-05-28 12:40`.
  - DU-071-12: kata kunci Search `Zebra Tidak Ada`, tidak cocok dengan baris mana pun.
  - DU-071-13: override Scope `Asset Name`, Target `<b>Excavator</b> PC200`, Overridden `Max duration (5 days)`, Category `Machinery`, Created By `Siti Nurbaya`, Created At `2026-05-27 10:10`.
  - DU-071-14: override Scope `Group`, Target `Proyek Bandung`, Overridden `Duration unit (Hours)` (Borrowing bukan versi penuh di plan), Category `Vehicle > Pool car`, Created By `Siti Nurbaya`, Created At `2026-05-26 08:55`.
- Kondisi:
  - K1: tab transaksi Borrow aktif; tabel berisi DU-071-1 sampai DU-071-5 dan DU-071-13; Date Format bernilai `dd/MM/yy`; Time Format bernilai `24h`; waktu pada respons sudah dalam Time Zone entitas; aktor berhak atas semua baris.
  - K2: tabel tanpa override untuk Category dan transaksi terpilih.
  - K3: tabel berisi DU-071-1; respons atas Search DU-071-12 dan atas Filter Scope `Asset` tidak memuat baris.
  - K4: memuat tabel gagal karena error server.
  - K5: tabel berisi DU-071-1 dan DU-071-6; DU-071-1 berada di dalam cakupan Group aktor dan DU-071-6 di luar cakupannya.
  - K6: tabel berisi DU-071-1; aktor tidak berhak membuat override.
  - K7: tabel berisi DU-071-7.
  - K8: tab transaksi Borrow aktif; tabel berisi DU-071-8, DU-071-9, dan DU-071-14; plan entitas tidak memuat Approval Workflow dan Borrowing penuh.
  - K10: bahasa aktif aplikasi `Bahasa Indonesia`, dan nama field, satuan, serta label `All categories` pada baris DU-071-2 dan DU-071-4 sudah punya terjemahan pada bahasa itu; tab transaksi Borrow aktif; tabel berisi DU-071-2, DU-071-3, dan DU-071-4.
  - K11: tab transaksi Assign aktif; tabel berisi DU-071-10; plan entitas tidak memuat Assignment penuh.
  - K9: tabel berisi DU-071-1 dan DU-071-11; Save ditolak karena kombinasi efektif Allowed assignee OFF/OFF pada aset yang dibuka DU-071-11.

## Test Steps

### Judul, toolbar, dan tooltip ikon toolbar
1. Tampilkan Tabel Overrides dengan kondisi K1
2. Verifikasi judul bagian `Overrides` tampil
3. Verifikasi tombol `[+ Override]` tampil dan aktif
4. Arahkan kursor ke ikon Search di toolbar
5. Verifikasi ikon Search menyampaikan nama fungsinya `Search`
6. Arahkan kursor ke ikon Filter di toolbar
7. Verifikasi ikon Filter menyampaikan nama fungsinya `Filter`
8. Verifikasi toolbar memuat ikon Search, ikon Filter, lalu tombol `[+ Override]` berurutan dari kiri ke kanan

### Placeholder kotak Search
9. Tampilkan Tabel Overrides dengan kondisi K1
10. Klik ikon Search di toolbar
11. Verifikasi kotak Search memuat placeholder `Search by target or overridden...`

### Field Filter Panel tiap kolom
12. Tampilkan Tabel Overrides dengan kondisi K1
13. Klik ikon Filter di toolbar
14. Verifikasi Filter Panel tampil bersama tabel Overrides
15. Verifikasi field filter `Scope` berupa multi-select dengan placeholder `All scopes`
16. Klik field filter `Scope`
17. Verifikasi daftar opsi field `Scope` menyediakan kotak pencarian opsi
18. Verifikasi field filter `Overridden` berupa multi-select dengan placeholder `All fields`
19. Klik field filter `Overridden`
20. Verifikasi daftar opsi field `Overridden` menyediakan kotak pencarian opsi
21. Verifikasi field filter `Created By` berupa multi-select dengan placeholder `All users`
22. Klik field filter `Created By`
23. Verifikasi daftar opsi field `Created By` menyediakan kotak pencarian opsi
24. Verifikasi field filter `Category` berupa multi-select dengan placeholder `All categories`
25. Klik field filter `Category`
26. Verifikasi daftar opsi field `Category` menyediakan kotak pencarian opsi
27. Verifikasi field filter `Created At` berupa pemilih rentang tanggal dengan placeholder `Select date`
28. Verifikasi Filter Panel tidak memuat field filter `Target`

### Visibilitas awal kolom dan daftar Column Visibility
29. Tampilkan Tabel Overrides dengan kondisi K1
30. Verifikasi tabel menampilkan header kolom `Scope`, `Target`, `Overridden`, `Created By`, dan `Created At`
31. Verifikasi tabel tidak menampilkan header kolom `Category`
32. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
33. Verifikasi kolom `Scope`, `Target`, `Overridden`, `Created By`, dan `Created At` tercentang dan tidak disabled di daftar Column Visibility
34. Verifikasi kolom `Category` tidak tercentang namun tidak disabled di daftar Column Visibility
35. Verifikasi daftar Column Visibility tidak memuat baris untuk checkbox seleksi baris maupun kolom Actions

### Format sel kolom Scope, Overridden, dan Target
36. Tampilkan Tabel Overrides dengan kondisi K1
37. Verifikasi sel Scope pada baris Target `Proyek Karawang` berisi `Group`
38. Verifikasi sel Scope pada baris Target `Excavator PC200` berisi `Asset Name`
39. Verifikasi sel Scope pada baris Target `EXC-0001 · Excavator PC200 - 1` berisi `Asset`
40. Verifikasi sel Overridden pada baris Target `Proyek Karawang` berisi `Max duration (30 days), Max extensions (1)`
41. Verifikasi sel Overridden pada baris Target `Excavator PC200` berisi `Max duration (10 days), Max extensions (No extension)`, nilai 0 tampil sebagai teks maknanya
42. Verifikasi sel Overridden pada baris Target `Workshop` berisi `Due date reminders (D-3; D-1; D-day)`, nilai berderet dipisah `; `
43. Verifikasi sel Target pada baris Scope `Asset Name` tampil verbatim `Excavator PC200`
44. Verifikasi sel Target pada baris Scope `Asset` tampil `EXC-0001 · Excavator PC200 - 1`
45. Verifikasi sel Target pada baris Scope `Group` dengan Overridden `Max duration (30 days), Max extensions (1)` berupa badge bernama `Proyek Karawang`
46. Arahkan kursor ke badge Target `Proyek Karawang`
47. Verifikasi hierarki lengkap `Region Jawa > Proyek Karawang` tersampaikan pada badge Target
48. Verifikasi badge Target pada baris Overridden `Max duration (14 days)` berisi `Jakarta Sela..ution Center`
49. Arahkan kursor ke badge Target `Jakarta Sela..ution Center`
50. Verifikasi hierarki lengkap `Region Jawa > Jakarta Selatan Distribution Center` tersampaikan pada badge Target
51. Verifikasi sel Target pada baris Scope `Asset Name` dengan Overridden `Max duration (5 days)` menampilkan `<b>Excavator</b> PC200` apa adanya sebagai teks
52. Verifikasi sel pada kolom Scope, Target, Overridden, Created By, dan Created At di setiap baris berisi nilai dan tidak menampilkan `—`

### Format sel kolom Created By dan Created At
53. Tampilkan Tabel Overrides dengan kondisi K1
54. Verifikasi sel Created By pada baris Target `Proyek Karawang` berisi `Budi S`
55. Verifikasi sel Created By pada baris Target `Excavator PC200` berisi `Siti N`
56. Verifikasi sel Created By pada baris Target `EXC-0001 · Excavator PC200 - 1` berisi `Alexander G`
57. Arahkan kursor ke sel Created By pada baris Target `Proyek Karawang`
58. Verifikasi nama lengkap `Budi Santoso` tersampaikan pada sel Created By
59. Verifikasi sel Created At pada baris Target `Proyek Karawang` memuat tanggal `15/06/26` dan jam `14:05`
60. Verifikasi sel Created At pada baris Target `Excavator PC200` memuat tanggal `12/06/26` dan jam `09:30`

### Format sel kolom Category yang ditampilkan lewat Column Visibility
61. Tampilkan Tabel Overrides dengan kondisi K1
62. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
63. Centang kolom `Category` di daftar Column Visibility
64. Verifikasi sel Category pada baris Target `Proyek Karawang` berisi `Vehicle > Pool car`
65. Verifikasi sel Category pada baris Target `Workshop` berisi `All categories`
66. Verifikasi sel Category di setiap baris berisi nilai dan tidak menampilkan `—`

### Badge Not applied pada Target yang dihapus
67. Tampilkan Tabel Overrides dengan kondisi K7
68. Verifikasi badge `Not applied` tampil pada sel Target baris `Gudang Lama`
69. Arahkan kursor ke badge `Not applied` pada baris Target `Gudang Lama`
70. Verifikasi alasan `This override doesn't apply because its target or category was deleted or deactivated.` tersampaikan pada badge

### Badge Not applied pada field bergerbang plan
71. Tampilkan Tabel Overrides dengan kondisi K8
72. Verifikasi badge `Not applied` tampil pada sel Target baris `Proyek Surabaya`
73. Arahkan kursor ke badge `Not applied` pada baris Target `Proyek Surabaya`
74. Verifikasi alasan `Requires Approval Workflow on your plan` tersampaikan pada badge
75. Verifikasi badge `Not applied` tampil pada sel Target baris `Proyek Medan`
76. Arahkan kursor ke badge `Not applied` pada baris Target `Proyek Medan`
77. Verifikasi alasan `Available on plans with full Borrowing` tersampaikan pada badge
78. Verifikasi badge `Not applied` tampil pada sel Target baris `Proyek Bandung`
79. Arahkan kursor ke badge `Not applied` pada baris Target `Proyek Bandung`
80. Verifikasi alasan `Available on plans with full Borrowing` tersampaikan pada badge

### Menu baris Actions pada baris dalam dan luar cakupan
81. Tampilkan Tabel Overrides dengan kondisi K5
82. Klik `⋯` pada baris Target `Proyek Karawang`
83. Verifikasi menu baris memuat tepat satu item, `Delete`, dan item itu aktif
84. Verifikasi menu baris tidak memuat `Edit`
85. Verifikasi menu baris tidak memuat `End now`
86. Klik `⋯` pada baris Target `Proyek Karawang` sekali lagi untuk menutup menu
87. Klik `⋯` pada baris Target `Proyek Bekasi`
88. Verifikasi `Delete` pada menu baris `Proyek Bekasi` disabled
89. Arahkan kursor ke `Delete` pada menu baris `Proyek Bekasi`
90. Verifikasi alasan `This override is outside your scope.` tersampaikan pada `Delete`

### Tombol + Override untuk aktor tanpa hak membuat override
91. Tampilkan Tabel Overrides dengan kondisi K6
92. Verifikasi tombol `[+ Override]` disabled
93. Arahkan kursor ke tombol `[+ Override]`
94. Verifikasi alasan `You don't have permission to add overrides.` tersampaikan pada tombol `[+ Override]`

### Pesan guard Allowed assignee pada baris override Allow
95. Tampilkan Tabel Overrides dengan kondisi K9
96. Verifikasi pesan `At least one assignee type must be enabled` tampil pada baris Target `Proyek Palembang`
97. Verifikasi baris Target `Proyek Karawang` tidak menampilkan pesan `At least one assignee type must be enabled`

### Empty state belum ada override
98. Tampilkan Tabel Overrides dengan kondisi K2
99. Verifikasi judul empty state `No overrides yet` tampil
100. Verifikasi deskripsi `Get started by creating your first override.` tampil
101. Verifikasi empty state tidak menyediakan tombol aksi

### Empty state hasil Search tanpa hasil
102. Tampilkan Tabel Overrides dengan kondisi K3
103. Klik ikon Search di toolbar
104. Ketik Search `Zebra Tidak Ada`, tekan Enter
105. Verifikasi judul `No results found` tampil
106. Verifikasi deskripsi `Try adjusting your search or filter.` tampil
107. Verifikasi `No overrides yet` tidak tampil

### Empty state hasil Filter tanpa hasil
108. Tampilkan Tabel Overrides dengan kondisi K3
109. Klik ikon Filter di toolbar
110. Klik field filter `Scope`
111. Pilih opsi `Asset` pada field filter `Scope`
112. Klik `[Apply]`
113. Verifikasi judul `No results found` tampil
114. Verifikasi deskripsi `Try adjusting your search or filter.` tampil

### Gagal memuat tabel
115. Tampilkan Tabel Overrides dengan kondisi K4
116. Verifikasi pesan `Unable to load this data.` tampil
117. Verifikasi tombol `[Try Again]` tampil
118. Verifikasi `No overrides yet` tidak tampil

### Badge Not applied pada field Assignment yang tidak tersedia di plan
119. Tampilkan Tabel Overrides dengan kondisi K11
120. Verifikasi badge `Not applied` tampil pada sel Target baris `Proyek Makassar`
121. Arahkan kursor ke badge `Not applied` pada baris Target `Proyek Makassar`
122. Verifikasi alasan `Available on plans with full Assignment` tersampaikan pada badge

### Urutan bar bulk pada toolbar saat ada baris terpilih
123. Tampilkan Tabel Overrides dengan kondisi K1
124. Centang baris Target `Proyek Karawang`
125. Verifikasi bar bulk berada di kiri ikon Search di toolbar

### Nilai verbatim dan label translatable pada bahasa aktif selain Inggris
126. Tampilkan Tabel Overrides dengan kondisi K10
127. Verifikasi sel Target pada baris Scope `Asset Name` tampil verbatim `Excavator PC200`
128. Klik header kolom Actions (`⋯`) untuk membuka Column Visibility
129. Centang kolom `Category` di daftar Column Visibility
130. Verifikasi sel Category pada baris Target `Excavator PC200` berisi `Machinery` persis sama
131. Verifikasi sel Target pada baris Scope `Asset` tampil `EXC-0001 · Excavator PC200 - 1` persis sama
132. Verifikasi sel Overridden pada baris Target `Excavator PC200` menampilkan nama field dan satuan dalam bahasa aktif, berbeda dari `Max duration (10 days), Max extensions (No extension)`
133. Verifikasi sel Category pada baris Target `Workshop` menampilkan label dalam bahasa aktif, berbeda dari `All categories`
