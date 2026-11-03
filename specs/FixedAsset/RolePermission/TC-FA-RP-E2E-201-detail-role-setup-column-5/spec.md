---
id: TC-FA-RP-E2E-201-detail-role-setup-column-5
title: "Detail Role: Setup Column (5/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-654
  - TC-FA-RP-655
  - TC-FA-RP-656
  - TC-FA-RP-1006
coverage:
  web: automated
---

# Detail Role: Setup Column (5/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, enam baris: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata) dan #18 (pohon group). Tidak diubah spec ini.
- Pre-setup #22 (Custom Field aktif `Cost Center` `CC-100`/`CC-200`, `Joined Date`, `Badge No`; Ahmad Fauzi `CC-100`, 10/01/26, `BN-77`; Budi Santoso `CC-200`, 15/02/26, `BN-88`).
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-654: Guard satu kolom tersisa pada Setup Column Detail Role

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
5. Hapus centang semua kolom kecuali satu (hapus centang `Group`, `Position`, dan `Division`, sisakan `Name`)
6. Arahkan kursor ke checkbox kolom terakhir (`Name`)
7. Verifikasi checkbox kolom terakhir Disabled dengan tooltip `At least one column must remain visible.`
8. Tutup popup Setup Column dengan klik `(X)`

### TC-FA-RP-655: Konfigurasi kolom Detail Role tidak memengaruhi tabel lain

9. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
10. Hapus centang kolom `Division` lalu klik `[Save]`
11. Klik segmen `System` pada Breadcrumb lalu klik Tab `Total Control`
12. Verifikasi tabel Tab `Total Control` memakai konfigurasi kolomnya sendiri (kolom bawaan `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated` tetap tampil)
13. Klik Tab `System`
14. Klik Role Name `Manage files` pada section Group Role
15. Klik `All Groups` di Sidebar Group Tree

### TC-FA-RP-656: Kolom matriks CRUD, Checkbox, dan Actions tidak masuk Setup Column dan selalu tampil

16. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
17. Verifikasi daftar Setup Column memuat kolom `Name`, `Group`, `Position`, `Division`, dan kolom curated
18. Verifikasi daftar Setup Column tidak memuat `Create`, `Read`, `Update`, `Delete`, Checkbox, maupun Actions
19. Hapus centang `Group`, `Position`, dan `Division` (sisakan `Name`) lalu klik `[Save]`
20. Verifikasi kolom CRUD dan Checkbox tetap tampil permanen setelah Save
21. Buka popup Setup Column, centang kembali `Group`, `Position`, dan `Division`, lalu klik `[Save]` (pemulihan kolom bawaan)

### TC-FA-RP-1006: Setup Column Detail Role Global Role: daftar kolom tanpa Group

22. Klik segmen `System` pada Breadcrumb
23. Klik Role Name `Manage accounting` pada section Global Role
24. Klik header `(⋯)`
25. Klik `Setup Column...`
26. Verifikasi kolom kelas Hideable tercentang: `Name`, `Position`, `Division`
27. Verifikasi kolom kelas Curated tidak tercentang: `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, `Badge No`
28. Verifikasi tidak ada kolom `Group` pada daftar
29. Verifikasi kolom Create, Read, Update, Delete, Checkbox, dan Actions tidak terdaftar
30. Tutup popup Setup Column dengan klik `(X)`

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-654, 655, 656, 1006). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 8, 13, 21, 22, 30.
- Temuan untuk QA:
  - TC-FA-RP-655 memberi pilihan "tab lain atau modal Changelog" tanpa menyebut konfigurasi kolom tabel lain; spec memakai Tab `Total Control` dengan kolom bawaannya (TC-FA-RP-74).
  - TC-FA-RP-656 tidak menyebut kolom yang disisakan; spec menyisakan `Name`. Expected a (daftar tidak memuat kolom CRUD) tidak punya anchor positif di TC; spec menambah Verifikasi daftar kolom Setup Column sebagai anchor (Notes S-03).
  - TC-FA-RP-1006 Precondition merujuk Pre-setup #22, tetapi hanya mengasersi daftar kolom Setup Column Global Role `Manage accounting`.
