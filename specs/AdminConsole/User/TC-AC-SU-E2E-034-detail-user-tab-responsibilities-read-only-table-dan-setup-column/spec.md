---
id: TC-AC-SU-E2E-034-detail-user-tab-responsibilities-read-only-table-dan-setup-column
title: "Detail User Tab Responsibilities: tabel Pending Approvals, default sort, badge count, Setup Column, dan export CSV"
priority: Medium
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

# Detail User Tab Responsibilities: tabel Pending Approvals, default sort, badge count, Setup Column, dan export CSV

## Prerequisites

- Login sebagai Role: Principal Total Control
- Target pengguna memiliki ≥1 transaksi Pending Approval (ACAP) dan target lain dengan 0 approval

## Test Steps

### Screening Tab Responsibilities dan Struktur Tabel Read-Only

1. Buka halaman Detail User > Tab `Responsibilities` pada pengguna yang memiliki pending approval
2. Verifikasi label tab menampilkan badge counter format `"Responsibilities (N)"` (contoh: `"Responsibilities (3)"`)
3. Verifikasi tabel langsung memuat 4 kolom data: `Transaction ID`, `Transaction`, `Requester`, `Submission Date` tanpa sub-tab switcher
4. Verifikasi urutan default tabel adalah kolom `Submission Date` Oldest First (terlama di atas)
5. Verifikasi tabel bersifat murni display informasi tanpa tombol aksi `[Approve]`, `[Reject]`, row action, maupun navigasi klik baris

### Setup Column, Export CSV, dan Empty State

1. Buka Setup Column pada Tab Responsibilities, sembunyikan kolom satu per satu, verifikasi sistem mencegah uncheck pada 1 kolom terakhir yang tersisa
2. Klik tombol `[Download]` pada toolbar tab, verifikasi file terunduh dengan nama `Pending-Approvals-[User Name].csv`
3. Buka Tab Responsibilities pada pengguna dengan 0 pending approval
4. Verifikasi tabel menampilkan empty state dengan Title `"No pending approvals"` dan Description `"Pending approval requests will appear here."`

## Notes

- Tab Responsibilities merangkum tugas persetujuan pending dari modul Approvals (ACAP).
