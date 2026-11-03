---
id: TC-FA-RP-E2E-057-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-2
title: "Assign Total Control: satu atau banyak user, timpa parsial, dan upgrade dari Read Only (2/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-190
  - TC-FA-RP-191
  - TC-FA-RP-192
  - TC-FA-RP-199
coverage:
  web: automated
---

# Assign Total Control: satu atau banyak user, timpa parsial, dan upgrade dari Read Only (2/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (kolam pengguna Standard: Ahmad Fauzi, Dimas Pranata, Budi Santoso, ...), #16 (Siti Rahayu Inactive, Eka Saputra Pending Activation, Fitri Handayani Pending Email Confirmation, Rudi Hartono), #12 (Maya Anggraeni Read Only), #3 (Rina Wulandari Total Control kedua), #1 (Admin Utama Default User), #43 (Kevin Susanto Group Manager di `Data Center` dan `Helpdesk`, Fajar Nugroho di `IT Infrastructure`, Lina Marlina di `Head Office`), #18 (pohon group).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-190: Popup Assign Total Control mengecualikan user yang tidak eligible

1. Klik `[+ Assign]` di Tab Total Control
2. Ketik Search `Siti Rahmawati`, tekan Enter
3. Verifikasi Siti Rahmawati (aktor sendiri) tidak ada di daftar (empty state hasil Search)
4. Ganti isi kotak search dengan `Admin Utama`, tekan Enter
5. Verifikasi Admin Utama (Default User) tidak ada di daftar (empty state hasil Search)
6. Ganti isi kotak search dengan `Rina Wulandari`, tekan Enter
7. Verifikasi Rina Wulandari (Total Control) tidak ada di daftar (empty state hasil Search)
8. Ganti isi kotak search dengan `Maya Anggraeni`, tekan Enter
9. Verifikasi Maya Anggraeni (Read Only) tetap ada di daftar (upgrade Read Only ke Total Control diizinkan)
10. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
11. Verifikasi Ahmad Fauzi (Standard) ada di daftar
12. Tutup popup lewat `✕`

### TC-FA-RP-191: Popup Assign Total Control: Status dan Activation Status apa pun eligible

13. Klik `[+ Assign]` di Tab Total Control
14. Ketik Search `Siti Rahayu`, tekan Enter
15. Verifikasi Siti Rahayu tampil di daftar picker dengan kolom Status `Inactive`
16. Ganti isi kotak search dengan `Eka Saputra`, tekan Enter
17. Verifikasi Eka Saputra tampil di daftar picker dengan kolom Status `Active`
18. Ganti isi kotak search dengan `Fitri Handayani`, tekan Enter
19. Verifikasi Fitri Handayani tampil di daftar picker dengan kolom Status `Active`
20. Klik `✕` pada Search, tekan Enter
21. Centang Siti Rahayu, Eka Saputra, dan Fitri Handayani lalu klik `[Assign]`
22. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`
23. Ketik Search `Siti Rahayu`, tekan Enter
24. Verifikasi baris Siti Rahayu tampil di Tab Total Control dengan Status `Inactive`
25. Ganti isi kotak search dengan `Eka Saputra`, tekan Enter
26. Verifikasi baris Eka Saputra tampil di Tab Total Control
27. Ganti isi kotak search dengan `Fitri Handayani`, tekan Enter
28. Verifikasi baris Fitri Handayani tampil di Tab Total Control
29. Klik `(←)` pada kotak Search

### TC-FA-RP-192: Assign Total Control ke user yang sedang Group Manager melepas seluruh penugasan GM dalam satu transaksi

30. Klik `[+ Assign]` di Tab Total Control
31. Centang Kevin Susanto lalu klik `[Assign]`
32. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`
33. Ketik Search `Kevin Susanto`, tekan Enter
34. Verifikasi Kevin Susanto tampil di Tab Total Control
35. Klik `(←)` pada kotak Search
36. Klik Tab `Group Manager`
37. Ketik Search `Kevin Susanto`, tekan Enter
38. Verifikasi Tab Group Manager tidak lagi memuat baris Kevin Susanto di `Data Center` maupun `Helpdesk` (empty state hasil Search)
39. Klik `(←)` pada kotak Search

### TC-FA-RP-199: Assign Total Control ke user Read Only menggantikan Read Only dalam satu transaksi

40. Klik Tab `Total Control`
41. Klik `[+ Assign]` di Tab Total Control
42. Centang Maya Anggraeni lalu klik `[Assign]`
43. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`
44. Ketik Search `Maya Anggraeni`, tekan Enter
45. Verifikasi Maya Anggraeni tampil di Tab Total Control
46. Klik `(←)` pada kotak Search
47. Klik Tab `Read Only`
48. Ketik Search `Maya Anggraeni`, tekan Enter
49. Verifikasi Maya Anggraeni tidak lagi ada di Tab Read Only (empty state hasil Search)
50. Klik `(←)` pada kotak Search
51. Buka Tab System lalu Detail Role `Manage Open API`
52. Verifikasi baris Maya Anggraeni: Read dan Update aktif
53. Verifikasi baris Maya Anggraeni: Create dan Delete menampilkan `—`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 53 langkah.
- Langkah penghubung (S-03): langkah 12, 20, 29, 35, 37, 39–40, 46, 48, 50. Akun aktor pertama sudah login di hook `before` (S-07).
- Search untuk menemukan baris target (R-16): langkah 23, 25, 27, 33, 44.
- Asersi absence di picker (langkah pada TC-FA-RP-190) memakai empty state hasil Search sebagai anchor positif (butir 8b.2); asersi absence di Tab Group Manager dan Tab Read Only memakai empty state hasil Search yang sama.
- Langkah Search pada Tab (R-16) menemukan baris yang baru ditambahkan karena tabel memuat lebih banyak baris daripada satu halaman.
- Post Condition TC-FA-RP-192 (pelepasan GM, log `Remove`, notifikasi in-app) dan TC-FA-RP-199 (log `Assign` Old Value `Read Only`, tidak ada notifikasi Remove Read Only) tidak punya langkah observasi dan tidak diasersi (S-01, S-15).
- Penyimpangan kecil: TC-FA-RP-191 mencari tiap user satu per satu sebelum mencentang ketiganya; Search dikosongkan di antara pencarian dan pencentangan agar ketiga user terlihat bersamaan.
- Temuan untuk QA:
  - TC-FA-RP-191: langkah 3 mencentang ketiga user setelah dicari satu per satu; TC tidak menyatakan apakah seleksi bertahan antar Search atau Search harus dikosongkan; spec mengosongkan Search dahulu.
  - TC-FA-RP-190 Expected d dan TC-FA-RP-199 menjadikan Maya Anggraeni (Read Only) eligible untuk Assign Total Control; TC-FA-RP-190 dan 199 berurutan pada Maya yang sama, TC-FA-RP-199 dijalankan terakhir agar TC-FA-RP-190 tidak terpengaruh.
- Ukuran spec (53 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan keempat blok (TC-FA-RP-190, 191, 192, 199) berurutan pada popup Assign Total Control dan Tab Total Control, Group Manager, dan Read Only dengan user dan Pre-setup yang sama, kondisi awalnya dibuat seeding di hook `before` (TC-FA-RP-199 dijalankan terakhir karena memakai Maya Anggraeni yang sama dengan TC-FA-RP-190), sehingga memecahnya hanya menggandakan login, hook, dan pembukaan popup yang sama; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
