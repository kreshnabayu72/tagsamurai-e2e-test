---
id: TC-AC-SU-E2E-082-user-list-kombinasi-search-filter-sort-bagian-2
title: "User List Kombinasi Search, Filter, Sort, dan Page Size (bagian 2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-290
  - TC-AC-SU-291
  - TC-AC-SU-292
  - TC-AC-SU-293
coverage:
  web: automated
---

# User List Kombinasi Search, Filter, Sort, dan Page Size (bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-082`): `John Doe {runId}-082` (Active, Activated, Position `Staff`, Email `a.john@{runId}-082.qwertysystem.net`), `Mike Tan {runId}-082` (Active, Activated, Position `Analyst`, Email `b.mike@{runId}-082.qwertysystem.net`), `Jane Smith {runId}-082` (Inactive, Position `Manager`, Email `c.jane@{runId}-082.qwertysystem.net`). Semua kolom pada user memuat teks `a`.
- State yang diubah TC-293: `John Doe {runId}-082` dinonaktifkan; pemulihan Active dijalankan hook `after` lewat Fixture BE (TC tidak memberi langkah pemulihan UI).
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### TC-AC-SU-290: Clear Search saat Filter dan Sort aktif

1. Klik icon Filter
2. Pilih Status `Active`, klik `[Apply]`
3. Klik header Name dua kali (Z-A)
4. Klik icon Search
5. Ketik Search `john`, tekan Enter
6. Klik `✕` pada Search, tekan Enter
7. Verifikasi baris `Mike Tan {runId}-082` tampil sebelum `John Doe {runId}-082` (sort Name Z-A tetap)
8. Verifikasi baris `John Doe {runId}-082` dan `Mike Tan {runId}-082` (Active) tampil
9. Verifikasi baris `Jane Smith {runId}-082` (Inactive) tidak tampil (filter Active tetap)
10. Klik header Name sekali sampai sort kembali ke default Name A-Z
11. Klik `[Clear Field]`, klik `[Apply]`
12. Klik `(←)` pada kotak Search

### TC-AC-SU-291: Ganti target sort saat Search dan Filter aktif

13. Klik icon Search
14. Ketik Search `a`, tekan Enter
15. Klik icon Filter
16. Pilih Status `Active`, klik `[Apply]`
17. Klik header Email
18. Klik header Position
19. Verifikasi baris `Mike Tan {runId}-082` (Position `Analyst`) tampil sebelum `John Doe {runId}-082` (Position `Staff`) (sort pindah ke Position A-Z)
20. Verifikasi ikon sort Email kembali netral
21. Verifikasi keyword search tetap `a`
22. Verifikasi baris `Jane Smith {runId}-082` (Inactive) tidak tampil (filter Active tetap)
23. Klik header Position dua kali sampai sort kembali ke default Name A-Z
24. Klik `[Clear Field]`, klik `[Apply]`
25. Klik `(←)` pada kotak Search

### TC-AC-SU-292: Pemulihan dari empty state kombinasi Search dan Filter

26. Klik icon Search
27. Ketik Search `john`, tekan Enter
28. Klik icon Filter
29. Pilih Status `Inactive`, klik `[Apply]`
30. Verifikasi empty state dengan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
31. Klik `✕` pada Search, tekan Enter
32. Verifikasi baris `Jane Smith {runId}-082` (Inactive) tampil kembali
33. Klik `[Clear Field]`, klik `[Apply]`
34. Klik `(←)` pada kotak Search

### TC-AC-SU-293: Mutasi saat tabel terfilter, user yang dinonaktifkan keluar dari hasil filter Active

35. Klik icon Filter
36. Pilih Status `Active`, klik `[Apply]`
37. Verifikasi baris `John Doe {runId}-082` tampil
38. Klik switch Active baris `John Doe {runId}-082`
39. Verifikasi dialog `Deactivate User` tampil
40. Klik `[Deactivate]`
41. Verifikasi toast `Success, user has been deactivated.`
42. Verifikasi baris `John Doe {runId}-082` tidak tampil di hasil filter Active
43. Klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): mengembalikan sort ke default, `[Clear Field]` lalu `[Apply]`, dan menutup Search di akhir TC mereset state List (S-09). TC-293 (aksi mengubah data) ditaruh paling akhir (S-10).
- Alasan di atas ±35 langkah: keempat TC kombinasi Search/Filter/Sort kelas fungsional, dataset sama, berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-082` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-293 Post Condition "John Doe Inactive (pulihkan via Activate untuk TC lain)" tidak punya langkah observasi dan tidak diasersi; pemulihan dilakukan hook `after`.
