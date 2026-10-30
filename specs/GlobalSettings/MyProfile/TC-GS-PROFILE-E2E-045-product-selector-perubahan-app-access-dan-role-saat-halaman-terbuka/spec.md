---
id: TC-GS-PROFILE-E2E-045-product-selector-perubahan-app-access-dan-role-saat-halaman-terbuka
title: "Product Selector: App Access Dicabut, Role Di-assign atau Dicabut, dan Role Produk Berubah saat Halaman Terbuka"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-201
  - TC-GS-PROFILE-202
  - TC-GS-PROFILE-203
  - TC-GS-PROFILE-264
  - TC-GS-PROFILE-265
  - TC-GS-PROFILE-266
coverage:
  web: automated
---

# Product Selector: App Access Dicabut, Role Di-assign atau Dicabut, dan Role Produk Berubah saat Halaman Terbuka

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Pre-setup #5 (Sinta Maharani, Total Control; App Access Global Settings, Fixed Asset, Admin Console, Supply Asset, SIEM; di Fixed Asset Global Role "Manage asset master data"; `Fixture.myProfile.accounts.multiAccess.email`, `Spectra.env.GS_PROFILE_MULTI_PASSWORD`) untuk TC-GS-PROFILE-201, 202, 203, dan 266. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (Step ganti akun): Pre-setup #4 (Budi Santoso, User Basic; 0 role individual; App Access Fixed Asset saja; `Fixture.myProfile.accounts.userBasic.email`, `Spectra.env.GS_PROFILE_BASIC_PASSWORD`) untuk TC-GS-PROFILE-264.
- Akun ketiga (Step ganti akun): Pre-setup #3 (Dewi Lestari, System Role; role individual "Manage user and role"; `Fixture.myProfile.accounts.systemRole.email`, `Spectra.env.GS_PROFILE_SYSROLE_PASSWORD`) untuk TC-GS-PROFILE-265.
- Pelaku kedua admin: Pre-setup #6 (Hendra Wijaya, Total Control; `Fixture.myProfile.accounts.admin.email`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`) mengubah App Access dan role lewat sesi API aktor (bukan sesi UI kedua); kemampuan disediakan tim BE/FE. Perubahan role Global Role Fixed Asset (TC-GS-PROFILE-266) dilakukan admin yang sama lewat sesi API aktor karena TC hanya menulis "admin Fixed Asset" (lihat Temuan untuk QA).
- State global dan pemulihan: spec mengubah (a) App Access Admin Console milik #5, (b) Global Role Fixed Asset milik #5, (c) role "Manage user and role" milik #4 dan #3. Tiap perubahan dipulihkan oleh langkah pemulihan spec segera sesudah bloknya, dan sekali lagi di hook `after` spec ini (bukan bagian Hook suite 7): App Access Admin Console #5 aktif, Global Role Fixed Asset #5 "Manage asset master data", #4 tanpa role individual, #3 dengan role "Manage user and role". Fixture pemulihan disediakan tim BE/FE.
- Jendela amat SSE 5 detik (pilihan spec, bukan nilai TC atau PRD): "Tunggu 5 detik tanpa memuat ulang halaman" sebelum asersi bahwa daftar opsi tidak berubah.
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Pelaku kedua admin (Pre-setup #6) memicu perubahan state lewat sesi API aktor yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE. Lihat `suite.md`, Hook suite 4.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-201: App Access dicabut saat halaman terbuka (Pre-setup #5)

1. Klik "Viewing: [Product ▾]" dan catat opsi
2. Tutup daftar opsi Product Selector
3. Admin Pre-setup #6 mencabut App Access Admin Console milik Pre-setup #5 lewat sesi API aktor hingga perubahan tersimpan
4. Tunggu 5 detik tanpa memuat ulang halaman
5. Buka ulang daftar opsi Product Selector tanpa memuat ulang halaman
6. Verifikasi daftar opsi masih memuat "Admin Console"
7. Muat ulang halaman My Profile (F5)
8. Buka daftar opsi Product Selector
9. Verifikasi daftar opsi memuat "Fixed Asset" dan "Global Settings"
10. Verifikasi daftar opsi tidak memuat "Admin Console"

### TC-GS-PROFILE-202 dan TC-GS-PROFILE-203: Race, produk terpilih dicabut sebelum fetch (Pre-setup #5)

11. Admin Pre-setup #6 memulihkan App Access Admin Console milik Pre-setup #5 lewat sesi API aktor hingga perubahan tersimpan
12. Muat ulang halaman My Profile (F5)
13. Admin Pre-setup #6 mencabut App Access Admin Console milik Pre-setup #5 lewat sesi API aktor hingga perubahan tersimpan
14. Pilih opsi "Admin Console" pada Product Selector
15. Verifikasi fetch ditolak 403: toast error "You don't have permission to do this."
16. Verifikasi tidak ada redirect (pengguna tetap berada di My Profile)
17. Buka daftar opsi Product Selector
18. Verifikasi daftar opsi memuat "Fixed Asset" dan "Global Settings"
19. Verifikasi daftar opsi tidak memuat "Admin Console"
20. Verifikasi Product Selector menampilkan "Viewing: Global Settings" (default)
21. Admin Pre-setup #6 memulihkan App Access Admin Console milik Pre-setup #5 lewat sesi API aktor hingga perubahan tersimpan

### TC-GS-PROFILE-266: Role produk Fixed Asset berubah (Pre-setup #5)

22. Admin Pre-setup #6 mengganti Global Role Fixed Asset milik Pre-setup #5 menjadi "Manage accounting" lewat sesi API aktor hingga perubahan tersimpan
23. Muat ulang halaman My Profile (F5)
24. Pilih opsi "Fixed Asset" pada Product Selector
25. Verifikasi daftar role konteks Fixed Asset: "Manage accounting"
26. Verifikasi daftar role tidak lagi memuat "Manage asset master data"
27. Admin Pre-setup #6 mengembalikan Global Role Fixed Asset milik Pre-setup #5 menjadi "Manage asset master data" lewat sesi API aktor hingga perubahan tersimpan

### Ganti akun ke Pre-setup #4

28. Logout
29. Login dengan `Fixture.myProfile.accounts.userBasic.email` dan `Spectra.env.GS_PROFILE_BASIC_PASSWORD`

### TC-GS-PROFILE-264: Admin meng-assign System Role (Pre-setup #4)

30. Buka Fixed Asset lalu buka My Profile dari account menu navbar
31. Admin Pre-setup #6 meng-assign role "Manage user and role" ke Pre-setup #4 lewat sesi API aktor hingga perubahan tersimpan
32. Buka Fixed Asset lalu buka My Profile dari account menu navbar
33. Verifikasi Product Selector menampilkan "Viewing: Fixed Asset" (default mengikuti app asal, S-04)
34. Pilih opsi "Global Settings" pada Product Selector
35. Verifikasi Section Access & Status konteks Global Settings menampilkan System Role "Manage user and role"
36. Verifikasi User Type "Admin"
37. Verifikasi state kosong S-10 tidak tampil
38. Admin Pre-setup #6 mencabut role "Manage user and role" dari Pre-setup #4 lewat sesi API aktor hingga perubahan tersimpan

### Ganti akun ke Pre-setup #3

39. Logout
40. Login dengan `Fixture.myProfile.accounts.systemRole.email` dan `Spectra.env.GS_PROFILE_SYSROLE_PASSWORD`
41. Buka My Profile dari account menu navbar

### TC-GS-PROFILE-265: Admin mencabut System Role (Pre-setup #3)

42. Admin Pre-setup #6 mencabut role "Manage user and role" dari Pre-setup #3 lewat sesi API aktor hingga perubahan tersimpan
43. Buka My Profile dari account menu navbar
44. Verifikasi User Type "Basic"
45. Verifikasi bagian Access Level dan System Role menampilkan state kosong "No access details yet"
46. Admin Pre-setup #6 meng-assign kembali role "Manage user and role" ke Pre-setup #3 lewat sesi API aktor hingga perubahan tersimpan

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-201, 202, 203, 264, 265, 266). Tidak ada TC hanya-BE. Pelaku kedua admin hanya memicu perubahan state lewat sesi API aktor, sehingga bukan konteks kedua kelas c dan tidak memakai `P-2`.
- Subjudul `###` memetakan langkah ke id TC. Blok per akun karena ada Step ganti akun eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah nyata butir b); semua TC satu topik (sinkronisasi perubahan App Access dan role ke Product Selector dan Section Access & Status).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 2 (menutup daftar opsi), langkah 4 (jendela amat SSE 5 detik), langkah 7, 12, 23, dan 32 (muat ulang atau buka ulang halaman agar perubahan terbaca), langkah 11, 21, 27, 38, dan 46 (pemulihan perubahan admin, bukan dari TC), langkah 28 sampai 29 dan 39 sampai 41 (Step ganti akun), langkah 30 (membuka My Profile dari Fixed Asset sesuai Precondition TC-GS-PROFILE-264 sebelum admin bertindak).
- TC-GS-PROFILE-202 dan 203 berbagi satu pemicu (produk terpilih dicabut sesaat sebelum fetch): TC-GS-PROFILE-203 langkah 1 sama dengan langkah 14, dan langkah 2 TC adalah langkah 17. Langkah 15 sampai 16 adalah Expected TC-GS-PROFILE-202 dan langkah 18 sampai 20 adalah Expected TC-GS-PROFILE-203. Langkah 18 adalah anchor positif untuk asersi absence di langkah 19; langkah 9 untuk langkah 10; langkah 35 untuk langkah 37; langkah 25 untuk langkah 26.
- Alasan spec melewati sekitar 35 langkah: seluruh blok satu topik dan satu kelas (sinkronisasi perubahan state oleh admin lewat sesi API ke Product Selector dan Section Access & Status, fungsional) dengan Step ganti akun eksplisit; tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah tambahan adalah pemulihan perubahan admin (S-09, R-08).
- Temuan untuk QA:
  - Precondition TC-GS-PROFILE-266 menyebut "admin Fixed Asset" tanpa menyebut akun Pre-setup; spec memakai admin Pre-setup #6 lewat sesi API aktor dan kemampuan mengubah Global Role Fixed Asset disediakan tim BE/FE.
  - Precondition TC-GS-PROFILE-264 dan 265 menyebut "Login sbg admin Pre-setup #6" sebagai langkah; spec memakai sesi API aktor admin (bukan login UI) karena hanya memicu perubahan state.
  - TC-GS-PROFILE-201 menandai sendiri sebagai "Manual Only (d) dua sesi paralel", tetapi hanya satu sesi UI yang diasersi; spec mengotomasi dengan admin lewat sesi API aktor.
  - TC-GS-PROFILE-202 dan 203 mensyaratkan App Access Admin Console "sudah dicabut di server setelah halaman dimuat"; spec menaruh pencabutan sesudah muat ulang halaman (langkah 12 dan 13) agar daftar opsi halaman masih memuat "Admin Console".
  - TC-GS-PROFILE-201 Expected a tidak menyebut durasi jendela observasi; spec memilih jendela amat 5 detik.
