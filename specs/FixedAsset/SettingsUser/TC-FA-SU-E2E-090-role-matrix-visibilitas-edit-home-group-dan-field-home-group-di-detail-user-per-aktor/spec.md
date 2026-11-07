---
id: TC-FA-SU-E2E-090-role-matrix-visibilitas-edit-home-group-dan-field-home-group-di-detail-user-per-aktor
title: "Role Matrix: Visibilitas Edit Home Group dan Field Home Group di Detail User per Aktor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-282
  - TC-FA-SU-284
coverage:
  web: automated
---

# Role Matrix: Visibilitas Edit Home Group dan Field Home Group di Detail User per Aktor

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Aktor lain berganti akun lewat langkah eksplisit; hook `after` memulihkan sesi ke akun default suite (Total Control Lina Marlina).
- Role yang diuji (tabel di bawah; kolom Menu ⋯ dan Bulk Action memakai nilai Tampil atau Hidden; kolom Ikon edit Detail memakai nilai Ada atau Tidak ada). Email akun yang tidak tertulis di Pre-setup TC ditulis "disediakan tim FE" (lihat Temuan untuk QA).

| Aktor | Pre-setup | Email | Env password | Menu ⋯ baris Gita Permata | Bulk Action | Detail target | Ikon edit Detail |
|---|---|---|---|---|---|---|---|
| Total Control Lina Marlina | #1 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `FA_TC_PASSWORD` | Tampil | Tampil | Gita Permata | Ada |
| Default User Ahmad Dahlan | #2 | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `FA_DU_PASSWORD` | Tampil | Tampil | - | - |
| Manage global user & role (Update) Qori Akbar | #4 | disediakan tim FE | `FA_MURG_UPD_PASSWORD` | Tampil | Tampil | - | - |
| Read Only Citra Lestari | #3 | `readOnly_automated_{namaCompany}@qwertysystem.net` | `FA_RO_PASSWORD` | Hidden | Hidden | Gita Permata | Tidak ada |
| Group Manager Oscar Pranata | #9 | disediakan tim FE | `FA_GM_PASSWORD` | Hidden | Hidden | Indra Wijaya (Group Role IT Infrastructure, dalam scope Oscar Pranata) | Tidak ada |
| Manage user & role Group (Update) Sinta Dewi | #6 | disediakan tim FE | `FA_MURGR_UPD_PASSWORD` | Hidden | Hidden | Gita Permata | Tidak ada |

- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: #1, #2, #3, #4, #6, #9, #20, #21, #23. Pengguna target: Gita Permata (Home Group Finance & Accounting), Hana Kusuma (Home Group General Affairs), Indra Wijaya. Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Spec ini mengosongkan Home Group Hana Kusuma (langkah 19); pemulihan ke General Affairs lewat seed API pada langkah 23 dan di hook `after`. Efek pada Pre-setup: Last Updated dan Modified By Hana Kusuma berubah dan satu entri log permanen `Edit Home Group` bertambah.

## Test Steps

### TC-FA-SU-282: Visibilitas Edit Home Group per aktor (Total Control)

1. Ketik Search `Gita Permata`, tekan Enter
2. Klik ⋯ pada baris Gita Permata
3. Verifikasi `Edit Home Group` tampil pada menu ⋯ baris Gita Permata sesuai kolom Menu ⋯ tabel Role yang diuji
4. Tekan Esc untuk menutup menu ⋯
5. Centang Gita Permata
6. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
7. Centang Budi Santoso lalu buka Bulk Action
8. Verifikasi Bulk Actions Bar menampilkan `Edit Home Group` sesuai kolom Bulk Action tabel Role yang diuji
9. Klik Unselect All

### TC-FA-SU-284: Field Home Group di Detail User (Total Control)

10. Ganti isi kotak search dengan `Gita Permata`, tekan Enter
11. Buka Detail Gita Permata
12. Verifikasi Home Group tampil sebagai badge nama grup Finance & Accounting
13. Hover badge Home Group
14. Verifikasi hover menampilkan hierarki lengkap `[Parent] > [Child]`
15. Verifikasi ikon edit (`Edit2Line`) tampil di samping badge Home Group
16. Klik badge Home Group
17. Verifikasi badge Home Group tidak dapat diklik
18. Kembali ke User List, ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
19. Kosongkan Home Group Hana Kusuma (klik ⋯ pada baris Hana Kusuma, `Edit Home Group`, klik ulang node General Affairs yang ter-highlight, lalu `[Select]`)
20. Tunggu aksi selesai: permintaan `[Select]` pada langkah 19 selesai dan popup tertutup
21. Buka Detail Hana Kusuma
22. Verifikasi Home Group tampil `—` pada pengguna tanpa Home Group
23. Pulihkan Home Group Hana Kusuma ke General Affairs lewat seed API

### TC-FA-SU-282 dan TC-FA-SU-284: aktor Default User dan Manage global user & role (Update)

24. Untuk setiap aktor pada baris Default User Ahmad Dahlan dan Manage global user & role (Update) Qori Akbar pada tabel Role yang diuji, jalankan langkah 25 sampai 35
25. Ganti akun: Logout lalu login sebagai aktor pada baris tabel (kredensial dari kolom Env password)
26. Buka Settings > User lewat sidebar
27. Ketik Search `Gita Permata`, tekan Enter
28. Klik ⋯ pada baris Gita Permata
29. Verifikasi `Edit Home Group` pada menu ⋯ baris Gita Permata sesuai kolom Menu ⋯ tabel Role yang diuji
30. Tekan Esc untuk menutup menu ⋯
31. Centang Gita Permata
32. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
33. Centang Budi Santoso lalu buka Bulk Action
34. Verifikasi Bulk Actions Bar menampilkan atau menyembunyikan `Edit Home Group` sesuai kolom Bulk Action tabel Role yang diuji
35. Klik Unselect All

### TC-FA-SU-282 dan TC-FA-SU-284: aktor Read Only, Group Manager, dan Manage user & role Group (Update)

36. Untuk setiap aktor pada baris Read Only Citra Lestari, Group Manager Oscar Pranata, dan Manage user & role Group (Update) Sinta Dewi pada tabel Role yang diuji, jalankan langkah 37 sampai 51
37. Ganti akun: Logout lalu login sebagai aktor pada baris tabel (kredensial dari kolom Env password)
38. Buka Settings > User lewat sidebar
39. Ketik Search `Gita Permata`, tekan Enter
40. Klik ⋯ pada baris Gita Permata
41. Verifikasi `Edit Home Group` pada menu ⋯ baris Gita Permata Hidden sesuai kolom Menu ⋯ tabel Role yang diuji
42. Tekan Esc untuk menutup menu ⋯
43. Centang Gita Permata
44. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
45. Centang Budi Santoso lalu buka Bulk Action
46. Verifikasi Bulk Actions Bar menyembunyikan `Edit Home Group` sesuai kolom Bulk Action tabel Role yang diuji
47. Klik Unselect All
48. Ganti isi kotak search dengan nama pengguna pada kolom Detail target tabel Role yang diuji, tekan Enter
49. Buka Detail pengguna pada kolom Detail target tabel Role yang diuji
50. Verifikasi badge Home Group tampil tanpa ikon edit sesuai kolom Ikon edit Detail tabel Role yang diuji
51. Kembali ke User List

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Role Matrix (bagian 3a): satu matriks visibilitas `Edit Home Group` banyak aktor dengan hasil berbeda per role. Spec ditulis per blok aktor karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`); langkah tiap blok identik sehingga ditulis sebagai perulangan "Untuk setiap aktor pada tabel" (langkah 25 sampai 35 dan langkah 37 sampai 51), parameter di tabel Prerequisites (8b butir 7).
- Alasan melewati sekitar 35 langkah: dengan ekspansi, spec berisi sekitar 90 langkah karena lima aktor ditambah aktor pertama. Seluruh langkah adalah satu kelas (fungsional) dan satu topik (matriks visibilitas `Edit Home Group`); tiap aktor berdiri sendiri sehingga kegagalan satu aktor tidak menghilangkan makna aktor lain, dan pemisahan akan mengulang hook, login, dan pemulihan Hana Kusuma.
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup menu ⋯ dengan Esc, Unselect All, ganti akun, kembali ke User List, dan pemulihan Home Group Hana Kusuma (langkah 23). Pengosongan Home Group Hana Kusuma (langkah 19) adalah langkah 5 TC-FA-SU-284.
- Langkah penghubung tambahan: langkah 1, 6, 10, 18, 27, 32, 39, 44, dan 48 (Search nama baris target sebelum membuka menu ⋯, mencentang, atau membuka Detail, karena User List memuat 3 halaman; R-16, bagian 8b butir 9 dan 13; dua baris dicentang dengan Search per baris), langkah 26 dan 38 (membuka Settings > User lewat sidebar sesudah ganti akun, S-14), dan langkah 20 (menunggu aksi `[Select]` selesai sebelum membuka Detail, bagian 8b butir 8).
- Aktor Group Manager mengamati Detail Indra Wijaya (Group Role IT Infrastructure, dalam scope Oscar Pranata) sesuai TC-FA-SU-284 langkah 4; aktor lain mengamati Detail Gita Permata.
- Temuan untuk QA (S-15): (1) Email akun Manage global user & role (Update) Qori Akbar, Group Manager Oscar Pranata, dan Manage user & role Group (Update) Sinta Dewi tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". (2) TC-FA-SU-284 langkah 4 hanya mengulang Detail sebagai Read Only, Manage user & role Group, dan Group Manager; ikon edit untuk Default User dan Manage global user & role (Expected b) tidak punya langkah observasi sehingga tidak diasersi (hanya Total Control yang diamati). (3) TC-FA-SU-282 langkah 2 hanya membuka menu ⋯ baris Gita Permata, sedangkan Expected b menyebut "pada baris mana pun"; spec hanya mengamati baris itu. (4) Expected a TC-FA-SU-284 menyebut ikon edit hanya bagi Default User, Total Control, dan Manage global user & role dengan Expected c untuk Group Manager pada Detail Indra Wijaya; ikon edit Default User dan Manage global user & role tetap tidak teramati. (5) Post Condition TC-FA-SU-282 dan TC-FA-SU-284 tidak ada. (6) TC-FA-SU-282 dan TC-FA-SU-284 mencentang dua baris tanpa menyebut cara menemukan baris; spec memakai Search per baris dan mengasumsikan seleksi bertahan saat isi Search berganti. Bila seleksi tidak bertahan, QA perlu menyebut cara lain.
