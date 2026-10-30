---
id: TC-GS-ROLE-E2E-052-filter-fungsional-multi-select-date-range-dan-urutan-search-filter
title: "Filter Fungsional: Multi-Select per Field, Date Range, OR dan AND, serta Urutan Search dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-144
  - TC-GS-ROLE-145
  - TC-GS-ROLE-147
  - TC-GS-ROLE-151
coverage:
  web: automated
---

# Filter Fungsional: Multi-Select per Field, Date Range, OR dan AND, serta Urutan Search dan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login di hook `before`): Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD` (sudah terdaftar). Tidak ada env baru.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control (Search, Filter, dan kolom tabel dalam keadaan bawaan).
- Data Pre-setup yang dipakai (Tabel Data Uji Pre-setup; hanya dibaca): Tab Total Control berisi Ahmad Fauzi (IT Manager, IT, Active), Budi Santoso (Default User, Active, Last Updated `—`), Dewi Lestari (Staff, Finance, Inactive), dan Bayu Nugraha (baris 19, Temporary User, Temporary Until terisi). Tab Read Only berisi Siti Nurhaliza (Finance Staff, Finance, Active, Last Updated 12 Jun, Modified By `Ahmad F`), Rina Putri (HR Manager, HR, Inactive, Last Updated 3 Jun), dan Intan Permata (baris 19, Temporary User). Kolom Position, Division, Status, dan Last Updated punya sedikitnya dua nilai distinct pada tiap tab (S-11).
- Given (hook `before`, lewat seeding API): Rudi Hartono (Pending Activation, Tabel Data Uji Pre-setup baris 11) di-assign Total Control (setara TC-GS-ROLE-59, hanya untuk Rudi Hartono). Dipakai oleh TC-GS-ROLE-144 (Activation Status).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): cabut Total Control Rudi Hartono (kembali ke state kandidat tanpa access level, Pre-setup baris 11); kolom Temporary Until dikembalikan lewat `[Reset to Default]` (langkah 31 sampai 33); filter dan Search dibersihkan di akhir tiap blok (hook `after` sebagai cadangan). Last Updated Rudi Hartono berubah dan tidak dipulihkan.
- Kemampuan teknis: membaca isi sel tabel (Last Updated dan Temporary Until dalam format tanggal General Settings aktif, Modified By); mengisi date range picker dengan rentang tanggal; Popup Setup Column untuk menampilkan kolom; seeding API disediakan tim FE/BE (nama endpoint tidak disebut di TC dan PRD, tidak dikarang di spec).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

Data uji TC-GS-ROLE-144 Tab Total Control (satu iterasi per baris; field diisi satu opsi, lalu Apply):

| Field | Opsi | Baris yang tampil | Baris yang tidak tampil |
|---|---|---|---|
| Position | `IT Manager` | `Ahmad Fauzi` | `Dewi Lestari` |
| Division | `Finance` | `Dewi Lestari` | `Ahmad Fauzi` |
| Status | `Inactive` | `Dewi Lestari` | `Budi Santoso` (Default User, Status `Active`), `Ahmad Fauzi` |
| Status | `Active` | `Ahmad Fauzi`, `Budi Santoso` (Default User) | `Dewi Lestari` |
| Activation Status | `Pending Activation` | `Rudi Hartono` | `Ahmad Fauzi` |
| Temporary User | `Yes` | `Bayu Nugraha` | `Ahmad Fauzi` |
| Modified By | `Budi S` | baris ber-Modified By `Budi S` (dibaca dari tabel sebelum filter) | baris ber-Modified By selain `Budi S` |

Data uji TC-GS-ROLE-144 Tab Read Only:

| Field | Opsi | Baris yang tampil | Baris yang tidak tampil |
|---|---|---|---|
| Position | `HR Manager` | `Rina Putri` | `Siti Nurhaliza` |
| Status | `Active` | `Siti Nurhaliza` | `Rina Putri` |
| Modified By | `Ahmad F` | `Siti Nurhaliza` | `Rina Putri` |

## Test Steps

### TC-GS-ROLE-144: Filter multi-select per field Tab Total Control dan Tab Read Only

1. Untuk setiap baris tabel Data uji TC-GS-ROLE-144 Tab Total Control (langkah 1 sampai 5): klik Filter, lalu klik `[Clear Field]`
2. Pada field kolom Field pilih opsi pada kolom Opsi
3. Klik `[Apply]`
4. Verifikasi baris pada kolom "Baris yang tampil" tampil
5. Verifikasi hanya baris dengan nilai field sama dengan opsi yang tampil, dan baris pada kolom "Baris yang tidak tampil" tidak tampil
6. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`
7. Klik Tab Read Only
8. Untuk setiap baris tabel Data uji TC-GS-ROLE-144 Tab Read Only (langkah 8 sampai 12): klik Filter, lalu klik `[Clear Field]`
9. Pada field kolom Field pilih opsi pada kolom Opsi
10. Klik `[Apply]`
11. Verifikasi baris pada kolom "Baris yang tampil" tampil
12. Verifikasi hanya baris dengan nilai field sama dengan opsi yang tampil, dan baris pada kolom "Baris yang tidak tampil" tidak tampil
13. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-ROLE-145: Filter date range Last Updated dan Temporary Until

14. Klik Tab Total Control
15. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
16. Centang kolom Temporary Until
17. Klik `[Save]`
18. Baca nilai Last Updated baris `Dewi Lestari` dan nilai Temporary Until baris `Bayu Nugraha` dari tabel (format tampil)
19. Klik Filter
20. Pada field Last Updated pilih rentang tanggal dari nilai Last Updated baris `Dewi Lestari` sampai tanggal yang sama
21. Klik `[Apply]`
22. Verifikasi baris `Dewi Lestari` tampil
23. Verifikasi hanya baris dengan Last Updated di dalam rentang yang tampil
24. Verifikasi baris `Budi Santoso` (Default User, Last Updated `—`) tidak tampil
25. Klik Filter, lalu klik `[Clear Field]`
26. Pada field Temporary Until pilih rentang tanggal yang memuat nilai Temporary Until baris `Bayu Nugraha`
27. Klik `[Apply]`
28. Verifikasi baris `Bayu Nugraha` tampil
29. Verifikasi hanya baris Temporary User dengan Temporary Until di dalam rentang yang tampil
30. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`
31. Buka Popup Setup Column lewat header Column Visibility (⋯) lalu `Setup Column...`
32. Klik `[Reset to Default]`
33. Klik `[Save]`
34. Klik Tab Read Only
35. Baca nilai Last Updated baris `Rina Putri` dari tabel (format tampil)
36. Klik Filter
37. Pada field Last Updated pilih rentang tanggal dari nilai Last Updated baris `Rina Putri` sampai tanggal yang sama
38. Klik `[Apply]`
39. Verifikasi baris `Rina Putri` tampil
40. Verifikasi hanya baris Read Only dengan Last Updated di dalam rentang yang tampil
41. Verifikasi baris `Siti Nurhaliza` (Last Updated berbeda) tidak tampil
42. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-ROLE-147: Filter OR dalam satu field dan AND antar field

43. Klik Tab Total Control
44. Klik Filter, lalu klik `[Clear Field]`
45. Pada field Division pilih `Finance` dan `IT`
46. Klik `[Apply]`
47. Verifikasi baris `Dewi Lestari` (Division `Finance`) tampil
48. Verifikasi baris `Ahmad Fauzi` (Division `IT`) tampil
49. Verifikasi hanya baris ber-Division `Finance` atau `IT` yang tampil
50. Klik Filter
51. Pada field Status pilih `Active`
52. Klik `[Apply]`
53. Verifikasi baris `Ahmad Fauzi` tampil
54. Verifikasi baris `Dewi Lestari` (Division `Finance`, Status `Inactive`) tidak tampil
55. Verifikasi hanya baris ber-Division `Finance` atau `IT` dan ber-Status `Active` yang tampil
56. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-ROLE-151: Search lalu Filter dan Filter lalu Search

57. Klik Tab Read Only
58. Ketik Search `a`, tekan Enter
59. Klik Filter
60. Pada field Division pilih `Finance`
61. Pada field Status pilih `Active`
62. Klik `[Apply]`
63. Verifikasi baris `Siti Nurhaliza` tampil
64. Verifikasi hanya baris ber-Name mengandung `a`, ber-Division `Finance`, dan ber-Status `Active` yang tampil
65. Verifikasi kotak Search tetap berisi `a`
66. Klik `(←)` pada kotak Search
67. Klik Filter, klik `[Clear Field]`, lalu klik `[Apply]`
68. Klik Filter
69. Pada field Division pilih `Finance`
70. Pada field Status pilih `Active`
71. Klik `[Apply]`
72. Ketik Search `a`, tekan Enter
73. Verifikasi baris `Siti Nurhaliza` tampil
74. Verifikasi hanya baris ber-Name mengandung `a`, ber-Division `Finance`, dan ber-Status `Active` yang tampil
75. Klik Filter
76. Verifikasi chip Division `Finance` dan chip Status `Active` tetap tampil di Filter Panel (filter tetap aktif)
77. Klik `[Clear Field]`, lalu klik `[Apply]`
78. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per baris tabel data uji: TC-GS-ROLE-144 langkah 1 sampai 5 (7 iterasi Tab Total Control) dan langkah 8 sampai 12 (3 iterasi Tab Read Only).
- Langkah penghubung (aksi tanpa `Verifikasi`): berpindah tab (langkah 7, 14, 34, 43, 57), menampilkan dan memulihkan kolom Temporary Until (langkah 17 dan 31 sampai 33), membaca nilai sel (langkah 18 dan 35), serta membersihkan filter dan Search (langkah 6, 13, 25, 30, 42, 56, 66, 78). Langkah "Klik Filter, lalu klik `[Clear Field]`" di awal tiap iterasi TC-GS-ROLE-144 membersihkan filter iterasi sebelumnya.
- Spec melewati sekitar 35 langkah (78 langkah nominal, sekitar 118 dengan ekspansi perulangan) karena empat TC menguji Filter Panel yang sama pada dua tab dan tiap field, tiap tab, dan tiap klausa Expected menjadi langkah sendiri (S-01). Seluruh blok satu kelas harness (fungsional), satu aktor, satu dataset; tiap blok membersihkan filter dan Search yang dibuatnya sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Asersi universal ("hanya baris ...") didahului baris yang cocok yang tampil (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-ROLE-144 Expected f: baris ber-Modified By `Budi S` tidak disebut namanya; spec membaca baris itu dari tabel sebelum filter.
  - TC-GS-ROLE-144 Expected g (Tab Read Only): "Status Active → hanya Siti Nurhaliza" dan "Modified By Ahmad F → hanya Siti Nurhaliza" bertentangan dengan Pre-setup baris 19 yang menambahkan Intan Permata (Read Only, Active, Temporary User) ke Tab Read Only; spec mengikuti TC dan menandai Rina Putri sebagai baris yang tidak tampil. Bila Intan Permata ikut tampil, asersi "hanya" gagal.
  - TC-GS-ROLE-144 Expected c menyebut Inactive hanya Dewi Lestari, sedangkan TC-GS-ROLE-139 menyebut "Dewi Lestari dan user Inactive lain"; spec mengikuti TC-GS-ROLE-144 pada spec ini.
  - TC-GS-ROLE-145 tidak menyebut tanggal konkret; spec membaca Last Updated baris Dewi Lestari, Temporary Until baris Bayu Nugraha, dan Last Updated baris Rina Putri dari tabel. Kolom Temporary Until perlu ditampilkan lebih dulu dan TC tidak menyebutnya.
  - TC-GS-ROLE-151 tidak menyebut tab; spec memakai Tab Read Only karena irisan Name `a`, Division `Finance`, dan Status `Active` hanya terjamin berisi Siti Nurhaliza di sana. Langkah "Reset" pada TC-GS-ROLE-151 Langkah 2 tidak dijelaskan; spec menulisnya sebagai `(←)` pada Search dan `[Clear Field]` lalu `[Apply]`.
