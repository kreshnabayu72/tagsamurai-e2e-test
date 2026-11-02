---
id: TC-GS-PROFILE-E2E-053-absence-log-lain
title: "Absence Log: Banner Email Change, Penolakan Change Password, dan Ganti Produk Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-227
  - TC-GS-PROFILE-236
  - TC-GS-PROFILE-237
coverage:
  web: automated
---

# Absence Log: Banner Email Change, Penolakan Change Password, dan Ganti Produk Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Akun aktor pertama spec: Pre-setup #8 (Citra Lestari, Activated, Email `citralestari@qwertysystem.net`) `pendingEmailProfile_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini dengan `Spectra.env.GS_PROFILE_PENDING_PASSWORD`. Ganti akun ke Pre-setup #7 (Maya Anggraini, password aktif `Spectra.env.GS_PROFILE_PWD_PASSWORD`, counter 0) `passwordProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_PWD_PASSWORD`; lalu Pre-setup #5 (Sinta Maharani, App Access Global Settings dan Fixed Asset) `multiAccessProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_MULTI_PASSWORD`. Pembaca log: admin Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`, login lewat UI pada langkah ganti akun.
- Env var: `GS_PROFILE_PENDING_PASSWORD`, `GS_PROFILE_PWD_PASSWORD`, `PROFILE_PASSWORD_NEW` (Data Dinamis #3), `GS_PROFILE_MULTI_PASSWORD`, `GS_PROFILE_ADMIN_PASSWORD`.
- Data Dinamis #2: permintaan Email change live dari Citra Lestari ke `citra.baru@qwertysystem.net`, dibuat lewat fixture BE di hook `before` (disediakan tim FE/BE) dan dibatalkan di hook `after`.
- Kemampuan teknis: muat ulang halaman; membaca jumlah baris Tab Changelog, Tab System Log, Tab User Log Detail User dan Activity Log sebelum dan sesudah aksi (baseline, S-12; disediakan tim FE/BE); fixture BE mengunci Change Password Maya Anggraini pada tier 15 menit (disediakan tim FE/BE) untuk TC-GS-PROFILE-236, dipulihkan oleh langkah 24 dan hook `after`; Product Selector.
- Pemulihan (R-08): langkah 24 memulihkan lock dan counter Change Password Maya Anggraini ke 0 lewat fixture BE; password Maya Anggraini tidak berubah karena semua submit ditolak.
- State global yang diubah: lock dan counter Pre-setup #7. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-PROFILE-227: Melihat banner Pending Email Change tidak menulis log

1. Catat baseline lewat kemampuan baca: jumlah baris Tab Changelog, Tab System Log, dan Activity Log Citra Lestari
2. Verifikasi banner Pending Email Change tampil di My Profile yang dibuka hook `beforeEach`
3. Muat ulang halaman (F5)
4. Verifikasi banner Pending Email Change tampil setelah muat ulang

### TC-GS-PROFILE-236: Penolakan Change Password tidak dicatat

5. Logout
6. Login sebagai Maya Anggraini (Pre-setup #7)
7. Buka My Profile dari account menu navbar
8. Catat baseline lewat kemampuan baca: jumlah baris Activity `Change Password` pada Tab User Log Detail Maya Anggraini
9. Klik `[Change Password]`
10. Isi New Password `Spectra.env.PROFILE_PASSWORD_NEW` dan Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW` dengan Current Password dikosongkan
11. Upaya submit: klik `[Save]` (Current kosong)
12. Isi Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD` dan ganti isi Confirm New Password dengan `Different1!`
13. Upaya submit: klik `[Save]` (Confirm tidak sama)
14. Ganti isi New Password dan Confirm New Password dengan `abc`
15. Upaya submit: klik `[Save]` (Policy gagal)
16. Ganti isi New Password dan Confirm New Password dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`
17. Upaya submit: klik `[Save]` (New sama dengan password lama)
18. Kunci Change Password Maya Anggraini pada tier 15 menit lewat fixture BE
19. Ganti isi New Password dan Confirm New Password dengan `Spectra.env.PROFILE_PASSWORD_NEW`
20. Upaya submit: klik `[Save]` (saat terkunci)
21. Klik `✕`
22. Verifikasi dialog `Unsaved Changes` tampil
23. Klik `[Leave]`
24. Pulihkan lock dan counter Change Password Maya Anggraini ke 0 lewat fixture BE

### TC-GS-PROFILE-237: Berganti produk di Product Selector tidak mencatat log

25. Logout
26. Login sebagai Sinta Maharani (Pre-setup #5)
27. Buka My Profile dari account menu navbar
28. Catat baseline lewat kemampuan baca: jumlah baris Tab Changelog, Tab System Log, dan Tab User Log Detail Sinta Maharani
29. Pilih opsi `Fixed Asset` di Product Selector
30. Verifikasi Product Selector menampilkan opsi `Fixed Asset` terpilih
31. Tunggu aksi selesai

### Pembacaan log oleh admin

32. Logout
33. Login sebagai admin Hendra Wijaya (Pre-setup #6)
34. Buka Global Settings > User > Detail Citra Lestari > Tab Changelog
35. Verifikasi Tab Changelog memuat sedikitnya satu baris pembanding
36. Verifikasi TC-GS-PROFILE-227: jumlah baris Tab Changelog Citra Lestari sama dengan baseline
37. Buka Tab System Log
38. Verifikasi Tab System Log memuat sedikitnya satu baris pembanding
39. Verifikasi TC-GS-PROFILE-227: jumlah baris Tab System Log Citra Lestari sama dengan baseline
40. Buka Global Settings > Activity Log
41. Verifikasi Activity Log memuat sedikitnya satu baris pembanding
42. Verifikasi TC-GS-PROFILE-227: jumlah baris Activity Log Citra Lestari sama dengan baseline
43. Buka Global Settings > User > Detail Maya Anggraini > Tab User Log
44. Verifikasi Tab User Log memuat sedikitnya satu baris pembanding
45. Verifikasi TC-GS-PROFILE-236: tidak ada baris Activity `Change Password` baru untuk submit field kosong, Confirm tidak sama, Policy gagal, New sama dengan password lama, dan percobaan saat terkunci (jumlah baris sama dengan baseline)
46. Buka Global Settings > User > Detail Sinta Maharani > Tab Changelog
47. Verifikasi Tab Changelog memuat sedikitnya satu baris pembanding
48. Verifikasi TC-GS-PROFILE-237: tidak ada baris baru di Tab Changelog akibat pergantian produk (jumlah baris sama dengan baseline)
49. Buka Tab System Log
50. Verifikasi Tab System Log memuat sedikitnya satu baris pembanding
51. Verifikasi TC-GS-PROFILE-237: tidak ada baris baru di Tab System Log akibat pergantian produk (jumlah baris sama dengan baseline)
52. Buka Tab User Log
53. Verifikasi Tab User Log memuat sedikitnya satu baris pembanding
54. Verifikasi TC-GS-PROFILE-237: tidak ada baris baru di Tab User Log akibat pergantian produk (jumlah baris sama dengan baseline)

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas g (asersi absence). Pemicu TC-GS-PROFILE-236 (fixture lock, kelas d) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji: `P-5` butir a. Tiap TC punya user dan baseline sendiri (langkah 1, 8, dan 28); admin membaca log sekali di akhir (langkah 32 sampai 54) sehingga ganti akun ke admin hanya sekali. Baseline dicatat sebelum pemicu tiap TC dan hanya berlaku untuk user TC itu.
- Spec melewati sekitar 35 langkah (54 langkah) karena tiga TC berada di satu kelas (g), tiap TC wajib punya user dan baseline sendiri (`P-5` butir a), dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok baca-log berpola (langkah 34 sampai 54, yaitu buka surface, pembanding, `Verifikasi` jumlah baris) tidak dihitung menurut bagian 3, sehingga langkah efektif sekitar 33.
- TC-GS-PROFILE-236 Expected (a) sampai (e) diasersi dengan satu `Verifikasi` (langkah 45) karena daftar kondisi yang sama-sama tidak tercatat disebut utuh dan diamati dari satu perbandingan jumlah baris terhadap baseline satu TC.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7, 27 (membuka My Profile setelah login), 21 sampai 23 (menutup modal dirty lewat `✕`, dialog `Unsaved Changes`, `[Leave]`, S-08), 24 (pemulihan lock), 31 (tunggu aksi selesai sebelum ganti akun).
- Asersi tambahan di luar Expected TC (S-03): langkah 2 dan 4 serta 30 adalah pembanding (anchor) pemicu; langkah 35, 38, 41, 44, 47, 50, dan 53 adalah pembanding surface (8b butir 2).
- Temuan untuk QA:
  - TC-GS-PROFILE-236 tidak menyebut nilai Current, New, dan Confirm untuk kasus selain yang disebut; spec memakai Current `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New dan Confirm `Spectra.env.PROFILE_PASSWORD_NEW` kecuali dinyatakan lain pada tiap kasus.
  - TC-GS-PROFILE-236 tidak menyatakan apakah `[Save]` Disabled pada kasus field kosong, Confirm tidak sama, dan Policy gagal; spec menulis "Upaya submit" dan penanganan tombol Disabled ditentukan di tahap script.
  - TC-GS-PROFILE-236 butir "Policy gagal" hanya menyebut New `abc` tanpa nilai Confirm; spec memakai Confirm `abc`.
  - TC-GS-PROFILE-237 menyebut Detail Sinta Maharani tanpa Expected untuk perubahan Product Selector sendiri; spec memakai tampilan opsi `Fixed Asset` terpilih sebagai pembanding pemicu.
