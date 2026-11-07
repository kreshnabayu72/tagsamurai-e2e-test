---
id: TC-FA-SU-E2E-007-screening-detail-user-header-general-information-dan-custom-field
title: "Screening Detail User: Header, General Information, dan Custom Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-20
  - TC-FA-SU-21
  - TC-FA-SU-22
  - TC-FA-SU-29
coverage:
  web: automated
---

# Screening Detail User: Header, General Information, dan Custom Field

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup (hanya dibaca kecuali disebut di bawah): Client `FaUserMain` dengan 25 pengguna (#20); Responsibilities Budi Santoso (#24, #25) dan Non-Login User Budi Santoso (#26) untuk angka `(N)` pada tab bar; Custom Field `Shift` aktif bertipe Dropdown (#31); Global Settings (#38: Rudi Hartono nonaktif di Global Settings dengan sakelar FAMS ON, Hana Kusuma Pending Activation, Indra Wijaya Pending Email Confirmation, Doni Prasetyo Inactive, Fajar Nugroho Temporary User sampai 31/12/26). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Pre-setup yang diubah: Custom Field `Shift` dinonaktifkan lewat seed API pada langkah 64 dan diaktifkan kembali pada langkah 67 (varian kedua nonaktif Pre-setup #31); plan Client diubah menjadi Starter oleh Principal Automation (Pre-setup #12) pada langkah 53 dan dikembalikan pada langkah 56. Pemulihan keduanya juga di hook `after`. Efeknya pada Last Updated: tidak ada perubahan pada baris pengguna.
- Data Dinamis: satu pengguna tanpa Home Group, nama `Zzz Tanpa Home Group {runId}-007`, email `tanpa.homegroup+{runId}-007@qwertysystem.net`, di-seed lewat API di hook `before` dan dihapus di hook `after`; nama diawali `Zzz` supaya menjadi baris terakhir halaman 3.
- Kemampuan teknis: Principal Automation mengubah plan Client dan seed API mengubah status aktif Custom Field (disediakan tim FE/BE); pembacaan hover hierarki Home Group.
- State global: plan Client dan status Custom Field `Shift`; dipulihkan langkah 56, 67, dan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-20: Screening Detail User: Breadcrumb, header, dan General Information

1. Ketik Search `Budi Santoso`, tekan Enter
2. Klik nama `Budi Santoso` di User List
3. Verifikasi Breadcrumb `Settings > User > Detail` (tiga segmen) tanpa Page Title
4. Verifikasi segmen `Settings` dan segmen terakhir `Detail` berupa label statis
5. Verifikasi header kartu memuat Avatar (fallback inisial), Full Name `Budi Santoso` dengan badge `Active`, dan subtitle Employee ID `EMP-10015`
6. Verifikasi di kanan header tampil sakelar Active dan tombol Resend kondisional
7. Verifikasi General Information grid 4 kolom baris 1: Email, User Type, Position, Division
8. Verifikasi General Information baris 2: Home Group (badge + ikon edit untuk aktor berwenang), Temporary Until (hanya Temporary User), TAG
9. Verifikasi Foto, Full Name, Employee ID, dan Status tidak diulang di General Information
10. Verifikasi tab bar `Role`, `Responsibilities (N)`, `Non-Login User (N)`, `Changelog`, `System Log`, `Transaction Admin Log`, `User Log`
11. Verifikasi tab pertama aktif `Role` dengan sub-tab `Global Role`

### TC-FA-SU-21: Header Detail: badge Active/Inactive mengikuti status aktif efektif dan sakelar tetap posisi FAMS

12. Verifikasi header Budi Santoso (Active di FAMS dan Global) menampilkan badge `Active`
13. Verifikasi sakelar Budi Santoso ON
14. Klik segmen Breadcrumb `User`
15. Verifikasi User List tampil
16. Ganti isi kotak search dengan `Doni Prasetyo`, tekan Enter
17. Klik nama `Doni Prasetyo`
18. Verifikasi header Doni Prasetyo (Inactive di FAMS) menampilkan badge `Inactive` (danger)
19. Verifikasi sakelar Doni Prasetyo OFF
20. Klik segmen Breadcrumb `User`
21. Ganti isi kotak search dengan `Rudi Hartono`, tekan Enter
22. Klik nama `Rudi Hartono`
23. Verifikasi header Rudi Hartono (nonaktif di Global Settings) menampilkan badge `Inactive`
24. Verifikasi sakelar Rudi Hartono tetap menampilkan posisi FAMS terakhir ON
25. Verifikasi sakelar Rudi Hartono Disabled
26. Klik segmen Breadcrumb `User`
27. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
28. Klik nama `Hana Kusuma`
29. Verifikasi Hana Kusuma menampilkan badge `Pending Activation` di sebelah nama
30. Klik segmen Breadcrumb `User`
31. Ganti isi kotak search dengan `Indra Wijaya`, tekan Enter
32. Klik nama `Indra Wijaya`
33. Verifikasi Indra Wijaya menampilkan badge `Pending Email Confirmation` di sebelah nama
34. Verifikasi badge `Pending Activation` dan `Pending Email Confirmation` saling eksklusif (Hana Kusuma tanpa `Pending Email Confirmation`, Indra Wijaya tanpa `Pending Activation`)

### TC-FA-SU-22: General Information: email pending, Temporary Until, TAG, dan Home Group

35. Verifikasi Indra Wijaya menampilkan teks `Pending email change to [New Email]` di samping Email
36. Verifikasi teks email pending Indra Wijaya tanpa tombol aksi
37. Klik segmen Breadcrumb `User`
38. Ganti isi kotak search dengan `Fajar Nugroho`, tekan Enter
39. Klik nama `Fajar Nugroho`
40. Verifikasi Fajar Nugroho (Temporary User) menampilkan `Temporary until [Date]` (31/12/26) mengikuti format General Settings
41. Verifikasi TAG Fajar Nugroho `—` karena belum paired
42. Klik segmen Breadcrumb `User`
43. Ganti isi kotak search dengan `Zzz Tanpa Home Group {runId}-007`, tekan Enter
44. Klik nama pengguna dinamis `Zzz Tanpa Home Group {runId}-007`
45. Verifikasi Home Group pengguna dinamis `—`
46. Klik segmen Breadcrumb `User`
47. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
48. Klik nama `Budi Santoso`
49. Verifikasi TAG Budi Santoso `TAG-0001`
50. Verifikasi Home Group Budi Santoso menampilkan badge (hover hierarki)
51. Verifikasi Budi Santoso (non-Temporary) tidak menampilkan field Temporary Until
52. Verifikasi General Information Budi Santoso tanpa sel kosong
53. Principal Automation mengubah plan Client menjadi Starter lewat sesi API hingga tersimpan
54. Muat ulang halaman Detail Budi Santoso
55. Verifikasi field TAG tidak tersedia pada plan Starter (Email dan Position tetap tampil)
56. Principal Automation mengembalikan plan Client ke Enterprise lewat sesi API hingga tersimpan

### TC-FA-SU-29: Custom Field accordion pada Detail User

57. Verifikasi accordion `Custom Field` collapsed secara default dengan ikon ▶
58. Klik header accordion `Custom Field`
59. Verifikasi accordion terbuka dengan ikon ▼
60. Verifikasi isi accordion berupa daftar label dan nilai read-only
61. Verifikasi tidak ada edit inline pada accordion
62. Klik header accordion `Custom Field` sekali lagi
63. Verifikasi accordion `Custom Field` collapsed dengan ikon ▶
64. Nonaktifkan Custom Field `Shift` lewat seed API hingga tersimpan
65. Muat ulang halaman Detail Budi Santoso
66. Verifikasi section `Custom Field` Hidden seluruhnya (General Information tampil sebagai anchor permukaan)
67. Aktifkan kembali Custom Field `Shift` lewat seed API hingga tersimpan
68. Klik segmen Breadcrumb `User`
69. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
70. Klik nama `Hana Kusuma`
71. Klik header accordion `Custom Field`
72. Verifikasi field aktif `Shift` tanpa nilai pada Hana Kusuma menampilkan `—`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 20, 21, 22, 29; kunjungan Detail diurut supaya Budi Santoso (langkah 2 dan 13 sampai 14), Indra Wijaya (langkah 32 sampai 36), dan Budi Santoso (langkah 48 sampai 63) tidak dibuka berulang tanpa asersi baru. Langkah Uji "buka Detail ... bergantian" TC-FA-SU-21 dipenuhi dengan kunjungan berurutan pada langkah 13 sampai 34.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14, 20, 26, 30, 37, 42, 46, dan 68 (kembali ke User List lewat Breadcrumb), langkah 1, 16, 21, 27, 31, 38, 43, 47, dan 69 (Search nama baris target sebelum klik nama, supaya spec tidak mengandalkan posisi baris di halaman pada User List 25 pengguna 3 halaman, R-16, bagian 8b butir 13; langkah pertama memakai "Ketik Search" dan sisanya "Ganti isi kotak search" karena kotak masih berisi nama sebelumnya, bagian 8b butir 9; langkah ini menggantikan klik halaman pagination), langkah 54 dan 65 (muat ulang), langkah 62 (klik header accordion `Custom Field` kedua untuk menutup; `Verifikasi` collapsed ada di langkah 63), langkah 53, 56, 64, dan 67 (pemicu state lewat sesi API atau seed; bukan objek asersi UI kedua). Klik nama pada langkah 2, 17, 22, 28, 32, 39, 44, 48, dan 70 membuka Detail. Langkah 15 adalah `Verifikasi` User List sesudah klik segmen Breadcrumb `User` pada langkah 14 (TC-FA-SU-20 Expected a).
- Langkah 55 memakai Email dan Position sebagai pembanding agar asersi absence TAG tidak lolos pada halaman yang belum termuat (bagian 8b butir 2, S-03). Langkah 66 memakai General Information sebagai anchor.
- Spec melewati sekitar 35 langkah (72 langkah). Seluruhnya satu kelas (screening Detail User, satu akun, tanpa mengubah data bisnis; state plan dan Custom Field dipulihkan), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain.
- Pembagian TC lintas spec: User Type Detail User (TC-FA-SU-23 sampai 28) ada di spec 008 dan 009.
- Temuan untuk QA:
  - TC-FA-SU-22 Expected a menyebut `Pending email change to [New Email]` tanpa menyebut alamat email baru Indra Wijaya; spec mengasersi awalan teks dan alamat email baru dari fixture.
  - TC-FA-SU-22 Langkah Uji 1 menyebut "pengguna tanpa Home Group" tetapi Pre-setup #43 memberi Home Group untuk semua 25 pengguna; spec memakai pengguna dinamis tanpa Home Group.
  - TC-FA-SU-22 Expected c ("pada plan Starter field TAG tidak tersedia") tidak punya Langkah Uji dan Pre-setup #20 berplan Enterprise; spec memicu plan Starter lewat Principal Automation (langkah 53), dan Client `FaUserStarter` (#32) tidak dipakai.
  - TC-FA-SU-29 Langkah Uji 3 ("Ulangi pada client tanpa Custom Field aktif") menyebut client lain; spec menonaktifkan Custom Field `Shift` pada Client yang sama lewat seed (varian kedua nonaktif Pre-setup #31) agar tidak berganti tenant.
  - TC-FA-SU-29 Expected b ("field aktif tanpa nilai menampilkan `—`") tidak punya pengguna acuan; spec memakai Hana Kusuma (Shift `—` pada Pre-setup #43).
  - TC-FA-SU-20 Expected e menulis `(N)` pada tab bar tanpa angka; spec mengasersi label tab dengan N dari fixture.
