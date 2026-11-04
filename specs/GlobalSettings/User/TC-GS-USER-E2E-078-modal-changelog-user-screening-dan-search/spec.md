---
id: TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search
title: "Modal Changelog User: Screening, State Kosong, dan Search Substring, Trim, Kolom Non-Searchable, serta Kolom Hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-465
  - TC-GS-USER-466
  - TC-GS-USER-467
  - TC-GS-USER-468
  - TC-GS-USER-469
  - TC-GS-USER-470
  - TC-GS-USER-471
  - TC-GS-USER-472
  - TC-GS-USER-473
  - TC-GS-USER-474
  - TC-GS-USER-475
  - TC-GS-USER-476
coverage:
  web: automated
---

# Modal Changelog User: Screening, State Kosong, dan Search Substring, Trim, Kolom Non-Searchable, serta Kolom Hidden

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2); kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite: login di hook `before`, hook `after` mengembalikan sesi ke akun ini. Nama singkat di kolom Modified By: `Siti N` (tooltip `Siti Nurhaliza`). Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role, Full CRUD (Fajar Nugroho), `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4); kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`. Dipakai hanya untuk memicu entri Changelog dengan Modified By kedua `Fajar N` (nama singkat dibentuk seperti `Siti N`; TC tidak menyebutnya), sehingga kolom Modified By punya sedikitnya dua nilai distinct (S-11). Tidak ada sesi UI kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Seeding minimal (S-11; lewat API di hook `before`, berurutan; kemampuan seeding user dan perubahan user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD. Tiap user seed diberi Position `Staff` (Tabel Data Uji Pre-setup No. 22), Division `Finance` (No. 23), dan Access `Fixed Asset` (No. 26), email `<nama>+{runId}-078@qwertysystem.net`. Kuota user plan cukup untuk user seed milik spec ini (disediakan tim FE). Hanya data yang dipakai `Verifikasi` yang di-seed, dengan sedikitnya dua nilai distinct pada kolom Action, User Name, Field, dan Modified By):
  - U-1: Create `Alfa {runId}-078` oleh Siti Nurhaliza (entri Action Create, Field Name, Old Value `—`, Modified By `Siti N`), lalu Edit Position `Staff` menjadi `Supervisor` oleh Siti Nurhaliza (entri Action Edit, Field Position, Old Value `Staff`, New Value `Supervisor`).
  - U-2: Create `Beta {runId}-078` oleh Fajar Nugroho (entri Action Create, Modified By `Fajar N`), lalu Deactivate oleh Siti Nurhaliza (entri Action Deactivate, Field Status (Global), Old Value `Active`, New Value `Inactive`).
  - U-3: Create `Sementara {runId}-078` sebagai Temporary User, lalu entri Action Auto-Deactivate (Modified By `System`) dihasilkan oleh job auto-deactivate. Pemicu job disediakan tim FE/BE (TC-GS-USER-467 tidak memberi cara membuat entri Auto-Deactivate); entri dicap waktu hari uji. Seeding ini dijalankan pertama.
  - Seluruh entri spec ini berjumlah 6 (kurang dari 10) dan dibuat tepat sebelum spec berjalan (suite serial), sehingga seluruhnya berada di halaman 1 pada urutan default Newest First.
- General Settings Time Format 12-hour pada entitas Client A disediakan tim FE (precondition TC-GS-USER-469); spec tidak mengubahnya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1, U-2, dan U-3 bila masih ada; kembalikan sesi ke akun default suite; hapus konfigurasi kolom Modal Changelog User di `localStorage` bila tersisa. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: hover (tooltip); membaca teks kolom Date dan menyalinnya ke kotak Search.
- Precondition TC-GS-USER-465 sampai 476: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); TC-GS-USER-466 memakai data pre-setup User (seed Default User selalu menulis 1 baris Create, sehingga modal tidak kosong tanpa Filter).
- Suite serial (`parallel: false`). Changelog bersifat append-only dan dipakai bersama spec lain: asersi memakai pola baris (nilai bersuffix `{runId}-078`), bukan jumlah baris total, kecuali dinyatakan lain. Spec ini tidak mengubah atau menghapus data Pre-setup (S-06).
- State global yang diubah: konfigurasi kolom Modal Changelog User (TC-GS-USER-475 menyembunyikan lalu menampilkan lagi `Modified By`, dipulihkan di langkah 71).

## Test Steps

### TC-GS-USER-465: Screening Modal Changelog User
1. Klik icon Changelog di Table Tools
2. Verifikasi Header: Title `Changelog: User`
3. Verifikasi Header: icon `[✕]`
4. Verifikasi Body: Toolbar memuat icon Search, Filter, dan Download
5. Klik icon Search di modal
6. Verifikasi Body: placeholder input Search `Search action, name, field, or value...`
7. Klik icon panah `(←)` untuk menutup Search
8. Verifikasi Body: kolom `Date (default Newest First) | Action | User Name | Field | Old Value | New Value | Modified By | Column Visibility (⋯)`
9. Verifikasi Body: ikon sort kolom Date menunjukkan Newest First
10. Verifikasi Body: User Name pada baris Create `Alfa {runId}-078` tampil sebagai plain text (bukan link)
11. Verifikasi Body: tabel read-only tanpa row action
12. Verifikasi Footer: Pagination default 10 data per halaman
### TC-GS-USER-468: Hover Modified By menampilkan nama lengkap
13. Hover sel Modified By `Siti N` pada baris Create `Alfa {runId}-078`
14. Verifikasi Tooltip `Siti Nurhaliza`
### TC-GS-USER-469: Date mengikuti format General Settings
15. Verifikasi kolom Date pada baris Create `Alfa {runId}-078` memakai format jam 12-hour sesuai General Settings
### TC-GS-USER-467: Opsi filter Modified By memuat System
16. Klik icon Filter di modal
17. Buka dropdown Modified By
18. Verifikasi opsi `System` tersedia
19. Tutup dropdown Modified By dan Filter Panel
### TC-GS-USER-470: Siklus Search reveal, Enter, clear, dan collapse
20. Klik icon Search di modal
21. Verifikasi search bar melebar
22. Verifikasi kursor auto-focus pada input Search
23. Ketik `edit` pada input Search
24. Verifikasi tabel belum tersaring (baris Create `Alfa {runId}-078` masih tampil)
25. Verifikasi icon `(✕)` muncul
26. Tekan Enter
27. Verifikasi tabel tersaring (baris Edit `Alfa {runId}-078` tampil)
28. Verifikasi tabel tersaring (baris Create `Alfa {runId}-078` tidak tampil)
29. Klik icon `(✕)`
30. Verifikasi input Search kosong
31. Verifikasi tabel tetap hasil terakhir (baris Edit `Alfa {runId}-078` tampil)
32. Verifikasi tabel tetap hasil terakhir (baris Create `Alfa {runId}-078` tidak tampil)
33. Tekan Enter pada input kosong
34. Verifikasi tabel kembali menampilkan semua data (baris Create `Alfa {runId}-078` tampil kembali)
35. Isi Search dengan `edit`, tekan Enter
36. Klik icon panah `(←)`
37. Verifikasi search bar collapse
38. Verifikasi tabel langsung di-reset (baris Create `Alfa {runId}-078` tampil kembali)
39. Klik icon Search di modal
40. Verifikasi input Search kosong
### TC-GS-USER-471: Query Search di-trim dan tidak case-sensitive
41. Isi Search dengan `  EDIT  ` (spasi di awal dan akhir), tekan Enter
42. Verifikasi baris Edit `Alfa {runId}-078` tampil
43. Verifikasi isi Search tetap `  EDIT  ` apa adanya
### TC-GS-USER-472: Search substring pada kolom kelas teks
44. Ganti isi kotak search dengan `deactiv`, tekan Enter
45. Verifikasi Action: baris Action `Deactivate` untuk `Beta {runId}-078` tampil
46. Ganti isi kotak search dengan `Beta {runId}-078`, tekan Enter
47. Verifikasi User Name: baris User Name `Beta {runId}-078` tampil
48. Ganti isi kotak search dengan `posit`, tekan Enter
49. Verifikasi Field: baris Field `Position` untuk `Alfa {runId}-078` tampil
50. Ganti isi kotak search dengan `fajar n`, tekan Enter
51. Verifikasi Modified By: baris Modified By `Fajar N` (Create `Beta {runId}-078`) tampil
### TC-GS-USER-473: Search substring pada kolom kelas nilai campuran
52. Ganti isi kotak search dengan `staf`, tekan Enter
53. Verifikasi Old Value: baris Old Value `Staff` (Edit `Alfa {runId}-078`) tampil
54. Ganti isi kotak search dengan `inactive`, tekan Enter
55. Verifikasi New Value: baris New Value `Inactive` (Deactivate `Beta {runId}-078`) tampil
### TC-GS-USER-474: Kolom Date tidak tercakup Search
56. Klik icon `(✕)`, tekan Enter pada input kosong
57. Verifikasi baris Create `Alfa {runId}-078` tampil dengan kolom Date terisi
58. Salin teks tanggal pada kolom Date baris Create `Alfa {runId}-078` (format yang tampil di kolom itu)
59. Isi Search dengan teks tanggal yang disalin, tekan Enter
60. Verifikasi pesan `No results found`
### TC-GS-USER-476: Empty filtered state
61. Ganti isi kotak search dengan `zzzqqq`, tekan Enter
62. Verifikasi Ilustrasi tampil
63. Verifikasi Title `No results found`
64. Verifikasi Description `Try adjusting your search or filter.`
### TC-GS-USER-475: Search tidak mencocokkan kolom yang di-hide, kembali cocok setelah unhide
65. Klik icon `(✕)`, tekan Enter pada input kosong
66. Klik header Column Visibility (⋯), hilangkan centang `Modified By` pada overlay
67. Tutup overlay Column Visibility
68. Verifikasi kolom `Modified By` tidak tampil di tabel
69. Isi Search dengan `fajar n`, tekan Enter
70. Verifikasi no result state (`No results found`)
71. Klik header Column Visibility (⋯), centang kembali `Modified By` pada overlay
72. Tutup overlay Column Visibility
73. Tekan Enter pada kotak Search (isi tetap `fajar n`)
74. Verifikasi baris Modified By `Fajar N` (Create `Beta {runId}-078`) kembali tampil
75. Klik `[✕]` untuk menutup Modal Changelog
### TC-GS-USER-466: Modal Changelog empty filtered state via Filter Date range
76. Klik icon Changelog di Table Tools
77. Verifikasi baris Create `Alfa {runId}-078` tampil
78. Klik icon Filter di modal
79. Pilih rentang tanggal 1 Jan 2000 sampai 31 Des 2000 pada Date, klik `[Apply]`
80. Verifikasi Ilustrasi tampil
81. Verifikasi Title `No results found`
82. Verifikasi Description `Try adjusting your search or filter.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-USER-465, 468, 469, 467, 470, 471, 472, 473, 474, 476, 475, 466. Alasan: screening (465) di awal dan TC tanpa aksi lanjutan (468, 469, 467) sebelum TC Search; TC-GS-USER-476 memakai Search yang sama dengan 474; TC-GS-USER-475 mengubah konfigurasi kolom sehingga sesudah TC Search lain dan memulihkannya sendiri; TC-GS-USER-466 di akhir karena membuka kembali Modal Changelog (langkah 76) sesudah Modal ditutup di langkah 75, sehingga Search dan konfigurasi kolom TC sebelumnya tidak memengaruhi filter Date. Modal Changelog dibuka sekali di langkah 1 untuk semua TC Client A.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): menutup dropdown Modified By dan Filter Panel sesudah TC-GS-USER-467; membuka kembali Search sesudah collapse (sebelum TC-GS-USER-471); mengosongkan Search sebelum TC-GS-USER-474 dan 475 (`(✕)` lalu Enter pada input kosong); menutup overlay Column Visibility pada TC-GS-USER-475; serta menutup Modal Changelog (langkah 75).
- Langkah tambahan atas TC (S-03): TC-GS-USER-465 b memuat placeholder Search yang hanya terlihat setelah icon Search diklik, sehingga ada langkah membuka lalu menutup Search; `Verifikasi` baris Create/Edit `Alfa` tampil pada TC-GS-USER-470 dan baris Create tampil pada TC-GS-USER-474 dan TC-GS-USER-466 (langkah 77, sebelum Filter) adalah anchor positif untuk asersi ketiadaan baris dan `No results found` (bagian 8b butir 2); `Verifikasi` kolom `Modified By` tidak tampil pada TC-GS-USER-475 mengunci state hide sebelum Search.
- Asersi memakai pola baris bersuffix `{runId}-078` (bukan jumlah baris), sehingga entri Changelog dari run atau spec lain tidak memengaruhi hasil. Kata kunci Search `fajar n`, `edit`, `deactiv`, `posit`, `staf`, dan `inactive` dicocokkan sebagai substring tanpa membedakan huruf besar kecil (prd-conventions.md §9.16).
- Spec melewati sekitar 35 langkah (82 langkah) karena dua belas TC memakai Modal Changelog yang sama dan tiap klausa Expected menjadi satu `Verifikasi` (S-01); semua blok satu layar (Modal Changelog User), satu akun aktor, dan satu dataset seed, dengan kasus pengosongan Search di antara blok.
- Temuan untuk QA: (1) TC-GS-USER-467 mensyaratkan entri Auto-Deactivate tanpa memberi cara membuatnya; pemicu job disediakan tim FE/BE. (2) TC-GS-USER-469 tidak menyebut format konkret (penanda AM atau PM); spec mengasersi kesesuaian dengan Time Format 12-hour General Settings. (3) TC-GS-USER-470 b dan f tidak menyebut cara mengamati tabel belum tersaring; spec memakai baris Create dan Edit `Alfa`. (4) TC-GS-USER-470 f menyebut keyword kosong tanpa cara mengamatinya setelah collapse; spec membuka Search kembali dan mengasersi input kosong. (5) TC-GS-USER-472 dan 473 menulis "lalu clear" di tiap kolom; spec mengganti isi kotak search dengan kata kunci berikutnya. (6) TC-GS-USER-474 Data Uji menyebut "tanggal/status" tetapi tabel tidak punya kolom status; spec memakai teks kolom Date. (7) TC-GS-USER-467 tidak menyebut teks opsi Modified By selain `System`; spec memakai nama singkat seperti di kolom tabel (`Siti N`, `Fajar N`).
