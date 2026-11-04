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
7. Klik pagination next sampai baris `Mike Tan {runId}-082` dan `John Doe {runId}-082` keduanya teramati di tabel
8. Verifikasi baris `Mike Tan {runId}-082` tampil sebelum `John Doe {runId}-082` (sort Name Z-A tetap; keduanya dibaca lintas halaman)
9. Verifikasi baris `John Doe {runId}-082` dan `Mike Tan {runId}-082` (Active) tampil
10. Verifikasi baris `Jane Smith {runId}-082` (Inactive) tidak tampil (filter Active tetap)
11. Klik header Name sekali sampai sort kembali ke default Name A-Z
12. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
13. Klik `(←)` pada kotak Search

### TC-AC-SU-291: Ganti target sort saat Search dan Filter aktif

14. Klik icon Search
15. Ketik Search `a`, tekan Enter
16. Klik icon Filter
17. Pilih Status `Active`, klik `[Apply]`
18. Klik header Email
19. Klik header Position
20. Klik pagination next sampai baris `Mike Tan {runId}-082` dan `John Doe {runId}-082` keduanya teramati di tabel
21. Verifikasi baris `Mike Tan {runId}-082` (Position `Analyst`) tampil sebelum `John Doe {runId}-082` (Position `Staff`) (sort pindah ke Position A-Z)
22. Verifikasi ikon sort Email kembali netral
23. Verifikasi keyword search tetap `a`
24. Verifikasi baris `Jane Smith {runId}-082` (Inactive) tidak tampil (filter Active tetap)
25. Klik header Position dua kali sampai sort kembali ke default Name A-Z
26. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
27. Klik `(←)` pada kotak Search

### TC-AC-SU-292: Pemulihan dari empty state kombinasi Search dan Filter

28. Klik icon Search
29. Ketik Search `john`, tekan Enter
30. Klik icon Filter
31. Pilih Status `Inactive`, klik `[Apply]`
32. Verifikasi empty state dengan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
33. Klik `✕` pada Search, tekan Enter
34. Verifikasi baris `Jane Smith {runId}-082` (Inactive) tampil kembali
35. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
36. Klik `(←)` pada kotak Search

### TC-AC-SU-293: Mutasi saat tabel terfilter, user yang dinonaktifkan keluar dari hasil filter Active

37. Klik icon Filter
38. Pilih Status `Active`, klik `[Apply]`
39. Klik icon Search
40. Ketik Search `John Doe {runId}-082`, tekan Enter
41. Verifikasi baris `John Doe {runId}-082` tampil
42. Klik switch Active baris `John Doe {runId}-082`
43. Verifikasi dialog `Deactivate User` tampil
44. Klik `[Deactivate]`
45. Verifikasi toast `Success, user has been deactivated.`
46. Verifikasi baris `John Doe {runId}-082` tidak tampil di hasil filter Active
47. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): langkah 39 dan 40 (Search `John Doe {runId}-082` agar baris yang diklik pasti tampil, karena Search ditutup di akhir TC sebelumnya), mengembalikan sort ke default, `Klik icon Filter` lalu `[Clear Field]` dan `[Apply]` (Apply menutup panel), dan menutup Search di akhir TC mereset state List (S-09). TC-293 (aksi mengubah data) ditaruh paling akhir (S-10).
- Cara membaca urutan (S-14): pada User List penuh baris seed bersuffix berada di antara baris Pre-setup dan bisa berbeda halaman; langkah 7 dan 20 membuka halaman berikutnya sampai kedua baris teramati, lalu urutan dibandingkan menurut sort aktif (baris di halaman lebih awal berarti lebih atas).
- Alasan di atas ±35 langkah: keempat TC kombinasi Search/Filter/Sort kelas fungsional, dataset sama, berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-082` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-293 Post Condition "John Doe Inactive (pulihkan via Activate untuk TC lain)" tidak punya langkah observasi dan tidak diasersi; pemulihan dilakukan hook `after`.
