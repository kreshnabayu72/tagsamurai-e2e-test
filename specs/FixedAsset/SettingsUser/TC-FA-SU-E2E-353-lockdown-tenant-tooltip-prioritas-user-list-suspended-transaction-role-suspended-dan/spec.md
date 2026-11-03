---
id: TC-FA-SU-E2E-353-lockdown-tenant-tooltip-prioritas-user-list-suspended-transaction-role-suspended-dan
title: "Tenant Suspended: User List dan Detail Read-only, Unsuspend, dan Tanpa Entri Log Perubahan Status"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-77
  - TC-FA-SU-80
  - TC-FA-SU-959
coverage:
  web: automated
---

# Tenant Suspended: User List dan Detail Read-only, Unsuspend, dan Tanpa Entri Log Perubahan Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, 25 pengguna), penugasan peran (#23), Changelog Budi Santoso (#27, 7 baris, dipakai sebagai baris pembanding), dan Global Settings (#38). Pengguna yang dipakai: Budi Santoso (Group Role `Manage group` pada Finance & Accounting), Ahmad Dahlan (Default User), Lina Marlina (akun sendiri), Hana Kusuma (Pending Activation), dan Doni Prasetyo (Inactive, target Activate). Client `FaUserSuspended` (#34) berpopulasi sama dengan #20; Suspended pada spec ini dicapai lewat Principal Automation pada Client `FaUserMain` (lihat Temuan untuk QA). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (berkas fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): Principal Automation (Pre-setup #12) mengubah status Client lewat sesi API; seed API memulihkan status aktif pengguna Pre-setup; pembacaan jumlah entri Tab Changelog pengguna sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline (S-12), bukan angka absolut.
- State global: status Client `FaUserMain` (Suspended pada langkah 2, aktif kembali pada langkah 32) dan status aktif Doni Prasetyo (Active pada langkah 37, dipulihkan ke Inactive pada langkah 42). Pemulihan keduanya juga di hook `after` (status Client aktif dan Doni Prasetyo Inactive). Efek pada Pre-setup: Last Updated dan Modified By Doni Prasetyo berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-77: Client Suspended, User List dan Detail read-only

1. Catat jumlah entri Tab Changelog Budi Santoso sebagai baseline
2. Principal Automation mengubah status Client `FaUserMain` menjadi Suspended lewat sesi API hingga tersimpan
3. Muat ulang halaman Fixed Asset > Settings > User
4. Verifikasi halaman User List dapat dibuka dan seluruh data pengguna terlihat
5. Verifikasi tidak ada banner di halaman Settings > User
6. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter, lalu hover sakelar Active baris Budi Santoso
7. Verifikasi sakelar Active baris Budi Santoso Disabled dengan tooltip `Entity is suspended.`
8. Ganti isi kotak search dengan `Ahmad Dahlan`, tekan Enter, lalu hover sakelar Active baris Ahmad Dahlan (Default User)
9. Verifikasi sakelar Active baris Ahmad Dahlan Disabled dengan tooltip `Entity is suspended.`
10. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter, lalu hover sakelar Active baris Lina Marlina (akun sendiri)
11. Verifikasi sakelar Active baris Lina Marlina Disabled dengan tooltip `Entity is suspended.`
12. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter, lalu hover checkbox baris Budi Santoso
13. Verifikasi checkbox baris Budi Santoso Disabled dengan tooltip `Entity is suspended.`
14. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu klik ⋯ pada baris Hana Kusuma
15. Verifikasi menu ⋯ baris Hana Kusuma terbuka
16. Verifikasi menu ⋯ tidak memuat `Edit Home Group` dan `Resend Activation Email`
17. Tutup menu ⋯
18. Verifikasi Bulk Actions Bar tidak dirender
19. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter, lalu klik nama Budi Santoso
20. Hover sakelar Active di header Detail
21. Verifikasi sakelar Active di header Detail Disabled dengan tooltip `Entity is suspended.`
22. Klik tab Role
23. Hover switch Global Role `Manage accounting`
24. Verifikasi switch Global Role `Manage accounting` Disabled dengan tooltip `Entity is suspended.`
25. Hover checkbox `Create` Global Role `Manage accounting`
26. Verifikasi checkbox `Create` Global Role `Manage accounting` Disabled dengan tooltip `Entity is suspended.`
27. Klik sub-tab Group Role
28. Verifikasi baris Group Role Budi Santoso tampil pada Sub-tab Group Role
29. Verifikasi row action `[Assign Group]` pada baris Group Role Budi Santoso tidak dirender
30. Klik Tab Changelog
31. Verifikasi Tab Changelog dapat dibaca dan memuat baris riwayat Budi Santoso

### TC-FA-SU-80 dan TC-FA-SU-959 (butir b): Client di-unsuspend

32. Principal Automation mengubah status Client `FaUserMain` menjadi aktif kembali lewat sesi API hingga tersimpan
33. Klik Breadcrumb `Settings` untuk kembali ke User List
34. Muat ulang halaman Fixed Asset > Settings > User
35. Verifikasi sakelar Active dan checkbox baris kembali interaktif (Enabled)
36. Ganti isi kotak search dengan `Doni Prasetyo`, tekan Enter, lalu klik sakelar Active baris Doni Prasetyo
37. Klik `[Confirm]` pada dialog konfirmasi
38. Verifikasi tidak ada dialog atau tombol reaktivasi tambahan pada baris Doni Prasetyo
39. Verifikasi sakelar Active baris Doni Prasetyo berstatus Active
40. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
41. Verifikasi kolom Role baris Budi Santoso sama dengan penugasan Pre-setup #23
42. Pulihkan Doni Prasetyo ke Inactive lewat seed API

### TC-FA-SU-959 (butir a): Tanpa entri log saat status Client berubah

43. Klik nama Budi Santoso
44. Klik Tab Changelog
45. Verifikasi Tab Changelog memuat baris riwayat Budi Santoso
46. Baca jumlah entri Tab Changelog Budi Santoso
47. Verifikasi jumlah entri Tab Changelog Budi Santoso sama dengan baseline langkah 1

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-SU-75 dan TC-FA-SU-81 ada di spec 354; TC-FA-SU-78 dan TC-FA-SU-79 ada di spec 358; TC-FA-SU-152 dan TC-FA-SU-283 ada di spec 359.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline), 3 (muat ulang), 17 (tutup menu), 33 dan 34 (kembali ke User List dan muat ulang), 40 (Ganti isi kotak search), 42 (pemulihan seed API), 43, 44, dan 46 (navigasi dan pembacaan jumlah). Langkah 6, 8, 10, 12, 14, 18, dan 36 menggabungkan Search baris target dengan aksi berikutnya karena baris di luar halaman 1 (R-16). Langkah 16 dan 28 adalah anchor positif untuk asersi absence berikutnya (8b.2). Langkah 2 dan 32 adalah pemicu state lewat sesi API (R-20), bukan objek asersi UI kedua.
- Urutan TC sumber diubah: TC-FA-SU-80 sesudah TC-FA-SU-77 karena unsuspend memakai Client yang sudah Suspended dari langkah 2. Butir b TC-FA-SU-959 (akses tulis kembali tanpa reaktivasi manual) diasersi pada langkah 39 karena aktivasi Doni Prasetyo (langkah 36 sampai 37) dikerjakan di blok TC-FA-SU-80; butir a TC-FA-SU-959 menyusul.
- TC-FA-SU-959 butir a ("tidak ada entri log") ditulis sebagai asersi jumlah dengan baseline (S-12) pada aksi nyata spec ini (perubahan status Client lewat Principal pada langkah 2 dan 32), bukan asersi absence kelas g.
- Verifikasi baris Doni Prasetyo (langkah 39) dikerjakan sebelum Verifikasi kolom Role baris Budi Santoso (langkah 41) supaya satu Search per baris target cukup (R-16); langkah 40 mengganti isi kotak search.
- Alasan spec melewati sekitar 35 langkah: seluruh blok berkelas h (state tenant) dan berbagi satu siklus Suspended lalu aktif kembali pada Client bersama; blok unsuspend dan blok tanpa entri log hanya bermakna sesudah Client benar-benar Suspended pada langkah 2.
- Temuan untuk QA (S-15): (1) TC-FA-SU-77 menyebut Pre-setup #34 (Client `FaUserSuspended`) sekaligus langkah "Principal mengubah status client menjadi Suspended" untuk akun Total Control #1 yang berada di `FaUserMain`; spec mengikuti langkah TC pada `FaUserMain`. (2) TC-FA-SU-77 dan TC-FA-SU-80 tidak menyebut pengguna untuk Detail dan untuk "Activate satu pengguna"; spec memakai Budi Santoso (Detail) dan Doni Prasetyo (Inactive, target Activate). (3) TC-FA-SU-77 butir c menyebut `[Assign Group]` tanpa lokasi; spec memeriksanya pada baris Group Role di Detail Budi Santoso. (4) TC-FA-SU-77 butir d tidak merinci Global Role yang dicek; spec memakai `Manage accounting`. (5) TC-FA-SU-80 butir b "penugasan peran tetap utuh" tidak punya data pembanding; spec membandingkan dengan Pre-setup #23. (6) TC-FA-SU-77 butir b meminta "semua baris"; spec mengasersi tiga baris wakil (pengguna biasa, Default User, akun sendiri). (7) Teks toast Activate tidak disebut di TC-FA-SU-80 sehingga tidak diasersi.
