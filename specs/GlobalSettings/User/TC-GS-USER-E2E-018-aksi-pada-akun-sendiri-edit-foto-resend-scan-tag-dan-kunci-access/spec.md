---
id: TC-GS-USER-E2E-018-aksi-pada-akun-sendiri-edit-foto-resend-scan-tag-dan-kunci-access
title: "Aksi pada Akun Sendiri: Edit dari Row Action dan Edit Profile, Kunci Access dan Temporary User, Resend Confirmation Email, Scan dan Unpair TAG, serta Edit Foto Profil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-83
  - TC-GS-USER-84
  - TC-GS-USER-1029
  - TC-GS-USER-1030
  - TC-GS-USER-1073
  - TC-GS-USER-1074
coverage:
  web: automated
---

# Aksi pada Akun Sendiri: Edit dari Row Action dan Edit Profile, Kunci Access dan Temporary User, Resend Confirmation Email, Scan dan Unpair TAG, serta Edit Foto Profil

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Role yang diuji (tiap role memakai akunnya sendiri; langkah ganti akun ditulis eksplisit di Test Steps):

| Role | Akun (Tabel Data Uji Pre-setup) | Nama user | Env var password | Aksi pada akun sendiri |
|---|---|---|---|---|
| Total Control | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (No. 2) | Siti Nurhaliza | `Spectra.env.GS_TC_PASSWORD` | Edit dari row action (TC-GS-USER-84), Edit Profile (TC-GS-USER-1073), kunci Access dan Temporary User (TC-GS-USER-1074), Resend Confirmation Email (TC-GS-USER-1029), Scan dan Unpair TAG (TC-GS-USER-1030) |
| Manage user and role (Full CRUD) | `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (No. 4) | Fajar Nugroho | `Spectra.env.GS_FULLCRUD_PASSWORD` | Edit foto profil (TC-GS-USER-83) |

- Login akun Total Control (aktor pertama spec, sekaligus akun default suite) dilakukan di hook `before`; Full CRUD memakai langkah ganti akun eksplisit. Karena spec berakhir di akun Full CRUD, hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Admin kedua (pelaku yang hanya memicu perubahan state, sesi API): akun Total Control kedua, disediakan tim FE (tidak ada di Tabel Pre-setup), password `Spectra.env.GS_TC2_PASSWORD`. Admin kedua mengubah email Siti Nurhaliza di langkah 34 (TC-GS-USER-1029 precondition c "diubah admin lain"); mekanismenya tidak disebut di TC dan PRD, disediakan tim FE/BE (nama endpoint ditentukan tim FE di tahap script).
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`, `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca kecuali yang tertulis di bawah): Position `Internal Auditor` (Master Data No. 22); TAG `TAG-USR-0001` (user, aktif, bebas, No. 25); Client plan Growth (No. 26). Berkas foto `avatar.png` (≤1 MB) disediakan tim FE di fixture. Siti Nurhaliza belum punya TAG terpasang dan Fajar Nugroho belum punya foto (precondition TC-GS-USER-1030 dan TC-GS-USER-83; Tabel Pre-setup tidak menyebut kedua state ini, disediakan tim FE/BE).
- Data Dinamis: email baru pending untuk Siti Nurhaliza `sitinurhaliza+{runId}-018@qwertysystem.net` (dipasang di langkah 34).
- Efek pada data Pre-setup akun aktor (S-06): TC-GS-USER-1073 mengubah Position Siti Nurhaliza menjadi `Internal Auditor` (nilai awal Position dicatat di hook `before`, Position awal bukan `Internal Auditor`); TC-GS-USER-1029 memasang pending email Siti Nurhaliza; TC-GS-USER-1030 memasang lalu melepas `TAG-USR-0001`; TC-GS-USER-83 mengunggah foto Fajar Nugroho. Hook `after` memulihkan Position awal, membatalkan pending email, melepas `TAG-USR-0001` bila masih terpasang, dan menghapus foto Fajar Nugroho lewat API. Last Updated dan Modified By Siti Nurhaliza dan Fajar Nugroho tidak ikut pulih.
- Kemampuan teknis (disediakan tim FE/BE): simulasi scan TAG (`TAG-USR-0001`); upload berkas lewat file picker; memajukan jam server dan jam browser bersama (cooldown Resend 60 detik pada TC-GS-USER-1029; countdown UI berjalan di jam browser).
- State global yang diubah: jam server dan jam browser (dimajukan di langkah 35, dipulihkan di langkah 45; hook `after` memulihkan sebagai cadangan), serta data akun aktor di atas. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-84: Edit akun sendiri dari row action User List

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Klik icon Search, ketik `Siti Nurhaliza`, tekan Enter
3. Klik (⋯) baris `Siti Nurhaliza` (akun sendiri)
4. Verifikasi opsi `Edit` tampil dan enabled
5. Klik `Edit`
6. Verifikasi modal Edit User terbuka
7. Verifikasi field modal Edit User terisi data Siti Nurhaliza (pre-filled)
8. Verifikasi checkbox Access disabled
9. Verifikasi checkbox Temporary User disabled
10. Klik `✕` pada header modal Edit User

### TC-GS-USER-1073: Edit Profile akun sendiri dari User Detail menyimpan data identitas

11. Klik Name `Siti Nurhaliza` untuk membuka Detail
12. Klik menu `[⋯]` header
13. Verifikasi menu `Edit Profile` tampil dan enabled
14. Klik `Edit Profile`
15. Verifikasi modal Edit User terbuka
16. Verifikasi field modal Edit User terisi data Siti Nurhaliza (pre-filled)
17. Catat penanda waktu baseline Changelog
18. Ubah Position ke `Internal Auditor`
19. Klik `[Save]`
20. Tunggu aksi selesai (modal Edit User tertutup)
21. Verifikasi Position `Internal Auditor` tampil di Detail
22. Klik Tab `Changelog`
23. Verifikasi entri Changelog baru untuk perubahan Position tercatat sesudah baseline

### TC-GS-USER-1074: Modal Edit akun sendiri mengunci Access dan Temporary User

24. Klik menu `[⋯]` header
25. Klik `Edit Profile`
26. Hover checkbox Access
27. Verifikasi checkbox Access tampil namun disabled
28. Verifikasi tooltip checkbox Access `"You can't manage your own account from here."`
29. Klik checkbox Temporary User
30. Hover checkbox Temporary User
31. Verifikasi checkbox Temporary User tampil namun disabled
32. Verifikasi tooltip checkbox Temporary User `"You can't manage your own account from here."`
33. Klik `✕` pada header modal Edit User

### TC-GS-USER-1029: Resend Confirmation Email pada akun sendiri tidak diblok

34. Admin kedua mengubah email Siti Nurhaliza menjadi `sitinurhaliza+{runId}-018@qwertysystem.net` lewat sesi API sehingga berstatus pending
35. Majukan jam server dan jam browser bersama 120 detik sehingga cooldown resend sudah lewat
36. Klik menu User di sidebar Global Settings
37. Klik icon Search, ketik `Siti Nurhaliza`, tekan Enter
38. Klik Name `Siti Nurhaliza` untuk membuka Detail
39. Verifikasi tombol `Resend Confirmation Email` di header Detail tampil dan enabled
40. Klik `Resend Confirmation Email`
41. Verifikasi toast sukses `Success, confirmation email has been sent to Siti Nurhaliza.`
42. Verifikasi tombol `Resend Confirmation Email` berubah disabled
43. Hover tombol `Resend Confirmation Email`
44. Verifikasi tooltip countdown cooldown 60 detik tampil pada tombol `Resend Confirmation Email`
45. Pulihkan jam server dan jam browser ke waktu semula

### TC-GS-USER-1030: Scan TAG dan Unpair TAG pada akun sendiri tidak diblok

46. Verifikasi `Scan TAG` tampil dan enabled pada Detail Siti Nurhaliza
47. Klik `Scan TAG`
48. Scan `TAG-USR-0001`
49. Verifikasi badge `Verified`
50. Verifikasi toast sukses `Success, TAG has been paired.`
51. Verifikasi `Unpair` tampil dan enabled
52. Klik `Unpair`
53. Klik `[Unpair]` pada dialog
54. Verifikasi badge `Unverified`
55. Verifikasi toast sukses `Success, TAG has been unpaired.`

### TC-GS-USER-83: Capability holder dapat Edit foto profil sendiri dari hover Avatar

56. Logout, lalu login sebagai Manage user and role (Full CRUD)
57. Buka Global Settings > User > User List (sub-tab Login User)
58. Klik icon Search, ketik `Fajar Nugroho`, tekan Enter
59. Klik Name `Fajar Nugroho` (akun sendiri) untuk membuka Detail
60. Hover Avatar header
61. Klik `[Edit]`
62. Pilih file `avatar.png`
63. Verifikasi toast sukses `Success, photo has been updated.`
64. Verifikasi Avatar header menampilkan foto baru

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (64 langkah) karena keenam TC berada di satu kelas (aksi pada akun sendiri, pada satu layar User Detail dan modal Edit User); tiap blok TC memakai data dan aksi sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Ganti akun hanya satu kali.
- Urutan TC sumber diubah: TC-GS-USER-83 (akun Full CRUD) paling akhir supaya ganti akun hanya satu kali; TC-GS-USER-84 mendahului TC-GS-USER-1073 dan TC-GS-USER-1074 (screening tanpa perubahan data lebih dulu); TC-GS-USER-1029 dan TC-GS-USER-1030 mengikuti TC-GS-USER-1074 karena TC-GS-USER-1029 memasang state pending email yang tidak dibutuhkan blok lain. TC-GS-USER-1030 memakai Detail Siti Nurhaliza yang sudah terbuka dari langkah 38 (langkah 1 TC-GS-USER-1030 dipenuhi oleh langkah 38).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 37, dan 58 (Search nama target), 10 dan 33 (menutup modal tanpa perubahan lewat `✕`), 17 (baseline Changelog sebelum aksi pemicu pertama yang diasersi, S-12), 20 (Tunggu aksi selesai), 22 (membuka Tab Changelog untuk mengamati entri), 34 (pemicu admin kedua), 35 dan 45 (memajukan dan memulihkan jam), 36 (kembali ke User List), 56 dan 57 (ganti akun dan membuka User List).
- Pembagian TC lintas spec: hover Avatar `[Edit]` pada akun sendiri (TC-GS-USER-75 f dan TC-GS-USER-79 e) diverifikasi di spec 015; Resend Confirmation Email pada Default User (TC-GS-USER-1046) diverifikasi di spec 017.
- Temuan untuk QA:
  - TC-GS-USER-1073 Position baru tidak diberi nilai di Data Uji; spec memakai `Internal Auditor` (Master Data Pre-setup No. 22) dan mensyaratkan Position awal Siti Nurhaliza berbeda.
  - TC-GS-USER-1073 Expected b ("entri Changelog tercatat") tidak menyebut lokasi atau isi entri; spec mengamati Tab Changelog di User Detail dan mengasersi entri baru sesudah baseline tanpa isi kolom.
  - TC-GS-USER-1074 Expected b menyebut "Centang Temporary User tampil namun disabled"; spec membaca sebagai checkbox Temporary User disabled dengan tooltip, dan langkah "centang" dilakukan sebagai klik pada checkbox yang disabled.
  - TC-GS-USER-1030 Expected a mengharapkan `Scan TAG` dan `Unpair` tampil dan enabled bersamaan tanpa precondition TAG pada akun Siti Nurhaliza; spec mengasersi `Scan TAG` sebelum scan dan `Unpair` sesudah scan. Post Condition "`TAG-USR-0001` kembali bebas" tidak punya langkah observasi; tidak diasersi.
  - TC-GS-USER-1029 precondition c tidak menyebut cooldown resend sudah lewat dan cara admin lain mengubah email; Expected c tidak menyebut teks tooltip countdown selain "cooldown 60 detik". Spec memajukan jam server dan jam browser bersama.
  - TC-GS-USER-83 tidak menyebut dialog atau langkah konfirmasi sesudah memilih file (mis. preview atau crop); spec mengikuti Langkah Uji TC.
  - TC-GS-USER-84 Expected b merujuk `USER-LOGIC-01f` untuk kunci Access dan Temporary User tanpa teks tooltip; tooltip hanya diasersi di TC-GS-USER-1074.
