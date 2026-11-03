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
- Data Pre-setup yang diubah: Custom Field `Shift` dinonaktifkan lewat seed API pada langkah 60 dan diaktifkan kembali pada langkah 63 (varian kedua nonaktif Pre-setup #31); plan Client diubah menjadi Starter oleh Principal Automation (Pre-setup #12) pada langkah 49 dan dikembalikan pada langkah 52. Pemulihan keduanya juga di hook `after`. Efeknya pada Last Updated: tidak ada perubahan pada baris pengguna.
- Data Dinamis: satu pengguna tanpa Home Group, nama `Zzz Tanpa Home Group {runId}-007`, email `tanpa.homegroup+{runId}-007@qwertysystem.net`, di-seed lewat API di hook `before` dan dihapus di hook `after`; nama diawali `Zzz` supaya menjadi baris terakhir halaman 3.
- Kemampuan teknis: Principal Automation mengubah plan Client dan seed API mengubah status aktif Custom Field (disediakan tim FE/BE); pembacaan hover hierarki Home Group.
- State global: plan Client dan status Custom Field `Shift`; dipulihkan langkah 52, 63, dan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-20: Screening Detail User: Breadcrumb, header, dan General Information

1. Klik nama `Budi Santoso` di User List
2. Verifikasi Breadcrumb `Settings > User > Detail` (tiga segmen) tanpa Page Title
3. Verifikasi segmen `Settings` dan segmen terakhir `Detail` berupa label statis
4. Verifikasi header kartu memuat Avatar (fallback inisial), Full Name `Budi Santoso` dengan badge `Active`, dan subtitle Employee ID `EMP-10015`
5. Verifikasi di kanan header tampil sakelar Active dan tombol Resend kondisional
6. Verifikasi General Information grid 4 kolom baris 1: Email, User Type, Position, Division
7. Verifikasi General Information baris 2: Home Group (badge + ikon edit untuk aktor berwenang), Temporary Until (hanya Temporary User), TAG
8. Verifikasi Foto, Full Name, Employee ID, dan Status tidak diulang di General Information
9. Verifikasi tab bar `Role`, `Responsibilities (N)`, `Non-Login User (N)`, `Changelog`, `System Log`, `Transaction Admin Log`, `User Log`
10. Verifikasi tab pertama aktif `Role` dengan sub-tab `Global Role`

### TC-FA-SU-21: Header Detail: badge Active/Inactive mengikuti status aktif efektif dan sakelar tetap posisi FAMS

11. Verifikasi header Budi Santoso (Active di FAMS dan Global) menampilkan badge `Active`
12. Verifikasi sakelar Budi Santoso ON
13. Klik segmen Breadcrumb `User`
14. Verifikasi User List tampil
15. Klik nama `Doni Prasetyo`
16. Verifikasi header Doni Prasetyo (Inactive di FAMS) menampilkan badge `Inactive` (danger)
17. Verifikasi sakelar Doni Prasetyo OFF
18. Klik segmen Breadcrumb `User`
19. Klik halaman 2 pada pagination
20. Klik nama `Rudi Hartono`
21. Verifikasi header Rudi Hartono (nonaktif di Global Settings) menampilkan badge `Inactive`
22. Verifikasi sakelar Rudi Hartono tetap menampilkan posisi FAMS terakhir ON
23. Verifikasi sakelar Rudi Hartono Disabled
24. Klik segmen Breadcrumb `User`
25. Klik halaman 1 pada pagination
26. Klik nama `Hana Kusuma`
27. Verifikasi Hana Kusuma menampilkan badge `Pending Activation` di sebelah nama
28. Klik segmen Breadcrumb `User`
29. Klik nama `Indra Wijaya`
30. Verifikasi Indra Wijaya menampilkan badge `Pending Email Confirmation` di sebelah nama
31. Verifikasi badge `Pending Activation` dan `Pending Email Confirmation` saling eksklusif (Hana Kusuma tanpa `Pending Email Confirmation`, Indra Wijaya tanpa `Pending Activation`)

### TC-FA-SU-22: General Information: email pending, Temporary Until, TAG, dan Home Group

32. Verifikasi Indra Wijaya menampilkan teks `Pending email change to [New Email]` di samping Email
33. Verifikasi teks email pending Indra Wijaya tanpa tombol aksi
34. Klik segmen Breadcrumb `User`
35. Klik nama `Fajar Nugroho`
36. Verifikasi Fajar Nugroho (Temporary User) menampilkan `Temporary until [Date]` (31/12/26) mengikuti format General Settings
37. Verifikasi TAG Fajar Nugroho `—` karena belum paired
38. Klik segmen Breadcrumb `User`
39. Klik halaman 3 pada pagination
40. Klik nama pengguna dinamis `Zzz Tanpa Home Group {runId}-007`
41. Verifikasi Home Group pengguna dinamis `—`
42. Klik segmen Breadcrumb `User`
43. Klik halaman 1 pada pagination
44. Klik nama `Budi Santoso`
45. Verifikasi TAG Budi Santoso `TAG-0001`
46. Verifikasi Home Group Budi Santoso menampilkan badge (hover hierarki)
47. Verifikasi Budi Santoso (non-Temporary) tidak menampilkan field Temporary Until
48. Verifikasi General Information Budi Santoso tanpa sel kosong
49. Principal Automation mengubah plan Client menjadi Starter lewat sesi API hingga tersimpan
50. Muat ulang halaman Detail Budi Santoso
51. Verifikasi field TAG tidak tersedia pada plan Starter (Email dan Position tetap tampil)
52. Principal Automation mengembalikan plan Client ke Enterprise lewat sesi API hingga tersimpan

### TC-FA-SU-29: Custom Field accordion pada Detail User

53. Verifikasi accordion `Custom Field` collapsed secara default dengan ikon ▶
54. Klik header accordion `Custom Field`
55. Verifikasi accordion terbuka dengan ikon ▼
56. Verifikasi isi accordion berupa daftar label dan nilai read-only
57. Verifikasi tidak ada edit inline pada accordion
58. Klik header accordion `Custom Field` sekali lagi
59. Verifikasi accordion `Custom Field` collapsed dengan ikon ▶
60. Nonaktifkan Custom Field `Shift` lewat seed API hingga tersimpan
61. Muat ulang halaman Detail Budi Santoso
62. Verifikasi section `Custom Field` Hidden seluruhnya (General Information tampil sebagai anchor permukaan)
63. Aktifkan kembali Custom Field `Shift` lewat seed API hingga tersimpan
64. Klik segmen Breadcrumb `User`
65. Klik nama `Hana Kusuma`
66. Klik header accordion `Custom Field`
67. Verifikasi field aktif `Shift` tanpa nilai pada Hana Kusuma menampilkan `—`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 20, 21, 22, 29; kunjungan Detail diurut supaya Budi Santoso (langkah 1 dan 12 sampai 13), Indra Wijaya (langkah 29 sampai 33), dan Budi Santoso (langkah 44 sampai 59) tidak dibuka berulang tanpa asersi baru. Langkah Uji "buka Detail ... bergantian" TC-FA-SU-21 dipenuhi dengan kunjungan berurutan pada langkah 12 sampai 31.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13, 18, 24, 28, 34, 38, 42, dan 64 (kembali ke User List lewat Breadcrumb), langkah 19, 25, 39, dan 43 (pindah halaman pagination supaya baris target tampil, S-14), langkah 50 dan 61 (muat ulang), langkah 58 (klik header accordion `Custom Field` kedua untuk menutup; `Verifikasi` collapsed ada di langkah 59), langkah 49, 52, 60, dan 63 (pemicu state lewat sesi API atau seed; bukan objek asersi UI kedua). Klik nama pada langkah 15, 20, 26, 29, 35, 40, 44, dan 65 membuka Detail. Langkah 14 adalah `Verifikasi` User List sesudah klik segmen Breadcrumb `User` pada langkah 13 (TC-FA-SU-20 Expected a).
- Langkah 51 memakai Email dan Position sebagai pembanding agar asersi absence TAG tidak lolos pada halaman yang belum termuat (bagian 8b butir 2, S-03). Langkah 62 memakai General Information sebagai anchor.
- Spec melewati sekitar 35 langkah (67 langkah). Seluruhnya satu kelas (screening Detail User, satu akun, tanpa mengubah data bisnis; state plan dan Custom Field dipulihkan), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain.
- Pembagian TC lintas spec: User Type Detail User (TC-FA-SU-23 sampai 28) ada di spec 008 dan 009.
- Temuan untuk QA:
  - TC-FA-SU-22 Expected a menyebut `Pending email change to [New Email]` tanpa menyebut alamat email baru Indra Wijaya; spec mengasersi awalan teks dan alamat email baru dari fixture.
  - TC-FA-SU-22 Langkah Uji 1 menyebut "pengguna tanpa Home Group" tetapi Pre-setup #43 memberi Home Group untuk semua 25 pengguna; spec memakai pengguna dinamis tanpa Home Group.
  - TC-FA-SU-22 Expected c ("pada plan Starter field TAG tidak tersedia") tidak punya Langkah Uji dan Pre-setup #20 berplan Enterprise; spec memicu plan Starter lewat Principal Automation (langkah 48), dan Client `FaUserStarter` (#32) tidak dipakai.
  - TC-FA-SU-29 Langkah Uji 3 ("Ulangi pada client tanpa Custom Field aktif") menyebut client lain; spec menonaktifkan Custom Field `Shift` pada Client yang sama lewat seed (varian kedua nonaktif Pre-setup #31) agar tidak berganti tenant.
  - TC-FA-SU-29 Expected b ("field aktif tanpa nilai menampilkan `—`") tidak punya pengguna acuan; spec memakai Hana Kusuma (Shift `—` pada Pre-setup #43).
  - TC-FA-SU-20 Expected e menulis `(N)` pada tab bar tanpa angka; spec mengasersi label tab dengan N dari fixture.
