---
id: TC-FA-RP-E2E-060-assign-read-only-2
title: "Assign Read Only (2/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-197
  - TC-FA-RP-198
  - TC-FA-RP-200
coverage:
  web: automated
---

# Assign Read Only (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #16 (Siti Rahayu Inactive, Eka Saputra Pending Activation, Fitri Handayani Pending Email Confirmation, Rudi Hartono), #3 (Rina Wulandari Total Control kedua), #43 (Kevin Susanto Group Manager di `Data Center` dan `Helpdesk`, Fajar Nugroho di `IT Infrastructure`, Lina Marlina di `Head Office`), #18 (pohon group).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-197: Popup Assign Read Only: Status dan Activation Status apa pun eligible

1. Klik Tab `Read Only`
2. Klik `[+ Assign]` di Tab Read Only
3. Ketik Search `Siti Rahayu`, tekan Enter
4. Verifikasi Siti Rahayu tampil di daftar picker dengan kolom Status `Inactive`
5. Ganti isi kotak search dengan `Eka Saputra`, tekan Enter
6. Verifikasi Eka Saputra tampil di daftar picker dengan kolom Status `Active`
7. Ganti isi kotak search dengan `Fitri Handayani`, tekan Enter
8. Verifikasi Fitri Handayani tampil di daftar picker dengan kolom Status `Active`
9. Klik `✕` pada Search, tekan Enter
10. Centang Siti Rahayu, Eka Saputra, dan Fitri Handayani lalu klik `[Assign]`
11. Verifikasi muncul toast sukses: `Success, Read Only has been assigned.`
12. Ketik Search `Siti Rahayu`, tekan Enter
13. Verifikasi baris Siti Rahayu tampil di Tab Read Only dengan Status `Inactive`
14. Ganti isi kotak search dengan `Eka Saputra`, tekan Enter
15. Verifikasi baris Eka Saputra tampil di Tab Read Only
16. Ganti isi kotak search dengan `Fitri Handayani`, tekan Enter
17. Verifikasi baris Fitri Handayani tampil di Tab Read Only
18. Klik `(←)` pada kotak Search

### TC-FA-RP-198: Assign Read Only ke user yang sedang Group Manager melepas seluruh penugasan GM dalam satu transaksi

19. Klik `[+ Assign]` di Tab Read Only
20. Centang Kevin Susanto lalu klik `[Assign]`
21. Verifikasi muncul toast sukses: `Success, Read Only has been assigned.`
22. Ketik Search `Kevin Susanto`, tekan Enter
23. Verifikasi Kevin Susanto tampil di Tab Read Only
24. Klik `(←)` pada kotak Search
25. Klik Tab `Group Manager`
26. Ketik Search `Kevin Susanto`, tekan Enter
27. Verifikasi Tab Group Manager tidak lagi memuat baris Kevin Susanto di `Data Center` maupun `Helpdesk` (empty state hasil Search)
28. Klik `(←)` pada kotak Search

### TC-FA-RP-200: Total Control tidak dapat menjadi Read Only secara langsung: Remove dulu lalu Assign

29. Klik Tab `Read Only`
30. Klik `[+ Assign]` di Tab Read Only
31. Ketik Search `Rina Wulandari`, tekan Enter
32. Verifikasi Rina Wulandari (Total Control) tidak ada di daftar picker Read Only (empty state hasil Search)
33. Tutup popup lewat `✕`
34. Klik Tab `Total Control`
35. Klik `[⋯]` baris Rina Wulandari lalu `Remove`, klik `[Remove]`
36. Verifikasi muncul toast sukses: `Success, Total Control has been removed.`
37. Klik Tab `Read Only`
38. Klik `[+ Assign]` di Tab Read Only
39. Ketik Search `Rina Wulandari`, tekan Enter
40. Verifikasi Rina Wulandari ada di daftar picker
41. Centang Rina Wulandari lalu klik `[Assign]`
42. Verifikasi muncul toast sukses: `Success, Read Only has been assigned.`
43. Ketik Search `Rina Wulandari`, tekan Enter
44. Verifikasi Rina Wulandari tampil di Tab Read Only
45. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 45 langkah.
- Langkah penghubung (S-03): langkah 1, 9, 18, 24, 26, 28–29, 45. Akun aktor pertama sudah login di hook `before` (S-07).
- Search untuk menemukan baris target (R-16): langkah 12, 14, 16, 22, 43.
- Langkah Search pada Tab (R-16) menemukan baris yang baru ditambahkan; absence di picker dan Tab Group Manager memakai empty state hasil Search sebagai anchor positif (butir 8b.2).
- Post Condition TC-FA-RP-198 (pelepasan GM beserta baris pola GM-nya sebelum baris pola tier ditulis, log `Remove`, notifikasi in-app per group) tidak punya langkah observasi dan tidak diasersi (S-01, S-15). Rina Wulandari dipulihkan ke Total Control di hook `after`.
- Temuan untuk QA:
  - TC-FA-RP-197: Search per user lalu centang ketiganya; TC tidak menyatakan apakah seleksi bertahan antar Search, jadi Search dikosongkan sebelum mencentang.
- Ukuran spec (45 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan ketiga blok (TC-FA-RP-197, 198, 200) berurutan pada popup Assign Read Only dan Tab Read Only dengan user dan Pre-setup yang sama, kondisi awalnya dibuat seeding di hook `before` dan Rina Wulandari dipulihkan di hook `after`, sehingga memecahnya hanya menggandakan login, hook, dan pembukaan popup yang sama; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
