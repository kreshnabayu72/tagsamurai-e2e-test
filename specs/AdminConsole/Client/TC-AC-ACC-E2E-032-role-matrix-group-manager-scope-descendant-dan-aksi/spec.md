---
id: TC-AC-ACC-E2E-032-role-matrix-group-manager-scope-descendant-dan-aksi
title: "Role Matrix: Group Manager (Scope Area Jakarta dan Descendant) pada Tree, List, per Sub-tab, dan Table Tools"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-47
  - TC-AC-ACC-48
  - TC-AC-ACC-563
  - TC-AC-ACC-582
  - TC-AC-ACC-562
  - TC-AC-ACC-561
coverage:
  web: automated
---

# Role Matrix: Group Manager (Scope Area Jakarta dan Descendant) pada Tree, List, per Sub-tab, dan Table Tools

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-03 | Group Manager (Principal, scope Area Jakarta + seluruh descendant) | `groupManagerJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_GM_PASSWORD` |

- Login di hook `before` spec ini (Group Manager, A-03); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Fixture A3 residen `C-ROL-5` `PT Suspend Menteng` (Suspended, Group `Cabang Menteng`, tanpa riwayat subscription), `C-ROL-6` `PT Arsip Menteng` (Archived, Group `Cabang Menteng`), dan Pre-setup `C-09` `PT Baru Daftar`, `C-03` `PT Wahana Nusantara`, `C-04` `PT Karya Abadi`, `C-12` `PT Timur Perkasa`, `C-14` `PT Uji Halaman 01…30` hanya dibaca. Group Manager di-assign pada `Area Jakarta`; `Cabang Menteng` adalah descendant.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-47: Group Manager: CRUD penuh pada group yang di-assign dan seluruh descendant

1. Klik ikon hierarchy toggle (expand all) pada Sidebar Group Tree
2. Lihat Sidebar Group Tree
3. Verifikasi node `Area Jakarta` dan descendant `Cabang Menteng` aktif dan dapat dipilih
4. Verifikasi ancestor `Regional Barat` greyed out
5. Ketik Search `PT Baru Daftar`, tekan Enter
6. Buka `⋯` baris `PT Baru Daftar` (Group `Cabang Menteng`)
7. Verifikasi Client di descendant `PT Baru Daftar` tampil
8. Verifikasi elemen tulis `[+ New Client]`, kolom Checkbox, serta `Edit`, `Suspend`, `Change Partner`, dan `Delete` pada menu `⋯` tampil dalam scope
9. Tutup menu `⋯`

### TC-AC-ACC-48: Group Manager: Client di luar group assignment tidak tampil (zero access)

10. Ganti isi kotak Search dengan `Timur Perkasa`, tekan Enter
11. Lihat Sidebar Group Tree
12. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (`PT Timur Perkasa`, Area Surabaya, tidak tampil)
13. Verifikasi node `Regional Timur` dan `Area Surabaya` tidak muncul di tree (hidden total)

### TC-AC-ACC-563: Group Manager dengan [All Groups]: Client di node assignment dan descendant tampil, di luar node tidak tampil

14. Pastikan `[All Groups]` terpilih di Sidebar Group Tree
15. Ganti isi kotak Search dengan `PT Baru Daftar`, tekan Enter
16. Verifikasi baris `PT Baru Daftar` (Group `Cabang Menteng`, descendant dari `Area Jakarta`) tampil
17. Ganti isi kotak Search dengan `PT Sejahtera Abadi`, tekan Enter
18. Verifikasi baris `PT Sejahtera Abadi` (Group `Area Jakarta`) tampil
19. Ganti isi kotak Search dengan `PT Timur Perkasa`, tekan Enter
20. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (`PT Timur Perkasa` berada di Area Surabaya)
21. Ganti isi kotak Search dengan `PT Uji Halaman 01`, tekan Enter
22. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.` (`PT Uji Halaman 01` berada di Regional Timur)
23. Klik `(←)` pada kotak Search

### TC-AC-ACC-582: Group Manager: Download dan Changelog List tampil dan berfungsi

24. Lihat Table Tools di sub-tab `Active`
25. Verifikasi Table Tools `Search`, `Filter`, `Download`, `Changelog`, `[+ New Client]` tampil
26. Klik `Download`
27. Verifikasi overlay Download menampilkan opsi `Download as CSV` dan `Download as XLSX`
28. Tutup overlay Download
29. Klik `Changelog`
30. Verifikasi modal dengan Title `Changelog: Client` terbuka
31. Tutup modal Changelog

### TC-AC-ACC-562: Group Manager pada sub-tab Suspended: Unsuspend tampil dan Delete menurut riwayat subscription

32. Klik sub-tab `Suspended`
33. Lihat tree Sidebar dan kolom tabel
34. Verifikasi `Area Jakarta` dan `Cabang Menteng` aktif
35. Verifikasi `Regional Barat` greyed out
36. Verifikasi `Area Surabaya` tidak tampil
37. Ketik Search `PT Suspend Menteng`, tekan Enter
38. Verifikasi baris `PT Suspend Menteng` tampil
39. Verifikasi kolom Checkbox tampil
40. Buka `⋯` baris `PT Suspend Menteng`
41. Verifikasi menu `⋯` `PT Suspend Menteng` memuat `Detail`, `Unsuspend`, dan `Delete`
42. Tutup menu `⋯` dan ganti isi kotak Search dengan `PT Wahana Nusantara`, tekan Enter
43. Verifikasi baris `PT Wahana Nusantara` tampil
44. Buka `⋯` baris `PT Wahana Nusantara`
45. Verifikasi menu `⋯` `PT Wahana Nusantara` memuat `Detail` dan `Unsuspend`
46. Verifikasi `Delete` tidak ada karena sudah pernah memiliki subscription
47. Tutup menu `⋯` dan klik `(←)` pada kotak Search

### TC-AC-ACC-561: Group Manager pada sub-tab Archived: Edit dan Delete tampil

48. Klik sub-tab `Archived`
49. Lihat tree Sidebar dan kolom tabel
50. Verifikasi `Area Jakarta` dan `Cabang Menteng` aktif
51. Verifikasi `Regional Barat` greyed out
52. Verifikasi `Area Surabaya` tidak tampil
53. Ketik Search `PT Arsip Menteng`, tekan Enter
54. Verifikasi baris `PT Arsip Menteng` tampil
55. Verifikasi kolom Checkbox tidak tersedia
56. Buka `⋯` baris `PT Arsip Menteng`
57. Verifikasi menu `⋯` `PT Arsip Menteng` memuat `Detail`, `Edit`, dan `Delete`
58. Tutup menu `⋯` dan ganti isi kotak Search dengan `PT Karya Abadi`, tekan Enter
59. Verifikasi baris `PT Karya Abadi` tampil
60. Buka `⋯` baris `PT Karya Abadi`
61. Verifikasi menu `⋯` `PT Karya Abadi` memuat `Detail`, `Edit`, dan `Delete`
62. Tutup menu `⋯`, klik `(←)` pada kotak Search, lalu klik sub-tab `Active`

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 5, 9, 23, 31, 37, 42, 47, 53, 58, 62. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): TC-AC-ACC-47, 48, 563, 582, 562, 561 (semula 47, 48, 561, 562, 563, 582); blok sub-tab `Active` didahulukan lalu `Suspended` dan `Archived` agar perpindahan sub-tab minimal.
- Asersi `Verifikasi` hidden total di tree TC-AC-ACC-48 didahului tree yang sudah ter-expand dan `Area Jakarta` aktif (anchor positif) dari langkah 2 sampai 3 TC-AC-ACC-47; empty state hasil Search menjadi anchor positif untuk asersi absence Client.
- Pembagian TC lintas spec: pola ancestor-disabled aktor Active-Read dan union multi-node di spec 033; defense tulis di luar scope (TC-AC-ACC-454, 987) di spec 035.
- Ukuran spec (62 langkah, melewati sekitar 35 langkah): satu akun (Group Manager), satu topik (scope Group dan descendant), tanpa aksi tulis, dan tiap blok TC dimulai dari state eksplisit (Search atau sub-tab) sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-47: nama TC menyebut "CRUD penuh", tetapi langkah dan Expected hanya mengamati keberadaan elemen tulis; spec tidak menjalankan Create, Edit, Suspend, Change Partner, atau Delete.
  - TC-AC-ACC-47: langkah TC "Lihat Sidebar Group Tree" tidak meng-expand tree, sementara Expected butir a menyebut descendant `Cabang Menteng` aktif; spec menambah langkah expand all (penghubung) agar descendant teramati.
