---
id: TC-GS-DIV-E2E-057-changelog-filter-fungsional-or-and-dan-kombinasi
title: "Modal Changelog: Filter Date dan Multi-Select, Logika OR/AND, serta Kombinasi dengan Search dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-198
  - TC-GS-DIV-199
  - TC-GS-DIV-200
  - TC-GS-DIV-201
  - TC-GS-DIV-205
  - TC-GS-DIV-226
  - TC-GS-DIV-227
  - TC-GS-DIV-228
  - TC-GS-DIV-229
coverage:
  web: automated
---

# Modal Changelog: Filter Date dan Multi-Select, Logika OR/AND, serta Kombinasi dengan Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API oleh akun Sari Dewi di hook `before`, urutan sebagai berikut):
  - Population D-02 oleh Sari Dewi (seeding Division lewat API, setara TC-GS-DIV-30): 26 Division dengan nama dan Code literal Accounting (`ACC`), Administration (`ADM`), Audit (`AUD`), Business Development (`BD`), Corporate Communication (`CCM`), Customer Service (`CSV`), Data Analytics (`DA`), Engineering (`ENG`), Facilities (`FAC`), General Affairs (`GA`), Information Technology (`IT`), Internal Control (`IC`), Logistics (`LOG`), Marketing (`MKT`), Procurement (`PRC`), Product Management (`PM`), Production (`PRD`), Quality Assurance (`QA`), Research and Development (`RND`), Risk Management (`RSK`), Sales (`SLS`), Security (`SEC`), Strategy (`STR`), Supply Chain (`SC`), Training (`TRN`), Warehouse (`WH`). Nama dan Code literal (pengecualian S-12 untuk Population Division: seeding idempotent, nama yang sudah ada dilewati; cleanup hanya menghapus yang dibuat spec ini; suite serial). Tiap Create mencatat entri Changelog Action Create oleh `Sari D` (Old Value `—`). Seluruh 26 Division dipakai: TC-GS-DIV-226 mengasersi 25 baris pada page size 25 dari entri Action `Create`, dan riwayat lebih dari 10 entri (TC-GS-DIV-226) serta entri hari uji (TC-GS-DIV-198) tersedia.
  - Division milik spec ini untuk entri Edit: `Accounting {runId}-057` (Code `ACC-057`) dan `Procurement {runId}-057` (Code `PRC-057`) dibuat oleh Sari Dewi lewat API, lalu diedit lewat API (setara TC-GS-DIV-101 dan TC-GS-DIV-102): Name `Accounting {runId}-057` diubah menjadi `Accounting and Tax {runId}-057`, dan Code `Procurement {runId}-057` diubah dari `PRC-057` menjadi `PROC-057` (entri Action Edit, Field `Division Name` dan `Code`, oleh `Sari D`). Population D-02 tidak diedit. Sebelum dibuat, hook `before` menghapus sisa Division run lama yang namanya bersuffix `-057` (berdasarkan nama bersuffix, bukan berdasarkan Code saja).
  - Division `Public Relations {runId}-057` (Code `PR`, setara TC-GS-DIV-65, D-10) dibuat lalu dihapus (setara TC-GS-DIV-116); menghasilkan entri Create dan Delete yang unik per run, dipakai TC-GS-DIV-199, 200, 205. Sebelum dibuat, hook `before` menghapus sisa Division bernama `Public Relations {runId lama}-057` dari run sebelumnya (berdasarkan nama bersuffix spec ini, bukan berdasarkan Code `PR` saja, karena Code `PR` juga dipakai spec lain), supaya Code `PR` bebas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Division Population yang dibuat spec ini, serta `Accounting and Tax {runId}-057` dan `Procurement {runId}-057`; hapus `Public Relations {runId}-057` bila masih ada. Entri Changelog tidak bisa dihapus.
- Kapasitas: Master Data Count Limit environment automation cukup untuk Division Pre-setup (6), Population (26), dan Division milik spec ini (`Public Relations`, `Accounting`, `Procurement` bersuffix) (disediakan tim FE).
- Kemampuan teknis: kontrol date range picker (memilih rentang 1 Jan 2020 sampai 31 Jan 2020 dan rentang hari uji); klik header kolom sort; ubah page size.
- Precondition TC-GS-DIV-198, 199, 200, 201, 205, 226, 227, 228, 229: login sebagai Total Control dan berada di Global Settings > User > Division; riwayat Changelog terisi. TC-GS-DIV-199: entri hasil TC-GS-DIV-101 dan TC-GS-DIV-102 ada. TC-GS-DIV-205: Division Public Relations dibuat dan dihapus. TC-GS-DIV-226: riwayat lebih dari 10 entri.
- Suite serial (`parallel: false`) karena Population D-02 bernama literal dan dipakai bersama spec lain.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang dipulihkan: tidak ada (spec hanya membaca).

## Test Steps

### TC-GS-DIV-198: Filter Date Modal Changelog menyaring berdasarkan rentang tanggal

1. Klik icon Changelog di Table Tools
2. Klik icon Filter di modal
3. Pilih rentang tanggal 1 Jan 2020 sampai 31 Jan 2020
4. Klik `[Apply]`
5. Verifikasi pesan `No results found`
6. Klik icon Filter di modal
7. Pilih rentang tanggal yang memuat hari uji
8. Klik `[Apply]`
9. Verifikasi baris Create `Public Relations {runId}-057` (entri hari uji) tampil

### TC-GS-DIV-199: Filter multi-select Modal Changelog: Action, Division Name, Field, dan Modified By

10. Klik Filter, klik `[Clear Field]`
11. Pilih Action `Delete`, klik `[Apply]`
12. Verifikasi tabel memuat sedikitnya satu baris Action `Delete`
13. Verifikasi tabel hanya memuat baris Action `Delete`
14. Klik Filter, klik `[Clear Field]`
15. Pilih Division Name `Accounting and Tax {runId}-057`, klik `[Apply]`
16. Verifikasi tabel memuat sedikitnya satu baris Division Name `Accounting and Tax {runId}-057`
17. Verifikasi tabel hanya memuat baris Division Name `Accounting and Tax {runId}-057`
18. Klik Filter, klik `[Clear Field]`
19. Pilih Field `Code`, klik `[Apply]`
20. Verifikasi tabel memuat sedikitnya satu baris Field `Code`
21. Verifikasi tabel hanya memuat baris Field `Code`
22. Klik Filter, klik `[Clear Field]`
23. Pilih Modified By `Sari D`, klik `[Apply]`
24. Verifikasi tabel memuat sedikitnya satu baris Modified By `Sari D`
25. Verifikasi tabel hanya memuat baris Modified By `Sari D`

### TC-GS-DIV-200: Dua opsi pada satu field filter digabung OR

26. Klik Filter, klik `[Clear Field]`
27. Pilih Action `Create` dan `Delete`, klik `[Apply]`
28. Verifikasi tabel memuat baris Action `Create`
29. Verifikasi tabel memuat baris Action `Delete`
30. Verifikasi tidak ada baris Action `Edit`

### TC-GS-DIV-201: Dua field filter berbeda digabung AND

31. Klik Filter, klik `[Clear Field]`
32. Pilih Action `Edit` dan Field `Code`, klik `[Apply]`
33. Verifikasi tabel memuat sedikitnya satu baris dengan Action `Edit` dan Field `Code`
34. Verifikasi tabel hanya memuat baris dengan Action `Edit` dan Field `Code`

### TC-GS-DIV-205: Search dan Filter Modal Changelog dikombinasikan lalu dipulihkan

35. Klik Filter, klik `[Clear Field]`
36. Pilih Action `Create`, klik `[Apply]`
37. Ketik Search `public` di modal, tekan Enter
38. Verifikasi tabel memuat baris Create `Public Relations {runId}-057`
39. Verifikasi tabel hanya memuat baris Action `Create`
40. Klik Filter, ubah pilihan Action dari `Create` menjadi `Edit`, klik `[Apply]`
41. Verifikasi pesan `No results found`
42. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`
43. Verifikasi hasil keyword `public` pulih: tabel memuat baris Create `Public Relations {runId}-057`
44. Verifikasi hasil keyword `public` pulih: tabel memuat baris Delete `Public Relations {runId}-057`

### TC-GS-DIV-226: Kombinasi Search, Filter, Sort, dan Pagination pada Modal Changelog

45. Klik icon `[✕]` untuk menutup Modal Changelog
46. Klik icon Changelog di Table Tools
47. Ketik Search `a` di modal, tekan Enter
48. Klik Filter, pilih Action `Create`, klik `[Apply]`
49. Klik header Division Name dua kali sampai descending
50. Ubah page size ke 25
51. Verifikasi keyword `a` tetap berlaku (input Search berisi `a`)
52. Verifikasi tabel memuat sedikitnya satu baris Action `Create`
53. Verifikasi Filter berlaku: tabel hanya memuat baris Action `Create`
54. Verifikasi Sort berlaku: baris terurut Division Name Z-A
55. Verifikasi Pagination berlaku: halaman 1 memuat 25 baris

### TC-GS-DIV-227: Clear Filter Modal Changelog saat Search dan Sort aktif mempertahankan keduanya

56. Klik icon `[✕]` untuk menutup Modal Changelog
57. Klik icon Changelog di Table Tools
58. Ketik Search `a` di modal, tekan Enter
59. Klik Filter, pilih Action `Create`, klik `[Apply]`
60. Klik header Date sekali sampai Oldest First
61. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`
62. Verifikasi keyword `a` tetap aktif (input Search berisi `a`)
63. Verifikasi ikon sort Date Oldest First tetap aktif (indikator sort; urutan baris tidak diasersi)

### TC-GS-DIV-228: Clear Search Modal Changelog saat Filter dan Sort aktif mempertahankan keduanya

64. Klik icon `[✕]` untuk menutup Modal Changelog
65. Klik icon Changelog di Table Tools
66. Klik Filter, pilih Action `Create`, klik `[Apply]`
67. Ketik Search `a` di modal, tekan Enter
68. Klik header Date sekali sampai Oldest First
69. Klik icon `(✕)` pada Search, lalu tekan Enter pada input kosong
70. Verifikasi tabel memuat sedikitnya satu baris Action `Create`
71. Verifikasi Filter Action `Create` tetap aktif (tabel hanya memuat baris Action `Create`)
72. Verifikasi ikon sort Date Oldest First tetap aktif (indikator sort; urutan baris tidak diasersi)

### TC-GS-DIV-229: Ganti kolom sort Modal Changelog saat Search dan Filter aktif tidak mereset saringan

73. Klik icon `[✕]` untuk menutup Modal Changelog
74. Klik icon Changelog di Table Tools
75. Ketik Search `a` di modal, tekan Enter
76. Klik Filter, pilih Action `Create`, klik `[Apply]`
77. Klik header Action
78. Klik header Division Name
79. Verifikasi sort berpindah ke kolom Division Name
80. Verifikasi ikon sort kolom Action kembali netral
81. Verifikasi keyword `a` tetap aktif (input Search berisi `a`)
82. Verifikasi tabel memuat sedikitnya satu baris Action `Create`
83. Verifikasi Filter Action `Create` tetap aktif (tabel hanya memuat baris Action `Create`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-DIV-198, 199, 200, 201, 205, 226, 227, 228, 229. Alasan: filter tunggal lebih dulu, kombinasi Search/Filter/Sort sesudahnya; tidak ada TC yang menghapus data. Modal Changelog dibuka di langkah 1 untuk TC-GS-DIV-198, 199, 200, 201, dan 205; TC-GS-DIV-226, 227, 228, dan 229 membuka modal sendiri dan memasang Search, Filter, dan Sort sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`, membersihkan state TC sebelumnya, S-03 dan S-09): langkah 10, 14, 18, 22, 26, 31, 35 (Clear Field sebelum filter berikutnya), serta langkah 45 dan 46, 56 dan 57, 64 dan 65, 73 dan 74 (menutup lalu membuka kembali Modal Changelog agar tiap TC kombinasi dimulai dari modal baru, S-09). Pemulihan Filter pada TC-GS-DIV-205 (langkah 42) dan TC-GS-DIV-227 (langkah 61) adalah langkah TC.
- Asersi memakai pola baris (bukan jumlah baris, kecuali 25 baris pada langkah 55 yang bergantung pada Population 26 Division), sehingga entri Changelog dari run atau spec lain tidak memengaruhi hasil. `Public Relations {runId}-057` bersuffix per run; kata kunci `public` tetap mencocokkan namanya. Langkah 9 mengasersi entri Create `Public Relations {runId}-057` sebagai entri hari uji yang dikenal. Asersi `Verifikasi tabel hanya memuat ...` didahului `Verifikasi tabel memuat sedikitnya satu baris ...` sebagai anchor positif (S-03, bagian 8b butir 2); pada TC-GS-DIV-205 anchor itu adalah langkah entri Create `Public Relations {runId}-057`.
- Spec melewati sekitar 35 langkah (83 langkah) karena sembilan TC memakai Search, Filter, dan Sort Modal Changelog dari dataset yang sama dan tiap klausa Expected menjadi satu `Verifikasi` (S-01); semua blok satu kelas harness (Search/Filter/Sort fungsional di Modal Changelog) dan satu akun. TC-GS-DIV-226, 227, 228, dan 229 masing-masing memasang state sendiri pada modal baru; TC-GS-DIV-198, 199, 200, 201, dan 205 memakai Modal Changelog yang dibuka di langkah 1 dan membersihkan Filter lewat langkah penghubung.
- Temuan untuk QA: (1) TC-GS-DIV-198 data "01-01-2020 sampai 31-01-2020" dan langkah "1 Jan 2020 sampai 31 Jan 2020" menunjuk rentang yang sama; spec memakai rentang itu dan cara mengisi date range picker disediakan tim FE. (2) TC-GS-DIV-226 Expected tidak menyebut jumlah baris; langkah 55 mengasersi 25 baris karena Population menyediakan 26 entri Create (kata kunci `a` mencocokkan Action `Create`). (3) TC-GS-DIV-227 dan 228 tidak menyebut apakah klik `(✕)`/Enter pada input kosong mereset sort; spec hanya mengasersi dua kondisi yang disebut Expected. (4) TC-GS-DIV-205 menyebut Division bernama `Public Relations`; spec memakai nama bersuffix per run (S-12). (5) Langkah 63 dan 72 mengasersi indikator ikon sort Date Oldest First, bukan urutan baris. (6) Sort kolom Date pada klik pertama diasumsikan Oldest First (TC-GS-DIV-207 Expected a).
