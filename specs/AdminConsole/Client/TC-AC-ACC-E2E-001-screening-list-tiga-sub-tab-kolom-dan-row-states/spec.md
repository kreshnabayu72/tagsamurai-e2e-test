---
id: TC-AC-ACC-E2E-001-screening-list-tiga-sub-tab-kolom-dan-row-states
title: "Screening List Client: Tiga Sub-tab, Kolom Default, Urutan A-Z, dan Row States"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-1
  - TC-AC-ACC-2
  - TC-AC-ACC-3
  - TC-AC-ACC-4
  - TC-AC-ACC-7
  - TC-AC-ACC-8
  - TC-AC-ACC-19
coverage:
  web: automated
---

# Screening List Client: Tiga Sub-tab, Kolom Default, Urutan A-Z, dan Row States

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Mode tidak memakai intercept, jam server, atau klien HTTP. Spec read-only atas Client Pre-setup; satu-satunya state yang diubah adalah centang baris dan kotak Search, dipulihkan dalam spec (langkah penghubung).
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-1: Screening List Client sub-tab Active

1. Amati header halaman (sesi Total Control dari hook `before`, List dibuka hook `beforeEach`)
2. Verifikasi Breadcrumb `Client` satu segmen
3. Verifikasi tidak ada Page Title Header terpisah
4. Verifikasi sub-tab `Active`, `Suspended`, `Archived` tampil berurutan
5. Verifikasi sub-tab `Active` aktif (underline primary, teks bold)
6. Verifikasi masing-masing sub-tab disertai badge jumlah Client
7. Verifikasi Table Tools menampilkan `Search`, `Filter`, `Download`, `Changelog`, `[+ New Client]`
8. Verifikasi placeholder Search `Search by company name, client code, or PIC name...`
9. Amati header kolom tabel
10. Verifikasi kolom tabel berurutan: `Checkbox`, `Company Name`, `Client Code`, `PIC Name`, `Managed By`, `Group`, `FAMS`, `SAMS`, `SIEM`, `Modified By`, `Last Updated`, `Column Visibility (⋯)`
11. Verifikasi header kolom `Company Name`, `Client Code`, `PIC Name`, `Managed By`, `Group`, `FAMS`, `SAMS`, `SIEM`, `Modified By`, `Last Updated` sortable dan `Column Visibility (⋯)` tidak sortable
12. Klik header kolom `Column Visibility (⋯)`
13. Verifikasi Overlay Column Visibility terbuka dengan CTA `[Setup Column]` di dalamnya
14. Tutup Overlay Column Visibility
15. Verifikasi sedikitnya satu baris tampil pada tabel
16. Verifikasi baris default terurut `Company Name` A-Z (case-insensitive)
17. Amati panel kanan Sidebar Group Tree
18. Verifikasi header `Groups` tampil tanpa tombol close
19. Verifikasi panel dapat di-collapse lewat floating handle di tepi panel
20. Verifikasi input `Search groups...` tampil
21. Verifikasi ikon hierarchy toggle tampil
22. Verifikasi opsi `[All Groups]` terpilih
23. Amati footer tabel
24. Verifikasi Pagination tampil
25. Verifikasi Pagination default 10 baris per halaman

### TC-AC-ACC-2: Screening List Client sub-tab Suspended

26. Klik sub-tab `Suspended`
27. Verifikasi sub-tab `Suspended` aktif dengan `Active` dan `Archived` tidak aktif
28. Verifikasi Table Tools menampilkan `Search`, `Filter`, `Download`, `Changelog`, `[+ New Client]`
29. Verifikasi kolom tabel sama dengan sub-tab `Active`: `Checkbox`, `Company Name`, `Client Code`, `PIC Name`, `Managed By`, `Group`, `FAMS`, `SAMS`, `SIEM`, `Modified By`, `Last Updated`, `Column Visibility (⋯)`
30. Verifikasi kolom `Checkbox` tampil
31. Ketik Search `PT Wahana Nusantara`, tekan Enter
32. Verifikasi baris `PT Wahana Nusantara` tampil
33. Verifikasi baris Client Suspended tampil dengan teks muted
34. Klik `(←)` pada kotak Search
35. Verifikasi Pagination default 10 baris per halaman

### TC-AC-ACC-3: Screening List Client sub-tab Archived

36. Klik sub-tab `Archived`
37. Verifikasi sub-tab `Archived` aktif dengan `Active` dan `Suspended` tidak aktif
38. Verifikasi Table Tools menampilkan `Search`, `Filter`, `Download`, `Changelog`, `[+ New Client]`
39. Verifikasi kolom `Checkbox` tidak tersedia
40. Verifikasi kolom data sama dengan sub-tab `Active`: `Company Name`, `Client Code`, `PIC Name`, `Managed By`, `Group`, `FAMS`, `SAMS`, `SIEM`, `Modified By`, `Last Updated`, `Column Visibility (⋯)`
41. Ketik Search `PT Karya Abadi`, tekan Enter
42. Verifikasi baris `PT Karya Abadi` tampil
43. Verifikasi baris Archived tampil dengan background netral/muted dan teks muted
44. Ganti isi kotak Search dengan `PT Lama Tak Berbayar`, tekan Enter
45. Verifikasi baris `PT Lama Tak Berbayar` tampil
46. Klik `(←)` pada kotak Search
47. Verifikasi Pagination default 10 baris per halaman

### TC-AC-ACC-4: Sub-tab default Active saat pertama membuka halaman Client

48. Klik item `Client` pada sidebar Admin Console
49. Verifikasi sub-tab `Active` terpilih (underline primary, teks bold)
50. Ketik Search `PT Wahana Nusantara`, tekan Enter
51. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, sehingga Client Suspended tidak ada di tabel `Active`
52. Klik `(←)` pada kotak Search
53. Verifikasi sedikitnya satu baris tampil pada tabel `Active`

### TC-AC-ACC-7: Kolom default Visible dan kolom Hidden default

54. Klik ikon Column Visibility `(⋯)` di header kolom terakhir
55. Verifikasi kolom Visible default pada header tabel: `Company Name`, `Client Code`, `PIC Name`, `Managed By`, `Group`, `FAMS`, `SAMS`, `SIEM`, `Modified By`, `Last Updated`
56. Verifikasi Overlay Column Visibility menampilkan kolom Curated `Company Email`, `PIC Email`, `PIC Phone`, `Industry`, `Country`, `State`, `City` belum dicentang
57. Verifikasi checkbox kolom `Company Name`, `Client Code`, `PIC Name`, `Managed By`, `Group`, `FAMS`, `SAMS`, `SIEM`, `Modified By`, `Last Updated`, `Company Email`, `PIC Email`, `PIC Phone`, `Industry`, `Country`, `State`, `City` enabled sehingga dapat di-hide/unhide
58. Tutup Overlay Column Visibility

### TC-AC-ACC-8: Urutan default Company Name A-Z tanpa membedakan huruf besar-kecil

59. Verifikasi sedikitnya satu baris tampil pada sub-tab `Active`
60. Verifikasi baris sub-tab `Active` terurut `Company Name` ascending case-insensitive
61. Verifikasi indikator sort aktif pada header `Company Name`
62. Klik sub-tab `Suspended`
63. Verifikasi sedikitnya satu baris tampil pada sub-tab `Suspended`
64. Verifikasi baris sub-tab `Suspended` terurut `Company Name` ascending case-insensitive
65. Klik sub-tab `Archived`
66. Verifikasi sedikitnya satu baris tampil pada sub-tab `Archived`
67. Verifikasi baris sub-tab `Archived` terurut `Company Name` ascending case-insensitive

### TC-AC-ACC-19: Row states Suspended muted, Archived background netral, Hover dan Selected

68. Klik sub-tab `Suspended`
69. Verifikasi sedikitnya satu baris tampil pada sub-tab `Suspended`
70. Verifikasi baris Suspended menampilkan teks muted
71. Klik sub-tab `Archived`
72. Verifikasi sedikitnya satu baris tampil pada sub-tab `Archived`
73. Verifikasi baris Archived menampilkan background netral/muted dan teks muted
74. Klik sub-tab `Active`
75. Arahkan kursor ke baris pertama sub-tab `Active`
76. Verifikasi baris pertama menampilkan state Hover
77. Centang checkbox baris pertama
78. Verifikasi baris pertama menampilkan state Selected
79. Hapus centang checkbox baris pertama dan pindahkan kursor dari baris

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 14, 31, 34, 41, 44, 46, 50, 52, 58, 79. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Pembagian TC lintas spec: TC-AC-ACC-5, 6, 23, dan 24 (badge dan empty state hasil pencarian) ada di spec 002; TC-AC-ACC-9, 10, 16, 17, dan 929 (isi sel) di spec 003.
- Penyimpangan urutan (S-05): TC-AC-ACC-4 ditaruh sesudah TC-AC-ACC-3 karena membuka halaman lewat sidebar mengembalikan sub-tab ke `Active` dari sub-tab `Archived` (klik sidebar mereset state List, bagian 4 konvensi).
- Asersi tambahan (S-03): pada TC-AC-ACC-4, Expected "hanya Client berstatus Active" diamati dengan mencari `PT Wahana Nusantara` (Client Suspended) yang harus menghasilkan empty state `No results found`; pada TC-AC-ACC-1, klik header `Column Visibility (⋯)` (langkah 12–14) dilakukan karena Expected TC-AC-ACC-1 butir b.i menyebut perilaku klik header.
- Pada TC-AC-ACC-2 dan 3, Expected "baris X tampil" diamati lewat Search nama Client karena sub-tab berpaginasi 10 baris dan populasi fixture A3 menambah baris (aturan isolasi hitungan Tabel A3).
- Ukuran spec (79 langkah, melewati sekitar 35 langkah): satu dataset (Client Pre-setup), tanpa aksi tulis, dan tiap blok TC berdiri sendiri (sub-tab dipilih eksplisit di awal blok) sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-8: Data Uji menyebut "Nama Client dengan huruf kecil/besar campur pada Pre-setup", tetapi Tabel A2 dan A3 tidak memuat nama berhuruf kecil di awal; urutan case-insensitive tidak dapat dibedakan dari urutan case-sensitive dengan data yang ada. Spec mengasersi urutan ascending sesuai TC.
  - TC-AC-ACC-19: Expected butir c "state visual masing-masing" untuk Hover dan Selected tidak menyebut wujud visualnya; spec hanya mengasersi state Hover dan state Selected tampil.
  - TC-AC-ACC-1: kolom Checkbox dan `[+ New Client]` diasersi ada untuk Total Control; angka badge sub-tab tidak diasersi absolut (populasi dinamis, aturan Tabel A3).
