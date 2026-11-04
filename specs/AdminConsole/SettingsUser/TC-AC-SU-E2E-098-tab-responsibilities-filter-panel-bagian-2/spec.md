---
id: TC-AC-SU-E2E-098-tab-responsibilities-filter-panel-bagian-2
title: "Tab Responsibilities Filter Panel: OR dan AND, Chip Opsi, dan Uncheck di Dropdown"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-350
  - TC-AC-SU-351
  - TC-AC-SU-352
coverage:
  web: automated
---

# Tab Responsibilities Filter Panel: OR dan AND, Chip Opsi, dan Uncheck di Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-098`): target `Jane Smith {runId}-098` dengan 3 Pending Approval; requester `Budi Santoso {runId}-098`, `Rina Putri {runId}-098`, dan `PT Maju Bersama {runId}-098`.
| ID (hasil seeding) | Transaction | Requester | Submission Date |
|---|---|---|---|
| `ID-HALC` (format `HALC-2026-NNNN`) | Device Allocation | `Budi Santoso {runId}-098` | 08 Jun 2026 |
| `ID-LALC` (format `LALC-2026-NNNN`) | License Allocation | `Rina Putri {runId}-098` | 02 Jun 2026 |
| `ID-WLT` (format `WLT-2026-NNNN`) | Wallet Top-Up | `PT Maju Bersama {runId}-098` | 05 Jun 2026 |
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### Persiapan: membuka Detail User

1. Klik icon Search
2. Ketik Search `Jane Smith {runId}-098`, tekan Enter
3. Klik Name `Jane Smith {runId}-098` untuk membuka Detail User

### TC-AC-SU-350: OR di dalam satu field, AND antar field

4. Klik tab `Responsibilities (3)`
5. Klik icon Filter
6. Pilih `Device Allocation` dan `Wallet Top-Up` di field `Transaction`
7. Klik `[Apply]`
8. Verifikasi baris `ID-HALC` (Device Allocation) dan `ID-WLT` (Wallet Top-Up) tampil
9. Verifikasi baris `ID-LALC` (License Allocation) tidak tampil
10. Klik icon Filter
11. Tambah `Budi Santoso {runId}-098` di field `Requester`
12. Klik `[Apply]`
13. Verifikasi baris `ID-HALC` (Device Allocation, Requester `Budi Santoso {runId}-098`) tampil
14. Verifikasi baris `ID-WLT` (Requester `PT Maju Bersama {runId}-098`) tidak tampil
15. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-SU-351: Chip opsi terpilih dan hapus via `(X)` chip

16. Klik icon Filter
17. Pilih `Device Allocation` lalu `Wallet Top-Up` di field `Transaction`
18. Verifikasi chip `Device Allocation` lalu chip `Wallet Top-Up` muncul berdampingan di dalam field `Transaction`
19. Klik `(X)` pada chip `Device Allocation` tanpa membuka dropdown
20. Verifikasi chip `Device Allocation` hilang
21. Verifikasi chip `Wallet Top-Up` tetap
22. Buka dropdown field `Transaction`
23. Verifikasi checkbox `Device Allocation` ter-uncheck
24. Verifikasi checkbox `Wallet Top-Up` tetap tercentang
25. Klik `[Apply]`
26. Verifikasi baris `ID-WLT` (Wallet Top-Up) tampil
27. Verifikasi baris `ID-HALC` (Device Allocation) tidak tampil
28. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-SU-352: Hapus opsi lewat uncheck di dalam dropdown

29. Klik icon Filter
30. Pilih `Device Allocation` lalu `Wallet Top-Up` di field `Transaction`
31. Buka dropdown `Transaction`, hapus centang `Wallet Top-Up`
32. Tutup dropdown
33. Verifikasi chip `Wallet Top-Up` hilang dari field
34. Verifikasi chip `Device Allocation` tetap
35. Klik `[Apply]`
36. Verifikasi baris `ID-HALC` (Device Allocation) tampil
37. Verifikasi baris `ID-WLT` (Wallet Top-Up) tidak tampil
38. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): Search lalu klik Name membuka Detail target (R-16); `[Apply]` menutup Filter Panel, sehingga tiap perubahan Filter sesudah Apply diawali `Klik icon Filter`; `[Clear Field]` lalu `[Apply]` di akhir tiap TC melepas filter (S-09).
- Alasan di atas ±35 langkah: ketiga TC adalah Filter Tab Responsibilities dengan dataset sama; berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-098` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-350 Expected (a) menyebut baris Transaction `Device Allocation` ATAU `Wallet Top-Up` tanpa menyebut data pembanding; spec memakai `ID-LALC` (License Allocation) sebagai baris yang tidak tampil.
