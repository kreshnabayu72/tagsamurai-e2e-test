---
id: TC-GS-ROLE-E2E-050-search-tab-total-control-dan-read-only
title: "Search Tab Total Control dan Tab Read Only: Siklus Input, Kolom Teks, Badge, TAG, dan Kolom Tanggal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-137
  - TC-GS-ROLE-138
  - TC-GS-ROLE-139
  - TC-GS-ROLE-140
  - TC-GS-ROLE-141
coverage:
  web: automated
---

# Search Tab Total Control dan Tab Read Only: Siklus Input, Kolom Teks, Badge, TAG, dan Kolom Tanggal

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login di hook `before`): Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD` (sudah terdaftar). Tidak ada env baru.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control (Search, Filter, dan kolom tabel dalam keadaan bawaan).
- Data Pre-setup yang dipakai (Tabel Data Uji Pre-setup; hanya dibaca): Tab Total Control berisi Ahmad Fauzi (IT Manager, IT; punya TAG `TG-00451`, precondition TC-GS-ROLE-140), Budi Santoso (Default User), Dewi Lestari (Staff, Finance, Inactive), dan Bayu Nugraha (baris 19, Temporary User, Temporary Until terisi). Tab Read Only berisi Siti Nurhaliza (Finance Staff, Finance, Active; Modified By `Ahmad F`), Rina Putri (HR Manager, HR, Inactive), dan Intan Permata (baris 19, Temporary User). Kedua tab masing-masing berisi 3 user atau lebih dengan Position dan Division berbeda, sehingga tiap kolom yang dicari punya sedikitnya dua nilai distinct (S-11).
- Given (hook `before`, lewat seeding API): Rudi Hartono (Pending Activation, Tabel Data Uji Pre-setup baris 11) di-assign Total Control (setara TC-GS-ROLE-59, hanya untuk Rudi Hartono). Dipakai oleh TC-GS-ROLE-139.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): cabut Total Control Rudi Hartono (kembali ke state kandidat tanpa access level, Pre-setup baris 11); kolom tabel dikembalikan ke bawaan lewat `[Reset to Default]` pada Setup Column (langkah 64 sampai 66; hook `after` sebagai cadangan). Last Updated Rudi Hartono berubah dan tidak dipulihkan.
- Kemampuan teknis: membaca isi sel tabel (nilai Last Updated baris Dewi Lestari dan nilai Temporary Until baris Bayu Nugraha dalam format tanggal General Settings aktif); Popup Setup Column untuk menampilkan kolom; seeding API disediakan tim FE/BE (nama endpoint tidak disebut di TC dan PRD, tidak dikarang di spec).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

Parameter Search TC-GS-ROLE-137 (satu iterasi per baris, kata kunci diketik di kotak Search tab itu):

| Tab | Kata kunci | Baris yang cocok | Baris pembanding yang tidak cocok |
|---|---|---|---|
| Total Control | `dew` | `Dewi Lestari` | `Ahmad Fauzi` |
| Read Only | `rin` | `Rina Putri` | `Siti Nurhaliza` |

Parameter Search TC-GS-ROLE-138 (kata kunci per kolom; huruf besar dan kecil mengikuti Data Uji TC untuk Tab Total Control, Tab Read Only memakai nilai baris Read Only):

| Tab | Kolom | Kata kunci | Baris yang tampil |
|---|---|---|---|
| Total Control | Name | `LESTARI` | `Dewi Lestari` |
| Total Control | Position | `manag` | `Ahmad Fauzi` (Position `IT Manager`) |
| Total Control | Division | `fin` | `Dewi Lestari` (Division `Finance`) |
| Total Control | Modified By | `budi` | baris ber-Modified By `Budi S` (dibaca dari tabel sebelum Search) |
| Read Only | Name | `putri` | `Rina Putri` |
| Read Only | Position | `manag` | `Rina Putri` (Position `HR Manager`) |
| Read Only | Division | `hr` | `Rina Putri` (Division `HR`) |
| Read Only | Modified By | `ahmad` | `Siti Nurhaliza` (Modified By `Ahmad F`) |

## Test Steps

### TC-GS-ROLE-137: Siklus interaksi Search Tab Total Control dan Tab Read Only

1. Untuk setiap baris tabel Parameter Search TC-GS-ROLE-137 (langkah 1 sampai 21): klik Tab sesuai kolom Tab
2. Klik icon Search
3. Verifikasi search bar melebar
4. Verifikasi input search mendapat auto-focus
5. Verifikasi placeholder `Search name...`
6. Ketik kata kunci di kotak search tanpa menekan Enter
7. Verifikasi icon (✕) muncul
8. Verifikasi tabel belum tersaring (baris pembanding tampil)
9. Tekan Enter
10. Verifikasi baris yang cocok tampil
11. Verifikasi baris pembanding tidak tampil (tabel hanya memuat baris yang cocok)
12. Klik (✕)
13. Verifikasi input kosong
14. Verifikasi fokus tetap berada di input
15. Verifikasi tabel masih tersaring (baris yang cocok tampil, baris pembanding tidak tampil)
16. Tekan Enter
17. Verifikasi tabel kembali menampilkan semua data (baris yang cocok dan baris pembanding tampil)
18. Ketik kata kunci di kotak search, tekan Enter
19. Klik (←)
20. Verifikasi search bar collapse
21. Verifikasi tabel langsung reset (baris pembanding tampil)

### TC-GS-ROLE-138: Search kolom teks visible Tab Total Control dan Tab Read Only

22. Untuk setiap baris tabel Parameter Search TC-GS-ROLE-138 dengan Tab Total Control (langkah 22 sampai 24): Ketik Search kata kunci kolom, tekan Enter
23. Verifikasi baris pada kolom "Baris yang tampil" tampil
24. Klik `(←)` pada kotak Search
25. Klik Tab Read Only
26. Untuk setiap baris tabel Parameter Search TC-GS-ROLE-138 dengan Tab Read Only (langkah 26 sampai 28): Ketik Search kata kunci kolom, tekan Enter
27. Verifikasi baris pada kolom "Baris yang tampil" tampil
28. Klik `(←)` pada kotak Search

### TC-GS-ROLE-139: Search kolom badge Status, Activation Status, Temporary User di Tab Total Control

29. Klik Tab Total Control
30. Ketik Search `inactive`, tekan Enter
31. Verifikasi baris `Dewi Lestari` tampil
32. Verifikasi setiap baris yang tampil ber-Status `Inactive` (pencarian case-insensitive)
33. Klik `(←)` pada kotak Search
34. Ketik Search `Pending`, tekan Enter (kolom Activation Status Hidden)
35. Verifikasi `No results found` tampil (keyword `Pending` tidak mencocokkan saat kolom Activation Status disembunyikan)
36. Klik `(←)` pada kotak Search
37. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
38. Centang kolom Activation Status
39. Centang kolom Temporary User
40. Klik `[Save]`
41. Ketik Search `Pending`, tekan Enter
42. Verifikasi baris `Rudi Hartono` tampil (Activation Status `Pending Activation`)
43. Ganti isi kotak search dengan `Yes`, tekan Enter
44. Verifikasi baris `Bayu Nugraha` tampil (Temporary User `Yes`)
45. Klik `(←)` pada kotak Search

### TC-GS-ROLE-140: Search kolom TAG saat di-hide dan setelah di-unhide

46. Ketik Search `TG-00451`, tekan Enter (kolom TAG default Hidden)
47. Verifikasi `No results found` tampil
48. Klik `(←)` pada kotak Search
49. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
50. Centang kolom TAG
51. Klik `[Save]`
52. Ketik Search `TG-00451`, tekan Enter
53. Verifikasi baris `Ahmad Fauzi` tampil
54. Klik `(←)` pada kotak Search

### TC-GS-ROLE-141: Search tidak mencocokkan kolom tanggal Last Updated dan Temporary Until

55. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
56. Centang kolom Temporary Until
57. Klik `[Save]`
58. Baca nilai Last Updated baris `Dewi Lestari` dan nilai Temporary Until baris `Bayu Nugraha` dari tabel (format tampil)
59. Ketik Search nilai Last Updated baris `Dewi Lestari` yang dibaca pada langkah 58, tekan Enter
60. Verifikasi `No results found` tampil
61. Ganti isi kotak search dengan nilai Temporary Until baris `Bayu Nugraha` yang dibaca pada langkah 58, tekan Enter
62. Verifikasi `No results found` tampil
63. Klik `(←)` pada kotak Search
64. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
65. Klik `[Reset to Default]`
66. Klik `[Save]`
67. Klik Filter
68. Verifikasi Filter Panel menyediakan field Last Updated dan Temporary Until (penyaringan tanggal hanya lewat Filter Panel)

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per baris tabel parameter (Prerequisites): TC-GS-ROLE-137 langkah 1 sampai 21 (2 iterasi: Tab Total Control dan Tab Read Only); TC-GS-ROLE-138 langkah 22 sampai 24 (4 iterasi Tab Total Control) dan langkah 26 sampai 28 (4 iterasi Tab Read Only).
- Langkah penghubung (aksi tanpa `Verifikasi`): berpindah tab (langkah 25 dan 29), mengosongkan Search lewat `(←)`, menampilkan kolom lewat Popup Setup Column (langkah 40, 51, 57), membaca nilai sel (langkah 58), dan memulihkan kolom ke bawaan (langkah 64 sampai 66). Kolom tidak dipulihkan di antara TC-GS-ROLE-139, 140, dan 141 karena tiap TC hanya menambah kolom yang diuji; pemulihan dilakukan sekali sesudah TC-GS-ROLE-141.
- Spec melewati sekitar 35 langkah (68 langkah nominal, sekitar 107 dengan ekspansi perulangan) karena lima TC menguji Search pada tabel yang sama (dua tab) dan tiap kolom, tiap tab, dan tiap klausa Expected menjadi langkah sendiri (S-01). Seluruh blok satu kelas harness (fungsional), satu aktor, satu dataset (Tab Total Control dan Tab Read Only), tanpa aksi yang mengubah data kecuali tampilan kolom; tiap blok mengosongkan Search di akhir dan berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Anchor absence (bagian 8b butir 2): `No results found` hasil Search adalah anchor sah untuk absence hasil Search (langkah TC-GS-ROLE-139, 140, 141). Asersi universal ("hanya baris yang cocok", "setiap baris ber-Status Inactive") didahului baris pembanding atau baris yang cocok yang tampil.
- Temuan untuk QA:
  - TC-GS-ROLE-138 baris Tab Read Only: Data Uji hanya menyebut "nilai baris Read Only" tanpa nilai konkret; spec memakai `putri` (Name), `manag` (Position), `hr` (Division), dan `ahmad` (Modified By `Ahmad F`, dari TC-GS-ROLE-144 g).
  - TC-GS-ROLE-138 Expected d: baris ber-Modified By `Budi S` tidak disebut namanya; spec membaca baris itu dari tabel sebelum Search.
  - TC-GS-ROLE-139 Expected a menyebut "Dewi Lestari dan user Inactive lain", sedangkan TC-GS-ROLE-144 Expected c menyebut Inactive hanya Dewi Lestari; spec mengasersi Dewi Lestari tampil dan setiap baris hasil ber-Status `Inactive`.
  - TC-GS-ROLE-139 Expected b membutuhkan Rudi Hartono sebagai Total Control (Pending Activation); kondisi itu berasal dari TC-GS-ROLE-59 dan disiapkan lewat seeding.
  - TC-GS-ROLE-141 tidak menyebut nilai tanggal dan tidak menyebut bahwa kolom Temporary Until perlu ditampilkan lebih dulu; spec membaca nilai dari tabel sesudah menampilkan kolom.
  - TC-GS-ROLE-141 Expected b ("Penyaringan tanggal hanya lewat Filter Panel") adalah pernyataan aturan tanpa langkah observasi; spec mengasersinya sebagai ketersediaan field Last Updated dan Temporary Until di Filter Panel.
