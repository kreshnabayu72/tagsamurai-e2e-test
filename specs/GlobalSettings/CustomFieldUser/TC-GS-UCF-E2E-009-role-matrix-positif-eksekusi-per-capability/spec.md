---
id: TC-GS-UCF-E2E-009-role-matrix-positif-eksekusi-per-capability
title: "Role Matrix Positif: Eksekusi Create, Edit, Activate, Deactivate, dan Delete oleh Aktor dengan Capability Spesifik dan Default User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-40
  - TC-GS-UCF-41
  - TC-GS-UCF-42
  - TC-GS-UCF-43
  - TC-GS-UCF-393
  - TC-GS-UCF-394
  - TC-GS-UCF-395
  - TC-GS-UCF-484
  - TC-GS-UCF-485
coverage:
  web: automated
---

# Role Matrix Positif: Eksekusi Create, Edit, Activate, Deactivate, dan Delete oleh Aktor dengan Capability Spesifik dan Default User

## Prerequisites

- Mode: FE+BE (backend nyata).
- Spec Role Matrix positif (bagian 3a konvensi): aksi berhasil; role yang diuji adalah role spesifik yang berhak atas aksi itu dan Default User. Langkah berbeda per role sehingga spec ditulis per blok role.

Role yang diuji (Tabel Data Uji Pre-setup; semua Client A):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-GS-UCF-40 | Manage user and role: Create dan Read (Rina Marlina, Modified By `Rina M`) | `manageUserCreate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` |
| TC-GS-UCF-41, 484, 485 | Manage user and role: Update dan Read (Agus Wijaya) | `manageUserUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-UCF-42 | Manage user and role: Delete dan Read (Dewi Lestari) | `manageUserDelete_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DELETE_PASSWORD` |
| TC-GS-UCF-43 | Manage user and role: Full CRUD (Bayu Saputra) | `manageUserFullCrud_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_FULLCRUD_PASSWORD` |
| TC-GS-UCF-393, 394, 395 | Default User (Teguh Santoso, Modified By `Teguh S`) | `defaultUser_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DEFAULT_PASSWORD` |

- Akun aktor pertama (Create dan Read) login di hook `before`; akun berikutnya login lewat langkah ganti akun eksplisit di awal tiap blok role. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite (`Spectra.env.GS_TC_PASSWORD`).
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > Custom Field untuk akun hook `before`; setelah ganti akun, tab Custom Field dibuka oleh langkah ganti akun (login membuka layar awal akun).
- Data Dinamis (bersuffix `{runId}-009`, milik spec ini; fixture baru `Fixture.customFieldUser.roleExec009`). Seed lewat API di hook `before` (semua Text, bebas nilai User):
  - D-05: `Delete Probe A {runId}-009` dan D-06: `Delete Probe B {runId}-009` (precondition TC-GS-UCF-42).
  - D-213: `Upd Act {runId}-009` (Inactive; TC-GS-UCF-484).
  - D-214: `Upd Off A {runId}-009` dan D-215: `Upd Off B {runId}-009` (Active; TC-GS-UCF-485).
  - D-172: `Default Status A {runId}-009` dan D-173: `Default Status B {runId}-009` (Active; TC-GS-UCF-394).
  - D-174: `Default Bulk A {runId}-009` dan D-175: `Default Bulk B {runId}-009` (TC-GS-UCF-395).
  - Dibuat lewat UI oleh spec: D-04 `Cost Allocation {runId}-009` (TC-GS-UCF-40; di-rename TC-GS-UCF-41 menjadi `Cost Allocation Code {runId}-009`; dihapus TC-GS-UCF-42), `Full Crud Probe {runId}-009` (TC-GS-UCF-43; di-rename `Full Crud Probe 2 {runId}-009`, dihapus di TC yang sama), dan `Default Probe {runId}-009` (TC-GS-UCF-393; di-rename `Default Probe 2 {runId}-009`, dihapus di TC yang sama).
- Rantai data dalam spec: TC-GS-UCF-40 membuat `Cost Allocation`, TC-GS-UCF-41 mengubahnya, TC-GS-UCF-42 menghapusnya (kolom Dependensi TC); rantai ini dijalankan dalam spec yang sama, tidak menumpang spec lain.
- Data Pre-setup: tidak ada yang dipakai langkah (6 field Pre-setup dan Population hanya mengisi tabel; tidak diubah). Population D-01 tidak di-seed karena tidak ada asersi yang bergantung pada urutan atau jumlahnya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua field bersuffix `{runId}-009` yang masih ada; kosongkan Search tabel; kembalikan sesi ke akun default suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk semua akun role di atas dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan toast, dialog, dan bullet dialog; pembacaan isi overlay `Bulk Action`; ganti akun (logout lalu login).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-40: Aktor Create dan Read berhasil membuat Custom Field

1. Klik `[+ Custom Field]`
2. Isi Field Name `Cost Allocation {runId}-009`, pilih Data Type `Text`
3. Klik `[Submit]`
4. Verifikasi toast sukses: "Success, custom field has been created."
5. Ketik Search `Cost Allocation`, tekan Enter
6. Verifikasi `Cost Allocation {runId}-009` muncul di tabel
7. Verifikasi switch Active baris `Cost Allocation {runId}-009` On
8. Verifikasi Modified By baris `Cost Allocation {runId}-009` `Rina M`
9. Klik `(←)` pada kotak Search

### TC-GS-UCF-41: Aktor Update dan Read berhasil mengubah, menonaktifkan, dan menjalankan Bulk Activate Custom Field

10. Ganti akun: logout, lalu login sebagai Manage user and role: Update dan Read
11. Buka Global Settings > User > Custom Field
12. Ketik Search `Cost Allocation`, tekan Enter
13. Klik `⋯` pada baris `Cost Allocation {runId}-009`, pilih `Edit`
14. Ubah Field Name menjadi `Cost Allocation Code {runId}-009`, klik `[Save]`
15. Verifikasi toast sukses: "Success, custom field has been updated."
16. Verifikasi baris menampilkan `Cost Allocation Code {runId}-009`
17. Matikan switch Active baris `Cost Allocation Code {runId}-009`, klik `[Deactivate]` pada dialog
18. Verifikasi toast sukses: "Success, custom field has been deactivated."
19. Verifikasi switch Active baris `Cost Allocation Code {runId}-009` Off
20. Centang baris `Cost Allocation Code {runId}-009`, klik `Bulk Action`, pilih `Activate`, klik `[Activate]` pada dialog
21. Verifikasi toast sukses: "Success, custom field has been activated."
22. Verifikasi switch Active baris `Cost Allocation Code {runId}-009` On
23. Klik `(←)` pada kotak Search

### TC-GS-UCF-484: Aktor Update dan Read mengaktifkan Custom Field single lewat switch Active

24. Ketik Search `Upd Act`, tekan Enter
25. Verifikasi switch Active baris `Upd Act {runId}-009` Enabled
26. Nyalakan switch Active baris `Upd Act {runId}-009`
27. Verifikasi dialog `Activate Custom Field` tampil dengan bullet `Upd Act {runId}-009`
28. Klik `[Activate]` pada dialog
29. Verifikasi toast sukses: "Success, custom field has been activated."
30. Verifikasi switch Active baris `Upd Act {runId}-009` On
31. Klik `(←)` pada kotak Search

### TC-GS-UCF-485: Aktor Update dan Read menjalankan Bulk Deactivate

32. Ketik Search `Upd Off`, tekan Enter
33. Centang baris `Upd Off A {runId}-009` dan `Upd Off B {runId}-009`
34. Klik `Bulk Action`, perhatikan daftar aksi
35. Verifikasi overlay `Bulk Action` memuat `Deactivate`
36. Verifikasi `Activate` tidak tampil pada overlay `Bulk Action` (seluruh seleksi Active)
37. Verifikasi `Delete` tidak tampil pada overlay `Bulk Action` (aktor tanpa capability Delete)
38. Pilih `Deactivate`
39. Verifikasi dialog `Deactivate Custom Fields` tampil dengan bullet `Upd Off A {runId}-009` dan `Upd Off B {runId}-009`
40. Klik `[Deactivate]` pada dialog
41. Verifikasi toast sukses: "Success, custom field has been deactivated."
42. Verifikasi switch Active baris `Upd Off A {runId}-009` Off
43. Verifikasi switch Active baris `Upd Off B {runId}-009` Off
44. Klik `(←)` pada kotak Search

### TC-GS-UCF-42: Aktor Delete dan Read berhasil menghapus single dan Bulk Delete

45. Ganti akun: logout, lalu login sebagai Manage user and role: Delete dan Read
46. Buka Global Settings > User > Custom Field
47. Ketik Search `Cost Allocation`, tekan Enter
48. Klik `⋯` pada baris `Cost Allocation Code {runId}-009`, pilih `Delete`
49. Verifikasi dialog `Delete Custom Field` tampil
50. Klik `[Delete]` pada dialog
51. Verifikasi toast sukses: "Success, custom field has been deleted."
52. Verifikasi baris `Cost Allocation Code {runId}-009` hilang dari tabel
53. Klik `(←)` pada kotak Search
54. Ketik Search `Delete Probe`, tekan Enter
55. Centang baris `Delete Probe A {runId}-009` dan `Delete Probe B {runId}-009`
56. Klik `Bulk Action`, pilih `Delete`
57. Verifikasi dialog `Delete Custom Fields` tampil dengan 2 bullet `Delete Probe A {runId}-009` dan `Delete Probe B {runId}-009`
58. Klik `[Delete]` pada dialog
59. Verifikasi toast sukses: "Success, custom field has been deleted."
60. Verifikasi baris `Delete Probe A {runId}-009` hilang dari tabel
61. Verifikasi baris `Delete Probe B {runId}-009` hilang dari tabel
62. Klik `(←)` pada kotak Search

### TC-GS-UCF-43: Aktor Full CRUD menjalankan Create, Edit, dan Delete pada satu field

63. Ganti akun: logout, lalu login sebagai Manage user and role: Full CRUD
64. Buka Global Settings > User > Custom Field
65. Klik `[+ Custom Field]`, isi Field Name `Full Crud Probe {runId}-009`, Data Type `Text`, klik `[Submit]`
66. Verifikasi toast sukses: "Success, custom field has been created."
67. Ketik Search `Full Crud Probe`, tekan Enter
68. Klik `⋯` pada baris `Full Crud Probe {runId}-009`, pilih `Edit`
69. Ubah Field Name menjadi `Full Crud Probe 2 {runId}-009`, klik `[Save]`
70. Verifikasi toast sukses: "Success, custom field has been updated."
71. Klik `⋯` pada baris `Full Crud Probe 2 {runId}-009`, pilih `Delete`, klik `[Delete]` pada dialog
72. Verifikasi toast sukses: "Success, custom field has been deleted."
73. Verifikasi baris `Full Crud Probe 2 {runId}-009` hilang dari tabel
74. Klik `(←)` pada kotak Search

### TC-GS-UCF-393: Aktor Default User membuat, mengubah, dan menghapus satu Custom Field

75. Ganti akun: logout, lalu login sebagai Default User
76. Buka Global Settings > User > Custom Field
77. Klik `[+ Custom Field]`, isi Field Name `Default Probe {runId}-009`, pilih Data Type `Text`, klik `[Submit]`
78. Verifikasi toast sukses: "Success, custom field has been created."
79. Ketik Search `Default Probe`, tekan Enter
80. Verifikasi baris `Default Probe {runId}-009` tampil
81. Verifikasi switch Active baris `Default Probe {runId}-009` On
82. Verifikasi Modified By baris `Default Probe {runId}-009` `Teguh S`
83. Klik `⋯` pada baris `Default Probe {runId}-009`, pilih `Edit`, ubah Field Name menjadi `Default Probe 2 {runId}-009`, klik `[Save]`
84. Verifikasi toast sukses: "Success, custom field has been updated."
85. Verifikasi baris menampilkan `Default Probe 2 {runId}-009`
86. Klik `⋯` pada baris `Default Probe 2 {runId}-009`, pilih `Delete`
87. Verifikasi dialog `Delete Custom Field` tampil
88. Klik `[Delete]` pada dialog
89. Verifikasi toast sukses: "Success, custom field has been deleted."
90. Verifikasi baris `Default Probe 2 {runId}-009` hilang dari tabel
91. Klik `(←)` pada kotak Search

### TC-GS-UCF-394: Aktor Default User menonaktifkan dan mengaktifkan field lewat switch dan Bulk Action

92. Ketik Search `Default Status`, tekan Enter
93. Matikan switch Active baris `Default Status A {runId}-009`
94. Verifikasi dialog `Deactivate Custom Field` tampil
95. Klik `[Deactivate]` pada dialog
96. Verifikasi toast sukses: "Success, custom field has been deactivated."
97. Verifikasi switch Active baris `Default Status A {runId}-009` Off
98. Nyalakan switch Active baris `Default Status A {runId}-009`
99. Verifikasi dialog `Activate Custom Field` tampil
100. Klik `[Activate]` pada dialog
101. Verifikasi toast sukses: "Success, custom field has been activated."
102. Verifikasi switch Active baris `Default Status A {runId}-009` On
103. Centang baris `Default Status A {runId}-009` dan `Default Status B {runId}-009`, klik `Bulk Action`, pilih `Deactivate`
104. Verifikasi dialog `Deactivate Custom Fields` tampil dengan bullet `Default Status A {runId}-009` dan `Default Status B {runId}-009`
105. Klik `[Deactivate]` pada dialog
106. Verifikasi toast sukses: "Success, custom field has been deactivated."
107. Verifikasi switch Active baris `Default Status A {runId}-009` dan `Default Status B {runId}-009` Off
108. Centang baris `Default Status A {runId}-009` dan `Default Status B {runId}-009`, klik `Bulk Action`, pilih `Activate`
109. Verifikasi dialog `Activate Custom Fields` tampil dengan bullet `Default Status A {runId}-009` dan `Default Status B {runId}-009`
110. Klik `[Activate]` pada dialog
111. Verifikasi toast sukses: "Success, custom field has been activated."
112. Verifikasi switch Active baris `Default Status A {runId}-009` dan `Default Status B {runId}-009` On
113. Klik `(←)` pada kotak Search

### TC-GS-UCF-395: Aktor Default User menjalankan Bulk Delete

114. Ketik Search `Default Bulk`, tekan Enter
115. Centang baris `Default Bulk A {runId}-009` dan `Default Bulk B {runId}-009`
116. Klik `Bulk Action`, pilih `Delete`
117. Verifikasi dialog `Delete Custom Fields` tampil dengan bullet `Default Bulk A {runId}-009` dan `Default Bulk B {runId}-009`
118. Klik `[Delete]` pada dialog
119. Verifikasi toast sukses: "Success, custom field has been deleted."
120. Verifikasi baris `Default Bulk A {runId}-009` dan `Default Bulk B {runId}-009` hilang dari tabel
121. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif (bagian 3a): satu kelas (eksekusi aksi sukses per capability). Spec melewati sekitar 35 langkah (121 langkah) karena lima blok role dijalankan berurutan; tiap blok berdiri sendiri dengan langkah ganti akun eksplisit dan data seed milik spec. Satu-satunya ketergantungan antar blok adalah rantai TC-GS-UCF-40 → 41 → 42 pada field `Cost Allocation` (Dependensi TC), yang dijalankan dalam spec yang sama; kegagalan TC-GS-UCF-40 membuat 41 dan 42 kehilangan data.
- Urutan TC di spec: 40, 41, 484, 485, 42, 43, 393, 394, 395. Pengelompokan per akun menyimpang dari daftar sumber supaya ganti akun satu kali per role (Update dan Read: 41, 484, 485; Default User: 393, 394, 395). Aksi yang menghapus data (TC-GS-UCF-42, 43, 393, 395) ditaruh sesudah aksi lain yang memakai data yang sama, dan tiap Delete hanya menghapus data milik spec.
- Langkah penghubung (aksi tanpa `Verifikasi`): ganti akun dan membuka Global Settings > User > Custom Field di awal tiap blok akun baru, Search atomik "Ketik Search `X`, tekan Enter" untuk menemukan baris target, dan `(←)` pada kotak Search untuk mengosongkan Search dan mereset tabel. Search `Cost Allocation` (bukan nama utuh) dipakai pada TC-GS-UCF-41 dan 42 supaya baris tetap ditemukan sebelum dan sesudah rename.
- Asersi "baris hilang dari tabel" sesudah Delete beranchor toast sukses yang sudah diasersi (bagian 8b butir 2).
- Toast sukses Bulk Delete memakai teks tunggal `Success, custom field has been deleted.` sesuai TC (Expected TC-GS-UCF-42 b, 395 b), demikian pula Bulk Activate dan Deactivate.
- Temuan untuk QA:
  - Post Condition TC-GS-UCF-484 dan 485 ("efek ke User, Non-Login User, My Profile, FA > Settings > User, AC > Settings > User, AC > Settings > Group popup Total User Detail, Import") tidak punya langkah observasi di TC dan tidak punya Expected padanan, sehingga tidak diasersi di spec ini (S-01). Post Condition TC-GS-UCF-40 (D-04), 41, dan 42 serupa: tidak diasersi.
  - TC-GS-UCF-40 Expected b menyebut Modified By "aktor" tanpa format; spec mengasersi `Rina M` berformat `[First Name] [Last Initial]` untuk Rina Marlina.
  - TC-GS-UCF-40 tidak menyebut apakah popup Create tertutup setelah `[Submit]` (checkbox Stay on this form after submitting tidak dicentang); spec mengasumsikan popup tertutup dan mencari baris lewat Search.
  - TC-GS-UCF-41 langkah 4 dan TC-GS-UCF-394 langkah 3 menyebut `Bulk Action` > `Activate` atau `Deactivate` tanpa menyebut apakah seleksi tersisa dari langkah sebelumnya; spec mencentang baris di tiap langkah bulk.
  - TC-GS-UCF-485 Expected a menyebut `Delete` tidak tampil karena aktor Update dan Read tidak memegang capability Delete; spec mengasersi `Delete` tidak tampil pada overlay yang sudah terbuka dan memuat `Deactivate`.
  - Email Pre-setup TC berbeda dari email di komentar `.env.example` untuk `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_FULLCRUD_PASSWORD`, dan `GS_DEFAULT_PASSWORD`; spec memakai email TC dan nama env yang sudah terdaftar (tim FE memastikan satu env untuk satu akun).
  - Dialog `Delete Custom Field` dan bullet dialog tidak punya teks isi di TC (hanya judul dan bullet); spec mengasersi judul dan bullet saja.
