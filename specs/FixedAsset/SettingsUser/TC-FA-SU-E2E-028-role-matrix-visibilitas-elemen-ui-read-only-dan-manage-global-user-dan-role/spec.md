---
id: TC-FA-SU-E2E-028-role-matrix-visibilitas-elemen-ui-read-only-dan-manage-global-user-dan-role
title: "Role Matrix: Visibilitas Elemen UI Read Only dan Manage global user & role (Update dan Read saja)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-52
  - TC-FA-SU-53
  - TC-FA-SU-54
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen UI Read Only dan Manage global user & role (Update dan Read saja)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Read Only (Citra Lestari, Pre-setup #3); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke Total Control (Lina Marlina). Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Role yang diuji (satu blok per aktor karena ganti akun menuntut Step eksplisit):

| Aktor | Pre-setup | Nama | Email | Env password |
|---|---|---|---|---|
| Read Only | #3 | Citra Lestari | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| Manage global user & role (Update) | #4 | Qori Akbar | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURG_UPD_PASSWORD` |
| Manage global user & role (Read saja) | #5 | Rina Susanti | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURG_RO_PASSWORD` |

- Nama env `FA_RO_PASSWORD`, `FA_MURG_UPD_PASSWORD`, dan `FA_MURG_RO_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; satu nama satu arti. Password tidak ditulis di spec atau fixture.
- Target terkunci (langkah 61 sampai 68, TC-FA-SU-53): Lina Marlina (Total Control) lalu Citra Lestari (Read Only).
- Data Pre-setup (hanya dibaca): Client `FaUserMain` dengan 25 pengguna (#20) tersebar 3 halaman (10, 10, 5 baris) dan tier serta penugasan (#23). Target biasa: Budi Santoso; pengguna Pending Activation: Hana Kusuma.
- Data Dinamis: tidak ada.
- Kemampuan teknis: login dan logout bergantian antar akun pada satu sesi browser; hover elemen.
- State global: tidak ada yang diubah. Dialog Bulk Deactivate pada TC-FA-SU-53 dibatalkan sebelum konfirmasi sehingga status pengguna tidak berubah; data Pre-setup tidak diubah.

## Test Steps

### TC-FA-SU-52: Visibilitas elemen UI untuk Read Only

1. Verifikasi halaman 1 tabel User List berisi 10 baris
2. Klik halaman 2 pada pagination
3. Verifikasi halaman 2 berisi 10 baris
4. Klik halaman 3 pada pagination
5. Verifikasi halaman 3 berisi 5 baris, sehingga daftar memuat seluruh 25 pengguna organisasi
6. Ketik Search `Budi Santoso`, tekan Enter
7. Hover sakelar Active baris Budi Santoso
8. Verifikasi sakelar Active Show Disabled dengan tooltip `You don't have permission to edit.`
9. Verifikasi Table Tools User List tampil
10. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
11. Buka row action menu `⋯` baris Hana Kusuma (Pending Activation)
12. Verifikasi row action `Resend Activation Email`, `Resend Confirmation Email`, dan `Edit Home Group` Hidden
13. Tutup row action menu dengan menekan Esc
14. Klik `(←)` pada kotak Search
15. Verifikasi kolom checkbox Hidden (header dan seluruh baris)
16. Verifikasi Bulk Actions Bar tidak muncul
17. Ketik Search `Budi Santoso`, tekan Enter
18. Buka Detail Budi Santoso lalu Tab Role (Sub-tab Global Role)
19. Hover switch Global Role dan checkbox C/R/U/D
20. Verifikasi switch dan checkbox C/R/U/D Show Disabled dengan tooltip `You don't have permission to edit.`
21. Buka Sub-tab Group Role
22. Verifikasi `[Detail]` pada baris Group Role Show Enabled
23. Verifikasi `[Assign Group]` Hidden
24. Buka Sub-tab Transaction Role
25. Verifikasi Sub-tab Transaction Role tampil
26. Verifikasi `[+ Assign]`, `Remove`, dan `[Bulk Remove]` Hidden
27. Verifikasi Tab Responsibilities, Non-Login User, Changelog, System Log, Transaction Admin Log, User Log, dan ikon Changelog Show

### TC-FA-SU-53: Visibilitas elemen UI untuk Manage global user & role dengan Update

28. Ganti akun: logout lalu login sebagai Manage global user & role (Update) (Qori Akbar)
29. Buka Settings > User dari sidebar
30. Verifikasi halaman 1 tabel User List berisi 10 baris tanpa batasan grup
31. Klik halaman 2 pada pagination
32. Verifikasi halaman 2 berisi 10 baris
33. Klik halaman 3 pada pagination
34. Verifikasi halaman 3 berisi 5 baris, sehingga daftar memuat seluruh 25 pengguna organisasi
35. Ketik Search `Budi Santoso`, tekan Enter
36. Verifikasi sakelar Active baris Budi Santoso Enabled
37. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
38. Buka row action menu `⋯` baris Hana Kusuma (Pending Activation)
39. Verifikasi row action `Resend Activation Email` Show Enabled
40. Verifikasi row action `Edit Home Group` Show
41. Tutup row action menu dengan menekan Esc
42. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
43. Centang baris Budi Santoso
44. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter
45. Centang baris Lina Marlina
46. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
47. Centang baris Citra Lestari
48. Verifikasi Bulk Actions Bar menampilkan `Activate`, `Deactivate`, dan `Edit Home Group`
49. Klik Bulk Action > `[Deactivate]`
50. Verifikasi dialog campuran mencantumkan Lina Marlina dan Citra Lestari pada kelompok `The following will be skipped (already inactive, inactive in Global Settings, or no permission):`
51. Klik `[Cancel]` pada dialog
52. Klik Unselect All
53. Klik `(←)` pada kotak Search
54. Ketik Search `Budi Santoso`, tekan Enter
55. Buka Detail Budi Santoso lalu Tab Role (Sub-tab Global Role)
56. Verifikasi switch dan checkbox C/R/U/D Global Role Enabled
57. Buka Sub-tab Group Role
58. Verifikasi `[Assign Group]` Enabled
59. Buka Sub-tab Transaction Role
60. Verifikasi `[+ Assign]`, `Remove`, dan `[Assign Group]` Enabled

Untuk setiap target pada tabel "Target terkunci" di `## Prerequisites` (Lina Marlina, lalu Citra Lestari), jalankan langkah 61 sampai 68.

61. Kembali ke User List
62. Ganti isi kotak search dengan nama target, tekan Enter
63. Buka Detail target lalu Tab Role (Sub-tab Global Role)
64. Hover switch Global Role dan checkbox C/R/U/D
65. Verifikasi switch dan checkbox C/R/U/D Disabled dengan tooltip `You don't have permission to edit.`
66. Buka Sub-tab Group Role
67. Hover `[Assign Group]`
68. Verifikasi `[Assign Group]` Disabled dengan tooltip `You don't have permission to edit.`

### TC-FA-SU-54: Visibilitas elemen UI untuk Manage global user & role tanpa Update (Read saja)

69. Ganti akun: logout lalu login sebagai Manage global user & role (Read saja) (Rina Susanti)
70. Buka Settings > User dari sidebar
71. Ketik Search `Budi Santoso`, tekan Enter
72. Hover sakelar Active baris Budi Santoso
73. Verifikasi sakelar Active Disabled dengan tooltip `You don't have permission to edit.`
74. Verifikasi Table Tools User List tampil
75. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
76. Buka row action menu `⋯` baris Hana Kusuma (Pending Activation)
77. Verifikasi row action `Resend Activation Email`, `Resend Confirmation Email`, dan `Edit Home Group` Hidden
78. Tutup row action menu dengan menekan Esc
79. Klik `(←)` pada kotak Search
80. Verifikasi kolom checkbox Hidden
81. Verifikasi Bulk Actions Bar tidak muncul
82. Ketik Search `Budi Santoso`, tekan Enter
83. Buka Detail Budi Santoso, Tab Role, lalu Sub-tab Group Role
84. Verifikasi sedikitnya satu baris Group Role tampil
85. Verifikasi `[Assign Group]` Hidden
86. Buka Sub-tab Transaction Role
87. Verifikasi Sub-tab Transaction Role tampil
88. Verifikasi `[+ Assign]`, `Remove`, dan `[Bulk Remove]` Hidden
89. Klik segmen Breadcrumb `User`
90. Klik `(←)` pada kotak Search
91. Verifikasi halaman 1 tabel User List berisi 10 baris (row scope tetap seluruh pengguna)
92. Klik halaman 2 pada pagination
93. Verifikasi halaman 2 berisi 10 baris
94. Klik halaman 3 pada pagination
95. Verifikasi halaman 3 berisi 5 baris, sehingga daftar memuat seluruh 25 pengguna organisasi

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Role Matrix (bagian 3a) ditulis per blok role: langkah tiap aktor tidak identik (TC-FA-SU-53 memuat blok target terkunci) dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Judul tanpa kata Positif atau Negatif karena spec memuat tampil dan Hidden/Disabled.
- Spec melewati sekitar 35 langkah (95 langkah). Alasan: seluruh blok satu kelas (fungsional Role Matrix, hanya membaca), TC-FA-SU-52, TC-FA-SU-53, dan TC-FA-SU-54 berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan tiap blok menambah satu ganti akun eksplisit. Langkah 61 sampai 68 diulang untuk dua target (ekspansi 103 langkah) dengan parameter di tabel `## Prerequisites`.
- TC-FA-SU-50 dan TC-FA-SU-51 ada di spec 017.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 13, 41, dan 78 (menutup row action menu), 52 (membatalkan seleksi, S-09), 61 (kembali ke User List), 89 (kembali ke User List lewat Breadcrumb karena kotak Search masih berisi nama baris sebelumnya), langkah 6, 17, 35, 54, 71, dan 82 ("Ketik Search" nama baris target sebelum Verifikasi, hover, membuka `⋯`, atau Buka Detail, R-16, bagian 8b butir 13), langkah 10, 37, 75, 42, 44, 46, dan 62 (mengganti isi kotak search yang masih berisi nama sebelumnya, termasuk target iterasi sebelumnya pada blok berulang, bagian 8b butir 9; karena User List memuat 3 halaman dan Lina Marlina ada di halaman 2, R-16, bagian 8b butir 13), langkah 14, 79, 53, dan 90 (menutup input Search dan mereset tabel supaya asersi kolom checkbox, Bulk Actions Bar, dan jumlah baris memakai tabel penuh, S-09), langkah 2, 4, 31, 33, 92, dan 94 (pindah halaman pagination supaya jumlah baris tiap halaman dan total 25 pengguna teramati, S-14).
- Langkah 9, 25, 74, dan 87 adalah anchor permukaan untuk asersi Hidden pada Role Matrix (bagian 8b butir 2 dan 11). Langkah 84 adalah anchor positif untuk Hidden `[Assign Group]` langkah 85. Langkah 22 (`[Detail]` Enabled) adalah klausa c TC-FA-SU-52 sekaligus anchor untuk langkah 23.
- Langkah 49 sampai 51 (TC-FA-SU-53) tidak ada di langkah TC: Expected b menyebut target Total Control dan Read Only "di-skip" pada Bulk Activate dan Deactivate tanpa langkah aksi. Spec membuka dialog Bulk Deactivate dan membatalkannya sehingga kelompok skip teramati tanpa mengubah data (S-03, alasan: Expected b tanpa aksi). Skip pada Bulk Activate tidak dibuka di spec ini karena Lina Marlina dan Citra Lestari aktif sehingga skip karena tier tidak dapat dibedakan dari "already active"; skip karena tier pada Activate diasersi di TC-FA-SU-1065 (spec 027).
- Teks dialog campuran dikutip dari TC-FA-SU-1063 (kelompok `The following will be skipped (already inactive, inactive in Global Settings, or no permission):`) dan label `[Cancel]` mengikuti konvensi dialog konfirmasi (bagian 9, label tombol).
- Temuan untuk QA:
  - Expected a TC-FA-SU-52, 53, dan 54 menyebut "seluruh pengguna" tanpa jumlah; spec memakai 25 pengguna Pre-setup #20 (halaman 1: 10, halaman 2: 10, halaman 3: 5) dan memeriksa tiap halaman lewat pagination (S-14), bukan menyatakan 25 pengguna pada satu langkah.
  - Email akun #4 dan #5 tidak tertulis di Pre-setup TC; password tidak diberi nama env di TC.
  - TC-FA-SU-52 dan TC-FA-SU-54 Expected b menyebut row action Hidden tanpa menyebut apakah menu `⋯` tetap ada bagi Read Only; spec membuka menu `⋯` baris Hana Kusuma dan mengasumsikan menu tampil dengan item lain (atau mengikuti keputusan tim FE bila menu itu sendiri Hidden).
  - TC-FA-SU-53 Expected b "target Total Control dan Read Only di-skip" tanpa langkah aksi (lihat butir di atas); TC-FA-SU-53 Expected c tidak menyebut apakah `[Assign Group]` pada target Total Control atau Read Only ikut Disabled; spec mengasersi Disabled dengan tooltip yang sama (konsisten dengan TC-FA-SU-72).
  - TC-FA-SU-54 Expected c "row scope tetap seluruh pengguna organisasi" tidak punya langkah di TC; spec mengamati User List pada langkah 89 sampai 95.
  - TC-FA-SU-52 dan 53 tidak menyebut pengguna sasaran Detail; spec memakai Budi Santoso (target biasa).
  - TC-FA-SU-53 Langkah Uji 2 tidak menyebut cara memilih tiga baris yang tersebar di beberapa halaman; spec memilih tiap baris lewat Search (langkah 42 sampai 47) dan mengasumsikan seleksi bertahan lintas pergantian Search seperti lintas halaman (TC-FA-SU-120 Expected a); mohon konfirmasi.
