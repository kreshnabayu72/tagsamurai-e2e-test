---
id: TC-AC-SU-E2E-051-sub-tab-group-role-screening-dan-sort-group
title: "Sub-tab Group Role: Screening Kolom dan Sort Kolom Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-194
  - TC-AC-SU-666
coverage:
  web: automated
---

# Sub-tab Group Role: Screening Kolom dan Sort Kolom Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-051` tanpa tingkat akses dan bukan Group Manager; Group Role: `Manage active client` aktif di `Region A {runId}-051`, `Manage allocation` tanpa group, `Manage archived client` aktif di `Branch 1 {runId}-051`, `Manage distributor` aktif di `Region A {runId}-051` dan `Branch 1 {runId}-051`, `Manage partner` aktif di `Region A {runId}-051`.
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-051`): `Region A {runId}-051` > `Branch 1 {runId}-051` > `Floor 1 {runId}-051`; `Region A {runId}-051` > `Branch 3 {runId}-051`; `Region B {runId}-051`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-051@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-051`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-051` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-194: Screening Sub-tab Group Role pada Detail User target standar

1. Ketik Search `Budi Santoso {runId}-051`, tekan Enter
2. Klik nama `Budi Santoso {runId}-051` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Amati sub-tab sebelum klik apa pun
5. Verifikasi Sub-tab: `Global Role | Group Role (aktif)`
6. Verifikasi toolbar: icon Changelog `[📋]` tampil
7. Verifikasi kolom tabel: `Role Name (sortable) | Group (sortable) | Column Visibility (⋯) (unsortable)`
8. Klik header `Column Visibility (⋯)`
9. Verifikasi overlay Column Visibility terbuka dengan CTA `[Setup Column]`
10. Tutup overlay dengan Esc
11. Verifikasi body per baris memuat row action `[Detail]` `[Assign Group]`
12. Verifikasi seluruh baris katalog Group Role entitas Principal tampil A-Z: `Manage active client`, `Manage allocation`, `Manage archived client`, `Manage distributor`, `Manage partner`, `Manage wallet & pricing`
13. Verifikasi kolom Group `Manage active client` = badge `Region A {runId}-051`
14. Verifikasi kolom Group `Manage allocation` = `—`
15. Verifikasi kolom Group `Manage archived client` = badge `Branch 1 {runId}-051`
16. Verifikasi tidak ada kolom Active (switch) di tabel utama
17. Verifikasi tidak ada kolom C/R/U/D di tabel utama
18. Verifikasi footer tidak ada pagination

### TC-AC-SU-666: Sub-tab Group Role: kolom Group sortable menurut jumlah group

19. Klik header `Group` sekali
20. Verifikasi `Manage partner` (1 group) tampil sebelum `Manage distributor` (2 group)
21. Verifikasi baris tanpa group (`Manage allocation` dan `Manage wallet & pricing`) berada di akhir, berurut Role Name A-Z
22. Klik header `Group` lagi
23. Verifikasi `Manage distributor` tampil sebelum `Manage partner`
24. Verifikasi baris tanpa group (`Manage allocation` dan `Manage wallet & pricing`) berada di awal, berurut Role Name A-Z

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 10 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- TC-194 dan TC-666 memakai satu user dengan gabungan role kedua TC; nilai yang diasersi tiap TC tetap sama dengan Expected TC (tiga baris yang disebut di TC-194 dan urutan jumlah group di TC-666).
- Pembagian TC: TC-AC-SU-195 sampai 200 dan 645 (screening, badge, empty) ada di spec 052 dan 053.
- Langkah penghubung klik header `Column Visibility (⋯)` (S-03): Expected TC-194 menyebut overlay Column Visibility pada header; TC tidak memberi langkah klik.
- Temuan untuk QA:
  - Expected TC-666 menyebut "Manage allocation dan role lain tanpa group"; spec memakai `Manage wallet & pricing` sebagai role lain tanpa group karena katalog Group Role hanya enam.
