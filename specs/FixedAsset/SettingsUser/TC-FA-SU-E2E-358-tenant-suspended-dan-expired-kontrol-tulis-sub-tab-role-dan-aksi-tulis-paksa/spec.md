---
id: TC-FA-SU-E2E-358-tenant-suspended-dan-expired-kontrol-tulis-sub-tab-role-dan-aksi-tulis-paksa
title: "Tenant Suspended dan Expired: Kontrol Tulis Sub-tab Role dan Aksi Tulis Paksa"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-78
  - TC-FA-SU-79
coverage:
  web: automated
---

# Tenant Suspended dan Expired: Kontrol Tulis Sub-tab Role dan Aksi Tulis Paksa

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, 25 pengguna), Client `FaUserExpired` (#35, berpopulasi sama dengan #20), penugasan peran (#23), dan Transaction Role (#39). Pengguna yang dipakai: Budi Santoso (Global Role dan Group Role; target permintaan tulis paksa), Mira Anggraini (Transaction Role `Disposal` x `Staff` dan `Borrowing & Assignment` x `Approver` pada Finance & Accounting), dan Hana Kusuma (Pending Activation). Suspended dan Expired pada spec ini dicapai lewat Principal Automation pada Client `FaUserMain` (lihat Temuan untuk QA). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (berkas fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): Principal Automation (Pre-setup #12) mengubah status Client lewat sesi API; klien HTTP dengan token sesi Lina Marlina untuk permintaan tulis langsung (endpoint permintaan tidak tertulis di TC dan disediakan tim FE/BE, tanpa endpoint karangan di spec ini).
- State global: status Client `FaUserMain` (Suspended pada langkah 1, Expired pada langkah 27, aktif kembali pada langkah 46). Pemulihan status aktif juga di hook `after`. Permintaan tulis paksa pada langkah 44 diharapkan ditolak sehingga data Budi Santoso tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-78: Client Suspended, kontrol tulis Sub-tab Role

1. Principal Automation mengubah status Client `FaUserMain` menjadi Suspended lewat sesi API hingga tersimpan
2. Muat ulang halaman Fixed Asset > Settings > User
3. Ketik Search `Budi Santoso`, tekan Enter, lalu klik nama Budi Santoso
4. Klik tab Role
5. Klik sub-tab Global Role
6. Hover switch Global Role `Manage accounting`
7. Verifikasi switch Global Role `Manage accounting` Disabled dengan tooltip `Entity is suspended.`
8. Hover checkbox `Create` Global Role `Manage accounting`
9. Verifikasi checkbox `Create` Global Role `Manage accounting` Disabled dengan tooltip `Entity is suspended.`
10. Klik sub-tab Group Role
11. Verifikasi baris Group Role Budi Santoso tampil pada Sub-tab Group Role
12. Verifikasi row action `[Assign Group]` pada baris Group Role Budi Santoso tidak dirender
13. Klik Breadcrumb `Settings` untuk kembali ke User List
14. Ganti isi kotak search dengan `Mira Anggraini`, tekan Enter, lalu klik nama Mira Anggraini
15. Klik tab Role
16. Klik sub-tab Transaction Role
17. Hover `[+ Assign]`
18. Verifikasi `[+ Assign]` Disabled dengan tooltip `Entity is suspended.`
19. Klik ⋯ pada baris Transaction Role `Disposal` x `Staff`
20. Hover row action `Remove`
21. Verifikasi row action `Remove` Disabled dengan tooltip `Entity is suspended.`
22. Tutup menu ⋯
23. Hover checkbox baris Transaction Role `Disposal` x `Staff`
24. Verifikasi checkbox baris Disabled dengan tooltip `Entity is suspended.`
25. Verifikasi Bulk Actions Bar tidak muncul
26. Verifikasi row action `[Assign Group]` pada Sub-tab Transaction Role tidak dirender

### TC-FA-SU-79: Client Expired diperlakukan identik dengan Suspended

27. Principal Automation mengubah status Client `FaUserMain` menjadi Expired lewat sesi API hingga tersimpan
28. Klik Breadcrumb `Settings` untuk kembali ke User List
29. Muat ulang halaman Fixed Asset > Settings > User
30. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter, lalu hover sakelar Active baris Budi Santoso
31. Verifikasi sakelar Active baris Budi Santoso Disabled dengan tooltip `Entity is suspended.`
32. Hover checkbox baris Budi Santoso
33. Verifikasi checkbox baris Budi Santoso Disabled dengan tooltip `Entity is suspended.`
34. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter, lalu klik ⋯ pada baris Hana Kusuma
35. Verifikasi menu ⋯ baris Hana Kusuma terbuka
36. Verifikasi menu ⋯ tidak memuat `Resend Activation Email` dan `Edit Home Group`
37. Tutup menu ⋯
38. Verifikasi Bulk Actions Bar tidak dirender
39. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter, lalu klik nama Budi Santoso
40. Klik tab Role
41. Klik sub-tab Group Role
42. Verifikasi baris Group Role Budi Santoso tampil pada Sub-tab Group Role
43. Verifikasi row action `[Assign Group]` tidak dirender
44. Kirim permintaan tulis Deactivate untuk Budi Santoso lewat klien HTTP dengan token sesi Lina Marlina
45. Verifikasi server menolak permintaan tulis tersebut
46. Principal Automation mengubah status Client `FaUserMain` menjadi aktif kembali lewat sesi API hingga tersimpan

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-SU-77, TC-FA-SU-80, dan TC-FA-SU-959 ada di spec 353; TC-FA-SU-75 dan TC-FA-SU-81 ada di spec 354; TC-FA-SU-152 dan TC-FA-SU-283 ada di spec 359.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 dan 29 (muat ulang), 13 dan 28 (kembali ke User List), 22 dan 37 (tutup menu), 44 (pemicu permintaan langsung; objek asersi adalah respons pada langkah 45). Langkah 3, 14, 30, 34, dan 39 menggabungkan Search baris target dengan aksi berikutnya karena baris di luar halaman 1 (R-16). Langkah 11, 35, dan 42 adalah anchor positif untuk asersi absence berikutnya (8b.2). Langkah 1, 27, dan 46 adalah pemicu state lewat sesi API (R-20).
- Langkah 44 sampai 45 mengikuti bagian 8b butir 1: hanya respons server yang diasersi; toast penolakan "Changes can't be saved while this workspace is suspended or expired." tidak diasersi di spec ini karena request langsung tidak melewati UI (perilaku FE untuk respons yang sama diasersi di spec 354, langkah 7).
- Alasan spec melewati sekitar 35 langkah: kedua TC berkelas h dan berbagi satu siklus status Client yang sama; TC-FA-SU-79 (Expired) berlanjut dari Client yang sudah tidak aktif pada langkah 1 tanpa membangun ulang state di spec lain.
- Temuan untuk QA (S-15): (1) TC-FA-SU-78 menyebut Detail Budi Santoso untuk ketiga sub-tab, tetapi Pre-setup #39 tidak menugaskan Transaction Role kepada Budi Santoso dan tidak ada satu pengguna Pre-setup dengan baris Group Role sekaligus Transaction Role; spec memakai Budi Santoso (Global Role dan Group Role) dan Mira Anggraini (Transaction Role). (2) Butir Global Role TC-FA-SU-78 tidak merinci peran yang dicek; spec memakai `Manage accounting`. (3) Butir b TC-FA-SU-79 mengharapkan toast pada aksi tulis paksa "dari konsol penguji"; TC tidak menyebut endpoint maupun payload dan perilaku FE tidak dapat diasersi pada request langsung (8b butir 1), sehingga hanya penolakan server yang diasersi tanpa kode status. (4) Pre-setup #35 (Client `FaUserExpired`) dan langkah "Principal mengubah status client menjadi Expired" pada TC-FA-SU-79 tidak konsisten; spec mengikuti langkah TC pada `FaUserMain`.
