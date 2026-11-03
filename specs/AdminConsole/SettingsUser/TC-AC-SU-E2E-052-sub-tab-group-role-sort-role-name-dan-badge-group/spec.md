---
id: TC-AC-SU-E2E-052-sub-tab-group-role-sort-role-name-dan-badge-group
title: "Sub-tab Group Role: Sort Role Name dan Group Summary Badge"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-195
  - TC-AC-SU-196
  - TC-AC-SU-197
coverage:
  web: automated
---

# Sub-tab Group Role: Sort Role Name dan Group Summary Badge

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-052` tanpa tingkat akses dan bukan Group Manager; Group Role: `Manage allocation` tanpa group, `Manage active client` aktif di `Region A {runId}-052`, `Manage partner` aktif di `Region B {runId}-052` dan `Branch 3 {runId}-052`, `Manage distributor` aktif di `Region A {runId}-052`, `Region B {runId}-052`, `Branch 1 {runId}-052`, `Branch 3 {runId}-052` (tidak di `Floor 1 {runId}-052`).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-052`): `Region A {runId}-052` > `Branch 1 {runId}-052` > `Floor 1 {runId}-052`; `Region A {runId}-052` > `Branch 3 {runId}-052`; `Region B {runId}-052`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-052@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-052`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-052` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-195: Sort kolom Role Name Group Role siklus 3-state

1. Ketik Search `Budi Santoso {runId}-052`, tekan Enter
2. Klik nama `Budi Santoso {runId}-052` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik header `Role Name` 1×
5. Verifikasi urutan A-Z (`Manage active client` teratas)
6. Verifikasi icon `↑` pada header `Role Name`
7. Klik header `Role Name` lagi 1×
8. Verifikasi urutan Z-A (`Manage wallet & pricing` teratas)
9. Verifikasi icon `↓` pada header `Role Name`
10. Klik header `Role Name` lagi 1×
11. Verifikasi urutan kembali ke default A-Z
12. Verifikasi tidak ada icon arah pada header `Role Name`

### TC-AC-SU-196: Group Summary Badge: 0, 1, dan 2 group

13. Amati kolom Group ketiga baris
14. Verifikasi `Manage allocation`: `—`
15. Verifikasi `Manage active client`: 1 badge `Region A {runId}-052`
16. Verifikasi `Manage partner`: 2 badge berurutan A-Z `Branch 3 {runId}-052`, `Region B {runId}-052`

### TC-AC-SU-197: Group Summary Badge: lebih dari 2 group dan popup +N more

17. Amati kolom Group baris `Manage distributor`
18. Verifikasi sel menampilkan 2 badge pertama A-Z `Branch 1 {runId}-052`, `Branch 3 {runId}-052` dan chip `+2 more`
19. Klik chip `+2 more`
20. Verifikasi popup daftar semua group terbuka berisi `Branch 1 {runId}-052`, `Branch 3 {runId}-052`, `Region A {runId}-052`, `Region B {runId}-052` (A-Z)
21. Verifikasi popup daftar group scrollable
22. Klik di luar popup
23. Verifikasi popup daftar group tertutup

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Pembagian TC: TC-AC-SU-194 dan 666 ada di spec 051; TC-AC-SU-198, 199, 200, 645 ada di spec 053.
- Group dan role berbeda untuk TC-196 dan TC-197 digabung dalam satu user; nilai yang diasersi mengikuti Expected tiap TC.
- Temuan untuk QA:
  - TC-195 mengasersi `Manage wallet & pricing` sebagai teratas pada Z-A; katalog Group Role pada TC-194 menyebut keenam role.
