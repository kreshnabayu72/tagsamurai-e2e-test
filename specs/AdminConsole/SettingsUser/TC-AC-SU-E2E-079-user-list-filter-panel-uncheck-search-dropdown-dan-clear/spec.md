---
id: TC-AC-SU-E2E-079-user-list-filter-panel-uncheck-search-dropdown-dan-clear
title: "User List Filter Panel: Uncheck di Dropdown, Search Dropdown, Clear Field, dan Custom Field Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-279
  - TC-AC-SU-280
  - TC-AC-SU-281
  - TC-AC-SU-282
coverage:
  web: automated
---

# User List Filter Panel: Uncheck di Dropdown, Search Dropdown, Clear Field, dan Custom Field Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-079`): `John Doe {runId}-079` (Active, Division `Finance`, Role aktif `Manage group`, Custom Field `Shift` = `Day`), `Jane Smith {runId}-079` (Inactive, Custom Field `Shift` = `Night`), `Mike Tan {runId}-079` (Active, Division `IT Operations`). Custom Field Pre-setup `Shift` (Dropdown: `Day`, `Night`) berstatus Active (Pre-setup #10) dan tidak diubah.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### TC-AC-SU-279: Hapus opsi via uncheck di dalam dropdown

1. Klik icon Filter
2. Pilih Division `IT Operations` dan `Finance`
3. Buka dropdown Division, hapus centang `Finance`
4. Verifikasi chip `Finance` hilang
5. Verifikasi chip `IT Operations` tetap
6. Tutup dropdown, klik `[Apply]`
7. Verifikasi baris `Mike Tan {runId}-079` (Division `IT Operations`) tampil
8. Verifikasi baris `John Doe {runId}-079` (Division `Finance`) tidak tampil
9. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-SU-280: Search internal dropdown filter

10. Buka dropdown Role, ketik `MANAGE`
11. Verifikasi opsi `Manage group` tampil
12. Verifikasi opsi yang tidak memuat `manage` (mis. `Total Control`) tidak tampil (case-insensitive)
13. Ganti ketikan menjadi `xyz`
14. Verifikasi tidak ada opsi yang tampil
15. Verifikasi empty state dropdown tampil
16. Tutup dropdown

### TC-AC-SU-281: `[Clear Field]` di Filter Panel lalu Apply

17. Pilih Status `Inactive`, klik `[Apply]`
18. Verifikasi baris `Jane Smith {runId}-079` (Inactive) tampil
19. Verifikasi baris `John Doe {runId}-079` (Active) tidak tampil
20. Klik `[Clear Field]`
21. Verifikasi semua field Filter Panel kembali ke placeholder
22. Verifikasi tabel masih tersaring Inactive (baris `John Doe {runId}-079` tidak tampil)
23. Klik `[Apply]`
24. Verifikasi seluruh baris tampil (baris `John Doe {runId}-079` dan `Jane Smith {runId}-079` tampil)
25. Verifikasi button Filter kembali ke state normal

### TC-AC-SU-282: Filter Custom Field aktif bertipe Dropdown (`Shift`)

26. Pilih field `Shift` = `Night`, klik `[Apply]`
27. Verifikasi baris `Jane Smith {runId}-079` (Night) tampil
28. Verifikasi baris `John Doe {runId}-079` (Day) tidak tampil
29. Klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): `[Clear Field]` lalu `[Apply]` dan menutup dropdown di akhir tiap TC mengembalikan Filter Panel ke keadaan bersih (S-09).
- TC-279, TC-280, dan TC-281 memakai Filter Panel yang dibuka pada langkah pertama TC-279 tanpa menutupnya; Filter Panel tetap terbuka sampai akhir spec.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-079` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-282 tidak menyatakan apakah field `Shift` pada Filter Panel muncul tanpa kolom `Shift` ditampilkan lewat Setup Column (TC-272 menampilkan kolom curated lebih dulu); spec tidak menampilkan kolom dan mengikuti TC.
