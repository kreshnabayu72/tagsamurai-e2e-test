---
id: TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile
title: "Sesi-produk Bersama Web dan Mobile"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-104
  - TC-AUTH-SES-137
  - TC-AUTH-SES-144
  - TC-AUTH-SES-271
  - TC-AUTH-SES-272
  - TC-AUTH-SES-273
  - TC-AUTH-SES-300
coverage:
  web: automated
  mobile: automated
---

# Sesi-produk Bersama Web dan Mobile

## Prerequisites

- Mode: FE+BE.
- Kelas harness c (multi-konteks: web dan mobile pada user yang sama, Open Product paralel). Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2; batas idle 15 menit. Client Alpha `Alpha Logistik` (Tabel Data Uji Pre-setup #5) hanya dipakai TC-AUTH-SES-144 (batas idle 15 menit).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan scope Client Q2 (Tabel Data Uji Pre-setup #26), kredensial `Spectra.env.GS_TC_PASSWORD`): tujuh user profil BASE milik Client Q2 dengan App Access Fixed Asset dan Supply Asset serta satu user profil BASE milik Client Alpha (user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run; user Client Alpha di-seed lewat API oleh akun aktor Total Control (Global Settings) Client Alpha `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1, kredensial `Spectra.env.GS_TC_PASSWORD`):
  - Seed seat (TC-AUTH-SES-300): `Gunawan Prakoso` (`gunawanprakoso+{runId}-034@qwertysystem.net`)
  - TC-AUTH-SES-104: `Eko Rahayu` (`ekorahayu+{runId}-034@qwertysystem.net`)
  - TC-AUTH-SES-271: `Dewi Santoso` (`dewisantoso+{runId}-034@qwertysystem.net`)
  - TC-AUTH-SES-272: `Rizky Kusuma` (`rizkykusuma+{runId}-034@qwertysystem.net`)
  - TC-AUTH-SES-273: `Nur Permata` (`nurpermata+{runId}-034@qwertysystem.net`)
  - TC-AUTH-SES-300: `Dewi Rahayu` (`dewirahayu+{runId}-034@qwertysystem.net`)
  - TC-AUTH-SES-137: `Citra Firmansyah` (`citrafirmansyah+{runId}-034@qwertysystem.net`)
  - TC-AUTH-SES-144: `Galih Wijaya` (`galihwijaya+{runId}-034@qwertysystem.net`), Client Alpha
- Sesi dan sesi-produk per TC dibuat lewat API oleh akun aktor pada awal bagian TC itu (langkah penghubung), bukan di hook `before`, karena perangkat Android uji A (Tabel Data Uji Pre-setup #10) dipakai bergantian oleh ketujuh TC, kuota Client Q2 hanya 2, dan TC-AUTH-SES-271 memajukan jam server: sesi web Active di Browser A (Chrome on Windows, konteks browser terpisah per TC) melalui login API pada konteks itu; sesi mobile Active di perangkat Android uji A (login nyata dengan email dan password user, ketuk [Not now] pada Prompt Enable Biometric; Tabel Data Uji Pre-setup #28; data aplikasi akun sebelumnya dibersihkan); sesi-produk Fixed Asset Active (seat terpakai), sebelumnya semua sesi-produk aktif Client Q2 diakhiri lewat API; TC-AUTH-SES-144 hanya memakai sesi web dan sesi mobile tanpa sesi-produk, dan TC-AUTH-SES-137 membentuk satu sesi-produk Fixed Asset dengan membuka Fixed Asset di web lalu di mobile.
- Konteks browser (hook `before`): Browser License login oleh akun aktor `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Global Role Manage Global License di Client Q2, Tabel Data Uji Pre-setup #2, kredensial `Spectra.env.FA_MGL_PASSWORD`); Browser B untuk TC-AUTH-SES-272 adalah konteks baru yang belum login (Firefox on macOS).
- Hook `after`: kembalikan jam server uji dan jam browser/perangkat ke waktu nyata; akhiri semua sesi dan sesi-produk seed (web, mobile); bersihkan data aplikasi mobile di perangkat Android uji A; tutup semua konteks browser; hapus kedelapan user (password `Nur Permata` yang diubah TC-AUTH-SES-273 ikut terhapus bersama user). Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`), juga karena satu perangkat Android uji A dipakai bersama oleh ketujuh TC; state global yang diubah: seat Fixed Asset Client Q2, password `Nur Permata` (TC-AUTH-SES-273, menjadi `Spectra.env.SES_PASSWORD_NEW`), jam server uji dan jam browser/perangkat (TC-AUTH-SES-271, diatur bersama; TC ini paling akhir karena sesi seluruh konteks lain ikut Expired), dipulihkan di hook `after`.
- Jeda nyata: 10 detik untuk menunggu event push SSE (langkah 14 dan 16); tidak ada jeda nyata lain, pemajuan jam pada TC-AUTH-SES-271 tidak menunggu waktu nyata.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`, `SES_PASSWORD_NEW`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: konteks browser bersamaan (Browser A, Browser B, Browser License); satu perangkat Android uji A dengan aplikasi mobile terpasang dan dapat diketuk serta digerakkan layarnya oleh driver otomasi; login nyata di perangkat Android uji A (Prompt Enable Biometric: ketuk [Not now]); pemicu dua aksi pada saat yang sama (klik card Fixed Asset di Browser A dan di aplikasi mobile, TC-AUTH-SES-300); user agent Firefox on macOS (Browser B); jam server uji dan jam browser/perangkat yang diatur bersama (dimajukan dengan presisi menit dan dipulihkan ke waktu nyata; Tabel Data Uji Pre-setup #18; kelas harness d: time-travel); penerimaan push SSE dan pengamatan dialog Log Out di Browser A dan di aplikasi mobile tanpa interaksi (TC-AUTH-SES-137, TC-AUTH-SES-144); pembacaan ID sesi-produk, status sesi platform, status sesi-produk, dan hitungan seat dari BE oleh akun aktor, disediakan tim FE/BE tanpa endpoint tertentu; reCAPTCHA mode uji di environment (halaman Login with Password, TC-AUTH-SES-272).
- Akun yang dipakai: user uji masing-masing TC pada Browser A, Browser B, dan perangkat Android uji A; akun aktor Manage Global License pada Browser License (juga untuk Force Logout, TC-AUTH-SES-137).

## Test Steps

### TC-AUTH-SES-104: Produk dibuka dari web dan mobile memakai satu sesi-produk dan satu seat

1. Siapkan: akhiri semua sesi-produk aktif Client Q2; sesi web Active milik `Eko Rahayu` di Browser A (Chrome on Windows), sesi mobile Active di perangkat Android uji A lewat login nyata (data aplikasi akun sebelumnya dibersihkan), dan sesi-produk Fixed Asset Active milik `Eko Rahayu` yang dibuat dari web (seat terpakai 1)
2. Di perangkat Android uji A buka aplikasi mobile dan buka card Fixed Asset → Fixed Asset terbuka
3. Verifikasi Aplikasi mobile masuk Fixed Asset
4. Verifikasi Tidak ada popup yang tampil di aplikasi mobile
5. Verifikasi Tetap satu sesi-produk Fixed Asset untuk `Eko Rahayu`
6. Verifikasi Tetap satu seat untuk `Eko Rahayu`

### TC-AUTH-SES-137: Force-logout mengakhiri sesi platform web dan mobile yang memakai sesi-produk yang sama

7. Siapkan: akhiri semua sesi-produk aktif Client Q2; sesi web Active milik `Citra Firmansyah` di Browser A (Chrome on Windows), sesi mobile Active di perangkat Android uji A lewat login nyata (data aplikasi akun sebelumnya dibersihkan), dan satu sesi-produk Fixed Asset Active yang dibentuk dengan membuka Fixed Asset di web lalu di mobile sehingga dipakai sesi web dan sesi mobile (seat terpakai 1); aplikasi mobile terbuka
8. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), catat hitungan seat aktif dan baris `Citra Firmansyah` (`citrafirmansyah+{runId}-034@qwertysystem.net`) → halaman Concurrent User Fixed Asset tampil
9. Pilih baris `Citra Firmansyah`
10. Klik [Force Logout] → dialog konfirmasi "Force Logout User" muncul
11. Klik [Confirm Logout]
12. Verifikasi Sesi platform web `Citra Firmansyah` berstatus Force Logged Out
13. Verifikasi Sesi platform mobile `Citra Firmansyah` berstatus Force Logged Out
14. Di Browser A (sesi `Citra Firmansyah`) amati tanpa interaksi selama 10 detik (event push SSE)
15. Verifikasi Dialog "Log Out" tampil di web (Browser A)
16. Di perangkat Android uji A amati layar aplikasi tanpa interaksi selama 10 detik
17. Verifikasi Dialog "Log Out" tampil di mobile (perangkat Android uji A)
18. Verifikasi Sesi-produk Fixed Asset `Citra Firmansyah` berstatus Force Logged Out
19. Verifikasi Seat dilepas (hitungan seat aktif berkurang 1 dari hitungan yang dicatat pada langkah 8)

### TC-AUTH-SES-144: Manual Logout di web tidak memengaruhi sesi mobile

20. Siapkan: sesi web Active milik `Galih Wijaya` di Browser A (Chrome on Windows) dan sesi mobile Active di perangkat Android uji A lewat login nyata (data aplikasi akun sebelumnya dibersihkan), aplikasi mobile terbuka
21. Di Browser A (sesi `Galih Wijaya`) klik menu Profile di navbar lalu pilih Log Out
22. Verifikasi Sesi web `Galih Wijaya` berstatus Logged Out
23. Di perangkat Android uji A ketuk layar
24. Verifikasi Sesi mobile `Galih Wijaya` tetap Active
25. Verifikasi Tidak ada dialog yang tampil di perangkat Android uji A

### TC-AUTH-SES-272: Duplicate Confirm yang mengakhiri sesi web saat sesi mobile masih Active: sesi-produk tetap Active

26. Siapkan: akhiri semua sesi-produk aktif Client Q2; sesi web Active milik `Rizky Kusuma` di Browser A (Chrome on Windows), sesi mobile Active di perangkat Android uji A lewat login nyata (data aplikasi akun sebelumnya dibersihkan), dan satu sesi-produk Fixed Asset Active yang dipakai sesi web dan sesi mobile (seat terpakai 1); Browser B belum login
27. Di Browser B (Firefox on macOS) buka `Auth > Login with Password`, ketik email `rizkykusuma+{runId}-034@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog Duplicate Login Attempt muncul
28. Klik [Confirm]
29. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan periksa baris `Rizky Kusuma` (`rizkykusuma+{runId}-034@qwertysystem.net`) dan hitungan seat → halaman Concurrent User Fixed Asset tampil
30. Verifikasi Sesi web lama `Rizky Kusuma` berstatus Force Logged Out
31. Verifikasi Sesi mobile `Rizky Kusuma` tetap Active
32. Verifikasi Sesi-produk Fixed Asset tetap Active
33. Verifikasi Seat tetap terpakai karena sesi mobile masih memakainya (baris `Rizky Kusuma` masih ada pada daftar)

### TC-AUTH-SES-273: Change Password dari sesi web: sesi mobile di-invalidate tetapi sesi-produk tetap Active selama sesi web Active

34. Siapkan: akhiri semua sesi-produk aktif Client Q2; sesi web Active milik `Nur Permata` di Browser A (Chrome on Windows), sesi mobile Active di perangkat Android uji A lewat login nyata (data aplikasi akun sebelumnya dibersihkan), dan satu sesi-produk Fixed Asset Active yang dipakai sesi web dan sesi mobile (seat terpakai 1)
35. Di Browser A buka `Global Settings > My Profile > Change Password`, sebagai `nurpermata+{runId}-034@qwertysystem.net` → modal Change Password tampil
36. Isi Current Password dengan password lama yang benar `Spectra.env.SES_PASSWORD`, serta New Password dan Confirm New Password dengan password baru yang valid sesuai kebijakan password `Spectra.env.SES_PASSWORD_NEW`
37. Klik [Save] → password berhasil diubah
38. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan periksa baris `Nur Permata` (`nurpermata+{runId}-034@qwertysystem.net`) dan hitungan seat → halaman Concurrent User Fixed Asset tampil
39. Verifikasi Sesi mobile `Nur Permata` berstatus Force Logged Out
40. Verifikasi Sesi web `Nur Permata` (sesi pemicu) tetap Active
41. Verifikasi Sesi-produk Fixed Asset tetap Active
42. Verifikasi Seat tetap terpakai karena sesi web masih memakainya (baris `Nur Permata` masih ada pada daftar)

### TC-AUTH-SES-300: Open Product paralel oleh user yang sama dari web dan mobile saat tersisa satu seat memakai satu seat

43. Siapkan: akhiri semua sesi-produk aktif Client Q2, lalu buat satu sesi-produk Fixed Asset Active milik `Gunawan Prakoso` (kuota 2, seat terpakai 1); sesi platform web Active milik `Dewi Rahayu` di Browser A di Portal — Product Hub dan sesi mobile Active di perangkat Android uji A lewat login nyata di Portal — Product Hub
44. Klik card Fixed Asset di Browser A dan di aplikasi mobile pada saat yang sama → kedua perangkat membuka Fixed Asset
45. Verifikasi Browser A masuk Fixed Asset
46. Verifikasi Tidak ada popup yang tampil di Browser A
47. Verifikasi Aplikasi mobile masuk Fixed Asset
48. Verifikasi Tidak ada popup yang tampil di aplikasi mobile
49. Verifikasi Keduanya memakai satu sesi-produk Fixed Asset milik `Dewi Rahayu` (ID sesi-produk sama)
50. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) → halaman Concurrent User Fixed Asset tampil
51. Verifikasi Seat aktif menjadi 2 (bukan 3)

### TC-AUTH-SES-271: Sesi web expired karena idle saat sesi mobile masih Active: sesi-produk tetap Active

52. Siapkan: akhiri semua sesi-produk aktif Client Q2; sesi web Active milik `Dewi Santoso` di Browser A (Chrome on Windows), sesi mobile Active di perangkat Android uji A lewat login nyata (data aplikasi akun sebelumnya dibersihkan), dan satu sesi-produk Fixed Asset Active yang dipakai sesi web dan sesi mobile (seat terpakai 1); batas idle 15 menit
53. Gerakkan layar aplikasi mobile di perangkat Android uji A secara berkala sambil memajukan jam server uji dan jam browser/perangkat bersama 16 menit tanpa aktivitas di Browser A
54. Di Browser License login ulang sebagai `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_MGL_PASSWORD` (sesi sebelumnya Expired akibat jam server dimajukan) → beranda akun Manage Global License tampil
55. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan periksa baris `Dewi Santoso` (`dewisantoso+{runId}-034@qwertysystem.net`) dan hitungan seat → halaman Concurrent User Fixed Asset tampil
56. Verifikasi Sesi web `Dewi Santoso` berstatus Expired
57. Verifikasi Sesi mobile `Dewi Santoso` tetap Active
58. Verifikasi Sesi-produk Fixed Asset tetap Active
59. Verifikasi Seat tetap terpakai (baris `Dewi Santoso` masih ada pada daftar)
60. Majukan jam server uji dan jam browser/perangkat bersama 16 menit lagi tanpa aktivitas di aplikasi mobile sehingga sesi mobile juga berakhir
61. Verifikasi Sesi mobile `Dewi Santoso` berakhir
62. Verifikasi Sesi-produk Fixed Asset berstatus Ended
63. Verifikasi Seat dilepas
64. Pulihkan jam server uji dan jam browser/perangkat ke waktu nyata

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness c (multi-konteks); TC-AUTH-SES-271 juga memakai time-travel (kelas d) dan diletakkan paling akhir. TC-AUTH-SES-137 dan TC-AUTH-SES-144 ada di spec ini karena sesi mobile di perangkat Android uji A menjadi objek asersi di samping sesi web (kelas c); spec `TC-AUTH-SES-E2E-042-admin-force-logout-license-concurrent-user` dan `TC-AUTH-SES-E2E-043-manual-logout` tidak memuat keduanya. Alasan ukuran: ketujuh TC berbagi satu perangkat Android uji A dan satu aktor License, tiap TC berdiri sendiri dengan user sendiri, dan jam dimajukan hanya sebagai pemicu idle (objek ujinya sesi-produk bersama), sehingga TC-AUTH-SES-271 ditaruh paling akhir dan tidak dipisah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-104, 137, 144, 272, 273, 300, 271 (urutan TC sumber 104, 137, 144, 271, 272, 273, 300). Hanya TC-AUTH-SES-271 yang dipindah, ke paling akhir, karena memajukan jam server 16 menit dua kali sehingga sesi konteks lain ikut Expired. Tiap TC memakai user sendiri dan menyiapkan kondisinya di awal bagiannya sehingga tidak saling bergantung (S-06).
- Pencatatan: asersi "tidak ada entri `Session started` kedua" pada Expected TC-AUTH-SES-104 (butir c) tidak ditulis di spec ini; dirujuk ke spec absence `TC-AUTH-SES-E2E-067-absence-sesi-produk-dan-concurrent` (S-05).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menyiapkan sesi dan sesi-produk lewat API (langkah 1, 7, 20, 26, 34, 43, 52); membuka card Fixed Asset di aplikasi mobile atau di Browser A dan aplikasi mobile bersamaan (langkah 2 dan 44); membuka halaman Concurrent User di Browser License (langkah 8, 29, 38, 46, 55); memilih baris dan membuka serta mengonfirmasi dialog Force Logout (langkah 9 s.d. 11); mengamati Browser A dan perangkat Android uji A tanpa interaksi (langkah 14 dan 16); mengklik menu Profile lalu Log Out di Browser A (langkah 21); mengetuk layar aplikasi mobile (langkah 23); login Browser B, [Confirm] pada Dialog Duplicate Login Attempt (langkah 27 dan 28); membuka modal Change Password, mengisi password, dan mengklik [Save] (langkah 35 s.d. 37); login ulang akun aktor setelah jam server dimajukan (langkah 54); langkah 53 dan 60 memajukan jam, dengan langkah 60 sebagai pemajuan kedua agar butir c TC-AUTH-SES-271 ("setelah sesi mobile juga berakhir") dapat diasersi; langkah 64 memulihkan jam server uji dan jam browser/perangkat sebelum spec selesai (hook `after` sebagai cadangan).
- Temuan untuk QA: (1) TC-AUTH-SES-273 menulis "dengan data valid" tanpa nilai, tanpa nama field, dan tanpa label tombol simpan; spec memakai `Spectra.env.SES_PASSWORD` dan `Spectra.env.SES_PASSWORD_NEW` untuk field Current Password, New Password, dan Confirm New Password, serta `[Save]` pada modal Change Password mengikuti PRD My Profile dan konvensi bagian 9. (2) TC-AUTH-SES-271 butir c menyebut "setelah sesi mobile juga berakhir" tanpa langkah pemicunya; spec menambah pemajuan jam server (langkah 60) dan mengasumsikan batas idle mobile sama dengan batas idle web (15 menit). (3) TC-AUTH-SES-300 menulis "pada saat yang sama" tanpa menyebut cara mensinkronkan dua perangkat; spec mengandalkan pemicu paralel dari driver. (4) TC-AUTH-SES-104, 137, 144, 271, 272, 273, dan 300 tidak menyebut permukaan baca status sesi dan sesi-produk selain License > Concurrent User; spec membacanya dari BE oleh akun aktor. (5) TC-AUTH-SES-272 mengetik email dan password lalu login tanpa menyebut label tombol dan widget reCAPTCHA; spec memakai label `[Log in]` mengikuti PRD Login with Password dan mengandalkan reCAPTCHA mode uji. (6) Akun #2 `manageGlobalLicenseFixedAsset` pada Tabel Data Uji Pre-setup tidak menyebut Client cakupannya; spec mengasumsikan scope Client Q2. (7) TC-AUTH-SES-137 Expected butir b tidak menyebut Body Dialog Log Out di mobile; spec hanya mengasersikan dialog tampil. (8) TC-AUTH-SES-137 Precondition d tidak menyebut cara membentuk satu sesi-produk yang dipakai sesi web dan sesi mobile; spec membukanya di web lalu di mobile. (9) TC-AUTH-SES-137 Langkah 1 hanya menyebut "force-logout"; spec memakai [Force Logout] dan [Confirm Logout] serta dialog "Force Logout User" mengikuti `fixed-asset/license/PRD/license.md` §3.2. (10) TC-AUTH-SES-144 menulis tombol Log Out sebagai menu Profile di navbar tanpa label tombol dan "ketuk layar" tanpa menyebut layar aplikasi mobile; spec mengikuti TC dan mengandalkan aplikasi mobile terbuka. (11) TC-AUTH-SES-144 Precondition a menyebut Client Alpha (Tabel Data Uji Pre-setup #5), berbeda dari Client Q2 pada TC lain di spec ini; spec mengikuti TC dan men-seed `Galih Wijaya` di Client Alpha. (12) TC-AUTH-SES-273 Langkah 1 tidak menyebut cara Browser A, yang sedang berada di Fixed Asset, membuka `Global Settings > My Profile`; jalur lewat App Switcher mengakhiri sesi-produk sehingga Expected b ("sesi-produk tetap Active") tidak terpenuhi. Langkah 35 menuliskan halaman tujuan persis seperti TC tanpa jalur; jalur navigasi yang tidak melewati App Switcher perlu ditulis di TC.
- Jumlah langkah (64) melewati sekitar 35 karena tujuh TC multi-konteks, masing-masing dengan user dan sesi sendiri sehingga bagian sesudahnya tetap bermakna walau bagian di atasnya gagal; tiap TC menyiapkan kondisinya di awal bagiannya.
