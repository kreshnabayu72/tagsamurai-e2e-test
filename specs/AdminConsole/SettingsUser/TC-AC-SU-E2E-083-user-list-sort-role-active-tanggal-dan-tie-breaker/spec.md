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
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-083`): `Sarah Lee {runId}-083` (0 role aktif), `Mike Tan {runId}-083` (1 role aktif; Last Updated 30 Jan 2026; Temporary Until 20 Feb 2026), `Jane Smith {runId}-083` (2 role aktif; Last Updated 15 Jan 2026), `Rudi Hartono {runId}-083` (10 role aktif), `Dewi Lestari {runId}-083` (tingkat akses Total Control; seluruh peran individual aktif CRUD penuh), `Andi Wijaya {runId}-083` (Read Only; Position `Staff`; Temporary Until 10 Feb 2026), `Budi Santoso {runId}-083` (Inactive; Position `Staff`), `John Doe {runId}-083` (Active; Last Updated 01 Jan 2026). Asersi urutan memakai urutan relatif antar baris milik spec; Search `{runId}-083` menyaring baris Pre-setup (termasuk Default User) dari tabel sebelum asersi urutan.
- Last Updated dan Temporary Until user milik spec diatur Fixture BE sesuai nilai di atas.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-295: Sort kolom Role, jumlah role numerik natural lalu badge tier

1. Klik icon Search
2. Ketik Search `{runId}-083`, tekan Enter
3. Klik header Role (klik 1)
4. Verifikasi tabel menampilkan sedikitnya dua baris data uji
5. Verifikasi urutan baris dari atas: `Sarah Lee {runId}-083` (`0 roles`), `Mike Tan {runId}-083` (`1 role`), `Jane Smith {runId}-083` (`2 roles`), `Rudi Hartono {runId}-083` (`10 roles`), `Andi Wijaya {runId}-083` (`Read Only`), `Dewi Lestari {runId}-083` (`Total Control`)
6. Klik header Role (klik 2)
7. Verifikasi urutan baris terbalik dari urutan klik 1 (`Dewi Lestari {runId}-083` (`Total Control`) paling atas, `Andi Wijaya {runId}-083` (`Read Only`) di bawahnya, lalu `Rudi Hartono {runId}-083`, `Jane Smith {runId}-083`, `Mike Tan {runId}-083`, `Sarah Lee {runId}-083`)
8. Klik header Role (klik 3)
9. Verifikasi urutan kembali ke default Name A-Z (`Andi Wijaya {runId}-083`, `Dewi Lestari {runId}-083`, `Jane Smith {runId}-083`, `Mike Tan {runId}-083`, `Rudi Hartono {runId}-083`, `Sarah Lee {runId}-083`)

### TC-AC-SU-296: Sort kolom Active (toggle)

10. Klik header Active (klik 1)
11. Verifikasi baris `John Doe {runId}-083` (Active) tampil sebelum `Budi Santoso {runId}-083` (Inactive) (Active First)
12. Klik header Active (klik 2)
13. Verifikasi baris `Budi Santoso {runId}-083` (Inactive) tampil sebelum `John Doe {runId}-083` (Active) (Inactive First)
14. Klik header Active (klik 3)
15. Verifikasi urutan kembali ke default Name A-Z (`Budi Santoso {runId}-083` sebelum `John Doe {runId}-083`)

### TC-AC-SU-297: Sort kelas tanggal (Last Updated, Temporary Until)

16. Klik `⋯` pada header Actions
17. Klik `[Setup Column]`
18. Centang kolom `Temporary Until` pada Setup Column
19. Klik `[Save]`
20. Klik header Last Updated (klik 1)
21. Verifikasi urutan baris `John Doe {runId}-083`, `Jane Smith {runId}-083`, `Mike Tan {runId}-083` (Oldest First, ikon ↑)
22. Klik header Last Updated (klik 2)
23. Verifikasi urutan baris `Mike Tan {runId}-083`, `Jane Smith {runId}-083`, `John Doe {runId}-083` (Newest First, ikon ↓)
24. Klik header Last Updated (klik 3)
25. Verifikasi urutan kembali ke default Name A-Z
26. Klik header Temporary Until (klik 1)
27. Verifikasi urutan baris `Andi Wijaya {runId}-083`, `Mike Tan {runId}-083` (Oldest First), baris tanpa Temporary Until (`—`) `John Doe {runId}-083` di akhir
28. Klik header Temporary Until (klik 2)
29. Verifikasi baris `John Doe {runId}-083` (`—`) di awal, lalu `Mike Tan {runId}-083`, `Andi Wijaya {runId}-083` (Newest First)
30. Klik header Temporary Until (klik 3)
31. Verifikasi urutan kembali ke default Name A-Z

### TC-AC-SU-656: Sort User List, nilai kunci sama diurutkan menurut default sort lalu identifier

32. Klik header Position
33. Verifikasi baris `Andi Wijaya {runId}-083` tampil sebelum `Budi Santoso {runId}-083`
34. Klik header Position (klik 2, Z-A)
35. Verifikasi urutan relatif keduanya tetap (`Andi Wijaya {runId}-083` sebelum `Budi Santoso {runId}-083`)
36. Tekan F5
37. Ganti isi kotak search dengan `{runId}-083`, tekan Enter
38. Verifikasi ikon sort Position ↓ tetap tampil
39. Verifikasi urutan `Andi Wijaya {runId}-083` sebelum `Budi Santoso {runId}-083` identik dengan sebelum F5

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (Search `{runId}-083` agar urutan sort tidak bergantung baris Pre-setup), langkah 37 (Search dipulihkan saat F5; isi kotak search diganti dengan nilai yang sama agar hasil Search dimuat ulang); langkah Setup Column di TC-297 (langkah 16 sampai 19) menampilkan Temporary Until; klik header ketiga di tiap TC mengembalikan sort ke default (S-09).
- TC-656 Position `Staff` dipakai bersama oleh `Andi Wijaya {runId}-083` dan `Budi Santoso {runId}-083`; sort Position diaktifkan dari default Name A-Z.
- Alasan di atas ±35 langkah: keempat TC adalah Sort User List kelas fungsional dengan dataset sama dan berdiri sendiri; TC-294 (sort kelas teks) ada di spec 194.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-083` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-297 tidak menyebut cara membuat Last Updated berbeda antar user; spec mengaturnya lewat Fixture BE dengan nilai tetap.
  - TC-656 langkah 3 ("Refresh halaman, ulangi langkah 1") mengabaikan bahwa Sort ikut dipulihkan saat F5; spec mengasersi ikon sort Position ↓ tetap tampil sesudah F5 sebelum asersi urutan.
