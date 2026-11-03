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
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Spec ini mengosongkan Home Group Hana Kusuma (langkah 14); pemulihan ke General Affairs lewat seed API pada langkah 17 dan di hook `after`. Efek pada Pre-setup: Last Updated dan Modified By Hana Kusuma berubah dan satu entri log permanen `Edit Home Group` bertambah.

## Test Steps

### TC-FA-SU-282: Visibilitas Edit Home Group per aktor (Total Control)

1. Klik ⋯ pada baris Gita Permata
2. Verifikasi `Edit Home Group` tampil pada menu ⋯ baris Gita Permata sesuai kolom Menu ⋯ tabel Role yang diuji
3. Tekan Esc untuk menutup menu ⋯
4. Centang dua baris (Gita Permata dan Budi Santoso) lalu buka Bulk Action
5. Verifikasi Bulk Actions Bar menampilkan `Edit Home Group` sesuai kolom Bulk Action tabel Role yang diuji
6. Klik Unselect All

### TC-FA-SU-284: Field Home Group di Detail User (Total Control)

7. Buka Detail Gita Permata
8. Verifikasi Home Group tampil sebagai badge nama grup Finance & Accounting
9. Hover badge Home Group
10. Verifikasi hover menampilkan hierarki lengkap `[Parent] > [Child]`
11. Verifikasi ikon edit (`Edit2Line`) tampil di samping badge Home Group
12. Klik badge Home Group
13. Verifikasi badge Home Group tidak dapat diklik
14. Kosongkan Home Group Hana Kusuma (klik ⋯ pada baris Hana Kusuma, `Edit Home Group`, klik ulang node General Affairs yang ter-highlight, lalu `[Select]`)
15. Buka Detail Hana Kusuma
16. Verifikasi Home Group tampil `—` pada pengguna tanpa Home Group
17. Pulihkan Home Group Hana Kusuma ke General Affairs lewat seed API

### TC-FA-SU-282 dan TC-FA-SU-284: aktor Default User dan Manage global user & role (Update)

18. Untuk setiap aktor pada baris Default User Ahmad Dahlan dan Manage global user & role (Update) Qori Akbar pada tabel Role yang diuji, jalankan langkah 19 sampai 25
19. Ganti akun: Logout lalu login sebagai aktor pada baris tabel (kredensial dari kolom Env password)
20. Klik ⋯ pada baris Gita Permata
21. Verifikasi `Edit Home Group` pada menu ⋯ baris Gita Permata sesuai kolom Menu ⋯ tabel Role yang diuji
22. Tekan Esc untuk menutup menu ⋯
23. Centang dua baris (Gita Permata dan Budi Santoso) lalu buka Bulk Action
24. Verifikasi Bulk Actions Bar menampilkan atau menyembunyikan `Edit Home Group` sesuai kolom Bulk Action tabel Role yang diuji
25. Klik Unselect All

### TC-FA-SU-282 dan TC-FA-SU-284: aktor Read Only, Group Manager, dan Manage user & role Group (Update)

26. Untuk setiap aktor pada baris Read Only Citra Lestari, Group Manager Oscar Pranata, dan Manage user & role Group (Update) Sinta Dewi pada tabel Role yang diuji, jalankan langkah 27 sampai 36
27. Ganti akun: Logout lalu login sebagai aktor pada baris tabel (kredensial dari kolom Env password)
28. Klik ⋯ pada baris Gita Permata
29. Verifikasi `Edit Home Group` pada menu ⋯ baris Gita Permata Hidden sesuai kolom Menu ⋯ tabel Role yang diuji
30. Tekan Esc untuk menutup menu ⋯
31. Centang dua baris (Gita Permata dan Budi Santoso) lalu buka Bulk Action
32. Verifikasi Bulk Actions Bar menyembunyikan `Edit Home Group` sesuai kolom Bulk Action tabel Role yang diuji
33. Klik Unselect All
34. Buka Detail pengguna pada kolom Detail target tabel Role yang diuji
35. Verifikasi badge Home Group tampil tanpa ikon edit sesuai kolom Ikon edit Detail tabel Role yang diuji
36. Kembali ke User List

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Role Matrix (bagian 3a): satu matriks visibilitas `Edit Home Group` banyak aktor dengan hasil berbeda per role. Spec ditulis per blok aktor karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`); langkah tiap blok identik sehingga ditulis sebagai perulangan "Untuk setiap aktor pada tabel" (langkah 19 sampai 25 dan langkah 27 sampai 36), parameter di tabel Prerequisites (8b butir 7).
- Alasan melewati sekitar 35 langkah: dengan ekspansi, spec berisi sekitar 60 langkah karena lima aktor ditambah aktor pertama. Seluruh langkah adalah satu kelas (fungsional) dan satu topik (matriks visibilitas `Edit Home Group`); tiap aktor berdiri sendiri sehingga kegagalan satu aktor tidak menghilangkan makna aktor lain, dan pemisahan akan mengulang hook, login, dan pemulihan Hana Kusuma.
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup menu ⋯ dengan Esc, Unselect All, ganti akun, kembali ke User List, dan pemulihan Home Group Hana Kusuma (langkah 17). Pengosongan Home Group Hana Kusuma (langkah 14) adalah langkah 5 TC-FA-SU-284.
- Aktor Group Manager mengamati Detail Indra Wijaya (Group Role IT Infrastructure, dalam scope Oscar Pranata) sesuai TC-FA-SU-284 langkah 4; aktor lain mengamati Detail Gita Permata.
- Temuan untuk QA (S-15): (1) Email akun Manage global user & role (Update) Qori Akbar, Group Manager Oscar Pranata, dan Manage user & role Group (Update) Sinta Dewi tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". (2) TC-FA-SU-284 langkah 4 hanya mengulang Detail sebagai Read Only, Manage user & role Group, dan Group Manager; ikon edit untuk Default User dan Manage global user & role (Expected b) tidak punya langkah observasi sehingga tidak diasersi (hanya Total Control yang diamati). (3) TC-FA-SU-282 langkah 2 hanya membuka menu ⋯ baris Gita Permata, sedangkan Expected b menyebut "pada baris mana pun"; spec hanya mengamati baris itu. (4) Expected a TC-FA-SU-284 menyebut ikon edit hanya bagi Default User, Total Control, dan Manage global user & role dengan Expected c untuk Group Manager pada Detail Indra Wijaya; ikon edit Default User dan Manage global user & role tetap tidak teramati. (5) Post Condition TC-FA-SU-282 dan TC-FA-SU-284 tidak ada.
