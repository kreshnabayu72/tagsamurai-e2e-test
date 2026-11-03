---
id: TC-FA-SU-E2E-045-bulk-resend-activation-email-sukses-sebagian-cooldown-seluruh-cooldown-dan-seleksi
title: "Bulk Resend Activation Email: Sukses, Sebagian Cooldown, Seluruh Cooldown, dan Seleksi Campuran"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-153
  - TC-FA-SU-154
  - TC-FA-SU-155
  - TC-FA-SU-157
coverage:
  web: automated
---

# Bulk Resend Activation Email: Sukses, Sebagian Cooldown, Seluruh Cooldown, dan Seleksi Campuran

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; layanan #37): Hana Kusuma dan Kartika Sari (Pending Activation; Kartika Inactive), Indra Wijaya (Pending Email Confirmation), dan Gita Permata (Activated). Cooldown Resend belum berjalan saat tiap blok dimulai; dipulihkan lewat seed API di hook `before`, langkah 19, dan langkah 29.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri log Resend per pengguna di Tab Changelog target dan di Tab System Log aktor (baseline, bagian 8b butir 10); jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC); seed API untuk mereset cooldown.
- Baseline log: hook `before` mencatat jumlah entri `Resend Activation Email` Hana dan Kartika pada Tab Changelog target, Tab System Log aktor, dan Activity Log. Entri log muncul eventual (NC-03): pemeriksaan surface log memuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- Jam: jam server dan jam browser dibekukan bersama pada langkah 1 supaya tooltip cooldown bernilai tepat 60 detik, dilepas pada langkah 10 (sebelum surface log dibuka, S-09). Hook `after` memulihkan jam.
- State global dan pemulihan: jam; cooldown Hana dan Kartika dipulihkan lewat seed API di hook `after`; entri log Resend bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-153: Bulk Resend Activation Email seluruh baris Pending Activation

1. Bekukan jam server dan jam browser bersamaan
2. Centang baris Hana Kusuma dan Kartika Sari di User List
3. Verifikasi Bulk Actions Bar memuat aksi `Resend Activation Email`
4. Klik Bulk Action, pilih `Resend Activation Email`
5. Verifikasi toast "Success, activation email has been sent." tampil tanpa nama pengguna
6. Klik ⋯ pada baris Hana Kusuma, hover `Resend Activation Email`
7. Verifikasi `Resend Activation Email` baris Hana Kusuma Disabled dengan tooltip "Please wait 60 seconds before resending."
8. Klik ⋯ pada baris Kartika Sari, hover `Resend Activation Email`
9. Verifikasi `Resend Activation Email` baris Kartika Sari Disabled dengan tooltip "Please wait 60 seconds before resending."
10. Lepaskan pembekuan jam
11. Buka Detail Hana Kusuma > Tab Changelog, muat ulang sampai entri tampil
12. Verifikasi satu entri `Resend Activation Email` Hana Kusuma tercatat (selisih 1 dari baseline) di Tab Changelog Hana Kusuma
13. Buka Detail Kartika Sari > Tab Changelog, muat ulang sampai entri tampil
14. Verifikasi satu entri `Resend Activation Email` Kartika Sari tercatat (selisih 1 dari baseline) di Tab Changelog Kartika Sari
15. Buka Tab System Log aktor, muat ulang sampai entri tampil
16. Verifikasi satu entri `Resend Activation Email` per pengguna (Hana Kusuma dan Kartika Sari) tercatat (selisih 1 dari baseline masing-masing) di Tab System Log aktor
17. Buka Activity Log, muat ulang sampai entri tampil
18. Verifikasi satu entri `Resend Activation Email` per pengguna (Hana Kusuma dan Kartika Sari) tercatat (selisih 1 dari baseline masing-masing) di Activity Log

### TC-FA-SU-154: Bulk Resend sebagian baris dalam cooldown

19. Pulihkan Hana Kusuma dan Kartika Sari tanpa cooldown lewat seed API, lalu muat ulang halaman User List
20. Klik ⋯ pada baris Hana Kusuma lalu `Resend Activation Email`
21. Buka Detail Hana Kusuma > Tab Changelog, muat ulang sampai entri `Resend Activation Email` dari langkah 20 tampil, lalu catat baseline jumlah entri `Resend Activation Email` Hana Kusuma; buka Detail Kartika Sari > Tab Changelog dan catat baseline jumlah entri `Resend Activation Email` Kartika Sari
22. Kembali ke User List, centang baris Hana Kusuma dan Kartika Sari (Hana dalam masa cooldown)
23. Klik Bulk Action, pilih `Resend Activation Email`
24. Verifikasi toast "Success, activation email has been sent. Some items were skipped (cooldown not finished)."
25. Buka Detail Hana Kusuma > Tab Changelog
26. Verifikasi jumlah entri `Resend Activation Email` Hana Kusuma sama dengan baseline langkah 21 (baris cooldown di-skip tanpa entri log)
27. Buka Detail Kartika Sari > Tab Changelog, muat ulang sampai entri tampil
28. Verifikasi jumlah entri `Resend Activation Email` Kartika Sari bertambah tepat satu dibanding baseline langkah 21

### TC-FA-SU-155: Bulk Resend seluruh baris dalam cooldown

29. Pulihkan Hana Kusuma dan Kartika Sari tanpa cooldown lewat seed API, lalu muat ulang halaman User List
30. Klik ⋯ pada baris Hana Kusuma lalu `Resend Activation Email`, kemudian klik ⋯ pada baris Kartika Sari lalu `Resend Activation Email`
31. Buka Tab System Log aktor, muat ulang sampai kedua entri `Resend Activation Email` dari langkah 30 tampil, lalu catat baseline jumlah entri `Resend Activation Email` di Tab System Log aktor
32. Kembali ke User List, centang baris Hana Kusuma dan Kartika Sari (keduanya dalam masa cooldown)
33. Klik Bulk Action, pilih `Resend Activation Email`
34. Verifikasi toast "Error, failed to send activation email. Please wait a moment before resending."
35. Buka Tab System Log aktor, muat ulang sampai entri langkah 30 tampil
36. Verifikasi jumlah entri `Resend Activation Email` di Tab System Log aktor sama dengan baseline langkah 31 (tidak ada entri log baru)

### TC-FA-SU-157: Bulk Resend Activation Email Hidden pada seleksi campuran

37. Muat ulang halaman User List, centang baris Hana Kusuma dan Gita Permata
38. Verifikasi Bulk Actions Bar tampil
39. Verifikasi `Resend Activation Email` tidak ada di Bulk Actions Bar pada seleksi Hana Kusuma dan Gita Permata
40. Hapus centang Hana Kusuma dan Gita Permata, lalu centang baris Indra Wijaya
41. Verifikasi Bulk Actions Bar tampil pada seleksi Indra Wijaya
42. Verifikasi aksi `Resend Confirmation Email` tidak ada di Bulk Actions Bar

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1 dan 10 (pembekuan dan pelepasan jam), langkah 11, 13, 15, 17, 25, 27, dan 35 (membuka surface log), langkah 19 dan 29 (memulihkan cooldown lewat seed API dan memuat ulang halaman), langkah 20 dan 30 (prasyarat cooldown yang disebut Langkah Uji TC-FA-SU-154 dan TC-FA-SU-155), langkah 21 dan 31 (membuka surface log, memuat ulang sampai entri langkah 20 dan 30 tampil, lalu mencatat baseline; baseline tidak dicatat sebelum entri eventual tampil, NC-03), langkah 22 dan 32 (kembali ke User List sebelum seleksi), langkah 37 dan 40 (membersihkan dan mengganti seleksi, S-09).
- Asersi tambahan di luar Expected TC: langkah 38 dan 41 (Bulk Actions Bar tampil) adalah anchor positif bagi asersi absence langkah 39 dan 42 (bagian 8b butir 2); toast langkah 24 dan 34 menjadi anchor bagi asersi jumlah entri log langkah 26, 28, dan 36.
- Spec ini 42 langkah. Alasan melewati sekitar 35 langkah: keempat blok satu topik (Bulk Resend Activation Email) dengan dataset yang sama (Hana, Kartika, Indra, Gita) dan satu pembukaan halaman User List; tiap blok berdiri sendiri karena cooldown dipulihkan lewat seed API di antara blok, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - Expected a TC-FA-SU-154 ("di-skip server-side tanpa entri log") dan Expected b TC-FA-SU-155 ("tidak ada entri log baru") tidak menyebut surface log; spec memakai Tab Changelog target (TC-FA-SU-154) dan Tab System Log aktor (TC-FA-SU-155) sebagai surface asersi jumlah dengan baseline (bagian 3 prinsip 13g).
  - Post Condition TC-FA-SU-153 (cooldown dan tiga permukaan log) hanya diasersi lewat Expected c; Post Condition TC-FA-SU-154 dan TC-FA-SU-155 tidak punya langkah observasi dan tidak diasersi (S-01).
  - Expected a TC-FA-SU-157 menyebut aksi Bulk `Resend Activation Email` Hidden pada seleksi campuran; seleksi hanya Indra Wijaya tidak memuat langkah "Hidden" untuk `Resend Activation Email` pada Expected b, sehingga spec hanya mengasersi `Resend Confirmation Email` tidak ada sesuai Expected b.
  - TC tidak menyebut cara menghapus seleksi sebelum seleksi berikutnya; spec memuat ulang halaman atau menghapus centang secara eksplisit.
