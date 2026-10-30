---
id: TC-GS-UCF-E2E-038-multi-konteks-edit-bersamaan-dan-form-stale
title: "Multi-Konteks: Edit Bersamaan Last-Write-Wins, Form Edit Stale (Decimal Places, Data Type, Value Dropdown), Field Dihapus atau Dinonaktifkan Admin Lain di Tengah Edit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-102
  - TC-GS-UCF-540
  - TC-GS-UCF-375
  - TC-GS-UCF-388
  - TC-GS-UCF-368
  - TC-GS-UCF-316
  - TC-GS-UCF-381
  - TC-GS-UCF-321
  - TC-GS-UCF-317
coverage:
  web: automated
---

# Multi-Konteks: Edit Bersamaan Last-Write-Wins, Form Edit Stale (Decimal Places, Data Type, Value Dropdown), Field Dihapus atau Dinonaktifkan Admin Lain di Tengah Edit

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun (password hanya lewat env var, tidak ditulis di spec atau fixture):
  - Sesi A (Admin A): Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`. Konteks browser utama.
  - Sesi B (Admin B): Total Control Client A admin kedua (Nadia Pratama, Modified By `Nadia P`) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`. Sesi B memakai konteks browser kedua (UI) hanya pada TC-GS-UCF-316 dan 381 yang mengasersi hasil Save Admin B. Pada TC lain Admin B hanya memicu perubahan state (pengisian nilai User, penghapusan value Dropdown, Deactivate, Delete) lewat sesi API "disediakan tim FE/BE" (P-2); langkah pemicu ditulis "hingga ... tersimpan".
  - Sesi A dan Sesi B login di hook `before` pada Global Settings > User > Custom Field; hook `after` menutup konteks Sesi B dan mengembalikan sesi ke akun default suite.
- Layar awal Global Settings > User > Custom Field (kedua sesi) dibuka hook `beforeEach`; hook `beforeEach` menutup dialog atau popup yang masih terbuka di kedua sesi.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk kedua akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Akun Login User Client A `rahmatHidayat_automated_qaTeam1@qwertysystem.net` (Rahmat Hidayat) sebagai pemilik nilai Custom Field yang diisi Admin B dan dibaca pada Detail User (tidak dipakai login).
- Data Dinamis milik spec (seeding lewat API di hook `before`, bersuffix `{runId}-038`; fixture baru `Fixture.customFieldUser.concurrent038`; Active, Required No, Placeholder kosong; sembilan field sehingga Search `{runId}-038` muat satu halaman dengan ukuran halaman default 10; nilai User di-seed lewat mekanisme yang disediakan tim FE/BE):
  - `Dec Stale {runId}-038`: Numeric, Decimal Places 1, belum bernilai saat popup dibuka (TC-GS-UCF-102).
  - `Dec Stale Clean {runId}-038`: Numeric, Decimal Places 1, belum bernilai saat popup dibuka (TC-GS-UCF-540).
  - `Snap Field {runId}-038`: Text, belum bernilai (TC-GS-UCF-375).
  - `Snap Used DD {runId}-038`: Dropdown `Alpha`, `Beta`, belum bernilai (TC-GS-UCF-388).
  - `Stale Opt DD {runId}-038`: Dropdown `Alpha`, `Beta`, `Gamma`, bebas nilai User (TC-GS-UCF-368).
  - `Concurrent Edit {runId}-038`: Text (TC-GS-UCF-316).
  - `Conc Rename DD {runId}-038`: Dropdown `Alpha`, `Beta`, nilai User Rahmat Hidayat = `Alpha` (TC-GS-UCF-381).
  - `Race DT {runId}-038`: Dropdown `p`, `q`, nilai User Rahmat Hidayat = `p` (TC-GS-UCF-321).
  - `Gone While Editing {runId}-038`: Text (TC-GS-UCF-317; dihapus Admin B).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-038` yang masih ada; tutup konteks Sesi B.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; sesi API Admin B untuk mengisi nilai User, menghapus value Dropdown, Deactivate, dan Delete (mekanisme tidak didefinisikan di TC, PRD, atau LLD, disediakan tim FE/BE); membaca Changelog Custom Field (Search); langkah dijalankan berurutan dengan penanda `[Sesi A]`, `[Sesi B]`, dan `[Pemicu Admin B]`.
- State global yang diubah: tidak ada selain Custom Field dan nilai User milik spec.

## Test Steps

### Persiapan

1. [Sesi A] Ketik Search `{runId}-038`, tekan Enter
2. [Sesi B] Ketik Search `{runId}-038`, tekan Enter

### TC-GS-UCF-102: Decimal Places diubah pada form stale setelah field mendapat nilai User

3. [Sesi A] Klik `⋯` pada baris `Dec Stale {runId}-038`, pilih `Edit`
4. [Pemicu Admin B] Isi nilai `3.5` pada `Dec Stale {runId}-038` untuk Rahmat Hidayat lewat Edit User hingga tersimpan
5. [Sesi A] Ubah Placeholder menjadi `Keep`, pilih Decimal Places `2`, klik `[Save]`
6. [Sesi A] Verifikasi dialog `Decimal Places Locked`: `This field's decimal places is locked because it's already used by users. Delete this field and create a new one to change it.` dengan tombol `[OK]`
7. [Sesi A] Verifikasi tidak ada toast gagal "Error, failed to update custom field."
8. [Sesi A] Klik `[OK]`
9. [Sesi A] Verifikasi hanya Decimal Places yang dimuat ulang ke nilai tersimpan `1`
10. [Sesi A] Verifikasi Placeholder `Keep` dipertahankan
11. [Sesi A] Verifikasi popup tetap terbuka
12. [Sesi A] Klik `[✕]`
13. [Sesi A] Verifikasi dialog `Unsaved Changes` tampil (form tetap dirty)
14. [Sesi A] Klik `[Leave]`
15. [Sesi A] Verifikasi perubahan tidak tersimpan (Value Setting baris `Dec Stale {runId}-038` tetap `1 Decimal Place`)

### TC-GS-UCF-540: Decimal Places diubah pada form stale sebagai satu-satunya perubahan, form kembali bersih

16. [Sesi A] Klik `⋯` pada baris `Dec Stale Clean {runId}-038`, pilih `Edit`
17. [Pemicu Admin B] Isi nilai `3.5` pada `Dec Stale Clean {runId}-038` untuk Rahmat Hidayat lewat Edit User hingga tersimpan
18. [Sesi A] Pilih Decimal Places `2` tanpa mengubah field lain, klik `[Save]`
19. [Sesi A] Verifikasi dialog `Decimal Places Locked`: `This field's decimal places is locked because it's already used by users. Delete this field and create a new one to change it.` dengan tombol `[OK]`
20. [Sesi A] Verifikasi tidak ada toast gagal "Error, failed to update custom field."
21. [Sesi A] Klik `[OK]`
22. [Sesi A] Verifikasi nilai Decimal Places dimuat ulang ke nilai tersimpan `1`
23. [Sesi A] Verifikasi popup tetap terbuka
24. [Sesi A] Klik `[✕]`
25. [Sesi A] Verifikasi popup tertutup langsung tanpa dialog `Unsaved Changes` (Decimal Places satu-satunya perubahan, form kembali bersih)
26. [Sesi A] Ganti isi kotak search dengan `Dec Stale Clean {runId}-038`, tekan Enter
27. [Sesi A] Verifikasi kolom Value Setting baris `Dec Stale Clean {runId}-038` menampilkan `1 Decimal Place`
28. [Sesi A] Ganti isi kotak search dengan `{runId}-038`, tekan Enter

### TC-GS-UCF-375: Save Data Type pada form yang dibuka sebelum field mendapat nilai User ditolak server dan dialog Change Data Type ditampilkan ulang

29. [Sesi A] Klik `⋯` pada baris `Snap Field {runId}-038`, pilih `Edit`
30. [Pemicu Admin B] Isi nilai `X1` pada `Snap Field {runId}-038` untuk Rahmat Hidayat lewat Edit User hingga tersimpan
31. [Sesi A] Ubah Data Type menjadi `Numeric`, klik `[Save]`
32. [Sesi A] Verifikasi dialog `Change Data Type` dengan bullet `Snap Field {runId}-038` tampil walau saat form dibuka field belum bernilai
33. [Sesi A] Verifikasi belum ada perubahan tersimpan (baris `Snap Field {runId}-038` di belakang dialog tetap `Text`)
34. [Sesi A] Klik `[Cancel]` pada dialog
35. [Sesi A] Verifikasi popup tetap terbuka dengan Data Type `Numeric`
36. [Sesi A] Klik `[Save]` lagi, klik `[Change Data Type]`
37. [Sesi A] Verifikasi toast sukses: "Success, custom field has been updated."
38. [Sesi A] Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
39. [Sesi A] Verifikasi nilai `Snap Field {runId}-038` pada Detail User Rahmat Hidayat kosong
40. [Sesi A] Buka Global Settings > User > Custom Field, klik icon Changelog, Search `Snap Field {runId}-038`
41. [Sesi A] Verifikasi Changelog memuat entri Edit `Snap Field {runId}-038 — Data Type` dengan Old Value `Text` dan New Value `Numeric` (Modified By `Sari D`)
42. [Sesi A] Verifikasi Changelog memuat entri Edit `Snap Field {runId}-038 — Value Setting` dengan Old Value `-` dan New Value `0 Decimal Places` (Modified By `Sari D`)
43. [Sesi A] Verifikasi Changelog memuat tepat dua entri Edit dari aksi ini
44. [Sesi A] Tutup Modal Changelog, ketik Search `{runId}-038`, tekan Enter

### TC-GS-UCF-388: Dialog Remove Value ditampilkan ulang setelah penolakan 409, Remove mengulang Save dan Cancel mempertahankan form

45. [Sesi A] Klik `⋯` pada baris `Snap Used DD {runId}-038`, pilih `Edit`
46. [Pemicu Admin B] Isi nilai `Alpha` pada `Snap Used DD {runId}-038` untuk Rahmat Hidayat lewat Edit User hingga tersimpan
47. [Sesi A] Klik `×` pada badge `Alpha`
48. [Sesi A] Verifikasi badge `Alpha` hilang tanpa dialog (saat form dibuka belum dipakai)
49. [Sesi A] Klik `[Save]`
50. [Sesi A] Verifikasi dialog `Remove Value` dengan bullet `Alpha` dan `Used by 1 user(s). Removing it will clear this value from their profile — they'll need to select a new one. This will take effect when you save.` tampil
51. [Sesi A] Verifikasi belum ada perubahan tersimpan
52. [Sesi A] Klik `[Cancel]` pada dialog
53. [Sesi A] Verifikasi dialog tertutup tanpa Save
54. [Sesi A] Verifikasi popup tetap terbuka
55. [Sesi A] Verifikasi badge `Alpha` tetap terhapus dari form
56. [Sesi A] Klik `[Save]` lagi
57. [Sesi A] Verifikasi dialog `Remove Value` yang sama tampil
58. [Sesi A] Klik `[Remove]`
59. [Sesi A] Verifikasi toast sukses: "Success, custom field has been updated."
60. [Sesi A] Verifikasi Value Setting baris `Snap Used DD {runId}-038` `Beta`
61. [Sesi A] Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
62. [Sesi A] Verifikasi nilai `Snap Used DD {runId}-038` pada Detail User Rahmat Hidayat kosong
63. [Sesi A] Buka Global Settings > User > Custom Field, klik icon Changelog, Search `Snap Used DD {runId}-038`
64. [Sesi A] Verifikasi Changelog memuat tepat satu entri Edit dari aksi ini (Modified By `Sari D`)
65. [Sesi A] Verifikasi entri Edit itu berfield `Snap Used DD {runId}-038 — Value Setting` dengan Old Value `Alpha, Beta` dan New Value `Beta`
66. [Sesi A] Tutup Modal Changelog, ketik Search `{runId}-038`, tekan Enter

### TC-GS-UCF-368: Save ditolak saat value Dropdown yang diubah sudah dihapus admin lain

67. [Sesi A] Klik `⋯` pada baris `Stale Opt DD {runId}-038`, pilih `Edit`
68. [Pemicu Admin B] Hapus badge `Beta` pada `Stale Opt DD {runId}-038` lalu simpan hingga tersimpan
69. [Sesi A] Klik teks badge `Beta`, ubah menjadi `Delta`, klik `[Save]`
70. [Sesi A] Verifikasi error inline pada Dropdown Values `Beta no longer exists. Please select another.`
71. [Sesi A] Verifikasi tidak ada toast sukses
72. [Sesi A] Verifikasi badge stale hilang dari form
73. [Sesi A] Verifikasi badge `Alpha` dan `Gamma` tetap ada
74. [Sesi A] Klik `[✕]`
75. [Sesi A] Verifikasi dialog `Unsaved Changes` (warning) tampil dengan `[Cancel]` dan `[Leave]` (popup tetap terbuka dan form tetap dirty)
76. [Sesi A] Klik `[Leave]`
77. [Sesi A] Verifikasi popup tertutup
78. [Sesi A] Buka Changelog Custom Field, Search `Stale Opt DD {runId}-038`
79. [Sesi A] Verifikasi Changelog memuat entri Edit `Stale Opt DD {runId}-038 — Value Setting` dari admin kedua (Modified By `Nadia P`)
80. [Sesi A] Verifikasi Changelog tidak memuat entri Edit dari Admin A (Modified By `Sari D`) pada field ini (anchor: entri `Nadia P` di atas tampil pada Modal Changelog yang sama)
81. [Sesi A] Tutup Modal Changelog

### TC-GS-UCF-316: Edit bersamaan oleh dua admin pada record yang sama, last-write-wins

82. [Sesi A] Klik `⋯` pada baris `Concurrent Edit {runId}-038`, pilih `Edit`
83. [Sesi B] Klik `⋯` pada baris `Concurrent Edit {runId}-038`, pilih `Edit`
84. [Sesi A] Ubah Placeholder menjadi `A`, klik `[Save]`
85. [Sesi A] Verifikasi toast sukses: "Success, custom field has been updated."
86. [Sesi A] Verifikasi tidak ada dialog konflik versi
87. [Sesi B] Ubah Placeholder menjadi `B`, klik `[Save]`
88. [Sesi B] Verifikasi toast sukses: "Success, custom field has been updated."
89. [Sesi B] Verifikasi tidak ada dialog konflik versi
90. [Sesi A] Muat ulang halaman (F5)
91. [Sesi A] Verifikasi Placeholder baris `Concurrent Edit {runId}-038` `B` (nilai akhir setelah muat ulang)

### TC-GS-UCF-381: Rename value Dropdown yang sama oleh dua admin mengikuti last-write-wins

92. [Sesi A] Klik `⋯` pada baris `Conc Rename DD {runId}-038`, pilih `Edit`
93. [Sesi A] Ubah badge `Alpha` menjadi `Delta`, tekan Enter (belum Save)
94. [Sesi B] Klik `⋯` pada baris `Conc Rename DD {runId}-038`, pilih `Edit`
95. [Sesi B] Ubah badge `Alpha` menjadi `Gamma`, klik `[Save]`
96. [Sesi B] Verifikasi toast sukses: "Success, custom field has been updated."
97. [Sesi A] Klik `[Save]`
98. [Sesi A] Verifikasi toast sukses: "Success, custom field has been updated."
99. [Sesi A] Verifikasi tidak ada dialog konflik versi
100. [Sesi A] Verifikasi tidak ada error stale
101. [Sesi A] Verifikasi Value Setting baris `Conc Rename DD {runId}-038` menampilkan `Delta`, `Beta` (label terakhir disimpan)
102. [Sesi A] Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
103. [Sesi A] Verifikasi Detail User Rahmat Hidayat menampilkan `Conc Rename DD {runId}-038` dengan nilai `Delta`
104. [Sesi A] Buka Global Settings > User > Custom Field, ketik Search `{runId}-038`, tekan Enter

### TC-GS-UCF-321: Edit Data Type berbalapan dengan Deactivate pada field yang sama

105. [Sesi A] Klik `⋯` pada baris `Race DT {runId}-038`, pilih `Edit`
106. [Sesi A] Ubah Data Type menjadi `Text`
107. [Pemicu Admin B] Nonaktifkan `Race DT {runId}-038` hingga tersimpan
108. [Sesi A] Klik `[Save]`, lalu klik `[Change Data Type]`
109. [Sesi A] Verifikasi Data Type baris `Race DT {runId}-038` `Text`
110. [Sesi A] Verifikasi baris `Race DT {runId}-038` berstatus Inactive
111. [Sesi A] Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
112. [Sesi A] Verifikasi nilai `Race DT {runId}-038` pada Detail User Rahmat Hidayat kosong
113. [Sesi A] Buka Global Settings > User > Custom Field, klik icon Changelog, Search `Race DT {runId}-038`
114. [Sesi A] Verifikasi Changelog memuat entri Deactivate untuk `Race DT {runId}-038`
115. [Sesi A] Verifikasi Changelog memuat entri Edit Data Type untuk `Race DT {runId}-038`
116. [Sesi A] Tutup Modal Changelog, ketik Search `{runId}-038`, tekan Enter

### TC-GS-UCF-317: Edit pada field yang sudah dihapus admin lain

117. [Sesi A] Klik `⋯` pada baris `Gone While Editing {runId}-038`, pilih `Edit`
118. [Pemicu Admin B] Hapus `Gone While Editing {runId}-038` hingga tersimpan
119. [Sesi A] Ubah Placeholder dan klik `[Save]`
120. [Sesi A] Verifikasi toast netral: "This custom field is no longer available."
121. [Sesi A] Verifikasi popup tertutup
122. [Sesi A] Verifikasi list di-refresh dan baris `Concurrent Edit {runId}-038` tampil sebagai pembanding
123. [Sesi A] Verifikasi baris `Gone While Editing {runId}-038` tidak ada di list
124. [Sesi A] Buka Changelog Custom Field, Search `Gone While Editing {runId}-038`
125. [Sesi A] Verifikasi Changelog memuat entri Delete oleh `Nadia P` (anchor)
126. [Sesi A] Verifikasi Changelog tidak memuat entri Edit untuk `Gone While Editing {runId}-038`
127. [Sesi A] Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Kelas harness: multi-konteks (dua admin pada entitas yang sama), bagian 3 prinsip 13c. Spec serial.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 127 langkah (di atas smell sekitar 35 langkah): seluruhnya satu kelas harness (dua admin pada entitas yang sama) dan satu topik (form Edit yang dibuka saat admin lain mengubah state), tiap blok memakai field seed bersuffix sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; jumlah langkah muncul dari satu baris per aksi per sesi dan satu `Verifikasi` per klausa Expected.
- Urutan TC: form stale yang tidak menghapus data (TC-GS-UCF-102, 540, 375, 388, 368), edit bersamaan (TC-GS-UCF-316, 381), TC-GS-UCF-321 (Deactivate), dan TC-GS-UCF-317 (field dihapus) paling akhir (prinsip 5). Urutan berbeda dari TC sumber.
- P-2: Admin B hanya memicu perubahan state pada TC-GS-UCF-102, 540, 375, 388, 368, 321, dan 317, sehingga memakai sesi API (langkah `[Pemicu Admin B]`, mekanisme disediakan tim FE/BE). Sesi UI Admin B dipakai pada TC-GS-UCF-316 dan 381 karena hasil Save Admin B diasersi.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search `{runId}-038` pada kedua sesi dan Search ulang setelah berpindah ke Detail User atau Changelog, membuka dan menutup Modal Changelog, kembali ke tab Custom Field dari Detail User, muat ulang halaman (F5) sebelum asersi nilai akhir TC-GS-UCF-316, serta langkah `[Pemicu Admin B]`. Menutup popup dirty ditulis `✕`, `Verifikasi` dialog `Unsaved Changes`, lalu `[Leave]` (S-08).
- P-1 (state berat): asersi tidak-ada-entri-log TC-GS-UCF-368 (langkah 80) dan TC-GS-UCF-317 (langkah 126) tetap di spec ini, bukan di spec absence 070, karena konteksnya bergantung pada state yang dibangun langkah sebelumnya: pelaku kedua (Admin B) mengubah record (TC-GS-UCF-368, value Dropdown dihapus) atau menghapusnya (TC-GS-UCF-317) di antara pembukaan form atau dialog dan konfirmasi Save Admin A. Admin A memicu aksi Save sungguhan di spec ini dengan baseline dan anchor positif sendiri; state itu tidak murah dibentuk ulang di spec 070.
- Pada TC-GS-UCF-317 `Verifikasi` baris `Concurrent Edit {runId}-038` tampil adalah pembanding list yang sudah di-refresh dan, bersama toast netral, menjadi anchor positif bagi asersi absence baris `Gone While Editing {runId}-038`. Asersi "tidak ada entri log" TC-GS-UCF-317 memakai anchor entri Delete dari Admin B dan nama field bersuffix unik (S-12), bukan asersi absence kelas g (aksi Save Admin A ada di spec ini; butir `P-1` untuk state berat yang dibangun langkah sebelumnya).
- Pembagian TC lintas spec: TC-GS-UCF-317 dan TC-GS-UCF-321 berpasangan dengan TC-GS-UCF-318 (Delete) dan 322 di spec 047 serta TC-GS-UCF-319 dan 320 di spec 048; TC-GS-UCF-323 dan 324 (Create bersamaan) ada di spec 029.
- Temuan untuk QA:
  - Semua TC multi-konteks spec ini bertanda Manual Only (d) di kolom Automation; kebutuhannya (dua konteks browser dan sesi API Admin B) ditulis di Prerequisites sesuai konvensi bagian 2.
  - TC-GS-UCF-102, 540, 375, 388: cara Admin B "mengisi nilai ... lewat Edit User" tidak didefinisikan di TC (endpoint atau alur UI); disediakan tim FE/BE. TC mengisi nilai lewat Edit User UI; spec memakai sesi API karena Admin B hanya pemicu (P-2).
  - TC-GS-UCF-102: Expected b dan c ("perubahan tidak tersimpan", "form tetap dirty") diasersi lewat Value Setting tabel dan dialog `Unsaved Changes`; TC tidak memberi langkah observasi lain.
  - TC-GS-UCF-316 dan 381: asersi "tanpa dialog konflik versi" mengikuti keputusan NC-13 (last-write-wins, FE tidak mengirim `updatedAt`); LLD menetapkan `409` bila `updatedAt` berbeda, sehingga backend nyata dapat gagal sampai LLD diselaraskan.
  - TC-GS-UCF-317: keputusan NC-17 (toast netral untuk Edit pada field yang sudah dihapus) berbeda dari API/LLD; asersi mengikuti TC dan backend nyata dapat gagal sampai LLD diselaraskan. Expected c "Tidak ada entri log" diasersi dengan anchor entri Delete dan tanpa entri Edit; TC tidak menyebut aktor yang dimaksud.
  - TC-GS-UCF-321: Expected tidak menyebut toast Save Admin A; spec mengasersi hasil lewat tabel, Detail User, dan Changelog sesuai Expected a dan b.
  - TC-GS-UCF-368: Expected d "tidak memuat entri dari Admin A" diasersi dengan anchor entri `Nadia P`; akun yang membuat seed lewat API bisa memengaruhi kolom Modified By entri Create, tetapi asersi dibatasi pada entri Edit.
  - Keputusan NC-19 (dialog `Decimal Places Locked` untuk 409) dan NC-21 (dialog `Change Data Type` berdasarkan nilai saat ini) berbeda dari API/LLD; asersi mengikuti TC dan backend nyata dapat gagal sampai LLD diselaraskan.
