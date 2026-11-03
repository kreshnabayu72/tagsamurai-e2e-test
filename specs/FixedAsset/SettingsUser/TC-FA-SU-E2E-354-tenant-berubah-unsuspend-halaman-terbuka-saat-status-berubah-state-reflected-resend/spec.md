---
id: TC-FA-SU-E2E-354-tenant-berubah-unsuspend-halaman-terbuka-saat-status-berubah-state-reflected-resend
title: "Tenant Berubah: Halaman Terbuka Saat Status Client Berubah dan Prioritas Tooltip Disabled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-81
  - TC-FA-SU-75
coverage:
  web: automated
---

# Tenant Berubah: Halaman Terbuka Saat Status Client Berubah dan Prioritas Tooltip Disabled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Akun kedua: Read Only Citra Lestari (Pre-setup #3, `readOnly_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_RO_PASSWORD`, dipakai pada langkah 37 sampai 45; spec berakhir pada akun ini dan hook `after` memulihkan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, 25 pengguna), pohon grup (#21), penugasan peran (#23), dan Global Settings (#38: Rudi Hartono nonaktif di Global Settings dengan sakelar FAMS ON). Pengguna yang dipakai: Budi Santoso (target Deactivate yang ditolak server), Ahmad Dahlan (Default User), Lina Marlina (akun sendiri), Rudi Hartono (nonaktif Global Settings), Nanda Pratama (Global Role `Manage global user & role` OFF, #23), dan Hana Kusuma (Pending Activation). Client `FaUserSuspended` (#34) berpopulasi sama dengan #20; Suspended pada spec ini dicapai lewat Principal Automation pada Client `FaUserMain` (lihat Temuan untuk QA). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (berkas fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): Principal Automation (Pre-setup #12) mengubah status Client lewat sesi API; jeda 5 detik tanpa memuat ulang halaman pada langkah 3 adalah pilihan spec (bukan nilai TC atau PRD) sebagai jendela propagasi.
- State global: status Client `FaUserMain` (Suspended pada langkah 2, aktif kembali pada langkah 22, Suspended lagi pada langkah 41, aktif kembali pada langkah 45). Pemulihan juga di hook `after`. Aksi Deactivate Budi Santoso pada langkah 5 sampai 6 ditolak server sehingga status Budi Santoso tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-81: Halaman terbuka saat Client berubah menjadi Suspended

1. Ketik Search `Budi Santoso`, tekan Enter
2. Principal Automation mengubah status Client `FaUserMain` menjadi Suspended lewat sesi API hingga tersimpan, tanpa memuat ulang halaman User List yang sudah terbuka
3. Tunggu 5 detik tanpa memuat ulang halaman
4. Verifikasi sakelar Active baris Budi Santoso masih Enabled (tampilan halaman tidak berubah otomatis)
5. Klik sakelar Active baris Budi Santoso
6. Klik `[Confirm]` pada dialog konfirmasi
7. Verifikasi toast "Changes can't be saved while this workspace is suspended or expired."
8. Verifikasi halaman tetap berada di Settings > User tanpa redirect
9. Hover sakelar Active baris Budi Santoso
10. Verifikasi sakelar Active baris Budi Santoso Disabled dengan tooltip "Entity is suspended."
11. Hover checkbox baris Budi Santoso
12. Verifikasi checkbox baris Budi Santoso Disabled dengan tooltip "Entity is suspended."
13. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu klik ⋯ pada baris Hana Kusuma
14. Verifikasi menu ⋯ baris Hana Kusuma terbuka
15. Verifikasi menu ⋯ tidak memuat `Resend Activation Email`
16. Tutup menu ⋯
17. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter, lalu klik nama Budi Santoso
18. Klik tab Role
19. Klik sub-tab Group Role
20. Verifikasi baris Group Role Budi Santoso tampil pada Sub-tab Group Role
21. Verifikasi row action `[Assign Group]` tidak dirender

### TC-FA-SU-75: Prioritas tooltip Disabled bila beberapa kondisi berlaku sekaligus

22. Principal Automation mengubah status Client `FaUserMain` menjadi aktif kembali lewat sesi API hingga tersimpan
23. Klik Breadcrumb `Settings` untuk kembali ke User List
24. Muat ulang halaman Fixed Asset > Settings > User
25. Ganti isi kotak search dengan `Ahmad Dahlan`, tekan Enter, lalu hover sakelar Active baris Ahmad Dahlan (Default User)
26. Verifikasi sakelar Active baris Ahmad Dahlan Disabled dengan tooltip `Default User cannot be modified.`
27. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter, lalu hover sakelar Active baris Lina Marlina (akun sendiri)
28. Verifikasi sakelar Active baris Lina Marlina Disabled dengan tooltip `You can't manage your own account from here.`
29. Ganti isi kotak search dengan `Rudi Hartono`, tekan Enter, lalu hover sakelar Active baris Rudi Hartono
30. Verifikasi sakelar Active baris Rudi Hartono Disabled dengan tooltip `This user is inactive in Global Settings. Contact a Global Settings admin to reactivate.`
31. Ganti isi kotak search dengan `Nanda Pratama`, tekan Enter, lalu klik nama Nanda Pratama
32. Klik tab Role
33. Hover checkbox `Create` Global Role `Manage global user & role`
34. Verifikasi checkbox `Create` Global Role `Manage global user & role` Disabled dengan tooltip `Turn on this role first.`
35. Klik Breadcrumb `Settings` untuk kembali ke User List
36. Logout sebagai Lina Marlina
37. Login sebagai Citra Lestari (Read Only) dengan `Spectra.env.FA_RO_PASSWORD`
38. Buka halaman Fixed Asset > Settings > User
39. Ketik Search `Ahmad Dahlan`, tekan Enter, lalu hover sakelar Active baris Ahmad Dahlan (Default User)
40. Verifikasi sakelar Active baris Ahmad Dahlan Disabled dengan tooltip `You don't have permission to edit.`
41. Principal Automation mengubah status Client `FaUserMain` menjadi Suspended lewat sesi API hingga tersimpan
42. Muat ulang halaman Fixed Asset > Settings > User
43. Ganti isi kotak search dengan `Ahmad Dahlan`, tekan Enter, lalu hover sakelar Active baris Ahmad Dahlan (Default User)
44. Verifikasi sakelar Active baris Ahmad Dahlan Disabled dengan tooltip `Entity is suspended.`
45. Principal Automation mengubah status Client `FaUserMain` menjadi aktif kembali lewat sesi API hingga tersimpan

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-SU-77, TC-FA-SU-80, dan TC-FA-SU-959 ada di spec 353; TC-FA-SU-78 dan TC-FA-SU-79 ada di spec 358; TC-FA-SU-152 dan TC-FA-SU-283 ada di spec 359.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search Budi Santoso sebelum status berubah supaya halaman terbuka tetap basi), 3 (jeda propagasi), 16 (tutup menu), 23 dan 24 (kembali ke User List dan muat ulang), 35 (kembali ke User List), 36 sampai 38 (ganti akun dengan langkah eksplisit), 42 (muat ulang), dan 45 (pemulihan). Langkah 13, 17, 25, 27, 29, 31, 39, dan 43 menggabungkan Search baris target dengan aksi berikutnya karena baris di luar halaman 1 (R-16). Langkah 14 dan 20 adalah anchor positif untuk asersi absence berikutnya (8b.2). Langkah 2, 22, 41, dan 45 adalah pemicu state lewat sesi API (R-20, bukan objek asersi UI kedua).
- Urutan butir TC-FA-SU-75 mengikuti state, bukan urutan butir TC (8b butir 5): butir c, d, e, f pada Client aktif sebagai Total Control, butir b sebagai Read Only pada Client aktif, lalu butir a sebagai Read Only pada Client Suspended. Satu `Verifikasi` butir c memakai baris Ahmad Dahlan yang sekaligus Total Control; tooltip menimpa tier dan scope.
- Alasan spec melewati sekitar 35 langkah: kedua TC berkelas h dan berbagi siklus status Client yang sama (aktif, Suspended, aktif, Suspended); TC-FA-SU-75 butir a membutuhkan Client Suspended dengan akun Read Only sehingga urutan state tidak dapat disisipkan di spec lain tanpa membangun ulang siklus itu.
- Temuan untuk QA (S-15): (1) Pre-setup #34 dan langkah "Principal mengubah status" pada TC-FA-SU-75 dan TC-FA-SU-81 tidak konsisten (lihat Prerequisites); spec mengikuti langkah TC pada `FaUserMain`. (2) TC-FA-SU-75 meminta kombinasi yang tidak dapat disusun dengan Pre-setup #1, #3, #20, #23, #34, #38: "diri sendiri + nonaktif Global" (aktor nonaktif Global tidak dapat login), "nonaktif Global + Total Control" (Rudi Hartono bukan Total Control), dan "Total Control + switch OFF" (Nanda Pratama bukan Total Control); spec mengasersi tooltip per kondisi utama pada baris yang tersedia. (3) TC-FA-SU-75 butir b menyebut "Manage user & role tanpa Update" tetapi Pre-setup TC hanya menyediakan Read Only (#3); spec hanya memakai Read Only. (4) TC-FA-SU-75 butir c mengharuskan menimpa kondisi "scope" tanpa aktor ber-scope di Pre-setup TC; tidak diasersi terpisah. (5) TC-FA-SU-81 butir c menyebut `[Assign Group]` tanpa lokasi; spec memeriksanya pada baris Group Role di Detail Budi Santoso. (6) TC-FA-SU-81 butir b ("disusul refresh UI") diasersi sebagai halaman tetap di Settings > User tanpa redirect, sedangkan keadaan Disabled sesudah refresh diasersi pada langkah 8 sampai 11 tanpa muat ulang manual.
