---
id: TC-FA-SU-E2E-355-selection-limit-tooltip-disabled-checkbox-limit-1-auto-cap-dan-perubahan-limit-live
title: "Selection Limit: Tooltip Disabled Lain dan Checkbox Limit+1 dengan Auto-cap"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-76
  - TC-FA-SU-123
coverage:
  web: automated
---

# Selection Limit: Tooltip Disabled Lain dan Checkbox Limit+1 dengan Auto-cap

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user & role Group (Update) Sinta Dewi (Pre-setup #6, Group Role `Manage user & role` pada Finance & Accounting, Read dan Update), password `Spectra.env.FA_MURGR_UPD_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Login di hook `before` spec ini pada Client `FaUserSel`; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Akun kedua: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, login pada langkah 32. Hook `after` memulihkan sesi ke Lina Marlina pada Client default suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserSel` (#36, plan Enterprise, Selection Limit 100 yang ditetapkan Principal Automation, 120 pengguna di-seed lewat skrip atau API sehingga 118 baris dapat dipilih karena Default User dan akun sendiri tidak dapat dipilih; N = 118 diturunkan dari seeding), pohon grup (#21), dan Transaction Role (#39). Pengguna yang dipakai: Wawan Setiawan (Group Role `Manage files` pada IT Infrastructure dan Branch Surabaya, di luar scope Sinta Dewi), Gita Permata (Global Role `Manage accounting` ON; Group Role `Manage group` pada Finance & Accounting), dan Yuda Pratama (Transaction Role `Disposal` x `Approver` pada All Groups sudah ada). Client `FaUserMain` (#20) tidak dipakai. Seed 120 pengguna Client `FaUserSel` memuat juga Wawan Setiawan, Gita Permata, dan Yuda Pratama dengan penugasan peran yang sama seperti Pre-setup #23 dan #39 pada Client `FaUserMain` (disediakan tim FE; Pre-setup #36 tidak menyebutnya, lihat Temuan untuk QA). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (berkas fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): seed 120 pengguna pada Client `FaUserSel` dengan Selection Limit 100 (Principal Automation, Pre-setup #12) sebelum spec berjalan; akun Sinta Dewi dan Lina Marlina pada Client `FaUserSel` serta cara memilih Client saat login (TC tidak menyebutnya).
- State global: Selection Limit Client `FaUserSel` tetap 100 (tidak diubah spec ini). Data pengguna Pre-setup tidak diubah; modal Assign pada langkah 23 sampai 29 ditutup tanpa menyimpan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-76: Tooltip Disabled lain bagi aktor Group

1. Ketik Search `Wawan Setiawan`, tekan Enter, lalu klik nama Wawan Setiawan
2. Klik tab Role
3. Klik sub-tab Group Role
4. Hover checkbox baris Group Role `Manage files` pada IT Infrastructure (di luar scope aktor Group)
5. Verifikasi checkbox baris Disabled dengan tooltip `You don't have permission to edit.`
6. Klik Breadcrumb `Settings` untuk kembali ke User List
7. Ganti isi kotak search dengan `Gita Permata`, tekan Enter, lalu klik nama Gita Permata
8. Klik tab Role
9. Klik sub-tab Global Role
10. Hover switch Global Role `Manage accounting`
11. Verifikasi switch Global Role `Manage accounting` Disabled dengan tooltip `You don't have permission to edit.`
12. Hover checkbox `Update` Global Role `Manage accounting`
13. Verifikasi checkbox `Update` Global Role `Manage accounting` Disabled dengan tooltip `You don't have permission to edit.`
14. Klik sub-tab Group Role
15. Klik `[Assign Group]` pada baris Group Role `Manage group`
16. Hover node Finance & Accounting di pemilih grup
17. Verifikasi node Finance & Accounting Disabled dengan tooltip `This group is already assigned to this role.`
18. Klik `✕` pada pemilih grup
19. Klik Breadcrumb `Settings` untuk kembali ke User List
20. Ganti isi kotak search dengan `Yuda Pratama`, tekan Enter, lalu klik nama Yuda Pratama
21. Klik tab Role
22. Klik sub-tab Transaction Role
23. Klik `[+ Assign]`
24. Pilih Transaction Type `Disposal` pada Modal Assign Transaction Role
25. Hover opsi Role `Approver`
26. Verifikasi opsi Role `Approver` Disabled dengan tooltip `This role is already assigned. Use Assign Group on its row to add groups.`
27. Klik `✕` pada Modal Assign Transaction Role
28. Verifikasi dialog `Unsaved Changes` tampil
29. Klik `[Leave]`
30. Klik Breadcrumb `Settings` untuk kembali ke User List

### TC-FA-SU-123: Checkbox ke-(limit+1) Disabled dan Select All auto-cap

31. Logout sebagai Sinta Dewi
32. Login sebagai Lina Marlina (Total Control) dengan `Spectra.env.FA_TC_PASSWORD` pada Client `FaUserSel`
33. Buka halaman Fixed Asset > Settings > User
34. Centang 99 baris pertama yang dapat dipilih secara manual lintas halaman
35. Centang baris ke-100
36. Verifikasi checkbox baris ke-100 tercentang (batas inklusif)
37. Hover checkbox baris ke-101
38. Verifikasi checkbox baris ke-101 Disabled dengan tooltip "You've reached the maximum selection of 100 rows."
39. Verifikasi (TC-FA-SU-76 butir d) checkbox baris ke-101 Disabled dengan tooltip `You've reached the maximum selection of 100 rows.`
40. Klik `Unselect All`
41. Klik `Select All (118 records)`
42. Verifikasi toast error persist "Error, only the first 100 of 118 rows were selected. Narrow your filter to include the rest."
43. Verifikasi 100 baris pertama menurut sort aktif terpilih
44. Klik `Unselect All`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-SU-950 ada di spec 356.
- Langkah 1, 7, dan 20 menggabungkan Search baris target dengan klik nama karena 120 pengguna tersebar lintas halaman (R-16).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 19, dan 30 (kembali ke User List), 18 (tutup pemilih grup tanpa perubahan), 31 sampai 33 (ganti akun dengan langkah eksplisit; S-07), 40 dan 44 (Unselect All), dan 34 (pengulangan centang baris sampai ke-99 sebagai satu langkah karena aksi yang sama diulang tanpa asersi). Langkah 28 sampai 29 menjalankan penutupan form dirty (S-08).
- Urutan TC sumber diubah: butir d TC-FA-SU-76 (checkbox melebihi Selection Limit) diasersi pada langkah 39 bersama TC-FA-SU-123 dengan aktor Total Control, karena aktor Group hanya melihat pengguna dalam scope grupnya sehingga tidak dijamin memiliki lebih dari 100 baris yang dapat dipilih.
- Alasan spec melewati sekitar 35 langkah: kedua TC berkelas e pada Client `FaUserSel` yang sama; TC-FA-SU-76 memuat lima kondisi tooltip Disabled dalam satu TC sumber sehingga lima asersinya tetap berurutan pada data yang sama.
- Temuan untuk QA (S-15): (1) TC-FA-SU-76 menyatukan lima kondisi tooltip (scope aktor, Global Role target, node grup, Selection Limit, kombinasi Transaction Role) dalam satu TC dan tidak menyebut pengguna target; spec memilih Wawan Setiawan, Gita Permata, dan Yuda Pratama dari Pre-setup #23 dan #39. (2) Pre-setup TC tidak menyebut apakah Sinta Dewi, Lina Marlina, Wawan Setiawan, Gita Permata, dan Yuda Pratama ada pada Client `FaUserSel` (#36) maupun cara memilih Client saat login; spec mensyaratkan seed memuat semuanya. (3) Email akun Sinta Dewi (#6) tidak tertulis di Pre-setup TC. (4) Butir a TC-FA-SU-76 menyebut "Baris Group Role atau Transaction Role" di luar scope; spec mengasersi baris Group Role saja (Transaction Role di luar scope tidak diasersi). (5) Butir b TC-FA-SU-76 menyebut aktor Group dan Group Manager; Pre-setup TC pada TC itu tidak memuat Group Manager, sehingga hanya aktor Group yang diasersi. (6) Butir e TC-FA-SU-76 tidak menyebut Transaction Type; spec memakai `Disposal` sesuai Data Uji "Approver Disposal sudah ada". (7) TC-FA-SU-123 langkah 1 menyebut "muat 120 pengguna" sebagai langkah; spec memperlakukannya sebagai seeding Pre-setup #36.
