---
id: TC-AC-SU-E2E-083-user-list-sort-role-active-tanggal-dan-tie-breaker
title: "User List Sort: Kolom Role, Active, Kelas Tanggal, dan Tie-Breaker Nilai Sama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-295
  - TC-AC-SU-296
  - TC-AC-SU-297
  - TC-AC-SU-656
coverage:
  web: automated
---

# User List Sort: Kolom Role, Active, Kelas Tanggal, dan Tie-Breaker Nilai Sama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-083`): `Sarah Lee {runId}-083` (0 role aktif), `Mike Tan {runId}-083` (1 role aktif; Last Updated 30 Jan 2026; Temporary Until 20 Feb 2026), `Jane Smith {runId}-083` (2 role aktif; Last Updated 15 Jan 2026), `Rudi Hartono {runId}-083` (10 role aktif), `Andi Wijaya {runId}-083` (Read Only; Position `Staff`; Temporary Until 10 Feb 2026), `Budi Santoso {runId}-083` (Inactive; Position `Staff`), `John Doe {runId}-083` (Active; Last Updated 01 Jan 2026). Baris Default User Principal (Pre-setup #1, Total Control) dipakai apa adanya. Asersi urutan memakai urutan relatif antar baris milik spec; baris Pre-setup ikut tampil dan tidak diasersi.
- Last Updated dan Temporary Until user milik spec diatur Fixture BE sesuai nilai di atas.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-295: Sort kolom Role, jumlah role numerik natural lalu badge tier

1. Klik header Role (klik 1)
2. Verifikasi urutan baris dari atas: `Sarah Lee {runId}-083` (`0 roles`), `Mike Tan {runId}-083` (`1 role`), `Jane Smith {runId}-083` (`2 roles`), `Rudi Hartono {runId}-083` (`10 roles`), `Andi Wijaya {runId}-083` (`Read Only`), Default User (`Total Control`)
3. Klik header Role (klik 2)
4. Verifikasi urutan baris terbalik dari urutan klik 1
5. Klik header Role (klik 3)
6. Verifikasi urutan kembali ke default Name A-Z (`Andi Wijaya {runId}-083`, `Jane Smith {runId}-083`, `Mike Tan {runId}-083`, `Rudi Hartono {runId}-083`, `Sarah Lee {runId}-083`)

### TC-AC-SU-296: Sort kolom Active (toggle)

7. Klik header Active (klik 1)
8. Verifikasi baris `John Doe {runId}-083` (Active) tampil sebelum `Budi Santoso {runId}-083` (Inactive) (Active First)
9. Klik header Active (klik 2)
10. Verifikasi baris `Budi Santoso {runId}-083` (Inactive) tampil sebelum `John Doe {runId}-083` (Active) (Inactive First)
11. Klik header Active (klik 3)
12. Verifikasi urutan kembali ke default Name A-Z (`Budi Santoso {runId}-083` sebelum `John Doe {runId}-083`)

### TC-AC-SU-297: Sort kelas tanggal (Last Updated, Temporary Until)

13. Klik `⋯` pada header Actions
14. Klik `[Setup Column]`
15. Centang kolom `Temporary Until` pada Setup Column
16. Klik `[Save]`
17. Klik header Last Updated (klik 1)
18. Verifikasi urutan baris `John Doe {runId}-083`, `Jane Smith {runId}-083`, `Mike Tan {runId}-083` (Oldest First, ikon ↑)
19. Klik header Last Updated (klik 2)
20. Verifikasi urutan baris `Mike Tan {runId}-083`, `Jane Smith {runId}-083`, `John Doe {runId}-083` (Newest First, ikon ↓)
21. Klik header Last Updated (klik 3)
22. Verifikasi urutan kembali ke default Name A-Z
23. Klik header Temporary Until (klik 1)
24. Verifikasi urutan baris `Andi Wijaya {runId}-083`, `Mike Tan {runId}-083` (Oldest First), baris tanpa Temporary Until (`—`) `John Doe {runId}-083` di akhir
25. Klik header Temporary Until (klik 2)
26. Verifikasi baris `John Doe {runId}-083` (`—`) di awal, lalu `Mike Tan {runId}-083`, `Andi Wijaya {runId}-083` (Newest First)
27. Klik header Temporary Until (klik 3)
28. Verifikasi urutan kembali ke default Name A-Z

### TC-AC-SU-656: Sort User List, nilai kunci sama diurutkan menurut default sort lalu identifier

29. Klik header Position (klik 1, A-Z)
30. Verifikasi baris `Andi Wijaya {runId}-083` tampil sebelum `Budi Santoso {runId}-083`
31. Klik header Position (klik 2, Z-A)
32. Verifikasi urutan relatif keduanya tetap (`Andi Wijaya {runId}-083` sebelum `Budi Santoso {runId}-083`)
33. Tekan F5
34. Klik header Position (klik 1, A-Z)
35. Verifikasi urutan `Andi Wijaya {runId}-083` sebelum `Budi Santoso {runId}-083` identik dengan sebelum F5

## Notes

- Langkah penghubung (S-03): langkah Setup Column di TC-297 memenuhi kebutuhan menampilkan Temporary Until; klik header ketiga di tiap TC mengembalikan sort ke default (S-09).
- TC-656 Position `Staff` dipakai bersama oleh `Andi Wijaya {runId}-083` dan `Budi Santoso {runId}-083`; sort Position diaktifkan dari default Name A-Z.
- Alasan di atas ±35 langkah: keempat TC adalah Sort User List kelas fungsional dengan dataset sama dan berdiri sendiri; TC-294 (sort kelas teks) ada di spec 194.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-083` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-295 menyebut urutan `Total Control` setelah `Read Only` memakai baris Default User; spec mengasersi baris Default User Principal apa adanya.
  - TC-297 tidak menyebut cara membuat Last Updated berbeda antar user; spec mengaturnya lewat Fixture BE dengan nilai tetap.
