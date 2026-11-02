---
id: TC-AC-SU-E2E-087-user-list-setup-column-guard-reset-discard-dan-cache
title: "User List Setup Column: Guard Satu Kolom, Reset to Default, Discard, dan Independensi Cache dengan Modal Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-311
  - TC-AC-SU-312
  - TC-AC-SU-313
  - TC-AC-SU-314
coverage:
  web: automated
---

# User List Setup Column: Guard Satu Kolom, Reset to Default, Discard, dan Independensi Cache dengan Modal Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-087`): `John Doe {runId}-087` (Active, Activated).
- Kolom default Modal Changelog: User (PRD §4.1.8): Date, Action, User Name, Field, Old Value, New Value, Modified By.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-311: Setup Column guard satu kolom tersisa

1. Klik `⋯` pada header Actions
2. Klik `[Setup Column]`
3. Hapus centang semua kolom kecuali Name
4. Hover checkbox Name
5. Verifikasi checkbox Name tetap tampil namun disabled
6. Verifikasi tooltip `At least one column must remain visible.` tampil
7. Klik icon (X) pada popup

### TC-AC-SU-312: Setup Column Reset to Default

8. Klik `⋯` pada header Actions
9. Klik `[Setup Column]`
10. Hapus centang Email, drag Name ke posisi pertama, dan klik icon Pin pada Name
11. Klik `[Save]`
12. Klik `⋯` pada header Actions, klik `[Setup Column]`
13. Klik `[Reset to Default]`
14. Klik `[Save]`
15. Verifikasi konfigurasi tabel kembali ke default (urutan dan visibilitas kolom default, tanpa pin)
16. Tekan F5
17. Verifikasi konfigurasi default bertahan setelah F5

### TC-AC-SU-313: Setup Column discard via (X) dan Esc

18. Klik `⋯` pada header Actions
19. Klik `[Setup Column]`
20. Hapus centang Email
21. Klik icon (X) pada popup
22. Verifikasi popup tertutup
23. Verifikasi kolom Email tetap tampil di tabel
24. Klik `⋯` pada header Actions, klik `[Setup Column]`
25. Hapus centang Email
26. Tekan Esc
27. Verifikasi popup tertutup
28. Verifikasi kolom Email tetap tampil di tabel

### TC-AC-SU-314: Independensi cache Setup Column User List dan Modal Changelog: User

29. Klik `⋯` pada header Actions
30. Klik `[Setup Column]`
31. Hapus centang Email
32. Klik `[Save]`
33. Klik icon Changelog di toolbar
34. Verifikasi kolom modal Changelog: User tetap default: Date, Action, User Name, Field, Old Value, New Value, Modified By
35. Tutup modal Changelog: User dengan icon (X)
36. Klik `⋯` pada header Actions, klik `[Setup Column]`, klik `[Reset to Default]`, klik `[Save]`

## Notes

- Langkah penghubung (S-03): icon (X) menutup popup tanpa menyimpan pada TC-311; menutup modal dan `[Reset to Default]` lalu `[Save]` di akhir TC-314 mengembalikan konfigurasi kolom.
- Alasan di atas ±35 langkah: keempat TC adalah Setup Column User List dengan dataset yang sama dan berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-087` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-312 langkah 1 berbunyi "Ubah urutan, pin, dan visibilitas" tanpa nilai; spec memakai menyembunyikan Email, memindah Name ke posisi pertama, dan mem-pin Name.
  - TC-314 menyebut "Kolom modal tetap default §4.1.8" tanpa daftar kolom; spec menyalin kolom default dari PRD §4.1.8.
