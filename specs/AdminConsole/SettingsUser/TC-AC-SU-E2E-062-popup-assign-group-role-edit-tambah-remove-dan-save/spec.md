---
id: TC-AC-SU-E2E-062-popup-assign-group-role-edit-tambah-remove-dan-save
title: "Popup Assign Group Role: Edit CRUD, Tambah Group, Remove Pending, dan Remove Lalu Add Ulang"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-222
  - TC-AC-SU-223
  - TC-AC-SU-224
  - TC-AC-SU-225
coverage:
  web: automated
---

# Popup Assign Group Role: Edit CRUD, Tambah Group, Remove Pending, dan Remove Lalu Add Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-062` tanpa tingkat akses dan bukan Group Manager; `Manage wallet & pricing` aktif di `Region A {runId}-062` (C ☑ R ☑ U ☑) dan `Branch 3 {runId}-062` (R saja); `Manage partner` aktif di `Region A {runId}-062`.
- Data milik spec untuk TC-AC-SU-224 (seed lewat Fixture BE): `Budi Santoso B {runId}-062` tanpa tingkat akses dan bukan Group Manager; `Manage partner` aktif di `Region A {runId}-062` dan `Region B {runId}-062`.
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-062`): `Region A {runId}-062` > `Branch 1 {runId}-062` > `Floor 1 {runId}-062`; `Region A {runId}-062` > `Branch 3 {runId}-062`; `Region B {runId}-062`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-062@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-062`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-062` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-222: Edit CRUD satu group lalu Save: toast updated

1. Ketik Search `Budi Santoso {runId}-062`, tekan Enter
2. Klik nama `Budi Santoso {runId}-062` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage wallet & pricing`
5. Centang C baris `Branch 3 {runId}-062`
6. Klik `[Save]`
7. Verifikasi popup tertutup
8. Verifikasi muncul toast sukses: "Success, group role has been updated."
9. Klik `[Detail]` baris `Manage wallet & pricing`
10. Verifikasi popup Group Assignment menampilkan baris `Branch 3 {runId}-062`: C ☑ R ☑ U ○
11. Tutup popup dengan `[×]`

### TC-AC-SU-223: Tambah group baru lalu Save: toast assigned

12. Tunggu toast lama hilang otomatis
13. Klik `[Assign Group]` baris `Manage partner`
14. Klik `[+ Assign Group]`
15. Centang `Region B {runId}-062`, klik `[Select]`
16. Klik `[Save]`
17. Verifikasi popup tertutup
18. Verifikasi kolom Group `Manage partner`: 2 badge `Region A {runId}-062`, `Region B {runId}-062`
19. Verifikasi muncul toast sukses: "Success, group role has been assigned."

### TC-AC-SU-225: Remove lalu add ulang group yang sama dalam satu Save: CRUD tersimpan pulih dan no-op

20. Tunggu toast lama hilang otomatis
21. Klik `[Assign Group]` baris `Manage wallet & pricing`
22. Klik `[🗑]` baris `Region A {runId}-062`
23. Klik `[+ Assign Group]`, centang `Region A {runId}-062` (kini enabled), klik `[Select]`
24. Verifikasi baris `Region A {runId}-062` kembali dengan C `[☑]` R `[☑]` U `[☑]` (bukan default R saja)
25. Klik `[Save]`
26. Verifikasi popup tertutup
27. Verifikasi muncul toast `"No changes to save."`

### TC-AC-SU-224: Remove group via 🗑 bersifat pending sampai Save

28. Tunggu toast lama hilang otomatis
29. Buka Settings > User lewat sidebar
30. Ketik Search `Budi Santoso B {runId}-062`, tekan Enter
31. Klik nama `Budi Santoso B {runId}-062` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
32. Klik Sub-tab [Group Role]
33. Klik `[Assign Group]` baris `Manage partner`
34. Klik `[🗑]` baris `Region B {runId}-062`
35. Verifikasi baris `Region B {runId}-062` hilang dari tabel popup
36. Verifikasi kolom Group di halaman masih `Region A {runId}-062`, `Region B {runId}-062`
37. Klik `[Save]`
38. Verifikasi popup tertutup
39. Verifikasi kolom Group `Manage partner` = `Region A {runId}-062`
40. Verifikasi muncul toast sukses: "Success, group role has been updated."

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 11, 12, 20, 28, 29, 30 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Observasi `[Detail]` sesudah Save TC-222 adalah langkah observasi Post Condition TC itu ("popup `[Detail]` menampilkan C ☑ R ☑ U ○").
- Urutan TC di spec (S-05, S-10): 222, 223, 225, 224. TC-AC-SU-224 memakai user seed sendiri (`Budi Santoso B {runId}-062`) dan ditaruh terakhir supaya perpindahan user hanya sekali; TC-AC-SU-225 tidak bergantung pada TC-AC-SU-223 atau TC-AC-SU-224.
- Pembagian TC: TC-AC-SU-226 sampai 229 ada di spec 063.
- Alasan spec melewati sekitar 35 langkah: seluruh TC memakai satu permukaan (Popup Assign Group Role) pada halaman Detail user; tiap blok punya data seed yang cukup untuk dirinya sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Post Condition TC-222 butir b (Role & Permission), TC-223 ("Role Count bertambah 1"), dan TC-225 ("tidak ada entri baru di Tab Changelog, System Log aktor, dan Activity Log") tidak punya langkah observasi di TC dan tidak diasersi.
