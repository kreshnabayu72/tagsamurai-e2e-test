---
id: TC-GS-UCF-E2E-010-multi-konteks-capability-dicabut-saat-aksi-berjalan
title: "Multi-Konteks: Capability Create, Update, atau Delete Dicabut Saat Popup atau Dialog Terbuka, Aksi Ditolak dan UI Memuat Ulang Kontrol"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-328
  - TC-GS-UCF-340
  - TC-GS-UCF-342
  - TC-GS-UCF-344
  - TC-GS-UCF-349
  - TC-GS-UCF-548
  - TC-GS-UCF-551
coverage:
  web: automated
---

# Multi-Konteks: Capability Create, Update, atau Delete Dicabut Saat Popup atau Dialog Terbuka, Aksi Ditolak dan UI Memuat Ulang Kontrol

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah capability role akun Full CRUD (data Pre-setup bersama) sehingga tidak boleh berjalan paralel dengan spec lain yang memakai akun itu (spec 007 dan 009).
- Dua konteks (kelas multi-konteks/izin) dalam satu spec, ditandai `[Sesi A]` dan `[Sesi B]`:
  - Sesi A (aktor): Manage user and role: Full CRUD (Bayu Saputra) `manageUserFullCrud_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A), `Spectra.env.GS_FULLCRUD_PASSWORD`. Login di hook `before`; layar awal Global Settings > User > Custom Field dibuka hook `beforeEach`.
  - Sesi B (pencabut capability): Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A), `Spectra.env.GS_TC_PASSWORD`. Pelaku kedua ini hanya memicu perubahan state (P-2), sehingga memakai sesi API; langkah pemicunya ditulis "hingga ... tersimpan". Padanan UI yang ditulis TC: Global Settings > Role & Permission > Tab System > `Manage user and role` > Detail, lalu meng-uncheck checkbox kolom `C`, `U`, atau `D` pada baris Bayu Saputra (perubahan capability tersimpan per sel tanpa tombol Save; `role.md` §2.3, §4.8). Mekanisme API pencabutan dan pemulihan capability tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE/BE.
  - Password tidak ditulis di spec atau fixture.
- State global yang diubah: capability Create, Update, dan Delete pada role akun Full CRUD (data Pre-setup bersama, Tabel Data Uji Pre-setup) dicabut satu per satu dan dipulihkan sesudah tiap TC oleh langkah eksplisit (Post Condition TC); capability Read tetap. Hook `before` mencatat nilai awal capability akun itu (C, R, U, D) dan hook `after` memulihkannya walau spec gagal di tengah, serta menutup sesi API Sesi B dan mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Selama capability dicabut, akun Full CRUD tidak dapat menjalankan aksi terkait.
- Data Dinamis (bersuffix `{runId}-010`, milik spec ini; fixture baru `Fixture.customFieldUser.revoke010`). Seed lewat API di hook `before`, semua Text dan bebas nilai User:
  - D-117: `Revoke Edit {runId}-010` (Placeholder kosong; nilai efektif `Enter revoke edit {runId}-010`).
  - D-119: `Revoke Del {runId}-010`.
  - D-123: `Revoke Bulk A {runId}-010` dan D-124: `Revoke Bulk B {runId}-010` (Active).
  - D-132: `Revoke Toggle {runId}-010` (Active).
  - D-251: `Revoke Bulk Del A {runId}-010` dan `Revoke Bulk Del B {runId}-010` (Active).
  - D-252: `Revoke Bulk Act A {runId}-010` dan `Revoke Bulk Act B {runId}-010` (Inactive).
  - Dibuat lewat UI oleh TC-GS-UCF-328: `Revoked Create {runId}-010` (tidak pernah tersimpan; bila server ternyata menerimanya, hook `after` menghapusnya).
- Data Pre-setup: tidak ada yang dipakai langkah selain akun dan capability. Population D-01 tidak di-seed karena tidak ada asersi yang bergantung pada jumlah atau urutannya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua field bersuffix `{runId}-010` yang masih ada; pulihkan capability; tutup Sesi B; kosongkan Search tabel.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun Full CRUD dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: dua sesi paralel (UI untuk Sesi A, API untuk Sesi B); pencabutan dan pemulihan capability oleh Total Control (disediakan tim FE/BE); pengamatan toast, dialog, dan tooltip; muat ulang halaman (F5; tidak ada form terbuka saat dijalankan sehingga tidak ada dialog `beforeunload`).

## Test Steps

### TC-GS-UCF-328: Capability Create dicabut saat popup Create terbuka, Submit ditolak dan UI memuat ulang kontrol

1. [Sesi A] Klik `[+ Custom Field]`
2. [Sesi A] Isi Field Name `Revoked Create {runId}-010`, Data Type `Text`
3. [Sesi B] Cabut capability Create (kolom `C`) dari role Bayu Saputra hingga pencabutan tersimpan
4. [Sesi A] Klik `[Submit]`
5. [Sesi A] Verifikasi muncul toast error: "You don't have permission to do this."
6. [Sesi A] Klik `✕` di header popup
7. [Sesi A] Verifikasi dialog `Unsaved Changes` muncul
8. [Sesi A] Klik `[Leave]`
9. [Sesi A] Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
10. [Sesi A] Verifikasi UI di-refresh: `[+ Custom Field]` tidak lagi tampil
11. [Sesi A] Ketik Search `Revoked Create`, tekan Enter
12. [Sesi A] Verifikasi `Revoked Create {runId}-010` tidak ada di tabel (empty state `No results found`)
13. [Sesi A] Klik `(←)` pada kotak Search
14. [Sesi B] Pulihkan capability Create (kolom `C`) pada role Bayu Saputra hingga pemulihan tersimpan
15. [Sesi A] Muat ulang halaman (F5) agar kontrol sesuai capability yang dipulihkan

### TC-GS-UCF-340: Capability Update dicabut saat popup Edit terbuka, Save ditolak dan UI memuat ulang kontrol

16. [Sesi A] Ketik Search `Revoke Edit`, tekan Enter
17. [Sesi A] Klik `⋯` pada baris `Revoke Edit {runId}-010`, pilih `Edit`
18. [Sesi A] Ubah Placeholder menjadi `Blocked`
19. [Sesi B] Cabut capability Update (kolom `U`) dari role Bayu Saputra hingga pencabutan tersimpan
20. [Sesi A] Klik `[Save]`
21. [Sesi A] Verifikasi muncul toast error: "You don't have permission to do this."
22. [Sesi A] Klik `✕` di header popup
23. [Sesi A] Verifikasi dialog `Unsaved Changes` muncul
24. [Sesi A] Klik `[Leave]`
25. [Sesi A] Klik `⋯` pada baris `Revoke Edit {runId}-010`
26. [Sesi A] Verifikasi menu `⋯` memuat `Delete` (pembanding capability Delete yang tetap aktif)
27. [Sesi A] Verifikasi UI di-refresh: row action `Edit` tidak lagi tampil
28. [Sesi A] Tutup menu `⋯` dengan Esc
29. [Sesi A] Arahkan kursor ke switch Active baris `Revoke Edit {runId}-010`
30. [Sesi A] Verifikasi switch Active Disabled
31. [Sesi A] Verifikasi tooltip `You don't have permission to edit.`
32. [Sesi A] Verifikasi kolom Placeholder baris `Revoke Edit {runId}-010` tetap `Enter revoke edit {runId}-010` (bukan `Blocked`)
33. [Sesi A] Klik `(←)` pada kotak Search
34. [Sesi B] Pulihkan capability Update (kolom `U`) pada role Bayu Saputra hingga pemulihan tersimpan
35. [Sesi A] Muat ulang halaman (F5) agar kontrol sesuai capability yang dipulihkan

### TC-GS-UCF-342: Capability Delete dicabut saat dialog Delete terbuka, Delete ditolak dan UI memuat ulang kontrol

36. [Sesi A] Ketik Search `Revoke Del`, tekan Enter
37. [Sesi A] Klik `⋯` pada baris `Revoke Del {runId}-010`, pilih `Delete`
38. [Sesi B] Cabut capability Delete (kolom `D`) dari role Bayu Saputra hingga pencabutan tersimpan
39. [Sesi A] Klik `[Delete]` pada dialog
40. [Sesi A] Verifikasi muncul toast error: "You don't have permission to do this."
41. [Sesi A] Klik `⋯` pada baris `Revoke Del {runId}-010`
42. [Sesi A] Verifikasi menu `⋯` memuat `Edit` (pembanding capability Update yang tetap aktif)
43. [Sesi A] Verifikasi UI di-refresh: row action `Delete` tidak lagi tampil
44. [Sesi A] Tutup menu `⋯` dengan Esc
45. [Sesi A] Verifikasi `Revoke Del {runId}-010` tetap ada di tabel
46. [Sesi A] Klik `(←)` pada kotak Search
47. [Sesi B] Pulihkan capability Delete (kolom `D`) pada role Bayu Saputra hingga pemulihan tersimpan
48. [Sesi A] Muat ulang halaman (F5) agar kontrol sesuai capability yang dipulihkan

### TC-GS-UCF-344: Capability Update dicabut saat dialog Bulk Deactivate terbuka, aksi ditolak dan opsi bulk dimuat ulang

49. [Sesi A] Ketik Search `Revoke Bulk`, tekan Enter
50. [Sesi A] Centang baris `Revoke Bulk A {runId}-010` dan `Revoke Bulk B {runId}-010`
51. [Sesi A] Klik `Bulk Action`, pilih `Deactivate`
52. [Sesi B] Cabut capability Update (kolom `U`) dari role Bayu Saputra hingga pencabutan tersimpan
53. [Sesi A] Klik `[Deactivate]` pada dialog
54. [Sesi A] Verifikasi muncul toast error: "You don't have permission to do this."
55. [Sesi A] Klik `Bulk Action` pada Bulk Action Bar, perhatikan daftar aksi
56. [Sesi A] Verifikasi `Delete` tampil pada `Bulk Action` (pembanding capability Delete yang tetap aktif)
57. [Sesi A] Verifikasi UI di-refresh: `Activate` dan `Deactivate` tidak lagi tersedia pada `Bulk Action`
58. [Sesi A] Tutup overlay `Bulk Action` dengan Esc dan hapus centang kedua baris
59. [Sesi A] Verifikasi switch Active baris `Revoke Bulk A {runId}-010` tetap On
60. [Sesi A] Verifikasi switch Active baris `Revoke Bulk B {runId}-010` tetap On
61. [Sesi A] Klik `(←)` pada kotak Search
62. [Sesi B] Pulihkan capability Update (kolom `U`) pada role Bayu Saputra hingga pemulihan tersimpan
63. [Sesi A] Muat ulang halaman (F5) agar kontrol sesuai capability yang dipulihkan

### TC-GS-UCF-349: Capability Update dicabut saat dialog Deactivate terbuka, aksi ditolak dan switch menjadi Disabled

64. [Sesi A] Ketik Search `Revoke Toggle`, tekan Enter
65. [Sesi A] Matikan switch Active baris `Revoke Toggle {runId}-010`
66. [Sesi B] Cabut capability Update (kolom `U`) dari role Bayu Saputra hingga pencabutan tersimpan
67. [Sesi A] Klik `[Deactivate]` pada dialog
68. [Sesi A] Verifikasi muncul toast error: "You don't have permission to do this."
69. [Sesi A] Arahkan kursor ke switch Active baris `Revoke Toggle {runId}-010`
70. [Sesi A] Verifikasi UI di-refresh: switch Active Disabled
71. [Sesi A] Verifikasi tooltip `You don't have permission to edit.`
72. [Sesi A] Verifikasi `Revoke Toggle {runId}-010` tetap Active (switch On)
73. [Sesi A] Klik `(←)` pada kotak Search
74. [Sesi B] Pulihkan capability Update (kolom `U`) pada role Bayu Saputra hingga pemulihan tersimpan
75. [Sesi A] Muat ulang halaman (F5) agar kontrol sesuai capability yang dipulihkan

### TC-GS-UCF-548: Capability Delete dicabut saat dialog Bulk Delete terbuka, aksi ditolak dan opsi bulk dimuat ulang

76. [Sesi A] Ketik Search `Revoke Bulk Del`, tekan Enter
77. [Sesi A] Centang baris `Revoke Bulk Del A {runId}-010` dan `Revoke Bulk Del B {runId}-010`
78. [Sesi A] Klik `Bulk Action`, pilih `Delete`
79. [Sesi B] Cabut capability Delete (kolom `D`) dari role Bayu Saputra hingga pencabutan tersimpan
80. [Sesi A] Klik `[Delete]` pada dialog
81. [Sesi A] Verifikasi muncul toast error: "You don't have permission to do this."
82. [Sesi A] Klik `Bulk Action` pada Bulk Action Bar, perhatikan daftar aksi
83. [Sesi A] Verifikasi `Deactivate` tetap tersedia pada `Bulk Action` karena capability Update tetap aktif
84. [Sesi A] Verifikasi UI di-refresh: `Delete` tidak lagi tersedia pada `Bulk Action`
85. [Sesi A] Tutup overlay `Bulk Action` dengan Esc dan hapus centang kedua baris
86. [Sesi A] Verifikasi `Revoke Bulk Del A {runId}-010` tetap ada di tabel
87. [Sesi A] Verifikasi `Revoke Bulk Del B {runId}-010` tetap ada di tabel
88. [Sesi A] Klik `(←)` pada kotak Search
89. [Sesi B] Pulihkan capability Delete (kolom `D`) pada role Bayu Saputra hingga pemulihan tersimpan
90. [Sesi A] Muat ulang halaman (F5) agar kontrol sesuai capability yang dipulihkan

### TC-GS-UCF-551: Capability Update dicabut saat dialog Bulk Activate terbuka, aksi ditolak dan opsi bulk dimuat ulang

91. [Sesi A] Ketik Search `Revoke Bulk Act`, tekan Enter
92. [Sesi A] Centang baris `Revoke Bulk Act A {runId}-010` dan `Revoke Bulk Act B {runId}-010`
93. [Sesi A] Klik `Bulk Action`, pilih `Activate`
94. [Sesi B] Cabut capability Update (kolom `U`) dari role Bayu Saputra hingga pencabutan tersimpan
95. [Sesi A] Klik `[Activate]` pada dialog
96. [Sesi A] Verifikasi muncul toast error: "You don't have permission to do this."
97. [Sesi A] Klik `Bulk Action` pada Bulk Action Bar, perhatikan daftar aksi
98. [Sesi A] Verifikasi `Delete` tetap tersedia pada `Bulk Action` karena capability Delete tetap aktif
99. [Sesi A] Verifikasi UI di-refresh: `Activate` tidak lagi tersedia pada `Bulk Action`
100. [Sesi A] Tutup overlay `Bulk Action` dengan Esc dan hapus centang kedua baris
101. [Sesi A] Verifikasi switch Active baris `Revoke Bulk Act A {runId}-010` tetap Off
102. [Sesi A] Verifikasi switch Active baris `Revoke Bulk Act B {runId}-010` tetap Off
103. [Sesi A] Klik `(←)` pada kotak Search
104. [Sesi B] Pulihkan capability Update (kolom `U`) pada role Bayu Saputra hingga pemulihan tersimpan
105. [Sesi A] Muat ulang halaman (F5) agar kontrol sesuai capability yang dipulihkan

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Kelas harness: multi-konteks/izin (dua sesi, capability role diubah), serial.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- P-2 (bagian 3 konvensi): Sesi B (Total Control) hanya memicu pencabutan capability (pemicu, bukan objek asersi), sehingga memakai sesi API; seluruh asersi berada di Sesi A. Pencabutan capability di tengah aksi adalah objek uji kelas ini, bukan pemicu terpisah.
- Urutan TC mengikuti daftar sumber (328, 340, 342, 344, 349, 548, 551); tiap TC mencabut satu capability lalu memulihkannya dengan langkah penghubung (Post Condition TC) dan memuat ulang halaman supaya kontrol Sesi A kembali sesuai capability sebelum TC berikutnya.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target, `(←)` untuk mengosongkan Search, pemulihan capability oleh Sesi B beserta F5 Sesi A, `✕` dan `[Leave]` pada popup dirty (didahului `Verifikasi` dialog `Unsaved Changes`, S-08), dan menutup overlay `Bulk Action` lalu menghapus centang.
- Toast diasersi segera sesudah `[Submit]`, `[Save]`, atau aksi dialog (sebelum langkah berikutnya, butir 5 bagian 8b). Asersi "tidak lagi tampil" pada `[+ Custom Field]` dan row action beranchor Table Tools tampil, menu `⋯` yang memuat aksi pembanding (capability yang tetap aktif), serta `Bulk Action` yang memuat aksi pembanding (bagian 8b butir 2 dan 11).
- Spec melewati sekitar 35 langkah (105 langkah). Seluruhnya satu kelas (multi-konteks: capability dicabut saat aksi berjalan) dengan data seed milik spec; tiap blok TC berdiri sendiri (capability dipulihkan dan halaman dimuat ulang di antara blok) sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Penolakan permission memakai toast `You don't have permission to do this.` (keputusan NC-18, global) yang berbeda dari toast gagal baku aksi PRD awal; selisih terhadap API/LLD dilacak di `nc-followups.md`. Asersi mengikuti TC dan bisa gagal pada backend nyata sampai API/LLD diselaraskan.
- Temuan untuk QA:
  - TC-GS-UCF-328, 340, 342, 344, 349, 548, dan 551 menyebut sesi kedua Sari Dewi mencabut capability lewat UI Role & Permission; spec memakai sesi API untuk pelaku kedua yang hanya memicu (P-2) dan menaruh padanan UI di Prerequisites. Menunggu konfirmasi QA bila sesi UI kedua dibutuhkan.
  - Post Condition ketujuh TC ("capability dipulihkan Sari Dewi") tidak punya langkah observasi dan tidak diasersi; pemulihan dilakukan langkah penghubung dan hook `after`.
  - TC-GS-UCF-328 tidak mendefinisikan state popup Create setelah toast error 403 (tetap terbuka atau tertutup); spec menutup popup lewat `✕`, `Verifikasi` dialog `Unsaved Changes`, dan `[Leave]`, sehingga langkah itu gagal bila popup tertutup sendiri. TC-GS-UCF-340 serupa untuk popup Edit.
  - TC-GS-UCF-342, 344, 349, 548, dan 551 tidak mendefinisikan state dialog konfirmasi sesudah toast error; spec mengasumsikan dialog tertutup sesudah UI di-refresh (sejalan dengan langkah 5 TC-GS-UCF-548 dan 551 yang langsung mengklik `Bulk Action`). Menunggu jawaban QA.
  - TC-GS-UCF-344 tidak punya langkah mengamati daftar aksi `Bulk Action` meskipun Expected b memintanya (TC-GS-UCF-548 dan 551 punya); spec menambah langkah itu berdasar Expected b. TC-GS-UCF-344, 548, dan 551 juga mengandaikan seleksi baris dan Bulk Action Bar bertahan sesudah UI di-refresh tanpa menyebutnya; spec mengikuti TC (klik `Bulk Action` pada Bulk Action Bar) dan langkah itu gagal bila seleksi terhapus.
  - TC-GS-UCF-340 Expected c menyebut Placeholder `Enter revoke edit`; spec memakai nilai efektif bersuffix `Enter revoke edit {runId}-010` karena nama field bersuffix.
  - TC-GS-UCF-340 Expected b menyebut `Edit` tidak lagi tampil dan switch Disabled tanpa langkah observasi; spec mengamati lewat klik `⋯` dan hover switch.
  - TC-GS-UCF-328 Expected c ("`Revoked Create` tidak ada di tabel") tidak menyebut cara memeriksa; spec memakai Search dengan empty state `No results found` sebagai anchor.
