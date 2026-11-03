---
id: TC-FA-SU-E2E-017-role-matrix-gate-sub-menu-settings-user-dan-visibilitas-elemen-ui-total-control
title: "Role Matrix: Gate Sub-menu Settings > User dan Visibilitas Elemen UI Total Control"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-50
  - TC-FA-SU-51
coverage:
  web: automated
---

# Role Matrix: Gate Sub-menu Settings > User dan Visibilitas Elemen UI Total Control

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Lina Marlina, Pre-setup #1); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke Total Control. Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Role yang diuji (TC-FA-SU-50, satu blok per aktor karena ganti akun menuntut Step eksplisit):

| Aktor | Pre-setup | Nama | Email | Env password |
|---|---|---|---|---|
| Total Control | #1 | Lina Marlina | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Default User | #2 | Ahmad Dahlan | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
| Read Only | #3 | Citra Lestari | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| Manage global user & role (Update) | #4 | Qori Akbar | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURG_UPD_PASSWORD` |
| Manage user & role Group (Update) | #6 | Sinta Dewi | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURGR_UPD_PASSWORD` |
| Group Manager (IT Infrastructure dan Accounts Payable) | #9 | Oscar Pranata | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_GM_PASSWORD` |
| Peran tanpa akses (hanya Manage files) | #10 | Vina Maharani | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_NOACCESS_PASSWORD` |

- Nama env `FA_DU_PASSWORD`, `FA_RO_PASSWORD`, `FA_MURG_UPD_PASSWORD`, `FA_MURGR_UPD_PASSWORD`, `FA_GM_PASSWORD`, dan `FA_NOACCESS_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; satu nama satu arti. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` dengan 25 pengguna (#20) tersebar 3 halaman (10, 10, 5 baris) dan penugasan tier serta Group Role (#23). Target biasa: Budi Santoso; pengguna Pending Activation: Hana Kusuma; pengguna Pending Email Confirmation: Indra Wijaya.
- Data Dinamis: tidak ada.
- Kemampuan teknis: login dan logout bergantian antar akun pada satu sesi browser; hover elemen.
- State global: tidak ada yang diubah; data Pre-setup tidak diubah. Spec membaca saja sehingga tidak butuh pemulihan.

## Test Steps

### TC-FA-SU-50: Gate halaman, sub-menu Settings > User

1. Perluas menu Settings di sidebar
2. Verifikasi sub-menu `Settings > User` Show untuk Total Control (Lina Marlina)
3. Ganti akun: logout lalu login sebagai Default User (Ahmad Dahlan)
4. Perluas menu Settings di sidebar
5. Verifikasi sub-menu `Settings > User` Show untuk Default User (Ahmad Dahlan)
6. Ganti akun: logout lalu login sebagai Read Only (Citra Lestari)
7. Perluas menu Settings di sidebar
8. Verifikasi sub-menu `Settings > User` Show untuk Read Only (Citra Lestari)
9. Ganti akun: logout lalu login sebagai Manage global user & role (Update) (Qori Akbar)
10. Perluas menu Settings di sidebar
11. Verifikasi sub-menu `Settings > User` Show untuk Manage global user & role (Qori Akbar)
12. Ganti akun: logout lalu login sebagai Manage user & role Group (Update) (Sinta Dewi)
13. Perluas menu Settings di sidebar
14. Verifikasi sub-menu `Settings > User` Show untuk Manage user & role Group (Sinta Dewi)
15. Ganti akun: logout lalu login sebagai Group Manager (Oscar Pranata)
16. Perluas menu Settings di sidebar
17. Verifikasi sub-menu `Settings > User` Show untuk Group Manager (Oscar Pranata)
18. Ganti akun: logout lalu login sebagai Peran tanpa akses (Vina Maharani)
19. Perluas menu Settings di sidebar
20. Verifikasi sedikitnya satu item menu lain pada sidebar yang sama tampil
21. Verifikasi sub-menu `Settings > User` Hidden untuk Peran tanpa akses (Vina Maharani)

### TC-FA-SU-51: Visibilitas elemen UI untuk Total Control

22. Ganti akun: logout lalu login sebagai Total Control (Lina Marlina)
23. Buka Settings > User dari sidebar
24. Verifikasi halaman 1 tabel User List berisi 10 baris
25. Klik halaman 2 pada pagination
26. Verifikasi halaman 2 berisi 10 baris
27. Klik halaman 3 pada pagination
28. Verifikasi halaman 3 berisi 5 baris, sehingga daftar memuat seluruh 25 pengguna organisasi
29. Klik halaman 1 pada pagination
30. Verifikasi sakelar Active baris Budi Santoso Enabled
31. Buka row action menu `⋯` baris Hana Kusuma (Pending Activation)
32. Verifikasi row action `Resend Activation Email` Show Enabled
33. Verifikasi row action `Edit Home Group` Show
34. Tutup row action menu dengan menekan Esc
35. Buka row action menu `⋯` baris Indra Wijaya (Pending Email Confirmation)
36. Verifikasi row action `Resend Confirmation Email` Show Enabled
37. Tutup row action menu dengan menekan Esc
38. Verifikasi kolom checkbox Show
39. Centang baris Budi Santoso
40. Verifikasi Bulk Actions Bar menampilkan `Activate`, `Deactivate`, `Edit Home Group`, dan `Resend Activation Email`
41. Hapus centang baris Budi Santoso
42. Buka Detail Budi Santoso lalu Tab Role (Sub-tab Global Role)
43. Verifikasi switch dan checkbox C/R/U/D Global Role Show Enabled
44. Buka Sub-tab Group Role
45. Verifikasi `[Assign Group]` dan `[Detail]` Show
46. Buka Sub-tab Transaction Role
47. Verifikasi `[+ Assign]`, `Remove`, `[Assign Group]`, dan `[Bulk Remove]` Show Enabled
48. Verifikasi Tab Responsibilities, Non-Login User, Changelog, System Log, Transaction Admin Log, User Log, dan ikon Changelog Show

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Role Matrix (bagian 3a) ditulis per blok role: langkah tiap aktor identik, tetapi ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Judul tanpa kata Positif atau Negatif karena spec memuat tampil (Show) dan tersembunyi (Hidden).
- Spec melewati sekitar 35 langkah (48 langkah). Alasan: seluruh blok satu kelas (fungsional Role Matrix, hanya membaca), TC-FA-SU-50 dan TC-FA-SU-51 berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan tujuh aktor TC-FA-SU-50 menuntut ganti akun eksplisit.
- TC-FA-SU-52 sampai TC-FA-SU-54 ada di spec 028.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 34 dan 37 (menutup row action menu), 41 (menghapus centang baris, S-09), langkah 25, 27, dan 29 (pindah halaman pagination supaya jumlah baris tiap halaman dan total 25 pengguna teramati, S-14).
- Langkah 20 adalah anchor positif untuk asersi Hidden langkah 21 (bagian 8b butir 2: item menu lain pada sidebar yang sama sudah tampil).
- Langkah 24 sampai 28 menyatakan "seluruh pengguna" sebagai 25 pengguna Pre-setup #20 (halaman 1: 10, halaman 2: 10, halaman 3: 5) dengan memeriksa tiap halaman; angka itu berasal dari Pre-setup dan TC-FA-SU-58, bukan dari Expected TC-FA-SU-51 (S-02). Langkah 29 mengembalikan tabel ke halaman 1 supaya baris Budi Santoso, Hana Kusuma, dan Indra Wijaya tampil.
- Temuan untuk QA:
  - TC-FA-SU-50 Expected a menyebut Manage user & role Group "dengan maupun tanpa Update", tetapi Data Uji hanya memuat tujuh aktor (#1, #2, #3, #4, #6, #9, #10) tanpa #5 dan #7; spec mengikuti Data Uji (hanya Group Update #6).
  - Email akun #4, #6, #9, dan #10 tidak tertulis di Pre-setup TC; password semua akun selain Total Control tidak diberi nama env di TC.
  - Judul TC-FA-SU-51 menyebut Default User, tetapi precondition, langkah, dan Expected hanya memuat Total Control; tampilan elemen UI Default User tidak diasersi selain gate sub-menu di TC-FA-SU-50.
  - TC-FA-SU-51 Expected a "sesuai status" untuk Resend tidak menyebut baris target; spec memakai Hana Kusuma (Pending Activation) dan Indra Wijaya (Pending Email Confirmation) dari Pre-setup #20.
  - TC-FA-SU-50 dan TC-FA-SU-51 tidak menyebut nama pengguna sasaran untuk Detail; spec memakai Budi Santoso (target biasa, Pre-setup #20).
