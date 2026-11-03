---
id: TC-AC-SU-E2E-094-tab-responsibilities-sort-3-state
title: "Tab Responsibilities: Sort 3-State Kelas Teks dan Kelas Tanggal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-338
  - TC-AC-SU-339
coverage:
  web: automated
---

# Tab Responsibilities: Sort 3-State Kelas Teks dan Kelas Tanggal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-094`): target `Jane Smith {runId}-094` dengan 3 Pending Approval; requester `Budi Santoso {runId}-094`, `Rina Putri {runId}-094`, dan `PT Maju Bersama {runId}-094`.
| ID (hasil seeding) | Transaction | Requester | Submission Date |
|---|---|---|---|
| `ID-HALC` (format `HALC-2026-NNNN`) | Device Allocation | `Budi Santoso {runId}-094` | 08 Jun 2026 |
| `ID-LALC` (format `LALC-2026-NNNN`) | License Allocation | `Rina Putri {runId}-094` | 02 Jun 2026 |
| `ID-WLT` (format `WLT-2026-NNNN`) | Wallet Top-Up | `PT Maju Bersama {runId}-094` | 05 Jun 2026 |
- Tabel sort TC-338 (parameter langkah 5 sampai 10):
| No | Kolom | Urutan baris klik 1 (A-Z, ikon ↑) | Urutan baris klik 2 (Z-A, ikon ↓) |
|---|---|---|---|
| 1 | ID | `ID-HALC`, `ID-LALC`, `ID-WLT` | `ID-WLT`, `ID-LALC`, `ID-HALC` |
| 2 | Transaction | `ID-HALC` (Device Allocation), `ID-LALC` (License Allocation), `ID-WLT` (Wallet Top-Up) | `ID-WLT`, `ID-LALC`, `ID-HALC` |
| 3 | Requester | `ID-HALC` (Budi Santoso), `ID-WLT` (PT Maju Bersama), `ID-LALC` (Rina Putri) | `ID-LALC`, `ID-WLT`, `ID-HALC` |
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### Persiapan: membuka Detail User

1. Klik icon Search
2. Ketik Search `Jane Smith {runId}-094`, tekan Enter
3. Klik Name `Jane Smith {runId}-094` untuk membuka Detail User

### TC-AC-SU-338: Sort 3-state Tab Responsibilities kelas teks

4. Klik tab `Responsibilities (3)`
5. Klik header kolom pada kolom "Kolom" tabel sort TC-338 (klik 1)
6. Verifikasi urutan baris pada kolom "Urutan baris klik 1" tabel sort TC-338
7. Klik header kolom yang sama (klik 2)
8. Verifikasi urutan baris pada kolom "Urutan baris klik 2" tabel sort TC-338
9. Klik header kolom yang sama (klik 3)
10. Verifikasi urutan kembali ke default Submission Date Oldest First (`ID-LALC`, `ID-WLT`, `ID-HALC`)

### TC-AC-SU-339: Sort 3-state Tab Responsibilities kelas tanggal

11. Klik header Submission Date (klik 1)
12. Verifikasi urutan baris `ID-LALC`, `ID-WLT`, `ID-HALC` (Oldest First, ikon ↑)
13. Klik header Submission Date (klik 2)
14. Verifikasi urutan baris `ID-HALC`, `ID-WLT`, `ID-LALC` (Newest First, ikon ↓)
15. Klik header Submission Date (klik 3)
16. Verifikasi urutan kembali ke default Submission Date Oldest First

## Notes

- Langkah 5 sampai 10 diulang untuk tiap baris tabel sort TC-338 (8b butir 7); parameter ada di Prerequisites.
- Langkah penghubung (S-03): Search lalu klik Name membuka Detail target (R-16).
- Alasan di atas ±35 langkah (ekspansi): kedua TC adalah Sort Tab Responsibilities dengan dataset sama; berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-094` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-338 menyebut sort A-Z kolom ID; spec mengasersi urutan relatif atas ID hasil seeding dengan prefix `HALC`, `LALC`, `WLT`.
