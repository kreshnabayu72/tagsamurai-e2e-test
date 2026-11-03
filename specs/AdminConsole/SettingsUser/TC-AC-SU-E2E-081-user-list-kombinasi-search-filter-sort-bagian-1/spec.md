---
id: TC-AC-SU-E2E-081-user-list-kombinasi-search-filter-sort-bagian-1
title: "User List Kombinasi Search, Filter, Sort, dan Page Size (bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-286
  - TC-AC-SU-287
  - TC-AC-SU-288
  - TC-AC-SU-289
coverage:
  web: automated
---

# User List Kombinasi Search, Filter, Sort, dan Page Size (bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-081`): `Mike Tan {runId}-081` (Active, Activated, Division `IT Operations`, Email `a.mike@{runId}-081.qwertysystem.net`), `Jane Smith {runId}-081` (Inactive, Division `IT Operations`, Email `b.jane@{runId}-081.qwertysystem.net`), `Sarah Lee {runId}-081` (Active, Activated, Division `Finance`, Email `c.sarah@{runId}-081.qwertysystem.net`), `John Doe {runId}-081` (Active, Activated, Division `Finance`, Email `d.john@{runId}-081.qwertysystem.net`). Semua nama user memuat teks `a` pada kolom Division, Email, atau Name.
- Page size awal 10 (default).
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### TC-AC-SU-286: Alur Search lalu Filter multi-field

1. Ketik Search `a`, tekan Enter
2. Klik icon Filter
3. Pilih Status `Active` dan Division `IT Operations`, klik `[Apply]`
4. Verifikasi baris `Mike Tan {runId}-081` (memuat `a`, Active, IT Operations) tampil
5. Verifikasi baris `Jane Smith {runId}-081` (Inactive) dan `Sarah Lee {runId}-081` (Division `Finance`) tidak tampil
6. Verifikasi keyword search tetap terisi `a`
7. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
8. Klik `(←)` pada kotak Search

### TC-AC-SU-287: Alur Filter lalu Search

9. Klik icon Filter
10. Pilih Status `Active` dan Activation Status `Activated`, klik `[Apply]`
11. Ketik Search `doe`, tekan Enter
12. Verifikasi baris `John Doe {runId}-081` tampil
13. Verifikasi baris `Mike Tan {runId}-081` tidak tampil
14. Klik icon Filter
15. Verifikasi field Status berisi `Active`
16. Verifikasi field Activation Status berisi `Activated`
17. Klik `[Clear Field]`, klik `[Apply]`
18. Klik `(←)` pada kotak Search

### TC-AC-SU-288: Kombinasi Search, Filter, Sort, dan Page Size

19. Ubah page size menjadi 25
20. Ketik Search `a`, tekan Enter
21. Klik icon Filter
22. Pilih Status `Active`, klik `[Apply]`
23. Klik header Email
24. Verifikasi baris `Mike Tan {runId}-081` tampil sebelum `Sarah Lee {runId}-081` dan `Sarah Lee {runId}-081` sebelum `John Doe {runId}-081` (Email A-Z)
25. Verifikasi baris `Jane Smith {runId}-081` (Inactive) tidak tampil
26. Verifikasi page size tetap 25
27. Verifikasi tabel berada di halaman 1

### TC-AC-SU-289: Clear Filter saat Search dan Sort aktif

28. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
29. Klik header Email dua kali sehingga sort kembali ke default Name A-Z
30. Ubah page size menjadi 10
31. Klik `(←)` pada kotak Search
32. Ketik Search `a`, tekan Enter
33. Klik header Email
34. Klik icon Filter
35. Pilih Status `Active`, klik `[Apply]`
36. Verifikasi baris `Mike Tan {runId}-081` tampil
37. Verifikasi baris `Jane Smith {runId}-081` (Inactive) tidak tampil
38. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
39. Verifikasi keyword search tetap terisi `a`
40. Verifikasi sort Email A-Z tetap berlaku (`Mike Tan {runId}-081` tampil sebelum `Jane Smith {runId}-081`)
41. Verifikasi baris `Jane Smith {runId}-081` (Inactive) tampil kembali karena hanya kriteria Status dilepas
42. Klik header Email dua kali sampai sort kembali ke default Name A-Z
43. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): `[Clear Field]` lalu `[Apply]`, menutup Search, mengembalikan page size ke 10, dan mengembalikan sort ke default Name A-Z di antara TC mereset state List (S-09; klik sidebar tidak dipakai karena mereset Search, Sort, dan Filter sekaligus).
- Langkah 28 sampai 35 mengembalikan state ke awal (filter dilepas, sort default, page size 10, Search ditutup) lalu membangun state TC-289 dengan urutan aksi yang ditulis TC-289 (Search, sort Email, lalu Filter); state akhir TC-288 tidak diteruskan karena dibangun dengan urutan berbeda (Search, Filter, lalu sort).
- Langkah 36 dan 37 adalah asersi tambahan (S-03, dasar 8b.2): langkah 36 menjadi anchor positif bagi absence baris `Jane Smith {runId}-081` pada langkah 37, basis perbandingan langkah 41.
- Alasan di atas ±35 langkah: keempat TC adalah kombinasi Search/Filter/Sort User List kelas fungsional dengan dataset yang sama; berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-081` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-288 mengasersi "hasil irisan terurut Email A-Z" tanpa data; spec memberi prefix huruf pada Email seed (`a.`, `b.`, `c.`, `d.`) agar urutan Email berbeda dari urutan Name.
  - PRD §9.8 tidak menyatakan keadaan Filter Panel sesudah `[Apply]`; spec berasumsi `[Apply]` menutup panel, sehingga langkah 7, 28, dan 38 diawali `Klik icon Filter` sebelum `[Clear Field]`.
  - TC-289 langkah 4 melepas kriteria Status tetapi Expected tidak menyebut baris yang kembali tampil; spec memakai `Jane Smith {runId}-081` (Inactive) sebagai bukti kriteria dilepas.
