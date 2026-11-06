---
id: TC-FA-RP-E2E-070-remove-group-manager-1
title: "Remove Group Manager (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-235
  - TC-FA-RP-236
  - TC-FA-RP-237
  - TC-FA-RP-240
  - TC-FA-RP-1017
coverage:
  web: automated
---

# Remove Group Manager (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #43 (Fajar Nugroho Group Manager di `IT Infrastructure`, Kevin Susanto di `Data Center`, Lina Marlina di `Head Office`), #18 (pohon group), #13 (Kevin Susanto: Group Manager di `Data Center`; baris pola GM di `Data Center` dan `Rack A1` (Group Role katalog selain `Manage user & role` CRUD penuh sesuai kolom berlaku, Role Transaksi Asset Admin dan Approver pada tiap Jenis Transaksi); baris non-pola: Group Role `Manage user & role` di `Data Center`, `Manage files` Read dan Delete di `Helpdesk`, Global Role `Manage accounting` hanya Read), #24 (Company Changelog). Pada TC-FA-RP-237 Kevin Susanto Group Manager di `Data Center` dan `Helpdesk`; pada TC-FA-RP-1017 Kevin Susanto satu-satunya Group Manager pada node `Data Center` dan toggle Require Approval OFF.
- Sesi kedua: sesi API Total Control kedua (Pre-setup #3, Rina Wulandari, `Spectra.env.FA_TC2_PASSWORD`) untuk TC-FA-RP-240; sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC2_PASSWORD`, `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-235: Dialog Remove Group Manager: copy dan Cancel

1. Klik Tab `Group Manager`
2. Klik `[⋯]` baris Kevin Susanto di `Data Center` lalu `Remove`
3. Amati dialog
4. Verifikasi dialog severity danger: Title `Remove Group Manager`; Body `• Kevin S` lalu `This user will lose Group Manager access for this group and its sub-groups. Their role assignments in this group and its sub-groups will be removed permanently.`; tombol `[Cancel]` dan `[Remove]`
5. Klik `[Cancel]`
6. Verifikasi tidak ada toast
7. Verifikasi dialog tertutup tanpa perubahan

### TC-FA-RP-236: Confirm Remove Group Manager melepas penugasan itu dan menghapus permanen baris pola GM pada node penugasan dan descendant-nya

8. Klik `[⋯]` baris Kevin Susanto di `Data Center` lalu `Remove`
9. Klik `[Remove]`
10. Verifikasi muncul toast sukses: `Success, Group Manager has been removed.`
11. Verifikasi baris Kevin Susanto di `Data Center` hilang dari Tab Group Manager
12. Buka Tab System lalu Detail Role `Manage files` dan pilih node `Data Center`
13. Verifikasi sedikitnya satu baris lain tampil pada node `Data Center`
14. Verifikasi baris pola Group Role Kevin Susanto di `Data Center` terhapus permanen dalam transaksi yang sama
15. Klik node `Rack A1`
16. Verifikasi tabel Detail Role `Manage files` tampil (anchor permukaan termuat)
17. Verifikasi baris pola Group Role Kevin Susanto di descendant `Rack A1` terhapus permanen dalam transaksi yang sama
18. Klik node `Helpdesk`
19. Verifikasi baris Group Role Kevin Susanto di `Helpdesk` (node lain, non-pola) tetap ada
20. Tetapkan ulang Kevin Susanto sebagai Group Manager di `Data Center` dan `Helpdesk` beserta baris pola GM dan baris non-pola-nya (Pre-setup #13) lewat seeding API

### TC-FA-RP-237: Remove Group Manager di satu group tidak melepas penugasan GM di group lain

21. Klik Tab `Group Manager`
22. Klik `[⋯]` baris Kevin Susanto di `Data Center` lalu `Remove`, klik `[Remove]`
23. Verifikasi muncul toast sukses: `Success, Group Manager has been removed.`
24. Verifikasi baris Kevin Susanto di `Helpdesk` tetap ada di Tab Group Manager
25. Buka Tab System lalu Detail Role `Manage files` dan pilih node `Helpdesk`
26. Verifikasi baris Group Role Kevin Susanto pada `Helpdesk` tetap ada
27. Tetapkan ulang Kevin Susanto sebagai Group Manager di `Data Center` dan `Helpdesk` lewat seeding API

### TC-FA-RP-240: Remove Group Manager atas penugasan yang sudah dihapus admin lain

28. Klik Tab `Group Manager`
29. Amati baris Kevin Susanto di `Data Center` pada sesi 1
30. Remove penugasan Group Manager Kevin Susanto di `Data Center` lewat sesi API Total Control kedua (Rina Wulandari) hingga tersimpan
31. Pada sesi 1 klik `[⋯]` baris Kevin Susanto di `Data Center` lalu `Remove`, klik `[Remove]`
32. Verifikasi sesi 1: muncul toast netral: `This Group Manager assignment is no longer available.`
33. Verifikasi data di-refresh dan perubahan tidak tersimpan

### TC-FA-RP-1017: Remove Group Manager terakhir pada node menuju empty state dan Assign keluar dari empty state

34. Tetapkan Kevin Susanto sebagai satu-satunya Group Manager pada node `Data Center` dengan toggle Require Approval OFF lewat seeding API
35. Klik Tab `Read Only` lalu klik Tab `Group Manager`
36. Klik node `Data Center` di Sidebar Group Tree
37. Klik `[⋯]` baris Kevin Susanto lalu `Remove`, klik `[Remove]`
38. Verifikasi muncul toast sukses: `Success, Group Manager has been removed.`
39. Amati tabel
40. Verifikasi tabel menampilkan empty state Title `No group managers yet` dan Description `Assign group managers to delegate administrative control.`
41. Klik `[+ Assign]`
42. Verifikasi field Group popup terisi `Data Center`
43. Centang Kevin Susanto, klik `[Assign]`
44. Verifikasi muncul toast sukses: `Success, Group Manager has been assigned.`
45. Verifikasi empty state hilang
46. Verifikasi baris Kevin Susanto di `Data Center` tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 46 langkah.
- Langkah penghubung (S-03): langkah 1, 15, 18, 21, 25, 35. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 20, 27, 34; tidak ada `Verifikasi`.
- TC-FA-RP-240 memakai dua sesi (Manual Only (d) di TC): sesi 2 adalah pelaku kedua yang hanya memicu perubahan state sehingga memakai sesi API (suite.md; langkah ditulis "... hingga ... tersimpan", R-20), bukan konteks kedua kelas c.
- Langkah klik tab ganda pada TC-FA-RP-1017 memuat ulang data tabel setelah seeding (TC langkah 1 klik node Sidebar tidak memuat ulang data tab).
- Absence baris pada TC-FA-RP-236 didahului `Verifikasi` baris lain pada tabel yang sama (butir 8b.2); absence baris sesudah Remove pada Tab Group Manager memakai toast sukses sebagai anchor; absence pada `Rack A1` memakai `Verifikasi` tabel Detail Role termuat (langkah 16).
- Post Condition TC-FA-RP-236 (notifikasi in-app ke Kevin Susanto dan log `Remove`, lihat Section 5) tidak punya langkah observasi dan tidak diasersi (S-01, S-15).
- Temuan untuk QA:
  - TC-FA-RP-237 Expected c menyatakan baris Group Role Kevin Susanto pada `Helpdesk` tetap ada; TC tidak memberi langkah membuka Detail Role untuk `Helpdesk`; spec menambah langkah penghubung (Buka Tab System lalu Detail Role `Manage files` dan pilih node `Helpdesk`) untuk mengamatinya.
  - TC-FA-RP-236 Expected c (baris pola Group Role Kevin Susanto di `Data Center` dan `Rack A1` terhapus) hanya diamati pada Detail Role `Manage files` (satu dari tujuh capability), sesuai langkah TC.
- Ukuran spec (46 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
