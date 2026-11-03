---
id: TC-AC-SU-E2E-061-popup-assign-group-role-select-group-cancel-search-dan-semua-ter-assign
title: "Popup Assign Group Role: Select Group Menambah Baris, Cancel, Search Tree, dan Semua Node Ter-assign"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-218
  - TC-AC-SU-219
  - TC-AC-SU-220
  - TC-AC-SU-221
coverage:
  web: automated
---

# Popup Assign Group Role: Select Group Menambah Baris, Cancel, Search Tree, dan Semua Node Ter-assign

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-061` (tanpa tingkat akses dan bukan Group Manager) dengan `Manage partner` aktif di `Region A {runId}-061` saja (TC-218, 219, 220); `Dewi Lestari {runId}-061` tanpa tingkat akses dan bukan Group Manager dengan `Manage partner` aktif di kelima group (TC-221).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-061`): `Region A {runId}-061` > `Branch 1 {runId}-061` > `Floor 1 {runId}-061`; `Region A {runId}-061` > `Branch 3 {runId}-061`; `Region B {runId}-061`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-061@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-061`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-061` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-218: Select Group menambahkan group dengan R checked dan C/U/D unchecked

1. Ketik Search `Budi Santoso {runId}-061`, tekan Enter
2. Klik nama `Budi Santoso {runId}-061` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage partner`
5. Klik `[+ Assign Group]`
6. Centang `Branch 1 {runId}-061` dan `Region B {runId}-061`, klik `[Select]`
7. Verifikasi Popup Select Group tertutup, kembali ke Popup Assign Group Role
8. Verifikasi baris baru `Branch 1 {runId}-061` dan `Region B {runId}-061`: R `[☑]` disabled, C/U/D `[☐]`
9. Verifikasi belum ada toast (belum tersimpan)
10. Klik `✕` pada popup
11. Verifikasi dialog `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` `[Leave]`
12. Klik `[Leave]`

### TC-AC-SU-219: Cancel di Popup Select Group tidak menambah baris

13. Klik `[Assign Group]` baris `Manage partner`
14. Klik `[+ Assign Group]`
15. Centang `Region B {runId}-061`
16. Klik `[Cancel]`
17. Verifikasi kembali ke Popup Assign Group Role
18. Verifikasi tabel tetap hanya `Region A {runId}-061`
19. Tutup popup dengan `[×]`

### TC-AC-SU-220: Search tree di Popup Select Group termasuk node disabled dan tanpa hasil

20. Klik `[Assign Group]` baris `Manage partner`
21. Klik `[+ Assign Group]`
22. Ketik Search `region`, tekan Enter
23. Verifikasi `Region A {runId}-061` tampil (tetap disabled)
24. Verifikasi `Region B {runId}-061` tampil
25. Ganti isi kotak search dengan `xyz`, tekan Enter
26. Verifikasi empty state Title `No results found` + Description `Try adjusting your search or filter.`
27. Klik `[Cancel]` di Popup Select Group, lalu `[×]` pada Popup Assign Group Role

### TC-AC-SU-221: Semua node sudah ter-assign: tree tetap tampil dan Select disabled

28. Klik Breadcrumb Settings > User untuk kembali ke User List
29. Ketik Search `Dewi Lestari {runId}-061`, tekan Enter
30. Klik nama `Dewi Lestari {runId}-061` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
31. Klik Sub-tab [Group Role]
32. Klik `[Assign Group]` baris `Manage partner`
33. Klik `[+ Assign Group]`
34. Verifikasi seluruh node tampil disabled
35. Verifikasi `[Select]` tampil namun disabled
36. Klik `[Cancel]` di Popup Select Group, lalu `[×]` pada Popup Assign Group Role

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 19, 27, 28, 29, 36 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Pembagian TC: TC-AC-SU-214 sampai 217 ada di spec 060.
- TC-221 memakai `Dewi Lestari {runId}-061` terpisah karena `Manage partner` aktif di kelima group tidak sejalan dengan `Manage partner` hanya `Region A {runId}-061` pada TC-218 sampai 220.
- Alasan spec melewati sekitar 35 langkah: seluruh TC memakai satu permukaan (Popup Select Group dari Popup Assign Group Role) dan berdiri sendiri; tidak ada perubahan data tersimpan sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Penutupan Popup Assign Group Role pada TC-218 memakai `✕` dan dialog Unsaved Changes `[Leave]` karena baris baru membuat popup dirty (S-08).
