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
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` (akun default suite); tidak ada ganti akun. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah; Tabel Data Uji Pre-setup): Ahmad Fauzi (No. 13; holder `Manage user and role` non-tier, role lain belum di-assign: `Manage master reference` dan `Manage hardware` termasuk yang belum di-assign) untuk TC-GS-USER-371, 375, 1051, 871, dan 872; Dewi Lestari (No. 12; Basic, tanpa assignment role) untuk TC-GS-USER-372; Andi Wijaya (No. 10; tier Total Control) untuk TC-GS-USER-373; Doni Pratama (No. 11; tier Read Only) untuk TC-GS-USER-374; akun aktor Siti Nurhaliza sendiri (No. 2) untuk TC-GS-USER-382.
- Data Dinamis: tidak ada (spec hanya membaca; semua aksi pada Tab Role berupa hover, klik header, dan Column Visibility yang dipulihkan di dalam TC).
- Kemampuan teknis (disediakan tim FE/BE): tidak ada selain akses UI.
- State global yang diubah: tidak ada. Column Visibility Tab Role (TC-GS-USER-872) dikembalikan ke semula pada langkah 27 (hook `after` memuat ulang halaman sebagai cadangan).

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-371: Screening Tab Role user non-tier (tanpa switch Active)

3. Klik Name `Ahmad Fauzi` di User List
4. Klik Tab `Role`
5. Verifikasi Toolbar Tab Role hanya memuat icon Changelog
6. Verifikasi Banner Access Level tidak tampil
7. Verifikasi kolom tabel `Role Name | Create | Read | Update | Delete | Column Visibility (⋯)`
8. Verifikasi header kolom tidak dapat diklik (tanpa ikon sort)
9. Verifikasi 6 baris tetap urut: `Import data` | `Manage files` | `Manage hardware` | `Manage master reference` | `Manage TAG` | `Manage user and role`
10. Verifikasi sel permission yang tidak applicable untuk role tampil `—`

### TC-GS-USER-375: Read baseline tercentang dan disabled saat role sudah di-assign

11. Verifikasi checkbox Read baris `Manage user and role` tercentang
12. Verifikasi checkbox Read baris `Manage user and role` tetap tampil namun disabled

### TC-GS-USER-1051: Role belum di-assign tampil inactive dan checkbox tidak disabled

13. Hover checkbox Update baris `Manage master reference`
14. Verifikasi baris `Manage master reference` tampil inactive
15. Verifikasi semua checkbox baris `Manage master reference` kosong
16. Verifikasi checkbox Update baris `Manage master reference` enabled
17. Verifikasi tooltip disabled tidak tampil pada checkbox Update baris `Manage master reference`
18. Verifikasi tidak ada switch Active di baris mana pun

### TC-GS-USER-871: Header kolom tidak dapat diklik dan urutan baris tetap

19. Klik header `Role Name`
20. Klik header `Create`
21. Verifikasi header `Role Name` dan `Create` tampil tanpa ikon sort
22. Verifikasi urutan baris tetap A-Z Role Name

### TC-GS-USER-872: Column Visibility hide kolom Delete lalu unhide

23. Klik header `(⋯)`
24. Uncheck `Delete`
25. Verifikasi kolom `Delete` hilang
26. Verifikasi kolom `Create`, `Read`, dan `Update` tetap tampil
27. Check `Delete` lagi
28. Verifikasi kolom `Delete` tampil kembali
29. Tekan Esc untuk menutup Column Visibility

### TC-GS-USER-372: Tab Role user tanpa assignment, semua role inactive tanpa empty state

30. Klik menu User di sidebar Global Settings
31. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
32. Klik Name `Dewi Lestari` di User List
33. Klik Tab `Role`
34. Verifikasi 6 baris katalog tampil sebagai role inactive
35. Verifikasi tidak ada switch Active di baris mana pun
36. Verifikasi tidak ada CRUD yang tercentang
37. Verifikasi checkbox tetap dapat diklik (tidak disabled)
38. Verifikasi empty state tidak tampil

### TC-GS-USER-373: Tab Role user Total Control menampilkan banner

39. Klik menu User di sidebar Global Settings
40. Klik icon Search, ketik `Andi Wijaya`, tekan Enter
41. Klik Name `Andi Wijaya` di User List
42. Klik Tab `Role`
43. Verifikasi banner `This user has Total Control access.`
44. Verifikasi banner tanpa tombol assign dan remove

### TC-GS-USER-374: Tab Role user Read Only menampilkan banner

45. Klik menu User di sidebar Global Settings
46. Klik icon Search, ketik `Doni Pratama`, tekan Enter
47. Klik Name `Doni Pratama` di User List
48. Klik Tab `Role`
49. Verifikasi banner `This user has Read Only access.`
50. Verifikasi banner tanpa tombol assign dan remove

### TC-GS-USER-382: Checkbox CRUD disabled untuk target self

51. Klik menu User di sidebar Global Settings
52. Klik icon Search, ketik `Siti Nurhaliza`, tekan Enter
53. Klik Name `Siti Nurhaliza` di User List (Detail akun sendiri)
54. Klik Tab `Role`
55. Hover checkbox Create baris `Import data`
56. Verifikasi checkbox Create baris `Import data` tampil namun disabled
57. Verifikasi tooltip `"You can't manage your own account from here."`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Spec melewati sekitar 35 langkah (57 langkah, di antaranya 15 langkah pembukaan Detail berulang berupa klik menu User, Search, dan klik Name) karena sembilan TC berada di satu kelas harness (fungsional, baca saja, tanpa aksi yang mengubah data), satu layar (Tab Role User Detail), dan tiap blok TC berdiri sendiri.
- Urutan TC sumber diubah: TC-GS-USER-375, 1051, 871, dan 872 dimajukan tepat sesudah TC-GS-USER-371 karena memakai Detail Ahmad Fauzi dan Tab Role yang sama (langkah 1 sampai 2 TC-GS-USER-375, 1051, 871, dan 872 dipenuhi langkah 3 sampai 4); TC-GS-USER-872 (mengubah Column Visibility) paling akhir di blok Ahmad Fauzi; TC-GS-USER-382 paling akhir karena membuka Detail akun sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (100 baris per halaman agar Ahmad Fauzi tampil tanpa Search), 29 (menutup Column Visibility), 30 sampai 31, 39 sampai 40, 45 sampai 46, dan 51 sampai 52 (kembali ke User List dan mencari user target).
- Anchor dan asersi tambahan (bagian 8b butir 2; tidak ada di TC dan hanya sebagai anchor): langkah 26 (kolom `Create`, `Read`, `Update` tetap tampil, anchor untuk "kolom Delete hilang") dan langkah 21 (header tampil, anchor untuk "tidak ada ikon sort"). Langkah 5 (Toolbar tampil) mendahului langkah 6 (banner tidak tampil) dan berfungsi sebagai anchor dari Toolbar yang sama, sehingga urutan butir a dan b Expected TC-GS-USER-371 ditukar.
- Kolom Column Visibility (langkah 24 dan 27) dikembalikan ke semula pada TC yang sama sehingga tidak memengaruhi blok berikutnya; Column Visibility pada Tab Role tidak diasumsikan tersimpan lintas Detail.
- Pembagian TC lintas spec: edit dan auto-save Tab Role (TC-GS-USER-376 dan seterusnya) diverifikasi di spec 064. Spec ini hanya membaca dan menggunakan data Pre-setup; spec 064 menulis ke user milik spec.
- Temuan untuk QA:
  - TC-GS-USER-871 langkah 3 menyebut klik header `Active`, padahal kolom tabel Tab Role pada TC-GS-USER-371 Expected c tidak memuat kolom `Active` (tanpa switch Active). Spec mengklik `Role Name` dan `Create` saja.
  - TC-GS-USER-371 Expected e ("Sel permission yang tidak applicable ... tampil `—`") tidak menyebut sel mana yang tidak applicable; spec mengasersi keberadaan `—` pada sel yang tidak applicable tanpa menyebut baris atau kolom.
  - TC-GS-USER-382 langkah 2 "Hover checkbox" tidak menyebut checkbox yang di-hover dan cara membuka Detail akun sendiri; spec membuka dari User List dan meng-hover Create baris `Import data`.
  - TC-GS-USER-372 dan TC-GS-USER-1051 tidak menyebut cara membuktikan "checkbox dapat diklik" tanpa mengubah data; spec mengasersi state enabled tanpa mengeklik.
  - TC-GS-USER-371 precondition tidak menyebut kondisi role Ahmad Fauzi (hanya `Manage user and role` ter-assign); kondisi ini disimpulkan dari TC-GS-USER-375 dan TC-GS-USER-1051.
