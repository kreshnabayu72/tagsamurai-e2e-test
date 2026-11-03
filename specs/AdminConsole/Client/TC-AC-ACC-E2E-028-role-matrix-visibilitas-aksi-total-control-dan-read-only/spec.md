---
id: TC-AC-ACC-E2E-028-role-matrix-visibilitas-aksi-total-control-dan-read-only
title: "Role Matrix: Visibilitas Elemen dan Aksi List dan Detail untuk Total Control dan Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-45
  - TC-AC-ACC-577
  - TC-AC-ACC-46
  - TC-AC-ACC-57
  - TC-AC-ACC-581
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen dan Aksi List dan Detail untuk Total Control dan Read Only

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| A-02 | Read Only (Principal) | `readOnlyPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_RO_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Pre-setup `C-01` `PT Sejahtera Abadi` (Active; Station `Gerbang Gudang A` dengan Tablet `Tablet Lobi 1` Active), `C-02` `PT Teknologi Maju` (Default User Not Yet Activated), `C-04` `PT Karya Abadi` (Archived), `C-09` `PT Baru Daftar` (Active, belum pernah memiliki subscription), dan `C-14` `PT Uji Halaman 01…30` hanya dibaca.
- Filter, Sort, Search, dan halaman aktif yang diubah blok Read Only dipulihkan dalam spec (langkah penghubung).
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-45: Total Control: seluruh elemen aksi tampil di sub-tab Active

1. Lihat toolbar dan kolom Checkbox
2. Ketik Search `PT Sejahtera Abadi`, tekan Enter
3. Buka `⋯` pada baris `PT Sejahtera Abadi`
4. Verifikasi tampil: `[+ New Client]`
5. Verifikasi tampil: kolom Checkbox
6. Verifikasi tampil: `Download` dan `Changelog`
7. Verifikasi menu `⋯` baris `PT Sejahtera Abadi` pada sub-tab `Active` memuat `Detail`, `Edit`, `Change Partner`, dan `Suspend`
8. Verifikasi `Unsuspend` tidak ada di menu `⋯` baris `PT Sejahtera Abadi`
9. Verifikasi `Delete` tidak ada pada baris `PT Sejahtera Abadi` (memiliki riwayat subscription)
10. Tutup menu `⋯` dan klik `(←)` pada kotak Search
11. Ketik Search `PT Baru Daftar`, tekan Enter
12. Buka `⋯` pada baris `PT Baru Daftar`
13. Verifikasi menu `⋯` baris `PT Baru Daftar` memuat `Detail`, `Edit`, `Change Partner`, `Suspend`, dan `Delete`
14. Verifikasi `Unsuspend` tidak ada di menu `⋯` baris `PT Baru Daftar`
15. Tutup menu `⋯` dan klik `(←)` pada kotak Search

### TC-AC-ACC-577: Total Control pada sub-tab Archived: menu ⋯ memuat Detail, Edit, Delete

16. Klik sub-tab `Archived`
17. Ketik Search `PT Karya Abadi`, tekan Enter
18. Buka `⋯` baris `PT Karya Abadi`
19. Verifikasi menu `⋯` `PT Karya Abadi` memuat `Detail`, `Edit`, dan `Delete`
20. Verifikasi aksi `Change Partner`, `Suspend`, dan `Unsuspend` tidak ada di menu
21. Tutup menu `⋯`, klik `(←)` pada kotak Search, lalu klik sub-tab `Active`
22. Logout dari akun Total Control
23. Login sebagai Read Only (A-02)

### TC-AC-ACC-46: Read Only: hanya Detail dan Download/Changelog; aksi tulis Hidden

24. Lihat toolbar dan kolom Checkbox
25. Ketik Search `PT Sejahtera Abadi`, tekan Enter
26. Buka `⋯` baris `PT Sejahtera Abadi`
27. Verifikasi `[+ New Client]` Hidden
28. Verifikasi kolom Checkbox dan Bulk Action Bar Hidden
29. Verifikasi tampil: `Download` dan `[Changelog]` List
30. Verifikasi menu `⋯` hanya memuat `Detail`
31. Verifikasi `Edit`, `Suspend`, `Unsuspend`, `Change Partner`, dan `Delete` Hidden
32. Tutup menu `⋯`
33. Klik Company Name `PT Sejahtera Abadi` untuk membuka Detail
34. Verifikasi toggle `Allow Self-Purchased Device Activation` dan `[Resend Activation Email]` Hidden
35. Klik Tab Subscription
36. Verifikasi `[Changelog]` Tab Subscription tampil
37. Verifikasi link `Manage in Client Subscription →` dan info banner tampil
38. Klik Tab Asset Control
39. Verifikasi `[Changelog]` Tab Asset Control tampil
40. Verifikasi `Generate Enrollment QR` Hidden
41. Klik baris Station `Gerbang Gudang A` untuk expand Tablet List
42. Verifikasi `Deactivate` pada Station `Gerbang Gudang A` dan `Revoke` pada Tablet `Tablet Lobi 1` Hidden
43. Kembali ke List dengan tombol Back browser

### TC-AC-ACC-57: Elemen Detail Page per role: Edit header, toggle BYO, Resend Activation Email

44. Ketik Search `PT Teknologi Maju`, tekan Enter
45. Klik Company Name `PT Teknologi Maju` (Not Yet Activated) untuk membuka Detail
46. Verifikasi Detail `PT Teknologi Maju` terbuka
47. Verifikasi tombol `[Edit]` header Hidden untuk Read Only
48. Verifikasi toggle `Allow Self-Purchased Device Activation` Hidden untuk Read Only
49. Verifikasi `[Resend Activation Email]` Hidden untuk Read Only
50. Kembali ke List dengan tombol Back browser dan klik `(←)` pada kotak Search

### TC-AC-ACC-581: Read Only: Search, Sort, Pagination, Filter, dan Column Visibility tetap aktif

51. Ketik Search `PT Uji Halaman`, tekan Enter
52. Verifikasi Pagination menampilkan 3 halaman (30 baris `PT Uji Halaman 01` sampai `PT Uji Halaman 30`)
53. Verifikasi halaman 1 dimulai dari `PT Uji Halaman 01`
54. Klik header kolom `Client Code` dua kali
55. Verifikasi baris pertama memiliki Client Code `UJH-030`
56. Klik halaman 2 pada Pagination
57. Verifikasi baris pertama halaman 2 memiliki Client Code `UJH-020`
58. Buka Filter Panel, pilih field `Partner` (placeholder `All partners`) dengan `CV Mitra Lestari`, klik `[Apply]`
59. Verifikasi tabel tersaring dan tidak ada baris `PT Uji Halaman` (Client Direct tanpa relasi CV Mitra Lestari)
60. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
61. Ganti isi kotak Search dengan `PT Teknologi Maju`, tekan Enter
62. Verifikasi baris `PT Teknologi Maju` tampil
63. Klik header kolom Actions `(⋯)`
64. Verifikasi dropdown Column Visibility terbuka dengan kolom Curated `Company Email`, `PIC Email`, `PIC Phone`, `Industry`, `Country`, `State`, `City` belum dicentang
65. Tutup dropdown Column Visibility, klik `[Clear Field]` pada field `Partner`, klik `[Apply]`, klik header `Client Code` sampai sort ter-reset, dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2, 10, 11, 15, 17, 21 sampai 23, 25, 32, 41, 43, 44, 50, 65. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Spec Role Matrix per blok role (bagian 3a): langkah tiap role berbeda dan ganti akun menuntut Step eksplisit; login akun pertama (Total Control, A-01) dilakukan hook `before`.
- Asersi tambahan (S-03): pada TC-AC-ACC-46, kondisi Hidden `toggle BYO`, `Resend`, `Generate QR`, `Deactivate`, `Revoke` serta `[Changelog]` Tab Subscription dan Tab Asset Control diamati dengan membuka Detail, Tab Subscription, Tab Asset Control, dan Station `Gerbang Gudang A` (langkah 3 TC hanya berbunyi "buka Detail Client") karena Expected butir a, b, dan c menyebutnya.
- TC-AC-ACC-45 memakai dua Client: `PT Sejahtera Abadi` (memiliki riwayat subscription; tanpa Delete) dan `PT Baru Daftar` (C-09; belum pernah memiliki subscription; memuat Delete); Search pada langkah 2 dan 11 mencari baris target (R-16).
- Pembagian TC lintas spec: visibilitas untuk Default User, Distributor, dan Partner ada di spec 029; role Manage active client di spec 030; role Manage archived client di spec 031; Group Manager di spec 032.
- Ukuran spec (65 langkah, melewati sekitar 35 langkah): Role Matrix per blok role (dua role; langkah berbeda) pada satu dataset; tiap blok dimulai dari state eksplisit (Search atau ganti akun eksplisit) sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-AC-ACC-46: langkah TC hanya "Buka Detail Client" tanpa menyebut Client; spec memakai `PT Sejahtera Abadi` dan membuka Tab Subscription serta Tab Asset Control untuk mengamati elemen yang Expected sebut.
  - TC-AC-ACC-581: Expected butir d (hasil gabungan Search `PT Uji Halaman` dan Filter Partner) bergantung pada Search yang masih aktif saat Filter di-Apply.
