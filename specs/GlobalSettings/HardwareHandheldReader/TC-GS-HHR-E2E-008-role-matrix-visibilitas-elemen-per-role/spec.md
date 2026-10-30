---
id: TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role
title: "Role Matrix: Visibilitas Elemen Handheld Reader per Role"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-33
  - TC-GS-HHR-34
  - TC-GS-HHR-36
  - TC-GS-HHR-37
  - TC-GS-HHR-38
  - TC-GS-HHR-39
  - TC-GS-HHR-40
  - TC-GS-HHR-41
  - TC-GS-HHR-201
  - TC-GS-HHR-202
  - TC-GS-HHR-203
  - TC-GS-HHR-204
  - TC-GS-HHR-205
  - TC-GS-HHR-206
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Handheld Reader per Role

## Prerequisites

- Mode: FE+BE. Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk setiap akun pada tabel di bawah (lihat `suite.md`, Hook suite).
- Kemampuan teknis: pembaca berkas unduhan CSV/XLSX (hanya untuk memastikan berkas terunduh pada blok Read Only).
- Data: Client A (plan Growth). Seed Reader A (DD-01 s.d. DD-10, Tabel Data Uji Dinamis TC) tersedia dan dipulihkan fixture BE (disediakan tim FE) sebelum spec berjalan. Spec hanya membaca: Overlay row action dibuka lalu ditutup, seleksi checkbox dibersihkan, tidak ada aksi mutasi yang dijalankan sehingga data Seed Reader A tidak berubah. Jumlah `Select All (8 records)` pada TC-GS-HHR-203 berasal dari 8 reader berstatus Available, Damaged, atau Missing pada Seed Reader A (DD-01 s.d. DD-04, DD-06 s.d. DD-09), sedangkan DD-05 dan DD-10 berstatus Waiting for Approval.
- Spec ini Role Matrix visibilitas elemen (bagian 3a konvensi): langkah tiap role berbeda (elemen yang tampil dan Hidden berbeda), sehingga ditulis per blok role, bukan perulangan.

Role yang diuji (Tabel Data Uji Pre-setup #1 s.d. #7, Client A):

| Blok | TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| 1 | TC-GS-HHR-36 | Total Control | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| 2 | TC-GS-HHR-34, TC-GS-HHR-37, TC-GS-HHR-204 | Read Only | Maya Putri | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| 3 | TC-GS-HHR-34, TC-GS-HHR-38, TC-GS-HHR-205 | Manage hardware (Read) | Tono Hartono | `manageHardwareRead_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_READ_PASSWORD` |
| 4 | TC-GS-HHR-39, TC-GS-HHR-206 | Manage hardware (Create) | Rina Lestari | `manageHardwareCreate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` |
| 5 | TC-GS-HHR-40, TC-GS-HHR-201, TC-GS-HHR-203 | Manage hardware (Update) | Agus Wijaya | `manageHardwareUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| 6 | TC-GS-HHR-41, TC-GS-HHR-202 | Manage hardware (Delete) | Dewi Anggraini | `manageHardwareDelete_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DELETE_PASSWORD` |
| 7 | TC-GS-HHR-33 | Tanpa Capability | Hendra Gunawan | `noCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_NOCAP_PASSWORD` |

- Login Total Control (blok 1) dilakukan di hook `before`; blok berikutnya memakai langkah ganti akun eksplisit (logout lalu login). Karena spec berakhir di akun Tanpa Capability, hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password hanya lewat env, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > Hardware > Handheld Reader dibuka di hook `beforeEach`; blok yang butuh halaman utama Global Settings (TC-GS-HHR-33 dan TC-GS-HHR-34) membukanya lewat langkah eksplisit.
- State global yang diubah: tidak ada.

## Test Steps

### Blok 1 - Total Control: TC-GS-HHR-36

1. Verifikasi toolbar menampilkan `Search`, `Filter`, `Download`, `Changelog`, `Event Log`, dan `+ Activate Reader` (semuanya Show)
2. Klik `⋯` pada baris DD-01 (`Zebra RFID Reader - 1`)
3. Verifikasi Overlay row action DD-01 berisi `Detail`, `Edit Alias Name`, `Edit Reader Power`, `Mark as Damaged`, `Mark as Missing`, `Delete`
4. Tutup Overlay row action dengan Esc
5. Klik `⋯` pada baris DD-03 (`Zebra Mobile Reader - 1`)
6. Verifikasi Overlay row action DD-03 berisi `Detail`, `Edit Alias Name`, `Edit Reader Power`, `Mark as Available`, `Delete`
7. Tutup Overlay row action dengan Esc
8. Klik `⋯` pada baris DD-05 (`Chainway C72 - 1`)
9. Verifikasi Overlay row action DD-05 berisi `Detail` dan `Cancel Request`
10. Tutup Overlay row action dengan Esc

### Blok 2 - Read Only: TC-GS-HHR-34, TC-GS-HHR-37, TC-GS-HHR-204

11. Logout, lalu login sebagai Maya Putri (Read Only)
12. Buka halaman utama Global Settings
13. Buka sidebar Global Settings dan menu Hardware
14. Verifikasi item `Handheld Reader` tampil di sidebar
15. Klik `Handheld Reader`
16. Verifikasi halaman Handheld Reader terbuka dengan data 10 baris
17. Verifikasi tombol `[+ Activate Reader]` Hidden
18. Klik `⋯` pada baris DD-01 (`Zebra RFID Reader - 1`)
19. Verifikasi Overlay row action DD-01 hanya berisi `Detail`
20. Tutup Overlay row action dengan Esc
21. Klik `⋯` pada baris DD-05 (`Chainway C72 - 1`)
22. Verifikasi Overlay row action DD-05 hanya berisi `Detail`
23. Tutup Overlay row action dengan Esc
24. Klik ikon Changelog
25. Verifikasi Modal Changelog tampil dan memuat entri
26. Tutup Modal Changelog
27. Klik ikon Event Log
28. Verifikasi popup Event Log tampil dan memuat baris
29. Tutup popup Event Log
30. Klik `Gudang Reader - 1`
31. Verifikasi Popup Detail tampil dengan tab `Usage` dan `Changelog`
32. Tutup Popup Detail
33. Verifikasi License Counter Cards tampil
34. Klik ikon Download
35. Verifikasi pilihan CSV dan XLSX tampil
36. Klik `CSV`
37. Verifikasi berkas CSV terunduh
38. Klik ikon Download
39. Klik `XLSX`
40. Verifikasi berkas XLSX terunduh
41. Verifikasi tidak ada elemen mutasi Disabled yang menampilkan tooltip izin pada toolbar dan Overlay row action (elemen mutasi Hidden, bukan Disabled)
42. Verifikasi Search tampil dan aktif
43. Verifikasi Filter tampil dan aktif
44. Verifikasi Pagination tampil dan aktif
45. Verifikasi header kolom Actions `(⋯)` (Column Visibility) tampil dan aktif
46. Klik header kolom `Device Name` sekali
47. Verifikasi indikator sort pada header `Device Name` berubah
48. Verifikasi header tabel dimulai dari `Device Name` (kolom `Checkbox` tidak tampil)
49. Verifikasi tidak ada Bulk Action Bar

### Blok 3 - Manage hardware (Read): TC-GS-HHR-34, TC-GS-HHR-38, TC-GS-HHR-205

50. Logout, lalu login sebagai Tono Hartono (Manage hardware level Read)
51. Buka halaman utama Global Settings
52. Buka sidebar Global Settings dan menu Hardware
53. Verifikasi item `Handheld Reader` tampil di sidebar
54. Klik `Handheld Reader`
55. Verifikasi halaman Handheld Reader terbuka dengan data 10 baris
56. Verifikasi tombol `[+ Activate Reader]` Hidden
57. Klik `⋯` pada baris DD-01 (`Zebra RFID Reader - 1`)
58. Verifikasi Overlay row action DD-01 hanya berisi `Detail`
59. Tutup Overlay row action dengan Esc
60. Klik `⋯` pada baris DD-05 (`Chainway C72 - 1`)
61. Verifikasi Overlay row action DD-05 hanya berisi `Detail`
62. Tutup Overlay row action dengan Esc
63. Verifikasi ikon Changelog tampil
64. Verifikasi ikon Event Log tampil
65. Verifikasi ikon Download (Export) tampil
66. Verifikasi License Counter Cards tampil
67. Verifikasi Search tampil dan aktif
68. Verifikasi Filter tampil dan aktif
69. Verifikasi Pagination tampil dan aktif
70. Verifikasi header kolom Actions `(⋯)` (Column Visibility) tampil dan aktif
71. Klik header kolom `Device Name` sekali
72. Verifikasi indikator sort pada header `Device Name` berubah
73. Verifikasi header tabel dimulai dari `Device Name` (kolom `Checkbox` tidak tampil)
74. Verifikasi tidak ada Bulk Action Bar

### Blok 4 - Manage hardware (Create): TC-GS-HHR-39, TC-GS-HHR-206

75. Logout, lalu login sebagai Rina Lestari (Manage hardware level Create)
76. Buka Global Settings > Hardware > Handheld Reader
77. Verifikasi tombol `[+ Activate Reader]` tampil (Show)
78. Klik `⋯` pada baris DD-01 (`Zebra RFID Reader - 1`)
79. Verifikasi Overlay row action DD-01 hanya berisi `Detail`
80. Tutup Overlay row action dengan Esc
81. Klik `⋯` pada baris DD-05 (`Chainway C72 - 1`)
82. Verifikasi Overlay row action DD-05 hanya berisi `Detail`
83. Tutup Overlay row action dengan Esc
84. Verifikasi ikon Changelog tampil
85. Verifikasi ikon Event Log tampil
86. Verifikasi ikon Download (Export) tampil
87. Verifikasi header tabel dimulai dari `Device Name` (kolom `Checkbox` tidak tampil)
88. Verifikasi tidak ada Bulk Action Bar

### Blok 5 - Manage hardware (Update): TC-GS-HHR-40, TC-GS-HHR-201, TC-GS-HHR-203

89. Logout, lalu login sebagai Agus Wijaya (Manage hardware level Update)
90. Buka Global Settings > Hardware > Handheld Reader
91. Verifikasi tombol `[+ Activate Reader]` Hidden
92. Klik `⋯` pada baris DD-01 (`Zebra RFID Reader - 1`)
93. Verifikasi Overlay row action DD-01 berisi `Detail`, `Edit Alias Name`, `Edit Reader Power`, `Mark as Damaged`, `Mark as Missing`
94. Tutup Overlay row action dengan Esc
95. Klik `⋯` pada baris DD-03 (`Zebra Mobile Reader - 1`)
96. Verifikasi Overlay row action DD-03 berisi `Detail`, `Edit Alias Name`, `Edit Reader Power`, `Mark as Available`
97. Tutup Overlay row action dengan Esc
98. Klik `⋯` pada baris DD-05 (`Chainway C72 - 1`)
99. Verifikasi Overlay row action DD-05 hanya berisi `Detail`
100. Tutup Overlay row action dengan Esc
101. Centang checkbox baris DD-01
102. Centang checkbox baris DD-07
103. Klik tombol `Bulk Action`
104. Verifikasi opsi `Mark as Damaged` dan `Mark as Missing` tampil
105. Verifikasi opsi `Delete` tidak ada
106. Tutup daftar opsi Bulk Action dengan Esc
107. Klik ikon `×` pada Bulk Action Bar untuk membersihkan seleksi
108. Centang checkbox baris DD-01
109. Centang checkbox baris DD-03
110. Verifikasi Bulk Action Bar tampil dengan teks `2 Readers selected`, tombol `Select All (8 records)`, dan ikon `×`
111. Verifikasi tombol `Bulk Action` tidak tampil
112. Klik ikon `×` pada Bulk Action Bar untuk membersihkan seleksi

### Blok 6 - Manage hardware (Delete): TC-GS-HHR-41, TC-GS-HHR-202

113. Logout, lalu login sebagai Dewi Anggraini (Manage hardware level Delete)
114. Buka Global Settings > Hardware > Handheld Reader
115. Verifikasi tombol `[+ Activate Reader]` Hidden
116. Klik `⋯` pada baris DD-01 (`Zebra RFID Reader - 1`)
117. Verifikasi Overlay row action DD-01 berisi `Detail` dan `Delete`
118. Tutup Overlay row action dengan Esc
119. Klik `⋯` pada baris DD-03 (`Zebra Mobile Reader - 1`)
120. Verifikasi Overlay row action DD-03 berisi `Detail` dan `Delete`
121. Tutup Overlay row action dengan Esc
122. Klik `⋯` pada baris DD-05 (`Chainway C72 - 1`)
123. Verifikasi Overlay row action DD-05 berisi `Detail` dan `Cancel Request`
124. Tutup Overlay row action dengan Esc
125. Centang checkbox baris DD-01
126. Centang checkbox baris DD-07
127. Klik tombol `Bulk Action`
128. Verifikasi opsi `Delete` tampil
129. Verifikasi opsi `Mark as Damaged` dan `Mark as Missing` tidak ada
130. Tutup daftar opsi Bulk Action dengan Esc
131. Klik ikon `×` pada Bulk Action Bar untuk membersihkan seleksi

### Blok 7 - Tanpa Capability: TC-GS-HHR-33

132. Logout, lalu login sebagai Hendra Gunawan (Tanpa Capability)
133. Buka halaman utama Global Settings
134. Buka sidebar Global Settings
135. Verifikasi sidebar Global Settings tampil dengan sedikitnya satu item menu
136. Verifikasi item `Handheld Reader` tidak tampil di sidebar (menu Hardware)

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 2 Role & Capability Access Flow dan section 3k Bulk). Kelas harness: Role Matrix (bagian 3a), `caseType` Negative mengikuti alur dominan (sebagian besar TC menguji elemen Hidden atau tidak tersedia).
- Subjudul `###` memetakan langkah ke blok role dan id TC granular. TC-GS-HHR-34 muncul di blok 2 (Read Only) dan blok 3 (Manage hardware Read) karena judul TC menyebut keduanya.
- Spec melewati sekitar 35 langkah (136 langkah nominal, tanpa perulangan). Semua langkah satu kelas harness (Role Matrix, hanya baca, tanpa aksi mutasi dan tanpa data yang dibuat); tiap blok role berdiri sendiri dengan login ulang di awal blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok ditulis per role karena elemen yang diasersi berbeda per role (bagian 3a, `[KEPUTUSAN 2026-10-21]`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): menutup Overlay row action, daftar Bulk Action, Modal Changelog, popup Event Log, dan Popup Detail (langkah 4, 10, 20, 23, 26, 29, 32, 59, 62, 80, 83, 94, 97, 100, 106, 118, 121, 124, 130); membersihkan seleksi lewat `×` (langkah 107, 112, 131, S-09); logout lalu login ke role berikutnya (langkah 11, 50, 75, 89, 113, 132); membuka halaman utama Global Settings dan halaman Handheld Reader; klik kedua `Download` pada langkah 38.
- Asersi Hidden dan "tidak ada" memakai anchor permukaan: elemen lain pada toolbar atau Overlay yang sama sudah tampil (Overlay row action hanya `Detail` didahului Overlay yang terbuka; opsi Bulk Action yang tidak ada didahului opsi lain yang tampil; kolom `Checkbox` tidak tampil didahului header `Device Name` pada halaman yang sudah termuat), bagian 8b butir 2 dan 11.
- Temuan untuk QA:
  - TC-GS-HHR-34 berjudul "Read Only dan pemegang capability Manage hardware level Read", tetapi Precondition hanya Login Read Only; spec menjalankannya untuk kedua role (blok 2 dan blok 3).
  - TC-GS-HHR-33 tidak menyebut item menu yang pasti tampil pada sidebar akun Tanpa Capability; anchor absence memakai pembanding generik "sedikitnya satu item menu" pada sidebar.
  - TC-GS-HHR-36 sampai TC-GS-HHR-41 tidak menyebut halaman tempat baris DD-01, DD-03, DD-05, dan DD-07 berada; spec mengasumsikan halaman 1 pada urutan default (10 baris).
  - TC-GS-HHR-37 butir d ("tidak ada tooltip izin karena elemen mutasi Hidden") tidak punya cara pengamatan langsung; spec menulis satu `Verifikasi` yang menyimpulkan dari elemen mutasi yang Hidden. TC-GS-HHR-37 butir c ("tampil dan berfungsi") tidak merinci "berfungsi" untuk Download; spec memakai berkas CSV dan XLSX terunduh.
  - Seed Reader A dipakai sebagai target buka Overlay (S-06): spec tidak menjalankan aksi mutasi sehingga tidak ada perubahan yang perlu dipulihkan; Seed Reader A disiapkan fixture BE (disediakan tim FE).
  - TC-GS-HHR-203 menyebut `Select All (8 records)`: jumlah 8 mengikuti Seed Reader A; bila fixture memuat jumlah reader lain, angka itu berubah.
