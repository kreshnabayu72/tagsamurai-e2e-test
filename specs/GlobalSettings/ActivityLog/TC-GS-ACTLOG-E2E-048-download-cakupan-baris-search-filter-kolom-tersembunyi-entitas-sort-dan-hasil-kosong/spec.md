---
id: TC-GS-ACTLOG-E2E-048-download-cakupan-baris-search-filter-kolom-tersembunyi-entitas-sort-dan-hasil-kosong
title: "Download: Cakupan Baris, Search, Filter, Kolom Tersembunyi, Entitas, Sort, dan Hasil Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-122
  - TC-GS-ACTLOG-123
  - TC-GS-ACTLOG-124
  - TC-GS-ACTLOG-127
  - TC-GS-ACTLOG-128
  - TC-GS-ACTLOG-135
coverage:
  web: automated
---

# Download: Cakupan Baris, Search, Filter, Kolom Tersembunyi, Entitas, Sort, dan Hasil Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas log-terbatas khusus spec ini (`Fixture.activityLog.entitasLog048`, disediakan tim FE/BE; email ditetapkan tim FE); password dari `Spectra.env.GS_LIMITLOG_TC_PASSWORD` (semua akun Total Control entitas log-terbatas berbagi password ini). Login sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite. Entitas ini dipakai hanya oleh spec ini (bukan Client Alfa) karena TC-GS-ACTLOG-122 mengasersi jumlah eksak 35 baris per tab pada log append-only; entitas segar disediakan tim FE/BE sebelum run dan baris log di-seed di hook `before`, bukan di Test Steps. TC-GS-ACTLOG-127 menyebut aktor Client Alfa; spec memetakannya ke entitas ini.
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun `entitasLog048` dan halaman Global Settings > Activity Log (kemampuan disediakan tim FE/BE).
- Akun pembentuk log Client Beta (`Fixture.activityLog.clientBeta`, email ditetapkan tim FE): password dari `Spectra.env.GS_CLIENTBETA_TC_PASSWORD`; dipakai hanya lewat sesi API di hook `before` untuk membuat baris log Client Beta lewat aksi nyata.
- Data Dinamis (suffix `{runId}-048`), dibuat lewat sesi API atau alur Auth di hook `before`; password user dinamis dari `Spectra.env.ACTLOG_PASSWORD`:
  - Entitas log-terbatas, Tab Session: user `Budi Anwar {runId}-048` (Position `Supervisor {runId}-048`, Division `Finance {runId}-048`) dengan dua percobaan Login `Failed` (password salah dari `Spectra.env.LP_PASSWORD_WRONG`) dan satu Login sukses, ditambah baris Session lain dari aktor.
  - Entitas log-terbatas, Tab User Action: satu baris `Edit` pada user `Siti Nurbaya {runId}-048` (tanpa Position, Division `Operations {runId}-048`) oleh aktor, ditambah baris `Create` Brand `Brand Alfa {runId}-048`.
  - Client Beta: user admin `Rina Marlina {runId}-048` login lewat sesi API (baris Session) lalu membuat Brand `Brand Beta {runId}-048` lewat API (baris User Action).
  - Jumlah total dari seeding (bagian 8b butir 10): seed BE melengkapi log entitas log-terbatas hingga N = 35 baris di Tab Session dan N = 35 baris di Tab User Action pada saat TC-GS-ACTLOG-122 dijalankan (page size 10), dihitung termasuk baris login aktor hook `before`, dengan lebih dari satu User dan lebih dari satu Object (kebutuhan TC-GS-ACTLOG-128).
  - Cleanup di hook `after`: Brand, user, Position, dan Division dinamis dihapus lewat API tanpa berasumsi seeding berhasil penuh (baris log tetap ada karena log tidak dapat dihapus).
- Kemampuan teknis (disediakan tim FE/BE):
  - Kelas binary buffer (prinsip 13f): menangkap berkas unduhan browser ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV (baris header, jumlah baris data, urutan baris, pencarian teks di seluruh sel). Berkas unduhan dihapus di hook `after`.
  - Seed BE untuk melengkapi jumlah baris tepat 35 per tab; mekanisme seed tidak disebut di TC, PRD, atau LLD.
- State global yang diubah dan dipulihkan: visibilitas kolom Setup Column kedua tab (dipulihkan di langkah 47 dan 60), sort kolom User dan Object (dipulihkan di langkah 70 dan 75), Search dan Filter kedua tab (dipulihkan di langkah 22, 28, 33, dan 38). Hook `after` mengembalikan Setup Column ke default sebagai cadangan.
- Suite serial (`parallel: false`).
- Hook `beforeEach`: kembali ke layar Global Settings > Activity Log > Session.

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-122: Download tanpa Search dan Filter mengekspor seluruh baris, bukan satu halaman, kedua tab

2. Verifikasi tab Session menampilkan 10 baris per halaman
3. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
4. Verifikasi berkas `Activity-Log-Session.csv` berisi baris header
5. Verifikasi berkas `Activity-Log-Session.csv` berisi 35 baris data
6. Klik tab "User Action"
7. Verifikasi tab User Action menampilkan 10 baris per halaman
8. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
9. Verifikasi berkas `Activity-Log-User-Action.csv` berisi baris header
10. Verifikasi berkas `Activity-Log-User-Action.csv` berisi 35 baris data

### TC-GS-ACTLOG-127: Berkas Download hanya memuat log entitas aktif, kedua tab

11. Klik tab "Session", klik icon Download, klik `Download as CSV`, buka isi berkas yang terunduh, lalu cari `Rina`
12. Verifikasi berkas Tab Session memuat baris Login `Budi Anwar {runId}-048` (baris milik entitas aktif)
13. Verifikasi berkas Tab Session tidak memuat baris milik Client Beta (pencarian `Rina` tanpa hasil)
14. Klik tab "User Action", klik icon Download, klik `Download as CSV`, buka isi berkas yang terunduh, lalu cari `Rina`
15. Verifikasi berkas Tab User Action memuat baris `Edit` `Siti Nurbaya {runId}-048` (baris milik entitas aktif)
16. Verifikasi berkas Tab User Action tidak memuat baris milik Client Beta (pencarian `Rina` tanpa hasil)

### TC-GS-ACTLOG-123: Download mengikuti Search dan Filter yang aktif, kedua tab

17. Klik tab "Session", ketik Search `Budi`, tekan Enter
18. Klik icon Filter, pilih Activity `Login`, lalu klik [Apply]
19. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
20. Verifikasi berkas Tab Session hanya memuat baris Login milik `Budi Anwar {runId}-048`
21. Verifikasi baris berkas Tab Session sama dengan hasil tabel
22. Klik icon Filter, klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search
23. Klik tab "User Action", ketik Search `Siti`, tekan Enter
24. Klik icon Filter, pilih Action `Edit`, lalu klik [Apply]
25. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
26. Verifikasi berkas Tab User Action hanya memuat baris `Edit` milik `Siti Nurbaya {runId}-048`
27. Verifikasi baris berkas Tab User Action sama dengan hasil tabel
28. Klik icon Filter, klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search

### TC-GS-ACTLOG-135: Download hasil kosong tetap menghasilkan berkas berisi header saja, kedua tab

29. Klik tab "Session", ketik Search `zzznotfound`, tekan Enter
30. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
31. Verifikasi berkas Tab Session berisi baris header kolom
32. Verifikasi berkas Tab Session tanpa baris data
33. Klik `(←)` pada kotak Search
34. Klik tab "User Action", ketik Search `zzznotfound`, tekan Enter
35. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
36. Verifikasi berkas Tab User Action berisi baris header kolom
37. Verifikasi berkas Tab User Action tanpa baris data
38. Klik `(←)` pada kotak Search

### TC-GS-ACTLOG-124: Download mengikuti visibilitas kolom, kolom tersembunyi tidak ikut dan ikut lagi setelah ditampilkan

39. Klik tab "Session", lalu buka Popup Setup Column lewat `⋯` pada header kolom Actions
40. Hilangkan centang kolom Note, lalu klik [Save]
41. Tunggu aksi Save selesai (Popup Setup Column tertutup)
42. Klik icon Download, lalu klik `Download as CSV`
43. Verifikasi tidak ada toast atau dialog peringatan pada unduhan pertama Tab Session
44. Buka isi berkas yang terunduh
45. Verifikasi berkas pertama Tab Session memuat kolom `Activity`
46. Verifikasi berkas pertama Tab Session tanpa kolom Note
47. Buka Popup Setup Column, centang kolom Note, lalu klik [Save]
48. Tunggu aksi Save selesai (Popup Setup Column tertutup)
49. Klik icon Download, lalu klik `Download as CSV`
50. Verifikasi tidak ada toast atau dialog peringatan pada unduhan kedua Tab Session
51. Buka isi berkas yang terunduh
52. Verifikasi berkas kedua Tab Session memuat kolom Note
53. Klik tab "User Action", buka Popup Setup Column lewat `⋯` pada header kolom Actions, hilangkan centang kolom Field, lalu klik [Save]
54. Tunggu aksi Save selesai (Popup Setup Column tertutup)
55. Klik icon Download, lalu klik `Download as CSV`
56. Verifikasi tidak ada toast atau dialog peringatan pada unduhan pertama Tab User Action
57. Buka isi berkas yang terunduh
58. Verifikasi berkas pertama Tab User Action memuat kolom `Object`
59. Verifikasi berkas pertama Tab User Action tanpa kolom Field
60. Buka Popup Setup Column, centang kolom Field, lalu klik [Save]
61. Tunggu aksi Save selesai (Popup Setup Column tertutup)
62. Klik icon Download, lalu klik `Download as CSV`
63. Verifikasi tidak ada toast atau dialog peringatan pada unduhan kedua Tab User Action
64. Buka isi berkas yang terunduh
65. Verifikasi berkas kedua Tab User Action memuat kolom Field

### TC-GS-ACTLOG-128: Urutan baris berkas Download mengikuti sort aktif, kedua tab

66. Klik tab "Session", lalu klik header kolom User satu kali
67. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
68. Verifikasi baris berkas Tab Session terurut User A-Z menurut nama lengkap
69. Verifikasi urutan baris berkas Tab Session sama dengan urutan tabel
70. Pulihkan sort kolom User ke default
71. Klik tab "User Action", lalu klik header kolom Object satu kali
72. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
73. Verifikasi baris berkas Tab User Action terurut Object A-Z
74. Verifikasi urutan baris berkas Tab User Action sama dengan urutan tabel
75. Pulihkan sort kolom Object ke default

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`. Mode: FE+BE. Kelas binary buffer (prinsip 13f): isi dan cakupan baris berkas CSV dipisah dari kegagalan export (spec 049), volume threshold (spec 050), serta nama berkas dan format nilai (spec 047).
- Urutan TC dalam spec: 122, 127, 123, 135, 124, 128. TC yang tidak mengubah state (122, 127) lebih dulu, lalu TC yang memakai Search dan Filter (123, 135), lalu TC yang mengubah Setup Column dan sort (124, 128); tiap perubahan state dipulihkan sebelum TC berikutnya. Urutan ini berbeda dari urutan nomor sumber demi pemulihan state yang paling sedikit.
- Blok per TC memuat kedua tab sesuai pemetaan TC, sehingga pindah tab berulang (langkah 6, 11, 14, 17, 23, 29, 34, 39, 53, 66, 71).
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab "Session" dan "User Action" antar TC; langkah 22, 28, 33, 38 (membersihkan Filter dan Search lewat `Filter > Clear Field > Apply` dan `(←)`, S-09); langkah 41, 48, 54, dan 61 (Tunggu aksi Save selesai, bagian 8b butir 8); langkah 47 dan 60 (menampilkan kembali kolom, sekaligus bagian TC-GS-ACTLOG-124); langkah 44, 51, 57, 64 (membuka isi berkas); langkah 70 dan 75 (memulihkan sort ke default).
- Urutan langkah TC-GS-ACTLOG-124 mengikuti urutan state (bagian 8b butir 11): absence toast atau dialog peringatan diasersi segera setelah pemicu unduhan dan sebelum asersi isi berkas.
- Asersi tambahan di luar Expected TC (S-03): langkah 2 dan 7 (page size 10 sebagai syarat makna "bukan satu halaman"); langkah 12 dan 15 (berkas memuat baris milik entitas aktif) sebagai anchor positif sebelum asersi tidak adanya baris Client Beta pada langkah 13 dan 16 (bagian 8b butir 2); langkah 45 dan 58 (berkas memuat kolom pembanding `Activity` dan `Object`) sebagai anchor sebelum asersi kolom tersembunyi tidak ada pada langkah 46 dan 59. Semuanya memakai data milik spec ini.
- Spec di atas smell 35 langkah (75 langkah). Alasan: seluruh blok berkelas satu harness (binary buffer) dan berdiri sendiri; kegagalan satu blok TC tidak membuat blok lain kehilangan makna. State yang diubah (Search, Filter, Setup Column, sort) dipulihkan sebelum blok berikutnya, dan tiap TC mencakup dua tab dengan Expected bermajemuk yang dipecah per klausa (S-01).
- Dependensi TC-GS-ACTLOG-124 pada TC-GS-ACTLOG-96 dan TC-GS-ACTLOG-183 (menyembunyikan kolom lewat Popup Setup Column) dipenuhi dengan menyalin langkah menyembunyikan dan menampilkan kolom.
- Pembagian TC lintas spec: TC-GS-ACTLOG-125, 129, 130, 131, 133, dan 134 ada di spec 047; TC-GS-ACTLOG-132 di spec 049; TC-GS-ACTLOG-136 dan 137 di spec 050.
- Temuan untuk QA:
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 22 dan 28 mengikuti TC-GS-ACTLOG-123.
  - TC-GS-ACTLOG-122: TC tidak menyebut entitas maupun cara menetapkan tepat 35 baris pada log append-only; spec memakai entitas log-terbatas khusus dengan seed BE di hook `before` (S-13).
  - TC-GS-ACTLOG-123: Data Uji menyebut `Siti Nurbaya` sebagai pemilik baris `Edit` di Tab User Action tanpa menyebut kolomnya (Name atau Modified By); spec memakai kolom Name (user yang diedit).
  - TC-GS-ACTLOG-127: TC menyebut Client Alfa dan Client Beta, tetapi Pre-setup 7 hanya mencantumkan Client Beta tanpa Client Alfa; spec memetakan Client Alfa ke entitas log-terbatas spec ini dan Client Beta ke `Fixture.activityLog.clientBeta`. TC hanya mencari `Rina` sehingga baris Client Beta tanpa kata itu tidak teruji.
  - TC-GS-ACTLOG-128: TC tidak menyebut cara mengembalikan sort ke default; spec menulis pemulihan sebagai aksi tanpa menyebut jumlah klik.
  - TC-GS-ACTLOG-135: TC tidak menyebut apakah icon Download tetap aktif saat hasil kosong; spec mengikuti TC (unduh tetap bisa dilakukan).
  - TC-GS-ACTLOG-124 dan 128: tidak ada Post Condition tanpa langkah observasi.
  - Guided Tooltip: kebutuhan flag akun entitas log-terbatas ini ditulis di Prerequisites (penyetelannya disediakan tim FE/BE).
