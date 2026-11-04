---
id: TC-AC-SU-E2E-078-user-list-filter-panel-role-date-range-or-and-chip
title: "User List Filter Panel: Role, Date Range, OR dan AND, Hapus Chip, dan Activation Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-275
  - TC-AC-SU-276
  - TC-AC-SU-277
  - TC-AC-SU-278
  - TC-AC-SU-649
coverage:
  web: automated
---

# User List Filter Panel: Role, Date Range, OR dan AND, Hapus Chip, dan Activation Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-078`): `John Doe {runId}-078` (Active, Activated, Global Role `Manage group` aktif, Position `HR Business Partner`), `Jane Smith {runId}-078` (Inactive, Activated, Global Role `Manage group` switch OFF, Position `Finance Manager`, Last Updated hari seeding), `Dewi Lestari {runId}-078` dan `Rina Putri {runId}-078` (Total Control; `Rina Putri {runId}-078` Pending Email Confirmation), `Mike Tan {runId}-078` (Active, Pending Activation), `Sarah Lee {runId}-078` (Inactive, Pending Activation), `Budi Santoso {runId}-078` (Pending Email Confirmation), `Andi Wijaya {runId}-078` (Active, Temporary User `Yes`, Temporary Until terisi). Baris Default User Principal (Pre-setup #1) dipakai apa adanya dan tidak diubah.
- Fixture `Fixture.settingsUser` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `defaultUserName` (nama tampil baris Default User Principal, Pre-setup #1).
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-275: Filter Role mencocokkan role aktif; user TC/RO hanya lewat opsi tier

1. Klik icon Filter
2. Pilih Role `Manage group`, klik `[Apply]`
3. Verifikasi baris `John Doe {runId}-078` tampil
4. Verifikasi baris `Jane Smith {runId}-078` dan `Dewi Lestari {runId}-078` tidak tampil
5. Klik icon Filter
6. Ganti pilihan Role menjadi `Total Control`, klik `[Apply]`
7. Verifikasi baris `Fixture.settingsUser.defaultUserName`, `Dewi Lestari {runId}-078`, dan `Rina Putri {runId}-078` tampil
8. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-SU-276: Filter kelas date range (Last Updated, Temporary Until) inklusif

9. Klik `⋯` pada header Actions
10. Klik `[Setup Column]`
11. Centang kolom `Temporary Until` pada Setup Column
12. Klik `[Save]`
13. Baca tanggal Last Updated baris `Jane Smith {runId}-078`
14. Klik icon Filter
15. Atur Last Updated: Start dan End sama dengan tanggal tersebut
16. Verifikasi input Last Updated menampilkan tanggal sesuai Date Format General Settings
17. Klik `[Apply]`
18. Verifikasi baris `Jane Smith {runId}-078` tampil (batas inklusif)
19. Klik icon Filter, klik `[Clear Field]`
20. Atur Temporary Until: rentang yang memuat Temporary Until baris `Andi Wijaya {runId}-078`, klik `[Apply]`
21. Verifikasi baris `Andi Wijaya {runId}-078` tampil
22. Verifikasi baris `John Doe {runId}-078` tidak tampil
23. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-SU-277: OR di dalam satu field vs AND antar field

24. Klik icon Filter
25. Pilih Status `Active` dan `Inactive`, klik `[Apply]`
26. Verifikasi baris `John Doe {runId}-078` (Active) dan `Jane Smith {runId}-078` (Inactive) tampil
27. Klik icon Filter
28. Tambah Activation Status `Pending Activation`, klik `[Apply]`
29. Verifikasi baris `Mike Tan {runId}-078` dan `Sarah Lee {runId}-078` tampil
30. Verifikasi baris `John Doe {runId}-078` dan `Jane Smith {runId}-078` tidak tampil
31. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-SU-278: Hapus chip opsi via (X) pada chip

32. Klik icon Filter
33. Pilih Position `Finance Manager` dan `HR Business Partner`
34. Verifikasi dua chip tampil di dalam field Position
35. Klik (X) pada chip `Finance Manager`
36. Verifikasi chip `Finance Manager` hilang
37. Verifikasi chip `HR Business Partner` tetap
38. Buka dropdown Position
39. Verifikasi checkbox `Finance Manager` ter-uncheck
40. Tutup dropdown, klik `[Apply]`
41. Verifikasi baris `John Doe {runId}-078` (Position `HR Business Partner`) tampil
42. Verifikasi baris `Jane Smith {runId}-078` (Position `Finance Manager`) tidak tampil
43. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-SU-649: Filter Activation Status memperlakukan Pending Email Confirmation sebagai nilai tersendiri

44. Klik `⋯` pada header Actions
45. Klik `[Setup Column]`
46. Centang kolom `Activation Status` pada Setup Column
47. Klik `[Save]`
48. Klik icon Filter
49. Pilih Activation Status `Activated`, klik `[Apply]`
50. Verifikasi baris `John Doe {runId}-078` (Activated) tampil
51. Verifikasi baris `Rina Putri {runId}-078` dan `Budi Santoso {runId}-078` tidak tampil
52. Klik icon Filter
53. Ganti pilihan Activation Status menjadi `Pending Email Confirmation`, klik `[Apply]`
54. Verifikasi baris `Rina Putri {runId}-078` dan `Budi Santoso {runId}-078` tampil
55. Verifikasi baris `John Doe {runId}-078` tidak tampil
56. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): `[Apply]` menutup Filter Panel, sehingga tiap perubahan Filter sesudah Apply diawali `Klik icon Filter`; `[Clear Field]` lalu `[Apply]` di akhir tiap TC melepas filter supaya TC berikutnya tidak mewarisi kriteria (S-09); langkah Setup Column di TC-276 dan TC-649 memenuhi precondition TC dan konfigurasi kolomnya dipulihkan hook `after`.
- Alasan di atas ±35 langkah: kelima TC adalah Filter Panel User List kelas fungsional, dataset sama, berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-078` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-276 tidak menyatakan Temporary Until harus ditampilkan sebelum dipakai di Filter; spec menampilkannya lewat Setup Column sebagai langkah penghubung.
  - TC-275 menyebut Default User ikut hasil `Total Control` tanpa nama baris; spec memakai baris Default User Principal (Pre-setup #1) tanpa mengubahnya.
