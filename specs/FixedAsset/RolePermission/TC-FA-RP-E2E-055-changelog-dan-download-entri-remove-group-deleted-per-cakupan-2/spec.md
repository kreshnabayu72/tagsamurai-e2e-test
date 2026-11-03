---
id: TC-FA-RP-E2E-055-changelog-dan-download-entri-remove-group-deleted-per-cakupan-2
title: "Changelog dan Download entri Remove (Group Deleted) per cakupan aktor (2/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1112
  - TC-FA-RP-1116
  - TC-FA-RP-1120
coverage:
  web: automated
---

# Changelog dan Download entri Remove (Group Deleted) per cakupan aktor (2/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login akun pertama di hook `before`; akun berikutnya lewat langkah ganti akun eksplisit):

| Urutan | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| 1 | Group Manager (`IT Infrastructure`) | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
| 2 | Manage user & role (Group, Update, `IT Infrastructure`) | Gita Maharani (Pre-setup #7) | `murGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #43 (Fajar Nugroho Group Manager di `IT Infrastructure`, Kevin Susanto di `Data Center`, Lina Marlina di `Head Office`), #39 (Detail Role Group Role `Manage files` terisi: Ahmad Fauzi di `Data Center`, Budi Santoso di `Helpdesk`, Citra Lestari di `Head Office`, Endah Susanti di `Rack A1`, Fitri Handayani di `Dock 1`), #18 (pohon group), #24 (Company Changelog). Pre-setup dianggap utuh pada awal tiap blok (Catatan TC).
- Kemampuan teknis: sesi API Total Control (Pre-setup #2) untuk menghapus, mengganti nama, dan memulihkan group; pembaca berkas unduhan CSV (disediakan tim FE/BE); hook `after` memulihkan group yang dihapus atau diganti namanya spec ini.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_GM_PASSWORD`, `FA_MUR_GROUP_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1120: Changelog dan Download Tab Group Manager bagi Group Manager: entri Remove (Group Deleted) tetap tampil dengan nama group tersimpan setelah ancestor pada path tersimpan di-rename

1. Klik Tab `Group Manager`
2. Hapus group `Data Center` lewat sesi API Total Control hingga tersimpan; log memuat entri `Remove (Group Deleted)` `Kevin Susanto — Data Center` dengan path tersimpan `Head Office > IT Infrastructure > Data Center`; kemudian ganti nama group `IT Infrastructure` menjadi `IT Infrastructure Renamed {runId}-055` hingga tersimpan; tidak ada group lain yang dihapus
3. Klik ikon Changelog di toolbar Tab Group Manager
4. Amati entri modal
5. Verifikasi modal memuat entri Action `Remove (Group Deleted)` dengan User Name — Group Name `Kevin Susanto — Data Center`, Field `Group Manager`, Old Value `Assigned`, New Value `—`
6. Verifikasi entri tetap tampil: ancestor `IT Infrastructure` pada path tersimpan tetap dikenali sebagai group yang dikelola aktor karena pencocokan memakai ID, bukan nama, walau group sudah di-rename
7. Tutup modal
8. Unduh Changelog sebagai CSV
9. Verifikasi file Download memuat baris yang sama dengan modal
10. Verifikasi file Download memuat baris `Kevin Susanto — Data Center`
11. Pulihkan group `Data Center` dan pulihkan nama group `IT Infrastructure` lewat seeding API
12. Logout dari akun Group Manager (Fajar Nugroho)
13. Login sebagai Manage user & role (Group, Update) (`murGroup_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_MUR_GROUP_PASSWORD`)
14. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `System`

### TC-FA-RP-1112: Changelog dan Download Detail Role Group Role bagi Manage user & role (Group, Update): entri Remove (Group Deleted) tetap tampil dengan nama group tersimpan

15. Hapus group `Data Center` lewat sesi API Total Control hingga tersimpan; log Detail Role `Manage files` memuat entri `Remove (Group Deleted)` untuk Ahmad Fauzi dengan path tersimpan `Head Office > IT Infrastructure > Data Center` dan entri `Manage files` untuk Citra Lestari di `Head Office`
16. Buka Detail Role `Manage files` pada section Group Role
17. Klik ikon Changelog pada toolbar
18. Amati entri modal
19. Verifikasi modal memuat entri Action `Remove (Group Deleted)` dengan Role Name — User `Manage files — Ahmad Fauzi — Data Center`, Field `Access`, Old Value `Assigned`, New Value `—`
20. Verifikasi nama group `Data Center` tampil dari nama tersimpan pada entri; entri tampil karena path tersimpan memuat `IT Infrastructure` dalam cakupan aktor
21. Verifikasi entri `Manage files` untuk Citra Lestari di `Head Office` tidak tampil karena di luar cakupan `IT Infrastructure`
22. Tutup modal
23. Unduh Changelog sebagai CSV
24. Verifikasi file Download memuat baris yang sama dengan modal
25. Verifikasi file Download memuat baris `Remove (Group Deleted)` dengan nama group `Data Center`
26. Pulihkan group `Data Center` lewat seeding API

### TC-FA-RP-1116: Changelog dan Download Detail Role Group Role bagi Manage user & role (Group, Update): entri Remove (Group Deleted) untuk group yang semula di luar cakupan aktor tidak tampil

27. Hapus group `Data Center` dan group `Dock 1` (di bawah `Logistics Warehouse`) lewat sesi API Total Control hingga tersimpan; log Detail Role `Manage files` memuat entri `Remove (Group Deleted)` untuk Ahmad Fauzi (`Data Center`) dan Fitri Handayani (`Dock 1`) dengan path tersimpan `Head Office > IT Infrastructure > Data Center` dan `Head Office > Logistics Warehouse > Dock 1`
28. Buka Detail Role `Manage files` pada section Group Role
29. Klik ikon Changelog pada toolbar
30. Amati entri modal
31. Verifikasi modal memuat entri `Remove (Group Deleted)` dengan Role Name — User `Manage files — Ahmad Fauzi — Data Center` (group semula berada di bawah cakupan)
32. Verifikasi entri `Remove (Group Deleted)` untuk Fitri Handayani di `Dock 1` tidak tampil karena path tersimpan `Head Office > Logistics Warehouse > Dock 1` tidak memuat group dalam cakupan aktor
33. Tutup modal
34. Unduh Changelog sebagai CSV
35. Verifikasi file Download memuat baris yang sama dengan modal, dan baris Ahmad Fauzi ada
36. Verifikasi tidak ada baris di file Download yang menyebut `Fitri Handayani` atau `Dock 1`
37. Pulihkan group `Data Center` dan `Dock 1` lewat seeding API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 37 langkah.
- Langkah penghubung (S-03): langkah 1, 7, 12–14, 22, 33. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 2, 11, 15, 26–27, 37; tidak ada `Verifikasi`.
- Penyimpangan urutan (S-05 catatan urutan): TC-FA-RP-1120 (aktor Group Manager) dijalankan lebih dulu, lalu TC-FA-RP-1112 dan 1116 (aktor Manage user & role) agar ganti akun hanya sekali. Ganti akun ada di langkah 12–14 (login akun pertama di hook `before`).
- Pembagian TC lintas spec: TC-FA-RP-1111 dan 1115 ada di spec 054; TC-FA-RP-1118 dan 1119 ada di spec 299.
- Absence entri pada TC-FA-RP-1112 dan 1116 didahului `Verifikasi` entri lain pada modal yang sama (anchor positif, butir 8b.2).
- Temuan untuk QA:
  - TC-FA-RP-1112, 1116, 1120: precondition d menyebut group "sudah dihapus" dan "di-rename" di Settings > Groups tanpa pelaku dan nama baru; spec menulisnya lewat sesi API Total Control dan nama `IT Infrastructure Renamed {runId}-055` (kemampuan disediakan tim FE/BE).
  - Entri `Remove (Group Deleted)` bersifat audit trail permanen; asersi absence TC-FA-RP-1116 (`Fitri Handayani`, `Dock 1`) mengandalkan Catatan TC bahwa Pre-setup #24 utuh pada awal tiap TC (seed ulang log disediakan tim FE/BE).
  - Post Condition ketiga TC (pemulihan group) tidak punya langkah observasi dan tidak diasersi.
- Ukuran spec (37 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
