---
id: TC-FA-RP-E2E-059-assign-read-only-1
title: "Assign Read Only (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-193
  - TC-FA-RP-194
  - TC-FA-RP-195
  - TC-FA-RP-196
coverage:
  web: automated
---

# Assign Read Only (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso, Budi Setiawan, Citra Lestari, Dimas Pranata, Endah Susanti; Citra Lestari memegang `Import data` Read saja, `Manage Open API` Read dan Update, `Manage accounting` CRUD penuh), #12 (Maya Anggraeni Read Only), #3 (Rina Wulandari Total Control kedua), #1 (Admin Utama Default User).
- Waktu: jam server dan jam browser sinkron untuk asersi Last Updated (S-12); waktu dicatat sesudah `[Assign]`, toleransi satu menit.
- Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): daftar penugasan Group Role Citra Lestari dicatat sebagai baseline sebelum TC-FA-RP-195.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-196: Popup Assign Read Only mengecualikan user yang tidak eligible

1. Klik Tab `Read Only`
2. Klik `[+ Assign]` di Tab Read Only
3. Ketik Search `Siti Rahmawati`, tekan Enter
4. Verifikasi Siti Rahmawati (aktor sendiri) tidak ada di daftar (empty state hasil Search)
5. Ganti isi kotak search dengan `Admin Utama`, tekan Enter
6. Verifikasi Admin Utama (Default User) tidak ada di daftar (empty state hasil Search)
7. Ganti isi kotak search dengan `Rina Wulandari`, tekan Enter
8. Verifikasi Rina Wulandari (Total Control) tidak ada di daftar (empty state hasil Search)
9. Ganti isi kotak search dengan `Maya Anggraeni`, tekan Enter
10. Verifikasi Maya Anggraeni (Read Only) tidak ada di daftar (empty state hasil Search)
11. Ganti isi kotak search dengan `Ahmad Fauzi`, tekan Enter
12. Verifikasi Ahmad Fauzi (Standard) ada di daftar
13. Tutup popup lewat `✕`

### TC-FA-RP-193: Assign Read Only ke satu user Standard lewat popup

14. Klik `[+ Assign]` di Tab Read Only
15. Centang Ahmad Fauzi
16. Klik `[Assign]`
17. Catat waktu sesudah `[Assign]` untuk pembanding Last Updated
18. Verifikasi popup tertutup
19. Verifikasi muncul toast sukses: `Success, Read Only has been assigned.`
20. Ketik Search `Ahmad Fauzi`, tekan Enter
21. Verifikasi baris Ahmad Fauzi (Asset Custodian, Logistics, Status `Active`) tampil di Tab Read Only
22. Verifikasi kolom Modified By baris Ahmad Fauzi berisi `Siti R`
23. Verifikasi kolom Last Updated baris Ahmad Fauzi berisi waktu Assign sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
24. Klik `(←)` pada kotak Search

### TC-FA-RP-194: Assign Read Only ke tiga user sekaligus menghasilkan satu toast tunggal

25. Tunggu toast lama hilang otomatis
26. Klik `[+ Assign]` di Tab Read Only
27. Centang Budi Santoso, Budi Setiawan, dan Dimas Pranata
28. Amati counter
29. Verifikasi counter sebelum Assign `3 Users selected`
30. Klik `[Assign]`
31. Verifikasi muncul satu toast sukses: `Success, Read Only has been assigned.` (bentuk tunggal tanpa angka)
32. Ketik Search `Budi`, tekan Enter
33. Verifikasi baris Budi Santoso dan Budi Setiawan tampil di Tab Read Only
34. Ganti isi kotak search dengan `Dimas Pranata`, tekan Enter
35. Verifikasi baris Dimas Pranata tampil di Tab Read Only
36. Klik `(←)` pada kotak Search

### TC-FA-RP-195: Assign Read Only menyelaraskan seluruh Global Role user dengan penugasan parsial

37. Klik `[+ Assign]` di Tab Read Only
38. Centang Citra Lestari lalu klik `[Assign]`
39. Tunggu aksi selesai: popup tertutup
40. Buka Tab System lalu Detail Role `Import data`
41. Verifikasi baris Citra Lestari: hanya Read aktif
42. Verifikasi baris Citra Lestari: Create tidak aktif
43. Verifikasi baris Citra Lestari: Update dan Delete menampilkan `—`
44. Buka Detail Role `Manage Open API`
45. Verifikasi baris Citra Lestari: hanya Read aktif
46. Verifikasi baris Citra Lestari: Update tidak aktif (sebelumnya aktif)
47. Buka Detail Role `Manage asset transactional policy`
48. Verifikasi baris Citra Lestari (baru): hanya Read aktif
49. Buka Detail Role `Manage accounting`
50. Verifikasi baris Citra Lestari: hanya Read aktif
51. Buka Detail Role Group Role `Manage files` lalu klik `All Groups`
52. Ketik Search `Citra Lestari`, tekan Enter
53. Verifikasi jumlah baris Citra Lestari pada Detail Role `Manage files` sama dengan baseline (tidak ada baris baru; Group Role tidak ikut cascade)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 53 langkah.
- Langkah penghubung (S-03): langkah 1, 13, 17, 24–25, 36, 39, 51–52. Akun aktor pertama sudah login di hook `before` (S-07).
- Search untuk menemukan baris target (R-16): langkah 20, 32, 34.
- Penyimpangan urutan (S-05 catatan urutan): TC-FA-RP-196 dijalankan lebih dulu daripada TC-FA-RP-193, 194, dan 195 karena TC-FA-RP-196 Expected e mengharuskan Ahmad Fauzi masih Standard; kolom aksi sukses mengubah status user sesudahnya (validasi diblokir sebelum aksi sukses, S-10).
- Langkah Search pada Tab Read Only (R-16) menemukan baris yang baru ditambahkan karena tabel memuat lebih banyak baris daripada satu halaman.
- Post Condition TC-FA-RP-193 (a sampai d) dan TC-FA-RP-195 (a, b) tidak punya langkah observasi dan tidak diasersi (S-01, S-15).
- Temuan untuk QA:
  - TC-FA-RP-195 Expected e: Pre-setup #39 memuat Citra Lestari di `Head Office` pada `Manage files`; "tidak ada baris baru" diasersi sebagai jumlah baris sama dengan baseline (S-12).
  - TC-FA-RP-195 Expected b menyebut "Update yang tadi aktif menjadi tidak aktif" (nilai sebelum Assign, didasarkan Pre-setup #15); spec mengasersi keadaan sesudah Assign (Update tidak aktif).
- Ukuran spec (53 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan keempat blok (TC-FA-RP-196, 193, 194, 195) berurutan pada popup Assign Read Only di Tab Read Only dengan user dan Pre-setup yang sama, kondisi awalnya dibuat seeding di hook `before` dan urutannya terikat (TC-FA-RP-196 harus lebih dulu karena aksi sukses mengubah status user), sehingga memecahnya hanya menggandakan login, hook, dan pembukaan popup yang sama; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
