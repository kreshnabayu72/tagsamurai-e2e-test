---
id: TC-FA-RP-E2E-064-remove-read-only-1
title: "Remove Read Only (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-211
  - TC-FA-RP-212
  - TC-FA-RP-214
  - TC-FA-RP-215
  - TC-FA-RP-216
coverage:
  web: automated
---

# Remove Read Only (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi di-seed berstatus Read Only dengan seluruh Global Role selaras dan baris pola Group Role Read saja pada setiap group (pola tier Read Only, termasuk `Manage files` di `Data Center`) untuk TC-FA-RP-212), #1 (Admin Utama), #2 (Siti Rahmawati aktor), #37 (Tab Read Only terisi: Dewi Anggraini, Maya Anggraeni, Yoga Pratama, Gilang Prakoso), #39 (Detail Role `Manage files` terisi, termasuk Dimas Pranata di `Data Center`).
- Sesi kedua: sesi API Total Control kedua (Pre-setup #3, Rina Wulandari, `Spectra.env.FA_TC2_PASSWORD`) untuk TC-FA-RP-214 dan 215; sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi.
- Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): tingkat akses dan penugasan user dicatat sebagai baseline untuk Expected "tidak berubah oleh sesi 1".
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC2_PASSWORD`, `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-211: Dialog Remove Read Only: copy, Cancel membatalkan tanpa perubahan

1. Klik Tab `Read Only`
2. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
3. Amati dialog
4. Verifikasi dialog severity danger: Title `Remove Read Only`; Body `• Ahmad F` lalu `This user will lose Read Only access, and all of their roles and group assignments will be reset.`; tombol `[Cancel]` (Text, Contrast) dan `[Remove]`
5. Klik `[Cancel]`
6. Verifikasi tidak ada toast
7. Verifikasi dialog tertutup
8. Verifikasi baris Ahmad Fauzi tetap ada di Tab Read Only

### TC-FA-RP-212: Confirm Remove Read Only: tingkat akses dicabut, seluruh Global Role direset total, dan seluruh Group Role dihapus

9. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
10. Klik `[Remove]`
11. Verifikasi muncul toast sukses: `Success, Read Only has been removed.`
12. Verifikasi baris Ahmad Fauzi hilang dari Tab Read Only
13. Buka Tab System lalu Detail Role `Manage Open API`
14. Verifikasi sedikitnya satu baris lain tampil di Detail Role `Manage Open API`
15. Verifikasi baris Ahmad Fauzi tidak tampil lagi (Global Role direset total ke kondisi tanpa role, `FARP-LOGIC-17c`)
16. Buka Detail Role Group Role `Manage files` dan pilih node `Data Center`
17. Verifikasi sedikitnya satu baris lain tampil di Detail Role `Manage files` node `Data Center`
18. Verifikasi baris Ahmad Fauzi tidak tampil lagi (seluruh penugasan Group Role dihapus, `FARP-LOGIC-17c`)
19. Tetapkan ulang Ahmad Fauzi sebagai Read Only dengan seluruh Global Role selaras lewat seeding API

### TC-FA-RP-214: Remove Read Only atas user yang sudah dilepas admin lain: toast netral dan data di-refresh

20. Klik Tab `Read Only`
21. Amati baris Ahmad Fauzi pada sesi 1
22. Remove Read Only milik Ahmad Fauzi lewat sesi API Total Control kedua (Rina Wulandari) hingga tersimpan
23. Catat tingkat akses dan penugasan Ahmad Fauzi lewat fixture BE sebagai baseline
24. Pada sesi 1 klik `[⋯]` baris Ahmad Fauzi lalu `Remove`, klik `[Remove]`
25. Verifikasi sesi 1: muncul toast netral: `This access level is no longer available.`
26. Verifikasi tabel sesi 1 di-refresh dan baris Ahmad Fauzi tidak ada
27. Verifikasi tingkat akses dan penugasan Ahmad Fauzi sama dengan baseline (tidak berubah oleh sesi 1)

### TC-FA-RP-215: Remove Read Only atas user yang tingkatnya sudah berbeda dari tab yang dirender

28. Tetapkan ulang Ahmad Fauzi sebagai Read Only lewat seeding API
29. Klik Tab `Total Control` lalu klik Tab `Read Only`
30. Amati baris Ahmad Fauzi pada sesi 1
31. Remove Read Only milik Ahmad Fauzi lalu Assign Total Control untuk Ahmad Fauzi lewat sesi API Total Control kedua (Rina Wulandari) hingga tersimpan
32. Catat tingkat akses Ahmad Fauzi lewat fixture BE sebagai baseline
33. Pada sesi 1 klik `[⋯]` baris Ahmad Fauzi lalu `Remove`, klik `[Remove]`
34. Verifikasi sesi 1: muncul toast netral: `This access level is no longer available.`
35. Verifikasi tingkat akses Total Control Ahmad Fauzi tidak berubah (sama dengan baseline)

### TC-FA-RP-216: Tab Read Only memuat Maya Anggraeni dan tidak memuat Total Control: Admin Utama dan Siti Rahmawati tidak ada di daftar

36. Klik Tab `Total Control` lalu klik Tab `Read Only`
37. Ketik Search `Maya Anggraeni`, tekan Enter
38. Verifikasi Maya Anggraeni tampil di Tab Read Only
39. Ganti isi kotak search dengan `Admin Utama`, tekan Enter
40. Verifikasi Admin Utama tidak ada di daftar karena Total Control, bukan Read Only (empty state hasil Search)
41. Ganti isi kotak search dengan `Siti Rahmawati`, tekan Enter
42. Verifikasi Siti Rahmawati tidak ada di daftar karena Total Control, bukan Read Only (empty state hasil Search)
43. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 43 langkah.
- Langkah penghubung (S-03): langkah 1, 23, 29, 32, 36, 43. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 19, 28; tidak ada `Verifikasi`.
- TC-FA-RP-214 dan 215 memakai dua sesi (Manual Only (d) di TC): sesi 2 adalah pelaku kedua yang hanya memicu perubahan state sehingga memakai sesi API (suite.md; langkah ditulis "... hingga ... tersimpan", R-20), bukan konteks kedua kelas c. Langkah klik tab ganda pada TC-FA-RP-215 dan 216 memuat ulang data tabel setelah seeding (TC langkah 1 "membuka tab dan melihat baris").
- Absence baris pada TC-FA-RP-212 didahului `Verifikasi` baris lain pada tabel yang sama (butir 8b.2); absence pada TC-FA-RP-216 memakai empty state hasil Search sebagai anchor positif.
- Temuan untuk QA:
  - TC-FA-RP-212 precondition d memuat baris pola Group Role Read saja pada setiap group untuk Ahmad Fauzi; precondition c hanya merujuk Pre-setup #15.
  - TC-FA-RP-214 dan 215 Expected b "tingkat akses dan penugasan tidak berubah oleh sesi 1" tidak punya langkah observasi di TC; spec mengasersinya lewat baseline yang dicatat sesudah sesi 2.
  - Post Condition TC-FA-RP-212 (log `Remove` dan notifikasi in-app ke Ahmad Fauzi, satu entri `Remove (via Read Only)` per baris Group Role) tidak punya langkah observasi di TC dan tidak diasersi; pencatatan per baris diasersi TC-FA-RP-1135 di spec `TC-FA-RP-E2E-247-changelog-detail-role-global-role-3`.
- Ukuran spec (43 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
