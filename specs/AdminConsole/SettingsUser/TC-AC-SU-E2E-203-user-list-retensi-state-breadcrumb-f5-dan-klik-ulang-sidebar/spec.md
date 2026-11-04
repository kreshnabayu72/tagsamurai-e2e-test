---
id: TC-AC-SU-E2E-203-user-list-retensi-state-breadcrumb-f5-dan-klik-ulang-sidebar
title: "User List Retensi State: Breadcrumb dari Detail, F5 dengan Node Sidebar Group, dan Klik Ulang Sidebar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-323
  - TC-AC-SU-324
  - TC-AC-SU-325
coverage:
  web: automated
---

# User List Retensi State: Breadcrumb dari Detail, F5 dengan Node Sidebar Group, dan Klik Ulang Sidebar

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-203`): group `Region A {runId}-203`; `Anton 01 {runId}-203` sampai `Anton 12 {runId}-203` (Active, Activated, Division `Finance`, Group Role aktif di `Region A {runId}-203`); `John Doe {runId}-203` (Active, Activated, Division `Finance`, Group Role aktif di `Region A {runId}-203`). Seluruh user milik spec memuat teks `a` pada kolom Division; hasil Search `a` dan Filter Status `Active` memuat lebih dari 10 baris. Entitas memuat lebih dari 10 user.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### TC-AC-SU-323: State List dipertahankan saat kembali dari Detail via breadcrumb

1. Ketik Search `a`, tekan Enter
2. Klik icon Filter
3. Pilih Status `Active`, klik `[Apply]`
4. Klik header Email
5. Ubah page size ke 25
6. Klik Name `John Doe {runId}-203` untuk membuka Detail User
7. Klik segmen `User` di breadcrumb
8. Verifikasi keyword Search `a` tetap terisi
9. Verifikasi Filter Status `Active` tetap aktif
10. Verifikasi sort Email A-Z tetap berlaku
11. Verifikasi page size 25
12. Verifikasi halaman aktif sama seperti sebelum membuka Detail
13. Klik header Email dua kali sampai sort kembali ke default Name A-Z
14. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
15. Klik `(←)` pada kotak Search
16. Ubah page size ke 10

### TC-AC-SU-324: State List termasuk node Sidebar Group dipertahankan setelah F5

17. Klik node Sidebar Group `Region A {runId}-203`
18. Ketik Search `a`, tekan Enter
19. Klik icon Filter
20. Pilih Status `Active`, klik `[Apply]`
21. Klik header Email
22. Klik next agar berada di halaman 2
23. Tekan F5
24. Verifikasi node Sidebar Group `Region A {runId}-203` tetap terpilih
25. Verifikasi keyword Search `a` tetap terisi
26. Verifikasi Filter Status `Active` tetap aktif
27. Verifikasi sort Email A-Z tetap berlaku
28. Verifikasi tabel tetap berada di halaman 2

### TC-AC-SU-325: Klik ulang menu sidebar mereset state List

29. Klik menu sidebar Settings > User
30. Verifikasi List kembali ke default: tanpa Search dan tanpa Filter
31. Verifikasi sort Name A-Z
32. Verifikasi halaman 1

## Notes

- Langkah penghubung (S-03): `Klik icon Filter` lalu `[Clear Field]` dan `[Apply]` (Apply menutup panel), menutup Search, mengembalikan sort dan page size ke default di akhir TC-323 (S-09); TC-324 membiarkan state tersisa karena langkah terakhir TC-325 mereset seluruhnya dengan klik ulang menu sidebar.
- TC-325 mengandalkan state dari TC-324 (Search `a`, Filter Status `Active`, node Sidebar Group, sort Email) dan tidak membuat state baru; klik ulang menu sidebar mereset state List. Ketiga TC berada di spec yang sama karena itu.
- Pembagian TC User List Pagination dan retensi state: TC-AC-SU-321 dan 322 di spec 090; TC-AC-SU-323, 324, dan 325 di spec ini.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-203` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-323 mengklik Name `John Doe` untuk Detail; spec memakai `John Doe {runId}-203` milik spec yang berada di Region A.
  - TC-325 langkah 1 menyebut "Search `a`, Filter Status = Active" tanpa mengatur ulang; spec memakai state sisa TC-324 (S-04).
