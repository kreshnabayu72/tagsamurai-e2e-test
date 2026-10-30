---
id: TC-GS-POS-E2E-039-changelog-search
title: "Popup Changelog: Search (Siklus, Kolom Teks, Field, Bukan Date, Tanpa Hasil, dan Terikat Visibilitas Kolom)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-205
  - TC-GS-POS-206
  - TC-GS-POS-207
  - TC-GS-POS-208
  - TC-GS-POS-209
  - TC-GS-POS-210
coverage:
  web: automated
---

# Popup Changelog: Search (Siklus, Kolom Teks, Field, Bukan Date, Tanpa Hasil, dan Terikat Visibilitas Kolom)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Total Control Create-Only (Sari Dewi) `manageUserRoleCreate_automated_{namaCompany}@qwertysystem.net` (Pre-setup 5), `Spectra.env.GS_CREATE_PASSWORD`, hanya sebagai aktor seeding entri `Procurement Analyst` di hook `before`.
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite.
- Data Dinamis (di-seed lewat API oleh masing-masing aktor di hook `before`, berurutan; nama bersuffix per run; fixture baru `Fixture.position.changelogSearch039`):
  1. Budi Santoso: Create `IT Support Specialist {runId}-039`.
  2. Budi Santoso: Edit `IT Support Specialist {runId}-039` menjadi `IT Operations Lead {runId}-039`.
  3. Budi Santoso: Create `Temporary Staff {runId}-039`, lalu Delete `Temporary Staff {runId}-039`.
  4. Sari Dewi: Create `Procurement Analyst {runId}-039`.
  Entri 4 dipakai sebagai precondition TC, tidak diasersi (Changelog berisi entri Create-Only).
  Mekanisme seeding oleh aktor (sesi atau fixture BE per aktor) disediakan tim FE/BE. Data Pre-setup tidak dipakai.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Position bersuffix `{runId}-039` yang masih ada (`IT Operations Lead`, `Procurement Analyst`); entri Changelog tidak dihapus. Pulihkan visibilitas kolom Popup Changelog ke default (`[Reset to Default]` pada Setup Column) bila langkah 62 sampai 64 tidak selesai.
- Kemampuan teknis: salin teks sel dan tempel ke input Search; pembacaan fokus input, placeholder, dan jumlah entri total pada pagination.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- State global: preferensi visibilitas kolom Popup Changelog (tersimpan di browser per pengguna per tabel) diubah di langkah 55 dan dipulihkan di langkah 63 sampai 64 serta hook `after`; flag Guided Tooltip dipulihkan seperti di atas. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-POS-205: Search Popup Changelog tanpa hasil

1. Klik ikon Changelog
2. Verifikasi User > Position > Popup Changelog: Position terbuka
3. Catat baseline: jumlah entri total dan baris yang tampil di halaman 1 sebelum Search
4. Ketik Search `Astronaut`, tekan Enter
5. Verifikasi Illustration tampil
6. Verifikasi Title "No results found"
7. Verifikasi Description "Try adjusting your search or filter."
8. Klik `←`

### TC-GS-POS-206: Siklus interaksi Search Popup Changelog

9. Klik ikon Search
10. Verifikasi input Search melebar
11. Verifikasi input Search fokus
12. Verifikasi placeholder "Search changelog..."
13. Ketik `Delete` (belum tekan Enter)
14. Verifikasi icon `✕` muncul
15. Verifikasi tabel belum tersaring (baris sama dengan baseline langkah 3)
16. Tekan Enter
17. Verifikasi baris Delete `Temporary Staff {runId}-039` tampil sebagai baris pembanding
18. Verifikasi tabel tersaring: setiap baris yang tampil memuat `Delete`
19. Klik `✕`
20. Verifikasi teks input Search kosong
21. Verifikasi tabel tetap menampilkan hasil terakhir (tersaring `Delete`)
22. Tekan Enter pada input kosong
23. Verifikasi tabel kembali menampilkan seluruh entri (sama dengan baseline langkah 3)
24. Ketik Search `Delete`, tekan Enter
25. Klik `←`
26. Verifikasi input Search tertutup
27. Verifikasi tabel langsung kembali menampilkan seluruh entri (sama dengan baseline langkah 3)

### TC-GS-POS-207: Search Popup Changelog, kelas kolom teks

28. Ketik Search `delete`, tekan Enter
29. Verifikasi baris Delete `Temporary Staff {runId}-039` tampil (Action, case-insensitive)
30. Klik `✕`
31. Ketik Search `temporary`, tekan Enter
32. Verifikasi baris Create `Temporary Staff {runId}-039` tampil (Position Name)
33. Verifikasi baris Delete `Temporary Staff {runId}-039` tampil (Position Name)
34. Klik `✕`
35. Ketik Search `SUPPORT SPEC`, tekan Enter
36. Verifikasi baris Edit dengan Old Value `IT Support Specialist {runId}-039` tampil (Old Value)
37. Klik `✕`
38. Ketik Search `Lead`, tekan Enter
39. Verifikasi baris dengan New Value `IT Operations Lead {runId}-039` tampil (New Value)
40. Klik `✕`
41. Ketik Search `budi`, tekan Enter
42. Verifikasi baris oleh `Budi S` tampil (Modified By)
43. Klik `←`

### TC-GS-POS-208: Search Popup Changelog, kolom Field

44. Ketik Search `position name`, tekan Enter
45. Verifikasi seluruh entri tampil (jumlah entri total sama dengan baseline langkah 3)
46. Verifikasi kolom Field bernilai `Position Name`
47. Klik `←`

### TC-GS-POS-209: Search Popup Changelog tidak mencari kolom Date

48. Salin teks sel Date salah satu baris
49. Tempel teks Date ke kotak Search (membuka input bila tertutup), tekan Enter
50. Verifikasi Illustration tampil
51. Verifikasi Title "No results found"
52. Verifikasi Description "Try adjusting your search or filter."
53. Klik `←`

### TC-GS-POS-210: Search Popup Changelog terikat visibilitas kolom

54. Klik `⋯` pada header kolom, pilih item `Setup Column...`
55. Sembunyikan kolom Position Name, Old Value, dan New Value pada modal Setup Column
56. Klik `[Save]`
57. Ketik Search `Temporary Staff`, tekan Enter
58. Verifikasi Illustration tampil (kolom tersembunyi)
59. Verifikasi Title "No results found" (kolom tersembunyi)
60. Verifikasi Description "Try adjusting your search or filter." (kolom tersembunyi)
61. Klik `←`
62. Klik `⋯` pada header kolom, pilih item `Setup Column...`
63. Tampilkan kembali kolom Position Name, Old Value, dan New Value pada modal Setup Column
64. Klik `[Save]`
65. Ketik Search `Temporary Staff`, tekan Enter
66. Verifikasi baris `Temporary Staff {runId}-039` tampil
67. Klik `←`
68. Klik `[✕]` di header untuk menutup Popup Changelog

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dipertahankan (205 sampai 210); TC-GS-POS-210 yang mengubah preferensi visibilitas kolom ada di akhir dan memulihkannya pada langkah 62 sampai 64. Popup Changelog dibuka sekali (langkah 1) dan ditutup sekali (langkah 68), karena tiap TC memulai dari state yang sama: Search tertutup dan tabel penuh (diakhiri `←` yang mereset tabel, diasersi di langkah 26 dan 27).
- Asersi memakai nama bersuffix `{runId}-039`; entri Changelog dari spec lain pada entitas yang sama ikut tampil pada hasil Search, sehingga asersi bersifat "baris tampil" dan bukan "hanya baris ini". Pada langkah 18 yang diasersi adalah setiap baris yang tampil memuat `Delete`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3 (mencatat baseline), langkah 8, 25, 43, 47, 53, 61, 67 (`←` menutup input dan mereset tabel), langkah 19, 30, 34, 37, 40 (`✕` mengosongkan input sebelum kata kunci berikutnya), langkah 48 (menyalin teks Date), langkah 68 (menutup popup tanpa dialog).
- Langkah 17 (baris Delete `Temporary Staff {runId}-039` tampil) adalah asersi tambahan di luar Expected TC-GS-POS-206 c; ditulis sebagai baris pembanding supaya asersi universal "setiap baris yang tampil memuat `Delete`" pada langkah 18 tidak lulus pada tabel kosong (konvensi 8b butir 2).
- Search ditulis atomik ("Ketik Search `X`, tekan Enter" membuka input bila tertutup) sesuai Expected TC-GS-POS-205 sampai 210. "Klik ikon Search" eksplisit hanya pada langkah 9 (TC-GS-POS-206, siklus input).
- Langkah 54, 62 (`Setup Column...` lewat Panel Column Visibility dari header `⋯`) mengikuti PRD §4.1 #11 dan #11a; TC-GS-POS-210 hanya menyebut "via Setup Column modal". Cara menyembunyikan dan menampilkan kolom di modal (kontrol per baris) dibahas lengkap di spec 042.
- Spec melewati sekitar 35 langkah (68 langkah). Seluruhnya satu kelas (Search pada Popup Changelog), satu akun, dataset seeding yang sama, dan tiap blok TC dimulai dari state bersih; blok 205 sampai 209 hanya membaca dan tetap bermakna walau blok lain gagal. Blok 210 mengubah preferensi kolom dan memulihkannya dalam blok yang sama.
- Topik satu dataset Changelog (screening 038, Search 039, Filter 040, Sort 041, Setup Column 042, Download 043) dipertahankan sebagai spec terpisah karena gabungan keenamnya melewati batas ukuran jauh dan tiap spec menyiapkan dan membersihkan seeding sendiri, sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Temuan untuk QA:
  - TC-GS-POS-205 sampai 210 memakai entri Changelog dari "TC Section 3" sebagai precondition; spec men-seed entri itu sendiri dengan nama bersuffix.
  - TC-GS-POS-206 langkah 7 menulis "Ketik `Delete` + Enter, klik `←`" tanpa menyebut kondisi awal input; spec mengikuti urutan tersebut setelah baris pembanding dicatat.
  - TC-GS-POS-208 Expected menulis "seluruh entri" tanpa angka; spec membandingkan jumlah entri total dengan baseline langkah 3.
  - TC-GS-POS-209 tidak menyebut baris Date mana yang disalin dan formatnya; spec menyalin teks sel Date baris mana pun dan tidak menulis nilainya.
  - TC-GS-POS-210 tidak menyebut cara membuka Setup Column dan cara menyembunyikan kolom; spec memakai alur PRD §4.1 #11 dan #11a.
