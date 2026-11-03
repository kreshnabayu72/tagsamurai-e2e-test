---
id: TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role
title: "Absence Log: Edit No-Op, Aksi Lintas User, Pair TAG dari Create, Product Selector, Entry Per-Role Assign dan Remove Tier, Reset Authenticator, dan Aksi Admin Console Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-919
  - TC-GS-USER-920
  - TC-GS-USER-923
  - TC-GS-USER-925
  - TC-GS-USER-929
  - TC-GS-USER-930
  - TC-GS-USER-931
  - TC-GS-USER-932
  - TC-GS-USER-942
  - TC-GS-USER-943
coverage:
  web: automated
---

# Absence Log: Edit No-Op, Aksi Lintas User, Pair TAG dari Create, Product Selector, Entry Per-Role Assign dan Remove Tier, Reset Authenticator, dan Aksi Admin Console Tidak Menulis Log

## Prerequisites

- Mode: FE+BE (kelas g, asersi absence). Pemicu kelas lain (simulasi scan TAG pada TC-GS-USER-923, aksi staff di Admin Console pada TC-GS-USER-943) hanya membentuk kondisi yang diasersi tidak tercatat (P-5a, lihat Notes).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor pertama: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Akun kedua (ganti akun eksplisit di TC-GS-USER-943): Total Control entitas Principal (Tabel Data Uji Pre-setup No. 26, entitas Principal), disediakan tim FE; kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Pelaku pemicu TC-GS-USER-943: staff Principal `Rizal Akbar`, disediakan tim FE (tidak ada di Tabel Data Uji Pre-setup); kredensial `Spectra.env.AC_STAFF_PASSWORD` (nama baru). Hook `after` mengembalikan sesi ke akun default suite (Total Control, Siti Nurhaliza).
- Env var: `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`, `AC_STAFF_PASSWORD`, `USER_PASSWORD` (password login user seed `John Doe B {runId}-147`; memenuhi policy password), semuanya didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup (hanya dibaca, tidak diubah): akun aktor Siti Nurhaliza (No. 2) sebagai pemilik Tab System Log; Position `Staff` dan `Supervisor` (No. 22) dan Division `Finance` (No. 23); TAG `TAG-USR-0001` (No. 25, user, aktif, bebas); entitas Principal (No. 26).
- Data Dinamis milik spec (suffix per run dan nomor spec; tiap TC punya user dan baseline sendiri), semuanya Activated, Division `Finance`, Access `Fixed Asset` kecuali dinyatakan lain, di-seed lewat API di hook `before` (HK1) dan dihapus di hook `after`:
  - TC-GS-USER-919: `Dewi Lestari {runId}-147`, Email `dewilestari+{runId}-147@qwertysystem.net`.
  - TC-GS-USER-920: `Dewi Lestari B {runId}-147`, Email `dewilestarib+{runId}-147@qwertysystem.net`, Position `Staff`; `John Doe {runId}-147`, Email `johndoe+{runId}-147@qwertysystem.net` (user lain yang tidak boleh bertambah barisnya).
  - TC-GS-USER-923: `Tag Create {runId}-147` (First Name `Tag`, Last Name `Create {runId}-147`), Email `tagcreate+{runId}-147@qwertysystem.net`, dibuat lewat UI oleh spec (tidak di-seed), TAG `TAG-USR-0001`.
  - TC-GS-USER-925: `Joko Susilo {runId}-147`, Email `jokosusilo+{runId}-147@qwertysystem.net`, Access `Fixed Asset` dan `Supply Asset`.
  - TC-GS-USER-929: `Ahmad Fauzi {runId}-147`, Email `ahmadfauzi+{runId}-147@qwertysystem.net`, tanpa tier akses, role `Manage files` Assigned. TC-GS-USER-930: `Ahmad Fauzi B {runId}-147` (Email `ahmadfauzib+{runId}-147@qwertysystem.net`), keadaan awal sama. TC-GS-USER-931: `Ahmad Fauzi C {runId}-147` (Email `ahmadfauzic+{runId}-147@qwertysystem.net`), role `Manage files` Assigned lebih dulu, lalu tier Total Control. TC-GS-USER-932: `Ahmad Fauzi D {runId}-147` (Email `ahmadfauzid+{runId}-147@qwertysystem.net`), role `Manage files` Assigned lebih dulu, lalu tier Read Only.
  - TC-GS-USER-942: `John Doe B {runId}-147`, Email `johndoeb+{runId}-147@qwertysystem.net`, MFA Enrolled, password `Spectra.env.USER_PASSWORD`, sudah login sekali sebelum baseline dicatat sehingga Tab User Log memuat `Login` `Success`.
  - TC-GS-USER-943: `Rizal Akbar` (staff Principal, disediakan tim FE) dengan sedikitnya satu baris di Tab System Log GS yang dibuat sebelum baseline dicatat.
- Kemampuan teknis, disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut cara atau endpoint): (1) seeding user, tier Total Control atau Read Only, penugasan role `Manage files`, dan event login lewat API, memakai endpoint aplikasi dengan sesi API aktor Total Control (Siti Nurhaliza) sehingga entri log seed (Create dan Assign) ditulis sebelum baseline dicatat dan Modified By seed adalah aktor itu; kemampuan baca jumlah baris log per user dan Action lewat BE (baseline) disediakan tim FE/BE tanpa endpoint karangan; (2) simulasi RFID reader tersambung dan scan `TAG-USR-0001` pada tombol `Scan TAG` (HK7); (3) sesi login user seed yang memenuhi MFA (`John Doe B {runId}-147`); (4) aksi Assign Role oleh `Rizal Akbar` di Admin Console lewat sesi API, termasuk satu baris aksi GS milik Rizal Akbar di Tab System Log sebagai kondisi awal; (5) akun Total Control entitas Principal.
- State global yang diubah: TAG `TAG-USR-0001` dipasang ke `Tag Create {runId}-147` (TC-GS-USER-923); sesi UI berpindah ke akun Total Control Principal (TC-GS-USER-943). Hook `after`, yang tetap berjalan walau spec gagal di tengah, menghapus `Tag Create {runId}-147` dan memastikan `TAG-USR-0001` kembali bebas, lalu mengembalikan sesi ke akun default suite. Suite berjalan serial (`suite.md`).
- Baseline log: jumlah entri audit trail permanen tidak dapat diturunkan dari seeding. Tiap TC mencatat baseline jumlah baris per user dan Action pada surface yang diasersi (langkah `Catat baseline TC-GS-USER-N`) lewat kemampuan baca BE sebelum aksi pemicu TC itu; user yang dibuat spec dengan nama bersuffix unik (TC-GS-USER-923) berbaseline nol. Asersi absence memakai jumlah yang tetap sama dengan baseline, bukan anchor baris seed (S-12); anchor positif diasersi lebih dulu pada surface yang sama (8b butir 2).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua user bersuffix `{runId}-147` yang masih ada. Hook `before` menghapus sisa user bersuffix `-147` dari run lama. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### TC-GS-USER-919: Edit No-Op tidak menulis log di Tab Changelog, System Log, maupun Activity Log

1. Catat baseline TC-GS-USER-919 lewat kemampuan baca BE, sebelum aksi pemicu TC ini: `{n0-cl}` jumlah seluruh baris Tab Changelog `Dewi Lestari {runId}-147`, `{n0-sl}` jumlah baris Tab System Log `Siti Nurhaliza` untuk `Dewi Lestari {runId}-147`, dan `{n0-al}` jumlah baris Activity Log untuk `Dewi Lestari {runId}-147`
2. Klik icon Search, ketik `Dewi Lestari {runId}-147`, tekan Enter, klik `⋯` pada baris tersebut > Edit
3. Klik [Save] tanpa mengubah field apa pun
4. Tunggu aksi selesai (modal Edit tertutup)
5. Buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-147`, tekan Enter, klik Name `Dewi Lestari {runId}-147`, buka Tab Changelog
6. Verifikasi Tab Changelog `Dewi Lestari {runId}-147` memuat baris Action `Create` dan Field `Name` (entri seeding)
7. Verifikasi Tab Changelog `Dewi Lestari {runId}-147`: jumlah seluruh baris tetap sama dengan baseline `{n0-cl}` (tidak bertambah)
8. Buka Global Settings > User > User List, klik icon Search, ketik `Siti Nurhaliza`, tekan Enter, klik Name `Siti Nurhaliza`, buka Tab System Log, klik icon Search, ketik `Dewi Lestari {runId}-147`, tekan Enter
9. Verifikasi Tab System Log `Siti Nurhaliza` memuat baris Action `Create`, Object `User`, dan Name `Dewi Lestari {runId}-147` (entri seeding)
10. Verifikasi Tab System Log `Siti Nurhaliza`: jumlah baris untuk `Dewi Lestari {runId}-147` tetap sama dengan baseline `{n0-sl}` (tidak bertambah)
11. Buka Global Settings > Activity Log, klik icon Search, ketik `Dewi Lestari {runId}-147`, tekan Enter
12. Verifikasi Activity Log memuat baris Action `Create`, Object `User`, dan Name `Dewi Lestari {runId}-147` (entri seeding)
13. Verifikasi Activity Log: jumlah baris untuk `Dewi Lestari {runId}-147` tetap sama dengan baseline `{n0-al}` (tidak bertambah)

### TC-GS-USER-920: Aksi pada satu user tidak menulis log ke user lain

14. Catat baseline TC-GS-USER-920 lewat kemampuan baca BE, sebelum aksi pemicu TC ini: `{n0-edit}` jumlah baris Action `Edit` dengan Field `Position` di Tab Changelog `Dewi Lestari B {runId}-147` dan `{n0-john}` jumlah seluruh baris Tab Changelog `John Doe {runId}-147`
15. Buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari B {runId}-147`, tekan Enter, klik `⋯` pada baris tersebut > Edit
16. Ganti Position dari `Staff` menjadi `Supervisor`
17. Klik [Save]
18. Tunggu aksi selesai (modal Edit tertutup)
19. Buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari B {runId}-147`, tekan Enter, klik Name `Dewi Lestari B {runId}-147`, buka Tab Changelog
20. Verifikasi Tab Changelog `Dewi Lestari B {runId}-147`: jumlah baris dengan Action `Edit` dan Field `Position` bertambah tepat 1 dari baseline `{n0-edit}`
21. Verifikasi Tab Changelog `Dewi Lestari B {runId}-147`: baris teratas dengan Action `Edit`, Field `Position`, Old Value `Staff`, New Value `Supervisor`
22. Buka Global Settings > User > User List, klik icon Search, ketik `John Doe {runId}-147`, tekan Enter, klik Name `John Doe {runId}-147`, buka Tab Changelog
23. Verifikasi Tab Changelog `John Doe {runId}-147` memuat baris Action `Create` dan Field `Name` (entri seeding)
24. Verifikasi Tab Changelog `John Doe {runId}-147`: jumlah seluruh baris tetap sama dengan baseline `{n0-john}` (tidak bertambah)

### TC-GS-USER-923: Pair TAG dari Popup Create tidak menulis baris Pair TAG terpisah

25. Catat baseline TC-GS-USER-923 lewat kemampuan baca BE, sebelum aksi pemicu TC ini: jumlah baris Modal Changelog User untuk `Tag Create {runId}-147` adalah nol (user dibuat oleh spec ini; nama bersuffix unik berbaseline nol)
26. Buka Global Settings > User > User List, klik [+ User] di Table Tools
27. Isi First Name `Tag`, Last Name `Create {runId}-147`, Division `Finance`, Email `tagcreate+{runId}-147@qwertysystem.net`, centang Access `Fixed Asset`
28. Klik `Scan TAG`, simulasikan scan `TAG-USR-0001`
29. Klik [Submit]
30. Tunggu aksi selesai (Popup tertutup)
31. Klik icon Changelog di Table Tools (Modal Changelog User), klik icon Search, ketik `Tag Create {runId}-147`, tekan Enter
32. Verifikasi Modal Changelog User: jumlah baris dengan Action `Create` dan Field `Name` untuk User Name `Tag Create {runId}-147` bertambah tepat 1 dari baseline nol
33. Verifikasi Modal Changelog User: baris teratas dengan Action `Create`, User Name `Tag Create {runId}-147`, dan Field `Name`
34. Verifikasi Modal Changelog User: jumlah baris dengan Action `Pair TAG` untuk `Tag Create {runId}-147` tetap nol (tidak bertambah), sehingga hanya baris `Create` dengan Field `Name` yang tercatat
35. Tutup Modal Changelog User

### TC-GS-USER-925: Product Selector tidak menulis log

36. Catat baseline TC-GS-USER-925 lewat kemampuan baca BE, sebelum aksi pemicu TC ini: `{n0-al}` jumlah baris Activity Log untuk `Joko Susilo {runId}-147`
37. Buka Global Settings > User > User List, klik icon Search, ketik `Joko Susilo {runId}-147`, tekan Enter, klik Name `Joko Susilo {runId}-147`
38. Pilih Product Selector `Fixed Asset`
39. Kembali ke User List dengan klik Back
40. Buka Global Settings > Activity Log, klik icon Search, ketik `Joko Susilo {runId}-147`, tekan Enter
41. Verifikasi Activity Log memuat baris Action `Create`, Object `User`, dan Name `Joko Susilo {runId}-147` (entri seeding)
42. Verifikasi Activity Log: jumlah baris untuk `Joko Susilo {runId}-147` tetap sama dengan baseline `{n0-al}` (tidak bertambah)

### TC-GS-USER-929: Assign Total Control tidak menulis entry per-role di Modal Changelog User > Role

43. Catat baseline TC-GS-USER-929 lewat kemampuan baca BE, sebelum aksi pemicu TC ini: `{n0-role}` jumlah seluruh baris Modal Changelog User > Role `Ahmad Fauzi {runId}-147` dan `{n0-cl}` jumlah baris Action `Assign` dengan Field `Access Level` di Tab Changelog `Ahmad Fauzi {runId}-147`
44. Buka Global Settings > Role & Permission, buka Tab Total Control, klik [+ Assign]
45. Isi Search Popup Table User Picker dengan `Ahmad Fauzi {runId}-147`, tekan Enter, centang barisnya, klik [Assign]
46. Tunggu aksi selesai (Popup tertutup)
47. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-147`, tekan Enter, klik Name `Ahmad Fauzi {runId}-147`, buka Tab Role, klik icon Changelog di Tab Role (Modal Changelog: User > Role)
48. Verifikasi Modal Changelog User > Role `Ahmad Fauzi {runId}-147` memuat baris Action `Assign`, Role `Manage files`, Field `Access`, Old Value `—`, New Value `Assigned` (entri seeding)
49. Verifikasi Modal Changelog User > Role `Ahmad Fauzi {runId}-147`: jumlah seluruh baris tetap sama dengan baseline `{n0-role}` akibat Assign Total Control (tidak bertambah; tidak ada baris `Assign (via ...)` atau `Remove (via ...)`)
50. Tutup Modal Changelog User > Role
51. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-147`, tekan Enter, klik Name `Ahmad Fauzi {runId}-147`, buka Tab Changelog
52. Verifikasi Tab Changelog `Ahmad Fauzi {runId}-147`: jumlah baris dengan Action `Assign` dan Field `Access Level` (ringkasan Assign Total Control) bertambah tepat 1 dari baseline `{n0-cl}`

### TC-GS-USER-930: Assign Read Only tidak menulis entry per-role di Modal Changelog User > Role

53. Catat baseline TC-GS-USER-930 lewat kemampuan baca BE, sebelum aksi pemicu TC ini: `{n0-role}` jumlah seluruh baris Modal Changelog User > Role `Ahmad Fauzi B {runId}-147` dan `{n0-cl}` jumlah baris Action `Assign` dengan Field `Access Level` di Tab Changelog `Ahmad Fauzi B {runId}-147`
54. Buka Global Settings > Role & Permission, buka Tab Read Only, klik [+ Assign]
55. Isi Search Popup Table User Picker dengan `Ahmad Fauzi B {runId}-147`, tekan Enter, centang barisnya, klik [Assign]
56. Tunggu aksi selesai (Popup tertutup)
57. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi B {runId}-147`, tekan Enter, klik Name `Ahmad Fauzi B {runId}-147`, buka Tab Role, klik icon Changelog di Tab Role (Modal Changelog: User > Role)
58. Verifikasi Modal Changelog User > Role `Ahmad Fauzi B {runId}-147` memuat baris Action `Assign`, Role `Manage files`, Field `Access`, Old Value `—`, New Value `Assigned` (entri seeding)
59. Verifikasi Modal Changelog User > Role `Ahmad Fauzi B {runId}-147`: jumlah seluruh baris tetap sama dengan baseline `{n0-role}` akibat Assign Read Only (tidak bertambah; tidak ada baris `Assign (via ...)` atau `Remove (via ...)`)
60. Tutup Modal Changelog User > Role
61. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi B {runId}-147`, tekan Enter, klik Name `Ahmad Fauzi B {runId}-147`, buka Tab Changelog
62. Verifikasi Tab Changelog `Ahmad Fauzi B {runId}-147`: jumlah baris dengan Action `Assign` dan Field `Access Level` (ringkasan Assign Read Only) bertambah tepat 1 dari baseline `{n0-cl}`

### TC-GS-USER-931: Remove Total Control tidak menulis entry per-role di Modal Changelog User > Role

63. Catat baseline TC-GS-USER-931 lewat kemampuan baca BE, sebelum aksi pemicu TC ini: `{n0-role}` jumlah seluruh baris Modal Changelog User > Role `Ahmad Fauzi C {runId}-147` dan `{n0-cl}` jumlah baris Action `Remove` dengan Field `Access Level` di Tab Changelog `Ahmad Fauzi C {runId}-147`
64. Buka Global Settings > Role & Permission, buka Tab Total Control, klik icon Search, ketik `Ahmad Fauzi C {runId}-147`, tekan Enter, klik `⋯` pada baris `Ahmad Fauzi C {runId}-147` > Remove
65. Klik [Remove] pada dialog Remove Total Control
66. Tunggu aksi selesai (dialog tertutup)
67. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi C {runId}-147`, tekan Enter, klik Name `Ahmad Fauzi C {runId}-147`, buka Tab Role, klik icon Changelog di Tab Role (Modal Changelog: User > Role)
68. Verifikasi Modal Changelog User > Role `Ahmad Fauzi C {runId}-147` memuat baris Action `Assign`, Role `Manage files`, Field `Access`, Old Value `—`, New Value `Assigned` (entri seeding)
69. Verifikasi Modal Changelog User > Role `Ahmad Fauzi C {runId}-147`: jumlah seluruh baris tetap sama dengan baseline `{n0-role}` akibat Remove Total Control (tidak bertambah; tidak ada baris `Assign (via ...)` atau `Remove (via ...)`)
70. Tutup Modal Changelog User > Role
71. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi C {runId}-147`, tekan Enter, klik Name `Ahmad Fauzi C {runId}-147`, buka Tab Changelog
72. Verifikasi Tab Changelog `Ahmad Fauzi C {runId}-147`: jumlah baris dengan Action `Remove` dan Field `Access Level` (ringkasan Remove Total Control) bertambah tepat 1 dari baseline `{n0-cl}`

### TC-GS-USER-932: Remove Read Only tidak menulis entry per-role di Modal Changelog User > Role

73. Catat baseline TC-GS-USER-932 lewat kemampuan baca BE, sebelum aksi pemicu TC ini: `{n0-role}` jumlah seluruh baris Modal Changelog User > Role `Ahmad Fauzi D {runId}-147` dan `{n0-cl}` jumlah baris Action `Remove` dengan Field `Access Level` di Tab Changelog `Ahmad Fauzi D {runId}-147`
74. Buka Global Settings > Role & Permission, buka Tab Read Only, klik icon Search, ketik `Ahmad Fauzi D {runId}-147`, tekan Enter, klik `⋯` pada baris `Ahmad Fauzi D {runId}-147` > Remove
75. Klik [Remove] pada dialog Remove Read Only
76. Tunggu aksi selesai (dialog tertutup)
77. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi D {runId}-147`, tekan Enter, klik Name `Ahmad Fauzi D {runId}-147`, buka Tab Role, klik icon Changelog di Tab Role (Modal Changelog: User > Role)
78. Verifikasi Modal Changelog User > Role `Ahmad Fauzi D {runId}-147` memuat baris Action `Assign`, Role `Manage files`, Field `Access`, Old Value `—`, New Value `Assigned` (entri seeding)
79. Verifikasi Modal Changelog User > Role `Ahmad Fauzi D {runId}-147`: jumlah seluruh baris tetap sama dengan baseline `{n0-role}` akibat Remove Read Only (tidak bertambah; tidak ada baris `Assign (via ...)` atau `Remove (via ...)`)
80. Tutup Modal Changelog User > Role
81. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi D {runId}-147`, tekan Enter, klik Name `Ahmad Fauzi D {runId}-147`, buka Tab Changelog
82. Verifikasi Tab Changelog `Ahmad Fauzi D {runId}-147`: jumlah baris dengan Action `Remove` dan Field `Access Level` (ringkasan Remove Read Only) bertambah tepat 1 dari baseline `{n0-cl}`

### TC-GS-USER-942: Tab User Log tidak memuat Reset Authenticator

83. Catat baseline TC-GS-USER-942 lewat kemampuan baca BE, sebelum aksi pemicu TC ini: `{n0-ra}` jumlah baris Action `Reset Authenticator` di Tab Changelog `John Doe B {runId}-147` dan `{n0-ul}` jumlah seluruh baris Tab User Log `John Doe B {runId}-147`
84. Buka Global Settings > User > User List, klik icon Search, ketik `John Doe B {runId}-147`, tekan Enter, klik Name `John Doe B {runId}-147`
85. Klik `Reset Authenticator`
86. Klik [Reset] pada dialog Reset Authenticator
87. Tunggu aksi selesai (Badge `Enrolled` diganti teks muted `Not enrolled yet`)
88. Buka Tab Changelog
89. Verifikasi Tab Changelog `John Doe B {runId}-147`: jumlah baris dengan Action `Reset Authenticator` bertambah tepat 1 dari baseline `{n0-ra}`
90. Buka Tab User Log
91. Verifikasi Tab User Log `John Doe B {runId}-147` memuat baris Activity `Login` dan Status `Success` (event login seeding)
92. Verifikasi Tab User Log `John Doe B {runId}-147`: jumlah seluruh baris tetap sama dengan baseline `{n0-ul}` (tidak ada baris terkait reset)

### TC-GS-USER-943: Aksi staff di Admin Console tidak tercatat di System Log GS

93. Logout dari akun Total Control Siti Nurhaliza
94. Login sebagai Total Control entitas Principal (akun disediakan tim FE, kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`)
95. Buka Global Settings > User > User List
96. Catat baseline TC-GS-USER-943 lewat kemampuan baca BE, sebelum aksi pemicu TC ini: `{n0-sl}` jumlah baris Tab System Log `Rizal Akbar`
97. Staff `Rizal Akbar` melakukan Assign Role di Admin Console (sesi API Admin Console milik Rizal Akbar, kredensial `Spectra.env.AC_STAFF_PASSWORD`; role dan target Assign disediakan tim FE)
98. Klik icon Search, ketik `Rizal Akbar`, tekan Enter, klik Name `Rizal Akbar`, buka Tab System Log
99. Verifikasi Tab System Log `Rizal Akbar` memuat baris aksi GS milik Rizal Akbar yang dibuat sebelum baseline dicatat
100. Verifikasi Tab System Log `Rizal Akbar`: jumlah baris tetap sama dengan baseline `{n0-sl}` (aksi Assign Role di Admin Console tidak tercatat di System Log GS)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Spec ini kelas g (asersi absence); tiap TC punya user dan baseline sendiri.
- P-5a: spec absence boleh memuat pemicu kelas lain bila hanya membentuk kondisi yang diasersi tidak tercatat. Pemicu TC-GS-USER-923 (simulasi scan TAG, kelas d) dan TC-GS-USER-943 (aksi staff di Admin Console dan ganti entitas, kelas c/h) tidak menjadi objek uji; objek ujinya tetap ketiadaan baris log.
- Urutan TC di spec: 919, 920, 923, 925, 929, 930, 931, 932, 942, 943 (urutan sumber). 943 paling akhir karena berganti akun ke entitas Principal.
- Pembagian TC lintas spec: pencatatan Assign dan Remove Total Control dan Read Only (TC-GS-USER-898 sampai 901) dan Auto-Revert (TC-GS-USER-905, 906) diverifikasi di spec `TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert`. Pencatatan Edit Position diverifikasi di spec `TC-GS-USER-E2E-138-pencatatan-create-edit-delete-field-di-changelog-system-log-dan-activity-log`; pencatatan Pair/Unpair TAG dari Detail dan Reset Authenticator (TC-GS-USER-924) diverifikasi di spec `TC-GS-USER-E2E-142-pencatatan-add-remove-access-pair-unpair-tag-dan-reset-authenticator`. Spec ini memuat sisi presence untuk TC-GS-USER-923 dan 929 sampai 932 (baris `Create` `Name` dan baris ringkasan `Access Level`) karena TC-nya satu rangkaian dengan sisi absence.
- Anchor positif (8b butir 2): TC-GS-USER-919, 920, 925: baris `Create` hasil seeding pada surface yang sama (baseline jumlah yang dicatat), ditambah baris `Edit` `Position` pemicu pada TC-GS-USER-920 sebagai bukti aksi tercatat di user yang diedit; TC-GS-USER-923: baris `Create` `Name` dari aksi yang sama; TC-GS-USER-929 sampai 932: baris `Assign` `Manage files` hasil seeding di Modal Changelog User > Role; TC-GS-USER-942: baris `Reset Authenticator` di Tab Changelog (aksi yang sama) dan baris `Login` `Success` hasil seeding di Tab User Log; TC-GS-USER-943: baris aksi GS milik Rizal Akbar yang dibuat sebelum baseline dicatat.
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan baseline jumlah baris tiap TC, Search nama user dan pembukaan tiap surface log (tiap surface dibuka segar), "Tunggu aksi selesai" (8b butir 8), pemilihan user di Popup Table User Picker, penutupan Modal Changelog User dan Modal Changelog User > Role, serta Back dari Detail ke User List (TC-GS-USER-925).
- TC-GS-USER-919: Langkah Uji menyebut Tab Changelog Dewi dan Activity Log, sedangkan Expected Result menyebut juga System Log; spec mengasersi ketiganya (Tab System Log dibuka di Detail Siti Nurhaliza, aktor yang menjalankan Edit).
- TC-GS-USER-925: Expected Result "Tidak ada entri baru" diasersi pada hasil Search nama user di Activity Log (surface agregat dengan banyak user), bukan pada seluruh isi Activity Log.
- TC-GS-USER-929 sampai 932: "Changelog User" pada Langkah Uji 3 dibaca sebagai Tab Changelog di Detail user (Changelog per user). Asersi ringkasan memakai Action dan Field `Access Level` (Expected TC) tanpa Old Value dan New Value.
- Spec melewati sekitar 35 langkah karena sepuluh TC berada dalam satu kelas (g), tiap TC berdiri sendiri dengan user dan baseline sendiri, dan hampir seluruh langkah adalah blok baca-log berpola (buka surface, Search, anchor, absence). Memecah per TC melipatgandakan hook seeding dan login tanpa mengubah makna; kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-USER-929 Langkah 1 ("role belum punya baris") bertentangan dengan anchor positif 8b butir 2 yang butuh baris di Modal Changelog User > Role; spec men-seed penugasan role `Manage files` sebelum baseline dicatat sebagai anchor. Perlu konfirmasi QA bahwa keadaan itu tidak mengubah hasil yang dimaksud TC.
  - TC-GS-USER-919, 920, 925, 929 sampai 932, 942, 943: anchor positif memerlukan entri log seed (Create, Assign, Login, aksi GS Rizal Akbar) yang ditulis lewat endpoint aplikasi dengan sesi API aktor Total Control; TC tidak menyebut mekanisme seeding dan log-nya (disediakan tim FE/BE).
  - TC-GS-USER-942: "Tidak ada baris terkait reset" tidak menjelaskan baris apa yang dianggap terkait reset; spec mengasersi tidak ada baris baru apa pun di Tab User Log sesudah baseline dicatat.
  - TC-GS-USER-943: TC tidak menyebut role yang di-assign, target Assign Role, atau data awal Rizal Akbar; judul TC menyebut "Changelog dan System Log GS" tetapi Expected Result hanya System Log. Spec hanya mengasersi Tab System Log Rizal Akbar sesuai Expected Result.
  - TC-GS-USER-923: "Create user dengan scan TAG" tidak menyebut nilai field wajib lain atau TAG yang discan; spec memakai First Name `Tag`, Last Name `Create {runId}-147`, Division `Finance`, Access `Fixed Asset`, dan `TAG-USR-0001`.
  - TC-GS-USER-920 Langkah 1 ("Edit Position Dewi Lestari") tidak menyebut nilai Position awal dan akhir; spec memakai `Staff` menjadi `Supervisor` (Position Pre-setup No. 22).
  - Slice ini tidak punya Post Condition pada TC sumber.
