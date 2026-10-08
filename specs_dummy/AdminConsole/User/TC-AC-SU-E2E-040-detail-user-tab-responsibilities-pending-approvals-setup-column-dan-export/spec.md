---
id: TC-AC-SU-E2E-040-detail-user-tab-responsibilities-pending-approvals-setup-column-dan-export
title: "Detail User Tab Responsibilities: Pending Approvals, Setup Column, dan Export CSV"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-116
  - TC-AC-SU-117
  - TC-AC-SU-119
  - TC-AC-SU-120
  - TC-AC-SU-121
  - TC-AC-SU-122
  - TC-AC-SU-123
  - TC-AC-SU-253
coverage:
  web: automated
---

# Detail User Tab Responsibilities: Pending Approvals, Setup Column, dan Export CSV

## Prerequisites

- Login sebagai Total Control
- Target user memiliki beberapa transaksi persetujuan aktif (Pending Approvals)

## Test Steps

### Screening Tab Responsibilities dan Counter Badge
1. Buka Detail User target > klik tab `Responsibilities`
2. Verifikasi badge count di samping label tab menampilkan angka yang sesuai dengan total pending tasks (misal `"5"`)
3. Verifikasi struktur tabel memuat 4 kolom data kanonikal: `Transaction ID`, `Transaction`, `Requester`, dan `Submission Date` (GAP-ACSU-E2E-004)

### Setup Column dan Penyesuaian Visibilitas
4. Klik tombol `[Setup Column]` pada toolbar tab
5. Verifikasi modal Setup Column menampilkan 4 opsi kolom data kanonikal
6. Nonaktifkan toggle visibilitas kolom `Requester` dan klik simpan
7. Verifikasi kolom `Requester` tersembunyi dari tabel data Responsibilities

### Ekspor Berkas CSV
8. Klik tombol `[Download]` pada toolbar
9. Verifikasi berkas CSV berhasil terunduh dengan konten baris tanggung jawab persetujuan yang sesuai tampilan tabel

## Notes

Mengintegrasikan klarifikasi struktur kolom 4-data kanonikal GAP-ACSU-E2E-004.
