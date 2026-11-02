---
id: TC-AC-SU-E2E-093-tab-responsibilities-screening-state-dan-display-only
title: "Tab Responsibilities: Screening, Sort Default, Display-Only, Search Kosong, Loading, dan Label 0 Pending Approvals"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-331
  - TC-AC-SU-337
  - TC-AC-SU-332
  - TC-AC-SU-336
  - TC-AC-SU-334
  - TC-AC-SU-333
coverage:
  web: automated
---

# Tab Responsibilities: Screening, Sort Default, Display-Only, Search Kosong, Loading, dan Label 0 Pending Approvals

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-093`): target `Jane Smith {runId}-093` dengan 3 Pending Approval; target `Mike Tan {runId}-093` tanpa Pending Approval; requester `Budi Santoso {runId}-093`, `Rina Putri {runId}-093`, dan `PT Maju Bersama {runId}-093`.
| ID (hasil seeding) | Transaction | Requester | Submission Date |
|---|---|---|---|
| `ID-HALC` (format `HALC-2026-NNNN`) | Device Allocation | `Budi Santoso {runId}-093` | 08 Jun 2026 |
| `ID-LALC` (format `LALC-2026-NNNN`) | License Allocation | `Rina Putri {runId}-093` | 02 Jun 2026 |
| `ID-WLT` (format `WLT-2026-NNNN`) | Wallet Top-Up | `PT Maju Bersama {runId}-093` | 05 Jun 2026 |
- Kemampuan teknis: Fixture BE untuk Pending Approval target (ID dibuat oleh seeding), `Spectra.intercept()` untuk menahan respons data tabel Tab Responsibilities (endpoint tidak disebut TC; disediakan tim FE).
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.

## Test Steps

### Persiapan: membuka Detail User

1. Klik icon Search
2. Ketik Search `Jane Smith {runId}-093`, tekan Enter
3. Klik Name `Jane Smith {runId}-093` untuk membuka Detail User

### TC-AC-SU-331: Screening Tab Responsibilities

4. Klik tab `Responsibilities (3)`
5. Verifikasi label tab `Responsibilities (3)`
6. Verifikasi tidak ada sub-tab switcher
7. Verifikasi toolbar `Search | Filter | Download` tanpa Changelog
8. Verifikasi kolom: `ID (sortable) | Transaction (sortable) | Requester (sortable) | Submission Date (sortable) | Column Visibility (⋯) (unsortable)`
9. Verifikasi tabel tanpa row action di body
10. Verifikasi Transaction tampil sebagai badge
11. Verifikasi Submission Date mengikuti format General Settings
12. Verifikasi footer pagination standar

### TC-AC-SU-337: Sort default Tab Responsibilities

13. Verifikasi urutan baris tanpa interaksi: `ID-LALC`, `ID-WLT`, `ID-HALC` (Submission Date Oldest First)

### TC-AC-SU-332: Tab Responsibilities display-only, tanpa row action dan klik baris

14. Klik salah satu baris pada kolom ID
15. Verifikasi klik baris tidak melakukan navigasi apa pun
16. Hover baris
17. Verifikasi tidak ada row action atau tombol Approve/Reject di baris
18. Verifikasi tidak ada tombol Approve/Reject di toolbar

### TC-AC-SU-336: Empty state hasil Search tanpa kecocokan

19. Klik icon Search
20. Ketik Search `zzqx-tidak-ada`, tekan Enter
21. Verifikasi empty state dengan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
22. Klik `(←)` pada kotak Search

### TC-AC-SU-334: Loading state Tab Responsibilities

23. Klik tab `Role`
24. Tahan respons data tabel Tab Responsibilities selama 3000 ms (`Spectra.intercept()`)
25. Klik tab `Responsibilities (3)`
26. Verifikasi tabel menampilkan 5 skeleton rows sesuai layout kolom
27. Lepas tahanan respons
28. Verifikasi baris data (`ID-LALC`, `ID-WLT`, `ID-HALC`) menggantikan skeleton

### TC-AC-SU-333: Label tab Responsibilities saat 0 Pending Approvals

29. Klik segmen `User` di breadcrumb
30. Klik icon Search
31. Ketik Search `Mike Tan {runId}-093`, tekan Enter
32. Klik Name `Mike Tan {runId}-093` untuk membuka Detail User
33. Klik tab `Responsibilities (0)`
34. Verifikasi label tab `Responsibilities (0)`
35. Verifikasi tabel menampilkan ilustrasi, judul `No pending approvals`, dan deskripsi `Pending approval requests will appear here.`

## Notes

- Langkah penghubung (S-03): mencari lalu membuka Detail target lewat Search dan klik Name (R-16); klik tab `Role` sebelum menahan respons memastikan tab Responsibilities dimuat ulang saat diklik; `(←)` menutup Search.
- Urutan spec: TC-337 (sort default) segera sesudah screening sebelum interaksi sort; TC-333 memakai target lain (`Mike Tan {runId}-093`) karena state 0 Pending Approvals bertentangan dengan 3 Pending Approval `Jane Smith {runId}-093`.
- TC-335 (error load) ada di spec lain; menahan respons pada TC-334 hanya mengamati Loading dan bukan kelas fault injection.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-093` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-333 menyebut target Jane Smith tanpa Pending Approval, padahal TC lain di bagian yang sama memberi Jane Smith 3 Pending Approval; spec memakai user terpisah bernama `Mike Tan {runId}-093`.
  - TC-331 sampai TC-365 menyebut ID Approval literal (`HALC-2026-0012`, `LALC-2026-0044`, `WLT-2026-0301`); spec memakai ID hasil seeding bernama `ID-HALC`, `ID-LALC`, `ID-WLT` karena ID bersifat unik sistem.
