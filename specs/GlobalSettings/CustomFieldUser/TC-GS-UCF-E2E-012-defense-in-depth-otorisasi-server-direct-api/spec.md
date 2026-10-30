---
id: TC-GS-UCF-E2E-012-defense-in-depth-otorisasi-server-direct-api
title: "Defense-in-Depth Otorisasi Server: Request Langsung Tanpa Capability Ditolak 403 dan id Custom Field Milik Entitas Lain Diperlakukan Tidak Ditemukan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-304
  - TC-GS-UCF-305
  - TC-GS-UCF-306
  - TC-GS-UCF-557
  - TC-GS-UCF-558
  - TC-GS-UCF-559
  - TC-GS-UCF-563
coverage:
  web: automated
---

# Defense-in-Depth Otorisasi Server: Request Langsung Tanpa Capability Ditolak 403 dan id Custom Field Milik Entitas Lain Diperlakukan Tidak Ditemukan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Kelas a (defense-in-depth): request dikirim langsung ke server lewat console browser dan asersi hanya respons server dan state data; perilaku FE (toast, redirect) untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1). Pembacaan tabel, Detail user, dan Changelog sesudah request adalah observasi state data sesuai langkah TC.
- Akun aktor (urutan pemakaian dalam spec; password tidak ditulis di spec atau fixture):

| TC | Akun | Email (Pre-setup) | Env var password |
|---|---|---|---|
| TC-GS-UCF-304 | Read Only (Maya Putri) | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-UCF-305 | Manage user and role: Delete dan Read (Dewi Lestari) | `manageUserDelete_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DELETE_PASSWORD` |
| TC-GS-UCF-306 | Manage user and role: Update dan Read (Agus Wijaya) | `manageUserUpdate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-UCF-563 (request) | Import data: Create dan Read (Rina Marlina, Modified By `Rina M`; hanya capability Import data C dan R, tanpa Manage user and role) | `importCreate_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_IMPORTCREATE_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`) |
| TC-GS-UCF-563 (pengamatan), 557, 558, 559 | Total Control Client A (Sari Dewi, Modified By `Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-UCF-557, 558, 559 (pengamatan Client B dan seed `Client B Iso Probe`) | Total Control Client B (Lina Kusuma, Modified By `Lina K`) | `totalControl_automated_qaTeam2@qwertysystem.net` | `Spectra.env.GS_CLIENTB_TC_PASSWORD` |

  Akun Read Only login di hook `before`; akun lain login lewat langkah ganti akun eksplisit. Blok TC-GS-UCF-563 berpindah dari Rina Marlina ke Total Control Client A, dan blok TC-GS-UCF-557 melanjutkan sesi itu. Hook `after` mengembalikan sesi ke akun Total Control default suite.
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > Custom Field untuk akun hook `before`; setelah ganti akun, tab dibuka oleh langkah spec.
- Data Dinamis (bersuffix `{runId}-012`; fixture baru `Fixture.customFieldUser.authz012`). Seed lewat API di hook `before`:
  - Client A: `Auth Probe {runId}-012` (Text, Active, Required No, Placeholder `Select auth probe`), dipakai sebagai target request TC-GS-UCF-305 dan 306. Spec ini tidak memakai `Cost Center` Pre-setup sebagai target request langsung (S-06: request langsung yang diuji ditolak memakai data milik spec). Nilai User `Probe Value` untuk Rahmat Hidayat (`rahmatHidayat_automated_qaTeam1@qwertysystem.net`, Pre-setup) pada field ini dipakai TC-GS-UCF-306 (mekanisme mengisi nilai User disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD).
  - Client A: `Cost Center Probe {runId}-012` (Dropdown `Finance`, `Operations`, `Marketing`; Placeholder `Select cost center`; Active; Required No), dipakai sebagai target request TC-GS-UCF-563 (padanan `Cost Center` Pre-setup di TC, S-06); id dicatat sebagai `{id Cost Center Probe}` dari respons seeding. Seeding menghasilkan satu entri Create di Changelog yang menjadi anchor positif asersi absence TC-GS-UCF-563 d.
  - Client A: D-254 `Iso Own Probe {runId}-012` (Text, Active, bebas nilai User) untuk TC-GS-UCF-558.
  - Client B: D-253 `Client B Iso Probe {runId}-012` (Text, Active, Required No, Placeholder kosong sehingga nilai efektif `Enter client b iso probe {runId}-012`), dibuat lewat sesi API Total Control Client B; id-nya dicatat sebagai `{id Client B Iso Probe}` dari respons List sesi itu. Dihapus backend sesudah TC pemakai (Post Condition TC-GS-UCF-557, 558, dan 559: jumlah field Client B kembali 11).
  - Nilai uji request: `Rogue Field {runId}-012` (TC-GS-UCF-304), `Rogue Import {runId}-012` (TC-GS-UCF-563), id yang tidak ada `1000000000000000000` (TC-GS-UCF-557, 558, 559), `{id Auth Probe}` dan `{id Iso Own Probe}` dari respons seeding.
- Data Pre-setup: Rahmat Hidayat (user Login Client A) dibaca di Detail pada TC-GS-UCF-306. Population D-01 tidak di-seed karena tidak ada asersi yang bergantung pada jumlah atau urutannya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua field bersuffix `{runId}-012` yang masih ada di Client A dan Client B (termasuk `Rogue Field {runId}-012` bila server ternyata membuatnya); kosongkan Search tabel; kembalikan sesi ke akun default suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk semua akun di atas dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: klien HTTP lewat console browser sesi akun aktor (mengirim `POST`, `PATCH`, dan `DELETE` ke `/v2/iam/user-custom-fields` dengan token sesi) dan pembacaan status serta isi respons; pembacaan jumlah entri Changelog (total pada Pagination), Search pada Changelog, dan Detail user; ganti akun (logout lalu login).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-304: Server menolak Create dari aktor tanpa capability Create walau UI di-bypass

1. Sebagai Read Only, kirim `POST /v2/iam/user-custom-fields` dengan body `{"fieldName": "Rogue Field {runId}-012", "dataType": "text"}` lewat console browser
2. Verifikasi respons server `403 Forbidden`
3. Muat ulang tab Custom Field (F5)
4. Ketik Search `Rogue Field`, tekan Enter
5. Verifikasi `Rogue Field {runId}-012` tidak ada di tabel (empty state `No results found` tampil sebagai anchor hasil Search)
6. Klik `(←)` pada kotak Search

### TC-GS-UCF-305: Server menolak Edit dan perubahan status dari aktor tanpa capability Update

7. Ganti akun: logout, lalu login sebagai Manage user and role: Delete dan Read
8. Buka Global Settings > User > Custom Field
9. Kirim `PATCH /v2/iam/user-custom-fields/{id Auth Probe}` untuk `Auth Probe {runId}-012` dengan body `{"placeholder": "Hacked"}` lewat console browser
10. Kirim `PATCH /v2/iam/user-custom-fields/status` dengan body `{"ids": ["{id Auth Probe}"], "isActive": false}` lewat console browser
11. Verifikasi respons `PATCH` field `403 Forbidden`
12. Verifikasi respons `PATCH` status `403 Forbidden`
13. Muat ulang tab Custom Field (F5)
14. Ketik Search `Auth Probe`, tekan Enter
15. Verifikasi kolom Placeholder baris `Auth Probe {runId}-012` tetap `Select auth probe`
16. Verifikasi switch Active baris `Auth Probe {runId}-012` tetap On
17. Klik `(←)` pada kotak Search

### TC-GS-UCF-306: Server menolak Delete dari aktor tanpa capability Delete

18. Ganti akun: logout, lalu login sebagai Manage user and role: Update dan Read
19. Buka Global Settings > User > Custom Field
20. Klik icon Changelog
21. Ketik Search `Auth Probe {runId}-012`, tekan Enter
22. Catat jumlah entri Changelog hasil Search sebagai baseline
23. Tutup popup Changelog dengan `✕`
24. Kirim `DELETE /v2/iam/user-custom-fields` dengan body `{"ids": ["{id Auth Probe}"]}` lewat console browser
25. Verifikasi respons server `403 Forbidden`
26. Muat ulang tab Custom Field (F5)
27. Ketik Search `Auth Probe`, tekan Enter
28. Verifikasi baris `Auth Probe {runId}-012` tetap ada di tabel
29. Klik `(←)` pada kotak Search
30. Buka Global Settings > User > User List, ketik Search `rahmatHidayat_automated_qaTeam1@qwertysystem.net`, tekan Enter, buka Detail user Rahmat Hidayat
31. Verifikasi Section Custom Fields pada Detail Rahmat Hidayat memuat field `Auth Probe {runId}-012` dengan nilai `Probe Value`
32. Buka Global Settings > User > Custom Field
33. Klik icon Changelog
34. Ketik Search `Auth Probe {runId}-012`, tekan Enter
35. Verifikasi entri Changelog hasil Search tampil dengan jumlah sama dengan baseline (langkah 22)
36. Verifikasi tidak ada entri Changelog dengan Action `Delete` untuk `Auth Probe {runId}-012`
37. Tutup popup Changelog dengan `✕`

### TC-GS-UCF-563: Pemegang Import data Create tanpa Manage user and role tidak dapat Edit, Delete, Toggle, atau Create Custom Field lewat permintaan langsung

38. Ganti akun: logout, lalu login sebagai Import data: Create dan Read (Rina Marlina)
39. Buka Global Settings > Import > User Login
40. Kirim `PATCH /v2/iam/user-custom-fields/{id Cost Center Probe}` untuk `Cost Center Probe {runId}-012` dengan body `{"placeholder": "Hacked"}` lewat console browser
41. Verifikasi respons `PATCH` field `403 Forbidden`
42. Kirim `PATCH /v2/iam/user-custom-fields/status` dengan body `{"ids": ["{id Cost Center Probe}"], "isActive": false}` lewat console browser
43. Verifikasi respons `PATCH` status `403 Forbidden`
44. Kirim `DELETE /v2/iam/user-custom-fields` dengan body `{"ids": ["{id Cost Center Probe}"]}` lewat console browser
45. Verifikasi respons `DELETE` `403 Forbidden`
46. Kirim `POST /v2/iam/user-custom-fields` dengan body `{"fieldName": "Rogue Import {runId}-012", "dataType": "text"}` lewat console browser
47. Verifikasi respons `POST` `403 Forbidden`
48. Ganti akun: logout, lalu login sebagai Total Control Client A (Sari Dewi)
49. Buka Global Settings > User > Custom Field
50. Ketik Search `Cost Center Probe`, tekan Enter
51. Verifikasi kolom Placeholder baris `Cost Center Probe {runId}-012` tetap `Select cost center`
52. Verifikasi switch Active baris `Cost Center Probe {runId}-012` tetap On
53. Ganti isi kotak search dengan `Rogue Import`, tekan Enter
54. Verifikasi `Rogue Import {runId}-012` tidak ada di tabel (empty state `No results found` tampil sebagai anchor hasil Search)
55. Klik `(←)` pada kotak Search
56. Klik icon Changelog
57. Ketik Search `Cost Center Probe {runId}-012`, tekan Enter
58. Verifikasi Changelog memuat entri Create `Cost Center Probe {runId}-012` (anchor: entri seeding tampil)
59. Verifikasi Changelog tidak memuat entri baru dari `Rina M`
60. Tutup popup Changelog dengan `✕`

### TC-GS-UCF-557: Edit ke id Custom Field milik entitas lain diperlakukan sebagai tidak ditemukan

61. Klik icon Changelog
62. Catat jumlah total entri Changelog Client A (total pada Pagination) sebagai baseline
63. Tutup popup Changelog dengan `✕`
64. Kirim `PATCH /v2/iam/user-custom-fields/{id Client B Iso Probe}` dengan body `{"fieldName": "Hacked Name", "dataType": "text", "placeholder": "Hacked"}` lewat console browser
65. Kirim `PATCH /v2/iam/user-custom-fields/1000000000000000000` dengan body yang sama (id yang tidak ada)
66. Verifikasi respons request id Client B Iso Probe `404 Not Found`
67. Verifikasi respons request id `1000000000000000000` `404 Not Found`
68. Verifikasi isi respons untuk id Client B Iso Probe sama dengan isi respons untuk id yang tidak ada (keberadaan record entitas lain tidak terungkap)
69. Muat ulang tab Custom Field Client A (F5)
70. Klik icon Changelog
71. Verifikasi jumlah total entri Changelog Client A sama dengan baseline (langkah 62), tidak ada entri baru
72. Tutup popup Changelog dengan `✕`

### TC-GS-UCF-558: Delete single dan bulk Delete dengan id Custom Field milik entitas lain menghasilkan hasil per ID tidak ditemukan

73. Kirim `DELETE /v2/iam/user-custom-fields` dengan body `{"ids": ["{id Client B Iso Probe}"]}` lewat console browser
74. Kirim `DELETE /v2/iam/user-custom-fields` dengan body `{"ids": ["{id Iso Own Probe}", "{id Client B Iso Probe}", "1000000000000000000"]}` lewat console browser
75. Verifikasi respons request pertama `200` dengan hasil per ID (bukan `404` dan bukan `403`)
76. Verifikasi respons request kedua `200` dengan hasil per ID (bukan `404` dan bukan `403`)
77. Verifikasi hasil id Client B Iso Probe pada request pertama sama dengan hasil id `1000000000000000000` pada request kedua (id tidak ditemukan)
78. Verifikasi hasil id Client B Iso Probe pada request kedua sama dengan hasil id `1000000000000000000` pada request kedua (id tidak ditemukan)
79. Verifikasi hasil id Iso Own Probe pada request kedua: terhapus
80. Muat ulang tab Custom Field Client A (F5)
81. Ketik Search `Iso Own Probe`, tekan Enter
82. Verifikasi `Iso Own Probe {runId}-012` tidak ada di tabel Client A (empty state `No results found` tampil sebagai anchor hasil Search)
83. Klik `(←)` pada kotak Search
84. Klik icon Changelog
85. Ketik Search `Iso Own Probe {runId}-012`, tekan Enter
86. Verifikasi Changelog Client A memuat tepat satu entri Delete untuk `Iso Own Probe {runId}-012`
87. Verifikasi Modified By entri Delete tersebut `Sari D`
88. Ganti isi kotak search Changelog dengan `Client B Iso Probe`, tekan Enter
89. Verifikasi Changelog Client A tidak memuat entri untuk `Client B Iso Probe {runId}-012` (empty state `No results found` tampil sebagai anchor hasil Search)
90. Kosongkan kotak search Changelog, tekan Enter
91. Catat jumlah total entri Changelog Client A sebagai baseline TC-GS-UCF-559
92. Tutup popup Changelog dengan `✕`

### TC-GS-UCF-559: Perubahan status dengan id Custom Field milik entitas lain menghasilkan hasil per ID tidak ditemukan

93. Kirim `PATCH /v2/iam/user-custom-fields/status` dengan body `{"ids": ["{id Client B Iso Probe}", "1000000000000000000"], "isActive": false}` lewat console browser
94. Verifikasi respons `200` dengan hasil per ID (bukan `404` dan bukan `403`)
95. Verifikasi hasil id Client B Iso Probe sama dengan hasil id `1000000000000000000` (id tidak ditemukan)
96. Muat ulang tab Custom Field Client A (F5)
97. Klik icon Changelog
98. Verifikasi jumlah total entri Changelog Client A sama dengan baseline (langkah 91), tidak ada entri baru
99. Tutup popup Changelog dengan `✕`

### Pengamatan pada Client B (TC-GS-UCF-557 d, TC-GS-UCF-558 e, dan TC-GS-UCF-559 d)

100. Ganti akun: logout, lalu login sebagai Total Control Client B (Lina Kusuma)
101. Buka Global Settings > User > Custom Field
102. Ketik Search `Client B Iso Probe`, tekan Enter
103. Verifikasi kolom Placeholder baris `Client B Iso Probe {runId}-012` tetap `Enter client b iso probe {runId}-012`
104. Verifikasi `Client B Iso Probe {runId}-012` tetap ada di tabel Client B
105. Verifikasi switch Active baris `Client B Iso Probe {runId}-012` tetap On
106. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Spec ini kelas a (defense-in-depth): request dikirim langsung ke server (bagian 8b butir 1).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok: akun Read Only (304), Delete dan Read (305), Update dan Read (306), Import data: Create dan Read (563, request) dilanjutkan pengamatan sebagai Total Control Client A, Total Control Client A (557, 558, 559; sesi dilanjutkan dari pengamatan 563, tanpa ganti akun ulang), lalu pengamatan Client B. TC-GS-UCF-563 ditaruh sebelum 557 supaya ganti akun ke Total Control hanya sekali. Aksi TC-GS-UCF-563 ditolak 403 dan tidak menambah entri Changelog, sehingga tidak memengaruhi baseline TC-GS-UCF-557 (langkah 62). Observasi sisi Client B (TC-GS-UCF-557 d, 558 e, 559 d) digabung dalam satu blok di akhir supaya ganti akun ke Client B hanya sekali; tiga asersi itu bermakna pada akhir ketiga request (Placeholder tetap, field tetap ada, switch tetap On). Urutan 557 sebelum 558 sebelum 559 memastikan baseline Changelog tiap TC diambil sesudah TC sebelumnya (TC-GS-UCF-558 menambah satu entri Delete yang sah).
- P-1 (bagian 3 konvensi): asersi "tidak ada entri Delete di Changelog" (TC-GS-UCF-306), "tidak ada entri baru dari Rina M" (TC-GS-UCF-563 d, dibatasi pada entri `Cost Center Probe {runId}-012` dengan anchor entri Create seeding), dan "tidak ada entri baru di Changelog" (TC-GS-UCF-557, 559) ditulis sebagai `Verifikasi` berbaseline jumlah entri di spec asal, karena spec absence (kelas g) tidak memuat aksi nyata untuk TC ini (S-05).
- Langkah penghubung (aksi tanpa `Verifikasi`): ganti akun, membuka Global Settings > User > Custom Field, Search untuk menemukan baris target, `(←)` untuk mengosongkan Search, muat ulang halaman (tidak ada form terbuka sehingga tidak ada dialog `beforeunload`), mencatat baseline jumlah entri Changelog (langkah 22, 62, dan 91), dan menutup popup Changelog dengan `✕`.
- Penolakan dengan `403` mengikuti keputusan NC-18 dan perilaku id milik entitas lain (`404` untuk Edit, `200` dengan hasil per ID untuk Delete dan perubahan status) mengikuti keputusan NC-15 sampai NC-17 dan EC-20; API/LLD belum seluruhnya diselaraskan (dilacak di `nc-followups.md`), sehingga asersi mengikuti TC dan bisa gagal pada backend nyata sampai API/LLD diselaraskan.
- Spec melewati sekitar 35 langkah (106 langkah). Seluruhnya satu kelas (defense-in-depth otorisasi server), tiap blok TC memakai data seed milik spec dan berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain, dan langkah ganti akun eksplisit ada di awal tiap blok akun baru.
- TC-GS-UCF-563 (kelas a) berada di spec ini, bukan di spec Import (keputusan K-8): request langsung ke server dengan akun Import data: Create dan Read, asersi hanya respons server dan state data (bagian 8b butir 1). Spec memakai `Cost Center Probe {runId}-012` milik spec sebagai target (S-06) dengan Placeholder `Select cost center` sebagai padanan `Cost Center` Pre-setup di TC.
- Temuan untuk QA:
  - TC-GS-UCF-305 dan 306 memakai `Cost Center` Pre-setup sebagai target; spec memakai `Auth Probe {runId}-012` milik spec (S-06) dengan Placeholder `Select auth probe` sebagai padanan Placeholder `Select cost center`. Detail Rahmat Hidayat pada TC-GS-UCF-306 butuh nilai User pada field itu; mekanisme mengisinya tidak ada di TC, PRD, atau LLD dan disediakan tim FE/BE.
  - TC-GS-UCF-563 Expected d ("Changelog tidak memuat entri baru dari Rina M") tidak menyebut baseline dan kolom pencarian Changelog (NC-06); spec membatasi asersi pada entri `Cost Center Probe {runId}-012` dengan anchor entri Create seeding, dan akun `importCreate_automated_qaTeam1@qwertysystem.net` tidak punya env var terdaftar (nama baru `GS_IMPORTCREATE_PASSWORD`).
  - TC-GS-UCF-559 Expected b menyebut id `9999999999999999999` sedangkan Data Uji dan langkah 1 memakai `1000000000000000000`; spec memakai `1000000000000000000`.
  - TC-GS-UCF-304 sampai 306 dan 557 sampai 559 tidak menyebut cara mengirim request dari console selain "lewat console browser"; spec menuliskan kemampuan klien HTTP dengan token sesi akun aktor di Prerequisites.
  - TC-GS-UCF-557 sampai 559 mengandaikan id `{id Client B Iso Probe}` dicatat dari sesi Client B; mekanisme pembacaannya disediakan hook `before` (sesi API Client B) dan tim FE/BE.
  - Post Condition TC-GS-UCF-557, 558, dan 559 ("Client B Iso Probe dihapus backend") tidak punya langkah observasi dan tidak diasersi; penghapusan dilakukan hook `after`.
  - TC-GS-UCF-306 langkah 2 menyebut "Detail Rahmat Hidayat section Custom Fields" tanpa jalur navigasi; spec membuka Detail lewat User List dan Search email Pre-setup. Teks dan struktur Section Custom Fields di Detail User milik modul User.
  - TC-GS-UCF-558 Expected b memuat dua klausa pada hasil id Client B Iso Probe (request pertama dan kedua); spec memecahnya menjadi dua `Verifikasi`.
