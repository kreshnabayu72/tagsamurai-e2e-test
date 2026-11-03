---
id: TC-FA-SU-E2E-357-multi-konteks-sesi-target-terputus-saat-deactivate-login-pengguna-nonaktif-sesi-lain
title: "Multi-konteks: Sesi Target Terputus Saat Deactivate, Login Pengguna Nonaktif, Sesi Produk Lain Tetap Aktif, dan Sesi Aktor Berakhir"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-97
  - TC-FA-SU-98
  - TC-FA-SU-963
  - TC-FA-SU-1008
coverage:
  web: automated
---

# Multi-konteks: Sesi Target Terputus Saat Deactivate, Login Pengguna Nonaktif, Sesi Produk Lain Tetap Aktif, dan Sesi Aktor Berakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini sebagai konteks aktor; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Konteks browser: konteks aktor (Lina Marlina), konteks kedua (jendela privat, pengguna target Gita Permata, FAMS dan Global Settings pada dua tab), dan konteks ketiga (jendela privat, dipakai pada langkah 35 dan 40). Konteks kedua dan ketiga adalah objek asersi (TC-FA-SU-97, 98, 963, 1008) sehingga bukan pemicu `P-2`. Tiap konteks ditutup dan sesi loginnya dihapus pada langkah 37 dan 44 sebelum konteks berikutnya dibuka (S-09).
- Akun pengguna target: Gita Permata (Pre-setup #20 dan #23; Global Role `Import Data` dan `Manage accounting`, Group Role `Manage group` pada Finance & Accounting, Home Group Finance & Accounting). Email dan password akun Gita Permata tidak tertulis di Pre-setup TC; password lewat `Spectra.env.FA_GITA_PASSWORD` (nama usulan, didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Akses akun itu ke Global Settings (produk lain) disediakan tim FE.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, 25 pengguna), penugasan peran (#23), dan User Log Gita Permata sub-tab Session (#30 hanya untuk Budi Santoso; baris `Session ended` Gita Permata dihitung dengan baseline). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (berkas fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): tiga konteks browser paralel; seed API memulihkan status aktif Gita Permata; pembacaan jumlah entri Tab Changelog Gita Permata, Tab System Log aktor, Activity Log, dan baris `Session ended` sub-tab Session sebelum dan sesudah aksi (audit trail permanen, asersi memakai selisih terhadap baseline, S-12); mekanisme mengakhiri sesi aktor dari konteks lain pada langkah 40 (TC-FA-SU-1008 tidak merinci caranya).
- State global: status aktif Gita Permata (Inactive pada langkah 5, Active pada langkah 23, Inactive pada langkah 31, dipulihkan ke Active pada langkah 38). Pemulihan juga di hook `after` (Gita Permata Active) dan sesi dipulihkan ke Lina Marlina. Efek pada Pre-setup: Last Updated dan Modified By Gita Permata berubah; entri Changelog, System Log, Activity Log, dan User Log permanen bertambah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-97: Deactivate memutus sesi FAMS target

1. Catat jumlah baris `Session ended` pada Tab User Log sub-tab Session Gita Permata sebagai baseline
2. Buka konteks kedua dan login sebagai Gita Permata ke FAMS dengan `Spectra.env.FA_GITA_PASSWORD`
3. Buka Global Settings pada tab kedua di konteks kedua
4. Di konteks aktor, klik sakelar Active baris Gita Permata
5. Klik `[Confirm]` pada dialog konfirmasi
6. Tunggu aksi selesai
7. Pada tab FAMS di konteks kedua, klik menu apa pun
8. Verifikasi aksi di tab FAMS konteks kedua diarahkan ke halaman login
9. Verifikasi tidak ada dialog `Account Deactivated` pada konteks kedua
10. Pada tab Global Settings di konteks kedua, lakukan aksi apa pun
11. Verifikasi aksi di tab Global Settings berhasil tanpa diarahkan ke halaman login
12. Di konteks aktor, klik nama Gita Permata
13. Klik Tab User Log
14. Klik sub-tab Session
15. Muat ulang sub-tab Session tiap 5 detik sampai baris `Session ended` baru tampil (batas 2 menit)
16. Verifikasi jumlah baris `Session ended` bertambah satu dari baseline dengan Note `Session ended`

### TC-FA-SU-98: Pengguna nonaktif tidak dapat login

17. Pada konteks kedua (halaman login FAMS), login sebagai Gita Permata dengan `Spectra.env.FA_GITA_PASSWORD`
18. Verifikasi login ke FAMS ditolak
19. Di konteks aktor, klik Tab Role
20. Verifikasi Global Role `Import Data` dan `Manage accounting` serta Group Role `Manage group` pada Finance & Accounting Gita Permata sama dengan Pre-setup #23
21. Verifikasi Home Group Gita Permata tetap Finance & Accounting di General Information
22. Klik sakelar Active di header Detail Gita Permata
23. Klik `[Confirm]` pada dialog konfirmasi
24. Tunggu aksi selesai
25. Pada konteks kedua, login sebagai Gita Permata dengan `Spectra.env.FA_GITA_PASSWORD`
26. Verifikasi login ke FAMS berhasil
27. Di konteks aktor, muat ulang Detail Gita Permata
28. Verifikasi penugasan Global Role dan Group Role yang sama tampil di Tab Role

### TC-FA-SU-963: Deactivate FAMS tidak memutus sesi produk lain

29. Pada konteks kedua, buka Global Settings pada tab kedua
30. Di konteks aktor, klik sakelar Active di header Detail Gita Permata
31. Klik `[Confirm]` pada dialog konfirmasi
32. Tunggu aksi selesai
33. Pada tab Global Settings di konteks kedua, lakukan aksi apa pun
34. Verifikasi aksi di tab Global Settings berhasil (sesi produk lain tetap aktif)
35. Buka konteks ketiga dan login sebagai Gita Permata ke Global Settings dengan `Spectra.env.FA_GITA_PASSWORD`
36. Verifikasi login ke Global Settings berhasil
37. Tutup konteks kedua dan konteks ketiga serta hapus sesi loginnya

### TC-FA-SU-1008: Sesi aktor berakhir saat aksi tulis

38. Pulihkan Gita Permata ke Active lewat seed API
39. Catat jumlah entri Gita Permata pada Tab Changelog, Tab System Log aktor, dan Activity Log sebagai baseline
40. Buka konteks ketiga, login sebagai Lina Marlina, dan akhiri sesi konteks aktor dari konteks ketiga
41. Di konteks aktor (sesinya sudah berakhir), klik sakelar Active baris Gita Permata
42. Klik `[Confirm]` pada dialog konfirmasi
43. Verifikasi aksi tulis ditolak server mengikuti penanganan sesi platform
44. Tutup konteks ketiga, hapus sesi loginnya, lalu login ulang sebagai Lina Marlina di konteks aktor
45. Klik nama Gita Permata
46. Verifikasi sakelar Active di header Detail Gita Permata berstatus Active
47. Verifikasi jumlah entri Gita Permata pada Tab Changelog, Tab System Log aktor, dan Activity Log sama dengan baseline langkah 39

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 39 (baseline), 3, 29, dan 35 (membuka tab atau konteks tambahan), 12 sampai 15, 19, 27, dan 45 (navigasi dan muat ulang), 37 dan 44 (menutup konteks, S-09), serta 38 (pemulihan seed API). Langkah 6, 24, dan 32 (Tunggu aksi selesai) menghubungkan `[Confirm]` dengan perpindahan ke konteks lain (8b.8). Langkah 44 juga login ulang aktor setelah sesinya berakhir.
- Urutan TC sumber dipertahankan (97, 98, 963, 1008). TC-FA-SU-98 langkah 1 (Deactivate Gita Permata) sudah terpenuhi oleh langkah 4 sampai 5 TC-FA-SU-97 dan tidak diulang; Gita Permata Inactive sejak langkah 5 sampai langkah 22.
- TC-FA-SU-1008 butir b ("tidak ada entri log") ditulis sebagai asersi jumlah dengan baseline (S-12) pada aksi nyata spec ini (aksi tulis yang ditolak), bukan asersi absence kelas g; anchor positif pada langkah 46 (sakelar Active Gita Permata).
- Alasan spec melewati sekitar 35 langkah: seluruh blok berkelas c (multi-konteks) dengan target pengguna yang sama; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan tiap blok membutuhkan konteks kedua dengan sesi login pengguna target yang baru dibangun.
- Temuan untuk QA (S-15): (1) Pre-setup TC tidak mencantumkan email dan password akun Gita Permata; nama env `FA_GITA_PASSWORD` adalah usulan. (2) TC-FA-SU-963 menyebut dua tab (FAMS dan Global Settings) tanpa menyebut akses Gita Permata ke Global Settings. (3) TC-FA-SU-1008 langkah 1 ("Akhiri sesi aktor dari sesi lain") tidak merinci mekanismenya; Expected butir a "mengikuti penanganan sesi platform" tidak menyebut bentuk tampilan, sehingga asersi langkah 43 tidak memuat teks atau kode status. (4) TC-FA-SU-97 butir c ("sesi platform dan produk lain tetap aktif") tidak punya langkah observasi; spec mengobservasinya lewat tab Global Settings pada langkah 10 sampai 11. (5) Post Condition TC-FA-SU-97 butir c, TC-FA-SU-98, dan TC-FA-SU-963 tanpa langkah observasi tambahan tidak diasersi (S-01). (6) TC-FA-SU-97 butir b meminta Note `Session ended` sekaligus nama Action `Session ended`; spec mengasersi baris `Session ended` dengan Note `Session ended` sebagai satu baris log.
