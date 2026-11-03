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
- Target terkunci (langkah 50 sampai 56, TC-FA-SU-53): Lina Marlina (Total Control) lalu Citra Lestari (Read Only).
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
6. Klik halaman 1 pada pagination
7. Hover sakelar Active baris Budi Santoso
8. Verifikasi sakelar Active Show Disabled dengan tooltip `You don't have permission to edit.`
9. Verifikasi Table Tools User List tampil
10. Buka row action menu `⋯` baris Hana Kusuma (Pending Activation)
11. Verifikasi row action `Resend Activation Email`, `Resend Confirmation Email`, dan `Edit Home Group` Hidden
12. Tutup row action menu dengan menekan Esc
13. Verifikasi kolom checkbox Hidden (header dan seluruh baris)
14. Verifikasi Bulk Actions Bar tidak muncul
15. Buka Detail Budi Santoso lalu Tab Role (Sub-tab Global Role)
16. Hover switch Global Role dan checkbox C/R/U/D
17. Verifikasi switch dan checkbox C/R/U/D Show Disabled dengan tooltip `You don't have permission to edit.`
18. Buka Sub-tab Group Role
19. Verifikasi `[Detail]` pada baris Group Role Show Enabled
20. Verifikasi `[Assign Group]` Hidden
21. Buka Sub-tab Transaction Role
22. Verifikasi Sub-tab Transaction Role tampil
23. Verifikasi `[+ Assign]`, `Remove`, dan `[Bulk Remove]` Hidden
24. Verifikasi Tab Responsibilities, Non-Login User, Changelog, System Log, Transaction Admin Log, User Log, dan ikon Changelog Show

### TC-FA-SU-53: Visibilitas elemen UI untuk Manage global user & role dengan Update

25. Ganti akun: logout lalu login sebagai Manage global user & role (Update) (Qori Akbar)
26. Buka Settings > User dari sidebar
27. Verifikasi halaman 1 tabel User List berisi 10 baris tanpa batasan grup
28. Klik halaman 2 pada pagination
29. Verifikasi halaman 2 berisi 10 baris
30. Klik halaman 3 pada pagination
31. Verifikasi halaman 3 berisi 5 baris, sehingga daftar memuat seluruh 25 pengguna organisasi
32. Klik halaman 1 pada pagination
33. Verifikasi sakelar Active baris Budi Santoso Enabled
34. Buka row action menu `⋯` baris Hana Kusuma (Pending Activation)
35. Verifikasi row action `Resend Activation Email` Show Enabled
36. Verifikasi row action `Edit Home Group` Show
37. Tutup row action menu dengan menekan Esc
38. Centang baris Budi Santoso, Lina Marlina, dan Citra Lestari
39. Verifikasi Bulk Actions Bar menampilkan `Activate`, `Deactivate`, dan `Edit Home Group`
40. Klik Bulk Action > `[Deactivate]`
41. Verifikasi dialog campuran mencantumkan Lina Marlina dan Citra Lestari pada kelompok `The following will be skipped (already inactive, inactive in Global Settings, or no permission):`
42. Klik `[Cancel]` pada dialog
43. Klik Unselect All
44. Buka Detail Budi Santoso lalu Tab Role (Sub-tab Global Role)
45. Verifikasi switch dan checkbox C/R/U/D Global Role Enabled
46. Buka Sub-tab Group Role
47. Verifikasi `[Assign Group]` Enabled
48. Buka Sub-tab Transaction Role
49. Verifikasi `[+ Assign]`, `Remove`, dan `[Assign Group]` Enabled

Untuk setiap target pada tabel "Target terkunci" di `## Prerequisites` (Lina Marlina, lalu Citra Lestari), jalankan langkah 50 sampai 56.

50. Kembali ke User List
51. Buka Detail target lalu Tab Role (Sub-tab Global Role)
52. Hover switch Global Role dan checkbox C/R/U/D
53. Verifikasi switch dan checkbox C/R/U/D Disabled dengan tooltip `You don't have permission to edit.`
54. Buka Sub-tab Group Role
55. Hover `[Assign Group]`
56. Verifikasi `[Assign Group]` Disabled dengan tooltip `You don't have permission to edit.`

### TC-FA-SU-54: Visibilitas elemen UI untuk Manage global user & role tanpa Update (Read saja)

57. Ganti akun: logout lalu login sebagai Manage global user & role (Read saja) (Rina Susanti)
58. Buka Settings > User dari sidebar
59. Hover sakelar Active baris Budi Santoso
60. Verifikasi sakelar Active Disabled dengan tooltip `You don't have permission to edit.`
61. Verifikasi Table Tools User List tampil
62. Buka row action menu `⋯` baris Hana Kusuma (Pending Activation)
63. Verifikasi row action `Resend Activation Email`, `Resend Confirmation Email`, dan `Edit Home Group` Hidden
64. Tutup row action menu dengan menekan Esc
65. Verifikasi kolom checkbox Hidden
66. Verifikasi Bulk Actions Bar tidak muncul
67. Buka Detail Budi Santoso, Tab Role, lalu Sub-tab Group Role
68. Verifikasi sedikitnya satu baris Group Role tampil
69. Verifikasi `[Assign Group]` Hidden
70. Buka Sub-tab Transaction Role
71. Verifikasi Sub-tab Transaction Role tampil
72. Verifikasi `[+ Assign]`, `Remove`, dan `[Bulk Remove]` Hidden
73. Buka Settings > User dari sidebar
74. Verifikasi halaman 1 tabel User List berisi 10 baris (row scope tetap seluruh pengguna)
75. Klik halaman 2 pada pagination
76. Verifikasi halaman 2 berisi 10 baris
77. Klik halaman 3 pada pagination
78. Verifikasi halaman 3 berisi 5 baris, sehingga daftar memuat seluruh 25 pengguna organisasi

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Role Matrix (bagian 3a) ditulis per blok role: langkah tiap aktor tidak identik (TC-FA-SU-53 memuat blok target terkunci) dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Judul tanpa kata Positif atau Negatif karena spec memuat tampil dan Hidden/Disabled.
- Spec melewati sekitar 35 langkah (78 langkah). Alasan: seluruh blok satu kelas (fungsional Role Matrix, hanya membaca), TC-FA-SU-52, TC-FA-SU-53, dan TC-FA-SU-54 berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan tiap blok menambah satu ganti akun eksplisit. Langkah 50 sampai 56 diulang untuk dua target (ekspansi 85 langkah) dengan parameter di tabel `## Prerequisites`.
- TC-FA-SU-50 dan TC-FA-SU-51 ada di spec 017.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 12, 37, dan 64 (menutup row action menu), 43 (membatalkan seleksi, S-09), 50 (kembali ke User List), langkah 2, 4, 6, 28, 30, 32, 75, dan 77 (pindah halaman pagination supaya jumlah baris tiap halaman dan total 25 pengguna teramati, S-14; langkah 6 dan 32 mengembalikan tabel ke halaman 1 untuk langkah sesudahnya).
- Langkah 9, 22, 61, dan 71 adalah anchor permukaan untuk asersi Hidden pada Role Matrix (bagian 8b butir 2 dan 11). Langkah 68 adalah anchor positif untuk Hidden `[Assign Group]` langkah 69. Langkah 19 (`[Detail]` Enabled) adalah klausa c TC-FA-SU-52 sekaligus anchor untuk langkah 20.
- Langkah 40 sampai 42 (TC-FA-SU-53) tidak ada di langkah TC: Expected b menyebut target Total Control dan Read Only "di-skip" pada Bulk Activate dan Deactivate tanpa langkah aksi. Spec membuka dialog Bulk Deactivate dan membatalkannya sehingga kelompok skip teramati tanpa mengubah data (S-03, alasan: Expected b tanpa aksi). Skip pada Bulk Activate tidak dibuka di spec ini karena Lina Marlina dan Citra Lestari aktif sehingga skip karena tier tidak dapat dibedakan dari "already active"; skip karena tier pada Activate diasersi di TC-FA-SU-1065 (spec 027).
- Teks dialog campuran dikutip dari TC-FA-SU-1063 (kelompok `The following will be skipped (already inactive, inactive in Global Settings, or no permission):`) dan label `[Cancel]` mengikuti konvensi dialog konfirmasi (bagian 9, label tombol).
- Temuan untuk QA:
  - Expected a TC-FA-SU-52, 53, dan 54 menyebut "seluruh pengguna" tanpa jumlah; spec memakai 25 pengguna Pre-setup #20 (halaman 1: 10, halaman 2: 10, halaman 3: 5) dan memeriksa tiap halaman lewat pagination (S-14), bukan menyatakan 25 pengguna pada satu langkah.
  - Email akun #4 dan #5 tidak tertulis di Pre-setup TC; password tidak diberi nama env di TC.
  - TC-FA-SU-52 dan TC-FA-SU-54 Expected b menyebut row action Hidden tanpa menyebut apakah menu `⋯` tetap ada bagi Read Only; spec membuka menu `⋯` baris Hana Kusuma dan mengasumsikan menu tampil dengan item lain (atau mengikuti keputusan tim FE bila menu itu sendiri Hidden).
  - TC-FA-SU-53 Expected b "target Total Control dan Read Only di-skip" tanpa langkah aksi (lihat butir di atas); TC-FA-SU-53 Expected c tidak menyebut apakah `[Assign Group]` pada target Total Control atau Read Only ikut Disabled; spec mengasersi Disabled dengan tooltip yang sama (konsisten dengan TC-FA-SU-72).
  - TC-FA-SU-54 Expected c "row scope tetap seluruh pengguna organisasi" tidak punya langkah di TC; spec mengamati User List pada langkah 73 sampai 78.
  - TC-FA-SU-52 dan 53 tidak menyebut pengguna sasaran Detail; spec memakai Budi Santoso (target biasa).
