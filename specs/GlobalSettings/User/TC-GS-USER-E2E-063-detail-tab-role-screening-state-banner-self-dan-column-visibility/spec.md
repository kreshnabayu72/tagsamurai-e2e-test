---
id: TC-GS-USER-E2E-063-detail-tab-role-screening-state-banner-self-dan-column-visibility
title: "User Detail Tab Role: Screening User Non-Tier, Role Belum Di-assign, Banner Total Control dan Read Only, Read Baseline Disabled, Checkbox Akun Sendiri Disabled, Urutan Baris Tetap, dan Column Visibility"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-371
  - TC-GS-USER-372
  - TC-GS-USER-373
  - TC-GS-USER-374
  - TC-GS-USER-375
  - TC-GS-USER-1051
  - TC-GS-USER-382
  - TC-GS-USER-871
  - TC-GS-USER-872
coverage:
  web: automated
---

# User Detail Tab Role: Screening User Non-Tier, Role Belum Di-assign, Banner Total Control dan Read Only, Read Baseline Disabled, Checkbox Akun Sendiri Disabled, Urutan Baris Tetap, dan Column Visibility

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini (akun default suite); halaman dibuka hook `beforeEach` suite; tidak ada ganti akun. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah; Tabel Data Uji Pre-setup): Ahmad Fauzi (No. 13; holder `Manage user and role` non-tier, role lain belum di-assign: `Manage files` dan `Manage hardware` termasuk yang belum di-assign dan tampil switch Active OFF) untuk TC-GS-USER-371, 375, 1051, 871, dan 872; Dewi Lestari (No. 12; Basic, tanpa assignment role) untuk TC-GS-USER-372; Andi Wijaya (No. 10; tier Total Control) untuk TC-GS-USER-373; Doni Pratama (No. 11; tier Read Only) untuk TC-GS-USER-374; akun aktor Siti Nurhaliza sendiri (No. 2) untuk TC-GS-USER-382.
- Data Dinamis: tidak ada (spec hanya membaca; semua aksi pada Tab Role berupa hover, klik header, dan Column Visibility yang dipulihkan di dalam TC).
- Kemampuan teknis (disediakan tim FE/BE): menghitung request tulis yang terkirim saat klik checkbox disabled (intercept, TC-GS-USER-1051); selain itu hanya akses UI.
- State global yang diubah: tidak ada. Column Visibility Tab Role (TC-GS-USER-872) dikembalikan ke semula pada langkah 34 (hook `after` memuat ulang halaman sebagai cadangan).

## Test Steps

### Persiapan

1. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-371: Screening Tab Role user non-tier (kolom Active dan switch per role)

2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Role`
4. Verifikasi Toolbar Tab Role hanya memuat icon Changelog
5. Verifikasi Banner Access Level tidak tampil
6. Verifikasi kolom tabel `Active | Role Name | Create | Read | Update | Delete | Column Visibility (⋯)`
7. Verifikasi header kolom tidak dapat diklik (tanpa ikon sort)
8. Verifikasi switch Active berada di kolom paling kiri tiap baris
9. Verifikasi 6 baris tetap urut: `Import data` | `Manage files` | `Manage hardware` | `Manage master reference` | `Manage TAG` | `Manage user and role`
10. Verifikasi sel permission yang tidak applicable untuk role tampil `—`
11. Verifikasi baris dengan switch Active ON (`Manage user and role`): checkbox Read tercentang dan disabled
12. Verifikasi baris dengan switch Active OFF (`Manage hardware`): seluruh checkbox disabled

### TC-GS-USER-375: Read baseline tercentang dan disabled saat role sudah di-assign

13. Verifikasi checkbox Read baris `Manage user and role` tercentang
14. Verifikasi checkbox Read baris `Manage user and role` tetap tampil namun disabled
15. Verifikasi checkbox Read baris `Manage hardware` disabled karena switch Active baris itu OFF

### TC-GS-USER-1051: Role belum pernah di-assign tampil switch OFF dan checkbox disabled

16. Hover checkbox Delete baris `Manage files`
17. Verifikasi switch Active baris `Manage files` OFF
18. Verifikasi seluruh checkbox baris `Manage files` disabled
19. Verifikasi seluruh checkbox baris `Manage files` tidak tercentang
20. Verifikasi tooltip `"Turn on this role first."` tampil
21. Verifikasi switch Active baris `Manage files` enabled
22. Klik checkbox Delete baris `Manage files`
23. Verifikasi state checkbox baris `Manage files` tidak berubah (tetap kosong dan disabled)
24. Verifikasi tidak ada request tulis yang terkirim saat klik checkbox

### TC-GS-USER-871: Header kolom tidak dapat diklik dan urutan baris tetap

25. Klik header `Role Name`
26. Klik header `Active`
27. Klik header `Create`
28. Verifikasi header `Role Name`, `Active`, dan `Create` tampil tanpa ikon sort
29. Verifikasi urutan baris tetap A-Z Role Name

### TC-GS-USER-872: Column Visibility hide kolom Delete lalu unhide

30. Klik header `(⋯)`
31. Uncheck `Delete`
32. Verifikasi kolom `Delete` hilang
33. Verifikasi kolom `Create`, `Read`, dan `Update` tetap tampil
34. Check `Delete` lagi
35. Verifikasi kolom `Delete` tampil kembali
36. Tekan Esc untuk menutup Column Visibility

### TC-GS-USER-372: Tab Role user tanpa assignment, semua switch OFF tanpa empty state

37. Klik menu User di sidebar Global Settings
38. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
39. Klik Name `Dewi Lestari` di User List
40. Klik Tab `Role`
41. Verifikasi 6 baris katalog tampil
42. Verifikasi switch Active seluruh baris OFF
43. Verifikasi seluruh checkbox disabled
44. Verifikasi tidak ada CRUD yang tercentang
45. Verifikasi checkbox tidak dapat diklik (disabled)
46. Verifikasi empty state tidak tampil

### TC-GS-USER-373: Tab Role user Total Control menampilkan banner

47. Klik menu User di sidebar Global Settings
48. Klik icon Search, ketik `Andi Wijaya`, tekan Enter
49. Klik Name `Andi Wijaya` di User List
50. Klik Tab `Role`
51. Verifikasi banner `This user has Total Control access.`
52. Verifikasi banner tanpa tombol assign dan remove

### TC-GS-USER-374: Tab Role user Read Only menampilkan banner

53. Klik menu User di sidebar Global Settings
54. Klik icon Search, ketik `Doni Pratama`, tekan Enter
55. Klik Name `Doni Pratama` di User List
56. Klik Tab `Role`
57. Verifikasi banner `This user has Read Only access.`
58. Verifikasi banner tanpa tombol assign dan remove

### TC-GS-USER-382: Checkbox CRUD disabled untuk target self

59. Klik menu User di sidebar Global Settings
60. Klik icon Search, ketik `Siti Nurhaliza`, tekan Enter
61. Klik Name `Siti Nurhaliza` di User List (Detail akun sendiri)
62. Klik Tab `Role`
63. Hover checkbox Create baris `Import data`
64. Verifikasi checkbox Create baris `Import data` tampil namun disabled
65. Verifikasi tooltip `"You can't manage your own account from here."`
66. Hover switch Active baris `Import data`
67. Verifikasi switch Active baris `Import data` tampil namun disabled
68. Verifikasi tooltip `"You can't manage your own account from here."`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Spec melewati sekitar 35 langkah (68 langkah, di antaranya 15 langkah pembukaan Detail berulang berupa klik menu User, Search, dan klik Name) karena sembilan TC berada di satu kelas harness (fungsional, baca saja, tanpa aksi yang mengubah data), satu layar (Tab Role User Detail), dan tiap blok TC berdiri sendiri.
- Urutan TC sumber diubah: TC-GS-USER-375, 1051, 871, dan 872 dimajukan tepat sesudah TC-GS-USER-371 karena memakai Detail Ahmad Fauzi dan Tab Role yang sama (langkah 1 sampai 2 TC-GS-USER-375, 1051, 871, dan 872 dipenuhi langkah 2 sampai 3); TC-GS-USER-872 (mengubah Column Visibility) paling akhir di blok Ahmad Fauzi; TC-GS-USER-382 paling akhir karena membuka Detail akun sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (100 baris per halaman agar Ahmad Fauzi tampil tanpa Search), 36 (menutup Column Visibility), 37 sampai 38, 47 sampai 48, 53 sampai 54, dan 59 sampai 60 (kembali ke User List dan mencari user target).
- Anchor dan asersi tambahan (bagian 8b butir 2; tidak ada di TC dan hanya sebagai anchor): langkah 33 (kolom `Create`, `Read`, `Update` tetap tampil, anchor untuk "kolom Delete hilang") dan langkah 28 (header tampil, anchor untuk "tidak ada ikon sort"). Langkah 4 (Toolbar tampil) mendahului langkah 5 (banner tidak tampil) dan berfungsi sebagai anchor dari Toolbar yang sama, sehingga urutan butir a dan b Expected TC-GS-USER-371 ditukar.
- Kolom Column Visibility (langkah 31 dan 34) dikembalikan ke semula pada TC yang sama sehingga tidak memengaruhi blok berikutnya; Column Visibility pada Tab Role tidak diasumsikan tersimpan lintas Detail.
- Pembagian TC lintas spec: edit dan auto-save Tab Role (TC-GS-USER-376 dan seterusnya) diverifikasi di spec 064. Spec ini hanya membaca dan menggunakan data Pre-setup; spec 064 menulis ke user milik spec.
- Temuan untuk QA:
  - TC-GS-USER-371 Expected e ("Sel permission yang tidak applicable ... tampil `—`") tidak menyebut sel mana yang tidak applicable; spec mengasersi keberadaan `—` pada sel yang tidak applicable tanpa menyebut baris atau kolom.
  - TC-GS-USER-382 langkah 2 "Hover checkbox" tidak menyebut checkbox yang di-hover dan cara membuka Detail akun sendiri; spec membuka dari User List dan meng-hover Create dan switch Active baris `Import data`.
  - TC-GS-USER-1051 berlabel UI Only tetapi Expected c menyebut klik checkbox "tidak mengirim request"; spec mengasersinya lewat penghitung request tulis yang disediakan tim FE/BE.
  - TC-GS-USER-371 precondition tidak menyebut kondisi role Ahmad Fauzi (hanya `Manage user and role` ter-assign); kondisi ini disimpulkan dari TC-GS-USER-375 (`Manage hardware`) dan TC-GS-USER-1051 (`Manage files`).
