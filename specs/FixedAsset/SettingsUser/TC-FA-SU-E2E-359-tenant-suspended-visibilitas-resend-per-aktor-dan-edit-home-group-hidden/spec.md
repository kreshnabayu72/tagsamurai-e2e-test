---
id: TC-FA-SU-E2E-359-tenant-suspended-visibilitas-resend-per-aktor-dan-edit-home-group-hidden
title: "Tenant Suspended: Visibilitas Resend per Aktor dan Edit Home Group Hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-152
  - TC-FA-SU-283
coverage:
  web: automated
---

# Tenant Suspended: Visibilitas Resend per Aktor dan Edit Home Group Hidden

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Role yang diuji (ganti akun dengan langkah eksplisit):

| Role | Akun | Email | Password | Langkah |
|---|---|---|---|---|
| Total Control (Client aktif) | Lina Marlina (#1) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | 1 sampai 14 |
| Read Only | Citra Lestari (#3) | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | 16 sampai 25 |
| Manage global user & role (Update) | Qori Akbar (#4) | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURG_UPD_PASSWORD` | 27 sampai 34 |
| Total Control (Client Suspended) | Lina Marlina (#1) | sama seperti di atas | `Spectra.env.FA_TC_PASSWORD` | 37 sampai 47 |

- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API. Spec berakhir pada akun Lina Marlina (akun default suite).
- Data Pre-setup: Client `FaUserMain` (#20, 25 pengguna), Client `FaUserSuspended` (#34, berpopulasi sama dengan #20), penugasan peran (#23), dan layanan (#37: Hana Kusuma Pending Activation). Pengguna yang dipakai: Ahmad Dahlan (Default User), Lina Marlina (akun sendiri), dan Hana Kusuma (Pending Activation, target Resend dan Edit Home Group). Suspended pada spec ini dicapai lewat Principal Automation pada Client `FaUserMain` (lihat Temuan untuk QA). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (berkas fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): Principal Automation (Pre-setup #12) mengubah status Client lewat sesi API; cooldown Resend untuk Hana Kusuma tidak berjalan pada awal spec (60 detik sejak pengiriman terakhir telah lewat; precondition TC-FA-SU-152), dipenuhi dengan mengatur jam server dan jam browser bersama atau seed API tanpa pengiriman Resend sebelumnya.
- State global: status Client `FaUserMain` (Suspended pada langkah 35, aktif kembali pada langkah 48). Pemulihan status aktif juga di hook `after`. Spec tidak mengubah data pengguna Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-283: Edit Home Group Hidden pada Default User dan akun sendiri (Client aktif)

1. Ketik Search `Ahmad Dahlan`, tekan Enter, lalu klik ⋯ pada baris Ahmad Dahlan (Default User)
2. Verifikasi menu ⋯ baris Ahmad Dahlan terbuka
3. Verifikasi menu ⋯ baris Ahmad Dahlan tidak memuat `Edit Home Group`
4. Tutup menu ⋯
5. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter, lalu klik ⋯ pada baris Lina Marlina (akun sendiri)
6. Verifikasi menu ⋯ baris Lina Marlina terbuka
7. Verifikasi menu ⋯ baris Lina Marlina tidak memuat `Edit Home Group`
8. Tutup menu ⋯
9. Ganti isi kotak search dengan `Ahmad Dahlan`, tekan Enter, lalu klik nama Ahmad Dahlan
10. Verifikasi field Home Group di Detail Ahmad Dahlan tampil sebagai badge tanpa ikon edit
11. Klik Breadcrumb `Settings` untuk kembali ke User List
12. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter, lalu klik nama Lina Marlina
13. Verifikasi field Home Group di Detail Lina Marlina tampil sebagai badge tanpa ikon edit
14. Klik Breadcrumb `Settings` untuk kembali ke User List

### TC-FA-SU-152: Visibilitas Resend per aktor

15. Logout sebagai Lina Marlina
16. Login sebagai Citra Lestari (Read Only) dengan `Spectra.env.FA_RO_PASSWORD`
17. Buka halaman Fixed Asset > Settings > User
18. Ketik Search `Hana Kusuma`, tekan Enter, lalu klik ⋯ pada baris Hana Kusuma
19. Verifikasi menu ⋯ baris Hana Kusuma terbuka
20. Verifikasi menu ⋯ baris Hana Kusuma tidak memuat `Resend Activation Email` dan `Resend Confirmation Email`
21. Tutup menu ⋯
22. Klik nama Hana Kusuma
23. Verifikasi header Detail Hana Kusuma tampil
24. Verifikasi header Detail Hana Kusuma tidak memuat `Resend Activation Email` dan `Resend Confirmation Email`
25. Klik Breadcrumb `Settings` untuk kembali ke User List
26. Logout sebagai Citra Lestari
27. Login sebagai Qori Akbar (Manage global user & role Update) dengan `Spectra.env.FA_MURG_UPD_PASSWORD`
28. Buka halaman Fixed Asset > Settings > User
29. Ketik Search `Hana Kusuma`, tekan Enter, lalu klik ⋯ pada baris Hana Kusuma
30. Verifikasi menu ⋯ baris Hana Kusuma memuat `Resend Activation Email` Enabled
31. Tutup menu ⋯
32. Klik nama Hana Kusuma
33. Verifikasi header Detail Hana Kusuma memuat `Resend Activation Email` Enabled
34. Klik Breadcrumb `Settings` untuk kembali ke User List
35. Principal Automation mengubah status Client `FaUserMain` menjadi Suspended lewat sesi API hingga tersimpan
36. Logout sebagai Qori Akbar
37. Login sebagai Lina Marlina (Total Control) dengan `Spectra.env.FA_TC_PASSWORD`
38. Buka halaman Fixed Asset > Settings > User
39. Ketik Search `Hana Kusuma`, tekan Enter, lalu klik ⋯ pada baris Hana Kusuma
40. Verifikasi menu ⋯ baris Hana Kusuma terbuka
41. Verifikasi menu ⋯ baris Hana Kusuma tidak memuat `Resend Activation Email` dan `Resend Confirmation Email`
42. Verifikasi menu ⋯ seluruh baris tidak memuat `Edit Home Group` (diwakili baris Hana Kusuma)
43. Tutup menu ⋯
44. Klik nama Hana Kusuma
45. Verifikasi header Detail Hana Kusuma tampil
46. Verifikasi header Detail Hana Kusuma tidak memuat `Resend Activation Email` dan `Resend Confirmation Email`
47. Verifikasi field Home Group di Detail Hana Kusuma tampil sebagai badge tanpa ikon edit
48. Principal Automation mengubah status Client `FaUserMain` menjadi aktif kembali lewat sesi API hingga tersimpan

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-SU-77, TC-FA-SU-80, dan TC-FA-SU-959 ada di spec 353; TC-FA-SU-75 dan TC-FA-SU-81 ada di spec 354; TC-FA-SU-78 dan TC-FA-SU-79 ada di spec 358.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4, 8, 21, 31, dan 43 (tutup menu), 11, 14, 25, dan 34 (kembali ke User List), 15 sampai 17, 26 sampai 28, dan 36 sampai 38 (ganti akun dengan langkah eksplisit; S-07), dan 35 serta 48 (pemicu state lewat sesi API, R-20). Langkah 1, 5, 9, 12, 18, 29, dan 39 menggabungkan Search baris target dengan aksi berikutnya karena baris di luar halaman 1 (R-16). Langkah 2, 6, 19, 23, 40, dan 45 adalah anchor positif untuk asersi absence berikutnya (8b.2).
- Urutan TC sumber diubah: TC-FA-SU-283 butir a dan butir c untuk Default User dan akun sendiri pada Client aktif didahulukan sebagai akun default, lalu TC-FA-SU-152, dan butir b serta butir c (Suspended) TC-FA-SU-283 diasersi bersama butir c TC-FA-SU-152 pada langkah 39 sampai 47 karena keduanya membaca menu dan Detail baris yang sama pada Client Suspended (8b butir 5, urutan mengikuti state).
- Alasan spec melewati sekitar 35 langkah: kedua TC berkelas h dan berbagi satu siklus Client aktif lalu Suspended; ganti akun menuntut langkah eksplisit (tiga langkah per ganti) dan butir TC-FA-SU-152 membutuhkan tiga aktor pada Client aktif dan Suspended yang tidak dapat dibangun ulang tanpa menduplikasi siklus status Client.
- Temuan untuk QA (S-15): (1) TC-FA-SU-152 menyebut Hana Kusuma dengan dua label (`Resend Activation Email` dan `Resend Confirmation Email`), padahal Hana Kusuma Pending Activation hanya relevan untuk `Resend Activation Email`; butir Enabled hanya diasersi untuk label itu, dan `Resend Confirmation Email` tidak diuji Enabled karena tidak ada pengguna kedua yang disebut TC. (2) Butir b TC-FA-SU-152 menyebut aktor Group "dalam scope", tetapi Pre-setup TC pada TC itu (#1, #3, #4, #12, #20, #34) tidak memuat aktor Group; tidak diasersi. (3) Email akun Qori Akbar (#4) tidak tertulis di Pre-setup TC. (4) Butir b TC-FA-SU-283 meminta Hidden "bagi semua aktor"; spec mengasersi dengan Lina Marlina (Total Control) saja. (5) TC-FA-SU-283 langkah 1 menyebut Ahmad Dahlan sebagai Default User; Pre-setup #20 mencatat Ahmad Dahlan sekaligus Total Control, sehingga baris itu dipakai sebagai Default User. (6) TC-FA-SU-283 butir c untuk kondisi Suspended tidak menyebut pengguna; spec memakai Hana Kusuma. (7) Pre-setup #34 dan langkah "Principal mengubah Client menjadi Suspended" tidak konsisten; spec mengikuti langkah TC pada `FaUserMain`.
