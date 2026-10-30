---
id: TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus
title: "Defense-in-Depth: Request Langsung Tanpa Wewenang Ditolak 403, Payload Script, dan Karakter Khusus Search"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-969
  - TC-GS-USER-970
  - TC-GS-USER-971
  - TC-GS-USER-972
  - TC-GS-USER-973
  - TC-GS-USER-974
  - TC-GS-USER-975
  - TC-GS-USER-976
  - TC-GS-USER-977
  - TC-GS-USER-978
  - TC-GS-USER-979
  - TC-GS-USER-980
  - TC-GS-USER-981
  - TC-GS-USER-982
  - TC-GS-USER-983
  - TC-GS-USER-1067
  - TC-GS-USER-1075
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Tanpa Wewenang Ditolak 403, Payload Script, dan Karakter Khusus Search

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun yang diuji (spec memakai enam akun dan berganti akun secara eksplisit):

  | Urutan | Role (Tabel Data Uji Pre-setup) | Email | Environment variable password |
  |---|---|---|---|
  | 1 | Read Only, Yudi Pratomo (No. 3) | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `GS_RO_PASSWORD` |
  | 2 | Manage user and role (Update-Only: R+U), Bayu Saputra (No. 6) | `manageUserUpdate_automated_{namaCompany}@qwertysystem.net` | `GS_UPDATE_PASSWORD` |
  | 3 | Manage user and role (Full CRUD), Fajar Nugroho (No. 4) | `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` | `GS_FULLCRUD_PASSWORD` |
  | 4 | Total Control Client tanpa subscription Supply Asset (disediakan tim FE, tidak ada di Tabel Pre-setup) | `totalControlGlobalSettings_automated_{namaCompanyTanpaSupplyAsset}@qwertysystem.net` | `GS_NOSUPPLY_TC_PASSWORD` |
  | 5 | Total Control Client A, Siti Nurhaliza (No. 2), akun default suite | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `GS_TC_PASSWORD` |

  Login akun 1 di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (akun 5). Password tidak ditulis di spec atau fixture.
- Env var: `GS_RO_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_FULLCRUD_PASSWORD`, `GS_NOSUPPLY_TC_PASSWORD`, `GS_TC_PASSWORD`.
- Kemampuan teknis (S-11): (a) klien HTTP yang mengirim request Create, Edit, Delete, Toggle Active, Pair TAG, Reset Authenticator, Remove Access, dan ubah Access langsung ke server dengan token sesi akun yang sedang login, tanpa lewat UI (endpoint dan cara menangkap token disediakan tim FE; TC dan PRD tidak menyebutnya); (b) membaca data user dari BE lewat fixture BE (Name, email, Access, status Active, Temporary User, TAG, MFA, Last Update, Modified By) untuk membandingkan "data tidak berubah" dengan snapshot `S0`; (c) seeding Login User dan penghapusannya lewat API (sesi API akun 5).
- Data Pre-setup dibaca saja dan tidak diubah: Default User Hendra Gunawan (No. 1) menjadi target request yang ditolak pada TC-GS-USER-975 dan 978 (akun Default User tunggal, tidak dapat diganti user seed; request ditolak sehingga data tidak berubah), TAG `TAG-USR-0001` (No. 25) menjadi nilai request Pair TAG yang ditolak, dan akun aktor akun 5 (Siti Nurhaliza) menjadi target "akun sendiri" pada TC-GS-USER-974, 976, 977, dan 1075.
- Data Dinamis (suffix per run dan nomor spec), di-seed lewat API di hook `before` oleh akun 5 (nilai field wajib lain user mengikuti fixture `fixtures/user.json` yang belum ada, disediakan tim FE):
  - Login User `Dewi Lestari {runId}-155`, email `dewilestari+{runId}-155@qwertysystem.net`, Basic, Activated, Active, Access `Fixed Asset` dan `Global Settings`, tanpa TAG (setara Dewi Lestari Tabel Pre-setup No. 12; target TC-GS-USER-969, 970, 971, 972, 973, 983, 1067).
  - Login User `Andi Wijaya {runId}-155`, email `andiwijaya+{runId}-155@qwertysystem.net`, tier Total Control, Activated, Active (setara Andi Wijaya Tabel Pre-setup No. 10; target TC-GS-USER-979).
  - Snapshot `S0` (hook `before`, sesudah seeding): data Dewi Lestari `{runId}-155`, Andi Wijaya `{runId}-155`, Default User Hendra Gunawan, dan Siti Nurhaliza yang dibaca lewat fixture BE.
  - Input uji request yang ditolak (tidak membuat data): email `dewilestari+{runId}-155@qwertysystem.net` pada request Create TC-GS-USER-969; First Name `Dewi Bypass` pada request Edit TC-GS-USER-970; email `supplyuser+{runId}-155@qwertysystem.net` dengan Access `Supply Asset` pada request Create TC-GS-USER-980.
  - Dibuat spec lewat UI pada TC-GS-USER-981: Login User dengan First Name `<script>alert(1)</script>`, Last Name `XSS {runId}-155`, email `xssuser+{runId}-155@qwertysystem.net`; field wajib lain mengikuti fixture `fixtures/user.json`.
  - Akun 4 mewakili precondition c TC-GS-USER-980 (Client tanpa subscription Supply Asset).
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah berhasil penuh): hapus lewat API Login User `dewilestari+{runId}-155@qwertysystem.net`, `andiwijaya+{runId}-155@qwertysystem.net`, `xssuser+{runId}-155@qwertysystem.net`, dan `supplyuser+{runId}-155@qwertysystem.net` bila ada; kembalikan sesi ke akun 5.
- Tidak ada state global yang diubah.

## Test Steps

### Akun 1, Read Only (TC-GS-USER-969, 970, 972, 973, 983)

1. Tangkap token sesi Read Only, lalu kirim request Create user dengan email `dewilestari+{runId}-155@qwertysystem.net` langsung ke server tanpa lewat UI
2. Verifikasi server menolak dengan `403`
3. Verifikasi (dibaca lewat fixture BE) data `Dewi Lestari {runId}-155` sama dengan snapshot `S0`
4. Kirim request Edit user `Dewi Lestari {runId}-155` dengan First Name `Dewi Bypass` langsung ke server
5. Verifikasi server menolak dengan `403`
6. Verifikasi (dibaca lewat fixture BE) data `Dewi Lestari {runId}-155` sama dengan snapshot `S0`
7. Kirim request Toggle Active untuk `Dewi Lestari {runId}-155` langsung ke server
8. Verifikasi server menolak dengan `403`
9. Verifikasi (dibaca lewat fixture BE) data `Dewi Lestari {runId}-155` sama dengan snapshot `S0`
10. Kirim request Pair TAG `TAG-USR-0001` untuk `Dewi Lestari {runId}-155` langsung ke server
11. Verifikasi server menolak dengan `403`
12. Verifikasi (dibaca lewat fixture BE) data `Dewi Lestari {runId}-155` sama dengan snapshot `S0`
13. Kirim request aksi Save Edit untuk `Dewi Lestari {runId}-155` langsung ke server
14. Verifikasi server menolak dengan `403`

### Akun 2, Update-Only (TC-GS-USER-971, 1067)

15. Ganti akun: logout, lalu login sebagai Manage user and role (Update-Only: R+U) (`manageUserUpdate_automated_{namaCompany}@qwertysystem.net`) dengan `Spectra.env.GS_UPDATE_PASSWORD`, lalu buka Global Settings > User > User List
16. Kirim request Delete user `Dewi Lestari {runId}-155` langsung ke server tanpa lewat UI
17. Verifikasi server menolak dengan `403`
18. Verifikasi (dibaca lewat fixture BE) data `Dewi Lestari {runId}-155` sama dengan snapshot `S0`
19. Dari sesi aktif halaman User List, kirim request Delete user `Dewi Lestari {runId}-155` langsung ke server
20. Verifikasi server menolak dengan `403`
21. Verifikasi (dibaca lewat fixture BE) data `Dewi Lestari {runId}-155` sama dengan snapshot `S0`

### Akun 3, Full CRUD (TC-GS-USER-979)

22. Ganti akun: logout, lalu login sebagai Manage user and role (Full CRUD) (`manageUserFullCrud_automated_{namaCompany}@qwertysystem.net`) dengan `Spectra.env.GS_FULLCRUD_PASSWORD`, lalu buka Global Settings > User > User List
23. Kirim request Edit user `Andi Wijaya {runId}-155` langsung ke server
24. Verifikasi server menolak dengan `403`
25. Verifikasi (dibaca lewat fixture BE) data `Andi Wijaya {runId}-155` sama dengan snapshot `S0`

### Akun 4, Client tanpa subscription Supply Asset (TC-GS-USER-980)

26. Ganti akun: logout, lalu login sebagai Total Control Client tanpa subscription Supply Asset (`totalControlGlobalSettings_automated_{namaCompanyTanpaSupplyAsset}@qwertysystem.net`) dengan `Spectra.env.GS_NOSUPPLY_TC_PASSWORD`, lalu buka Global Settings > User > User List
27. Kirim request Create user dengan email `supplyuser+{runId}-155@qwertysystem.net` dan Access `Supply Asset` langsung ke server
28. Verifikasi server menolak request
29. Verifikasi (dibaca lewat fixture BE) user `supplyuser+{runId}-155@qwertysystem.net` tidak dibuat

### Akun 5, Total Control (TC-GS-USER-974, 975, 976, 977, 978, 1075)

30. Ganti akun: logout, lalu login sebagai Total Control Client A (`totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`) dengan `Spectra.env.GS_TC_PASSWORD`, lalu buka Global Settings > User > User List
31. Kirim request Deactivate untuk akun sendiri langsung ke server
32. Verifikasi server menolak dengan `403`
33. Verifikasi (dibaca lewat fixture BE) data akun sendiri (Siti Nurhaliza) sama dengan snapshot `S0`
34. Kirim request Delete untuk Default User Hendra Gunawan langsung ke server
35. Verifikasi server menolak dengan `403`
36. Verifikasi (dibaca lewat fixture BE) data Default User Hendra Gunawan sama dengan snapshot `S0`
37. Kirim request Reset Authenticator untuk akun sendiri langsung ke server
38. Verifikasi server menolak dengan `403`
39. Verifikasi (dibaca lewat fixture BE) data akun sendiri (Siti Nurhaliza) sama dengan snapshot `S0`
40. Kirim request Remove Access untuk akun sendiri langsung ke server
41. Verifikasi server menolak dengan `403`
42. Verifikasi (dibaca lewat fixture BE) data akun sendiri (Siti Nurhaliza) sama dengan snapshot `S0`
43. Kirim request ubah Access untuk Default User Hendra Gunawan langsung ke server
44. Verifikasi server menolak dengan `403`
45. Verifikasi (dibaca lewat fixture BE) data Default User Hendra Gunawan sama dengan snapshot `S0`
46. Kirim request Edit User untuk akun sendiri yang mengubah `access`
47. Verifikasi server menolak dengan `403`
48. Verifikasi respons server memuat pesan "You can't manage your own account from here."
49. Kirim request Edit User untuk akun sendiri yang mengubah Temporary User
50. Verifikasi server menolak dengan `403`
51. Verifikasi respons server memuat pesan "You can't manage your own account from here."
52. Verifikasi (dibaca lewat fixture BE) Access akun sendiri (Siti Nurhaliza) tidak berubah dari snapshot `S0`
53. Verifikasi (dibaca lewat fixture BE) Temporary User akun sendiri (Siti Nurhaliza) tidak berubah dari snapshot `S0`

### Karakter khusus Search (TC-GS-USER-982)

54. Klik icon Search, ketik `{runId}-155`, tekan Enter pada tabel User List
55. Verifikasi baris `Dewi Lestari {runId}-155` tampil di tabel
56. Ganti isi kotak search dengan `%' OR 1=1 --`, tekan Enter
57. Verifikasi state No result tampil pada tabel
58. Verifikasi tidak ada toast error atau pesan error pada halaman
59. Kosongkan Search

### Payload script (TC-GS-USER-981)

60. Klik `[+ User]`, isi First Name `<script>alert(1)</script>`, Last Name `XSS {runId}-155`, Email `xssuser+{runId}-155@qwertysystem.net`, dan field wajib lain sesuai fixture, lalu klik `[Submit]`
61. Tunggu aksi selesai
62. Isi Search dengan `XSS {runId}-155`, tekan Enter
63. Verifikasi Name baris tampil sebagai teks literal `<script>alert(1)</script> XSS {runId}-155` di User List
64. Verifikasi tidak ada script yang dieksekusi dan tidak ada dialog browser di User List
65. Klik Name `<script>alert(1)</script> XSS {runId}-155`
66. Verifikasi Name tampil sebagai teks literal `<script>alert(1)</script> XSS {runId}-155` di Detail
67. Verifikasi tidak ada script yang dieksekusi dan tidak ada dialog browser di Detail
68. Kembali ke User List dengan klik Back
69. Kosongkan Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas defense-in-depth (prinsip 13a) tanpa harness eksternal.
- Subjudul `###` memetakan langkah ke id TC granular dan akun.
- Request langsung ke server (TC-GS-USER-969 sampai 980, 983, 1067, 1075): asersi hanya respons server dan state data lewat fixture BE (bagian 8b butir 1); toast, refresh UI, dan perilaku FE lain tidak diasersi dan dicatat sebagai temuan. "Data tidak berubah" dibandingkan dengan snapshot `S0` yang dibaca hook `before` (S-11).
- Urutan TC sumber diubah dan dikelompokkan per akun dengan empat kali ganti akun eksplisit (langkah 15, 22, 26, 30): Read Only (969, 970, 972, 973, 983), Update-Only (971, 1067), Full CRUD (979), Client tanpa Supply Asset (980), lalu Total Control (974, 975, 976, 977, 978, 1075, 982, 981). Akun 4 ditaruh sebelum akun 5 supaya spec berakhir pada akun default suite; TC-GS-USER-981 (membuat data) paling akhir di akun 5 (bagian 3 prinsip 3).
- Spec melewati sekitar 35 langkah (69 langkah). Alasan: tujuh belas TC semuanya satu kelas harness (defense-in-depth tanpa harness eksternal) dan tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); mayoritas langkah adalah trio berpola "kirim request, `Verifikasi` 403, `Verifikasi` data tidak berubah" yang tidak dapat digabung (S-01) dan empat kali ganti akun dibutuhkan precondition role TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 15, 22, 26, 30 (ganti akun dan membuka User List); langkah 54 dan 62 (Search); langkah 59 dan 69 (mengosongkan Search); langkah 61 (menunggu Create selesai); langkah 68 (Back ke User List). Verifikasi pembanding `Dewi Lestari {runId}-155` tampil pada langkah 55 menjadi anchor positif bagi State No result pada langkah 57 (bagian 8b butir 2).
- Tidak ada TC yang terbelah lintas spec. Perilaku FE untuk respons 403 yang sama (toast `"You don't have permission to do this."`, refresh UI, aksi tidak tersedia) tidak diasersi di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-969, 970, 971, 972, 973: Expected a memuat "muncul toast error `"You don't have permission to do this."` bila dipicu dari UI" dan TC-GS-USER-1067 Expected a dan b (toast, UI di-refresh, aksi Delete tetap tidak tersedia) adalah perilaku FE; tidak diasersi pada request langsung (bagian 8b butir 1).
  - TC-GS-USER-969 sampai 983, 1067, 1075: TC tidak menyebut endpoint, cara menangkap token sesi, dan payload (contoh Name baru pada request Edit, TAG pada request Pair TAG); disediakan tim FE dan spec memakai `Dewi Bypass` dan `TAG-USR-0001`.
  - TC-GS-USER-971 dan 1067: keduanya menguji Delete oleh holder tanpa hak Delete (Update-Only) pada Dewi Lestari; spec menjalankan dua request terpisah.
  - TC-GS-USER-975 dan 978: target Default User tidak dapat diganti dengan user seed milik spec; ditolak sehingga data tidak berubah.
  - TC-GS-USER-974 sampai 978: Expected "Data tidak berubah" tidak menyebut data yang dibandingkan; spec membandingkan snapshot `S0` (Name, email, Access, status Active, Temporary User, TAG, MFA, Last Update, Modified By).
  - TC-GS-USER-979: tidak menyebut payload Edit pada Andi Wijaya; spec memakai Andi seed milik spec dengan tier Total Control.
  - TC-GS-USER-980: precondition "Client tanpa subscription Supply Asset" tidak punya akun di Tabel Pre-setup; akun dan env var `GS_NOSUPPLY_TC_PASSWORD` disediakan tim FE. Expected "Request ditolak" tidak menyebut kode status; spec mengasersi penolakan tanpa kode.
  - TC-GS-USER-981: tidak menyebut Last Name, email, dan field wajib lain; spec memakai Last Name `XSS {runId}-155`. TC-GS-USER-982: Expected "No result state" tidak menyebut teks state.
  - TC-GS-USER-983: judul skenario menyebut "membuka URL Edit user langsung" sedangkan Langkah Uji memanggil aksi Save Edit lewat request langsung; spec mengikuti Langkah Uji dan Expected (403).
  - TC-GS-USER-1075: pesan "You can't manage your own account from here." diasersi pada respons server; TC tidak menyebut apakah pesan itu ada di badan respons atau di toast.
