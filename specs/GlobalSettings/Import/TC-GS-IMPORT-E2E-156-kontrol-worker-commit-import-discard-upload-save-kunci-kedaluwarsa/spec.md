---
id: TC-GS-IMPORT-E2E-156-kontrol-worker-commit-import-discard-upload-save-kunci-kedaluwarsa
title: "Kontrol worker commit: Import, Discard, Upload, Save kunci kedaluwarsa, Confirm Mapping dari halaman basi memunculkan dialog Import In Progress"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-365
  - TC-GS-IMPORT-382
  - TC-GS-IMPORT-830
  - TC-GS-IMPORT-831
  - TC-GS-IMPORT-832
coverage:
  web: automated
---

# Kontrol worker commit: Import, Discard, Upload, Save kunci kedaluwarsa, Confirm Mapping dari halaman basi memunculkan dialog Import In Progress

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (kontrol worker commit, jam server) dan memakai Client E yang dipakai bersama spec commit lain; lihat `suite.md`.
- Akun (login aktor pertama di hook `before`; ganti akun eksplisit di tengah spec, hook `after` mengembalikan sesi ke akun default suite):
  - Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC_PASSWORD`: aktor pertama untuk TC-365, 382, 831, 832; juga pemicu sesi API pada TC-830.
  - Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC2_PASSWORD`: aktor UI pada TC-830 (ganti akun eksplisit); pada TC-365, 382, 831, 832 hanya pemicu lewat sesi API (permintaan Import fixture; P-2).
  - Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; TC-365, 382, 830, 831, 832 tidak merujuk D-47 pada kolom D-ref pada beberapa baris tetapi membutuhkannya):
  - Kontrol worker commit D-47 mode 1 (dijeda sebelum job mulai, job yang dimulai tetap `committing`) untuk TC-830, 831, 832 dan mode 2 (dijeda di dalam batch pertama) untuk TC-365, 382.
  - Sesi API Admin kedua dan Total Control Client E untuk permintaan Import (memulai commit).
  - Fixture jam server (TC-831): memajukan jam server 11 menit (TTL kunci sesi edit 10 menit) dan memulihkannya; jam browser tidak diubah karena TTL dihitung di server dan tidak diamati lewat countdown UI.
  - Margin jam TC-831 (kurang dari 5 menit; 8b.3): batas TTL kunci sesi edit 10 menit; pergeseran jam server 11 menit (langkah 32) memberi margin 11 − 10 = 1 menit (60 detik) di atas batas. Usia kunci pada langkah 35 = pergeseran 11 menit + waktu nyata sejak sesi edit dibuka (langkah 30), sehingga waktu nyata hanya menambah usia (arah aman: kunci tetap kedaluwarsa). Nilai 11 menit mengikuti TC-831 dan tidak dinaikkan.
  - Hook umur draft D-76 varian 1 (>=24 jam; `created_at` dimundurkan 25 jam) untuk TC-382, 830, 831, 832.
  - Skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, hapus hasil commit) dan seeding draft.
- Data Dinamis (milik spec ini; draft dibuang oleh reset sehingga nama baris berkas literal):
  - D-56 `brand-250-impor.csv`: `Brand Impor 001` sampai `Brand Impor 250`, semua valid dan unik (TC-365, 382).
  - D-50 `brand-12.csv`: 12 baris `Acme Corp`, `Lenovo`, `Zebra Technologies`, `Honeywell`, `Dell`, `HP Inc`, `Canon`, `Epson`, `Brother`, `Logitech`, `Cisco`, `Asus` (TC-830, 831, 832).
  - `brand-6.csv`: header `Brand Name`; `Nikon`, `Ricoh`, `Xerox`, `Sony`, `Panasonic`, `Sharp` (TC-830, 832).
  - TC-831: Brand Name baris #1 diubah menjadi `Acme Corporation` (tidak pernah tersimpan).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, pulihkan jam server ke waktu nyata, hapus draft Client E, hapus hasil commit bila ada, tutup konteks tambahan, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-365: Import dari halaman basi saat committing

1. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
2. Buka Global Settings > Import, pilih Sub-Tab Brand
3. Verifikasi footer `[Import (250)]` Enabled
4. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
5. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
6. Tunggu aksi selesai (permintaan mendapat respons)
7. Pada halaman langkah 2 (tanpa muat ulang) klik `[Import (250)]`
8. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
9. Klik `[OK]`
10. Verifikasi dialog menutup
11. Verifikasi Staging Table tetap menampilkan 250 baris tanpa perubahan (kartu Total Rows 250)

### TC-GS-IMPORT-382: Discard Draft dari halaman basi saat committing

12. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
13. Buka Global Settings > Import, pilih Sub-Tab Brand
14. Verifikasi footer `[Import (250)]` Enabled
15. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
16. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
17. Tunggu aksi selesai (permintaan mendapat respons)
18. Pada halaman langkah 13 (tanpa muat ulang) klik `[Discard]` pada Unsaved Banner
19. Klik `[Discard Draft]` pada dialog Discard Draft
20. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
21. Klik `[OK]`
22. Muat ulang halaman Import > Brand
23. Verifikasi Unsaved Banner tampil
24. Verifikasi kartu Total Rows tetap 250 (draft utuh)

### TC-GS-IMPORT-831: Save pemegang kunci yang sudah kedaluwarsa saat job committing

25. Reset Client E (D-47) dan seed draft Brand D-50 (12 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
26. Buka Global Settings > Import, pilih Sub-Tab Brand
27. Verifikasi Unsaved Banner tampil
28. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
29. Klik `⋯` pada baris #1
30. Pilih Edit
31. Ubah Brand Name baris #1 menjadi `Acme Corporation`
32. Majukan jam server 11 menit (fixture jam server)
33. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
34. Tunggu aksi selesai (permintaan mendapat respons)
35. Klik `[Save]`
36. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
37. Klik `[OK]` pada dialog
38. Verifikasi dialog tertutup
39. Pulihkan jam server ke waktu nyata (fixture jam server)
40. Klik `[Cancel]` pada footer sesi edit baris #1
41. Verifikasi dialog Discard Changes dengan Title "Discard Changes", Body "Unsaved edits will be lost.", dan tombol `[Keep Editing]` dan `[Discard]`
42. Klik `[Discard]` pada dialog Discard Changes
43. Muat ulang halaman Import > Brand
44. Verifikasi baris #1 menampilkan `Acme Corp`
45. Verifikasi kartu Total Rows menampilkan 12
46. Arahkan kursor ke `[Discard]`
47. Verifikasi `[Discard]` Disabled dengan tooltip "Can't discard while an import is in progress."

### TC-GS-IMPORT-832: Confirm Mapping dari Modal Column Mapping yang dibuka sebelum commit dimulai

48. Reset Client E (D-47) dan seed draft Brand D-50 (12 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
49. Buka Global Settings > Import, pilih Sub-Tab Brand
50. Verifikasi Unsaved Banner tampil
51. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
52. Klik `[Upload File]`
53. Pilih berkas `brand-6.csv` di file picker
54. Klik `[Append Records]` pada dialog Append to Draft
55. Verifikasi Modal Column Mapping berjudul `Column Mapping: Brand` terbuka
56. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API)
57. Tunggu aksi selesai (permintaan mendapat respons)
58. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
59. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
60. Klik `[OK]` pada dialog
61. Verifikasi dialog tertutup
62. Muat ulang halaman Import > Brand
63. Verifikasi kartu Total Rows 12 Active
64. Verifikasi kartu Ready to Import 12
65. Verifikasi kartu Errors 0 Disabled
66. Verifikasi kartu Duplicates 0 Disabled
67. Verifikasi Pagination "Showing 1 - 10 of 12 items"

### TC-GS-IMPORT-830: Upload dari halaman basi saat committing

68. Reset Client E (D-47) dan seed draft Brand D-50 (12 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
69. Ganti akun: logout, lalu login sebagai Admin kedua Client E (Dimas Anggoro)
70. Buka Global Settings > Import, pilih Sub-Tab Brand
71. Verifikasi Unsaved Banner tampil
72. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
73. Mulai commit draft Brand Client E atas nama Total Control Client E lewat permintaan Import fixture (sesi API)
74. Tunggu aksi selesai (permintaan mendapat respons)
75. Pada halaman langkah 70 (tanpa muat ulang) klik `[Upload File]`
76. Pilih berkas `brand-6.csv` di file picker
77. Verifikasi dialog Append to Draft dengan Title "Append to Draft", Body "The organization already has an active draft for this import type. Do you want to append new records to it?", dan tombol `[Cancel]` dan `[Append Records]`
78. Klik `[Append Records]` pada dialog Append to Draft
79. Verifikasi dialog Import In Progress dengan Title "Import In Progress", Body "An import is currently running for this draft. Please try again after it finishes.", dan tombol hanya `[OK]`
80. Klik `[OK]` pada dialog
81. Verifikasi dialog tertutup
82. Verifikasi Modal Column Mapping tidak tampil
83. Muat ulang halaman Import > Brand
84. Verifikasi kartu Total Rows tetap 12
85. Arahkan kursor ke `[Discard]`
86. Verifikasi `[Discard]` Disabled dengan tooltip "Can't discard while an import is in progress."

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah dialog Import In Progress dari halaman basi saat job `committing` yang dibentuk kontrol worker D-47. Pelaku kedua hanya memicu perubahan state lewat sesi API (P-2); jam server pada TC-831 adalah pemicu TTL kunci.
- Alasan melewati sekitar 35 langkah (86 langkah nominal): lima blok homogen (aksi dari halaman basi pada job `committing`), semua satu kelas dan berdiri sendiri dengan reset Client E di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok TC-830 diletakkan terakhir karena memakai ganti akun eksplisit ke Admin kedua Client E (langkah 69); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok mengikuti kebutuhan akun, bukan nomor TC.
- Peran akun pada TC-830, 831, 832 dibalik dibanding Langkah TC agar pelaku yang hanya memicu commit memakai sesi API: pada TC-831 dan TC-832 Total Control Client E yang memegang halaman basi dan Admin kedua memicu Import; pada TC-830 Admin kedua memegang halaman basi dan Total Control Client E memicu Import (langkah TC menyebut pelaku yang sama).
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 12, 25, 48, 68), aktivasi kontrol worker, pembukaan halaman dan Sub-Tab, pemicu sesi API (langkah 5, 16, 33, 56, 73) yang masing-masing diikuti "Tunggu aksi selesai" (langkah 6, 17, 34, 57, 74; K-16 dan bagian 8b butir 8: permintaan sesi API mendapat respons sebelum aksi UI berikutnya), memajukan dan memulihkan jam server (langkah 32 dan 39), pengubahan nama pada Edit (langkah 31), dan ganti akun (langkah 69). Langkah 40 sampai 42 menutup sesi edit yang masih dirty sebelum muat ulang langkah 43 (K-19c, S-08, S-09): `[Cancel]` pada sesi edit dengan perubahan belum disimpan membuka dialog Discard Changes (PRD), `Verifikasi` dialog pada langkah 41, lalu `[Discard]` pada langkah 42, sehingga tidak ada dialog `beforeunload` yang perlu ditangani. Langkah 39 memulihkan jam server sesudah asersi dialog dan sebelum muat ulang; TTL kunci dihitung di server dan tidak diamati lewat countdown UI sehingga jam browser tidak diubah.
- Langkah 3, 14, 27, 50, dan 71 adalah `Verifikasi` tambahan di luar Expected TC yang membuktikan prasyarat TC sebelum commit dimulai pelaku kedua (halaman basi dimuat dengan `[Import (N)]` Enabled atau Unsaved Banner tampil).
- Temuan untuk QA:
  - TC-GS-IMPORT-830, 831, 832 menyebut Admin kedua dan Total Control Client E sebagai dua sesi browser terpisah (halaman Unsaved Banner Admin kedua dibuka pada Langkah 1 TC); spec memakai satu sesi UI dan satu sesi API sesuai P-2, sehingga langkah "Admin kedua: buka Import > Brand dan perhatikan Unsaved Banner" pada TC-831 dan TC-832 tidak dijalankan sebagai UI kedua. Menunggu konfirmasi QA.
  - Penanda selesai untuk pemicu sesi API (langkah 5, 16, 33, 56, 73) tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di surface aktor UI.
  - TC-GS-IMPORT-831 menggeser jam server 11 menit untuk TTL kunci 10 menit tetapi tidak menyebut jam browser; spec hanya memajukan jam server (TTL dihitung di server).
  - TC-GS-IMPORT-830, 831, 832 memakai D-47 mode 1 dan D-76 varian 1; TC-GS-IMPORT-365 dan TC-GS-IMPORT-382 tidak merujuk D-47 pada kolom D-ref.
  - TC-GS-IMPORT-830 Expected a menyebut dialog Append to Draft tampil lebih dulu padahal job sudah `committing`; urutan dialog (Append sebelum Import In Progress) mengikuti Langkah TC.
  - Post Condition TC-GS-IMPORT-365, 382 ("job committing dengan worker dijeda; draft tetap 250 baris") dan TC-GS-IMPORT-830, 831, 832 ("worker dilanjutkan dan hasil commit direset") tidak punya langkah observasi tersendiri dan tidak diasersi (S-01); Post Condition b TC-GS-IMPORT-831 (jam server dikembalikan) dikerjakan langkah 39.
