---
id: TC-AC-SU-E2E-090-user-list-pagination-dan-retensi-state
title: "User List Pagination: Navigasi Halaman dan Reset Halaman saat Search atau Filter Berubah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-321
  - TC-AC-SU-322
coverage:
  web: automated
---

# User List Pagination: Navigasi Halaman dan Reset Halaman saat Search atau Filter Berubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-090`): group `Region A {runId}-090`; `Anton 01 {runId}-090` sampai `Anton 12 {runId}-090` (Active, Activated, Division `Finance`, Group Role aktif di `Region A {runId}-090`); Seluruh user milik spec memuat teks `a` pada kolom Division; hasil Search `a` dan Filter Status `Active` memuat lebih dari 10 baris. Entitas memuat lebih dari 10 user.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### TC-AC-SU-321: Screening dan navigasi pagination

1. Amati footer tabel
2. Verifikasi default 10 baris per halaman
3. Verifikasi opsi page size 10, 25, 50, 100 tanpa opsi All
4. Klik next
5. Verifikasi tabel berpindah ke halaman 2
6. Klik prev
7. Verifikasi tabel kembali ke halaman 1
8. Ubah page size ke 25, lalu 50, lalu 100
9. Ubah page size ke 10
10. Ketik halaman 2 pada input halaman, tekan Enter
11. Verifikasi tabel langsung ke halaman 2
12. Klik prev agar kembali ke halaman 1

### TC-AC-SU-322: Pagination kembali ke halaman 1 saat Search atau Filter berubah, sort tetap di halaman sekarang

13. Klik next agar berada di halaman 2
14. Klik icon Search
15. Ketik Search `a`, tekan Enter
16. Verifikasi tabel berada di halaman 1
17. Klik next agar berada di halaman 2
18. Klik icon Filter
19. Pilih Status `Active`, klik `[Apply]`
20. Verifikasi tabel berada di halaman 1
21. Klik next agar berada di halaman 2
22. Klik header Email
23. Verifikasi tabel tetap berada di halaman 2
24. Verifikasi urutan baris di halaman 2 mengikuti Email A-Z
25. Klik header Email dua kali sampai sort kembali ke default Name A-Z
26. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
27. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): `Klik icon Filter` lalu `[Clear Field]` dan `[Apply]` (Apply menutup panel), menutup Search, dan mengembalikan sort ke default di akhir TC-322 (S-09).
- Pembagian TC User List Pagination dan retensi state: TC-AC-SU-321 dan 322 di spec ini; TC-AC-SU-323, 324, dan 325 di spec 203, yang memakai dataset dan akun yang sama dengan seeding sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-090` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
