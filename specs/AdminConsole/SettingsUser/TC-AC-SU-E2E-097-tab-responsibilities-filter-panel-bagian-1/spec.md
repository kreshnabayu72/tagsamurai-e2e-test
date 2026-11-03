---
id: TC-AC-SU-E2E-097-tab-responsibilities-filter-panel-bagian-1
title: "Tab Responsibilities Filter Panel: Screening, Isi Opsi, Satu Opsi per Field, Date Range, dan Requester Kosong"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-346
  - TC-AC-SU-347
  - TC-AC-SU-348
  - TC-AC-SU-349
  - TC-AC-SU-658
coverage:
  web: automated
---

# Tab Responsibilities Filter Panel: Screening, Isi Opsi, Satu Opsi per Field, Date Range, dan Requester Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-097`): target `Jane Smith {runId}-097` dengan 3 Pending Approval; target `John Doe {runId}-097` dengan 1 Pending Approval TAG Stock tanpa pemohon; requester `Budi Santoso {runId}-097`, `Rina Putri {runId}-097`, dan `PT Maju Bersama {runId}-097`.
| ID (hasil seeding) | Transaction | Requester | Submission Date |
|---|---|---|---|
| `ID-HALC` (format `HALC-2026-NNNN`) | Device Allocation | `Budi Santoso {runId}-097` | 08 Jun 2026 |
| `ID-LALC` (format `LALC-2026-NNNN`) | License Allocation | `Rina Putri {runId}-097` | 02 Jun 2026 |
| `ID-WLT` (format `WLT-2026-NNNN`) | Wallet Top-Up | `PT Maju Bersama {runId}-097` | 05 Jun 2026 |
- Tabel filter TC-348 (parameter langkah 18 sampai 24):
| No | Field | Opsi | Baris yang tampil | Baris yang tidak tampil |
|---|---|---|---|---|
| 1 | Transaction | `Device Allocation` | `ID-HALC` | `ID-LALC`, `ID-WLT` |
| 2 | Requester | `Rina Putri {runId}-097` | `ID-LALC` | `ID-HALC`, `ID-WLT` |
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### Persiapan: membuka Detail User

1. Ketik Search `Jane Smith {runId}-097`, tekan Enter
2. Klik Name `Jane Smith {runId}-097` untuk membuka Detail User

### TC-AC-SU-346: Screening Filter Panel Tab Responsibilities

3. Klik tab `Responsibilities (3)`
4. Hover icon Filter
5. Verifikasi tooltip `Filter` tampil
6. Klik icon Filter
7. Verifikasi Filter Panel terbuka di bawah toolbar
8. Verifikasi field berurutan: `Transaction` (multi-select searchable, placeholder `All transactions`) | `Requester` (multi-select searchable, placeholder `All requesters`) | `Submission Date` (date range picker, placeholder `Select date`)
9. Verifikasi footer panel: link `[Clear Field]` (kiri) dan `[Apply]` (kanan)

### TC-AC-SU-347: Isi opsi dropdown Filter populate dari data tabel

10. Buka dropdown `Transaction`
11. Verifikasi opsi `Device Allocation`, `License Allocation`, dan `Wallet Top-Up` tampil
12. Verifikasi dropdown `Transaction` memuat tepat tiga opsi (nilai yang tidak ada di baris tabel tidak muncul)
13. Tutup dropdown `Transaction`
14. Buka dropdown `Requester`
15. Verifikasi opsi `Budi Santoso {runId}-097`, `Rina Putri {runId}-097`, dan `PT Maju Bersama {runId}-097` tampil
16. Verifikasi dropdown `Requester` memuat tepat tiga opsi (nilai yang tidak ada di baris tabel tidak muncul)
17. Tutup dropdown `Requester`, lalu klik icon Filter untuk menutup Filter Panel

### TC-AC-SU-348: Filter field multi-select, satu opsi per field

18. Klik icon Filter, pilih opsi pada kolom "Opsi" untuk field pada kolom "Field" tabel filter TC-348, klik `[Apply]`
19. Verifikasi baris pada kolom "Baris yang tampil" tampil
20. Verifikasi baris pada kolom "Baris yang tidak tampil" tidak tampil
21. Verifikasi icon Filter menampilkan badge titik (filter ter-Apply)
22. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
23. Verifikasi seluruh baris tampil (`ID-HALC`, `ID-LALC`, `ID-WLT`)
24. Verifikasi badge titik pada icon Filter hilang

### TC-AC-SU-349: Filter date range Submission Date inklusif

25. Klik icon Filter
26. Klik field `Submission Date`
27. Pilih tanggal awal 02 Jun 2026 dan tanggal akhir 05 Jun 2026
28. Klik `[Apply]`
29. Verifikasi isi field `Submission Date` tampil sesuai Date Format General Settings
30. Verifikasi baris `ID-LALC` (02 Jun 2026) dan `ID-WLT` (05 Jun 2026) tampil (batas inklusif)
31. Verifikasi baris `ID-HALC` (08 Jun 2026) tidak tampil
32. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-SU-658: Requester `—` untuk sub-menu tanpa kolom pemohon

33. Klik segmen `User` di breadcrumb
34. Ganti isi kotak Search dengan `John Doe {runId}-097`, tekan Enter
35. Klik Name `John Doe {runId}-097` untuk membuka Detail User
36. Klik tab `Responsibilities (1)`
37. Verifikasi baris TAG Stock menampilkan Requester `—`

## Notes

- Langkah 18 sampai 24 diulang untuk tiap baris tabel filter TC-348 (8b butir 7); parameter ada di Prerequisites.
- Langkah penghubung (S-03): langkah 17 menutup dropdown `Requester` dan Filter Panel, dan langkah 18 membukanya kembali, agar tiap iterasi langkah 18 sampai 24 identik (asumsi kerja: `[Apply]` menutup panel; PRD §9.8 tidak menyatakan keadaan panel sesudah Apply); Search lalu klik Name membuka Detail target (R-16); membuka lalu mengosongkan Filter Panel di akhir tiap TC melepas kriteria (S-09); TC-658 memakai target lain (`John Doe {runId}-097`) di akhir karena Pending Approval TAG Stock tanpa pemohon.
- Alasan di atas ±35 langkah (ekspansi): kelima TC adalah Filter Tab Responsibilities dengan dataset sama dan berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-097` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-658 menyebut sub-menu TAG Stock sebagai Transaction tanpa pemohon; label Transaction persisnya (`TAG Stock`) tidak tertulis di TC dan diikuti PRD approvals §5.7.
