---
id: TC-FA-RP-E2E-061-remove-total-control-1
title: "Remove Total Control (1/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-205
  - TC-FA-RP-206
  - TC-FA-RP-208
  - TC-FA-RP-209
  - TC-FA-RP-210
coverage:
  web: automated
---

# Remove Total Control (1/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi dan kolam pengguna Standard; Ahmad Fauzi di-seed berstatus Total Control dengan seluruh Global Role selaras dan Group Role `Manage files` Read di `Data Center` untuk TC-FA-RP-206), #1 (Admin Utama Default User), #2 (Siti Rahmawati aktor), #36 (Tab Total Control terisi), #39 (Detail Role `Manage files` terisi, termasuk Dimas Pranata di `Data Center`).
- Sesi kedua: sesi API Total Control kedua (Pre-setup #3, Rina Wulandari, `Spectra.env.FA_TC2_PASSWORD`) untuk TC-FA-RP-208 dan 209; sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi.
- Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): tingkat akses dan penugasan user dicatat sebagai baseline untuk Expected "tidak berubah oleh sesi 1".
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC2_PASSWORD`, `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-205: Dialog Remove Total Control: copy, Cancel membatalkan tanpa perubahan

1. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
2. Amati dialog
3. Verifikasi dialog severity danger: Title `Remove Total Control`; Body `• Ahmad F` lalu `This user will lose Total Control access, and all of their roles and group assignments will be reset.`; tombol `[Cancel]` (Text, Contrast) dan `[Remove]`
4. Klik `[Cancel]`
5. Verifikasi tidak ada toast
6. Verifikasi dialog tertutup
7. Verifikasi baris Ahmad Fauzi tetap ada di Tab Total Control

### TC-FA-RP-206: Confirm Remove Total Control: tingkat akses dicabut, seluruh Global Role direset total, dan seluruh Group Role dihapus

8. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
9. Klik `[Remove]`
10. Verifikasi muncul toast sukses: `Success, Total Control has been removed.`
11. Verifikasi baris Ahmad Fauzi hilang dari Tab Total Control
12. Buka Tab System lalu Detail Role `Manage Open API`
13. Verifikasi sedikitnya satu baris lain tampil di Detail Role `Manage Open API`
14. Verifikasi baris Ahmad Fauzi tidak tampil lagi (Global Role direset total ke kondisi tanpa role, `FARP-LOGIC-17c`)
15. Buka Detail Role Group Role `Manage files` dan pilih node `Data Center`
16. Verifikasi sedikitnya satu baris lain tampil di Detail Role `Manage files` node `Data Center`
17. Verifikasi baris Ahmad Fauzi tidak tampil lagi (seluruh penugasan Group Role dihapus, `FARP-LOGIC-17c`)
18. Tetapkan ulang Ahmad Fauzi sebagai Total Control dengan seluruh Global Role selaras lewat seeding API

### TC-FA-RP-208: Remove Total Control atas user yang sudah dilepas admin lain: toast netral dan data di-refresh

19. Klik Tab `Total Control`
20. Amati baris Ahmad Fauzi pada sesi 1
21. Remove Total Control milik Ahmad Fauzi lewat sesi API Total Control kedua (Rina Wulandari) hingga tersimpan
22. Catat tingkat akses dan penugasan Ahmad Fauzi lewat fixture BE sebagai baseline
23. Pada sesi 1 klik `[⋯]` baris Ahmad Fauzi lalu `Remove`, klik `[Remove]`
24. Verifikasi sesi 1: muncul toast netral: `This access level is no longer available.`
25. Verifikasi tabel sesi 1 di-refresh dan baris Ahmad Fauzi tidak ada
26. Verifikasi tingkat akses dan penugasan Ahmad Fauzi sama dengan baseline (tidak berubah oleh sesi 1)

### TC-FA-RP-209: Remove Total Control atas user yang tingkatnya sudah berbeda dari tab yang dirender

27. Tetapkan ulang Ahmad Fauzi sebagai Total Control lewat seeding API
28. Klik Tab `Read Only` lalu klik Tab `Total Control`
29. Amati baris Ahmad Fauzi pada sesi 1
30. Remove Total Control milik Ahmad Fauzi lalu Assign Read Only untuk Ahmad Fauzi lewat sesi API Total Control kedua (Rina Wulandari) hingga tersimpan
31. Catat tingkat akses Ahmad Fauzi lewat fixture BE sebagai baseline
32. Pada sesi 1 klik `[⋯]` baris Ahmad Fauzi lalu `Remove`, klik `[Remove]`
33. Verifikasi sesi 1: muncul toast netral: `This access level is no longer available.`
34. Verifikasi tingkat akses Read Only Ahmad Fauzi tidak berubah (sama dengan baseline)

### TC-FA-RP-210: Remove Total Control: baris Default User dan baris sendiri Disabled dengan tooltip

35. Klik `[⋯]` baris Admin Utama
36. Hover `Remove`
37. Verifikasi `Remove` baris Admin Utama Disabled dengan tooltip `Default User cannot be modified.`
38. Tekan Esc untuk menutup dropdown
39. Klik `[⋯]` baris Siti Rahmawati
40. Hover `Remove`
41. Verifikasi `Remove` baris Siti Rahmawati Disabled dengan tooltip `You can't manage your own account from here.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 41 langkah.
- Langkah penghubung (S-03): langkah 22, 28, 31, 38. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 18, 27; tidak ada `Verifikasi`.
- TC-FA-RP-208 dan 209 memakai dua sesi (Manual Only (d) di TC): sesi 2 adalah pelaku kedua yang hanya memicu perubahan state, sehingga memakai sesi API (suite.md; langkah ditulis "... hingga ... tersimpan", R-20) dan bukan konteks kedua kelas c. Langkah "Klik Tab `Total Control`" pada TC-FA-RP-208 dan "Klik Tab `Read Only` lalu klik Tab `Total Control`" pada TC-FA-RP-209 adalah langkah TC 1 ("membuka tab dan melihat baris") yang memuat ulang data tabel setelah seeding.
- Absence baris pada TC-FA-RP-206 didahului `Verifikasi` baris lain pada tabel yang sama (butir 8b.2); absence baris sesudah Remove pada Tab Total Control memakai toast sukses sebagai anchor.
- Temuan untuk QA:
  - TC-FA-RP-206 precondition d memuat Group Role `Manage files` Read di `Data Center` untuk Ahmad Fauzi (Pre-setup #39 memuat Ahmad Fauzi di `Data Center`); precondition c hanya merujuk Pre-setup #15.
  - TC-FA-RP-208 dan 209 Expected b "tingkat akses dan penugasan tidak berubah oleh sesi 1" tidak punya langkah observasi di TC; spec mengasersinya lewat baseline yang dicatat sesudah sesi 2 (kemampuan baca state disediakan tim FE/BE).
  - Post Condition TC-FA-RP-206 (log `Remove` dan notifikasi in-app ke Ahmad Fauzi) tidak punya langkah observasi dan tidak diasersi.
- Ukuran spec (41 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
