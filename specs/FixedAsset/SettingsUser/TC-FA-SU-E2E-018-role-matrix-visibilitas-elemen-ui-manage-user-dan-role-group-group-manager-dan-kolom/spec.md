---
id: TC-FA-SU-E2E-018-role-matrix-visibilitas-elemen-ui-manage-user-dan-role-group-group-manager-dan-kolom
title: "Role Matrix: Visibilitas Elemen UI Manage user & role Group, Group Manager, dan Kolom Checkbox"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-55
  - TC-FA-SU-56
  - TC-FA-SU-57
  - TC-FA-SU-86
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen UI Manage user & role Group, Group Manager, dan Kolom Checkbox

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage user & role Group (Update) (Sinta Dewi, Pre-setup #6); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke Total Control (Lina Marlina). Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Role yang diuji (satu blok per aktor karena ganti akun menuntut Step eksplisit):

| Aktor | Pre-setup | Nama | Email | Env password |
|---|---|---|---|---|
| Manage user & role Group (Update) | #6 | Sinta Dewi | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURGR_UPD_PASSWORD` |
| Manage user & role Group (Read saja) | #7 | Teguh Prakoso | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURGR_RO_PASSWORD` |
| Group Manager (IT Infrastructure dan Accounts Payable) | #9 | Oscar Pranata | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_GM_PASSWORD` |
| Manage global user & role (Read saja) | #5 | Rina Susanti | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURG_RO_PASSWORD` |
| Total Control | #1 | Lina Marlina | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Nama env `FA_MURGR_UPD_PASSWORD`, `FA_MURGR_RO_PASSWORD`, `FA_GM_PASSWORD`, dan `FA_MURG_RO_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; satu nama satu arti. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` dengan 25 pengguna (#20), pohon grup (#21: Finance & Accounting dengan anak Accounts Payable, IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse), tier dan penugasan (#23). Scope Finance & Accounting (aktor Sinta Dewi dan Teguh Prakoso): 12 pengguna yaitu Ahmad Dahlan, Budi Santoso, Citra Lestari, Gita Permata, Lina Marlina, Nanda Pratama, Oscar Pranata, Putri Anggraeni, Sinta Dewi, Teguh Prakoso, Umar Faruq, dan Wawan Setiawan. Scope IT Infrastructure (aktor Oscar Pranata): 8 pengguna yaitu Ahmad Dahlan, Citra Lestari, Indra Wijaya, Lina Marlina, Oscar Pranata, Putri Anggraeni, Qori Akbar, dan Wawan Setiawan. Pengguna Pending Email Confirmation dalam scope Oscar Pranata: Indra Wijaya.
- Data Dinamis: tidak ada.
- Kemampuan teknis: login dan logout bergantian antar akun pada satu sesi browser; hover elemen.
- State global: tidak ada yang diubah; data Pre-setup tidak diubah.

## Test Steps

### TC-FA-SU-55: Visibilitas elemen UI untuk Manage user & role Group dengan Update

1. Verifikasi halaman 1 User List berisi 10 baris yang seluruhnya termasuk 12 nama scope Finance & Accounting
2. Klik halaman 2 pada Pagination
3. Verifikasi halaman 2 berisi 2 baris sisanya sehingga halaman 1 dan 2 memuat tepat 12 nama scope Finance & Accounting
4. Ketik Search `Budi Santoso`, tekan Enter
5. Verifikasi sakelar Active baris Budi Santoso (dalam scope) Enabled
6. Verifikasi Table Tools User List tampil
7. Buka row action menu `⋯` baris Budi Santoso
8. Verifikasi row action `Edit Home Group` Hidden
9. Tutup row action menu dengan menekan Esc
10. Centang baris Budi Santoso
11. Verifikasi Bulk Actions Bar menampilkan `Activate` dan `Deactivate`
12. Verifikasi `Edit Home Group` (Bulk Edit Home Group) Hidden pada Bulk Actions Bar
13. Hapus centang baris Budi Santoso
14. Buka Detail Budi Santoso lalu Tab Role (Sub-tab Global Role)
15. Hover switch Global Role dan checkbox C/R/U/D
16. Verifikasi switch dan checkbox C/R/U/D Global Role Disabled dengan tooltip `You don't have permission to edit.`
17. Buka Sub-tab Group Role
18. Verifikasi baris Group Role Budi Santoso pada Finance & Accounting Enabled
19. Verifikasi `[Assign Group]` Enabled

### TC-FA-SU-56: Visibilitas elemen UI untuk Manage user & role Group tanpa Update (Read saja)

20. Ganti akun: logout lalu login sebagai Manage user & role Group (Read saja) (Teguh Prakoso)
21. Buka Settings > User dari sidebar
22. Verifikasi halaman 1 User List berisi 10 baris yang seluruhnya termasuk 12 nama scope Finance & Accounting
23. Klik halaman 2 pada Pagination
24. Verifikasi halaman 2 berisi 2 baris sisanya sehingga halaman 1 dan 2 memuat tepat 12 nama scope Finance & Accounting
25. Ketik Search `Budi Santoso`, tekan Enter
26. Hover sakelar Active baris Budi Santoso
27. Verifikasi sakelar Active Disabled dengan tooltip `You don't have permission to edit.`
28. Verifikasi Table Tools User List tampil
29. Buka row action menu `⋯` baris Budi Santoso
30. Verifikasi row action `Resend Activation Email`, `Resend Confirmation Email`, dan `Edit Home Group` Hidden
31. Tutup row action menu dengan menekan Esc
32. Verifikasi kolom checkbox Hidden
33. Verifikasi Bulk Actions Bar tidak muncul

### TC-FA-SU-57: Visibilitas elemen UI untuk Group Manager

34. Ganti akun: logout lalu login sebagai Group Manager (Oscar Pranata)
35. Buka Settings > User dari sidebar
36. Verifikasi tabel User List memuat tepat 8 pengguna scope IT Infrastructure pada satu halaman
37. Ketik Search `Indra Wijaya`, tekan Enter
38. Verifikasi sakelar Active baris Indra Wijaya Enabled
39. Verifikasi Table Tools User List tampil
40. Buka row action menu `⋯` baris Indra Wijaya (Pending Email Confirmation)
41. Verifikasi row action `Resend Confirmation Email` Show Enabled
42. Verifikasi row action `Edit Home Group` Hidden
43. Tutup row action menu dengan menekan Esc
44. Centang baris Indra Wijaya
45. Verifikasi Bulk Actions Bar menampilkan `Activate` dan `Deactivate`
46. Verifikasi `Edit Home Group` (Bulk Edit Home Group) Hidden pada Bulk Actions Bar
47. Hapus centang baris Indra Wijaya
48. Buka Detail Indra Wijaya lalu Tab Role (Sub-tab Global Role)
49. Hover switch Global Role dan checkbox C/R/U/D
50. Verifikasi switch dan checkbox C/R/U/D Global Role Disabled dengan tooltip `You don't have permission to edit.`

### TC-FA-SU-86: Aktor tanpa Update tidak melihat kolom checkbox, Bulk Actions Bar tidak dapat muncul

51. Ganti akun: logout lalu login sebagai Manage global user & role (Read saja) (Rina Susanti)
52. Buka Settings > User dari sidebar
53. Verifikasi header kolom Name tampil
54. Verifikasi kolom checkbox tidak dirender pada header tabel
55. Ketik Search `Ahmad Dahlan`, tekan Enter
56. Verifikasi baris Ahmad Dahlan (Default User) tampil tanpa checkbox
57. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
58. Hover sakelar Active baris Budi Santoso
59. Verifikasi sakelar Active Disabled dengan tooltip `You don't have permission to edit.`
60. Ganti isi kotak search dengan `Rina Susanti`, tekan Enter
61. Verifikasi baris Rina Susanti (akun sendiri) tampil tanpa checkbox
62. Klik `(←)` pada kotak Search
63. Verifikasi Bulk Actions Bar tidak muncul
64. Ganti akun: logout lalu login sebagai Total Control (Lina Marlina)
65. Buka Settings > User dari sidebar
66. Ketik Search `Ahmad Dahlan`, tekan Enter
67. Hover checkbox baris Ahmad Dahlan
68. Verifikasi checkbox baris Ahmad Dahlan Disabled dengan tooltip `Default User cannot be modified.`
69. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter
70. Hover checkbox baris Lina Marlina
71. Verifikasi checkbox baris Lina Marlina (akun sendiri) Disabled dengan tooltip `You can't manage your own account from here.`
72. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Role Matrix (bagian 3a) ditulis per blok role: langkah tiap aktor berbeda dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Judul tanpa kata Positif atau Negatif karena spec memuat tampil dan Hidden/Disabled.
- Spec melewati sekitar 35 langkah (72 langkah). Alasan: seluruh blok satu kelas (fungsional Role Matrix, hanya membaca), keempat TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan tiap blok menuntut ganti akun eksplisit (lima akun).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Search untuk menemukan baris target pada langkah 4, 25, 37, 55, 57, 60, 66, 69 dan menutup Search pada langkah 62 dan 72 (R-16); menutup row action menu pada langkah 9, 31, 43; menghapus centang pada langkah 13 dan 47.
- Langkah 6, 28, dan 39 adalah anchor permukaan untuk asersi Hidden (bagian 8b butir 2 dan 11); langkah 53 adalah anchor positif untuk Hidden kolom checkbox langkah 54, 56, dan 61.
- Teks tooltip checkbox pada langkah 68 dan 71 dikutip dari TC-FA-SU-70 (`Default User cannot be modified.`) dan TC-FA-SU-71 (`You can't manage your own account from here.`) karena TC-FA-SU-86 menyebut "tooltip masing-masing" tanpa teks (R-14).
- TC-FA-SU-55, 56, dan 57 tidak punya langkah aksi tulis; asersi "kontrol tulis" dibatasi pada kontrol yang disebut Expected dan dapat diamati tanpa mengubah data.
- Temuan untuk QA:
  - TC-FA-SU-55 Expected b dan TC-FA-SU-56 Expected a menyebut Resend Show Enabled dalam scope, tetapi tidak ada pengguna berstatus Pending Activation atau Pending Email Confirmation dalam scope Finance & Accounting pada Pre-setup #20 (Hana Kusuma, Kartika Sari, Indra Wijaya, dan Lukman Hakim berada di luar scope); asersi Resend tidak dapat diamati dan tidak ditulis untuk Sinta Dewi. Untuk Teguh Prakoso, asersi Hidden Resend (langkah 30) mengasersi item menu pada baris Budi Santoso yang berstatus aktif sehingga Resend tidak pernah tampil di baris itu; QA perlu menambah pengguna Pending dalam scope pada Pre-setup agar kedua klausa bermakna.
  - TC-FA-SU-55 Expected b "Resend Show Enabled dalam scope" dan Expected d "Group Role Enabled pada grup dalam scope" tidak menyebut baris sasaran; spec memakai Budi Santoso (Group Role Manage group pada Finance & Accounting).
  - TC-FA-SU-56 Expected a menyebut "kontrol lain Hidden" tanpa daftar; spec mengasersi Resend dan Edit Home Group pada row action, kolom checkbox, dan Bulk Actions Bar; kontrol Detail (`[Assign Group]`, `[+ Assign]`, `Remove`) tidak diasersi di spec ini.
  - TC-FA-SU-57 Expected a menyebut "pengguna Total Control dan Read Only" dalam scope Group Manager dan tidak menyebut pengguna Pending dalam scope; spec memakai Indra Wijaya (Pending Email Confirmation) untuk Resend.
  - TC-FA-SU-57 Expected b "Kolom dan kontrol mengikuti kolom Manage user & role Group" tidak menyebut daftar kontrol; spec mengasersi sakelar Active, Resend Confirmation Email, Edit Home Group, dan Bulk Actions Bar.
  - Email akun #5, #6, #7, dan #9 tidak tertulis di Pre-setup TC; password tidak diberi nama env di TC.
  - TC-FA-SU-86 Expected c tidak menyebut teks tooltip; spec memakai teks dari TC-FA-SU-70 dan TC-FA-SU-71.
