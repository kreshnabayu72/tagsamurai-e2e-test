---
id: TC-FA-RP-E2E-085-bulk-remove-dialog-hasil-dan-cancel-1
title: "Bulk Remove: dialog, hasil, dan Cancel (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-295
  - TC-FA-RP-296
  - TC-FA-RP-297
  - TC-FA-RP-298
  - TC-FA-RP-301
coverage:
  web: automated
---

# Bulk Remove: dialog, hasil, dan Cancel (1/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`, `FA_TC2_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Sesi API aktor: login API untuk pelaku kedua dan pembacaan state lewat fixture BE mengikuti pernyataan di suite.md.
- Pelaku kedua (Sesi 2) pada TC-FA-RP-301: Total Control kedua Rina Wulandari (Pre-setup #3), `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC2_PASSWORD`, lewat sesi API (hanya memicu perubahan state, bukan konteks UI kedua).
- Data Pre-setup: pool #15 (Budi Santoso, Budi Setiawan, Dimas Pranata), #39 (Detail Role Group Role `Manage files` terisi; dirujuk TC-FA-RP-295), #3 (Rina Wulandari, Total Control), #12 (Maya Anggraeni, Read Only), dan #4 (Dewi Anggraini sebagai pembanding Tab Read Only). Penugasan Global Role `Manage Open API` per blok disiapkan lewat seed API di hook `before` dan sebagai langkah penghubung (langkah 6, 17, 23, dan 37).
- Kemampuan teknis: pembaca jumlah entri Changelog (baseline sebelum aksi, S-12) disediakan tim FE/BE.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan `Manage Open API` pool #15, tingkat akses Rina Wulandari (Total Control) dan Maya Anggraeni (Read Only)), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-295: Bulk Remove tepat satu baris memakai dialog single

1. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
2. Centang baris Budi Santoso
3. Klik `Bulk Action` > `Remove`
4. Verifikasi dialog `Remove User` (bukan `Remove Users`) tampil dengan bullet `Budi S`
5. Klik `[Cancel]`, lalu klik ikon `(✕)` pada bar untuk membatalkan seleksi

### TC-FA-RP-296: Bulk Remove N>=2 tanpa baris bertier: dialog D-06 dan hasil

6. Pulihkan state lewat seed API: Budi Santoso, Budi Setiawan, dan Dimas Pranata memegang `Manage Open API`, lalu muat ulang halaman
7. Centang baris Budi Santoso, Budi Setiawan, dan Dimas Pranata
8. Klik `Bulk Action` > `Remove`
9. Verifikasi dialog severity danger: Title `Remove Users`; bullet `Budi S`, `Budi S`, `Dimas P`; Body `The role assignments, including their permissions, will be removed permanently.` dan `Are you sure you want to remove them?`; tombol `[Cancel]` dan `[Remove]`
10. Klik `[Cancel]`
11. Verifikasi dialog tertutup tanpa perubahan: ketiga baris tetap ada
12. Verifikasi seleksi dipertahankan
13. Klik `Bulk Action` > `Remove`, klik `[Remove]`
14. Verifikasi muncul toast sukses: `Success, user has been removed.`
15. Verifikasi ketiga baris hilang
16. Verifikasi Bulk Action Bar tertutup

### TC-FA-RP-297: Bulk Remove memuat satu baris bertier: dialog D-07 dengan anotasi dan kalimat satu user

17. Pulihkan state lewat seed API: Rina Wulandari (Total Control) dan Budi Santoso memegang `Manage Open API`, lalu muat ulang halaman
18. Centang baris Rina Wulandari dan Budi Santoso
19. Klik `Bulk Action` > `Remove`
20. Verifikasi dialog Title `Remove Users`; bullet `Rina W (Total Control)` dan bullet `Budi S` (format anotasi `[User Name] ([Access Level])`, copy usulan)
21. Verifikasi Body memuat `The role assignments, including their permissions, will be removed permanently.`, lalu `Rina W will lose their access level as a result.`, ditutup `Are you sure you want to remove them?`
22. Klik `[Cancel]`, lalu klik ikon `(✕)` pada bar untuk membatalkan seleksi

### TC-FA-RP-298: Bulk Remove memuat dua baris bertier: dialog D-07 dengan kalimat banyak user

23. Pulihkan state lewat seed API: Rina Wulandari (Total Control), Maya Anggraeni (Read Only), dan Budi Santoso memegang `Manage Open API`, lalu muat ulang halaman
24. Centang baris Rina Wulandari, Maya Anggraeni, dan Budi Santoso
25. Klik `Bulk Action` > `Remove`
26. Verifikasi dialog memuat bullet `Rina W (Total Control)` dan `Maya A (Read Only)` (format anotasi `[User Name] ([Access Level])`, copy usulan)
27. Verifikasi kalimat `The users marked above will lose their access level as a result.` tampil sebelum `Are you sure you want to remove them?`
28. Klik `[Remove]`
29. Verifikasi muncul toast sukses: `Success, user has been removed.`
30. Verifikasi ketiga baris dihapus dari Detail Role `Manage Open API`
31. Klik Tab `Total Control`
32. Verifikasi baris Siti Rahmawati tampil di Tab Total Control
33. Verifikasi Rina Wulandari tidak ada di Tab Total Control (auto-revert)
34. Klik Tab `Read Only`
35. Verifikasi baris Dewi Anggraini tampil di Tab Read Only
36. Verifikasi Maya Anggraeni tidak ada di Tab Read Only (auto-revert)

### TC-FA-RP-301: Bulk Remove atas baris yang sudah dihapus admin lain dianggap sukses tanpa efek

37. Pulihkan state lewat seed API: Rina Wulandari memegang kembali tingkat akses Total Control, Maya Anggraeni kembali Read Only, dan Budi Santoso serta Budi Setiawan memegang `Manage Open API`
38. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
39. Centang baris Budi Santoso dan Budi Setiawan, klik `Bulk Action` > `Remove` hingga dialog Bulk Remove terbuka
40. Sesi 2 (sesi API Total Control Rina Wulandari) meng-Remove baris Budi Santoso pada `Manage Open API` hingga penghapusan tersimpan
41. Tunggu aksi selesai: Sesi 2 selesai sebelum berpindah ke Sesi 1; catat jumlah entri Changelog Detail Role `Manage Open API` sebagai baseline (dibaca lewat kemampuan baca FE/BE)
42. Di Sesi 1, klik `[Remove]`
43. Verifikasi muncul toast sukses: `Success, user has been removed.`
44. Verifikasi tidak muncul toast parsial `Success, user has been removed. Some items were skipped.`
45. Klik ikon Changelog di toolbar Detail Role `Manage Open API`
46. Verifikasi jumlah entri `Remove` bertambah tepat satu dibanding baseline
47. Verifikasi entri baru adalah `Remove` untuk Budi Setiawan

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-295, TC-FA-RP-296, TC-FA-RP-297, TC-FA-RP-298, TC-FA-RP-301).
- Langkah penghubung (S-03): membuka Detail Role; membatalkan dialog dan seleksi antar blok (langkah 5 dan 22, S-09); pemulihan state seed; berpindah sesi (langkah 40 sampai 42); "Tunggu aksi selesai" pada langkah 41 karena aktor berpindah sesi sesudah aksi tanpa asersi (bagian 8b butir 8).
- Asersi tambahan yang tidak ada di TC: toast sukses `Success, user has been removed.` pada langkah 29 (bentuk tunggal PRD, sama dengan TC-FA-RP-296) dipakai sebagai anchor positif untuk asersi absence baris di Detail Role dan Tab (bagian 8b butir 2); `Verifikasi` baris Siti Rahmawati dan Dewi Anggraini tampil (langkah 32 dan 35) sebagai pembanding absence tab.
- Dialog langkah 9 disebut utuh sebagai satu elemen dialog konfirmasi (S-01); pada langkah 20 dan 21 dialog TC-FA-RP-297 dipisah menjadi dua `Verifikasi` karena Expected TC memisahkan butir a (judul dan bullet) dari butir b (Body).
- Pembagian TC lintas spec: TC-FA-RP-299 dan TC-FA-RP-300 (Bulk Remove oleh Manage global user & role (Update)) ada di spec 302.
- Temuan untuk QA:
  - TC-FA-RP-295 menyebut "Pre-setup #15 tersedia" dan Budi Santoso memegang `Manage Open API`; TC-FA-RP-296 sampai TC-FA-RP-298 menyebut pemegang role serupa; keadaan awal antar blok dipulihkan oleh langkah penghubung karena Remove di blok sebelumnya mengubah state.
  - TC-FA-RP-301 baris Budi Santoso dihapus Sesi 2 dan menghasilkan entri `Remove` sendiri; baseline Changelog dicatat sesudah Sesi 2 selesai sehingga asersi "hanya satu entri bertambah" hanya menghitung aksi Sesi 1.
  - TC-FA-RP-298 Expected c menyebut Rina Wulandari dan Maya Anggraeni "hilang dari Tab Total Control dan Read Only" tanpa pembanding; spec memakai Siti Rahmawati dan Dewi Anggraini sebagai pembanding berdasarkan Pre-setup #2 dan #4.
  - Post Condition TC sumber pada TC-FA-RP-295 sampai TC-FA-RP-301 yang tidak memuat langkah observasi tidak diasersi (S-01).
- Spec ini 47 langkah, di atas smell 35 langkah. Alasan: lima blok satu kelas (fungsional) pada surface Bulk Remove yang sama; tiap blok memulihkan state seed sendiri lewat langkah penghubung sehingga berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
