---
id: TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired
title: "State Tenant: Client Suspended dan Expired Menolak Create, Edit, Delete, Toggle, dan Bulk Action Custom Field, Baca Tetap Tersedia"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-312
  - TC-GS-UCF-313
  - TC-GS-UCF-314
  - TC-GS-UCF-315
  - TC-GS-UCF-422
  - TC-GS-UCF-423
  - TC-GS-UCF-424
  - TC-GS-UCF-425
  - TC-GS-UCF-426
  - TC-GS-UCF-427
  - TC-GS-UCF-428
  - TC-GS-UCF-429
  - TC-GS-UCF-430
  - TC-GS-UCF-431
  - TC-GS-UCF-432
  - TC-GS-UCF-433
  - TC-GS-UCF-434
coverage:
  web: automated
---

# State Tenant: Client Suspended dan Expired Menolak Create, Edit, Delete, Toggle, dan Bulk Action Custom Field, Baca Tetap Tersedia

## Prerequisites

- Mode: FE+BE (backend nyata). Kelas state tenant (h): write-lockdown Client Suspended dan Expired.
- Suite serial (`parallel: false`): spec ini mengubah status Client A (Suspended lalu Expired) secara global untuk seluruh pengguna Client A; tidak berjalan bersamaan dengan spec lain. Sesuai Catatan TC, seluruh TC Suspended dijalankan dalam satu jendela dan seluruh TC Expired dalam jendela lain, dan Client A dikembalikan ke Active sesudah tiap jendela.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah tidak mengulang pembukaan layar kecuali sesudah muat ulang halaman.
- Akun aktor: Total Control Client A `Sari Dewi` (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` saat Client A Active. Password tidak ditulis di spec atau fixture.
- Pelaku perubahan state tenant: Total Control (Principal) `Hendra Wijaya` `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup; instance Principal yang mengatur System Limits dan status entitas). Mekanisme pengubahan status Client A (Active, Suspended, Expired) oleh Principal tidak didefinisikan di TC, PRD, atau LLD modul ini dan disediakan tim FE/BE (kredensial dan sesi Principal disediakan tim FE/BE; tidak ada endpoint karangan). Langkah `[Principal]` hanya memicu perubahan state dan tidak diasersi.
- Data Pre-setup Client A (hanya dibaca; semua aksi tulis ditolak server sehingga record dan Last Updated tidak berubah, pengecualian S-06): `Cost Center` (Active, Placeholder `Select cost center`), `Employee Grade` (Active), `Bonus` (Active), dan `Joining Date` (Inactive) dari 14 Custom Field yang di-seed idempotent oleh hook `before` lewat API (disediakan tim FE/BE; dilewati bila sudah ada).
- Data Dinamis: nama bersuffix `Frozen {runId}-050` dan `Frozen Expired {runId}-050` hanya diketik pada form Create dan tidak pernah tersimpan (ditolak server). Tidak ada seeding lain.
- Cleanup (hook `after`, tidak berasumsi spec berjalan penuh): kembalikan Client A ke Active oleh Principal (wajib walau spec gagal di tengah, supaya spec lain tidak terkena lockdown); tutup popup atau dialog yang masih terbuka; dismiss toast; hapus lewat API Custom Field bersuffix `{runId}-050` bila ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: pengubahan status Client A oleh Principal (di atas); Download CSV dan pengamatan bahwa unduhan berhasil (hanya keberhasilan, tanpa isi berkas); Changelog Custom Field dengan pembacaan baris teratas; Search tabel; penekanan `Esc`; muat ulang halaman (F5) tanpa dialog `beforeunload` (tidak ada form terbuka saat F5).
- State global: status Client A diubah ke Suspended lalu Expired dan dipulihkan ke Active oleh Principal pada langkah akhir dan di hook `after`; flag Guided Tooltip diatur hook suite.

## Test Steps

### Jendela Client A berstatus Suspended

1. [Principal] Ubah status Client A menjadi Suspended (disediakan tim FE/BE), lalu muat ulang halaman Custom Field pada sesi Total Control

### TC-GS-UCF-315: Baca data tetap tersedia saat entitas Suspended

2. Buka tab Custom Field
3. Verifikasi tabel Custom Field tampil normal
4. Klik icon Changelog
5. Verifikasi Changelog tampil normal
6. Catat baris teratas Changelog sebagai baseline jendela Suspended, lalu tutup modal Changelog dengan `[✕]`
7. Klik Download > `Download as CSV`
8. Verifikasi download berhasil

### TC-GS-UCF-312: Create saat entitas Suspended ditolak

9. Klik `[+ Custom Field]`, isi Field Name `Frozen {runId}-050`, pilih Data Type `Text`
10. Klik `[Submit]`
11. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
12. Dismiss toast
13. Klik `[✕]` pada popup Create
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik `[Leave]`
16. Ketik Search `Frozen {runId}-050`, tekan Enter
17. Verifikasi tabel menampilkan empty state "No results found" (`Frozen {runId}-050` tidak dibuat)
18. Klik `(←)` pada kotak Search
19. Verifikasi `[+ Custom Field]` tetap tampil
20. Verifikasi switch Active dan menu `⋯` baris `Cost Center` tetap tampil

### TC-GS-UCF-313: Edit saat entitas Suspended ditolak

21. Klik `⋯` pada baris `Cost Center` > Edit, ubah Placeholder menjadi `Frozen hint`, klik `[Save]`
22. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
23. Verifikasi popup Edit tetap terbuka
24. Verifikasi Placeholder `Frozen hint` dipertahankan di popup Edit
25. Dismiss toast, klik `[✕]` pada popup Edit
26. Verifikasi dialog Unsaved Changes tampil
27. Klik `[Leave]`
28. Verifikasi kolom Placeholder baris `Cost Center` tetap `Select cost center`
29. Klik icon Changelog dan perhatikan baris teratas
30. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
31. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-314: Delete single saat entitas Suspended ditolak

32. Klik `⋯` pada baris `Cost Center` > Delete, klik `[Delete]` pada dialog
33. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
34. Verifikasi baris `Cost Center` tetap ada di tabel
35. Dismiss toast, tekan Esc
36. Klik icon Changelog dan perhatikan baris teratas
37. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
38. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-423: Deactivate single saat entitas Suspended ditolak

39. Matikan switch Active baris `Employee Grade`, klik `[Deactivate]` pada dialog
40. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
41. Verifikasi switch Active baris `Employee Grade` tetap On
42. Dismiss toast, tekan Esc
43. Klik icon Changelog dan perhatikan baris teratas
44. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
45. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-425: Activate single saat entitas Suspended ditolak

46. Nyalakan switch Active baris `Joining Date`, klik `[Activate]` pada dialog
47. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
48. Verifikasi switch Active baris `Joining Date` tetap Off
49. Dismiss toast, tekan Esc
50. Klik icon Changelog dan perhatikan baris teratas
51. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
52. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-429: Bulk Delete saat entitas Suspended ditolak

53. Centang baris `Employee Grade` dan `Bonus`, klik `Bulk Action` > `Delete`, klik `[Delete]` pada dialog
54. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
55. Verifikasi `Employee Grade` dan `Bonus` tetap ada di tabel
56. Dismiss toast, tekan Esc, lalu muat ulang halaman (F5) untuk mengosongkan seleksi
57. Klik icon Changelog dan perhatikan baris teratas
58. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
59. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-431: Bulk Activate saat entitas Suspended ditolak

60. Centang baris `Joining Date` dan `Cost Center`, klik `Bulk Action` > `Activate`, klik `[Activate]` pada dialog
61. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
62. Verifikasi `Joining Date` tetap Inactive
63. Verifikasi `Cost Center` tetap Active
64. Dismiss toast, tekan Esc, lalu muat ulang halaman (F5) untuk mengosongkan seleksi
65. Klik icon Changelog dan perhatikan baris teratas
66. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
67. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-433: Bulk Deactivate saat entitas Suspended ditolak

68. Centang baris `Cost Center` dan `Bonus`, klik `Bulk Action` > `Deactivate`, klik `[Deactivate]` pada dialog
69. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
70. Verifikasi `Cost Center` dan `Bonus` tetap Active
71. Dismiss toast, tekan Esc, lalu muat ulang halaman (F5) untuk mengosongkan seleksi
72. Klik icon Changelog dan perhatikan baris teratas
73. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
74. Tutup modal Changelog dengan `[✕]`

### Jendela Client A berstatus Expired

75. [Principal] Kembalikan Client A ke Active, lalu ubah status Client A menjadi Expired (disediakan tim FE/BE), lalu muat ulang halaman Custom Field pada sesi Total Control
76. Klik icon Changelog, catat baris teratas sebagai baseline jendela Expired, lalu tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-427: Create saat entitas Expired ditolak

77. Klik `[+ Custom Field]`, isi Field Name `Frozen Expired {runId}-050`, pilih Data Type `Text`, klik `[Submit]`
78. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
79. Verifikasi popup Create tetap terbuka
80. Verifikasi Field Name `Frozen Expired {runId}-050` dipertahankan di popup Create
81. Dismiss toast
82. Klik `[✕]` pada popup Create
83. Verifikasi dialog `Unsaved Changes` tampil
84. Klik `[Leave]`
85. Ketik Search `Frozen Expired {runId}-050`, tekan Enter
86. Verifikasi tabel menampilkan empty state "No results found" (`Frozen Expired {runId}-050` tidak ada di tabel)
87. Klik `(←)` pada kotak Search
88. Verifikasi `[+ Custom Field]` tetap tampil
89. Klik icon Changelog dan perhatikan baris teratas
90. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
91. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-422: Edit saat entitas Expired ditolak

92. Klik `⋯` pada baris `Cost Center` > Edit, ubah Placeholder menjadi `Frozen hint`, klik `[Save]`
93. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
94. Verifikasi popup Edit tetap terbuka
95. Verifikasi Placeholder `Frozen hint` dipertahankan di popup Edit
96. Dismiss toast, klik `[✕]` pada popup Edit
97. Verifikasi dialog Unsaved Changes tampil
98. Klik `[Leave]`
99. Verifikasi kolom Placeholder baris `Cost Center` tetap `Select cost center`
100. Klik icon Changelog dan perhatikan baris teratas
101. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
102. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-424: Deactivate single saat entitas Expired ditolak

103. Matikan switch Active baris `Employee Grade`, klik `[Deactivate]` pada dialog
104. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
105. Verifikasi switch Active baris `Employee Grade` tetap On
106. Dismiss toast, tekan Esc
107. Klik icon Changelog dan perhatikan baris teratas
108. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
109. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-426: Activate single saat entitas Expired ditolak

110. Nyalakan switch Active baris `Joining Date`, klik `[Activate]` pada dialog
111. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
112. Verifikasi switch Active baris `Joining Date` tetap Off
113. Dismiss toast, tekan Esc
114. Klik icon Changelog dan perhatikan baris teratas
115. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
116. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-432: Bulk Activate saat entitas Expired ditolak

117. Centang baris `Joining Date` dan `Cost Center`, klik `Bulk Action` > `Activate`, klik `[Activate]` pada dialog
118. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
119. Verifikasi `Joining Date` tetap Inactive
120. Verifikasi `Cost Center` tetap Active
121. Dismiss toast, tekan Esc, lalu muat ulang halaman (F5) untuk mengosongkan seleksi
122. Klik icon Changelog dan perhatikan baris teratas
123. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
124. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-434: Bulk Deactivate saat entitas Expired ditolak

125. Centang baris `Cost Center` dan `Bonus`, klik `Bulk Action` > `Deactivate`, klik `[Deactivate]` pada dialog
126. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
127. Verifikasi `Cost Center` dan `Bonus` tetap Active
128. Dismiss toast, tekan Esc, lalu muat ulang halaman (F5) untuk mengosongkan seleksi
129. Klik icon Changelog dan perhatikan baris teratas
130. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
131. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-430: Bulk Delete saat entitas Expired ditolak

132. Centang baris `Employee Grade` dan `Bonus`, klik `Bulk Action` > `Delete`, klik `[Delete]` pada dialog
133. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
134. Verifikasi `Employee Grade` dan `Bonus` tetap ada di tabel
135. Dismiss toast, tekan Esc, lalu muat ulang halaman (F5) untuk mengosongkan seleksi
136. Klik icon Changelog dan perhatikan baris teratas
137. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
138. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-428: Delete single saat entitas Expired ditolak

139. Klik `⋯` pada baris `Cost Center` > Delete, klik `[Delete]` pada dialog
140. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
141. Verifikasi baris `Cost Center` tetap ada di tabel
142. Dismiss toast, tekan Esc
143. Klik icon Changelog dan perhatikan baris teratas
144. Verifikasi baris teratas Changelog sama dengan baseline yang dicatat (tidak ada entri baru)
145. Tutup modal Changelog dengan `[✕]`

### Pemulihan status Client A

146. [Principal] Kembalikan Client A ke Active (disediakan tim FE/BE)

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness: state tenant (prinsip 13h).
- Spec melewati sekitar 35 langkah (146 langkah). Seluruhnya satu kelas (write-lockdown tenant) dengan satu akun dan data Pre-setup yang hanya dibaca; dua jendela status (Suspended lalu Expired) mengulang pola yang sama (aksi tulis, toast error, state tetap, Changelog tidak berubah) per aksi. Jendela Expired tetap bermakna bila jendela Suspended gagal keras karena dimulai dari langkah Principal yang memulihkan lalu mengubah status. Jumlah langkah muncul dari 9 TC Suspended dan 8 TC Expired dengan satu `Verifikasi` per klausa Expected serta pembacaan Changelog di tiap TC tulis.
- Urutan TC dalam spec: jendela Suspended (315, 312, 313, 314, 423, 425, 429, 431, 433), lalu jendela Expired (427, 422, 424, 426, 432, 434, 430, 428). TC-GS-UCF-315 (baca, screening) berada di awal jendela Suspended. Aksi Delete single dan Bulk Delete ditaruh di akhir jendela Expired dan di tengah jendela Suspended; semua aksi ditolak server sehingga tidak ada data yang hilang. Urutan menyimpang dari urutan TC sumber (312 sampai 315, 422 sampai 434).
- Baseline Changelog: TC sumber meminta "catat baris teratas" di langkah 1 tiap TC. Spec mencatat baseline sekali per jendela (jendela Suspended pada blok TC-GS-UCF-315, jendela Expired pada langkah pembuka jendela) karena tidak ada entri baru dari aksi yang ditolak; tiap TC membandingkan baris teratas Changelog dengan baseline jendela itu (S-12, baseline sebelum aksi pemicu pertama).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah `[Principal]` (mengubah status Client A), muat ulang halaman, Search dan `(←)`, dismiss toast, tekan Esc (menutup dialog konfirmasi pada TC tulis; TC sumber tidak mendefinisikan apakah dialog tertutup sendiri sesudah penolakan, sehingga Esc dipakai sebagai penutup deterministik tanpa langkah bersyarat), klik `[✕]` dan `[Leave]` (menutup popup dirty, S-08), dan penutupan modal Changelog.
- Dismiss toast sebelum aksi berikutnya karena teks toast error identik antar TC (S-09).
- Asersi tambahan di luar Expected TC (S-03): dialog Unsaved Changes pada TC Edit diasersi karena penutupan form dirty mengikuti S-08. Pada TC-GS-UCF-312, penutupan popup Create (`[✕]` lalu `[Leave]`) dan Search `Frozen {runId}-050` (empty state "No results found" sebagai anchor absence) adalah langkah penghubung untuk mengamati "Frozen tidak dibuat"; TC-GS-UCF-312 tidak memuat langkah penutupan.
- Pembagian TC lintas spec: perilaku identik lintas plan ada di spec 075.
- Temuan untuk QA:
  - Mekanisme pengubahan status Client A (Suspended, Expired, Active) oleh Principal tidak didefinisikan di TC, PRD, atau LLD modul; ditulis sebagai kemampuan tim FE/BE. Catatan TC menyebut "entitas Suspended atau Expired diatur Principal".
  - Post Condition "Data Custom Field tidak berubah" (TC-GS-UCF-313, 314, 422 sampai 434) tidak punya langkah observasi terpisah selain Expected; diwakili oleh Expected "tetap ada" atau "tetap" dan baris teratas Changelog, sedangkan Last Updated tidak diasersi.
  - TC-GS-UCF-312 butir b ("list di-refresh") dan butir c ("visibilitas elemen tidak berubah") tidak mendefinisikan elemen yang dibandingkan; spec mengasersi `[+ Custom Field]`, switch Active, dan menu `⋯` tetap tampil. TC-GS-UCF-312 tidak memuat langkah penutupan popup Create sedangkan TC-GS-UCF-427 mendefinisikan popup tetap terbuka; spec menutup popup lewat `[✕]` dan `[Leave]`.
  - TC sumber tidak mendefinisikan state dialog konfirmasi setelah penolakan (tertutup atau tetap terbuka) untuk TC-GS-UCF-314, 423 sampai 426, 428 sampai 434; spec menutupnya dengan `Esc` sebagai langkah penghubung.
  - TC-GS-UCF-315 butir b ("Download berhasil") tidak menyebut format, nama, atau isi berkas; spec hanya mengasersi bahwa unduhan CSV berhasil. Tidak ada TC baca untuk jendela Expired.
  - Nama `Frozen` dan `Frozen Expired` pada TC-GS-UCF-312 dan 427 tidak bersuffix; spec memakai `Frozen {runId}-050` dan `Frozen Expired {runId}-050` (tidak pernah tersimpan).
  - Email akun Total Control Principal tercantum di Pre-setup TC tetapi kredensialnya tidak (disediakan tim FE/BE).
