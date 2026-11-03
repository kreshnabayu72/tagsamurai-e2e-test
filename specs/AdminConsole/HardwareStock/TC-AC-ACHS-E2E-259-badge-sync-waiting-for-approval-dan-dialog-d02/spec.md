---
id: TC-AC-ACHS-E2E-259-badge-sync-waiting-for-approval-dan-dialog-d02
title: "Badge Sync Waiting for Approval dan Dialog D-02"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-132
  - TC-AC-ACHS-133
  - TC-AC-ACHS-134
  - TC-AC-ACHS-135
  - TC-AC-ACHS-136
  - TC-AC-ACHS-137
  - TC-AC-ACHS-138
  - TC-AC-ACHS-139
  - TC-AC-ACHS-147
  - TC-AC-ACHS-148
  - TC-AC-ACHS-592
coverage:
  web: automated
---

# Badge Sync Waiting for Approval dan Dialog D-02

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List dan Approvals untuk akun aktor suite, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20, #24, dan #27. Suite serial (`parallel: false`). Flag Guided Tooltip akun selain Total Control disetel true di hook `before` spec ini dan dipulihkan di `after`.
- Login di hook `before` spec ini: Total Control (baris pertama tabel); halaman Hardware > Stock dibuka hook `beforeEach` suite. Akun lain login lewat Step ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Kelas harness: d (simulator reader USB, Pre-setup #25).
- Role yang diuji:

| Role | Akun (Pre-setup) | Env password | Blok langkah |
|---|---|---|---|
| Total Control | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (#1) | `Spectra.env.AC_TC_PASSWORD` | 1 sampai 84 (TC-132, 133, 134, 592, 138, 139, 135), 141 sampai 153 (pengamat dan Reject TC-147, 148) |
| Create-Only | `createOnlyPrincipal_automated_qaTeam1@qwertysystem.net` (#4) | `Spectra.env.AC_CREATE_ONLY_PASSWORD` | 85 sampai 122 (TC-137, 136) |
| Additional Approver Create | `additionalApproverCreatePrincipal_automated_qaTeam1@qwertysystem.net` (#6) | `Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD` | 123 sampai 140 (TC-147, 148), 154 sampai 164 (TC-148) |

- Nama env password selain `AC_TC_PASSWORD` mengikuti pola `AC_<ROLE>_PASSWORD` dan ditetapkan tim FE; nama pastinya tidak tertulis di TC (lihat Temuan untuk QA).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuLong}` | #16 Tabel A baris 4; #17; #18 | kode SKU Handheld Reader Long Range, Total Registered 25 (18 Available, 7 In Use) dan 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `{skuBulk}` | #16 Tabel A baris 8; #24 | kode SKU Smart Fixed Reader dengan 120 Available | `Fixture.hardwareStock.p16.a[8].sku` |
| `{snInUse1}` | #18 Tabel F baris N = 1 | Serial Number unit In Use berstatus Damaged | `Fixture.hardwareStock.p18.f[1].serialNumber` |
| `{snCakraFx}` | #27 | Serial Number unit Available pertama SKU Smart Fixed Reader milik Distributor Pre-setup #10 | `Fixture.hardwareStock.p27.fx[1].serialNumber` |
| `{snCakraFxLower}` | #27 (turunan) | `{snCakraFx}` dalam huruf kecil | `Fixture.hardwareStock.derived.cakraFxSerialLower` |
| `{snFxRej}` | #27 | Serial Number unit Rejected SKU Smart Fixed Reader | `Fixture.hardwareStock.p27.fxRejectedSerial` |
| `{snMulti}` | #27b | Serial Number terdaftar Rejected di SKU pertama, Available di SKU kedua, In Use di SKU ketiga | `Fixture.hardwareStock.p27.multiSerial` |
| `{snBulk02}` | #24 | Serial Number unit Available urutan ke-02 pada SKU Smart Fixed Reader 120 unit | `Fixture.hardwareStock.p24.bulk[2].serialNumber` |
| `{snBulk03}` | #24 | Serial Number unit Available urutan ke-03 pada SKU Smart Fixed Reader 120 unit | `Fixture.hardwareStock.p24.bulk[3].serialNumber` |
| `{snBulk04}` | #24 | Serial Number unit Available urutan ke-04 pada SKU Smart Fixed Reader 120 unit | `Fixture.hardwareStock.p24.bulk[4].serialNumber` |
| `{snBulk05}` | #24 | Serial Number unit Available urutan ke-05 pada SKU Smart Fixed Reader 120 unit | `Fixture.hardwareStock.p24.bulk[5].serialNumber` |
| `{snBulk06}` | #24 | Serial Number unit Available urutan ke-06 pada SKU Smart Fixed Reader 120 unit | `Fixture.hardwareStock.p24.bulk[6].serialNumber` |
| `{snBulk12}` | #24 | Serial Number unit Available urutan ke-12 pada SKU Smart Fixed Reader 120 unit | `Fixture.hardwareStock.p24.bulk[12].serialNumber` |
| `{emailTc}` | #1 | email akun Total Control Principal | `Fixture.hardwareStock.account.p01.totalControl.email` |
| `{emailCr}` | #4 | email akun Create-Only | `Fixture.hardwareStock.account.p04.createOnly.email` |
| `{emailAa}` | #6 | email akun Additional Approver dengan capability Create | `Fixture.hardwareStock.account.p06.additionalApproverCreate.email` |

- Data Pre-setup (hanya dibaca): SKU `{skuLong}` (Pre-setup #16); unit Available `{snCakraFx}`, unit Rejected `{snFxRej}` (Pre-setup #27), unit In Use `{snInUse1}` (Pre-setup #18), dan unit Available `{snBulk02}` sampai `{snBulk06}` dan `{snBulk12}` pada SKU `{skuBulk}` (Pre-setup #24) sebagai unit yang dicocokkan; `{snMulti}` terdaftar Rejected di SKU A, Available di SKU B, In Use di SKU C (Pre-setup #27b); service driver mock (Pre-setup #25).
- Data Dinamis (suffix `{runId}-259`): perangkat simulasi OK `SN-ZEBRA-RFD40-100041-a-{runId}-259`, `-b-`, `-c-` (TC-132, 133, 134; tidak disimpan), `SN-ZEBRA-RFD40-100071-{runId}-259` (TC-138), `SN-ZEBRA-RFD40-100081-{runId}-259` (TC-139), `SN-ZEBRA-RFD40-100051-{runId}-259` dan `SN-ZEBRA-RFD40-100052-{runId}-259` (TC-135, disimpan; Current Power `25 dBm` dan `26 dBm`, Min `-20 dBm`, Max `30 dBm`), `SN-ZEBRA-RFD40-100061-{runId}-259` dan `SN-ZEBRA-RFD40-100062-{runId}-259` (TC-136, disimpan), `SN-ZEBRA-RFD40-100091-{runId}-259` (TC-148, disimpan). Tiap TC memakai Serial Number OK terpisah supaya baris tidak bentrok dengan V-09.
- Kemampuan teknis (disediakan tim FE/BE): simulator USB Pre-setup #25 dengan Serial Number dan Min/Max/Current Power yang dapat diatur; fixture BE yang membersihkan unit Available hasil Add Stock, unit Waiting for Approval, dan Subject Register Duplicate pending untuk `{snCakraFx}`, `{snBulk02}`, `{snBulk12}` (Rejected), dan `{snMulti}` di hook `after` (mekanisme tidak didefinisikan di TC, PRD, atau LLD, lihat Temuan untuk QA).
- Efek pada Pre-setup: antrean Approvals Tab Active/History, hitungan baris SKU {skuLong}, dan Last Updated berubah selama spec berjalan; dipulihkan hook `after`. Spec ini dijalankan sesudah spec baca baseline (suite.md).

## Test Steps

### Persiapan baseline

1. Ketik Search `{skuLong}`, tekan Enter
2. Catat Total Registered dan Available baris SKU `{skuLong}` sebagai baseline

### TC-AC-ACHS-132: Cocok dengan unit Available pada SKU lain

3. Klik `(⋯)` pada baris SKU `{skuLong}`
4. Klik opsi `Add Stock`
5. Atur simulator: perangkat `{snCakraFx}`
6. Klik `[Sync]`
7. Verifikasi baris `{snCakraFx}` tetap masuk dengan Status `Waiting for Approval` (badge warning)
8. Atur simulator: perangkat `SN-ZEBRA-RFD40-100041-a-{runId}-259`
9. Klik `[Sync]`
10. Verifikasi baris `SN-ZEBRA-RFD40-100041-a-{runId}-259` Status `OK` (badge success) sehingga unit lain tidak terhalang
11. Verifikasi `[Submit]` enabled

### TC-AC-ACHS-133: Cocok dengan unit In Use pada SKU yang sama

12. Atur simulator: perangkat `{snInUse1}`
13. Klik `[Sync]`
14. Verifikasi baris `{snInUse1}` tetap masuk dengan Status `Waiting for Approval` (badge warning)
15. Atur simulator: perangkat `SN-ZEBRA-RFD40-100041-b-{runId}-259`
16. Klik `[Sync]`
17. Verifikasi baris `SN-ZEBRA-RFD40-100041-b-{runId}-259` Status `OK` (badge success) sehingga unit lain tidak terhalang
18. Verifikasi `[Submit]` enabled

### TC-AC-ACHS-134: Cocok dengan unit Rejected

19. Atur simulator: perangkat `{snFxRej}`
20. Klik `[Sync]`
21. Verifikasi baris `{snFxRej}` tetap masuk dengan Status `Waiting for Approval` (badge warning)
22. Atur simulator: perangkat `SN-ZEBRA-RFD40-100041-c-{runId}-259`
23. Klik `[Sync]`
24. Verifikasi baris `SN-ZEBRA-RFD40-100041-c-{runId}-259` Status `OK` (badge success) sehingga unit lain tidak terhalang
25. Verifikasi `[Submit]` enabled
26. Klik `[Cancel]`
27. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
28. Klik `[Leave]`

### TC-AC-ACHS-592: Normalisasi huruf kecil dan spasi tepi

29. Atur simulator: perangkat dengan Serial Number `  {snCakraFxLower}  `
30. Klik `[Add Stock]` pada toolbar Tab Available SKU `{skuLong}` (form baru)
31. Klik `[Sync]`
32. Verifikasi baris masuk dengan Serial Number `{snCakraFxLower}` (spasi di awal dan akhir dibuang, huruf asli dipertahankan)
33. Verifikasi Status baris `Waiting for Approval` (badge warning) karena cocok dengan `{snCakraFx}` tanpa membedakan huruf besar-kecil
34. Verifikasi `[Submit]` enabled
35. Klik `[Cancel]`
36. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
37. Klik `[Leave]`

### TC-AC-ACHS-138: Dialog D-02 bentuk jamak

38. Klik `[Add Stock]` pada toolbar Tab Available (form baru)
39. Atur simulator: perangkat `{snBulk03}`
40. Klik `[Sync]`
41. Atur simulator: perangkat `{snBulk04}`
42. Klik `[Sync]`
43. Atur simulator: perangkat `{snBulk05}`
44. Klik `[Sync]`
45. Atur simulator: perangkat `SN-ZEBRA-RFD40-100071-{runId}-259`
46. Klik `[Sync]`
47. Klik `[Submit]`
48. Verifikasi dialog berjudul `Partial Register` dengan "3 units matched existing records and were sent for approval:" dan tiga bullet `• {snBulk03}`, `• {snBulk04}`, `• {snBulk05}`
49. Verifikasi "1 unit(s) will be registered:" dengan bullet `• SN-ZEBRA-RFD40-100071-{runId}-259`
50. Verifikasi penutup dialog "Are you sure you want to continue?"
51. Klik `[Cancel]` pada dialog D-02
52. Verifikasi dialog tertutup dan tetap di form Synced Units
53. Klik `[Cancel]`
54. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
55. Klik `[Leave]`

### TC-AC-ACHS-139: Cancel pada dialog D-02 membatalkan total

56. Klik `[Add Stock]` pada toolbar Tab Available (form baru)
57. Atur simulator: perangkat `SN-ZEBRA-RFD40-100081-{runId}-259`
58. Klik `[Sync]`
59. Atur simulator: perangkat `{snBulk06}`
60. Klik `[Sync]`
61. Klik `[Submit]`
62. Klik `[Cancel]` pada dialog D-02
63. Verifikasi dialog tertutup dan form Synced Units tetap berisi dua baris
64. Klik `[Cancel]`
65. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
66. Klik `[Leave]`
67. Verifikasi Summary bar Total Registered dan Available sama dengan baseline langkah 2 (tidak ada unit baru tersimpan termasuk `SN-ZEBRA-RFD40-100081-{runId}-259`)
68. Buka Approvals > Hardware Stock Tab Active
69. Verifikasi Tab Active menampilkan sedikitnya satu baris
70. Ketik Search `{snBulk06}`, tekan Enter
71. Verifikasi tidak ada Subject Register Duplicate baru: hasil Search menampilkan empty state `No results found`

### TC-AC-ACHS-135: Submit tanpa kecocokan

72. Buka Hardware > Stock lewat sidebar
73. Ketik Search `{skuLong}`, tekan Enter
74. Klik `(⋯)` pada baris SKU `{skuLong}`
75. Klik opsi `Add Stock`
76. Atur simulator: perangkat `SN-ZEBRA-RFD40-100051-{runId}-259` (Min -20 dBm, Max 30 dBm, Current 25 dBm)
77. Klik `[Sync]`
78. Atur simulator: perangkat `SN-ZEBRA-RFD40-100052-{runId}-259` (Min -20 dBm, Max 30 dBm, Current 26 dBm)
79. Klik `[Sync]`
80. Klik `[Submit]`
81. Verifikasi toast sukses "Success, unit has been added to stock."
82. Verifikasi dialog konfirmasi D-02 tidak tampil
83. Verifikasi halaman berpindah ke Stock Detail > Tab Available
84. Verifikasi kedua unit `SN-ZEBRA-RFD40-100051-{runId}-259` dan `SN-ZEBRA-RFD40-100052-{runId}-259` berstatus `Available` dengan Min Power `-20 dBm`, Max Power `30 dBm`, Current Power `25 dBm` dan `26 dBm`

### TC-AC-ACHS-137: Semua baris Waiting for Approval (Create-Only)

85. Logout, lalu login sebagai Create-Only `{emailCr}` (`Spectra.env.AC_CREATE_ONLY_PASSWORD`)
86. Buka Hardware > Stock lewat sidebar
87. Ketik Search `{skuLong}`, tekan Enter
88. Klik row action `Detail` pada baris SKU `{skuLong}`
89. Catat jumlah unit pada banner "waiting for approval" dan Total Registered pada Summary bar sebagai baseline akun Create-Only
90. Klik segmen `Stock` pada breadcrumb
91. Ketik Search `{skuLong}`, tekan Enter
92. Klik `(⋯)` pada baris SKU `{skuLong}`
93. Klik opsi `Add Stock`
94. Atur simulator: perangkat `{snBulk02}`
95. Klik `[Sync]`
96. Klik `[Submit]`
97. Verifikasi dialog berjudul `Send for Approval` hanya berisi kelompok pertama "1 unit matched existing records and was sent for approval:" dengan bullet `• {snBulk02}`
98. Verifikasi penutup dialog "Are you sure you want to send them for approval?"
99. Verifikasi tombol dialog `[Cancel]` dan `[Send]`
100. Klik `[Send]`
101. Verifikasi toast sukses "Success, unit has been sent for approval."
102. Verifikasi unit `{snBulk02}` tampil sebagai `Waiting for Approval`
103. Catat jumlah unit pada banner "waiting for approval" dan Total Registered pada Summary bar sebagai baseline setelah TC-137

### TC-AC-ACHS-136: Campuran (Create-Only)

104. Klik `[Add Stock]` pada toolbar Tab Available (form baru)
105. Atur simulator: perangkat `SN-ZEBRA-RFD40-100061-{runId}-259`
106. Klik `[Sync]`
107. Atur simulator: perangkat `SN-ZEBRA-RFD40-100062-{runId}-259`
108. Klik `[Sync]`
109. Atur simulator: perangkat `{snCakraFx}`
110. Klik `[Sync]`
111. Klik `[Submit]`
112. Verifikasi dialog berjudul `Partial Register` dengan "1 unit matched existing records and was sent for approval:" dan bullet `• {snCakraFx}`
113. Verifikasi "2 unit(s) will be registered:" dengan bullet `• SN-ZEBRA-RFD40-100061-{runId}-259` dan `• SN-ZEBRA-RFD40-100062-{runId}-259`
114. Verifikasi penutup dialog "Are you sure you want to continue?"
115. Verifikasi tombol dialog `[Cancel]` dan `[Continue]`
116. Klik `[Continue]`
117. Verifikasi toast sukses "Success, unit has been sent for approval."
118. Verifikasi halaman berpindah ke Stock Detail > Tab Available
119. Verifikasi kedua unit `SN-ZEBRA-RFD40-100061-{runId}-259` dan `SN-ZEBRA-RFD40-100062-{runId}-259` berstatus `Available`
120. Verifikasi unit `{snCakraFx}` tampil sebagai baris `Waiting for Approval` pada SKU {skuLong}
121. Verifikasi banner jumlah unit menunggu persetujuan bertambah 1 dari baseline setelah TC-137
122. Verifikasi Total Registered hanya bertambah 2 dari baseline setelah TC-137

### TC-AC-ACHS-147 dan TC-AC-ACHS-148: Additional Approver

123. Logout, lalu login sebagai Additional Approver `{emailAa}` (`Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD`)
124. Buka Hardware > Stock lewat sidebar
125. Ketik Search `{skuLong}`, tekan Enter
126. Klik `(⋯)` pada baris SKU `{skuLong}`
127. Klik opsi `Add Stock`
128. Atur simulator: perangkat `{snMulti}` (terdaftar Rejected di SKU A, Available di SKU B, In Use di SKU C; Pre-setup #27b)
129. Klik `[Sync]`
130. Klik `[Submit]`
131. Klik `[Send]`
132. Tunggu aksi selesai (redirect ke Stock Detail > Tab Available)
133. Catat nomor tertinggi Device Name pada Tab Available sebagai N0
134. Klik `[Add Stock]` pada toolbar Tab Available (form baru)
135. Atur simulator: perangkat `{snBulk12}`
136. Klik `[Sync]`
137. Klik `[Submit]`
138. Klik `[Send]`
139. Verifikasi unit `{snBulk12}` berstatus `Waiting for Approval` dengan nomor Device Name N berikutnya setelah N0
140. Tunggu aksi selesai
141. Logout, lalu login sebagai Total Control `{emailTc}` (`Spectra.env.AC_TC_PASSWORD`)
142. Buka Approvals > Hardware Stock Tab Active
143. Ketik Search `{snMulti}`, tekan Enter
144. Klik row action `Review` pada Subject Matched Identifier `{snMulti}`
145. Verifikasi blok Existing Record menampilkan unit rujukan berstatus `In Use` (prioritas tertinggi), bukan Available atau Rejected
146. Klik `[Cancel]` pada dialog Detail Approval
147. Ketik Search `{snBulk12}`, tekan Enter
148. Klik row action `Review` pada Subject Matched Identifier `{snBulk12}`
149. Pilih radio `Reject`
150. Isi Approval Note `Rejected for numbering test`
151. Klik `[Submit]`
152. Verifikasi toast sukses "Success, duplicate has been rejected."
153. Tunggu aksi selesai
154. Logout, lalu login sebagai Additional Approver `{emailAa}` (`Spectra.env.AC_ADDITIONAL_APPROVER_CREATE_PASSWORD`)
155. Buka Hardware > Stock lewat sidebar
156. Ketik Search `{skuLong}`, tekan Enter
157. Klik `(⋯)` pada baris SKU `{skuLong}`
158. Klik opsi `Add Stock`
159. Atur simulator: perangkat `SN-ZEBRA-RFD40-100091-{runId}-259`
160. Klik `[Sync]`
161. Klik `[Submit]`
162. Verifikasi toast sukses "Success, unit has been added to stock."
163. Verifikasi nomor N unit `{snBulk12}` tidak muncul pada Tab Available setelah Reject
164. Verifikasi unit `SN-ZEBRA-RFD40-100091-{runId}-259` menerima nomor setelah N (nomor N tidak dipakai ulang)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-132, 133, 134, 135, 136, 137, 138, 139, 147, 148, 592). Tidak ada TC hanya-BE di spec ini.
- Spec ini melewati sekitar 35 langkah (164 langkah). Alasan: seluruh blok satu kelas harness (d, simulator USB) dan satu topik (badge Sync dan dialog D-02); ganti akun memakai Step eksplisit (langkah 85, 123, 141, 154) dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras (bagian 3, pemisah beda akun kasus b); tiap blok membuka form baru dan berdiri sendiri.
- Urutan TC di spec berbeda dari nomor TC: dikelompokkan menurut akun dan, dalam akun Total Control, blok tanpa Submit (TC-132, 133, 134, 592, 138, 139) lebih dulu lalu TC-135 yang menyimpan unit; dilanjutkan Create-Only (TC-137 lalu TC-136) dan (TC-147, 148). Tiap blok membuka form baru untuk setiap kejadian menutup form (`[Leave]` pada form dirty atau Submit).
- Langkah 141 sampai 153 (Total Control membuka Detail Approval dan Reject) dan langkah 154 sampai 164 ( menambah Stock OK sesudah Reject) mengikuti Expected TC-147 butir a dan TC-148 butir a sampai c. Label Reject mengikuti TC-182 (row action `Review`, radio `Reject`, Approval Note, `[Submit]`, toast "Success, duplicate has been rejected.").
- Langkah penghubung (aksi tanpa `Verifikasi`): baseline (langkah 2, 89, 103, 133), Search untuk menemukan baris target, pengaturan simulator, `[Add Stock]` toolbar sebagai pembuka form baru sesudah mendarat di Tab Available, `[Cancel]` dan `[Leave]` yang menutup form dirty (dialog Unsaved Changes diverifikasi, S-08), dan `Tunggu aksi selesai` sebelum ganti akun.
- Unit pencocokan Pre-setup (`{snBulk02}` dan seterusnya, `{snMulti}`, `{snCakraFx}`) dibaca saja; yang berubah adalah Subject pending dan unit Waiting for Approval baru pada SKU {skuLong} yang dibersihkan hook `after`.
- Temuan untuk QA:
  - TC-135 Post Condition (Total Registered, Event Log, Hardware Log `Source: Sync`), TC-136 Post Condition (Subject di Approvals, notifikasi, kuota), dan TC-137 Post Condition tidak punya langkah observasi dan tidak diasersi; Hardware Log ditutup di spec 278.
  - TC-147 butir b ("bila dua unit berstatus sama, yang Registered At terbaru ditampilkan") bersyarat dan Pre-setup #27b tidak memuat dua unit berstatus sama; tidak diasersi.
  - TC-148 tidak menyebut akun untuk langkah 7 (Add Stock unit OK); spec memakai akun yang sama dengan langkah 3. TC-148 juga menyebut dependensi TC-182 (Reject) yang dijalankan di spec ini sebagai langkah.
  - TC-132 dan TC-133 memakai Serial Number OK yang sama (nilai literal TC) pada tabel terpisah per TC di TC sumber; spec memakai huruf pembeda `a`, `b`, `c` karena ketiganya berada di satu form (V-09).
  - TC-136 butir g menyebut banner "1 unit is waiting for approval." tanpa menyebut bentuk jamak; spec mengasersi pertambahan jumlah pada banner.
  - TC-134 memakai `{snFxRej}` (Rejected) yang diubah TC-140 menjadi Available pada spec lain; TC-134 hanya Sync tanpa Submit sehingga tidak mengubahnya.
  - Nama env password selain `AC_TC_PASSWORD` tidak tertulis di TC; disediakan tim FE.
