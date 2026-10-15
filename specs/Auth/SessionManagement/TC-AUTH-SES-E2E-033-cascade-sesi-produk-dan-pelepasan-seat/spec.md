---
id: TC-AUTH-SES-E2E-033-cascade-sesi-produk-dan-pelepasan-seat
title: "Cascade Sesi Platform ke Sesi-produk dan Pelepasan Seat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-245
  - TC-AUTH-SES-246
  - TC-AUTH-SES-255
  - TC-AUTH-SES-263
  - TC-AUTH-SES-301
coverage:
  web: automated
  mobile: automated
---

# Cascade Sesi Platform ke Sesi-produk dan Pelepasan Seat

## Prerequisites

- Mode: FE+BE (TC-AUTH-SES-263 memakai intercept parsial di atas backend nyata).
- Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2; batas idle 15 menit.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan scope Client Q2 (Tabel Data Uji Pre-setup #26), kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil BASE milik Client Q2 dengan App Access Fixed Asset dan Supply Asset (user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-245: `Rina Firmansyah` (`rinafirmansyah+{runId}-033@qwertysystem.net`)
  - TC-AUTH-SES-246: `Hendra Damayanti` (`hendradamayanti+{runId}-033@qwertysystem.net`)
  - TC-AUTH-SES-255: `Intan Kusuma` (`intankusuma+{runId}-033@qwertysystem.net`)
  - TC-AUTH-SES-263: `Sari Puspita` (`saripuspita+{runId}-033@qwertysystem.net`)
  - TC-AUTH-SES-301: `Rizky Anggraini` (`rizkyanggraini+{runId}-033@qwertysystem.net`)
- Sesi dan sesi-produk per TC dibuat lewat API oleh akun aktor pada awal bagian TC itu (langkah penghubung), bukan di hook `before`, karena perangkat Android uji A (Tabel Data Uji Pre-setup #10) dipakai bergantian oleh TC-AUTH-SES-301 dan 246, kuota Client Q2 hanya 2, dan TC-AUTH-SES-245 memajukan jam server: sesi platform web Active di Browser A (Chrome on Windows, konteks browser terpisah per TC) melalui login API pada konteks itu; sesi mobile Active di perangkat Android uji A (login nyata dengan email dan password user, ketuk [Not now] pada Prompt Enable Biometric; Tabel Data Uji Pre-setup #28; data aplikasi akun sebelumnya dibersihkan); sesi-produk Fixed Asset Active (seat terpakai).
- Konteks browser (hook `before`): Browser License login oleh akun aktor `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Global Role Manage Global License di Client Q2, Tabel Data Uji Pre-setup #2, kredensial `Spectra.env.FA_MGL_PASSWORD`); Browser Admin login oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26); Browser B untuk TC-AUTH-SES-255 adalah konteks baru yang belum login (Firefox on macOS).
- Hook `after`: kembalikan jam server uji dan jam browser/perangkat ke waktu nyata dan matikan failure injection; akhiri semua sesi dan sesi-produk seed (web, mobile); bersihkan data aplikasi mobile di perangkat Android uji A; tutup semua konteks browser; hapus kelima user. Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: seat Fixed Asset Client Q2 (diambil dan dilepas oleh TC), jam server uji dan jam browser/perangkat (TC-AUTH-SES-245, diatur bersama; TC ini paling akhir karena sesi seluruh konteks lain ikut Expired), failure injection 5xx pada request End Product (TC-AUTH-SES-263), dipulihkan di hook `after`.
- Jeda nyata: 10 detik tanpa interaksi di Browser A untuk pengamatan event push SSE (langkah 24, mengikuti TC-AUTH-SES-26 langkah 3); tidak ada jeda nyata lain, pemajuan waktu memakai jam server dan jam browser/perangkat bersama.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: konteks browser bersamaan (Browser A, Browser B, Browser License, Browser Admin); satu perangkat Android uji A dengan aplikasi mobile terpasang dan dapat diketuk oleh driver otomasi; login nyata di perangkat Android uji A (Prompt Enable Biometric: ketuk [Not now]); user agent yang dapat ditetapkan (Chrome on Windows, Firefox on macOS); event push SSE yang teramati di Browser A; jam server uji dan jam browser/perangkat yang diatur bersama (dimajukan dengan presisi menit dan dipulihkan ke waktu nyata; Tabel Data Uji Pre-setup #18; kelas harness d: time-travel); reCAPTCHA mode uji di environment (halaman Login with Password, TC-AUTH-SES-255); failure injection 5xx pada request End Product (`POST /v2/iam/auth/product-sessions/{id}/end`) lewat `Spectra.intercept()`, dinyalakan dan dimatikan oleh langkah; pembacaan status sesi platform, status sesi-produk, dan hitungan seat dari BE oleh akun aktor.
- Akun yang dipakai: user uji masing-masing TC pada Browser A, Browser B, dan perangkat Android uji A; akun aktor Manage Global License pada Browser License; akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) pada Browser Admin.

## Test Steps

### TC-AUTH-SES-301: Force-logout produk X tidak mengakhiri sesi platform yang tidak memakai sesi-produk X

1. Siapkan: sesi web Active milik `Rizky Anggraini` di Browser A (Chrome on Windows), sesi mobile Active di perangkat Android uji A lewat login nyata (tidak membuka Fixed Asset), dan sesi-produk Fixed Asset Active milik `Rizky Anggraini` yang hanya dipakai sesi web
2. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) → halaman Concurrent User Fixed Asset tampil
3. Pilih `Rizky Anggraini` (`rizkyanggraini+{runId}-033@qwertysystem.net`), lalu klik [Force Logout] → dialog konfirmasi "Force Logout User" tampil
4. Klik [Confirm Logout] pada dialog konfirmasi "Force Logout User" → force logout selesai
5. Di perangkat Android uji A ketuk layar
6. Verifikasi Sesi web `Rizky Anggraini` berstatus Force Logged Out
7. Verifikasi Sesi-produk Fixed Asset `Rizky Anggraini` berakhir
8. Verifikasi Sesi mobile `Rizky Anggraini` tetap Active
9. Verifikasi Perangkat Android uji A tidak menampilkan dialog

### TC-AUTH-SES-246: Sesi-produk bersama web dan mobile tetap Active selama salah satu sesi platform masih Active

10. Siapkan: sesi web Active milik `Hendra Damayanti` di Browser A, sesi mobile Active di perangkat Android uji A lewat login nyata (data aplikasi akun sebelumnya dibersihkan), dan satu sesi-produk Fixed Asset Active yang dipakai sesi web dan sesi mobile (seat terpakai 1)
11. Di Browser A klik menu Profile lalu pilih Log Out → Browser A keluar dari sesi web
12. Periksa sesi-produk dan seat Fixed Asset `Hendra Damayanti`
13. Verifikasi Sesi-produk Fixed Asset tetap Active setelah logout web
14. Verifikasi Seat tetap terpakai karena sesi mobile masih Active
15. Di perangkat Android uji A klik menu Profile lalu pilih Log Out → aplikasi mobile keluar dari sesi mobile
16. Periksa sesi-produk dan seat Fixed Asset `Hendra Damayanti`
17. Verifikasi Sesi-produk Fixed Asset berstatus Ended setelah logout mobile
18. Verifikasi Seat dilepas setelah logout mobile

### TC-AUTH-SES-255: Confirm pada Dialog Duplicate Login Attempt mengakhiri sesi-produk anak dari sesi lama

19. Siapkan lewat API: sesi web Active milik `Intan Kusuma` di Browser A (Chrome on Windows) dengan sesi-produk Fixed Asset Active (seat terpakai); Browser B belum login; catat penanda waktu dasar Activity Log sebelum login di Browser B
20. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) → halaman Concurrent User Fixed Asset tampil
21. Catat hitungan seat aktif Fixed Asset Client Q2
22. Di Browser B (Firefox on macOS) buka `Auth > Login with Password`, ketik email `intankusuma+{runId}-033@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog Duplicate Login Attempt muncul
23. Klik [Confirm]
24. Pindah ke Browser A dan amati tanpa interaksi selama 10 detik (event push SSE)
25. Verifikasi Sesi web lama `Intan Kusuma` berstatus Force Logged Out
26. Periksa sesi-produk Fixed Asset dan seat Client Q2
27. Verifikasi Sesi-produk Fixed Asset anak berstatus Ended
28. Verifikasi Seat dilepas
29. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan `Global Settings > User > Detail > User Log` milik `Intan Kusuma` → halaman log tampil
30. Verifikasi Entri `Session ended` untuk sesi-produk anak `Intan Kusuma` tercatat di `Activity Log > Session` milik Fixed Asset (di User Log tampil `Session ended (Fixed Asset)`) dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)
31. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
32. Verifikasi Baris `Intan Kusuma` hilang dari daftar sesi aktif
33. Verifikasi Hitungan seat aktif berkurang 1 dari hitungan yang dicatat pada langkah 21

### TC-AUTH-SES-263: End Product bersifat idempotent dan gagal diam-diam tanpa toast

34. Siapkan lewat API: sesi web Active milik `Sari Puspita` (`saripuspita+{runId}-033@qwertysystem.net`) di Browser A dan sesi-produk Fixed Asset Active milik `Sari Puspita` (seat terpakai); Browser A berada di dashboard Fixed Asset
35. Aktifkan failure injection 5xx pada request End Product → request End Product dijawab 500
36. Di Browser A klik App Switcher di header Fixed Asset saat failure injection aktif
37. Verifikasi Kegagalan pertama tidak menampilkan toast
38. Verifikasi Aksi dapat diulang (App Switcher di header tetap tersedia dan sesi-produk Fixed Asset belum berakhir)
39. Nonaktifkan failure injection → request End Product kembali normal
40. Di Browser A klik App Switcher lagi
41. Verifikasi Sesi-produk Fixed Asset `Sari Puspita` berstatus Ended
42. Verifikasi Seat dilepas
43. Di Browser A klik App Switcher sekali lagi pada sesi-produk yang sudah Ended
44. Verifikasi Panggilan pada sesi-produk yang sudah Ended tidak berefek (status sesi-produk tetap Ended)
45. Verifikasi Panggilan pada sesi-produk yang sudah Ended tidak berefek (hitungan seat tidak berubah)

### TC-AUTH-SES-245: Sesi platform expired karena idle mengakhiri sesi-produk anak dan melepas seat

46. Siapkan lewat API: sesi platform web Active milik `Rina Firmansyah` dan sesi-produk Fixed Asset Active milik `Rina Firmansyah` di Browser A (seat terpakai 1); batas idle 15 menit; catat penanda waktu dasar Activity Log (waktu server) sebelum jam dimajukan
47. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) → halaman Concurrent User Fixed Asset tampil
48. Catat hitungan seat aktif Fixed Asset Client Q2
49. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat bersama 16 menit
50. Periksa status sesi-produk dan seat Client Q2
51. Verifikasi Sesi platform `Rina Firmansyah` berstatus Expired
52. Verifikasi Sesi-produk Fixed Asset berstatus Ended
53. Verifikasi Seat dilepas
54. Pulihkan jam server uji dan jam browser/perangkat ke waktu nyata
55. Di Browser Admin login ulang sebagai `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.GS_TC_PASSWORD` (sesi sebelumnya Expired akibat jam server dimajukan) → beranda akun Total Control Global Settings tampil
56. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Activity Log > Session` milik Fixed Asset → halaman log tampil
57. Verifikasi Entri `Session expired` untuk sesi platform `Rina Firmansyah` tercatat di `Global Settings > Activity Log > Session` dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)
58. Verifikasi Entri `Session ended` untuk sesi-produk anak `Rina Firmansyah` tercatat di `Activity Log > Session` milik Fixed Asset dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)
59. Di Browser License login ulang sebagai `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_MGL_PASSWORD` (sesi sebelumnya Expired akibat jam server dimajukan) → beranda akun Manage Global License tampil
60. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) → halaman Concurrent User Fixed Asset tampil
61. Verifikasi Baris `Rina Firmansyah` hilang dari daftar sesi aktif
62. Verifikasi Hitungan seat aktif berkurang 1 dari hitungan yang dicatat pada langkah 48

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-301, 246, 255, 263, 245 (urutan TC sumber 245, 246, 255, 263, 301). TC-AUTH-SES-245 dipindah paling akhir karena memajukan jam server 16 menit sehingga sesi konteks lain ikut Expired; TC-AUTH-SES-301 dan 255 (force-logout dan Duplicate Confirm) mengakhiri sesi milik user TC itu sendiri dan tidak memengaruhi TC lain. Tiap TC memakai user sendiri dan menyiapkan kondisinya di awal bagiannya sehingga tidak saling bergantung (S-06). Alasan ukuran: lima TC berdiri sendiri dengan user sendiri; TC-AUTH-SES-245 memajukan jam hanya sebagai pemicu (objek ujinya cascade sesi), sehingga ditaruh paling akhir dan tidak dipisah.
- Dependensi disalin sebagai langkah (S-04): TC-AUTH-SES-255 berdependensi pada TC-AUTH-SES-26 (langkah 22 sampai 24 menyalin login di Browser B, Confirm, dan pengamatan 10 detik di Browser A); TC-AUTH-SES-263 berdependensi pada TC-AUTH-SES-132 (langkah 40 menyalin klik App Switcher; pemeriksaan sesi-produk dan seat pada TC itu dilakukan langkah 41 dan 42 lewat pembacaan BE sesuai langkah TC-AUTH-SES-263 sendiri; langkah observasi TC-AUTH-SES-132 berupa daftar License > Concurrent User dan User Log milik TC itu dan diasersi di spec 041).
- Pengecualian konvensi: TC-AUTH-SES-263 adalah objek uji ringan kelas b (satu kegagalan 5xx pada End Product tanpa harness eksternal dan tanpa state berat sendiri) dan berada di spec ini menurut P-5 butir b (paling banyak dua TC objek uji ringan per spec; spec ini memuat satu). Browser B pada TC-AUTH-SES-255 adalah konteks kedua yang hanya memicu Dialog Duplicate Login Attempt (kondisi yang diuji dibaca dari sesi lama di Browser A, sesi-produk anak, seat, dan log); pemakaian ini menurut P-2 sebagai pemicu, bukan objek asersi lintas-konteks.
- Pencatatan: asersi `Session ended` pada TC-AUTH-SES-255 mengikuti rujukan ke TC-AUTH-SES-201 untuk lokasi log; asersi `Session expired` dan `Session ended` pada TC-AUTH-SES-245 memakai lokasi log GS Session dan Session Fixed Asset. Asersi "tidak mencatat `Session ended` kedua" pada Expected TC-AUTH-SES-263 (butir c) tidak ditulis di spec ini; dirujuk ke spec absence `TC-AUTH-SES-E2E-067-absence-sesi-produk-dan-concurrent` (S-05).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menyiapkan sesi dan sesi-produk lewat API; mencatat hitungan seat; memeriksa status sesi-produk dan seat; membuka halaman log; mencatat penanda waktu dasar log; memulihkan jam server dan jam browser/perangkat ke waktu nyata sebelum akun aktor membuka log (langkah 54); mengetuk layar; login ulang akun aktor setelah jam server dimajukan (langkah 55 dan 59).
- Temuan untuk QA: (1) TC-AUTH-SES-246, 245, dan 301 menulis "periksa sesi-produk dan seat" tanpa menyebut permukaan; spec membaca status sesi dan sesi-produk dari BE oleh akun aktor, dan License > Concurrent User hanya bila TC menyebutnya. (2) TC-AUTH-SES-263 tidak menjelaskan apakah Browser A tetap berada di header Fixed Asset (App Switcher tersedia) setelah End Product gagal dan setelah berhasil; spec mengikuti TC dan mengandalkan header Fixed Asset tetap ada pada klik kedua dan ketiga. Kegagalan 5xx dipicu lewat intercept pada endpoint End Product yang tercantum di `openapi.yaml`. (3) TC-AUTH-SES-255 mengetik email dan password lalu login tanpa menyebut label tombol dan widget reCAPTCHA; spec memakai label `[Log in]` mengikuti PRD Login with Password dan mengandalkan reCAPTCHA mode uji (TC-AUTH-SES-26 juga tidak menyebut widget itu). (4) TC-AUTH-SES-301 tidak menyebut Dialog "Log Out" pada web (PRD menyebutnya); spec hanya mengasersi status dan hasil sesi mobile sesuai Expected TC. (5) TC-AUTH-SES-245 butir c menyebut dua entri log tanpa lokasi di luar rujukan TC-AUTH-SES-201; spec memakai GS Session untuk `Session expired` dan Session Fixed Asset untuk `Session ended`. (6) Akun #2 `manageGlobalLicenseFixedAsset` pada Tabel Data Uji Pre-setup tidak menyebut Client cakupannya; spec mengasumsikan scope Client Q2.
