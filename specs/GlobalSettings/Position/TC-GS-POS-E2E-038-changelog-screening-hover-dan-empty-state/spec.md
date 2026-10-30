---
id: TC-GS-POS-E2E-038-changelog-screening-hover-dan-empty-state
title: "Popup Changelog: Screening 3 Zona, Tooltip, Tutup lewat ✕ dan Esc, Klik Backdrop, Hover Modified By, Nama Panjang, dan Empty State"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-200
  - TC-GS-POS-201
  - TC-GS-POS-202
  - TC-GS-POS-203
  - TC-GS-POS-204
  - TC-GS-POS-241
  - TC-GS-POS-292
coverage:
  web: automated
---

# Popup Changelog: Screening 3 Zona, Tooltip, Tutup lewat ✕ dan Esc, Klik Backdrop, Hover Modified By, Nama Panjang, dan Empty State

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1) untuk seluruh TC kecuali TC-GS-POS-204. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Total Control Client Kosong (Pre-setup 18) untuk TC-GS-POS-204: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTEMPTY_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Email akun ini tidak tertulis di tabel Pre-setup TC (lihat Temuan untuk QA).
  - Total Control Create-Only (Sari Dewi) `manageUserRoleCreate_automated_{namaCompany}@qwertysystem.net` (Pre-setup 5), `Spectra.env.GS_CREATE_PASSWORD`, hanya sebagai aktor seeding entri `Procurement Analyst` di hook `before`.
  - Aktor `Buzzlightyear Sumardi` dan aktor satu kata `Budi` untuk TC-GS-POS-292, hanya sebagai aktor seeding di hook `before`. Akun, email, dan env var keduanya tidak ditetapkan di TC (lihat Temuan untuk QA).
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite.
- Data Pre-setup: entitas `Client Kosong` (Pre-setup 18), baca-saja: tanpa Changelog Position dan tidak diubah spec ini. Tidak ada spec yang menulis ke entitas itu (spec penulis memakai `Client Tulis`, Pre-setup 27), sehingga TC-GS-POS-204 tidak bergantung pada urutan spec.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; `## Test Steps` tidak mengulang langkah buka kecuali sesudah ganti akun (langkah 60).
- Data Dinamis (di-seed lewat API oleh masing-masing aktor di hook `before`, berurutan; nama bersuffix per run; fixture baru `Fixture.position.changelogScreen038`):
  1. Budi Santoso: Create `IT Support Specialist {runId}-038`.
  2. Budi Santoso: Edit `IT Support Specialist {runId}-038` menjadi `IT Operations Lead {runId}-038`.
  3. Budi Santoso: Create `Temporary Staff {runId}-038`, lalu Delete `Temporary Staff {runId}-038`.
  4. Sari Dewi: Create `Procurement Analyst {runId}-038`.
  5. `Buzzlightyear Sumardi`: Create `Position Aktor Panjang {runId}-038`.
  6. `Budi`: Create `Position Aktor Satu Kata {runId}-038`.
  Entri 2 dan 4 dipakai sebagai precondition TC, tidak diasersi (TC-GS-POS-200 sampai 203: Changelog berisi Create, Edit, Delete, dan entri Create-Only).
  Entri 5 dan 6 dibuat terakhir, sehingga seluruh entri di atas berada di halaman 1 Popup Changelog (urutan Date terbaru di atas, 10 baris per halaman). Mekanisme seeding oleh aktor (sesi atau fixture BE per aktor) disediakan tim FE/BE.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor spec ini (Total Control dan Client Kosong) dan hook `after` memulihkannya, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Position bersuffix `{runId}-038` yang masih ada (`IT Operations Lead`, `Procurement Analyst`, `Position Aktor Panjang`, `Position Aktor Satu Kata`). Entri Changelog tidak dihapus (tetap di entitas; tidak memengaruhi spec lain karena asersi memakai nama bersuffix).
- Selisih Date (TC-GS-POS-200 b.ii, precondition d): disediakan tim FE/BE, sedikitnya dua entri Changelog Position dengan Date berselisih minimal 1 menit (kolom Date berketelitian menit), supaya urutan default Date terbaru di atas (langkah 16) teramati.
- Kemampuan teknis: hover untuk tooltip; klik area backdrop di luar popup; tombol Esc; ganti akun (logout lalu login).
- State global: tidak ada yang diubah selain flag Guided Tooltip dan sesi akun (dipulihkan seperti di atas).

## Test Steps

### TC-GS-POS-200: Screening Popup Changelog: Position, 3 zona

1. Klik ikon Changelog
2. Verifikasi User > Position > Popup Changelog: Position terbuka
3. Verifikasi Header: Title "Changelog: Position"
4. Verifikasi Header: icon `[✕]`
5. Verifikasi Header: toolbar `Search | Filter | Download`
6. Verifikasi Body: urutan kolom `Date | Action | Position Name | Field | Old Value | New Value | Modified By | Actions (⋯)`
7. Verifikasi Body: kolom Date sortable
8. Verifikasi Body: kolom Action sortable
9. Verifikasi Body: kolom Position Name sortable
10. Verifikasi Body: kolom Field sortable
11. Verifikasi Body: kolom Old Value sortable
12. Verifikasi Body: kolom New Value sortable
13. Verifikasi Body: kolom Modified By sortable
14. Verifikasi Body: kolom `Actions (⋯)` unsortable
15. Verifikasi Body: tidak ada row action
16. Verifikasi Body: urutan default Date terbaru di atas
17. Verifikasi Body: baris Create `IT Support Specialist {runId}-038` memiliki Old Value `—`
18. Verifikasi Body: baris Create `IT Support Specialist {runId}-038` memiliki New Value `IT Support Specialist {runId}-038`
19. Verifikasi Body: baris Delete `Temporary Staff {runId}-038` memiliki Old Value `Temporary Staff {runId}-038`
20. Verifikasi Body: baris Delete `Temporary Staff {runId}-038` memiliki New Value `—`
21. Verifikasi Body: Action ditulis teks polos (bukan badge)
22. Verifikasi Body: Modified By pada entri aktor Budi Santoso berformat `Budi S`
23. Verifikasi Footer: pagination default 10 baris per halaman
24. Klik `⋯` pada header kolom Actions
25. Verifikasi Overlay Column Visibility terbuka
26. Tekan Esc
27. Verifikasi Overlay Column Visibility tertutup

### TC-GS-POS-201: Tooltip toolbar dan header Column Visibility Popup Changelog

28. Hover ikon Search
29. Verifikasi tooltip "Search"
30. Hover ikon Filter
31. Verifikasi tooltip "Filter"
32. Hover ikon Download
33. Verifikasi tooltip "Download"
34. Hover `⋯` pada header kolom
35. Verifikasi tooltip "Column Visibility"

### TC-GS-POS-241: Hover Modified By menampilkan nama lengkap

36. Hover sel `Budi S` pada baris Create `IT Support Specialist {runId}-038`
37. Verifikasi tooltip `Budi Santoso`

### TC-GS-POS-292: Tampilan Modified By nama depan panjang dan nama satu kata

38. Verifikasi sel Modified By pada baris Create `Position Aktor Panjang {runId}-038` tampil `Buzzlightyear S` utuh, tanpa pemotongan `..`
39. Verifikasi sel Modified By pada baris Create `Position Aktor Satu Kata {runId}-038` tampil `Budi`
40. Hover sel `Buzzlightyear S` pada baris Create `Position Aktor Panjang {runId}-038`
41. Verifikasi tooltip `Buzzlightyear Sumardi`
42. Hover sel `Budi` pada baris Create `Position Aktor Satu Kata {runId}-038`
43. Verifikasi tooltip `Budi`

### TC-GS-POS-203: Klik backdrop pada Popup Changelog

44. Klik area backdrop di luar popup
45. Verifikasi Popup Changelog tetap terbuka (klik backdrop diabaikan)
46. Klik `[✕]`
47. Verifikasi Popup Changelog tertutup
48. Klik ikon Changelog
49. Tekan Esc
50. Verifikasi Popup Changelog tertutup

### TC-GS-POS-202: Menutup Popup Changelog via ✕ dan Esc

51. Klik ikon Changelog
52. Klik `[✕]`
53. Verifikasi Popup Changelog tertutup
54. Verifikasi tampilan kembali ke tabel Position
55. Klik ikon Changelog
56. Tekan Esc
57. Verifikasi Popup Changelog tertutup

### TC-GS-POS-204: Empty state Popup Changelog, belum ada riwayat

58. Ganti akun: logout dari akun Total Control Budi Santoso
59. Login sebagai Total Control Client Kosong (`Spectra.env.GS_CLIENTEMPTY_TC_PASSWORD`)
60. Buka Global Settings > User > Position
61. Klik ikon Changelog
62. Verifikasi User > Position > Popup Changelog: Position terbuka
63. Verifikasi Illustration tampil
64. Verifikasi Title "No changelog yet"
65. Verifikasi Description "Activities and changes will appear here."
66. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 200, 201, 241, 292, 203, 202, 204. Screening dan hover dilakukan pada satu pembukaan popup; kasus klik backdrop (203) ditaruh sebelum kasus menutup (202); TC-GS-POS-204 di akhir karena berganti akun. Urutan ini menyimpang dari urutan TC sumber. Pembukaan Popup Changelog lima kali (langkah 1, 48, 51, 55, 61) sama dengan jumlah kejadian menutup popup (langkah 46, 49, 52, 56, 66).
- Expected a, b, c TC-GS-POS-203 diasersi di blok TC-GS-POS-203: klik backdrop diabaikan (langkah 45), `[✕]` menutup (langkah 46 sampai 47), dan Esc menutup popup yang dibuka ulang (langkah 48 sampai 50). TC-GS-POS-202 mengulang `[✕]` dan Esc untuk Expected a dan b miliknya sendiri (langkah 51 sampai 57).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka popup), langkah 48, 51, dan 55 (membuka ulang popup), langkah 58 sampai 60 (ganti akun dan buka tab Position), langkah 66 (menutup popup tanpa dialog karena tidak ada form).
- Klausa "klik `⋯` pada header kolom: Overlay Column Visibility terbuka; Esc menutup overlay" (Expected b.v TC-GS-POS-200) diasersi di langkah 24 sampai 27.
- Asersi absence log tidak ada di spec ini. Asersi empty state Changelog untuk entitas lain (`Client Tanpa Seed`) ada di spec 002 (TC-GS-POS-296).
- Spec melewati sekitar 35 langkah (66 langkah). Seluruhnya satu kelas (tampilan Popup Changelog, hanya membaca, tanpa aksi yang mengubah data), dataset hasil seeding yang sama, dan tiap blok TC berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain. Ganti akun di langkah 58 memiliki langkah eksplisit dan bagian sesudahnya (TC-GS-POS-204, entitas `Client Kosong`) tetap bermakna walau bagian sebelumnya gagal.
- Topik satu dataset Changelog (screening 038, Search 039, Filter 040, Sort 041, Setup Column 042, Download 043) dipertahankan sebagai spec terpisah karena gabungan keenamnya melewati batas ukuran jauh dan tiap spec menyiapkan dan membersihkan seeding sendiri, sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Temuan untuk QA:
  - TC-GS-POS-200 precondition d mensyaratkan dua entri Date berselisih minimal 1 menit tanpa menyebut cara membentuknya; spec menyatakannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-POS-292 menyebut aktor `Buzzlightyear Sumardi` dan `Budi` tanpa akun, email, atau env var, dan tanpa nama Position yang dibuat; spec memakai nama `Position Aktor Panjang {runId}-038` dan `Position Aktor Satu Kata {runId}-038`. Env var password kedua aktor belum ditetapkan.
  - Email akun Total Control Client Kosong tidak tertulis di Pre-setup 18; env var `GS_CLIENTEMPTY_TC_PASSWORD` baru.
  - TC-GS-POS-292 langkah 1 menulis "klik ikon Changelog" tanpa menyebut baris yang menjadi pembanding; spec mencari baris lewat nama Position bersuffix.
  - TC-GS-POS-241 memakai sel `Budi S`; entri Changelog lain dari Budi Santoso (dari spec lain) bisa ikut tampil, sehingga spec hover pada baris bernama bersuffix.
  - TC-GS-POS-200 b.v menyebut "Esc menutup overlay" tanpa menyatakan apakah Popup Changelog tetap terbuka; spec melanjutkan TC berikutnya dengan popup masih terbuka.