---
id: TC-AC-SU-E2E-084-user-list-sort-badge-modified-by-custom-field-dan-guard
title: "User List Sort: Kolom Badge, Modified By, Custom Field Text, dan Guard Kolom Tanpa Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-298
  - TC-AC-SU-299
  - TC-AC-SU-300
  - TC-AC-SU-301
  - TC-AC-SU-302
coverage:
  web: automated
---

# User List Sort: Kolom Badge, Modified By, Custom Field Text, dan Guard Kolom Tanpa Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-084`): `John Doe {runId}-084` (Activated, Temporary User `No`, Modified By `Budi Hartono {runId}-084`, Office Location `Jakarta HQ`), `Mike Tan {runId}-084` (Pending Activation, Temporary User `Yes`, Modified By `Budi Santoso {runId}-084`, Office Location `Surabaya`), `Rina Putri {runId}-084` (Pending Email Confirmation, Temporary User `No`), `Jane Smith {runId}-084` (Activated, Office Location `Bandung`). Custom Field Pre-setup `Office Location` (Text) berstatus Active (Pre-setup #10); spec hanya mengisi nilai pada user milik spec.
- Asersi urutan memakai urutan relatif antar baris milik spec; baris Pre-setup ikut tampil dan tidak diasersi.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### Persiapan kolom

1. Klik `⋯` pada header Actions
2. Klik `[Setup Column]`
3. Centang kolom `Activation Status`, `Temporary User`, dan `Office Location` pada Setup Column
4. Klik `[Save]`

### TC-AC-SU-298: Sort kolom badge Activation Status

5. Klik header Activation Status (klik 1)
6. Verifikasi urutan baris `John Doe {runId}-084` (`Activated`), `Mike Tan {runId}-084` (`Pending Activation`), `Rina Putri {runId}-084` (`Pending Email Confirmation`)
7. Klik header Activation Status (klik 2)
8. Verifikasi urutan baris terbalik dari urutan klik 1
9. Klik header Activation Status (klik 3)
10. Verifikasi urutan kembali ke default Name A-Z

### TC-AC-SU-299: Sort kolom Temporary User (Yes First / No First)

11. Klik header Temporary User (klik 1)
12. Verifikasi baris `Mike Tan {runId}-084` (`Yes`) tampil sebelum `John Doe {runId}-084` (`No`) (Yes First)
13. Klik header Temporary User (klik 2)
14. Verifikasi baris `John Doe {runId}-084` (`No`) tampil sebelum `Mike Tan {runId}-084` (`Yes`) (No First)
15. Klik header Temporary User (klik 3)
16. Verifikasi urutan kembali ke default Name A-Z

### TC-AC-SU-300: Sort Modified By berdasarkan nama lengkap

17. Klik header Modified By (klik 1)
18. Verifikasi baris dengan modifier `Budi Hartono {runId}-084` (`John Doe {runId}-084`) tampil sebelum baris dengan modifier `Budi Santoso {runId}-084` (`Mike Tan {runId}-084`)
19. Hover sel Modified By `Budi S` pada baris `Mike Tan {runId}-084`
20. Verifikasi tooltip `Budi Santoso {runId}-084` tampil
21. Klik header Modified By (klik 2)
22. Klik header Modified By (klik 3)

### TC-AC-SU-301: Sort kolom Custom Field Text

23. Verifikasi kolom Custom Field aktif `Office Location` tampil di tabel
24. Klik header `Office Location` (klik 1)
25. Verifikasi urutan baris `Jane Smith {runId}-084` (`Bandung`), `John Doe {runId}-084` (`Jakarta HQ`), `Mike Tan {runId}-084` (`Surabaya`) (A-Z)
26. Klik header `Office Location` (klik 2)
27. Verifikasi urutan baris terbalik (Z-A)
28. Klik header `Office Location` (klik 3)
29. Verifikasi urutan kembali ke default Name A-Z

### TC-AC-SU-302: Guard kolom tanpa sort (Checkbox, Actions)

30. Amati header kolom Checkbox dan Actions `(⋯)`
31. Verifikasi tidak ada ikon sort pada header Checkbox dan header Actions
32. Klik header Actions
33. Verifikasi overlay Column Visibility terbuka
34. Verifikasi urutan baris tabel tidak berubah (default Name A-Z)
35. Tekan Esc untuk menutup overlay

## Notes

- Langkah penghubung (S-03): langkah Persiapan kolom menampilkan kolom curated yang dipakai TC-298, TC-299, dan TC-301; klik ketiga pada tiap kolom mengembalikan sort ke default (S-09). Klik 2 dan klik 3 pada TC-300 mengembalikan sort ke default tanpa `Verifikasi`; Esc menutup overlay Column Visibility.
- Alasan di atas ±35 langkah: kelima TC adalah Sort User List kelas fungsional dengan dataset yang sama dan berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-084` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-301 Expected (a) mengasersi kolom `Office Location` tampil tetapi langkah TC menampilkannya lewat Setup Column; spec menampilkannya pada Persiapan kolom.
