---
id: TC-FA-RP-E2E-265-sinkronisasi-detail-role-dan-tab-role-settings-user-1
title: "Sinkronisasi Detail Role dan Tab Role Settings > User (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-889
  - TC-FA-RP-890
  - TC-FA-RP-891
  - TC-FA-RP-892
  - TC-FA-RP-893
  - TC-FA-RP-894
  - TC-FA-RP-895
coverage:
  web: automated
---

# Sinkronisasi Detail Role dan Tab Role Settings > User (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (kolam pengguna Standard; Ahmad Fauzi dan Budi Santoso tanpa tingkat akses) dan #39 (Detail Role Global Role `Manage accounting` terisi, termasuk baris Ahmad Fauzi; TC-FA-RP-891 dan 892). Kondisi awal yang di-seed di hook `before`: Ahmad Fauzi memegang Global Role `Manage accounting` dengan Create dan Update nonaktif (TC-FA-RP-891 dan 892); Budi Santoso memegang Global Role `Manage Open API` (TC-FA-RP-893 sampai 895) dan tidak memegang `Manage accounting` maupun Group Role `Manage files` di `Data Center` (TC-FA-RP-889 dan 890).
- Pemulihan: antara TC-FA-RP-893 dan 894 Budi Santoso dipulihkan memegang `Manage Open API` lewat seeding API; hook `after` memulihkan Pre-setup yang diubah (Catatan TC "Pemulihan fixture destruktif").
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-889: Assign User ke Global Role di Detail Role tersinkron ke Tab Role Settings > User

1. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage accounting`
2. Klik `[+ Assign]`, centang Budi Santoso, klik `[Assign]`
3. Tunggu aksi selesai: popup tertutup
4. Buka Settings > User > Detail Budi Santoso > Tab Role sub-tab Global Role
5. Verifikasi switch `Manage accounting` aktif dengan Read tercentang dan Create, Update, Delete tidak tercentang

### TC-FA-RP-890: Assign User ke Group Role tersinkron ke Tab Role: baris group muncul

6. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage files` dan pilih node `Data Center`
7. Klik `[+ Assign]`, centang Budi Santoso, klik `[Assign]`
8. Tunggu aksi selesai: popup tertutup
9. Buka Settings > User > Detail Budi Santoso > Tab Role sub-tab Group Role
10. Verifikasi baris `Manage files` untuk group `Data Center` muncul pada Tab Role Budi Santoso

### TC-FA-RP-891: Edit CRUD di Detail Role tersinkron ke Tab Role (arah Detail Role ke Settings > User)

11. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage accounting`
12. Centang Create pada baris Ahmad Fauzi
13. Tunggu aksi selesai: perubahan Create tersimpan
14. Buka Settings > User > Detail Ahmad Fauzi > Tab Role sub-tab Global Role
15. Verifikasi checkbox Create `Manage accounting` pada Tab Role Ahmad Fauzi tercentang tanpa muat ulang manual

### TC-FA-RP-892: Edit CRUD di Tab Role Settings > User tersinkron ke Detail Role (arah sebaliknya)

16. Buka Settings > User > Detail Ahmad Fauzi > Tab Role sub-tab Global Role
17. Centang Update pada `Manage accounting`
18. Tunggu aksi selesai: perubahan Update tersimpan
19. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage accounting`
20. Verifikasi baris Ahmad Fauzi pada Detail Role menampilkan Update tercentang

### TC-FA-RP-893: Remove di Detail Role mencabut penugasan permanen sehingga switch Tab Role OFF

21. Catat baseline (aksi tanpa `Verifikasi`): jumlah kolom Users baris `Manage Open API` di Tab System
22. Buka Detail Role `Manage Open API`
23. Klik `[⋯]` baris Budi Santoso lalu `Remove`, klik `[Remove]`
24. Tunggu aksi selesai: dialog tertutup
25. Buka Settings > User > Detail Budi Santoso > Tab Role sub-tab Global Role
26. Verifikasi switch `Manage Open API` OFF
27. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage Open API`
28. Verifikasi sedikitnya satu baris pengguna lain tampil pada Detail Role `Manage Open API`
29. Verifikasi baris Budi Santoso tidak ada di Detail Role
30. Buka Tab System
31. Verifikasi kolom Users baris `Manage Open API` berkurang satu terhadap baseline

### TC-FA-RP-894: Switch OFF di Tab Role menyembunyikan baris Detail Role dan mencatat Remove (assignment disimpan inactive)

32. Pulihkan Budi Santoso memegang `Manage Open API` lewat seeding API hingga tersimpan, lalu catat baseline (aksi tanpa `Verifikasi`): jumlah kolom Users baris `Manage Open API` di Tab System dan jumlah entri Action `Remove` untuk Budi Santoso pada Changelog Detail Role `Manage Open API`
33. Buka Settings > User > Detail Budi Santoso > Tab Role sub-tab Global Role
34. Matikan switch `Manage Open API`
35. Tunggu aksi selesai: perubahan tersimpan
36. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage Open API`
37. Verifikasi sedikitnya satu baris pengguna lain tampil pada Detail Role `Manage Open API`
38. Verifikasi baris Budi Santoso tidak tampil di Detail Role
39. Buka Tab System dan perhatikan kolom Users
40. Verifikasi kolom Users baris `Manage Open API` berkurang satu terhadap baseline
41. Buka Detail Role `Manage Open API`, lalu klik ikon Changelog di toolbar Detail Role
42. Verifikasi entri baru Action `Remove` Field `Access` `Assigned` ke `—` tampil (selisih terhadap baseline)

### TC-FA-RP-895: Switch ON kembali memunculkan baris dan mencatat Assign

43. Catat baseline (aksi tanpa `Verifikasi`): jumlah entri Action `Assign` untuk Budi Santoso pada Changelog Detail Role `Manage Open API` (Budi Santoso memegang `Manage Open API` dengan switch dimatikan dari TC-FA-RP-894)
44. Buka Settings > User > Detail Budi Santoso > Tab Role sub-tab Global Role
45. Nyalakan switch `Manage Open API`
46. Tunggu aksi selesai: perubahan tersimpan
47. Buka Fixed Asset > Settings > Role & Permission > Tab System, lalu Detail Role `Manage Open API`
48. Verifikasi baris Budi Santoso muncul kembali di Detail Role
49. Klik ikon Changelog di toolbar Detail Role
50. Verifikasi entri baru Action `Assign` Field `Access` `—` ke `Assigned` tampil (selisih terhadap baseline)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 50 langkah.
- Urutan blok: TC-FA-RP-889 sampai 892 (aksi menambah dan mengubah), lalu TC-FA-RP-893 (Remove), TC-FA-RP-894 (switch OFF), dan TC-FA-RP-895 (switch ON); TC-FA-RP-895 memakai state akhir TC-FA-RP-894 sesuai Precondition-nya ("switch dimatikan").
- Langkah penghubung (S-03): pencatatan baseline, pembukaan Detail Role dan halaman Settings > User, "Tunggu aksi selesai", dan pemulihan lewat seeding API. Akun aktor pertama sudah login di hook `before` (S-07).
- Asersi "baris Budi Santoso tidak ada/tidak tampil di Detail Role" didahului Verifikasi baris pengguna lain pada Detail Role yang sama sebagai anchor (bagian 8b butir 2).
- Spec melewati 35 langkah dengan alasan: seluruh blok satu kelas yang sama (sinkronisasi atau efek lintas modul), tiap blok berdiri sendiri dan punya Expected sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); memecahnya menambah login, hook, dan cleanup tanpa manfaat.
- Temuan untuk QA:
  - Precondition TC-FA-RP-889, 890, dan 893 sampai 895 hanya merujuk Pre-setup #15; penugasan Budi Santoso pada `Manage Open API` (TC-FA-RP-893 sampai 895) tidak tertulis di #15; spec men-seed kondisi itu lewat seeding API.
  - TC-FA-RP-893 Expected menyebut baris Budi Santoso "tidak ada di ... kolom Users"; spec menafsirkannya sebagai kolom Users baris `Manage Open API` di Tab System berkurang satu terhadap baseline. TC-FA-RP-893 dan 895 tidak menyebut toast atau dialog sesudah aksi; tidak diasersi.
  - Post Condition TC-FA-RP-889 ("Kolom Users baris `Manage accounting` di Tab System bertambah satu") tidak punya langkah observasi di TC-FA-RP-889 sehingga tidak diasersi; kolom Users diasersi pada TC-FA-RP-893, 894, dan (spec 266) TC-FA-RP-911.
