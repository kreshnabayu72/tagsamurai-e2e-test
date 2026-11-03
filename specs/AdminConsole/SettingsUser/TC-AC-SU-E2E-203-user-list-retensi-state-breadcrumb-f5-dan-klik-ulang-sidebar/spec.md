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

1. Klik icon Search
2. Ketik Search `a`, tekan Enter
3. Klik icon Filter
4. Pilih Status `Active`, klik `[Apply]`
5. Klik header Email
6. Ubah page size ke 25
7. Klik Name `John Doe {runId}-203` untuk membuka Detail User
8. Klik segmen `User` di breadcrumb
9. Verifikasi keyword Search `a` tetap terisi
10. Verifikasi Filter Status `Active` tetap aktif
11. Verifikasi sort Email A-Z tetap berlaku
12. Verifikasi page size 25
13. Verifikasi halaman aktif sama seperti sebelum membuka Detail
14. Klik header Email dua kali sampai sort kembali ke default Name A-Z
15. Klik `[Clear Field]`, klik `[Apply]`
16. Klik `(←)` pada kotak Search
17. Ubah page size ke 10

### TC-AC-SU-324: State List termasuk node Sidebar Group dipertahankan setelah F5

18. Klik node Sidebar Group `Region A {runId}-203`
19. Klik icon Search
20. Ketik Search `a`, tekan Enter
21. Klik icon Filter
22. Pilih Status `Active`, klik `[Apply]`
23. Klik header Email
24. Klik next agar berada di halaman 2
25. Tekan F5
26. Verifikasi node Sidebar Group `Region A {runId}-203` tetap terpilih
27. Verifikasi keyword Search `a` tetap terisi
28. Verifikasi Filter Status `Active` tetap aktif
29. Verifikasi sort Email A-Z tetap berlaku
30. Verifikasi tabel tetap berada di halaman 2

### TC-AC-SU-325: Klik ulang menu sidebar mereset state List

31. Klik menu sidebar Settings > User
32. Verifikasi List kembali ke default: tanpa Search dan tanpa Filter
33. Verifikasi sort Name A-Z
34. Verifikasi halaman 1

## Notes

- Langkah penghubung (S-03): `[Clear Field]` lalu `[Apply]`, menutup Search, mengembalikan sort dan page size ke default di akhir TC-323 (S-09); TC-324 membiarkan state tersisa karena langkah terakhir TC-325 mereset seluruhnya dengan klik ulang menu sidebar.
- TC-325 mengandalkan state dari TC-324 (Search `a`, Filter Status `Active`, node Sidebar Group, sort Email) dan tidak membuat state baru; klik ulang menu sidebar mereset state List. Ketiga TC berada di spec yang sama karena itu.
- Pembagian TC User List Pagination dan retensi state: TC-AC-SU-321 dan 322 di spec 090; TC-AC-SU-323, 324, dan 325 di spec ini.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-203` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-323 mengklik Name `John Doe` untuk Detail; spec memakai `John Doe {runId}-203` milik spec yang berada di Region A.
  - TC-325 langkah 1 menyebut "Search `a`, Filter Status = Active" tanpa mengatur ulang; spec memakai state sisa TC-324 (S-04).
