---
id: TC-FA-RP-E2E-075-assign-user-ke-group-role-di-detail-role-3
title: "Assign User ke Group Role di Detail Role (3/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-261
  - TC-FA-RP-263
  - TC-FA-RP-1087
  - TC-FA-RP-1088
  - TC-FA-RP-1141
coverage:
  web: automated
---

# Assign User ke Group Role di Detail Role (3/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso, Dimas Pranata, ...), #17 (Hesti Rahma dan lainnya), #13 (Kevin Susanto Group Manager di `Data Center`; baris pola GM di `Data Center` dan `Rack A1`; baris non-pola: Group Role `Manage user & role` di `Data Center`, `Manage files` Read dan Delete di `Helpdesk`, Global Role `Manage accounting` hanya Read), #18 (pohon group). Pada TC-FA-RP-261 Ahmad Fauzi memegang `Manage asset & TAG` di `IT Infrastructure` (Read saja) dan di `Data Center` (Create, Read, Update), di-seed lewat seeding API.
- Sesi kedua: sesi API Total Control kedua (Pre-setup #3, Rina Wulandari, `Spectra.env.FA_TC2_PASSWORD`) menghapus group `Dock 1` pada TC-FA-RP-263; sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi.
- Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): daftar penugasan Group Role Budi Santoso dicatat sebagai baseline untuk TC-FA-RP-263.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC2_PASSWORD`, `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-261: Role sama di node induk dan turunan untuk user yang sama tampil sebagai dua baris dengan CRUD masing-masing

1. Klik Tab `System`
2. Buka Detail Role `Manage asset & TAG`
3. Klik `All Groups`
4. Ketik Search `Ahmad Fauzi`, tekan Enter
5. Verifikasi dua baris Ahmad Fauzi tampil: badge `IT Infrastructure` dengan hanya Read
6. Verifikasi baris Ahmad Fauzi dengan badge `Data Center` memuat Create, Read, dan Update
7. Verifikasi tabel tidak menggabungkan kedua baris Ahmad Fauzi
8. Klik `(←)` pada kotak Search

### TC-FA-RP-263: Assign Group Role ke group yang dihapus sesi lain: error inline di bawah field Group

9. Klik segmen `System` pada breadcrumb
10. Catat daftar penugasan Group Role Budi Santoso lewat fixture BE sebagai baseline
11. Pada sesi 1 buka Detail Role `Manage files`, klik `[+ Assign]`, pilih group `Dock 1`, centang Budi Santoso
12. Hapus group `Dock 1` lewat sesi API Total Control kedua (Rina Wulandari) hingga tersimpan
13. Pada sesi 1 klik `[Assign]`
14. Verifikasi pesan inline di bawah field Group: `This group no longer exists. Please select another.`
15. Verifikasi daftar penugasan Group Role Budi Santoso (fixture BE) sama dengan baseline: tidak ada penugasan tersimpan
16. Tutup popup lewat `✕`
17. Pulihkan group `Dock 1` lewat seeding API

### TC-FA-RP-1087: Popup Assign User Group Role dari All Groups: field Group kosong, Table User Picker kosong dan Disabled tanpa tooltip

18. Klik segmen `System` pada breadcrumb
19. Buka Detail Role `Manage files` dengan Sidebar pada `All Groups`
20. Klik `[+ Assign]`
21. Amati field Group dan Table User Picker
22. Hover Table User Picker
23. Verifikasi field Group kosong dengan placeholder `Select group`
24. Verifikasi Table User Picker kosong dan Disabled sampai Group dipilih
25. Verifikasi tidak ada tooltip pada Table User Picker
26. Pilih group `Data Center` pada field Group
27. Verifikasi Table User Picker terisi kandidat yang eligible untuk `Data Center`
28. Tutup popup lewat `✕`

### TC-FA-RP-1088: Mengubah nilai field Group popup Assign User Group Role mengosongkan seleksi user dan memuat ulang kandidat

29. Klik node `Data Center` di Sidebar Group Tree
30. Klik `[+ Assign]`
31. Centang Dimas Pranata dan Budi Santoso
32. Ubah field Group menjadi `Helpdesk`
33. Amati counter, daftar, dan header modal
34. Verifikasi seluruh pilihan user dikosongkan (counter tidak tampil)
35. Verifikasi daftar kandidat dimuat ulang untuk group `Helpdesk`
36. Verifikasi header modal menjadi `Assign User — Manage files (Helpdesk)`
37. Tutup popup lewat `✕`

### TC-FA-RP-1141: Popup Assign User Group Role oleh Total Control: target Group Manager tidak tampil pada node GM-nya maupun descendant, dan tampil di luar subtree

38. Klik `[+ Assign]`
39. Pilih group `Data Center`
40. Ketik Search `Kevin Susanto`, tekan Enter
41. Verifikasi Kevin Susanto tidak ada di daftar picker (node penugasan GM-nya sendiri; sudah memegang baris pola GM; eksklusi berlaku juga bagi aktor Total Control; empty state hasil Search)
42. Ubah group menjadi `Rack A1` lalu ganti isi kotak search dengan `Kevin Susanto`, tekan Enter
43. Verifikasi Kevin Susanto tidak ada di daftar picker (`Rack A1` adalah descendant dalam subtree penugasan GM-nya dan memegang baris pola GM; empty state hasil Search)
44. Ubah group menjadi `Helpdesk` lalu ganti isi kotak search dengan `Kevin Susanto`, tekan Enter
45. Verifikasi Kevin Susanto ada di daftar picker (`Helpdesk` di luar subtree)
46. Tutup popup lewat `✕`
47. Klik segmen `System` pada breadcrumb
48. Buka Detail Role `Manage user & role`
49. Klik `[+ Assign]` dan pilih group `Rack A1`
50. Ketik Search `Kevin Susanto`, tekan Enter
51. Verifikasi Kevin Susanto ada di daftar picker (`Manage user & role` bukan bagian pola GM dan Kevin Susanto tidak memegang baris itu di `Rack A1`)
52. Tutup popup lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 52 langkah.
- Langkah penghubung (S-03): langkah 1, 8–10, 16, 18, 28, 37, 46–47, 52. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 17; tidak ada `Verifikasi`.
- Search untuk menemukan baris target (R-16): langkah 4.
- TC-FA-RP-263 memakai dua sesi (Manual Only (d) di TC): sesi 2 adalah pelaku kedua yang hanya memicu penghapusan group sehingga memakai sesi API (suite.md; langkah ditulis "... hingga ... tersimpan", R-20), bukan konteks kedua kelas c. Group `Dock 1` dipulihkan di langkah 17 dan di hook `after`.
- Search pada TC-FA-RP-261 (langkah 4) menemukan baris Ahmad Fauzi pada tabel `All Groups` (R-16).
- Post Condition TC-FA-RP-263 (pemulihan group) tidak punya langkah observasi dan tidak diasersi.
- Temuan untuk QA:
  - TC-FA-RP-261 langkah 3 meminta mengamati baris Ahmad Fauzi tanpa Search; spec memakai Search sebagai langkah penghubung agar dua baris terlihat pada satu halaman.
  - TC-FA-RP-1088 langkah 1 memakai node `Data Center`; TC-FA-RP-1087 mensyaratkan Sidebar `All Groups` sebelum `[+ Assign]` sehingga Table User Picker Disabled sampai group dipilih.
  - TC-FA-RP-1141 langkah 6 tidak menyebut cara pindah dari Detail Role `Manage files` ke `Manage user & role`; spec memakai segmen `System` pada breadcrumb (sama dengan TC-FA-RP-1087).
  - TC-FA-RP-263 precondition d hanya menyebut "Dua sesi"; spec memakai sesi API Total Control kedua (Pre-setup #3).
- Ukuran spec (52 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
