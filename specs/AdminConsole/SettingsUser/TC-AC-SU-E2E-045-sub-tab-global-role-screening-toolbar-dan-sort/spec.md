---
id: TC-AC-SU-E2E-045-sub-tab-global-role-screening-toolbar-dan-sort
title: "Sub-tab Global Role: Screening, Tooltip Changelog, dan Header Tidak Bisa Di-sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-170
  - TC-AC-SU-171
  - TC-AC-SU-172
coverage:
  web: automated
---

# Sub-tab Global Role: Screening, Tooltip Changelog, dan Header Tidak Bisa Di-sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-045` tanpa tingkat akses dan bukan Group Manager; Global Role: `Manage device master data` ON (C ☐ R ☑ U ☐ D ☐), `Manage group` ON (C ☐ R ☑ U ☑ D ☑), `Manage hardware stock` ON (C ☑ R ☑ D ☐), `Manage TAG stock` OFF; role lain OFF.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-045@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-045`.
- Tabel "Header yang diklik" (TC-172): `Role Name`, `C`, `R`, `U`, `D`, `Active`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-045` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-170: Screening Sub-tab Global Role pada Detail User target standar

1. Ketik Search `Budi Santoso {runId}-045`, tekan Enter
2. Klik nama `Budi Santoso {runId}-045` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Amati Tab Role sebelum klik apa pun
4. Verifikasi Sub-tab: `Global Role (aktif) | Group Role`
5. Verifikasi tidak ada banner pada header Tab Role (target tanpa tingkat akses dan bukan Group Manager)
6. Verifikasi toolbar: icon Changelog `[📋]` tampil
7. Verifikasi kolom tabel: `Active | Role Name | C | R | U | D | Column Visibility (⋯)`, seluruhnya unsortable
8. Klik header `Column Visibility (⋯)`
9. Verifikasi overlay Column Visibility terbuka dengan CTA `[Setup Column]`
10. Verifikasi baris tabel tanpa row action
11. Tutup overlay dengan Esc
12. Verifikasi switch berada di kolom paling kiri
13. Verifikasi seluruh baris katalog Global Role entitas Principal tampil berurutan A-Z: `Manage device master data`, `Manage group`, `Manage hardware stock`, `Manage language`, `Manage plans & licensing`, `Manage preload`, `Manage presetup`, `Manage privacy policy`, `Manage TAG stock`, `Manage user and role`
14. Verifikasi baris `Manage device master data`: C `[☐]`, R `[☑]` disabled, U `[☐]`, D `[☐]`
15. Verifikasi baris `Manage hardware stock`: U tampil `—` tanpa bracket (bukan checkbox)
16. Verifikasi baris `Manage TAG stock` (OFF): C/R/U/D tampil `[─]` terkunci
17. Verifikasi footer tidak ada pagination
18. Verifikasi footer tidak ada tombol Save

### TC-AC-SU-171: Hover icon Changelog di toolbar Sub-tab Global Role lalu klik

19. Hover icon `[📋]` di toolbar Sub-tab Global Role
20. Verifikasi tooltip `"Changelog"` tampil
21. Klik icon `[📋]`
22. Verifikasi modal `"Changelog: User > Global Role"` terbuka
23. Tutup modal Changelog dengan `✕`

### TC-AC-SU-172: Header kolom Global Role tidak bisa di-sort

24. Untuk setiap header pada tabel "Header yang diklik" di Prerequisites (langkah 24 sampai 25): klik header tersebut
25. Verifikasi urutan baris tetap A-Z by Role Name
26. Verifikasi tidak ada icon sort di header kolom mana pun

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 11, 23 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Langkah 24 sampai 25 diulang untuk tiap header pada tabel "Header yang diklik" (bagian 8b butir 7); `Verifikasi` urutan tetap satu per iterasi.
- Pembagian TC lintas spec: TC-AC-SU-176, 179, 180 (guard Sub-tab Global Role) ada di spec 046.
- Temuan untuk QA:
  - TC-170 menyebut kolom Column Visibility (⋯) "header klik = buka overlay Column Visibility → CTA [Setup Column], tanpa row action"; spec menambah satu klik pada header itu untuk mengamati overlay (S-03).
